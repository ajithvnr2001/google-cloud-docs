---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/disk-backup-vault/
title: Protect and recover disks to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:40.503963+00:00
---

# Protect and recover disks to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/quickstarts/disk-backup-vault/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Protect and recover disks to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page details how to use Backup and DR to back up the disks of a Compute Engine instance. It is an end-to-end overview about how to back up and restore your disks and monitor your backups.

## Before you begin

Before you begin, be sure that you have these prerequisites:

  1. This quickstart assumes that you have Backup and DR API enabled in your project.
  2. You will need a backup vault. If you don't have a backup vault, then [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create).
  3. You will need a backup plan configured to protect disks. To create a backup plan for disks, follow these steps:



###  Console 

  1. In the Google Cloud console, go to the **Backup plans** page. [Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. Click **Create Backup plan**.

  3. For **Resource type** , select **Disks**.

  4. In the **Backup plan name** field, enter a name for the backup plan. You can't change the name of a plan after the backup plan is created.

  5. In the **Backup plan description** field, enter an optional description for the backup plan.

  6. From the **Regions** list, select a backup plan region. The backup plan is created in this region. You can protect resources in the same region as the backup plan.

  7. From the **Backup vault** list, select a backup vault to store the backups.

  8. Click **Add rule**.

  9. In the **Add a backup rule** pane, enter your backup rule information and click **Save**.

     * **Name your backup rule** : Enter a name for the backup rule.
     * **Choose when to create backups** : Specify the recurrence and frequency of the backup.
     * **Window** : Select the **Timezone** , **Start time** , and **Endtime** for the backup job.
     * **Choose how long backups are kept before they are deleted** : Enter the duration in days that the backups should be retained before they are deleted. Note that this value must be equal to or greater than the [backup vault minimum enforced retention period](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#enforced-retention).
**Note:** You can add more than one backup rule to take weekly, monthly, or yearly backups of your disks depending on your need.
  10. Optionally set a **maximum custom on-demand retention**.

Your custom on-demand backups can be kept for up to the maximum custom on-demand retention. When you create an on-demand backup, set your retention or you can use an existing backup rule. If unspecified, the vault's minimum enforced retention period plus 30 days is used as the maximum limit for custom retention period.

Enter a value in days in **Maximum retention**. This value must be greater than or equal to the vault's minimum enforced retention period.

**Note:** All retention periods are capped at 36,135 days (99 years).
  11. Click **Create**.




###  gcloud 

  1. Create a backup plan
         
         gcloud backup-dr backup-plans create BACKUP_PLAN_NAME \
             --location=REGION \
             --backup-vault=BACKUPVAULT_NAME \
             --resource-type=compute.googleapis.com/Disk \
             --description="Daily application-consistent backups for production disks" \
             --labels=environment=prod,team=ops \
             --disk-properties=guest-flush=true \
             --max-custom-on-demand-retention-days=180 \
             --backup-rule='rule-id=daily-rule,retention-days=30,recurrence=DAILY,time-zone=UTC,backup-window-start=0,backup-window-end=4'
         




Replace the following:

  * `BACKUP_PLAN_NAME`: the name of the backup plan.
  * `REGION`: the region where you want to create the backup plan.
  * `BACKUPVAULT_NAME`: the name of the backup vault where you want to store the backups.



## Configure backup for disks

To back up disks, follow these steps:

###  Console 

  1. In your project, in Backup and DR, click **Vaulted backups**.
  2. Click **Schedule backups**.
  3. In the **Choose resources** page that appears, complete the following: 
     * **Resource type** : Select **Disks**.
     * **Project** : The current project is selected, or you can browse to the project that contains the disks that you want to back up.
     * **Region** : Select the region where your resources are located.
     * **Resources** : Click **Browse** to open a pane where you can select the disks to back up into this backup vault.
  4. Click **Continue**.
  5. In the **Select a backup plan** page select a backup plan and then click **Done**.

**Tip:** If the selected disk is CMEK-encrypted, the list of available backup plans is automatically filtered to show only CMEK-compatible backup plans.
  6. Click **Continue**.

  7. Review your selections and click **Schedule**. At this point you have associated a backup plan with the disks. The backup plan schedules the chosen disks to get backed up per the frequency set in the backup policy, but they are not backed up up yet.

  8. From the **Resources with vaulted backups** , select the resource that you just assigned the backup plan to. Click **Create an on-demand backup**. An on-demand backup is a backup job that you can manually trigger at any time.

  9. Review the details and click **Create**.




###  gcloud 

  1. Configure backups
         
         gcloud backup-dr backup-plan-associations create my-disk-assoc \
             --project=PROJECT_ID \
             --location= REGION \
             --resource=projects/PROJECT_ID/zones/ZONE/disks/DISK_ID \
             --resource-type=compute.googleapis.com/Disk \
             --backup-plan=projects/PROJECT_ID/locations/us-central1/backupPlans/my-disk-plan
         




Replace the following:

  * `PROJECT_ID`: the project ID of the project where your backup plan and disks are located.
  * `ZONE`: the zone where your disk is located.
  * `DISK_ID`: the ID of the disk that you want to back up.


  1. List backups
         
         gcloud backup-dr backups list \
             --project=PROJECT_ID \
             --location=us-central1 \
             --backup-vault=BACKUPVAULT_NAME \
             --data-source=DATA_SOURCE_ID
         




Replace the following:

  * `PROJECT_ID`: the project ID of the project where your backup plan and disks are located.
  * `BACKUPVAULT_NAME`: the name of the backup vault.
  * `DATA_SOURCE_ID`: the ID of the data source.



**Note:** If you encounter a `Failed to backup PersistentVolumeClaim` error, see [Error 100010104: Failed to backup PersistentVolumeClaim - Org policy constraint violation while creating snapshot](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup-vault-issues#org-policy-constraint-violation-during-snapshot-creation)

## Restore disks

You can restore the source Compute Engine instance using a **Restore** operation and restore instance to an alternate location using the **Mount** operation.

###  Console 

  1. On the **Vaulted backups** page, select the disk to restore.
  2. In the **Backup details** list, select the disk backup, and then select **Restore** under the more_vert icon.
  3. The **Choose the backup to restore** section is prefilled with the information about the selected disk.
  4. The **Choose the restore destination** is prefilled with the current project. Don't change it for this exercise.
  5. If you need any permissions, the next section indicates which ones with a link to get them.
  6. Click **Restore**. The disk is restored to the selected project with the same name appended by "-restore-" and a date and timestamp. You can see it in **Compute Engine** > **Storage** > **Disks**.



###  gcloud 

  1. Restore disks
         
         gcloud backup-dr backups restore disk BACKUP_ID \
             --project=PROJECT_ID \
             --location=us-central1 \
             --backup-vault=BACKUPVAULT_NAME \
             --data-source=DATA_SOURCE_ID \
             --name=restored-my-disk \
             --target-project=PROJECT_ID \
             --target-zone=ZONE \
             --type=pd-balanced \
             --size=500 \
             --labels=restored-from=BACKUP_ID \
             --clear-encryption-key
         




Replace the following:

  * `BACKUP_ID`: the ID of the backup.
  * `PROJECT_ID`: the project ID of the project where your backup plan and disks are located.
  * `DATA_SOURCE_ID`: the ID of the data source.
  * `ZONE`: the target zone where you want to restore your disk.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
