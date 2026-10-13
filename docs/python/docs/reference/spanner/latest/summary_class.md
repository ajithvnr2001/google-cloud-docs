---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/summary_class/
title: Package Classes (3.71.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:38:47.628655+00:00
---

# Package Classes (3.71.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/summary_class/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Classes (3.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 

Summary of entries of Classes for spanner.

## Classes 

### [DatabaseAdminAsyncClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminAsyncClient)

Cloud Spanner Database Admin API

The Cloud Spanner Database Admin API can be used to:

  * create, drop, and list databases
  * update the schema of pre-existing databases
  * create, delete, copy and list backups for a database
  * restore a database from an existing backup



### [DatabaseAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.DatabaseAdminClient)

Cloud Spanner Database Admin API

The Cloud Spanner Database Admin API can be used to:

  * create, drop, and list databases
  * update the schema of pre-existing databases
  * create, delete, copy and list backups for a database
  * restore a database from an existing backup



### [ListBackupOperationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsAsyncPager)

A pager for iterating through `list_backup_operations` requests.

This class thinly wraps an initial [ListBackupOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsResponse) object, and provides an `__aiter__` method to iterate through its `operations` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListBackupOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupOperationsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupOperationsPager)

A pager for iterating through `list_backup_operations` requests.

This class thinly wraps an initial [ListBackupOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsResponse) object, and provides an `__iter__` method to iterate through its `operations` field.

If there are more pages, the `__iter__` method will make additional `ListBackupOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListBackupOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupSchedulesAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesAsyncPager)

A pager for iterating through `list_backup_schedules` requests.

This class thinly wraps an initial [ListBackupSchedulesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesResponse) object, and provides an `__aiter__` method to iterate through its `backup_schedules` field.

If there are more pages, the `__aiter__` method will make additional `ListBackupSchedules` requests and continue to iterate through the `backup_schedules` field on the corresponding responses.

All the usual [ListBackupSchedulesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupSchedulesPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupSchedulesPager)

A pager for iterating through `list_backup_schedules` requests.

This class thinly wraps an initial [ListBackupSchedulesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesResponse) object, and provides an `__iter__` method to iterate through its `backup_schedules` field.

If there are more pages, the `__iter__` method will make additional `ListBackupSchedules` requests and continue to iterate through the `backup_schedules` field on the corresponding responses.

All the usual [ListBackupSchedulesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsAsyncPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsResponse) object, and provides an `__aiter__` method to iterate through its `backups` field.

If there are more pages, the `__aiter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListBackupsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListBackupsPager)

A pager for iterating through `list_backups` requests.

This class thinly wraps an initial [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsResponse) object, and provides an `__iter__` method to iterate through its `backups` field.

If there are more pages, the `__iter__` method will make additional `ListBackups` requests and continue to iterate through the `backups` field on the corresponding responses.

All the usual [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatabaseOperationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsAsyncPager)

A pager for iterating through `list_database_operations` requests.

This class thinly wraps an initial [ListDatabaseOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsResponse) object, and provides an `__aiter__` method to iterate through its `operations` field.

If there are more pages, the `__aiter__` method will make additional `ListDatabaseOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListDatabaseOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatabaseOperationsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseOperationsPager)

A pager for iterating through `list_database_operations` requests.

This class thinly wraps an initial [ListDatabaseOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsResponse) object, and provides an `__iter__` method to iterate through its `operations` field.

If there are more pages, the `__iter__` method will make additional `ListDatabaseOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListDatabaseOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatabaseRolesAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesAsyncPager)

A pager for iterating through `list_database_roles` requests.

This class thinly wraps an initial [ListDatabaseRolesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesResponse) object, and provides an `__aiter__` method to iterate through its `database_roles` field.

If there are more pages, the `__aiter__` method will make additional `ListDatabaseRoles` requests and continue to iterate through the `database_roles` field on the corresponding responses.

All the usual [ListDatabaseRolesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatabaseRolesPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabaseRolesPager)

A pager for iterating through `list_database_roles` requests.

This class thinly wraps an initial [ListDatabaseRolesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesResponse) object, and provides an `__iter__` method to iterate through its `database_roles` field.

If there are more pages, the `__iter__` method will make additional `ListDatabaseRoles` requests and continue to iterate through the `database_roles` field on the corresponding responses.

All the usual [ListDatabaseRolesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatabasesAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesAsyncPager)

A pager for iterating through `list_databases` requests.

This class thinly wraps an initial [ListDatabasesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesResponse) object, and provides an `__aiter__` method to iterate through its `databases` field.

If there are more pages, the `__aiter__` method will make additional `ListDatabases` requests and continue to iterate through the `databases` field on the corresponding responses.

All the usual [ListDatabasesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListDatabasesPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers.ListDatabasesPager)

A pager for iterating through `list_databases` requests.

This class thinly wraps an initial [ListDatabasesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesResponse) object, and provides an `__iter__` method to iterate through its `databases` field.

If there are more pages, the `__iter__` method will make additional `ListDatabases` requests and continue to iterate through the `databases` field on the corresponding responses.

All the usual [ListDatabasesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AddSplitPointsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.AddSplitPointsRequest)

The request for `AddSplitPoints][google.spanner.admin.database.v1.DatabaseAdmin.AddSplitPoints]`.

### [AddSplitPointsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.AddSplitPointsResponse)

The response for `AddSplitPoints][google.spanner.admin.database.v1.DatabaseAdmin.AddSplitPoints]`.

### [Backup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup)

A backup of a Cloud Spanner database.

### [State](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup.State)

Indicates the current state of the backup.

### [BackupInfo](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupInfo)

Information about a backup.

### [BackupInstancePartition](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupInstancePartition)

Instance partition information for the backup.

### [BackupSchedule](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupSchedule)

BackupSchedule expresses the automated backup creation specification for a Spanner database. Next ID: 10

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [BackupScheduleSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupScheduleSpec)

Defines specifications of the backup schedule.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CopyBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupEncryptionConfig)

Encryption configuration for the copied backup.

### [EncryptionType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupEncryptionConfig.EncryptionType)

Encryption types for the backup.

### [CopyBackupMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupMetadata)

Metadata type for the operation returned by `CopyBackup][google.spanner.admin.database.v1.DatabaseAdmin.CopyBackup]`.

### [CopyBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CopyBackupRequest)

The request for `CopyBackup][google.spanner.admin.database.v1.DatabaseAdmin.CopyBackup]`.

### [CreateBackupEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig)

Encryption configuration for the backup to create.

### [EncryptionType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupEncryptionConfig.EncryptionType)

Encryption types for the backup.

### [CreateBackupMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupMetadata)

Metadata type for the operation returned by `CreateBackup][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup]`.

### [CreateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupRequest)

The request for `CreateBackup][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup]`.

### [CreateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateBackupScheduleRequest)

The request for `CreateBackupSchedule][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackupSchedule]`.

### [CreateDatabaseMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateDatabaseMetadata)

Metadata type for the operation returned by `CreateDatabase][google.spanner.admin.database.v1.DatabaseAdmin.CreateDatabase]`.

### [CreateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CreateDatabaseRequest)

The request for `CreateDatabase][google.spanner.admin.database.v1.DatabaseAdmin.CreateDatabase]`.

### [CrontabSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.CrontabSpec)

CrontabSpec can be used to specify the version time and frequency at which the backup should be created.

### [Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database)

A Cloud Spanner database.

### [State](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Database.State)

Indicates the current state of the database.
    
    
        In this state, the database still references the backup it
        was restore from, preventing the backup from being deleted.
        When optimizations are complete, the full performance of the
        database will be restored, and the database will transition
        to `READY` state.
    

### [DatabaseDialect](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DatabaseDialect)

Indicates the dialect type of a database.

### [DatabaseRole](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DatabaseRole)

A Cloud Spanner database role.

### [DdlStatementActionInfo](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DdlStatementActionInfo)

Action information extracted from a DDL statement. This proto is used to display the brief info of the DDL statement for the operation `UpdateDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl]`.

### [DeleteBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DeleteBackupRequest)

The request for `DeleteBackup][google.spanner.admin.database.v1.DatabaseAdmin.DeleteBackup]`.

### [DeleteBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DeleteBackupScheduleRequest)

The request for `DeleteBackupSchedule][google.spanner.admin.database.v1.DatabaseAdmin.DeleteBackupSchedule]`.

### [DropDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DropDatabaseRequest)

