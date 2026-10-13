---
url: https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1
title: Package google.spanner.admin.database.v1 \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:30:26.372873+00:00
---

# Package google.spanner.admin.database.v1  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Package google.spanner.admin.database.v1 Stay organized with collections  Save and categorize content based on your preferences. 

## Index

  * `[DatabaseAdmin](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin)` (interface)
  * `[AddSplitPointsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.AddSplitPointsRequest)` (message)
  * `[AddSplitPointsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.AddSplitPointsResponse)` (message)
  * `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)` (message)
  * `[Backup.State](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup.State)` (enum)
  * `[BackupInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupInfo)` (message)
  * `[BackupInstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupInstancePartition)` (message)
  * `[BackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupSchedule)` (message)
  * `[BackupScheduleSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupScheduleSpec)` (message)
  * `[ChangeQuorumMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ChangeQuorumMetadata)` (message)
  * `[ChangeQuorumRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ChangeQuorumRequest)` (message)
  * `[CompactDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CompactDatabaseMetadata)` (message)
  * `[CopyBackupEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupEncryptionConfig)` (message)
  * `[CopyBackupEncryptionConfig.EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupEncryptionConfig.EncryptionType)` (enum)
  * `[CopyBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupMetadata)` (message)
  * `[CopyBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupRequest)` (message)
  * `[CreateBackupEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig)` (message)
  * `[CreateBackupEncryptionConfig.EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig.EncryptionType)` (enum)
  * `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupMetadata)` (message)
  * `[CreateBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupRequest)` (message)
  * `[CreateBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupScheduleRequest)` (message)
  * `[CreateDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateDatabaseMetadata)` (message)
  * `[CreateDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateDatabaseRequest)` (message)
  * `[CrontabSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CrontabSpec)` (message)
  * `[Database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database)` (message)
  * `[Database.State](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database.State)` (enum)
  * `[DatabaseDialect](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseDialect)` (enum)
  * `[DatabaseRole](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseRole)` (message)
  * `[DdlStatementActionInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DdlStatementActionInfo)` (message)
  * `[DeleteBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DeleteBackupRequest)` (message)
  * `[DeleteBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DeleteBackupScheduleRequest)` (message)
  * `[DropDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DropDatabaseRequest)` (message)
  * `[EncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionConfig)` (message)
  * `[EncryptionInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionInfo)` (message)
  * `[EncryptionInfo.Type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionInfo.Type)` (enum)
  * `[FullBackupSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.FullBackupSpec)` (message)
  * `[GetBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetBackupRequest)` (message)
  * `[GetBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetBackupScheduleRequest)` (message)
  * `[GetDatabaseDdlRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetDatabaseDdlRequest)` (message)
  * `[GetDatabaseDdlResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetDatabaseDdlResponse)` (message)
  * `[GetDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetDatabaseRequest)` (message)
  * `[IncrementalBackupSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.IncrementalBackupSpec)` (message)
  * `[ListBackupOperationsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupOperationsRequest)` (message)
  * `[ListBackupOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupOperationsResponse)` (message)
  * `[ListBackupSchedulesRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupSchedulesRequest)` (message)
  * `[ListBackupSchedulesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupSchedulesResponse)` (message)
  * `[ListBackupsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupsRequest)` (message)
  * `[ListBackupsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupsResponse)` (message)
  * `[ListDatabaseOperationsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseOperationsRequest)` (message)
  * `[ListDatabaseOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseOperationsResponse)` (message)
  * `[ListDatabaseRolesRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseRolesRequest)` (message)
  * `[ListDatabaseRolesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseRolesResponse)` (message)
  * `[ListDatabasesRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabasesRequest)` (message)
  * `[ListDatabasesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabasesResponse)` (message)
  * `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` (message)
  * `[OptimizeRestoredDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)` (message)
  * `[QuorumInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumInfo)` (message)
  * `[QuorumInfo.Initiator](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumInfo.Initiator)` (enum)
  * `[QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType)` (message)
  * `[QuorumType.DualRegionQuorum](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType.DualRegionQuorum)` (message)
  * `[QuorumType.SingleRegionQuorum](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType.SingleRegionQuorum)` (message)
  * `[RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig)` (message)
  * `[RestoreDatabaseEncryptionConfig.EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.EncryptionType)` (enum)
  * `[RestoreDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseMetadata)` (message)
  * `[RestoreDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseRequest)` (message)
  * `[RestoreInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreInfo)` (message)
  * `[RestoreSourceType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreSourceType)` (enum)
  * `[SplitPoints](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.SplitPoints)` (message)
  * `[SplitPoints.Key](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.SplitPoints.Key)` (message)
  * `[UpdateBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateBackupRequest)` (message)
  * `[UpdateBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateBackupScheduleRequest)` (message)
  * `[UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata)` (message)
  * `[UpdateDatabaseDdlRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseDdlRequest)` (message)
  * `[UpdateDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseMetadata)` (message)
  * `[UpdateDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseRequest)` (message)



## DatabaseAdmin

Cloud Spanner Database Admin API

The Cloud Spanner Database Admin API can be used to: * create, drop, and list databases * update the schema of pre-existing databases * create, delete, copy and list backups for a database * restore a database from an existing backup

