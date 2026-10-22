---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home/
title: OAuth 2.0 home \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:30:34.282640+00:00
---

# OAuth 2.0 home  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-home/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  OAuth 2.0 home Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

Welcome to the home page for OAuth 2.0 on Apigee. This landing page provides links to documentation, samples, and other resources related to using OAuth 2.0 on Apigee.

## The OAuth 2.0 framework

Secure your APIs with OAuth 2.0. This section lists resources, sample code, videos, and other topics to help you be successful using OAuth 2.0 on Apigee.

### Learn about OAuth 2.0

This collection of resources will help you get up to speed on OAuth 2.0. 

  * **Apigee documentation:**
    * [Introduction to OAuth 2.0](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-introduction) \-- Covers basic OAuth 2.0 concepts and terms. Focuses using OAuth 2.0 on Apigee.
  * **Apigee training and certifications:**
    * Apigee offers online training for API developers, including a course on [API security](https://www.coursera.org/learn/api-security-apigee-gcp), which includes OAuth 2.0.
  * **IETF Specification:**
    * [IETF Specification](https://tools.ietf.org/html/draft-ietf-oauth-v2-31) \-- Apigee highly recommends that you review this specification. It includes a good basic introduction and conceptual overview. 
  * **Apigee e-book:**
    * [ OAuth the Big Picture](https://cloud.google.com//apigee/resources/ebook/oauth-big-picture-register/), a free Apigee e-book. 



* * *

### Implement the grant type flows

The following topics explain how to implement the OAuth 2.0 grant types on Apigee: 

  * [Implementing the client credentials grant type](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-20-client-credentials-grant-type) \- Introduces the grant type, with an emphasis on the steps you need to follow to implement this grant type on Apigee. 
  * [Implementing the authorization code grant type](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/oauth-v2-policy-authorization-code-grant-type) \-- Introduces the grant type, with an emphasis on the steps you need to follow to implement this grant type on Apigee. 
  * [Use the implicit grant type](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens#requestinganaccesstokenimplicitgranttype) \-- Shows how to request tokens with the implicit grant type. 
  * [Implementing the password grant type](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/implementing-password-grant-type) \-- Introduces the grant type, with an emphasis on the steps you need to follow to implement this grant type on Apigee.



* * *

### How-to topics

These topics explain how to handle common OAuth 2.0 tasks in Apigee:

  * [OAuth 2.0: Configuring a new API proxy](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/understanding-default-oauth-20-configuration)
  * [Registering client apps](https://docs.cloud.google.com/apigee/docs/api-platform/security/registering-client-apps)
  * [Obtaining client credentials](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/obtaining-developer-keys)
  * [Understanding OAuth endpoints](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/configuring-oauth-endpoints-and-policies)
  * [Get OAuth 2.0 tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/access-tokens)
  * [Customizing tokens and authorization codes](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/customizing-access-tokens)
  * [Revoking and approving tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/validating-and-invalidating-access-tokens)
  * [Sending an access token](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/sending-access-token)
  * [Verifying access tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-access-tokens)
  * [Working with OAuth 2.0 scopes](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/working-scopes)
  * [Advanced OAuth 2.0 topics](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/advanced-oauth-20-topics)
  * [Using JWT OAuth 2.0 tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/using-jwt-oauth#refreshing-a-jwt-access-token)



### OAuth 2.0 policies

These policies allow you to perform OAuth 2.0 operations in an Apigee API proxy: 

  * [OAuthV2 policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/oauthv2-policy): The heart of the Apigee OAuth 2.0 implementation. It lets you configure OAuth 2.0 _operations_ on Apigee that generate access and refresh tokens, issue authorization codes, and validate tokens. This topic includes code samples to help illustrate how things work.
  * [GetOAuthV2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/get-oauth-v2-info-policy): Gets attributes of tokens and makes them available to policies and code executing in an API proxy. This policy type can be useful when you need to configure dynamic, conditional behavior based on a value in an access token. See also [Customizing access tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/customizing-access-tokens).
  * [SetOAuthV2Info policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/set-oauth-v2-info-policy): Updates the profile of an access token. For example, you may want to embed a tag that is unique to your business. See also [Customizing access tokens](https://docs.cloud.google.com/apigee/docs/api-platform/security/oauth/customizing-access-tokens).



* * *

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
