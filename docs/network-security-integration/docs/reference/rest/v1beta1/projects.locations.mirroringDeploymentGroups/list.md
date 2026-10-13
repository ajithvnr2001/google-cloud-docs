---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups/list/
title: Method: projects.locations.mirroringDeploymentGroups.list \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:41.438460+00:00
---

# Method: projects.locations.mirroringDeploymentGroups.list  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  Method: projects.locations.mirroringDeploymentGroups.list Stay organized with collections  Save and categorize content based on your preferences. 

Lists deployment groups in a given project and location. See <https://google.aip.dev/132>.

### HTTP request

`GET https://networksecurity.googleapis.com/v1beta1/{parent=projects/*/locations/*}/mirroringDeploymentGroups`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of deployment groups. Example: `projects/123456789/locations/global`. See <https://google.aip.dev/132> for more details.  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default. See <https://google.aip.dev/158> for more details.  
`pageToken` |  `string` Optional. A page token, received from a previous `mirroringDeploymentGroups.list` call. Provide this to retrieve the subsequent page. When paginating, all other parameters provided to `mirroringDeploymentGroups.list` must match the call that provided the page token. See <https://google.aip.dev/158> for more details.  
`filter` |  `string` Optional. Filter expression. See <https://google.aip.dev/160#filtering> for more details.  
`orderBy` |  `string` Optional. Sort expression. See <https://google.aip.dev/132#ordering> for more details.  
  
### Request body

The request body must be empty.

### Response body

Response message for mirroringDeploymentGroups.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "mirroringDeploymentGroups": [
        {
          object ([MirroringDeploymentGroup](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups#MirroringDeploymentGroup))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`mirroringDeploymentGroups[]` |  `object (`[MirroringDeploymentGroup](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.mirroringDeploymentGroups#MirroringDeploymentGroup)`)` The deployment groups from the specified parent.  
`nextPageToken` |  `string` A token that can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages. See <https://google.aip.dev/158> for more details.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networksecurity.mirroringDeploymentGroups.list`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
