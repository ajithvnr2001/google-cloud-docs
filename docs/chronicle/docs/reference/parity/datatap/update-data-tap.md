---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/update-data-tap/
title: UpdateDataTap parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:06.567240+00:00
---

# UpdateDataTap parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/update-data-tap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# UpdateDataTap parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Data Tap API (**`UpdateDataTap`**) to the modern Chronicle API (**`UpdateDataTap`**).

## Protocol and mapping overview

Feature | Legacy API (`UpdateDataTap`) | Modern Chronicle API (`UpdateDataTap`)  
---|---|---  
**HTTP Method** | `PATCH` | `PATCH`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/dataTaps.update`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `UpdateDataTapRequest` targets resources using Google Cloud resource name paths and enforces `PATCH` partial updates using a field mask.

Legacy Field (`UpdateDataTapRequest` / `DataTap`) | Modern Field (`UpdateDataTapRequest` / `DataTap`) | Field type | Parity & Migration Notes  
---|---|---|---  
`data_tap.name` | `data_tap.name` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context:** The legacy request used path format `dataTaps/<tap_id>`. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{region}/instances/{instance}/dataTaps/{id}`.  
`data_tap.display_name` | `data_tap.display_name` | `string` | **Parity Mapped:** Display name of the data tap. Rename to `displayName` in JSON payloads.  
`data_tap.cloud_pubsub_sink` | `data_tap.cloud_pubsub_sink` | `Message` | **Parity Mapped:** Sink options configuration. Rename to `cloudPubsubSink` in JSON payloads. Sub-field topic maps directly.  
`data_tap.filter` | `data_tap.filter` | `enum` | **Parity Mapped:** Target filter type (for example, `ALL_UDM_EVENTS`, `ALERT_UDM_EVENTS`, `LABELED_UDM_EVENTS`).  
`data_tap.serialization_format` | `data_tap.serialization_format` | `enum` | **Value Translation:** Rename to `serializationFormat` in JSON. Mapped as follows:  
• `MARSHALLED_PROTO` → `MARSHALLED_PROTO`  
• `JSON` (Legacy) → `JSON_OBJECT` (Modern).  
— | `update_mask` | `FieldMask` | **New Parameter:** Standard FieldMask selects which properties are modified in the `PATCH` request (must include the target fields, for example, `display_name`).  
`data_tap.customer_id` | — | — | **Removed:** Scopes are derived implicitly from request location path.  
`data_tap.tap_id` | — | — | **Removed:** Output only.  
  
* * *

## Response payload field-by-field parity

Both responses return the modified `DataTap` message representation.

Legacy Field (`DataTap` message) | Modern Field (`DataTap` message) | Field type | Parity & Migration Notes  
---|---|---|---  
`name` | `name` | `string` | **Parity Mapped:** Contains the standard canonical resource path: `projects/{project}/locations/{location}/instances/{instances}/dataTaps/{id}`.  
`display_name` | `display_name` | `string` | Rename to `displayName` in JSON responses.  
`cloud_pubsub_sink` | `cloud_pubsub_sink` | `Message` | Rename to `cloudPubsubSink` in JSON responses. Sub-field topic maps directly.  
`filter` | `filter` | `enum` | Direct enum mappings.  
`serialization_format` | `serialization_format` | `enum` | Mapped with value translation: `JSON` (Legacy) → `JSON_OBJECT` (Modern). Rename to `serializationFormat` in JSON responses.  
`customer_id` | — | — | **Removed:** Embedded within parent path of `name`.  
`tap_id` | — | — | **Removed:** Equivalent to the final resource ID segment of the `name` path.  
  
* * *

## Key differences

  * **PATCH Semantics and Field Masking:**
    * The legacy backstory API performed full-resource updates. The modern Chronicle API uses standard gRPC partial `PATCH` requests with a `FieldMask` to select which properties are updated.
  * **Serialization Format Enums:**
    * The value to request JSON formatted events outputs changed from `JSON` (Legacy) to `JSON_OBJECT` (Modern).
  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
