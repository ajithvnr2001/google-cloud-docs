---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponseOrBuilder
title: Interface BatchCommitWriteStreamsResponseOrBuilder (3.35.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:00:00.223545+00:00
---

# Interface BatchCommitWriteStreamsResponseOrBuilder (3.35.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.BatchCommitWriteStreamsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface BatchCommitWriteStreamsResponseOrBuilder (3.35.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.35.0 (latest)  3.31.0  3.30.0  3.29.0  3.27.0  3.24.0  3.23.0  3.21.0  3.20.0  3.19.1  3.18.0  3.17.3  3.16.3  3.15.3  3.14.1  3.12.0  3.11.4  3.10.3  3.9.3  3.8.0  3.6.1  3.5.2  3.4.0  3.3.1  3.2.0  3.1.0  3.0.1  2.47.0  2.45.0  2.44.1  2.43.0 
    
    
    public interface BatchCommitWriteStreamsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getCommitTime()
    
    
    public abstract Timestamp getCommitTime()

The time at which streams were committed in microseconds granularity. This field will only exist when there are no stream errors. **Note** if this field is not set, it means the commit was not successful.

`.google.protobuf.Timestamp commit_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The commitTime.  
  
### getCommitTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCommitTimeOrBuilder()

The time at which streams were committed in microseconds granularity. This field will only exist when there are no stream errors. **Note** if this field is not set, it means the commit was not successful.

`.google.protobuf.Timestamp commit_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getStreamErrors(int index)
    
    
    public abstract StorageError getStreamErrors(int index)

Stream level error if commit failed. Only streams with error will be in the list. If empty, there is no error and all streams are committed successfully. If non empty, certain streams have errors and ZERO stream is committed due to atomicity guarantee.

`repeated .google.cloud.bigquery.storage.v1.StorageError stream_errors = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageError)` |   
  
### getStreamErrorsCount()
    
    
    public abstract int getStreamErrorsCount()

Stream level error if commit failed. Only streams with error will be in the list. If empty, there is no error and all streams are committed successfully. If non empty, certain streams have errors and ZERO stream is committed due to atomicity guarantee.

`repeated .google.cloud.bigquery.storage.v1.StorageError stream_errors = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getStreamErrorsList()
    
    
    public abstract List<StorageError> getStreamErrorsList()

Stream level error if commit failed. Only streams with error will be in the list. If empty, there is no error and all streams are committed successfully. If non empty, certain streams have errors and ZERO stream is committed due to atomicity guarantee.

`repeated .google.cloud.bigquery.storage.v1.StorageError stream_errors = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[StorageError](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageError)>` |   
  
### getStreamErrorsOrBuilder(int index)
    
    
    public abstract StorageErrorOrBuilder getStreamErrorsOrBuilder(int index)

Stream level error if commit failed. Only streams with error will be in the list. If empty, there is no error and all streams are committed successfully. If non empty, certain streams have errors and ZERO stream is committed due to atomicity guarantee.

`repeated .google.cloud.bigquery.storage.v1.StorageError stream_errors = 2;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[StorageErrorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigquerystorage/latest/com.google.cloud.bigquery.storage.v1.StorageErrorOrBuilder)` |   
  
### getStreamErrorsOrBuilderList()
    
    
    public abstract List<? extends StorageErrorOrBuilder> getStreamErrorsOrBuilderList()

Stream level error if commit failed. Only streams with error will be in the list. If empty, there is no error and all streams are committed successfully. If non empty, certain streams have errors and ZERO stream is committed due to atomicity guarantee.

`repeated .google.cloud.bigquery.storage.v1.StorageError stream_errors = 2;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.cloud.bigquery.storage.v1.StorageErrorOrBuilder>` |   
  
### hasCommitTime()
    
    
    public abstract boolean hasCommitTime()

The time at which streams were committed in microseconds granularity. This field will only exist when there are no stream errors. **Note** if this field is not set, it means the commit was not successful.

`.google.protobuf.Timestamp commit_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the commitTime field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
