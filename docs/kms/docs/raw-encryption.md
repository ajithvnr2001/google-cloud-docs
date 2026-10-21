---
url: https://docs.cloud.google.com/kms/docs/raw-encryption/
title: Raw symmetric encryption \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:24:33.927608+00:00
---

# Raw symmetric encryption  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/raw-encryption/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Raw symmetric encryption Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to do the following raw symmetric key operations:

  * Encrypt text or binary plaintext content locally or using Cloud KMS.
  * Decrypt ciphertexts locally or using Cloud KMS.



If instead you want to do a regular (non-raw) symmetric key operation, see [Encrypting and decrypting data with a symmetric key](https://docs.cloud.google.com/kms/docs/encrypt-decrypt).

The raw symmetric encryption lets you encrypt and decrypt your data locally on-premises or using Cloud KMS, and move encrypted data between different libraries and service providers without having to decrypt it first. This functionality depends on the ability to access the key at the point of operation. If you want to use the ciphertexts outside of Google Cloud, you must use an imported key because keys generated in Cloud KMS can't be exported. These encryption algorithms generate standard ciphertexts that can be decrypted by any standard decryption service. We support the following raw symmetric encryption algorithms:

  * `AES-128-GCM`
  * `AES-256-GCM`
  * `AES-128-CBC`
  * `AES-256-CBC`
  * `AES-128-CTR`
  * `AES-256-CTR`

**Caution:** While giving more options to the customer, raw symmetric encryption limits advanced KMS features such as automatic rotation on the corresponding keys. It also does not support [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).

Note the following points about these raw encryption algorithms:

  * `AES-GCM` provides authentication based on the additional authenticated data (AAD) and generates an authentication tag, and is the recommended encryption algorithm to use. Data encrypted using `AES-GCM` algorithms can't be decrypted without the provided AAD.

  * `AES-CBC` requires the size of the plaintext to be a multiple of the block size (16 bytes). If the plaintext is not a multiple of the block size, pad the plaintext before encrypting it; otherwise, the operation will fail with an error indicating the issue.

  * `AES-CBC` and `AES-CTR` are not authenticated encryption schemes, which means that they can carry greater risk of accidental misuse. They are offered to support legacy and interoperability needs, and should be used with caution. To prevent casual misuse, using these encryption algorithms requires the following IAM permissions:

    * `cloudkms.cryptoKeyVersions.manageRawAesCbcKeys` for `AES-CBC`.
    * `cloudkms.cryptoKeyVersions.manageRawAesCtrKeys` for `AES-CTR`.
**Caution:** Grant these permissions only to principals who understand the risks associated with using unauthenticated encryption.



## Required roles

To get the permissions that you need to use raw encryption, ask your administrator to grant you the following IAM roles on your key: 

  * To encrypt only: [Cloud KMS CryptoKey Encrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypter) (`roles/cloudkms.cryptoKeyEncrypter`) 
  * To decrypt only: [Cloud KMS CryptoKey Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyDecrypter) (`roles/cloudkms.cryptoKeyDecrypter`) 
  * To encrypt and decrypt: [Cloud KMS CryptoKey Encrypter/Decrypter ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudkms#cloudkms.cryptoKeyEncrypterDecrypter) (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Additional roles for unauthenticated raw encryption algorithms

  * To use `AES-CBC` keys: Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)
  * To use `AES-CTR` keys: Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)



