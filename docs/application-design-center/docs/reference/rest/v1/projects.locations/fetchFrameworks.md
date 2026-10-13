---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations/fetchFrameworks/
title: Method: projects.locations.fetchFrameworks \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:05.008569+00:00
---

# Method: projects.locations.fetchFrameworks  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations/fetchFrameworks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  Method: projects.locations.fetchFrameworks Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Fetches all frameworks for assessment report.

### HTTP request

`GET https://designcenter.googleapis.com/v1/{parent=projects/*/locations/*}:fetchFrameworks`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource name. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`projects[]` |  `string` Optional. Projects to fetch frameworks for. Format: projects/{project}  
`pageSize` |  `integer` Optional. The maximum number of results to return from this request. Non-positive values are ignored. The presence of nextPageToken in the response indicates that more results might be available.  
`pageToken` |  `string` Optional. If present, then retrieve the next batch of results from the preceding call to this method. pageToken must be the value of nextPageToken from the previous response. The values of other method parameters should be identical to those in the previous call.  
`filter` |  `string` Optional. Filter for frameworks list.  
  
### Request body

The request body must be empty.

### Response body

Response for locations.fetchFrameworks rpc

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "frameworks": [
        {
          object ([Framework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Framework))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`frameworks[]` |  `object (`[Framework](https://docs.cloud.google.com/application-design-center/docs/reference/rest/Shared.Types/Framework)`)` The list of frameworks.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `designcenter.locations.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
