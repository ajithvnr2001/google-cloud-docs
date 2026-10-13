---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet
title: Google Bigtable v2 API - Class PartialResultSet (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:42:56.848125+00:00
---

# Google Bigtable v2 API - Class PartialResultSet (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class PartialResultSet (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class PartialResultSet : IMessage<PartialResultSet>, IEquatable<PartialResultSet>, IDeepCloneable<PartialResultSet>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class PartialResultSet.

A partial result set from the streaming query API. Cloud Bigtable clients buffer partial results received in this message until a `resume_token` is received.

The pseudocode below describes how to buffer and parse a stream of `PartialResultSet` messages.

Having:

  * queue of row results waiting to be returned `queue`
  * extensible buffer of bytes `buffer`
  * a place to keep track of the most recent `resume_token` for each PartialResultSet `p` received { if p.reset { ensure `queue` is empty ensure `buffer` is empty } if p.estimated_batch_size != 0 { (optional) ensure `buffer` is sized to at least `p.estimated_batch_size` } if `p.proto_rows_batch` is set { append `p.proto_rows_batch.bytes` to `buffer` } if p.batch_checksum is set and `buffer` is not empty { validate the checksum matches the contents of `buffer` (see comments on `batch_checksum`) parse `buffer` as `ProtoRows` message, clearing `buffer` add parsed rows to end of `queue` } if p.resume_token is set { release results in `queue` save `p.resume_token` in `resume_token` } }



## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > PartialResultSet

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[PartialResultSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[PartialResultSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[PartialResultSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### PartialResultSet()
    
    
    public PartialResultSet()

### PartialResultSet(PartialResultSet)
    
    
    public PartialResultSet(PartialResultSet other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[PartialResultSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet)`  
  
  
## Properties 

### BatchChecksum
    
    
    public uint BatchChecksum { get; set; }

CRC32C checksum of concatenated `partial_rows` data for the current batch.

When present, the buffered data from `partial_rows` forms a complete parseable message of the appropriate type.

The client should mark the end of a parseable message and prepare to receive a new one starting from the next `PartialResultSet` message. Clients must verify the checksum of the serialized batch before yielding it to the caller.

This does NOT mean the values can be yielded to the callers since a `resume_token` is required to safely do so.

If `resume_token` is non-empty and any data has been received since the last one, this field is guaranteed to be non-empty. In other words, clients may assume that a batch will never cross a `resume_token` boundary.

**Property Value**  
---  
**Type** | **Description**  
`[uint](https://learn.microsoft.com/dotnet/api/system.uint32)` |   
  
### EstimatedBatchSize
    
    
    public int EstimatedBatchSize { get; set; }

Estimated size of the buffer required to hold the next batch of results.

This value will be sent with the first `partial_rows` of a batch. That is, on the first `partial_rows` received in a stream, on the first message after a `batch_checksum` message, and any time `reset` is true.

The client can use this estimate to allocate a buffer for the next batch of results. This helps minimize the number of allocations required, though the buffer size may still need to be increased if the estimate is too low.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### HasBatchChecksum
    
    
    public bool HasBatchChecksum { get; }

Gets whether the "batch_checksum" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### PartialRowsCase
    
    
    public PartialResultSet.PartialRowsOneofCase PartialRowsCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[PartialResultSet](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet)[PartialRowsOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.PartialResultSet.PartialRowsOneofCase)` |   
  
### ProtoRowsBatch
    
    
    public ProtoRowsBatch ProtoRowsBatch { get; set; }

Partial rows in serialized ProtoRows format.

**Property Value**  
---  
**Type** | **Description**  
`[ProtoRowsBatch](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ProtoRowsBatch)` |   
  
### Reset
    
    
    public bool Reset { get; set; }

If `true`, any data buffered since the last non-empty `resume_token` must be discarded before the other parts of this message, if any, are handled.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ResumeToken
    
    
    public ByteString ResumeToken { get; set; }

An opaque token sent by the server to allow query resumption and signal that the buffered values constructed from received `partial_rows` can be yielded to the caller. Clients can provide this token in a subsequent request to resume the result stream from the current point.

When `resume_token` is non-empty, the buffered values received from `partial_rows` since the last non-empty `resume_token` can be yielded to the callers, provided that the client keeps the value of `resume_token` and uses it on subsequent retries.

A `resume_token` may be sent without information in `partial_rows` to checkpoint the progress of a sparse query. Any previous `partial_rows` data should still be yielded in this case, and the new `resume_token` should be saved for future retries as normal.

A `resume_token` will only be sent on a boundary where there is either no ongoing result batch, or `batch_checksum` is also populated.

The server will also send a sentinel `resume_token` when last batch of `partial_rows` is sent. If the client retries the ExecuteQueryRequest with the sentinel `resume_token`, the server will emit it again without any data in `partial_rows`, then return OK.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
