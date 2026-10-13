---
url: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/get/
title: Method: organizations.policies.get \u00a0|\u00a0 Organization Policy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:00:41.636537+00:00
---

# Method: organizations.policies.get  |  Organization Policy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/organization-policy/reference/rest/v2/organizations.policies/get/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Organization Policy ](https://docs.cloud.google.com/organization-policy)
  * [ Reference ](https://docs.cloud.google.com/organization-policy/apis)



Send feedback 

#  Method: organizations.policies.get Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Try it!



Gets a policy on a resource.

If no policy is set on the resource, `NOT_FOUND` is returned. The entity tag (ETag) can be used with `policies.patch()` to update a policy during read-modify-write.

### HTTP request

`GET https://orgpolicy.googleapis.com/v2/{name=organizations/*/policies/*}`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Resource name of the policy. See `[Policy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy)` for naming requirements. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `orgpolicy.policies.get`

  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[Policy](https://docs.cloud.google.com/organization-policy/reference/rest/v2/folders.policies#Policy)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * `https://www.googleapis.com/auth/organizationpolicy`
  * `https://www.googleapis.com/auth/organizationpolicy.readonly`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-22 UTC."],[],[]] 
