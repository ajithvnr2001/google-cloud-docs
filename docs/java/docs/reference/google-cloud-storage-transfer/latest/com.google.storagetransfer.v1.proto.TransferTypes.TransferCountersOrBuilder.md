---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferCountersOrBuilder
title: Interface TransferTypes.TransferCountersOrBuilder (1.99.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:18.430897+00:00
---

# Interface TransferTypes.TransferCountersOrBuilder (1.99.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-storage-transfer/latest/com.google.storagetransfer.v1.proto.TransferTypes.TransferCountersOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransferTypes.TransferCountersOrBuilder (1.99.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.99.0 (latest)  1.95.0  1.94.0  1.93.0  1.91.0  1.88.0  1.87.0  1.85.0  1.83.0  1.82.0  1.80.0  1.78.0  1.76.0  1.75.0  1.74.0  1.73.0  1.72.0  1.70.0  1.68.0  1.67.0  1.64.0  1.63.0  1.62.0  1.60.0  1.59.0  1.58.0  1.57.0  1.56.0  1.55.0  1.54.0  1.53.0  1.52.0  1.51.0  1.49.0  1.48.0  1.47.0  1.46.0  1.45.0  1.44.0  1.43.0  1.42.0  1.41.0  1.40.0  1.39.0  1.37.0  1.36.0  1.35.0  1.34.0  1.33.0  1.32.0  1.31.0  1.30.0  1.29.0  1.28.0  1.27.0  1.24.0  1.23.0  1.22.0  1.21.0  1.20.0  1.19.0  1.18.0  1.17.0  1.16.0  1.15.0  1.14.0  1.13.0  1.12.0  1.11.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.0  1.0.4 
    
    
    public static interface TransferTypes.TransferCountersOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBytesCopiedToSink()
    
    
    public abstract long getBytesCopiedToSink()

Bytes that are copied to the data sink.

`int64 bytes_copied_to_sink = 8;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesCopiedToSink.  
  
### getBytesDeletedFromSink()
    
    
    public abstract long getBytesDeletedFromSink()

Bytes that are deleted from the data sink.

`int64 bytes_deleted_from_sink = 12;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesDeletedFromSink.  
  
### getBytesDeletedFromSource()
    
    
    public abstract long getBytesDeletedFromSource()

Bytes that are deleted from the data source.

`int64 bytes_deleted_from_source = 10;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesDeletedFromSource.  
  
### getBytesFailedToDeleteFromSink()
    
    
    public abstract long getBytesFailedToDeleteFromSink()

Bytes that failed to be deleted from the data sink.

`int64 bytes_failed_to_delete_from_sink = 16;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesFailedToDeleteFromSink.  
  
### getBytesFoundFromSource()
    
    
    public abstract long getBytesFoundFromSource()

Bytes found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync.

`int64 bytes_found_from_source = 2;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesFoundFromSource.  
  
### getBytesFoundOnlyFromSink()
    
    
    public abstract long getBytesFoundOnlyFromSink()

Bytes found only in the data sink that are scheduled to be deleted.

`int64 bytes_found_only_from_sink = 4;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesFoundOnlyFromSink.  
  
### getBytesFromSourceFailed()
    
    
    public abstract long getBytesFromSourceFailed()

Bytes in the data source that failed to be transferred or that failed to be deleted after being transferred.

`int64 bytes_from_source_failed = 14;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesFromSourceFailed.  
  
### getBytesFromSourceSkippedBySync()
    
    
    public abstract long getBytesFromSourceSkippedBySync()

Bytes in the data source that are not transferred because they already exist in the data sink.

`int64 bytes_from_source_skipped_by_sync = 6;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The bytesFromSourceSkippedBySync.  
  
### getDirectoriesFailedToListFromSource()
    
    
    public abstract long getDirectoriesFailedToListFromSource()

For transfers involving PosixFilesystem only.

Number of listing failures for each directory found at the source. Potential failures when listing a directory include permission failure or block failure. If listing a directory fails, no files in the directory are transferred.

`int64 directories_failed_to_list_from_source = 18;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The directoriesFailedToListFromSource.  
  
### getDirectoriesFoundFromSource()
    
    
    public abstract long getDirectoriesFoundFromSource()

For transfers involving PosixFilesystem only.

Number of directories found while listing. For example, if the root directory of the transfer is `base/` and there are two other directories, `a/` and `b/` under this directory, the count after listing `base/`, `base/a/` and `base/b/` is 3.

`int64 directories_found_from_source = 17;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The directoriesFoundFromSource.  
  
### getDirectoriesSuccessfullyListedFromSource()
    
    
    public abstract long getDirectoriesSuccessfullyListedFromSource()

For transfers involving PosixFilesystem only.

Number of successful listings for each directory found at the source.

`int64 directories_successfully_listed_from_source = 19;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The directoriesSuccessfullyListedFromSource.  
  
### getIntermediateObjectsCleanedUp()
    
    
    public abstract long getIntermediateObjectsCleanedUp()

Number of successfully cleaned up intermediate objects.

`int64 intermediate_objects_cleaned_up = 22;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The intermediateObjectsCleanedUp.  
  
### getIntermediateObjectsFailedCleanedUp()
    
    
    public abstract long getIntermediateObjectsFailedCleanedUp()

Number of intermediate objects failed cleaned up.

`int64 intermediate_objects_failed_cleaned_up = 23;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The intermediateObjectsFailedCleanedUp.  
  
### getObjectsCopiedToSink()
    
    
    public abstract long getObjectsCopiedToSink()

Objects that are copied to the data sink.

`int64 objects_copied_to_sink = 7;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsCopiedToSink.  
  
### getObjectsDeletedFromSink()
    
    
    public abstract long getObjectsDeletedFromSink()

Objects that are deleted from the data sink.

`int64 objects_deleted_from_sink = 11;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsDeletedFromSink.  
  
### getObjectsDeletedFromSource()
    
    
    public abstract long getObjectsDeletedFromSource()

Objects that are deleted from the data source.

`int64 objects_deleted_from_source = 9;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsDeletedFromSource.  
  
### getObjectsFailedToDeleteFromSink()
    
    
    public abstract long getObjectsFailedToDeleteFromSink()

Objects that failed to be deleted from the data sink.

`int64 objects_failed_to_delete_from_sink = 15;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsFailedToDeleteFromSink.  
  
### getObjectsFoundFromSource()
    
    
    public abstract long getObjectsFoundFromSource()

Objects found in the data source that are scheduled to be transferred, excluding any that are filtered based on object conditions or skipped due to sync.

`int64 objects_found_from_source = 1;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsFoundFromSource.  
  
### getObjectsFoundOnlyFromSink()
    
    
    public abstract long getObjectsFoundOnlyFromSink()

Objects found only in the data sink that are scheduled to be deleted.

`int64 objects_found_only_from_sink = 3;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsFoundOnlyFromSink.  
  
### getObjectsFromSourceFailed()
    
    
    public abstract long getObjectsFromSourceFailed()

Objects in the data source that failed to be transferred or that failed to be deleted after being transferred.

`int64 objects_from_source_failed = 13;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsFromSourceFailed.  
  
### getObjectsFromSourceSkippedBySync()
    
    
    public abstract long getObjectsFromSourceSkippedBySync()

Objects in the data source that are not transferred because they already exist in the data sink.

`int64 objects_from_source_skipped_by_sync = 5;`

**Returns**  
---  
**Type** | **Description**  
`[long](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The objectsFromSourceSkippedBySync.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
