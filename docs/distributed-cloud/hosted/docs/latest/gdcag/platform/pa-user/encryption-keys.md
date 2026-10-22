---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-keys/
title: Client-side encryption \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T13:32:51.577522+00:00
---

# Client-side encryption  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/encryption-keys/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Client-side encryption Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** To access the URLs listed on this page, you must connect to the internet. The URLs are provided to access outside of your air-gapped environment.

This page discusses _client-side encryption_ , which is any data encryption you perform prior to sending your data to Cloud Storage.

When you perform client-side encryption, you must create and manage your own encryption keys, and use your own tools to encrypt data prior to sending it to Cloud Storage. Data that you encrypt on the client side arrives at Cloud Storage in an encrypted state. Google Distributed Cloud (GDC) air-gapped has no knowledge of the keys you use to encrypt the data.

When GDC receives your data, it encrypts the data a second time. This second encryption is _server-side encryption_ , which GDC manages. When you retrieve your data, GDC removes the server-side layer of encryption. You must decrypt the client-side layer yourself.

**Warning:** GDC does not know if your data has already encrypted on the client side and has no knowledge of your client-side encryption keys. You must securely manage your client-side keys and ensure that they are not lost. If you lose your keys, you are no longer able to read your data. You continue to receive charges for storage of your objects until you delete them.

## Use multiple encryption methods

Depending on your requirements, use more than one encryption method at a time. For example:

  * Use a KMS to protect appliance nodes and also use a drive security feature to _double encrypt_ data on the self-encrypting drives in the same appliances.
  * Use a KMS to secure data on appliance nodes and also an option to encrypt all objects when they are ingested.



If only a small portion of your objects require encryption, consider controlling encryption at the bucket or individual object level instead. Enabling multiple levels of encryption has an additional performance cost.

## GDC data encryption

GDC Storage encrypts your data on the server side, before it writes the data to disk, at no additional charge. Besides this standard, Google-managed behavior, there are additional ways to encrypt your data when using GDC Storage.

An encryption option available to you is the client-side encryption, an encryption that occurs before data goes to GDC Storage. Such data arrives at GDC Storage encrypted, and undergoes server-side encryption.

**Warning:** If you use client-side encryption, you must securely manage your keys and ensure they are not lost. If you lose your keys, you can no longer read your data. GDC continues to charge you for the storage of your objects until you delete them.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
