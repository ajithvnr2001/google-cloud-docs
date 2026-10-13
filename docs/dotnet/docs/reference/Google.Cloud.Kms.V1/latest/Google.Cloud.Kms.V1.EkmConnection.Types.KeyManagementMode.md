---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types.KeyManagementMode
title: Google Cloud Key Management Service v1 API - Enum EkmConnection.Types.KeyManagementMode (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:04.195753+00:00
---

# Google Cloud Key Management Service v1 API - Enum EkmConnection.Types.KeyManagementMode (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.EkmConnection.Types.KeyManagementMode

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Enum EkmConnection.Types.KeyManagementMode (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public enum EkmConnection.Types.KeyManagementMode

Reference documentation and code samples for the Google Cloud Key Management Service v1 API enum EkmConnection.Types.KeyManagementMode.

[KeyManagementMode][google.cloud.kms.v1.EkmConnection.KeyManagementMode] describes who can perform control plane cryptographic operations using this [EkmConnection][google.cloud.kms.v1.EkmConnection].

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`CloudKms` | All [CryptoKeys][google.cloud.kms.v1.CryptoKey] created with this [EkmConnection][google.cloud.kms.v1.EkmConnection] use EKM-side key management operations initiated from Cloud KMS. This means that:

  * When a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] associated with this [EkmConnection][google.cloud.kms.v1.EkmConnection] is created, the EKM automatically generates new key material and a new key path. The caller cannot supply the key path of pre-existing external key material.
  * Destruction of external key material associated with this [EkmConnection][google.cloud.kms.v1.EkmConnection] can be requested by calling [DestroyCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.DestroyCryptoKeyVersion].
  * Automatic rotation of key material is supported.

  
`Manual` | EKM-side key management operations on [CryptoKeys][google.cloud.kms.v1.CryptoKey] created with this [EkmConnection][google.cloud.kms.v1.EkmConnection] must be initiated from the EKM directly and cannot be performed from Cloud KMS. This means that:

  * When creating a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] associated with this [EkmConnection][google.cloud.kms.v1.EkmConnection], the caller must supply the key path of pre-existing external key material that will be linked to the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].
  * Destruction of external key material cannot be requested via the Cloud KMS API and must be performed directly in the EKM.
  * Automatic rotation of key material is not supported.

  
`Unspecified` | Not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
