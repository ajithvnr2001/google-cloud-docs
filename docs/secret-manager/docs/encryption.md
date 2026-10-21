---
url: https://docs.cloud.google.com/secret-manager/docs/encryption/
title: Encryption of secrets \u00a0|\u00a0 Secret Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T05:40:21.563616+00:00
---

# Encryption of secrets  |  Secret Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/docs/encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)



Send feedback 

#  Encryption of secrets Stay organized with collections  Save and categorize content based on your preferences. 

Secret Manager always encrypts your secret data before it is persisted to disk. This page discusses the default encryption that Secret Manager performs. To learn more about Google Cloud encryption options, refer to [Encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

Secret Manager manages server-side encryption keys on your behalf using the same hardened key management systems that we use for our own encrypted data, including strict key access controls and auditing. Secret Manager encrypts user data at rest using AES-256. There is no setup or configuration required, no need to modify the way you access the service, and no visible performance impact. Your secret data is automatically and transparently decrypted when accessed by an authorized user.

The Secret Manager API always communicates over a secure HTTP(S) connection.

## Customer-managed encryption keys (CMEK)

Customer-managed encryption keys (CMEK) refers to the ability to control and manage the encryption keys used to protect data related to a Google Cloud service.

See [CMEK documentation](https://docs.cloud.google.com/secret-manager/docs/cmek) for details on how to configure and use customer-managed encryption keys.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
