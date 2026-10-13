---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey
title: Google Cloud Key Management Service v1 API - Class CryptoKey (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:59.785255+00:00
---

# Google Cloud Key Management Service v1 API - Class CryptoKey (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class CryptoKey (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class CryptoKey : IMessage<CryptoKey>, IEquatable<CryptoKey>, IDeepCloneable<CryptoKey>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class CryptoKey.

A [CryptoKey][google.cloud.kms.v1.CryptoKey] represents a logical key that can be used for cryptographic operations.

A [CryptoKey][google.cloud.kms.v1.CryptoKey] is made up of zero or more [versions][google.cloud.kms.v1.CryptoKeyVersion], which represent the actual key material used in cryptographic operations.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CryptoKey

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### CryptoKey()
    
    
    public CryptoKey()

### CryptoKey(CryptoKey)
    
    
    public CryptoKey(CryptoKey other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey)`  
  
  
## Properties 

### CreateTime
    
    
    public Timestamp CreateTime { get; set; }

Output only. The time at which this [CryptoKey][google.cloud.kms.v1.CryptoKey] was created.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### CryptoKeyBackend
    
    
    public string CryptoKeyBackend { get; set; }

Immutable. The resource name of the backend environment where the key material for all [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] associated with this [CryptoKey][google.cloud.kms.v1.CryptoKey] reside and where all related cryptographic operations are performed. Only applicable if [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] have a [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of [EXTERNAL_VPC][google.cloud.kms.v1.ProtectionLevel.EXTERNAL_VPC], with the resource name in the format `projects/*/locations/*/ekmConnections/*`. Only applicable if [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] have a [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of [HSM_SINGLE_TENANT][google.cloud.kms.v1.ProtectionLevel.HSM_SINGLE_TENANT], with the resource name in the format `projects/*/locations/*/singleTenantHsmInstances/*`. Note, this list is non-exhaustive and may apply to additional [ProtectionLevels][google.cloud.kms.v1.ProtectionLevel] in the future.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### CryptoKeyBackendAsResourceName
    
    
    public IResourceName CryptoKeyBackendAsResourceName { get; set; }

[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)-typed view over the [CryptoKeyBackend](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey#Google_Cloud_Kms_V1_CryptoKey_CryptoKeyBackend) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[IResourceName](https://cloud.google.com/dotnet/docs/reference/Google.Api.Gax/latest/Google.Api.Gax.IResourceName.html)` |   
  
### CryptoKeyName
    
    
    public CryptoKeyName CryptoKeyName { get; set; }

[CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey#Google_Cloud_Kms_V1_CryptoKey_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyName)` |   
  
### DestroyScheduledDuration
    
    
    public Duration DestroyScheduledDuration { get; set; }

Immutable. The period of time that versions of this key spend in the [DESTROY_SCHEDULED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROY_SCHEDULED] state before transitioning to [DESTROYED][google.cloud.kms.v1.CryptoKeyVersion.CryptoKeyVersionState.DESTROYED]. If not specified at creation time, the default duration is 30 days.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### ImportOnly
    
    
    public bool ImportOnly { get; set; }

Immutable. Whether this key may contain imported versions only.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### KeyAccessJustificationsPolicy
    
    
    public KeyAccessJustificationsPolicy KeyAccessJustificationsPolicy { get; set; }

Optional. The policy used for Key Access Justifications Policy Enforcement. If this field is present and this key is enrolled in Key Access Justifications Policy Enforcement, the policy will be evaluated in encrypt, decrypt, and sign operations, and the operation will fail if rejected by the policy. The policy is defined by specifying zero or more allowed justification codes. <https://cloud.google.com/assured-workloads/key-access-justifications/docs/justification-codes> By default, this field is absent, and all justification codes are allowed. If the `key_access_justifications_policy.allowed_access_reasons` is empty (zero allowed justification code), all encrypt, decrypt, and sign operations will fail.

**Property Value**  
---  
**Type** | **Description**  
`[KeyAccessJustificationsPolicy](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyAccessJustificationsPolicy)` |   
  
### Labels
    
    
    public MapField<string, string> Labels { get; }

Labels with user-defined metadata. For more information, see [Labeling Keys](https://cloud.google.com/kms/docs/labeling-keys).

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Name
    
    
    public string Name { get; set; }

Output only. The resource name for this [CryptoKey][google.cloud.kms.v1.CryptoKey] in the format `projects/*/locations/*/keyRings/*/cryptoKeys/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### NextRotationTime
    
    
    public Timestamp NextRotationTime { get; set; }

At [next_rotation_time][google.cloud.kms.v1.CryptoKey.next_rotation_time], the Key Management Service will automatically:

  1. Create a new version of this [CryptoKey][google.cloud.kms.v1.CryptoKey].
  2. Mark the new version as primary.



Key rotations performed manually via [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] and [UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion] do not affect [next_rotation_time][google.cloud.kms.v1.CryptoKey.next_rotation_time].

Keys with [purpose][google.cloud.kms.v1.CryptoKey.purpose] [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT] support automatic rotation. For other keys, this field must be omitted.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Primary
    
    
    public CryptoKeyVersion Primary { get; set; }

Output only. A copy of the "primary" [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] that will be used by [Encrypt][google.cloud.kms.v1.KeyManagementService.Encrypt] when this [CryptoKey][google.cloud.kms.v1.CryptoKey] is given in [EncryptRequest.name][google.cloud.kms.v1.EncryptRequest.name].

The [CryptoKey][google.cloud.kms.v1.CryptoKey]'s primary version can be updated via [UpdateCryptoKeyPrimaryVersion][google.cloud.kms.v1.KeyManagementService.UpdateCryptoKeyPrimaryVersion].

Keys with [purpose][google.cloud.kms.v1.CryptoKey.purpose] [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT] may have a primary. For other keys, this field will be omitted.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyVersion](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersion)` |   
  
### Purpose
    
    
    public CryptoKey.Types.CryptoKeyPurpose Purpose { get; set; }

Immutable. The immutable purpose of this [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types)[CryptoKeyPurpose](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.Types.CryptoKeyPurpose)` |   
  
### RotationPeriod
    
    
    public Duration RotationPeriod { get; set; }

[next_rotation_time][google.cloud.kms.v1.CryptoKey.next_rotation_time] will be advanced by this period when the service automatically rotates a key. Must be at least 24 hours and at most 876,000 hours.

If [rotation_period][google.cloud.kms.v1.CryptoKey.rotation_period] is set, [next_rotation_time][google.cloud.kms.v1.CryptoKey.next_rotation_time] must also be set.

Keys with [purpose][google.cloud.kms.v1.CryptoKey.purpose] [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT] support automatic rotation. For other keys, this field must be omitted.

**Property Value**  
---  
**Type** | **Description**  
`[Duration](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Duration.html)` |   
  
### RotationScheduleCase
    
    
    public CryptoKey.RotationScheduleOneofCase RotationScheduleCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey)[RotationScheduleOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey.RotationScheduleOneofCase)` |   
  
### VersionTemplate
    
    
    public CryptoKeyVersionTemplate VersionTemplate { get; set; }

A template describing settings for new [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] instances. The properties of new [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] instances created by either [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] or auto-rotation are controlled by this template.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyVersionTemplate](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionTemplate)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
