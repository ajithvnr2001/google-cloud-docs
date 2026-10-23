---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/cmek/
title: Customer-managed encryption keys (CMEK) \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:31.765512+00:00
---

# Customer-managed encryption keys (CMEK)  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/cmek/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  Customer-managed encryption keys (CMEK) Stay organized with collections  Save and categorize content based on your preferences. 

By default, Customer Experience Agent Studio encrypts customer content at rest. CX Agent Studio handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. Google default encryption uses the same hardened key management systems that we use for our own encrypted data. These systems include strict key access controls and auditing.

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including CX Agent Studio. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your CX Agent Studio resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

## Protected data

All agent application [data-at-rest](https://en.wikipedia.org/wiki/Data_at_rest) can be protected with CMEKs.

## Limitations

  * Key rotation is supported but data re-encryption is not. That is, re-encrypting previously encrypted data with a new key version is not supported.
  * One key should be used per project location.
  * Existing resources in non-CMEK integrated projects cannot be CMEK integrated retroactively. Instead, it is recommended that resources be exported and restored in a new project for CMEK.



## Manage keys

Key management (create, enable, and revoke) is handled by using the [Conversational Insights API](https://docs.cloud.google.com/contact-center/insights/docs/cmek).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
