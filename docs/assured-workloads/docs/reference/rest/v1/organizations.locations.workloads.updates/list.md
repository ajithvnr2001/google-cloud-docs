---
url: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates/list/
title: Method: organizations.locations.workloads.updates.list \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:38:29.626475+00:00
---

# Method: organizations.locations.workloads.updates.list  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/reference/rest/v1/organizations.locations.workloads.updates/list/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Reference ](https://docs.cloud.google.com/assured-workloads/docs/apis)



Send feedback 

#  Method: organizations.locations.workloads.updates.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * IAM Permissions



This endpoint lists all updates for the given workload.

### HTTP request

`GET https://{endpoint}/v1/{parent=organizations/*/locations/*/workloads/*}/updates`

Where `{endpoint}` is one of the [supported service endpoints](https://docs.cloud.google.com/assured-workloads/docs/reference/rest#rest_endpoints).

The URLs use [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. organizations/{org_id}/locations/{locationId}/workloads/{workload_id} Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `assuredworkloads.updates.list`

  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Page size. The default value is 20 and the max allowed value is 100.  
`pageToken` |  `string` Page token returned from previous request.  
  
### Request body

The request body must be empty.

### Response body

Response of listing the compliance updates per workload with pagination.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workloadUpdates": [
        {
          object (WorkloadUpdate)
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workloadUpdates[]` |  `object (`WorkloadUpdate`)` The list of workload updates for a given workload.  
`nextPageToken` |  `string` The next page token. Return empty if reached the last page.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `assuredworkloads.updates.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-30 UTC."],[],[]] 
