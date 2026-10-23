---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-restore/
title: Restore a Cloud SQL instance from a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:57.522341+00:00
---

# Restore a Cloud SQL instance from a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore a Cloud SQL instance from a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to restore a Cloud SQL instance from a backup vault using the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). It describes how to restore to a new or existing instance, overwrite a source instance, or perform point-in-time recovery (PITR).

For more information about Backup and DR conceptual capabilities, see [Backup and DR overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr). If you want to backup your databases first, see [Back up Cloud SQL instances to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/sql/csql-backup).

## Disaster recovery and resilience

Backup and DR provides disaster recovery options for your Cloud SQL instances. Backups stored in a backup vault are independent of the source instance's lifecycle and project.

  * **Project deletion** : you can restore backups even if the original workload project containing the source Cloud SQL instance has been deleted. This is because the necessary decryption permissions for CMEK-encrypted backups are granted to the Backup and DR service agent within the backup vault's project, not the workload project. This ensures that your backups remain accessible and restorable as long as the backup vault and the Cloud Key Management Service key are intact and the service agent has permissions.

  * **Flexible restore targets** : you can restore to a new instance in the same or a different project, providing flexibility in recovery scenarios.




## Before you begin

Before you restore a Cloud SQL instance from a backup vault, ensure you have the required roles.

