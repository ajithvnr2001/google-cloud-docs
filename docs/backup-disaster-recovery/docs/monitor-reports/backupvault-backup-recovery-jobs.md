---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backupvault-backup-recovery-jobs/
title: Backup and restore job logs for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:48.231882+00:00
---

# Backup and restore job logs for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backupvault-backup-recovery-jobs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup and restore job logs for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the backup and restore job logs for vaulted backups in Cloud Logging. These backups are for the resources protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan). If you want to view the backup and restore job logs that are protected using the [backup template](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/create-template) in the appliance management console, see [Backup and recovery job logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/job-logs).

## Permissions and roles

You need the IAM permission `roles/logging.viewer` to view the backup and restore job logs. The `Logs Viewer` role gives you read-only access to view backup and restore job logs of all resources protected by backup plan in the specified project. If backup and restore operations are performed in a different project, ask your administrator to assign the permission `roles/logging.viewer` in the project where you want to view logs. For more information about the IAM permissions and roles to control access to logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View backup and restore job logs

You can view backup, restore, and PITR job logs for vaulted backups in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To view backup jobs, select either the backup vault project or the resource project where the backup is performed. To view restore and PITR jobs, select either the backup vault project or the project in which the resource is restored.

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the backup and restore logs entries for your vaulted backups:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **bdr_backup_restore_jobs** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the logging API. To read your backup and restore log entries of a project, run the following command:
    
    
    ```none
     gcloud logging read "logName:bdr_backup_restore_jobs" --project=PROJECT_ID
    ```
    

Replace the following:

  * `PROJECT_ID`: the name of the project. To view backup jobs, you can enter either the backup vault project or the resource project where the backup is performed. To view restore jobs, you can enter either the backup vault project or the project in which the resource is restored.



### Backup and restore jobs log format

Backup and restore log entries include the following fields:

Field | Description  
---|---  
`jobId` | The ID associated with the job.  
`sourceResourceName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the protected resource.  
`jobCategory` | The category of job, which can be `SCHEDULED_BACKUP`, `ON_DEMAND_BACKUP`, `RESTORE`, or `PITR`.  
`sourceResourceId` | The ID of the protected resource.  
`resourceType` | The type of resource. For example, a Compute Engine instance.  
`jobStatus` | The status of the job, which can be `SUCCESSFUL`, `FAILED`, `RUNNING`, `SKIPPED`.  
`backupRule` | The name of the backup rule that triggered the backup job.  
`backupVaultName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup vault where the backups are stored.  
`startTime` | The start time of the job, which is in the `YYYY-MM-DD HH:MM:SS.SSS` UTC format.  
`backupPlanName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup plan that is associated with the resource. For restore jobs, the backup plan name field remains `Null`.  
`errorCode` | The error code associated for the failed job. The error code is displayed as `Null` if no error occurred for the job.  
`errorType` | The name of the error type. For example, `PERMISSION_DENIED`. The error type is displayed as `Null` if no error occurred for the job.  
`errorMessage` | The error message for the failed job. The error message is displayed as `Null` if no error occurred for the job.  
`restoreResourceName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the resource that gets created after the successful restoration.  
`backupName` | For backup jobs, the backup name is a system generated name for the backup in the form of UUID. For restore jobs, the backup name is the name of the backup used to perform the restore.  
`recoveryPointTime` | For point-in-time restores (PITR), restore is done to a point-in-time instead of restoring just a backup. This field captures the user provided recovery point in the `YYYY-MM-DD HH:MM:SS.SSS` UTC format.  
`dataSourceName` | Name of the Data source in backup vault where the backups are stored. The point-in-time restore is triggered on data source not backups.  
  
