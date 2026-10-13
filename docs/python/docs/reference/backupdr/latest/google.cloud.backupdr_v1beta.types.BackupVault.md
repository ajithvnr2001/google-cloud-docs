---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault
title: Class BackupVault (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:55.642293+00:00
---

# Class BackupVault (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupVault (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupVault(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing a BackupVault object.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. Name of the backup vault to create. It must have the format\ `"projects/{project}/locations/{location}/backupVaults/{backupvault}"`. `{backupvault}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the project and location.   
`description` |  `str`   
Optional. The description of the BackupVault instance (2048 characters or less). This field is a member of `oneof`_ `_description`.   
`labels` |  `MutableMapping[str, str]`   
Optional. Resource labels to represent user provided metadata. No labels currently defined:   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was created. This field is a member of `oneof`_ `_create_time`.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was updated. This field is a member of `oneof`_ `_update_time`.   
`backup_minimum_enforced_retention_duration` |  `google.protobuf.duration_pb2.Duration`   
Required. The default and minimum enforced retention for each backup within the backup vault. The enforced retention for each backup can be extended. Note: Longer minimum enforced retention period impacts potential storage costs post introductory trial. We recommend starting with a short duration of 3 days or less. This field is a member of `oneof`_ `_backup_minimum_enforced_retention_duration`.   
`backup_retention_inheritance` |  `[google.cloud.backupdr_v1beta.types.BackupVault.BackupRetentionInheritance](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.BackupRetentionInheritance)`   
Optional. Setting for how a backup's enforced retention end time is inherited. This field is a member of `oneof`_ `_backup_retention_inheritance`.   
`deletable` |  `bool`   
Output only. Set to true when there are no backups nested under this resource. This field is a member of `oneof`_ `_deletable`.   
`etag` |  `str`   
Optional. Server specified ETag for the backup vault resource to prevent simultaneous updates from overwiting each other. This field is a member of `oneof`_ `_etag`.   
`state` |  `[google.cloud.backupdr_v1beta.types.BackupVault.State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.State)`   
Output only. The BackupVault resource instance state.   
`effective_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. Time after which the BackupVault resource is locked. This field is a member of `oneof`_ `_effective_time`.   
`backup_count` |  `int`   
Output only. The number of backups in this backup vault.   
`service_account` |  `str`   
Output only. Service account used by the BackupVault Service for this BackupVault. The user should grant this account permissions in their workload project to enable the service to run backups and restores there.   
`total_stored_bytes` |  `int`   
Output only. Total size of the storage used by all backup resources.   
`uid` |  `str`   
Output only. Immutable after resource creation until resource deletion.   
`annotations` |  `MutableMapping[str, str]`   
Optional. User annotations. See https://google.aip.dev/128#annotations Stores small amounts of arbitrary data.   
`access_restriction` |  `[google.cloud.backupdr_v1beta.types.BackupVault.AccessRestriction](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.AccessRestriction)`   
Optional. Restricts access to certain sources and destinations for data being sent into, or restored from, the backup vault. Defaults to WITHIN_ORGANIZATION if not provided during creation.   
`encryption_config` |  `[google.cloud.backupdr_v1beta.types.BackupVault.EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupVault.EncryptionConfig)`   
Optional. The encryption config of the backup vault. This field is a member of `oneof`_ `_encryption_config`.   
  
## Classes 

### AccessRestriction
    
    
    AccessRestriction(value)

Holds the access restriction for the backup vault.

### AnnotationsEntry
    
    
    AnnotationsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### BackupRetentionInheritance
    
    
    BackupRetentionInheritance(value)

How a backup's enforced retention end time is inherited.
    
    
        This is the default behavior.
    MATCH_BACKUP_EXPIRE_TIME (2):
        The enforced retention end time of a backup
        will always match the expire time of the backup.
    
        If this is set, the backup's enforced retention
        end time will be set to match the expire time
        during creation of the backup. When updating,
        the ERET and expire time must be updated
        together and have the same value. Invalid update
        requests will be rejected by the server.
    

### EncryptionConfig
    
    
    EncryptionConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing the EncryptionConfig of backup vault. This determines how data within the vault is encrypted at rest.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

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

Holds the state of the backup vault resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
