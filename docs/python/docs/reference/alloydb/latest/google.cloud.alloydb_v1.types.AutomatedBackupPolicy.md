---
url: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.AutomatedBackupPolicy
title: Class AutomatedBackupPolicy (0.11.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:33:11.730829+00:00
---

# Class AutomatedBackupPolicy (0.11.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.AutomatedBackupPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class AutomatedBackupPolicy (0.11.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.11.3 (latest)  0.11.2  0.10.0  0.9.0  0.7.0  0.6.0  0.5.0  0.4.9  0.3.16  0.2.1  0.1.1 
    
    
    AutomatedBackupPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Message describing the user-specified automated backup policy. All fields in the automated backup policy are optional. Defaults for each field are provided if they are not set.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`weekly_schedule` |  `[google.cloud.alloydb_v1.types.AutomatedBackupPolicy.WeeklySchedule](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.AutomatedBackupPolicy.WeeklySchedule)`   
Weekly schedule for the Backup. This field is a member of `oneof`_ `schedule`.   
`time_based_retention` |  `[google.cloud.alloydb_v1.types.AutomatedBackupPolicy.TimeBasedRetention](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.AutomatedBackupPolicy.TimeBasedRetention)`   
Time-based Backup retention policy. This field is a member of `oneof`_ `retention`.   
`quantity_based_retention` |  `[google.cloud.alloydb_v1.types.AutomatedBackupPolicy.QuantityBasedRetention](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.AutomatedBackupPolicy.QuantityBasedRetention)`   
Quantity-based Backup retention policy to retain recent backups. This field is a member of `oneof`_ `retention`.   
`enabled` |  `bool`   
Whether automated automated backups are enabled. If not set, defaults to true. This field is a member of `oneof`_ `_enabled`.   
`backup_window` |  `google.protobuf.duration_pb2.Duration`   
The length of the time window during which a backup can be taken. If a backup does not succeed within this time window, it will be canceled and considered failed. The backup window must be at least 5 minutes long. There is no upper bound on the window. If not set, it defaults to 1 hour.   
`encryption_config` |  `[google.cloud.alloydb_v1.types.EncryptionConfig](https://docs.cloud.google.com/python/docs/reference/alloydb/latest/google.cloud.alloydb_v1.types.EncryptionConfig)`   
Optional. The encryption config can be specified to encrypt the backups with a customer-managed encryption key (CMEK). When this field is not specified, the backup will use the cluster's encryption config.   
`location` |  `str`   
The location where the backup will be stored. Currently, the only supported option is to store the backup in the same region as the cluster. If empty, defaults to the region of the cluster.   
`labels` |  `MutableMapping[str, str]`   
Labels to apply to backups created using this configuration.   
  
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
  
### QuantityBasedRetention
    
    
    QuantityBasedRetention(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A quantity based policy specifies that a certain number of the most recent successful backups should be retained.

### TimeBasedRetention
    
    
    TimeBasedRetention(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A time based retention policy specifies that all backups within a certain time period should be retained.

### WeeklySchedule
    
    
    WeeklySchedule(mapping=None, *, ignore_unknown_fields=False, **kwargs)

A weekly schedule starts a backup at prescribed start times within a day, for the specified days of the week.

The weekly schedule message is flexible and can be used to create many types of schedules. For example, to have a daily backup that starts at 22:00, configure the `start_times` field to have one element "22:00" and the `days_of_week` field to have all seven days of the week.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
