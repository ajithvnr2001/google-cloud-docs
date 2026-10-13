---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/list-supported-log-types/
title: ListSupportedLogTypes to ListLogTypeSettings APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:55.481324+00:00
---

# ListSupportedLogTypes to ListLogTypeSettings APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/list-supported-log-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListSupportedLogTypes to ListLogTypeSettings APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API v2 (**`ListSupportedLogTypes`**) to the modern Chronicle API ([**`ListLogTypeSettings`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.logTypeSettings/list)).

> [!IMPORTANT] The modern `ListLogTypeSettings` API does not accept legacy Ingestion API keys or partner tokens. Callers must authenticate using standard Google Cloud IAM credentials authorized with `chronicle.googleapis.com/logTypeSettings.list` for the target instance resource.

## Protocol and mapping overview

Feature | Legacy API v2 (`ListSupportedLogTypes`) | Modern Chronicle API (`ListLogTypeSettings`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/logTypeSettings.list`  
  
* * *

## Request payload field-by-field parity

In the legacy Ingestion API v2, `ListSupportedLogTypes` was an unparameterized global `GET` endpoint returning a static enumeration of supported log types.

In the modern Chronicle API, log type configuration is queried through `ListLogTypeSettingsRequest`. Callers specify the parent instance and log type collection in the URL path, with support for the `-` wildcard to list settings across all log types within the instance, alongside standard pagination controls.

Legacy field (`ListSupportedLogTypesRequest`) | Modern field (`ListLogTypeSettingsRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In legacy v2, `/v2/logtypes` was a global unparameterized endpoint. In the modern API, the parent collection path is required in the URL: `projects/{project}/locations/{location}/instances/{instance}/logTypes/-/logTypeSettings` (using `-` wildcard to list settings across all log types) or `.../logTypes/{log_type}/logTypeSettings` for a specific log type.  
— | `page_size` | `int32` | **Standardized pagination:** Maximum number of setting records to return in a single page.  
— | `page_token` | `string` | **Standardized pagination:** Continuation token for retrieving the subsequent page of settings.  
  
* * *

## Response payload field-by-field parity

In legacy v2, the response contained a flat list of `SupportedLogType` records. In the modern API, the response returns `LogTypeSetting` resources that represent instance-level parser extraction and deduplication configurations.

Legacy field (`ListSupportedLogTypesResponse`) | Modern field (`ListLogTypeSettingsResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`log_types` | `log_type_settings` | `repeated LogTypeSetting` | **Shift from static catalogue to instance configuration:** Legacy v2 returned static log type descriptors (`SupportedLogType`). Modern `ListLogTypeSettings` returns `LogTypeSetting` resources containing instance-specific parsing and extraction controls for each log type.  
`log_types[].log_type` | `log_type_settings[].name` | `string` | **Resource naming:** In legacy v2, the raw log type string (such as `OKTA` or `WINEVTLOG`) was returned. In the modern API, the log type is embedded in the canonical resource name: `projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}/logTypeSetting`.  
`log_types[].description` | — | `string` | **Managed in`LogType` resource:** Descriptive metadata and product labels are available using `LogType.product_source` and `LogType.display_name` through the [**`ListLogTypes`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes/list) API.  
`log_types[].index` | — | `int32` | **Deprecated:** Internal protobuf enum indexes are deprecated in favor of canonical string resource identifiers.  
— | `log_type_settings[].autonomous_parsing_dedupe_enabled` | `bool` | **New setting:** Controls whether key-value pairs present in extracted fields are deduplicated if already populated in UDM.  
— | `log_type_settings[].autonomous_parsing_extraction_type` | `ExtractionType` enum | **New setting:** Autonomous parsing extraction mode (`ALL_FIELDS`, `OPT_IN`, `DISABLED`).  
— | `log_type_settings[].autonomous_parsing_max_optin_fields` | `int32` | **New setting:** Maximum number of fields eligible for opt-in autonomous parsing.  
— | `log_type_settings[].autonomous_parsing_max_array_elements` | `int32` | **New setting:** Maximum number of elements extracted from array fields.  
— | `next_page_token` | `string` | **Standardized pagination:** Continuation token returned when additional setting records exist.  
  
* * *

## Key differences

  * **Global catalog discovery vs. instance configuration settings:**
    * Legacy `ListSupportedLogTypes` served as a global catalog for discovering which log type strings were supported by the legacy Ingestion API.
    * In the modern Chronicle API:
    * To discover supported log types and parser availability, callers use [**`ListLogTypes`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes/list) or [**`SearchLogTypes`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes/search).
    * `ListLogTypeSettings` specifically queries and manages parsing behavior and extraction rules for log types within a given customer instance.
  * **Instance-level resource scoping:**
    * Legacy v2 requests were global (`/v2/logtypes`) and returned identical responses regardless of the calling customer.
    * Modern `ListLogTypeSettings` requires an explicit instance path (`/v1/projects/{project}/locations/{location}/instances/{instance}/logTypes/-/logTypeSettings`), reflecting instance-specific configuration.
  * **AIP-158 pagination support:**
    * Legacy v2 returned an unbounded, unpaginated array.
    * Modern Chronicle API implements standard cursor pagination using `page_size`, `page_token`, and `next_page_token`.
  * **Modern IAM authorization:**
    * Authentication transitions from legacy Ingestion API keys to standard Google Cloud IAM credentials requiring `chronicle.googleapis.com/logTypeSettings.list`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
