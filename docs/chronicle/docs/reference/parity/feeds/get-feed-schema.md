---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/get-feed-schema/
title: GetFeedSchema parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:07:25.969988+00:00
---

# GetFeedSchema parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/get-feed-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# GetFeedSchema parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Feed Management API (**`GetFeedSchema`**) to the modern Chronicle API (**`ListLogTypeSchemas`**).

## Protocol and mapping overview

Feature | Legacy API (`GetFeedSchema`) | Modern Chronicle API (`ListLogTypeSchemas`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/logTypeSchemas.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListLogTypeSchemasRequest` replaces global dumps by querying log schemas scoped under a specific parent feed source type.

Legacy field (`GetFeedSchemaRequest`) | Modern field (`ListLogTypeSchemasRequest`) | Field type | Parity and migration notes  
---|---|---|---  
`name` _(in HTTP path)_ | `parent` _(in HTTP path)_ | `string` | **GCP scoping / granularity shift:** Legacy passed the global string `feedSchema` to dump all schemas at once. Modern requests scope log schemas under specific source types: `projects/{project}/locations/{location}/instances/{instance}/feedSourceTypeSchemas/{source_type}`.  
— | `page_size` | `int32` | **New parameter:** Configures pagination size limits (default 5000, max 10000). Rename to `pageSize` in JSON.  
— | `page_token` | `string` | **New parameter:** Token to resume schema pagination. Rename to `pageToken` in JSON.  
  
* * *

## Response payload field-by-field parity

Both the legacy Backstory Feed Management API (`GetFeedSchema`) and the modern Chronicle API (`ListLogTypeSchemas`) return schema structures, with the modern Chronicle API returning granular, paginated log type definitions.

Legacy field (`FeedSchema` message) | Modern field (`ListLogTypeSchemasResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`feed_source_type_schemas[].log_type_schemas` | `log_type_schemas` | `repeated LogTypeSchema` | **Parity mapped / restructured:** Mapped from the nested `log_type_schemas` inside the global legacy schema to the root repeated list `log_type_schemas` on the response.  
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

  * **Granular query architecture:**
    * Legacy `GetFeedSchema` returned a monolithic, global dump of all feed source types and log types in one unpaginated payload.
    * Modern Chronicle API implements granular querying (`ListLogTypeSchemas`), allowing clients to fetch log schemas scoped specifically to a target `feed_source_type`.
  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Pagination support:**
    * Introduces `page_size`, `page_token`, and `next_page_token` to handle large schema dictionaries reliably without timeout truncation.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
