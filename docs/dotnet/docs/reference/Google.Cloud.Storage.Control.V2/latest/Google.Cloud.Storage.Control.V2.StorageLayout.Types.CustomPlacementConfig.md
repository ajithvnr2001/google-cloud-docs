---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types.CustomPlacementConfig
title: Cloud Storage v2 API - Class StorageLayout.Types.CustomPlacementConfig (1.11.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:44:33.301986+00:00
---

# Cloud Storage v2 API - Class StorageLayout.Types.CustomPlacementConfig (1.11.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types.CustomPlacementConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Cloud Storage v2 API - Class StorageLayout.Types.CustomPlacementConfig (1.11.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.0 (latest)  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.1 
    
    
    public sealed class StorageLayout.Types.CustomPlacementConfig : IMessage<StorageLayout.Types.CustomPlacementConfig>, IEquatable<StorageLayout.Types.CustomPlacementConfig>, IDeepCloneable<StorageLayout.Types.CustomPlacementConfig>, IBufferMessage, IMessage

Reference documentation and code samples for the Cloud Storage v2 API class StorageLayout.Types.CustomPlacementConfig.

Configuration for Custom Dual Regions. It should specify precisely two eligible regions within the same Multiregion. More information on regions may be found [here](https://cloud.google.com/storage/docs/locations).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > StorageLayout.Types.CustomPlacementConfig

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types)[CustomPlacementConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types.CustomPlacementConfig), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types)[CustomPlacementConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types.CustomPlacementConfig), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types)[CustomPlacementConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types.CustomPlacementConfig), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Storage.Control.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2)

## Assembly

Google.Cloud.Storage.Control.V2.dll

## Constructors 

### CustomPlacementConfig()
    
    
    public CustomPlacementConfig()

### CustomPlacementConfig(CustomPlacementConfig)
    
    
    public CustomPlacementConfig(StorageLayout.Types.CustomPlacementConfig other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[StorageLayout](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types)[CustomPlacementConfig](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Storage.Control.V2/latest/Google.Cloud.Storage.Control.V2.StorageLayout.Types.CustomPlacementConfig)`  
  
  
## Properties 

### DataLocations
    
    
    public RepeatedField<string> DataLocations { get; }

List of locations to use for data placement.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-24 UTC."],[],[]] 
