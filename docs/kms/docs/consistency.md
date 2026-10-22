---
url: https://docs.cloud.google.com/kms/docs/consistency/
title: Cloud KMS resource consistency \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:09:36.483218+00:00
---

# Cloud KMS resource consistency  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/consistency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Cloud KMS resource consistency Stay organized with collections  Save and categorize content based on your preferences. 

This document provides information about the impact of consistency when Cloud KMS resources are created or modified.

Some operations to Cloud Key Management Service resources are strongly consistent, while others are eventually consistent. Eventually consistent operations typically propagate within 1 minute, but may take several hours in exceptional cases.

**Note:** Fast "eventually consistent" operations are in **Preview** , meaning there may be times where operations become consistent in a time longer than what is documented.

## Consistency of key rings

Creating a key ring is a strongly consistent operation. Upon creation, a key ring is instantly available for use.

## Consistency of keys

Creating a key is a strongly consistent operation. Upon creation, a key is instantly available for use.

## Consistency of key versions

Enabling a key version is a strongly consistent operation. The enabled key version is instantly available for encrypting and decrypting data.

Disabling a key version is an eventually consistent operation. The key version typically remains usable for encrypting and decrypting data for up to 1 minute after it is disabled. In exceptional cases, the key version remains usable for several hours after it is disabled. See the [Service Health dashboard](https://status.cloud.google.com/) for Cloud KMS data freshness issues.

Changing the primary key version, manually or during key rotation, is an eventually consistent operation. While such eventually-consistent changes propagate, `Encrypt` operations for a `CryptoKey` might use the `CryptoKey`'s previous primary version to encrypt.

## Impact of changing IAM access

If you need to prevent a user from using a Cloud KMS resource during the time needed for propagation of an eventually consistent operation, remove the Identity and Access Management (IAM) permission for the resource. For example, you can prevent a user from using a newly-disabled key version by removing the IAM role that allows the user to access the key. IAM changes are consistent within seconds; to learn more, see [Access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
