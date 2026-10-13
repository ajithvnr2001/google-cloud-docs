---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Cloud-BinaryAuthorization-V1-PkixPublicKey-SignatureAlgorithm/
title: Binary Authorization V1 API - Module Google::Cloud::BinaryAuthorization::V1::PkixPublicKey::SignatureAlgorithm (v1.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:11:42.865583+00:00
---

# Binary Authorization V1 API - Module Google::Cloud::BinaryAuthorization::V1::PkixPublicKey::SignatureAlgorithm (v1.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-binary_authorization-v1/latest/Google-Cloud-BinaryAuthorization-V1-PkixPublicKey-SignatureAlgorithm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Binary Authorization V1 API - Module Google::Cloud::BinaryAuthorization::V1::PkixPublicKey::SignatureAlgorithm (v1.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

1.8.1 (latest)  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.1  1.1.0  1.0.1  0.8.0  0.7.0  0.6.2  0.5.0  0.4.0  0.3.0  0.2.1  0.1.2 

Reference documentation and code samples for the Binary Authorization V1 API module Google::Cloud::BinaryAuthorization::V1::PkixPublicKey::SignatureAlgorithm.

Represents a signature algorithm and other information necessary to verify signatures with a given public key. This is based primarily on the public key types supported by Tink's PemKeyType, which is in turn based on KMS's supported signing [algorithms](https://cloud.google.com/kms/docs/algorithms). In the future, Binary Authorization might support additional public key types independently of Tink and/or KMS.

## Constants 

### SIGNATURE_ALGORITHM_UNSPECIFIED

**value:** 0  
Not specified.

### RSA_PSS_2048_SHA256

**value:** 1  
RSASSA-PSS 2048 bit key with a SHA256 digest.

### RSA_SIGN_PSS_2048_SHA256

**value:** 1  
RSASSA-PSS 2048 bit key with a SHA256 digest.

### RSA_PSS_3072_SHA256

**value:** 2  
RSASSA-PSS 3072 bit key with a SHA256 digest.

### RSA_SIGN_PSS_3072_SHA256

**value:** 2  
RSASSA-PSS 3072 bit key with a SHA256 digest.

### RSA_PSS_4096_SHA256

**value:** 3  
RSASSA-PSS 4096 bit key with a SHA256 digest.

### RSA_SIGN_PSS_4096_SHA256

**value:** 3  
RSASSA-PSS 4096 bit key with a SHA256 digest.

### RSA_PSS_4096_SHA512

**value:** 4  
RSASSA-PSS 4096 bit key with a SHA512 digest.

### RSA_SIGN_PSS_4096_SHA512

**value:** 4  
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

**value:** 8  
RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA512 digest.

### ECDSA_P256_SHA256

**value:** 9  
ECDSA on the NIST P-256 curve with a SHA256 digest.

### EC_SIGN_P256_SHA256

**value:** 9  
ECDSA on the NIST P-256 curve with a SHA256 digest.

### ECDSA_P384_SHA384

**value:** 10  
ECDSA on the NIST P-384 curve with a SHA384 digest.

### EC_SIGN_P384_SHA384

**value:** 10  
ECDSA on the NIST P-384 curve with a SHA384 digest.

### ECDSA_P521_SHA512

**value:** 11  
ECDSA on the NIST P-521 curve with a SHA512 digest.

### EC_SIGN_P521_SHA512

**value:** 11  
ECDSA on the NIST P-521 curve with a SHA512 digest.

### ML_DSA_65

**value:** 13  
ML-DSA-65 Post-Quantum Cryptography signature algorithm.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
