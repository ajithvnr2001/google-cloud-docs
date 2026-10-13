---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/undelete/
title: Method: locations.workforcePools.providers.scimTenants.tokens.undelete \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:51.437389+00:00
---

# Method: locations.workforcePools.providers.scimTenants.tokens.undelete  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/undelete/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: locations.workforcePools.providers.scimTenants.tokens.undelete Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Gemini Enterprise only. Undeletes a `[WorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#WorkforcePoolProviderScimToken)`,that was deleted fewer than 30 days ago.

### HTTP request

`POST https://iam.googleapis.com/v1/{name=locations/*/workforcePools/*/providers/*/scimTenants/*/tokens/*}:undelete`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`name` |  `string` Required. Gemini Enterprise only. The name of the SCIM token to undelete.Format: `locations/{location}/workforcePools/{workforcePool}/providers/{provider}/scimTenants/{scim_tenant}/tokens/{token}`  
  
### Request body

The request body must be empty.

### Response body

If successful, the response body contains an instance of `[WorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#WorkforcePoolProviderScimToken)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-18 UTC."],[],[]] 
