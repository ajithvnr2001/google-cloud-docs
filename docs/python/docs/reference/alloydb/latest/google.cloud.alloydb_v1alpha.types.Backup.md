---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.Backup
title: Class Backup (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:03:01.944145+00:00
---

# Class Backup (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.Backup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Backup (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    Backup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing Backup object

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. The name of the backup resource with the format: \- projects/{project}/locations/{region}/backups/{backup_id} where the cluster and backup ID segments should satisfy the regex expression `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`, e.g. 1-63 characters of lowercase letters, numbers, and dashes, starting with a letter, and ending with a letter or number. For more details see https://google.aip.dev/122. The prefix of the backup resource name is the name of the parent resource: \- projects/{project}/locations/{region}   
`display_name` |  `str`   
User-settable and human-readable display name for the Backup.   
`uid` |  `str`   
Output only. The system-generated UID of the resource. The UID is assigned when the resource is created, and it is retained until it is deleted.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Create time stamp   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Update time stamp Users should not infer any meaning from this field. Its value is generally unrelated to the timing of the backup creation operation.   
`delete_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Delete time stamp   
`create_completion_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp when the resource finished being created.   
`labels` |  `MutableMapping[str, str]`   
Labels as key value pairs   
`state` |  `[google.cloud.alloydb_v1alpha.types.Backup.State](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.Backup.State)`   
Output only. The current state of the backup.   
`type_` |  `[google.cloud.alloydb_v1alpha.types.Backup.Type](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.Backup.Type)`   
The backup type, which suggests the trigger for the backup.   
`description` |  `str`   
User-provided description of the backup.   
`cluster_uid` |  `str`   
Output only. The system-generated UID of the cluster which was used to create this resource.   
`cluster_name` |  `str`   
Required. The full resource name of the backup source cluster (e.g., projects/{project}/locations/{region}/clusters/{cluster_id}).   
`reconciling` |  `bool`   
Output only. Reconciling (https://google.aip.dev/128#reconciliation), if true, indicates that the service is actively updating the resource. This can happen due to user-triggered updates or system actions like failover or maintenance.   
`encryption_config` |  `[google.cloud.alloydb_v1alpha.types.EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.EncryptionConfig)`   
Optional. The encryption config can be specified to encrypt the backup with a customer-managed encryption key (CMEK). When this field is not specified, the backup will then use default encryption scheme to protect the user data.   
`encryption_info` |  `[google.cloud.alloydb_v1alpha.types.EncryptionInfo](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.EncryptionInfo)`   
Output only. The encryption information for the backup.   
`etag` |  `str`   
For Resource freshness validation (https://google.aip.dev/154)   
`annotations` |  `MutableMapping[str, str]`   
Annotations to allow client tools to store small amount of arbitrary data. This is distinct from labels. https://google.aip.dev/128   
`size_bytes` |  `int`   
Output only. The size of the backup in bytes.   
`expiry_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time at which after the backup is eligible to be garbage collected. It is the duration specified by the backup's retention policy, added to the backup's create_time.   
`expiry_quantity` |  `[google.cloud.alloydb_v1alpha.types.Backup.QuantityBasedExpiry](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.Backup.QuantityBasedExpiry)`   
Output only. The QuantityBasedExpiry of the backup, specified by the backup's retention policy. Once the expiry quantity is over retention, the backup is eligible to be garbage collected.   
`satisfies_pzi` |  `bool`   
Output only. Reserved for future use.   
`satisfies_pzs` |  `bool`   
Output only. Reserved for future use.   
`database_version` |  `[google.cloud.alloydb_v1alpha.types.DatabaseVersion](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1alpha.types.DatabaseVersion)`   
Output only. The database engine major version of the cluster this backup was created from. Any restored cluster created from this backup will have the same database version.   
`tags` |  `MutableMapping[str, str]`   
Optional. Input only. Immutable. Tag keys/values directly bound to this resource. For example: :: "123/environment": "production", "123/costCenter": "marketing".   
  
## Classes 

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
  
### QuantityBasedExpiry
    
    
    QuantityBasedExpiry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A backup's position in a quantity-based retention queue, of backups with the same source cluster and type, with length, retention, specified by the backup's retention policy. Once the position is greater than the retention, the backup is eligible to be garbage collected.

Example: 5 backups from the same source cluster and type with a quantity-based retention of 3 and denoted by backup_id (position, retention).

Safe: backup_5 (1, 3), backup_4, (2, 3), backup_3 (3, 3). Awaiting garbage collection: backup_2 (4, 3), backup_1 (5, 3)

### State
    
    
    State(value)

Backup State

### TagsEntry
    
    
    TagsEntry(mapping=None, *, ignore_unknown_fields=False, **kwargs)

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
  
### Type
    
    
    Type(value)

Backup Type

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
