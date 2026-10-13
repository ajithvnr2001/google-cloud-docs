---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/get-log-type-schema/
title: GetLogTypeSchema parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:27.946508+00:00
---

# GetLogTypeSchema parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/get-log-type-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetLogTypeSchema parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Feed Management API (**`GetLogTypeSchema`**) to the modern Chronicle API (**`ListLogTypeSchemas`**).

## Protocol and mapping overview

Feature | Legacy API (`GetLogTypeSchema`) | Modern Chronicle API (`ListLogTypeSchemas`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/logTypeSchemas.list`  
  
* * *

## Request payload field-by-field parity

Because the standalone `GetLogTypeSchema` method was retired in the Chronicle API, clients must invoke `ListLogTypeSchemas` targeting the parent source type and select the log type locally from the returned array.

Legacy field (`GetLogTypeSchemaRequest`) | Modern field (`ListLogTypeSchemasRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`name` _(in HTTP path)_ | `parent` _(in HTTP path)_ | `string` | **GCP scoping / architectural shift:** The legacy request specified the direct child schema path `feedSourceTypeSchemas/{source_type}/logTypeSchemas/{log_type}`. Because there is no standalone `GetLogTypeSchema` method in the modern Chronicle API, clients must invoke `ListLogTypeSchemas` targeting the parent source type path: `projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{source_type}`, and then filter the returned list for the target `{log_type}`.  
— | `page_size` | `int32` | **New parameter:** Configures pagination size limits (default 5000, max 10000). Rename to `pageSize` in JSON.  
— | `page_token` | `string` | **New parameter:** Token to resume schema pagination. Rename to `pageToken` in JSON.  
  
* * *

## Response payload field-by-field parity

In the legacy Backstory Feed Management API (`GetLogTypeSchema`), a single `LogTypeSchema` object was returned directly as the root response. In the modern Chronicle API (`ListLogTypeSchemas`), the response returns a repeated list of schemas (`ListLogTypeSchemasResponse`).

Legacy field (`FeedSchema.LogTypeSchema` root) | Modern field (`ListLogTypeSchemasResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`FeedSchema.LogTypeSchema` _(Root object)_ | `log_type_schemas[]` | `repeated LogTypeSchema` | **Restructured:** Instead of returning a single root schema object, the modern API returns a repeated list `log_type_schemas`. The client extracts the target log type schema from this array where `log_type` matches the requested schema.  
— | `next_page_token` | `string` | **New parameter:** Token to retrieve subsequent pages of schemas. Rename to `nextPageToken` in JSON.  
  
### Nested LogTypeSchema field parity

The fields mapping inside individual LogTypeSchema definitions is as follows:

Legacy field (`FeedSchema.LogTypeSchema`) | Modern field (`LogTypeSchema` message) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` | `string` | Contains canonical Google Cloud resource path: `projects/{pr}/locations/{loc}/instances/{in}/feedSourceTypeSchemas/{st}/logTypeSchemas/{log_type}`.  
`display_name` | `display_name` | `string` | Rename to `displayName` in JSON responses.  
`log_type` | `log_type` | `string` | Rename to `logType` in JSON responses.  
`read_only` | `read_only` | `bool` | Rename to `readOnly` in JSON.  
`supporting_documentation` | `supporting_documentation` | `string` | Rename to `supportingDocumentation` in JSON.  
`details_field_schemas` | `details_field_schemas` | `repeated DetailsFieldSchema` | Direct mapping of compatible field properties. Rename to `detailsFieldSchemas` in JSON.  
`details_field_schema_alternatives` | `details_field_schema_alternatives` | `repeated DetailsFieldSchemaAlternative` | Direct mapping of alternative schema sets. Rename to `detailsFieldSchemaAlternatives` in JSON.  
  
* * *

## Key differences between the Backstory and Chronicle APIs

  * **Method consolidation and architectural shift:**
    * In legacy backstory, clients could perform direct lookup of an individual log type schema using `GetLogTypeSchema`.
    * In the modern Chronicle API, standalone `GET` lookups for single log type schemas were retired in favor of the unified `ListLogTypeSchemas` list endpoint. Clients query all schemas for the parent `feed_source_type` and select the schema locally.
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Pagination support:**
    * Introduces `page_size`, `page_token`, and `next_page_token` on the list container response.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
