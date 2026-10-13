---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk
title: Google Bigtable v2 API - Class ReadRowsResponse.Types.CellChunk (3.33.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:43:03.488871+00:00
---

# Google Bigtable v2 API - Class ReadRowsResponse.Types.CellChunk (3.33.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Bigtable v2 API - Class ReadRowsResponse.Types.CellChunk (3.33.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.33.0 (latest)  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.0  3.26.0  3.25.0  3.24.0  3.23.0  3.22.0  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.0  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0 
    
    
    public sealed class ReadRowsResponse.Types.CellChunk : IMessage<ReadRowsResponse.Types.CellChunk>, IEquatable<ReadRowsResponse.Types.CellChunk>, IDeepCloneable<ReadRowsResponse.Types.CellChunk>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Bigtable v2 API class ReadRowsResponse.Types.CellChunk.

Specifies a piece of a row's contents returned as part of the read response stream.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ReadRowsResponse.Types.CellChunk

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types)[CellChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types)[CellChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types)[CellChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Bigtable.V2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2)

## Assembly

Google.Cloud.Bigtable.V2.dll

## Constructors 

### CellChunk()
    
    
    public CellChunk()

### CellChunk(CellChunk)
    
    
    public CellChunk(ReadRowsResponse.Types.CellChunk other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types)[CellChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk)`  
  
  
## Properties 

### CommitRow
    
    
    public bool CommitRow { get; set; }

Indicates that the client can safely process all previous chunks for `row_key`, as its data has been fully read.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### FamilyName
    
    
    public string FamilyName { get; set; }

The column family name for this chunk of data. If this message is not present this CellChunk is a continuation of the same column family as the previous CellChunk. The empty string can occur as a column family name in a response so clients must check explicitly for the presence of this message, not just for `family_name.value` being non-empty.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### HasCommitRow
    
    
    public bool HasCommitRow { get; }

Gets whether the "commit_row" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### HasResetRow
    
    
    public bool HasResetRow { get; }

Gets whether the "reset_row" field is set

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### Labels
    
    
    public RepeatedField<string> Labels { get; }

Labels applied to the cell by a [RowFilter][google.bigtable.v2.RowFilter]. Labels are only set on the first CellChunk per cell.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Qualifier
    
    
    public ByteString Qualifier { get; set; }

The column qualifier for this chunk of data. If this message is not present, this CellChunk is a continuation of the same column as the previous CellChunk. Column qualifiers may be empty so clients must check for the presence of this message, not just for `qualifier.value` being non-empty.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### ResetRow
    
    
    public bool ResetRow { get; set; }

Indicates that the client should drop all previous chunks for `row_key`, as it will be re-read from the beginning.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### RowKey
    
    
    public ByteString RowKey { get; set; }

The row key for this chunk of data. If the row key is empty, this CellChunk is a continuation of the same row as the previous CellChunk in the response stream, even if that CellChunk was in a previous ReadRowsResponse message.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### RowStatusCase
    
    
    public ReadRowsResponse.Types.CellChunk.RowStatusOneofCase RowStatusCase { get; }

**Property Value**  
---  
**Type** | **Description**  
`[ReadRowsResponse](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types)[CellChunk](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk)[RowStatusOneofCase](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Bigtable.V2/latest/Google.Cloud.Bigtable.V2.ReadRowsResponse.Types.CellChunk.RowStatusOneofCase)` |   
  
### TimestampMicros
    
    
    public long TimestampMicros { get; set; }

The cell's stored timestamp, which also uniquely identifies it within its column. Values are always expressed in microseconds, but individual tables may set a coarser granularity to further restrict the allowed values. For example, a table which specifies millisecond granularity will only allow values of `timestamp_micros` which are multiples of

  1. Timestamps are only set in the first CellChunk per cell (for cells split into multiple chunks).



**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### Value
    
    
    public ByteString Value { get; set; }

The value stored in the cell. Cell values can be split across multiple CellChunks. In that case only the value field will be set in CellChunks after the first: the timestamp and labels will only be present in the first CellChunk, even if the first CellChunk came in a previous ReadRowsResponse.

**Property Value**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.ByteString.html)` |   
  
### ValueSize
    
    
    public int ValueSize { get; set; }

If this CellChunk is part of a chunked cell value and this is not the final chunk of that cell, value_size will be set to the total length of the cell value. The client can use this size to pre-allocate memory to hold the full cell value.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
