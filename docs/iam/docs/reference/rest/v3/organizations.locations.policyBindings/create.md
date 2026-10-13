---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/create/
title: Method: organizations.locations.policyBindings.create \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:24.322675+00:00
---

# Method: organizations.locations.policyBindings.create  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: organizations.locations.policyBindings.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Creates a policy binding and returns a long-running operation. Callers will need the IAM permissions on both the policy and target. After the binding is created, the policy is applied to the target.

### HTTP request

`POST https://iam.googleapis.com/v3/{parent=organizations/*/locations/*}/policyBindings`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this policy binding will be created. The binding parent is the closest Resource Manager resource (project, folder or organization) to the binding target.Format:

  * `projects/{projectId}/locations/{location}`
  * `projects/{projectNumber}/locations/{location}`
  * `folders/{folderId}/locations/{location}`
  * `organizations/{organizationId}/locations/{location}`

  
  
### Query parameters

Parameters  
---  
`policyBindingId` |  `string` Required. The ID to use for the policy binding, which will become the final component of the policy binding's resource name.This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`validateOnly` |  `boolean` Optional. If set, validate the request and preview the creation, but do not actually post it.  
  
### Request body

The request body contains an instance of `[PolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rest/v3/folders.locations.policyBindings#PolicyBinding)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-12 UTC."],[],[]] 
