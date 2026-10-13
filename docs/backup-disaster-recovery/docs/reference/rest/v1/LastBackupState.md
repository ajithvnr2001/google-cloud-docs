---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/LastBackupState/
title: LastBackupState \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:51:01.139746+00:00
---

# LastBackupState  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/rest/v1/LastBackupState/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Reference ](https://docs.cloud.google.com/backup-disaster-recovery/docs/reference/reference)



Send feedback 

#  LastBackupState Stay organized with collections  Save and categorize content based on your preferences. 

LastBackupstate tracks whether the last backup was not yet started, successful, failed, or could not be run because of the lack of permissions.

Enums  
---  
`LAST_BACKUP_STATE_UNSPECIFIED` | Status not set.  
`FIRST_BACKUP_PENDING` | The first backup has not yet completed  
`SUCCEEDED` | The most recent backup was successful  
`FAILED` | The most recent backup failed  
`PERMISSION_DENIED` | The most recent backup could not be run/failed because of the lack of permissions  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-08 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-08 UTC."],[],[]] 
