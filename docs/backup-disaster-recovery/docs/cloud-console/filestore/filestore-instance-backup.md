---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup/
title: Back up Filestore instances to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:28.386978+00:00
---

# Back up Filestore instances to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up Filestore instances to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to back up Filestore instances to a Backup and DR backup vault including how to grant backup vault access in your Filestore project, configure scheduled backups, create on-demand backups, and how to manage your vaulted backups.

## Overview

Sending backups to a backup vault provides immutability and enforced retention. With a backup vault, you can store backups in a single region or in a multi-region. You can learn more about backup vaults at [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

## IAM roles and permissions for the backup user

To get the permissions that you need to configure scheduled backups or run on-demand backups, ask your administrator to grant you the following IAM roles on your backup vault project: 

  * [Backup and DR Backup User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)
  * [Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure scheduled backups or run on-demand backups. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure scheduled backups or run on-demand backups:

  * `backupdr.backupPlans.list`
  * `backupdr.backupPlanAssociations.createForFilestoreInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.get`
  * `backupdr.backupPlanAssociations.triggerBackupForFilestoreInstance`
  * `backupdr.backupPlanAssociations.deleteForFilestoreInstance`
  * `backupdr.backupPlans.useForFilestoreInstance`
  * `backupdr.locations.list`
  * `backupdr.operations.get`
  * `cloudasset.assets.searchAllResources`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Caution:** If you disable, delete, or modify the permissions of a customer-managed encryption key (CMEK) used for active Filestore backup chains, the associated backups become unrestorable. To ensure backups can be successfully restored, don't disable, delete, or modify the permissions of any KMS key associated with ongoing backup chains

The following table lists the dynamic permissions required for each API call:

Resource | Action to be Performed on the Resource | Permissions required for each API call | Project where it needs to be assigned  
---|---|---|---  
Backup vault | Create BackupVault | `backupdr.backupVaults.create` | Admin project  
| Delete BackupVault | `backupdr.backupVaults.delete` | Admin project  
| Update BackupVault | `backupdr.backupVaults.update` | Admin project  
| List BackupVaults | `backupdr.backupVaults.list` | Admin project  
| Get BackupVault | `backupdr.backupVaults.get` | Admin project  
Backup plan | Create BackupPlan | `backupdr.backupPlans.create` | Admin project  
| Delete BackupPlan | `backupdr.backupPlans.delete` | Admin project  
| Get BackupPlan | `backupdr.backupPlans.get` | Admin project  
| List Backup Plans | `backupdr.backupPlans.list` | Admin project  
Backup Plan Associations | Create Backup Plan Association | `file.instances.updateBackupDrConfig` | Workload project  
|  | `backupdr.backupPlanAssociations.createForFilestoreInstance` | Workload project  
|  | `backupdr.backupPlans.useForFilestoreInstance` | Admin project  
| Delete Backup Plan Association | `backupdr.backupPlanAssociations.deleteForFilestoreInstance` | Workload project  
|  | `file.instances.updateBackupDrConfig` | Workload project  
| Trigger an on-demand backup on Backup Plan Association | `backupdr.backupPlanAssociations.triggerBackupForFilestoreInstance` | Workload project  
| Get Backup Plan Association | `backupdr.backupPlanAssociations.getForFilestoreInstance` | Workload project  
| List Backup Plan Associations | `backupdr.backupPlanAssociations.list` | Workload project  
| Fetch Backup Plan Associations | `backupdr.backupPlanAssociations.fetchForFilestoreInstance` | Workload project  
Data Source | Get DataSource | `backupdr.bvdataSources.get` | Admin project  
| List DataSources | `backupdr.backupPlanAssociations.list` | Admin project  
Backups | Get Backup | `backupdr.bvbackups.get` | Admin project  
| List Backups | `backupdr.bvbackups.list` | Admin project  
| Delete Backup | `backupdr.bvbackups.delete` | Admin project  
| Restore Backup | `backupdr.bvbackups.useReadOnlyForFilestoreInstance` | Admin project  
Data Source References | Get DataSource Reference | `backupdr.dataSourceReferences.getForFilestoreInstance` | Workload project  
| Fetch DataSource References | `backupdr.dataSourceReferences.fetchForFilestoreInstance` | Workload project  
Operations | List Operations | `backupdr.operations.list` | Respective project  
| Get Operations | `backupdr.operations.get` | Respective project  
  
## Grant backup vault access in the Filestore project

To back up a Filestore instance in a project different from where the backup vault is created, you must grant the Backup and DR Filestore Operator (Beta) (`roles/backupdr.filestoreOperator`) IAM role for the backup vault service agent of the vault in the target project where the Filestore backup is to be performed.

To back up a Filestore instance in the same project as where the backup vault is created, no roles are required to be granted.

For information about granting roles to the backup vault service agent within the project you intend to back up, see [Grant a role to the service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service_agent).

### Grant CMEK permissions for CMEK-enabled backup vaults

If you store backups in a CMEK-enabled backup vault, you must grant the Cloud KMS CryptoKey Encrypter/Decrypter (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) IAM role to the Backup and DR service agent of the vault's project on the backup vault's CMEK key.

**Note:** Backup and DR proactively blocks backup plan association (BPA) creation if the Backup and DR service agent (P4SA) of the vault project does not have permissions on the backup vault's CMEK key.

To grant the required role on the CMEK key, run the following command:
    
    
    gcloud kms keys add-iam-policy-binding KEY_NAME \
        --keyring=KEY_RING_NAME \
        --location=LOCATION \
        --member="serviceAccount:service-VAULT_PROJECT_NUMBER@gcp-sa-backupdr.iam.gserviceaccount.com" \
        --role="roles/cloudkms.cryptoKeyEncrypterDecrypter"
    

Replace the following:

  * `KEY_NAME`: the name of the Cloud Key Management Service key configured on the backup vault.
  * `KEY_RING_NAME`: the name of the key ring where the key is stored.
  * `LOCATION`: the location of the key ring.
  * `VAULT_PROJECT_NUMBER`: the project number where the backup vault is located.



## Before you begin

  1. Enable the Backup and DR API where the Filestore instances are located.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  2. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create)

  3. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)

  4. Assign IAM roles and permission to the backup user

  5. Grant backup vault access in the Filestore project

  6. Set up Observability Analytics on your bucket to monitor Backup and DR backup jobs.

  7. **For CMEK-enabled instances** : If you store backups in a CMEK-enabled backup vault, you must grant the required CMEK permissions to the Backup and DR service agent on the backup vault's CMEK key.




