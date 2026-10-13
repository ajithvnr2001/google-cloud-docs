---
url: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/list/
title: Method: locations.workforcePools.providers.scimTenants.tokens.list \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:53:50.814514+00:00
---

# Method: locations.workforcePools.providers.scimTenants.tokens.list  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Reference ](https://docs.cloud.google.com/iam/docs/apis)



Send feedback 

#  Method: locations.workforcePools.providers.scimTenants.tokens.list Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Path parameters
  * Query parameters
  * Request body
  * Response body
    * JSON representation
  * Authorization scopes
  * Examples
  * Try it!



Gemini Enterprise only. Lists all non-deleted [WorkforcePoolProviderScimTokens][]s in a `[WorkforcePoolProviderScimTenant](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants#WorkforcePoolProviderScimTenant)`. If `showDeleted` is set to `true`, then deleted SCIM tokens are also listed.

### HTTP request

`GET https://iam.googleapis.com/v1/{parent=locations/*/workforcePools/*/providers/*/scimTenants/*}/tokens`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. Gemini Enterprise only. The parent to list SCIM tokens. Format: 'locations/{location}/workforcePools/{workforcePool}/providers/{provider}/scimTenants/{scim_tenant}'  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` Optional. Gemini Enterprise only. The maximum number of SCIM tokens to return. If unspecified, at most 2 SCIM tokens will be returned.  
`pageToken` |  `string` Optional. Gemini Enterprise only. A page token, received from a previous `tokens.list` call. Provide this to retrieve the subsequent page.  
`showDeleted` |  `boolean` Optional. Gemini Enterprise only. Whether to return soft-deleted SCIM tokens.  
  
### Request body

The request body must be empty.

### Response body

Gemini Enterprise only. Response message for tokens.list.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "workforcePoolProviderScimTokens": [
        {
          object ([WorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#WorkforcePoolProviderScimToken))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`workforcePoolProviderScimTokens[]` |  `object (`[WorkforcePoolProviderScimToken](https://docs.cloud.google.com/iam/docs/reference/rest/v1/locations.workforcePools.providers.scimTenants.tokens#WorkforcePoolProviderScimToken)`)` Output only. Gemini Enterprise only. A list of SCIM tokens.  
`nextPageToken` |  `string` Optional. Gemini Enterprise only. A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-platform`
  * ` https://www.googleapis.com/auth/iam`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-18 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-18 UTC."],[],[]] 
