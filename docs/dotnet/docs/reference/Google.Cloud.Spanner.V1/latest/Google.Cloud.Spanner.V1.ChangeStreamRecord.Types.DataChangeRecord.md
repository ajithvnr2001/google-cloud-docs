---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord
title: Google Cloud Spanner v1 API - Class ChangeStreamRecord.Types.DataChangeRecord (5.13.0-beta11) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:11:14.690912+00:00
---

# Google Cloud Spanner v1 API - Class ChangeStreamRecord.Types.DataChangeRecord (5.13.0-beta11)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Google Cloud Spanner v1 API - Class ChangeStreamRecord.Types.DataChangeRecord (5.13.0-beta11) Stay organized with collections  Save and categorize content based on your preferences. 

5.13.0-beta11  5.13.0-beta10  5.12.0 (latest)  5.11.0  5.10.0  5.9.0  5.8.0  5.7.0  5.6.0  5.5.0  5.4.0  5.3.0  5.2.0  5.1.0  5.0.0  4.6.0  4.5.0  4.4.0  4.3.0  4.2.0  4.1.0  4.0.0  3.15.1  3.14.0  3.13.0  3.12.0  3.11.0  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0 
    
    
    public sealed class ChangeStreamRecord.Types.DataChangeRecord : IMessage<ChangeStreamRecord.Types.DataChangeRecord>, IEquatable<ChangeStreamRecord.Types.DataChangeRecord>, IDeepCloneable<ChangeStreamRecord.Types.DataChangeRecord>, IBufferMessage, IMessage

Reference documentation and code samples for the Google Cloud Spanner v1 API class ChangeStreamRecord.Types.DataChangeRecord.

A data change record contains a set of changes to a table with the same modification type (insert, update, or delete) committed at the same commit timestamp in one change stream partition for the same transaction. Multiple data change records can be returned for the same transaction across multiple change stream partitions.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > ChangeStreamRecord.Types.DataChangeRecord

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.Spanner.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1)

## Assembly

Google.Cloud.Spanner.V1.dll

## Constructors 

### DataChangeRecord()
    
    
    public DataChangeRecord()

### DataChangeRecord(DataChangeRecord)
    
    
    public DataChangeRecord(ChangeStreamRecord.Types.DataChangeRecord other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord)`  
  
  
## Properties 

### ColumnMetadata
    
    
    public RepeatedField<ChangeStreamRecord.Types.DataChangeRecord.Types.ColumnMetadata> ColumnMetadata { get; }

Provides metadata describing the columns associated with the [mods][google.spanner.v1.ChangeStreamRecord.DataChangeRecord.mods] listed below.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types)[ColumnMetadata](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types.ColumnMetadata)` |   
  
### CommitTimestamp
    
    
    public Timestamp CommitTimestamp { get; set; }

Indicates the timestamp in which the change was committed. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.

**Property Value**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.WellKnownTypes.Timestamp.html)` |   
  
### IsLastRecordInTransactionInPartition
    
    
    public bool IsLastRecordInTransactionInPartition { get; set; }

Indicates whether this is the last record for a transaction in the current partition. Clients can use this field to determine when all records for a transaction in the current partition have been received.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### IsSystemTransaction
    
    
    public bool IsSystemTransaction { get; set; }

Indicates whether the transaction is a system transaction. System transactions include those issued by time-to-live (TTL), column backfill, etc.

**Property Value**  
---  
**Type** | **Description**  
`[bool](https://learn.microsoft.com/dotnet/api/system.boolean)` |   
  
### ModType
    
    
    public ChangeStreamRecord.Types.DataChangeRecord.Types.ModType ModType { get; set; }

Describes the type of change.

**Property Value**  
---  
**Type** | **Description**  
`[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types)[ModType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types.ModType)` |   
  
### Mods
    
    
    public RepeatedField<ChangeStreamRecord.Types.DataChangeRecord.Types.Mod> Mods { get; }

Describes the changes that were made.

**Property Value**  
---  
**Type** | **Description**  
`[RepeatedField](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.Collections.RepeatedField-1.html)[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types)[Mod](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types.Mod)` |   
  
### NumberOfPartitionsInTransaction
    
    
    public int NumberOfPartitionsInTransaction { get; set; }

Indicates the number of partitions that return data change records for this transaction. This value can be helpful in assembling all records associated with a particular transaction.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### NumberOfRecordsInTransaction
    
    
    public int NumberOfRecordsInTransaction { get; set; }

Indicates the number of data change records that are part of this transaction across all change stream partitions. This value can be used to assemble all the records associated with a particular transaction.

**Property Value**  
---  
**Type** | **Description**  
`[int](https://learn.microsoft.com/dotnet/api/system.int32)` |   
  
### RecordSequence
    
    
    public string RecordSequence { get; set; }

Record sequence numbers are unique and monotonically increasing (but not necessarily contiguous) for a specific timestamp across record types in the same partition. To guarantee ordered processing, the reader should process records (of potentially different types) in record_sequence order for a specific timestamp in the same partition.

The record sequence number ordering across partitions is only meaningful in the context of a specific transaction. Record sequence numbers are unique across partitions for a specific transaction. Sort the DataChangeRecords for the same [server_transaction_id][google.spanner.v1.ChangeStreamRecord.DataChangeRecord.server_transaction_id] by [record_sequence][google.spanner.v1.ChangeStreamRecord.DataChangeRecord.record_sequence] to reconstruct the ordering of the changes within the transaction.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ServerTransactionId
    
    
    public string ServerTransactionId { get; set; }

Provides a globally unique string that represents the transaction in which the change was committed. Multiple transactions can have the same commit timestamp, but each transaction has a unique server_transaction_id.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### Table
    
    
    public string Table { get; set; }

Name of the table affected by the change.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### TransactionTag
    
    
    public string TransactionTag { get; set; }

Indicates the transaction tag associated with this transaction.

**Property Value**  
---  
**Type** | **Description**  
`[string](https://learn.microsoft.com/dotnet/api/system.string)` |   
  
### ValueCaptureType
    
    
    public ChangeStreamRecord.Types.DataChangeRecord.Types.ValueCaptureType ValueCaptureType { get; set; }

Describes the value capture type that was specified in the change stream configuration when this change was captured.

**Property Value**  
---  
**Type** | **Description**  
`[ChangeStreamRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types)[DataChangeRecord](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord)[Types](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types)[ValueCaptureType](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.Spanner.V1/latest/Google.Cloud.Spanner.V1.ChangeStreamRecord.Types.DataChangeRecord.Types.ValueCaptureType)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
