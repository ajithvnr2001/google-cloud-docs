---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary
title: KMS Inventory v1 API - Class ProtectedResourcesSummary (1.6.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:17:06.677722+00:00
---

# KMS Inventory v1 API - Class ProtectedResourcesSummary (1.6.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  KMS Inventory v1 API - Class ProtectedResourcesSummary (1.6.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 1.6.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)
  * [ 1.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.5.0/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)
  * [ 1.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.4.0/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)
  * [ 1.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.3.0/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.2.0/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.1.0/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/1.0.0/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)


    
    
    public sealed class ProtectedResourcesSummary : IMessage<ProtectedResourcesSummary>, IEquatable<ProtectedResourcesSummary>, IDeepCloneable<ProtectedResourcesSummary>, IBufferMessage, IMessage

Reference documentation and code samples for the KMS Inventory v1 API class ProtectedResourcesSummary.

Aggregate information about the resources protected by a Cloud KMS key in the same Cloud organization/project as the key.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ProtectedResourcesSummary

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ProtectedResourcesSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ProtectedResourcesSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ProtectedResourcesSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Kms.Inventory.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1)

## Assembly

Google.Cloud.Kms.Inventory.V1.dll

## Constructors 

### ProtectedResourcesSummary()
    
    
    public ProtectedResourcesSummary()

### ProtectedResourcesSummary(ProtectedResourcesSummary)
    
    
    public ProtectedResourcesSummary(ProtectedResourcesSummary other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ProtectedResourcesSummary](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary)`  
  
  
## Properties 

### CloudProducts
    
    
    public MapField<string, long> CloudProducts { get; }

The number of resources protected by the key grouped by Cloud product.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Locations
    
    
    public MapField<string, long> Locations { get; }

The number of resources protected by the key grouped by region.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Name
    
    
    public string Name { get; set; }

The full name of the ProtectedResourcesSummary resource. Example: projects/test-project/locations/us/keyRings/test-keyring/cryptoKeys/test-key/protectedResourcesSummary

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ProjectCount
    
    
    public int ProjectCount { get; set; }

The number of distinct Cloud projects in the same Cloud organization as the key that have resources protected by the key.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ProtectedResourcesSummaryName
    
    
    public ProtectedResourcesSummaryName ProtectedResourcesSummaryName { get; set; }

[ProtectedResourcesSummaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummaryName)-typed view over the [Name](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummary#Google_Cloud_Kms_Inventory_V1_ProtectedResourcesSummary_Name) resource name property.

**Property Value**  
---  
**Type** | **Description**  
`[ProtectedResourcesSummaryName](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.ProtectedResourcesSummaryName)` |   
  
### ResourceCount
    
    
    public long ResourceCount { get; set; }

The total number of protected resources in the same Cloud organization as the key.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ResourceTypes
    
    
    public MapField<string, long> ResourceTypes { get; }

The number of resources protected by the key grouped by resource type.

**Property Value**  
---  
**Type** | **Description**  
`[MapField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.MapField-2.html)[string](https://learn.microsoft.com/dotnet/api/system.string)[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Warnings
    
    
    public RepeatedField<Warning> Warnings { get; }

Warning messages for the state of response [ProtectedResourcesSummary][google.cloud.kms.inventory.v1.ProtectedResourcesSummary] For example, if the organization service account is not configured, INSUFFICIENT_PERMISSIONS_PARTIAL_DATA warning will be returned.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[Warning](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Kms.Inventory.V1/latest/Google.Cloud.Kms.Inventory.V1.Warning)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
