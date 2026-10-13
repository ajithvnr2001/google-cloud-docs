---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/list-log-type-schemas/
title: ListLogTypeSchemas parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:56.107897+00:00
---

# ListLogTypeSchemas parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/list-log-type-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListLogTypeSchemas parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Feed Management API (**`ListLogTypeSchemas`**) to the modern Chronicle API (**`ListLogTypeSchemas`**).

## Protocol and mapping overview

Feature | Legacy API (`ListLogTypeSchemas`) | Modern Chronicle API (`ListLogTypeSchemas`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/logTypeSchemas.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListLogTypeSchemasRequest` requires parent scoping.

Legacy field (`ListLogTypeSchemasRequest`) | Modern field (`ListLogTypeSchemasRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`parent` _(in HTTP path)_ | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes the target under standard parent project instance folder bindings. Pattern: `projects/{project}/locations/{location}/instances/{instance_uuid}/feedSourceTypeSchemas/{feed_source_type}`.  
`page_size` | `page_size` | `int32` | **Parity mapped:** Pagination page size limits (default 5000, max 10000). Rename to `pageSize` in JSON payloads.  
`page_token` | `page_token` | `string` | **Parity mapped:** Paging resumption token. Rename to `pageToken` in JSON payloads.  
  
* * *

## Response payload field-by-field parity

Both the legacy Backstory Feed Management API (`ListLogTypeSchemas`) and the modern Chronicle API (`ListLogTypeSchemas`) return pagination results with matching schema models. In the modern Chronicle API, returned log schemas are fully populated with field definitions.

Legacy field (`ListLogTypeSchemasResponse` message) | Modern field (`ListLogTypeSchemasResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`log_type_schemas` | `log_type_schemas` | `repeated LogTypeSchema` | **Parity mapped / enriched:** Array list of log type schema definitions. In the modern API, this returns full schemas including details field alternatives. Rename to `logTypeSchemas` in JSON.  
`next_page_token` | `next_page_token` | `string` | **Parity mapped:** Next page resumption token. Rename to `nextPageToken` in JSON.  
  
### Nested LogTypeSchema field parity

The fields mapping inside individual LogTypeSchema items is as follows:

Legacy field (`FeedSchema.LogTypeSchema` message) | Modern field (`LogTypeSchema` message) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` | `string` | Contains canonical Google Cloud resource path: `projects/{pr}/locations/{loc}/instances/{in}/feedSourceTypeSchemas/{st}/logTypeSchemas/{log_type}`.  
`display_name` | `display_name` | `string` | Rename to `displayName` in JSON responses.  
`log_type` | `log_type` | `string` | Rename to `logType` in JSON responses.  
`read_only` | `read_only` | `bool` | Rename to `readOnly` in JSON.  
`supporting_documentation` | `supporting_documentation` | `string` | Rename to `supportingDocumentation` in JSON.  
`details_field_schemas` | `details_field_schemas` | `repeated DetailsFieldSchema` | Direct mapping of compatible field properties. In legacy list responses, this was empty/attenuated; in modern list responses, it is fully populated. Rename to `detailsFieldSchemas` in JSON.  
`details_field_schema_alternatives` | `details_field_schema_alternatives` | `repeated DetailsFieldSchemaAlternative` | Direct mapping of alternative schema sets. In legacy list responses, this was empty/attenuated; in modern list responses, it is fully populated. Rename to `detailsFieldSchemaAlternatives` in JSON.  
  
* * *

## Key differences between the Backstory and Chronicle APIs

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Full vs. attenuated schema returns:**
    * In legacy backstory, `ListLogTypeSchemas` returned attenuated schemas (with empty field definitions), requiring a secondary call to `GetLogTypeSchema` to get details. In the modern Chronicle API, because `GetLogTypeSchema` was retired, `ListLogTypeSchemas` returns full, comprehensive schema descriptions directly.
  * **Explicit paging token behavior:**
    * The Chronicle API provides standard Google Cloud paging checkpoint logic.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
