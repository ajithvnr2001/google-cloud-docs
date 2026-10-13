---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/
title: REST Resource: inboundSamlSsoProfiles \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:41.325593+00:00
---

# REST Resource: inboundSamlSsoProfiles  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: inboundSamlSsoProfiles Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: InboundSamlSsoProfile

A [SAML 2.0](https://www.oasis-open.org/standards#samlv2.0) federation between a Google enterprise customer and a SAML identity provider.

JSON representation  
---  
      
    
    {
      "name": string,
      "customer": string,
      "displayName": string,
      "idpConfig": {
        object ([SamlIdpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#SamlIdpConfig))
      },
      "spConfig": {
        object ([SamlSpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#SamlSpConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the SAML SSO profile.  
`customer` |  `string` Immutable. The customer.For example: `customers/C0123abc`.  
`displayName` |  `string` Human-readable name of the SAML SSO profile.  
`idpConfig` |  `object (`[SamlIdpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#SamlIdpConfig)`)` SAML identity provider configuration.  
`spConfig` |  `object (`[SamlSpConfig](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#SamlSpConfig)`)` SAML service provider configuration for this SAML SSO profile. These are the service provider details provided by Google that should be configured on the corresponding identity provider.  
  
## SamlIdpConfig

SAML IDP (identity provider) configuration.

JSON representation  
---  
      
    
    {
      "entityId": string,
      "singleSignOnServiceUri": string,
      "logoutRedirectUri": string,
      "changePasswordUri": string
    }  
  
Fields  
---  
`entityId` |  `string` Required. The SAML **Entity ID** of the identity provider.  
`singleSignOnServiceUri` |  `string` Required. The `SingleSignOnService` endpoint location (sign-in page URL) of the identity provider. This is the URL where the `AuthnRequest` will be sent. Must use `HTTPS`. Assumed to accept the `HTTP-Redirect` binding.  
`logoutRedirectUri` |  `string` The **Logout Redirect URL** (sign-out page URL) of the identity provider. When a user clicks the sign-out link on a Google page, they will be redirected to this URL. This is a pure redirect with no attached SAML `LogoutRequest` i.e. SAML single logout is not supported. Must use `HTTPS`.  
`changePasswordUri` |  `string` The **Change Password URL** of the identity provider. Users will be sent to this URL when changing their passwords at `myaccount.google.com`. This takes precedence over the change password URL configured at customer-level. Must use `HTTPS`.  
  
## SamlSpConfig

SAML SP (service provider) configuration.

JSON representation  
---  
      
    
    {
      "entityId": string,
      "assertionConsumerServiceUri": string
    }  
  
Fields  
---  
`entityId` |  `string` Output only. The SAML **Entity ID** for this service provider.  
`assertionConsumerServiceUri` |  `string` Output only. The SAML **Assertion Consumer Service (ACS) URL** to be used for the IDP-initiated login. Assumed to accept response messages via the `HTTP-POST` binding.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/create)`

|  Creates an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)` for a customer.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/delete)`

|  Deletes an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/get)`

|  Gets an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/list)`

|  Lists `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`s for a customer.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles/patch)`

|  Updates an `[InboundSamlSsoProfile](https://docs.cloud.google.com/identity/docs/reference/rest/v1/inboundSamlSsoProfiles#InboundSamlSsoProfile)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-06 UTC."],[],[]] 
