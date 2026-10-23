---
url: https://docs.cloud.google.com/kms/docs/verifying-imported-key/
title: Verify an imported key version \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:39.307941+00:00
---

# Verify an imported key version  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/verifying-imported-key/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Verify an imported key version Stay organized with collections  Save and categorize content based on your preferences. 

This topic shows you how to verify an asymmetric key version that you [import](https://docs.cloud.google.com/kms/docs/importing-a-key) into Cloud KMS or Cloud HSM.

For more details about how import works, including limitations and restrictions, refer to [Key import](https://docs.cloud.google.com/kms/docs/key-import).

## Limitations on verifying imported keys

### Data encrypted outside of Cloud KMS

The best way to test an imported key is to decrypt data that was encrypted before the key was imported, or to encrypt data using the imported key and decrypt it using the key before import.

In Cloud KMS or Cloud HSM, this is only possible when you import an asymmetric key. This is because when data is encrypted using a symmetric Cloud KMS or Cloud HSM key, extra metadata about the encryption key version is saved, encrypted, along with the encrypted data. This metadata is not present in data encrypted outside of Cloud KMS.

### Verify attestations

You can verify attestations about Cloud HSM keys. These attestations assert that the key is an HSM key, that the HSM module is owned by Google, and other details about the key. These attestations are not available for software keys.

## Before you begin

  * [Import an asymmetric key](https://docs.cloud.google.com/kms/docs/importing-a-key) into Cloud KMS or Cloud HSM. You must use Cloud HSM if you want to verify the key's attestations.
  * If possible, complete the tasks in this topic using the same local system where you imported the key, so the local system already has the Google Cloud CLI installed and configured.
  * Encrypt a file using the local key, or copy a file encrypted with that key to the local system.



## Verify that the key material is identical

After you import an asymmetric key into Cloud KMS or Cloud HSM, the key material is identical to the local key. To verify that this is true, you can use the imported key to decrypt data that was encrypted using the key before it was imported.

To decrypt a file using a Cloud KMS or Cloud HSM key:
    
    
    gcloud kms decrypt \
      --location=location  \
      --keyring=key-ring-name \
      --key=key-name \
      --ciphertext-file=filepath-and-file-to-decrypt \
      --plaintext-file=decrypted-filepath-and-file.dec
    

If the file pointed to by the `--plaintext-file` flag contains the correct decrypted data, the key material of the external and imported key is identical.

To learn more, see [encrypting and decrypting data](https://docs.cloud.google.com/kms/docs/encrypt-decrypt).

## Verify attestations for a Cloud HSM key

After a key is imported into an HSM, you can view attestations to verify that the HSM is owned by Google. The procedure is different to verify symmetric Cloud HSM keys and asymmetric keys.

Attestations are not available for software keys in Cloud KMS.

### Symmetric Cloud HSM keys

You can use the Extended Key Checksum Value (EKCV) key attribute to verify an imported Cloud HSM key's key material. This value is calculated by following [RFC 5869](https://tools.ietf.org/html/rfc5869), section 2. The value is derived using SHA-256-based HMAC-based Extract-and-Expand Key Derivation Function (HKDF) with 32 zero bytes as salt and expanding it with the fixed string **Key Check Value** as info. To retrieve this value, you can [attest the key](https://docs.cloud.google.com/kms/docs/attest-key#verify_key_properties).

### Asymmetric Cloud HSM keys

When you make the import request for an asymmetric key, you include your wrapped private key. The private key contains sufficient information for Cloud KMS to derive the public key. After your key is imported, you can retrieve the public key and verify that it matches the public key you have stored locally. For more information about checking the public key attribute, see [To verify the public key](https://docs.cloud.google.com/kms/docs/attest-key#verify_public_key).

You can verify the EKCV verification for asymmetric keys. In this case, the value is the SHA-256 digest of the DER-encoded public key. You can retrieve this value by looking at the attestation of the key. For more information about checking the EKCV key attribute, see [To verify key properties](https://docs.cloud.google.com/kms/docs/attest-key#verify_key_properties).

For additional information about attesting keys you import, see [Attesting a key](https://docs.cloud.google.com/kms/docs/attest-key#verify_key_properties)

## What's next

  * Learn how to [create keys](https://docs.cloud.google.com/kms/docs/creating-keys)
  * Learn about [encrypting and decrypting](https://docs.cloud.google.com/kms/docs/encrypt-decrypt)
  * Learn about [signing and validating data](https://docs.cloud.google.com/kms/docs/create-validate-signatures)



[ Previous arrow_back  Import a key version  ](https://docs.cloud.google.com/kms/docs/importing-a-key)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
