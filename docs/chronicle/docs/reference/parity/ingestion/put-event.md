---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/put-event/
title: PutEvent to ImportEvents APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:34.711489+00:00
---

# PutEvent to ImportEvents APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/put-event/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PutEvent to ImportEvents APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API (**`PutEvent`**) to the modern Chronicle API ([**`ImportEvents`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events/import)).

> [!IMPORTANT] The modern `ImportEvents` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized for the target instance resource.

## Protocol and mapping overview

Feature | Legacy API (`PutEvent`) | Modern Chronicle API (`ImportEvents`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/events.import`  
  
* * *

## Request payload field-by-field parity

In the legacy API, `PutEvent` accepted a low-level pipeline container (`PutEventRequest.batch`) containing internal `malachite.Event` objects with disparate protocol-specific payloads (`oneof payload`). In the modern Chronicle API, all event ingestion is unified through `ImportEventsRequest`, which scopes the request to the parent instance in the URL path and wraps the event batch inside an `inline_source` structure containing Universal Data Model (UDM) events.

Legacy field (`PutEventRequest.batch`) | Modern field (`ImportEventsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`source.customer_id` | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, the target customer was identified within the `source.customer_id` field or inferred from the API key. In the modern API, the parent instance is explicitly specified in the request URL: `projects/{project}/locations/{location}/instances/{instance}`.  
— | `inline_source` | `EventsInlineSource` (oneof `source`) | **Encapsulation wrapper:** The modern API encapsulates ingested events inside a `oneof source` container. Inlined event batches are provided within `inline_source`.  
`events` | `inline_source.events` | `repeated Event` | **Parity mapped to canonical UDM events:** List of events to ingest. While the legacy API carried internal `malachite.Event` objects with typed payloads, the modern API standardizes on canonical `Event` resources embedding the `backstory.UDM` schema.  
`id` | — | `bytes` | **Internal batch identifier:** Unique batch deduplication key used in legacy backend pipelines; not exposed in the modern REST API contract.  
`source.collector_id` | — | `bytes` | **Forwarder binding:** In the legacy API, collector identification was passed in the source struct. In modern Chronicle, forwarder and collector attribution is managed using Chronicle Forwarder resource bindings.  
`source.namespace` | `inline_source.events[].udm` | `string` | **Shifted to UDM noun namespace:** Legacy environment namespace is mapped to respective UDM entity/noun namespaces or managed using instance configurations.  
`source.labels` | `inline_source.events[].udm` | `repeated backstory.Label` | **Shifted to UDM labels:** Custom labels are represented in UDM metadata or entity definitions.  
`type` | `inline_source.events[].udm.metadata.event_type` | `EventType` enum | **Mapped to UDM event taxonomy:** Legacy event type classifications (such as `DNS`, `DHCP`, `ALERT`, `USER`, `EDR`) map to standard Universal Data Model `event_type` enumerations.  
`start_time` / `is_replay` / `replay_time` | — | `google.protobuf.Timestamp` / `bool` | **Internal pipeline metadata:** Legacy collector session and replay markers; telemetry replay and ordering in modern Chronicle is governed by event and collection timestamps.  
  
* * *

### Event structure parity (`malachite.Event` versus `google.cloud.chronicle.v1main.Event`)

Each item in `inline_source.events` is an `Event` resource container whose internal `udm` field unifies the disparate legacy payload types into the Universal Data Model:

Legacy field (`malachite.Event`) | Modern field (`Event`) | Field type | Parity and migration notes  
---|---|---|---  
— | `name` | `string` | **New field:** Optional canonical resource name of the event (`projects/{project}/locations/{location}/instances/{instance}/events/{event_id}`).  
`payload` (`oneof payload`) / `idm` | `udm` | `backstory.UDM` | **Unified UDM payload:** The legacy API utilized a polymorphic `oneof payload` containing separate message schemas (`DnsEvent`, `DhcpEvent`, `AlertEvent`, `WebProxyEvent`, `EdrEvent`, `StatsEvent`) or wrapped `idm`. Modern `ImportEvents` consolidates all telemetry into the Universal Data Model schema (`backstory.UDM`).  
`timestamp` | `udm.metadata.event_timestamp` | `google.protobuf.Timestamp` | **Direct mapping:** Time at which the event occurred.  
`collection_time` | `udm.metadata.collected_timestamp` | `google.protobuf.Timestamp` | **Direct mapping:** Time at which the event was collected by the collector or agent.  
`raw_log_index` / `disambiguation_key` | `udm.metadata.id` | `int32` / `bytes` | **Event identity:** Event tracking and deduplication in the modern schema is represented by the unique UDM identifier.  
  
* * *

## Response payload field-by-field parity

Both endpoints return an empty confirmation payload upon successful receipt of the events.

Legacy field (`PutEventResponse`) | Modern field (`ImportEventsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | — | `message` | **Equivalent:** Both APIs return an empty JSON object (`{}`) upon successful validation and queuing of the event batch.  
  
* * *

## Key differences

  * **Internal pipeline format vs. Universal Data Model (UDM) standardization:**
    * Legacy `PutEvent` transmitted events using internal `malachite.EventBatch` structures with fragmented, protocol-specific payloads (`DnsEvent`, `DhcpEvent`, `StatsEvent`, `WebProxyEvent`, `AlertEvent`).
    * Modern `ImportEvents` standardizes all incoming telemetry on the Universal Data Model (`backstory.UDM`), providing consistent entity, network, and security semantics across all data sources.
  * **Specialized forwarder heartbeat telemetry:**
    * In legacy production environments, `PutEvent` was primarily restricted to forwarder heartbeat events (`type: STATS`).
    * For forwarder-specific collector telemetry and health statistics in modern Chronicle, callers can also leverage the dedicated `ImportStatsEvents` API (`chronicle.googleapis.com/forwarders.importStatsEvents`).
  * **Resource-scoped URL vs. global endpoint:**
    * Legacy `PutEvent` posted to `/v1/event:put`, embedding tenant information within `source.customer_id` or resolving it from API credentials.
    * Modern `ImportEvents` adheres to Google Cloud resource hierarchy conventions, placing instance ownership directly in the URL path (`projects/{project}/locations/{location}/instances/{instance}`).
  * **Atomic all-or-nothing batch validation:**
    * Modern `ImportEvents` enforces atomic validation: all events in the batch must conform to valid UDM structures. Any validation error in a single event causes the entire import request to fail.
  * **Modern IAM authorization:**
    * Authentication shifts from legacy Ingestion API keys and partner tokens to standard Google Cloud IAM OAuth 2.0 bearer tokens with permission check `chronicle.googleapis.com/events.import`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
