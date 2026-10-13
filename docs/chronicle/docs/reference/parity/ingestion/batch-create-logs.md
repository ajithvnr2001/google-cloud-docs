---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-logs/
title: BatchCreateLogs to ImportLogs APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:35.520107+00:00
---

# BatchCreateLogs to ImportLogs APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BatchCreateLogs to ImportLogs APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API v2 (**`BatchCreateLogs`**) to the modern Chronicle API ([**`ImportLogs`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.logs/import)).

> [!IMPORTANT] The modern `ImportLogs` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized with `chronicle.googleapis.com/logs.import` for the target instance and log type resources.

## Protocol and mapping overview

Feature | Legacy API v2 (`BatchCreateLogs`) | Modern Chronicle API (`ImportLogs`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/logs.import`  
  
* * *

## Request payload field-by-field parity

In the legacy Ingestion API v2, callers sent batches of telemetry logs using `BatchCreateLogsRequest`, wrapping entries and collection metadata in `LogEntryBatch`. Customer identification, collector ID, log type, and parser hints were passed as body attributes.

In the modern Chronicle API, telemetry logs are ingested through `ImportLogsRequest`. The target instance and log type are bound directly within the `parent` URL path parameter, while log entries, forwarder identity, and source file metadata are wrapped inside an `inline_source` structure (`LogsInlineSource`).

Legacy field (`BatchCreateLogsRequest`) | Modern field (`ImportLogsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`batch.source.customer_id` | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In legacy v2, customer GUID was supplied in `batch.source.customer_id`. In the modern API, the customer instance is specified in the request URL: `projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}`.  
`batch.log_type` / `batch.type` | `parent` _(in HTTP path)_ | `string` | **Path-based log type binding:** In legacy v2, the log type was specified using string `batch.log_type` or enum `batch.type`. In the modern API, the log type is bound directly as the terminal element of the `parent` URL path.  
`batch.hint` | `hint` | `string` | **Direct mapping:** Opaque hint string passed to assist log parsing and normalization routines.  
— | `inline_source` | `LogsInlineSource` (oneof `source`) | **Encapsulation wrapper:** Modern Chronicle API encapsulates inline log payloads within a `oneof source` container (`inline_source`).  
`batch.entries` | `inline_source.logs` | `repeated Log` | **Parity mapped with per-log metadata:** List of raw log entries. In the modern API, entries are modeled as `Log` resources with dedicated timestamps, labels, and per-log metadata.  
`batch.source.collector_id` | `inline_source.forwarder` | `string` | **Resource reference:** In legacy v2, the collector GUID was supplied in `batch.source.collector_id`. In the modern API, callers specify the Chronicle Forwarder resource name (`projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder}`), establishing the SecOps CollectorID.  
`batch.source.filename` | `inline_source.source_filename` | `string` | **Direct mapping:** Name of the source file processed by out-of-band collection agents, used by parsers during normalization.  
`batch.source.namespace` | `inline_source.logs[].environment_namespace` | `string` | **Shifted to per-log scope:** In legacy v2, environment namespace was defined on `batch.source`. In the modern API, namespace tagging is configured individually per entry in `Log.environment_namespace`.  
`batch.source.labels` | `inline_source.logs[].labels` | `map<string, LogLabel>` | **Shifted to per-log scope with RBAC:** In legacy v2, labels were passed as repeated key-value pairs on `batch.source`. In the modern API, labels are configured per log as a key-value map with optional Role-Based Access Control (`rbac_enabled`).  
`batch.additionals` | `inline_source.logs[].additionals` | `google.protobuf.Struct` | **Shifted to per-log scope:** In legacy v2, supplemental JSON metadata applied across the entire batch. In the modern API, structured metadata is supplied per sign in `Log.additionals`.  
`batch.id` | — | `bytes` | **Managed by ingestion pipeline:** In legacy v2, callers provided a batch UUID for deduplication. Modern Chronicle API handles idempotency and deduplication through ingestion pipeline sequencing.  
`batch.start_time` | — | `google.protobuf.Timestamp` | **Deprecated:** Collector startup timestamp is not required for log telemetry ingestion.  
`batch.is_replay` / `batch.replay_time` | — | `bool` / `Timestamp` | **Deprecated:** Replay tracking flags from legacy batch collectors are not used in modern API log imports.  
`batch.is_out_of_quota_batch` | — | `bool` | **Internal / deprecated:** Legacy internal quota routing indicator is managed automatically by Chronicle infrastructure.  
`batch.source.feed_id` | — | `string` | **Deprecated:** Feed routing is handled using forwarder and log type configuration in Chronicle.  
  
* * *

### Log entry structure parity (`malachite.LogEntry` versus `google.cloud.chronicle.v1main.Log`)

Each individual log entry in `batch.entries` maps to a modern `Log` resource in `inline_source.logs`:

Legacy `LogEntry` field | Modern `Log` field | Field type | Parity and migration notes  
---|---|---|---  
`data` | `data` | `bytes` | **Direct mapping:** Raw payload of the log entry. Text logs must be encoded as UTF-8 bytes.  
`timestamp` | `log_entry_time` | `google.protobuf.Timestamp` | **Direct mapping:** The timestamp when the log event occurred at the source.  
`collection_time` | `collection_time` | `google.protobuf.Timestamp` | **Direct mapping:** The timestamp when the log entry was collected. Must be equal to or after `log_entry_time`.  
`timezone` | `time_zone` | `string` | **Direct mapping:** IANA time zone database name (for example, `America/New_York`) used to resolve UTC offsets when raw log strings lack timezone metadata.  
`source.namespace` | `environment_namespace` | `string` | **Per-log environment namespace:** User-configured data domain tag for indexing, enrichment, and filtering.  
`source.labels` | `labels` | `map<string, LogLabel>` | **Per-log labels:** Custom metadata key-value pairs supporting fine-grained RBAC controls.  
_(batch-level)_ `additionals` | `additionals` | `google.protobuf.Struct` | **Per-log JSON metadata:** Dynamic JSON structure for arbitrary custom fields.  
`udm` | — | `bytes` | **Separated into dedicated endpoint:** In legacy v2, callers could optionally attach raw UDM bytes to `LogEntry`. In the modern Chronicle API, structured UDM telemetry is ingested using [**`ImportEvents`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events/import).  
— | `name` | `string` | **Output only:** Canonical resource name of the log (`projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}/logs/{log}`).  
  
* * *

## Response payload field-by-field parity

Both endpoints return an empty confirmation payload upon successful receipt and queuing of the log batch.

Legacy field (`BatchCreateLogsResponse`) | Modern field (`ImportLogsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | — | `message` | **Equivalent:** Both APIs return an empty JSON object (`{}`) upon successful validation of the log batch.  
  
* * *

## Key differences

  * **Hierarchical URL path scoping (`parent`):**
    * Legacy `BatchCreateLogs` sent requests to a global endpoint (`/v2/logs:batchCreate`), passing customer and log type identifiers inside `batch.source` and `batch.log_type`.
    * Modern `ImportLogs` embeds instance and log type ownership directly in the URL path (`/v1/projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}/logs:import`), adhering to standard Google Cloud resource naming.
  * **Per-log metadata flexibility:**
    * In legacy v2, `additionals`, `namespace`, and `labels` were set at the batch level (`LogEntryBatch`), applying uniformly across all entries in the batch.
    * In the modern API, each `Log` entry within `inline_source.logs` can define its own `environment_namespace`, `labels`, and `additionals`, allowing heterogeneous domains and metadata within a single batch.
  * **Forwarder and collector resource binding:**
    * Legacy v2 passed a raw GUID in `batch.source.collector_id`.
    * Modern `ImportLogs` references the full Google Cloud Forwarder resource name (`inline_source.forwarder`), ensuring consistent lifecycle and configuration management.
  * **Separation of structured UDM and raw log telemetry:**
    * Legacy `LogEntry` supported an optional `udm` field embedded within the log entry.
    * The modern API maintains clean architectural separation: raw logs intended for parser ingestion are handled by `ImportLogs`, whereas structured UDM events bypass parsers and are ingested directly using `ImportEvents`.
  * **Modern IAM authorization:**
    * Authentication transitions from legacy Ingestion API keys and partner tokens to standard Google Cloud IAM credentials requiring `chronicle.googleapis.com/logs.import`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
