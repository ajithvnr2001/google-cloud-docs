---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/update-log-type/
title: PutLog to UpdateLogType APIs request and response mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:36:11.045437+00:00
---

# PutLog to UpdateLogType APIs request and response mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/update-log-type/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# PutLog to UpdateLogType APIs request and response mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Ingestion API (**`PutLog`**) to the modern Chronicle API ([**`UpdateLogType`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes/patch)).

> [!IMPORTANT] The modern `UpdateLogType` API requires standard Google Cloud IAM authentication authorized for the target instance and log type resources. Legacy Ingestion API keys and partner tokens are not accepted.

## Protocol and mapping overview

Feature | Legacy API (`PutLog`) | Modern Chronicle API (`UpdateLogType`)  
---|---|---  
**HTTP method** | `POST` | `PATCH`  
**Permissions** | Ingestion API key or legacy partner tokens | `chronicle.googleapis.com/logTypes.update`  
  
* * *

## Architectural evolution and separation of concerns

In the legacy Ingestion API, `PutLog` coupled raw log streaming with implicit log type registration and parser hints inside a procedural `LogEntryBatch` container. 

In the modern Chronicle API, data ingestion and log type lifecycle management are cleanly decoupled into dedicated AIP-compliant services:

  1. **Log data ingestion:** Streaming raw and unstructured logs is handled by [**`ImportLogs`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1/projects.locations.instances.logTypes.logs/import) (`POST /v1/{parent}/logs:import`), covered in the [`ImportLogs` parity guide](https://docs.cloud.google.com/chronicle/docs/reference/parity/ingestion/import-logs).
  2. **Log type configuration:** Managing log type definitions, display metadata, parser bindings, and UI configurations is handled by [**`UpdateLogType`**](https://docs.cloud.google.com/chronicle/docs/reference/rest/v1alpha/projects.locations.instances.logTypes/patch) (`PATCH /v1alpha/{log_type.name}`).



* * *

## Request payload field-by-field parity

The following table maps the configuration attributes from the legacy `PutLogRequest.batch` payload to the modern `UpdateLogTypeRequest` structure:

Legacy field (`PutLogRequest.batch`) | Modern field (`UpdateLogTypeRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`source.customer_id` | `log_type.name` _(in HTTP path)_ | `string` | **Google Cloud scoping hierarchy:** In the legacy API, customer identification was passed inside `source.customer_id` or resolved using API key. In the modern API, instance ownership is defined in the resource path: `projects/{project}/locations/{location}/instances/{instance}/logTypes/{log_type}`.  
`log_type` / `type` | `log_type.name` / `log_type.display_name` | `string` | **Direct mapping:** The log type identifier is bound as the final segment of `log_type.name` and represented by `log_type.display_name` for rule and query tagging.  
`hint` | _(Parser management)_ | `string` | **Separated into parser configuration:** In the legacy API, an opaque hint string was passed alongside log batches. In the modern API, parsing rules are configured through dedicated parser management or passed as `hint` during log ingestion with `ImportLogs`.  
`entries` | _(Ingestion separation)_ | `repeated LogEntry` | **Decoupled to`ImportLogs`:** Raw log entries are no longer transmitted using log type management calls; callers stream telemetry using `ImportLogs`.  
— | `update_mask` | `google.protobuf.FieldMask` | **New standard patch parameter:** Standard AIP-134 field mask specifying the exact fields to update (for example, `display_name` or `product_source`). If omitted, all non-empty fields in `log_type` are updated.  
— | `log_type.product_source` | `string` | **New field:** UI product source description displayed when configuring feeds.  
— | `log_type.is_custom` | `bool` | **New field:** Identifies whether the log type is custom to the customer tenant.  
— | `log_type.has_custom_parser` | `bool` | **New field:** Indicates whether a custom CBN parser is bound to the log type.  
— | `log_type.parser_type` | `ParserType` | **New field:** Classification of the parser assigned to this log type (`CUSTOM`, `PREBUILT`).  
  
* * *

## Response payload field-by-field parity

The legacy API returned an empty confirmation message. The modern API returns the full updated `LogType` resource.

Legacy field (`PutLogResponse`) | Modern field (`LogType`) | Field type | Parity and migration notes  
---|---|---|---  
— | `name` | `string` | **New field:** Full canonical resource name of the updated log type.  
— | `display_name` | `string` | **New field:** Updated display name of the log type.  
— | `product_source` | `string` | **New field:** Updated product source label.  
— | `is_custom` | `bool` | **New field:** Indicates whether the log type is custom.  
— | `parser_type` | `ParserType` | **New field:** Active parser type bound to the log type.  
— | `last_ingested_time` | `google.protobuf.Timestamp` | **New field:** Timestamp when logs were last ingested for this log type.  
— | `feed_count` | `int32` | **New field:** Number of active feeds associated with the log type.  
  
* * *

## Key differences

  * **Decoupling ingestion from configuration:**
    * Legacy `PutLog` combined log streaming and log type registration into a single endpoint.
    * Modern Chronicle cleanly separates data plane ingestion (`ImportLogs`) from control plane log type configuration (`UpdateLogType`).
  * **Standard RESTful PATCH semantics (AIP-134):**
    * Legacy `PutLog` utilized a custom `POST /v1/log:put` method.
    * Modern `UpdateLogType` follows standard Google Cloud API guidelines, using `PATCH` semantics with a `FieldMask` (`update_mask`) to allow selective updates without risking accidental attribute erasure.
  * **Rich resource state returned in response:**
    * Legacy `PutLog` returned an empty object (`{}`).
    * Modern `UpdateLogType` returns the complete updated `LogType` resource, including ingestion status (`last_ingested_time`), feed associations (`feed_count`), and parser metadata.
  * **Modern IAM authorization:**
    * Authentication shifts from legacy Ingestion API keys to standard Google Cloud IAM OAuth 2.0 bearer tokens requiring `chronicle.googleapis.com/logTypes.update`.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
