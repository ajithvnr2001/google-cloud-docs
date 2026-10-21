---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/queryMetrics/
title: Method: projects.locations.authorizedViewSets.authorizedViews.queryMetrics \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:46:01.132274+00:00
---

# Method: projects.locations.authorizedViewSets.authorizedViews.queryMetrics  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/queryMetrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.authorizedViewSets.authorizedViews.queryMetrics Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Query metrics.

### HTTP request

`POST https://{endpoint}/v1/{location=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}:queryMetrics`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`location` |  `string` Required. The location of the data. "projects/{project}/locations/{location}"  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
      "timeGranularity": enum ([TimeGranularity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/TimeGranularity)),
      "dimensions": [
        {
          object ([Dimension](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Dimension))
        }
      ],
      "measureMask": string
    }  
  
Fields  
---  
`filter` |  `string` Required. Filter to select a subset of conversations to compute the metrics. Must specify a window of the conversation create time to compute the metrics. The returned metrics will be from the range [DATE(starting create time), DATE(ending create time)).  
`timeGranularity` |  `enum (`[TimeGranularity](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/TimeGranularity)`)` The time granularity of each data point in the time series. Defaults to NONE if this field is unspecified.  
`dimensions[]` |  `object (`[Dimension](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/Dimension)`)` The dimensions that determine the grouping key for the query. Defaults to no dimension if this field is unspecified. If a dimension is specified, its key must also be specified. Each dimension's key must be unique.If a time granularity is also specified, metric values in the dimension will be bucketed by this granularity.Up to one dimension is supported for now.  
`measureMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Measures to return. Defaults to all measures if this field is unspecified. A valid mask should traverse from the `measure` field from the response. For example, a path from a measure mask to get the conversation count is "conversationMeasure.count".This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `location` resource:

  * `contactcenterinsights.authorizedConversations.list`
  * `contactcenterinsights.conversations.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
