---
url: https://docs.cloud.google.com/identity-platform/docs/product-comparison/
title: Differences between Identity Platform and Firebase Authentication \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:49:23.853207+00:00
---

# Differences between Identity Platform and Firebase Authentication  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/product-comparison/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

#  Differences between Identity Platform and Firebase Authentication 

[Identity Platform](https://docs.cloud.google.com/identity-platform) serves as the backend for Firebase Authentication with Identity Platform and offers identical features. As an upgrade from Firebase Authentication, Identity Platform includes the following additional capabilities:

  * [Multi-factor authentication (MFA)](https://docs.cloud.google.com/identity-platform/docs/web/mfa)
  * [Blocking functions](https://docs.cloud.google.com/identity-platform/docs/blocking-functions)
  * [OpenID Connect (OIDC)](https://docs.cloud.google.com/identity-platform/docs/how-to-enable-application-for-oidc) and [Security Assertion Markup Language (SAML)](https://docs.cloud.google.com/identity-platform/docs/how-to-enable-application-for-saml) authentication.
  * [Multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy) support.
  * [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/authenticate-users-external-identities) integration.
  * [BAA coverage](https://docs.cloud.google.com/docs/security/compliance/hipaa).
  * A 99.95% uptime [SLA](https://cloud.google.com/identity-platform/sla).



You do not need to change your apps when upgrading from Firebase Authentication to Identity Platform (or Firebase Authentication with Identity Platform) and your app continues to work with existing Firebase services.

**Note:** Firebase Authentication with Identity Platform and Identity Platform are [paid services](https://cloud.google.com/identity-platform/pricing).

Firebase Authentication with Identity Platform is available without a billing instrument up to daily [limits](https://cloud.google.com/identity-platform/quotas).

## Feature comparison

The following tables list differences between Identity Platform, Firebase Authentication with Identity Platform, and Firebase Authentication.

### Authentication

Feature | Identity Platform | Firebase Authentication  
---|---|---  
Sign in with email | Yes | Yes  
Sign in with OAuth | Yes | Yes  
Sign in with phone | Yes | Yes  
Custom authentication | Yes | Yes  
Multi-factor authentication | Yes | No  
Blocking Functions | Yes | No  
Sign in with OIDC | Yes | No  
Sign in with SAML | Yes | No  
Multi-tenancy | Yes | No  
IAP integration | Yes | No  
  
### SDKs

Identity Platform and Firebase Authentication both support a collection of Client and Admin SDKs. To preserve backwards-compatibility, the SDKs occasionally use Firebase branding and naming conventions.

Feature | Identity Platform | Firebase Authentication  
---|---|---  
Web SDK | Yes | Yes  
iOS SDK | Yes | Yes  
Android SDK | Yes | Yes  
Admin SDK | Yes | Yes  
  
### Compliance and uptime

Feature | Identity Platform | Firebase Authentication  
---|---|---  
ISO 27001 | Yes | Yes  
SSAE 18 SOC1 | Yes | Yes  
SSAE 18 SOC2 | Yes | Yes  
SSAE 18 SOC3 | Yes | Yes  
TISAX | Yes | No  
BAA coverage | Yes | No  
PCI-DSS in scope | Yes | No  
Enterprise SLA | 99.95% uptime | No  
  
## What's next

  * [Get started with Identity Platform](https://docs.cloud.google.com/identity-platform/docs/quickstart-cicp).
  * [Learn more about Firebase Authentication](https://firebase.google.com/docs/auth).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