## Before you begin

  * Grant the mentioned raw symmetric encryption permissions to the intended principals.
  * Create a key ring as described in creating [key rings](https://docs.cloud.google.com/kms/docs/create-key-ring).
  * Create and import a raw symmetric encryption key as described in [creating keys](https://docs.cloud.google.com/kms/docs/creating-keys) and [importing keys](https://docs.cloud.google.com/kms/docs/importing-a-key).



## Encrypt

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms raw-encrypt \
        --location LOCATION \
        --keyring KEY_RING \
        --key KEY_NAME \
        --version KEY_VERSION \
        --plaintext-file INPUT_FILE_PATH \
        --ciphertext-file OUTPUT_FILE_PATH
    

Replace the following:

  * `LOCATION`: the Cloud KMS location of the key ring.

  * `KEY_RING`: the name of the key ring that contains the key.

  * `KEY_NAME`: the name of the key to use for encryption.

  * `KEY_VERSION`: the ID of the key version to use for encryption.

  * `INPUT_FILE_PATH`: the local file path for reading the plaintext data.

  * `OUTPUT_FILE_PATH`: the local file path for saving the encrypted output.




For information on all flags and possible values, run the command with the `--help` flag.

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

When using JSON and the REST API, content must be base64 encoded before it can be encrypted by Cloud KMS.

**Tip** : You can base64-encode or decode data using the `base64` command on Linux or macOS, or the `Base64.exe` command on Windows. Programming and scripting languages typically include libraries for base64-encoding. For command-line examples, see [Base64 Encoding](https://docs.cloud.google.com/vision/docs/base64) in the Cloud Vision API documentation.

Use the `rawEncrypt` method to encrypt a plaintext data:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION:rawEncrypt" \
      --request "POST" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data '{"plaintext": "BASE64_ENCODED_INPUT", "additionalAuthenticatedData": "BASE64_ENCODED_AAD"}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key to use for encryption.
  * `KEY_VERSION`: the ID of the key version to use for encryption.
  * `BASE64_ENCODED_INPUT`: the base64-encoded plaintext data that you want to encrypt.
  * `BASE64_ENCODED_AAD`: the base64-encoded additional authenticated data that is used to provide integrity and authenticity assurances. This field only applies for the `AES-GCM` algorithms.



The output is a JSON object containing the encrypted ciphertext and the associated initialization vector as base64-encoded strings. 

## Decrypt

### gcloud

To use Cloud KMS on the command line, first [Install or upgrade to the latest version of Google Cloud CLI](https://docs.cloud.google.com/sdk/install).
    
    
    gcloud kms raw-decrypt \
        --location LOCATION \
        --keyring KEY_RING \
        --key KEY_NAME \
        --version KEY_VERSION \
        --ciphertext-file INPUT_FILE_PATH \
        --plaintext-file OUTPUT_FILE_PATH
    

Replace the following:

  * `LOCATION`: the Cloud KMS location of the key ring.

  * `KEY_RING`: the name of the key ring that contains the key.

  * `KEY_NAME`: the name of the key to use for encryption.

  * `KEY_VERSION`: the ID of the key version to use for encryption.

  * `INPUT_FILE_PATH`: the local file path to the ciphertext that you want to decrypt.

  * `OUTPUT_FILE_PATH`: the local file path where you want to save the decrypted plaintext.




For information on all flags and possible values, run the command with the `--help` flag.

### API

These examples use [curl](https://curl.haxx.se/) as an HTTP client to demonstrate using the API. For more information about access control, see [Accessing the Cloud KMS API](https://docs.cloud.google.com/kms/docs/accessing-the-api). 

When using the REST API, content must be base64-encoded before it can be decrypted by Cloud KMS.

**Tip** : You can base64-encode or decode data using the `base64` command on Linux or macOS, or the `Base64.exe` command on Windows. Programming and scripting languages typically include libraries for base64-encoding. For command-line examples, see [Base64 Encoding](https://docs.cloud.google.com/vision/docs/base64) in the Cloud Vision API documentation.

To decrypt the encrypted data, use the `rawDecrypt` method:
    
    
    curl "https://cloudkms.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME/cryptoKeyVersions/KEY_VERSION:rawDecrypt" \
      --request "POST" \
      --header "authorization: Bearer TOKEN" \
      --header "content-type: application/json" \
      --data '{"ciphertext": "BASE64_ENCODED_DATA", "additionalAuthenticatedData": "BASE64_ENCODED_AAD", "initializationVector": "BASE64_ENCODED_IV"}'
    

Replace the following:

  * `PROJECT_ID`: the ID of the project that contains the key ring.
  * `LOCATION`: the Cloud KMS location of the key ring.
  * `KEY_RING`: the name of the key ring that contains the key.
  * `KEY_NAME`: the name of the key to use for decryption.
  * `KEY_VERSION`: the ID of the key version to use for decryption.
  * `BASE64_ENCODED_DATA`: the base64-encoded ciphertext that you want to decrypt.
  * `BASE64_ENCODED_AAD`: the base64-encoded additional authenticated data that was used when the data was encrypted. This field only applies for the `AES-GCM` algorithms.
  * `BASE64_ENCODED_IV`: the base64-encoded initialization vector that was used when the data was encrypted.



The output is a JSON object containing the decrypted plaintext as a base64-encoded string.

## What's next

  * Read more about [importing a key version](https://docs.cloud.google.com/kms/docs/importing-a-key)
  * Read more about [envelope encryption](https://docs.cloud.google.com/kms/docs/data-encryption-keys).
  * Try the [Encrypt and decrypt data with Cloud KMS Codelab](https://codelabs.developers.google.com/codelabs/encrypt-and-decrypt-data-with-cloud-kms). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
