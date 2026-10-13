---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion
title: Google Cloud Key Management Service v1 API - Class CryptoKeyVersion (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:00.685492+00:00
---

# Google Cloud Key Management Service v1 API - Class CryptoKeyVersion (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class CryptoKeyVersion (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class CryptoKeyVersion : IMessage<CryptoKeyVersion>, IEquatable<CryptoKeyVersion>, IDeepCloneable<CryptoKeyVersion>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class CryptoKeyVersion.

A [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] represents an individual cryptographic key, and the associated key material.

An [ENABLED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.ENABLED] version can be used for cryptographic operations.

For security reasons, the raw cryptographic key material represented by a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] can never be viewed or exported. It can only be used to encrypt, decrypt, or sign data when an authorized user or application invokes Cloud KMS.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CryptoKeyVersion

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### CryptoKeyVersion()
    
    
    public CryptoKeyVersion()

### CryptoKeyVersion(CryptoKeyVersion)
    
    
    public CryptoKeyVersion(CryptoKeyVersion other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion)`  
  
  
## Properties 

### Algorithm
    
    
    public CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm Algorithm { get; set; }

Output only. The [CryptoKeyVersionAlgorithm][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionAlgorithm] that this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] supports.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types)[CryptoKeyVersionAlgorithm](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionAlgorithm)` |   
  
### Attestation
    
    
    public KeyOperationAttestation Attestation { get; set; }

Output only. Statement that was generated and signed by the HSM at key creation time. Use this statement to verify attributes of the key as stored on the HSM, independently of Google. Only provided for key versions with [protection_level][google.cloud.kms.v1.CryptoKeyVersion.protection_level] [HSM][google.cloud.kms.v1.ProtectionLevel.HSM].

**Property Value**  
---  
**Type** | **Description**  
`[KeyOperationAttestation](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyOperationAttestation)` |   
  
### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time at which this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CryptoKeyVersionName
    
    
    public CryptoKeyVersionName CryptoKeyVersionName { get; set; }

[CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion#Google_Cloud_Kms_V1_CryptoKeyVersion_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName)` |   
  
### DestroyEventTime
    
    
    public Timestamp DestroyEventTime { get; set; }

Output only. The time this CryptoKeyVersion's key material was destroyed. Only present if [state][google.cloud.kms.v1.CryptoKeyVersion.state] is [DESTROYED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROYED].

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### DestroyTime
    
    
    public Timestamp DestroyTime { get; set; }

Output only. The time this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s key material is scheduled for destruction. Only present if [state][google.cloud.kms.v1.CryptoKeyVersion.state] is [DESTROY_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY_SCHEDULED].

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### ExternalDestructionFailureReason
    
    
    public string ExternalDestructionFailureReason { get; set; }

Output only. The root cause of the most recent external destruction failure. Only present if [state][google.cloud.kms.v1.CryptoKeyVersion.state] is [EXTERNAL_DESTRUCTION_FAILED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.EXTERNAL_DESTRUCTION_FAILED].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ExternalProtectionLevelOptions
    
    
    public ExternalProtectionLevelOptions ExternalProtectionLevelOptions { get; set; }

ExternalProtectionLevelOptions stores a group of additional fields for configuring a [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] that are specific to the [EXTERNAL][google.cloud.kms.v1.ProtectionLevel.EXTERNAL] protection level and [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC] protection levels.

**Property Value**  
---  
**Type** | **Description**  
`[ExternalProtectionLevelOptions](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ExternalProtectionLevelOptions)` |   
  
### GenerateTime
    
    
    public Timestamp GenerateTime { get; set; }

Output only. The time this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s key material was generated.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### GenerationFailureReason
    
    
    public string GenerationFailureReason { get; set; }

Output only. The root cause of the most recent generation failure. Only present if [state][google.cloud.kms.v1.CryptoKeyVersion.state] is [GENERATION_FAILED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.GENERATION_FAILED].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HsmTrusted
    
    
    public bool HsmTrusted { get; set; }

Output only. Field indicating that the key wrapping key is trusted. This field is only valid for key purpose [AES_256_WRAPPING][CryptoKey.CryptoKeyPurpose.AES_256_WRAPPING], and protection level [HSM_SINGLE_TENANT][google.cloud.kms.v1.ProtectionLevel.HSM_SINGLE_TENANT].

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ImportFailureReason
    
    
    public string ImportFailureReason { get; set; }

Output only. The root cause of the most recent import failure. Only present if [state][google.cloud.kms.v1.CryptoKeyVersion.state] is [IMPORT_FAILED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.IMPORT_FAILED].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ImportJob
    
    
    public string ImportJob { get; set; }

Output only. The name of the [ImportJob][google.cloud.kms.v1.ImportJob] used in the most recent import of this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]. Only present if the underlying key material was imported.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ImportTime
    
    
    public Timestamp ImportTime { get; set; }

Output only. The time at which this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion]'s key material was most recently imported.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name for this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*/cryptoKeyVersions/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProtectionLevel
    
    
    public ProtectionLevel ProtectionLevel { get; set; }

Output only. The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] describing how crypto operations are performed with this [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].

**Property Value**  
---  
**Type** | **Description**  
`[ProtectionLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel)` |   
  
### ReimportEligible
    
    
    public bool ReimportEligible { get; set; }

Output only. Whether or not this key version is eligible for reimport, by being specified as a target in [ImportCryptoKeyVersionRequest.crypto_key_version][google.cloud.kms.v1.ImportCryptoKeyVersionRequest.crypto_key_version].

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### State
    
    
    public CryptoKeyVersion.Types.CryptoKeyVersionState State { get; set; }

The current state of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion].

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types)[CryptoKeyVersionState](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion.Types.CryptoKeyVersionState)` |   
  
### TrustedWrappingEnabled
    
    
    public bool TrustedWrappingEnabled { get; set; }

Immutable. Field indicating that the key may be wrapped by a trusted key. This field can be set for all key purposes except [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT], and is only valid for keys with protection level [HSM_SINGLE_TENANT][google.cloud.kms.v1.ProtectionLevel.HSM_SINGLE_TENANT]. This field can only be set at creation or import time via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion], or [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion].

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
