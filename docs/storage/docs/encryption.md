---
url: https://docs.cloud.google.com/storage/docs/encryption/
title: Data encryption options \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:31:37.237452+00:00
---

# Data encryption options  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Data encryption options Stay organized with collections  Save and categorize content based on your preferences. 

Cloud Storage always encrypts your data on the server side, before it is written to disk, at no additional charge. Besides this [standard, Cloud Storage behavior](https://docs.cloud.google.com/storage/docs/encryption/default-keys), there are additional ways to encrypt your data when using Cloud Storage. Below is a summary of the encryption options available to you:

_Server-side encryption_ : Encryption that occurs after Cloud Storage receives your data, but before the data is written to disk and stored.

  * [_Customer-managed encryption keys_ (CMEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-managed-keys): You can create and manage your encryption keys through [Cloud Key Management Service](https://docs.cloud.google.com/security-key-management). CMEK can be stored as software keys, in an [HSM cluster](https://docs.cloud.google.com/kms/docs/hsm), or [externally](https://docs.cloud.google.com/kms/docs/ekm).

  * [_Customer-supplied encryption keys_ (CSEK)](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys): You can create and manage your own encryption keys. These keys act as an additional encryption layer on top of the standard Cloud Storage encryption.




[_Client-side encryption_](https://docs.cloud.google.com/storage/docs/encryption/client-side-keys): Encryption that occurs before data is sent to Cloud Storage. Such data arrives at Cloud Storage already encrypted but also undergoes server-side encryption.

**Warning:** If you use customer-supplied encryption keys or client-side encryption, you must securely manage your keys and ensure that they are not lost. If you lose your keys, you are no longer able to read your data, and you continue to be charged for storage of your objects until you delete them.

## Comparing encryption options

Encryption method | Key management | Use case  
---|---|---  
**Standard (Default)** | Google manages the encryption keys. | **General purpose:** Cloud Storage's standard encryption is ideal for most users who need their data encrypted at rest without wanting to manage encryption keys. It satisfies many compliance requirements automatically.  
**CMEK** | You manage the keys using Cloud Key Management Service. | **Compliance and control:** Use CMEK when you need to control the lifecycle of your encryption keys to meet specific compliance standards (for example, PCI-DSS or HIPAA). You can grant, revoke, and rotate keys on your own schedule.  
**CSEK** | You provide your own encryption keys with each request to Cloud Storage. | **External key management:** CSEK is best for scenarios where you have an existing key management system outside of Google Cloud and you want to use those keys to encrypt your Cloud Storage data. The key is not stored by Google.  
**Client-side encryption** | You encrypt the data and manage the keys entirely on your own before sending it to Cloud Storage. | **Maximum secrecy:** Use client-side encryption when you need to ensure that Google has no possible access to the unencrypted data. This provides the highest level of control but also places the full burden of key management and the encryption and decryption processes on you.  
  
## What's next

  * [Configure which encryption methods are allowed or restricted](https://docs.cloud.google.com/storage/docs/encryption/enforce-encryption-types) for new objects in your buckets.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
