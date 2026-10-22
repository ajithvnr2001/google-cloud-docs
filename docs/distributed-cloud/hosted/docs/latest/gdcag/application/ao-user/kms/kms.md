---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/kms/
title: Key management system \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:57:46.364317+00:00
---

# Key management system  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/kms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Key management system Stay organized with collections  Save and categorize content based on your preferences. 

The Key Management System (KMS) service centrally manages cryptographic keys and runs in the Management API server. The Application Operator (AO) creates, uses, and destroys the keys in the KMS.

## Supported keys

KMS supports the following keys:

Key primitive | Key primitive (API) | Description | Default algorithm  
---|---|---|---  
`AEAD` | `aeadkey` | The authenticated encryption with associated data (`AEAD`) key that performs authenticated encryption using `AES-256`.  
  
The key's components represent the following:   


  * `AES-256`: the 256-bit Advanced Encryption Standard (AES) symmetric key algorithm. This algorithm is the default algorithm.

| `AES_256_GCM`  
`Signing` | `signingkey` | The signing key that provides asymmetric signing using elliptic curve support.   
  
The key's components represent the following:   


  * `EC`: the elliptic curve key.


  * `P384`: the size of the EC curve.


  * `SHA384`: the digest algorithm used in signing. This algorithm is the default algorithm.

| `EC_SIGN_P384_SHA384`  
  
## Key features

The AO centrally manages symmetric and asymmetric cryptographic keys with the AEAD and Signing keys. Through the KMS Creator role, the AO has the ability to [create](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#create) keys.

Through the KMS Admin role, the AO can [use](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#create), [destroy](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/create-delete-keys#delete), [import](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/import-key), and [export](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/import-key) aeadkey and signingkey cryptographic keys.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
