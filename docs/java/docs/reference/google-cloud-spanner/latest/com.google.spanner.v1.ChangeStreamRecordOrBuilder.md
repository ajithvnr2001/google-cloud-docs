---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecordOrBuilder
title: Interface ChangeStreamRecordOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:33:51.070857+00:00
---

# Interface ChangeStreamRecordOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecordOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ChangeStreamRecordOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface ChangeStreamRecordOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getDataChangeRecord()
    
    
    public abstract ChangeStreamRecord.DataChangeRecord getDataChangeRecord()

Data change record describing a data change for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.DataChangeRecord data_change_record = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.DataChangeRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.DataChangeRecord)` | The dataChangeRecord.  
  
### getDataChangeRecordOrBuilder()
    
    
    public abstract ChangeStreamRecord.DataChangeRecordOrBuilder getDataChangeRecordOrBuilder()

Data change record describing a data change for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.DataChangeRecord data_change_record = 1;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.DataChangeRecordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.DataChangeRecordOrBuilder)` |   
  
### getHeartbeatRecord()
    
    
    public abstract ChangeStreamRecord.HeartbeatRecord getHeartbeatRecord()

Heartbeat record describing a heartbeat for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.HeartbeatRecord heartbeat_record = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.HeartbeatRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.HeartbeatRecord)` | The heartbeatRecord.  
  
### getHeartbeatRecordOrBuilder()
    
    
    public abstract ChangeStreamRecord.HeartbeatRecordOrBuilder getHeartbeatRecordOrBuilder()

Heartbeat record describing a heartbeat for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.HeartbeatRecord heartbeat_record = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.HeartbeatRecordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.HeartbeatRecordOrBuilder)` |   
  
### getPartitionEndRecord()
    
    
    public abstract ChangeStreamRecord.PartitionEndRecord getPartitionEndRecord()

Partition end record describing a terminated change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionEndRecord partition_end_record = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEndRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEndRecord)` | The partitionEndRecord.  
  
### getPartitionEndRecordOrBuilder()
    
    
    public abstract ChangeStreamRecord.PartitionEndRecordOrBuilder getPartitionEndRecordOrBuilder()

Partition end record describing a terminated change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionEndRecord partition_end_record = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEndRecordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEndRecordOrBuilder)` |   
  
### getPartitionEventRecord()
    
    
    public abstract ChangeStreamRecord.PartitionEventRecord getPartitionEventRecord()

Partition event record describing key range changes for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord partition_event_record = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord)` | The partitionEventRecord.  
  
### getPartitionEventRecordOrBuilder()
    
    
    public abstract ChangeStreamRecord.PartitionEventRecordOrBuilder getPartitionEventRecordOrBuilder()

Partition event record describing key range changes for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord partition_event_record = 5; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionEventRecordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionEventRecordOrBuilder)` |   
  
### getPartitionStartRecord()
    
    
    public abstract ChangeStreamRecord.PartitionStartRecord getPartitionStartRecord()

Partition start record describing a new change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionStartRecord partition_start_record = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionStartRecord](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionStartRecord)` | The partitionStartRecord.  
  
### getPartitionStartRecordOrBuilder()
    
    
    public abstract ChangeStreamRecord.PartitionStartRecordOrBuilder getPartitionStartRecordOrBuilder()

Partition start record describing a new change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionStartRecord partition_start_record = 3; `

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.PartitionStartRecordOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.PartitionStartRecordOrBuilder)` |   
  
### getRecordCase()
    
    
    public abstract ChangeStreamRecord.RecordCase getRecordCase()

**Returns**  
---  
**Type** | **Description**  
`[ChangeStreamRecord.RecordCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.ChangeStreamRecord.RecordCase)` |   
  
### hasDataChangeRecord()
    
    
    public abstract boolean hasDataChangeRecord()

Data change record describing a data change for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.DataChangeRecord data_change_record = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the dataChangeRecord field is set.  
  
### hasHeartbeatRecord()
    
    
    public abstract boolean hasHeartbeatRecord()

Heartbeat record describing a heartbeat for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.HeartbeatRecord heartbeat_record = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the heartbeatRecord field is set.  
  
### hasPartitionEndRecord()
    
    
    public abstract boolean hasPartitionEndRecord()

Partition end record describing a terminated change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionEndRecord partition_end_record = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partitionEndRecord field is set.  
  
### hasPartitionEventRecord()
    
    
    public abstract boolean hasPartitionEventRecord()

Partition event record describing key range changes for a change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionEventRecord partition_event_record = 5; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partitionEventRecord field is set.  
  
### hasPartitionStartRecord()
    
    
    public abstract boolean hasPartitionStartRecord()

Partition start record describing a new change stream partition.

`.google.spanner.v1.ChangeStreamRecord.PartitionStartRecord partition_start_record = 3; `

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partitionStartRecord field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
