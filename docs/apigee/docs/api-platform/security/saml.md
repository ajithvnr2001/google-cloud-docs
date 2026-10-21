---
url: https://docs.cloud.google.com/apigee/docs/api-platform/security/saml/
title: Using SAML policies in an API proxy \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:56:33.289279+00:00
---

# Using SAML policies in an API proxy  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/security/saml/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Guides ](https://docs.cloud.google.com/apigee/docs/api-platform/get-started/what-apigee)



Send feedback 

#  Using SAML policies in an API proxy Stay organized with collections  Save and categorize content based on your preferences. 

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

## Security Assertion Markup Language (SAML)

The [Security Assertion Markup Language (SAML)](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language) specification defines formats and protocols that enable applications to exchange XML-formatted information for authentication and authorization.

Apigee API Services enables you to authenticate and authorize apps that are capable of presenting SAML tokens. A SAML token is a digitally signed fragment of XML that presents a set of "assertions". These assertions can be used to enforce authentication and authorization.

To use SAML terminology, API Services can function as a service provider (SP) or an Identity Provider (IDP). When API Services validates SAML tokens on inbound requests from apps, it acts in the role of SP. (API Services can also act in the IDP role, when generating SAML tokens to be used when communicating with backend services. See [Last-mile security](https://docs.cloud.google.com/apigee/docs/api-platform/security/last-mile-security)).

The SAML policy type enables API proxies to validate SAML assertions that are attached to inbound SOAP requests. The SAML policy validates incoming messages that contain a digitally-signed SAML assertion, rejects them if they are invalid, and sets variables that allow additional policies, or the backend services itself, to further validate the information in the assertion.

To validate SAML tokens, you need to make digital certificates available to the SAML policy by creating at least one TrustStore. TrustStores are scoped to environments in your organizations. Thus, you can configure different trust chains in test and prod, ensuring that test SAML tokens cannot be used in prod, and vice-versa.

For details on SAML validation, see [SAML Assertion policies](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policy).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
