---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-restore-backupvault-report/
title: Backup and restore job reports for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:48.056502+00:00
---

# Backup and restore job reports for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-restore-backupvault-report/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and restore job reports for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of prebuilt backup and restore job reports, which are available in BigQuery and Data Studio. These reports are displayed for resources that are protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).

You can access these reports after you [execute the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#sink) in the same project where the logs are being routed through the log sink.

**Note:** If you want to learn about the backup and restore job report that are protected using the [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) in the appliance management console, see [Job reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-recovery-reports).

## Backup job details report

The backup job details report provides a summary of the backup jobs and includes the following fields.

  * **job_name** : The name of the backup job.
  * **resource_name** : The name of the protected resource.
  * **resource_project_name** : The project name of the resource.
  * **job_status** : The status of the job, which can be `SUCCESSFUL`, `FAILED`, `RUNNING`, or `SKIPPED`.
  * **error_type** : The description of the error type. For example, `PERMISSION_DENIED`. The error type is displayed as `Null` if no error occurred for the job.
  * **error_code** : The error code associated for the failed job. The error code is displayed as `Null` if no error occurred for the job.
  * **error_message** : The error message for the failed job. The error message is displayed as `Null` if no error occurred for the job.
  * **job_start_time** : The start time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **job_end_time** : The end time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **duration** : The duration taken to complete the backup job.
  * **incremental_backup_size_in_gib** : The amount of incremental backup data copied in GiB.
  * **backup_consistency_time** : The timestamp when the backup was successfully taken, which is in the `YYYY-MM-DDTHH:MM:SS.SSSZ` format.
  * **backup_plan_name** : The name of the backup plan that is associated to backup the resource.
  * **backup_rule** : The name of the backup rule that triggered the backup job.
  * **backup_vault_name** : The name of the backup vault where the backups are stored.
  * **backup_vault_project_name** : The name of the backup vault project where the backups are stored.
  * **backup_vault_location** : The location of the backup vault where the backups are stored.
  * **resource_location** : The location of the protected resource.
  * **resource_type** : The type of resource. For example, a Compute Engine instance.
  * **resource_id** : The resource ID associated with a job.
  * **job_category** : The category of job, which can be `SCHEDULED_BACKUP`, `ON_DEMAND_BACKUP`, or `RESTORE`.
  * **job_id** : The ID associated with the backup job.



## Backup jobs summary

The backup jobs summary report provides a daily summary of backup jobs and includes the following fields.

  * **date** : The backup job date, which is in YYYY-MM-DD format.
  * **resource_project_name** : The project name of the resource.
  * **job_category** : The category of job, which can be `SCHEDULED_BACKUP` or `ON_DEMAND_BACKUP`.
  * **success_percent** : The percentage of backup jobs that are successful.
  * **total** : The total number of backup jobs that ran.
  * **successful** : The total number of backup jobs succeeded.
  * **failed** : The total number of backup jobs failed.
  * **skipped** : The total number of backup jobs skipped.



## Successful backup jobs report

The successful backup jobs report includes the following fields.

  * **job_name** : The name of the backup job.
  * **resource_name** : The name of the protected resource.
  * **resource_project_name** : The project name of the resource.
  * **job_start_time** : The start time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **job_end_time** : The end time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **duration** : The duration taken to complete the backup job.
  * **incremental_backup_size_in_gib** : The amount of incremental backup data copied in GiB.
  * **backup_consistency_time** : The timestamp when the backup was successfully taken, which is in the `YYYY-MM-DDTHH:MM:SS.SSSZ` format.
  * **backup_plan_name** : The name of the backup plan that is associated to backup the resource.
  * **backup_rule** : The name of the backup rule that triggered the backup job.
  * **backup_vault_name** : The name of the backup vault where the backups are stored.
  * **backup_vault_project_name** : The name of the backup vault project where the backups are stored.
  * **backup_vault_location** : The location of the backup vault where the backups are stored.
  * **resource_type** : The type of resource. For example, a Compute Engine instance.
  * **resource_id** : The resource ID associated with a job.
  * **job_category** : The category of job, which can be `SCHEDULED_BACKUP`, `ON_DEMAND_BACKUP`, or `RESTORE`.
  * **job_id** : The ID associated with the job.



## Failed backup jobs report

The failed backup jobs report includes the following fields.

  * **job_name** : The name of the backup job.
  * **resource_name** : The name of the protected resource.
  * **resource_project_name** : The project name of the resource.
  * **error_type** : The description of the error type. For example, `PERMISSION_DENIED`. The error type is displayed as `Null` if no error occurred for the job.
  * **error_code** : The error code associated for the failed job. The error code is displayed as `Null` if no error occurred for the job.
  * **error_message** : The error message for the failed job. The error message is displayed as `Null` if no error occurred for the job.
  * **job_start_time** : The start time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **job_end_time** : The end time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **duration** : The duration taken to complete the backup job.
  * **backup_plan_name** : The name of the backup plan that is associated to backup the resource.
  * **backup_rule** : The name of the backup rule that triggered the backup job.
  * **backup_vault_name** : The name of the backup vault where the backups are stored.
  * **backup_vault_project_name** : The name of the backup vault project where the backups are stored.
  * **backup_vault_location** : The location of the backup vault where the backups are stored.
  * **resource_type** : The type of resource. For example, a Compute Engine instance.
  * **resource_id** : The resource ID associated with a job.
  * **job_category** : The category of job, which can be `SCHEDULED_BACKUP`, `ON_DEMAND_BACKUP`, or `RESTORE`.
  * **job_id** : The ID associated with the job.



## Skipped backup jobs report

The skipped backup jobs report includes details of the skipped backup jobs and the following fields. Backup jobs might skip to backup when the backup fails to start within the backup window.

  * **job_name** : The name of the backup job.
  * **resource_name** : The name of the protected resource.
  * **resource_project_name** : The project name of the resource.
  * **backup_plan_name** : The name of the backup plan that is associated to backup the resource.
  * **backup_rule** : The name of the backup rule that triggered the backup job.
  * **backup_vault_name** : The name of the backup vault where the backups are stored.
  * **job_start_time** : The start time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **backup_vault_project_name** : The name of the backup vault project where the backups are stored.
  * **backup_vault_location** : The location of the backup vault where the backups are stored.
  * **resource_type** : The type of resource. For example, a Compute Engine instance.
  * **resource_id** : The resource ID associated with a job.
  * **job_category** : The category of job, which can be `SCHEDULED_BACKUP`, `ON_DEMAND_BACKUP`, or `RESTORE`.
  * **job_id** : The ID associated with the job.



## Restore jobs summary

The restore jobs summary report provides a daily summary of restore jobs and includes the following fields.

  * **date** : The restore job date, which is in YYYY-MM-DD format.
  * **restore_project_name** : The project name where the backups are restored.
  * **backup_vault_project_name** : The name of the backup vault project from where the restores are triggered.
  * **job_category** : The category of the restore job, which can be `RESTORE` or `PITR`.
  * **success_percent** : The percentage of restored jobs that are successful.
  * **total** : The total number of restored jobs that ran.
  * **successful** : The total number of restored jobs succeeded.
  * **failed** : The total number of restored jobs failed.



## Restore job details

The restore job details report includes the following fields.

  * **job_name** : The name of the job.
  * **resource_name** : The name of the resource that is associated with the restore job.
  * **resource_project_name** : The project name of the source resource from where the backup was taken.
  * **job_status** : The status of the job, which can be `SUCCESSFUL`, `FAILED`, or `RUNNING`.
  * **error_type** : The description of the error type. For example, `PERMISSION_DENIED`. The error type is displayed as `Null` if no error occurred for the job.
  * **error_code** : The error code associated for the failed restore job. The error code is displayed as `Null` if no error occurred for the job.
  * **error_message** : The error message for the failed restore job. The error message is displayed as `Null` if no error occurred for the job.
  * **job_start_time** : The start time of the restore job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **job_end_time** : The end time of the restore job, which is in the `YYYY-MM-DD HH:MM:SS.SSS UTC` format.
  * **duration** : The duration taken to complete the restore job.
  * **restore_resource_name** : The name of the resource that is being restored.
  * **restore_project_name** : The name of the project where the backups are being restored.
  * **restore_resource_location** : The location where the resource is restored.
  * **recovery_point_time** : The timestamp of the recovery point used for Point-in-time Restore, which is in the `YYYY-MM-DDTHH:MM:SS.SSSZ` format.
  * **backup_vault_name** : The name of the backup vault where the backup of the resource is stored.
  * **backup_vault_project_name** : The name of the backup vault project from where restores are triggered.
  * **backup_vault_location** : The location of the backup vault from where the restores are triggered.
  * **data_source_name** : The data source ID of the restored resource.
  * **resource_location** : The location of the protected resource.
  * **resource_type** : The type of resource. For example, a Compute Engine instance.
  * **resource_id** : The resource ID associated with a job.
  * **job_category** : The category of the restore job, which can be `RESTORE` or `PITR`.
  * **job_id** : The ID associated with the job.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-vault-bigquery#sink)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/custom-query)
  * Learn how to [View prebuilt reports in Connected Sheets](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets)
  * Learn how to [View prebuilt reports in Looker Studio](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-lookerstudio)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
