---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/
title: REST Resource: inboundOidcSsoProfiles \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:40.361504+00:00
---

# REST Resource: inboundOidcSsoProfiles  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: inboundOidcSsoProfiles Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: InboundOidcSsoProfile

An [OIDC](https://openid.net/developers/how-connect-works/) federation between a Google enterprise customer and an OIDC identity provider.

JSON representation  
---  
      
    
    {
      "name": string,
      "customer": string,
      "displayName": string,
      "idpConfig": {
        object ([OidcIdpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#OidcIdpConfig))
      },
      "rpConfig": {
        object ([OidcRpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#OidcRpConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the OIDC SSO profile.  
`customer` |  `string` Immutable. The customer.For example: `customers/C0123abc`.  
`displayName` |  `string` Human-readable name of the OIDC SSO profile.  
`idpConfig` |  `object (`[OidcIdpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#OidcIdpConfig)`)` OIDC identity provider configuration.  
`rpConfig` |  `object (`[OidcRpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#OidcRpConfig)`)` OIDC relying party (RP) configuration for this OIDC SSO profile. These are the RP details provided by Google that should be configured on the corresponding identity provider.  
  
## OidcIdpConfig

OIDC IDP (identity provider) configuration.

JSON representation  
---  
      
    
    {
      "issuerUri": string,
      "changePasswordUri": string
    }  
  
Fields  
---  
`issuerUri` |  `string` Required. The Issuer identifier for the IdP. Must be a URL. The discovery URL will be derived from this as described in Section 4 of [the OIDC specification](https://openid.net/specs/openid-connect-discovery-1_0.html).  
`changePasswordUri` |  `string` The **Change Password URL** of the identity provider. Users will be sent to this URL when changing their passwords at `myaccount.google.com`. This takes precedence over the change password URL configured at customer-level. Must use `HTTPS`.  
  
## OidcRpConfig

OIDC RP (relying party) configuration.

JSON representation  
---  
      
    
    {
      "clientId": string,
      "clientSecret": string,
      "redirectUris": [
        string
      ]
    }  
  
Fields  
---  
`clientId` |  `string` OAuth2 client ID for OIDC.  
`clientSecret` |  `string` Input only. OAuth2 client secret for OIDC.  
`redirectUris[]` |  `string` Output only. The URL(s) that this client may use in authentication requests.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/create)`

|  Creates an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)` for a customer.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/delete)`

|  Deletes an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/get)`

|  Gets an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/list)`

|  Lists `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)` objects for a Google enterprise customer.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles/patch)`

|  Updates an `[InboundOidcSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundOidcSsoProfiles#InboundOidcSsoProfile)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-06 UTC."],[],[]] 
