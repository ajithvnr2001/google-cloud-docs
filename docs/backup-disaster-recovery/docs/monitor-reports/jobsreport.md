---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/jobsreport/
title: Jobs reports in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:27.892158+00:00
---

# Jobs reports in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/jobsreport/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Jobs reports in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Each protection operation is a job. There are three categories of jobs:

  * Snapshot

  * Replication

  * Recovery




Job reports record the execution and results of these operations.

  * Application backup status by consistency date

  * Backup job details

  * Backup job summary

  * Database log backup summary

  * Failed jobs

  * Job history summary by application

  * Recovery job details

  * Recovery job summary

  * Unresolved failures




## Application backup status by consistency date

This report provides backup jobs details of successful images and data handled by snapshot job.

The data provided in this report is grouped by each application and displayed for the selected consistency dates.

### Column description

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Consistency Date** : Timestamp when the application freezes for the backup job.

  * **Policy Template** : Name of the policy template used for application protection.

  * **Profile Name** : Name of the profile used for application protection.

  * **Job Name** : Name of the job run for the consistency date.

  * **Image Name** : Name of the image created by the successful backup job.

  * **Backup Status** : Status of the backup job (**Succeeded** , **Failed** , or **Canceled**).

  * **Data Copied (GB)** : Application data copied into the storage pools. This field is specific for snapshot jobs.




## Backup job details

This report provides details about the following backup jobs: Snapshot, OnVault, Log Replicate, StreamSnap, and Direct-to-OnVault. The report also shows the log backup jobs and includes an option to show only Log backup jobs. The chart in the report shows the count of jobs based on the status (succeeded, failed, canceled, not run) for the selected dates. The **Backup Job Details** report also shows how long a queued job has been waiting.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Policy Template** : Policy Template used for application protection.

  * **Policy Name** : Name of the policy used for protection.

  * **Job Name** : Name of the job.

  * **Job Type** : Type of the job.

  * **Target** : Pool name or remote appliance name or ID.

  * **Log Backup** : Sub-job type log backup for snapshot and StreamSnap jobs only.

  * **Status** : Completion status of the job: **Succeeded** , **Failed** , **Canceled** , or **Running**.

  * **Percent Complete** : Shows the progress of running jobs. This is not applicable for succeeded, failed, or canceled jobs.

  * **Queued** : Timestamp of the job queue for queued jobs.

  * **Started** : Timestamp of the start of the job. This is blank if the jobs have not been run.

  * **Ended** : Timestamp of the end of the job. Shows the violation time for jobs that have not been run.

  * **Duration (Hours)** : Time taken for job completion in hours.

  * **Consistency Point** : Consistency date for the job.

  * **Application Size (GB)** : Size of protected application.

  * **Data Copied (GB)** : Size of data copied.

  * **Percent Changed** : Percentage of data copied is of application size.

  * **Full Copy** : True when data capture job is a full backup.

  * **Crash Consistent** : True when backup is crash consistent.

  * **Scheduled** : True when the job is run by policy scheduler.

  * **Message** : Cause of the job failure. Blank for successful, canceled, and running jobs.

  * **Hours Since Last Success** : Hours since the last job for the policy ran successfully.




## Backup job summary

This report provides a backup job summary for the appliances configured with **Report Manager**. The summary contains tabular data that shows the job count based on all the job type, snapshot, remote, StreamSnap, OnVault, log backup, and log replicate jobs. It also provides the job status as **Succeeded** , **Failed** , **Running** , **Canceled** , and **Not Run** for each appliance. The **Summary** row displays the enterprise job count.

There are two sets of summary charts based on aggregated data for all job types: snapshot, remote, StreamSnap, OnVault, and log replicate.

  * **Two dual level pie graphs** : One graph represents appliance-wise job counts for the mentioned job types. (For the top five appliances, it shows that each appliance is aggregated into a single group called other Appliances.) The other representing job counts for job types with the corresponding statuses.

  * **Line chart** : Shows the trend over time for job count by status. (Optional controlled by show time series graphs input control.)




The report also provides an option to drill down within the backup job details report. This capability is provided in the appliance name and job count in the table, as well as the data points in the column chart and the line chart.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **All Job Types** : Refers to the count of job, irrespective of the job type selected.

  * **Snapshot or Remote or StreamSnap or OnVault or Log Backup or Log Replication** : Refers to the count of jobs for the respective job type category.

  * **Total** : Job count for the selected appliances and date range, irrespective of the job types or status.

  * **Succeeded** : Job count for the selected appliances and date range, irrespective of the job types or status.

  * **Success Percent** : Percentage of jobs succeeded for the selected appliances and date range, irrespective of the job types or status.

  * **Failed** : Job count for the selected appliances and date range, irrespective of the job type or status.

  * **Running** : Job count for the selected appliances and date range, irrespective of the job type or status.

  * **Canceled** : Job count for the selected appliances and date range, irrespective of the job type or status.

  * **Queued** : Job count for the selected appliances and date range, irrespective of the job type or status.

  * **Not Run** : Violation count of jobs that did not run for the selected appliances and date range, irrespective of the job type or status.




## Database log backup summary

