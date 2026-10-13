---
url: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/list-feed-source-type-schemas/
title: ListFeedSourceTypeSchemas parity mapping \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:35:54.629900+00:00
---

# ListFeedSourceTypeSchemas parity mapping  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reference/parity/feeds/list-feed-source-type-schemas/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Reference ](https://docs.cloud.google.com/chronicle/docs/reference/google-secops-api-libraries-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ListFeedSourceTypeSchemas parity mapping

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

This guide details the request and response mapping specifications and property parity analysis for migrating from the legacy Backstory Feed Management API (**`ListFeedSourceTypeSchemas`**) to the modern Chronicle API (**`ListFeedSourceTypeSchemas`**).

## Protocol and mapping overview

Feature | Legacy API (`ListFeedSourceTypeSchemas`) | Modern Chronicle API (`ListFeedSourceTypeSchemas`)  
---|---|---  
**HTTP method** | `GET` | `GET`  
**Permissions** | Partner token or legacy API keys | `chronicle.googleapis.com/feedSourceTypeSchemas.list`  
  
* * *

## Request payload field-by-field parity

The modern Chronicle API `ListFeedSourceTypeSchemasRequest` requires parent scoping.

Legacy field (`ListFeedSourceTypeSchemasRequest`) | Modern field (`ListFeedSourceTypeSchemasRequest`) | Field type | Parity and migration notes  
---|---|---|---  
— | `parent` _(in HTTP path)_ | `string` | **Google Cloud scoping context:** Scopes the list target under parent projects using the standard resource name path in the URL. Pattern: `projects/{project}/locations/{location}/instances/{instance_uuid}`.  
`page_size` | `page_size` | `int32` | **Parity mapped:** Pagination page size limits. Rename to `pageSize` in JSON payloads.  
`page_token` | `page_token` | `string` | **Parity mapped:** Paging resumption token. Rename to `pageToken` in JSON payloads.  
  
* * *

## Response payload field-by-field parity

Both the legacy Backstory Feed Management API (`ListFeedSourceTypeSchemas`) and the modern Chronicle API (`ListFeedSourceTypeSchemas`) return pagination results with matching schema models.

Legacy field (`ListFeedSourceTypeSchemasResponse` message) | Modern field (`ListFeedSourceTypeSchemasResponse` message) | Field type | Parity and migration notes  
---|---|---|---  
`feed_source_type_schemas` | `feed_source_type_schemas` | `repeated FeedSourceTypeSchema` | **Parity mapped:** Array list of feed source type schema definitions. Rename to `feedSourceTypeSchemas` in JSON.  
`next_page_token` | `next_page_token` | `string` | **Parity mapped:** Next page resumption token. Rename to `nextPageToken` in JSON.  
  
### Nested FeedSourceTypeSchema field parity

The fields mapping inside individual FeedSourceTypeSchema items is as follows:

Legacy field (`FeedSourceTypeSchema` message) | Modern field (`FeedSourceTypeSchema` message) | Field type | Parity and migration notes  
---|---|---|---  
`name` | `name` | `string` | **Parity mapped:** Contains standard Google Cloud canonical resource path: `projects/{pr}/locations/{loc}/instances/{in}/feedSourceTypeSchemas/{feed_source_type}`.  
`display_name` | `display_name` | `string` | Rename to `displayName` in JSON responses.  
`description` | `description` | `string` | Human-readable description.  
`read_only` | `read_only` | `bool` | Rename to `readOnly` in JSON. Note tag number shifted from 6 (legacy) to 4 (modern).  
`feed_source_type` | `feed_source_type` | `enum` | Direct enum mapping to `FeedDetails.FeedSourceType`. Note tag number shifted from 4 (legacy) to 5 (modern).  
`log_type_schemas` | — | — | **Removed:** In modern Chronicle APIs, log type schemas are decoupled and queried separately using `ListLogTypeSchemas`.  
  
* * *

## Key differences between the Backstory and Chronicle APIs

  * **Google Cloud project scoping integration:**
    * Scoped natively under parent project instance folder bindings.
  * **Schema decoupling:**
    * In legacy backstory, `FeedSourceTypeSchema` contained an empty or attenuated repeated `LogTypeSchema` `log_type_schemas` field. In the modern API, this nested field is removed entirely; log type schemas must be retrieved independently using `ListLogTypeSchemas`.
  * **Tag number shifts:**
    * Within protobuf formatting, tag numbers inside `FeedSourceTypeSchema` shifted (`read_only` moved from 6 to 4; `feed_source_type` moved from 4 to 5).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
