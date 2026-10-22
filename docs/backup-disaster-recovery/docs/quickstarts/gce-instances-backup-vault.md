---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-vault/
title: Back up and recover a Compute Engine instance to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:35:46.948328+00:00
---

# Back up and recover a Compute Engine instance to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up and recover a Compute Engine instance to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

Learn how to back up and restore your Compute Engine instance to a backup vault.

In this quickstart, you perform the following tasks:

  * Create a backup vault.
  * Create a backup plan.
  * Back up a Compute Engine instance into a backup vault.
  * Restore a Compute Engine instance from the backup.



## Before you begin

  1. Enable the Backup and DR API in your Google Cloud project.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  2. If you don't have a VM, [Create and start a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance) in a location where the backup vault is [supported](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#regions). For the purpose of this quickstart, create a Compute Engine instance in the `us-central1` region.

  3. Have the following IAM roles assigned to you in your project:

     * BackupDR Admin (`roles/backupdr.admin`)
     * Backup and DR User V2 (`backupdr.backupPlanAssociations.createForComputeInstance`)
     * Cloud Asset Viewer (`cloudasset.assets.searchAllResources`)
     * Compute Instance Admin (v1) (`roles/compute.instanceAdmin.v1`)
     * Compute Viewer (`roles/compute.viewer`)
     * Logs Viewer (`roles/logging.logEntries.list`)
     * OS Config Admin (`osconfig.osPolicyAssignments.create.`)
     * Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)
     * Service Usage Admin (`serviceusage.services.enable`)
     * Service Account User (`iam.serviceAccountUser`)
  4. The backup vault service agent must be granted the required roles in the restore project to create a new instance using the backup.

     * Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`)
     * Compute Network User (`roles/compute.networkUser`) if you are using a shared VPC



## Create a backup vault

A backup vault is a container to store backups in, similar to self-managed storage. Backup vaults provide protection for backups by storing them in secure, isolated, and specialized storage. For more information about backup vault, see [Overview of backup vaults](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault).

your VMs. For more information, see [Protect and recover a Compute Engine instance using appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/gce-instances-backup-recovery).

Use the following instructions to create a backup vault.

###  Console 

  1. In the Google Cloud console **Backup and DR** section, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. Click **Create backup vault**.

  3. On the **Create a backup vault** page, enter your backup vault information.

  4. In the **Name your backup vault** field, enter a name for the backup vault and an optional description.

  5. At **Choose where to store your data** , configure the following settings:

     * **Region** : for the backup vault—for example, `us-central1`.
     * **Multi-region** : for the backup vault}—for example, `Americas`.
  6. In the **Prevent backup deletion** field, enter the [minimum enforced retention](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#enforced-retention) period defining how long backups are protected against deletion. The minimum is 1 day and the maximum is 99 years.

If you want to lock the value of the minimum enforced retention period, select **Lock the enforced retention** and then click the calendar_month icon and select the date from the calendar.

     * **Prevent deletion for duration specified in backup rule** : You can set the vault to inherit the **Delete backups after** value set in a backup plan. Backups can't be manually deleted, they will be deleted according to the value in their associated backup plan.

     * **Lock the enforced retention** : If you want to lock the value of the minimum enforced retention period, check this and then click the calendar_month icon and select the date from the calendar.

  7. If you want to use your own encryption key, then under **Encryption** , select the **Customer-managed encryption key (CMEK)** option, and then select your key from the drop-down list. Only keys from the same location as the backup vault are displayed. You can only configure CMEK when you create a backup vault. For more details on using CMEK, see [Encryption](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#encryption).

For required permissions, see [CMEK permissions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/cmek#permissions_required_to_use_cmek).

**Note:** Access to CMEK for Persistent Disk and for Compute Engine is available by invitation only. If you'd like to request access to CMEK for Persistent Disk or for your Google Cloud project, contact your sales representative.
  8. In the **Define access to your backup vault** section, select an option to define [access restrictions](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#access-restrictions) for the backup vault. If you don't select an option, the backup vault is created with the **Restrict access to current organization** restriction.

  9. Click **Create**.




###  gcloud 

  1. Create a backup vault.
         
         gcloud backup-dr backup-vaults create BACKUPVAULT_NAME \
             --project=PROJECT_ID \
             --location=LOCATION \
             --backup-min-enforced-retention=RETENTION_PERIOD_IN_DAYS \
             --backup-retention-inheritance=RETENTION_PERIOD_INHERITANCE
         

Replace the following:

     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `PROJECT_ID`: the name of the project where you want to create the backup vault.
     * `LOCATION`: the location where you want to create a backup vault. For example, `us-central1`.
     * `RETENTION_PERIOD_IN_DAYS`: the period of time that each backup in the backup vault cannot be deleted. The minimum is 1 day and the maximum is 99 years. For example, `1`.
     * `RETENTION_PERIOD_INHERITANCE`: the inheritance mode for enforced retention end time. For example, `match-backup-expire-time` to inherit the retention from the backup rule.



## Create a backup plan

A backup plan lets you define advanced backup strategies to back up your Compute Engine instances. In a backup plan, you can define when and how to back up a Compute Engine instance. You must create the backup plan in the same region that the workload is running in and the backup vault must exist in a location that is [compatible with the workload location](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility). Also, a backup plan can only back up Compute Engine instances that are in the same region. For more information, see [Backup plans in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan).

Use the following instructions to create a backup plan. In this procedure, you'll create a backup plan for hourly backup of the Compute Engine instances and use the backup vault that you have created in the `us-central1` region.

###  Console 

  1. In the Google Cloud console **Backup and DR** section, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. Click **Create Backup plan**.

  3. For **Resource type** , select **Compute Engine**.

  4. In the **Backup plan name** field, enter a name for the backup plan. You can't change the name of a plan after the backup plan is created.

  5. In the **Backup plan description** field, enter an optional description for the backup plan.

  6. From the **Regions** list, select a backup plan region. The backup plan is created in this region. You can protect resources in the same region as the backup plan.

  7. From the **Backup vault** list, select a backup vault to store the backups.

  8. In the **Add backup rules** section, the default backup rule is already in place.

     1. If you want to use the default rule and no other backup rules, you can click **Create**.
     2. If you want to add a different backup rule for this quickstart, click **Add rule**.

In the **Add a backup rule** pane, enter your backup rule information and click **Save**.

     * **Name your backup rule** : Enter a name for the backup rule.
     * **Choose when to create backups** : Specify the recurrence and frequency of the backup.
     * **Window** : Select the **Timezone** , **Start time** , and **Endtime** for the backup job.
     * **Choose how long backups are kept before they are deleted** : Enter the duration in days that the backups should be retained before they are deleted. Note that this value must be equal to or greater than the [backup vault minimum enforced retention period](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#enforced-retention).
  9. Optionally set a **maximum custom on-demand retention**.

Your custom on-demand backups can be kept for up to the maximum custom on-demand retention. When you create an on-demand backup, set your retention or you can use an existing backup rule. If unspecified, the vault's minimum enforced retention period plus 30 days is used as the maximum limit for custom retention period.

Enter a value in days in **Maximum retention**. This value must be greater than or equal to the vault's minimum enforced retention period.

**Note:** All retention periods are capped at 36,135 days (99 years).
  10. Click **Create**.




###  gcloud 

  1. Create a backup plan.
         
         gcloud backup-dr backup-plans create BACKUP_PLAN_NAME \
             --location=REGION \
             --resource-type=compute.googleapis.com/Instance \
             --project=PROJECT_ID \
             --backup-vault=BACKUPVAULT_NAME \
             --backup-rule=rule-id=RULE_NAME,recurrence=RECURRENCE,hourly-frequency=HOURS,time-zone=TIME_ZONE,backup-window-start=START_TIME,backup-window-end=END_TIME,retention-days=BACKUP_RETENTION
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.
     * `REGION`: the region where you want to create the backup plan. For example, `us-central1`.
     * `PROJECT_ID`: the name of the project where the backup vault resides.
     * `BACKUPVAULT_NAME`: the name of the backup vault that you want to use for backup storage.
     * `RULE_NAME`: the name of the backup rule.
     * `RECURRENCE`: the frequency at which backups to be created. For example, `HOURLY`.
     * `HOURS`: the frequency of the hourly backups. For example, `6`.
     * `TIME_ZONE`: the time zone for the backup plan. For example, `UTC`.
     * `START_TIME`: the start time of the backup window in 24-hour format. For example, `0`.
     * `END_TIME`: the end time of the backup window in 24-hour format. For example, `4`.
     * `BACKUP_RETENTION`: the retention period of the backup in days. For example, `30`.



## Back up a Compute Engine instance into a backup vault

In the Google Cloud console, you can back up Compute Engine instances to a backup vault by applying backup plans. You can back up in either of these two ways: **Scheduled backups** and **On-demand backups**.

### Configure a scheduled backup

Use the following instructions to configure a scheduled backup.

###  Console 

  1. In the Google Cloud console **Backup and DR** section, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backup**.

  3. Select the **Resource type** Compute Engine.

  4. Leave the **Project** unchanged.

  5. From the **Region** list, select the instance region `us-central1`.

  6. From the **Resources** list, click **Browse**.

  7. Choose the Compute Engine instance that you want to back up and click **Done**.

  8. Click **Continue**.

  9. From the **Backup plan** list, click **Select** , and select the backup plan that you just created.

  10. Click **Continue**.

  11. Review the backup details and click **Schedule**.




###  gcloud 

  1. Get the instance ID:
         
         gcloud compute instances describe VM_NAME \
             --zone=VM_ZONE \
             --format="value(id)"
         

Replace the following:

     * `VM_NAME`: the name of the VM instance.
     * `VM_ZONE`: the zone where the VM is located.
  2. Configure a scheduled backup:
         
         gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME \
             --location=VM_REGION \
             --resource=projects/VM_PROJECT_ID/zones/VM_ZONE/instances/VM_ID \
             --backup-plan=projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUP_PLAN
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
     * `VM_REGION`: the region where the VM instance is located.
     * `VM_PROJECT_ID`: the project ID where the VM instance is located.
     * `VM_ZONE`: the zone where the VM instance is located.
     * `VM_ID`: the VM instance ID retrieved in the previous step.
     * `PROJECT_ID`: the project ID where the backup plan exists.
     * `LOCATION`: the region where the backup plan exists.
     * `BACKUP_PLAN`: the name of the backup plan.



The first backup made according to this backup plan will be triggered when the current time is within the backup window. If the backup job is not running yet, then run an on-demand backup now.

## Take on-demand backup

Use the following instructions to create an on-demand backup.

###  Console 

  1. In the Google Cloud console **Backup and DR** section, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. In the **Resources with vaulted backups** list, in the row that contains the backed up instance, click the more_vert icon. Click **Create on-demand backup**.

  3. At **Choose when to delete this backup** select **Based on an existing backup rule** and click **Create**.

  4. To view the backup operation status, you can:

     * Check the notification bell at the top of the Google Cloud console.
     * Go to the **Jobs** page.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)




###  gcloud 

  1. Create an on-demand backup:
         
         gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
             --project=PROJECT_ID \
             --location=REGION \
             --backup-rule-id=RULE_ID
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
     * `PROJECT_ID`: the project ID.
     * `REGION`: the region of the backup plan association.
     * `RULE_ID`: the backup rule name in the backup plan to determine retention.



## Restore a Compute Engine instance from a backup

You can restore a Compute Engine instance to the same project or to a different project. This quickstart guides you to restore the VM in the same project.

Use the following instructions to restore a Compute Engine instance from a backup in a backup vault.

###  Console 

  1. In the Google Cloud console **Backup and DR** section, go to the **Vaulted resources** page.

[Go to Vaulted resources](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. Click the instance that you just backed up.

  3. In the details page, from the actions menu of the backup, select the backup that you just made and click the more_vert icon, and then select **Restore**.


**Note:** If there has been enough time for the backup window in the backup plan to open, you may see multiple backups timestamped for when they were made.

  1. In the **Restore a backup** page, review the restore details and click **Browse** to select the backup.
  2. Click **Continue**.
  3. In the **Create a VM instance from a backup** page, leave the instance configuration to the default and click **Create**.

  4. In the Google Cloud console, go to the **Jobs** page to view the restore operation status.

[Go to Jobs](https://console.cloud.google.com/backupdr/jobs)




###  gcloud 

  1. Find the data source ID:
         
         gcloud backup-dr data-sources list \
             --project=PROJECT_ID \
             --location=REGION \
             --backup-vault=BACKUPVAULT_NAME \
             "--filter=dataSourceGcpResource.computeInstanceDatasourceProperties.name:(VM_NAME)" \
             "--format=get(name)"
         

Replace the following:

     * `PROJECT_ID`: the project ID of the backup vault.
     * `REGION`: the region of the backup vault.
     * `BACKUPVAULT_NAME`: the name of the backup vault.
     * `VM_NAME`: the name of the VM instance.
  2. List backups for the data source to find the `BACKUP_ID`:
         
         gcloud backup-dr backups list \
             --project=PROJECT_ID \
             --location=REGION \
             --backup-vault=BACKUPVAULT_NAME \
             --data-source=DATA_SOURCE
         

Replace `DATA_SOURCE` with the data source name retrieved in the previous step.

  3. Restore the VM:
         
         gcloud backup-dr backups restore compute BACKUP_ID \
             --project=PROJECT_ID \
             --location=REGION \
             --backup-vault=BACKUPVAULT_NAME \
             --data-source=DATA_SOURCE \
             --name=RESTORED_VM_NAME \
             --target-project=TARGET_PROJECT_ID \
             --target-zone=TARGET_ZONE
         

Replace the following:

     * `BACKUP_ID`: the ID of the backup to restore.
     * `RESTORED_VM_NAME`: the name for the restored VM.
     * `TARGET_PROJECT_ID`: the project where you want to restore the VM.
     * `TARGET_ZONE`: the zone where you want to restore the VM.



## Clean up

To avoid incurring charges to your Google Cloud account for the instances used on this page, follow these steps.

### Delete the restored VM

###  Console 

  1. In the Google Cloud console Compute Engine section, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the row containing the VM instance that you've created as part of the restore.

  3. Click **Delete** and click **Delete** to confirm.




###  gcloud 

  1. Delete the restored VM instance:
         
         gcloud compute instances delete RESTORED_VM_NAME --zone=TARGET_ZONE
         




### Remove the backup plan from the backed up Compute Engine instance

###  Console 

  1. In the Google Cloud console Backup and DR section, go to the **Vaulted backups** page.

[Go to Vaulted resources](https://console.cloud.google.com/backupdr/vaulted-resources)

  2. In the row that contains the backed up instance, click the more_vert icon. Click **Remove backup plan** and then confirm the removal.


**Note:** The backup automatically expires and gets deleted after the one day retention period.

###  gcloud 

  1. Delete the backup plan association:
         
         gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME \
             --project=PROJECT_ID \
             --location=REGION
         

**Note:** The backups stored in the vault will remain until they expire.



### Delete the backup plan (optional)

###  Console 

  1. In the Google Cloud console Compute Engine section, go to the **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. In the row that contains the backup plan, click the more_vert icon. Click **Delete** and then type **delete** to confirm the deletion.




###  gcloud 

  1. Delete the backup plan:
         
         gcloud backup-dr backup-plans delete BACKUP_PLAN_NAME \
             --project=PROJECT_ID \
             --location=REGION
         




### Delete the backup vault (optional)

###  Console 

  1. In the Google Cloud console Backup and DR section, go to the **Backup vaults** page.

[Go to Backup vaults](https://console.cloud.google.com/backupdr/backup-vaults/list)

  2. In the row that contains the backup vault, click the more_vert icon. Click **Delete** and then type **delete** to confirm the deletion.


**Note:** The backup vault incurs a cost only when the backup vault stores data. The existence of an empty backup plan doesn't incur any cost. You cannot delete the vault until the last of the backups has passed the minimum retention period and is eligible for deletion or has been automatically deleted.

###  gcloud 

  1. Delete the backup vault:
         
         gcloud backup-dr backup-vaults delete BACKUPVAULT_NAME \
             --project=PROJECT_ID \
             --location=REGION
         

**Note:** You cannot delete the vault until all backups inside it have expired.



### Delete the VM created for this quickstart (optional)

###  Console 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Select the row containing the VM instance that you've created in this quickstart.

  3. Click **Delete** and then click **Delete** to confirm.




###  gcloud 

  1. Delete the VM instance:
         
         gcloud compute instances delete VM_NAME --zone=VM_ZONE
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
