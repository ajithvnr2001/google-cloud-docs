---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.CloseStream
title: Google Bigtable v2 API - Class ReadChangeStreamResponse.Types.CloseStream (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:00.533616+00:00
---

# Google Bigtable v2 API - Class ReadChangeStreamResponse.Types.CloseStream (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.CloseStream

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class ReadChangeStreamResponse.Types.CloseStream (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ReadChangeStreamResponse.Types.CloseStream : IMessage<ReadChangeStreamResponse.Types.CloseStream>, IEquatable<ReadChangeStreamResponse.Types.CloseStream>, IDeepCloneable<ReadChangeStreamResponse.Types.CloseStream>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class ReadChangeStreamResponse.Types.CloseStream.

A message indicating that the client should stop reading from the stream. If status is OK and `continuation_tokens` & `new_partitions` are empty, the stream has finished (for example if there was an `end_time` specified). If `continuation_tokens` & `new_partitions` are present, then a change in partitioning requires the client to open a new stream for each token to resume reading. Example:
    
    
                                     [B,      D) ends
                                          |
                                          v
                  new_partitions:  [A,  C) [C,  E)
    continuation_tokens.partitions:  [B,C) [C,D)
                                     ^---^ ^---^
                                     ^     ^
                                     |     |
                                     |     StreamContinuationToken 2
                                     |
                                     StreamContinuationToken 1
    

To read the new partition [A,C), supply the continuation tokens whose ranges cover the new partition, for example ContinuationToken[A,B) & ContinuationToken[B,C).

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReadChangeStreamResponse.Types.CloseStream

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[CloseStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.CloseStream), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[CloseStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.CloseStream), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[CloseStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.CloseStream), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### CloseStream()
    
    
    public CloseStream()

### CloseStream(CloseStream)
    
    
    public CloseStream(ReadChangeStreamResponse.Types.CloseStream other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReadChangeStreamResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types)[CloseStream](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadChangeStreamResponse.Types.CloseStream)`  
  
  
## Properties 

### ContinuationTokens
    
    
    public RepeatedField<StreamContinuationToken> ContinuationTokens { get; }

If non-empty, contains the information needed to resume reading their associated partitions.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[StreamContinuationToken](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.StreamContinuationToken)` |   
  
### NewPartitions
    
    
    public RepeatedField<StreamPartition> NewPartitions { get; }

If non-empty, contains the new partitions to start reading from, which are related to but not necessarily identical to the partitions for the above `continuation_tokens`.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[StreamPartition](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.StreamPartition)` |   
  
### Status
    
    
    public Status Status { get; set; }

The status of the stream.

**Property Value**  
---  
**Type** | **Description**  
`[Status](https://cloud.google.com/dotnet/docs/reference/Google.Api.CommonProtos/latest/Google.Rpc.Status.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
