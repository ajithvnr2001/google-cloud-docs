---
url: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/workforce-identity-federation-apigee/
title: Access Apigee using Workforce Identity Federation \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:28:25.609961+00:00
---

# Access Apigee using Workforce Identity Federation  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/system-administration/workforce-identity-federation-apigee/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Access Apigee using Workforce Identity Federation Stay organized with collections  Save and categorize content based on your preferences. 

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

This page describes how to use a third-party identity provider to access Apigee with [Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). Workforce Identity Federation lets you use an external identity provider (IdP) to authenticate and authorize a workforce — a group of users, such as employees, partners, and contractors — using [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) to access Apigee services.

You can use Workforce Identity Federation with any IdP that supports [OpenID Connect (OIDC)](https://openid.net/connect/) or [SAML 2.0](https://docs.oasis-open.org/security/saml/Post2.0/sstc-saml-tech-overview-2.0.html), such as Azure Active Directory (Azure AD), Active Directory Federation Services (AD FS), Okta, and others.

## Benefits of using Workforce Identity Federation

We understand that many Apigee customers already use some form of single sign-on (SSO), allowing their employees to sign-in using existing corporate credentials. Many of our customers also maintain an identity management system. Synchronizing user identities from your existing IdP to Google Cloud identities can be challenging and time-consuming.

Using Workforce Identity Federation can decrease Apigee onboarding time and streamline your identity and security processes by removing the need to synchronize user identities from your existing IdP to Google Cloud identities. Workforce Identity Federation can be used across Google Cloud and provides a single point of control for managing access to Apigee.

## Supported Apigee organization types

You can use Workforce Identity Federation to access and manage resources in any Apigee [Subscription](https://docs.cloud.google.com/apigee/docs/api-platform/reference/subscription-entitlements) or [Pay-as-you-go](https://docs.cloud.google.com/apigee/docs/api-platform/reference/pay-as-you-go-updated-overview) organization, including [Apigee hybrid](https://docs.cloud.google.com/apigee/docs/hybrid/v1.12/what-is-hybrid)-enabled organizations. Workforce Identity Federation users can also create and manage Apigee [evaluation organizations](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/compare-paid-eval).

## Limitations and considerations

Before using Workforce Identity Federation with Apigee, consider the limitations described below. Apigee support for Workforce Identity Federation is also described in the [ Identity federation: products and limitations](https://docs.cloud.google.com/iam/docs/federated-identity-supported-services#apigee) documentation. 

### Accessing the Apigee UI

You can use Workforce Identity Federation to access Apigee services using the [Apigee UI](https://console.cloud.google.com/apigee), or via the Apigee APIs.

### Preview features

Some Apigee features in [Preview](https://cloud.google.com/products#product-launch-stages) may not be available to Workforce Identity Federation users. All Generally Available (GA) features accessible in the Apigee UI will be available to Workforce Identity Federation users.

### Unsupported features

The following Apigee features are not supported for Workforce Identity Federation users: 

  * Workforce Identity Federation users cannot use Cloud Code and the [Visual Studio Code (VS Code) IDE](https://code.visualstudio.com/) for [local development](https://docs.cloud.google.com/apigee/docs/api-platform/local-development/overview) of Apigee APIs and API proxies.
  * The Apigee Connect API (`apigeeconnect.googleapis.com`) is not supported for Workforce Identity Federation users with Apigee hybrid organizations.



## Use Apigee UI as a Workforce Identity Federation user

Workforce Identity Federation users can sign in to Apigee using one of three methods: 

  * [Using an SSO link](https://docs.cloud.google.com/iam/docs/workforce-console-sso#inform-users)
  * [Using the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso#initiate-console)
  * [Using IdP-initiated sign-in](https://docs.cloud.google.com/iam/docs/workforce-console-sso#initiate-console)



Ask your Apigee administrator to determine which method you should use.

Detailed information about each sign-in method is available in the [Set up user access to the console (federated)](https://docs.cloud.google.com/iam/docs/workforce-console-sso) documentation.

## Use the Apigee APIs as a Workforce Identity Federation user

Before you can access the Apigee APIs as a Workforce Identity Federation user, you must obtain a short-lived token from the Security Token Service (STS). Once you have a token, you can access the Apigee APIs with no additional steps.

For more information, see [ Obtain short-lived tokens for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#use_the_rest_api).

## Use the Google Cloud CLI as a Workforce Identity Federation user

Before you can use the Google Cloud CLI (gcloud CLI) as a Workforce Identity Federation user, you must obtain a short-lived token from the Security Token Service (STS). Once you have a token, you can use the gcloud CLI libraries with no additional steps.

For more information, see [ Obtain short-lived tokens for Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-obtaining-short-lived-credentials#use_the_client_libraries).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
