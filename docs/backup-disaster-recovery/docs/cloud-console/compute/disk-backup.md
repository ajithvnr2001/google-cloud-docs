---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-backup/
title: Back up disks to a backup vault \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:07.261124+00:00
---

# Back up disks to a backup vault  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/disk-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up disks to a backup vault Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to back up disks to a backup vault. Sending backups to a backup vault provides immutability and enforced retention. With a backup vault, you can store backups in a region or in a multi-region.

In the Google Cloud console, you can back up disks to a backup vault by applying backup plans. You can back up in two ways:

  * Scheduled backups: You can automatically back up disks at specific intervals, such as daily, weekly, monthly, or yearly.
  * On-demand backups: You can create on-demand backups whenever needed. On-demand backups are useful for creating backups before making significant changes to your instances or for _ad hoc_ data protection.



Both methods allow you to store your backups securely in a backup vault, providing a reliable way to recover your disks in case of data loss or other unexpected events.

## Before you begin

  1. Enable the Backup and DR API where the disks are located.
  2. [Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)
  3. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create)
  4. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create)
  5. Assign IAM roles and permission to the backup user
  6. Grant backup vault access in the Compute Engine project
  7. Set up Observability Analytics on your bucket to monitor Backup and DR backup jobs.



## Limitations

Backup and DR doesn't support:

  * Backing up disks to a backup vault for disks with customer-supplied encryption keys (CSEK). Customer-managed encryption keys (CMEK) are supported. For more information about required permissions, see Grant backup vault access.
  * Backing up disks with access mode READ_WRITE_MANY is not supported.
  * More than one backup per hour.



## IAM roles and permissions for the backup user

