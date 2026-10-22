---
url: https://docs.cloud.google.com/kms/docs/key-import/
title: Key import \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:02:48.489957+00:00
---

# Key import  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/key-import/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Key import Stay organized with collections  Save and categorize content based on your preferences. 

This topic covers conceptual information about importing keys into Cloud Key Management Service as new key versions. For step-by-step instructions, see [importing a key version](https://docs.cloud.google.com/kms/docs/importing-a-key).

## Introduction

You may be using existing cryptographic keys that were created on your premises or in an external key management system. If you migrate an application to Google Cloud or if you add cryptographic support to an existing Google Cloud application, you can import the relevant keys into Cloud KMS.

  * You can import into Multi-tenant Cloud HSM keys, Single-tenant Cloud HSM keys, or software keys in Cloud KMS. 
  * Key material is wrapped for protection in transit. You can use the Google Cloud CLI to automatically wrap the key, or you can [wrap the key manually](https://docs.cloud.google.com/kms/docs/wrapping-a-key). 
  * Google Cloud has access to the wrapping key only within the scope of the import job. For Cloud HSM keys, the wrapping key never resides outside of Cloud HSM. 



This topic provides details about limitations and requirements for importing keys, and gives an overview of how key import works.

## Limitations and requirements

Review these sections to verify that your keys can be imported into Cloud KMS.

### Supported key formats

  * **Symmetric keys for encryption** : Imported symmetric keys must be 16 bytes (for [raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption) only) or 32 bytes of binary data, and must _not_ be encoded. If your key is hex-encoded or base64-encoded, then you must decode it before attempting to import it.
  * **Symmetric keys for signing (MAC keys)** : Imported HMAC signing keys must have a length equal to the output length of the cryptographic hash function being used (for example, HMAC-SHA256 keys must have a length of 32 bytes), and must _not_ be encoded. If your key is hex-encoded or base64-encoded, then you must decode it before attempting to import it.
  * **Asymmetric keys for encryption or signing** : Imported asymmetric keys must be in PKCS #8 format and must be DER-encoded. PCKS #8 format is defined in [RFC 5208](https://tools.ietf.org/html/rfc5208). DER encoding is defined in [International Telecommunications Union X.680](https://www.itu.int/rec/T-REC-X.680/en). Asymmetric keys must use one of the [length and algorithm combinations](https://docs.cloud.google.com/kms/docs/algorithms) supported by Cloud KMS.

**Important:** An RSA key's public exponent must be 65,537 or higher. This is a Digital Signature Standard (DSS) requirement noted in the Criteria for IFC Key Pairs section of [FIPS PUB 186-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf), Section B.3.1

Some aspects of a key, such as the key's length, cannot be changed after the key is created. In these cases, the key cannot be imported into Cloud KMS.

To verify and reformat your key for import, see [Formatting keys for import](https://docs.cloud.google.com/kms/docs/formatting-keys-for-import).

### Supported protection levels

You can import a key into a Cloud KMS key, a Multi-tenant Cloud HSM key, or a Single-tenant Cloud HSM key by setting the key's [protection level](https://docs.cloud.google.com/kms/docs/algorithms#protection_levels) to `SOFTWARE`, `HSM`, or `HSM_SINGLE_TENANT`. You can't import into a Cloud External Key Manager key. 

### Supported wrapping key sizes

When you create an import job, you can control the size of the wrapping key used to protect your key in transit to Google Cloud by setting the import job's _import method_. The default size for the wrapping key is 3072. If you have specific requirements, you can configure the import job to use a 4096-bit key instead.

You can learn more about the algorithms used for [key wrapping](https://docs.cloud.google.com/kms/docs/key-wrapping) or about [configuring an import job](https://docs.cloud.google.com/kms/docs/importing-a-key#create_importjob).

## How key import works

This section illustrates what happens when you import a key. Some parts of the flow are different if you use automatic wrapping or manually wrap the key. Using automatic wrapping is recommended. For specific instructions, see [Import a key version](https://docs.cloud.google.com/kms/docs/importing-a-key). For specific instructions about manually wrapping your key before import, see [Wrapping a key using OpenSSL on Linux](https://docs.cloud.google.com/kms/docs/wrapping-a-key).

The following diagram illustrates the key import process using automatic key wrapping. The phases shown in the diagram are described in this section.

![Import flow, described in this section](https://docs.cloud.google.com/static/kms/images/import_flow.png)

  1. Get ready to import keys.

     1. First, you [create a target key ring and key](https://docs.cloud.google.com/kms/docs/importing-a-key#create_targets) that will eventually contain the import job and the imported key material. At this point, the target key contains no key versions.

     2. Next, you [create an import job](https://docs.cloud.google.com/kms/docs/importing-a-key#create_importjob). The import job defines the target key ring and key for the imported key material. The import job also defines the import method, which is the algorithm used to create the wrapping key that protects the key material during import requests.

        * The public key is used to wrap the key to be imported on the client.
        * The private key is stored within Google Cloud and is used to unwrap the key after it reaches the Google Cloud project.

This separation prevents Google from being able to unwrap your key material outside of the scope of the import job.

     3. The key must be cryptographically wrapped before transmitting it to Google. Most users can use the gcloud CLI to automatically wrap, transmit, and import the key, as described in the next step. If you have compliance or regulatory requirements to [wrap the key manually](https://docs.cloud.google.com/kms/docs/wrapping-a-key), you can do it at this time. To wrap the key manually on the local system:

        1. Configure OpenSSL.
        2. Once per import job, download the wrapping key associated with the import job.
        3. Once per key, set several environment variables and wrap the key.
  2. For up to three days, until the import job expires, you can use it to [make import requests](https://docs.cloud.google.com/kms/docs/importing-a-key#request_import) to import one or more keys. During an import request:

     1. If the key was not manually wrapped, the Google Cloud CLI downloads the import job's public key from Google Cloud to the local system, then uses the public key, along with a private key associated with the client, to wrap the local key material.
     2. The wrapped key material is transmitted to the Google Cloud project.
     3. The key material is unwrapped using the import job's private key and is inserted as a new version of the target key on the target key ring. This is an atomic operation.
     4. For symmetric keys, you set the imported key version to be the primary key version.
**Note:** The imported key version is not automatically set to be the primary key version.



After the import request completes successfully, you can use the imported key version to protect data in Google Cloud.

## What's next

  * [Import a key version](https://docs.cloud.google.com/kms/docs/importing-a-key)
  * [Encrypt and decrypt data using a symmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt)
  * [Encrypt and decrypt data using an asymmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt-rsa)
  * Learn about [Creating and validating digital signatures](https://docs.cloud.google.com/kms/docs/create-validate-signatures)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
