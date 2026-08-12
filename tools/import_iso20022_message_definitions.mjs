#!/usr/bin/env node
/** Normalize the current ISO 20022 Message Definitions from the official e-Repository. */

import { createHash } from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SOURCE_ZIP_SHA256 = "9a9d060dd94b6858a4ef4836ca36a9a67308e96b69d7d184ff97f28295b96039";
const SOURCE_XML_SHA256 = "926ffb9db92092b1ffe8c8253378691950d715e2639dffcfc525483049eee359";
const SOURCE_URL = "https://www.iso20022.org/sites/default/files/media/file/eRepository_ISO20022_20260626.zip";
const HEADERS = ["business_area", "message_id", "message_number", "variant", "version", "name"];

function usage() {
  throw new Error("usage: import_iso20022_message_definitions.mjs INPUT.iso20022 [OUTPUT.csv]");
}

function quoteCsv(value) {
  const text = String(value ?? "");
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

function attributes(source) {
  const result = {};
  for (const match of source.matchAll(/([\w:]+)="([^"]*)"/g)) {
    result[match[1]] = match[2]
      .replaceAll("&quot;", '"')
      .replaceAll("&apos;", "'")
      .replaceAll("&lt;", "<")
      .replaceAll("&gt;", ">")
      .replaceAll("&amp;", "&");
  }
  return result;
}

const root = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const [inputArg, outputArg] = process.argv.slice(2);
if (!inputArg) usage();
const input = path.resolve(inputArg);
const output = path.resolve(outputArg ?? path.join(root, "data/iso20022/message_definitions.csv"));
const bytes = await fs.readFile(input);
const actualHash = createHash("sha256").update(bytes).digest("hex");
if (actualHash !== SOURCE_XML_SHA256) {
  throw new Error(
    `source XML hash mismatch for ${SOURCE_URL} `
    + `(ZIP ${SOURCE_ZIP_SHA256}): expected ${SOURCE_XML_SHA256}, got ${actualHash}`,
  );
}
const xml = bytes.toString("utf8").replace(/^\uFEFF/, "");
if (!xml.startsWith("<?xml") || !xml.includes("<iso20022:Repository")) {
  throw new Error(`input is not the extracted ${SOURCE_URL} e-Repository XML`);
}

const catalogueMatch = xml.match(/<businessProcessCatalogue\b[^>]*>([\s\S]*?)<\/businessProcessCatalogue>/);
if (!catalogueMatch) throw new Error("businessProcessCatalogue not found");
const catalogue = catalogueMatch[1];

const currentMessageIds = new Set();
for (const match of catalogue.matchAll(/<topLevelCatalogueEntry\s+([^>]*xsi:type="iso20022:MessageSet"[^>]*)\/?\s*>/g)) {
  const entry = attributes(match[1]);
  const name = entry.name ?? "";
  const isCurrent = /(?:Latest version|Latest Version|ISO Latest)$/.test(name)
    || name === "BMR Administrator And Benchmark Reporting";
  if (/Supplementary Data/.test(name)) continue;
  if (!isCurrent) continue;
  for (const id of (entry.messageDefinition ?? "").split(/\s+/).filter(Boolean)) {
    currentMessageIds.add(id);
  }
}

const rows = [];
for (const areaMatch of catalogue.matchAll(
  /<topLevelCatalogueEntry\s+[^>]*xsi:type="iso20022:BusinessArea"[^>]*>([\s\S]*?)<\/topLevelCatalogueEntry>/g,
)) {
  for (const definitionMatch of areaMatch[1].matchAll(/<messageDefinition\s+([^>]*)>([\s\S]*?)<\/messageDefinition>/g)) {
    const definition = attributes(definitionMatch[1]);
    if (!currentMessageIds.has(definition["xmi:id"])) continue;
    const identifierMatch = definitionMatch[2].match(/<messageDefinitionIdentifier\s+([^>]*)\/>/);
    if (!identifierMatch) throw new Error(`messageDefinitionIdentifier missing for ${definition.name}`);
    const identifier = attributes(identifierMatch[1]);
    const businessArea = identifier.businessArea;
    const messageNumber = identifier.messageFunctionality;
    const variant = identifier.flavour;
    const version = identifier.version;
    const name = definition.name;
    const messageId = `${businessArea}.${messageNumber}.${variant}.${version}`;
    if (!/^[a-z]{4}\.\d{3}\.\d{3}\.\d{2}$/.test(messageId)) {
      throw new Error(`invalid message identifier: ${messageId}`);
    }
    rows.push({
      business_area: businessArea,
      message_id: messageId,
      message_number: messageNumber,
      variant,
      version,
      name,
    });
  }
}

rows.sort((left, right) => left.message_id.localeCompare(right.message_id));
if (rows.length !== 797) throw new Error(`expected 797 current message definitions, found ${rows.length}`);
if (new Set(rows.map((row) => row.message_id)).size !== rows.length) {
  throw new Error("current message identifiers are not unique");
}
const spotChecks = new Map(rows.map((row) => [row.message_id, row.name]));
for (const [identifier, name] of [
  ["acmt.001.001.08", "AccountOpeningInstructionV08"],
  ["camt.053.001.14", "BankToCustomerStatementV14"],
  ["pacs.008.001.14", "FIToFICustomerCreditTransferV14"],
  ["seev.001.001.13", "MeetingNotificationV13"],
]) {
  if (spotChecks.get(identifier) !== name) {
    throw new Error(`catalogue spot check failed: ${identifier} => ${spotChecks.get(identifier)}`);
  }
}

const csv = [HEADERS.join(","), ...rows.map((row) => HEADERS.map((header) => quoteCsv(row[header])).join(",")), ""].join("\n");
await fs.mkdir(path.dirname(output), { recursive: true });
await fs.writeFile(output, csv, "utf8");
const normalizedHash = createHash("sha256").update(csv).digest("hex");
console.log(`wrote ${rows.length} rows to ${output} (${normalizedHash})`);