The request for `DropDatabase][google.spanner.admin.database.v1.DatabaseAdmin.DropDatabase]`.

### [EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.EncryptionConfig)

Encryption configuration for a Cloud Spanner database.

### [EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.EncryptionInfo)

Encryption information for a Cloud Spanner database or backup.

### [Type](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.EncryptionInfo.Type)

Possible encryption types.

### [FullBackupSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.FullBackupSpec)

The specification for full backups. A full backup stores the entire contents of the database at a given version time.

### [GetBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetBackupRequest)

The request for `GetBackup][google.spanner.admin.database.v1.DatabaseAdmin.GetBackup]`.

### [GetBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetBackupScheduleRequest)

The request for `GetBackupSchedule][google.spanner.admin.database.v1.DatabaseAdmin.GetBackupSchedule]`.

### [GetDatabaseDdlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseDdlRequest)

The request for `GetDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDdl]`.

### [GetDatabaseDdlResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseDdlResponse)

The response for `GetDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.GetDatabaseDdl]`.

### [GetDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.GetDatabaseRequest)

The request for `GetDatabase][google.spanner.admin.database.v1.DatabaseAdmin.GetDatabase]`.

### [IncrementalBackupSpec](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.IncrementalBackupSpec)

The specification for incremental backup chains. An incremental backup stores the delta of changes between a previous backup and the database contents at a given version time. An incremental backup chain consists of a full backup and zero or more successive incremental backups. The first backup created for an incremental backup chain is always a full backup.

### [InternalUpdateGraphOperationRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.InternalUpdateGraphOperationRequest)

Internal request proto, do not use directly.

### [InternalUpdateGraphOperationResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.InternalUpdateGraphOperationResponse)

Internal response proto, do not use directly.

### [ListBackupOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsRequest)

The request for `ListBackupOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations]`.

### [ListBackupOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupOperationsResponse)

The response for `ListBackupOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupOperations]`.

### [ListBackupSchedulesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesRequest)

The request for `ListBackupSchedules][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupSchedules]`.

### [ListBackupSchedulesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupSchedulesResponse)

The response for `ListBackupSchedules][google.spanner.admin.database.v1.DatabaseAdmin.ListBackupSchedules]`.

### [ListBackupsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsRequest)

The request for `ListBackups][google.spanner.admin.database.v1.DatabaseAdmin.ListBackups]`.

### [ListBackupsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListBackupsResponse)

The response for `ListBackups][google.spanner.admin.database.v1.DatabaseAdmin.ListBackups]`.

### [ListDatabaseOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsRequest)

The request for `ListDatabaseOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseOperations]`.

### [ListDatabaseOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseOperationsResponse)

The response for `ListDatabaseOperations][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseOperations]`.

### [ListDatabaseRolesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesRequest)

The request for `ListDatabaseRoles][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseRoles]`.

### [ListDatabaseRolesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabaseRolesResponse)

The response for `ListDatabaseRoles][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabaseRoles]`.

### [ListDatabasesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesRequest)

The request for `ListDatabases][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases]`.

### [ListDatabasesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.ListDatabasesResponse)

The response for `ListDatabases][google.spanner.admin.database.v1.DatabaseAdmin.ListDatabases]`.

### [OperationProgress](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.OperationProgress)

Encapsulates progress related information for a Cloud Spanner long running operation.

### [OptimizeRestoredDatabaseMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.OptimizeRestoredDatabaseMetadata)

Metadata type for the long-running operation used to track the progress of optimizations performed on a newly restored database. This long-running operation is automatically created by the system after the successful completion of a database restore, and cannot be cancelled.

### [RestoreDatabaseEncryptionConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseEncryptionConfig)

Encryption configuration for the restored database.

### [EncryptionType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseEncryptionConfig.EncryptionType)

Encryption types for the database to be restored.

### [RestoreDatabaseMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseMetadata)

Metadata type for the long-running operation returned by `RestoreDatabase][google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreDatabaseRequest)

The request for `RestoreDatabase][google.spanner.admin.database.v1.DatabaseAdmin.RestoreDatabase]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreInfo](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreInfo)

Information about the database restore.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RestoreSourceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.RestoreSourceType)

Indicates the type of the restore source.

### [SplitPoints](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.SplitPoints)

The split points of a table/index.

### [Key](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.SplitPoints.Key)

A split key.

### [UpdateBackupRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateBackupRequest)

The request for `UpdateBackup][google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackup]`.

### [UpdateBackupScheduleRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateBackupScheduleRequest)

The request for `UpdateBackupScheduleRequest][google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackupSchedule]`.

### [UpdateDatabaseDdlMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseDdlMetadata)

Metadata type for the operation returned by `UpdateDatabaseDdl][google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabaseDdl]`.

### [UpdateDatabaseDdlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseDdlRequest)

Enqueues the given DDL statements to be applied, in order but not necessarily all at once, to the database schema at some point (or points) in the future. The server checks that the statements are executable (syntactically valid, name tables that exist, etc.) before enqueueing them, but they may still fail upon later execution (e.g., if a statement from another batch of statements is applied first and it conflicts in some way, or if there is some data-related problem like a `NULL` value in a column to which `NOT NULL` would be added). If a statement fails, all subsequent statements in the batch are automatically cancelled.

Each batch of statements is assigned a name which can be used with the `Operations][google.longrunning.Operations]` API to monitor progress. See the `operation_id][google.spanner.admin.database.v1.UpdateDatabaseDdlRequest.operation_id]` field for more details.

### [UpdateDatabaseMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseMetadata)

Metadata type for the operation returned by `UpdateDatabase][google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase]`.

### [UpdateDatabaseRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.UpdateDatabaseRequest)

The request for `UpdateDatabase][google.spanner.admin.database.v1.DatabaseAdmin.UpdateDatabase]`.

### [InstanceAdminAsyncClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminAsyncClient)

Cloud Spanner Instance Admin API

The Cloud Spanner Instance Admin API can be used to create, delete, modify and list instances. Instances are dedicated Cloud Spanner serving and storage resources to be used by Cloud Spanner databases.

Each instance has a "configuration", which dictates where the serving resources for the Cloud Spanner instance are located (e.g., US-central, Europe). Configurations are created by Google based on resource availability.

Cloud Spanner billing is based on the instances that exist and their sizes. After an instance exists, there are no additional per-database or per-operation charges for use of the instance (though there may be additional network bandwidth charges). Instances offer isolation: problems with databases in one instance will not affect other instances. However, within an instance databases can affect each other. For example, if one database in an instance receives a lot of requests and consumes most of the instance resources, fewer resources are available for other databases in that instance, and their performance may suffer.

### [InstanceAdminClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.InstanceAdminClient)

Cloud Spanner Instance Admin API

The Cloud Spanner Instance Admin API can be used to create, delete, modify and list instances. Instances are dedicated Cloud Spanner serving and storage resources to be used by Cloud Spanner databases.

Each instance has a "configuration", which dictates where the serving resources for the Cloud Spanner instance are located (e.g., US-central, Europe). Configurations are created by Google based on resource availability.

Cloud Spanner billing is based on the instances that exist and their sizes. After an instance exists, there are no additional per-database or per-operation charges for use of the instance (though there may be additional network bandwidth charges). Instances offer isolation: problems with databases in one instance will not affect other instances. However, within an instance databases can affect each other. For example, if one database in an instance receives a lot of requests and consumes most of the instance resources, fewer resources are available for other databases in that instance, and their performance may suffer.

### [ListInstanceConfigOperationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsAsyncPager)

A pager for iterating through `list_instance_config_operations` requests.

This class thinly wraps an initial [ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigOperationsResponse) object, and provides an `__aiter__` method to iterate through its `operations` field.

If there are more pages, the `__aiter__` method will make additional `ListInstanceConfigOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstanceConfigOperationsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigOperationsPager)

A pager for iterating through `list_instance_config_operations` requests.

This class thinly wraps an initial [ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigOperationsResponse) object, and provides an `__iter__` method to iterate through its `operations` field.

If there are more pages, the `__iter__` method will make additional `ListInstanceConfigOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstanceConfigsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsAsyncPager)

A pager for iterating through `list_instance_configs` requests.

This class thinly wraps an initial [ListInstanceConfigsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigsResponse) object, and provides an `__aiter__` method to iterate through its `instance_configs` field.

If there are more pages, the `__aiter__` method will make additional `ListInstanceConfigs` requests and continue to iterate through the `instance_configs` field on the corresponding responses.

