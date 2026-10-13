---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-udm-events/
title: BatchCreateUDMEvents to ImportEvents APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:33.187664+00:00
---

# BatchCreateUDMEvents to ImportEvents APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/batch-create-udm-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# BatchCreateUDMEvents to ImportEvents APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API v2 (**`BatchCreateUDMEvents`**) to the modern Chronicle API ([**`ImportEvents`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events/import)).

> [!IMPORTANT] The modern `ImportEvents` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized with `chronicle.googleapis.com/events.import` for the target instance resource.

## Protocol and mapping overview

Feature | Legacy API v2 (`BatchCreateUDMEvents`) | Modern Chronicle API (`ImportEvents`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/events.import`  
  
* * *

## Request payload field-by-field parity

In the legacy Ingestion API v2, callers submitted Unified Data Model (UDM) event batches using `BatchCreateUDMEventsRequest`, specifying `customer_id` and an optional `log_type` or associated raw log `entries` in the request body.

In the modern Chronicle API, events are ingested through `ImportEventsRequest`. The request scopes the target customer instance using the `parent` URL path parameter and wraps the event batch inside an `inline_source` structure (`EventsInlineSource`), with each event structured as an `Event` resource container.

Legacy field (`BatchCreateUDMEventsRequest`) | Modern field (`ImportEventsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`customer_id` | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In legacy v2, the customer GUID was supplied in `customer_id`. In the modern API, the customer instance is specified directly in the request URL: `projects/{project}/locations/{location}/instances/{instance}`.  
— | `inline_source` | `EventsInlineSource` (oneof `source`) | **Encapsulation wrapper:** Modern Chronicle API encapsulates inline event batches inside a `oneof source` container (`inline_source`).  
`events` | `inline_source.events` | `repeated Event` | **Parity mapped with resource container:** Repeated list of UDM events to be ingested. Whereas legacy v2 held `repeated backstory.UDM` directly, the modern API encapsulates each event in a canonical `Event` resource container holding the `udm` payload and an optional `name` identifier.  
`log_type` | `inline_source.events[].udm.metadata.product_name` | `string` | **Embedded in UDM metadata:** In legacy v2, an optional top-level `log_type` could be specified (defaulting to `UDM`). In the modern API, event categorization and product identification are modeled directly inside each event's UDM metadata (`udm.metadata.vendor_name`, `udm.metadata.product_name`, and `udm.metadata.product_event_type`).  
`entries` | — | `repeated UnstructuredLogEntry` | **Decoupled raw log ingestion:** In legacy v2, callers could optionally attach raw unparsed log strings alongside UDM events. In modern Chronicle architecture, raw log ingestion is handled through [**`ImportLogs`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.logs/import) to ensure proper pipeline indexing and normalization, while `ImportEvents` is dedicated strictly to structured UDM telemetry.  
  
* * *

### Event container and UDM structure parity (`backstory.UDM` versus `google.cloud.chronicle.v1main.Event`)

Each item in `inline_source.events` is an `Event` resource container whose internal `udm` field retains 100% schema fidelity with the Universal Data Model (`backstory.UDM`):

Modern field (`Event`) | Legacy equivalent | Field type | Parity and migration notes  
---|---|---|---  
`name` | — | `string` | **New field:** Optional canonical resource name of the event (`projects/{project}/locations/{location}/instances/{instance}/events/{event_id}` where `{event_id}` is the URL-encoded Base64 representation of `udm.metadata.id`).  
`udm` | `events[]` | `backstory.UDM` | **Direct mapping:** Complete UDM event payload containing event taxonomy, entities, network attributes, and metadata.  
  
#### Top-level UDM event fields (`backstory.UDM`)

The schema of `udm` inside each `Event` directly corresponds to the legacy UDM event structure:

UDM field | Field type | Parity and migration notes  
---|---|---  
`metadata` | `Metadata` | **Direct mapping:** Core event metadata including `event_timestamp`, `event_type`, `product_name`, `vendor_name`, `product_event_type`, `product_log_id`, and `id`.  
`principal` | `Noun` | **Direct mapping:** Acting entity (user, asset, process) originating the activity.  
`target` | `Noun` | **Direct mapping:** Target entity (user, asset, file, process, registry) being acted upon.  
`src` | `Noun` | **Direct mapping:** Source entity where activity originated when distinct from `principal`.  
`intermediary` | `repeated Noun` | **Direct mapping:** Proxy servers, firewalls, or relay devices through which the activity passed.  
`observer` | `Noun` | **Direct mapping:** Sensors, packet sniffers, or scanning engines that observed the activity.  
`about` | `repeated Noun` | **Direct mapping:** Ancillary entities referenced in the event (such as file attachments or embedded URLs).  
`security_result` | `repeated SecurityResult` | **Direct mapping:** Security verdicts, detection actions, alert classifications, and risk scores.  
`network` | `Network` | **Direct mapping:** Network protocol metadata, including `ip_protocol`, `direction`, and protocol-specific details (such as HTTP, DNS, DHCP, email).  
`extensions` | `Extensions` | **Direct mapping:** Domain-specific telemetry extensions (such as authentication, vulnerability, or cloud context).  
`additional` | `google.protobuf.Struct` | **Direct mapping:** Dynamic JSON structure for supplementary vendor attributes not accommodated in standard UDM fields.  
`extracted` | `google.protobuf.Struct` | **Direct mapping:** Raw log fields extracted during processing.  
`grouped` | `GroupedFields` | **Direct mapping:** Grouped fields for correlated telemetry attributes.  
  
* * *

## Response payload field-by-field parity

Both endpoints return an empty confirmation payload upon successful receipt and queuing of the event batch.

Legacy field (`BatchCreateUDMEventsResponse`) | Modern field (`ImportEventsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | — | `message` | **Equivalent:** Both APIs return an empty JSON object (`{}`) upon successful validation of the event batch.  
  
* * *

## Key differences

  * **Resource-scoped URL vs. global endpoint:**
    * Legacy `BatchCreateUDMEvents` sent requests to a global endpoint (`/v2/udmevents:batchCreate`), passing `customer_id` in the request body.
    * Modern `ImportEvents` adopts Google Cloud resource hierarchy standards, placing instance ownership directly in the URL path (`/v1/projects/{project}/locations/{location}/instances/{instance}/events:import`).
  * **Payload encapsulation (`oneof source`):**
    * Legacy v2 accepted the `events` array directly at the root level of the request body.
    * Modern `ImportEvents` wraps the event batch inside an `inline_source` container (`EventsInlineSource`), preparing the contract for future ingestion sources while encapsulating each UDM payload in an `Event` resource wrapper.
  * **Separation of raw unparsed logs from UDM events:**
    * Legacy v2 included an optional `entries` field allowing raw log strings to accompany UDM events.
    * Modern Chronicle architecture cleanly distinguishes between raw log ingestion ([**`ImportLogs`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.logs/import)), which triggers Chronicle parsing pipelines, and pre-normalized UDM ingestion ([**`ImportEvents`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events/import)), which inserts structured telemetry directly into the UDM data plane.
  * **Atomic batch validation consistency:**
    * Both legacy v2 and modern APIs enforce atomic validation across the entire batch: all events in the request must be valid for the call to succeed. A validation error in any single event causes the entire import request to fail.
  * **Modern IAM authorization:**
    * Authentication transitions from legacy Ingestion API keys to standard Google Cloud IAM credentials with the `chronicle.googleapis.com/events.import` permission.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
