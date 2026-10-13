---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/create/
title: Method: organizations.locations.principalAccessBoundaryPolicies.create \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:24.993141+00:00
---

# Method: organizations.locations.principalAccessBoundaryPolicies.create  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: organizations.locations.principalAccessBoundaryPolicies.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * IAM Permissions
  * Examples
  * Try it!



Creates a principal access boundary policy, and returns a long running operation.

### HTTP request

`POST https://iam.googleapis.com/v3/{parent=organizations/*/locations/*}/principalAccessBoundaryPolicies`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent resource where this principal access boundary policy will be created. Only organizations are supported.Format: `organizations/{organizationId}/locations/{location}`  
  
### Query parameters

Parameters  
---  
`principalAccessBoundaryPolicyId` |  `string` Required. The ID to use for the principal access boundary policy, which will become the final component of the principal access boundary policy's resource name.This value must start with a lowercase letter followed by up to 62 lowercase letters, numbers, hyphens, or dots. Pattern, /[a-z][a-z0-9-.]{2,62}/.  
`validateOnly` |  `boolean` Optional. If set, validate the request and preview the creation, but do not actually post it.  
  
### Request body

The request body contains an instance of `[PrincipalAccessBoundaryPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies#PrincipalAccessBoundaryPolicy)`.

### Response body

If successful, the response body contains a newly created instance of `[Operation](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

### IAM Permissions

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `iam.principalaccessboundarypolicies.create`



For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-05-21 UTC."],[],[]] 
