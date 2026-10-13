---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest
title: Google Cloud Key Management Service v1 API - Class CreateCryptoKeyRequest (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:58.562655+00:00
---

# Google Cloud Key Management Service v1 API - Class CreateCryptoKeyRequest (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class CreateCryptoKeyRequest (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class CreateCryptoKeyRequest : IMessage<CreateCryptoKeyRequest>, IEquatable<CreateCryptoKeyRequest>, IDeepCloneable<CreateCryptoKeyRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class CreateCryptoKeyRequest.

Request message for [KeyManagementService.CreateCryptoKey][google.cloud.kms.v1.KeyManagementService.CreateCryptoKey].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > CreateCryptoKeyRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[CreateCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[CreateCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[CreateCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### CreateCryptoKeyRequest()
    
    
    public CreateCryptoKeyRequest()

### CreateCryptoKeyRequest(CreateCryptoKeyRequest)
    
    
    public CreateCryptoKeyRequest(CreateCryptoKeyRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[CreateCryptoKeyRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest)`  
  
  
## Properties 

### CryptoKey
    
    
    public CryptoKey CryptoKey { get; set; }

Required. A [CryptoKey][google.cloud.kms.v1.CryptoKey] with initial field values.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKey](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKey)` |   
  
### CryptoKeyId
    
    
    public string CryptoKeyId { get; set; }

Required. It must be unique within a KeyRing and match the regular expression `[a-zA-Z0-9_-]{1,63}`

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Parent
    
    
    public string Parent { get; set; }

Required. The [name][google.cloud.kms.v1.KeyRing.name] of the KeyRing associated with the [CryptoKeys][google.cloud.kms.v1.CryptoKey].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ParentAsKeyRingName
    
    
    public KeyRingName ParentAsKeyRingName { get; set; }

[KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName)-typed view over the [Parent](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CreateCryptoKeyRequest#Google_Cloud_Kms_V1_CreateCryptoKeyRequest_Parent) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[KeyRingName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.KeyRingName)` |   
  
### SkipInitialVersionCreation
    
    
    public bool SkipInitialVersionCreation { get; set; }

If set to true, the request will create a [CryptoKey][google.cloud.kms.v1.CryptoKey] without any [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion]. You must manually call [CreateCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.CreateCryptoKeyVersion] or [ImportCryptoKeyVersion][google.cloud.kms.v1.KeyManagementService.ImportCryptoKeyVersion] before you can use this [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### TrustedWrappingEnabled
    
    
    public bool TrustedWrappingEnabled { get; set; }

Optional. Whether trusted wrapping will be enabled on the first [CryptoKeyVersions][google.cloud.kms.v1.CryptoKeyVersion] created for this [CryptoKey][google.cloud.kms.v1.CryptoKey]. This field is only supported for keys with [CryptoKeyVersionTemplate.protection_level][google.cloud.kms.v1.CryptoKeyVersionTemplate.protection_level] [HSM_SINGLE_TENANT][google.cloud.kms.v1.ProtectionLevel.HSM_SINGLE_TENANT]. This field is supported for all [CryptoKeyPurposes][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose] except [ENCRYPT_DECRYPT][google.cloud.kms.v1.CryptoKey.CryptoKeyPurpose.ENCRYPT_DECRYPT].

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
