---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PkixPublicKey.Types.SignatureAlgorithm
title: Binary Authorization v1beta1 API - Enum PkixPublicKey.Types.SignatureAlgorithm (2.0.0-beta10) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:53.643403+00:00
---

# Binary Authorization v1beta1 API - Enum PkixPublicKey.Types.SignatureAlgorithm (2.0.0-beta10)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1.PkixPublicKey.Types.SignatureAlgorithm

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Binary Authorization v1beta1 API - Enum PkixPublicKey.Types.SignatureAlgorithm (2.0.0-beta10) Stay organized with collections  Save and categorize content based on your preferences. 

2.0.0-beta10 (latest)  2.0.0-beta09  1.0.0-beta05 
    
    
    public enum PkixPublicKey.Types.SignatureAlgorithm

Reference documentation and code samples for the Binary Authorization v1beta1 API enum PkixPublicKey.Types.SignatureAlgorithm.

Represents a signature algorithm and other information necessary to verify signatures with a given public key. This is based primarily on the public key types supported by Tink's PemKeyType, which is in turn based on KMS's supported signing algorithms. See <https://cloud.google.com/kms/docs/algorithms>. In the future, BinAuthz might support additional public key types independently of Tink and/or KMS.

## Namespace

[Google.Cloud.BinaryAuthorization.V1Beta1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BinaryAuthorization.V1Beta1/latest/Google.Cloud.BinaryAuthorization.V1Beta1)

## Assembly

Google.Cloud.BinaryAuthorization.V1Beta1.dll

## Fields   
  
---  
**Name** | **Description**  
`EcSignP256Sha256` | ECDSA on the NIST P-256 curve with a SHA256 digest.  
`EcSignP384Sha384` | ECDSA on the NIST P-384 curve with a SHA384 digest.  
`EcSignP521Sha512` | ECDSA on the NIST P-521 curve with a SHA512 digest.  
`EcdsaP256Sha256` | ECDSA on the NIST P-256 curve with a SHA256 digest.  
`EcdsaP384Sha384` | ECDSA on the NIST P-384 curve with a SHA384 digest.  
`EcdsaP521Sha512` | ECDSA on the NIST P-521 curve with a SHA512 digest.  
`MlDsa65` | ML-DSA-65 Post-Quantum Cryptography signature algorithm.  
`RsaPss2048Sha256` | RSASSA-PSS 2048 bit key with a SHA256 digest.  
`RsaPss3072Sha256` | RSASSA-PSS 3072 bit key with a SHA256 digest.  
`RsaPss4096Sha256` | RSASSA-PSS 4096 bit key with a SHA256 digest.  
`RsaPss4096Sha512` | RSASSA-PSS 4096 bit key with a SHA512 digest.  
`RsaSignPkcs12048Sha256` | RSASSA-PKCS1-v1_5 with a 2048 bit key and a SHA256 digest.  
`RsaSignPkcs13072Sha256` | RSASSA-PKCS1-v1_5 with a 3072 bit key and a SHA256 digest.  
`RsaSignPkcs14096Sha256` | RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA256 digest.  
`RsaSignPkcs14096Sha512` | RSASSA-PKCS1-v1_5 with a 4096 bit key and a SHA512 digest.  
`RsaSignPss2048Sha256` | RSASSA-PSS 2048 bit key with a SHA256 digest.  
`RsaSignPss3072Sha256` | RSASSA-PSS 3072 bit key with a SHA256 digest.  
`RsaSignPss4096Sha256` | RSASSA-PSS 4096 bit key with a SHA256 digest.  
`RsaSignPss4096Sha512` | RSASSA-PSS 4096 bit key with a SHA512 digest.  
`Unspecified` | Not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
