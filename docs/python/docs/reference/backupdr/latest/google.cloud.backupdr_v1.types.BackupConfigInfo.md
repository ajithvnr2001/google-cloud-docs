---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigInfo
title: Class BackupConfigInfo (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:48.599412+00:00
---

# Class BackupConfigInfo (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigInfo

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupConfigInfo (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupConfigInfo(mapping=None, *, ignore_unknown_fields=False, **kwargs)

BackupConfigInfo has information about how the resource is configured for Backup and about the most recent backup to this vault.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`last_backup_state` |  `[google.cloud.backupdr_v1.types.BackupConfigInfo.LastBackupState](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigInfo.LastBackupState)`   
Output only. The status of the last backup to this BackupVault   
`last_successful_backup_consistency_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. If the last backup were successful, this field has the consistency date.   
`last_backup_error` |  `google.rpc.status_pb2.Status`   
Output only. If the last backup failed, this field has the error message.   
`gcp_backup_config` |  `[google.cloud.backupdr_v1.types.GcpBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.GcpBackupConfig)`   
Configuration for a Google Cloud resource. This field is a member of `oneof`_ `backup_config`.   
`backup_appliance_backup_config` |  `[google.cloud.backupdr_v1.types.BackupApplianceBackupConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceBackupConfig)`   
Configuration for an application backed up by a Backup Appliance. This field is a member of `oneof`_ `backup_config`.   
  
## Classes 

### LastBackupState
    
    
    LastBackupState(value)

LastBackupstate tracks whether the last backup was not yet started, successful, failed, or could not be run because of the lack of permissions.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
