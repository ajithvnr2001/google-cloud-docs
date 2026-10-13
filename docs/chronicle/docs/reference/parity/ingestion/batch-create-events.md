---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-events/
title: BatchCreateEvents to ImportStatsEvents APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:36.185026+00:00
---

# BatchCreateEvents to ImportStatsEvents APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BatchCreateEvents to ImportStatsEvents APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API v2 (**`BatchCreateEvents`**) to the modern Chronicle API ([**`ImportStatsEvents`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.forwarders/importStatsEvents)).

> [!IMPORTANT] The modern `ImportStatsEvents` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized with `chronicle.googleapis.com/forwarders.importStatsEvents` for the target forwarder resource.

## Protocol and mapping overview

Feature | Legacy API v2 (`BatchCreateEvents`) | Modern Chronicle API (`ImportStatsEvents`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/forwarders.importStatsEvents`  
  
* * *

## Request payload field-by-field parity

In the legacy Ingestion API v2, forwarders and collection agents reported heartbeat and performance statistics using `BatchCreateEventsRequest`. While `EventBatch` was structurally shared with security events, this endpoint was restricted to forwarder heartbeat events (`type = STATS` or `type = AGENT_STATS`), carrying customer and collector identifiers inside `batch.source`.

In the modern Chronicle API, forwarder statistics are ingested through the purpose-built `ImportStatsEventsRequest` on `ForwarderService`. The request is directly addressed to the target forwarder resource in the URL path, and stats events are wrapped in an `inline_source` structure containing dedicated `IngestionStatsEvent` objects.

Legacy field (`BatchCreateEventsRequest`) | Modern field (`ImportStatsEventsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`batch.source.customer_id` | `name` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API v2, the customer GUID was passed in `batch.source.customer_id`. In the modern API, the customer instance is specified as part of the forwarder resource hierarchy in the request URL: `projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder}`.  
`batch.source.collector_id` | `name` _(in HTTP path)_ | `string` | **Resource identification:** In legacy v2, the collector GUID was passed in `batch.source.collector_id`. In the modern API, the forwarder is identified directly as the target resource in the URL: `.../forwarders/{forwarder}`.  
`batch.id` | `inline_source.event_batch_id` | `bytes` | **Direct mapping:** Unique batch identifier used for deduplication and idempotent processing of stats batches.  
— | `inline_source` | `InlineSource` (oneof `source`) | **Encapsulation wrapper:** The modern API encapsulates ingested stats events inside a `oneof source` container. Inlined stats events are provided within `inline_source`.  
`batch.events` | `inline_source.events` | `repeated IngestionStatsEvent` | **Streamlined event structure:** In legacy v2, events were sent as generic `Event` messages holding a `oneof payload`. The modern API uses a dedicated `IngestionStatsEvent` structure that eliminates unused security event fields.  
`batch.type` | — | `EventType` enum | **Deprecated / implicit:** Legacy v2 required setting `type = STATS` or `type = AGENT_STATS`. In the modern API, the event type is inherently defined by the `ImportStatsEvents` method and the `oneof event` choice (`stats` or `agent_stats`).  
`batch.raw_log_type` | — | `LogType` enum | **Not required:** Forwarder operational heartbeat telemetry does not require raw log type categorization.  
`batch.start_time` | `agent_stats.start_time` _(if applicable)_ | `google.protobuf.Timestamp` | **Relocated:** Collector startup timestamp can be supplied within `AgentStatsEvent.start_time`.  
`batch.is_replay` / `batch.replay_time` | — | `bool` / `Timestamp` | **Deprecated:** Forwarder telemetry statistics represent real-time heartbeat and resource usage reports; replay semantics don't apply.  
`batch.source.namespace` | — | `string` | **Managed by forwarder resource:** Environment namespaces are configured on the `Forwarder` resource (`Forwarder.config.metadata.namespace`) rather than repeatedly transmitted with every heartbeat batch.  
`batch.source.labels` | — | `repeated Label` | **Managed by forwarder resource:** Metadata labels are defined at the `Forwarder` resource level in Chronicle.  
  
* * *

### Event structure parity (`malachite.Event` versus `IngestionStatsEvent`)

In the legacy API, each entry in `batch.events` was an instance of the generic `malachite.Event` message. In the modern API, `inline_source.events` uses `IngestionStatsEvent`, providing clean separation between forwarder metrics and security event ingestion:

Legacy `Event` field | Modern `IngestionStatsEvent` field | Field type | Parity and migration notes  
---|---|---|---  
`timestamp` | `event_time` | `google.protobuf.Timestamp` | **Direct mapping:** The timestamp at which the heartbeat or stats sample was recorded.  
`collection_time` | — | `google.protobuf.Timestamp` | **Simplified:** For operational forwarder statistics, collection time is equivalent to `event_time`.  
`payload.stats` | `event.stats` | `malachite.StatsEvent` | **Direct mapping:** Forwarder performance and health metrics. Retains the identical schema in both APIs.  
`payload.agent_stats` | `event.agent_stats` | `malachite.AgentStatsEvent` | **Direct mapping:** Agent lifecycle telemetry. Retains the identical schema in both APIs.  
`source` | — | `EventSource` | **Redundant:** Forwarder identity is established by the resource path in the request URL.  
`raw_log_index` | — | `int32` | **Not applicable:** Forwarder heartbeat events are synthetic telemetry and are not derived from raw log entries.  
`si_event_data` | — | `SIEventData` | **Not applicable:** Indexing and search structures are not used for forwarder statistics.  
`idm` | — | `IDM` | **Not applicable:** Universal Data Model (UDM) structures are not used for forwarder statistics.  
  
* * *

### Telemetry payload parity (`StatsEvent` and `AgentStatsEvent`)

Both the legacy and modern APIs share the identical underlying protobuf definitions for forwarder and agent statistics:

  * **`StatsEvent` (`event.stats`)**: 
    * **System resource usage:** `rusage` (`RUsage`), `mem_stats` (`MemStats`), `disk_stats` (`DiskStats`), `cpu_stats` (`CpuStats`), `net_stats` (`NetStats`), and `container_stats` (`ContainerStats`).
    * **Ingestion performance:** `input_stats` (`repeated InputStatsEvent`) tracking per-input dropped lines, byte counts, and queue latencies; `aggregated_batch_stats` (`LogEntryBatchMetrics`) across all inputs.
    * **Collector and environment metadata:** `collector_version`, `collector_hostname`, `os`, `os_version`, `config_hash`, `auth_config_hash`, `semantic_version`, and `auto_update_enabled`.
    * **Diagnostics:** `error_info` (`repeated ErrorInfo`), `last_failed_upload`, `last_attempted_upload`, `last_failed_status_code`, and `remote_logging_verbosity_level`.
  * **`AgentStatsEvent` (`event.agent_stats`)**: 
    * **Lifecycle timestamps:** `start_time` (collector process start timestamp), `window_start_time` (statistical collection window start), and `last_successful_upload_time`.



* * *

## Response payload field-by-field parity

Both endpoints return an empty confirmation payload upon successful receipt and queuing of the statistics batch.

Legacy field (`BatchCreateEventsResponse`) | Modern field (`ImportStatsEventsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | — | `message` | **Equivalent:** Both APIs return an empty JSON object (`{}`) upon successful validation of the stats batch.  
  
* * *

## Key differences

  * **Dedicated forwarder service vs. overloaded event endpoint:**
    * In the legacy Ingestion API v2, `BatchCreateEvents` re-used the generic `EventBatch` schema, relying on convention (`type = STATS`) to route forwarder heartbeat events.
    * In the modern Chronicle API, forwarder telemetry is handled by `ImportStatsEvents` on `ForwarderService`, utilizing a focused `IngestionStatsEvent` structure that removes extraneous fields unrelated to forwarder monitoring.
  * **Google Cloud resource hierarchy scoping:**
    * Legacy v2 requests were sent to a global endpoint (`/v2/events:batchCreate`) with customer and collector GUIDs embedded in `batch.source`.
    * The modern API addresses the forwarder resource directly in the URL path (`/v1/projects/{project}/locations/{location}/instances/{instance}/forwarders/{forwarder}:importStatsEvents`).
  * **Resource-level configuration and label management:**
    * In legacy v2, collectors submitted `namespace` and `labels` with each heartbeat batch in `batch.source`.
    * In the modern API, forwarder metadata and namespaces are configured centrally on the `Forwarder` resource (`Forwarder.config.metadata`), ensuring consistency across all telemetry without per-batch overhead.
  * **Modern IAM authorization:**
    * Authentication transitions from legacy Ingestion API keys to standard Google Cloud IAM credentials with the `chronicle.googleapis.com/forwarders.importStatsEvents` permission.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