## Back up a Filestore instance

You back up Filestore instances to a backup vault by applying backup plans. You can back up your data using either of the following methods:

  * Configure a scheduled backup: automatically back up Filestore instances at specific intervals, such as daily, weekly, monthly, or yearly.

  * Create an on-demand backup: create on-demand backups whenever needed, such as before making significant changes to your instances or for _ad hoc_ data protection.




## Configure a scheduled backup

Use the following instructions to configure a scheduled backup for Filestore instances.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backup**.

  3. From the **Resource type** list, select **Filestore instance**.

  4. From the **Project** list, select a project where the Filestore instance is located.

  5. From the **Region** list, select the region where your instance is located.

  6. From the **Resources** list, click **Browse**. Choose the Filestore instance that you want to back up and click **Done**.

  7. Click **Continue**.

  8. From the **Backup plan** list, click **Select**.

  9. Choose a backup plan that you want to protect the Filestore instance with.

  10. Click **Done**.

  11. Review the backup details and click **Schedule**.




###  gcloud 

  1. Configure a scheduled backup.
         
         gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME   
         
           --location=LOCATION   
         
           --backup-plan=BACKUP_PLAN   
         
           --resource=projects/PROJECT_ID/locations/RESOURCE_LOCATION/instances/INSTANCE_NAME   
         
           --resource-type='file.googleapis.com/Instance'
           

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: The name of the backup plan association.
     * `LOCATION`: The location of the backup plan association.
     * `BACKUP_PLAN`: The name of the backup plan.
     * `PROJECT_ID`: The project ID of the Filestore instance.
     * `RESOURCE_LOCATION`: The location of the resource.

The resource can be of two types:

       * Regional: `projects/my-gcp-project/locations/us-central1/instances/my-regional-fs` (regional instance)
       * Zonal: `projects/my-awesome-project/locations/us-central1-a/instances/my-filestore-instance` (zonal instance)
     * `INSTANCE_NAME`: The name of the Filestore instance.

**Note:** For a zonal resource, --resource must be in the same region as that of the --location. A zonal location such as region `us-central1` zone `a` can be indicated by `us-central1-a`.



## Change the backup plan applied to a Filestore instance

You can change the backup plan applied to a Filestore instance to another backup plan. The other backup plan must meet these criteria:

  * Use the same backup vault
  * Be in the same region as the Filestore instance



Use the following instructions to change the backup plan associated with a Filestore instance.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the backup that will get a different plan. Either from the backup details page for the backup, or from the more_vert menu, select **Change backup plan**. The **Select a backup plan** window lists only the backup plans that are valid for this instance.

  3. Select a backup plan and click **Apply**.