The following sample is an example of a log entry for a scheduled backup on a Compute Engine instance.
    
    
            {
            "insertId": "696883be-582d-4af4-b2b8-a4c497e49489",
            "jsonPayload": {
              "jobId": "696883be-582d-4af4-b2b8-a4c497e49489",
              "@type": "type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupRestoreJobLog",
              "sourceResourceName": "projects/Source_project_ID/zones/asia-east1-c/instances/Instance_name",
              "jobCategory": "SCHEDULED_BACKUP",
              "sourceResourceId": "6114243930178522357",
              "resourceType": "Compute Engine",
              "jobStatus": "RUNNING",
              "backupRule": "backup-rule-1",
              "backupVaultName": "projects/Backupvault_project_ID/locations/asia-east1/backupVaults/Backupvault_name",
              "startTime": "2024-09-10T06:37:00.303416182Z",
              "backupPlanName": "projects/Backupplan_project_ID/locations/asia-east1/backupPlans/Backupplan_Name"
            },
            "resource": {
              "type": "backupdr.googleapis.com/BackupDRProject",
              "labels": {
                "resource_container": "projects/223618678509",
                "location": "asia-east1"
              }
            },
            "timestamp": "2024-09-10T06:37:00.303416182Z",
            "logName": "projects/Backupvault_Name/logs/backupdr.googleapis.com%2Fbdr_backup_restore_jobs",
            "receiveTimestamp": "2024-09-10T06:37:01.818767274Z"
          }
    

### Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view failed jobs.
    
    
        logName:"bdr_backup_restore_jobs" jsonPayload.jobStatus="FAILED"
    

Use the following query to view jobs stored in a backup vault.
    
    
        logName:"bdr_backup_restore_jobs" jsonPayload.backupVaultName:"backupVaults/BACKUPVAULT_NAME"
    

Use the following query to view jobs created with a backup plan.
    
    
        logName:"bdr_backup_restore_jobs" jsonPayload.backupPlanName:"backupPlans/BACKUPPLAN_NAME"
    

## View backup plan details logs

You can view backup plan details logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To view backup jobs, select the project where the backup plan was created.

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the backup plan details logs entries:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **bdr_backup_plan_details** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the logging API. To read your backup and restore log entries of a project, run the following command:
    
    
     ```none
     gcloud logging read "logName: bdr_backup_plan_details" --project=PROJECT_ID
     ```
    

Replace the following:

  * `PROJECT_ID`: the name of the project where the backup plan was created.



### Backup plan details log format

Backup and restore log entries include the following fields:

Field | Description  
---|---  
`backupPlanName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup plan.  
`ruleName` | The name of the backup rule used for backup jobs.  
`recurrence` | The backup recurrence type, which can be hourly, daily, weekly, monthly, or yearly.  
`recurrenceSchedule` | The recurrence schedule of a backup based on the backup rule.  
`backupWindow` | The timeframe of when backup jobs can start.  
`retentionDays` | The duration in days for which the backups should be retained.  
`backupWindowTimezone` | The timezone that applies to the backup window.  
`backupVaultName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup vault that is associated with the backup plan.  
`resourcesProtectedCount` | The number of resources protected by the backup plan.  
`protectedDataVolumeGib` | The total size in GiB of the source data protected by the backup plan.  
  
The following sample is an example of a `bdr_backup_plan_details` log entry.
    
    
            {
              "insertId": "15792541403682418506",
              "jsonPayload": {
                "resourcesProtectedCount": 3,
                "protectedDataVolumeGib": 30,
                "@type": "type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupPlanDetailsLog",
                "backupVaultName": "projects/hk-staging-saas-report-1/locations/us-central1/backupVaults/hk-bv-1",
                "backupPlanName": "projects/hk-staging-saas-report-1/locations/us-central1/backupPlans/hk-bp-2",
                "backupRuleDetails": [
                  {
                    "retentionDays": 10,
                    "recurrence": "Daily",
                    "recurrenceSchedule": "Every day",
                    "backupWindow": "00:00 to 24:00",
                    "ruleName": "hk-br-2",
                    "backupWindowTimezone": "Asia/Calcutta"
                  }
                ]
              },
              "resource": {
                "type": "staging-backupdr.sandbox.googleapis.com/BackupPlan",
                "labels": {
                  "location": "us-central1",
                  "resource_container": "838468076466",
                  "backup_plan_id": "hk-bp-2"
                }
              },
              "timestamp": "2025-06-09T08:04:10Z",
              "severity": "INFO",
              "logName": "projects/hk-staging-saas-report-1/logs/staging-backupdr.sandbox.googleapis.com%2Fbdr_backup_plan_details",
              "receiveTimestamp": "2025-06-09T09:40:14.711832094Z"
            }
    

### Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view backup plans associated with a specific backup plan:
    
    
        logName:"bdr_backup_plan_details" jsonPayload.backupPlanName:"projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUPPLAN_NAME"
    

Use the following query to view backup plans associated with a specific backup vault:
    
    
        logName:"bdr_backup_plan_details" jsonPayload.backupVaultName:"projects/PROJECT_ID/locations/LOCATION/backupVaults/BACKUPVAULT_NAME"
    

Use the following query to view backup plans that contain a specific rule name:
    
    
        logName:"bdr_backup_plan_details" jsonPayload.backupRuleDetails.ruleName:"RULE_NAME
    

## View backup plan reports for vaulted backups

**You can view backup plan details logs in Cloud Logging by using the Google Cloud console and the[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To view backup jobs, select the project where the backup plan was created.**

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the backup plan details logs entries:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **bdr_backup_plan_details** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the logging API. To read your backup and restore log entries of a project, run the following command:
    
    
     ```none
     gcloud logging read "logName: bdr_backup_plan_details" --project=PROJECT_ID
     ```
    

Replace the following:

  * `PROJECT_ID`: the name of the project where the backup plan was created.



### Backup plan report format

This report provides comprehensive insights into configured backup plans, detailing their rules, associated backup vaults, and the statistics of the resources they protect.

The report includes the following fields:

  * date: The most recent date on which the backup plan information was updated.
  * backup_plan_name: The designated name of the backup plan.
  * backup_plan_location: The geographical location of the backup plan.
  * backup_rules: A repeated record (array) containing granular details for each backup rule within the plan. Each rule record comprises: 
    * backup_rules.rule_name: The designated name of the backup rule.
    * backup_rules.recurrence: The specified recurrence type for the backup (e.g., "hourly," "daily," "weekly," "monthly," "yearly").
    * backup_rules.recurrence_schedule: The defined recurrence schedule for the backup rule (e.g., "every day at 10:00," "every Monday").
    * backup_rules.backup_window: The defined timeframe (in 24-hour clock format) during which backup jobs are permitted to commence (e.g., "02:00-08:00").
    * backup_rules.backup_window_time_zone: The timezone in which the backups are scheduled (e.g., "UTC," "America/Los_Angeles").
    * backup_rules.retention_days: The specified duration (in days) for which backups are to be retained in accordance with this rule.
  * backup_vault_name: The name of the backup vault intrinsically linked to the backup plan.
  * backup_vault_location: The geographical location of the backup vault associated with the backup plan.
  * resources_protected_count: The quantifiable number of resources protected by this specific backup plan.
  * protected_data_volume_gib: The aggregate data volume (expressed in GiB) of the resources protected by this backup plan.
  * minimum_enforced_retention_days: The minimum mandatory retention period (in days) applicable to backups associated with this backup plan.
  * effective_date_for_enforced_retention_lock: The precise effective date for the enforced retention lock.
  * lock_on_enforced_retention: An indicator of whether the retention is in a locked state. This field is dynamically generated based on the subsequent logic:

    * If the `effective_date_for_enforced_retention_lock` timestamp is present and corresponds to either the current time or a past time, then the value is designated as "locked."
    * If this condition is not met, the value is designated as "unlocked."



### Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view backup plans associated with a specific backup plan:
    
    
        logName:"bdr_backup_plan_details" jsonPayload.backupPlanName:"projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUPPLAN_NAME"
    

Use the following query to view backup plans associated with a specific backup vault:
    
    
        logName:"bdr_backup_plan_details" jsonPayload.backupVaultName:"projects/PROJECT_ID/locations/LOCATION/backupVaults/BACKUPVAULT_NAME"
    

Use the following query to view backup plans that contain a specific rule name:
    
    
        logName:"bdr_backup_plan_details" jsonPayload.backupRuleDetails.ruleName:"RULE_NAME
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter job logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
