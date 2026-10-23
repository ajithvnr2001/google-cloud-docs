---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/vaulted-protected-resource/
title: Protected resource logs for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:18.062387+00:00
---

# Protected resource logs for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/vaulted-protected-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protected resource logs for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the protected resource logs for vaulted backups in Cloud Logging. These logs provide insights of the resources protected and have their backups stored in the backup vault using the [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan). You can view these logs in the project where the backup vault is created.

If you want to view the backups logs of the resources that are protected using the backup template in the appliance management console, see [Protected resource logs](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-logs).

## Permissions and roles

You need the IAM permission `roles/logging.viewer` to view the protected resource logs. The `Logs Viewer` role gives you read-only access to view protected resource logs of all resources protected by backup plan in your backup vault project. For more information about the IAM permissions and roles that apply to protected resource logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View protected resource logs

You can view Backup and DR protected resource logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). To view the protected resource log, select the project where the backup vault is created.

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the protected resource logs entries for your vaulted backups:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project, where the backup vault is created.
  3. In the **Query builder** pane, select **bdr_protected_resource** from the **Select log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the logging API. To read your protected resource log entries of a project, run the following command:
    
    
     ```gcloud
     gcloud logging read "logName: bdr_protected_resource" --project=PROJECT_ID
     ```
    

Replace the following:

  * `PROJECT_ID`: the name of the project where the backup vault is created.



## Protected resource log format

Protected resource log entries include the following fields:

Field | Description  
---|---  
`sourceResourceLocation` | The location of the source resource.  
`sourceResourceId` | The ID of the source resource.  
`currentBackupVaultName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup vault that is associated with the source resource.  
`currentBackupRuleDetails` | The backup rule details of the backup plan that is associated with the source resource.  
`ruleName` | The name of the backup rule used to backup jobs.  
`retentionDays` | The duration in days for which the backups should be retained in the backup vault before they are deleted.  
`recurrenceSchedule` | The recurrence schedule of a backup based on the backup rule.  
`backupWindow` | The backup window where you have defined the timeframe of when backup jobs can start. The backup window uses the 24-hour clock format, with start and end times between 00 and 24 hours, and a minimum of six hours for the window.  
`recurrence` | The backup recurrence type, which can be hourly, daily, weekly, monthly, or yearly.  
`lastProtectedOn` | The timestamp when the resource was last protected, which is in the `YYYY-MM-DDTHH:MM:SS.SSSZ` format.  
`currentBackupPlanName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup plan that is associated with the source resource.  
`sourceResourceName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the resource.  
`resourceType` | The type of resource. For example, a Compute Engine instance.  
`sourceResourceDataSizeGib` | The size of the source resource.  
  
The following sample is an example of a log entry for viewing protected resources stored in the backup vault `doc-test`.
    
    
          {
            "insertId": "15471111095544249995",
            "jsonPayload": {
              "lastProtectedOn": "2024-08-21T06:51:54Z",
              "currentBackupRuleDetails": [
                {
                  "backupWindow": "01:00 to 23:00",
                  "retentionDays": 14,
                  "recurrence": "Hourly",
                  "recurrenceSchedule": "Every 6 hours",
                  "backupWindowTimezone": "Etc/UTC",
                  "ruleName": "random-plan"
                }
              ],
              "sourceResourceDataSizeGib": 10,
              "currentBackupPlanName": "projects/Backupvault_project_ID/locations/us-central1/backupPlans/backup-plan",
              "resourceType": "Compute Engine",
              "currentBackupVaultName": "projects/Backupvault_project_ID/locations/us-central1/backupVaults/doc-set",
              "sourceResourceLocation": "us-central1-a",
              "sourceResourceId": "1606474933247566298",
              "sourceResourceName": "projects/Source_project_ID/zones/us-central1-a/instances/farhanmd-log-test--instance",
              "@type": "type.googleapis.com/google.cloud.backupdr.logging.v1.BDRProtectedResourceLog"
            },
            "resource": {
              "type": "backupdr.googleapis.com/BackupPlan",
              "labels": {
                "location": "us-central1",
                "backup_plan_id": "backup-plan",
                "resource_container": "236738525349"
              }
            },
            "timestamp": "2024-11-05T10:39:03Z",
            "severity": "INFO",
            "logName": "projects/Backupvault_Name/logs/backupdr.googleapis.com%2Fbdr_protected_resource",
            "receiveTimestamp": "2024-11-05T10:50:34.275819255Z"
          }
    

## Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view resources protected using a backup plan.
    
    
        logName:"bdr_protected_resource" jsonPayload.currentBackupPlanName:"backupPlans/BACKUPPLAN_NAME"
    

Use the following query to view resources protected in a backup vault.
    
    
        logName:"bdr_protected_resource" jsonPayload.currentBackupVaultName:"backupVaults/BACKUPVAULT_NAME"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter job logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