AddSplitPoints  
---  
` rpc AddSplitPoints(`[AddSplitPointsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.AddSplitPointsRequest)`) returns (`[AddSplitPointsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.AddSplitPointsResponse)`) ` Adds split points to specified tables and indexes of a database.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ChangeQuorum  
---  
` rpc ChangeQuorum(`[ChangeQuorumRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ChangeQuorumRequest)`) returns (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` `ChangeQuorum` is strictly restricted to databases that use dual-region instance configurations.Initiates a background operation to change the quorum of a database from dual-region mode to single-region mode or vice versa.The returned long-running operation has a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operation_id>` and can be used to track execution of the `ChangeQuorum`. The metadata field type is `[ChangeQuorumMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ChangeQuorumMetadata)`.Authorization requires `spanner.databases.changequorum` permission on the resource database.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CopyBackup  
---  
` rpc CopyBackup(`[CopyBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupRequest)`) returns (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Starts copying a Cloud Spanner Backup. The returned backup long-running operation will have a name of the format `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation_id>` and can be used to track copying of the backup. The operation is associated with the destination backup. The metadata field type is `[CopyBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupMetadata)`. The response field type is `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)`, if successful. Cancelling the returned operation will stop the copying and delete the destination backup. Concurrent CopyBackup requests can run on the same source backup.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `spanner.backups.create`

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `sourceBackup` resource:

  * `spanner.backups.copy`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateBackup  
---  
` rpc CreateBackup(`[CreateBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupRequest)`) returns (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Starts creating a new Cloud Spanner Backup. The returned backup long-running operation will have a name of the format `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation_id>` and can be used to track creation of the backup. The metadata field type is `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupMetadata)`. The response field type is `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)`, if successful. Cancelling the returned operation will stop the creation and delete the backup. There can be only one pending backup creation per database. Backup creation of different databases can run concurrently.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `database` resource:

  * `spanner.databases.createBackup`

Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `parent` resource:

  * `spanner.backups.create`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
CreateBackupSchedule  
---  
` rpc CreateBackupSchedule(`[CreateBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupScheduleRequest)`) returns (`[BackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupSchedule)`) ` Creates a new backup schedule.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
CreateDatabase  
---  
` rpc CreateDatabase(`[CreateDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateDatabaseRequest)`) returns (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Creates a new Spanner database and starts to prepare it for serving. The returned long-running operation will have a name of the format `<database_name>/operations/<operation_id>` and can be used to track preparation of the database. The metadata field type is `[CreateDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateDatabaseMetadata)`. The response field type is `[Database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database)`, if successful.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteBackup  
---  
` rpc DeleteBackup(`[DeleteBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DeleteBackupRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a pending or completed `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DeleteBackupSchedule  
---  
` rpc DeleteBackupSchedule(`[DeleteBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DeleteBackupScheduleRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Deletes a backup schedule.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
DropDatabase  
---  
` rpc DropDatabase(`[DropDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DropDatabaseRequest)`) returns (`[Empty](https://protobuf.dev/reference/protobuf/google.protobuf/#empty)`) ` Drops (aka deletes) a Cloud Spanner database. Completed backups for the database will be retained according to their `expire_time`. Note: Cloud Spanner might continue to accept requests for a few seconds after the database has been deleted.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetBackup  
---  
` rpc GetBackup(`[GetBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetBackupRequest)`) returns (`[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)`) ` Gets metadata on a pending or completed `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetBackupSchedule  
---  
` rpc GetBackupSchedule(`[GetBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetBackupScheduleRequest)`) returns (`[BackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupSchedule)`) ` Gets backup schedule for the input schedule name.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDatabase  
---  
` rpc GetDatabase(`[GetDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetDatabaseRequest)`) returns (`[Database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database)`) ` Gets the state of a Cloud Spanner database.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetDatabaseDdl  
---  
` rpc GetDatabaseDdl(`[GetDatabaseDdlRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetDatabaseDdlRequest)`) returns (`[GetDatabaseDdlResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.GetDatabaseDdlResponse)`) ` Returns the schema of a Cloud Spanner database as a list of formatted DDL statements. This method does not show pending schema updates, those may be queried using the `[Operations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations)` API.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
GetIamPolicy  
---  
` rpc GetIamPolicy(`[GetIamPolicyRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.GetIamPolicyRequest)`) returns (`[Policy](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)`) ` Gets the access control policy for a database or backup resource. Returns an empty policy if a database or backup exists but does not have a policy set.Authorization requires `spanner.databases.getIamPolicy` permission on `[resource](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.GetIamPolicyRequest.FIELDS.string.google.iam.v1.GetIamPolicyRequest.resource)`. For backups, authorization requires `spanner.backups.getIamPolicy` permission on `[resource](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.GetIamPolicyRequest.FIELDS.string.google.iam.v1.GetIamPolicyRequest.resource)`. For backup schedules, authorization requires `spanner.backupSchedules.getIamPolicy` permission on `[resource](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.GetIamPolicyRequest.FIELDS.string.google.iam.v1.GetIamPolicyRequest.resource)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListBackupOperations  
---  
` rpc ListBackupOperations(`[ListBackupOperationsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupOperationsRequest)`) returns (`[ListBackupOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupOperationsResponse)`) ` Lists the backup long-running operations in the given instance. A backup operation has a name of the form `projects/<project>/instances/<instance>/backups/<backup>/operations/<operation>`. The long-running operation metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations. Operations returned are ordered by `operation.metadata.value.progress.start_time` in descending order starting from the most recently started operation.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListBackupSchedules  
---  
` rpc ListBackupSchedules(`[ListBackupSchedulesRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupSchedulesRequest)`) returns (`[ListBackupSchedulesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupSchedulesResponse)`) ` Lists all the backup schedules for the database.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListBackups  
---  
` rpc ListBackups(`[ListBackupsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupsRequest)`) returns (`[ListBackupsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupsResponse)`) ` Lists completed and pending backups. Backups returned are ordered by `create_time` in descending order, starting from the most recent `create_time`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDatabaseOperations  
---  
` rpc ListDatabaseOperations(`[ListDatabaseOperationsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseOperationsRequest)`) returns (`[ListDatabaseOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseOperationsResponse)`) ` Lists database longrunning-operations. A database operation has a name of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>`. The long-running operation metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that have completed/failed/canceled within the last 7 days, and pending operations.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDatabaseRoles  
---  
` rpc ListDatabaseRoles(`[ListDatabaseRolesRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseRolesRequest)`) returns (`[ListDatabaseRolesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseRolesResponse)`) ` Lists Cloud Spanner database roles.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
ListDatabases  
---  
` rpc ListDatabases(`[ListDatabasesRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabasesRequest)`) returns (`[ListDatabasesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabasesResponse)`) ` Lists Cloud Spanner databases.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
RestoreDatabase  
---  
` rpc RestoreDatabase(`[RestoreDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseRequest)`) returns (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Create a new database by restoring from a completed backup. The new database must be in the same project and in an instance with the same instance configuration as the instance containing the backup. The returned database long-running operation has a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operation_id>`, and can be used to track the progress of the operation, and to cancel it. The metadata field type is `[RestoreDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseMetadata)`. The response type is `[Database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database)`, if successful. Cancelling the returned operation will stop the restore and delete the database. There can be only one database being restored into an instance at a time. Once the restore operation completes, a new restore operation can be initiated, without waiting for the optimize operation associated with the first restore to complete.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
SetIamPolicy  
---  
` rpc SetIamPolicy(`[SetIamPolicyRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.SetIamPolicyRequest)`) returns (`[Policy](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.Policy)`) ` Sets the access control policy on a database or backup resource. Replaces any existing policy.Authorization requires `spanner.databases.setIamPolicy` permission on `[resource](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.SetIamPolicyRequest.FIELDS.string.google.iam.v1.SetIamPolicyRequest.resource)`. For backups, authorization requires `spanner.backups.setIamPolicy` permission on `[resource](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.SetIamPolicyRequest.FIELDS.string.google.iam.v1.SetIamPolicyRequest.resource)`. For backup schedules, authorization requires `spanner.backupSchedules.setIamPolicy` permission on `[resource](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.SetIamPolicyRequest.FIELDS.string.google.iam.v1.SetIamPolicyRequest.resource)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
TestIamPermissions  
---  
` rpc TestIamPermissions(`[TestIamPermissionsRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.TestIamPermissionsRequest)`) returns (`[TestIamPermissionsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.iam.v1#google.iam.v1.TestIamPermissionsResponse)`) ` Returns permissions that the caller has on the specified database or backup resource.Attempting this RPC on a non-existent Cloud Spanner database will result in a NOT_FOUND error if the user has `spanner.databases.list` permission on the containing Cloud Spanner instance. Otherwise returns an empty set of permissions. Calling this method on a backup that does not exist will result in a NOT_FOUND error if the user has `spanner.backups.list` permission on the containing instance. Calling this method on a backup schedule that does not exist will result in a NOT_FOUND error if the user has `spanner.backupSchedules.list` permission on the containing database.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateBackup  
---  
` rpc UpdateBackup(`[UpdateBackupRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateBackupRequest)`) returns (`[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)`) ` Updates a pending or completed `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)`.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

IAM Permissions
     Requires the following [IAM](https://cloud.google.com/iam/docs) permission on the `name` resource:

  * `spanner.backups.update`

For more information, see the [IAM documentation](https://cloud.google.com/iam/docs).  
UpdateBackupSchedule  
---  
` rpc UpdateBackupSchedule(`[UpdateBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateBackupScheduleRequest)`) returns (`[BackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupSchedule)`) ` Updates a backup schedule.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDatabase  
---  
` rpc UpdateDatabase(`[UpdateDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseRequest)`) returns (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates a Cloud Spanner database. The returned long-running operation can be used to track the progress of updating the database. If the named database does not exist, returns `NOT_FOUND`.While the operation is pending:

  * The database's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database.FIELDS.bool.google.spanner.admin.database.v1.Database.reconciling)` field is set to true.
  * Cancelling the operation is best-effort. If the cancellation succeeds, the operation metadata's `[cancel_time](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseMetadata.FIELDS.google.protobuf.Timestamp.google.spanner.admin.database.v1.UpdateDatabaseMetadata.cancel_time)` is set, the updates are reverted, and the operation terminates with a `CANCELLED` status.
  * New UpdateDatabase requests will return a `FAILED_PRECONDITION` error until the pending operation is done (returns successfully or with error).
  * Reading the database via the API continues to give the pre-request values.

Upon completion of the returned operation:

  * The new values are in effect and readable via the API.
  * The database's `[reconciling](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database.FIELDS.bool.google.spanner.admin.database.v1.Database.reconciling)` field becomes false.

The returned long-running operation will have a name of the format `projects/<project>/instances/<instance>/databases/<database>/operations/<operation_id>` and can be used to track the database modification. The metadata field type is `[UpdateDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseMetadata)`. The response field type is `[Database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database)`, if successful.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
UpdateDatabaseDdl  
---  
` rpc UpdateDatabaseDdl(`[UpdateDatabaseDdlRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseDdlRequest)`) returns (`[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)`) ` Updates the schema of a Cloud Spanner database by creating/altering/dropping tables, columns, indexes, etc. The returned long-running operation will have a name of the format `<database_name>/operations/<operation_id>` and can be used to track execution of the schema changes. The metadata field type is `[UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseDdlMetadata)`. The operation has no response.

Authorization scopes
     Requires one of the following OAuth scopes:

  * `https://www.googleapis.com/auth/spanner.admin`
  * `https://www.googleapis.com/auth/cloud-platform`

For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).  
  
## AddSplitPointsRequest

The request for `[AddSplitPoints](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.AddSplitPoints)`.

Fields  
---  
`database` |  `string` Required. The database on whose tables or indexes the split points are to be added. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.addSplitPoints`

  
`split_points[]` |  `[SplitPoints](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.SplitPoints)` Required. The split points to add.  
`initiator` |  `string` Optional. A user-supplied tag associated with the split points. For example, "initial_data_load", "special_event_1". Defaults to "CloudAddSplitPointsAPI" if not specified. The length of the tag must not exceed 50 characters, or else it is trimmed. Only valid UTF8 characters are allowed.  
  
## AddSplitPointsResponse

This type has no fields.

The response for `[AddSplitPoints](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.AddSplitPoints)`.

## Backup

A backup of a Cloud Spanner database.

Fields  
---  
`database` |  `string` Required for the `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`.  
`version_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The backup will contain an externally consistent copy of the database at the timestamp specified by `version_time`. If `version_time` is not specified, the system will set `version_time` to the `create_time` of the backup.  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required for the `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup.  
`name` |  `string` Output only for the `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` operation. Required for the `[UpdateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackup)` operation.A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/<project>/instances/<instance>/backups/[a-z][a-z0-9_\-]*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length.The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form `projects/<project>/instances/<instance>`.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time the `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` request is received. If the request does not specify `version_time`, the `version_time` of the backup will be equivalent to the `create_time`.  
`size_bytes` |  `int64` Output only. Size of the backup in bytes. For a backup in an incremental backup chain, this is the sum of the `exclusive_size_bytes` of itself and all older backups in the chain.  
`freeable_size_bytes` |  `int64` Output only. The number of bytes that will be freed by deleting this backup. This value will be zero if, for example, this backup is part of an incremental backup chain and younger backups in the chain require that we keep its data. For backups not in an incremental backup chain, this is always the size of the backup. This value may change if backups on the same chain get created, deleted or expired.  
`exclusive_size_bytes` |  `int64` Output only. For a backup in an incremental backup chain, this is the storage space needed to keep the data that has changed since the previous backup. For all other backups, this is always the size of the backup. This value may change if backups on the same chain get deleted or expired.This field can be used to calculate the total storage space used by a set of backups. For example, the total space used by all backups of a database can be computed by summing up this field.  
`state` |  `[State](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup.State)` Output only. The current state of the backup.  
`referencing_databases[]` |  `string` Output only. The names of the restored databases that reference the backup. The database names are of the form `projects/<project>/instances/<instance>/databases/<database>`. Referencing databases may exist in different instances. The existence of any referencing database prevents the backup from being deleted. When a restored database from the backup enters the `READY` state, the reference to the backup is removed.  
`encryption_info` |  `[EncryptionInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionInfo)` Output only. The encryption information for the backup.  
`encryption_information[]` |  `[EncryptionInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionInfo)` Output only. The encryption information for the backup, whether it is protected by one or more KMS keys. The information includes all Cloud KMS key versions used to encrypt the backup. The `encryption_status` field inside of each `EncryptionInfo` is not populated. At least one of the key versions must be available for the backup to be restored. If a key version is revoked in the middle of a restore, the restore behavior is undefined.  
`database_dialect` |  `[DatabaseDialect](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseDialect)` Output only. The database dialect information for the backup.  
`referencing_backups[]` |  `string` Output only. The names of the destination backups being created by copying this source backup. The backup names are of the form `projects/<project>/instances/<instance>/backups/<backup>`. Referencing backups may exist in different instances. The existence of any referencing backup prevents the backup from being deleted. When the copy operation is done (either successfully completed or cancelled or the destination backup is deleted), the reference to the backup is removed.  
`max_expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The max allowed expiration time of the backup, with microseconds granularity. A backup's expiration time can be configured in multiple APIs: CreateBackup, UpdateBackup, CopyBackup. When updating or copying an existing backup, the expiration time specified must be less than `Backup.max_expire_time`.  
`backup_schedules[]` |  `string` Output only. List of backup schedule URIs that are associated with creating this backup. This is only applicable for scheduled backups, and is empty for on-demand backups.To optimize for storage, whenever possible, multiple schedules are collapsed together to create one backup. In such cases, this field captures the list of all backup schedule URIs that are associated with creating this backup. If collapsing is not done, then this field captures the single backup schedule URI associated with creating this backup.  
`incremental_backup_chain_id` |  `string` Output only. Populated only for backups in an incremental backup chain. Backups share the same chain id if and only if they belong to the same incremental backup chain. Use this field to determine which backups are part of the same incremental backup chain. The ordering of backups in the chain can be determined by ordering the backup `version_time`.  
`oldest_version_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Data deleted at a time older than this is guaranteed not to be retained in order to support this backup. For a backup in an incremental backup chain, this is the version time of the oldest backup that exists or ever existed in the chain. For all other backups, this is the version time of the backup. This field can be used to understand what data is being retained by the backup system.  
`instance_partitions[]` |  `[BackupInstancePartition](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupInstancePartition)` Output only. The instance partition storing the backup.This is the same as the list of the instance partitions that the database recorded at the backup's `version_time`.  
`minimum_restorable_edition` |  `[Edition](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.instance.v1#google.spanner.admin.instance.v1.Instance.Edition)` Output only. The minimum edition required to successfully restore the backup. Populated only if the edition is Enterprise or Enterprise Plus.  
  
## State

Indicates the current state of the backup.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`CREATING` | The pending backup is still being created. Operations on the backup may fail with `FAILED_PRECONDITION` in this state.  
`READY` | The backup is complete and ready for use.  
  
## BackupInfo

Information about a backup.

Fields  
---  
`backup` |  `string` Name of the backup.  
`version_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The backup contains an externally consistent copy of `source_database` at the timestamp specified by `version_time`. If the `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` request did not specify `version_time`, the `version_time` of the backup is equivalent to the `create_time`.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time the `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` request was received.  
`source_database` |  `string` Name of the database the backup was created from.  
  
## BackupInstancePartition

Instance partition information for the backup.

Fields  
---  
`instance_partition` |  `string` A unique identifier for the instance partition. Values are of the form `projects/<project>/instances/<instance>/instancePartitions/<instance_partition_id>`  
  
## BackupSchedule

BackupSchedule expresses the automated backup creation specification for a Spanner database.

Fields  
---  
`name` |  `string` Identifier. Output only for the `[CreateBackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackupSchedule)` operation. Required for the `[UpdateBackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackupSchedule)` operation. A globally unique identifier for the backup schedule which cannot be changed. Values are of the form `projects/<project>/instances/<instance>/databases/<database>/backupSchedules/[a-z][a-z0-9_\-]*[a-z0-9]` The final segment of the name must be between 2 and 60 characters in length.  
`spec` |  `[BackupScheduleSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupScheduleSpec)` Optional. The schedule specification based on which the backup creations are triggered.  
`retention_duration` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Optional. The retention duration of a backup that must be at least 6 hours and at most 366 days. The backup is eligible to be automatically deleted once the retention period has elapsed.  
`encryption_config` |  `[CreateBackupEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig)` Optional. The encryption configuration that is used to encrypt the backup. If this field is not specified, the backup uses the same encryption configuration as the database.  
`update_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp at which the schedule was last updated. If the schedule has never been updated, this field contains the timestamp when the schedule was first created.  
Union field `backup_type_spec`. Required. Backup type specification determines the type of backup that is created by the backup schedule. `backup_type_spec` can be only one of the following:  
`full_backup_spec` |  `[FullBackupSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.FullBackupSpec)` The schedule creates only full backups.  
`incremental_backup_spec` |  `[IncrementalBackupSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.IncrementalBackupSpec)` The schedule creates incremental backup chains.  
  
## BackupScheduleSpec

Defines specifications of the backup schedule.

Fields  
---  
Union field `schedule_spec`. Required. `schedule_spec` can be only one of the following:  
`cron_spec` |  `[CrontabSpec](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CrontabSpec)` Cron style schedule specification.  
  
## ChangeQuorumMetadata

Metadata type for the long-running operation returned by `[ChangeQuorum](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ChangeQuorum)`.

Fields  
---  
`request` |  `[ChangeQuorumRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ChangeQuorumRequest)` The request for `[ChangeQuorum](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ChangeQuorum)`.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time the request was received.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` If set, the time at which this operation failed or was completed successfully.  
  
## ChangeQuorumRequest

The request for `[ChangeQuorum](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ChangeQuorum)`.

Fields  
---  
`name` |  `string` Required. Name of the database in which to apply `ChangeQuorum`. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.databases.changequorum`

  
`quorum_type` |  `[QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType)` Required. The type of this quorum.  
`etag` |  `string` Optional. The etag is the hash of the `QuorumInfo`. The `ChangeQuorum` operation is only performed if the etag matches that of the `QuorumInfo` in the current database resource. Otherwise the API returns an `ABORTED` error.The etag is used for optimistic concurrency control as a way to help prevent simultaneous change quorum requests that could create a race condition.  
  
## CompactDatabaseMetadata

Metadata type for the long-running operation returned by `CALL compact_all()`, which can be executed using `[ExecuteSql](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.ExecuteSql)` or `[ExecuteStreamingSql](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.v1#google.spanner.v1.Spanner.ExecuteStreamingSql)` APIs.

Fields  
---  
`database` |  `string` Output only. The database being compacted.  
`progress` |  `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` Output only. The progress of the compaction operation.  
`cancel_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The time at which cancellation of this operation was received. `[Operations.CancelOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)` starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use `[Operations.GetOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a `[google.rpc.Status.code](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
  
## CopyBackupEncryptionConfig

Encryption configuration for the copied backup.

Fields  
---  
`encryption_type` |  `[EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupEncryptionConfig.EncryptionType)` Required. The encryption type of the backup.  
`kms_key_name` |  `string` Optional. This field is maintained for backwards compatibility. For new callers, we recommend using `kms_key_names` to specify the KMS key. Only use `kms_key_name` if the location of the KMS key matches the database instance's configuration (location) exactly. For example, if the KMS location is in `us-central1` or `nam3`, then the database instance must also be in `us-central1` or `nam3`.The Cloud KMS key that is used to encrypt and decrypt the restored database. Set this field only when `[encryption_type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupEncryptionConfig.FIELDS.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.EncryptionType.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.encryption_type)` is `CUSTOMER_MANAGED_ENCRYPTION`. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.  
`kms_key_names[]` |  `string` Optional. Specifies the KMS configuration for the one or more keys used to protect the backup. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`. KMS keys specified can be in any order.The keys referenced by `kms_key_names` must fully cover all regions of the backup's instance configuration. Some examples:

  * For regional (single-region) instance configurations, specify a regional location KMS key.
  * For multi-region instance configurations of type `GOOGLE_MANAGED`, either specify a multi-region location KMS key or multiple regional location KMS keys that cover all regions in the instance configuration.
  * For an instance configuration of type `USER_MANAGED`, specify only regional location KMS keys to cover each region in the instance configuration. Multi-region location KMS keys aren't supported for `USER_MANAGED` type instance configurations.

  
  
## EncryptionType

Encryption types for the backup.

Enums  
---  
`ENCRYPTION_TYPE_UNSPECIFIED` | Unspecified. Do not use.  
`USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION` | This is the default option for `[CopyBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CopyBackup)` when `[encryption_config](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupEncryptionConfig)` is not specified. For example, if the source backup is using `Customer_Managed_Encryption`, the backup will be using the same Cloud KMS key as the source backup.  
`GOOGLE_DEFAULT_ENCRYPTION` | Use Google default encryption.  
`CUSTOMER_MANAGED_ENCRYPTION` | Use customer managed encryption. If specified, either `kms_key_name` or `kms_key_names` must contain valid Cloud KMS keys.  
  
## CopyBackupMetadata

Metadata type for the operation returned by `[CopyBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CopyBackup)`.

Fields  
---  
`name` |  `string` The name of the backup being created through the copy operation. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`.  
`source_backup` |  `string` The name of the source backup that is being copied. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`.  
`progress` |  `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` The progress of the `[CopyBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CopyBackup)` operation.  
`cancel_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which cancellation of CopyBackup operation was received. `[Operations.CancelOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)` starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use `[Operations.GetOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an `[Operation.error](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
  
## CopyBackupRequest

The request for `[CopyBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CopyBackup)`.

Fields  
---  
`parent` |  `string` Required. The name of the destination instance that will contain the backup copy. Values are of the form: `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.backups.create`

  
`backup_id` |  `string` Required. The id of the backup copy. The `backup_id` appended to `parent` forms the full backup_uri of the form `projects/<project>/instances/<instance>/backups/<backup>`.  
`source_backup` |  `string` Required. The source backup to be copied. The source backup needs to be in READY state for it to be copied. Once CopyBackup is in progress, the source backup cannot be deleted or cleaned up on expiration until CopyBackup is finished. Values are of the form: `projects/<project>/instances/<instance>/backups/<backup>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `sourceBackup`:

  * `spanner.backups.copy`

  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Required. The expiration time of the backup in microsecond granularity. The expiration time must be at least 6 hours and at most 366 days from the `create_time` of the source backup. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup.  
`encryption_config` |  `[CopyBackupEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupEncryptionConfig)` Optional. The encryption configuration used to encrypt the backup. If this field is not specified, the backup will use the same encryption configuration as the source backup by default, namely `[encryption_type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupEncryptionConfig.FIELDS.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.EncryptionType.google.spanner.admin.database.v1.CopyBackupEncryptionConfig.encryption_type)` = `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`.  
  
## CreateBackupEncryptionConfig

Encryption configuration for the backup to create.

Fields  
---  
`encryption_type` |  `[EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig.EncryptionType)` Required. The encryption type of the backup.  
`kms_key_name` |  `string` Optional. This field is maintained for backwards compatibility. For new callers, we recommend using `kms_key_names` to specify the KMS key. Only use `kms_key_name` if the location of the KMS key matches the database instance's configuration (location) exactly. For example, if the KMS location is in `us-central1` or `nam3`, then the database instance must also be in `us-central1` or `nam3`.The Cloud KMS key that is used to encrypt and decrypt the restored database. Set this field only when `[encryption_type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig.FIELDS.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.EncryptionType.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.encryption_type)` is `CUSTOMER_MANAGED_ENCRYPTION`. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.  
`kms_key_names[]` |  `string` Optional. Specifies the KMS configuration for the one or more keys used to protect the backup. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.The keys referenced by `kms_key_names` must fully cover all regions of the backup's instance configuration. Some examples:

  * For regional (single-region) instance configurations, specify a regional location KMS key.
  * For multi-region instance configurations of type `GOOGLE_MANAGED`, either specify a multi-region location KMS key or multiple regional location KMS keys that cover all regions in the instance configuration.
  * For an instance configuration of type `USER_MANAGED`, specify only regional location KMS keys to cover each region in the instance configuration. Multi-region location KMS keys aren't supported for `USER_MANAGED` type instance configurations.

  
  
## EncryptionType

Encryption types for the backup.

Enums  
---  
`ENCRYPTION_TYPE_UNSPECIFIED` | Unspecified. Do not use.  
`USE_DATABASE_ENCRYPTION` | Use the same encryption configuration as the database. This is the default option when `[encryption_config](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig)` is empty. For example, if the database is using `Customer_Managed_Encryption`, the backup will be using the same Cloud KMS key as the database.  
`GOOGLE_DEFAULT_ENCRYPTION` | Use Google default encryption.  
`CUSTOMER_MANAGED_ENCRYPTION` | Use customer managed encryption. If specified, `kms_key_name` must contain a valid Cloud KMS key.  
  
## CreateBackupMetadata

Metadata type for the operation returned by `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)`.

Fields  
---  
`name` |  `string` The name of the backup being created.  
`database` |  `string` The name of the database the backup is created from.  
`progress` |  `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` The progress of the `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)` operation.  
`cancel_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which cancellation of this operation was received. `[Operations.CancelOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)` starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use `[Operations.GetOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an `[Operation.error](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation.FIELDS.google.rpc.Status.google.longrunning.Operation.error)` value with a `[google.rpc.Status.code](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
  
## CreateBackupRequest

The request for `[CreateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup)`.

Fields  
---  
`parent` |  `string` Required. The name of the instance in which the backup is created. This must be the same instance that contains the database the backup is created from. The backup will be stored in the locations specified in the instance configuration of this instance. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.backups.create`

  
`backup_id` |  `string` Required. The id of the backup to be created. The `backup_id` appended to `parent` forms the full backup name of the form `projects/<project>/instances/<instance>/backups/<backup_id>`.  
`backup` |  `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)` Required. The backup to create.  
`encryption_config` |  `[CreateBackupEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig)` Optional. The encryption configuration used to encrypt the backup. If this field is not specified, the backup will use the same encryption configuration as the database by default, namely `[encryption_type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupEncryptionConfig.FIELDS.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.EncryptionType.google.spanner.admin.database.v1.CreateBackupEncryptionConfig.encryption_type)` = `USE_DATABASE_ENCRYPTION`.  
  
## CreateBackupScheduleRequest

The request for `[CreateBackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateBackupSchedule)`.

Fields  
---  
`parent` |  `string` Required. The name of the database that this backup schedule applies to. Authorization requires one or more of the following [IAM](https://cloud.google.com/iam/docs/) permissions on the specified resource `parent`:

  * `spanner.backupSchedules.create`
  * `spanner.databases.createBackup`

  
`backup_schedule_id` |  `string` Required. The Id to use for the backup schedule. The `backup_schedule_id` appended to `parent` forms the full backup schedule name of the form `projects/<project>/instances/<instance>/databases/<database>/backupSchedules/<backup_schedule_id>`.  
`backup_schedule` |  `[BackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupSchedule)` Required. The backup schedule to create.  
  
## CreateDatabaseMetadata

Metadata type for the operation returned by `[CreateDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateDatabase)`.

Fields  
---  
`database` |  `string` The database being created.  
  
## CreateDatabaseRequest

The request for `[CreateDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.CreateDatabase)`.

Fields  
---  
`parent` |  `string` Required. The name of the instance that will serve the new database. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databases.create`

  
`create_statement` |  `string` Required. A `CREATE DATABASE` statement, which specifies the ID of the new database. The database ID must conform to the regular expression `[a-z][a-z0-9_\-]*[a-z0-9]` and be between 2 and 30 characters in length. If the database ID is a reserved word or if it contains a hyphen, the database ID must be enclosed in backticks (```).  
`extra_statements[]` |  `string` Optional. A list of DDL statements to run inside the newly created database. Statements can create tables, indexes, etc. These statements execute atomically with the creation of the database: if there is an error in any statement, the database is not created.  
`encryption_config` |  `[EncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionConfig)` Optional. The encryption configuration for the database. If this field is not specified, Cloud Spanner will encrypt/decrypt all data at rest using Google default encryption.  
`database_dialect` |  `[DatabaseDialect](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseDialect)` Optional. The dialect of the Cloud Spanner Database.  
`proto_descriptors` |  `bytes` Optional. Proto descriptors used by `CREATE/ALTER PROTO BUNDLE` statements in 'extra_statements'. Contains a protobuf-serialized [`google.protobuf.FileDescriptorSet`](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto) descriptor set. To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run
    
    
    $protoc  --proto_path=/app_path --proto_path=/lib_path \
             --include_imports \
             --descriptor_set_out=descriptors.data \
             moon/shot/app.proto
    

For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).  
  
## CrontabSpec

CrontabSpec can be used to specify the version time and frequency at which the backup is created.

Fields  
---  
`text` |  `string` Required. Textual representation of the crontab. User can customize the backup frequency and the backup version time using the cron expression. The version time must be in UTC timezone. The backup will contain an externally consistent copy of the database at the version time.Full backups must be scheduled a minimum of 12 hours apart and incremental backups must be scheduled a minimum of 4 hours apart. Examples of valid cron specifications:

  * `0 2/12 * * *` : every 12 hours at (2, 14) hours past midnight in UTC.
  * `0 2,14 * * *` : every 12 hours at (2, 14) hours past midnight in UTC.
  * `0 */4 * * *` : (incremental backups only) every 4 hours at (0, 4, 8, 12, 16, 20) hours past midnight in UTC.
  * `0 2 * * *` : once a day at 2 past midnight in UTC.
  * `0 2 * * 0` : once a week every Sunday at 2 past midnight in UTC.
  * `0 2 8 * *` : once a month on 8th day at 2 past midnight in UTC.

  
`time_zone` |  `string` Output only. The time zone of the times in `CrontabSpec.text`. Currently, only UTC is supported.  
`creation_window` |  `[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` Output only. Scheduled backups contain an externally consistent copy of the database at the version time specified in `schedule_spec.cron_spec`. However, Spanner might not initiate the creation of the scheduled backups at that version time. Spanner initiates the creation of scheduled backups within the time window bounded by the version_time specified in `schedule_spec.cron_spec` and version_time + `creation_window`.  
  
## Database

A Cloud Spanner database.

Fields  
---  
`name` |  `string` Required. The name of the database. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`, where `<database>` is as specified in the `CREATE DATABASE` statement. This name can be passed to other API methods to identify the database.  
`state` |  `[State](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database.State)` Output only. The current database state.  
`create_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. If exists, the time at which the database creation started.  
`restore_info` |  `[RestoreInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreInfo)` Output only. Applicable only for restored databases. Contains information about the restore source.  
`encryption_config` |  `[EncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionConfig)` Output only. For databases that are using customer managed encryption, this field contains the encryption configuration for the database. For databases that are using Google default or other types of encryption, this field is empty.  
`encryption_info[]` |  `[EncryptionInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionInfo)` Output only. For databases that are using customer managed encryption, this field contains the encryption information for the database, such as all Cloud KMS key versions that are in use. The `encryption_status` field inside of each `EncryptionInfo` is not populated.For databases that are using Google default or other types of encryption, this field is empty.This field is propagated lazily from the backend. There might be a delay from when a key version is being used and when it appears in this field.  
`version_retention_period` |  `string` Output only. The period in which Cloud Spanner retains all versions of data for the database. This is the same as the value of version_retention_period database option set using `[UpdateDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)`. Defaults to 1 hour, if not set.  
`earliest_version_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. Earliest timestamp at which older versions of the data can be read. This value is continuously updated by Cloud Spanner and becomes stale the moment it is queried. If you are using this value to recover data, make sure to account for the time from the moment when the value is queried to the moment when you initiate the recovery.  
`default_leader` |  `string` Output only. The read-write region which contains the database's leader replicas.This is the same as the value of default_leader database option set using DatabaseAdmin.CreateDatabase or DatabaseAdmin.UpdateDatabaseDdl. If not explicitly set, this is empty.  
`database_dialect` |  `[DatabaseDialect](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseDialect)` Output only. The dialect of the Cloud Spanner Database.  
`enable_drop_protection` |  `bool` Optional. Whether drop protection is enabled for this database. Defaults to false, if not set. For more details, please see how to [prevent accidental database deletion](https://cloud.google.com/spanner/docs/prevent-database-deletion).  
`reconciling` |  `bool` Output only. If true, the database is being updated. If false, there are no ongoing update operations for the database.  
`quorum_info` |  `[QuorumInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumInfo)` Output only. Applicable only for databases that use dual-region instance configurations. Contains information about the quorum.  
  
## State

Indicates the current state of the database.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified.  
`CREATING` | The database is still being created. Operations on the database may fail with `FAILED_PRECONDITION` in this state.  
`READY` | The database is fully created and ready for use.  
`READY_OPTIMIZING` | The database is fully created and ready for use, but is still being optimized for performance and cannot handle full load.In this state, the database still references the backup it was restore from, preventing the backup from being deleted. When optimizations are complete, the full performance of the database will be restored, and the database will transition to `READY` state.  
  
## DatabaseDialect

Indicates the dialect type of a database.

Enums  
---  
`DATABASE_DIALECT_UNSPECIFIED` | Default value. This value will create a database with the GOOGLE_STANDARD_SQL dialect.  
`GOOGLE_STANDARD_SQL` | GoogleSQL supported SQL.  
`POSTGRESQL` | PostgreSQL supported SQL.  
  
## DatabaseRole

A Cloud Spanner database role.

Fields  
---  
`name` |  `string` Required. The name of the database role. Values are of the form `projects/<project>/instances/<instance>/databases/<database>/databaseRoles/<role>` where `<role>` is as specified in the `CREATE ROLE` DDL statement.  
  
## DdlStatementActionInfo

Action information extracted from a DDL statement. This proto is used to display the brief info of the DDL statement for the operation `[UpdateDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)`.

Fields  
---  
`action` |  `string` The action for the DDL statement, for example, CREATE, ALTER, DROP, GRANT, etc. This field is a non-empty string.  
`entity_type` |  `string` The entity type for the DDL statement, for example, TABLE, INDEX, VIEW, etc. This field can be empty string for some DDL statement, for example, for statement "ANALYZE", `entity_type` = "".  
`entity_names[]` |  `string` The entity names being operated on the DDL statement. For example, 1. For statement "CREATE TABLE t1(...)", `entity_names` = ["t1"]. 2. For statement "GRANT ROLE r1, r2 ...", `entity_names` = ["r1", "r2"]. 3. For statement "ANALYZE", `entity_names` = [].  
  
## DeleteBackupRequest

The request for `[DeleteBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.DeleteBackup)`.

Fields  
---  
`name` |  `string` Required. Name of the backup to delete. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.backups.delete`

  
  
## DeleteBackupScheduleRequest

The request for `[DeleteBackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.DeleteBackupSchedule)`.

Fields  
---  
`name` |  `string` Required. The name of the schedule to delete. Values are of the form `projects/<project>/instances/<instance>/databases/<database>/backupSchedules/<backup_schedule_id>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.backupSchedules.delete`

  
  
## DropDatabaseRequest

The request for `[DropDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.DropDatabase)`.

Fields  
---  
`database` |  `string` Required. The database to be dropped. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.drop`

  
  
## EncryptionConfig

Encryption configuration for a Cloud Spanner database.

Fields  
---  
`kms_key_name` |  `string` The Cloud KMS key to be used for encrypting and decrypting the database. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.  
`kms_key_names[]` |  `string` Specifies the KMS configuration for one or more keys used to encrypt the database. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.The keys referenced by `kms_key_names` must fully cover all regions of the database's instance configuration. Some examples:

  * For regional (single-region) instance configurations, specify a regional location KMS key.
  * For multi-region instance configurations of type `GOOGLE_MANAGED`, either specify a multi-region location KMS key or multiple regional location KMS keys that cover all regions in the instance configuration.
  * For an instance configuration of type `USER_MANAGED`, specify only regional location KMS keys to cover each region in the instance configuration. Multi-region location KMS keys aren't supported for `USER_MANAGED` type instance configurations.

  
  
## EncryptionInfo

Encryption information for a Cloud Spanner database or backup.

Fields  
---  
`encryption_type` |  `[Type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.EncryptionInfo.Type)` Output only. The type of encryption.  
`encryption_status` |  `[Status](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.rpc#google.rpc.Status)` Output only. If present, the status of a recent encrypt/decrypt call on underlying data for this database or backup. Regardless of status, data is always encrypted at rest.  
`kms_key_version` |  `string` Output only. A Cloud KMS key version that is being used to protect the database or backup.  
  
## Type

Possible encryption types.

Enums  
---  
`TYPE_UNSPECIFIED` | Encryption type was not specified, though data at rest remains encrypted.  
`GOOGLE_DEFAULT_ENCRYPTION` | The data is encrypted at rest with a key that is fully managed by Google. No key version or status will be populated. This is the default state.  
`CUSTOMER_MANAGED_ENCRYPTION` | The data is encrypted at rest with a key that is managed by the customer. The active version of the key. `kms_key_version` will be populated, and `encryption_status` may be populated.  
  
## FullBackupSpec

This type has no fields.

The specification for full backups. A full backup stores the entire contents of the database at a given version time.

## GetBackupRequest

The request for `[GetBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetBackup)`.

Fields  
---  
`name` |  `string` Required. Name of the backup. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.backups.get`

  
  
## GetBackupScheduleRequest

The request for `[GetBackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetBackupSchedule)`.

Fields  
---  
`name` |  `string` Required. The name of the schedule to retrieve. Values are of the form `projects/<project>/instances/<instance>/databases/<database>/backupSchedules/<backup_schedule_id>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.backupSchedules.get`

  
  
## GetDatabaseDdlRequest

The request for `[GetDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDdl)`.

Fields  
---  
`database` |  `string` Required. The database whose schema we wish to get. Values are of the form `projects/<project>/instances/<instance>/databases/<database>` Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.getDdl`

  
  
## GetDatabaseDdlResponse

The response for `[GetDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDdl)`.

Fields  
---  
`statements[]` |  `string` A list of formatted DDL statements defining the schema of the database specified in the request.  
`proto_descriptors` |  `bytes` Proto descriptors stored in the database. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).  
  
## GetDatabaseRequest

The request for `[GetDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.GetDatabase)`.

Fields  
---  
`name` |  `string` Required. The name of the requested database. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `name`:

  * `spanner.databases.get`

  
  
## IncrementalBackupSpec

This type has no fields.

The specification for incremental backup chains. An incremental backup stores the delta of changes between a previous backup and the database contents at a given version time. An incremental backup chain consists of a full backup and zero or more successive incremental backups. The first backup created for an incremental backup chain is always a full backup.

## ListBackupOperationsRequest

The request for `[ListBackupOperations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations)`.

Fields  
---  
`parent` |  `string` Required. The instance of the backup operations. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.backupOperations.list`

  
`filter` |  `string` An expression that filters the list of returned backup operations.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the operation are eligible for filtering:

  * `name` \- The name of the long-running operation
  * `done` \- False if the operation is in progress, else true.
  * `metadata.@type` \- the type of metadata. For example, the type string for `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupMetadata)` is `type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata`.
  * `metadata.<field_name>` \- any field in metadata.value. `metadata.@type` must be specified first if filtering on metadata fields.
  * `error` \- Error associated with the long-running operation.
  * `response.@type` \- the type of response.
  * `response.<field_name>` \- any field in response.value.

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly.Here are a few examples:

  * `done:true` \- The operation is complete.
  * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `metadata.database:prod` \- Returns operations where: 
    * The operation's metadata type is `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupMetadata)`.
    * The source database name of backup contains the string "prod".
  * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.name:howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: 
    * The operation's metadata type is `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupMetadata)`.
    * The backup name contains the string "howl".
    * The operation started before 2018-03-28T14:50:00Z.
    * The operation resulted in an error.
  * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test) AND` \ `(metadata.progress.start_time < \"2022-01-18T14:50:00Z\") AND` \ `(error:*)` \- Returns operations where: 
    * The operation's metadata type is `[CopyBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupMetadata)`.
    * The source backup name contains the string "test".
    * The operation started before 2022-01-18T14:50:00Z.
    * The operation resulted in an error.
  * `((metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CreateBackupMetadata) AND` \ `(metadata.database:test_db)) OR` \ `((metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.CopyBackupMetadata) AND` \ `(metadata.source_backup:test_bkp)) AND` \ `(error:*)` \- Returns operations where: 
    * The operation's metadata matches either of criteria:
    * The operation's metadata type is `[CreateBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CreateBackupMetadata)` AND the source database name of the backup contains the string "test_db"
    * The operation's metadata type is `[CopyBackupMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.CopyBackupMetadata)` AND the source backup name contains the string "test_bkp"
    * The operation resulted in an error.

  
`page_size` |  `int32` Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`page_token` |  `string` If non-empty, `page_token` should contain a `[next_page_token](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupOperationsResponse.FIELDS.string.google.spanner.admin.database.v1.ListBackupOperationsResponse.next_page_token)` from a previous `[ListBackupOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupOperationsResponse)` to the same `parent` and with the same `filter`.  
  
## ListBackupOperationsResponse

The response for `[ListBackupOperations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations)`.

Fields  
---  
`operations[]` |  `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` The list of matching backup long-running operations. Each operation's name will be prefixed by the backup's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata. Operations returned include those that are pending or have completed/failed/canceled within the last 7 days. Operations returned are ordered by `operation.metadata.value.progress.start_time` in descending order starting from the most recently started operation.  
`next_page_token` |  `string` `next_page_token` can be sent in a subsequent `[ListBackupOperations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations)` call to fetch more of the matching metadata.  
  
## ListBackupSchedulesRequest

The request for `[ListBackupSchedules](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupSchedules)`.

Fields  
---  
`parent` |  `string` Required. Database is the parent resource whose backup schedules should be listed. Values are of the form projects//instances//databases/ Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.backupSchedules.list`

  
`page_size` |  `int32` Optional. Number of backup schedules to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`page_token` |  `string` Optional. If non-empty, `page_token` should contain a `[next_page_token](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupSchedulesResponse.FIELDS.string.google.spanner.admin.database.v1.ListBackupSchedulesResponse.next_page_token)` from a previous `[ListBackupSchedulesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupSchedulesResponse)` to the same `parent`.  
  
## ListBackupSchedulesResponse

The response for `[ListBackupSchedules](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupSchedules)`.

Fields  
---  
`backup_schedules[]` |  `[BackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupSchedule)` The list of backup schedules for a database.  
`next_page_token` |  `string` `next_page_token` can be sent in a subsequent `[ListBackupSchedules](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackupSchedules)` call to fetch more of the schedules.  
  
## ListBackupsRequest

The request for `[ListBackups](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackups)`.

Fields  
---  
`parent` |  `string` Required. The instance to list backups from. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.backups.list`

  
`filter` |  `string` An expression that filters the list of returned backups.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)` are eligible for filtering:

  * `name`
  * `database`
  * `state`
  * `create_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `expire_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `version_time` (and values are of the format YYYY-MM-DDTHH:MM:SSZ)
  * `size_bytes`
  * `backup_schedules`

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic, but you can specify AND, OR, and NOT logic explicitly.Here are a few examples:

  * `name:Howl` \- The backup's name contains the string "howl".
  * `database:prod` \- The database's name contains the string "prod".
  * `state:CREATING` \- The backup is pending creation.
  * `state:READY` \- The backup is fully created and ready for use.
  * `(name:howl) AND (create_time < \"2018-03-28T14:50:00Z\")` \- The backup name contains the string "howl" and `create_time` of the backup is before 2018-03-28T14:50:00Z.
  * `expire_time < \"2018-03-28T14:50:00Z\"` \- The backup `expire_time` is before 2018-03-28T14:50:00Z.
  * `size_bytes > 10000000000` \- The backup's size is greater than 10GB
  * `backup_schedules:daily` \- The backup is created from a schedule with "daily" in its name.

  
`page_size` |  `int32` Number of backups to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`page_token` |  `string` If non-empty, `page_token` should contain a `[next_page_token](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupsResponse.FIELDS.string.google.spanner.admin.database.v1.ListBackupsResponse.next_page_token)` from a previous `[ListBackupsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListBackupsResponse)` to the same `parent` and with the same `filter`.  
  
## ListBackupsResponse

The response for `[ListBackups](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackups)`.

Fields  
---  
`backups[]` |  `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)` The list of matching backups. Backups returned are ordered by `create_time` in descending order, starting from the most recent `create_time`.  
`next_page_token` |  `string` `next_page_token` can be sent in a subsequent `[ListBackups](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListBackups)` call to fetch more of the matching backups.  
  
## ListDatabaseOperationsRequest

The request for `[ListDatabaseOperations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseOperations)`.

Fields  
---  
`parent` |  `string` Required. The instance of the database operations. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databaseOperations.list`

  
`filter` |  `string` An expression that filters the list of returned operations.A filter expression consists of a field name, a comparison operator, and a value for filtering. The value must be a string, a number, or a boolean. The comparison operator must be one of: `<`, `>`, `<=`, `>=`, `!=`, `=`, or `:`. Colon `:` is the contains operator. Filter rules are not case sensitive.The following fields in the operation are eligible for filtering:

  * `name` \- The name of the long-running operation
  * `done` \- False if the operation is in progress, else true.
  * `metadata.@type` \- the type of metadata. For example, the type string for `[RestoreDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseMetadata)` is `type.googleapis.com/google.spanner.admin.database.v1.RestoreDatabaseMetadata`.
  * `metadata.<field_name>` \- any field in metadata.value. `metadata.@type` must be specified first, if filtering on metadata fields.
  * `error` \- Error associated with the long-running operation.
  * `response.@type` \- the type of response.
  * `response.<field_name>` \- any field in response.value.

You can combine multiple expressions by enclosing each expression in parentheses. By default, expressions are combined with AND logic. However, you can specify AND, OR, and NOT logic explicitly.Here are a few examples:

  * `done:true` \- The operation is complete.
  * `(metadata.@type=type.googleapis.com/google.spanner.admin.database.v1.RestoreDatabaseMetadata) AND` \ `(metadata.source_type:BACKUP) AND` \ `(metadata.backup_info.backup:backup_howl) AND` \ `(metadata.name:restored_howl) AND` \ `(metadata.progress.start_time < \"2018-03-28T14:50:00Z\") AND` \ `(error:*)` \- Return operations where: 
    * The operation's metadata type is `[RestoreDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseMetadata)`.
    * The database is restored from a backup.
    * The backup name contains "backup_howl".
    * The restored database's name contains "restored_howl".
    * The operation started before 2018-03-28T14:50:00Z.
    * The operation resulted in an error.

  
`page_size` |  `int32` Number of operations to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`page_token` |  `string` If non-empty, `page_token` should contain a `[next_page_token](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseOperationsResponse.FIELDS.string.google.spanner.admin.database.v1.ListDatabaseOperationsResponse.next_page_token)` from a previous `[ListDatabaseOperationsResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseOperationsResponse)` to the same `parent` and with the same `filter`.  
  
## ListDatabaseOperationsResponse

The response for `[ListDatabaseOperations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseOperations)`.

Fields  
---  
`operations[]` |  `[Operation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operation)` The list of matching database long-running operations. Each operation's name will be prefixed by the database's name. The operation's metadata field type `metadata.type_url` describes the type of the metadata.  
`next_page_token` |  `string` `next_page_token` can be sent in a subsequent `[ListDatabaseOperations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseOperations)` call to fetch more of the matching metadata.  
  
## ListDatabaseRolesRequest

The request for `[ListDatabaseRoles](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseRoles)`.

Fields  
---  
`parent` |  `string` Required. The database whose roles should be listed. Values are of the form `projects/<project>/instances/<instance>/databases/<database>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databasesRoles.list`

  
`page_size` |  `int32` Number of database roles to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`page_token` |  `string` If non-empty, `page_token` should contain a `[next_page_token](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseRolesResponse.FIELDS.string.google.spanner.admin.database.v1.ListDatabaseRolesResponse.next_page_token)` from a previous `[ListDatabaseRolesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabaseRolesResponse)`.  
  
## ListDatabaseRolesResponse

The response for `[ListDatabaseRoles](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseRoles)`.

Fields  
---  
`database_roles[]` |  `[DatabaseRole](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseRole)` Database roles that matched the request.  
`next_page_token` |  `string` `next_page_token` can be sent in a subsequent `[ListDatabaseRoles](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseRoles)` call to fetch more of the matching roles.  
  
## ListDatabasesRequest

The request for `[ListDatabases](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases)`.

Fields  
---  
`parent` |  `string` Required. The instance whose databases should be listed. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databases.list`

  
`page_size` |  `int32` Number of databases to be returned in the response. If 0 or less, defaults to the server's maximum allowed page size.  
`page_token` |  `string` If non-empty, `page_token` should contain a `[next_page_token](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabasesResponse.FIELDS.string.google.spanner.admin.database.v1.ListDatabasesResponse.next_page_token)` from a previous `[ListDatabasesResponse](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.ListDatabasesResponse)`.  
  
## ListDatabasesResponse

The response for `[ListDatabases](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases)`.

Fields  
---  
`databases[]` |  `[Database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database)` Databases that matched the request.  
`next_page_token` |  `string` `next_page_token` can be sent in a subsequent `[ListDatabases](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases)` call to fetch more of the matching databases.  
  
## OperationProgress

Encapsulates progress related information for a Cloud Spanner long running operation.

Fields  
---  
`progress_percent` |  `int32` Percent completion of the operation. Values are between 0 and 100 inclusive.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Time the request was received.  
`end_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` If set, the time at which this operation failed or was completed successfully.  
  
## OptimizeRestoredDatabaseMetadata

Metadata type for the long-running operation used to track the progress of optimizations performed on a newly restored database. This long-running operation is automatically created by the system after the successful completion of a database restore, and cannot be cancelled.

Fields  
---  
`name` |  `string` Name of the restored database being optimized.  
`progress` |  `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` The progress of the post-restore optimizations.  
  
## QuorumInfo

Information about the dual-region quorum.

Fields  
---  
`quorum_type` |  `[QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType)` Output only. The type of this quorum. See `[QuorumType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType)` for more information about quorum type specifications.  
`initiator` |  `[Initiator](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumInfo.Initiator)` Output only. Whether this `ChangeQuorum` is Google or User initiated.  
`start_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Output only. The timestamp when the request was triggered.  
`etag` |  `string` Output only. The etag is used for optimistic concurrency control as a way to help prevent simultaneous `ChangeQuorum` requests that might create a race condition.  
  
## Initiator

Describes who initiated `ChangeQuorum`.

Enums  
---  
`INITIATOR_UNSPECIFIED` | Unspecified.  
`GOOGLE` | `ChangeQuorum` initiated by Google.  
`USER` | `ChangeQuorum` initiated by User.  
  
## QuorumType

Information about the database quorum type. This only applies to dual-region instance configs.

Fields  
---  
Union field `type`. The type of quorum. `type` can be only one of the following:  
`single_region` |  `[SingleRegionQuorum](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType.SingleRegionQuorum)` Single-region quorum type.  
`dual_region` |  `[DualRegionQuorum](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.QuorumType.DualRegionQuorum)` Dual-region quorum type.  
  
## DualRegionQuorum

This type has no fields.

Message type for a dual-region quorum. Currently this type has no options.

## SingleRegionQuorum

Message type for a single-region quorum.

Fields  
---  
`serving_location` |  `string` Required. The location of the serving region, for example, "us-central1". The location must be one of the regions within the dual-region instance configuration of your database. The list of valid locations is available using the [GetInstanceConfig][InstanceAdmin.GetInstanceConfig] API.This should only be used if you plan to change quorum to the single-region quorum type.  
  
## RestoreDatabaseEncryptionConfig

Encryption configuration for the restored database.

Fields  
---  
`encryption_type` |  `[EncryptionType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.EncryptionType)` Required. The encryption type of the restored database.  
`kms_key_name` |  `string` Optional. This field is maintained for backwards compatibility. For new callers, we recommend using `kms_key_names` to specify the KMS key. Only use `kms_key_name` if the location of the KMS key matches the database instance's configuration (location) exactly. For example, if the KMS location is in `us-central1` or `nam3`, then the database instance must also be in `us-central1` or `nam3`.The Cloud KMS key that is used to encrypt and decrypt the restored database. Set this field only when `[encryption_type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.FIELDS.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.EncryptionType.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.encryption_type)` is `CUSTOMER_MANAGED_ENCRYPTION`. Values are of the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.  
`kms_key_names[]` |  `string` Optional. Specifies the KMS configuration for one or more keys used to encrypt the database. Values have the form `projects/<project>/locations/<location>/keyRings/<key_ring>/cryptoKeys/<kms_key_name>`.The keys referenced by `kms_key_names` must fully cover all regions of the database's instance configuration. Some examples:

  * For regional (single-region) instance configurations, specify a regional location KMS key.
  * For multi-region instance configurations of type `GOOGLE_MANAGED`, either specify a multi-region location KMS key or multiple regional location KMS keys that cover all regions in the instance configuration.
  * For an instance configuration of type `USER_MANAGED`, specify only regional location KMS keys to cover each region in the instance configuration. Multi-region location KMS keys aren't supported for `USER_MANAGED` type instance configurations.

  
  
## EncryptionType

Encryption types for the database to be restored.

Enums  
---  
`ENCRYPTION_TYPE_UNSPECIFIED` | Unspecified. Do not use.  
`USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION` | This is the default option when `[encryption_config](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig)` is not specified.  
`GOOGLE_DEFAULT_ENCRYPTION` | Use Google default encryption.  
`CUSTOMER_MANAGED_ENCRYPTION` | Use customer managed encryption. If specified, `kms_key_name` must must contain a valid Cloud KMS key.  
  
## RestoreDatabaseMetadata

Metadata type for the long-running operation returned by `[RestoreDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase)`.

Fields  
---  
`name` |  `string` Name of the database being created and restored to.  
`source_type` |  `[RestoreSourceType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreSourceType)` The type of the restore source.  
`progress` |  `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` The progress of the `[RestoreDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase)` operation.  
`cancel_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which cancellation of this operation was received. `[Operations.CancelOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.CancelOperation)` starts asynchronous cancellation on a long-running operation. The server makes a best effort to cancel the operation, but success is not guaranteed. Clients can use `[Operations.GetOperation](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations.GetOperation)` or other methods to check whether the cancellation succeeded or whether the operation completed despite cancellation. On successful cancellation, the operation is not deleted; instead, it becomes an operation with an Operation.error value with a `[google.rpc.Status.code](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.rpc#google.rpc.Status.FIELDS.int32.google.rpc.Status.code)` of 1, corresponding to `Code.CANCELLED`.  
`optimize_database_operation_name` |  `string` If exists, the name of the long-running operation that will be used to track the post-restore optimization process to optimize the performance of the restored database, and remove the dependency on the restore source. The name is of the form `projects/<project>/instances/<instance>/databases/<database>/operations/<operation>` where the  is the name of database being created and restored to. The metadata type of the long-running operation is `[OptimizeRestoredDatabaseMetadata](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OptimizeRestoredDatabaseMetadata)`. This long-running operation will be automatically created by the system after the RestoreDatabase long-running operation completes successfully. This operation will not be created if the restore was not successful.  
Union field `source_info`. Information about the source used to restore the database, as specified by `source` in `[RestoreDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseRequest)`. `source_info` can be only one of the following:  
`backup_info` |  `[BackupInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupInfo)` Information about the backup used to restore the database.  
  
## RestoreDatabaseRequest

The request for `[RestoreDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase)`.

Fields  
---  
`parent` |  `string` Required. The name of the instance in which to create the restored database. This instance must be in the same project and have the same instance configuration as the instance containing the source backup. Values are of the form `projects/<project>/instances/<instance>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `parent`:

  * `spanner.databases.create`

  
`database_id` |  `string` Required. The id of the database to create and restore to. This database must not already exist. The `database_id` appended to `parent` forms the full database name of the form `projects/<project>/instances/<instance>/databases/<database_id>`.  
`encryption_config` |  `[RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig)` Optional. An encryption configuration describing the encryption type and key resources in Cloud KMS used to encrypt/decrypt the database to restore to. If this field is not specified, the restored database will use the same encryption configuration as the backup by default, namely `[encryption_type](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.FIELDS.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.EncryptionType.google.spanner.admin.database.v1.RestoreDatabaseEncryptionConfig.encryption_type)` = `USE_CONFIG_DEFAULT_OR_BACKUP_ENCRYPTION`.  
Union field `source`. Required. The source from which to restore. `source` can be only one of the following:  
`backup` |  `string` Name of the backup from which to restore. Values are of the form `projects/<project>/instances/<instance>/backups/<backup>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `backup`:

  * `spanner.backups.restoreDatabase`

  
  
## RestoreInfo

Information about the database restore.

Fields  
---  
`source_type` |  `[RestoreSourceType](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.RestoreSourceType)` The type of the restore source.  
Union field `source_info`. Information about the source used to restore the database. `source_info` can be only one of the following:  
`backup_info` |  `[BackupInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupInfo)` Information about the backup used to restore the database. The backup may no longer exist.  
  
## RestoreSourceType

Indicates the type of the restore source.

Enums  
---  
`TYPE_UNSPECIFIED` | No restore associated.  
`BACKUP` | A backup was used as the source of the restore.  
  
## SplitPoints

The split points of a table or an index.

Fields  
---  
`table` |  `string` The table to split.  
`index` |  `string` The index to split. If specified, the `table` field must refer to the index's base table.  
`keys[]` |  `[Key](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.SplitPoints.Key)` Required. The list of split keys. In essence, the split boundaries.  
`expire_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Optional. The expiration timestamp of the split points. A timestamp in the past means immediate expiration. The maximum value can be 30 days in the future. Defaults to 10 days in the future if not specified.  
  
## Key

A split key.

Fields  
---  
`key_parts` |  `[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` Required. The column values making up the split key.  
  
## UpdateBackupRequest

The request for `[UpdateBackup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackup)`.

Fields  
---  
`backup` |  `[Backup](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Backup)` Required. The backup to update. `backup.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. Update is only supported for the following fields: * `backup.expire_time`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `backup`:

  * `spanner.backups.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. A mask specifying which fields (for example, `expire_time`) in the backup resource should be updated. This mask is relative to the backup resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally by clients that do not know about them.  
  
## UpdateBackupScheduleRequest

The request for `[UpdateBackupScheduleRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackupSchedule)`.

Fields  
---  
`backup_schedule` |  `[BackupSchedule](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.BackupSchedule)` Required. The backup schedule to update. `backup_schedule.name`, and the fields to be updated as specified by `update_mask` are required. Other fields are ignored. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `backupSchedule`:

  * `spanner.backupSchedules.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. A mask specifying which fields in the BackupSchedule resource should be updated. This mask is relative to the BackupSchedule resource, not to the request message. The field mask must always be specified; this prevents any future fields from being erased accidentally.  
  
## UpdateDatabaseDdlMetadata

Metadata type for the operation returned by `[UpdateDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)`.

Fields  
---  
`database` |  `string` The database being modified.  
`statements[]` |  `string` For an update this list contains all the statements. For an individual statement, this list contains only that statement.  
`commit_timestamps[]` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` Reports the commit timestamps of all statements that have succeeded so far, where `commit_timestamps[i]` is the commit timestamp for the statement `statements[i]`.  
`throttled` |  `bool` Output only. When true, indicates that the operation is throttled, for example, due to resource constraints. When resources become available the operation will resume and this field will be false again.  
`progress[]` |  `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` The progress of the `[UpdateDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)` operations. All DDL statements will have continuously updating progress, and `progress[i]` is the operation progress for `statements[i]`. Also, `progress[i]` will have start time and end time populated with commit timestamp of operation, as well as a progress of 100% once the operation has completed.  
`actions[]` |  `[DdlStatementActionInfo](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DdlStatementActionInfo)` The brief action info for the DDL statements. `actions[i]` is the brief info for `statements[i]`.  
  
## UpdateDatabaseDdlRequest

Enqueues the given DDL statements to be applied, in order but not necessarily all at once, to the database schema at some point (or points) in the future. The server checks that the statements are executable (syntactically valid, name tables that exist, etc.) before enqueueing them, but they may still fail upon later execution (for example, if a statement from another batch of statements is applied first and it conflicts in some way, or if there is some data-related problem like a `NULL` value in a column to which `NOT NULL` would be added). If a statement fails, all subsequent statements in the batch are automatically cancelled.

Each batch of statements is assigned a name which can be used with the `[Operations](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.longrunning#google.longrunning.Operations)` API to monitor progress. See the `[operation_id](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseDdlRequest.FIELDS.string.google.spanner.admin.database.v1.UpdateDatabaseDdlRequest.operation_id)` field for more details.

Fields  
---  
`database` |  `string` Required. The database to update. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.updateDdl`

  
`statements[]` |  `string` Required. DDL statements to be applied to the database.  
`operation_id` |  `string` If empty, the new update request is assigned an automatically-generated operation ID. Otherwise, `operation_id` is used to construct the name of the resulting Operation.Specifying an explicit operation ID simplifies determining whether the statements were executed in the event that the `[UpdateDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)` call is replayed, or the return value is otherwise lost: the `[database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseDdlRequest.FIELDS.string.google.spanner.admin.database.v1.UpdateDatabaseDdlRequest.database)` and `operation_id` fields can be combined to form the `name` of the resulting longrunning.Operation: `<database>/operations/<operation_id>`.`operation_id` should be unique within the database, and must be a valid identifier: `[a-z][a-z0-9_]*`. Note that automatically-generated operation IDs always begin with an underscore. If the named operation already exists, `[UpdateDatabaseDdl](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl)` returns `ALREADY_EXISTS`.  
`proto_descriptors` |  `bytes` Optional. Proto descriptors used by CREATE/ALTER PROTO BUNDLE statements. Contains a protobuf-serialized [google.protobuf.FileDescriptorSet](https://github.com/protocolbuffers/protobuf/blob/main/src/google/protobuf/descriptor.proto). To generate it, [install](https://grpc.io/docs/protoc-installation/) and run `protoc` with --include_imports and --descriptor_set_out. For example, to generate for moon/shot/app.proto, run
    
    
    $protoc  --proto_path=/app_path --proto_path=/lib_path \
             --include_imports \
             --descriptor_set_out=descriptors.data \
             moon/shot/app.proto
    

For more details, see protobuffer [self description](https://developers.google.com/protocol-buffers/docs/techniques#self-description).  
  
## UpdateDatabaseMetadata

Metadata type for the operation returned by `[UpdateDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase)`.

Fields  
---  
`request` |  `[UpdateDatabaseRequest](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.UpdateDatabaseRequest)` The request for `[UpdateDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase)`.  
`progress` |  `[OperationProgress](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.OperationProgress)` The progress of the `[UpdateDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase)` operation.  
`cancel_time` |  `[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` The time at which this operation was cancelled. If set, this operation is in the process of undoing itself (which is best-effort).  
  
## UpdateDatabaseRequest

The request for `[UpdateDatabase](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase)`.

Fields  
---  
`database` |  `[Database](https://docs.cloud.google.com/spanner/docs/reference/rpc/google.spanner.admin.database.v1#google.spanner.admin.database.v1.Database)` Required. The database to update. The `name` field of the database is of the form `projects/<project>/instances/<instance>/databases/<database>`. Authorization requires the following [IAM](https://cloud.google.com/iam/docs/) permission on the specified resource `database`:

  * `spanner.databases.update`

  
`update_mask` |  `[FieldMask](https://protobuf.dev/reference/protobuf/google.protobuf/#field-mask)` Required. The list of fields to update. Currently, only `enable_drop_protection` field can be updated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-24 UTC."],[],[]] 
