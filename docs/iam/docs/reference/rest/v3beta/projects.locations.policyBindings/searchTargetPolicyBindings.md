---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/searchTargetPolicyBindings/
title: Method: projects.locations.policyBindings.searchTargetPolicyBindings \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:40.824688+00:00
---

# Method: projects.locations.policyBindings.searchTargetPolicyBindings  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/searchTargetPolicyBindings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.policyBindings.searchTargetPolicyBindings Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Search policy bindings by target. Returns all policy binding objects bound directly to target.

### HTTP request

`GET https://iam.googleapis.com/v3beta/{parent=projects/*/locations/*}/policyBindings:searchTargetPolicyBindings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this search will be performed. This should be the nearest Resource Manager resource (project, folder, or organization) to the target.Format:

  * `projects/{projectId}/locations/{location}`
  * `projects/{projectNumber}/locations/{location}`
  * `folders/{folderId}/locations/{location}`
  * `organizations/{organizationId}/locations/{location}`

  
  
### Query parameters

Parameters  
---  
`target` |  `string` Required. The target resource, which is bound to the policy in the binding.Format:

  * `//iam.googleapis.com/locations/global/workforcePools/POOL_ID`
  * `//iam.googleapis.com/projects/PROJECT_NUMBER/locations/global/workloadIdentityPools/POOL_ID`
  * `//iam.googleapis.com/locations/global/workspace/WORKSPACE_ID`
  * `//cloudresourcemanager.googleapis.com/projects/{projectNumber}`
  * `//cloudresourcemanager.googleapis.com/folders/{folderId}`
  * `//cloudresourcemanager.googleapis.com/organizations/{organizationId}`

  
`pageSize` |  `integer` Optional. The maximum number of policy bindings to return. The service may return fewer than this value.The default value is 50. The maximum value is 1000.  
`pageToken` |  `string` Optional. A page token, received from a previous `SearchTargetPolicyBindingsRequest` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `SearchTargetPolicyBindingsRequest` must match the call that provided the page token.  
`filter` |  `string` Optional. Filtering currently only supports the kind of policies to return, and must be in the format "policyKind={policyKind}".If String is empty, bindings bound to all kinds of policies would be returned.The only supported values are the following:

  * "policyKind=PRINCIPAL_ACCESS_BOUNDARY",
  * "policyKind=ACCESS"

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[SearchTargetPolicyBindingsResponse](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/SearchTargetPolicyBindingsResponse)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
