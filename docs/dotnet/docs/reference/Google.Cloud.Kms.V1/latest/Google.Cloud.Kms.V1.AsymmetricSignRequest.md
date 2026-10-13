---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest
title: Google Cloud Key Management Service v1 API - Class AsymmetricSignRequest (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:48:54.259541+00:00
---

# Google Cloud Key Management Service v1 API - Class AsymmetricSignRequest (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class AsymmetricSignRequest (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class AsymmetricSignRequest : IMessage<AsymmetricSignRequest>, IEquatable<AsymmetricSignRequest>, IDeepCloneable<AsymmetricSignRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class AsymmetricSignRequest.

Request message for [KeyManagementService.AsymmetricSign][google.cloud.kms.v1.KeyManagementService.AsymmetricSign].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > AsymmetricSignRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[AsymmetricSignRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[AsymmetricSignRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[AsymmetricSignRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### AsymmetricSignRequest()
    
    
    public AsymmetricSignRequest()

### AsymmetricSignRequest(AsymmetricSignRequest)
    
    
    public AsymmetricSignRequest(AsymmetricSignRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[AsymmetricSignRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest)`  
  
  
## Properties 

### CryptoKeyVersionName
    
    
    public CryptoKeyVersionName CryptoKeyVersionName { get; set; }

[CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.AsymmetricSignRequest#Google_Cloud_Kms_V1_AsymmetricSignRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[CryptoKeyVersionName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.CryptoKeyVersionName)` |   
  
### Data
    
    
    public ByteString Data { get; set; }

Optional. The data to sign. It can't be supplied if [AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest] is supplied.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### DataCrc32C
    
    
    public long? DataCrc32C { get; set; }

Optional. An optional CRC32C checksum of the [AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data]. If specified, [KeyManagementService][google.cloud.kms.v1.KeyManagementService] will verify the integrity of the received [AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data] using this checksum. [KeyManagementService][google.cloud.kms.v1.KeyManagementService] will report an error if the checksum verification fails. If you receive a checksum error, your client should verify that CRC32C([AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data]) is equal to [AsymmetricSignRequest.data_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.data_crc32c], and if so, perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Digest
    
    
    public Digest Digest { get; set; }

Optional. The digest of the data to sign. The digest must be produced with the same digest algorithm as specified by the key version's [algorithm][google.cloud.kms.v1.CryptoKeyVersion.algorithm].

This field may not be supplied if [AsymmetricSignRequest.data][google.cloud.kms.v1.AsymmetricSignRequest.data] is supplied.

**Property Value**  
---  
**Type** | **Description**  
`[Digest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.Digest)` |   
  
### DigestCrc32C
    
    
    public long? DigestCrc32C { get; set; }

Optional. An optional CRC32C checksum of the [AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest]. If specified, [KeyManagementService][google.cloud.kms.v1.KeyManagementService] will verify the integrity of the received [AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest] using this checksum. [KeyManagementService][google.cloud.kms.v1.KeyManagementService] will report an error if the checksum verification fails. If you receive a checksum error, your client should verify that CRC32C([AsymmetricSignRequest.digest][google.cloud.kms.v1.AsymmetricSignRequest.digest]) is equal to [AsymmetricSignRequest.digest_crc32c][google.cloud.kms.v1.AsymmetricSignRequest.digest_crc32c], and if so, perform a limited number of retries. A persistent mismatch may indicate an issue in your computation of the CRC32C checksum. Note: This field is defined as int64 for reasons of compatibility across different languages. However, it is a non-negative integer, which will never exceed 2^32-1, and can be safely downconverted to uint32 in languages that support this type.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the [CryptoKeyVersion][google.cloud.kms.v1.CryptoKeyVersion] to use for signing.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
