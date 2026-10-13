---
url: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.TransferCounters
title: Storage Transfer v1 API - Class TransferCounters (2.10.0) \u00a0|\u00a0 .NET client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:12:03.450132+00:00
---

# Storage Transfer v1 API - Class TransferCounters (2.10.0)  |  .NET client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.TransferCounters

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ .NET ](https://docs.cloud.google.com/dotnet/docs)
  * [ Client libraries ](https://docs.cloud.google.com/dotnet/docs/reference)



Send feedback 

#  Storage Transfer v1 API - Class TransferCounters (2.10.0) Stay organized with collections  Save and categorize content based on your preferences. 

Version latestkeyboard_arrow_down

  * [ 2.10.0 (latest) ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.9.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.9.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.8.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.8.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.7.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.7.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.6.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.6.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.5.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.5.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.4.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.4.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.3.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.3.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.2.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.1.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 2.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/2.0.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 1.2.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/1.2.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 1.1.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/1.1.0/Google.Cloud.StorageTransfer.V1.TransferCounters)
  * [ 1.0.0 ](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/1.0.0/Google.Cloud.StorageTransfer.V1.TransferCounters)


    
    
    public sealed class TransferCounters : IMessage<TransferCounters>, IEquatable<TransferCounters>, IDeepCloneable<TransferCounters>, IBufferMessage, IMessage

Reference documentation and code samples for the Storage Transfer v1 API class TransferCounters.

A collection of counters that report the progress of a transfer operation.

## Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object) > TransferCounters

## Implements

[IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage-1.html)[TransferCounters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.TransferCounters), [IEquatable](https://learn.microsoft.com/dotnet/api/system.iequatable-1)[TransferCounters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.TransferCounters), [IDeepCloneable](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IDeepCloneable-1.html)[TransferCounters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.TransferCounters), [IBufferMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IBufferMessage.html), [IMessage](https://cloud.google.com/dotnet/docs/reference/Google.Protobuf/latest/Google.Protobuf.IMessage.html)

## Inherited Members

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

## Namespace

[Google.Cloud.StorageTransfer.V1](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1)

## Assembly

Google.Cloud.StorageTransfer.V1.dll

## Constructors 

### TransferCounters()
    
    
    public TransferCounters()

### TransferCounters(TransferCounters)
    
    
    public TransferCounters(TransferCounters other)

**Parameter**  
---  
**Name** | **Description**  
`other` | `[TransferCounters](https://docs.cloud.google.com/dotnet/docs/reference/Google.Cloud.StorageTransfer.V1/latest/Google.Cloud.StorageTransfer.V1.TransferCounters)`  
  
  
## Properties 

### BytesCopiedToSink
    
    
    public long BytesCopiedToSink { get; set; }

Bytes that are copied to the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BytesDeletedFromSink
    
    
    public long BytesDeletedFromSink { get; set; }

Bytes that are deleted from the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BytesDeletedFromSource
    
    
    public long BytesDeletedFromSource { get; set; }

Bytes that are deleted from the data source.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BytesFailedToDeleteFromSink
    
    
    public long BytesFailedToDeleteFromSink { get; set; }

Bytes that failed to be deleted from the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BytesFoundFromSource
    
    
    public long BytesFoundFromSource { get; set; }

Bytes found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BytesFoundOnlyFromSink
    
    
    public long BytesFoundOnlyFromSink { get; set; }

Bytes found only in the data sink that are scheduled to be deleted.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BytesFromSourceFailed
    
    
    public long BytesFromSourceFailed { get; set; }

Bytes in the data source that failed to be transferred or that failed to be deleted after being transferred.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### BytesFromSourceSkippedBySync
    
    
    public long BytesFromSourceSkippedBySync { get; set; }

Bytes in the data source that are not transferred because they already exist in the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### DirectoriesFailedToListFromSource
    
    
    public long DirectoriesFailedToListFromSource { get; set; }

For transfers involving PosixFilesystem only.

Number of listing failures for each directory found at the source. Potential failures when listing a directory include permission failure or block failure. If listing a directory fails, no files in the directory are transferred.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### DirectoriesFoundFromSource
    
    
    public long DirectoriesFoundFromSource { get; set; }

For transfers involving PosixFilesystem only.

Number of directories found while listing. For example, if the root directory of the transfer is `base/` and there are two other directories, `a/` and `b/` under this directory, the count after listing `base/`, `base/a/` and `base/b/` is 3.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### DirectoriesSuccessfullyListedFromSource
    
    
    public long DirectoriesSuccessfullyListedFromSource { get; set; }

For transfers involving PosixFilesystem only.

Number of successful listings for each directory found at the source.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### IntermediateObjectsCleanedUp
    
    
    public long IntermediateObjectsCleanedUp { get; set; }

Number of successfully cleaned up intermediate objects.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### IntermediateObjectsFailedCleanedUp
    
    
    public long IntermediateObjectsFailedCleanedUp { get; set; }

Number of intermediate objects failed cleaned up.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsCopiedToSink
    
    
    public long ObjectsCopiedToSink { get; set; }

Objects that are copied to the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsDeletedFromSink
    
    
    public long ObjectsDeletedFromSink { get; set; }

Objects that are deleted from the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsDeletedFromSource
    
    
    public long ObjectsDeletedFromSource { get; set; }

Objects that are deleted from the data source.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsFailedToDeleteFromSink
    
    
    public long ObjectsFailedToDeleteFromSink { get; set; }

Objects that failed to be deleted from the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsFoundFromSource
    
    
    public long ObjectsFoundFromSource { get; set; }

Objects found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsFoundOnlyFromSink
    
    
    public long ObjectsFoundOnlyFromSink { get; set; }

Objects found only in the data sink that are scheduled to be deleted.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsFromSourceFailed
    
    
    public long ObjectsFromSourceFailed { get; set; }

Objects in the data source that failed to be transferred or that failed to be deleted after being transferred.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
### ObjectsFromSourceSkippedBySync
    
    
    public long ObjectsFromSourceSkippedBySync { get; set; }

Objects in the data source that are not transferred because they already exist in the data sink.

**Property Value**  
---  
**Type** | **Description**  
`[long](https://learn.microsoft.com/dotnet/api/system.int64)` |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-03-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-03-09 UTC."],[],[]] 
