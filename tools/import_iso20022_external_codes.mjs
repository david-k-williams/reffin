#!/usr/bin/env node
/** Normalize a pinned ISO 20022 External Code Sets workbook for Reffin.
 *
 * This importer intentionally accepts local source artifacts. Downloading and
 * terms review remain explicit steps, while the pinned hashes make regeneration
 * deterministic. Run it with the bundled @oai/artifact-tool runtime.
 */

import crypto from "node:crypto";
import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";
import { fileURLToPath } from "node:url";

import { FileBlob, SpreadsheetFile } from "@oai/artifact-tool";

const EXPECTED_XLSX_SHA256 =
  "b07da9c46cad77b10e11a50ad91b3254caa2265eaed0e1b2aafdddecdcc222c6";
const EXPECTED_JSON_SHA256 =
  "c1d92bb021f0f7d1d3607b802b74969f4b8bed62527d0a461e2b65c8aec39fc0";
const SOURCE = "iso20022_external_code_sets_1q2026_v1";
const CODE_SET_FIELDS = ["code_set", "definition", "status", "source"];
const EXTERNAL_CODE_FIELDS = [
  "code_set",
  "code",
  "name",
  "label",
  "definition",
  "requester",
  "status",
  "last_updated",
  "creation_date",
  "replaced_by",
  "mapping_standard_1",
  "mapping_value_1",
  "mapping_standard_2",
  "mapping_value_2",
  "additional_information",
  "source",
];

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const repositoryRoot = path.resolve(scriptDirectory, "..");

function usage() {
  return [
    "Usage:",
    "  node tools/import_iso20022_external_codes.mjs \\",
    "    --xlsx /path/to/1Q2026_externalcodesets_v1.xlsx \\",
    "    --json /path/to/1Q2026_externalcodesets_v1.json \\",
    "    [--output-dir data/iso20022]",
  ].join("\n");
}

function parseArguments(argv) {
  const parsed = {
    xlsx: null,
    json: null,
    outputDir: path.join(repositoryRoot, "data", "iso20022"),
  };
  for (let index = 0; index < argv.length; index += 1) {
    const argument = argv[index];
    if (argument === "--help" || argument === "-h") {
      process.stdout.write(`${usage()}\n`);
      process.exit(0);
    }
    const value = argv[index + 1];
    if (!value || value.startsWith("--")) {
      throw new Error(`missing value for ${argument}`);
    }
    if (argument === "--xlsx") parsed.xlsx = path.resolve(value);
    else if (argument === "--json") parsed.json = path.resolve(value);
    else if (argument === "--output-dir") parsed.outputDir = path.resolve(value);
    else throw new Error(`unknown argument: ${argument}`);
    index += 1;
  }
  if (!parsed.xlsx || !parsed.json) throw new Error("--xlsx and --json are required");
  return parsed;
}

function sha256(bytes) {
  return crypto.createHash("sha256").update(bytes).digest("hex");
}

function assertEqual(actual, expected, label) {
  if (actual !== expected) {
    throw new Error(`${label}: expected ${expected}, got ${actual}`);
  }
}

