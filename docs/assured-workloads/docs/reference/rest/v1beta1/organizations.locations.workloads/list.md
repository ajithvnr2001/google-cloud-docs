---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/list/
title: Method: organizations.locations.workloads.list \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:26.227023+00:00
---

# Method: organizations.locations.workloads.list  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads/list/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  Method: organizations.locations.workloads.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



Lists Assured Workloads under a CRM Node.

### HTTP request

`GET https://{endpoint}/v1beta1/{parent=organizations/*/locations/*}/workloads`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Parent Resource to list workloads from. Must be of the form `organizations/{org_id}/locations/{location}`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `assuredworkloads.workload.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Page size.  
`pageToken` |  `string` Page token returned from previous request. Page token contains context from previous request. Page token needs to be passed in the second and following requests.  
`filter` |  `string` A custom filter for filtering by properties of a workload. At this time, only filtering by labels is supported.  
  
### Request body

The request body must be empty.

### Response body

Response of workloads.list endpoint.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workloads": [
        {
          object ([Workload](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads#Workload))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workloads[]` |  `object (`[Workload](https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1beta1/organizations.locations.workloads#Workload)`)` List of Workloads under a given parent.  
`nextPageToken` |  `string` The next page token. Return empty if reached the last page.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `assuredworkloads.workload.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
