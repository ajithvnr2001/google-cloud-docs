---
url: https://docs.cloud.google.com/storage/docs/encryption/default-keys/
title: Standard Cloud Storage encryption \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:30:30.396236+00:00
---

# Standard Cloud Storage encryption  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/default-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Standard Cloud Storage encryption Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage always encrypts your data on the server side, before it is written to disk, at no additional charge. This page discusses the standard encryption that Cloud Storage performs. For other encryption options, see [Data Encryption Options](https://docs.cloud.google.com/storage/docs/encryption).

Cloud Storage manages server-side encryption keys on your behalf using the same hardened key management systems that we use for our own encrypted data, including strict key access controls and auditing. Cloud Storage encrypts user data at rest using [AES-256](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard), in most cases using [Galois/Counter Mode (GCM)](http://wikipedia.org/wiki/Galois/Counter_Mode). There is no setup or configuration required, no need to modify the way you access the service, and no visible performance impact. Data is automatically decrypted when read by an authorized user.

For more information about how Google Cloud and Cloud Storage manage encryption keys, see [Default encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption).

To protect your data as it travels over the Internet during read and write operations, use Transport Layer Security, commonly known as TLS or HTTPS.

## What's next

  * Learn more about [Choosing an encryption option](https://docs.cloud.google.com/storage/docs/encryption).

  * For more information about how Google-owned and Google-managed encryption keys are rotated, managed, and stored, see [Key management](https://docs.cloud.google.com/docs/security/encryption/default-encryption#key_management).

  * See [Encryption at the storage system layer](https://docs.cloud.google.com/docs/security/encryption/default-encryption#hardware) to learn about the encryption modes that are used in Google Cloud.

  * [Configure which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in your buckets.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
