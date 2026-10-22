---
url: https://docs.cloud.google.com/kms/docs/mac-signatures/
title: MAC signatures \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:46.093191+00:00
---

# MAC signatures  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/mac-signatures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  MAC signatures Stay organized with collections  Save and categorize content based on your preferences. 

A _MAC signature_ is a cryptographic output used to verify the integrity and authenticity of data. A MAC signature algorithm lets you perform two distinct operations:

  * A signing operation, which uses a signing key to produce a MAC signature over raw data.

  * A verification operation, where the authenticity of the message can be validated given the signing key and the MAC tag to be verified.




There are two main purposes of a MAC signature:

  * Verify the integrity of the signed data.
  * Verify the authenticity of the message.



While the purpose of MAC signatures is similar to that of digital signatures, MAC signatures rely on symmetric cryptography. MAC tags are generated and verified using the same secret key. The sender and the receiver of a message must both have the same key to use MAC signatures.

**Note:** Since the sender and the receiver have the same cryptographic material, you can't use MAC tags to prove which of the two signed the file. If you need to be able to verify that the message was signed by the sender, use [digital signatures based on asymmetric keys](https://docs.cloud.google.com/kms/docs/digital-signatures) instead.

## Example use case for a MAC signature

MAC algorithms like keyed-hash message authentication code (HMAC) are an excellent file transfer data integrity-checking mechanism because of their efficiency. Hash functions can take a message of arbitrary length and transform it into a fixed-length digest, thus maximizing bandwidth usage.

## MAC signing workflow

The following describes the flow for creating and validating a signature. The two participants in this workflow consist of the signer of data, and the data recipient.

  1. The signer and the recipient agree on using a specific, shared MAC key.

Both can use this key to create or verify MAC signatures.

  2. The signer performs a sign operation over the data to compute a MAC tag.

  3. The signer provides the data and the MAC tag to the data recipient.

  4. The recipient uses the shared MAC key to verify the MAC signature. If verification is unsuccessful, then the data has been altered.




## Signing algorithms

Cloud Key Management Service only supports keyed-hash message authentication code (HMAC) algorithms for MAC signing. HMAC algorithms use cryptographic hash functions, such as SHA-2 or SHA-3, to compute the MAC tag. The strength of the HMAC function depends on the strength of the hash function, the size of the hash output, and the size of the key. For more information about HMAC signing algorithms, see [HMAC signing algorithms](https://docs.cloud.google.com/kms/docs/algorithms#mac_signing_algorithms).

## Limitations

When using Cloud KMS for MAC signatures, the maximum file size is 16 KiB for Cloud HSM keys and 64 KiB for all other keys. 

## What's next

  * Learn about [HMAC signing algorithms](https://docs.cloud.google.com/kms/docs/algorithms#hmac_signing_algorithms).
  * [Create a key](https://docs.cloud.google.com/kms/docs/creating-keys) with the [`MAC`](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys#CryptoKeyPurpose.ENUM_VALUES.MAC) key purpose and an [HMAC signing algorithm](https://docs.cloud.google.com/kms/docs/algorithms#hmac_signing_algorithms).
  * [Create a MAC signature](https://docs.cloud.google.com/kms/docs/create-validate-mac-signatures#create_mac_signature) using an existing `MAC` key with a message.
  * [Verify a MAC signature](https://docs.cloud.google.com/kms/docs/create-validate-mac-signatures#verify_mac_signature) using an existing `MAC` key with a message and its signature.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
