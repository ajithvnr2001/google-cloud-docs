---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/import-logs/
title: ImportLogs APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:36.774181+00:00
---

# ImportLogs APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/import-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ImportLogs APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API (**`CreateUnstructuredLogEntries`**) to the modern Chronicle API ([**`ImportLogs`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.logs/import)).

> [!IMPORTANT] The modern `ImportLogs` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized for the target instance and log type resources.

## Protocol and mapping overview

Feature | Legacy API (`CreateUnstructuredLogEntries`) | Modern Chronicle API (`ImportLogs`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/logs.import`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers sent batches of raw telemetry using `UnstructuredLogEntriesUpload`, supplying `customer_id` and `log_type` alongside batch-level metadata in the request body. In the modern Chronicle API, logs are ingested through `ImportLogsRequest`, which encodes both the instance hierarchy and target log type directly within the `parent` resource path and wraps the log batch inside an `inline_source` structure.

Legacy field (`UnstructuredLogEntriesUpload`) | Modern field (`ImportLogsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_id` | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, customer identification was passed using the `customer_id` body field. In the modern API, the customer instance is identified in the resource path: `projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}`.  
`log_type` | `parent` _(in HTTP path)_ | `string` | **Path-based log type binding:** The log type identifying the format and parser (for example, `WINEVTLOG` or `PAN_FIREWALL`) is bound directly in the URL path as a subresource of the instance.  
— | `inline_source` | `LogsInlineSource` (oneof `source`) | **Encapsulation wrapper:** The modern API encapsulates ingested telemetry inside a `oneof source` container. Inlined log batches are provided within `inline_source`.  
`entries` | `inline_source.logs` | `repeated Log` | **Parity mapped with per-log metadata:** Repeated list of log entries to be ingested. The modern API converts entries into canonical `Log` resources with dedicated timestamps, labels, and metadata.  
`additionals` | `inline_source.logs[].additionals` | `google.protobuf.Struct` | **Shifted to per-log scope:** In the legacy API, `additionals` applied across the entire batch. In the modern API, supplemental structured metadata is specified per log entry in `Log.additionals`.  
`namespace` | `inline_source.logs[].environment_namespace` | `string` | **Shifted to per-log scope:** In the legacy API, environment namespace applied across the entire batch. In the modern API, namespace tagging is configured individually per log entry in `Log.environment_namespace`.  
`labels` | `inline_source.logs[].labels` | `map<string, LogLabel>` | **Shifted to per-log scope with RBAC support:** In the legacy API, labels were passed as a repeated list of key-value pairs at the batch level. In the modern API, labels are configured per log as a key-value map with optional Role-Based Access Control (`rbac_enabled`).  
— | `inline_source.forwarder` | `string` | **New field:** Optional resource name of the Chronicle Forwarder (`projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder}`) sending the import request, establishing CollectorID binding.  
— | `inline_source.source_filename` | `string` | **New field:** Optional source filename used for out-of-band processing metadata.  
— | `hint` | `string` | **New field:** Optional opaque hint string provided at the request root to aid parser execution.  
  
* * *

### Log entry structure parity (`UnstructuredLogEntry` versus `google.cloud.chronicle.v1main.Log`)

The individual log structure transitions from the legacy `UnstructuredLogEntry` to the modern `Log` resource definition:

Legacy field (`UnstructuredLogEntry`) | Modern field (`Log`) | Field type | Parity and migration notes  
---|---|---|---  
`content.log_text` / `content.log_binary` | `data` | `bytes` | **Standardized binary data:** The legacy API offered a `oneof content` supporting either text (`log_text`) or binary (`log_binary`). The modern API unifies payload representation using `bytes data` (raw text logs should be sent as UTF-8 encoded bytes).  
`timestamp.ts_epoch_microseconds` / `timestamp.ts_rfc3339` | `log_entry_time` | `google.protobuf.Timestamp` | **Standardized timestamp:** The legacy API supported epoch microseconds or RFC 3339 string timestamps. The modern API standardizes on `google.protobuf.Timestamp` representing when the log event occurred.  
— | `collection_time` | `google.protobuf.Timestamp` | **New required field:** The timestamp when the log entry was collected by the ingestion client or forwarder. Must be equal to or after `log_entry_time`.  
— | `name` | `string` | **Output only:** Canonical resource name of the log (`projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}/logs/{log}`).  
— | `time_zone` | `string` | **New field:** Optional IANA time zone database name (for example, `America/New_York`) to calculate UTC offset when timestamps in the raw payload lack timezone context.  
_(batch-level)_ `namespace` | `environment_namespace` | `string` | **Per-log environment namespace:** User-configured data domain tag for indexing and enrichment.  
_(batch-level)_ `additionals` | `additionals` | `google.protobuf.Struct` | **Per-log JSON metadata:** Dynamic JSON structure for arbitrary custom fields.  
_(batch-level)_ `labels` | `labels` | `map<string, LogLabel>` | **Per-log labels:** Key-value map of custom labels, with each entry containing `value` (`string`) and `rbac_enabled` (`bool`).  
  
* * *

## Response payload field-by-field parity

Both endpoints return an empty confirmation payload upon successful receipt of the log batch.

Legacy field (`google.protobuf.Empty`) | Modern field (`ImportLogsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | — | `message` | **Equivalent:** Both APIs return an empty JSON object (`{}`) upon successful validation and queuing of the log batch.  
  
* * *

## Key differences

  * **Hierarchical URL path scoping (`parent`):**
    * Legacy `CreateUnstructuredLogEntries` passed `customer_id` and `log_type` as payload fields to a global endpoint (`/v1/unstructuredlogentries`).
    * Modern `ImportLogs` adheres to Google Cloud Resource Manager hierarchy conventions, binding both the instance and the log type in the URL path (`/v1/projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}/logs:import`).
  * **Per-log metadata scoping:**
    * In the legacy API, `namespace`, `additionals`, and `labels` were defined at the batch root and applied uniformly across all entries in the batch.
    * In the modern API, these attributes are configured individually on each `Log` resource (`environment_namespace`, `additionals`, `labels`), allowing diverse domains, labels, and metadata within a single batch upload.
  * **Unified raw payload representation (`bytes data`):**
    * Legacy `UnstructuredLogEntry` utilized a `oneof content` supporting either `log_text` (string) or `log_binary` (bytes).
    * Modern `Log` standardizes on `bytes data`. Text logs must be encoded into UTF-8 bytes prior to transmission.
  * **Granular time tracking (`log_entry_time` and `collection_time`):**
    * Modern `ImportLogs` requires explicit population of `collection_time` alongside `log_entry_time`, providing latency and collection telemetry essential for downstream pipeline ordering.
  * **Forwarder and collector attribution:**
    * Modern `ImportLogsRequest` provides optional direct linkage to forwarder configurations using `inline_source.forwarder`, ensuring accurate SecOps Collector attribution.
  * **Modern IAM authorization:**
    * Authentication shifts from legacy Ingestion API keys and partner tokens to standard Google Cloud IAM OAuth 2.0 bearer tokens with permission check `chronicle.googleapis.com/logs.import`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
