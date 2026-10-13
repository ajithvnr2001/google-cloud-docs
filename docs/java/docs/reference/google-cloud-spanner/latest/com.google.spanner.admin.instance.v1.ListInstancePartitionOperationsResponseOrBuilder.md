---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ListInstancePartitionOperationsResponseOrBuilder
title: Interface ListInstancePartitionOperationsResponseOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:40:45.469227+00:00
---

# Interface ListInstancePartitionOperationsResponseOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.instance.v1.ListInstancePartitionOperationsResponseOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface ListInstancePartitionOperationsResponseOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface ListInstancePartitionOperationsResponseOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getNextPageToken()
    
    
    public abstract String getNextPageToken()

`next_page_token` can be sent in a subsequent ListInstancePartitionOperations call to fetch more of the matching metadata.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The nextPageToken.  
  
### getNextPageTokenBytes()
    
    
    public abstract ByteString getNextPageTokenBytes()

`next_page_token` can be sent in a subsequent ListInstancePartitionOperations call to fetch more of the matching metadata.

`string next_page_token = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for nextPageToken.  
  
### getOperations(int index)
    
    
    public abstract Operation getOperations(int index)

The list of matching instance partition long-running operations. Each operation's name will be prefixed by the instance partition's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata.

`repeated .google.longrunning.Operation operations = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)` |   
  
### getOperationsCount()
    
    
    public abstract int getOperationsCount()

The list of matching instance partition long-running operations. Each operation's name will be prefixed by the instance partition's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata.

`repeated .google.longrunning.Operation operations = 1;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` |   
  
### getOperationsList()
    
    
    public abstract List<Operation> getOperationsList()

The list of matching instance partition long-running operations. Each operation's name will be prefixed by the instance partition's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata.

`repeated .google.longrunning.Operation operations = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[Operation](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.Operation.html)>` |   
  
### getOperationsOrBuilder(int index)
    
    
    public abstract OperationOrBuilder getOperationsOrBuilder(int index)

The list of matching instance partition long-running operations. Each operation's name will be prefixed by the instance partition's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata.

`repeated .google.longrunning.Operation operations = 1;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
  
**Returns**  
---  
**Type** | **Description**  
`[OperationOrBuilder](https://docs.cloud.google.com/java/docs/reference/gax/latest/com.google.longrunning.OperationOrBuilder.html)` |   
  
### getOperationsOrBuilderList()
    
    
    public abstract List<? extends OperationOrBuilder> getOperationsOrBuilderList()

The list of matching instance partition long-running operations. Each operation's name will be prefixed by the instance partition's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata.

`repeated .google.longrunning.Operation operations = 1;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<? extends com.google.longrunning.OperationOrBuilder>` |   
  
### getUnreachableInstancePartitions(int index)
    
    
    public abstract String getUnreachableInstancePartitions(int index)

The list of unreachable instance partitions. It includes the names of instance partitions whose operation metadata could not be retrieved within instance_partition_deadline.

`repeated string unreachable_instance_partitions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The unreachableInstancePartitions at the given index.  
  
### getUnreachableInstancePartitionsBytes(int index)
    
    
    public abstract ByteString getUnreachableInstancePartitionsBytes(int index)

The list of unreachable instance partitions. It includes the names of instance partitions whose operation metadata could not be retrieved within instance_partition_deadline.

`repeated string unreachable_instance_partitions = 3;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the unreachableInstancePartitions at the given index.  
  
### getUnreachableInstancePartitionsCount()
    
    
    public abstract int getUnreachableInstancePartitionsCount()

The list of unreachable instance partitions. It includes the names of instance partitions whose operation metadata could not be retrieved within instance_partition_deadline.

`repeated string unreachable_instance_partitions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of unreachableInstancePartitions.  
  
### getUnreachableInstancePartitionsList()
    
    
    public abstract List<String> getUnreachableInstancePartitionsList()

The list of unreachable instance partitions. It includes the names of instance partitions whose operation metadata could not be retrieved within instance_partition_deadline.

`repeated string unreachable_instance_partitions = 3;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the unreachableInstancePartitions.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
