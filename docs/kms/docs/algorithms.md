---
url: https://docs.cloud.google.com/kms/docs/algorithms/
title: Key purposes and algorithms \u00a0|\u00a0 Cloud Key Management Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T06:42:54.606890+00:00
---

# Key purposes and algorithms  |  Cloud Key Management Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kms/docs/algorithms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud KMS ](https://docs.cloud.google.com/kms/docs)
  * [ Guides ](https://docs.cloud.google.com/kms/docs/key-management-service)



Send feedback 

#  Key purposes and algorithms Stay organized with collections  Save and categorize content based on your preferences. 

The function of a Cloud KMS key is determined by the following parameters:

  * **Protection level** : Controls where cryptographic operations are performed, for example, in Google Cloud hardware security modules or in an external key manager.
  * **Purpose** : Determines the cryptographic operations that the key can perform.
  * **Algorithm** : The specific parameters that are used for cryptographic operations.



This document lists the protection levels, key purposes, and algorithms that you can use with Cloud KMS. For each one, the "SDK" value is used with gcloud CLI, and the "REST" value is used with the Cloud KMS API. This document also identifies whether each algorithm is considered quantum-safe, and whether an algorithm is the recommended algorithm for its purpose.

For each group of algorithms, select a protection level to see supported algorithms.

## Protection levels

The protection level indicates where cryptographic operations are performed. After you create a key, you can't change the protection level. Some key purposes and algorithms are available only for specific protection levels.

Protection level | Description  
---|---  
SDK: `software`  
REST: `SOFTWARE` | Cryptographic operations are performed in software.  
SDK: `hsm`  
REST: `HSM` | Cryptographic operations are performed in an HSM.  
SDK: `hsm-single-tenant`  
REST: `HSM_SINGLE_TENANT` | Cryptographic operations are performed in a dedicated cluster of HSM partitions, exclusively created for a single-tenant Cloud HSM instance.   
SDK: `external`  
REST: `EXTERNAL` | Cryptographic operations are performed using a key stored in an [external key manager](https://docs.cloud.google.com/kms/docs/ekm) connected to Google Cloud using the internet. Limited to symmetric encryption and asymmetric signing.   
SDK: `external-vpc`  
REST: `EXTERNAL_VPC` | Cryptographic operations are performed using a key stored in an [external key manager](https://docs.cloud.google.com/kms/docs/ekm) connected to Google Cloud over Virtual Private Cloud (VPC). Limited to symmetric encryption and asymmetric signing.   
  
## Key purposes

Cloud KMS supports the following key purposes:

Use for | Purpose | Supported methods  
---|---|---  
[Symmetric encryption](https://docs.cloud.google.com/kms/docs/encrypt-decrypt) | SDK: `encryption`  
REST: `ENCRYPT_DECRYPT` | 

  * [cryptoKeys.encrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/encrypt)
  * [cryptoKeys.decrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys/decrypt)

  
[Raw symmetric encryption](https://docs.cloud.google.com/kms/docs/raw-encryption) | SDK: `raw-encryption`  
REST: `RAW_ENCRYPT_DECRYPT` | 

  * [cryptoKeys.rawEncrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawEncrypt)
  * [cryptoKeys.rawDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/rawDecrypt)

  
[Asymmetric signing](https://docs.cloud.google.com/kms/docs/digital-signatures) | SDK: `asymmetric-signing`  
REST: `ASYMMETRIC_SIGN` | 

  * [cryptoKeyVersions.asymmetricSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricSign)
  * [cryptoKeyVersions.getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey)

  
[Asymmetric encryption](https://docs.cloud.google.com/kms/docs/asymmetric-encryption) | SDK: `asymmetric-encryption`  
REST: `ASYMMETRIC_DECRYPT` | 

  * [cryptoKeyVersions.asymmetricDecrypt](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/asymmetricDecrypt)
  * [cryptoKeyVersions.getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey)

  
[Key encapsulation mechanisms](https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms) | SDK: `key-encapsulation`  
REST: `KEY_ENCAPSULATION` | 

  * [cryptoKeyVersions.decapsulate](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/decapsulate)
  * [cryptoKeyVersions.getPublicKey](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/getPublicKey)

  
[MAC signing](https://docs.cloud.google.com/kms/docs/mac-signatures) | SDK: `mac`  
REST: `MAC` | 

  * [cryptoKeyVersions.macSign](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macSign)
  * [cryptoKeyVersions.macVerify](https://docs.cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys.cryptoKeyVersions/macVerify)

  
  
When you create a key, you define the purpose and the algorithm of that key. You can change the algorithm when you create new key versions, subject to the scope of its purpose. The purpose can't be changed.

Two keys with the same purpose may use different underlying algorithms, but they must support the same set of cryptographic operations.

## Symmetric encryption algorithms

The `ENCRYPT_DECRYPT` key purpose enables symmetric encryption. Standard symmetric encryption algorithms use 256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM). Symmetric encryption algorithms such as AES-256 are generally considered quantum-safe. You can continue to use symmetric encryption.

Algorithm support varies by protection level.

### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `google-symmetric-encryption`  
REST: `GOOGLE_SYMMETRIC_ENCRYPTION` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM), padded with Cloud KMS-internal metadata.  | Yes  
SDK: `external-symmetric-encryption`  
REST: `EXTERNAL_SYMMETRIC_ENCRYPTION` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM).  | Yes  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `google-symmetric-encryption`  
REST: `GOOGLE_SYMMETRIC_ENCRYPTION` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM), padded with Cloud KMS-internal metadata.  | Yes  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `google-symmetric-encryption`  
REST: `GOOGLE_SYMMETRIC_ENCRYPTION` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM), padded with Cloud KMS-internal metadata.  | Yes  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `google-symmetric-encryption`  
REST: `GOOGLE_SYMMETRIC_ENCRYPTION` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM), padded with Cloud KMS-internal metadata.  | Yes  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `external-symmetric-encryption`  
REST: `EXTERNAL_SYMMETRIC_ENCRYPTION` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM).  | Yes  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `external-symmetric-encryption`  
REST: `EXTERNAL_SYMMETRIC_ENCRYPTION` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM).  | Yes  
  
### Raw symmetric encryption algorithms

Raw symmetric encryption algorithms let you perform symmetric encryption and decryption without using Cloud KMS-internal metadata. You can use raw symmetric encryption algorithms with imported keys to encrypt data locally to be decrypted within Google Cloud or to encrypt data in Google Cloud to be decrypted locally.

You can use the algorithms in this table with the following protection levels:

  * `software`
  * `hsm`
  * `hsm-single-tenant`



### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `aes-128-cbc`  
REST: `AES_128_CBC` |  128-bit Advanced Encryption Standard (AES-128) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-128-ctr`  
REST: `AES_128_CTR` |  128-bit Advanced Encryption Standard (AES-128) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-128-gcm`  
REST: `AES_128_GCM` |  128-bit Advanced Encryption Standard (AES-128) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
SDK: `aes-256-cbc`  
REST: `AES_256_CBC` |  256-bit Advanced Encryption Standard (AES-256) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-256-ctr`  
REST: `AES_256_CTR` |  256-bit Advanced Encryption Standard (AES-256) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-256-gcm`  
REST: `AES_256_GCM` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `aes-128-cbc`  
REST: `AES_128_CBC` |  128-bit Advanced Encryption Standard (AES-128) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-128-ctr`  
REST: `AES_128_CTR` |  128-bit Advanced Encryption Standard (AES-128) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-128-gcm`  
REST: `AES_128_GCM` |  128-bit Advanced Encryption Standard (AES-128) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
SDK: `aes-256-cbc`  
REST: `AES_256_CBC` |  256-bit Advanced Encryption Standard (AES-256) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-256-ctr`  
REST: `AES_256_CTR` |  256-bit Advanced Encryption Standard (AES-256) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-256-gcm`  
REST: `AES_256_GCM` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `aes-128-cbc`  
REST: `AES_128_CBC` |  128-bit Advanced Encryption Standard (AES-128) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-128-ctr`  
REST: `AES_128_CTR` |  128-bit Advanced Encryption Standard (AES-128) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-128-gcm`  
REST: `AES_128_GCM` |  128-bit Advanced Encryption Standard (AES-128) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
SDK: `aes-256-cbc`  
REST: `AES_256_CBC` |  256-bit Advanced Encryption Standard (AES-256) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-256-ctr`  
REST: `AES_256_CTR` |  256-bit Advanced Encryption Standard (AES-256) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-256-gcm`  
REST: `AES_256_GCM` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `aes-128-cbc`  
REST: `AES_128_CBC` |  128-bit Advanced Encryption Standard (AES-128) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-128-ctr`  
REST: `AES_128_CTR` |  128-bit Advanced Encryption Standard (AES-128) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-128-gcm`  
REST: `AES_128_GCM` |  128-bit Advanced Encryption Standard (AES-128) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
SDK: `aes-256-cbc`  
REST: `AES_256_CBC` |  256-bit Advanced Encryption Standard (AES-256) keys in Cipher Block Chaining (CBC) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CBC Key Manager (`roles/cloudkms.expertRawAesCbc`)  | Yes  
SDK: `aes-256-ctr`  
REST: `AES_256_CTR` |  256-bit Advanced Encryption Standard (AES-256) keys in Counter (CTR) mode with no authentication.  **Requires expert role:** Cloud KMS Expert Raw AES-CTR Key Manager (`roles/cloudkms.expertRawAesCtr`)  | Yes  
SDK: `aes-256-gcm`  
REST: `AES_256_GCM` |  256-bit Advanced Encryption Standard (AES-256) keys in Galois Counter Mode (GCM) with additional authenticated data (AAD)  | Yes  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
  
## Asymmetric signing algorithms

The `ASYMMETRIC_SIGN` key purpose enables asymmetric signing. These algorithms fall into several categories: elliptic curve, RSA, and post-quantum.

Asymmetric signing algorithms that use elliptic curves and RSA are susceptible to attacks by future quantum computers. For long-term non-repudiation of your signatures, choose a post-quantum asymmetric signing algorithm instead.

### Elliptic curve signing algorithms

The name of the elliptic curve signing algorithm indicates the elliptic curve and the digest algorithm that it uses in the following format:
    
    
    EC_SIGN_ELLIPTIC_CURVE_DIGEST_ALGORITHM
    

The following table lists elliptic curve algorithms. 

Algorithm support varies by protection level.

### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `ec-sign-ed25519`  
REST: `EC_SIGN_ED25519` |  EdDSA on the Curve25519 in [PureEdDSA mode](https://datatracker.ietf.org/doc/html/rfc8032#section-4), which takes raw data as input instead of hashed data  | No  
SDK: `ec-sign-p256-sha256`  
REST: `EC_SIGN_P256_SHA256` |  **Recommended**  
ECDSA on the P-256 Curve with a SHA-256 digest | No  
SDK: `ec-sign-p384-sha384`  
REST: `EC_SIGN_P384_SHA384` |  ECDSA on the P-384 Curve with a SHA-384 digest | No  
SDK: `ec-sign-secp256k1-sha256`  
REST: `EC_SIGN_SECP256K1_SHA256` |  ECDSA on the Secp256k1 Curve with a SHA-256 digest | No  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `ec-sign-ed25519`  
REST: `EC_SIGN_ED25519` |  EdDSA on the Curve25519 in [PureEdDSA mode](https://datatracker.ietf.org/doc/html/rfc8032#section-4), which takes raw data as input instead of hashed data  | No  
SDK: `ec-sign-p256-sha256`  
REST: `EC_SIGN_P256_SHA256` |  **Recommended**  
ECDSA on the P-256 Curve with a SHA-256 digest | No  
SDK: `ec-sign-p384-sha384`  
REST: `EC_SIGN_P384_SHA384` |  ECDSA on the P-384 Curve with a SHA-384 digest | No  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `ec-sign-p256-sha256`  
REST: `EC_SIGN_P256_SHA256` |  **Recommended**  
ECDSA on the P-256 Curve with a SHA-256 digest | No  
SDK: `ec-sign-p384-sha384`  
REST: `EC_SIGN_P384_SHA384` |  ECDSA on the P-384 Curve with a SHA-384 digest | No  
SDK: `ec-sign-secp256k1-sha256`  
REST: `EC_SIGN_SECP256K1_SHA256` |  ECDSA on the Secp256k1 Curve with a SHA-256 digest | No  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `ec-sign-p256-sha256`  
REST: `EC_SIGN_P256_SHA256` |  **Recommended**  
ECDSA on the P-256 Curve with a SHA-256 digest | No  
SDK: `ec-sign-p384-sha384`  
REST: `EC_SIGN_P384_SHA384` |  ECDSA on the P-384 Curve with a SHA-384 digest | No  
SDK: `ec-sign-secp256k1-sha256`  
REST: `EC_SIGN_SECP256K1_SHA256` |  ECDSA on the Secp256k1 Curve with a SHA-256 digest | No  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `ec-sign-p256-sha256`  
REST: `EC_SIGN_P256_SHA256` |  **Recommended**  
ECDSA on the P-256 Curve with a SHA-256 digest | No  
SDK: `ec-sign-p384-sha384`  
REST: `EC_SIGN_P384_SHA384` |  ECDSA on the P-384 Curve with a SHA-384 digest | No  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `ec-sign-p256-sha256`  
REST: `EC_SIGN_P256_SHA256` |  **Recommended**  
ECDSA on the P-256 Curve with a SHA-256 digest | No  
SDK: `ec-sign-p384-sha384`  
REST: `EC_SIGN_P384_SHA384` |  ECDSA on the P-384 Curve with a SHA-384 digest | No  
  
**Note:** `secp256k1` curves generate signatures in the "normalized" form only (also known as the "lower-S form"). For additional cryptographic details about these signatures, see [DER encoding](https://en.bitcoin.it/wiki/BIP_0062#DER_encoding).

### RSA signing algorithms

For most RSA signing algorithms, the name of the RSA signing algorithm indicates the padding algorithm, the modulus bit length, and the digest algorithm that it uses in the following format:
    
    
    RSA_SIGN_PADDING_ALGORITHM_MODULUS_BIT_LENGTH_DIGEST_ALGORITHM
    

Some RSA signing algorithms omit the digest algorithm. These "raw" algorithms are a variant of PKCS #1 signing that omits encoding into a `DigestInfo`. Instead, raw signing algorithms do the following:

  * A digest is computed over the message that will be signed.
  * PKCS #1 padding is applied to the digest directly.
  * A signature of the padded digest is computed, using the RSA private key.



For raw RSA signing algorithms, the name of the RSA signing algorithm indicates the padding algorithm and the modulus bit length that it uses in the following format:
    
    
    RSA_SIGN_RAW_PADDING_ALGORITHM_MODULUS_BIT_LENGTH
    

The following table lists RSA signing algorithms.

Algorithm support varies by protection level.

### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-sign-pss-2048-sha256`  
REST: `RSA_SIGN_PSS_2048_SHA256` |  RSASSA-PSS 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-3072-sha256`  
REST: `RSA_SIGN_PSS_3072_SHA256` |  **Recommended**  
RSASSA-PSS 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha256`  
REST: `RSA_SIGN_PSS_4096_SHA256` |  RSASSA-PSS 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha512`  
REST: `RSA_SIGN_PSS_4096_SHA512` |  RSASSA-PSS 4096-bit key with a SHA-512 digest | No  
SDK: `rsa-sign-pkcs1-2048-sha256`  
REST: `RSA_SIGN_PKCS1_2048_SHA256` |  RSASSA-PKCS1 v1.5 with a 2048-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-3072-sha256`  
REST: `RSA_SIGN_PKCS1_3072_SHA256` |  RSASSA-PKCS1 v1.5 with a 3072-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha256`  
REST: `RSA_SIGN_PKCS1_4096_SHA256` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha512`  
REST: `RSA_SIGN_PKCS1_4096_SHA512` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-512 digest | No  
SDK: `rsa-sign-raw-pkcs1-2048`  
REST: `RSA_SIGN_RAW_PKCS1_2048` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 2048-bit key | No  
SDK: `rsa-sign-raw-pkcs1-3072`  
REST: `RSA_SIGN_RAW_PKCS1_3072` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 3072-bit key | No  
SDK: `rsa-sign-raw-pkcs1-4096`  
REST: `RSA_SIGN_RAW_PKCS1_4096` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 4096-bit key | No  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-sign-pss-2048-sha256`  
REST: `RSA_SIGN_PSS_2048_SHA256` |  RSASSA-PSS 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-3072-sha256`  
REST: `RSA_SIGN_PSS_3072_SHA256` |  **Recommended**  
RSASSA-PSS 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha256`  
REST: `RSA_SIGN_PSS_4096_SHA256` |  RSASSA-PSS 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha512`  
REST: `RSA_SIGN_PSS_4096_SHA512` |  RSASSA-PSS 4096-bit key with a SHA-512 digest | No  
SDK: `rsa-sign-pkcs1-2048-sha256`  
REST: `RSA_SIGN_PKCS1_2048_SHA256` |  RSASSA-PKCS1 v1.5 with a 2048-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-3072-sha256`  
REST: `RSA_SIGN_PKCS1_3072_SHA256` |  RSASSA-PKCS1 v1.5 with a 3072-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha256`  
REST: `RSA_SIGN_PKCS1_4096_SHA256` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha512`  
REST: `RSA_SIGN_PKCS1_4096_SHA512` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-512 digest | No  
SDK: `rsa-sign-raw-pkcs1-2048`  
REST: `RSA_SIGN_RAW_PKCS1_2048` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 2048-bit key | No  
SDK: `rsa-sign-raw-pkcs1-3072`  
REST: `RSA_SIGN_RAW_PKCS1_3072` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 3072-bit key | No  
SDK: `rsa-sign-raw-pkcs1-4096`  
REST: `RSA_SIGN_RAW_PKCS1_4096` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 4096-bit key | No  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-sign-pss-2048-sha256`  
REST: `RSA_SIGN_PSS_2048_SHA256` |  RSASSA-PSS 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-3072-sha256`  
REST: `RSA_SIGN_PSS_3072_SHA256` |  **Recommended**  
RSASSA-PSS 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha256`  
REST: `RSA_SIGN_PSS_4096_SHA256` |  RSASSA-PSS 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha512`  
REST: `RSA_SIGN_PSS_4096_SHA512` |  RSASSA-PSS 4096-bit key with a SHA-512 digest | No  
SDK: `rsa-sign-pkcs1-2048-sha256`  
REST: `RSA_SIGN_PKCS1_2048_SHA256` |  RSASSA-PKCS1 v1.5 with a 2048-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-3072-sha256`  
REST: `RSA_SIGN_PKCS1_3072_SHA256` |  RSASSA-PKCS1 v1.5 with a 3072-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha256`  
REST: `RSA_SIGN_PKCS1_4096_SHA256` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha512`  
REST: `RSA_SIGN_PKCS1_4096_SHA512` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-512 digest | No  
SDK: `rsa-sign-raw-pkcs1-2048`  
REST: `RSA_SIGN_RAW_PKCS1_2048` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 2048-bit key | No  
SDK: `rsa-sign-raw-pkcs1-3072`  
REST: `RSA_SIGN_RAW_PKCS1_3072` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 3072-bit key | No  
SDK: `rsa-sign-raw-pkcs1-4096`  
REST: `RSA_SIGN_RAW_PKCS1_4096` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 4096-bit key | No  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-sign-pss-2048-sha256`  
REST: `RSA_SIGN_PSS_2048_SHA256` |  RSASSA-PSS 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-3072-sha256`  
REST: `RSA_SIGN_PSS_3072_SHA256` |  **Recommended**  
RSASSA-PSS 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha256`  
REST: `RSA_SIGN_PSS_4096_SHA256` |  RSASSA-PSS 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha512`  
REST: `RSA_SIGN_PSS_4096_SHA512` |  RSASSA-PSS 4096-bit key with a SHA-512 digest | No  
SDK: `rsa-sign-pkcs1-2048-sha256`  
REST: `RSA_SIGN_PKCS1_2048_SHA256` |  RSASSA-PKCS1 v1.5 with a 2048-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-3072-sha256`  
REST: `RSA_SIGN_PKCS1_3072_SHA256` |  RSASSA-PKCS1 v1.5 with a 3072-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha256`  
REST: `RSA_SIGN_PKCS1_4096_SHA256` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha512`  
REST: `RSA_SIGN_PKCS1_4096_SHA512` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-512 digest | No  
SDK: `rsa-sign-raw-pkcs1-2048`  
REST: `RSA_SIGN_RAW_PKCS1_2048` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 2048-bit key | No  
SDK: `rsa-sign-raw-pkcs1-3072`  
REST: `RSA_SIGN_RAW_PKCS1_3072` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 3072-bit key | No  
SDK: `rsa-sign-raw-pkcs1-4096`  
REST: `RSA_SIGN_RAW_PKCS1_4096` |  RSASSA-PKCS1 v1.5 signing without encoding, with a 4096-bit key | No  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-sign-pss-2048-sha256`  
REST: `RSA_SIGN_PSS_2048_SHA256` |  RSASSA-PSS 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-3072-sha256`  
REST: `RSA_SIGN_PSS_3072_SHA256` |  **Recommended**  
RSASSA-PSS 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha256`  
REST: `RSA_SIGN_PSS_4096_SHA256` |  RSASSA-PSS 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha512`  
REST: `RSA_SIGN_PSS_4096_SHA512` |  RSASSA-PSS 4096-bit key with a SHA-512 digest | No  
SDK: `rsa-sign-pkcs1-2048-sha256`  
REST: `RSA_SIGN_PKCS1_2048_SHA256` |  RSASSA-PKCS1 v1.5 with a 2048-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-3072-sha256`  
REST: `RSA_SIGN_PKCS1_3072_SHA256` |  RSASSA-PKCS1 v1.5 with a 3072-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha256`  
REST: `RSA_SIGN_PKCS1_4096_SHA256` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha512`  
REST: `RSA_SIGN_PKCS1_4096_SHA512` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-512 digest | No  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-sign-pss-2048-sha256`  
REST: `RSA_SIGN_PSS_2048_SHA256` |  RSASSA-PSS 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-3072-sha256`  
REST: `RSA_SIGN_PSS_3072_SHA256` |  **Recommended**  
RSASSA-PSS 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha256`  
REST: `RSA_SIGN_PSS_4096_SHA256` |  RSASSA-PSS 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-sign-pss-4096-sha512`  
REST: `RSA_SIGN_PSS_4096_SHA512` |  RSASSA-PSS 4096-bit key with a SHA-512 digest | No  
SDK: `rsa-sign-pkcs1-2048-sha256`  
REST: `RSA_SIGN_PKCS1_2048_SHA256` |  RSASSA-PKCS1 v1.5 with a 2048-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-3072-sha256`  
REST: `RSA_SIGN_PKCS1_3072_SHA256` |  RSASSA-PKCS1 v1.5 with a 3072-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha256`  
REST: `RSA_SIGN_PKCS1_4096_SHA256` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-256 digest | No  
SDK: `rsa-sign-pkcs1-4096-sha512`  
REST: `RSA_SIGN_PKCS1_4096_SHA512` |  RSASSA-PKCS1 v1.5 with a 4096-bit key and a SHA-512 digest | No  
  
For Probabilistic Signature Scheme (PSS), the salt length used is equal to the length of the digest algorithm and the digest algorithm is also used for the mask generation function (MGF1). For example, `RSA_SIGN_PSS_2048_SHA256` uses PSS with a salt length of 256 bits and takes a SHA-256 hash of the data to be signed, and Cloud KMS will internally use SHA-256 as the hash algorithm for MGF1 when computing the signature.

### PQC signing algorithms

Post-quantum cryptography (PQC) signing algorithm names start with the prefix `PQ_SIGN_`. The following table lists the PQC algorithms that Cloud KMS can use for keys with purpose `ASYMMETRIC_SIGN`. The pure algorithms take raw data as input, while the pre-hash and external-μ (external-mu) algorithms accept a hash value derived from the data.

You can use the algorithms in this table with the following protection levels:

  * `software`



### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `pq-sign-ml-dsa-44`  
REST: `PQ_SIGN_ML_DSA_44` |  Pure module-lattice-based digital signature algorithm using the ML-DSA-44 parameter set (FIPS 204), where the dimensions of the matrix A are (4,4).  | Yes  
SDK: `pq-sign-ml-dsa-44-external-mu`  
REST: `PQ_SIGN_ML_DSA_44_EXTERNAL_MU` |  External-μ module-lattice-based digital signature algorithm using the ML-DSA-44 parameter set (FIPS 204), where the dimensions of the matrix A are (4,4).  | Yes  
SDK: `pq-sign-ml-dsa-65`  
REST: `PQ_SIGN_ML_DSA_65` |  Pure module-lattice-based digital signature algorithm using the ML-DSA-65 parameter set (FIPS 204), where the dimensions of the matrix A are (6,5).  | Yes  
SDK: `pq-sign-ml-dsa-65-external-mu`  
REST: `PQ_SIGN_ML_DSA_65_EXTERNAL_MU` |  External-μ module-lattice-based digital signature algorithm using the ML-DSA-65 parameter set (FIPS 204), where the dimensions of the matrix A are (6,5).  | Yes  
SDK: `pq-sign-ml-dsa-87`  
REST: `PQ_SIGN_ML_DSA_87` |  Pure module-lattice-based digital signature algorithm using the ML-DSA-87 parameter set (FIPS 204), where the dimensions of the matrix A are (8,7).  | Yes  
SDK: `pq-sign-ml-dsa-87-external-mu`  
REST: `PQ_SIGN_ML_DSA_87_EXTERNAL_MU` |  External-μ module-lattice-based digital signature algorithm using the ML-DSA-87 parameter set (FIPS 204), where the dimensions of the matrix A are (8,7).  | Yes  
SDK: `pq-sign-slh-dsa-sha2-128s`  
REST: `PQ_SIGN_SLH_DSA_SHA2_128S` |  Pure stateless hash-based digital signature algorithm. | Yes  
SDK: `pq-sign-hash-slh-dsa-sha2-128s-sha256`  
REST: `PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256` |  Pre-hash stateless hash-based digital signature algorithm. | Yes  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `pq-sign-ml-dsa-44`  
REST: `PQ_SIGN_ML_DSA_44` |  Pure module-lattice-based digital signature algorithm using the ML-DSA-44 parameter set (FIPS 204), where the dimensions of the matrix A are (4,4).  | Yes  
SDK: `pq-sign-ml-dsa-44-external-mu`  
REST: `PQ_SIGN_ML_DSA_44_EXTERNAL_MU` |  External-μ module-lattice-based digital signature algorithm using the ML-DSA-44 parameter set (FIPS 204), where the dimensions of the matrix A are (4,4).  | Yes  
SDK: `pq-sign-ml-dsa-65`  
REST: `PQ_SIGN_ML_DSA_65` |  Pure module-lattice-based digital signature algorithm using the ML-DSA-65 parameter set (FIPS 204), where the dimensions of the matrix A are (6,5).  | Yes  
SDK: `pq-sign-ml-dsa-65-external-mu`  
REST: `PQ_SIGN_ML_DSA_65_EXTERNAL_MU` |  External-μ module-lattice-based digital signature algorithm using the ML-DSA-65 parameter set (FIPS 204), where the dimensions of the matrix A are (6,5).  | Yes  
SDK: `pq-sign-ml-dsa-87`  
REST: `PQ_SIGN_ML_DSA_87` |  Pure module-lattice-based digital signature algorithm using the ML-DSA-87 parameter set (FIPS 204), where the dimensions of the matrix A are (8,7).  | Yes  
SDK: `pq-sign-ml-dsa-87-external-mu`  
REST: `PQ_SIGN_ML_DSA_87_EXTERNAL_MU` |  External-μ module-lattice-based digital signature algorithm using the ML-DSA-87 parameter set (FIPS 204), where the dimensions of the matrix A are (8,7).  | Yes  
SDK: `pq-sign-slh-dsa-sha2-128s`  
REST: `PQ_SIGN_SLH_DSA_SHA2_128S` |  Pure stateless hash-based digital signature algorithm. | Yes  
SDK: `pq-sign-hash-slh-dsa-sha2-128s-sha256`  
REST: `PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256` |  Pre-hash stateless hash-based digital signature algorithm. | Yes  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
  
For more information about module lattice algorithms, see [FIPS 204: Module-Lattice-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/204/final). For more information about stateless hash-based signatures, see [FIPS 205: Stateless Hash-Based Digital Signature Standard](https://csrc.nist.gov/pubs/fips/205/final).

**Note:** Use `external_mu` as the `[DIGEST_ALGORITHM]` for all external-μ ML-DSA variants.

## Asymmetric decryption algorithms

Asymmetric decryption algorithms in Cloud KMS are used with a private key to decrypt data that was encrypted outside of Cloud KMS using the corresponding public key. The name of the algorithm indicates the padding algorithm, the modulus bit length, and the digest algorithm that it uses for the mask generation function (MGF1) in the following format:
    
    
    RSA_DECRYPT_PADDING_ALGORITHM_MODULUS_BIT_LENGTH_DIGEST_ALGORITHM
    

RSA encryption algorithms are susceptible to quantum computing attacks, including "store now, decrypt later" (SNDL) attacks. In an SNDL attack, a bad actor intercepts a ciphertext that they can't decrypt, and then stores it intending to eventually decrypt it using quantum computing. If you're transmitting data that must remain confidential long term despite advances in quantum computing, choose a key encapsulation algorithm instead.

The following table lists the asymmetric decryption algorithms.

You can use the algorithms in this table with the following protection levels:

  * `software`
  * `hsm`
  * `hsm-single-tenant`



### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-decrypt-oaep-2048-sha1`  
REST: `RSA_DECRYPT_OAEP_2048_SHA1` |  RSAES-OAEP 2048-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-2048-sha256`  
REST: `RSA_DECRYPT_OAEP_2048_SHA256` |  RSAES-OAEP 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha1`  
REST: `RSA_DECRYPT_OAEP_3072_SHA1` |  RSAES-OAEP 3072-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha256`  
REST: `RSA_DECRYPT_OAEP_3072_SHA256` |  **Recommended**  
RSAES-OAEP 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha1`  
REST: `RSA_DECRYPT_OAEP_4096_SHA1` |  RSAES-OAEP 4096-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha256`  
REST: `RSA_DECRYPT_OAEP_4096_SHA256` |  RSAES-OAEP 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha512`  
REST: `RSA_DECRYPT_OAEP_4096_SHA512` |  RSAES-OAEP 4096-bit key with a SHA-512 digest | No  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-decrypt-oaep-2048-sha1`  
REST: `RSA_DECRYPT_OAEP_2048_SHA1` |  RSAES-OAEP 2048-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-2048-sha256`  
REST: `RSA_DECRYPT_OAEP_2048_SHA256` |  RSAES-OAEP 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha1`  
REST: `RSA_DECRYPT_OAEP_3072_SHA1` |  RSAES-OAEP 3072-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha256`  
REST: `RSA_DECRYPT_OAEP_3072_SHA256` |  **Recommended**  
RSAES-OAEP 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha1`  
REST: `RSA_DECRYPT_OAEP_4096_SHA1` |  RSAES-OAEP 4096-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha256`  
REST: `RSA_DECRYPT_OAEP_4096_SHA256` |  RSAES-OAEP 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha512`  
REST: `RSA_DECRYPT_OAEP_4096_SHA512` |  RSAES-OAEP 4096-bit key with a SHA-512 digest | No  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-decrypt-oaep-2048-sha1`  
REST: `RSA_DECRYPT_OAEP_2048_SHA1` |  RSAES-OAEP 2048-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-2048-sha256`  
REST: `RSA_DECRYPT_OAEP_2048_SHA256` |  RSAES-OAEP 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha1`  
REST: `RSA_DECRYPT_OAEP_3072_SHA1` |  RSAES-OAEP 3072-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha256`  
REST: `RSA_DECRYPT_OAEP_3072_SHA256` |  **Recommended**  
RSAES-OAEP 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha1`  
REST: `RSA_DECRYPT_OAEP_4096_SHA1` |  RSAES-OAEP 4096-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha256`  
REST: `RSA_DECRYPT_OAEP_4096_SHA256` |  RSAES-OAEP 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha512`  
REST: `RSA_DECRYPT_OAEP_4096_SHA512` |  RSAES-OAEP 4096-bit key with a SHA-512 digest | No  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `rsa-decrypt-oaep-2048-sha1`  
REST: `RSA_DECRYPT_OAEP_2048_SHA1` |  RSAES-OAEP 2048-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-2048-sha256`  
REST: `RSA_DECRYPT_OAEP_2048_SHA256` |  RSAES-OAEP 2048-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha1`  
REST: `RSA_DECRYPT_OAEP_3072_SHA1` |  RSAES-OAEP 3072-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-3072-sha256`  
REST: `RSA_DECRYPT_OAEP_3072_SHA256` |  **Recommended**  
RSAES-OAEP 3072-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha1`  
REST: `RSA_DECRYPT_OAEP_4096_SHA1` |  RSAES-OAEP 4096-bit key with a SHA-1 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha256`  
REST: `RSA_DECRYPT_OAEP_4096_SHA256` |  RSAES-OAEP 4096-bit key with a SHA-256 digest | No  
SDK: `rsa-decrypt-oaep-4096-sha512`  
REST: `RSA_DECRYPT_OAEP_4096_SHA512` |  RSAES-OAEP 4096-bit key with a SHA-512 digest | No  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
  
All of these algorithms use Optimal Asymmetric Encryption Padding (OAEP).

## Key encapsulation algorithms

The `KEY_ENCAPSULATION` key purpose is used to establish shared secrets using [key encapsulation mechanisms](https://docs.cloud.google.com/kms/docs/key-encapsulation-mechanisms).

The following table lists the key encapsulation algorithms.

You can use the algorithms in this table with the following protection levels:

  * `software`



### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `kem-xwing`  
REST: `KEM_XWING` |  **Recommended**  
X-Wing hybrid KEM combining ML-KEM-768 with X25519 | Yes  
SDK: `ml-kem-768`  
REST: `ML_KEM_768` |  Module-lattice-based key-encapsulation mechanism with ML-KEM-768 parameter set (FIPS 203)  | Yes  
SDK: `ml-kem-1024`  
REST: `ML_KEM_1024` |  Module-lattice-based key-encapsulation mechanism with ML-KEM-1024 parameter set (FIPS 203)  | Yes  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `kem-xwing`  
REST: `KEM_XWING` |  **Recommended**  
X-Wing hybrid KEM combining ML-KEM-768 with X25519 | Yes  
SDK: `ml-kem-768`  
REST: `ML_KEM_768` |  Module-lattice-based key-encapsulation mechanism with ML-KEM-768 parameter set (FIPS 203)  | Yes  
SDK: `ml-kem-1024`  
REST: `ML_KEM_1024` |  Module-lattice-based key-encapsulation mechanism with ML-KEM-1024 parameter set (FIPS 203)  | Yes  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
  
For more information about key encapsulation algorithms, see [FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard](https://csrc.nist.gov/pubs/fips/203/final).

## MAC signing algorithms

The `MAC` key purpose is used for symmetric MAC signing. The name of the algorithm indicates the hash algorithm in the following format:
    
    
    HMAC_HASH_ALGORITHM
    

Most symmetric algorithms are generally considered quantum-safe. However, the `HMAC-SHA1` algorithm is not quantum-safe. If you need your symmetric signatures to remain trustworthy long-term despite advances in quantum computing, choose an HMAC key with a larger hash algorithm size.

The following table lists the HMAC algorithms.

You can use the algorithms in this table with the following protection levels:

  * `software`
  * `hsm`
  * `hsm-single-tenant`



### Any

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `hmac-sha1`  
REST: `HMAC_SHA1` |  HMAC with a SHA-1 digest  | No  
SDK: `hmac-sha224`  
REST: `HMAC_SHA224` |  HMAC with a SHA-224 digest | Yes  
SDK: `hmac-sha256`  
REST: `HMAC_SHA256` |  **Recommended**  
HMAC with a SHA-256 digest | Yes  
SDK: `hmac-sha384`  
REST: `HMAC_SHA384` |  HMAC with a SHA-384 digest | Yes  
SDK: `hmac-sha512`  
REST: `HMAC_SHA512` |  HMAC with a SHA-512 digest | Yes  
  
### software

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `hmac-sha1`  
REST: `HMAC_SHA1` |  HMAC with a SHA-1 digest  | No  
SDK: `hmac-sha224`  
REST: `HMAC_SHA224` |  HMAC with a SHA-224 digest | Yes  
SDK: `hmac-sha256`  
REST: `HMAC_SHA256` |  **Recommended**  
HMAC with a SHA-256 digest | Yes  
SDK: `hmac-sha384`  
REST: `HMAC_SHA384` |  HMAC with a SHA-384 digest | Yes  
SDK: `hmac-sha512`  
REST: `HMAC_SHA512` |  HMAC with a SHA-512 digest | Yes  
  
### hsm

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `hmac-sha1`  
REST: `HMAC_SHA1` |  HMAC with a SHA-1 digest  | No  
SDK: `hmac-sha224`  
REST: `HMAC_SHA224` |  HMAC with a SHA-224 digest | Yes  
SDK: `hmac-sha256`  
REST: `HMAC_SHA256` |  **Recommended**  
HMAC with a SHA-256 digest | Yes  
SDK: `hmac-sha384`  
REST: `HMAC_SHA384` |  HMAC with a SHA-384 digest | Yes  
SDK: `hmac-sha512`  
REST: `HMAC_SHA512` |  HMAC with a SHA-512 digest | Yes  
  
### hsm-single-tenant

Algorithm | Description | Quantum-safe  
---|---|---  
SDK: `hmac-sha1`  
REST: `HMAC_SHA1` |  HMAC with a SHA-1 digest  | No  
SDK: `hmac-sha224`  
REST: `HMAC_SHA224` |  HMAC with a SHA-224 digest | Yes  
SDK: `hmac-sha256`  
REST: `HMAC_SHA256` |  **Recommended**  
HMAC with a SHA-256 digest | Yes  
SDK: `hmac-sha384`  
REST: `HMAC_SHA384` |  HMAC with a SHA-384 digest | Yes  
SDK: `hmac-sha512`  
REST: `HMAC_SHA512` |  HMAC with a SHA-512 digest | Yes  
  
### external

Algorithm | Description | Quantum-safe  
---|---|---  
  
### external-vpc

Algorithm | Description | Quantum-safe  
---|---|---  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-12 UTC."],[],[]] 
