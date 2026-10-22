---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-logs/
title: Daily schedule compliance logs in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:39.949085+00:00
---

# Daily schedule compliance logs in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/compliance-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Daily schedule compliance logs in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the daily schedule compliance logs created in Cloud Logging for backup/recovery appliances. These logs provide information about the compliance status of daily scheduled backup policies for your resources. These logs only show compliance for daily schedule policies and don't include weekly and monthly policies. These logs only display data for the last seven days.

Daily schedule compliance logs for each appliance are bundled together and share a common timestamp. This represents the compliance status of all daily policy schedules associated with that appliance for the preceding seven days from `DAY` to `DAY-6`. These logs won't contain information beyond the seven day timeframe.

The daily schedule compliance logs are transmitted in batches for each appliance three times a day at an eight-hour interval. The batch of logs with the latest timestamp always reflects the most up-to-date compliance picture for all daily policy schedules linked to a specific appliance.

## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the compliance logs. The Logs Viewer role gives you read-only access to view compliance logs of all backup/recovery appliances in the specified project. For more information about the IAM permissions and roles that apply to compliance logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View compliance logs

You can view Backup and DR compliance logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the Backup and DR compliance log entries for your backup/recovery appliances:

  1. In the Google Cloud console, go to **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **gcb_daily_schedule_compliance** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Cloud Logging API. To read your compliance log entries of backup/recovery appliances in a project, run the following command:
    
    
     ```sh
     gcloud logging read "logName : projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_daily_schedule_compliance" --project=PROJECT_ID
     ```
    

## Daily schedule compliance log format

Backup and DR daily schedule compliance log entries include the following fields:

  
**Field** |   
**Description**  
---|---  
  
**Appliance name** |   
The name of the appliance associated with the daily schedule backup policy.  
  
**Resource name** |   
The name of the resource associated with the daily schedule backup policy.  
  
**Backup rule policy ID** |   
The ID of the backup policy that the compliance is reported.  
  
**Host ID** |   
The host ID associated with the daily schedule backup policy.   
  
**Host name** |   
The hostname associated with the daily schedule backup policy.  
  
**Job type** |   
The daily schedule backup policy job type. It can be snapshot, OnVault, streamsnap, restore, or direct to OnVault.  
  
**Backup window start time** |   
The start time of the daily schedule backup policy window.  
  
**Status** |   
The compliance status of the daily schedule backup policy. The status can be success, failure, unknown, or blank.  
  
**Resource ID** |   
The resource ID associated with the daily schedule backup policy.  
  
**Resource type** |   
The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, or a database.  
  
**Appliance ID** |   
The appliance ID associated with the daily schedule backup policy.  
  
**Date** |   
The date that the compliance status is reported on.  
  
**Comment** |   
A description explaining the compliance status of the daily schedule backup policy.  
  
**Backup plan policy template ID** |   
The ID of the backup template of which the daily schedule backup policy is part of.   
  
**Backup rule policy name** |   
The backup policy name that the compliance has reporting for.  
  
**Backup plan policy template** |   
The name of the template that the daily schedule backup policy is part of.  
  
The following sample is an example log entry representing the compliance status for the daily backup policy schedule `logsmart_snap`.
    
    
        {
          "insertId": "209569_144675069838",
          "jsonPayload": {
            "backup_window_start_time": "19:00",
            "job_type": "Snapshot",
            "resource_id": "6223",
            "date": "2024-02-07",
            "host_name": "uistress-sql19stdm",
            "resource_type": "SqlServerWriter",
            "appliance_name": "appliance-test5-64573",
            "backup_plan_policy_template_id": "6381",
            "backup_rule_policy_name": "logsmart_snap",
            "backup_plan_policy_template": "a_logsmart",
            "backup_rule_policy_id": "6383",
            "resource_name": "DB-RMV2",
            "comment": "Job_0181855 finished at 2024-02-07 19:01 with consistency point 2024-02-07 19:01",
            "appliance_id": "xxxxxxxxxxxx",
            "status": "Success",
            "host_id": "5169"
          },
          "resource": {
            "type": "backupdr.googleapis.com/ManagementConsole",
            "labels": {
              "location": "us-central1",
              "management_server_id": "
        xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
              "resource_container": "projects/xxxxxxxxxxxx
        "
            }
          },
          "timestamp": "2024-02-08T23:15:00.704Z",
          "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fgcb_daily_schedule_compliance",
          "receiveTimestamp": "2024-02-08T23:19:21.193161111Z"
        }
    

## Sample queries

You can write custom compliance log queries in the query section to view selected logs:

Use the following query to view all the daily scheduled backup policy compliance logs for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_daily_schedule_compliance"
    

If you are looking for compliance logs where the compliance status is `failure`.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_daily_schedule_compliance"
        jsonPayload.status="Failure"
    

If you are looking for compliance logs for policies that are associated with a backup/recovery appliance.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_daily_schedule_compliance"
        jsonPayload.appliance_name="appliance_name"
    

If you are looking for the compliance logs for policies associated with a particular resource.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_daily_schedule_compliance"
        jsonPayload.resource_name="resource_name"
    

If you are looking for compliance logs associated with a specific host.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_daily_schedule_compliance"
        jsonPayload.host_name="hostname"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter compliance logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