All the usual [ListInstanceConfigsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstanceConfigsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstanceConfigsPager)

A pager for iterating through `list_instance_configs` requests.

This class thinly wraps an initial [ListInstanceConfigsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigsResponse) object, and provides an `__iter__` method to iterate through its `instance_configs` field.

If there are more pages, the `__iter__` method will make additional `ListInstanceConfigs` requests and continue to iterate through the `instance_configs` field on the corresponding responses.

All the usual [ListInstanceConfigsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstancePartitionOperationsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsAsyncPager)

A pager for iterating through `list_instance_partition_operations` requests.

This class thinly wraps an initial [ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionOperationsResponse) object, and provides an `__aiter__` method to iterate through its `operations` field.

If there are more pages, the `__aiter__` method will make additional `ListInstancePartitionOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstancePartitionOperationsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionOperationsPager)

A pager for iterating through `list_instance_partition_operations` requests.

This class thinly wraps an initial [ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionOperationsResponse) object, and provides an `__iter__` method to iterate through its `operations` field.

If there are more pages, the `__iter__` method will make additional `ListInstancePartitionOperations` requests and continue to iterate through the `operations` field on the corresponding responses.

All the usual [ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionOperationsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstancePartitionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsAsyncPager)

A pager for iterating through `list_instance_partitions` requests.

This class thinly wraps an initial [ListInstancePartitionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionsResponse) object, and provides an `__aiter__` method to iterate through its `instance_partitions` field.

If there are more pages, the `__aiter__` method will make additional `ListInstancePartitions` requests and continue to iterate through the `instance_partitions` field on the corresponding responses.

All the usual [ListInstancePartitionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstancePartitionsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancePartitionsPager)

A pager for iterating through `list_instance_partitions` requests.

This class thinly wraps an initial [ListInstancePartitionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionsResponse) object, and provides an `__iter__` method to iterate through its `instance_partitions` field.

If there are more pages, the `__iter__` method will make additional `ListInstancePartitions` requests and continue to iterate through the `instance_partitions` field on the corresponding responses.

All the usual [ListInstancePartitionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstancesAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesAsyncPager)

A pager for iterating through `list_instances` requests.

This class thinly wraps an initial [ListInstancesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancesResponse) object, and provides an `__aiter__` method to iterate through its `instances` field.

If there are more pages, the `__aiter__` method will make additional `ListInstances` requests and continue to iterate through the `instances` field on the corresponding responses.

All the usual [ListInstancesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListInstancesPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers.ListInstancesPager)

A pager for iterating through `list_instances` requests.

This class thinly wraps an initial [ListInstancesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancesResponse) object, and provides an `__iter__` method to iterate through its `instances` field.

If there are more pages, the `__iter__` method will make additional `ListInstances` requests and continue to iterate through the `instances` field on the corresponding responses.

All the usual [ListInstancesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancesResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [AutoscalingConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig)

Autoscaling configuration for an instance.

### [AsymmetricAutoscalingOption](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig.AsymmetricAutoscalingOption)

AsymmetricAutoscalingOption specifies the scaling of replicas identified by the given selection.

### [AutoscalingConfigOverrides](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig.AsymmetricAutoscalingOption.AutoscalingConfigOverrides)

Overrides the top-level autoscaling configuration for the replicas identified by `replica_selection`. All fields in this message are optional. Any unspecified fields will use the corresponding values from the top-level autoscaling configuration.

### [AutoscalingLimits](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig.AutoscalingLimits)

The autoscaling limits for the instance. Users can define the minimum and maximum compute capacity allocated to the instance, and the autoscaler will only scale within that range. Users can either use nodes or processing units to specify the limits, but should use the same unit to set both the min_limit and max_limit.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [AutoscalingTargets](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.AutoscalingConfig.AutoscalingTargets)

The autoscaling targets for an instance.

### [CreateInstanceConfigMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.CreateInstanceConfigMetadata)

Metadata type for the operation returned by `CreateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstanceConfig]`.

### [CreateInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.CreateInstanceConfigRequest)

The request for `CreateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstanceConfig]`.

### [CreateInstanceMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.CreateInstanceMetadata)

Metadata type for the operation returned by `CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance]`.

### [CreateInstancePartitionMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.CreateInstancePartitionMetadata)

Metadata type for the operation returned by `CreateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstancePartition]`.

### [CreateInstancePartitionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.CreateInstancePartitionRequest)

The request for `CreateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstancePartition]`.

### [CreateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.CreateInstanceRequest)

The request for `CreateInstance][google.spanner.admin.instance.v1.InstanceAdmin.CreateInstance]`.

### [DeleteInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.DeleteInstanceConfigRequest)

The request for `DeleteInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstanceConfig]`.

### [DeleteInstancePartitionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.DeleteInstancePartitionRequest)

The request for `DeleteInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstancePartition]`.

### [DeleteInstanceRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.DeleteInstanceRequest)

The request for `DeleteInstance][google.spanner.admin.instance.v1.InstanceAdmin.DeleteInstance]`.

### [FreeInstanceMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.FreeInstanceMetadata)

Free instance specific metadata that is kept even after an instance has been upgraded for tracking purposes.

### [ExpireBehavior](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.FreeInstanceMetadata.ExpireBehavior)

Allows users to change behavior when a free instance expires.

### [FulfillmentPeriod](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.FulfillmentPeriod)

Indicates the expected fulfillment period of an operation.

### [GetInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.GetInstanceConfigRequest)

The request for `GetInstanceConfigRequest][google.spanner.admin.instance.v1.InstanceAdmin.GetInstanceConfig]`.

### [GetInstancePartitionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.GetInstancePartitionRequest)

The request for `GetInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.GetInstancePartition]`.

### [GetInstanceRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.GetInstanceRequest)

The request for `GetInstance][google.spanner.admin.instance.v1.InstanceAdmin.GetInstance]`.

### [Instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance)

An isolated set of Cloud Spanner resources on which databases can be hosted.

### [DefaultBackupScheduleType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.DefaultBackupScheduleType)

Indicates the `default backup schedule <https://cloud.google.com/spanner/docs/backup#default-backup-schedules>`__ behavior for new databases within the instance.

### [Edition](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.Edition)

The edition selected for this instance. Different editions provide different capabilities at different price points.

### [InstanceType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.InstanceType)

The type of this instance. The type can be used to distinguish product variants, that can affect aspects like: usage restrictions, quotas and billing. Currently this is used to distinguish FREE_INSTANCE vs PROVISIONED instances.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.LabelsEntry)

The abstract base class for a message.

### [State](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.Instance.State)

Indicates the current state of the instance.

### [InstanceConfig](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstanceConfig)

A possible configuration for a Cloud Spanner instance. Configurations define the geographic placement of nodes and their replication.

### [FreeInstanceAvailability](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstanceConfig.FreeInstanceAvailability)

Describes the availability for free instances to be created in an instance configuration.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstanceConfig.LabelsEntry)

The abstract base class for a message.

### [QuorumType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstanceConfig.QuorumType)

Indicates the quorum type of this instance configuration.
    
    
        This instance configuration requires failover in the event
        of regional failures.
    MULTI_REGION (3):
        An instance configuration tagged with the `MULTI_REGION`
        quorum type forms a write quorum from replicas that are
        spread across more than one region in a multi-region
        configuration.
    

### [State](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstanceConfig.State)

Indicates the current state of the instance configuration.

### [Type](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstanceConfig.Type)

The type of this configuration.

### [InstancePartition](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstancePartition)

An isolated set of Cloud Spanner resources that databases can define placements on.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [State](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.InstancePartition.State)

Indicates the current state of the instance partition.

### [ListInstanceConfigOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigOperationsRequest)

The request for `ListInstanceConfigOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations]`.

### [ListInstanceConfigOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigOperationsResponse)

The response for `ListInstanceConfigOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigOperations]`.

### [ListInstanceConfigsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigsRequest)

The request for `ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs]`.

### [ListInstanceConfigsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstanceConfigsResponse)

The response for `ListInstanceConfigs][google.spanner.admin.instance.v1.InstanceAdmin.ListInstanceConfigs]`.

### [ListInstancePartitionOperationsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionOperationsRequest)

The request for `ListInstancePartitionOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations]`.

### [ListInstancePartitionOperationsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionOperationsResponse)

The response for `ListInstancePartitionOperations][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitionOperations]`.

### [ListInstancePartitionsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionsRequest)

