---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata
title: Google Cloud Key Management Service v1 API - Class DeleteCryptoKeyMetadata (3.27.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:49:02.401751+00:00
---

# Google Cloud Key Management Service v1 API - Class DeleteCryptoKeyMetadata (3.27.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Key Management Service v1 API - Class DeleteCryptoKeyMetadata (3.27.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.27.0 (latest)  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.9.0  2.8.0  2.7.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class DeleteCryptoKeyMetadata : IMessage<DeleteCryptoKeyMetadata>, IEquatable<DeleteCryptoKeyMetadata>, IDeepCloneable<DeleteCryptoKeyMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Key Management Service v1 API class DeleteCryptoKeyMetadata.

Represents the metadata of the [KeyManagementService.DeleteCryptoKey][google.cloud.kms.v1.KeyManagementService.DeleteCryptoKey] long-running operation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > DeleteCryptoKeyMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[DeleteCryptoKeyMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[DeleteCryptoKeyMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[DeleteCryptoKeyMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1)

## Assembly

Google.Cloud.Kms.V1.dll

## Constructors 

### DeleteCryptoKeyMetadata()
    
    
    public DeleteCryptoKeyMetadata()

### DeleteCryptoKeyMetadata(DeleteCryptoKeyMetadata)
    
    
    public DeleteCryptoKeyMetadata(DeleteCryptoKeyMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[DeleteCryptoKeyMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata)`  
  
  
## Properties 

### RetiredResource
    
    
    public string RetiredResource { get; set; }

Output only. The resource name of the [RetiredResource][google.cloud.kms.v1.RetiredResource] created as a result of this operation, in the format `projects/*/locations/*/retiredResources/*`.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### RetiredResourceAsRetiredResourceName
    
    
    public RetiredResourceName RetiredResourceAsRetiredResourceName { get; set; }

[RetiredResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RetiredResourceName)-typed view over the [RetiredResource](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.DeleteCryptoKeyMetadata#Google_Cloud_Kms_V1_DeleteCryptoKeyMetadata_RetiredResource) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[RetiredResourceName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.V1/latest/Google.Cloud.Kms.V1.RetiredResourceName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-12 UTC."],[],[]] 
