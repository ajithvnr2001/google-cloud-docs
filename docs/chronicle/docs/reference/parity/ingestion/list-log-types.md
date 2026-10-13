---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/list-log-types/
title: ListLogTypes APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:56.632767+00:00
---

# ListLogTypes APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/list-log-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListLogTypes APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API (**`ListLogTypes`**) to the modern Chronicle API ([**`ListLogTypes`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes/list)).

> [!IMPORTANT] The modern `ListLogTypes` API requires standard Google Cloud IAM authentication authorized for the target instance resource. Legacy Ingestion API keys and partner tokens are not supported.

## Protocol and mapping overview

Feature | Legacy API (`ListLogTypes`) | Modern Chronicle API (`ListLogTypes`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/logTypes.list`  
  
* * *

## Request parameter field-by-field parity

In the legacy API, callers issued a parameterless `GET` request against `/v1/logtypes` to retrieve a global catalog of supported log types. In the modern Chronicle API, `ListLogTypes` is scoped to a specific Chronicle instance using the `parent` path parameter and supports standard AIP pagination, filtering, and sorting parameters.

Legacy field (`google.protobuf.Empty`) | Modern field (`ListLogTypesRequest`) | Parameter type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** Scopes the request to the target Chronicle instance: `projects/{project}/locations/{location}/instances/{instance}`.  
— | `page_size` | `int32` | **New pagination parameter:** Maximum number of log types to return in a single page.  
— | `page_token` | `string` | **New pagination parameter:** Page token returned by a prior `ListLogTypes` call to retrieve the next page of results.  
— | `filter` | `string` | **New filtering parameter:** AIP-160 filter expression to filter log types based on attributes (for example, filtering by display name or custom parser status).  
— | `order_by` | `string` | **New sorting parameter:** Order of returned log types (supports `data_size`, `data_size desc`, or name ascending by default).  
  
* * *

## Response payload field-by-field parity

The legacy API returned a list of `SupportedLogType` objects in a `SupportedLogTypes` container. The modern API returns a paginated list of canonical `LogType` resources in `ListLogTypesResponse`.

Legacy field (`SupportedLogTypes`) | Modern field (`ListLogTypesResponse`) | Field type | Parity and migration notes  
---|---|---|---  
`log_types` | `log_types` | `repeated LogType` | **Parity mapped to rich resource model:** List of log types available within the target Chronicle instance.  
— | `next_page_token` | `string` | **New pagination token:** Token used as `page_token` in subsequent requests to retrieve the next page. If omitted, no subsequent pages exist.  
  
* * *

### Log type entity structure parity (`SupportedLogType` versus `google.cloud.chronicle.v1main.LogType`)

Each item in `log_types` maps from the legacy `SupportedLogType` definition to the modern `LogType` resource schema:

Legacy field (`SupportedLogType`) | Modern field (`LogType`) | Field type | Parity and migration notes  
---|---|---|---  
`log_type` | `display_name` | `string` | **Direct mapping:** The log type tag/identifier used in YARA-L rules and search queries (for example, `WINEVTLOG`, `OKTA`, or `PAN_FIREWALL`).  
`description` | `product_source` | `string` | **Direct mapping:** Human-readable product or log source description presented in the console interface when configuring feeds.  
`index` | — | `int32` | **Deprecated:** Internal integer enum identifier. In the modern API, log types are addressed using canonical string resource names.  
— | `name` | `string` | **New field:** Canonical resource name of the log type (`projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}`).  
— | `custom_log_type_label` | `string` | **New field:** Custom log type label identifier if the log type is custom-defined.  
— | `golden` | `bool` | **New field:** Indicates whether the log type is a "Golden" log type supporting rapid customer onboarding.  
— | `is_custom` | `bool` | **New field:** Indicates whether the log type is tenant-specific (`true`) or globally available (`false`).  
— | `has_custom_parser` | `bool` | **New field:** Indicates whether a custom parser is bound to the log type.  
— | `parser_type` | `ParserType` | **New field:** Enum specifying the parser classification (`CUSTOM`, `PREBUILT`, or `PARSER_TYPE_UNSPECIFIED`).  
— | `feed_count` | `int32` | **New field:** Number of feeds configured for this log type within the instance.  
— | `last_ingested_time` | `google.protobuf.Timestamp` | **New telemetry field:** Timestamp when telemetry was most recently ingested for this log type.  
— | `collection_time` | `google.protobuf.Timestamp` | **New telemetry field:** Timestamp of the most recent collection event for this log type.  
  
* * *

## Key differences

  * **Global catalog vs. instance-scoped resource collection:**
    * Legacy `ListLogTypes` returned a static, global list of all log types supported across the entire Chronicle service.
    * Modern `ListLogTypes` scopes the query to an individual Chronicle instance (`parent`), returning log types along with customer-specific configurations (such as custom log types, feed associations, and ingestion activity).
  * **Standard Google Cloud pagination (AIP-158):**
    * Legacy `ListLogTypes` returned all items in a single response without pagination controls.
    * Modern `ListLogTypes` standardizes on `page_size` and `next_page_token`, improving response performance and reliability.
  * **Filtering and sorting capabilities (AIP-160):**
    * Modern `ListLogTypes` allows clients to filter log types (`filter`) and sort by lifetime ingestion volume (`order_by=data_size`).
  * **Instance runtime metadata:**
    * Modern `LogType` resources provide actionable operational metadata (`last_ingested_time`, `collection_time`, `feed_count`, `is_custom`, and `golden` status) that was not available in the legacy catalog.
  * **Modern IAM authorization:**
    * Authentication shifts from legacy ingestion API keys to standard Google Cloud IAM OAuth 2.0 bearer tokens with permission check `chronicle.googleapis.com/logTypes.list`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
