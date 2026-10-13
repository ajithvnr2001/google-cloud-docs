---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource
title: Class DataSource (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:54.688928+00:00
---

# Class DataSource (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class DataSource (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    DataSource(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing a DataSource object. Datasource object used to represent Datasource details for both admin and basic view.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Output only. Identifier. Name of the datasource to create. It must have the format\ `"projects/{project}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}"`. `{datasource}` cannot be changed after creation. It must be between 3-63 characters long and must be unique within the backup vault.   
`state` |  `[google.cloud.backupdr_v1.types.DataSource.State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSource.State)`   
Output only. The DataSource resource instance state.   
`labels` |  `MutableMapping[str, str]`   
Optional. Resource labels to represent user provided metadata. No labels currently defined:   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was created. This field is a member of `oneof`_ `_create_time`.   
`update_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the instance was updated. This field is a member of `oneof`_ `_update_time`.   
`backup_count` |  `int`   
Number of backups in the data source. This field is a member of `oneof`_ `_backup_count`.   
`etag` |  `str`   
Server specified ETag for the ManagementServer resource to prevent simultaneous updates from overwiting each other. This field is a member of `oneof`_ `_etag`.   
`total_stored_bytes` |  `int`   
The number of bytes (metadata and data) stored in this datasource. This field is a member of `oneof`_ `_total_stored_bytes`.   
`config_state` |  `[google.cloud.backupdr_v1.types.BackupConfigState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigState)`   
Output only. The backup configuration state.   
`backup_config_info` |  `[google.cloud.backupdr_v1.types.BackupConfigInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigInfo)`   
Output only. Details of how the resource is configured for backup.   
`data_source_gcp_resource` |  `[google.cloud.backupdr_v1.types.DataSourceGcpResource](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceGcpResource)`   
The backed up resource is a Google Cloud resource. The word 'DataSource' was included in the names to indicate that this is the representation of the Google Cloud resource used within the DataSource object. This field is a member of `oneof`_ `source_resource`.   
`data_source_backup_appliance_application` |  `[google.cloud.backupdr_v1.types.DataSourceBackupApplianceApplication](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.DataSourceBackupApplianceApplication)`   
The backed up resource is a backup appliance application. This field is a member of `oneof`_ `source_resource`.   
`backup_blocked_by_vault_access_restriction` |  `bool`   
Output only. This field is set to true if the backup is blocked by vault access restriction.   
  
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

Holds the state of the data source resource.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
