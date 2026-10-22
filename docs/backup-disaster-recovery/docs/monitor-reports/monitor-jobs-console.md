---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console/
title: Monitor jobs in the Google Cloud console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:37.306040+00:00
---

# Monitor jobs in the Google Cloud console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Monitor jobs in the Google Cloud console Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view Backup and DR jobs in the Google Cloud console.

The jobs feature in the Backup and DR lets you view the status of jobs, and failed backup and restore or point-in-time restore (PITR) jobs of resources, such as Compute Engine instances or Cloud SQL instances. You can view the total number of jobs run, succeeded, failed, skipped, and running in a particular period of time. By default, the jobs page displays the jobs of one day, which is the last 24 hours. You can change the frequency to 1 hour, 6 hours, 12 hours, 7 days, or 14 days. You can configure a log-based alert to receive notifications when an alert occurs. For instructions, see [Configure a log-based alert for vaulted backups](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/configure-alerts-vault).

The jobs feature displays the jobs status only for data resources protected through the Google Cloud console. If you want to view the jobs of other resources such as Google Cloud VMware Engine, file systems, or database resources that use appliance-based backup templates, go to the **Jobs** page in the appliance management console. For more information, see [Monitor jobs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs).

### Before you begin

  * [Assign permissions required to manage buckets](https://docs.cloud.google.com/logging/docs/buckets#before-you-begin)
  * [Upgrade a bucket to use Observability Analytics](https://docs.cloud.google.com/logging/docs/buckets#upgrade-bucket)



## View backup and restore jobs

Use the following instructions to view backup and restore jobs, including point-in-time restore jobs.

### Console

  1. In the Google Cloud console, go to the **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)

  2. From the analysis section, click **Jobs**.


**Note:** Both Backup and DR and Backup for GKE jobs are shown in the same dashboard.

### gcloud

To view backup and restore jobs for Backup and DR, use the following instructions:

  1. View backup and restore jobs.
         
         gcloud logging read 'logName=~"bdr_backup_restore_jobs"' --project=PROJECT_ID
         

Add the [`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read jobs that are more than 1 day old.

Replace `PROJECT_ID` with the name of the project.




To view backup and restore jobs for Backup for GKE, use the following instructions:

  1. View backup and restore jobs.
         
         gcloud logging read 'logName=~"bfg_backup_restore_jobs"' --project=PROJECT_ID
         

Add the [`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read jobs that are more than 1 day old.

Replace `PROJECT_ID`with the name of the project.




## Current backup job failures

The current failures section lets you view the details of unresolved backup job failures, specifically for resources whose backups have failed since their last successful backup. This section displays the following information.

  * **Error type** : the description of the error. For example, `PERMISSION_DENIED`.
  * **Source project name** : the name of the project where the protected resource exists.
  * **Current failures** : the total number of resources in the source project for which the last backup job failed due to a particular error type.
  * **Error code** : the error code that is associated with the error type.
  * **Error message** : the error message for the failed job.
  * **Resource ID** : the list of IDs of the resources for which the last backup job failed.



To resolve failed backup jobs, see:

  * For resources protected by Backup and DR backup vault jobs: [Troubleshoot backup failure issues](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-vault-issues)
  * For resources protected by GKE clusters: [Overview of backup for GKE error codes](https://docs.cloud.google.com/kubernetes-engine/docs/add-on/backup-for-gke/troubleshoot/backup-error-codes)



## Backup and restore job details

The backup and restore job details section displays the following information.

  * **Job ID** : the ID associated with the job.
  * **Job category** : the type of job, which can be scheduled backup, on-demand backup, restore, or point-in-time restore (PiTR).
  * **Job status** : the status of the job, which can be successful, failed, skipped, or running.
  * **Resource name** : the name of the protected resource.
  * **Source project name** : the name of the project where the source is created.
  * **Resource location** : the location of the protected resource.
  * **Backup plan name** : the name of the backup plan associated with the resource. The backup plan name field remains `Null` for the restore jobs.
  * **backup vault location** : the location of the backup vault where the backups are stored.
  * **Backup rule** : the name of the backup rule that triggered the backup job.
  * **Backup vault name** : the name of the backup vault where the backups are stored.
  * **Backup project name** : the name of the backup project where your backup vault and backup plan are created.
  * **Incremental backup size GiB** : The amount of incremental backup data copied in GiB.
  * **Start time** : the start time of the job. The start time is in `YYYY-MM-DD HH:MM:SS.SSS` UTC format.
  * **Duration** : the duration took to complete the job.
  * **Error type** : the name of the error type. For example, `PERMISSION_DENIED`. The error type is displayed as `Null` if no error occurred for the job.
  * **Error message** : the error message for the failed job. The error message is displayed as `Null` if no error occurred for the job.
  * **Error code** : the error code associated for the failed job. The error code is displayed as `Null` if no error occurred for the job.
  * **End time** : the end time of the job. The end time is in `YYYY-MM-DD HH:MM:SS.SSS` UTC format.
  * **Backup name** : for backup jobs, the backup name is a system generated name for the backup in the form of UUID. For restore jobs, the backup name is the name of the backup used to perform the restore.
  * **Restore project name** : the name of the project where the backup is being restored.
  * **Restore resource name** : the name of the resource that gets created after the successful restoration.
  * **Resource type** : the type of resource.
  * **Resource ID** : the ID of the resource.
  * **Recovery Point Time** : For PiTR, restore is done to a point-in-time instead of restoring just a backup. This field captures the user provided recovery point.
  * **Datasource** : Name of the Data source in backup vault where the backups are stored. PiTR is triggered on data source not backups.

**Note:** The **Backup rule** field is not applicable for resources managed by Backup for GKE. The field has a Null value in the dashboard.

## View system jobs

Use the following instructions to view system jobs.

### Console

  1. In the Google Cloud console in Backup and DR, go to the **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)

  2. From the analysis section, click **System Jobs**.


**Note:** Both Backup and DR and Backup for GKE jobs are shown in the same dashboard.

### gcloud

To view system jobs for Backup and DR, use the following instructions:

  1. View system jobs.
         
         gcloud logging read 'logName=~"LOG_NAME"' --project=PROJECT_ID
         

Add the [`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read jobs that are more than 1 day old.

Replace the following:

     * LOG_NAME: the name of the log, either:

       * `bdr_backup_plan_jobs`: jobs related to a backup plan
       * `bdr_backup_plan_association_jobs`: jobs related to backup plan association in the administrator project, in case of cross-project protection.
       * `bdr_backup_plan_association_source_jobs`: jobs related to backup plan association in the workload project.

       * PROJECT_ID: the name of the project.




To view system jobs for Backup for GKE, use the following instructions:

  1. View system jobs.
         
         gcloud logging read 'logName=~"bfg_backup_plan_jobs"' --project=PROJECT_ID
         

Add the [`--freshness` flag](https://docs.cloud.google.com/sdk/gcloud/reference/logging/read#--freshness) to your command to read jobs that are more than 1 day old.

Replace the following:

     * PROJECT_ID: the name of the project.



### Backup plan

The backup and restore job details section displays the following information.

  * **Job ID** : the ID associated with the job.
  * **Job category** : the type of job (only **update** jobs are shown).
  * **Job status** : the status of the job, which can be successful, failed, skipped, or running.
  * **Resource type** : the type of the protected resource.
  * **Backup plan name** : the name of the backup plan.
  * **Previous backup plan revision ID** : the previous revision ID of the backup plan.
  * **Previous backup plan revision name** : the name of the previous revision of the backup plan.
  * **New backup plan revision ID** : the new revision ID of the backup plan.
  * **New backup plan revision name** : the name of the new revision of the backup plan.
  * **Start time** : the start time of the job. The start time is in `YYYY-MM-DD HH:MM:SS.SSS` UTC format.
  * **End time** : the end time of the job. The end time is in `YYYY-MM-DD HH:MM:SS.SSS` UTC format.
  * **Number of workloads affected** : the number of workloads affected by the job.
  * **Previous backup plan rules** : a list of the backup rules in the previous revision of the backup plan.
  * **Revised backup plan rules** : a list of the backup rules in the new revision of the backup plan.
  * **Error code** : the error code associated for the failed job. The error code is displayed as `Null` if no error occurred for the job.
  * **Error type** : the name of the error type. For example, `PERMISSION_DENIED`. The error type is displayed as `Null` if no error occurred for the job.
  * **Error message** : the error message for the failed job. The error message is displayed as `Null` if no error occurred for the job.

**Note:** The following fields are not applicable for resources managed by Backup for GKE: **Backup rule** , **Backup plan revision name** , and **Backup plan revision ID**. They appear as Null values in the dashboard.

### Backup plan association

The backup and restore job details section displays the following information.

  * **Job ID** : the ID associated with the job.
  * **Job category** : the type of job, (update).
  * **Job status** : the status of the job, which can be successful, queued, failed, skipped, or running.
  * **Resource name** : the name of the protected resource.
  * **Resource ID** : the ID of the resource.
  * **Resource location** : the location of the protected resource.
  * **Resource type** : the type of resource.
  * **Backup plan association name** : the name of the backup plan association.
  * **Name of the previous backup plan** : the name of the previous backup plan.
  * **Previous backup plan revision ID** : the previous revision ID of the backup plan.
  * **Previous backup plan revision name** : the name of the previous revision of the backup plan.
  * **Name of the new backup plan** : the name of the new backup plan.
  * **New backup plan revision ID** : the new revision ID of the backup plan.
  * **New backup plan revision name** : the name of the new revision of the backup plan.
  * **Start time** : the start time of the job. The start time is in `YYYY-MM-DD HH:MM:SS.SSS` UTC format.
  * **End time** : the end time of the job. The end time is in `YYYY-MM-DD HH:MM:SS.SSS` UTC format.
  * **Duration** : the duration took to complete the job.
  * **Error code** : the error code associated for the failed job. The error code is displayed as `Null` if no error occurred for the job.
  * **Error type** : the name of the error type. For example, `PERMISSION_DENIED`. The error type is displayed as `Null` if no error occurred for the job.
  * **Error message** : the error message for the failed job. The error message is displayed as `Null` if no error occurred for the job.



## Current system job failures

The current system job failures section lets you view the details of unresolved system job failures, specifically for resources whose system events have failed. This section displays the following information.

  * **Error type** : the description of the error. For example, `PERMISSION_DENIED`.
  * **Source project name** : the name of the project where the protected resource exists.
  * **Current failures** : the total number of system events that have failed pertaining to that job.
  * **Error code** : the error code that is associated with the error type.
  * **Error message** : the error message for the failed job.
  * **Resource ID** :

    * **Backup plan association** : the list of IDs of the protected resources
    * **Backup plan** : the name of the backup plan



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
