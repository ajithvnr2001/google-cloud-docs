---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup
title: Class Backup (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:13.305127+00:00
---

# Class Backup (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class Backup (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    Backup(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A NetApp Backup.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the backup. Format: `projects/{project_id}/locations/{location}/backupVaults/{backup_vault_id}/backups/{backup_id}`.   
`state` |  `[google.cloud.netapp_v1.types.Backup.State](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup.State)`   
Output only. The backup state.   
`description` |  `str`   
A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected.   
`volume_usage_bytes` |  `int`   
Output only. Size of the file system when the backup was created. When creating a new volume from the backup, the volume capacity will have to be at least as big.   
`backup_type` |  `[google.cloud.netapp_v1.types.Backup.Type](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.Backup.Type)`   
Output only. Type of backup, manually created or created by a backup policy.   
`source_volume` |  `str`   
Volume full name of this backup belongs to. Either source_volume or ontap_source should be provided. Format: `projects/{projects_id}/locations/{location}/volumes/{volume_id}`  
`source_snapshot` |  `str`   
If specified, backup will be created from the given snapshot. If not specified, there will be a new snapshot taken to initiate the backup creation. Format: `projects/{project_id}/locations/{location}/volumes/{volume_id}/snapshots/{snapshot_id}` This field is a member of `oneof`_ `_source_snapshot`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the backup was created.   
`labels` |  `MutableMapping[str, str]`   
Resource labels to represent user provided metadata.   
`chain_storage_bytes` |  `int`   
Output only. Total size of all backups in a chain in bytes = baseline backup size + sum(incremental backup size)   
`satisfies_pzs` |  `bool`   
Output only. Reserved for future use   
`satisfies_pzi` |  `bool`   
Output only. Reserved for future use   
`volume_region` |  `str`   
Output only. Region of the volume from which the backup was created. Format: `projects/{project_id}/locations/{location}`  
`backup_region` |  `str`   
Output only. Region in which backup is stored. Format: `projects/{project_id}/locations/{location}`  
`enforced_retention_end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time until which the backup is not deletable.   
  
## Classes 

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

The Backup States

### Type
    
    
    Type(value)

Backup types.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
