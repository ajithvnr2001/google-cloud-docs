---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types.DocumentMetadata
title: Discovery Engine v1 API - Class Chunk.Types.DocumentMetadata (1.16.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:26:23.953679+00:00
---

# Discovery Engine v1 API - Class Chunk.Types.DocumentMetadata (1.16.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types.DocumentMetadata

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Discovery Engine v1 API - Class Chunk.Types.DocumentMetadata (1.16.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.16.0 (latest)  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.3.0  1.2.0  1.1.0  1.0.0-beta06 
    
    
    public sealed class Chunk.Types.DocumentMetadata : IMessage<Chunk.Types.DocumentMetadata>, IEquatable<Chunk.Types.DocumentMetadata>, IDeepCloneable<Chunk.Types.DocumentMetadata>, IBufferMessage, IMessage

Reference documentation and code samples for the Discovery Engine v1 API class Chunk.Types.DocumentMetadata.

Document metadata contains the information of the document of the current chunk.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Chunk.Types.DocumentMetadata

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types)[DocumentMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types.DocumentMetadata), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types)[DocumentMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types.DocumentMetadata), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types)[DocumentMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types.DocumentMetadata), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.DiscoveryEngine.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1)

## Assembly

Google.Cloud.DiscoveryEngine.V1.dll

## Constructors 

### DocumentMetadata()
    
    
    public DocumentMetadata()

### DocumentMetadata(DocumentMetadata)
    
    
    public DocumentMetadata(Chunk.Types.DocumentMetadata other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types)[DocumentMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.DiscoveryEngine.V1/latest/Google.Cloud.DiscoveryEngine.V1.Chunk.Types.DocumentMetadata)`  
  
  
## Properties 

### StructData
    
    
    public Struct StructData { get; set; }

Data representation. The structured JSON data for the document. It should conform to the registered [Schema][google.cloud.discoveryengine.v1.Schema] or an `INVALID_ARGUMENT` error is thrown.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### Title
    
    
    public string Title { get; set; }

Title of the document.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Uri
    
    
    public string Uri { get; set; }

Uri of the document.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
