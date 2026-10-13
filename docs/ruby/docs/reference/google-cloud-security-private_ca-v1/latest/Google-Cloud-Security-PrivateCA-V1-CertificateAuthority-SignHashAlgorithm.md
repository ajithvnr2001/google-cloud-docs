---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateAuthority-SignHashAlgorithm/
title: Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::CertificateAuthority::SignHashAlgorithm (v2.8.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:59:49.399200+00:00
---

# Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::CertificateAuthority::SignHashAlgorithm (v2.8.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-security-private_ca-v1/latest/Google-Cloud-Security-PrivateCA-V1-CertificateAuthority-SignHashAlgorithm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Certificate Authority Service V1 API - Module Google::Cloud::Security::PrivateCA::V1::CertificateAuthority::SignHashAlgorithm (v2.8.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.8.1 (latest)  2.8.0  2.7.0  2.6.1  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.1  0.1.6 

Reference documentation and code samples for the Certificate Authority Service V1 API module Google::Cloud::Security::PrivateCA::V1::CertificateAuthority::SignHashAlgorithm.

The algorithm of a Cloud KMS CryptoKeyVersion of a [CryptoKey][google.cloud.kms.v1.CryptoKey] with the [CryptoKeyPurpose][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose] value `ASYMMETRIC_SIGN`. These values correspond to the [CryptoKeyVersionAlgorithm][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm] values. For RSA signing algorithms, the PSS algorithms should be preferred, use PKCS1 algorithms if required for compatibility. For further recommendations, see <https://cloud.google.com/kms/docs/algorithms#algorithm_recommendations>.

## Constants 

### SIGN_HASH_ALGORITHM_UNSPECIFIED

**value:** 0  
Not specified.

### RSA_PSS_2048_SHA256

**value:** 1  
maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_2048_SHA256

### RSA_PSS_3072_SHA256

**value:** 2  
maps to CryptoKeyVersionAlgorithm. RSA_SIGN_PSS_3072_SHA256

### RSA_PSS_4096_SHA256

**value:** 3  
maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_4096_SHA256

### RSA_PKCS1_2048_SHA256

**value:** 6  
maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_2048_SHA256

### RSA_PKCS1_3072_SHA256

**value:** 7  
maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_3072_SHA256

### RSA_PKCS1_4096_SHA256

**value:** 8  
maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_4096_SHA256

### EC_P256_SHA256

**value:** 4  
maps to CryptoKeyVersionAlgorithm.EC_SIGN_P256_SHA256

### EC_P384_SHA384

**value:** 5  
maps to CryptoKeyVersionAlgorithm.EC_SIGN_P384_SHA384

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
