---
url: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/exportAnalyticsMetrics/
title: Method: projects.locations.catalogs.exportAnalyticsMetrics \u00a0|\u00a0 AI Commerce Search in Gemini Enterprise for Customer Experience \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:39:24.217421+00:00
---

# Method: projects.locations.catalogs.exportAnalyticsMetrics  |  AI Commerce Search in Gemini Enterprise for Customer Experience  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/projects.locations.catalogs/exportAnalyticsMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ AI Commerce Search ](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search)



Send feedback 

#  Method: projects.locations.catalogs.exportAnalyticsMetrics Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Exports analytics metrics.

`Operation.response` is of type `ExportAnalyticsMetricsResponse`. `Operation.metadata` is of type `ExportMetadata`.

### HTTP request

`POST https://retail.googleapis.com/v2beta/{catalog=projects/*/locations/*/catalogs/*}:exportAnalyticsMetrics`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`catalog` |  `string` Required. Full resource name of the parent catalog. Expected format: `projects/*/locations/*/catalogs/*`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "outputConfig": {
        object ([OutputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/OutputConfig))
      },
      "filter": string
    }  
  
Fields  
---  
`outputConfig` |  `object (`[OutputConfig](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/v2beta/OutputConfig)`)` Required. The output location of the data. Only `bigqueryDestination` is supported, and `bigqueryDestination.table_type` must be set to `view`.  
`filter` |  `string` A filtering expression to specify restrictions on returned metrics. The expression is a sequence of terms. Each term applies a restriction to the returned metrics. Use this expression to restrict results to a specific time range.Currently we expect only one types of fields:

  * `timestamp`: This can be specified twice, once with a less than operator and once with a greater than operator. The `timestamp` restriction should result in one, contiguous, valid, `timestamp` range.

Some examples of valid filters expressions:

  * Example 1: `timestamp > "2012-04-23T18:25:43.511Z" timestamp < "2012-04-23T18:30:43.511Z"`
  * Example 2: `timestamp > "2012-04-23T18:25:43.511Z"`

  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/ai-commerce-search/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `catalog` resource:

  * `retail.catalogs.exportAnalyticsMetrics`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-08 UTC."],[],[]] 
