---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupLock
title: Class BackupLock (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:38.817162+00:00
---

# Class BackupLock (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupLock

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupLock (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupLock(mapping=None, *, ignore_unknown_fields=False, **kwargs)

BackupLock represents a single lock on a Backup resource. An unexpired lock on a Backup prevents the Backup from being deleted.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`backup_appliance_lock_info` |  `[google.cloud.backupdr_v1beta.types.BackupApplianceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.BackupApplianceLockInfo)`   
If the client is a backup and recovery appliance, this contains metadata about why the lock exists. This field is a member of `oneof`_ `ClientLockInfo`.   
`service_lock_info` |  `[google.cloud.backupdr_v1beta.types.ServiceLockInfo](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1beta.types.ServiceLockInfo)`   
Output only. Contains metadata about the lock exist for Google Cloud native backups. This field is a member of `oneof`_ `ClientLockInfo`.   
`lock_until_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Required. The time after which this lock is not considered valid and will no longer protect the Backup from deletion.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
