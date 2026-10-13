---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/validate-cbn-parser/
title: ValidateCbnParser parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:13.851014+00:00
---

# ValidateCbnParser parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/validate-cbn-parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ValidateCbnParser parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Tools API (**`ValidateCbnParser`**) to the modern Chronicle API (**`CreateParser` coupled with ValidationReport**).

## Protocol and mapping overview

Feature | Legacy API (`ValidateCbnParser`) | Modern Chronicle API (`CreateParser`)  
---|---|---  
**HTTP Method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/parsers.create`  
  
* * *

## Request payload field-by-field parity

In the Chronicle API, validation is not a stateless standalone method; it is integrated directly into the stateful parser creation workflow.

Legacy Field (`ValidateCbnParserRequest`) | Modern Field (`CreateParserRequest` / `Parser`) | Field type | Parity & Migration Notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / Architectural Shift:** Legacy validation was stateless and did not bind to a parent resource in the URL. Modern parser creation and validation is scoped under target log types: `projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}`.  
`config` | `parser.cbn` | `bytes` | **Direct Map:** The raw configuration byte sequence to be validated and created. Maps to `cbn` inside the config oneof on `Parser`.  
`logs` | — _(in validation test suites)_ | `bytes` | **Architectural Shift:** Legacy validation required passing raw sample log bytes inline with the validation request. In modern Chronicle API workflows, sample logs and test cases are managed as persistent validation test suites or sample logs associated with the log type/parser, against which the backend automatically executes validation.  
  
* * *

## Response payload field-by-field parity

In legacy backstory, validation results were returned synchronously in `ValidateCbnParserResponse`. In modern Chronicle API workflows, `CreateParser` returns the `Parser` resource (reflecting initial `validation_stage`), while detailed compilation and execution errors are written to an asynchronous `ValidationReport` resource (referenced in `CreateParserMetadata.validation_report` and retrieved using `GetValidationReport`).

Legacy Field (`ValidateCbnParserResponse` message) | Modern Field (`CreateParserMetadata` / `ValidationReport` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`result` | `CreateParserMetadata.stage` / `Parser.validation_stage` | `enum` | **Restructured:** The legacy string status array is replaced by structured enum lifecycle states (`NEW`, `VALIDATING`, `PASSED`, `FAILED`, `INTERNAL_ERROR`, `VALIDATION_SKIPPED`).  
`errors` | `ValidationReport.errors` | `repeated Message` | **Parity Mapped / Restructured:** The list of validation failures (`ValidateCbnParserError`) is mapped to structured error records inside the generated `ValidationReport` resource.  
  
### Nested Validation error property mappings

The fields mapping inside individual validation error items is as follows:

Legacy Field (`ValidateCbnParserError` message) | Modern Field (`ValidationReport` error items) | Field type | Parity & Migration Notes  
---|---|---|---  
`index` | `index` | `int32` | **Parity Mapped:** Sequential index identifier of the encountered error.  
`log_entry` | `log_entry` / `sample_log` | `string` | **Parity Mapped:** The raw log line or sample entry that triggered the parsing exception during test execution.  
`error_msg` | `error_message` / `details` | `string` | **Parity Mapped:** Detailed diagnostic text explaining why normalization or compilation failed.  
  
* * *

## Key differences

  * **Workflow Integration and Stateful Validation:**
    * In legacy backstory, `ValidateCbnParser` was a stateless, standalone RPC where clients manually pushed ephemeral config bytes and sample logs before creating a parser.
    * In the modern Chronicle API, standalone validation RPCs are retired. Validation is built directly into the stateful `CreateParser` lifecycle: submitting a parser automatically triggers backend validation pipelines against associated test cases and logs.
  * **Asynchronous Validation Reporting:**
    * Rather than blocking synchronously to return all parsing traces, the modern API tracks validation status using operation metadata (`CreateParserMetadata.stage`) and outputs comprehensive diagnostic logs to a dedicated `ValidationReport` resource (`chronicle.googleapis.com/ValidationReport`).
  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance log type bindings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
