---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails
title: Class BackupConfigDetails (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:17:48.225811+00:00
---

# Class BackupConfigDetails (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupConfigDetails (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupConfigDetails(mapping=None, *, ignore_unknown_fields=False, **kwargs)

BackupConfigDetails has information about how the resource is configured for backups and about the most recent backup taken for this configuration.

This message has `oneof`_ fields (mutually exclusive fields). For each oneof, at most one member field can be set at the same time. Setting any member of the oneof automatically clears all other members.

.. _oneof: <https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields>

## Attributes  
  
---  
**Name** | **Description**  
`backup_config_source` |  `str`   
Output only. The full resource name of the backup config source resource. For example, "//backupdr.googleapis.com/v1/projects/{project}/locations/{region}/backupPlans/{backupplanId}" or "//compute.googleapis.com/projects/{project}/locations/{region}/resourcePolicies/{resourcePolicyId}".   
`backup_config_source_display_name` |  `str`   
Output only. The display name of the backup config source resource.   
`type_` |  `[google.cloud.backupdr_v1.types.BackupConfigDetails.Type](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails.Type)`   
Output only. The type of the backup config resource.   
`state` |  `[google.cloud.backupdr_v1.types.BackupConfigDetails.State](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupConfigDetails.State)`   
Output only. The state of the backup config resource.   
`pitr_settings` |  `[google.cloud.backupdr_v1.types.PitrSettings](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.PitrSettings)`   
Output only. Point in time recovery settings of the backup configuration resource.   
`latest_successful_backup_time` |  `google.protobuf.timestamp_pb2.Timestamp`   
Output only. Timestamp of the latest successful backup created via this backup configuration.   
`applicable_resource` |  `str`   
Output only. The `full resource name   
`backup_vault` |  `str`   
Output only. The `full resource name   
`backup_locations` |  `MutableSequence[[google.cloud.backupdr_v1.types.BackupLocation](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupLocation)]`   
The locations where the backups are to be stored.   
`backup_dr_plan_config` |  `[google.cloud.backupdr_v1.types.BackupDrPlanConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrPlanConfig)`   
Google Cloud Backup and DR's Backup Plan specific data. This field is a member of `oneof`_ `plan_specific_config`.   
`backup_dr_template_config` |  `[google.cloud.backupdr_v1.types.BackupDrTemplateConfig](https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupDrTemplateConfig)`   
Google Cloud Backup and DR's Template specific data. This field is a member of `oneof`_ `plan_specific_config`.   
  
## Classes 

### State
    
    
    State(value)

The state tells whether the backup config is active or not.

### Type
    
    
    Type(value)

Type of the backup configuration. This enum may receive new values in the future.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
