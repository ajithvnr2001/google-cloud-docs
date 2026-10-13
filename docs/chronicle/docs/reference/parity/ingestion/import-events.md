---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/import-events/
title: ImportEvents APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:33.992444+00:00
---

# ImportEvents APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/import-events/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ImportEvents APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API (**`CreateUDMEvents`**) to the modern Chronicle API ([**`ImportEvents`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.events/import)).

> [!IMPORTANT] The modern `ImportEvents` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized for the target instance resource.

## Protocol and mapping overview

Feature | Legacy API (`CreateUDMEvents`) | Modern Chronicle API (`ImportEvents`)  
---|---|---  
**HTTP method** | `POST` | `POST`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/events.import`  
  
* * *

## Request payload field-by-field parity

In the legacy API, callers sent Unified Data Model (UDM) events using `CreateUDMEventsRequest`, placing the `events` array directly at the top level of the request body. In the modern Chronicle API, events are ingested through `ImportEventsRequest`, which scopes the request to the parent instance in the URL path and wraps the event batch inside an `inline_source` structure.

Legacy field (`CreateUDMEventsRequest`) | Modern field (`ImportEventsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, the target customer was determined implicitly by the ingestion API key or partner authentication token. In the modern API, the parent instance is explicitly specified in the request URL: `projects/{project}/locations/{location}/instances/{instance}`.  
— | `inline_source` | `EventsInlineSource` (oneof `source`) | **Encapsulation wrapper:** The modern API encapsulates ingested events inside a `oneof source` container. Inlined event batches are provided within `inline_source`.  
`events` | `inline_source.events` | `repeated Event` | **Parity mapped with resource container:** Repeated list of UDM events to be ingested. Whereas the legacy API held `repeated backstory.UDM` directly, the modern API wraps each item in a canonical `Event` resource container containing the `udm` payload and an optional `name` identifier.  
  
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

Both endpoints return an empty confirmation payload upon successful receipt of the events.

Legacy field (`google.protobuf.Empty`) | Modern field (`ImportEventsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
— | — | `message` | **Equivalent:** Both APIs return an empty JSON object (`{}`) upon successful validation and queuing of the event batch.  
  
* * *

## Key differences

  * **Resource-scoped URL vs. global endpoint:**
    * Legacy `CreateUDMEvents` sent requests to `/v1/udmevents`, inferring tenant context from credentials.
    * Modern `ImportEvents` scopes requests explicitly under the Google Cloud resource hierarchy (`/v1/projects/{project}/locations/{location}/instances/{instance}/events:import`).
  * **Payload encapsulation (`oneof source` and `Event` container):**
    * Legacy `CreateUDMEventsRequest` accepted a raw list of `backstory.UDM` objects in the `events` array.
    * Modern `ImportEventsRequest` encapsulates the batch in an `inline_source` container (`EventsInlineSource`), wrapping each event in a `google.cloud.chronicle.v1main.Event` object that houses the `udm` payload alongside resource metadata.
  * **Modern IAM authorization:**
    * Authentication moves from legacy ingestion API keys or partner tokens to standard Google Cloud IAM OAuth 2.0 bearer tokens requiring `chronicle.googleapis.com/events.import`.
  * **Atomic all-or-nothing batch validation:**
    * Both legacy and modern APIs enforce atomic validation across the entire batch: all events in the request must be valid UDM structures. An error in any single event causes the entire import request to fail.
  * **Schema continuity:**
    * The underlying event definition remains the Universal Data Model (`backstory.UDM`), ensuring existing event generation and normalization logic requires no field transformation beyond packaging events into the `inline_source.events[].udm` structure.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
