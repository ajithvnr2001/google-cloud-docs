---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/job-logs/
title: View backup and recovery job logs created on a backup/recovery appliance in Cloud Logging \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:46.576117+00:00
---

# View backup and recovery job logs created on a backup/recovery appliance in Cloud Logging  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/job-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View backup and recovery job logs created on a backup/recovery appliance in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the job logs created in Cloud Logging for backup/recovery appliances. These logs provide insight into the jobs of your backup/recovery appliance, for example, job successes, failures, or other statuses.

## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the job logs. The **Logs Viewer** role gives you read-only access to view job logs of all backup/recovery appliances in the specified project. For more information about the IAM permissions and roles that apply to job logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View job logs

You can view Backup and DR job logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the Backup and DR job log entries for your backup/recovery appliances:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.

[Logs Explorer](https://console.cloud.google.com/logs/query)

  2. Select an existing Google Cloud project.

  3. In the **Query builder** pane, select **`gcb_backup_recovery_jobs`** from the **Select Log name** drop-down.




### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Logging API. Read your job log entries of backup/recovery appliances in a project:
    
    
     gCloud Logging read "logName : projects/PROJECT_ID/logs/gcb_backup_recovery_jobs"\--project=PROJECT_ID
    

## Job log format

Backup and DR job log entries include the following fields:

Field | Description  
---|---  
Appliance name | The name of the appliance associated with the job.  
Resource name | The name of the resource associated with the job.  
Backup consistency | This displays if the backup is crash consistent or application consistent.  
Backup data copied (GB) | The size of backup data copied.  
Backup plan | The name of the backup plan used for backup jobs.  
Backup rule | The name of the backup policy used for backup jobs.  
Backup rule ID | The backup policy ID used for backup jobs.  
Backup type | The type of the backup performed. It can be either full copy or incremental. For log backups, it is shown as _Log_.  
Compression ratio | The compression ratio achieved before sending the data to object storage. This is valid for both OnVault and direct to OnVault jobs.  
Data change rate | The percentage that data copied is of resource size (used data).  
Data sent (GB) | The total amount of data sent to the remote site for this job. This is valid only for streamsnap jobs.  
Data written (GB) | The amount of data written into the relevant pool at the remote site. This is valid only for streamsnap jobs.  
Error code | The error ID assigned to the unsuccessful job.  
Error message | The error message for a job.  
Host ID | The host ID associated with a job.  
Hostname | The hostname associated with the job.  
Job category | This displays if the job is for backup or recovery.  
Job duration | The duration taken to complete the job.  
Job end time | The end time of the job.  
Job ID | The ID associated with a job.  
Job initiation failure reason | The reason for not initiating or starting a job.  
Job name | The name of the job.  
Job type | The actual job type, for example, snapshot, OnVault, streamsnap, or restore.  
Job start time | The start time of the job.  
Job status | The status of the job. The status can be _Succeeded_ , _Failed_ , _Canceled_ , _Retry_ , or _Not run_.  
Job queued time | The timestamp of the job queue for queued jobs.  
Log backup | This field is displayed for database applications with the log backup types `DB` and `Log`. When a DB backup is taken, this field displays the `DB` backup type. When only a `Log` backup is taken for the DB, this field displays the log backup type.  
OnVault Pool Storage Consumed (GB) | The size of the OnVault pool consumed.  
Pre compress (GB) | The size of the resource precompression for OnVault jobs.  
Resource data size (GB) | The size of the protected resource.  
Resource ID | The resource ID associated with a job.  
Resource type | The type of resource, for example, Compute Engine instance, VMware Compute Engine, or a database.  
Recovery point | The date of when the last successful backup was taken.  
Snapshot disk size (GB) | The snapshot size of the recovered application.  
Target appliance ID | The ID of the target appliance associated with a job.  
Target hostname | The name of the target host.  
Target host ID | The ID of the target host.  
Target appliance name | The name of the target appliance associated with the job.  
Target pool ID | The ID of the target OnVault pool used for backup jobs.  
Target pool name | The name of the target OnVault pool used for backup jobs.  
  
The following sample is an example log entry logged on a backup/recovery appliance `appliance-test5-64573` for a snapshot job.
    
    
            {
            "insertId": "1717974_145859162970",
            "jsonPayload": {
            "target_host_name": "appliance-test6-8299",
            "hostname": "uistress-sql19stdm",
            "target_pool_name": "act_per_pool000",
            "error_code": 0,
            "data_sent_in_gib": 0,
            "compression_ratio": 0,
            "job_status": "succeeded",
            "job_duration_in_hours": 0.02,
            "job_initiation_failure_reason": "",
            "log_backup": "",
            "recovery_point": "2024-01-18T05:03:04Z",
            "resource_name": "DB02",
            "pre_compress_in_gib": 0,
            "job_name": "Job_1717931",
            "backup_consistency": "Application Consistent",
            "onvault_pool_storage_consumed_in_gib": 0,
            "job_id": "1717973",
            "job_queued_time": "2024-01-18T05:05:01Z",
            "host_id": "4677",
            "job_type": "Log Replicate",
            "resource_data_size_in_gib": 0.02,
            "target_appliance_id": "145240780891",
            "appliance_name": "appliance-test5-64573",
            "snapshot_disk_size_in_gib": 10,
            "target_pool_id": "73",
            "data_change_rate": 11.33,
            "backup_type": "Incremental",
            "target_host_id": "4677",
            "data_copied_in_gib": 0,
            "data_written_in_gib": 0,
            "resource_id": "57587",
            "resource_type": "SqlServerWriter",
            "error_message": "",
            "backup_rule_policy_id": "72954",
            "backup_plan_policy_template": "Copy of _a_logsmart_2023_11_23_15_44_8",
            "job_end_time": "2024-01-18T05:06:17Z",
            "job_category": "Backup Job",
            "backup_rule_policy_name": "logsmart_snap",
            "target_appliance_name": "appliance-test6-8299",
            "job_start_time": "2024-01-18T05:05:04.377Z"
            },
            "resource": {
            "type": "backupdr.googleapis.com/ManagementConsole",
            "labels": {
                  "management_server_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
                  "location": "us-central1",
                  "resource_container": "projects/xxxxxxxxxxxx"
            }
            },
            "timestamp": "2024-01-18T05:07:04.697Z",
            "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs",
            "receiveTimestamp": "2024-01-18T05:08:12.139517321Z"
            }
    

## Sample queries

You can write custom job queries in the query section to view selected logs.

Use the following query to view all the job logs associated with backup/recovery appliances for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs"
    

Use the following query for specific appliance backup recovery job details.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs"
        jsonPayload.appliance_name="appliance_name"
    

Use the following query for specific backup recovery job details that run for a specific resource.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs"
        jsonPayload.resource_name="resource_name"
    

Use the following query for specific jobs that ran for a given resource name and backup template.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs"
        jsonPayload.resource_name="resource_name"
        jsonPayload.backup_plan_policy_template="backup_template"
    

Use the following query for backup recovery jobs that run for applications for a specific host.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs"
        jsonPayload.hostname="hostname"
    

Use the following query if you are searching logs related to specific job types. Make sure to use uppercase `OR` operators in the query.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs"
        jsonPayload.job_type=("Snapshot" OR "Mount")
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter job logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
