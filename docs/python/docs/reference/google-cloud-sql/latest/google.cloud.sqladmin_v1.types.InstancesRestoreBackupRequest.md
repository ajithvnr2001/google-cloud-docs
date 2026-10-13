---
url: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.InstancesRestoreBackupRequest
title: Class InstancesRestoreBackupRequest (0.1.1) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:19:38.441578+00:00
---

# Class InstancesRestoreBackupRequest (0.1.1)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.InstancesRestoreBackupRequest

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InstancesRestoreBackupRequest (0.1.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.1.1 (latest)  0.1.0 
    
    
    InstancesRestoreBackupRequest(
        mapping=None, *, ignore_unknown_fields=False, **kwargs
    )

Database instance restore backup request.

## Attributes  
  
---  
**Name** | **Description**  
`restore_backup_context` |  `[google.cloud.sqladmin_v1.types.RestoreBackupContext](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.RestoreBackupContext)`   
Parameters required to perform the restore backup operation.   
`backup` |  `str`   
The name of the backup that's used to restore a Cloud SQL instance: Format: projects/{project-id}/backups/{backup-uid}. Only one of restore_backup_context, backup, backupdr_backup can be passed to the input.   
`backupdr_backup` |  `str`   
The name of the backup that's used to restore a Cloud SQL instance: Format: "projects/{project-id}/locations/{location}/backupVaults/{backupvault}/dataSources/{datasource}/backups/{backup-uid}". Only one of restore_backup_context, backup, backupdr_backup can be passed to the input.   
`restore_instance_settings` |  `[google.cloud.sqladmin_v1.types.DatabaseInstance](https://docs.cloud.google.com/python/docs/reference/google-cloud-sql/latest/google.cloud.sqladmin_v1.types.DatabaseInstance)`   
Optional. By using this parameter, Cloud SQL overrides any instance settings stored in the backup you are restoring from. You can't change the instance's major database version and you can only increase the disk size. You can use this field to restore new instances only. This field is not applicable for restore to existing instances.   
`restore_instance_clear_overrides_field_names` |  `MutableSequence[str]`   
Optional. This field has the same purpose as restore_instance_settings, changes any instance settings stored in the backup you are restoring from. With the difference that these fields are cleared in the settings.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
