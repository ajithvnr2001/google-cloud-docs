---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials/add/
title: Method: inboundSamlSsoProfiles.idpCredentials.add \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:56.146737+00:00
---

# Method: inboundSamlSsoProfiles.idpCredentials.add  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials/add/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  Method: inboundSamlSsoProfiles.idpCredentials.add Stay organized with collections  Save and categorize content based on your preferences. 

Adds an `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`. Up to 2 credentials are allowed.

When the target customer has enabled [Multi-party approval for sensitive actions](https://support.google.com/a/answer/13790448), the `Operation` in the response will have `"done": false`, it will not have a response, and the metadata will have `"state": "awaiting-multi-party-approval"`.

### HTTP request

`POST https://cloudidentity.googleapis.com/v1beta1/{parent=inboundSamlSsoProfiles/*}/idpCredentials:add`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Path parameters

Parameters  
---  
`parent` |  `string` Required. The `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles#InboundSamlSsoProfile)` that owns the `[IdpCredential](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSamlSsoProfiles.idpCredentials#IdpCredential)`. Format: `inboundSamlSsoProfiles/{sso_profile_id}`  
  
### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
    
      "pemData": string
    }  
  
Fields  
---  
Union field `data`.`data` can be only one of the following:  
`pemData` |  `string` PEM encoded x509 certificate containing the public key for verifying IdP signatures.  
  
### Response body

If successful, the response body contains an instance of `[Operation](https://docs.cloud.google.com/identity/docs/reference/rest/Shared.Types/Operation)`.

### Authorization scopes

Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/cloud-identity.inboundsso`
  * `https://www.googleapis.com/auth/cloud-identity`
  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authorization guide](https://developers.google.com/workspace/guides/configure-oauth-consent).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
