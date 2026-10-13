---
url: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments/patch/
title: Method: projects.locations.interceptDeployments.patch \u00a0|\u00a0 Network Security Integration \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:36:38.906298+00:00
---

# Method: projects.locations.interceptDeployments.patch  |  Network Security Integration  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Network Security Integration ](https://docs.cloud.google.com/network-security-integration)
  * [ Reference ](https://docs.cloud.google.com/network-security-integration/docs/apis)



Send feedback 

#  Method: projects.locations.interceptDeployments.patch Stay organized with collections  Save and categorize content based on your preferences. 

Updates a deployment. See <https://google.aip.dev/134>.

### HTTP request

`PATCH https://networksecurity.googleapis.com/v1beta1/{interceptDeployment.name=projects/*/locations/*/interceptDeployments/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`interceptDeployment.name` |  `string` Immutable. Identifier. The resource name of this deployment, for example: `projects/123456789/locations/us-central1-a/interceptDeployments/my-dep`. See <https://google.aip.dev/122> for more details.  
  
### Query parameters

Parameters  
---  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to update. Fields are specified relative to the deployment (e.g. `description`; _not_ `interceptDeployment.description`). See <https://google.aip.dev/161> for more details.This is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
`requestId` |  `string` Optional. A unique identifier for this request. Must be a UUID4. This request is only idempotent if a `requestId` is provided. See <https://google.aip.dev/155> for more details.  
  
### Request body

The request body contains an instance of `[InterceptDeployment](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/v1beta1/projects.locations.interceptDeployments#InterceptDeployment)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/network-security-integration/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `networksecurity.interceptDeployments.update`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-23 UTC."],[],[]] 
