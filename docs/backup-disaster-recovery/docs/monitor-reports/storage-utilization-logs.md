---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/storage-utilization-logs/
title: View storage resource usage logs created on a backup/recovery appliance in Cloud Logging \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:00.615281+00:00
---

# View storage resource usage logs created on a backup/recovery appliance in Cloud Logging  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/storage-utilization-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  View storage resource usage logs created on a backup/recovery appliance in Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the Backup and DR storage resource utilization logs created by Cloud Logging for backup/recovery appliances. The storage resource utilization logs provide essential insights into the data protection activities performed by applications and virtual machines (VMs). These logs include detailed information about the amount of protected data.

## Permissions and roles

You need the [IAM](https://docs.cloud.google.com/iam/docs) permission `roles/logging.viewer` to view the storage resource utilization logs. The Logs Viewer role gives you read-only access to view storage resource utilization logs of all backup/recovery appliances in the specified project. For more information about the IAM permissions and roles that apply to storage resource utilization logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View storage resource utilization logs

You can view Backup and DR storage resource utilization logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the Backup and DR storage resource utilization log entries for your backup/recovery appliances:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **gcb_backup_storage_utilization** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the Cloud Logging API. To read your log entries of backup/recovery appliances in a project, run the following command:
    
    
    ```sh
    gcloud logging read "logName : projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_storage_utilization" --project=PROJECT_ID
    ```
    

## Storage resource utilization log format

Backup and DR storage resource utilization log entries include the following fields:

**Field** | **Description**  
---|---  
Appliance name | The name of the appliance associated with the storage resource.  
Storage type | The type of storage pool, for example, perf pool, OnVault Pool, or primary pool.  
Pool name | The name of the pool.  
Total capacity (GiB) | The total capacity of the storage pool. This isn't applicable for OnVault pools.  
Used capacity (GiB) | The consumption of the storage pool.  
Appliance ID | The ID of the appliance associated with a storage resource.  
Utilization % | The percentage of vDisk and pool volume consumed. This isn't applicable for the OnVault pool.  
  
The following sample is an example log entry logged on a backup/recovery appliance `appliance-test5-64573`.
    
    
        {
          "insertId": "3302897_145859162970",
          "jsonPayload": {
            "appliance_id": "145859162970",
            "appliance_name": "appliance-test5-64573"
            "pool_name": "act_per_pool000",
            "storage_type": "perf",
            "total_capacity_in_gib": 4075.52,
            "used_capacity_in_gib": 163.84,
            "utilization_percentage": 4.020100502509347,
          },
          "resource": {
            "type": "backupdr.googleapis.com/ManagementConsole",
            "labels": {
              "location": "us-central1",
              "resource_container": "projects/xxxxxxxxxxxx",
              "management_server_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx",
            }
          },
          "timestamp": "2024-03-12T03:03:02.170Z",
          "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fgcb_backup_storage_utilization",
          "receiveTimestamp": "2024-03-12T03:03:06.740899360Z"
        }
    

## Sample queries

To view selected logs, you can write custom storage resource utilization queries in the query section

Use the following query to view all the storage resource utilization logs associated with backup/recovery appliances for a given PROJECT_ID:
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_storage_utilization"
    

Use the following query for specific storage resource details that run for a specific resource.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_storage_utilization"
        jsonPayload.appliance_name="appliance_name"
    

Use the following query for storage resource details that run for applications for a specific pool.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_storage_utilization"
        jsonPayload.pool_name="pool_name"
    

Use the following query for specific storage types.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_storage_utilization"
        jsonPayload.storage_type=("storage_type")
    

Use the following query to find applications with utilization percentage < 50%.
    
    
        logName="projects/PROJECT_ID/logs/backupdr.googleapis.com%2Fgcb_backup_storage_utilization"
        jsonPayload.utilization_percentage < 50
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter storage utilization logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
