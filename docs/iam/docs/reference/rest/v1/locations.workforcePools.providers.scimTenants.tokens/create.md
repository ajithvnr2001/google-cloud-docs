---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/create/
title: Method: locations.workforcePools.providers.scimTenants.tokens.create \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:50.280059+00:00
---

# Method: locations.workforcePools.providers.scimTenants.tokens.create  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/create/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: locations.workforcePools.providers.scimTenants.tokens.create Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
  * Authorization scopes
  * Examples
  * Try it!



Gemini Enterprise only. Creates a new `[WorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#WorkforcePoolProviderScimToken)` in a `[WorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants#WorkforcePoolProviderScimTenant)`. You cannot reuse the name of a deleted SCIM token until 30 days after deletion.

### HTTP request

`POST https://iam.googleapis.com/v1/{parent=locations/*/workforcePools/*/providers/*/scimTenants/*}/tokens`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Gemini Enterprise only. The parent tenant to create SCIM token. Format: 'locations/{location}/workforcePools/{workforcePool}/providers/{provider}/scimTenants/{scim_tenant}'  
  
### Query parameters

Parameters  
---  
`workforcePoolProviderScimTokenId` |  `string` Required. Gemini Enterprise only. The ID to use for the SCIM token, which becomes the final component of the resource name. This value should be 4-32 characters and follow the pattern: `([a-z]([a-z0-9\\-]{2,30}[a-z0-9]))`  
  
### Request body

The request body contains an instance of `[WorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#WorkforcePoolProviderScimToken)`.

### Response body

If successful, the response body contains a newly created instance of `[WorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#WorkforcePoolProviderScimToken)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-15 UTC."],[],[]] 
