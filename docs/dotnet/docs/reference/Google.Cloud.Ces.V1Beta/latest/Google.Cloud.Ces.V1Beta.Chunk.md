---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk
title: Gemini Enterprise for Customer Experience v1beta API - Class Chunk (1.0.0-beta09) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:40:00.257535+00:00
---

# Gemini Enterprise for Customer Experience v1beta API - Class Chunk (1.0.0-beta09)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Gemini Enterprise for Customer Experience v1beta API - Class Chunk (1.0.0-beta09) Stay organized with collections  Save and categorize content based on your preferences. 

1.0.0-beta09 (latest)  1.0.0-beta08 
    
    
    public sealed class Chunk : IMessage<Chunk>, IEquatable<Chunk>, IDeepCloneable<Chunk>, IBufferMessage, IMessage

Reference documentation and code samples for the Gemini Enterprise for Customer Experience v1beta API class Chunk.

A chunk of content within a message.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > Chunk

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Ces.V1Beta](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta)

## Assembly

Google.Cloud.Ces.V1Beta.dll

## Constructors 

### Chunk()
    
    
    public Chunk()

### Chunk(Chunk)
    
    
    public Chunk(Chunk other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk)`  
  
  
## Properties 

### AgentTransfer
    
    
    public AgentTransfer AgentTransfer { get; set; }

Optional. Agent transfer event.

**Property Value**  
---  
**Type** | **Description**  
`[AgentTransfer](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.AgentTransfer)` |   
  
### Blob
    
    
    public Blob Blob { get; set; }

Optional. Blob data.

**Property Value**  
---  
**Type** | **Description**  
`[Blob](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Blob)` |   
  
### DataCase
    
    
    public Chunk.DataOneofCase DataCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[Chunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk)[DataOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Chunk.DataOneofCase)` |   
  
### DefaultVariables
    
    
    public Struct DefaultVariables { get; set; }

A struct represents default variables at the start of the conversation, keyed by variable names.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### HasText
    
    
    public bool HasText { get; }

Gets whether the "text" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasTranscript
    
    
    public bool HasTranscript { get; }

Gets whether the "transcript" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Image
    
    
    public Image Image { get; set; }

Optional. Image data.

**Property Value**  
---  
**Type** | **Description**  
`[Image](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.Image)` |   
  
### Payload
    
    
    public Struct Payload { get; set; }

Optional. Custom payload data.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
### Text
    
    
    public string Text { get; set; }

Optional. Text data.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ToolCall
    
    
    public ToolCall ToolCall { get; set; }

Optional. Tool execution request.

**Property Value**  
---  
**Type** | **Description**  
`[ToolCall](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolCall)` |   
  
### ToolResponse
    
    
    public ToolResponse ToolResponse { get; set; }

Optional. Tool execution response.

**Property Value**  
---  
**Type** | **Description**  
`[ToolResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Ces.V1Beta/latest/Google.Cloud.Ces.V1Beta.ToolResponse)` |   
  
### Transcript
    
    
    public string Transcript { get; set; }

Optional. Transcript associated with the audio.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### UpdatedVariables
    
    
    public Struct UpdatedVariables { get; set; }

A struct represents variables that were updated in the conversation, keyed by variable names.

**Property Value**  
---  
**Type** | **Description**  
`[Struct](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Struct.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-14 UTC."],[],[]] 
