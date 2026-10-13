---
url: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.BackupRetentionInheritance
title: Class BackupRetentionInheritance (0.10.3) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:23.451647+00:00
---

# Class BackupRetentionInheritance (0.10.3)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/backupdr/latest/google.cloud.backupdr_v1.types.BackupVault.BackupRetentionInheritance

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class BackupRetentionInheritance (0.10.3) Stay organized with collections  Save and categorize content based on your preferences. 

0.10.3 (latest)  0.10.2  0.9.0  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.5  0.1.7 
    
    
    BackupRetentionInheritance(value)

How a backup's enforced retention end time is inherited.
    
    
        This is the default behavior.
    MATCH_BACKUP_EXPIRE_TIME (2):
        The enforced retention end time of a backup
        will always match the expire time of the backup.
    
        If this is set, the backup's enforced retention
        end time will be set to match the expire time
        during creation of the backup. When updating,
        the ERET and expire time must be updated
        together and have the same value. Invalid update
        requests will be rejected by the server.
    

## Enums  
  
---  
**Name** | **Description**  
`BACKUP_RETENTION_INHERITANCE_UNSPECIFIED` | Inheritance behavior not set. This will default to `INHERIT_VAULT_RETENTION`.  
`INHERIT_VAULT_RETENTION` | The enforced retention end time of a backup will be inherited from the backup vault's `backup_minimum_enforced_retention_duration` field.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-04 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-04 UTC."],[],[]] 