The request for `ListInstancePartitions][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions]`.

### [ListInstancePartitionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancePartitionsResponse)

The response for `ListInstancePartitions][google.spanner.admin.instance.v1.InstanceAdmin.ListInstancePartitions]`.

### [ListInstancesRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancesRequest)

The request for `ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances]`.

### [ListInstancesResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ListInstancesResponse)

The response for `ListInstances][google.spanner.admin.instance.v1.InstanceAdmin.ListInstances]`.

### [MoveInstanceMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.MoveInstanceMetadata)

Metadata type for the operation returned by `MoveInstance][google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance]`.

### [MoveInstanceRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.MoveInstanceRequest)

The request for `MoveInstance][google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance]`.

### [MoveInstanceResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.MoveInstanceResponse)

The response for `MoveInstance][google.spanner.admin.instance.v1.InstanceAdmin.MoveInstance]`.

### [OperationProgress](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.OperationProgress)

Encapsulates progress related information for a Cloud Spanner long running instance operations.

### [ReplicaComputeCapacity](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ReplicaComputeCapacity)

ReplicaComputeCapacity describes the amount of server resources that are allocated to each replica identified by the replica selection.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ReplicaInfo](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ReplicaInfo)

### [ReplicaType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ReplicaInfo.ReplicaType)

Indicates the type of replica. See the `replica types documentation <https://cloud.google.com/spanner/docs/replication#replica_types>`__ for more details.
    
    
        - Maintain a full copy of your data.
        - Serve reads.
        - Can vote whether to commit a write.
        - Participate in leadership election.
        - Are eligible to become a leader.
    READ_ONLY (2):
        Read-only replicas only support reads (not writes).
        Read-only replicas:
    
        - Maintain a full copy of your data.
        - Serve reads.
        - Do not participate in voting to commit writes.
        - Are not eligible to become a leader.
    WITNESS (3):
        Witness replicas don't support reads but do participate in
        voting to commit writes. Witness replicas:
    
        - Do not maintain a full copy of data.
        - Do not serve reads.
        - Vote whether to commit writes.
        - Participate in leader election but are not eligible to
          become leader.
    

### [ReplicaSelection](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.ReplicaSelection)

ReplicaSelection identifies replicas with common properties.

### [UpdateInstanceConfigMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.UpdateInstanceConfigMetadata)

Metadata type for the operation returned by `UpdateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstanceConfig]`.

### [UpdateInstanceConfigRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.UpdateInstanceConfigRequest)

The request for `UpdateInstanceConfig][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstanceConfig]`.

### [UpdateInstanceMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.UpdateInstanceMetadata)

Metadata type for the operation returned by `UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance]`.

### [UpdateInstancePartitionMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.UpdateInstancePartitionMetadata)

Metadata type for the operation returned by `UpdateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstancePartition]`.

### [UpdateInstancePartitionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.UpdateInstancePartitionRequest)

The request for `UpdateInstancePartition][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstancePartition]`.

### [UpdateInstanceRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.types.UpdateInstanceRequest)

The request for `UpdateInstance][google.spanner.admin.instance.v1.InstanceAdmin.UpdateInstance]`.

### [Batch](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.Batch)

Accumulate mutations for transmission during `commit`.

### [MutationGroup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.MutationGroup)

A container for mutations.

Clients should use xref_MutationGroups to obtain instances instead of directly creating instances.

### [MutationGroups](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch.MutationGroups)

Accumulate mutation groups for transmission during `batch_write`.

### [Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client)

Client for interacting with Cloud Spanner API.

**Note:** Since the Cloud Spanner API requires the gRPC transport, no `_http` argument is accepted by this class. 

### [BatchCheckout](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchCheckout)

Context manager for using a batch from a database.

Inside the context manager, checks out a session from the database, creates a batch from it, making the batch available.

Caller must _not_ use the batch to perform API requests outside the scope of the context manager.

### [BatchSnapshot](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.BatchSnapshot)

Wrapper for generating and processing read / query batches.

### [Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database)

Representation of a Cloud Spanner Database.

We can use a `Database` to:

  * `create` the database
  * `reload` the database
  * `update` the database
  * `drop` the database



### [MutationGroupsCheckout](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.MutationGroupsCheckout)

Context manager for using mutation groups from a database.

Inside the context manager, checks out a session from the database, creates mutation groups from it, making the groups available.

Caller must _not_ use the object to perform API requests outside the scope of the context manager.

### [SnapshotCheckout](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.SnapshotCheckout)

Context manager for using a snapshot from a database.

Inside the context manager, checks out a session from the database, creates a snapshot from it, making the snapshot available.

Caller must _not_ use the snapshot to perform API requests outside the scope of the context manager.

### [Instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance)

Representation of a Cloud Spanner Instance.

We can use a `Instance` to:

  * `reload` itself
  * `create` itself
  * `update` itself
  * `delete` itself



### [KeyRange](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset.KeyRange)

Identify range of table rows via start / end points.

Specify either a `start_open` or `start_closed` key, or defaults to `start_closed = []`. Specify either an `end_open` or `end_closed` key, or defaults to `end_closed = []`. However, at least one key has to be specified. If no keys are specified, ValueError is raised.

### [KeySet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset.KeySet)

Identify table rows via keys / ranges.

### [AbstractSessionPool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.AbstractSessionPool)

Specifies required API for concrete session pool implementations.

### [BurstyPool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.BurstyPool)

Concrete session pool implementation:

  * "Pings" existing sessions via `session.exists` before returning them.

  * Creates a new session, rather than blocking, when `get` is called on an empty pool.

  * Discards the returned session, rather than blocking, when `put` is called on a full pool.




### [FixedSizePool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.FixedSizePool)

Concrete session pool implementation:

  * Pre-allocates / creates a fixed number of sessions.

  * "Pings" existing sessions via `session.exists` before returning sessions that have not been used for more than 55 minutes and replaces expired sessions.

  * Blocks, with a timeout, when `get` is called on an empty pool. Raises after timing out.

  * Raises when `put` is called on a full pool. That error is never expected in normal practice, as users should be calling `get` followed by `put` whenever in need of a session.




### [PingingPool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.PingingPool)

Concrete session pool implementation:

  * Pre-allocates / creates a fixed number of sessions.

  * Sessions are used in "round-robin" order (LRU first).

  * "Pings" existing sessions in the background after a specified interval via an API call (`session.ping()`).

  * Blocks, with a timeout, when `get` is called on an empty pool. Raises after timing out.

  * Raises when `put` is called on a full pool. That error is never expected in normal practice, as users should be calling `get` followed by `put` whenever in need of a session.




The application is responsible for calling `ping` at appropriate times, e.g. from a background thread.

### [SessionCheckout](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.SessionCheckout)

Context manager: hold session checked out from a pool.

Deprecated. Sessions should be checked out indirectly using context managers or xref_run_in_transaction, rather than checked out directly from the pool.

### [TransactionPingingPool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool.TransactionPingingPool)

Concrete session pool implementation:

Deprecated: TransactionPingingPool no longer begins a transaction for each of its sessions at startup. Hence the TransactionPingingPool is same as `PingingPool` and maybe removed in the future.

In addition to the features of `PingingPool`, this class creates and begins a transaction for each of its sessions at startup.

When a session is returned to the pool, if its transaction has been committed or rolled back, the pool creates a new transaction for the session and pushes the transaction onto a separate queue of "transactions to begin." The application is responsible for flushing this queue as appropriate via the pool's `begin_pending_transactions` method.

### [SpannerAsyncClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerAsyncClient)

Cloud Spanner API

The Cloud Spanner API can be used to manage sessions and execute transactions on data stored in Cloud Spanner databases.

### [SpannerClient](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.SpannerClient)

Cloud Spanner API

The Cloud Spanner API can be used to manage sessions and execute transactions on data stored in Cloud Spanner databases.

### [ListSessionsAsyncPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.pagers.ListSessionsAsyncPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ListSessionsResponse) object, and provides an `__aiter__` method to iterate through its `sessions` field.

