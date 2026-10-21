---
url: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/
title: REST Resource: backupRuns \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:14:15.275212+00:00
---

# REST Resource: backupRuns  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/postgres/apis)



Send feedback 

#  REST Resource: backupRuns Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: BackupRun
    * JSON representation
  * SqlBackupRunStatus
  * SqlBackupRunType
  * Methods



## Resource: BackupRun

A BackupRun resource.

JSON representation  
---  
      
    
    {
      "kind": string,
      "status": enum ([SqlBackupRunStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns#SqlBackupRunStatus)),
      "enqueuedTime": string,
      "id": string,
      "startTime": string,
      "endTime": string,
      "error": {
        object ([OperationError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/OperationError))
      },
      "type": enum ([SqlBackupRunType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns#SqlBackupRunType)),
      "description": string,
      "windowStartTime": string,
      "instance": string,
      "selfLink": string,
      "location": string,
      "databaseVersion": enum ([SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion)),
      "diskEncryptionConfiguration": {
        object ([DiskEncryptionConfiguration](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/DiskEncryptionConfiguration))
      },
      "diskEncryptionStatus": {
        object ([DiskEncryptionStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/DiskEncryptionStatus))
      },
      "backupKind": enum ([SqlBackupKind](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlBackupKind)),
      "timeZone": string,
      "maxChargeableBytes": string
    }  
  
Fields  
---  
`kind` |  `string` This is always `sql#backupRun`.  
`status` |  `enum (`[SqlBackupRunStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns#SqlBackupRunStatus)`)` The status of this run.  
`enqueuedTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the run was enqueued in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`id` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The identifier for this backup run. Unique only for a specific Cloud SQL instance.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the backup operation actually started in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the backup operation completed in UTC timezone in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`error` |  `object (`[OperationError](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/OperationError)`)` Information about why the backup operation failed. This is only present if the run has the FAILED status.  
`type` |  `enum (`[SqlBackupRunType](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns#SqlBackupRunType)`)` The type of this run; can be either "AUTOMATED" or "ON_DEMAND" or "FINAL". This field defaults to "ON_DEMAND" and is ignored, when specified for insert requests.  
`description` |  `string` The description of this run, only applicable to on-demand backups.  
`windowStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The start time of the backup window during which this the backup was attempted in [RFC 3339](https://tools.ietf.org/html/rfc3339) format, for example `2012-11-15T16:19:00.094Z`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`instance` |  `string` Name of the database instance.  
`selfLink` |  `string` The URI of this resource.  
`location` |  `string` Location of the backups.  
`databaseVersion` |  `enum (`[SqlDatabaseVersion](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlDatabaseVersion)`)` Output only. The instance database version at the time this backup was made.  
`diskEncryptionConfiguration` |  `object (`[DiskEncryptionConfiguration](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/DiskEncryptionConfiguration)`)` Encryption configuration specific to a backup.  
`diskEncryptionStatus` |  `object (`[DiskEncryptionStatus](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/DiskEncryptionStatus)`)` Encryption status specific to a backup.  
`backupKind` |  `enum (`[SqlBackupKind](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/SqlBackupKind)`)` Specifies the kind of backup, PHYSICAL or DEFAULT_SNAPSHOT.  
`timeZone` |  `string` Backup time zone to prevent restores to an instance with a different time zone. Now relevant only for SQL Server.  
`maxChargeableBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The maximum chargeable bytes for the backup.  
  
## SqlBackupRunStatus

The status of a backup run.

Enums  
---  
`SQL_BACKUP_RUN_STATUS_UNSPECIFIED` | The status of the run is unknown.  
`ENQUEUED` | The backup operation was enqueued.  
`OVERDUE` | The backup is overdue across a given backup window. Indicates a problem. Example: Long-running operation in progress during the whole window.  
`RUNNING` | The backup is in progress.  
`FAILED` | The backup failed.  
`SUCCESSFUL` | The backup was successful.  
`SKIPPED` | The backup was skipped (without problems) for a given backup window. Example: Instance was idle.  
`DELETION_PENDING` | The backup is about to be deleted.  
`DELETION_FAILED` | The backup deletion failed.  
`DELETED` | The backup has been deleted.  
  
## SqlBackupRunType

Type of backup (i.e. automated, on demand, etc).

Enums  
---  
`SQL_BACKUP_RUN_TYPE_UNSPECIFIED` | This is an unknown BackupRun type.  
`AUTOMATED` | The backup schedule automatically triggers a backup.  
`ON_DEMAND` | The user manually triggers a backup.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/delete)`

|  Deletes the backup taken by a backup run.  
  
### `[get](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/get)`

|  Retrieves a resource containing information about a backup run.  
  
### `[insert](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/insert)`

|  Creates a new backup run on demand.  
  
### `[list](https://docs.cloud.google.com/sql/docs/postgres/admin-api/rest/v1/backupRuns/list)`

|  Lists all backup runs associated with the project or a given instance and configuration in the reverse chronological order of the backup initiation time.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
