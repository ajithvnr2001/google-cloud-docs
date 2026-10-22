---
url: https://docs.cloud.google.com/integration-connectors/docs/encryption/
title: Encryption methods \u00a0|\u00a0 Integration Connectors \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:38.299923+00:00
---

# Encryption methods  |  Integration Connectors  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/integration-connectors/docs/encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Integration Connectors ](https://docs.cloud.google.com/integration-connectors/docs)
  * [ Guides ](https://docs.cloud.google.com/integration-connectors/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Encryption methods

Encryption is a defensive mechanism that helps protect the privacy of your data stored in Google Cloud. Using encryption ensures that the data stored in Google Cloud is protected against malicious attacks or breaches which might lead to compromising the security of your entire project or organization. 

To know more about how encryption is handled in Google Cloud, see [Encryption](https://docs.cloud.google.com/docs/security/overview/whitepaper#encryption). 

Integration Connectors is a regional service and the infrastructure that runs your connections is located in the associated provisioned regions. To provision a new region, in the console, go to **Integration Connectors**

Compliant with Google Cloud's security standards for storing [customer data](https://docs.cloud.google.com/docs/security/encryption/default-encryption#what_is_customer_data), Integration Connectors automatically encrypts the data using one of the following data encryption methods: 

  * Google-owned and Google-managed encryption keys
  * Customer-managed encryption key



## Google-owned and Google-managed encryption keys

By default, Integration Connectors automatically encrypts data at rest using Google-owned and Google-managed encryption keys. These encryption keys are handled by Google and are encrypted using the [Advanced Encryption Standard (AES) algorithm](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard), AES-256. You don't have to perform any actions or configuration changes to use Google-owned and Google-managed encryption keys for Integration Connectors. For more information, see [Default encryption at rest](https://docs.cloud.google.com/security/encryption-at-rest/default-encryption). 

## Customer-managed encryption key

In addition to the standard, Google-owned and Google-managed encryption keys method, you can also use [Cloud Key Management Service (KMS)](https://cloud.google.com/security/products/security-key-management) or Customer-managed encryption keys to encrypt and decrypt your data at rest. These encryption keys are created, managed, and owned by you. For more information, see [Customer-managed encryption keys](https://docs.cloud.google.com/integration-connectors/docs/cmek). 

## Encrypted data

The following table lists the data encrypted in Integration Connectors: 

Resource | Encrypted data  
---|---  
Incoming events from your backend to the connection | Event payload  
Connections | Connection execution metadata  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