To get the permissions that you need to configure scheduled backups or run on-demand backups, ask your administrator to grant you the following IAM roles on your backup vault project: 

  * [Backup and DR Backup User ](https://docs.cloud.google.com/iam/docs/roles-permissions/backupdr#backupdr.backupUser) (`roles/backupdr.backupUser`)
  * [Viewer ](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to configure scheduled backups or run on-demand backups. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to configure scheduled backups or run on-demand backups:

  * `backupdr.backupPlans.list`
  * `backupdr.backupPlanAssociations.createForComputeDisk`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.get`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeDisk`
  * `backupdr.backupPlanAssociations.deleteForComputeDisk`
  * `backupdr.backupPlans.useForComputeDisk`
  * `backupdr.locations.list`
  * `backupdr.operations.get`
  * `cloudasset.assets.searchAllResources`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Grant backup vault access in the project where the disks are

To back up a disk in a project different from where the backup vault is created, you must grant the Backup and DR Disk Operator (`roles/backupdr.diskOperator`) IAM role to the backup vault service agent within the project where the disks are.

To back up a disk in the project where the backup vault is created, no roles are required to be granted.

If the disk is protected by customer-managed encryption keys (CMEK), you must grant the `Cloud KMS CryptoKey Encrypter/Decrypter` role (`roles/cloudkms.cryptoKeyEncrypterDecrypter`) to the backup vault service agent (`service-BACKUP_VAULT_PROJECT_NUMBER@gcp-sa-backupdr.iam.gserviceaccount.com`) on the KMS key used to encrypt the disk. This permission is required for Backup and DR to access the key during backup and restore operations.

For information about granting roles to the backup vault service agent within the project you intend to back up, see [Grant a role to the service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service_agent).

## Configure a scheduled backup

Use the following instructions to configure a scheduled backup for disks.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backups**.

  3. For **Resource type** , select **Disks**.

  4. From the **Projects** list, click **Browse** and select a project where the disks are located.

  5. From the **Region** list, select the region where your disks are located.

  6. From the **Resources** list, click **Browse**.

  7. Choose the disks that you want to back up and click **Done**.

  8. Click **Continue**.

  9. From the **Backup plan** list, click **Select**.

  10. Choose a backup plan that you want to protect the disks with.

  11. Click **Done**.

**Tip:** If the selected disk is CMEK-encrypted, the list of available backup plans is automatically filtered to show only CMEK-compatible backup plans.
  12. Review the backup details and click **Schedule**. At this point you have associated a backup plan with the disks. The backup plan schedules the chosen disks for backup per the frequency set in the backup policy, but they are not backed up yet. If the current time is within the window set in the backup plan, then the first backup job will start within a few minutes. If the current time is outside the plan window, then create an on-demand backup.




###  gcloud 

  1. Get the instance ID.
         
         gcloud compute instances describe DISK_NAME --zone=DISK_ZONE --format="value(id)"
         

Replace the following:

     * `DISK_NAME`: the name of the disk.
     * `DISK_ZONE`: the location where the disk is located.
  2. Configure a scheduled backup.
         
         gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME \
           --location=DISK_REGION \
           --resource=projects/DISK_PROJECT_ID/zones/DISK_ZONE/disks/DISK_ID \
           --resource-type=compute.googleapis.com/Disk \
           --backup-plan=projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUP_PLAN
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
     * `DISK_REGION`: the region where the disks are located.
     * `DISK_PROJECT_ID`: the name of the project where the disks are located.
     * `DISK_ZONE`: the zone where the disks are located.
     * `DISK_ID`: the disk ID.
     * `PROJECT_ID`: the name of the project where backup plans exist.
     * `LOCATION`: the region where your backup plans exist.
     * `BACKUP_PLAN`: the name of the backup plan that you want to associate with the disk.



### Terraform

You can use a [Terraform resource to configure a scheduled backup](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/backup_dr_backup_plan_association).
    
    
    # Before creating a backup plan association, you need to create backup plan (google_backup_dr_backup_plan)
    # and compute disk (google_compute_disk or google_compute_region_disk).
    resource "google_backup_dr_backup_plan_association" "disk_association" {
      provider                   = google-beta
      location                   = "us-central1"
      backup_plan_association_id = "my-disk-bpa"
      resource                   = google_compute_disk.default.id
      resource_type              = "compute.googleapis.com/Disk"
      backup_plan                = google_backup_dr_backup_plan.disk_default.name
    }
    

## Application consistency for Backup and DR disk backups

[Application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots) capture the state of application data at the time of backup with all application transactions completed and all pending writes flushed to the disk.

Use the following instructions to configure application-consistent backups for disks. This procedure can only be performed through the [gcloud CLI](https://docs.cloud.google.com/sdk/gcloud).

### Before you begin

  * In a Linux environment:

    1. Read [Application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots) before continuing and follow the steps in [Before you begin](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots#byb)

    2. A backup plan for application-consistent disk backups in a Linux environment requires pre- and post-scripts. [Create the necessary pre and post snapshot scripts for a Linux environment](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots#create-scripts).

  * In a Windows environment:

Read [Application consistent snapshots](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-persistent-disk-snapshot#byb) before continuing.




### Create a backup plan for application-consistent disk backups

Use the following instructions to create application-consistent backups for disks. This procedure can only be performed through the gcloud CLI.

###  gcloud 

  1. Create the backup plan.
         
         gcloud backup-dr backup-plans create BACKUP_PLAN_NAME \
         --disk-properties=guest-flush=true \
         --resource-type=compute.googleapis.com/Disk \
         --location=REGION \
         --project=PROJECT_ID \
         --backup-vault=BACKUPVAULT_NAME \
         --backup-rule=rule-id=RULE_NAME,recurrence=RECURRENCE,hourly-frequency=HOURS,time-zone=TIME_ZONE,backup-window-start=START_TIME,backup-window-end=END_TIME,retention-days=BACKUP_RETENTION --max-custom-on-demand-retention-days=MAX_ONDEMAND_RETENTION
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.
     * `REGION`: the Google Cloud region where you want to create the backup plan.
     * `PROJECT_ID`: the name of the project where the backup vault resides.
     * `BACKUPVAULT_NAME`: the name of the backup vault that you want to use for backup storage.
     * `RULE_NAME`: the name of the backup rule.
     * `RECURRENCE`: the frequency at which backups to be created. It can be hourly, daily, weekly, monthly, or yearly.
     * `HOURS`: the frequency of the hourly backups. Specify this value only if you set the recurrence to hourly. The minimum hourly is always set to six hours.
     * `TIME_ZONE`: the time zone for the backup plan, such as UTC. Use the [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) format to include the timezone for the backup plan.
     * `START_TIME`: the start time is the hour of the day in a 24 hour format. The start time must be before the end time and is inclusive for the backup window.
     * `END_TIME`: the end time is the hour of the day in a 24 hour format. The end time must be after the start time and is exclusive for the backup window.
     * `BACKUP_RETENTION`: the retention period of the backup. Note that the backup retention period must be equal to or greater than the backup vault enforced minimum retention period.
     * `MAX_ONDEMAND_RETENTION`: The maximum allowed custom retention period (in days) for on-demand backups created using this backup plan.
**Note:** All retention periods are capped at 36,135 days (99 years).**Note:** When `guest-flush` is set to true, all backups created with this plan will have `guest-flush` enabled.



**Note:** Application consistency for snapshots isn't supported for Google Cloud Hyperdisk.

### Update an existing backup plan for application-consistent disk backups

Use the following instructions to update a backup plan to produce application-consistent disk backups.

###  gcloud 

  1. Update the backup plan.
         
         gcloud backup-dr backup-plans update BACKUP_PLAN_NAME \
         --disk-properties=guest-flush=true \
         --project=PROJECT_ID\
         --location=REGION \
         --description=DESCRIPTION \
         --backup-rule=BACKUP_RULE \
         --add-backup-rule=ADD_BACKUP_RULE \
         --remove-backup-rule=REMOVE_BACKUP_RULE
         --max-custom-on-demand-retention-days=MAX_ONDEMAND_RETENTION
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.
     * `PROJECT_ID`: the name of the project where the backup vault resides.
     * `REGION`: the location where you want to create the backup plan.
     * `DESCRIPTION`: the updated description of the backup plan.
     * `BACKUP_RULE`: Full definition of an existing backup rule with updated values.
     * `ADD_BACKUP_RULE`: Parameters of the backup rule to be added to the backup plan. This flag can be repeated to add more backup rules.
     * `REMOVE_BACKUP_RULE`: The existing backup rule to be removed from the backup plan.
     * `MAX_ONDEMAND_RETENTION`: The maximum allowed custom retention period (in days) for on-demand backups created using this backup plan.
**Note:** All retention periods are capped at 36,135 days (99 years).



**Note:** Application consistency for snapshots isn't supported for Google Cloud Hyperdisk.

## Change the backup plan associated with disks

You can change the backup plan associated with a disk to another backup plan. The other backup plan must:

  * Use the same backup vault
  * Be in the same region as the disk Compute Engine instance 



Use the following instructions to change the backup plan associated with disks.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the data resource to get a different plan. Either from the backup details page for the backup, or from the more_vert menu on the far right of a Compute Engine instance, select **Change backup plan**.

  3. The **Select a backup plan** window lists only the backup plans that are valid for this instance. Select a backup plan and click **Apply**.

**Tip:** If the disk is CMEK-encrypted, the list of available backup plans is automatically filtered to show only CMEK-compatible backup plans.



###  gcloud 

  * Change the assigned backup plan.
        
        gcloud backup-dr backup-plan-associations update BACKUP_PLAN_ASSOCIATION_NAME \
          --resource-type=compute.googleapis.com/Disk \
          --workload-project=DISK_PROJECT_ID \
          --location=DISK_REGION \
          --backup-plan=BACKUP-PLAN \
          --project=PROJECT_ID
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association resource.
    * `DISK_PROJECT_ID`: the project-id of the disk.
    * `DISK_REGION`: the location of the disk.
    * `BACKUP_PLAN`: the name of the backup plan that you are switching to.
    * `PROJECT_ID`: the project-id of the selected backup plan.



## List scheduled and on-demand backups

Use the following instructions to list disks that are backed up or are scheduled to be backed up.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances and disks that have backup plans applied and their backups stored in a backup vault within a project.

  2. Click a disk to view all the backups (both scheduled and on-demand backups) available for that disk.




###  gcloud 

  1. List scheduled and on-demand backups.
         
         gcloud backup-dr backup-plan-associations list \
           --location=LOCATION \
           --project=PROJECT_ID
         

Replace the following:

     * `LOCATION`: the location of the scheduled backups.
     * `PROJECT_ID`: the name of the project.



## Create an on-demand backup

You can initiate an on-demand backup for disks with a backup plan by triggering the backup rule of your choice to run immediately. On-demand backups are incremental and capture only the changed data since the last backup.

When creating an on-demand backup, you can choose a rule from the backup plan associated with the disk. This rule determines when the on-demand backup gets deleted. You can check the backup job status from the **Jobs** page. For more information, see [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

**Note:** You can only run one backup job at a time. If an on-demand or scheduled backup job is already in progress, then attempting to start another on-demand backup job, the new job fails with the `Unable to queue the operation` error.

Use the following instructions to create an on-demand backup.

###  Console 

  1. Go to **Vaulted backups**.
  2. Select the disk to back up.
  3. Click **Create On-Demand Backup**.
  4. Choose when to delete this backup. You have these options:

     * **Based on custom retention period** By default, the limit is set as the backup vault's minimum enforced retention period plus 30 days. To set a different limit, add a maximum custom on-demand retention period to your backup plan.
     * **Based on an existing backup rule**. Select a rule from the **Delete backups after** drop-down.
  5. Click **Create** to start the on-demand backup creation process.

  6. To view the status of the on-demand backup job, click **Notifications**.


**Note:** The on-demand backup is stored in the backup vault that is configured with the associated backup plan.

###  gcloud 

  * Create an on-demand backup that uses a backup rule.
        
        gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
          --project=PROJECT_ID \
          --location=REGION \
          --backup-rule-id=RULE_ID
          --labels=LABELS
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association. Run the command `gcloud backup-dr backup-plan-associations list --location=LOCATION --project=PROJECT_ID` to get the list of the backup plans associated with the Compute Engine disk.
    * `PROJECT_ID`: the name of the project.
    * `REGION`: the location of the scheduled backups.
    * `RULE_ID`: the backup rule name that you want to associate to run on-demand backups.
    * `LABELS`: optional labels for the backup as comma-separated key-value pairs such as `webserver=backend,media=images`.
  * Create an on-demand backup that uses custom retention.
        
        gcloud backup-dr backup-plan-associations trigger-backup BACKUP_PLAN_ASSOCIATION_NAME \
          --project=PROJECT_ID \
          --location=REGION \
          --custom-retention-days=CUSTOM_RETENTION
          --labels=LABELS
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association. Run the command `gcloud backup-dr backup-plan-associations list --location=LOCATION --project=PROJECT_ID` to get the list of the backup plans associated with the Compute Engine disk.
    * `PROJECT_ID`: the name of the project.
    * `REGION`: the location of the scheduled backups.
    * `CUSTOM_RETENTION`: The custom retention period in days for this on-demand backup. This value must be equal to or greater than the backup vault retention time and less than or equal to the max-custom-on-demand-retention-days value that is configured in the backup plan (or the vault retention time + 30 days if max-custom-on-demand-retention-days is not configured).
    * `LABELS`: optional labels for the backup as comma-separated key-value pairs such as `webserver=backend,media=images`.



## Unprotect disks

You can unprotect disks by removing the backup plan applied to the disks. Removing a backup plan from disks doesn't delete the backup plan or any backups created while the instance was in use. You can still access and manage these existing backups.

Use the following instructions to unprotect a disk:

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click the name of the disk to remove a backup plan from.

  3. Select **Remove backup plan**.




###  gcloud 

  1. Unprotect disks.
         
         gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME\
           --project=PROJECT_ID \
           --location=REGION
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association to delete.
     * `PROJECT_ID`: the name of the project.
     * `REGION`: the location of the scheduled backup.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
