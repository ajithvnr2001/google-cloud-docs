---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo
title: Google Bigtable v2 API - Class ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:01.347625+00:00
---

# Google Bigtable v2 API - Class ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo : IMessage<ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo>, IEquatable<ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo>, IDeepCloneable<ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo.

Information about the chunking of this mutation. Only `SetCell` mutations can be chunked, and all chunks for a `SetCell` will be delivered contiguously with no other mutation types interleaved.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[MutationChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types)[ChunkInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[MutationChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types)[ChunkInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[MutationChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types)[ChunkInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### ChunkInfo()
    
    
    public ChunkInfo()

### ChunkInfo(ChunkInfo)
    
    
    public ChunkInfo(ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[MutationChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types)[ChunkInfo](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.MutationChunk.Types.ChunkInfo)`  
  
  
## Properties 

### ChunkedValueOffset
    
    
    public int ChunkedValueOffset { get; set; }

The byte offset of this chunk into the total value size of the mutation.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### ChunkedValueSize
    
    
    public int ChunkedValueSize { get; set; }

The total value size of all the chunks that make up the `SetCell`.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### LastChunk
    
    
    public bool LastChunk { get; set; }

When true, this is the last chunk of a chunked `SetCell`.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
