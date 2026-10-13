---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest
title: KMS Inventory v1 API - Class GetProtectedResourcesSummaryRequest (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:48:26.505078+00:00
---

# KMS Inventory v1 API - Class GetProtectedResourcesSummaryRequest (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  KMS Inventory v1 API - Class GetProtectedResourcesSummaryRequest (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.5.0/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.4.0/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.3.0/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.2.0/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.1.0/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.0.0/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)


    
    
    public sealed class GetProtectedResourcesSummaryRequest : IMessage<GetProtectedResourcesSummaryRequest>, IEquatable<GetProtectedResourcesSummaryRequest>, IDeepCloneable<GetProtectedResourcesSummaryRequest>, IBufferMessage, IMessage

Reference documentation and code samples for the KMS Inventory v1 API class GetProtectedResourcesSummaryRequest.

Request message for [KeyTrackingService.GetProtectedResourcesSummary][google.cloud.kms.inventory.v1.KeyTrackingService.GetProtectedResourcesSummary].

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > GetProtectedResourcesSummaryRequest

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[GetProtectedResourcesSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[GetProtectedResourcesSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[GetProtectedResourcesSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.Inventory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1)

## Assembly

Google.Cloud.Kms.Inventory.V1.dll

## Constructors 

### GetProtectedResourcesSummaryRequest()
    
    
    public GetProtectedResourcesSummaryRequest()

### GetProtectedResourcesSummaryRequest(GetProtectedResourcesSummaryRequest)
    
    
    public GetProtectedResourcesSummaryRequest(GetProtectedResourcesSummaryRequest other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[GetProtectedResourcesSummaryRequest](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest)`  
  
  
## Properties 

### FallbackScope
    
    
    public FallbackScope FallbackScope { get; set; }

Optional. The scope to use if the kms organization service account is not configured.

**Property Value**  
---  
**Type** | **Description**  
`[FallbackScope](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.FallbackScope)` |   
  
### Name
    
    
    public string Name { get; set; }

Required. The resource name of the [CryptoKey][google.cloud.kms.v1.CryptoKey].

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProtectedResourcesSummaryName
    
    
    public ProtectedResourcesSummaryName ProtectedResourcesSummaryName { get; set; }

[ProtectedResourcesSummaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummaryName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.GetProtectedResourcesSummaryRequest#Google_Cloud_Kms_Inventory_V1_GetProtectedResourcesSummaryRequest_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProtectedResourcesSummaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummaryName)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
