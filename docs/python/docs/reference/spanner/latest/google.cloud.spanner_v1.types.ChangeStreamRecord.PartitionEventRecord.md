---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord
title: Class PartitionEventRecord (3.71.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:21:53.652745+00:00
---

# Class PartitionEventRecord (3.71.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class PartitionEventRecord (3.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 
    
    
    PartitionEventRecord(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A partition event record describes key range changes for a change stream partition. The changes to a row defined by its primary key can be captured in one change stream partition for a specific time range, and then be captured in a different change stream partition for a different time range. This movement of key ranges across change stream partitions is a reflection of activities, such as Spanner's dynamic splitting and load balancing, etc. Processing this event is needed if users want to guarantee processing of the changes for any key in timestamp order. If time ordered processing of changes for a primary key is not needed, this event can be ignored. To guarantee time ordered processing for each primary key, if the event describes move-ins, the reader of this partition needs to wait until the readers of the source partitions have processed all records with timestamps <= this PartitionEventRecord.commit_timestamp, before advancing beyond this PartitionEventRecord. If the event describes move-outs, the reader can notify the readers of the destination partitions that they can continue processing.

## Attributes  
  
---  
**Name** | **Description**  
`commit_timestamp` |  `google.protobuf.timestamp_pb2.Timestamp`   
Indicates the commit timestamp at which the key range change occurred. DataChangeRecord.commit_timestamps, PartitionStartRecord.start_timestamps, PartitionEventRecord.commit_timestamps, and PartitionEndRecord.end_timestamps can have the same value in the same partition.   
`record_sequence` |  `str`   
Record sequence numbers are unique and monotonically increasing (but not necessarily contiguous) for a specific timestamp across record types in the same partition. To guarantee ordered processing, the reader should process records (of potentially different types) in record_sequence order for a specific timestamp in the same partition.   
`partition_token` |  `str`   
Unique partition identifier describing the partition this event occurred on. `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]` is equal to the partition token of the change stream partition currently queried to return this PartitionEventRecord.   
`move_in_events` |  `MutableSequence[[google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord.MoveInEvent](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord.MoveInEvent)]`   
Set when one or more key ranges are moved into the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]`. Example: Two key ranges are moved into partition (P1) from partition (P2) and partition (P3) in a single transaction at timestamp T. The PartitionEventRecord returned in P1 will reflect the move as: PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_in_events { source_partition_token: "P2" } move_in_events { source_partition_token: "P3" } } The PartitionEventRecord returned in P2 will reflect the move as: PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_out_events { destination_partition_token: "P1" } } The PartitionEventRecord returned in P3 will reflect the move as: PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_out_events { destination_partition_token: "P1" } }   
`move_out_events` |  `MutableSequence[[google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent)]`   
Set when one or more key ranges are moved out of the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]`. Example: Two key ranges are moved out of partition (P1) to partition (P2) and partition (P3) in a single transaction at timestamp T. The PartitionEventRecord returned in P1 will reflect the move as: PartitionEventRecord { commit_timestamp: T partition_token: "P1" move_out_events { destination_partition_token: "P2" } move_out_events { destination_partition_token: "P3" } } The PartitionEventRecord returned in P2 will reflect the move as: PartitionEventRecord { commit_timestamp: T partition_token: "P2" move_in_events { source_partition_token: "P1" } } The PartitionEventRecord returned in P3 will reflect the move as: PartitionEventRecord { commit_timestamp: T partition_token: "P3" move_in_events { source_partition_token: "P1" } }   
  
## Classes 

### MoveInEvent
    
    
    MoveInEvent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes move-in of the key ranges into the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]`.

To maintain processing the changes for a particular key in timestamp order, the query processing the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]` should not advance beyond the partition event record commit timestamp until the queries processing the source change stream partitions have processed all change stream records with timestamps <= the partition event record commit timestamp.

### MoveOutEvent
    
    
    MoveOutEvent(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Describes move-out of the key ranges out of the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]`.

To maintain processing the changes for a particular key in timestamp order, the query processing the `MoveOutEvent][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent]` in the partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]` should inform the queries processing the destination partitions that they can unblock and proceed processing records past the `commit_timestamp][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.commit_timestamp]`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