If there are more pages, the `__aiter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [ListSessionsPager](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.pagers.ListSessionsPager)

A pager for iterating through `list_sessions` requests.

This class thinly wraps an initial [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ListSessionsResponse) object, and provides an `__iter__` method to iterate through its `sessions` field.

If there are more pages, the `__iter__` method will make additional `ListSessions` requests and continue to iterate through the `sessions` field on the corresponding responses.

All the usual [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ListSessionsResponse) attributes are available on the pager. If multiple requests are made, only the most recent response is retained, and thus used for attribute lookup.

### [Session](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session.Session)

Representation of a Cloud Spanner Session.

We can use a `Session` to:

  * `create` the session
  * Use `exists` to check for the existence of the session
  * `drop` the session



### [Snapshot](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.snapshot.Snapshot)

Allow a set of reads / SQL statements with shared staleness.

### [StreamedResultSet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed.StreamedResultSet)

Process a sequence of partial result sets into a single set of row data.

### [Unmergeable](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed.Unmergeable)

Unable to merge two values.

### [Table](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.table.Table)

Representation of a Cloud Spanner Table.

### [BatchTransactionId](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.BatchTransactionId)

API documentation for `spanner_v1.transaction.BatchTransactionId` class.

### [DefaultTransactionOptions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.DefaultTransactionOptions)

DefaultTransactionOptions(isolation_level: str = <IsolationLevel.ISOLATION_LEVEL_UNSPECIFIED: 0>, read_lock_mode: str = <ReadLockMode.READ_LOCK_MODE_UNSPECIFIED: 0>)

### [Transaction](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction.Transaction)

Implement read-write transaction semantics for a session.

### [BatchCreateSessionsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.BatchCreateSessionsRequest)

The request for `BatchCreateSessions][google.spanner.v1.Spanner.BatchCreateSessions]`.

### [BatchCreateSessionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.BatchCreateSessionsResponse)

The response for `BatchCreateSessions][google.spanner.v1.Spanner.BatchCreateSessions]`.

### [BatchWriteRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.BatchWriteRequest)

The request for `BatchWrite][google.spanner.v1.Spanner.BatchWrite]`.

### [MutationGroup](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.BatchWriteRequest.MutationGroup)

A group of mutations to be committed together. Related mutations should be placed in a group. For example, two mutations inserting rows with the same primary key prefix in both parent and child tables are related.

### [BatchWriteResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.BatchWriteResponse)

The result of applying a batch of mutations.

### [BeginTransactionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.BeginTransactionRequest)

The request for `BeginTransaction][google.spanner.v1.Spanner.BeginTransaction]`.

### [CacheUpdate](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.CacheUpdate)

A `CacheUpdate` expresses a set of changes the client should incorporate into its location cache. These changes may or may not be newer than what the client has in its cache, and should be discarded if necessary. `CacheUpdate`\ s can be obtained in response to requests that included a `RoutingHint` field, but may also be obtained by explicit location-fetching RPCs which may be added in the future.

### [ChangeStreamRecord](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord)

Spanner Change Streams enable customers to capture and stream out changes to their Spanner databases in real-time. A change stream can be created with option partition_mode='IMMUTABLE_KEY_RANGE' or partition_mode='MUTABLE_KEY_RANGE'.

This message is only used in Change Streams created with the option partition_mode='MUTABLE_KEY_RANGE'. Spanner automatically creates a special Table-Valued Function (TVF) along with each Change Streams. The function provides access to the change stream's records. The function is named READ_<change_stream_name> (where <change_stream_name> is the name of the change stream), and it returns a table with only one column called ChangeRecord.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [DataChangeRecord](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.DataChangeRecord)

A data change record contains a set of changes to a table with the same modification type (insert, update, or delete) committed at the same commit timestamp in one change stream partition for the same transaction. Multiple data change records can be returned for the same transaction across multiple change stream partitions.

### [ColumnMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.DataChangeRecord.ColumnMetadata)

Metadata for a column.

### [Mod](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.DataChangeRecord.Mod)

A mod describes all data changes in a watched table row.

### [ModType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.DataChangeRecord.ModType)

Mod type describes the type of change Spanner applied to the data. For example, if the client submits an INSERT_OR_UPDATE request, Spanner will perform an insert if there is no existing row and return ModType INSERT. Alternatively, if there is an existing row, Spanner will perform an update and return ModType UPDATE.

### [ModValue](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.DataChangeRecord.ModValue)

Returns the value and associated metadata for a particular field of the `Mod][google.spanner.v1.ChangeStreamRecord.DataChangeRecord.Mod]`.

### [ValueCaptureType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.DataChangeRecord.ValueCaptureType)

Value capture type describes which values are recorded in the data change record.

### [HeartbeatRecord](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.HeartbeatRecord)

A heartbeat record is returned as a progress indicator, when there are no data changes or any other partition record types in the change stream partition.

### [PartitionEndRecord](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEndRecord)

A partition end record serves as a notification that the client should stop reading the partition. No further records are expected to be retrieved on it.

### [PartitionEventRecord](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord)

A partition event record describes key range changes for a change stream partition. The changes to a row defined by its primary key can be captured in one change stream partition for a specific time range, and then be captured in a different change stream partition for a different time range. This movement of key ranges across change stream partitions is a reflection of activities, such as Spanner's dynamic splitting and load balancing, etc. Processing this event is needed if users want to guarantee processing of the changes for any key in timestamp order. If time ordered processing of changes for a primary key is not needed, this event can be ignored. To guarantee time ordered processing for each primary key, if the event describes move-ins, the reader of this partition needs to wait until the readers of the source partitions have processed all records with timestamps <= this PartitionEventRecord.commit_timestamp, before advancing beyond this PartitionEventRecord. If the event describes move-outs, the reader can notify the readers of the destination partitions that they can continue processing.

### [MoveInEvent](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord.MoveInEvent)

Describes move-in of the key ranges into the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]`.

To maintain processing the changes for a particular key in timestamp order, the query processing the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]` should not advance beyond the partition event record commit timestamp until the queries processing the source change stream partitions have processed all change stream records with timestamps <= the partition event record commit timestamp.

### [MoveOutEvent](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent)

Describes move-out of the key ranges out of the change stream partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]`.

To maintain processing the changes for a particular key in timestamp order, the query processing the `MoveOutEvent][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.MoveOutEvent]` in the partition identified by `partition_token][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.partition_token]` should inform the queries processing the destination partitions that they can unblock and proceed processing records past the `commit_timestamp][google.spanner.v1.ChangeStreamRecord.PartitionEventRecord.commit_timestamp]`.

### [PartitionStartRecord](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ChangeStreamRecord.PartitionStartRecord)

A partition start record serves as a notification that the client should schedule the partitions to be queried. PartitionStartRecord returns information about one or more partitions.

### [CommitRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.CommitRequest)

