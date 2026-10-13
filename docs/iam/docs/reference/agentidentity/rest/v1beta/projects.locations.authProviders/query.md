---
url: https://docs.cloud.google.com/iam/docs/reference/agentidentity/rest/v1beta/projects.locations.authProviders/query/
title: Method: projects.locations.authProviders.query \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:51:31.169828+00:00
---

# Method: projects.locations.authProviders.query  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/agentidentity/rest/v1beta/projects.locations.authProviders/query/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.authProviders.query Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Queries which auth providers are used by a given workload ID.

### HTTP request

`GET https://agentidentity.googleapis.com/v1beta/{parent=projects/*/locations/*}/authProviders:query`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where the search is performed. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`workloadId` |  `string` Required. The workload identifier to filter by.  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. The maximum page size is 1000.  
`pageToken` |  `string` Optional. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, the first page is returned.A page token, received from a previous authProviders.query call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to authProviders.query must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response message for `authProviders.query`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "authProviderNames": [
        string
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`authProviderNames[]` |  `string` The unique list of auth provider resource names used by the workload.  
`nextPageToken` |  `string` A token identifying a page of results the server should return. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `agentidentity.authProviders.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-14 UTC."],[],[]] 
