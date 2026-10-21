---
url: https://docs.cloud.google.com/kms/docs/asymmetric-encryption/
title: Asymmetric encryption \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:33.727647+00:00
---

# Asymmetric encryption  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/asymmetric-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Asymmetric encryption Stay organized with collections  Save and categorize content based on your preferences. 

_Asymmetric encryption_ is the process of using a public key from a public/private key pair to encrypt plaintext, and then using the corresponding private key to decrypt the ciphertext. Asymmetric encryption relies on asymmetric cryptography, also known as public key cryptography.

Symmetric encryption, on the other hand, uses the same key to encrypt and decrypt data.

## Asymmetric encryption workflow

The following describes the flow for using an asymmetric key to encrypt and decrypt data. The two participants in this workflow consists of a sender and a recipient. The sender creates ciphertext using the recipient's public key, and then the recipient decrypts the ciphertext using the recipient's private key. Only someone with knowledge of the private key can decrypt the ciphertext.

  1. The sender retrieves the recipient's public key.

  2. The sender uses the public key to encrypt plaintext.

  3. The sender sends the ciphertext to the recipient.

  4. The recipient uses the recipient's private key to decrypt the ciphertext. The recipient can now view the plaintext.




## Example use case for asymmetric encryption

Asymmetric encryption only supports a very small plaintext size, so asymmetric encryption is generally used for encryption keys, not large pieces of data. As an example, you can use asymmetric encryption as a variation of [envelope encryption](https://docs.cloud.google.com/kms/docs/envelope-encryption). In this scenario, anyone with access to the public key can encrypt the data encryption key (DEK). Only Cloud KMS can then decrypt the encrypted DEK, on behalf of the owner of the asymmetric key.

## Asymmetric encryption algorithms

Cloud Key Management Service supports RSA algorithms for asymmetric encryption. RSA is an industry standard algorithm and offers choices of key size and digest algorithm. RSA cryptography relies on the difficulty in factoring a large integer into two or more factors. The larger the key size, the more difficult it is to factor the integers.

## Cloud KMS asymmetric encryption functionality

Cloud KMS provides the following functionality related to asymmetric encryption.

  * Ability to [create an asymmetric key](https://docs.cloud.google.com/kms/docs/creating-asymmetric-keys) with [key purpose](https://docs.cloud.google.com/kms/docs/algorithms#key_purposes) of `ASYMMETRIC_DECRYPT`. For information about which algorithms Cloud KMS supports, see [asymmetric encryption algorithms](https://docs.cloud.google.com/kms/docs/algorithms#asymmetric_encryption_algorithms).

  * Ability to [retrieve the public key](https://docs.cloud.google.com/kms/docs/retrieve-public-key) for an asymmetric key. You use the public key to [encrypt data](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa#encrypt_data). Cloud KMS does not directly provide a method to asymmetrically encrypt data. Instead, you encrypt data using openly available SDKs and tools, such as [OpenSSL](https://www.openssl.org/). These SDKs and tools require the public key that you retrieve from Cloud KMS.

  * Ability to [decrypt data with an asymmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa#decrypt_data).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
