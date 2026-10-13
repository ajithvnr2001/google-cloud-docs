---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types.EncryptionConfig
title: Backup and DR Service v1 API - Class BackupVault.Types.EncryptionConfig (2.9.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:13:30.621042+00:00
---

# Backup and DR Service v1 API - Class BackupVault.Types.EncryptionConfig (2.9.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types.EncryptionConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Backup and DR Service v1 API - Class BackupVault.Types.EncryptionConfig (2.9.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.9.0 (latest)  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.0  2.0.0  1.2.0  1.1.0  1.0.0-beta02 
    
    
    public sealed class BackupVault.Types.EncryptionConfig : IMessage<BackupVault.Types.EncryptionConfig>, IEquatable<BackupVault.Types.EncryptionConfig>, IDeepCloneable<BackupVault.Types.EncryptionConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Backup and DR Service v1 API class BackupVault.Types.EncryptionConfig.

Message describing the EncryptionConfig of backup vault. This determines how data within the vault is encrypted at rest.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > BackupVault.Types.EncryptionConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[BackupVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types)[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types.EncryptionConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[BackupVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types)[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types.EncryptionConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[BackupVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types)[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types.EncryptionConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.BackupDR.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1)

## Assembly

Google.Cloud.BackupDR.V1.dll

## Constructors 

### EncryptionConfig()
    
    
    public EncryptionConfig()

### EncryptionConfig(EncryptionConfig)
    
    
    public EncryptionConfig(BackupVault.Types.EncryptionConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[BackupVault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types)[EncryptionConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types.EncryptionConfig)`  
  
  
## Properties 

### HasKmsKeyName
    
    
    public bool HasKmsKeyName { get; }

Gets whether the "kms_key_name" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### KmsKeyName
    
    
    public string KmsKeyName { get; set; }

Optional. The Cloud KMS key name to encrypt backups in this backup vault. Must be in the same region as the vault. Some workload backups like compute disk backups may use their inherited source key instead. Format: projects/{project}/locations/{location}/keyRings/{ring}/cryptoKeys/{key}

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### KmsKeyNameAsCryptoKeyName
    
    
    public CryptoKeyName KmsKeyNameAsCryptoKeyName { get; set; }

[CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.CryptoKeyName)-typed view over the [KmsKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.BackupVault.Types.EncryptionConfig#Google_Cloud_BackupDR_V1_BackupVault_Types_EncryptionConfig_KmsKeyName) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.BackupDR.V1/latest/Google.Cloud.BackupDR.V1.CryptoKeyName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-31 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-31 UTC."],[],[]] 
