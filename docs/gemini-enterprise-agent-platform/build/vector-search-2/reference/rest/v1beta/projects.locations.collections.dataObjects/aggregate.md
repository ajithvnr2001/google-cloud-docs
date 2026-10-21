---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/aggregate/
title: Method: projects.locations.collections.dataObjects.aggregate \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:15:08.637596+00:00
---

# Method: projects.locations.collections.dataObjects.aggregate  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/aggregate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  Method: projects.locations.collections.dataObjects.aggregate Stay organized with collections  Save and categorize content based on your preferences. 

Aggregates data objects.

### HTTP request

`POST https://vectorsearch.googleapis.com/v1beta/{parent}/dataObjects:aggregate`

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The resource name of the Collection for which to query. Format: `projects/{project}/locations/{location}/collections/{collection}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": {
        object
      },
      "aggregate": enum ([AggregationMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/aggregate#AggregationMethod))
    }  
  
Fields  
---  
`filter` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A JSON filter expression, e.g. {"genre": {"$eq": "sci-fi"}}, represented as a google.protobuf.Struct.  
`aggregate` |  `enum (`[AggregationMethod](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/aggregate#AggregationMethod)`)` Required. The aggregation method to apply to the query.  
  
### Response body

Response message for `[DataObjectSearchService.AggregateDataObjects](https://docs.cloud.google.com/gemini-enterprise-agent-platform/build/vector-search-2/reference/rest/v1beta/projects.locations.collections.dataObjects/aggregate#google.cloud.vectorsearch.v1beta.DataObjectSearchService.AggregateDataObjects)`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "aggregateResults": [
        {
          object
        }
      ]
    }  
  
Fields  
---  
`aggregateResults[]` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The aggregated results of the query.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `vectorsearch.dataObjects.query`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

## AggregationMethod

Aggregation methods.

Enums  
---  
`AGGREGATION_METHOD_UNSPECIFIED` | Should not be used.  
`COUNT` | Count the number of data objects that match the filter.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
