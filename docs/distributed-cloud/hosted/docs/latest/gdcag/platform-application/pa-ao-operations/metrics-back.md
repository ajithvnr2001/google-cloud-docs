---
url: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-back/
title: Backup and Restore (BACK) \u00a0|\u00a0 Google Distributed Cloud air-gapped \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:18:46.524320+00:00
---

# Backup and Restore (BACK)  |  Google Distributed Cloud air-gapped  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag/platform-application/pa-ao-operations/metrics-back/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ Air-gapped ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdch)
  * [ 1.16.2 (Latest) ](https://docs.cloud.google.com/distributed-cloud/hosted/docs/latest/gdcag)



Send feedback 

#  Backup and Restore (BACK) Stay organized with collections  Save and categorize content based on your preferences. 

## Metrics list

Name and description | Type | Scrape interval or emit duration | Labels  
---|---|---|---  
`gdc_backup_backup_repositories_attached`  
The number of backup repositories that have been attached. | Gauge | 1m | 

  * **repoName** : The name of the backup repository
  * **importPolicy** : Specifes whether the import policy is ReadWrite or ReadOnly
  * **importStatus** : Specifies whether the backup repository has successfully imported existing resources from object storage

  
`gdc_backup_backups_created`  
The number of created backups. | Counter | 1m | 

  * **backupPlan** : The name of the associated backup plan
  * **type** : The type of backup. Possible values are `MANUAL` or `SCHEDULED`

  
`gdc_backup_backups_deleted`  
The number of deleted backups. | Counter | 1m | 

  * **backupPlan** : The name of the associated backup plan.
  * **success** : Specifies whether the deletion succeeded

  
`gdc_backup_backups_completed`  
The number of completed backups. | Counter | 1m | 

  * **backupPlan** : The name of the associated backup plan
  * **success** : Specifies whether the backup has completed successfully

  
`gdc_backup_backups_latency`  
The latency of backups. This is how long the backup took to complete. Measured in minutes. | Histogram | 1m | 

  * **backupPlan** : The name of the associated backup plan
  * **success** : Specifies whether or not the backup has completed successfully

  
`gdc_backup_backups_pile_up`  
Specifies whether the backup plan has too many backups in-progress. Any more than one backup in progress from the same backup plan is too many. | Gauge | 1m | 

  * **backupPlan** : The name of the backup plan

  
`gdc_backup_backups_config_backup_size`  
The size of configuration backups. Measured in GB. | Histogram | 1m | 

  * **backupPlan** : The name of the associated backup plan

  
`gdc_backup_volume_backups_created`  
The number of created volume backups. | Counter | 1m | 

  * **backupPlan** : The name of the associated backup plan

  
`gdc_backup_volume_backups_completed`  
The number of completed volume backups. | Counter | 1m | 

  * **backupPlan** : The name of the associated backup plan
  * **success** : Specifies whether or not the backup completed successfully.

  
`gdc_backup_volume_backups_sizes`  
The size of volume backups. Measured in GB. | Histogram | 1m | 

  * **backupPlan** : The name of the associated backup plan

  
`gdc_backup_restores_created`  
The number of created restores. | Counter | 1m | 

  * **restorePlan** : The name of the associated restore plan
  * **type** : The type of restore

  
`gdc_backup_restores_completed`  
The number of completed restores. | Counter | 1m | 

  * **restorePlan** : The name of the associated restore plan
  * **success** : Specifies whether or not the restore has completed successfully

  
`gdc_backup_restores_latency`  
The latency of restores. This is how long the restore took to complete. Measured in minutes. | Histogram | 1m | 

  * **restorePlan** : The name of the associated restore plan
  * **success** : Specifies whether or not the restore has completed successfully

  
`gdc_backup_volume_restores_created`  
The number of created volume restores. | Counter | 1m | 

  * **restorePlan** : The name of the associated restore plan

  
`gdc_backup_volume_restores_completed`  
The number of completed volume restores. | Counter | 1m | 

  * **restorePlan** : The name of the associated restore plan
  * **success** : Specifies whether or not the restore completed successfully

  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
