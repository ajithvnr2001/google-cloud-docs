---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.PacketHeader
title: Vision AI v1 API - Class PacketHeader (1.0.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:52:18.319996+00:00
---

# Vision AI v1 API - Class PacketHeader (1.0.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.PacketHeader

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Vision AI v1 API - Class PacketHeader (1.0.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0 (latest)  1.0.0-beta01 
    
    
    public sealed class PacketHeader : IMessage<PacketHeader>, IEquatable<PacketHeader>, IDeepCloneable<PacketHeader>, IBufferMessage, IMessage

Reference documentation and code samples for the Vision AI v1 API class PacketHeader.

The message that represents packet header.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PacketHeader

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PacketHeader](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.PacketHeader), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PacketHeader](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.PacketHeader), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PacketHeader](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.PacketHeader), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.VisionAI.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1)

## Assembly

Google.Cloud.VisionAI.V1.dll

## Constructors 

### PacketHeader()
    
    
    public PacketHeader()

### PacketHeader(PacketHeader)
    
    
    public PacketHeader(PacketHeader other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PacketHeader](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.PacketHeader)`  
  
  
## Properties 

### CaptureTime
    
    
    public Timestamp CaptureTime { get; set; }

Input only. The capture time of the packet.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### Flags
    
    
    public int Flags { get; set; }

Immutable. Packet flag set. SDK will set the flag automatically.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### Metadata
    
    
    public Struct Metadata { get; set; }

Input only. This field is for users to attach user managed metadata.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### SeriesMetadata
    
    
    public SeriesMetadata SeriesMetadata { get; set; }

Input only. Immutable. Metadata that the server needs to know where to write the packets to. It's only required for the first packet.

**Property Value**  
---  
**Type** | **Description**  
`[SeriesMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.SeriesMetadata)` |   
  
### ServerMetadata
    
    
    public ServerMetadata ServerMetadata { get; set; }

Output only. Metadata that the server appends to each packet before sending it to receivers. You don't need to set a value for this field when sending packets.

**Property Value**  
---  
**Type** | **Description**  
`[ServerMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.ServerMetadata)` |   
  
### TraceContext
    
    
    public string TraceContext { get; set; }

Immutable. Header string for tracing across services. It should be set when the packet is first arrived in the stream server.

The input format is a lowercase hex string:

  * version_id: 1 byte, currently must be zero - hex encoded (2 characters)
  * trace_id: 16 bytes (opaque blob) - hex encoded (32 characters)
  * span_id: 8 bytes (opaque blob) - hex encoded (16 characters)
  * trace_options: 1 byte (LSB means tracing enabled) - hex encoded (2 characters) Example: "00-404142434445464748494a4b4c4d4e4f-6162636465666768-01" v trace_id span_id options



**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Type
    
    
    public PacketType Type { get; set; }

Input only. Immutable. The type of the payload.

**Property Value**  
---  
**Type** | **Description**  
`[PacketType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.VisionAI.V1/latest/Google.Cloud.VisionAI.V1.PacketType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-11 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-11 UTC."],[],[]] 
