---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PartitionReadRequestOrBuilder
title: Interface PartitionReadRequestOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:18:17.816060+00:00
---

# Interface PartitionReadRequestOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PartitionReadRequestOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface PartitionReadRequestOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface PartitionReadRequestOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getColumns(int index)
    
    
    public abstract String getColumns(int index)

The columns of table to be returned for each row matching this request.

`repeated string columns = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the element to return.  
**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The columns at the given index.  
  
### getColumnsBytes(int index)
    
    
    public abstract ByteString getColumnsBytes(int index)

The columns of table to be returned for each row matching this request.

`repeated string columns = 5;`

**Parameter**  
---  
**Name** | **Description**  
`index` | `[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)`  
The index of the value to return.  
**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes of the columns at the given index.  
  
### getColumnsCount()
    
    
    public abstract int getColumnsCount()

The columns of table to be returned for each row matching this request.

`repeated string columns = 5;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The count of columns.  
  
### getColumnsList()
    
    
    public abstract List<String> getColumnsList()

The columns of table to be returned for each row matching this request.

`repeated string columns = 5;`

**Returns**  
---  
**Type** | **Description**  
`[List](https://docs.oracle.com/javase/8/docs/api/java/util/List.html)<[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)>` | A list containing the columns.  
  
### getIndex()
    
    
    public abstract String getIndex()

If non-empty, the name of an index on table. This index is used instead of the table primary key when interpreting key_set and sorting result rows. See key_set for further information.

`string index = 4;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The index.  
  
### getIndexBytes()
    
    
    public abstract ByteString getIndexBytes()

If non-empty, the name of an index on table. This index is used instead of the table primary key when interpreting key_set and sorting result rows. See key_set for further information.

`string index = 4;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for index.  
  
### getKeySet()
    
    
    public abstract KeySet getKeySet()

Required. `key_set` identifies the rows to be yielded. `key_set` names the primary keys of the rows in table to be yielded, unless index is present. If index is present, then key_set instead names index keys in index.

It isn't an error for the `key_set` to name rows that don't exist in the database. Read yields nothing for nonexistent rows.

`.google.spanner.v1.KeySet key_set = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[KeySet](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.KeySet)` | The keySet.  
  
### getKeySetOrBuilder()
    
    
    public abstract KeySetOrBuilder getKeySetOrBuilder()

Required. `key_set` identifies the rows to be yielded. `key_set` names the primary keys of the rows in table to be yielded, unless index is present. If index is present, then key_set instead names index keys in index.

It isn't an error for the `key_set` to name rows that don't exist in the database. Read yields nothing for nonexistent rows.

`.google.spanner.v1.KeySet key_set = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[KeySetOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.KeySetOrBuilder)` |   
  
### getPartitionOptions()
    
    
    public abstract PartitionOptions getPartitionOptions()

Additional options that affect how many partitions are created.

`.google.spanner.v1.PartitionOptions partition_options = 9;`

**Returns**  
---  
**Type** | **Description**  
`[PartitionOptions](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PartitionOptions)` | The partitionOptions.  
  
### getPartitionOptionsOrBuilder()
    
    
    public abstract PartitionOptionsOrBuilder getPartitionOptionsOrBuilder()

Additional options that affect how many partitions are created.

`.google.spanner.v1.PartitionOptions partition_options = 9;`

**Returns**  
---  
**Type** | **Description**  
`[PartitionOptionsOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.PartitionOptionsOrBuilder)` |   
  
### getSession()
    
    
    public abstract String getSession()

Required. The session used to create the partitions.

` string session = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The session.  
  
### getSessionBytes()
    
    
    public abstract ByteString getSessionBytes()

Required. The session used to create the partitions.

` string session = 1 [(.google.api.field_behavior) = REQUIRED, (.google.api.resource_reference) = { ... } `

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for session.  
  
### getTable()
    
    
    public abstract String getTable()

Required. The name of the table in the database to be read.

`string table = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The table.  
  
### getTableBytes()
    
    
    public abstract ByteString getTableBytes()

Required. The name of the table in the database to be read.

`string table = 3 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for table.  
  
### getTransaction()
    
    
    public abstract TransactionSelector getTransaction()

Read only snapshot transactions are supported, read/write and single use transactions are not.

`.google.spanner.v1.TransactionSelector transaction = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionSelector](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionSelector)` | The transaction.  
  
### getTransactionOrBuilder()
    
    
    public abstract TransactionSelectorOrBuilder getTransactionOrBuilder()

Read only snapshot transactions are supported, read/write and single use transactions are not.

`.google.spanner.v1.TransactionSelector transaction = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionSelectorOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionSelectorOrBuilder)` |   
  
### hasKeySet()
    
    
    public abstract boolean hasKeySet()

Required. `key_set` identifies the rows to be yielded. `key_set` names the primary keys of the rows in table to be yielded, unless index is present. If index is present, then key_set instead names index keys in index.

It isn't an error for the `key_set` to name rows that don't exist in the database. Read yields nothing for nonexistent rows.

`.google.spanner.v1.KeySet key_set = 6 [(.google.api.field_behavior) = REQUIRED];`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the keySet field is set.  
  
### hasPartitionOptions()
    
    
    public abstract boolean hasPartitionOptions()

Additional options that affect how many partitions are created.

`.google.spanner.v1.PartitionOptions partition_options = 9;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partitionOptions field is set.  
  
### hasTransaction()
    
    
    public abstract boolean hasTransaction()

Read only snapshot transactions are supported, read/write and single use transactions are not.

`.google.spanner.v1.TransactionSelector transaction = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the transaction field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