function cleanText(value) {
  if (value === null || value === undefined) return "";
  return String(value)
    .replace(/_x000D_/gi, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function normalizeStatus(value, context, allowed = new Set(["registered", "obsolete"])) {
  const status = cleanText(value).toLowerCase();
  const normalized = status.replace(/\s+/g, "_");
  if (!allowed.has(normalized)) {
    throw new Error(`${context}: unsupported status ${JSON.stringify(value)}`);
  }
  return normalized;
}

function normalizeDate(value, context) {
  const normalized = cleanText(value);
  if (!normalized) return "";
  if (!/^\d{4}-\d{2}-\d{2}$/.test(normalized)) {
    throw new Error(`${context}: invalid ISO date ${JSON.stringify(value)}`);
  }
  const parsed = new Date(`${normalized}T00:00:00Z`);
  if (Number.isNaN(parsed.getTime()) || parsed.toISOString().slice(0, 10) !== normalized) {
    throw new Error(`${context}: invalid calendar date ${JSON.stringify(value)}`);
  }
  return normalized;
}

function uiLabel(name) {
  return name
    .replace(/([a-z\d])([A-Z])/g, "$1 $2")
    .replace(/([A-Z]+)([A-Z][a-z])/g, "$1 $2")
    .replace(/([A-Za-z])(\d+)/g, "$1 $2")
    .replace(/(\d+)([A-Za-z])/g, "$1 $2")
    .replace(/\s+/g, " ")
    .trim();
}

function csvCell(value) {
  const text = String(value ?? "");
  return /[",\r\n]/.test(text) ? `"${text.replaceAll('"', '""')}"` : text;
}

function encodeCsv(fields, rows) {
  return `${[fields, ...rows.map((row) => fields.map((field) => row[field]))]
    .map((row) => row.map(csvCell).join(","))
    .join("\n")}\n`;
}

function compareValues(left, right) {
  return left.localeCompare(right, "en", { numeric: true });
}

function difference(left, right) {
  return [...left].filter((value) => !right.has(value)).sort(compareValues);
}

function validateJson(jsonSchema, descriptors, codes) {
  const definitions = jsonSchema.definitions;
  if (!definitions || typeof definitions !== "object" || Array.isArray(definitions)) {
    throw new Error("JSON artifact has no definitions object");
  }
  assertEqual(Object.keys(definitions).length, 158, "JSON definition count");
  const descriptorNames = new Set(descriptors.map((row) => row.code_set));
  const definitionNames = new Set(Object.keys(definitions));
  const missingDefinitions = difference(descriptorNames, definitionNames);
  const extraDefinitions = difference(definitionNames, descriptorNames);
  if (missingDefinitions.length || extraDefinitions.length) {
    throw new Error(
      `workbook/JSON code-set mismatch; missing=${missingDefinitions.join("|")}; ` +
        `extra=${extraDefinitions.join("|")}`,
    );
  }

  const registeredBySet = new Map(descriptors.map((row) => [row.code_set, new Set()]));
  for (const row of codes) {
    if (row.status !== "registered") continue;
    const registered = registeredBySet.get(row.code_set);
    if (registered.has(row.code)) {
      throw new Error(`${row.code_set}/${row.code}: duplicate registered value`);
    }
    registered.add(row.code);
  }

  let enumerableSets = 0;
  for (const descriptor of descriptors) {
    const definition = definitions[descriptor.code_set];
    const jsonValues = Array.isArray(definition.enum) ? definition.enum : [];
    const jsonSet = new Set(jsonValues);
    if (jsonSet.size !== jsonValues.length) {
      throw new Error(`${descriptor.code_set}: duplicate value in JSON enum`);
    }
    if (jsonValues.length) enumerableSets += 1;
    const workbookSet = registeredBySet.get(descriptor.code_set);
    const missingValues = difference(workbookSet, jsonSet);
    const extraValues = difference(jsonSet, workbookSet);
    if (missingValues.length || extraValues.length) {
      throw new Error(
        `${descriptor.code_set}: registered workbook values disagree with JSON; ` +
          `missing=${missingValues.join("|")}; extra=${extraValues.join("|")}`,
      );
    }
  }
  assertEqual(enumerableSets, 134, "currently enumerable JSON set count");
}

async function main() {
  const options = parseArguments(process.argv.slice(2));
  const [xlsxBytes, jsonBytes] = await Promise.all([
    fs.readFile(options.xlsx),
    fs.readFile(options.json),
  ]);
  assertEqual(sha256(xlsxBytes), EXPECTED_XLSX_SHA256, "XLSX SHA-256");
  assertEqual(sha256(jsonBytes), EXPECTED_JSON_SHA256, "JSON SHA-256");

  const input = await FileBlob.load(options.xlsx);
  const workbook = await SpreadsheetFile.importXlsx(input);
  const descriptorValues = workbook.worksheets
    .getItem("CodeSetsDefinition")
    .getRange("A2:C159").values;
  const codeValues = workbook.worksheets
    .getItem("AllCodeSets")
    .getRange("A2:N3247").values;

  const descriptors = descriptorValues.map((row, index) => {
    const codeSet = cleanText(row[0]);
    const definition = cleanText(row[1]);
    if (!codeSet || !definition) {
      throw new Error(`descriptor row ${index + 2}: missing code set or definition`);
    }
    return {
      code_set: codeSet,
      definition,
      status: normalizeStatus(
        row[2],
        `descriptor row ${index + 2}`,
        new Set(["registered", "obsolete", "provisionally_registered"]),
      ),
      source: SOURCE,
    };
  });

  const codes = codeValues.map((row, index) => {
    const rowNumber = index + 2;
    const codeSet = cleanText(row[0]);
    const code = cleanText(row[1]);
    const name = cleanText(row[2]);
    const definition = cleanText(row[3]);
    if (!codeSet || !code || !name || !definition) {
      throw new Error(`code row ${rowNumber}: missing required workbook value`);
    }
    return {
      code_set: codeSet,
      code,
      name,
      label: uiLabel(name),
      definition,
      requester: cleanText(row[4]),
      status: normalizeStatus(row[5], `code row ${rowNumber}`),
      last_updated: normalizeDate(row[6], `code row ${rowNumber} Last Update`),
      creation_date: normalizeDate(row[7], `code row ${rowNumber} Creation Date`),
      replaced_by: cleanText(row[8]),
      mapping_standard_1: cleanText(row[9]),
      mapping_value_1: cleanText(row[10]),
      mapping_standard_2: cleanText(row[11]),
      mapping_value_2: cleanText(row[12]),
      additional_information: cleanText(row[13]),
      source: SOURCE,
    };
  });

  assertEqual(descriptors.length, 158, "descriptor count");
  assertEqual(new Set(descriptors.map((row) => row.code_set)).size, 158, "distinct descriptor count");
  const descriptorStatusCounts = descriptors.reduce((counts, row) => {
    counts[row.status] = (counts[row.status] ?? 0) + 1;
    return counts;
  }, {});
  if (
    descriptorStatusCounts.registered !== 156 ||
    descriptorStatusCounts.provisionally_registered !== 1 ||
    descriptorStatusCounts.obsolete !== 1 ||
    Object.keys(descriptorStatusCounts).length !== 3
  ) {
    throw new Error(
      `unexpected code-set descriptor status counts: ${JSON.stringify(descriptorStatusCounts)}`,
    );
  }
  assertEqual(codes.length, 3246, "physical external-code row count");
  assertEqual(codes.filter((row) => row.status === "registered").length, 3213, "registered row count");
  assertEqual(codes.filter((row) => row.status === "obsolete").length, 33, "obsolete row count");
  const identities = codes.map((row) => `${row.code_set}\u0000${row.code}`);
  assertEqual(new Set(identities).size, 3245, "distinct code-set/code count");
  const duplicates = identities.filter((identity, index) => identities.indexOf(identity) !== index);
  if (duplicates.length !== 1 || duplicates[0] !== "ExternalLocalInstrument1Code\u0000CTP") {
    throw new Error(`unexpected lifecycle collision(s): ${duplicates.join("|")}`);
  }
  const ctpRows = codes.filter(
    (row) => row.code_set === "ExternalLocalInstrument1Code" && row.code === "CTP",
  );
  if (
    ctpRows.length !== 2 ||
    ctpRows[0].status !== "obsolete" ||
    ctpRows[0].name !== "CustomerTransferPlus" ||
    ctpRows[1].status !== "registered" ||
    ctpRows[1].name !== "CreditTransferPreferred"
  ) {
    throw new Error("ExternalLocalInstrument1Code/CTP lifecycle records changed");
  }

  const descriptorNames = new Set(descriptors.map((row) => row.code_set));
  for (const row of codes) {
    if (!descriptorNames.has(row.code_set)) {
      throw new Error(`${row.code_set}/${row.code}: missing code-set descriptor`);
    }
  }
  validateJson(JSON.parse(jsonBytes.toString("utf8")), descriptors, codes);

  descriptors.sort((left, right) => compareValues(left.code_set, right.code_set));
  codes.sort(
    (left, right) =>
      compareValues(left.code_set, right.code_set) ||
      compareValues(left.code, right.code) ||
      compareValues(left.creation_date, right.creation_date) ||
      compareValues(left.status, right.status),
  );
  await fs.mkdir(options.outputDir, { recursive: true });
  const codeSetsCsv = encodeCsv(CODE_SET_FIELDS, descriptors);
  const externalCodesCsv = encodeCsv(EXTERNAL_CODE_FIELDS, codes);
  const codeSetsPath = path.join(options.outputDir, "code_sets.csv");
  const externalCodesPath = path.join(options.outputDir, "external_codes.csv");
  await Promise.all([
    fs.writeFile(codeSetsPath, codeSetsCsv, "utf8"),
    fs.writeFile(externalCodesPath, externalCodesCsv, "utf8"),
  ]);
  process.stdout.write(
    [
      `wrote ${descriptors.length} code-set descriptors to ${codeSetsPath}`,
      `wrote ${codes.length} external-code records to ${externalCodesPath}`,
      `code_sets.csv sha256 ${sha256(Buffer.from(codeSetsCsv, "utf8"))}`,
      `external_codes.csv sha256 ${sha256(Buffer.from(externalCodesCsv, "utf8"))}`,
    ].join("\n") + "\n",
  );
}

main().catch((error) => {
  process.stderr.write(`${error.stack ?? error}\n`);
  process.exitCode = 1;
});
