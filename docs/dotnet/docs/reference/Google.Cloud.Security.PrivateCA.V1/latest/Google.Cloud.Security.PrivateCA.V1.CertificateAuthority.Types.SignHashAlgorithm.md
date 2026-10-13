---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateAuthority.Types.SignHashAlgorithm
title: Certificate Authority v1 API - Enum CertificateAuthority.Types.SignHashAlgorithm (3.12.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:34:10.752073+00:00
---

# Certificate Authority v1 API - Enum CertificateAuthority.Types.SignHashAlgorithm (3.12.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1.CertificateAuthority.Types.SignHashAlgorithm

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Certificate Authority v1 API - Enum CertificateAuthority.Types.SignHashAlgorithm (3.12.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.12.0 (latest)  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.3.0  2.2.0  2.1.0  2.0.0  1.0.0 
    
    
    public enum CertificateAuthority.Types.SignHashAlgorithm

Reference documentation and code samples for the Certificate Authority v1 API enum CertificateAuthority.Types.SignHashAlgorithm.

The algorithm of a Cloud KMS CryptoKeyVersion of a [CryptoKey][google.cloud.kms.v1.CryptoKey] with the [CryptoKeyPurpose][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose] value `ASYMMETRIC_SIGN`. These values correspond to the [CryptoKeyVersionAlgorithm][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm] values. For RSA signing algorithms, the PSS algorithms should be preferred, use PKCS1 algorithms if required for compatibility. For further recommendations, see <https://cloud.google.com/kms/docs/algorithms#algorithm_recommendations>.

## Namespace

[Google.Cloud.Security.PrivateCA.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Security.PrivateCA.V1/latest/Google.Cloud.Security.PrivateCA.V1)

## Assembly

Google.Cloud.Security.PrivateCA.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`EcP256Sha256` | maps to CryptoKeyVersionAlgorithm.EC_SIGN_P256_SHA256  
`EcP384Sha384` | maps to CryptoKeyVersionAlgorithm.EC_SIGN_P384_SHA384  
`RsaPkcs12048Sha256` | maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_2048_SHA256  
`RsaPkcs13072Sha256` | maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_3072_SHA256  
`RsaPkcs14096Sha256` | maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PKCS1_4096_SHA256  
`RsaPss2048Sha256` | maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_2048_SHA256  
`RsaPss3072Sha256` | maps to CryptoKeyVersionAlgorithm. RSA_SIGN_PSS_3072_SHA256  
`RsaPss4096Sha256` | maps to CryptoKeyVersionAlgorithm.RSA_SIGN_PSS_4096_SHA256  
`Unspecified` | Not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-30 UTC."],[],[]] 
