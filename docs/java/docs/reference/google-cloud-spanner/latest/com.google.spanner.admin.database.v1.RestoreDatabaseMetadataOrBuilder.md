---
url: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseMetadataOrBuilder
title: Interface RestoreDatabaseMetadataOrBuilder (6.124.0) \u00a0|\u00a0 Java client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:28.873777+00:00
---

# Interface RestoreDatabaseMetadataOrBuilder (6.124.0)  |  Java client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseMetadataOrBuilder

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Java ](https://docs.cloud.google.com/java/docs)
  * [ Client libraries ](https://docs.cloud.google.com/java/docs/reference)



Send feedback 

#  Interface RestoreDatabaseMetadataOrBuilder (6.124.0) Stay organized with collections  Save and categorize content based on your preferences. 

6.124.0 (latest)  6.120.0  6.119.0  6.118.0  6.116.0  6.111.1  6.108.0  6.107.0  6.103.0  6.102.1  6.101.1  6.100.0  6.99.0  6.98.1  6.97.1  6.96.1  6.95.1  6.94.0  6.93.0  6.89.0  6.88.0  6.87.0  6.86.0  6.85.0  6.83.0  6.82.0  6.80.1  6.79.0  6.77.0  6.74.1  6.72.0  6.71.0  6.69.0  6.68.0  6.66.0  6.65.1  6.62.0  6.60.0  6.58.0  6.57.0  6.56.0  6.55.0  6.54.0  6.53.0  6.52.1  6.51.0  6.50.1  6.49.0  6.25.1  6.24.0  6.23.4  6.22.0  6.21.2  6.20.0  6.19.1  6.18.0  6.17.4  6.14.1 
    
    
    public interface RestoreDatabaseMetadataOrBuilder extends MessageOrBuilder

## Implements

[MessageOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.MessageOrBuilder.html)

## Methods 

### getBackupInfo()
    
    
    public abstract BackupInfo getBackupInfo()

Information about the backup used to restore the database.

`.google.spanner.admin.database.v1.BackupInfo backup_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BackupInfo](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupInfo)` | The backupInfo.  
  
### getBackupInfoOrBuilder()
    
    
    public abstract BackupInfoOrBuilder getBackupInfoOrBuilder()

Information about the backup used to restore the database.

`.google.spanner.admin.database.v1.BackupInfo backup_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[BackupInfoOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.BackupInfoOrBuilder)` |   
  
### getCancelTime()
    
    
    public abstract Timestamp getCancelTime()

The time at which cancellation of this operation was received. Operations.CancelOperation starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

`.google.protobuf.Timestamp cancel_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[Timestamp](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.Timestamp.html)` | The cancelTime.  
  
### getCancelTimeOrBuilder()
    
    
    public abstract TimestampOrBuilder getCancelTimeOrBuilder()

The time at which cancellation of this operation was received. Operations.CancelOperation starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

`.google.protobuf.Timestamp cancel_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[TimestampOrBuilder](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.TimestampOrBuilder.html)` |   
  
### getName()
    
    
    public abstract String getName()

Name of the database being created and restored to.

`string name = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The name.  
  
### getNameBytes()
    
    
    public abstract ByteString getNameBytes()

Name of the database being created and restored to.

`string name = 1 [(.google.api.resource_reference) = { ... }`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for name.  
  
### getOptimizeDatabaseOperationName()
    
    
    public abstract String getOptimizeDatabaseOperationName()

If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored database, and remove the dependency on the restore source. The name is of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>` where the <database> is the name of database being created and restored to. The metadata type of the long-running operation is OptimizeRestoredDatabaseMetadata. This long-running operation will be automatically created by the system after the RestoreDatabase long-running operation completes successfully. This operation will not be created if the restore was not successful.

`string optimize_database_operation_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[String](https://docs.oracle.com/javase/8/docs/api/java/lang/String.html)` | The optimizeDatabaseOperationName.  
  
### getOptimizeDatabaseOperationNameBytes()
    
    
    public abstract ByteString getOptimizeDatabaseOperationNameBytes()

If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored database, and remove the dependency on the restore source. The name is of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>` where the <database> is the name of database being created and restored to. The metadata type of the long-running operation is OptimizeRestoredDatabaseMetadata. This long-running operation will be automatically created by the system after the RestoreDatabase long-running operation completes successfully. This operation will not be created if the restore was not successful.

`string optimize_database_operation_name = 6;`

**Returns**  
---  
**Type** | **Description**  
`[ByteString](https://cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.ByteString.html)` | The bytes for optimizeDatabaseOperationName.  
  
### getProgress()
    
    
    public abstract OperationProgress getProgress()

The progress of the RestoreDatabase operation.

`.google.spanner.admin.database.v1.OperationProgress progress = 4;`

**Returns**  
---  
**Type** | **Description**  
`[OperationProgress](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.OperationProgress)` | The progress.  
  
### getProgressOrBuilder()
    
    
    public abstract OperationProgressOrBuilder getProgressOrBuilder()

The progress of the RestoreDatabase operation.

`.google.spanner.admin.database.v1.OperationProgress progress = 4;`

**Returns**  
---  
**Type** | **Description**  
`[OperationProgressOrBuilder](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.OperationProgressOrBuilder)` |   
  
### getSourceInfoCase()
    
    
    public abstract RestoreDatabaseMetadata.SourceInfoCase getSourceInfoCase()

**Returns**  
---  
**Type** | **Description**  
`[RestoreDatabaseMetadata.SourceInfoCase](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreDatabaseMetadata.SourceInfoCase)` |   
  
### getSourceType()
    
    
    public abstract RestoreSourceType getSourceType()

The type of the restore source.

`.google.spanner.admin.database.v1.RestoreSourceType source_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[RestoreSourceType](https://docs.cloud.google.com/java/docs/reference/google-cloud-spanner/latest/com.google.spanner.admin.database.v1.RestoreSourceType)` | The sourceType.  
  
### getSourceTypeValue()
    
    
    public abstract int getSourceTypeValue()

The type of the restore source.

`.google.spanner.admin.database.v1.RestoreSourceType source_type = 2;`

**Returns**  
---  
**Type** | **Description**  
`[int](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | The enum numeric value on the wire for sourceType.  
  
### hasBackupInfo()
    
    
    public abstract boolean hasBackupInfo()

Information about the backup used to restore the database.

`.google.spanner.admin.database.v1.BackupInfo backup_info = 3;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the backupInfo field is set.  
  
### hasCancelTime()
    
    
    public abstract boolean hasCancelTime()

The time at which cancellation of this operation was received. Operations.CancelOperation starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use Operations.GetOperation or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a google.rpc.Status.code of 1, corresponding to `Code.CANCELLED`.

`.google.protobuf.Timestamp cancel_time = 5;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the cancelTime field is set.  
  
### hasProgress()
    
    
    public abstract boolean hasProgress()

The progress of the RestoreDatabase operation.

`.google.spanner.admin.database.v1.OperationProgress progress = 4;`

**Returns**  
---  
**Type** | **Description**  
`[boolean](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html)` | Whether the progress field is set.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-06 UTC."],[],[]] 
