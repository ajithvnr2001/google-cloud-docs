---
url: https://docs.cloud.google.com/iam/docs/reference/agentidentity/rest/v1/projects.locations.authProviders/queryWorkloads/
title: Method: projects.locations.authProviders.queryWorkloads \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:23:13.975605+00:00
---

# Method: projects.locations.authProviders.queryWorkloads  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/agentidentity/rest/v1/projects.locations.authProviders/queryWorkloads/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.authProviders.queryWorkloads Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions
  * Try it!



Queries which workloads are using a given auth provider.

### HTTP request

`GET https://agentidentity.googleapis.com/v1/{name=projects/*/locations/*/authProviders/*}:queryWorkloads`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. The name of the auth provider to query. Format: projects/{project}/locations/{location}/authProviders/{authProvider}  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. The maximum page size is 1000.  
`pageToken` |  `string` Optional. A token, which can be sent as `pageToken` to retrieve the next page. When paginating, all other parameters provided to `authProviders.queryWorkloads` must match the call that provided the page token. If this field is omitted, the first page is returned.  
  
### Request body

The request body must be empty.

### Response body

Response message for `authProviders.queryWorkloads`.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workloadIds": [
        string
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workloadIds[]` |  `string` The unique list of identifiers for the agents that used this auth provider, starting with `principal://`.  
`nextPageToken` |  `string` A token to retrieve the next page of results.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `agentidentity.authProviders.queryWorkloads`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-14 UTC."],[],[]] 
