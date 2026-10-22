---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-restore/
title: Restore an AlloyDB cluster from a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:38.303097+00:00
---

# Restore an AlloyDB cluster from a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore an AlloyDB cluster from a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This document shows you how to restore an AlloyDB cluster from a backup vault using the Google Cloud console or the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud). It describes how to restore from a vaulted backup or perform point-in-time recovery (PITR).

For more information about Backup and DR conceptual capabilities, see [Backup and DR overview](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr). If you want to backup your databases first, see [Back up AlloyDB clusters to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup).

## Disaster recovery options for your AlloyDB clusters.

Backups stored in a backup vault are independent of the source cluster's lifecycle and project.

You can restore backups even if the original workload project containing the source AlloyDB cluster is deleted. This is because the necessary decryption permissions for CMEK-encrypted backups are anchored to the Backup and DR service agent in the backup vault's project, not the workload project. This ensures that your backups remain accessible and restorable as long as the backup vault and the Cloud Key Management Service vault key are intact and the service agent has permissions.

## Before you begin

Before you restore an AlloyDB cluster from a vaulted backup, ensure you have the required roles and permissions.

To get the permissions that you need to restore an AlloyDB cluster from a vaulted backup, ask your administrator to grant you the following IAM roles: 

  * To create the restore target: [AlloyDB Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/alloydb#alloydb.admin) (`roles/alloydb.admin`) on the project where the target cluster is located 
  * To read the backup from the vault: [Backup and DR Restore User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.restoreUser) (`roles/backupdr.restoreUser`) on the project where the source backup exists 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to restore an AlloyDB cluster from a vaulted backup. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to restore an AlloyDB cluster from a vaulted backup:

  * To create the restore target: `alloydb.clusters.restore`
  * To read the backup from the vault: 
    * `backupdr.bvbackups.useReadOnlyForAlloydbCluster`
    * `backupdr.bvdataSources.useReadOnlyForAlloydbCluster`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Service agent roles and key version requirements

Because backups are incremental, a single backup can be encrypted by multiple Cloud Key Management Service key versions of the vault key if the key was rotated over time. For the restore operation to succeed, ensure the following prerequisites are met:

  * All Cloud Key Management Service key versions of the vault key used for an incremental backup must exist.

  * The Backup and DR service agent in the backup vault project must have the **Cloud KMS CryptoKey Encrypter/Decrypter** (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the vault key used for the backup.




## KMS key behavior of the restored cluster

If no specific CMEK is provided during the restore process, the restored cluster defaults to being encrypted by a Google-managed encryption key. It isn't automatically encrypted by the vault key or the original source cluster key.

If a CMEK is provided during the restore configuration, the restored cluster is encrypted with the newly specified key.

## Restore an AlloyDB cluster from a vaulted backup

To restore an AlloyDB for PostgreSQL cluster from a vaulted backup, complete the tasks in the following sections.

### Restore the backup to a new cluster

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Select the backup that you want to restore. On the **Backup details** page for the backup, or from the more_vert menu, select **Restore**.

The **Restore a backup** page displays. The **Resource type** is prefilled with `AlloyDB`.

  3. In **Resource name** , select the AlloyDB cluster to restore.

  4. Click **Backup**. A pane appears showing all available backups.

  5. Select the specific backup to restore.

  6. For **Choose the restore destination** , select the project into which you want to restore the AlloyDB cluster.

  7. Click **Continue**.

The next page shows the restore details so far, and prompts you to **Configure a new cluster**. This creates a new AlloyDB cluster based on the configuration stored in your backup. You can customize the cluster after the restore is complete.

  8. Provide a new **Cluster ID** using lowercase letters, numbers, and hyphens, starting with a letter.

  9. Choose a private connection method. There are two methods to connect services in Google Cloud or third party-hosted VPC networks, without assigning external IP addresses:

     * **Private services access** : Assigns the cluster to a single VPC network using a peering connection. Use this when connecting to specific Google Cloud and third-party services in the same VPC network as the AlloyDB cluster. This requires additional APIs.

     * **Private Service Connect** : Enables cluster access from one or more VPC networks using allowlists and Private Service Connect endpoints.

**Note:** The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within that project.



###  gcloud 
    
    
    gcloud beta alloydb clusters restore RESTORED_CLUSTER_ID \
        --project=WORKLOAD_PROJECT_ID \
        --region=REGION \
        --backupdr-backup=BACKUP_NAME
    

Replace the following:

  * `RESTORED_CLUSTER_ID`: the ID for the new AlloyDB cluster you are restoring.

  * `WORKLOAD_PROJECT_ID`: the ID of the project where you want to restore the AlloyDB cluster.

  * `REGION`: the Google Cloud region where you want to restore the AlloyDB cluster.

  * `BACKUP_NAME`: the name of the backup you want to restore.




### Create a primary instance

After Backup and DR finishes creating the cluster, [create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create) for it.

When creating the new primary instance, you need to specify its configuration, including its size and flags; Backup and DR does not store instance configuration as part of the backup. Note that the configuration need not exactly match that of the original primary instance.

When Backup and DR finishes creating the instance, you can use it to access your restored data.

### Set up read-pool instances

Finish configuring the new cluster by [setting up read-pool instances](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create), if necessary.

## Restore an AlloyDB cluster to a point in time

To restore an AlloyDB for PostgreSQL cluster to a specific point in time, complete the tasks in the following sections.

### Requirements

  * For a successful point-in-time restore (PITR) of a CMEK-encrypted source cluster, both the source cluster key and the vault key must exist and be accessible.

  * The AlloyDB for PostgreSQL service agent in the workload project must have the **Cloud KMS CryptoKeyEncrypter/Decrypter** (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the source cluster key, and the Backup and DR service agent in the backup vault project must have the **Cloud KMS CryptoKey Encrypter/Decrypter** (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) role on the vault key.




### Restore the backup to a new cluster

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the data resources that have backup plans applied and their backups stored in a backup vault within that project.

  2. At the top of the list of backups, select **Restore from a point in time**.

The **Restore from a point in time to a new cluster** pane appears, which is where you select the point in time to restore to and the details of the new cluster that you will create.

  3. Enter a target time within this cluster's recovery window to restore your cluster data from.

  4. Configure a new cluster. This creates a new AlloyDB cluster based on the configuration stored in your backup. You can customize the cluster after the restore is complete.

  5. Provide a new **Cluster ID** using lowercase letters, numbers, and hyphens, starting with a letter.

  6. Choose a private connection method. There are two methods to connect services in Google Cloud or third party-hosted VPC networks, without assigning external IP addresses:

     * **Private services access** : assigns the cluster to a single VPC network using a peering connection. Use this when connecting to specific Google Cloud and third-party services in the same VPC network as the AlloyDB cluster. This requires additional APIs.

     * **Private Service Connect** : enables cluster access from one or more VPC networks using allowlists and Private Service Connect endpoints.




###  gcloud 

  1. Find the data source ID using the following command:
         
         gcloud backup-dr data-source-references fetch-for-resource-type alloydb.googleapis.com/Cluster \
             --location=REGION \
             --project=WORKLOAD_PROJECT_ID \
             --filter='dataSourceGcpResourceInfo.gcp_resourcename="projects/WORKLOAD_PROJECT_NUMBER/locations/REGION/clusters/CLUSTER_NAME'
         

  2. Restore the cluster using the data source ID you located in the previous step:
         
         gcloud beta alloydb clusters restore RESTORED_CLUSTER_ID \
             --project=WORKLOAD_PROJECT_ID \
             --region=REGION \
             --backupdr-data-source=projects/VAULT_PROJECT_ID/locations/REGION/backupVaults/BV_ID/dataSources/DS_ID \
             --point-in-time=POINT_IN_TIME
         

Replace the following:

     * `WORKLOAD_PROJECT_ID`: the ID of the project where you want to restore the AlloyDB cluster.

     * `REGION`: the Google Cloud region where you want to restore the AlloyDB cluster.

     * `RESTORED_CLUSTER_ID`: the ID for the new AlloyDB cluster you are restoring.

     * `VAULT_PROJECT_ID`: the ID of the project containing the backup vault.

     * `BV_ID`: the ID of the backup vault.

     * `DS_ID`: the ID of the data source.

     * `POINT_IN_TIME`: the specific point in time to which you want to restore the cluster. A sample value is `2025-10-10T10:16:10Z`




### Create a primary instance

After Backup and DR finishes creating the cluster, [create a primary instance](https://docs.cloud.google.com/alloydb/docs/instance-primary-create) for it.

When creating the new primary instance, you need to specify its configuration, including its size and flags; Backup and DR does not store instance configuration as part of the backup. Note that the configuration need not exactly match that of the original primary instance.

When Backup and DR finishes creating the instance, you can use it to access your restored data.

### Set up read-pool instances

Finish configuring the new cluster by [setting up read-pool instances](https://docs.cloud.google.com/alloydb/docs/instance-read-pool-create), if necessary.

## List the backups in the backup vault

List the backups and select the backup to restore using [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud):

  1. Find the data source ID using the following command:
         
         gcloud backup-dr data-source-references fetch-for-resource-type alloydb.googleapis.com/Cluster \
              --location=REGION \
              --project=WORKLOAD_PROJECT_ID \
              --filter='dataSourceGcpResourceInfo.gcp_resourcename="projects/WORKLOAD_PROJECT_NUMBER/locations/REGION/clusters/CLUSTER_NAME "'
          ```
         

  2. List the backups using the following command:
         
         gcloud backup-dr backups list \
              --project=VAULT_PROJECT_ID \
              --location=REGION \
              --backup-vault=BV_ID \
              --data-source='projects/VAULT_PROJECT_ID/locations/REGION/backupVaults/BV_ID/dataSources/DS_ID'
         




Replace the following:

  * `REGION`: the Google Cloud region.

  * `WORKLOAD_PROJECT_ID`: the ID of the project where your AlloyDB cluster is located.

  * `WORKLOAD_PROJECT_NUMBER`: the number of the project where your AlloyDB cluster is located.

  * `CLUSTER_NAME`: the name of your AlloyDB cluster.

  * `VAULT_PROJECT_ID`: the ID of the project that contains the backup vault.

  * `BV_ID`: the ID of the backup vault.

  * `DS_ID`: the ID of the data source.




## What's next

  * [Back up AlloyDB clusters to a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/alloydb/alloydb-backup)
  * [Manage data sources in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage)
  * [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
