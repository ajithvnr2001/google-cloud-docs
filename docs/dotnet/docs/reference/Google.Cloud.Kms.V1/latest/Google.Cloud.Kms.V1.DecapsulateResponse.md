---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateResponse
title: Google Cloud Key Management Service v1 API - Class DecapsulateResponse (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:01.947614+00:00
---

# Google Cloud Key Management Service v1 API - Class DecapsulateResponse (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateResponse

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class DecapsulateResponse (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class DecapsulateResponse : IMessage<DecapsulateResponse>, IEquatable<DecapsulateResponse>, IDeepCloneable<DecapsulateResponse>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class DecapsulateResponse.

Response message for [KeyManagementService.Decapsulate][google.cloud.kms.v1.KeyManagementService.Decapsulate].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DecapsulateResponse

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DecapsulateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateResponse), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DecapsulateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateResponse), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DecapsulateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateResponse), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### DecapsulateResponse()
    
    
    public DecapsulateResponse()

### DecapsulateResponse(DecapsulateResponse)
    
    
    public DecapsulateResponse(DecapsulateResponse other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DecapsulateResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DecapsulateResponse)`  
  
  
## Properties 

### HasSharedSecretCrc32C
    
    
    public bool HasSharedSecretCrc32C { get; }

Gets whether the "shared_secret_crc32c" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Name
    
    
    public string Name { get; set; }

The resource name of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] used for decapsulation. Check this field to verify that the intended resource was used for decapsulation.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProtectionLevel
    
    
    public ProtectionLevel ProtectionLevel { get; set; }

The [ProtectionLevel][google.cloud.kms.v1.ProtectionLevel] of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] used in decapsulation.

**Property Value**  
---  
**Type** | **Description**  
`[ProtectionLevel](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.ProtectionLevel)` |   
  
### SharedSecret
    
    
    public ByteString SharedSecret { get; set; }

The decapsulated shared_secret originally encapsulated with the matching public key.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### SharedSecretCrc32C
    
    
    public long SharedSecretCrc32C { get; set; }

Integrity verification field. A CRC32C checksum of the returned [DecapsulateResponse.shared_secret][google.cloud.kms.v1.DecapsulateResponse.shared_secret]. An integrity check of [DecapsulateResponse.shared_secret][google.cloud.kms.v1.DecapsulateResponse.shared_secret] can be performed by computing the CRC32C checksum of [DecapsulateResponse.shared_secret][google.cloud.kms.v1.DecapsulateResponse.shared_secret] and comparing your results to this field. Discard the response in case of non-matching checksum values, and perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: receiving this response message indicates that [KeyManagementService][google.cloud.kms.v1.KeyManagementService] is able to successfully decrypt the [ciphertext][google.cloud.kms.v1.DecapsulateRequest.ciphertext]. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### VerifiedCiphertextCrc32C
    
    
    public bool VerifiedCiphertextCrc32C { get; set; }

Integrity verification field. A flag indicating whether [DecapsulateRequest.ciphertext_crc32c][google.cloud.kms.v1.DecapsulateRequest.ciphertext_crc32c] was received by [KeyManagementService][google.cloud.kms.v1.KeyManagementService] and used for the integrity verification of the [ciphertext][google.cloud.kms.v1.DecapsulateRequest.ciphertext]. A false value of this field indicates either that [DecapsulateRequest.ciphertext_crc32c][google.cloud.kms.v1.DecapsulateRequest.ciphertext_crc32c] was left unset or that it was not delivered to [KeyManagementService][google.cloud.kms.v1.KeyManagementService]. If you've set [DecapsulateRequest.ciphertext_crc32c][google.cloud.kms.v1.DecapsulateRequest.ciphertext_crc32c] but this field is still false, discard the response and perform a limited number of retries.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
