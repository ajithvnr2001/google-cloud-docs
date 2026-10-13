---
url: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault.BackupRetentionPolicy
title: Class BackupRetentionPolicy (0.10.2) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:28:14.306842+00:00
---

# Class BackupRetentionPolicy (0.10.2)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/netapp/latest/google.cloud.netapp_v1.types.BackupVault.BackupRetentionPolicy

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupRetentionPolicy (0.10.2) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.2 (latest)  0.10.1  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.24  0.2.0  0.1.0 
    
    
    BackupRetentionPolicy(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Retention policy for backups in the backup vault

## Attributes  
  
---  
**Name** | **Description**  
`backup_minimum_enforced_retention_days` |  `int`   
Required. Minimum retention duration in days for backups in the backup vault.   
`daily_backup_immutable` |  `bool`   
Optional. Indicates if the daily backups are immutable. At least one of daily_backup_immutable, weekly_backup_immutable, monthly_backup_immutable and manual_backup_immutable must be true.   
`weekly_backup_immutable` |  `bool`   
Optional. Indicates if the weekly backups are immutable. At least one of daily_backup_immutable, weekly_backup_immutable, monthly_backup_immutable and manual_backup_immutable must be true.   
`monthly_backup_immutable` |  `bool`   
Optional. Indicates if the monthly backups are immutable. At least one of daily_backup_immutable, weekly_backup_immutable, monthly_backup_immutable and manual_backup_immutable must be true.   
`manual_backup_immutable` |  `bool`   
Optional. Indicates if the manual backups are immutable. At least one of daily_backup_immutable, weekly_backup_immutable, monthly_backup_immutable and manual_backup_immutable must be true.   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
