---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/create/
title: Method: projects.locations.mirroringDeployments.create \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:00:45.441628+00:00
---

# Method: projects.locations.mirroringDeployments.create  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  Method: projects.locations.mirroringDeployments.create Stay organized with collections  Save and categorize content based on your preferences. 

Creates a deployment in a given project and location. See <https://google.aip.dev/133>.

### HTTP request

`POST https://networksecurity.googleapis.com/v1/{parent=projects/*/locations/*}/mirroringDeployments`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this deployment will be created. Format: projects/{project}/locations/{location}  
  
### Query parameters

Parameters  
---  
`mirroringDeploymentId` |  `string` Required. The ID to use for the new deployment, which will become the final component of the deployment's resource name.  
`requestId` |  `string` Optional. A unique identifier for this request. Must be a UUID4. This request is only idempotent if a `requestId` is provided. See <https://google.aip.dev/155> for more details.  
  
### Request body

The request body contains an instance of `[MirroringDeployment](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1/projects.locations.mirroringDeployments#MirroringDeployment)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `networksecurity.mirroringDeployments.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
