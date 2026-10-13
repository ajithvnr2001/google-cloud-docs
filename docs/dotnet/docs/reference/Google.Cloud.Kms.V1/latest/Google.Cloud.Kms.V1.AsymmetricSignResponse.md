---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse
title: Google Cloud Key Management Service v1 API - Class AsymmetricSignResponse (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:54.042484+00:00
---

# Google Cloud Key Management Service v1 API - Class AsymmetricSignResponse (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class AsymmetricSignResponse (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class AsymmetricSignResponse : IMessage<AsymmetricSignResponse>, IEquatable<AsymmetricSignResponse>, IDeepCloneable<AsymmetricSignResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class AsymmetricSignResponse.

Response message for [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AsymmetricSignResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AsymmetricSignResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AsymmetricSignResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AsymmetricSignResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### AsymmetricSignResponse()
    
    
    public AsymmetricSignResponse()

### AsymmetricSignResponse(AsymmetricSignResponse)
    
    
    public AsymmetricSignResponse(AsymmetricSignResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AsymmetricSignResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignResponse)`  
  
  
## Properties 

### Name
    
    
    public string Name { get; set; }

The resource name of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] used for signing. Check this field to verify that the intended resource was used for signing.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProtectionLevel
    
    
    public ProtectionLevel ProtectionLevel { get; set; }

The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] used for signing.

**Property Value**  
---  
**Type** | **Description**  
`[ProtectionLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel)` |   
  
### Signature
    
    
    public ByteString Signature { get; set; }

The created signature.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### SignatureCrc32C
    
    
    public long? SignatureCrc32C { get; set; }

Integrity verification field. A CRC32C checksum of the returned [AsymmetricSignResponse.signature][google.cloud.kms.v1.AsymmetricSignResponse.signature]. An integrity check of [AsymmetricSignResponse.signature][google.cloud.kms.v1.AsymmetricSignResponse.signature] can be performed by computing the CRC32C checksum of [AsymmetricSignResponse.signature][google.cloud.kms.v1.AsymmetricSignResponse.signature] and comparing your results to this field. Discard the response in case of non-matching checksum values, and perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### VerifiedDataCrc32C
    
    
    public bool VerifiedDataCrc32C { get; set; }

Integrity verification field. A flag indicating whether [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c] was received by [KeyManagementService][google.cloud.kms.v1.KeyManagementService] and used for the integrity verification of the [data][google.cloud.kms.v1.AsymmetricSignRequest.data]. A false value of this field indicates either that [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c] was left unset or that it was not delivered to [KeyManagementService][google.cloud.kms.v1.KeyManagementService]. If you've set [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c] but this field is still false, discard the response and perform a limited number of retries.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### VerifiedDigestCrc32C
    
    
    public bool VerifiedDigestCrc32C { get; set; }

Integrity verification field. A flag indicating whether [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c] was received by [KeyManagementService][google.cloud.kms.v1.KeyManagementService] and used for the integrity verification of the [digest][google.cloud.kms.v1.AsymmetricSignRequest.digest]. A false value of this field indicates either that [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c] was left unset or that it was not delivered to [KeyManagementService][google.cloud.kms.v1.KeyManagementService]. If you've set [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c] but this field is still false, discard the response and perform a limited number of retries.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
