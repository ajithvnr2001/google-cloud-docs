---
url: https://docs.cloud.google.com/access-context-manager/docs/understand-mtls/
title: Understand mutual TLS at Google Cloud \u00a0|\u00a0 Access Context Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:17:53.152504+00:00
---

# Understand mutual TLS at Google Cloud  |  Access Context Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/access-context-manager/docs/understand-mtls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Access Context Manager ](https://docs.cloud.google.com/access-context-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/access-context-manager/docs/create-access-level)



Send feedback 

#  Understand mutual TLS at Google Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Mutual TLS (mTLS) is an industry standard protocol for mutual authentication between a client and a server. The mTLS protocol ensures that both the client and server, at each end of a network connection, are who they claim they are by verifying that both possess the private key associated with the client certificate.

### What is a client certificate?

A client certificate, also called a Transport Layer Security (TLS) certificate, is a file that contains important information for verifying a device's identity. The certificate information includes the public key, a statement of who issued the certificate (certificates can be issued by certificate authorities or self- signed), and the certificate's expiration date.

### How the Google APIs validate device identity

The TLS protocol uses a technique called public key infrastructure (PKI), which relies on a pair of asymmetric keys: a public key and a private key. Anything encrypted with the private key can be decrypted only with the public key. The Google Cloud APIs use the TLS protocol to verify the identity of a device by decrypting the message encrypted by the private key using the public key of the certificate during the mTLS handshake. The successful decryption proves the possession of the private key which is only available from trusted devices.

To enable the mTLS handshake and validation process, a client must do the following:

  * Establish an mTLS connection with the Google APIs by using mTLS-specific API endpoints. The mTLS-specific endpoints have the following format: `[service].mtls.googleapis.com`

  * Discover and use the device certificate during the mTLS handshake. If you are using Endpoint Verification for certificate deployment, this type of certificate is automatically discovered and used by the supported clients.




The following diagram illustrates the mTLS handshake between a client and a Google API server:

![mTLS handshake between a client and a
Google API server](https://docs.cloud.google.com/access-context-manager/images/mtls-handshake.svg)

## What's next

  * [Set up certificate-based access](https://docs.cloud.google.com/access-context-manager/docs/set-up-cba)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
