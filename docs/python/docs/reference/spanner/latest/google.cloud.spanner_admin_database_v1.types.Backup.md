---
url: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup
title: Class Backup (3.71.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:03:43.671060+00:00
---

# Class Backup (3.71.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Backup (3.71.0) Stay organized with collections  Save and categorize content based on your preferences. 

3.71.0 (latest)  3.70.0  3.69.1  3.68.0  3.67.0  3.66.0  3.65.0  3.64.0  3.63.0  3.62.0  3.61.0  3.60.0  3.59.0  3.58.0  3.57.0  3.56.0  3.55.0  3.54.0  3.53.0  3.52.0  3.51.0  3.50.1  3.46.0  3.45.0  3.44.0  3.43.0  3.42.0  3.41.0  3.40.1  3.39.0  3.38.0  3.37.0  3.36.0  3.35.1  3.34.0  3.33.0  3.32.0  3.31.0  3.30.0  3.29.0  3.28.0  3.27.1  3.26.0  3.25.0  3.24.0  3.23.0  3.22.2  3.21.0  3.20.0  3.19.0  3.18.0  3.17.0  3.16.0  3.15.1  3.14.1  3.13.0  3.12.1  3.11.1  3.10.0  3.9.0  3.8.0  3.7.0  3.6.0  3.5.0  3.4.0  3.3.0  3.2.0  3.1.0  3.0.0  2.1.1  2.0.0  1.19.3  1.18.0  1.17.1  1.16.0  1.15.1  1.14.0  1.13.0  1.12.0  1.11.0  1.10.0 
    
    
    Backup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A backup of a Cloud Spanner database.

## Attributes  
  
---  
**Name** | **Description**  
`database` |  `str`   
Required for the `CreateBackup][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup]` operation. Name of the database from which this backup was created. This needs to be in the same instance as the backup. Values are of the form `projects/`.   
`version_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
The backup will contain an externally consistent copy of the database at the timestamp specified by `version_time`. If `version_time` is not specified, the system will set `version_time` to the `create_time` of the backup.   
`expire_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required for the `CreateBackup][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup]` operation. The expiration time of the backup, with microseconds granularity that must be at least 6 hours and at most 366 days from the time the CreateBackup request is processed. Once the `expire_time` has passed, the backup is eligible to be automatically deleted by Cloud Spanner to free the resources used by the backup.   
`name` |  `str`   
Output only for the `CreateBackup][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup]` operation. Required for the `UpdateBackup][google.spanner.admin.database.v1.DatabaseAdmin.UpdateBackup]` operation. A globally unique identifier for the backup which cannot be changed. Values are of the form `projects/` The final segment of the name must be between 2 and 60 characters in length. The backup is stored in the location(s) specified in the instance configuration of the instance containing the backup, identified by the prefix of the backup name of the form `projects/`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time the `CreateBackup][google.spanner.admin.database.v1.DatabaseAdmin.CreateBackup]` request is received. If the request does not specify `version_time`, the `version_time` of the backup will be equivalent to the `create_time`.   
`size_bytes` |  `int`   
Output only. Size of the backup in bytes.   
`freeable_size_bytes` |  `int`   
Output only. The number of bytes that will be freed by deleting this backup. This value will be zero if, for example, this backup is part of an incremental backup chain and younger backups in the chain require that we keep its data. For backups not in an incremental backup chain, this is always the size of the backup. This value may change if backups on the same chain get created, deleted or expired.   
`exclusive_size_bytes` |  `int`   
Output only. For a backup in an incremental backup chain, this is the storage space needed to keep the data that has changed since the previous backup. For all other backups, this is always the size of the backup. This value may change if backups on the same chain get deleted or expired. This field can be used to calculate the total storage space used by a set of backups. For example, the total space used by all backups of a database can be computed by summing up this field.   
`state` |  `[google.cloud.spanner_admin_database_v1.types.Backup.State](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.Backup.State)`   
Output only. The current state of the backup.   
`referencing_databases` |  `MutableSequence[str]`   
Output only. The names of the restored databases that reference the backup. The database names are of the form `projects/`. Referencing databases may exist in different instances. The existence of any referencing database prevents the backup from being deleted. When a restored database from the backup enters the `READY` state, the reference to the backup is removed.   
`encryption_info` |  `[google.cloud.spanner_admin_database_v1.types.EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.EncryptionInfo)`   
Output only. The encryption information for the backup.   
`encryption_information` |  `MutableSequence[[google.cloud.spanner_admin_database_v1.types.EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.EncryptionInfo)]`   
Output only. The encryption information for the backup, whether it is protected by one or more KMS keys. The information includes all Cloud KMS key versions used to encrypt the backup. The `encryption_status' field inside of each`\ EncryptionInfo\\` is not populated. At least one of the key versions must be available for the backup to be restored. If a key version is revoked in the middle of a restore, the restore behavior is undefined.   
`database_dialect` |  `[google.cloud.spanner_admin_database_v1.types.DatabaseDialect](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.DatabaseDialect)`   
Output only. The database dialect information for the backup.   
`referencing_backups` |  `MutableSequence[str]`   
Output only. The names of the destination backups being created by copying this source backup. The backup names are of the form `projects/`. Referencing backups may exist in different instances. The existence of any referencing backup prevents the backup from being deleted. When the copy operation is done (either successfully completed or cancelled or the destination backup is deleted), the reference to the backup is removed.   
`max_expire_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The max allowed expiration time of the backup, with microseconds granularity. A backup's expiration time can be configured in multiple APIs: CreateBackup, UpdateBackup, CopyBackup. When updating or copying an existing backup, the expiration time specified must be less than `Backup.max_expire_time`.   
`backup_schedules` |  `MutableSequence[str]`   
Output only. List of backup schedule URIs that are associated with creating this backup. This is only applicable for scheduled backups, and is empty for on-demand backups. To optimize for storage, whenever possible, multiple schedules are collapsed together to create one backup. In such cases, this field captures the list of all backup schedule URIs that are associated with creating this backup. If collapsing is not done, then this field captures the single backup schedule URI associated with creating this backup.   
`incremental_backup_chain_id` |  `str`   
Output only. Populated only for backups in an incremental backup chain. Backups share the same chain id if and only if they belong to the same incremental backup chain. Use this field to determine which backups are part of the same incremental backup chain. The ordering of backups in the chain can be determined by ordering the backup `version_time`.   
`oldest_version_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Data deleted at a time older than this is guaranteed not to be retained in order to support this backup. For a backup in an incremental backup chain, this is the version time of the oldest backup that exists or ever existed in the chain. For all other backups, this is the version time of the backup. This field can be used to understand what data is being retained by the backup system.   
`instance_partitions` |  `MutableSequence[[google.cloud.spanner_admin_database_v1.types.BackupInstancePartition](https://docs.cloud.google.com/python/docs/reference/spanner/latest/google.cloud.spanner_admin_database_v1.types.BackupInstancePartition)]`   
Output only. The instance partition(s) storing the backup. This is the same as the list of the instance partition(s) that the database had footprint in at the backup's `version_time`.   
  
## Classes 

### State
    
    
    State(value)

Indicates the current state of the backup.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
