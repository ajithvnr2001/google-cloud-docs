---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.StartBatchTransactionActionOrBuilder
title: Interface StartBatchTransactionActionOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:52:02.293594+00:00
---

# Interface StartBatchTransactionActionOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.StartBatchTransactionActionOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface StartBatchTransactionActionOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface StartBatchTransactionActionOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBatchTxnTime()
    
    
    public abstract Timestamp getBatchTxnTime()

The exact timestamp to start the batch transaction.

`.google.protobuf.Timestamp batch_txn_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The batchTxnTime.  
  
### getBatchTxnTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getBatchTxnTimeOrBuilder()

The exact timestamp to start the batch transaction.

`.google.protobuf.Timestamp batch_txn_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getCloudDatabaseRole()
    
    
    public abstract String getCloudDatabaseRole()

Database role to assume while performing this action. Setting the database_role will enforce additional role-based access checks on this action.

`string cloud_database_role = 3;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The cloudDatabaseRole.  
  
### getCloudDatabaseRoleBytes()
    
    
    public abstract ByteString getCloudDatabaseRoleBytes()

Database role to assume while performing this action. Setting the database_role will enforce additional role-based access checks on this action.

`string cloud_database_role = 3;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for cloudDatabaseRole.  
  
### getParamCase()
    
    
    public abstract StartBatchTransactionAction.ParamCase getParamCase()

**Returns**  
---  
**Type** | **Description**  
`[StartBatchTransactionAction.ParamCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.executor.v1.StartBatchTransactionAction.ParamCase)` |   
  
### getTid()
    
    
    public abstract ByteString getTid()

ID of a batch read-only transaction. It can be used to start the same batch transaction on multiple executors and parallelize partition processing.

`bytes tid = 2;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The tid.  
  
### hasBatchTxnTime()
    
    
    public abstract boolean hasBatchTxnTime()

The exact timestamp to start the batch transaction.

`.google.protobuf.Timestamp batch_txn_time = 1;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the batchTxnTime field is set.  
  
### hasTid()
    
    
    public abstract boolean hasTid()

ID of a batch read-only transaction. It can be used to start the same batch transaction on multiple executors and parallelize partition processing.

`bytes tid = 2;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the tid field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
