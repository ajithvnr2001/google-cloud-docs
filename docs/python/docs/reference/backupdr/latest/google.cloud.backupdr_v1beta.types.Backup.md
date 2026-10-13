---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup
title: Class Backup (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:08:28.657832+00:00
---

# Class Backup (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Backup (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    Backup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing a Backup object.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`compute_instance_backup_properties` |  `[google.cloud.backupdr_v1beta.types.ComputeInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ComputeInstanceBackupProperties)`   
Output only. Compute Engine specific backup properties. This field is a member of `oneof`_ `backup_properties`.   
`cloud_sql_instance_backup_properties` |  `[google.cloud.backupdr_v1beta.types.CloudSqlInstanceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.CloudSqlInstanceBackupProperties)`   
Output only. Cloud SQL specific backup properties. This field is a member of `oneof`_ `backup_properties`.   
`backup_appliance_backup_properties` |  `[google.cloud.backupdr_v1beta.types.BackupApplianceBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupApplianceBackupProperties)`   
Output only. Backup Appliance specific backup properties. This field is a member of `oneof`_ `backup_properties`.   
`alloy_db_backup_properties` |  `[google.cloud.backupdr_v1beta.types.AlloyDbClusterBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.AlloyDbClusterBackupProperties)`   
Output only. AlloyDB specific backup properties. This field is a member of `oneof`_ `backup_properties`.   
`disk_backup_properties` |  `[google.cloud.backupdr_v1beta.types.DiskBackupProperties](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.DiskBackupProperties)`   
Output only. Disk specific backup properties. This field is a member of `oneof`_ `backup_properties`.   
`gcp_backup_plan_info` |  `[google.cloud.backupdr_v1beta.types.Backup.GCPBackupPlanInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup.GCPBackupPlanInfo)`   
Output only. Configuration for a Google Cloud resource. This field is a member of `oneof`_ `plan_info`.   
`gcp_resource` |  `[google.cloud.backupdr_v1beta.types.BackupGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupGcpResource)`   
Output only. Unique identifier of the GCP resource that is being backed up. This field is a member of `oneof`_ `source_resource`.   
`name` |  `str`   
Output only. Identifier. Name of the backup to create. It must have the format\ `"projects/`. `{backup}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the datasource.   
`description` |  `str`   
Output only. The description of the Backup instance (2048 characters or less). This field is a member of `oneof`_ `_description`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was created. This field is a member of `oneof`_ `_create_time`.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was updated. This field is a member of `oneof`_ `_update_time`.   
`labels` |  `MutableMapping[str, str]`   
Optional. Resource labels to represent user provided metadata. No labels currently defined.   
`enforced_retention_end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The backup can not be deleted before this time. This field is a member of `oneof`_ `_enforced_retention_end_time`.   
`backup_retention_inheritance` |  `[google.cloud.backupdr_v1beta.types.BackupVault.BackupRetentionInheritance](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.BackupRetentionInheritance)`   
Output only. Setting for how the enforced retention end time is inherited. This value is copied from this backup's BackupVault. This field is a member of `oneof`_ `_backup_retention_inheritance`.   
`expire_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. When this backup is automatically expired. This field is a member of `oneof`_ `_expire_time`.   
`consistency_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The point in time when this backup was captured from the source. This field is a member of `oneof`_ `_consistency_time`.   
`etag` |  `str`   
Optional. Server specified ETag to prevent updates from overwriting each other. This field is a member of `oneof`_ `_etag`.   
`state` |  `[google.cloud.backupdr_v1beta.types.Backup.State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup.State)`   
Output only. The Backup resource instance state.   
`service_locks` |  `MutableSequence[[google.cloud.backupdr_v1beta.types.BackupLock](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupLock)]`   
Output only. The list of BackupLocks taken by the service to prevent the deletion of the backup.   
`backup_appliance_locks` |  `MutableSequence[[google.cloud.backupdr_v1beta.types.BackupLock](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupLock)]`   
Optional. The list of BackupLocks taken by the accessor Backup Appliance.   
`backup_type` |  `[google.cloud.backupdr_v1beta.types.Backup.BackupType](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.Backup.BackupType)`   
Output only. Type of the backup, unspecified, scheduled or ondemand.   
`resource_size_bytes` |  `int`   
Output only. source resource size in bytes at the time of the backup.   
`satisfies_pzs` |  `bool`   
Optional. Output only. Reserved for future use. This field is a member of `oneof`_ `_satisfies_pzs`.   
`satisfies_pzi` |  `bool`   
Optional. Output only. Reserved for future use. This field is a member of `oneof`_ `_satisfies_pzi`.   
`kms_key_versions` |  `MutableSequence[str]`   
Optional. Output only. The list of KMS key versions used to encrypt the backup.   
  
## Classes 

### BackupType
    
    
    BackupType(value)

Type of the backup, scheduled or ondemand.

### GCPBackupPlanInfo
    
    
    GCPBackupPlanInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

GCPBackupPlanInfo captures the plan configuration details of Google Cloud resources at the time of backup.

### LabelsEntry
    
    
    LabelsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

The abstract base class for a message.

**Parameters**  
---  
**Name** | **Description**  
`kwargs` |  `dict`   
Keys and values corresponding to the fields of the message.  
`mapping` |  `Union[dict, `.Message`]`   
A dictionary or message to be used to determine the values for this message.  
`ignore_unknown_fields` |  `Optional(bool)`   
If True, do not raise errors for unknown fields. Only applied if `mapping` is a mapping type or there are keyword parameters.  
  
### State
    
    
    State(value)

Holds the state of the backup resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
