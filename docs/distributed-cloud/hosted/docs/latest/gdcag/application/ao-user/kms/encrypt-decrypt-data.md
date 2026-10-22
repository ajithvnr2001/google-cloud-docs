---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/encrypt-decrypt-data/
title: Encrypt and decrypt data \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:22:07.076640+00:00
---

# Encrypt and decrypt data  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/application/ao-user/kms/encrypt-decrypt-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Encrypt and decrypt data Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to encrypt and decrypt data using Key Management System (KMS) keys with the gdcloud CLI.

This document is for audiences within the application operator group who need to perform cryptographic operations within GDC projects. For more information, see [Audiences for GDC air-gapped documentation](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/audiences).

## Before you begin

Before encrypting or decrypting data, you must have the necessary permissions and prepare your environment.

### Request IAM roles

To encrypt and decrypt data, contact your IAM Org Admin to request the **KMS Developer** (`kms-developer`) role in your project namespace.

### Prepare your environment

  * [Download](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-download) and [install](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/resources/gdcloud-install) the gdcloud CLI, if you haven't already done so.

  * [Sign in to the gdcloud CLI](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform/pa-user/iam/sign-in#cli).




## Encrypt data

To encrypt data, use the `gdcloud kms keys encrypt` command. This command encrypts a given plaintext file using the `AEAD` key, and writes it to a named ciphertext file.

  * To encrypt data, pass in the key name and the following:
        
        gdcloud kms keys encrypt namespaces/NAMESPACE/aeadKeys/KEY_NAME \
          --plaintext-file=PLAINTEXT_PATH \
          --additional-authenticated-data-file=ADDITIONAL_AUTHENTICATED_DATA_FILE \
          --ciphertext-file=CIPHERTEXT_PATH
        

Replace the following variables:

    * NAMESPACE: the project namespace—for example: `kms-test1`.
    * KEY_NAME: the name of the key used to encrypt the plaintext—for example: `key-1`.
    * PLAINTEXT_PATH: the path to the file that contains the plaintext to encrypt.
    * ADDITIONAL_AUTHENTICATED_DATA_FILE: an optional file that contains additional authenticated data (AAD). AAD is used for integrity checks and protects your data from a confused deputy attack. AAD and the plaintext each have a size limit of 64KB.
    * CIPHERTEXT_PATH: the path to the file that contains the encrypted plaintext.

After running the command, you see a file you specified in the `--ciphertext-file` flag that contains the encrypted contents of the plaintext file.




## Decrypt data

To decrypt data, use the `gdcloud kms keys decrypt` command. This command decrypts a given ciphertext file using the `AEAD` key, and writes it to a named plaintext file.

  * To decrypt ciphertext, pass in the key name and the following:
        
        gdcloud kms keys decrypt namespaces/NAMESPACE/aeadKeys/KEY_NAME \
         --ciphertext-file=CIPHERTEXT_PATH \
         --additional-authenticated-data-file=ADDITIONAL_AUTHENTICATED_DATA_FILE \
         --plaintext-file=PLAINTEXT_PATH
        

Replace the following variables:

    * NAMESPACE: the project namespace.
    * KEY_NAME: the name of the key used to encrypt the plaintext.
    * CIPHERTEXT_PATH: the path of the file you want to decrypt.
    * ADDITIONAL_AUTHENTICATED_DATA_FILE: an optional file that contains additional authenticated data (AAD). AAD is used for integrity checks and protects your data from a confused deputy attack. AAD and the plaintext each have a size limit of 64KB. **Note** : You must use the same AAD you passed during the encrypt operation for the decrypt operation. 
    * PLAINTEXT_PATH: the path to the file that contains the decrypted plaintext.

After running the command, you see a file you specified in the `--plaintext-file` flag that contains the decrypted data.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
