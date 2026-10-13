---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/patch/
title: Method: projects.locations.policyBindings.patch \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:40.696101+00:00
---

# Method: projects.locations.policyBindings.patch  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/projects.locations.policyBindings/patch/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: projects.locations.policyBindings.patch Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Updates a policy binding and returns a long-running operation. Callers will need the IAM permissions on the policy and target in the binding to update. Target and policy are immutable and cannot be updated.

### HTTP request

`PATCH https://iam.googleapis.com/v3beta/{policyBinding.name=projects/*/locations/*/policyBindings/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`policyBinding.name` |  `string` Identifier. The name of the policy binding, in the format `{binding_parent/locations/{location}/policyBindings/{policyBindingId}`. The binding parent is the closest Resource Manager resource (project, folder, or organization) to the binding target.Format:

  * `projects/{projectId}/locations/{location}/policyBindings/{policyBindingId}`
  * `projects/{projectNumber}/locations/{location}/policyBindings/{policyBindingId}`
  * `folders/{folderId}/locations/{location}/policyBindings/{policyBindingId}`
  * `organizations/{organizationId}/locations/{location}/policyBindings/{policyBindingId}`

  
  
### Query parameters

Parameters  
---  
`validateOnly` |  `boolean` Optional. If set, validate the request and preview the update, but do not actually post it.  
`updateMask` |  `string (`[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` format)` Optional. The list of fields to updateThis is a comma-separated list of fully qualified names of fields. Example: `"user.displayName,photo"`.  
  
### Request body

The request body contains an instance of `[PolicyBinding](https://docs.cloud.google.com/iam/docs/reference/rest/v3beta/folders.locations.policyBindings#PolicyBinding)`.

### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/iam/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-26 UTC."],[],[]] 