To get the permissions that you need to restore a Cloud SQL instance from a backup vault, ask your administrator to grant you the following IAM roles: 

  * To create the restore target: [Cloud SQL Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.admin) (`roles/cloudsql.admin`) on the project where the target instance is located 
  * To read the backup from the vault: [Backup and DR Restore User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`) on the project where the source backups exist 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to restore a Cloud SQL instance from a backup vault. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to restore a Cloud SQL instance from a backup vault:

  * To create the restore target: `cloudsql.instances.restore`
  * To read the backup from the vault: `backupdr.bvbackups.useReadOnlyForCloudSqlInstance`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Caution:** If the source Cloud SQL instance is protected with a customer-managed encryption key (CMEK), you cannot restore its backup if the **Cloud KMS CryptoKey Encrypter/Decrypter** (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role is revoked from the Backup and DR service agent (in the project where the backup vault is located) on the source instance's KMS key. 

## Restore a Cloud SQL instance from the most recent backup

Use the following instructions to restore a Cloud SQL instance:

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within that project.

  2. Select the backup that you want to restore. Either from the backup details page for the backup, or from the more_vert menu, select **Restore**.

The **Restore page** displays where you select the following restore options:

     * The **Resource type** is prefilled with `Cloud SQL`.

     * In **Resource name** , select the Cloud SQL instance to restore.

     * When you click **Backup** , a pane opens showing all available backups. Select the specific backup to restore.

     * For **Choose the restore destination** , select the project into which you want to restore the Cloud SQL instance.

  3. Click **Continue**.

  4. When you're prompted to **Choose restore destination** , make a selection from the following options:

     * **Restore to a new instance** : creates a new instance based on the configuration stored in your backup. You can customize the instance after the restore is complete. Provide a new **Instance ID** using lowercase letters, numbers, and hyphens. Start with a letter.
**Note:** When restoring a Cloud SQL instance from a CMEK-encrypted backup, the restored instance will, by default, be encrypted using the same Cloud KMS key that protected the source instance at the time of backup. You have the option to specify a different Cloud Key Management Service key for the target instance during the restore process.**Note:** During cross-region restores to a new instance, it's required to re-encrypt the restored Cloud SQL instance with a different Cloud Key Management Service key that resides in the restored target's region (not applicable when overwriting an existing instance).
     * **Overwrite an existing instance** : select an existing instance to overwrite from the list of available instances.

     * **Overwrite the source instance** : overwrites your current instance. All the current data on the selected instance will be overwritten, including previous point-in-time recovery logs. The overwritten data cannot be recovered later. This is not recommended for production use.




###  gcloud 

  1. Find the data source that contains the backup that you want to restore. You can find the data source from a Cloud SQL instance project or a backup vault project:

     * From Cloud SQL instance project: Use `data-source-reference`
           
           gcloud alpha backup-dr data-source-references fetch-for-resource-type sqladmin.googleapis.com/Instance \
           --location=LOCATION \
           --project=CSQL_INSTANCE_PROJECT_ID \
           --filter='dataSourceGcpResourceInfo.cloudSqlInstanceProperties.name="projects/CSQL_INSTANCE_PROJECT_ID/instances/CSQL_INSTANCE_ID"' \
           --format="table(RESOURCE_NAME,DATA_SOURCE)"
           

Replace the following:

       * LOCATION: the location of the backup vault.

       * CSQL_INSTANCE_ID: the database name of the Cloud SQL instance.

       * CSQL_INSTANCE_PROJECT_ID: the project containing the Cloud SQL instance.

     * From a backup vault project: Use `data-source`
           
           gcloud backup-dr data-sources list \
           --location=LOCATION \
           --project=BACKUP_VAULT_PROJECT_ID \
           --filter='dataSourceGcpResource.cloudSqlInstanceDatasourceProperties.name=projects/CSQL_INSTANCE_PROJECT_ID/instances/CSQL_INSTANCE_ID' \
           --format="table(dataSourceGcpResource.cloudSqlInstanceDatasourceProperties.name:label=RESOURCE_NAME,name:label=DATA_SOURCE)"
           

Replace the following:

       * LOCATION: the location of the backup vault.

       * CSQL_INSTANCE_ID: the name of the Cloud SQL instance.

       * CSQL_INSTANCE_PROJECT_ID: the project containing the Cloud SQL instance.

       * BACKUP_VAULT_PROJECT_ID: the project containing the backup vault.

  2. List and select the backup to restore by listing all the backups in the data source using the `gcloud backup-dr backups list` command.
         
         gcloud backup-dr backups list --data-source=DATA_SOURCE \
         --format="table(consistencyTime,backupType,name:label=BACKUP_NAME)"
         

  3. Restore a Cloud SQL instance using the `gcloud sql backups restore` command:
         
         gcloud sql backups restore BACKUP_NAME \
         --restore-instance=RESTORE_INSTANCE \
         --project=RESTORE_PROJECT
         --region=RESTORE_REGION
         

Replace the following:

     * BACKUP_NAME: the backup vault name you want to restore data from.

     * RESTORE_INSTANCE: the target Cloud SQL instance name.

     * RESTORE_PROJECT: the project where you want to restore the Cloud SQL instance.

     * RESTORE_REGION: the region where you want to restore to a new Cloud SQL instance. This is optional for regional backups. Don't use when restoring to an existing instance.

**Note:** During cross-region restores to a new instance, it's required to re-encrypt the restored Cloud SQL instance with a different Cloud Key Management Service key that resides in the restored target's region (not applicable when overwriting an existing instance).
  4. Optional: to override other properties, see [Overview of Backup and DR ](https://cloud.google.com/sdk/gcloud/reference/alpha/backup-dr/backups/restore)[gcloud CLI](https://docs.cloud.google.com/sdk/gcloud) commands.




## Restore a Cloud SQL instance to a different point-in-time

Use the following instructions to restore a Cloud SQL instance to a point in time. When you restore to a point in time, you create a Cloud SQL clone.

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. At the top of the table, select **Filter table** and then click **Resource type**. Select **Cloud SQL**. This limits the display to only the Cloud SQL instances that have backup plans applied and their backups stored in a backup vault within a project.

  3. Click **Restore from a point in time**. The Cloud SQL **Create a clone** page opens.

  4. Follow the procedures in [Perform PITR by using the backup vault](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#backup-vault-pitr).


**Note:** To restore a deleted instance using Point-In-Time Recovery, see [Restoring a Deleted Instance](https://docs.cloud.google.com/sql/docs/mysql/backup-recovery/pitr#perform-pitr-deleted-instance).

## Monitor restore and point-in-time restore jobs

When you trigger a restore or point-in-time restore (PITR) on a Cloud SQL instance, Backup and DR automatically tracks the job. You can monitor the progress and status of the job in the Google Cloud console.

**Note:** Cloud SQL restore monitoring is only available in regions where both Backup and DR and Cloud SQL are available.

To view the progress and status of the restore and PITR jobs:

  1. In the Google Cloud console, go to the Backup and DR **Jobs** page.
  2. Look for the job with the **Resource type** set to `Cloud SQL` and **Job category** set to `Restore` or `Point-in-Time Restore (PITR)`.



You can view restore and PITR job logs in both the workload project, where the target Cloud SQL instance is restored, and the backup vault project, where the backup is stored. Job details can be viewed in Backup and DR **Jobs** page and in Cloud Logging.

For more information, see [Monitor jobs in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

## What's next

For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
