---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/list-parsers/
title: ListParsers parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:59.218370+00:00
---

# ListParsers parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/list-parsers/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListParsers parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Tools API (**`ListCbnParserHistory`**) to the modern Chronicle API (**`ListParsers`**).

## Protocol and mapping overview

Feature | Legacy API (`ListCbnParserHistory`) | Modern Chronicle API (`ListParsers`)  
---|---|---  
**HTTP Method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/parsers.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListParsersRequest` scopes listings under target parent paths and adds options for filtering and basic views.

Legacy Field (`ListCbnParserHistoryRequest`) | Modern Field (`ListParsersRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`log_type` | `parent` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / Architectural Shift:** The legacy request specified the target `log_type` as a string parameter. The modern API scopes parser listings under a parent resource path: `projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}` (use `-` in place of `{log_type}` to list parsers across all log types).  
`page_size` | `page_size` | `int32` | **Parity Mapped:** Pagination page size limit. Rename to `pageSize` in JSON.  
`page_token` | `page_token` | `string` | **Parity Mapped:** Paging resumption token. Rename to `pageToken` in JSON.  
— | `filter` | `string` | **New Parameter:** Standard AIP-160 filter expression strings to filter returned parsers (for example, filtering by release stage or author).  
— | `view` | `enum` | **New Parameter:** Selects the parser view (`ParserView` enum: `BASIC_VIEW`, `FULL_VIEW`). Default is `FULL_VIEW`. `BASIC_VIEW` omits large binary configs and changelogs.  
  
* * *

## Response payload field-by-field parity

Both APIs return lists of parser configurations and pagination continuation tokens.

Legacy Field (`ListCbnParserHistoryResponse` / `CbnParserHistory`) | Modern Field (`ListParsersResponse` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`cbn_parsers` | `parsers` | `repeated Parser` | **Parity Mapped / Restructured:** Mapped from legacy `CbnParser` lists to standard `Parser` message lists. Rename to `parsers` in JSON.  
`next_page_token` | `next_page_token` | `string` | **Parity Mapped:** Token to retrieve subsequent pages of parsers. Rename to `nextPageToken` in JSON.  
  
### Nested Parser property mappings

The fields mapping inside individual `Parser` definitions is as follows:

Legacy Field (`CbnParser` message) | Modern Field (`Parser` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`config_id` | `name` | `string` | **Parity Mapped:** Mapped into standard canonical resource paths under name: `projects/{pr}/locations/{loc}/instances/{in}/logTypes/{lt}/parsers/{id}`.  
`log_type` | — _(implicit in resource path)_ | `string` | Managed under the parent segment of the canonical name.  
`config` | `cbn` | `bytes` | Raw CBN parser bytes (omitted if `view` was set to `BASIC_VIEW`).  
`state` | `release_stage` / `validation_stage` | `enum` | **Restructured:** Legacy monolithic `CbnConfigState` enum is split into granular lifecycle attributes: `release_stage` and `validation_stage`.  
`submit_time` / `timestamps` | `create_time` | `Timestamp` | Standardized creation timestamp (`createTime` in JSON).  
`sha256` | — | `string` | **Retired:** Hash verification is managed internally by Chronicle API storage engines.  
`validation_errors` | — _(in validation_stage)_ | `Message` | If validation failed, errors are captured under standard operation metadata or error details.  
`change_log` | `changelogs` | `Message` | Structured changelog representation (omitted in `BASIC_VIEW`).  
`author` | `creator.author` | `string` | Mapped inside creator object.  
  
* * *

## Key differences

  * **Service Consolidation and Architectural Shift:**
    * Legacy backstory provided two separate methods: `ListCbnParserHistory` (for a specific log type) and `ListCbnParsers` (for all default parsers).
    * Modern Chronicle API consolidates parser listing into a single `ListParsers` method on `ParserService`. Scoping is determined by the parent resource path (specifying a specific log type or `-` for all log types).
  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance log type bindings.
  * **View and Filtering Capabilities:**
    * Introduces filter strings and view options (`BASIC_VIEW` / `FULL_VIEW`) allowing clients to query parser summaries without downloading large configuration binaries.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
