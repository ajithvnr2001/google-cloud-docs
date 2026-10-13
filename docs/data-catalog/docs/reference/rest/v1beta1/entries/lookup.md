---
url: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/entries/lookup/
title: Method: entries.lookup \u00a0|\u00a0 Data Catalog Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:33:15.099603+00:00
---

# Method: entries.lookup  |  Data Catalog Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/entries/lookup/

Data Catalog API methods that are related to Data Catalog search and metadata are deprecated and will be discontinued on June 1, 2026. See [Transition from Data Catalog to Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/transition-to-dataplex-catalog). Methods that are related to policy tags and policy tag taxonomies are not deprecated. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Data Catalog ](https://docs.cloud.google.com/products)
  * [ Documentation ](https://docs.cloud.google.com/data-catalog/docs)
  * [ Reference ](https://docs.cloud.google.com/data-catalog/docs/reference)



Send feedback 

#  Method: entries.lookup Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Data Catalog is deprecated. Please use Dataplex Universal Catalog instead.

Get an entry by target resource name. This method allows clients to use the resource name from the source Google Cloud Platform service to get the Data Catalog Entry.

### HTTP request

`GET https://datacatalog.googleapis.com/v1beta1/entries:lookup`

### Query parameters

Parameters  
---  
Union parameter `target_name`. Required. Represents either the Google Cloud Platform resource or SQL name for a Google Cloud Platform resource. `target_name` can be only one of the following:  
`linkedResource` |  `string` The full name of the Google Cloud Platform resource the Data Catalog entry represents. See: <https://cloud.google.com/apis/design/resource_names#full_resource_name>. Full names are case-sensitive.Examples:

  * //bigquery.googleapis.com/projects/projectId/datasets/datasetId/tables/tableId
  * //pubsub.googleapis.com/projects/projectId/topics/topicId

  
`sqlResource` |  `string` The SQL name of the entry. SQL names are case-sensitive.Examples:

  * `pubsub.project_id.topic_id`
  * `pubsub.project_id.`topic.id.with.dots``
  * `bigquery.table.project_id.dataset_id.table_id`
  * `bigquery.dataset.project_id.dataset_id`
  * `datacatalog.entry.project_id.location_id.entry_group_id.entry_id`

`*_id`s should satisfy the GoogleSQL rules for identifiers. <https://cloud.google.com/bigquery/docs/reference/standard-sql/lexical>.  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Entry](https://docs.cloud.google.com/data-catalog/docs/reference/rest/v1beta1/projects.locations.entryGroups.entries#Entry)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-17 UTC."],[],[]] 
