---
url: https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.queryMetrics/fetch/
title: Method: projects.locations.queryMetrics.fetch \u00a0|\u00a0 Database Center Documentation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:51:30.809064+00:00
---

# Method: projects.locations.queryMetrics.fetch  |  Database Center Documentation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-center/docs/reference/databaseinsights/rest/v1beta/projects.locations.queryMetrics/fetch/

The Database Center REST and RPC APIs are in [Preview](https://docs.cloud.google.com/products#product-launch-stages). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Database Center ](https://docs.cloud.google.com/database-center/docs/overview)
  * [ Documentation ](https://docs.cloud.google.com/database-center/docs)
  * [ Reference ](https://docs.cloud.google.com/database-center/docs/reference)



Send feedback 

#  Method: projects.locations.queryMetrics.fetch Stay organized with collections  Save and categorize content based on your preferences. 

queryMetrics.fetch fetches the given database query level metrics.

### HTTP request

`POST https://databaseinsights.googleapis.com/v1beta/{parent=projects/*/locations/*}/queryMetrics:fetch`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The name of the location where we request metrics. Format: `projects/{project}/locations/{location}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "resource": string,
      "promqlQuery": string,
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`resource` |  `string` Required. The resource name used for query metrics. It is the project ID in this case.  
`promqlQuery` |  `string` Required. The promqlQuery to fetch the query metrics.  
`startTime` |  `string` Optional. The startTime of the metrics in RFC3339 format.  
`endTime` |  `string` Optional. The endTime of the metrics in RFC3339 format.  
  
### Response body

The response of the queryMetrics.fetch RPC.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "promqlResult": string
    }  
  
Fields  
---  
`promqlResult` |  `string` The result of the fetch query metrics.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `databaseinsights.queryMetrics.fetch`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
