---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionAlgorithm/
title: Cloud Key Management Service (KMS) V1 API - Module Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm (v1.16.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:08.726930+00:00
---

# Cloud Key Management Service (KMS) V1 API - Module Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm (v1.16.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionAlgorithm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Key Management Service (KMS) V1 API - Module Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm (v1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.2  1.14.0  1.13.0  1.12.1  1.11.0  1.10.0  1.9.2  1.8.0  1.7.0  1.6.0  1.5.1  1.4.0  1.3.2  1.2.1  1.1.0  1.0.2  0.27.0  0.26.0  0.25.1  0.24.3  0.23.0  0.22.1  0.21.0  0.20.0  0.19.0  0.18.1  0.17.0  0.16.0  0.15.0  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2 

Reference documentation and code samples for the Cloud Key Management Service (KMS) V1 API module Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm.

The algorithm of the [CryptoKeyVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion "Google::Cloud::Kms::V1::CryptoKeyVersion \(class\)"), indicating what parameters must be used for each cryptographic operation.

The [GOOGLE_SYMMETRIC_ENCRYPTION](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionAlgorithm#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionAlgorithm__GOOGLE_SYMMETRIC_ENCRYPTION "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm::GOOGLE_SYMMETRIC_ENCRYPTION \(constant\)") algorithm is usable with [CryptoKey.purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ENCRYPT_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ENCRYPT_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ENCRYPT_DECRYPT \(constant\)").

Algorithms beginning with `RSA_SIGN_` are usable with [CryptoKey.purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ASYMMETRIC_SIGN](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ASYMMETRIC_SIGN "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ASYMMETRIC_SIGN \(constant\)").

The fields in the name after `RSA_SIGN_` correspond to the following parameters: padding algorithm, modulus bit length, and digest algorithm.

For PSS, the salt length used is equal to the length of digest algorithm. For example, [RSA_SIGN_PSS_2048_SHA256](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKeyVersion-CryptoKeyVersionAlgorithm#Google__Cloud__Kms__V1__CryptoKeyVersion__CryptoKeyVersionAlgorithm__RSA_SIGN_PSS_2048_SHA256 "Google::Cloud::Kms::V1::CryptoKeyVersion::CryptoKeyVersionAlgorithm::RSA_SIGN_PSS_2048_SHA256 \(constant\)") will use PSS with a salt length of 256 bits or 32 bytes.

Algorithms beginning with `RSA_DECRYPT_` are usable with [CryptoKey.purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ASYMMETRIC_DECRYPT](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ASYMMETRIC_DECRYPT "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ASYMMETRIC_DECRYPT \(constant\)").

The fields in the name after `RSA_DECRYPT_` correspond to the following parameters: padding algorithm, modulus bit length, and digest algorithm.

Algorithms beginning with `EC_SIGN_` are usable with [CryptoKey.purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [ASYMMETRIC_SIGN](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__ASYMMETRIC_SIGN "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::ASYMMETRIC_SIGN \(constant\)").

The fields in the name after `EC_SIGN_` correspond to the following parameters: elliptic curve, digest algorithm.

Algorithms beginning with `HMAC_` are usable with [CryptoKey.purpose](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey#Google__Cloud__Kms__V1__CryptoKey_purpose_instance_ "Google::Cloud::Kms::V1::CryptoKey#purpose \(method\)") [MAC](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-kms-v1/latest/Google-Cloud-Kms-V1-CryptoKey-CryptoKeyPurpose#Google__Cloud__Kms__V1__CryptoKey__CryptoKeyPurpose__MAC "Google::Cloud::Kms::V1::CryptoKey::CryptoKeyPurpose::MAC \(constant\)").

The suffix following `HMAC_` corresponds to the hash algorithm being used (eg. SHA256).

Algorithms beginning with `PQ_` are post-quantum.

For more information, see [Key purposes and algorithms](https://cloud.google.com/kms/docs/algorithms).

## Constants 

### CRYPTO_KEY_VERSION_ALGORITHM_UNSPECIFIED

**value:** 0  
Not specified.

### GOOGLE_SYMMETRIC_ENCRYPTION

**value:** 1  
Creates symmetric encryption keys.

### AES_128_GCM

**value:** 41  
AES-GCM (Galois Counter Mode) using 128-bit keys.

### AES_256_GCM

**value:** 19  
AES-GCM (Galois Counter Mode) using 256-bit keys.

### AES_128_CBC

**value:** 42  
AES-CBC (Cipher Block Chaining Mode) using 128-bit keys.

### AES_256_CBC

**value:** 43  
AES-CBC (Cipher Block Chaining Mode) using 256-bit keys.

### AES_128_CTR

**value:** 44  
AES-CTR (Counter Mode) using 128-bit keys.

### AES_256_CTR

**value:** 45  
AES-CTR (Counter Mode) using 256-bit keys.

### RSA_SIGN_PSS_2048_SHA256

**value:** 2  
RSASSA-PSS 2048 bit key with a SHA256 digest.

### RSA_SIGN_PSS_3072_SHA256

**value:** 3  
RSASSA-PSS 3072 bit key with a SHA256 digest.

### RSA_SIGN_PSS_4096_SHA256

**value:** 4  
RSASSA-PSS 4096 bit key with a SHA256 digest.

### RSA_SIGN_PSS_4096_SHA512

**value:** 15  
RSASSA-PSS 4096 bit key with a SHA512 digest.

### RSA_SIGN_PKCS1_2048_SHA256

**value:** 5  
RSASSA-PKCS1-v1_5 with a 2048 bit key and a SHA256 digest.

### RSA_SIGN_PKCS1_3072_SHA256

**value:** 6  
RSASSA-PKCS1-v1_5 with a 3072 bit key and a SHA256 digest.

### RSA_SIGN_PKCS1_4096_SHA256

**value:** 7  
RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA256 digest.

### RSA_SIGN_PKCS1_4096_SHA512

**value:** 16  
RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA512 digest.

### RSA_SIGN_RAW_PKCS1_2048

**value:** 28  
RSASSA-PKCS1-v1_5 signing without encoding, with a 2048 bit key.

### RSA_SIGN_RAW_PKCS1_3072

**value:** 29  
RSASSA-PKCS1-v1_5 signing without encoding, with a 3072 bit key.

### RSA_SIGN_RAW_PKCS1_4096

**value:** 30  
RSASSA-PKCS1-v1_5 signing without encoding, with a 4096 bit key.

### RSA_DECRYPT_OAEP_2048_SHA256

**value:** 8  
RSAES-OAEP 2048 bit key with a SHA256 digest.

### RSA_DECRYPT_OAEP_3072_SHA256

**value:** 9  
RSAES-OAEP 3072 bit key with a SHA256 digest.

### RSA_DECRYPT_OAEP_4096_SHA256

**value:** 10  
RSAES-OAEP 4096 bit key with a SHA256 digest.

### RSA_DECRYPT_OAEP_4096_SHA512

**value:** 17  
RSAES-OAEP 4096 bit key with a SHA512 digest.

### RSA_DECRYPT_OAEP_2048_SHA1

**value:** 37  
RSAES-OAEP 2048 bit key with a SHA1 digest.

### RSA_DECRYPT_OAEP_3072_SHA1

**value:** 38  
RSAES-OAEP 3072 bit key with a SHA1 digest.

### RSA_DECRYPT_OAEP_4096_SHA1

**value:** 39  
RSAES-OAEP 4096 bit key with a SHA1 digest.

### EC_SIGN_P256_SHA256

**value:** 12  
ECDSA on the NIST P-256 curve with a SHA256 digest. Other hash functions can also be used: <https://cloud.google.com/kms/docs/create-validate-signatures#ecdsa_support_for_other_hash_algorithms>

### EC_SIGN_P384_SHA384

**value:** 13  
ECDSA on the NIST P-384 curve with a SHA384 digest. Other hash functions can also be used: <https://cloud.google.com/kms/docs/create-validate-signatures#ecdsa_support_for_other_hash_algorithms>

### EC_SIGN_SECP256K1_SHA256

**value:** 31  
ECDSA on the non-NIST secp256k1 curve. This curve is only supported for HSM protection level. Other hash functions can also be used: <https://cloud.google.com/kms/docs/create-validate-signatures#ecdsa_support_for_other_hash_algorithms>

### EC_SIGN_ED25519

**value:** 40  
EdDSA on the Curve25519 in pure mode (taking data as input).

### HMAC_SHA256

**value:** 32  
HMAC-SHA256 signing with a 256 bit key.

### HMAC_SHA1

**value:** 33  
HMAC-SHA1 signing with a 160 bit key.

### HMAC_SHA384

**value:** 34  
HMAC-SHA384 signing with a 384 bit key.

### HMAC_SHA512

**value:** 35  
HMAC-SHA512 signing with a 512 bit key.

### HMAC_SHA224

**value:** 36  
HMAC-SHA224 signing with a 224 bit key.

### EXTERNAL_SYMMETRIC_ENCRYPTION

**value:** 18  
Algorithm representing symmetric encryption by an external key manager.

### ML_KEM_768

**value:** 47  
ML-KEM-768 (FIPS 203)

### ML_KEM_1024

**value:** 48  
ML-KEM-1024 (FIPS 203)

### KEM_XWING

**value:** 63  
X-Wing hybrid KEM combining ML-KEM-768 with X25519 following datatracker.ietf.org/doc/draft-connolly-cfrg-xwing-kem/.

### PQ_SIGN_ML_DSA_44

**value:** 68  
The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 1. Randomized version.

### PQ_SIGN_ML_DSA_65

**value:** 56  
The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 3. Randomized version.

### PQ_SIGN_ML_DSA_87

**value:** 69  
The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 5. Randomized version.

### PQ_SIGN_SLH_DSA_SHA2_128S

**value:** 57  
The post-quantum stateless hash-based digital signature algorithm, at security level 1. Randomized version.

### PQ_SIGN_HASH_SLH_DSA_SHA2_128S_SHA256

**value:** 60  
The post-quantum stateless hash-based digital signature algorithm, at security level 1. Randomized pre-hash version supporting SHA256 digests.

### PQ_SIGN_ML_DSA_44_EXTERNAL_MU

**value:** 70  
The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 1. Randomized version supporting externally-computed message representatives.

### PQ_SIGN_ML_DSA_65_EXTERNAL_MU

**value:** 67  
The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 3. Randomized version supporting externally-computed message representatives.

### PQ_SIGN_ML_DSA_87_EXTERNAL_MU

**value:** 71  
The post-quantum Module-Lattice-Based Digital Signature Algorithm, at security level 5. Randomized version supporting externally-computed message representatives.

### AES_256_KWP

**value:** 73  
AES key wrap with zero padding algorithm (RFC 5649). Can only be used by keys with purpose AES_WRAPPING.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
