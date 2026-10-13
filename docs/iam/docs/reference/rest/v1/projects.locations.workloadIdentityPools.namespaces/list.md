---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/list/
title: Method: projects.locations.workloadIdentityPools.namespaces.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:58.843367+00:00
---

# Method: projects.locations.workloadIdentityPools.namespaces.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.workloadIdentityPools.namespaces.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Lists all non-deleted `[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`s in a workload identity pool. If `showDeleted` is set to `true`, then deleted namespaces are also listed.

### HTTP request

`GET https://iam.googleapis.com/v1/{parent=projects/*/locations/*/workloadIdentityPools/*}/namespaces`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource to list namespaces for.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of namespaces to return. If unspecified, at most 50 namespaces are returned. The maximum value is 1000; values above are 1000 truncated to 1000.  
`pageToken` |  `string` A page token, received from a previous `namespaces.list` call. Provide this to retrieve the subsequent page.  
`showDeleted` |  `boolean` Whether to return soft-deleted namespaces.  
  
### Request body

The request body must be empty.

### Response body

Response message for namespaces.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workloadIdentityPoolNamespaces": [
        {
          object ([WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workloadIdentityPoolNamespaces[]` |  `object (`[WorkloadIdentityPoolNamespace](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.locations.workloadIdentityPools.namespaces#WorkloadIdentityPoolNamespace)`)` A list of namespaces.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
