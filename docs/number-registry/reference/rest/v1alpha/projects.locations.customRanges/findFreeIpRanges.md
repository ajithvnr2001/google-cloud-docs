---
url: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/findFreeIpRanges/
title: Method: projects.locations.customRanges.findFreeIpRanges \u00a0|\u00a0 Cloud Number Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:51:53.941913+00:00
---

# Method: projects.locations.customRanges.findFreeIpRanges  |  Cloud Number Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/findFreeIpRanges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Cloud Number Registry ](https://docs.cloud.google.com/number-registry)
  * [ Reference ](https://docs.cloud.google.com/number-registry/apis)



Send feedback 

#  Method: projects.locations.customRanges.findFreeIpRanges Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Finds free IP ranges in a single CustomRange.

### HTTP request

`GET https://cloudnumberregistry.googleapis.com/v1alpha/{name=projects/*/locations/*/customRanges/*}:findFreeIpRanges`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The resource name of the CustomRange to search within.  
  
### Query parameters

Parameters  
---  
`cidrPrefixLength` |  `integer` Required. The prefix length of the free IP ranges to find.  
`rangeCount` |  `integer` Optional. The number of free IP ranges to find.  
`requestId` |  `string` Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request.For example, consider a situation where you make an initial request and the request times out. If you make the request again with the same request ID, the server can check if original operation with the same request ID was received, and if so, will ignore the second request. This prevents clients from accidentally creating duplicate commitments.The request ID must be a valid UUID with the exception that zero UUID is not supported (00000000-0000-0000-0000-000000000000).  
  
### Request body

The request body must be empty.

### Response body

Response message for the `[CloudNumberRegistry.FindCustomRangeFreeIpRanges](https://docs.cloud.google.com/number-registry/reference/rest/v1alpha/projects.locations.customRanges/findFreeIpRanges#google.cloud.numberregistry.v1alpha.CloudNumberRegistry.FindCustomRangeFreeIpRanges)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "freeIpCidrRanges": [
        string
      ]
    }  
  
Fields  
---  
`freeIpCidrRanges[]` |  `string` Output only. The free IP CIDR ranges found.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `cloudnumberregistry.customRanges.get`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
