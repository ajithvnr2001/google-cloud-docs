---
url: https://docs.cloud.google.com/kms/docs/envelope-encryption/
title: Envelope encryption \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:33.680672+00:00
---

# Envelope encryption  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/envelope-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Envelope encryption Stay organized with collections  Save and categorize content based on your preferences. 

## Introduction

Storing and encrypting data at Google's scale requires using a central cryptographic key management service with multiple layers of keys for the encrypted data. An example of multiple layer of keys is _envelope encryption_ , which is the process of encrypting a key with another key.

You can encrypt data at both the _application layer_ , which is responsible for displaying data to users, and the _storage layer_ , which provides the physical storage of data.

By default, at the storage layer, Google Cloud [encrypts customer content stored at rest](https://docs.cloud.google.com/docs/security/encryption/default-encryption) using envelope encryption, with Google's internal key management service as the central keystore. If you're storing and encrypting data yourself, you can use Cloud Key Management Service as your central keystore at the application layer, which is the focus of this topic.

Cloud KMS stores keys in a _key hierarchy_ designed for ease, with access to resources in the key hierarchy governed by [Identity and Access Management](https://docs.cloud.google.com/kms/docs/iam). The following shows the main levels of a Cloud KMS key hierarchy:

![Resources](https://docs.cloud.google.com/static/kms/images/resources2.png)

Find out more about the key hierarchy at [object hierarchy](https://docs.cloud.google.com/kms/docs/object-hierarchy).

### Data encryption keys

The key used to encrypt data itself is called a _data encryption key_ (DEK).

Here are best practices for managing DEKs:

  * Generate DEKs locally.
  * When stored, always ensure DEKs are encrypted at rest.
  * For easy access, store the DEK near the data that it encrypts.
  * Generate a new DEK every time you write the data. This means you don't need to rotate the DEKs.
  * Do not use the same DEK to encrypt data from two different users.
  * Use a strong algorithm such as 256-bit Advanced Encryption Standard (AES) in Galois Counter Mode (GCM).



### Key encryption keys

The DEK is encrypted (also known as _wrapped_) by a _key encryption key_ (KEK). The process of encrypting a key with another key is known as _envelope encryption_.

Here are best practices for managing KEKs:

  * Store KEKs centrally.

  * Set the granularity of the DEKs they encrypt based on their use case. For example, consider a workload that requires multiple DEKs to encrypt the workload's data chunks. You could use a single KEK to wrap all DEKs that are responsible for that workload's encryption.

  * Rotate keys regularly, and also after a suspected incident. To learn more, see [key rotation](https://docs.cloud.google.com/kms/docs/key-rotation).




## Balancing DEKs and KEKs

Having a smaller number of KEKs than DEKs and using a central key management service makes storing and encrypting data at scale more manageable. A central key service also is a singular point to more easily audit and restrict data access.

Depending on your situation, and the volume of data you are encrypting, you may choose to use a similar model. A single KEK can be used to protect many DEKs; this model permits individual data objects to each have their own DEK without massively increasing the volume of keys stored in a central key management service.

Cloud Key Management Service was designed to manage KEKs, and thus the maximum data input size for `Encrypt` and `Decrypt` functions is 64 KiB. However, for data that you know will not approach that limit, you could use Cloud KMS to encrypt and decrypt data directly.

## How to encrypt data using envelope encryption

The process of encrypting data is to generate a DEK locally, encrypt data with the DEK, use a KEK to wrap the DEK, and then store the encrypted data and the wrapped DEK. The KEK never leaves Cloud KMS.

![Encryption flow](https://docs.cloud.google.com/static/kms/images/envelope_encryption_store.svg)

To encrypt data using envelope encryption:

  1. Generate a DEK locally. You could do this with an open source library such as [OpenSSL](https://www.openssl.org), specifying a cipher type and a password from which to generate the key. You can also specify a salt and digest to use, if desired.

  2. Use this DEK locally to encrypt your data.

As an example, you could use OpenSSL as shown in the [encrypting the message](https://wiki.openssl.org/index.php/EVP_Symmetric_Encryption_and_Decryption#Encrypting_the_message) example. For best practice, use 256-bit Advanced Encryption Standard (AES-256) cipher in Galois Counter Mode (GCM).

  3. Generate a new key in Cloud KMS, or use an existing key, which will act as the KEK. Use this key to encrypt (wrap) the DEK.

  4. Store the encrypted data and the wrapped DEK.


**Warning:** Do **NOT** store a plaintext DEK.

## How to decrypt data using envelope encryption

The process of decrypting data is to retrieve the encrypted data and the wrapped DEK, identify the KEK that wrapped the DEK, use the KEK to unwrap the DEK, and then use the unwrapped DEK to decrypt the data. The KEK never leaves Cloud KMS.

![Decryption flow](https://docs.cloud.google.com/static/kms/images/envelope_encryption_retrieve.svg)

To decrypt data using envelope encryption:

  1. Retrieve the encrypted data and the wrapped DEK.

  2. Use the key stored in Cloud KMS to unwrap the encrypted DEK.

  3. Use the plaintext DEK to decrypt the encrypted data. If using OpenSSL as earlier, see the [decrypting the message](https://wiki.openssl.org/index.php/EVP_Symmetric_Encryption_and_Decryption#Decrypting_the_Message) example.




For sample code that shows how to encrypt and decrypt with envelope encryption, see [Client-side encryption with Tink and Cloud KMS](https://docs.cloud.google.com/kms/docs/client-side-encryption).

## Integration with Google Cloud services

Several Google Cloud products are integrated with Cloud KMS to support Customer-Managed Encryption Key (CMEK) functionality. CMEK with Cloud KMS adds an extra layer of protection for your data, provides you with control of your encryption keys, and leverages the key management benefits of Cloud KMS. See [Using Cloud KMS with other services](https://docs.cloud.google.com/kms/docs/using-other-products) to see a full list of products that support CMEK.

## Other options for Google Cloud services

For data stored in Google Cloud products that do not support CMEK, you can implement your own application-layer encryption. This requires implementing your own envelope encryption as described above, so that you store data encrypted locally in Google Cloud. This is also how you could use Cloud KMS to encrypt data you store in other cloud service providers or on premises.

In addition to supporting CMEK, the following products support Customer-Supplied Encryption Key (CSEK) functionality.

Product | CSEK topic  
---|---  
Cloud Storage | [Customer-supplied encryption keys](https://docs.cloud.google.com/storage/docs/encryption/customer-supplied-keys)  
Compute Engine | [Encrypt disks with customer-supplied encryption keys](https://docs.cloud.google.com/compute/docs/disks/customer-supplied-encryption)  
  
With CSEK, you supply your own AES-256 key to serve as the KEK, and your key protects the DEKs that protect your data. Your CSEK key is protected by an additional layer of protection, using a Cloud KMS key.

Now that you can [import keys into Cloud KMS](https://docs.cloud.google.com/kms/docs/importing-a-key), you can import your keys and use them with CMEK-enabled services instead of relying on CSEK.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
