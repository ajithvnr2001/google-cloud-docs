---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup/
title: Back up AlloyDB clusters to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:23.456075+00:00
---

# Back up AlloyDB clusters to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up AlloyDB clusters to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to back up AlloyDB to a backup vault. Sending backups to a backup vault provides immutability and enforced retention.

**Note:** Enable the [30-day introductory trial for Backup and DR](https://docs.cloud.google.com/backup-disaster-recovery/docs/30-day-introductory-trial/intro-trial) to explore a unified, centralized backup solution featuring immutable backup vaults.

In the Google Cloud console, you can back up AlloyDB for PostgreSQL clusters to a backup vault by applying backup plans. You can back up in either of these two ways. Both methods allow you to store your backups securely in a backup vault, providing a reliable way to recover your AlloyDB clusters in case of data loss or other unexpected events.

  * **Scheduled backups**. You can automatically back up AlloyDB for PostgreSQL clusters at specific intervals, such as daily, weekly, monthly, or yearly.
  * **On-demand backups**. You can create on-demand backups whenever needed. On-demand backups are useful for creating backups before making significant changes to your databases or for ad hoc data protection.



## Before you begin

  1. Enable the Backup and DR API where the AlloyDB for PostgreSQL clusters are located.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

     1. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create)
     2. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)

