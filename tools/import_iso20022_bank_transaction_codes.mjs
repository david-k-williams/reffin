#!/usr/bin/env node
/** Normalize ISO 20022 Bank Transaction Code combinations from the official XLSX. */

import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";
import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const SOURCE_SHA256 = "f73d6d72a5becb9f042f98b939f7c8301d434610e48afc60f1b1ef01cbb7ac6e";
const SOURCE_URL = "https://www.iso20022.org/sites/default/files/media/file/BTC_Codification_30Nov2025.xlsx";
const HEADERS = [
  "domain_code", "domain_name", "family_code", "family_name",
  "subfamily_code", "subfamily_name", "status", "status_date",
];
const EXPECTED_SOURCE_HEADERS = [
  "Domain", "Family", "SubFamily",
  "Domain Code\nExternalBankTransactionDomain1Code",
  "Family Code\nExternalBankTransactionFamily1Code",
  "SubFamily Code\nExternalBankTransactionSubFamily1Code",
  "Status", "Status Date",
];
const EXPECTED_STATUS_COUNTS = { corrected: 35, new: 1528, updated: 4 };

function usage() {
  throw new Error("usage: import_iso20022_bank_transaction_codes.mjs INPUT.xlsx [OUTPUT.csv]");
}

function clean(value) {
  return String(value ?? "").replace(/\u00a0/g, " ").replace(/\s+/g, " ").trim();
}

function quoteCsv(value) {
  const text = String(value ?? "");
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

function excelSerialToIsoDate(serial) {
  const milliseconds = Math.round((serial - 25569) * 86400000);
  return new Date(milliseconds).toISOString().slice(0, 10);
}

function normalizeDate(value) {
  if (typeof value === "number") return excelSerialToIsoDate(value);
  const match = clean(value).match(/^(\d{1,2})\/(\d{1,2})\/(\d{4})$/);
  if (!match) throw new Error(`invalid status date: ${JSON.stringify(value)}`);
  return `${match[3]}-${match[2].padStart(2, "0")}-${match[1].padStart(2, "0")}`;
}

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const [inputArg, outputArg] = process.argv.slice(2);
if (!inputArg) usage();
const input = path.resolve(inputArg);
const output = path.resolve(outputArg ?? path.join(root, "data/iso20022/bank_transaction_codes.csv"));
const bytes = await fs.readFile(input);
const actualHash = createHash("sha256").update(bytes).digest("hex");
if (actualHash !== SOURCE_SHA256) {
  throw new Error(`source hash mismatch for ${SOURCE_URL}: expected ${SOURCE_SHA256}, got ${actualHash}`);
}

const workbook = await SpreadsheetFile.importXlsx(await FileBlob.load(input));
const sheet = workbook.worksheets.getItem("BTC_Codification");
const values = sheet.getRange("A1:H1570").values;
if (JSON.stringify(values[2]) !== JSON.stringify(EXPECTED_SOURCE_HEADERS)) {
  throw new Error(`unexpected workbook headers: ${JSON.stringify(values[2])}`);
}
const sourceRows = values.slice(3);
if (sourceRows.length !== 1567 || sourceRows.some((row) => row.length !== 8)) {
  throw new Error(`expected 1,567 eight-column rows, found ${sourceRows.length}`);
}

const rows = sourceRows.map((row, index) => {
  const [domainName, familyName, subfamilyName, domainCode, familyCode, subfamilyCode, status, statusDate] = row;
  const normalized = {
    domain_code: clean(domainCode),
    domain_name: clean(domainName),
    family_code: clean(familyCode),
    family_name: clean(familyName),
    subfamily_code: clean(subfamilyCode),
    subfamily_name: clean(subfamilyName),
    status: clean(status).toLowerCase(),
    status_date: normalizeDate(statusDate),
  };
  for (const [field, value] of Object.entries(normalized)) {
    if (!value) throw new Error(`row ${index + 4}: empty ${field}`);
  }
  for (const field of ["domain_code", "family_code", "subfamily_code"]) {
    if (!/^[A-Z0-9]{4}$/.test(normalized[field])) {
      throw new Error(`row ${index + 4}: invalid ${field} ${normalized[field]}`);
    }
  }
  return normalized;
});

const statusCounts = Object.fromEntries(
  [...new Set(rows.map((row) => row.status))].sort().map((status) => [status, rows.filter((row) => row.status === status).length]),
);
if (JSON.stringify(statusCounts) !== JSON.stringify(EXPECTED_STATUS_COUNTS)) {
  throw new Error(`unexpected status counts: ${JSON.stringify(statusCounts)}`);
}
const keyCounts = new Map();
for (const row of rows) {
  const key = `${row.domain_code}/${row.family_code}/${row.subfamily_code}`;
  keyCounts.set(key, (keyCounts.get(key) ?? 0) + 1);
}
const duplicateKeys = [...keyCounts].filter(([, count]) => count > 1).map(([key]) => key).sort();
if (JSON.stringify(duplicateKeys) !== JSON.stringify(["SECU/CASH/CPEN", "SECU/CORP/INTR", "SECU/CUST/INTR"])) {
  throw new Error(`unexpected duplicate composite keys: ${JSON.stringify(duplicateKeys)}`);
}

const csv = [HEADERS.join(","), ...rows.map((row) => HEADERS.map((header) => quoteCsv(row[header])).join(",")), ""].join("\n");
await fs.mkdir(path.dirname(output), { recursive: true });
await fs.writeFile(output, csv, "utf8");
console.log(`wrote ${rows.length} rows (${keyCounts.size} composite keys) to ${output}`);

