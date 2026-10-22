---
url: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policies-overview/
title: SAML policies overview \u00a0|\u00a0 Apigee \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:57:54.524327+00:00
---

# SAML policies overview  |  Apigee  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/saml-assertion-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Apigee ](https://docs.cloud.google.com/apigee/docs)
  * [ Reference ](https://docs.cloud.google.com/apigee/docs/reference/apis/apigee/rest)



Send feedback 

#  SAML policies overview Stay organized with collections  Save and categorize content based on your preferences. 

[Extensible policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types)

_This page applies to**Apigee** and **Apigee hybrid**._

_View[ Apigee Edge](https://docs.apigee.com/api-platform/get-started/what-apigee-edge) documentation._ ![](https://fonts.gstatic.com/s/i/googlematerialicons/help/v13/gm_grey-24dp/1x/gm_help_gm_grey_24dp.png)

The SAMLAssertion policies enable API proxies to validate SAML assertions that are attached to inbound SOAP requests, or to attach SAML assertions to outbound XML requests. The SAML policy validates incoming messages that contain a digitally-signed SAML assertion, rejects them if they are invalid, and sets variables that allow additional policies, or the backend services itself, to further validate the information in the assertion.

Apigee provides two SAML-related policies:

  * **Inbound authentication and authorization:[Validate SAML Assertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/validate-saml-assertion-policy)**  
The SAML policy type enables API proxies to validate SAML assertions that are attached to inbound SOAP requests. The SAML policy validates incoming messages that contain a digitally-signed SAML assertion, rejects them if they are invalid, and sets variables that allow additional policies, or the backend services itself, to further validate the information in the assertion.
  * **Outbound token generation:[Generate SAML Assertion policy](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/generate-saml-assertion-policy)**  
The SAML policy type enables API proxies to attach SAML assertions to outbound XML requests. Those assertions are then available to enable backend services to apply further security processing for authentication and authorization.



This policy is an _Extensible policy_ and use of this policy might have cost or utilization implications, depending on your Apigee license. For information on policy types and usage implications, see [Policy types](https://docs.cloud.google.com/apigee/docs/api-platform/reference/policies/reference-overview-policy#policy-types).

## Usage notes

The Security Assertion Markup Language (SAML) specification defines formats and protocols that enable applications to exchange XML-formatted information for authentication and authorization.

A "security assertion" is a trusted token that describes an attribute of an app, an app user, or some other participant in a transaction. Security assertions are managed and consumed by two types of entities:

  * Identity providers: Generate security assertions on behalf of participants
  * Service providers: Validate security assertions through trusted relationships with identity providers



The API platform can act as an identity provider and as a service provider. It acts as an identity provider by generating assertions and attaching them to request messages, making those assertions available for processing by backend services. It acts as a service provider by validating assertions on inbound request messages.

The SAML policy type supports SAML assertions that match version 2.0 of the SAML Core Specification and Version 1.0 of the WS-Security SAML Token Profile specification.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
