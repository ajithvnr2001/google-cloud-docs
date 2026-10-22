---
url: https://docs.cloud.google.com/datastore/docs/concepts/encryption-at-rest/
title: Server-Side Encryption \u00a0|\u00a0 Firestore in Datastore mode \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:40:21.994677+00:00
---

# Server-Side Encryption  |  Firestore in Datastore mode  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastore/docs/concepts/encryption-at-rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Firestore in Datastore mode ](https://docs.cloud.google.com/datastore/docs)
  * [ Guides ](https://docs.cloud.google.com/datastore/docs/concepts/overview)



Send feedback 

#  Server-Side Encryption Stay organized with collections  Save and categorize content based on your preferences. 

Firestore in Datastore mode automatically encrypts all data before it is written to disk. There is no setup or configuration required and no need to modify the way you access the service. The data is automatically and transparently decrypted when read by an authorized user.

## Key management

With server-side encryption, you can either let Google manage cryptographic keys on your behalf or use customer-managed encryption keys (CMEK) to manage the keys yourself.

By default, Google manages cryptographic keys on your behalf using the same hardened key management systems that we use for our own encrypted data, including strict key access controls and auditing. Each Datastore mode object's data and metadata is [encrypted](https://docs.cloud.google.com/security/encryption/default-encryption) and each encryption key is itself encrypted with a regularly rotated set of keystore master keys.

For information about managing the keys yourself, see [CMEK for Datastore](https://docs.cloud.google.com/datastore/docs/cmek).

## Client-side encryption

Server-side encryption can be used in combination with client-side encryption. In client-side encryption, you manage your own encryption keys and encrypt data before writing it to your database. In this case, your data is encrypted twice, once with your keys and once with the server-side keys.

**Warning:** Firestore in Datastore mode does not know if your data has already been encrypted client-side, nor does Datastore mode have any knowledge of your client-side encryption keys. If you use client-side encryption, you must securely manage your encryption keys.

To protect your data as it travels over the Internet during read and write operations, we use Transport Layer Security (TLS). For more information about the supported TLS versions, see [Encryption in transit in Google Cloud](https://docs.cloud.google.com/docs/security/encryption-in-transit#user_to_google_front_end_encryption).

## What's next

For more information about encryption at rest for Firestore in Datastore mode and other Google Cloud products, see [Encryption at Rest in Google Cloud](https://docs.cloud.google.com/security/encryption/default-encryption).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