The request for `Commit][google.spanner.v1.Spanner.Commit]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CommitResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.CommitResponse)

The response for `Commit][google.spanner.v1.Spanner.Commit]`.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [CommitStats](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.CommitResponse.CommitStats)

Additional statistics about a commit.

### [CreateSessionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.CreateSessionRequest)

The request for `CreateSession][google.spanner.v1.Spanner.CreateSession]`.

### [DeleteSessionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.DeleteSessionRequest)

The request for `DeleteSession][google.spanner.v1.Spanner.DeleteSession]`.

### [DirectedReadOptions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.DirectedReadOptions)

The `DirectedReadOptions` can be used to indicate which replicas or regions should be used for non-transactional reads or queries.

`DirectedReadOptions` can only be specified for a read-only transaction, otherwise the API returns an `INVALID_ARGUMENT` error.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ExcludeReplicas](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.DirectedReadOptions.ExcludeReplicas)

An ExcludeReplicas contains a repeated set of ReplicaSelection that should be excluded from serving requests.

### [IncludeReplicas](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.DirectedReadOptions.IncludeReplicas)

An `IncludeReplicas` contains a repeated set of `ReplicaSelection` which indicates the order in which replicas should be considered.

### [ReplicaSelection](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.DirectedReadOptions.ReplicaSelection)

The directed read replica selector. Callers must provide one or more of the following fields for replica selection:

  * `location` \- The location must be one of the regions within the multi-region configuration of your database.
  * `type` \- The type of the replica.



Some examples of using replica_selectors are:

  * `location:us-east1` \--> The "us-east1" replica(s) of any available type is used to process the request.
  * `type:READ_ONLY` \--> The "READ_ONLY" type replica(s) in the nearest available location are used to process the request.
  * `location:us-east1 type:READ_ONLY` \--> The "READ_ONLY" type replica(s) in location "us-east1" is used to process the request.



### [Type](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.DirectedReadOptions.ReplicaSelection.Type)

Indicates the type of replica.

### [ExecuteBatchDmlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteBatchDmlRequest)

The request for `ExecuteBatchDml][google.spanner.v1.Spanner.ExecuteBatchDml]`.

### [Statement](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteBatchDmlRequest.Statement)

A single DML statement.

### [ParamTypesEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteBatchDmlRequest.Statement.ParamTypesEntry)

The abstract base class for a message.

### [ExecuteBatchDmlResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteBatchDmlResponse)

The response for `ExecuteBatchDml][google.spanner.v1.Spanner.ExecuteBatchDml]`. Contains a list of `ResultSet][google.spanner.v1.ResultSet]` messages, one for each DML statement that has successfully executed, in the same order as the statements in the request. If a statement fails, the status in the response body identifies the cause of the failure.

To check for DML statements that failed, use the following approach:

  1. Check the status in the response message. The `google.rpc.Code][google.rpc.Code]` enum value `OK` indicates that all statements were executed successfully.
  2. If the status was not `OK`, check the number of result sets in the response. If the response contains `N` `ResultSet][google.spanner.v1.ResultSet]` messages, then statement `N+1` in the request failed.



Example 1:

  * Request: 5 DML statements, all executed successfully.
  * Response: 5 `ResultSet][google.spanner.v1.ResultSet]` messages, with the status `OK`.



Example 2:

  * Request: 5 DML statements. The third statement has a syntax error.
  * Response: 2 `ResultSet][google.spanner.v1.ResultSet]` messages, and a syntax error (`INVALID_ARGUMENT`) status. The number of `ResultSet][google.spanner.v1.ResultSet]` messages indicates that the third statement failed, and the fourth and fifth statements were not executed.



### [ExecuteSqlRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteSqlRequest)

The request for `ExecuteSql][google.spanner.v1.Spanner.ExecuteSql]` and `ExecuteStreamingSql][google.spanner.v1.Spanner.ExecuteStreamingSql]`.

### [ParamTypesEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteSqlRequest.ParamTypesEntry)

The abstract base class for a message.

### [QueryMode](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryMode)

Mode in which the statement must be processed.

### [QueryOptions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ExecuteSqlRequest.QueryOptions)

Query optimizer configuration.

### [FetchCacheUpdateRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.FetchCacheUpdateRequest)

The request for `FetchCacheUpdate][google.spanner.v1.Spanner.FetchCacheUpdate]`.

### [GetSessionRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.GetSessionRequest)

The request for `GetSession][google.spanner.v1.Spanner.GetSession]`.

### [Group](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Group)

A `Group` represents a paxos group in a database. A group is a set of tablets that are replicated across multiple servers. Groups may have a leader tablet. Groups store one (or sometimes more) ranges of keys.

### [KeyRange](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeyRange)

KeyRange represents a range of rows in a table or index.

A range has a start key and an end key. These keys can be open or closed, indicating if the range includes rows with that key.

Keys are represented by lists, where the ith value in the list corresponds to the ith component of the table or index primary key. Individual values are encoded as described `here][google.spanner.v1.TypeCode]`.

For example, consider the following table definition:

::
    
    
    CREATE TABLE UserEvents (
      UserName STRING(MAX),
      EventDate STRING(10)
    ) PRIMARY KEY(UserName, EventDate);
    

The following keys name rows in this table:

::
    
    
    ["Bob", "2014-09-23"]
    ["Alfred", "2015-06-12"]
    

Since the `UserEvents` table's `PRIMARY KEY` clause names two columns, each `UserEvents` key has two elements; the first is the `UserName`, and the second is the `EventDate`.

Key ranges with multiple components are interpreted lexicographically by component using the table or index key's declared sort order. For example, the following range returns all events for user `"Bob"` that occurred in the year 2015:

::
    
    
    "start_closed": ["Bob", "2015-01-01"]
    "end_closed": ["Bob", "2015-12-31"]
    

Start and end keys can omit trailing key components. This affects the inclusion and exclusion of rows that exactly match the provided key components: if the key is closed, then rows that exactly match the provided components are included; if the key is open, then rows that exactly match are not included.

For example, the following range includes all events for `"Bob"` that occurred during and after the year 2000:

::
    
    
    "start_closed": ["Bob", "2000-01-01"]
    "end_closed": ["Bob"]
    

The next example retrieves all events for `"Bob"`:

::
    
    
    "start_closed": ["Bob"]
    "end_closed": ["Bob"]
    

To retrieve events before the year 2000:

::
    
    
    "start_closed": ["Bob"]
    "end_open": ["Bob", "2000-01-01"]
    

The following range includes all rows in the table:

::
    
    
    "start_closed": []
    "end_closed": []
    

This range returns all users whose `UserName` begins with any character from A to C:

::
    
    
    "start_closed": ["A"]
    "end_open": ["D"]
    

This range returns all users whose `UserName` begins with B:

::
    
    
    "start_closed": ["B"]
    "end_open": ["C"]
    

Key ranges honor column sort order. For example, suppose a table is defined as follows:

::
    
    
    CREATE TABLE DescendingSortedTable {
      Key INT64,
      ...
    ) PRIMARY KEY(Key DESC);
    

The following range retrieves all rows with key values between 1 and 100 inclusive:

::
    
    
    "start_closed": ["100"]
    "end_closed": ["1"]
    

Note that 100 is passed as the start, and 1 is passed as the end, because `Key` is a descending column in the schema.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [KeyRecipe](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeyRecipe)

A `KeyRecipe` provides the metadata required to translate reads, mutations, and queries into a byte array in "sortable string format" (ssformat)that can be used with `Range`\ s to route requests. Note that the client _must_ tolerate `KeyRecipe`\ s that appear to be invalid, since the `KeyRecipe` format may change over time. Requests with invalid `KeyRecipe`\ s should be routed to a default server.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Part](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeyRecipe.Part)

An ssformat key is composed of a sequence of tag numbers and key column values. `Part` represents a single tag or key column value.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [NullOrder](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeyRecipe.Part.NullOrder)

The null order of the key column. This dictates where NULL values sort in the sorted order. Note that columns which are `NOT NULL` can have a special encoding.

### [Order](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeyRecipe.Part.Order)

The remaining fields encode column values.

### [KeySet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.KeySet)

`KeySet` defines a collection of Cloud Spanner keys and/or key ranges. All the keys are expected to be in the same table or index. The keys need not be sorted in any particular way.

If the same key is specified multiple times in the set (for example if two ranges, two keys, or a key and a range overlap), Cloud Spanner behaves as if the key were only specified once.

### [ListSessionsRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ListSessionsRequest)

The request for `ListSessions][google.spanner.v1.Spanner.ListSessions]`.

### [ListSessionsResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ListSessionsResponse)

The response for `ListSessions][google.spanner.v1.Spanner.ListSessions]`.

### [MultiplexedSessionPrecommitToken](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.MultiplexedSessionPrecommitToken)

When a read-write transaction is executed on a multiplexed session, this precommit token is sent back to the client as a part of the `Transaction][google.spanner.v1.Transaction]` message in the `BeginTransaction][google.spanner.v1.BeginTransactionRequest]` response and also as a part of the `ResultSet][google.spanner.v1.ResultSet]` and `PartialResultSet][google.spanner.v1.PartialResultSet]` responses.

### [Mutation](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Mutation)

A modification to one or more Cloud Spanner rows. Mutations can be applied to a Cloud Spanner database by sending them in a `Commit][google.spanner.v1.Spanner.Commit]` call.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Ack](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Mutation.Ack)

Arguments to `ack][google.spanner.v1.Mutation.ack]` operations.

### [Delete](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Mutation.Delete)

Arguments to `delete][google.spanner.v1.Mutation.delete]` operations.

### [Send](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Mutation.Send)

Arguments to `send][google.spanner.v1.Mutation.send]` operations.

### [Write](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Mutation.Write)

Arguments to `insert][google.spanner.v1.Mutation.insert]`, `update][google.spanner.v1.Mutation.update]`, `insert_or_update][google.spanner.v1.Mutation.insert_or_update]`, and `replace][google.spanner.v1.Mutation.replace]` operations.

### [PartialResultSet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PartialResultSet)

Partial results from a streaming read or SQL query. Streaming reads and SQL queries better tolerate large result sets, large rows, and large values, but are a little trickier to consume.

### [Partition](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Partition)

Information returned for each partition returned in a PartitionResponse.

### [PartitionOptions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PartitionOptions)

Options for a `PartitionQueryRequest` and `PartitionReadRequest`.

### [PartitionQueryRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PartitionQueryRequest)

The request for `PartitionQuery][google.spanner.v1.Spanner.PartitionQuery]`

### [ParamTypesEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PartitionQueryRequest.ParamTypesEntry)

The abstract base class for a message.

### [PartitionReadRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PartitionReadRequest)

The request for `PartitionRead][google.spanner.v1.Spanner.PartitionRead]`

### [PartitionResponse](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PartitionResponse)

The response for `PartitionQuery][google.spanner.v1.Spanner.PartitionQuery]` or `PartitionRead][google.spanner.v1.Spanner.PartitionRead]`

### [PlanNode](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PlanNode)

Node information for nodes appearing in a `QueryPlan.plan_nodes][google.spanner.v1.QueryPlan.plan_nodes]`.

### [ChildLink](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PlanNode.ChildLink)

Metadata associated with a parent-child relationship appearing in a `PlanNode][google.spanner.v1.PlanNode]`.

### [Kind](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PlanNode.Kind)

The kind of `PlanNode][google.spanner.v1.PlanNode]`. Distinguishes between the two different kinds of nodes that can appear in a query plan.

### [ShortRepresentation](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PlanNode.ShortRepresentation)

Condensed representation of a node and its subtree. Only present for `SCALAR` [PlanNode(s)][google.spanner.v1.PlanNode].

### [SubqueriesEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.PlanNode.ShortRepresentation.SubqueriesEntry)

The abstract base class for a message.

### [QueryAdvisorResult](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.QueryAdvisorResult)

Output of query advisor analysis.

### [IndexAdvice](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.QueryAdvisorResult.IndexAdvice)

Recommendation to add new indexes to run queries more efficiently.

### [QueryPlan](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.QueryPlan)

Contains an ordered list of nodes appearing in the query plan.

### [Range](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Range)

A `Range` represents a range of keys in a database. The keys themselves are encoded in "sortable string format", also known as ssformat. Consult Spanner's open source client libraries for details on the encoding.

Each range represents a contiguous range of rows, possibly from multiple tables/indexes. Each range is associated with a single paxos group (known as a "group" throughout this API), a split (which names the exact range within the group), and a generation that can be used to determine whether a given `Range` represents a newer or older location for the key range.

### [ReadRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ReadRequest)

The request for `Read][google.spanner.v1.Spanner.Read]` and `StreamingRead][google.spanner.v1.Spanner.StreamingRead]`.

### [LockHint](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ReadRequest.LockHint)

A lock hint mechanism for reads done within a transaction.
    
    
        `LOCK_HINT_UNSPECIFIED` is equivalent to
        `LOCK_HINT_SHARED`.
    LOCK_HINT_SHARED (1):
        Acquire shared locks.
    
        By default when you perform a read as part of a read-write
        transaction, Spanner acquires shared read locks, which
        allows other reads to still access the data until your
        transaction is ready to commit. When your transaction is
        committing and writes are being applied, the transaction
        attempts to upgrade to an exclusive lock for any data you
        are writing. For more information about locks, see `Lock
        modes <https://cloud.google.com/spanner/docs/introspection/lock-statistics#explain-lock-modes>`__.
    LOCK_HINT_EXCLUSIVE (2):
        Acquire exclusive locks.
    
        Requesting exclusive locks is beneficial if you observe high
        write contention, which means you notice that multiple
        transactions are concurrently trying to read and write to
        the same data, resulting in a large number of aborts. This
        problem occurs when two transactions initially acquire
        shared locks and then both try to upgrade to exclusive locks
        at the same time. In this situation both transactions are
        waiting for the other to give up their lock, resulting in a
        deadlocked situation. Spanner is able to detect this
        occurring and force one of the transactions to abort.
        However, this is a slow and expensive operation and results
        in lower performance. In this case it makes sense to acquire
        exclusive locks at the start of the transaction because then
        when multiple transactions try to act on the same data, they
        automatically get serialized. Each transaction waits its
        turn to acquire the lock and avoids getting into deadlock
        situations.
    
        Because the exclusive lock hint is just a hint, it shouldn't
        be considered equivalent to a mutex. In other words, you
        shouldn't use Spanner exclusive locks as a mutual exclusion
        mechanism for the execution of code outside of Spanner.
    
        **Note:** Request exclusive locks judiciously because they
        block others from reading that data for the entire
        transaction, rather than just when the writes are being
        performed. Unless you observe high write contention, you
        should use the default of shared read locks so you don't
        prematurely block other clients from reading the data that
        you're writing to.
    

