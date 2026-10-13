---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose
title: Google Cloud Key Management Service v1 API - Enum CryptoKey.Types.CryptoKeyPurpose (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:00.069340+00:00
---

# Google Cloud Key Management Service v1 API - Enum CryptoKey.Types.CryptoKeyPurpose (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Enum CryptoKey.Types.CryptoKeyPurpose (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public enum CryptoKey.Types.CryptoKeyPurpose

Reference documentation and code samples for the Google Cloud Key Management Service v1 API enum CryptoKey.Types.CryptoKeyPurpose.

[CryptoKeyPurpose][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose] describes the cryptographic capabilities of a [CryptoKey][google.cloud.kms.v1.CryptoKey]. A given key can only be used for the operations allowed by its purpose. For more information, see [Key purposes](https://cloud.google.com/kms/docs/algorithms#key_purposes).

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`AesWrapping` | [CryptoKeys][google.cloud.kms.v1.CryptoKey] with this purpose may be used for AES key  
`AsymmetricDecrypt` | [CryptoKeys][google.cloud.kms.v1.CryptoKey] with this purpose may be used with [AsymmetricDecrypt][google.cloud.kms.v1.KeyManagementService.AsymmetricDecrypt] and [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].  
`AsymmetricSign` | [CryptoKeys][google.cloud.kms.v1.CryptoKey] with this purpose may be used with [AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign] and [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey].  
`EncryptDecrypt` | [CryptoKeys][google.cloud.kms.v1.CryptoKey] with this purpose may be used with [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt] and [Decrypt][google.cloud.kms.v1.KeyManagementService.Decrypt].  
`KeyEncapsulation` | [CryptoKeys][google.cloud.kms.v1.CryptoKey] with this purpose may be used with [GetPublicKey][google.cloud.kms.v1.KeyManagementService.GetPublicKey] and [Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].  
`Mac` | [CryptoKeys][google.cloud.kms.v1.CryptoKey] with this purpose may be used with [MacSign][google.cloud.kms.v1.KeyManagementService.MacSign].  
`RawEncryptDecrypt` | [CryptoKeys][google.cloud.kms.v1.CryptoKey] with this purpose may be used with [RawEncrypt][google.cloud.kms.v1.KeyManagementService.RawEncrypt] and [RawDecrypt][google.cloud.kms.v1.KeyManagementService.RawDecrypt]. This purpose is meant to be used for interoperable symmetric encryption and does not support automatic CryptoKey rotation.  
`Unspecified` | Not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
