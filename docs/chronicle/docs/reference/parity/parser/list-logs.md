---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/list-logs/
title: ListLogs parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:53.676802+00:00
---

# ListLogs parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/parser/list-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListLogs parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Tools API (**`RetrieveSampleLogs`**) to the modern Chronicle API (**`ListLogs`**).

## Protocol and mapping overview

Feature | Legacy API (`RetrieveSampleLogs`) | Modern Chronicle API (`ListLogs`)  
---|---|---  
**HTTP Method** | `POST` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/logs.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListLogsRequest` standardizes sample log queries into standard REST resource listing with pagination and AIP-160 filtering.

Legacy Field (`RetrieveSampleLogsRequest`) | Modern Field (`ListLogsRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`log_type` | `parent` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context / Architectural Shift:** Legacy passed `log_type` in the `POST` body. The modern API scopes log listing under a target parent path in the URL: `projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}`.  
`max_entries` | `page_size` | `int32` | **Parity Mapped / Type Shift:** Legacy required `max_entries` (up to 100k). The modern API maps this to standard pagination limit `page_size` (`int32` format). Rename to `pageSize` in JSON.  
`start_time` / `end_time` | `filter` | `string` | **Syntax Shift:** Legacy accepted distinct `start_time` and `end_time` Timestamp fields. The modern API consolidates timestamp bounds into standard AIP-160 filter expression strings on `collection_time`: `collection_time.seconds >= {start_time.seconds} AND collection_time.seconds <= {end_time.seconds}`.  
— | `page_token` | `string` | **New Parameter:** Standard token to retrieve subsequent pages of logs. Rename to `pageToken` in JSON.  
  
* * *

## Response payload field-by-field parity

While legacy backstory returned an array of raw byte sequences, the modern Chronicle API returns a list of structured `Log` messages.

Legacy Field (`SampleLogs` response) | Modern Field (`ListLogsResponse` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`data` | `logs` | `repeated Log` | **Parity Mapped / Enriched:** Legacy returned a raw list of byte strings (`repeated bytes data`). The modern API returns a repeated list of structured `Log` messages (`repeated Log logs`). Each item contains raw bytes inside `data` along with full ingestion timestamps and metadata. Rename to `logs` in JSON.  
— | `next_page_token` | `string` | **New Parameter:** Token to retrieve subsequent pages of logs. Rename to `nextPageToken` in JSON.  
  
### Nested Log property mappings

The fields mapping inside individual `Log` items is as follows:

Legacy Field (`SampleLogs.data[]` raw byte item) | Modern Field (`Log` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`data[]` (Raw log line byte sequence) | `data` | `bytes` | **Parity Mapped:** The raw log sequence byte array is stored directly in the `data` attribute of each `Log` item.  
— | `name` | `string` | **New Field:** Canonical resource path: `projects/{pr}/locations/{loc}/instances/{in}/logTypes/{lt}/logs/{log_id}`.  
— | `log_entry_time` | `Timestamp` | **New Field:** Timestamp of the log event itself. Rename to `logEntryTime` in JSON.  
— | `collection_time` | `Timestamp` | **New Field:** Timestamp recording when the log entry was ingested. Rename to `collectionTime` in JSON.  
— | `environment_namespace` | `string` | **New Field:** Identifies the data domain namespace where the log originated. Rename to `environmentNamespace` in JSON.  
— | `labels` | `map<string, LogLabel>` | **New Field:** Custom user-configured metadata labels map (values and RBAC flags).  
— | `additionals` | `Struct` | **New Field:** Additional structured JSON metadata.  
  
* * *

## Key differences

  * **Service Consolidation and Architectural Standardization:**
    * Legacy sample log retrieval was implemented as a custom `POST` tool action (`POST /v1/tools:retrieveSampleLogs`) under `ToolsService`.
    * Modern Chronicle API standardizes log sample retrieval as standard REST resource listing (`GET .../logs`) under `LogService`, supporting standard pagination (`page_size`, `page_token`).
  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance log type bindings.
  * **Filter-Based Time Windowing:**
    * Separate `start_time` and `end_time` fields are replaced by standard AIP-160 filter expressions targeting `collection_time.seconds`.
  * **Structured Log Responses:**
    * Instead of returning a plain array of raw byte sequences, the API returns structured `Log` messages containing canonical names, entry timestamps, collection times, and metadata labels.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
