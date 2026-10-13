---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/search-raw-logs/
title: SearchRawLogs parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:03.149555+00:00
---

# SearchRawLogs parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/search/search-raw-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SearchRawLogs parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Search API (**`SearchRawLogs`**) to the modern Chronicle API (**`SearchRawLogs`**).

## Protocol and mapping overview

Feature | Legacy API (`SearchRawLogs`) | Modern Chronicle API (`SearchRawLogs`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/events.searchRawLogs`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `SearchRawLogsRequest` scopes raw log searches under target instance environments and replaces single query strings with a two-stage baseline and snapshot filtering architecture.

Legacy field (`SearchRawLogsRequest`) | Modern field (`SearchRawLogsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `instance` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes raw log searches under target instance environments: `projects/{project}/locations/{location}/instances/{instance}`.  
`query` | `baseline_query` and `snapshot_query` | `string` | **Parity mapped, split query model:** Legacy accepted a single query. The modern API supports two-stage filtering: required `baseline_query` (initial scan) and optional `snapshot_query` (subsequent filter over baseline matches). Rename to `baselineQuery` and `snapshotQuery` in JSON.  
`start_time` and `end_time` | `baseline_time_range` and `snapshot_time_range` | `Interval` | **Consolidated:** Legacy distinct start and end timestamps map into required `baseline_time_range` and optional `snapshot_time_range` intervals (`Interval.start_time` and `Interval.end_time`).  
`regex_search` | — _(implicit in syntax)_ | `bool` | **Retired:** Regular expression query modes are embedded natively within modern query syntax strings (using a regular expression context) rather than toggled using standalone flags.  
`case_sensitive` | `case_sensitive` | `bool` | **Parity mapped:** Boolean flag toggling case sensitivity across baseline and snapshot queries. Rename to `caseSensitive` in JSON.  
`product_sources` | `log_types` | `repeated string` $\rightarrow$ `repeated LogType` | **Parity mapped, restructured:** Replaced by structured `LogType` definitions (`repeated LogType log_types`) restricting matches to specific telemetry log sources. Rename to `logTypes` in JSON.  
`page_size` | `page_size` | `int32` | **Parity mapped:** Sets the maximum returned result volume limit. Rename to `pageSize` in JSON.  
`page_token` | — _(retired for streaming)_ | `string` | **Retired:** Because modern `SearchRawLogs` streams results back in real-time, initial page tokens are not required on requests.  
`include_full_raw_logs` | — _(implicit in return model)_ | `bool` | **Retired:** Modern search results automatically populate raw snippets or normalized forms inside unified `RawLogResult` objects.  
— | `max_aggregations_per_field` or `draft_data_access_scope` | `int32` or `DataAccessScope` | **New parameters:** Adds control over prevalence aggregation limits (`max_aggregations_per_field`) and allows admins to preview in-development Data RBAC rules (`draft_data_access_scope`).  
  
* * *

## Response payload field-by-field parity

While legacy backstory returned an asynchronous LRO payload separating normalized UDM events and unparsed raw logs, the modern Chronicle API streams back unified `RawLogResult` matches alongside real-time progress, bucketed timelines, and field aggregations.

Legacy field (`SearchRawLogsResponse`) | Modern field (`SearchRawLogsResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`events` and `raw_log_events` | `matches` | `repeated RawLogResult` | **Parity mapped, consolidated:** Legacy separated normalized UDM events and unparsed `raw_log_events`. The modern API unifies these under `matches` (`repeated RawLogResult`), where each item exposes a summary string, ID, log type, and a result oneof containing either a normalized `Event`, normalized `Entity`, or unparsed `RawLogSnippet`. Rename to `matches` in JSON.  
— | `progress` | `int32` | **New field:** Real-time query execution progress represented as an integer percentage between 0 and 100.  
— | `timeline` | `EventTimeline` | **New field:** Streamed timeline buckets (`EventTimeline`) reporting parsed versus unparsed log counts across time intervals.  
— | `aggregations` | `Aggregations` | **New field:** Streamed field aggregations reporting top and bottom prevalence values across matched result types.  
`next_page_token` | `next_page_token` | `string` | **Parity mapped:** Token indicating whether more value matches are available. Rename to `nextPageToken` in JSON.  
`total_records`, `too_many_results`, `validation_error`, or `max_returned_raw_log_lines` | — _(moved to metadata and timeline)_ | `int64`, `bool`, or `Message` | **Retired, refactored:** Storage counters and truncation flags are relocated to timeline buckets (`EventTimelineBucket.too_many_events`) and stream metadata, while syntax validation failures are reported using standard gRPC stream error status codes.  
  
### Nested RawLogResult property mappings

The fields mapping inside individual RawLogResult items is as follows:

Legacy field (`events` and `raw_log_events` item) | Modern field (`RawLogResult` message) | Field type | Parity and migration notes  
---|---|---|---  
`events[].udm` | `event` | `Event` | Mapped inside the result oneof when the raw log successfully parsed into a UDM event.  
— | `entity` | `Entity` | Mapped inside the result oneof when the raw log parsed into an entity context record.  
`raw_log_events[].snippet` | `snippet` | `RawLogSnippet` | Mapped inside the result oneof when the raw log could not be normalized (`RawLogSnippet` contains id, snippet, and ingestion_time).  
`raw_log_events[].raw_logs_token` | `id` | `bytes` | Unique identifier byte array for the raw log, event, or entity result.  
— | `summary` | `string` | Human-readable summary string (snippet for unparsed logs, description for normalized telemetry and context events).  
— | `log_type` | `LogType` | Identifies the originating log source type of the match. Rename to `logType` in JSON.  
  
* * *

## Key differences

  * **Service consolidation and LRO to streaming shift:**
    * Legacy raw log searching was housed under `SearchService` and executed as an asynchronous LRO (`google.longrunning.Operation`).
    * Modern Chronicle API standardizes raw log searches under `EventService` (`SearchRawLogs`) as a streaming RPC (`returns (stream SearchRawLogsResponse)`), eliminating LRO polling overhead and delivering matches, timelines, and aggregations in real-time.
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings (`instance` path parameter).
  * **Consolidated result architecture (RawLogResult):**
    * Separate legacy arrays for UDM events and unparsed logs are unified into a single `matches` stream of `RawLogResult` objects, cleanly isolating parsed telemetry, entity context, and unparsed raw snippets using a protobuf `oneof`.
  * **Time window consolidation (Interval):**
    * Standalone timestamp pairs (`start_time`, `end_time`) are structured into standard `google.type.Interval` objects (`baseline_time_range`, `snapshot_time_range`).
  * **IAM permissions:**
    * Request validation maps to standard Cloud IAM permission validation check (`chronicle.googleapis.com/events.searchRawLogs`).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
