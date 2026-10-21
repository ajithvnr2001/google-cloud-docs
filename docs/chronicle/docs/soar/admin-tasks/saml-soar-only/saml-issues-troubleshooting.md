---
url: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-issues-troubleshooting/
title: Troubleshoot SAML issues \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T12:58:17.486130+00:00
---

# Troubleshoot SAML issues  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/saml-soar-only/saml-issues-troubleshooting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot SAML issues 

Supported in:

[ SOAR ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-soar-toc)

**Note:** This document applies only to the standalone Google SecOps SOAR platform. 

**Note:** This document only applies if you have not yet completed Stage 1 of [SOAR Migration to Google Cloud](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/migrate-to-gcp). After the completion of Stage 1, refer to [Google SecOps - Validation guide](https://docs.cloud.google.com/chronicle/docs/soar/admin-tasks/advanced/soar-pre-validation#authentication_workflow_architecture).

This document explains how to troubleshoot common issues you may encounter with SAML authentication in your Google Security Operations SOAR platform.

## Application not found in directory

**Message** : `AADSTS700016: Application with identifier 'https://yyy.yyyyyy.com/api/auth/saml/metadata' was not found in the directory 'yyy'.`

**Explanation** : There's a mismatch between the configuration in Azure AD (Basic SAML) and the system. 

**Fix** : In Azure AD, set **Identifier (Entity ID)** to the SP's Entity ID and ensure the **Reply URL (ACS)** matches your SP; confirm you're in the correct tenant and that users are assigned to the app.

## Invalid value for saml:AuthnContextDeclRef

**Message** : `Microsoft.IdentityModel.Tokens.Saml2.Saml2SecurityTokenReadException: IDX13102: Exception thrown while reading 'System.String' for Saml2SecurityToken. Inner exception: System.ArgumentException.`

**Explanation** : This error indicates an invalid value for `saml:AuthnContextDeclRef` in the SAML response.

**Fix** : Decode and inspect the SAML Response. If the IdP sends an invalid `AuthnContextDeclRef`, remove it or switch to a supported `saml:AuthnContextClassRef` (for example, `urn:oasis:names:tc:SAML:2.0:ac:classes:PasswordProtectedTransport`).

## System.ArgumentException: 'System.String' must be an absolute URI

**Message** : `/ds:Signature>saml:Subject<saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified" System.ArgumentException: IDX13300: 'System.String' must be an absolute URI, was: 'System.Uri"></saml:NameID>`

**Explanation** : The `NameID` `Format` must be a valid absolute URI (URN) supported by the SP, and the `<saml:NameID>` value must be present.

**Fix** : Set the `DefaultNameIDFormat` parameter in your SAML configuration to one of the following options:

  * `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress` (**most common**)
  * `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`
  * `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`



## User attributes not found and `LoginIdentifier` field is required

**Message** : `logs Server error Login error for user _yyyyyyyyyyyyyyyyyyyyyyy. User attributes were not found for creating new followed by Error: register : The LoginIdentifier field is required.`

**Explanation** : With Just-In-Time (JIT) provisioning enabled, the SP looks up the user using the `NameID` (or a mapped attribute). The incoming value doesn't match any existing login IDs.

**Fix** : The IdP must be configured to send a value that matches the **Login ID** field in user management (Settings > User Management). This value might be the user's email address or another unique ID.

## User type mismatch

**Message** : `Login error for user user@user.com. User type (Internal) does not match to this type of authentication (External).`

**Explanation** : An account with the same Login ID exists as **Internal** , but SAML authentication requires an **External** user.

**Fix** : Change the user type of the existing user with the conflicting username to **External** to match the SAML authentication method.

## Redirect loop

If your instance is configured for automatic redirection to the IdP login page, and you encounter a continuous redirect loop, you can temporarily disable auto-redirection by appending the following text to your instance hostname:

`/#/login?autoExternalLogin=false`

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
