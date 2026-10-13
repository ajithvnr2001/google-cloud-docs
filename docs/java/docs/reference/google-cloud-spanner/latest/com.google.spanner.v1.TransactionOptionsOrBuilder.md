---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptionsOrBuilder
title: Interface TransactionOptionsOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:11:11.835335+00:00
---

# Interface TransactionOptionsOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptionsOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface TransactionOptionsOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface TransactionOptionsOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getExcludeTxnFromChangeStreams()
    
    
    public abstract boolean getExcludeTxnFromChangeStreams()

When `exclude_txn_from_change_streams` is set to `true`, it prevents read or write transactions from being tracked in change streams.

  * If the DDL option `allow_txn_exclusion` is set to `true`, then the updates made within this transaction aren't recorded in the change stream.

  * If you don't set the DDL option `allow_txn_exclusion` or if it's set to `false`, then the updates made within this transaction are recorded in the change stream.

When `exclude_txn_from_change_streams` is set to `false` or not set, modifications from this transaction are recorded in all change streams that are tracking columns modified by these transactions.

The `exclude_txn_from_change_streams` option can only be specified for read-write or partitioned DML transactions, otherwise the API returns an `INVALID_ARGUMENT` error.




`bool exclude_txn_from_change_streams = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The excludeTxnFromChangeStreams.  
  
### getIsolationLevel()
    
    
    public abstract TransactionOptions.IsolationLevel getIsolationLevel()

Isolation level for the transaction.

`.google.spanner.v1.TransactionOptions.IsolationLevel isolation_level = 6;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.IsolationLevel](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.IsolationLevel)` | The isolationLevel.  
  
### getIsolationLevelValue()
    
    
    public abstract int getIsolationLevelValue()

Isolation level for the transaction.

`.google.spanner.v1.TransactionOptions.IsolationLevel isolation_level = 6;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for isolationLevel.  
  
### getModeCase()
    
    
    public abstract TransactionOptions.ModeCase getModeCase()

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ModeCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.ModeCase)` |   
  
### getPartitionedDml()
    
    
    public abstract TransactionOptions.PartitionedDml getPartitionedDml()

Partitioned DML transaction.

Authorization to begin a Partitioned DML transaction requires `spanner.databases.beginPartitionedDmlTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.PartitionedDml partitioned_dml = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.PartitionedDml](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.PartitionedDml)` | The partitionedDml.  
  
### getPartitionedDmlOrBuilder()
    
    
    public abstract TransactionOptions.PartitionedDmlOrBuilder getPartitionedDmlOrBuilder()

Partitioned DML transaction.

Authorization to begin a Partitioned DML transaction requires `spanner.databases.beginPartitionedDmlTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.PartitionedDml partitioned_dml = 3;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.PartitionedDmlOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.PartitionedDmlOrBuilder)` |   
  
### getReadOnly()
    
    
    public abstract TransactionOptions.ReadOnly getReadOnly()

Transaction does not write.

Authorization to begin a read-only transaction requires `spanner.databases.beginReadOnlyTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnly](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.ReadOnly)` | The readOnly.  
  
### getReadOnlyOrBuilder()
    
    
    public abstract TransactionOptions.ReadOnlyOrBuilder getReadOnlyOrBuilder()

Transaction does not write.

Authorization to begin a read-only transaction requires `spanner.databases.beginReadOnlyTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadOnlyOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.ReadOnlyOrBuilder)` |   
  
### getReadWrite()
    
    
    public abstract TransactionOptions.ReadWrite getReadWrite()

Transaction may write.

Authorization to begin a read-write transaction requires `spanner.databases.beginOrRollbackReadWriteTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWrite](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.ReadWrite)` | The readWrite.  
  
### getReadWriteOrBuilder()
    
    
    public abstract TransactionOptions.ReadWriteOrBuilder getReadWriteOrBuilder()

Transaction may write.

Authorization to begin a read-write transaction requires `spanner.databases.beginOrRollbackReadWriteTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TransactionOptions.ReadWriteOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.v1.TransactionOptions.ReadWriteOrBuilder)` |   
  
### hasPartitionedDml()
    
    
    public abstract boolean hasPartitionedDml()

Partitioned DML transaction.

Authorization to begin a Partitioned DML transaction requires `spanner.databases.beginPartitionedDmlTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.PartitionedDml partitioned_dml = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the partitionedDml field is set.  
  
### hasReadOnly()
    
    
    public abstract boolean hasReadOnly()

Transaction does not write.

Authorization to begin a read-only transaction requires `spanner.databases.beginReadOnlyTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.ReadOnly read_only = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readOnly field is set.  
  
### hasReadWrite()
    
    
    public abstract boolean hasReadWrite()

Transaction may write.

Authorization to begin a read-write transaction requires `spanner.databases.beginOrRollbackReadWriteTransaction` permission on the `session` resource.

`.google.spanner.v1.TransactionOptions.ReadWrite read_write = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the readWrite field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
