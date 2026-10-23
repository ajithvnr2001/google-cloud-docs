---
url: https://docs.cloud.google.com/speech-to-text/docs/encryption/
title: Introduction to encryption for Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:51:33.852407+00:00
---

# Introduction to encryption for Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)



Send feedback 

#  Introduction to encryption for Cloud Speech-to-Text Stay organized with collections  Save and categorize content based on your preferences. 

By default, Cloud Speech-to-Text encrypts customer content at rest. Cloud STT handles encryption for you without any additional actions on your part. This option is called _Google default encryption_. 

If you want to control your encryption keys, then you can use customer-managed encryption keys (CMEKs) in [Cloud KMS](https://docs.cloud.google.com/kms/docs) with CMEK-integrated services including Cloud STT. Using Cloud KMS keys gives you control over their protection level, location, rotation schedule, usage and access permissions, and cryptographic boundaries. Using Cloud KMS also lets you view audit logs and control key lifecycles. Instead of Google owning and managing the symmetric [key encryption keys (KEKs)](https://docs.cloud.google.com/kms/docs/envelope-encryption#key_encryption_keys) that protect your data, you control and manage these keys in Cloud KMS.

After you set up your resources with CMEKs, the experience of accessing your Cloud STT resources is similar to using Google default encryption. For more information about your encryption options, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

For information about the specific benefits of using CMEK with Cloud Speech-to-Text resources, see Understand CMEK for Cloud STT resources. 

## Understand CMEK for Cloud STT resources

The following conditions are true when a new key is set by using the Speech-to-Text API:

  * Resources previously encrypted with the original key remain encrypted with that earlier key. If a resource is updated (using an `Update*` method), it is re-encrypted with the new key.
  * Previously non-CMEK encrypted resources remain unencrypted. If a resource is updated (using an `Update*` method), it is then re-encrypted with the new key. For long-running operations (like [batch recognition](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize)), if processing is ongoing and not finished, the stored operation is re-encrypted with the new key.
  * Newly created resources are encrypted with the newly set key.



When you remove a key by using the Speech-to-Text API, new resources are created without CMEK encryption. Existing resources remain encrypted with the keys with which they were previously encrypted. If a resource is updated (using an `Update*` method), it is re-encrypted using the default encryption managed by Google. For long-running operations (like [batch recognition](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize)), if processing is ongoing and not finished, the stored operation will be re-encrypted using the default encryption managed by Google.

The location of the Cloud KMS key used for encrypting Cloud STT resources must match the Cloud STT endpoint used. For more information about Cloud STT locations, see [Cloud STT locations](https://docs.cloud.google.com/speech-to-text/docs/locations). For more information about Cloud KMS locations, see [Cloud KMS locations](https://docs.cloud.google.com/kms/docs/locations).

## CMEK-supported resources

The following are current Cloud Speech-to-Text resources covered by CMEK:

Resource | Material encrypted | Documentation links  
---|---|---  
[Recognizer](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#recognizer) | 

  * The language code in the recognition configuration.
  * Inline and reference adaptation resources.

| 

  * [Recognizers](https://docs.cloud.google.com/speech-to-text/docs/recognizers)
  * [Adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model)

  
[PhraseSet](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#phraseset) | 

  * Phrases in the phrase set.

| 

  * [Adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model)

  
[CustomClass](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.cloud.speech.v2#customclass) | 

  * Class items in the custom class.

| 

  * [Adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model)

  
[Operation](https://docs.cloud.google.com/speech-to-text/docs/reference/rpc/google.longrunning#operation) | 

  * The original request that spawned the operation.
  * The response from the method that spawned the operation.

| 

  * [Recognizers](https://docs.cloud.google.com/speech-to-text/docs/recognizers)
  * [Adaptation](https://docs.cloud.google.com/speech-to-text/docs/adaptation-model)
  * [Operations](https://docs.cloud.google.com/speech-to-text/docs/operations)

  
[Batch recognition artifacts](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize) | 

  * Adaptation resources used during transcription.
  * The accumulated transcript results.
  * Audio artifacts required for transcription.

| 

  * [Batch recognition](https://docs.cloud.google.com/speech-to-text/docs/batch-recognize)

  
  
## What's next

  * Learn [how to use encryption with Cloud STT](https://docs.cloud.google.com/speech-to-text/docs/how-to-encryption).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
