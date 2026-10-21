---
url: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/queryPerformanceOverview/
title: Method: projects.locations.authorizedViewSets.authorizedViews.queryPerformanceOverview \u00a0|\u00a0 Customer Experience Insights \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:46:01.034893+00:00
---

# Method: projects.locations.authorizedViewSets.authorizedViews.queryPerformanceOverview  |  Customer Experience Insights  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/projects.locations.authorizedViewSets.authorizedViews/queryPerformanceOverview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Customer Experience Insights ](https://docs.cloud.google.com/gemini-enterprise-cx/insights)



Send feedback 

#  Method: projects.locations.authorizedViewSets.authorizedViews.queryPerformanceOverview Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
    * JSON representation
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Try it!



Generates a summary of predefined performance metrics for a set of conversations. Conversations can be specified by specifying a time window and an agent id, for now. The summary includes a comparison of metrics computed for conversations in the previous time period, and also a comparison with peers in the same time period.

### HTTP request

`POST https://{endpoint}/v1/{parent=projects/*/locations/*/authorizedViewSets/*/authorizedViews/*}:queryPerformanceOverview`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource of the conversations to derive performance stats from. "projects/{project}/locations/{location}"  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "filter": string,
      "queryInterval": {
        object ([QueryInterval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/QueryInterval))
      },
    
      // Union field source can be only one of the following:
      "agentPerformanceSource": {
        object ([AgentSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AgentSource))
      }
      // End of list of possible types for union field source.
      "comparisonQueryInterval": {
        object ([QueryInterval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/QueryInterval))
      }
    }  
  
Fields  
---  
`filter` |  `string` Optional. Filter to select a subset of conversations to compute the performance overview. Supports the same filters as the filter field in QueryMetricsRequest. The source and query interval/comparison query interval should not be included here.  
`queryInterval` |  `object (`[QueryInterval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/QueryInterval)`)` Required. The time window of the conversations to derive performance stats from.  
Union field `source`. The type of source of conversations to derive performance from. `source` can be only one of the following:  
`agentPerformanceSource` |  `object (`[AgentSource](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/AgentSource)`)` Conversations are from a single agent.  
`comparisonQueryInterval` |  `object (`[QueryInterval](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/v1/QueryInterval)`)` The time window of the conversations to compare the performance to.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/gemini-enterprise-cx/insights/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permissions on the `parent` resource:

  * `contactcenterinsights.authorizedConversations.list`
  * `contactcenterinsights.conversations.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
