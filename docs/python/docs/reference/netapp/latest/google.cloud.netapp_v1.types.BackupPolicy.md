---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy
title: Class BackupPolicy (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:13.883389+00:00
---

# Class BackupPolicy (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupPolicy (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    BackupPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Backup Policy.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`name` |  `str`   
Identifier. The resource name of the backup policy. Format: `projects/{project_id}/locations/{location}/backupPolicies/{backup_policy_id}`.   
`daily_backup_limit` |  `int`   
Number of daily backups to keep. Note that the minimum daily backup limit is 2. This field is a member of `oneof`_ `_daily_backup_limit`.   
`weekly_backup_limit` |  `int`   
Number of weekly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1. This field is a member of `oneof`_ `_weekly_backup_limit`.   
`monthly_backup_limit` |  `int`   
Number of monthly backups to keep. Note that the sum of daily, weekly and monthly backups should be greater than 1. This field is a member of `oneof`_ `_monthly_backup_limit`.   
`description` |  `str`   
Description of the backup policy. This field is a member of `oneof`_ `_description`.   
`enabled` |  `bool`   
If enabled, make backups automatically according to the schedules. This will be applied to all volumes that have this policy attached and enforced on volume level. If not specified, default is true. This field is a member of `oneof`_ `_enabled`.   
`assigned_volume_count` |  `int`   
Output only. The total number of volumes assigned by this backup policy. This field is a member of `oneof`_ `_assigned_volume_count`.   
`create_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when the backup policy was created.   
`labels` |  `MutableMapping[str, str]`   
Resource labels to represent user provided metadata.   
`state` |  `[google.cloud.netapp_v1.types.BackupPolicy.State](https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupPolicy.State)`   
Output only. The backup policy state.   
  
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

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
