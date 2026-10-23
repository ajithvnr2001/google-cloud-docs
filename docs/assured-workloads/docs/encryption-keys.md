---
url: https://docs.cloud.google.com/assured-workloads/docs/encryption-keys/
title: Data encryption and encryption keys \u00a0|\u00a0 Assured Workloads \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:20:29.617625+00:00
---

# Data encryption and encryption keys  |  Assured Workloads  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/assured-workloads/docs/encryption-keys/

The names for some Assured Workloads control packages have changed. For information about the name change, see [Control package renaming notice](https://docs.cloud.google.com/assured-workloads/docs/overview#name-change). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Assured Workloads ](https://docs.cloud.google.com/assured-workloads/docs)
  * [ Guides ](https://docs.cloud.google.com/assured-workloads/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Data encryption and encryption keys

This page provides information about encryption of data on Google Cloud and about encryption keys.

## Encryption in transit and at rest

Google Cloud enables [encryption in transit](https://docs.cloud.google.com/security/encryption-in-transit) by default to encrypt requests before transmission and to protect the raw data using the Transport Layer Security (TLS) protocol.

Once data is transferred to Google Cloud to be stored, Google Cloud applies [encryption at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) by default. To gain more control over how data is encrypted at rest, Google Cloud customers can use [Cloud Key Management Service](https://docs.cloud.google.com/kms) to generate, use, rotate, and destroy encryption keys according to their own policies. These keys are called customer-managed encryption keys ([CMEK](https://docs.cloud.google.com/kms/docs/cmek)).

For certain control packages, Assured Workloads can deploy a CMEK project alongside your [resources project](https://docs.cloud.google.com/assured-workloads/docs/key-concepts#resources) when you create an Assured Workloads folder.

As an alternative to CMEK, Google-owned and Google-managed encryption keys, provided by default, are [FIPS-140-2](https://csrc.nist.gov/publications/detail/fips/140/2/final) compliant and are able to support most control packages in Assured Workloads. Customers can delete the CMEK project and rely solely on Google-owned and Google-managed encryption keys. We recommend, however, that you decide whether to use CMEK keys before you create your Assured Workloads folder as deletion of existing in-use CMEK can result in inability to access or recover data.

## Customer-managed encryption keys (CMEK)

If you need more control over the keys used to encrypt data at rest within a Google Cloud project than what Google Cloud's default encryption provides, Google Cloud services offer the ability to protect data by using encryption keys managed by the customer within Cloud KMS. These encryption keys are called customer-managed encryption keys (CMEK).

To learn which aspects of the lifecycle and management of your keys that CMEK provides, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek) in Cloud KMS documentation. For a tutorial that guides you through managing keys and encrypted data using Cloud KMS, see the [quickstart](https://docs.cloud.google.com/kms/docs/quickstart) or [codelab](https://codelabs.developers.google.com/codelabs/encrypt-and-decrypt-data-with-cloud-kms).

## What's next

  * Learn more about [creating a symmetrical key with Cloud KMS](https://docs.cloud.google.com/kms/docs/creating-keys).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
