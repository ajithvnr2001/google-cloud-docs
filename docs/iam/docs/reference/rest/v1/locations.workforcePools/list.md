---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/list/
title: Method: locations.workforcePools.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:44.666004+00:00
---

# Method: locations.workforcePools.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: locations.workforcePools.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all non-deleted `[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`s under the specified parent. If `showDeleted` is set to `true`, then deleted pools are also listed.

### HTTP request

`GET https://iam.googleapis.com/v1/{location=locations/*}/workforcePools`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`location` |  `string` The location of the pool.Format: `locations/{location}`.  
  
### Query parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource to list pools for.Format: `organizations/{org-id}`.  
`pageSize` |  `integer` The maximum number of pools to return. The default value is 50. The maximum value is 100.  
`pageToken` |  `string` A page token, received from a previous `workforcePools.list` call. Provide this to retrieve the subsequent page.  
`showDeleted` |  `boolean` Whether to return soft-deleted pools.  
  
### Request body

The request body must be empty.

### Response body

Response message for workforcePools.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workforcePools": [
        {
          object ([WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workforcePools[]` |  `object (`[WorkforcePool](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools#WorkforcePool)`)` A list of pools.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-18 UTC."],[],[]] 