### [OrderBy](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ReadRequest.OrderBy)

An option to control the order in which rows are returned from a read.
    
    
        `ORDER_BY_UNSPECIFIED` is equivalent to
        `ORDER_BY_PRIMARY_KEY`.
    ORDER_BY_PRIMARY_KEY (1):
        Read rows are returned in primary key order.
    
        In the event that this option is used in conjunction with
        the `partition_token` field, the API returns an
        `INVALID_ARGUMENT` error.
    ORDER_BY_NO_ORDER (2):
        Read rows are returned in any order.
    

### [RecipeList](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RecipeList)

A `RecipeList` contains a list of `KeyRecipe`\ s, which share the same schema generation.

### [RequestOptions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RequestOptions)

Common request options for various APIs.

### [ClientContext](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RequestOptions.ClientContext)

Container for various pieces of client-owned context attached to a request.

### [SecureContextEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RequestOptions.ClientContext.SecureContextEntry)

The abstract base class for a message.

### [Priority](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RequestOptions.Priority)

The relative priority for requests. Note that priority isn't applicable for `BeginTransaction][google.spanner.v1.Spanner.BeginTransaction]`.

The priority acts as a hint to the Cloud Spanner scheduler and doesn't guarantee priority or order of execution. For example:

  * Some parts of a write operation always execute at `PRIORITY_HIGH`, regardless of the specified priority. This can cause you to see an increase in high priority workload even when executing a low priority request. This can also potentially cause a priority inversion where a lower priority request is fulfilled ahead of a higher priority request.
  * If a transaction contains multiple operations with different priorities, Cloud Spanner doesn't guarantee to process the higher priority operations first. There might be other constraints to satisfy, such as the order of operations.



### [ResultSet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ResultSet)

Results from `Read][google.spanner.v1.Spanner.Read]` or `ExecuteSql][google.spanner.v1.Spanner.ExecuteSql]`.

### [ResultSetMetadata](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ResultSetMetadata)

Metadata about a `ResultSet][google.spanner.v1.ResultSet]` or `PartialResultSet][google.spanner.v1.PartialResultSet]`.

### [ResultSetStats](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.ResultSetStats)

Additional statistics about a `ResultSet][google.spanner.v1.ResultSet]` or `PartialResultSet][google.spanner.v1.PartialResultSet]`.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [RollbackRequest](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RollbackRequest)

The request for `Rollback][google.spanner.v1.Spanner.Rollback]`.

### [RoutingHint](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RoutingHint)

`RoutingHint` can be optionally added to location-aware Spanner requests. It gives the server hints that can be used to route the request to an appropriate server, potentially significantly decreasing latency and improving throughput. To achieve improved performance, most fields must be filled in with accurate values.

The presence of a valid `RoutingHint` tells the server that the client is location-aware.

`RoutingHint` does not change the semantics of the request; it is purely a performance hint; the request will perform the same actions on the database's data as if `RoutingHint` were not present. However, if the `RoutingHint` is incomplete or incorrect, the response may include a `CacheUpdate` the client can use to correct its location cache.

### [SkippedTablet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.RoutingHint.SkippedTablet)

A tablet that was skipped by the client. See `Tablet.tablet_uid` and `Tablet.incarnation`.

### [Session](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Session)

A session in the Cloud Spanner API.

### [LabelsEntry](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Session.LabelsEntry)

The abstract base class for a message.

### [StructType](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.StructType)

`StructType` defines the fields of a `STRUCT][google.spanner.v1.TypeCode.STRUCT]` type.

### [Field](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.StructType.Field)

Message representing a single field of a struct.

### [Tablet](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Tablet)

A `Tablet` represents a single replica of a `Group`. A tablet is served by a single server at a time, and can move between servers due to server death or simply load balancing.

### [Role](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Tablet.Role)

Indicates the role of the tablet.

### [Transaction](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Transaction)

A transaction.

### [TransactionOptions](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TransactionOptions)

Options to use for transactions.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [IsolationLevel](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TransactionOptions.IsolationLevel)

