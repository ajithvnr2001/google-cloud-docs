---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceBackupProperties
title: Class BackupApplianceBackupProperties (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:47.524799+00:00
---

# Class BackupApplianceBackupProperties (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupApplianceBackupProperties

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupApplianceBackupProperties (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupApplianceBackupProperties(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

BackupApplianceBackupProperties represents BackupDR backup appliance's properties.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`generation_id` |  `int`   
Output only. The numeric generation ID of the backup (monotonically increasing). This field is a member of `oneof`_ `_generation_id`.   
`finalize_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. The time when this backup object was finalized (if none, backup is not finalized). This field is a member of `oneof`_ `_finalize_time`.   
`recovery_range_start_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The earliest timestamp of data available in this Backup. This field is a member of `oneof`_ `_recovery_range_start_time`.   
`recovery_range_end_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Optional. The latest timestamp of data available in this Backup. This field is a member of `oneof`_ `_recovery_range_end_time`.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
