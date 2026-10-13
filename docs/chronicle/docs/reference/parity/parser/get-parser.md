---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/get-parser/
title: GetParser parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:28.766686+00:00
---

# GetParser parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/get-parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetParser parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Tools API (**`GetCbnParser`**) to the modern Chronicle API (**`GetParser`**).

## Protocol and mapping overview

Feature | Legacy API (`GetCbnParser`) | Modern Chronicle API (`GetParser`)  
---|---|---  
**HTTP Method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/parsers.get`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `GetParserRequest` identifies target resources using canonical Google Cloud resource name paths rather than standalone config IDs.

Legacy Field (`GetCbnParserRequest`) | Modern Field (`GetParserRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`config_id` | `name` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / Renaming:** The legacy request passed `config_id` globally in the URL path. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{region}/instances/{instance}/logTypes/{log_type}/parsers/{parser_id}`.  
  
* * *

## Response payload field-by-field parity

Both responses return the retrieved parser resource, with the modern API utilizing standardized lifecycle stages and canonical names.

Legacy Field (`CbnParser` message) | Modern Field (`Parser` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`config_id` | `name` | `string` | **Parity Mapped:** Mapped into the standard canonical resource path under name: `projects/{pr}/locations/{loc}/instances/{in}/logTypes/{lt}/parsers/{id}`.  
`log_type` | — _(implicit in resource path)_ | `string` | Managed under the parent segment of the canonical name.  
`config` | `cbn` | `bytes` | Raw CBN parser bytes.  
`state` | `release_stage` / `validation_stage` | `enum` | **Restructured:** The legacy monolithic `CbnConfigState` enum is split into granular lifecycle attributes: `release_stage` (for example, `RELEASE`, `ROLLBACK`, `ARCHIVED`) and `validation_stage` (for example, `PASSED`, `FAILED`).  
`submit_time` / `timestamps` | `create_time` | `Timestamp` | Standardized creation timestamp (`createTime` in JSON).  
`sha256` | — | `string` | **Retired:** Hash verification is managed internally by Chronicle API storage engines.  
`validation_errors` | — _(in validation_stage)_ | `Message` | If validation fails, errors are captured under standard operation metadata or error details.  
`change_log` | `changelogs` | `Message` | Structured changelog representation.  
`author` | `creator.author` | `string` | Mapped inside creator object.  
  
* * *

## Key differences

  * **Service Consolidation and Renaming:**
    * Legacy parser retrieval was housed under `ToolsService` with names like `GetCbnParser`.
    * Modern Chronicle API consolidates parser management under `ParserService` (`GetParser`), utilizing standard Google Cloud parent paths.
  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance log type bindings.
  * **Structured Lifecycle and Creator Attributes:**
    * Author strings and commit messages are expanded into structured `Creator` and `Changelogs` objects.
    * Monolithic config states are split into distinct release stages and validation stages.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
