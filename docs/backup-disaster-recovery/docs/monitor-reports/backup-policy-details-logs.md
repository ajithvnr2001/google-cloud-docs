---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-policy-details-logs/
title: Backup policy details logs for backup/recovery appliances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:15.077494+00:00
---

# Backup policy details logs for backup/recovery appliances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/backup-policy-details-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup policy details logs for backup/recovery appliances Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the backup policy details logs created in Cloud Logging for backup/recovery appliances. These logs provide insight into the configured backup policy details and the count of resources being protected using the specific backup policies.

## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the backup policy details logs. The **Logs Viewer** role gives you read-only access to view backup policy details logs of all backup/recovery appliances in the specified project.

For more information about the IAM permissions and roles that apply to backup policy details logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View backup policy details logs

You can view backup policy details logs in Cloud Logging by using the Google Cloud console and the gcloud CLI.

###  Console 

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the backup policy details log entries for your backup/recovery appliances:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Google Cloud project.
  3. In the **Query builder** pane, select **gcb_backup_rule_policy_details** from the **Select log name** drop-down.



###  gcloud 

The gcloud CLI provides a command-line interface to the Cloud Logging API.

To read backup policy details entries of backup/recovery appliances in a project, go to **Activate cloud shell** , click **Open editor** , and run the following command:
    
    
      gcloud logging read "logName : projects/PROJECT_ID/logs/gcb_backup_rule_policy_details" \
      --project=PROJECT_ID
    

## Backup Policy details log format

Backup Policy details log entries include the following fields:

Field | Description  
---|---  
appliance_name | The name of the appliance associated with the backup policy.  
appliance_id | The id of the appliance associated with the backup policy.  
backup_plan_policy_template | The name of the template of which the backup policy is part of.  
backup_plan_policy_template_id | The ID of the template of which the backup policy is part of.  
backup_rule_policy_type | The type of the backup policy. This can take two possible values: "Local Replication" or "Remote Replication"  
backup_rule_policy_name | The name of the backup policy.  
backup_rule_policy_id | The ID of the backup policy.  
backup_consistency | This represents the [kind of backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/policy-settings) configured for the policy. Possible values are **Crash consistent** , **Take application consistent backup** or **Take crash consistent backup on last try**.  
protected_resources_count | Count of resources protected with the given template.  
schedule_disabled_resources_count | Count of resources protected with the given template but with the schedule in disabled state.  
backup_frequency_in_days | The configured schedule frequency in days for the given backup  
log_backup_frequency_in_minutes | The frequency at which database logs are backed up in minutes. This field is applicable only for database type applications, otherwise it is reported as 0 by default.  
backup_retention_period_in_days | Retention period of backups in days. This field is in decimal format and shows up to 2 decimal places.  
backup_window_start_time | Backup Window Start time in HH:MM format. This field is applicable only for windowed schedule types. It will be "N/A" by default for continuous backup schedule type.  
backup_window_end_time | Backup Window End time in HH:MM format. This field is applicable only for windowed schedule types. It will be by default "23:59" for continuous backup schedule type.  
backup_schedule_type | Backup Schedule Type. It can be WINDOWED or CONTINUOUS.  
  
The following sample is an example policy details log entry.
    
    
    {
      "insertId": "49980724_142868351806",
      "jsonPayload": {
        "backup_rule_policy_type": "Local Replication",
        "appliance_name": "sky-full-82959",
        "backup_plan_policy_template_id": 13509,
        "backup_plan_policy_template": "testtemplate",
        "log_backup_frequency_in_minutes": 0,
        "backup_frequency_in_days": 1,
        "schedule_disabled_resources_count": 17,
        "backup_rule_policy_id": 13511,
        "backup_consistency": "Crash Consistency Backup",
        "protected_resources_count": 16,
        "backup_schedule_type": "WINDOWED",
        "backup_rule_policy_name": "testPolicy1",
        "backup_window_end_time": "07:00",
        "backup_window_start_time": "19:00",
        "appliance_id": "142868351806",
        "backup_retention_period_in_days": 2
      },
      "resource": {
        "type": "backupdr.googleapis.com/ManagementConsole",
        "labels": {
          "location": "us-central1",
          "management_server_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
          "resource_container": "projects/652683419448"
        }
      },
      "timestamp": "2024-07-26T04:34:46.504Z",
      "logName": "projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_rule_policy_details",
      "receiveTimestamp": "2024-07-26T04:36:29.496918995Z"
    }
    

## Sample queries

You can write custom queries in the query section to view selected logs.

Use the following query to view all the backup policy details logs associated with backup/recovery appliances for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_rule_policy_details"
    

Use the following query for specific appliance backup policy details.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_rule_policy_details"
    jsonPayload.appliance_name="<appliance_name>"
    

Use the following query for backup policy details for a specific backup template.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_recovery_jobs"
    jsonPayload.backup_plan_policy_template="<backup_template>"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter job logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
