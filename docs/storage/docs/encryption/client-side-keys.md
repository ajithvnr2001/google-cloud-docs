---
url: https://docs.cloud.google.com/storage/docs/encryption/client-side-keys/
title: Client-side encryption keys \u00a0|\u00a0 Cloud Storage \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:51.545142+00:00
---

# Client-side encryption keys  |  Cloud Storage  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/storage/docs/encryption/client-side-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Cloud Storage ](https://docs.cloud.google.com/storage/docs)
  * [ Guides ](https://docs.cloud.google.com/storage/docs/discover-object-storage-console)



Send feedback 

#  Client-side encryption keys Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses _client-side encryption_ , which is any data encryption you perform prior to sending your data to Cloud Storage. For other encryption options, see [Data Encryption Options](https://docs.cloud.google.com/storage/docs/encryption).

When you perform client-side encryption, you must create and manage your own encryption keys, and you must use your own tools to encrypt data prior to sending it to Cloud Storage. Data that you encrypt on the client side arrives at Cloud Storage in an encrypted state, and Cloud Storage has no knowledge of the keys you used to encrypt the data.

When Cloud Storage receives your data, it is encrypted a second time. This second encryption is called _server-side encryption_ , which Cloud Storage manages. When you retrieve your data, Cloud Storage removes the server-side layer of encryption, but you must decrypt the client-side layer yourself.

You can use the open source cryptographic SDK, Tink, to perform client-side encryption, then protect your keys with Cloud Key Management Service. For more details, see [Client-side encryption with Tink and Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/client-side-encryption).

**Warning:** Cloud Storage doesn't know if your data has already been encrypted on the client side and has no knowledge of your client-side encryption keys. You must securely manage your client-side keys and ensure that they are not lost. If you lose your keys, you are no longer able to read your data, and you continue to be charged for storage of your objects until you delete them.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
