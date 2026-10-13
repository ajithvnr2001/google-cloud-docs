---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/get-data-tap/
title: GetDataTap parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:23.337880+00:00
---

# GetDataTap parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/datatap/get-data-tap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetDataTap parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Data Tap API (**`GetDataTap`**) to the modern Chronicle API (**`GetDataTap`**).

## Protocol and mapping overview

Feature | Legacy API (`GetDataTap`) | Modern Chronicle API (`GetDataTap`)  
---|---|---  
**HTTP Method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/dataTaps.get`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `GetDataTapRequest` targets resources using Google Cloud resource name paths.

Legacy Field (`GetDataTapRequest`) | Modern Field (`GetDataTapRequest`) | Field type | Parity & Migration Notes  
---|---|---|---  
`name` | `name` _(in HTTP path)_ | `string` | **Google Cloud Scoping Context:** The legacy request used path format `dataTaps/<tap_id>`. The modern API routes this using the standard Google Cloud resource tree structure: `projects/{project}/locations/{region}/instances/{instance}/dataTaps/{id}`.  
  
* * *

## Response payload field-by-field parity

Both responses return the retrieved `DataTap` representation.

Legacy Field (`DataTap` response) | Modern Field (`DataTap` response) | Field type | Parity & Migration Notes  
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

  * **Google Cloud Project Scoping Integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Resource Path Renaming:**
    * Legacy path formats `dataTaps/<id>` are migrated to standard Google Cloud path parameters `projects/*/locations/*/instances/*/dataTaps/<id>`.
  * **Serialization Format Enums:**
    * The value to request JSON formatted events outputs changed from `JSON` (Legacy) to `JSON_OBJECT` (Modern).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