**Note:** If you create a backup plan using the gcloud CLI, specify the `--log-retention-days=13` flag (or another valid duration above the backup vault's minimum enforced retention) during plan creation to enable Point-in-Time Recovery (PITR). Unlike the Google Cloud console, which defaults to a recommended 13-day log retention, programmatic plan creation via the gcloud CLI leaves log retention disabled if unspecified.
     3. Assign IAM roles and permission to the backup user

     4. Grant backup vault access in the AlloyDB project

     5. Set up Observability Analytics on your bucket to monitor Backup and DR backup jobs.




## IAM roles and permissions for the backup user

To get the permissions that you need to configure scheduled backups or run on-demand backups, ask your administrator to grant you the following IAM roles on your backup vault project: 

  * [Backup and DR Backup User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)
  * [Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure scheduled backups or run on-demand backups. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure scheduled backups or run on-demand backups:

  * `backupdr.backupPlans.list`
  * `backupdr.backupPlanAssociations.createForAlloydbCluster`
  * `backupdr.backupPlanAssociations.fetchForAlloydbCluster`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.getForAlloydbCluster`
  * `backupdr.backupPlanAssociations.triggerBackupForAlloydbCluster`
  * `backupdr.backupPlanAssociations.deleteForAlloydbCluster`
  * `backupdr.backupPlans.useForAlloydbCluster`
  * `backupdr.locations.list`
  * `backupdr.operations.get`
  * `cloudasset.assets.searchAllResources`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

The following table lists the dynamic permissions required for each API call:

Resource | Action to be Performed on the Resource | Permissions required for each API call | Project where it needs to be assigned  
---|---|---|---  
Backup vault | Create BackupVault | backupdr.backupVaults.create | Admin project  
| Delete BackupVault | backupdr.backupVaults.delete | Admin project  
| Update BackupVault | backupdr.backupVaults.update | Admin project  
| List BackupVaults | backupdr.backupVaults.list | Admin project  
| Get BackupVault | backupdr.backupVaults.get | Admin project  
Backup plan | Create BackupPlan | backupdr.backupPlans.create | Admin project  
| Delete BackupPlan | backupdr.backupPlans.delete | Admin project  
| Get BackupPlan | backupdr.backupPlans.get | Admin project  
| List Backup Plans | backupdr.backupPlans.list | Admin project  
Backup Plan Associations | Create Backup Plan Association | backupdr.backupPlanAssociations.createForAlloydbCluster | Workload project  
| Delete Backup Plan Association | backupdr.backupPlanAssociations.deleteForAlloydbCluster | Workload project  
| Trigger an on-demand backup on Backup Plan Association | backupdr.backupPlanAssociations.triggerBackupForAlloydbCluster | Workload project  
| Get Backup Plan Association | backupdr.backupPlanAssociations.getForAlloydbCluster | Workload project  
| List Backup Plan Associations | backupdr.backupPlanAssociations.list | Workload project  
| Fetch Backup Plan Associations | backupdr.backupPlanAssociations.fetchForAlloydbCluster | Workload project  
Data Source | Get DataSource | backupdr.bvdataSources.get | Admin project  
| List DataSources | backupdr.bvdataSources.list | Admin project  
| PiTR Restore | backupdr.bvdataSources.useReadOnlyForAlloydbCluster | Admin project  
Backups | Get Backup | backupdr.bvbackups.get | Admin project  
| List Backups | backupdr.bvbackups.list | Admin project  
| Delete Backup | backupdr.bvbackups.delete | Admin project  
| Restore Backup | backupdr.bvbackups.useReadOnlyForAlloydbCluster | Admin project  
Data Source References | Get DataSource Reference | backupdr.dataSourceReferences.getForAlloydbCluster | Workload project  
| Fetch DataSource References | backupdr.dataSourceReferences.fetchForAlloydbCluster | Workload project  
Operations | List Operations | backupdr.operations.list | Respective project  
| Get Operations | backupdr.operations.get | Respective project  
  
## Grant backup vault access in the AlloyDB for PostgreSQL project

To back up an AlloyDB cluster in a project different from where the backup vault is created, you must grant the Backup and DR AlloyDB Operator (`roles/backupdr.alloydbOperator`) IAM role to the backup vault service agent within the AlloyDB project. If the backup vault project where the backups will be stored is different from the AlloyDB project, then assign the role to the backup vault service agent within the AlloyDB project.

To back up an AlloyDB cluster in the same project where the backup vault is created, no roles are required to be granted.

For information about granting roles to the backup vault service agent within the project you intend to back up, see [Grant a role to the service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service_agent).

## Configure a scheduled backup

To configure a scheduled backup for AlloyDB clusters, use the following instructions.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backup**.

  3. From the **Resource Type** list, select **AlloyDB**.

  4. From the **Project** list, select a project where the AlloyDB cluster is located.

  5. From the **Region** list, select the region where your clusters are located.

  6. From the **Resources** list, click **Browse**. Choose the AlloyDB cluster that you want to back up and click **Done**.

  7. Click **Continue**.

  8. From the **Backup plan** list, click **Select**.

  9. Choose a backup plan that you want to protect the AlloyDB clusters with.

  10. Click **Done**.

  11. Review the backup details and click **Schedule**.




###  gcloud 

  1. Configure a scheduled backup.
         
         gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME \
               --location=ALLOYDB_REGION \
               --project=ALLOYDB_PROJECT_ID \
               --resource=projects/ALLOYDB_PROJECT_ID/clusters/ALLOYDB_CLUSTER_ID \
               --resource-type=alloydb.googleapis.com/Cluster \
               --backup-plan=projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUP_PLAN
           ```
         
         Replace the following:
         

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
     * `ALLOYDB_REGION`: the region where the AlloyDB clusters are located.
     * `ALLOYDB_PROJECT_ID`: the name of the project where the AlloyDB clusters are located.
     * `ALLOYDB_CLUSTER_ID`: the AlloyDB cluster ID.
     * `PROJECT_ID`: the name of the project where backup plans exist.
     * `LOCATION`: the location of the cluster.



## List clusters for which backups are scheduled

To list the AlloyDB clusters for which backups are scheduled, use the following instructions.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. At the top of the table, select **Filter table** > **Resource type**. Select **AlloyDB**. This filters the display to show only the AlloyDB clusters that have backup plans applied and backups stored in a backup vault within a project.




###  gcloud 

List AlloyDB clusters for which backups are scheduled:
    
    
      gcloud backup-dr backup-plan-associations fetch-for-resource-type alloydb.googleapis.com/Cluster \
      --location=LOCATION \
      --project=PROJECT_ID
    

Replace the following:

  * LOCATION: the location of the scheduled backups.
  * PROJECT_ID: the name of the project where the AlloyDB clusters are located.



## Create an on-demand backup

You can initiate an on-demand backup for an AlloyDB cluster with a backup plan by triggering the backup rule of your choice to run immediately. On-demand backups typically capture only the data changed since the last backup (incremental).

When creating an on-demand backup, you can choose a rule from the backup plan associated with the AlloyDB cluster. This rule determines when the on-demand backup gets deleted. You can check the backup job status from the **Jobs** page. For more information, see [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

**Note:** You can only run one backup job at a time. If an on-demand or scheduled backup job is already in progress, then attempting to start another on-demand backup job, the new job fails with the `Unable to queue the operation` error.

Use the following instructions to create an on-demand backup.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the resource to back up. Either from the more_vert menu, or from the details page for the resource, select **Create on-demand backup**.

  3. Specify when the backup will be deleted using one of the following options:

     * **Based on custom retention period** ([Preview](https://docs.cloud.google.com/products#product-launch-stages)): add a custom, on-demand retention period to your backup plan, which by default, is set to the backup vault's minimum enforced retention period, plus an additional 30 days.
     * **Based on an existing backup rule** : select the existing rule from the **Delete backups after** drop-down menu.
  4. Click **Create** to start the on-demand backup creation.

  5. To view the status of the on-demand backup job, click **Notifications**.


**Note:** The on-demand backup is stored in the backup vault that is configured with the associated backup plan.

###  gcloud 

Create an on-demand backup using one of the following options:

  * **Based on a backup rule** :
        
        gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
        --backup-rule-id=RULE_ID \
        --project=PROJECT_ID \
        --location=LOCATION \
        [--no-async]
        

  * **Based on custom retention** :
        
        gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
        --custom-retention-days=CUSTOM_RETENTION \
        --project=PROJECT_ID \
        --location=LOCATION \
        --labels=LABELS
        

Replace the following:

    * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association. 

**Note:** To get a list of backup plans associated with the AlloyDB cluster, run the command `gcloud backup-dr backup-plan-associations fetch-for-resource-type alloydb.googleapis.com/Cluster --location=LOCATION --project=PROJECT_ID`
    * `RULE_ID`: the backup rule name that you want to associate to run on-demand backups.

    * `PROJECT_ID`: the name of the project.

    * `LOCATION`: the location of the scheduled backups.

    * `CUSTOM_RETENTION`: The custom retention period in days for this on-demand backup. This value must be equal to or greater than the backup vault retention time and less than or equal to the max-custom-on-demand-retention-days value that is configured in the backup plan (or the vault retention time + 30 days if max-custom-on-demand-retention-days is not configured).

    * `LABELS`: optional labels for the backup as comma-separated key-value pairs such as `webserver=backend,media=images`.




## Change the backup plan applied to an AlloyDB cluster

You can change the backup plan applied to an AlloyDB cluster to another backup plan. The other backup plan must meet these criteria:

  * Use the same backup vault
  * Be in the same region as the AlloyDB cluster



Use the following instructions to change the backup plan associated with an AlloyDB cluster.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the backup that will get a different plan. Either from the backup details page for the backup, or from the more_vert menu, select **Change backup plan**. The **Select a backup plan** window lists only the backup plans that are valid for this cluster.

  3. Select a backup plan and click **Apply**.




###  gcloud 

  * Change the assigned backup plan.
        
        gcloud backup-dr backup-plan-associations update BACKUP_PLAN_ASSOCIATION_NAME \
          --workload-project=ALLOYDB_PROJECT_ID \
          --location=ALLOYDB_REGION \
          --backup-plan=BACKUP_PLAN \
          --project=PROJECT_ID
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association resource.
    * `ALLOYDB_PROJECT_ID`: the project ID of the AlloyDB cluster.
    * `ALLOYDB_REGION`: the location of the AlloyDB cluster.
    * `BACKUP_PLAN`: the name of the backup plan that you are switching to.
    * `PROJECT_ID`: the project ID of the selected backup plan.



## Unprotect an AlloyDB cluster

You can unprotect an AlloyDB cluster by removing the backup plan applied to the cluster. Removing a backup plan from an AlloyDB cluster doesn't delete any backups created while the backup plan was in use. You can still access and manage these existing backups until they expire.

To unprotect an AlloyDB cluster, use these instructions.

###  Console 

  1. In the Google Cloud console, go to the Backup and DR **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click the name of the database that you want to remove a backup plan from.

  3. Select **Remove backup plan**.




###  gcloud 

Unprotect an AlloyDB cluster.
    
    
      gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME \
      --project=PROJECT_ID \
      --location=LOCATION
    

Replace the following:

  * BACKUP_PLAN_ASSOCIATION_NAME: the name of the backup plan association that you want to delete.
  * PROJECT_ID: the name of the project.
  * LOCATION: the location of the scheduled backup.



## Encrypt AlloyDB cluster backups

Unlike some other workloads, AlloyDB cluster backups use the Backup and DR backup vault key to encrypt the backup, rather than the source cluster key. For more information about customer-managed encryption keys, see [Customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek).

**Important:** The Backup and DR service agent requires Cloud Key Management Service CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) access to the vault key to successfully perform backup and restore operations.

### Incremental backups and key rotation

Because backups are incremental in nature, a single backup can be encrypted by multiple Cloud Key Management Service key versions of the vault key if the key version was rotated over time.

### Key tracking

You can refer to the Cloud Key Management Service key tracking page to monitor and track the Cloud Key Management Service key versions used for any given backup.

## What's next

  * [Restore an AlloyDB cluster from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-restore)
  * [Manage data sources in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage)
  * [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
