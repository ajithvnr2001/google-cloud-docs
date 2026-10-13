---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/deactivate-parser/
title: DeactivateParser parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:11.630978+00:00
---

# DeactivateParser parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/deactivate-parser/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# DeactivateParser parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Tools API (**`ArchiveCbnParser`**) to the modern Chronicle API (**`DeactivateParser`**).

## Protocol and mapping overview

Feature | Legacy API (`ArchiveCbnParser`) | Modern Chronicle API (`DeactivateParser`)  
---|---|---  
**HTTP Method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/parsers.deactivate`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `DeactivateParserRequest` identifies target parsers using Google Cloud resource name paths rather than standalone config IDs.

Legacy Field (`ArchiveCbnParserRequest`) | Modern Field (`DeactivateParserRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`config_id` | `name` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / Renaming:** The legacy request passed `config_id` globally in the URL path. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{region}/instances/{instance}/logTypes/{log_type}/parsers/{parser_id}`.  
  
* * *

## Response payload field-by-field parity

In legacy backstory, `ArchiveCbnParser` returned the archived parser config object (`CbnParser`). The modern `DeactivateParser` API simplifies this by returning an empty confirmation response (`google.protobuf.Empty`).

Legacy Field (`CbnParser` response) | Modern Field (`google.protobuf.Empty`) | Field type | Parity & Migration Notes  
---|---|---|---  
`config_id` / `state` / `sha256` or others | `google.protobuf.Empty` | `Empty` | **Architectural Simplification:** The legacy returned the modified `CbnParser` object (where state became `ARCHIVED`). The modern Chronicle API returns `google.protobuf.Empty` on successful deactivation. To verify updated parser states, invoke `GetParser` or `ListParsers`.  
  
* * *

## Key differences

  * **Service Consolidation and Renaming:**
    * Legacy parser operations were housed under `ToolsService` with names like `ArchiveCbnParser`.
    * Modern Chronicle API consolidates parser management under `ParserService`, using terminology aligned with parser lifecycles (`DeactivateParser`, `ActivateParser`).
  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Response Simplification:**
    * Successful deactivations return empty payloads rather than echoing back the entire parser schema and byte contents.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
