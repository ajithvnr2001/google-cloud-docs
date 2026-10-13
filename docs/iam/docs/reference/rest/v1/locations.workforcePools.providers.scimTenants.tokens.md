---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens
title: REST Resource: locations.workforcePools.providers.scimTenants.tokens \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:50.986174+00:00
---

# REST Resource: locations.workforcePools.providers.scimTenants.tokens  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  REST Resource: locations.workforcePools.providers.scimTenants.tokens Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: WorkforcePoolProviderScimToken
    * JSON representation
  * State
  * Methods



## Resource: WorkforcePoolProviderScimToken

Gemini Enterprise only. Represents a token for the `[WorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants#WorkforcePoolProviderScimTenant)`. Used for authenticating SCIM provisioning requests.

JSON representation  
---  
      
    
    {
      "name": string,
      "securityToken": string,
      "state": enum ([State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#State)),
      "displayName": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Gemini Enterprise only. The resource name of the SCIM Token.Format: `locations/{location}/workforcePools/{workforcePool}/providers/ {workforcePoolProvider}/scimTenants/{scim_tenant}/tokens/{token}`  
`securityToken` |  `string` Output only. Gemini Enterprise only. The token string. Provide this to the IdP for authentication. Will be set only during creation.  
`state` |  `enum (`[State](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#State)`)` Output only. Gemini Enterprise only. The state of the token.  
`displayName` |  `string` Optional. Gemini Enterprise only. The display name of the SCIM token.Cannot exceed 32 characters.  
  
## State

Gemini Enterprise only. The current state of the SCIM token.

Enums  
---  
`STATE_UNSPECIFIED` | Gemini Enterprise only. State unspecified.  
`ACTIVE` | Gemini Enterprise only. The token is active and may be used to provision users and groups.  
`DELETED` | Gemini Enterprise only. The token is soft-deleted. Soft-deleted tokens are permanently deleted after approximately 30 days.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/create)`

|  Gemini Enterprise only.  
  
### `[delete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/delete)`

|  Gemini Enterprise only.  
  
### `[get](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/get)`

|  Gemini Enterprise only.  
  
### `[list](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/list)`

|  Gemini Enterprise only.  
  
### `[patch](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/patch)`

|  Gemini Enterprise only.  
  
### `[undelete](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/undelete)`

|  Gemini Enterprise only.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-18 UTC."],[],[]] 
