---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/vault-consumption-logs/
title: Backup vault consumption logs for vaulted backups \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:00.129752+00:00
---

# Backup vault consumption logs for vaulted backups  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/vault-consumption-logs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Backup vault consumption logs for vaulted backups Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to view the backup vault consumption logs for the vaulted backups in Cloud Logging. These backups are for the resources protected using [backup plans](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan). These logs provide insights of the storage consumption details in a backup vault.

## Permissions and roles

You need the IAM permission `roles/logging.viewer` to view the backup vault consumption logs. The `Logs Viewer` role gives you read-only access to view backup vault consumption logs of all resources protected by backup plan in your backup vault project. For more information about the IAM permissions and roles that apply to backup vault consumption logs data, see [Access control with IAM](https://docs.cloud.google.com/logging/docs/access-control).

## View backup vault consumption logs

You can view backup vault consumption logs in Cloud Logging by using the Google Cloud console and the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Console

In the Google Cloud console, you can use the **Logs Explorer** to retrieve the backup vault consumption logs entries for your vaulted backups:

  1. In the Google Cloud console, go to the **Logging** > **Logs Explorer**.
  2. Select an existing Cloud project.
  3. In the **Query builder** pane, select **bdr_backup_vault_details** from the **Select Log name** drop-down.



### gcloud

The [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) provides a command-line interface to the logging API. To read your backup vault consumption logs entries, run the following command:
    
    
     ```gcloud
     gcloud logging read "logName: bdr_backup_vault_details" --project=PROJECT_ID
     ```
    

Replace the following:

  * `PROJECT_ID`: the name of the project where the backup vault is created.



## Backup vault consumption log format

Backup vault consumption log entries include the following fields:

Field | Description  
---|---  
`backupVaultName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup vault that is associated with the source resource.  
`sourceResourceName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the source resource.  
`minimumEnforcedRetentionDays` | The minimum timeframe in days that backups in that vault are being protected from deletion.  
`currentBackupPlanName` | The [relative name](https://docs.cloud.google.com/apis/design/resource_names#relative_resource_name) of the backup plan that is associated with the source resource.  
`firstAvailableRestorePoint` | The timestamp when the first (oldest) backup was taken, which is in the `YYYY-MM-DDTHH:MM:SS.SSSZ` format.  
`resourceType` | The type of resource that is protected in a backup vault.  
`storedBytesGib` | The amount of storage space consumed by backups in GiB.  
`lastAvailableRestorePoint` | The timestamp when the latest backup was taken, which is in the `YYYY-MM-DDTHH:MM:SS.SSSZ` format.  
  
The following sample is an example log entry logged on a backup vault `test-vault`.
    
    
            {
            "insertId": "6736263559768786491",
            "jsonPayload": {
              "backupVaultName": "projects/Backupvault_project_ID/locations/asia-east1/backupVaults/test-vault",
              "sourceResourceName": "projects/Source_project_ID/zones/asia-east1-c/instances/instance-20240826-175641",
              "minimumEnforcedRetentionDays": 1,
              "currentBackupPlanName": "projects/Backupvault_project_ID/locations/asia-east1/backupPlans/bp-asia-east1",
              "firstAvailableRestorePoint": "2024-10-08T01:10:08Z",
              "resourceType": "Compute Engine",
              "storedBytesGib": 0.73,
              "lastAvailableRestorePoint": "2024-10-08T01:10:08Z",
              "@type": "type.googleapis.com/google.cloud.backupdr.logging.v1.BDRBackupVaultDetailsLog"
            },
            "resource": {
              "type": "backupdr.googleapis.com/BackupVault",
              "labels": {
                "backup_vault_id": "projects/Backupvault_project_ID/locations/asia-east1/backupVaults/test-vault",
                "location": "asia-east1",
                "resource_container": "236738525349"
              }
            },
            "timestamp": "2024-10-08T08:01:53Z",
            "severity": "INFO",
            "logName": "projects/project_ID/logs/backupdr.googleapis.com%2Fbdr_backup_vault_details",
            "receiveTimestamp": "2024-10-08T08:12:08.404596022Z"
          }
    

## Sample queries

To view selected logs, you can write custom queries in the query section.

Use the following query to view consumption details in a backup vault.
    
    
        logName:"bdr_backup_vault_details" jsonPayload.backupVaultName:"backupVaults/BACKUPVAULT_NAME"
    

Use the following query to view consumption details using a backup plan.
    
    
        logName:"bdr_backup_vault_details" jsonPayload.currentBackupPlanName:"backupPlans/BACKUPPLAN_NAME"
    

Use the following query to view consumption details for a Compute Engine resource.
    
    
        logName:"bdr_backup_vault_details" jsonPayload.sourceResourceName:"instances/SOURCE_RESOURCE_NAME"
    

## What's next

  * To configure log-based alerts for Backup and DR, create a log query, using the filter job logs, and then [Configure log-based alerts](https://docs.cloud.google.com/backup-disaster-recovery/docs/configure-alerts).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
