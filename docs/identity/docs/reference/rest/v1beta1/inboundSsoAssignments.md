---
url: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/
title: REST Resource: inboundSsoAssignments \u00a0|\u00a0 Cloud Identity \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:38:55.957524+00:00
---

# REST Resource: inboundSsoAssignments  |  Cloud Identity  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Cloud Identity ](https://docs.cloud.google.com/identity/docs)
  * [ Reference ](https://docs.cloud.google.com/identity/docs/apis)



Send feedback 

#  REST Resource: inboundSsoAssignments Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: InboundSsoAssignment

Targets with "set" SSO assignments and their respective assignments.

JSON representation  
---  
      
    
    {
      "name": string,
      "customer": string,
      "rank": integer,
      "ssoMode": enum ([SsoMode](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#SsoMode)),
      "samlSsoInfo": {
        object ([SamlSsoInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#SamlSsoInfo))
      },
      "oidcSsoInfo": {
        object ([OidcSsoInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#OidcSsoInfo))
      },
      "signInBehavior": {
        object ([SignInBehavior](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#SignInBehavior))
      },
    
      "targetGroup": string,
      "targetOrgUnit": string
    }  
  
Fields  
---  
`name` |  `string` Output only. [Resource name](https://cloud.google.com/apis/design/resource_names) of the Inbound SSO Assignment.  
`customer` |  `string` Immutable. The customer.For example: `customers/C0123abc`.  
`rank` |  `integer` Must be zero (which is the default value so it can be omitted) for assignments with `targetOrgUnit` set and must be greater-than-or-equal-to one for assignments with `targetGroup` set.  
`ssoMode` |  `enum (`[SsoMode](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#SsoMode)`)` Inbound SSO behavior.  
`samlSsoInfo` |  `object (`[SamlSsoInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#SamlSsoInfo)`)` SAML SSO details. Must be set if and only if `ssoMode` is set to `SAML_SSO`.  
`oidcSsoInfo` |  `object (`[OidcSsoInfo](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#OidcSsoInfo)`)` OpenID Connect SSO details. Must be set if and only if `ssoMode` is set to `OIDC_SSO`.  
`signInBehavior` |  `object (`[SignInBehavior](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#SignInBehavior)`)` Assertions about users assigned to an IdP will always be accepted from that IdP. This controls whether/when Google should redirect a user to the IdP. Unset (defaults) is the recommended configuration.  
Union field `target`. Target of the assignment.When multiple assignments apply to a given user, precedence is as follows:1) The applicable group-targeting assignment with the numerically-lowest `rank` takes precedence.2) If no group-targeting assignments apply, the applicable orgUnit-targeting assignment on the innermost-enclosing Organizational Unit takes precedence.  
`target` can be only one of the following:  
`targetGroup` |  `string` Immutable. Must be of the form `groups/{group}`.  
`targetOrgUnit` |  `string` Immutable. Must be of the form `orgUnits/{orgUnit}`.  
  
## SsoMode

Inbound SSO behaviors.

Enums  
---  
`SSO_MODE_UNSPECIFIED` | Not allowed.  
`SSO_OFF` | Disable SSO for the targeted users.  
`SAML_SSO` | Use an external SAML Identity Provider for SSO for the targeted users.  
`OIDC_SSO` | Use an external OIDC Identity Provider for SSO for the targeted users.  
`DOMAIN_WIDE_SAML_IF_ENABLED` | Use the domain-wide SAML Identity Provider for the targeted users if one is configured; otherwise, this is equivalent to `SSO_OFF`. Note that this will also be equivalent to `SSO_OFF` if/when support for domain-wide SAML is removed. Google may disallow this mode at that point and existing assignments with this mode may be automatically changed to `SSO_OFF`.  
  
## SamlSsoInfo

Details that are applicable when `ssoMode` == `SAML_SSO`.

JSON representation  
---  
      
    
    {
      "inboundSamlSsoProfile": string
    }  
  
Fields  
---  
`inboundSamlSsoProfile` |  `string` Required. Name of the `InboundSamlSsoProfile` to use. Must be of the form `inboundSamlSsoProfiles/{inboundSamlSsoProfile}`.  
  
## OidcSsoInfo

Details that are applicable when `ssoMode` is set to `OIDC_SSO`.

JSON representation  
---  
      
    
    {
      "inboundOidcSsoProfile": string
    }  
  
Fields  
---  
`inboundOidcSsoProfile` |  `string` Required. Name of the `InboundOidcSsoProfile` to use. Must be of the form `inboundOidcSsoProfiles/{inboundOidcSsoProfile}`.  
  
## SignInBehavior

Controls sign-in behavior.

JSON representation  
---  
      
    
    {
      "redirectCondition": enum ([RedirectCondition](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#RedirectCondition))
    }  
  
Fields  
---  
`redirectCondition` |  `enum (`[RedirectCondition](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#RedirectCondition)`)` When to redirect sign-ins to the IdP.  
  
## RedirectCondition

Controls redirection to the IdP.

Enums  
---  
`REDIRECT_CONDITION_UNSPECIFIED` | Default and means "always"  
`NEVER` | Sign-in flows where the user is prompted for their identity will not redirect to the IdP (so the user will most likely be prompted by Google for a password), but special flows like IdP-initiated SAML and sign-in following automatic redirection to the IdP by domain-specific service URLs will accept the IdP's assertion of the user's identity.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/create)`

|  Creates an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)` for users and devices in a `Customer` under a given `Group` or `OrgUnit`.  
  
### `[delete](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/delete)`

|  Deletes an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`.  
  
### `[get](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/get)`

|  Gets an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`.  
  
### `[list](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/list)`

|  Lists the `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`s for a `Customer`.  
  
### `[patch](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments/patch)`

|  Updates an `[InboundSsoAssignment](https://docs.cloud.google.com/identity/docs/reference/rest/v1beta1/inboundSsoAssignments#InboundSsoAssignment)`.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-11 UTC."],[],[]] 
