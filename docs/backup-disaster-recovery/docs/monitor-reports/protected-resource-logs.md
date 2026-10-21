---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-logs/
title: View protected resource logs created on a backup/recovery appliance in Cloud Logging \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:46.673999+00:00
---

# View protected resource logs created on a backup/recovery appliance in Cloud Logging  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/protected-resource-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View protected resource logs created on a backup/recovery appliance in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the protected resource logs created in Cloud Logging for backup/recovery appliances. These logs provide information about the number of applications and virtual machines (VMs) protected in an appliance. These logs are generated once every eight hours.

## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the protected resource logs. The Logs Viewer role gives you read-only access to view protected resource logs of all backup/recovery appliances in the specified project. For more information about the IAM permissions and roles that apply to protected resource logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View protected resource logs

You can view Backup and DR protected resource logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the Backup and DR protected resource log entries for your backup/recovery appliances:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **gcb_protected_resource** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Cloud Logging API. To read your protected resource log entries of backup/recovery appliances in a project, run the following command:
    
    
    ```sh
    gcloud logging read "logName : projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_protected_resource" --project=PROJECT_ID
    ```
    

## Protected resource log format

Backup and DR protected resource log entries include the following fields:

**Field** | **Description**  
---|---  
Appliance name | The name of the appliance associated with the resource.  
Resource name | The name of the resource.  
Host ID | The host ID associated with the resource.  
Hostname | The hostname associated with the resource.  
Resource ID | The resource ID.  
Resource type | The type of resource, for example, Compute Engine instance, Google Cloud VMware Engine, file system, or database.  
Protected on | The date when the resource was protected.  
Source appliance | The source appliance where the backup is taken.  
Remote appliance | The remote appliance where the backup is replicated.  
Backup plan restrictions | The restrictions applied to a backup plan. The restrictions can be `scheduler disabled`, `expiration disabled`, `snapshots disabled`, `streamsnap disabled`, `OnVault disabled`, or `process latest snapshot`.  
Backup inclusion or exclusion | The volumes or databases that are included or excluded for virtual machines or database instances.  
Appliance ID | The appliance ID associated with the protected resource.  
Source appliance ID | The source appliance ID associated with the protected resource.  
Remote appliance ID | The remote appliance ID associated with the protected resource.  
Protected data (GiB) | The size of the protected data.  
Backup template | The name of the backup template used to protect the application.  
Backup template ID | The template ID associated with the protected application.  
OnVault (GiB) | The size of data protected using OnVault pool.  
Recovery point | The timestamp when the last successful backup was taken.  
Policy overrides | The policy overrides that are set at the backup template level.  
SLA ID | The protection ID associated with the resource.  
  
The following sample is an example log entry logged on a backup/recovery appliance `baname-417-ba-12092` for a Compute Engine instance.
    
    
        {
          "insertId": "5614471_142862358970",
          "jsonPayload": {
            "protected_on": "2024-02-27T01:16:28.357675",
            "host_id": "11072",
            "sla_id": "12241",
            "onvault_in_gib": 0,
            "appliance_id": "142862358970",
            "protected_data_in_gib": 20,
            "remote_appliance": "ironman-417-ba-12092",
            "source_appliance": "ironman-417-ba-12092",
            "recovery_point": "2024-03-12T11:13:45.574",
            "backup_plan_policy_template_id": "11892",
            "resource_type": "GCPInstance",
            "backup_inclusion_or_exclusion": "NA",
            "resource_name": "test-instance-129",
            "resource_id": "11073",
            "backup_plan_restrictions": "NA",
            "policy_overrides": "NA",
            "host_name": "test-instance-129",
            "source_appliance_id": "142862358970",
            "backup_plan_policy_template": "30-min-schedule-continuous",
            "remote_appliance_id": "142862358970",
            "appliance_name": "ironman-417-ba-12092"
          },
          "resource": {
            "type": "backupdr.googleapis.com/ManagementConsole",
            "labels": {
              "resource_container": "projects/xxxxxxxxxxxx",
              "location": "us-central1",
              "management_server_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
            }
          },
          "timestamp": "2024-03-12T11:15:42.138Z",
          "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fgcb_protected_resource",
          "receiveTimestamp": "2024-03-12T11:17:56.894501906Z"
        }
    

## Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view all the protected resource logs for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_protected_resource"
    

If you are looking for protected resource logs with a backup policy template name.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_protected_resource"
         jsonPayload.backup_plan_policy_template"backup_plan_policy_template"
    

If you are looking for protected resource logs associated with a backup/recovery appliance.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_protected_resource"
        jsonPayload.appliance_name="appliance_name"
    

If you are looking for the protected resource logs associated with a particular resource.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_protected_resource"
        jsonPayload.resource_name="resource_name"
    

If you are looking for protected resource logs associated with a specific host.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_protected_resource"
        jsonPayload.host_name="hostname"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter protected resource logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