`IsolationLevel` is used when setting the `isolation level <https://cloud.google.com/spanner/docs/isolation-levels>`__ for a transaction.
    
    
        If the value is not specified, the `SERIALIZABLE`
        isolation level is used.
    SERIALIZABLE (1):
        All transactions appear as if they executed in a serial
        order, even if some of the reads, writes, and other
        operations of distinct transactions actually occurred in
        parallel. Spanner assigns commit timestamps that reflect the
        order of committed transactions to implement this property.
        Spanner offers a stronger guarantee than serializability
        called external consistency. For more information, see
        `TrueTime and external
        consistency <https://cloud.google.com/spanner/docs/true-time-external-consistency#serializability>`__.
    REPEATABLE_READ (2):
        All reads performed during the transaction observe a
        consistent snapshot of the database, and the transaction is
        only successfully committed in the absence of conflicts
        between its updates and any concurrent updates that have
        occurred since that snapshot. Consequently, in contrast to
        `SERIALIZABLE` transactions, only write-write conflicts
        are detected in snapshot transactions.
    
        This isolation level does not support read-only and
        partitioned DML transactions.
    
        When `REPEATABLE_READ` is specified on a read-write
        transaction, the locking semantics default to
        `OPTIMISTIC`.
    

### [PartitionedDml](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TransactionOptions.PartitionedDml)

Message type to initiate a Partitioned DML transaction.

### [ReadOnly](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TransactionOptions.ReadOnly)

Message type to initiate a read-only transaction.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [ReadWrite](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TransactionOptions.ReadWrite)

Message type to initiate a read-write transaction. Currently this transaction type has no options.

### [ReadLockMode](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TransactionOptions.ReadWrite.ReadLockMode)

`ReadLockMode` is used to set the read lock mode for read-write transactions.
    
    
        - If isolation level is
          `SERIALIZABLE][google.spanner.v1.TransactionOptions.IsolationLevel.SERIALIZABLE]`,
          locking semantics default to `PESSIMISTIC`.
        - If isolation level is
          `REPEATABLE_READ][google.spanner.v1.TransactionOptions.IsolationLevel.REPEATABLE_READ]`,
          locking semantics default to `OPTIMISTIC`.
        - See `Concurrency
          control <https://cloud.google.com/spanner/docs/concurrency-control>`__
          for more details.
    PESSIMISTIC (1):
        Pessimistic lock mode.
    
        Lock acquisition behavior depends on the isolation level in
        use. In
        `SERIALIZABLE][google.spanner.v1.TransactionOptions.IsolationLevel.SERIALIZABLE]`
        isolation, reads and writes acquire necessary locks during
        transaction statement execution. In
        `REPEATABLE_READ][google.spanner.v1.TransactionOptions.IsolationLevel.REPEATABLE_READ]`
        isolation, reads that explicitly request to be locked and
        writes acquire locks. See `Concurrency
        control <https://cloud.google.com/spanner/docs/concurrency-control>`__
        for details on the types of locks acquired at each
        transaction step.
    OPTIMISTIC (2):
        Optimistic lock mode.
    
        Lock acquisition behavior depends on the isolation level in
        use. In both
        `SERIALIZABLE][google.spanner.v1.TransactionOptions.IsolationLevel.SERIALIZABLE]`
        and
        `REPEATABLE_READ][google.spanner.v1.TransactionOptions.IsolationLevel.REPEATABLE_READ]`
        isolation, reads and writes do not acquire locks during
        transaction statement execution. See `Concurrency
        control <https://cloud.google.com/spanner/docs/concurrency-control>`__
        for details on how the guarantees of each isolation level
        are provided at commit time.
    

### [TransactionSelector](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TransactionSelector)

This message is used to select the transaction in which a `Read][google.spanner.v1.Spanner.Read]` or `ExecuteSql][google.spanner.v1.Spanner.ExecuteSql]` call runs.

See `TransactionOptions][google.spanner.v1.TransactionOptions]` for more information about transactions.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

### [Type](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.Type)

`Type` indicates the type of a Cloud Spanner value, as might be stored in a table cell or returned from an SQL query.

### [TypeAnnotationCode](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TypeAnnotationCode)

`TypeAnnotationCode` is used as a part of `Type][google.spanner.v1.Type]` to disambiguate SQL types that should be used for a given Cloud Spanner value. Disambiguation is needed because the same Cloud Spanner type can be mapped to different SQL types depending on SQL dialect. TypeAnnotationCode doesn't affect the way value is serialized.

### [TypeCode](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.types.TypeCode)

`TypeCode` is used as part of `Type][google.spanner.v1.Type]` to indicate the type of a Cloud Spanner value.

Each legal value of a type can be encoded to or decoded from a JSON value, using the encodings described below. All Cloud Spanner values can be `null`, regardless of type; `null`\ s are always encoded as a JSON `null`.
    
    
        If the schema has the column option
        `allow_commit_timestamp=true`, the placeholder string
        `"spanner.commit_timestamp()"` can be used to instruct the
        system to insert the commit timestamp associated with the
        transaction commit.
    DATE (5):
        Encoded as `string` in RFC 3339 date format.
    STRING (6):
        Encoded as `string`.
    BYTES (7):
        Encoded as a base64-encoded `string`, as described in RFC
        4648, section 4.
    ARRAY (8):
        Encoded as `list`, where the list elements are represented
        according to
        `array_element_type][google.spanner.v1.Type.array_element_type]`.
    STRUCT (9):
        Encoded as `list`, where list element `i` is represented
        according to
        [struct_type.fields[i]][google.spanner.v1.StructType.fields].
    NUMERIC (10):
        Encoded as `string`, in decimal format or scientific
        notation format. Decimal format: `[+-]Digits[.[Digits]]`
        or `[+-][Digits].Digits`
    
        Scientific notation:
        `[+-]Digits[.[Digits]][ExponentIndicator[+-]Digits]` or
        `[+-][Digits].Digits[ExponentIndicator[+-]Digits]`
        (ExponentIndicator is `"e"` or `"E"`)
    JSON (11):
        Encoded as a JSON-formatted `string` as described in RFC
        7159. The following rules are applied when parsing JSON
        input:
    
        - Whitespace characters are not preserved.
        - If a JSON object has duplicate keys, only the first key is
          preserved.
        - Members of a JSON object are not guaranteed to have their
          order preserved.
        - JSON array elements will have their order preserved.
    PROTO (13):
        Encoded as a base64-encoded `string`, as described in RFC
        4648, section 4.
    ENUM (14):
        Encoded as `string`, in decimal format.
    INTERVAL (16):
        Encoded as `string`, in `ISO8601` duration format -
        `P[n]Y[n]M[n]DT[n]H[n]M[n[.fraction]]S` where `n` is an
        integer. For example, `P1Y2M3DT4H5M6.5S` represents time
        duration of 1 year, 2 months, 3 days, 4 hours, 5 minutes,
        and 6.5 seconds.
    UUID (17):
        Encoded as `string`, in lower-case hexa-decimal format, as
        described in RFC 9562, section 4.
    

## Modules 

### [pagers](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.services.database_admin.pagers)

API documentation for `spanner_admin_database_v1.services.database_admin.pagers` module.

### [pagers](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_instance_v1.services.instance_admin.pagers)

API documentation for `spanner_admin_instance_v1.services.instance_admin.pagers` module.

### [batch](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.batch)

Context manager for Cloud Spanner batched writes.

### [client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client)

Parent client for calling the Cloud Spanner API.

This is the base from which all interactions with the API occur.

In the hierarchy of API concepts

  * a [Client](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.client.Client) owns an [Instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance)
  * a [Instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance.Instance) owns a [Database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database.Database)



### [database](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.database)

User-friendly container for Cloud Spanner Database.

### [instance](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.instance)

User friendly container for Cloud Spanner Instance.

### [keyset](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.keyset)

Wrap representation of Spanner keys / ranges.

### [pool](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.pool)

Pools managing shared Session objects.

### [pagers](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.services.spanner.pagers)

API documentation for `spanner_v1.services.spanner.pagers` module.

### [session](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.session)

Wrapper for Cloud Spanner Session objects.

### [snapshot](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.snapshot)

Model a set of read-only queries to a database as a snapshot.

### [streamed](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.streamed)

Wrapper for streaming results.

### [table](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.table)

User friendly container for Cloud Spanner Table.

### [transaction](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_v1.transaction)

Spanner read-write transaction support.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