This report provide the log backup summary for database applications, for the selected date range. This reports the success percent of the LOG backup and also indicate the backups which are at risk with a different color highlighting.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Policy Template** : Policy Template used for application protection.

  * **Log Backups Attempted** : Total number of log-backups.

  * **Succeeded** : Number of succeeded jobs.

  * **Failed** : Number of failed jobs.

  * **Canceled** : Number of canceled jobs.

  * **Not Run** : Number of not run jobs.

  * **Queued** : Number of queued jobs.

  * **Running** : Number of running jobs.

  * **Success Percent** : Success percentage of jobs.




## Failed jobs

This report shows the details of all failed jobs for the selected job types, applications, and time period.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Job Type** : Backup job type.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Policy Template** : Policy template used for application protection.

  * **Job Name** : Name of the job.

  * **Started** : Timestamp of the start of the job. Blank for jobs that have not been run.

  * **Ended** : Violation Time: Timestamp of the end of the job.

  * **Duration (Hours)** : Time taken for job completion in hours.

  * **Error Code** : Error ID assigned to the failed job.

  * **Message** : Error message for the failed job.

  * **Hours Since Failure** : Hours since the job for the application has failed.




## Job history summary by application

Every application is protected by executing a set of jobs depending on the protection policy set for the application. Based on the execution frequency set in the protection policy, each type of job is run periodically as specified. This report provides a success, failure, canceled, and running summary for job types for each application. Log backups are treated as a separate job type from snapshots. Totals for log backups are provided on the last page of the report. These totals double-count jobs that are Db+Log backups if both log backup and snapshot jobs are selected.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Policy Template** : Policy template used for application protection.

  * **Application Type** : Type of the application.

  * **Job Type** : Type of the job.

  * **Total Jobs** : Total number of jobs for the job type that were run for the application.

  * **Succeeded Job** : Number of successful jobs for the job type that were run for the application.

  * **Success Percent (%)** : Percentage of successful jobs for the job type that were run for the application.

  * **Failed Jobs(#)** : Number of failed jobs for the job type that were run for the application.

  * **Failed Percent(%)** : Percentage of failed jobs for the job type that were run for the application.

  * **Canceled Jobs** : Number of canceled jobs for the job type that were run for the application.

  * **Running Jobs** : Number of running jobs for the application and job type.

  * **Queued Jobs** : Number of queued jobs for the application and job type.

  * **Not Run Jobs** : Number of jobs not run for the application and job type.




## Recovery job details

The report shows the job details of the summary information provided in the **Recovery Job Summary** report. This report shows the effectiveness of the VDP appliance in recovering backed-up application data. This report includes restore jobs, such as **Restore** , **Mount** , and **Clone**.

### Column descriptions

  * **Appliance** : Name of the source appliance.

  * **Target Appliance** : Name of the target appliance.

  * **Mounted Host** : Host on which the appliance is running.

  * **Application** : Name of the application.

  * **Application Type** : Type of application.

  * **Job Name** : Name of the job.

  * **Job Type** : Type of the job. This is a sub-type of the major type **Restore** that includes **Mount** and **Clone**.

  * **Virtual Size** **(GB)** : Virtual size of the recovered application.

  * **Started** : Date and time when the job started.

  * **Ended** : Date and time when the job ended.

  * **Duration (Hours)** : Time taken for completion of job (in hours).

  * **Consistency Point** : Consistency date for the job.

  * **Status** : Completion status (**Succeeded** or **Failed**) of the job.

  * **Error Message** : Reason for the job failure.




## Recovery job summary

This report shows the effectiveness of the backup/recovery appliance in recovering backed-up application data. All the job types are included in the summary. It summarizes the total number of restore jobs of all types, as well as the number and percentage of successful restore jobs for each protected application.

### Column descriptions

  * **Appliance** : Name of the appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application.

  * **Application Type** : Type of application.

  * **Job Name** : Name of the job.

  * **Job Type** : Type of the job. This a sub-type of the major type **Restore** that includes **Mount** and **Clone**.

  * **Job-s Total Count** : Total number of jobs for the application and job type combination.

  * **Succeeded** : Number of jobs that ran successfully.

  * **Failed** : Number of jobs that failed.

  * **Running** : Number of jobs that are running.

  * **Success%** : Percentage of jobs that ran successfully.




## Unresolved failures

This report displays applications that had job failures in the selected time period without any subsequent successful jobs. Failures are grouped by the combination of application, job type, and error code. A failure count and time range is provided in this report.

### Column descriptions

  * **Appliance** : Name of the source appliance.

  * **Host** : Name of the host where the application resides.

  * **Application** : Name of the application suffixed with the hostname.

  * **Application Type** : Type of the application.

  * **Policy Template** : Policy template used for application protection.

  * **Job Type** : Type of the job.

  * **Log Backup Status** : Sub-job type. Log backup is for snapshot and StreamSnap jobs only.

  * **Error Code** : Unique code for the failure reason.

  * **Error Message** : Error message for the failure reason.

  * **Failure Count** : Number of jobs failed with the reason for the application and job class combination.

  * **First Failure** : Timestamp of the first failed job for the selected interval.

  * **Last Failure** : Timestamp of the last failed job for the selected interval.

  * **Hours Since Failure** : Minimum hours since the job for the application has failed.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
