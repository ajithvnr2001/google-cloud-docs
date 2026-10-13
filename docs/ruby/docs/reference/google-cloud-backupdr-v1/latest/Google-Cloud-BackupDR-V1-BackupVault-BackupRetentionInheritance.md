---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-BackupRetentionInheritance/
title: Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance (v1.11.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:47:38.533203+00:00
---

# Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance (v1.11.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-backupdr-v1/latest/Google-Cloud-BackupDR-V1-BackupVault-BackupRetentionInheritance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Backup and DR Service V1 API - Module Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance (v1.11.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.11.2 (latest)  1.11.1  1.10.0  1.9.0  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.0  1.0.1  0.5.0  0.4.0  0.3.0  0.2.1  0.1.0 

Reference documentation and code samples for the Backup and DR Service V1 API module Google::Cloud::BackupDR::V1::BackupVault::BackupRetentionInheritance.

How a backup's enforced retention end time is inherited.

## Constants 

### BACKUP_RETENTION_INHERITANCE_UNSPECIFIED

**value:** 0  
Inheritance behavior not set. This will default to `INHERIT_VAULT_RETENTION`.

### INHERIT_VAULT_RETENTION

**value:** 1  
The enforced retention end time of a backup will be inherited from the backup vault's `backup_minimum_enforced_retention_duration` field.

This is the default behavior.

### MATCH_BACKUP_EXPIRE_TIME

**value:** 2  
The enforced retention end time of a backup will always match the expire time of the backup.

If this is set, the backup's enforced retention end time will be set to match the expire time during creation of the backup. When updating, the ERET and expire time must be updated together and have the same value. Invalid update requests will be rejected by the server.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-08-05 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-08-05 UTC."],[],[]] 
