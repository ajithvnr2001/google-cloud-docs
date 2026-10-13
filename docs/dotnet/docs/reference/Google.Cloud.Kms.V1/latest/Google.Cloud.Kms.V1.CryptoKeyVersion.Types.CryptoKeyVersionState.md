---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState
title: Google Cloud Key Management Service v1 API - Enum CryptoKeyVersion.Types.CryptoKeyVersionState (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:01.460096+00:00
---

# Google Cloud Key Management Service v1 API - Enum CryptoKeyVersion.Types.CryptoKeyVersionState (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Enum CryptoKeyVersion.Types.CryptoKeyVersionState (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public enum CryptoKeyVersion.Types.CryptoKeyVersionState

Reference documentation and code samples for the Google Cloud Key Management Service v1 API enum CryptoKeyVersion.Types.CryptoKeyVersionState.

The state of a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion], indicating if it can be used.

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Fields   
  
---  
**Name** | **Description**  
`DestroyScheduled` | This version is scheduled for destruction, and will be destroyed soon. Call [RestoreCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.RestoreCryptoKeyVersion] to put it back into the [DISABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DISABLED] state.  
`Destroyed` | The key material of this version is destroyed and no longer stored. This version may only become [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED] again if this version is [reimport_eligible][google.cloud.kms.v1.CryptoKeyVersion.reimport_eligible] and the original key material is reimported with a call to [KeyManagementService.ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].  
`Disabled` | This version may not be used, but the key material is still available, and the version can be placed back into the [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED] state.  
`Enabled` | This version may be used for cryptographic operations.  
`ExternalDestructionFailed` | This version was destroyed, and it may not be used or enabled again. However, Cloud KMS could not confirm that the corresponding key material residing in an external key manager was destroyed. Additional details can be found in [CryptoKeyVersion.external_destruction_failure_reason][google.cloud.kms.v1.CryptoKeyVersion.external_destruction_failure_reason].  
`GenerationFailed` | This version was not generated successfully. It may not be used, enabled, disabled, or destroyed. Additional details can be found in [CryptoKeyVersion.generation_failure_reason][google.cloud.kms.v1.CryptoKeyVersion.generation_failure_reason].  
`ImportFailed` | This version was not imported successfully. It may not be used, enabled, disabled, or destroyed. The submitted key material has been discarded. Additional details can be found in [CryptoKeyVersion.import_failure_reason][google.cloud.kms.v1.CryptoKeyVersion.import_failure_reason].  
`PendingExternalDestruction` | This version was destroyed, and it may not be used or enabled again. Cloud KMS is waiting for the corresponding key material residing in an external key manager to be destroyed.  
`PendingGeneration` | This version is still being generated. It may not be used, enabled, disabled, or destroyed yet. Cloud KMS will automatically mark this version [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED] as soon as the version is ready.  
`PendingImport` | This version is still being imported. It may not be used, enabled, disabled, or destroyed yet. Cloud KMS will automatically mark this version [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED] as soon as the version is ready.  
`Unspecified` | Not specified.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
