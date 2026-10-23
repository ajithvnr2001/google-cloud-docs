---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-recovery-reports/
title: Backup and recovery job reports \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:37.708120+00:00
---

# Backup and recovery job reports  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-recovery-reports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and recovery job reports Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

This page provides an overview of prebuilt Backup and Recovery reports in BigQuery.

The Backup and DR provides prebuilt Backup and Recovery reports that are accessible in BigQuery after [executing the prebuilt script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) in the same [dataset](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#sink) where the logs are being routed through the log sink.

  * Backup jobs summary report
  * Recovery jobs summary report
  * Failed job report
  * Unresolved failures report
  * Job details report



### Backup jobs summary report

The backup jobs summary report provides summary of the backup jobs for the last 30 days.

  * **Date** : The backup job date. It is in YYYY-MM-DD format.
  * **Resource name** : The name of the resource associated with the job.
  * **Resource type** : The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, or a database.
  * **Job type** : The actual job type. For example, snapshot, onvault, streamsnap, logreplicate, direct to onvault, log onvault, or log backup.
  * **Success %** : The percentage of jobs that were successful.
  * **Total jobs** : The total number of backup jobs that ran.
  * **Succeeded** : The total number of successful backup jobs.
  * **Failed** : The total number of backup jobs failed.
  * **Canceled** : The total number of backup jobs canceled.
  * **Not run** : The total number of backup jobs failed to run.



### Recovery jobs summary report

The recovery jobs summary report provides summary of the recovery jobs for the last 30 days.

  * **Date** : The recovery job date. It is in YYYY-MM-DD format.
  * **Resource name** : The name of the resource associated with the recovery job.
  * **Resource type** : The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, or a database.
  * **Job type** : The actual job type. For example, clone, live clone create, live clone refresh, live clone reprovision, local restore, mount, unmount, unmount and delete, remote clone, remote mount, or remote restore.
  * **Success %** : The percentage of jobs that are successful.
  * **Total jobs** : The total number of recovery jobs that ran.
  * **Succeeded** : The total number of recovery jobs succeeded.
  * **Failed** : The total number of recovery jobs failed.
  * **Canceled** : The total number of recovery jobs canceled.
  * **Not run** : The total number of recovery jobs failed to run.



### Failed job report

The failed jobs summary report provides details on the recently failed jobs.

  * **Job name** : The name of the job.
  * **Job category** : This displays if the job is for backup or recovery.
  * **Job type** : The actual job type, for example, snapshot, OnVault, streamsnap, or a restore.
  * **Resource name** : The name of the resource associated with the job.
  * **Resource type** : The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, or a database.
  * **Error code** : The error ID assigned to the failed job.
  * **Error message** : The error message for a job.
  * **Hostname** : The hostname associated with the job.
  * **Backup rule or policy name** : The name of the backup policy used for backup jobs.
  * **Backup plan or policy template** : The name of the backup plan used for backup jobs.
  * **Appliance name** : The name of the appliance associated with the job.
  * **Job start time** : The start time of the job. It is in YYYY-MM-DD HH:MM format.
  * **Job date** : The start date of the job.
  * **Backup type** : The type of the backup performed. It can be either full copy or incremental. For log backups, it is shown as log.



### Unresolved failures report

The unresolved failures report provides details on the failed jobs with a failure reason.

  * **Resource name** : The name of the resource associated with the job.
  * **Resource type** : The type of resource, for example, Compute Engine, Google Cloud VMware Engine, or database.
  * **Job type** : The actual job type, for example, snapshot, OnVault, streamsnap, or restore. 
  * **Job category** : This displays if the job is for backup or recovery.
  * **Error count** : The total count of failed jobs since the most recent successful one for the resource of the specific job type. If no successful job has run within the last seven days, this will show the total number of failed jobs for the last three days.
  * **Error code** : The error ID assigned to the failed job.
  * **Error message** : The error message for the last failed job.
  * **First failure** : The timestamp of the first failed job after the last successful job; it is in YYYY-MM-DD HH:MM format.
  * **Last failure** : The timestamp of the last failed job. It is in YYYY-MM-DD HH:MM format.
  * **Hours since last failure** : The elapsed hours since the last job failed.
  * **Appliance name** : The name of the appliance associated with the job.



### Job details report

The job details report provides job related details.

  * **Job name** : The name of the job.
  * **Job category** : This displays if the job is for backup or recovery.
  * **Job type:** The actual job type, for example, snapshot, OnVault, streamsnap, or a restore.
  * **Job status** : The status of the job. The status can be _Succeeded_ , _Failed_ , _Canceled_ , _Retry_ , or _Not run_.
  * **Job date** : The date when the job was executed.
  * **Resource name** : The name of the resource associated with the job.
  * **Resource type** : The type of resource, for example, Compute Engine, Google Cloud VMware Engine, or a database.
  * **Error code** : The error ID assigned to the unsuccessful job.
  * **Error message** : The error message for a job.
  * **Job initiation failure reason** : The reason for not initiating or starting a job.
  * **Appliance name** : The name of the appliance associated with the job.
  * **Hostname** : The hostname associated with the job.
  * **Target appliance name** : The name of the target appliance associated with the job.
  * **Target pool name** : The name of the target OnVault pool used for backup jobs.
  * **Target hostname** : The name of the target host.
  * **Backup plan or policy template** : The name of the backup plan used for backup jobs.
  * **Backup rule or policy name** : The name of the backup policy used for backup jobs.
  * **Log backup** : This field displays for database applications with the log backup types `DB` and `Log`. When a DB backup is taken, this field displays the `DB` backup type. When only a log backup is taken for the `DB`, this field displays the `Log` backup type.
  * **Job queued time** : The timestamp of the job queue for queued jobs; it is in YYYY-MM-DD HH:MM format.
  * **Job start time** : The start time of the job; it is in YYYY-MM-DD HH:MM format.
  * **Job end time** : The end time of the job; it is in YYYY-MM-DD HH:MM format.
  * **Job duration** : The duration taken to complete the job.
  * **Backup consistency** : This displays if the backup is crash consistent or application consistent.
  * **Resource data size (GB)** : The size of the protected resource.
  * **Snapshot disk size (GB)** : The snapshot size of the recovered application.
  * **Pre compress (GB)** : The size of the resource precompression for OnVault jobs.
  * **Compression ratio** : The compression ratio achieved before sending the data to object storage. This is valid for both OnVault and direct to OnVault jobs.
  * **Streamsnap data sent (GB)** : The total amount of data sent to the remote site for this job. This is valid only for streamsnap jobs.
  * **Streamsnap data written (GB)** : The amount of data written into the relevant pool at the remote site. This is valid only for streamsnap jobs.
  * **Data Copied (GB):** The size of data copied.
  * **Data change rate** : The percentage of a resource size that is copied data (used data).
  * **Backup type** : The type of the backup performed. It can be either full copy or incremental. For log backups, it is shown as _Log_.
  * **Recovery point** : The date of when the last successful backup was taken.
  * **OnVault Pool Storage Consumed (GB)** : The size of the OnVault pool consumed.



## What's next

  * Learn how to [Execute prebuilt reports script](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#script)
  * Learn how to [Write custom queries in BigQuery](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/logs-route-bigquery#custom-queries)
  * Learn how to [Download prebuilt reports](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/view-reports-sheets#download)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
