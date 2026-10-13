---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/list/
title: Method: inboundSamlSsoProfiles.idpCredentials.list \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:42.341924+00:00
---

# Method: inboundSamlSsoProfiles.idpCredentials.list  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/list/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: inboundSamlSsoProfiles.idpCredentials.list Stay organized with collections  Save and categorize content based on your preferences. 

Returns a list of `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`s in an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.

### HTTP request

`GET https://cloudidentity.googleapis.com/v1/{parent=inboundSamlSsoProfiles/*}/idpCredentials`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The parent, which owns this collection of `IdpCredential`s. Format: `inboundSamlSsoProfiles/{sso_profile_id}`  
  
### Query parameters

Parameters  
---  
`pageSize` |  `integer` The maximum number of `IdpCredential`s to return. The service may return fewer than this value.  
`pageToken` |  `string` A page token, received from a previous `idpCredentials.list` call. Provide this to retrieve the subsequent page.When paginating, all other parameters provided to `idpCredentials.list` must match the call that provided the page token.  
  
### Request body

The request body must be empty.

### Response body

Response of the `[InboundSamlSsoProfilesService.ListIdpCredentials](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials/list#google.apps.cloudidentity.inboundsamlssoprofiles.v1.InboundSamlSsoProfilesService.ListIdpCredentials)` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "idpCredentials": [
        {
          object ([IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential))
        }
      ],
      "nextPageToken": string
    }  
  
Fields  
---  
`idpCredentials[]` |  `object (`[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`)` The IdpCredentials from the specified `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
`nextPageToken` |  `string` A token, which can be sent as `pageToken` to retrieve the next page. If this field is omitted, there are no subsequent pages.  
  
### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.inboundsso.readonly`
  * `https://www.googleapis.com/auth/cloud-identity.inboundsso`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-12-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-12-16 UTC."],[],[]] 
