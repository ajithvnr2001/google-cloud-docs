---
url: https://docs.cloud.google.com/contact-center/ccai-platform/docs/authentication-context/
title: Authentication context \u00a0|\u00a0 Google Cloud Contact Center as a Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T16:20:28.977988+00:00
---

# Authentication context  |  Google Cloud Contact Center as a Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/contact-center/ccai-platform/docs/authentication-context/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Google Cloud CCaaS ](https://docs.cloud.google.com/contact-center/ccai-platform/docs)
  * [ User Guides ](https://docs.cloud.google.com/contact-center/ccai-platform/docs/get-started)



Send feedback 

#  Authentication context Stay organized with collections  Save and categorize content based on your preferences. 

When configuring external authentication, authentication context refers to the level of authentication requested. For example, `PasswordProtectedTransport` specifies that the authentication method must be through a secure, password-protected transport, enhancing security during the authentication process.

You set the authentication context when you configure your Contact Center AI Platform (CCAI Platform) instance for single sign-on (SSO). For more information about SSO for CCAI Platform, see [Single sign-on (SSO)](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso). For an example of configuring an instance for SSO, including setting the authentication context, see [Configure your CCAI Platform instance for SSO](https://docs.cloud.google.com/contact-center/ccai-platform/docs/sso-saml#configure-instance-for-sso-saml).

The following authentication contexts are available:

  * `AuthenticatedTelephony`: Telephony services requiring user verification for access.

  * `InternetProtocol`: Rules for formatting data sent over the internet or networks.

  * `InternetProtocolPassword`: A password related to an internet protocol for authentication.

  * `Kerberos`: A protocol using secret-key cryptography for client and server authentication.

  * `MobileOneFactorContract`: A mobile authentication agreement using one security factor, like a password.

  * `MobileOneFactorUnregistered`: Mobile authentication without prior registration, using a single factor.

  * `MobileTwoFactorContract`: An agreement for mobile authentication that requires two security factors.

  * `MobileTwoFactorUnregistered`: Mobile authentication with two factors, without registration.

  * `NomadTelephony`: Telephony services for users frequently changing locations or devices.

  * `Password`: Characters used to verify a user's identity.

  * `PasswordProtectedTransport`: Protecting data during transmission with a password.

  * `PersonalTelephony`: Telephony services for individual rather than business use.

  * `PGP`: Encryption program for secure data transmission.

  * `PreviousSession`: A session that took place before the current one.

  * `SmartCard`: A card with an embedded microchip for data storage and processing.

  * `SmartCardPKI`: Using smart cards in public key infrastructure for digital certificate management.

  * `SoftwarePKI`: Managing digital certificates with software.

  * `SPKI`: A framework for managing public keys and digital certificates.

  * `SecureRemotePassword`: A protocol for secure password authentication over a network.

  * `Telephony`: Technology for transmitting voice, video, or data over a distance.

  * `TimeSyncToken`: A device or mechanism for synchronizing time across different devices or systems.

  * `TLSClient`: Client side of the TLS protocol for secure communication.

  * `Unspecified`: Not detailed or mentioned explicitly.

  * `X509`: A standard for public key certificates in secure communication.

  * `XMLDSig`: A spec for digitally signing XML documents for integrity and authentication.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