###  gcloud 

  * Create a backup plan association:
        
        gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME \
        --location=LOCATION \
        --backup-plan=BACKUP_PLAN \
        --resource=projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME \
        --resource-type='file.googleapis.com/Instance'
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
    * `LOCATION`: the location of the backup plan association.
    * `BACKUP_PLAN`: the name of the backup plan.
    * `PROJECT_ID`: the project ID of the Filestore instance.
    * `ZONE`: the zone of the Filestore instance.
    * `INSTANCE_NAME`: the name of the Filestore instance.
  * Delete a backup plan association:
        
        gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME \
        --location=LOCATION
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
    * `LOCATION`: the location of the backup plan association.
  * Describe a backup plan association:
        
        gcloud backup-dr backup-plan-associations describe BACKUP_PLAN_ASSOCIATION_NAME \
        --location=LOCATION
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
    * `LOCATION`: the location of the backup plan association.
  * List backup plan associations:
        
        gcloud backup-dr backup-plan-associations list --location=LOCATION
        

Replace the following:

    * `LOCATION`: the location to list backup plan associations for.
  * Trigger a backup for a backup plan association:
        
        gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
        --location=LOCATION \
        --backup-rule-id=RULE_ID
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
    * `LOCATION`: the location of the backup plan association.
    * `RULE_ID`: the ID of the backup rule to use.



## List scheduled backups

Use the following instructions to list the backed up Filestore instances.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances that have backup plans applied and their backups stored in a backup vault within a project.




###  gcloud 

  1. List scheduled backups.
         
         gcloud backup-dr backup-plan-associations list \
           --location=LOCATION \
           --project=PROJECT_ID
         

Replace the following:

     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the scheduled backups.



## Create an on-demand backup

You can initiate an on-demand backup for a Filestore instance with a backup plan by triggering the backup rule of your choice to run immediately. On-demand backups typically capture only the data changed since the last backup (incremental).

When creating an on-demand backup, you can choose a rule from the backup plan associated with the Filestore instance. This rule determines when the on-demand backup gets deleted. You can check the backup job status from the **Jobs** page. For more information, see [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

**Note:** You can only run one backup job at a time. If an on-demand or scheduled backup job is already in progress, then attempting to start another on-demand backup job, the new job fails with the `Unable to queue the operation` error.

Use the following instructions to create an on-demand backup.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the Filestore instance that you want to back up. Either across from the instance on the right from the more_vert menu, or from the details page for the instance, select **Create on-demand backup**.

  3. In the **Create an on-demand backup** pane, choose when to delete this backup:

     * **Based on custom retention period** : By default, the limit is set as the backup vault's minimum enforced retention period plus 30 days. To set a different limit, select or enter the number of days.
     * **Based on an existing backup rule** : Select a rule from your backup plan in the drop-down list.
  4. Click **Create** to start the on-demand backup job.

  5. To view the status of the on-demand backup job, click **Notifications**.


**Note:** The on-demand backup is stored in the backup vault configured in the associated backup plan.

###  gcloud 

  * Create an on-demand backup that uses a backup rule.
        
        gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
        --project=PROJECT_ID \
        --location=REGION \
        --backup-rule-id=RULE_ID \
        --labels=LABELS
        




Replace the following:

  * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association. To get the list of the backup plans associated with the Filestore disk, run `gcloud backup-dr backup-plan-associations list --location=LOCATION --project=PROJECT_ID`.

  * `PROJECT_ID`: the name of the project.

  * `REGION`: the location of the scheduled backups.

  * `RULE_ID`: the backup rule name that you want to associate to run on-demand backups.

  * `LABELS`: optional labels for the backup as comma-separated key-value pairs such as `webserver=backend,media=images`.

  * Create an on-demand backup that uses custom retention.
        
        gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
          --project=PROJECT_ID \
          --location=REGION \
          --custom-retention-days=CUSTOM_RETENTION \
          --labels=LABELS
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association. Run the command `gcloud backup-dr backup-plan-associations list --location=LOCATION --project=PROJECT_ID` to get the list of the backup plans associated with the Filestore disk.

    * `PROJECT_ID`: the name of the project.

    * `REGION`: the location of the scheduled backups.

    * `CUSTOM_RETENTION`: The custom retention period in days for this on-demand backup. This value must be equal to or greater than the backup vault retention time and less than or equal to the max-custom-on-demand-retention-days value that is configured in the backup plan (or the vault retention time + 30 days if max-custom-on-demand-retention-days is not configured).

    * `LABELS`: optional labels for the backup as comma-separated key-value pairs such as `webserver=backend,media=images`.




## Unprotect a Filestore instance

You can unprotect a Filestore instance by removing the backup plan applied to the instance. Removing a backup plan from a Filestore instance doesn't delete the backup plan or any backups created while the instance was in use. You can still access and manage these existing backups.

Use the following instructions to unprotect a Filestore instance.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click the name of the instance that you want to remove a backup plan.

  3. Select **Remove backup plan**.




###  gcloud 

  1. Unprotect a Filestore instance.
         
         gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME \
           --project=PROJECT_ID \
           --location=LOCATION
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup you want to delete.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the scheduled backup.



## What's next

  * [Restore a Filestore instance from a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/filestore/filestore-instance-restore)
  * [Manage data sources in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage)
  * [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
