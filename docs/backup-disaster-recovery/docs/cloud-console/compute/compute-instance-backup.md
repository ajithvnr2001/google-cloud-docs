---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup/
title: Back up Compute Engine instances \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:00.323017+00:00
---

# Back up Compute Engine instances  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/compute/compute-instance-backup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Back up Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

The Google-managed backup process for Compute Engine instances involves sending data to a backup vault. These backup vaults provide immutability and enforced retention. You can choose to store backups in a single region or across multiple regions.

The Google-managed model supports two primary execution methods: scheduled backups and on-demand backups. This document shows you how to configure and manage these backups.

## Overview

Compute Engine instance backup protects not only the disks, but also the VM's configuration and metadata—such as machine type, network interfaces, IP settings, service accounts, labels, and tags—while ensuring multi-disk crash consistency. Sending backups to a backup vault provides immutability and enforced retention. With a backup vault, you can store backups in a single region or in a multi-region. There are two main methods for backing up Compute Engine instances:

  * **Use the Google Cloud console to back up Compute Engine instances** : in the Google Cloud console, you can back up Compute Engine instances to a backup vault by applying backup plans. You can back up your data using either of the following methods. Both methods allow you to store your backups securely in a backup vault, providing a reliable way to recover your Compute Engine instances in case of data loss or other unexpected events.

    * **Scheduled backups** : automatically back up Compute Engine instances at specific intervals, such as daily, weekly, monthly, or yearly.

    * **On-demand backups** : create on-demand backups whenever needed. On-demand backups are useful for creating backups before making significant changes to your instances or for ad hoc data protection.

  * **Use the management console to back up Compute Engine instances** : if you have any of the following backup requirements, you can use the management console to back up Compute Engine instances:

    * Cross-region backups
    * Backups of specific disks attached to a Compute Engine instances
    * Automated protection of Compute Engine instances based on tags
    * If the Google Cloud console-based backup plans and backup vaults are not in a [location that is compatible](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-vault#workload-location-compatibility) with the region where your source Compute Engine instances are running.



The appliance management console is part of Backup and DR for appliance-managed backups. If you must use the appliance management console, see [Discover and protect Compute Engine instances from the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-compute-engine).

## Before you begin

  1. Enable the Backup and DR API where the Compute Engine instances are located.

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=backupdr.googleapis.com&_ga=2.145630134.30427899.1640890668-1982243420.1634228058)

  2. [Create a backup vault](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create).

  3. [Create a backup plan](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create).

  4. Assign IAM roles and permission to the backup user.

  5. Grant backup vault access in the Compute Engine project.

  6. Set up Observability Analytics on your bucket to monitor Backup and DR backup jobs.




### IAM configuration

To configure scheduled backups or execute on-demand backups, an administrator must grant the following IAM roles on the backup vault project:

  * Backup and DR Backup User (`roles/backupdr.backupUser`)
  * Viewer (`roles/viewer`)



The specific permissions required for Google-managed backup operations include:

  * `backupdr.backupPlans.list`
  * `backupdr.backupPlanAssociations.createForComputeInstance`
  * `backupdr.backupPlanAssociations.list`
  * `backupdr.backupPlanAssociations.get`
  * `backupdr.backupPlanAssociations.triggerBackupForComputeInstance`
  * `backupdr.backupPlanAssociations.deleteForComputeInstance`
  * `backupdr.backupPlans.useForComputeInstance`
  * `backupdr.locations.list`
  * `backupdr.operations.get`
  * `cloudasset.assets.searchAllResources`



In addition to restoration permissions, the user must have permissions to view and retrieve backup metadata:

  * `backupdr.backupVaults.get`
  * `backupdr.backupVaults.list`
  * `backupdr.bvbackups.list`
  * `backupdr.bvbackups.get`
  * `backupdr.bvdataSources.list`
  * `backupdr.bvdataSources.get`



If the Compute Engine instance resides in a different project than the backup vault, you must grant the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) role to the backup vault service agent within the Compute Engine project.

The following table lists the permissions required for each API call:

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
Backup Plan Associations | Create Backup Plan Association | Workload project |   
|  | backupdr.backupPlanAssociations.createForComputeInstance | Workload project  
|  | backupdr.backupPlans.useForComputeInstance | Admin project  
| Delete Backup Plan Association | backupdr.backupPlanAssociations.deleteForComputeInstance | Workload project  
| Trigger an on-demand backup on Backup Plan Association | backupdr.backupPlanAssociations.triggerBackupForComputeInstance | Workload project  
| Get Backup Plan Association | backupdr.backupPlanAssociations.getForComputeInstance | Workload project  
| List Backup Plan Associations | backupdr.backupPlanAssociations.list | Workload project  
| Fetch Backup Plan Associations | backupdr.backupPlanAssociations.fetchForComputeInstance | Workload project  
Data Source | Get DataSource | backupdr.bvdataSources.get | Admin project  
| List DataSources | backupdr.backupPlanAssociations.list | Admin project  
Backups | Get Backup | backupdr.bvbackups.get | Admin project  
| List Backups | backupdr.bvbackups.list | Admin project  
| Delete Backup | backupdr.bvbackups.delete | Admin project  
| Restore Backup | backupdr.bvbackups.restore | Admin project  
Operations | List Operations | backupdr.operations.list | Respective project  
| Get Operations | backupdr.operations.get | Respective project  
  
### Grant backup vault access in the Compute Engine project

To back up a Compute Engine instance in a project different from where the backup vault is created, you must grant the Backup and DR Compute Engine Operator (`roles/backupdr.computeEngineOperator`) IAM role to the backup vault service agent within the Compute Engine project. If the backup vault project where the backups will be stored is different from the Compute Engine project then assign the role to the backup vault service agent within the Compute Engine project.

To back up a Compute Engine instance in the same project where the backup vault is created, you don't need to grant any roles.

For information about granting roles to the backup vault service agent within the project you intend to back up, see [Grant a role to the service agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-vault-create#service_agent).

### Constraints and limitations

The Backup and DR does not support Google-managed backups for Compute Engine instances that use the following configurations:

  * Instances with extreme persistent disks attached
  * Instances using any hyperdisk-* disk types
  * Instances using C3D, H3, A3, or Z3 machine types
  * Instances with customer-supplied encryption keys (CSEK). Customer-managed encryption keys (CMEK) are supported; see Identity and Access Management configurations for required permissions.
  * Instances that lack attached disks
  * Instances exceeding 200 terabytes (TB) in size



## Configure a scheduled backup

Use the following instructions to configure a scheduled backup for Compute Engine instances.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click **Schedule backup**.

  3. Using the **Resource type** drop-down menu, select the resource type.

  4. From the **Projects** list, click **Browse** and select a project where the Compute Engine instances are located.

  5. From the **Region** list, select the region where your instances are located.

  6. From the **Resources** list, click **Browse**.

  7. Choose the Compute Engine instance that you want to back up and click **Done**.

  8. Click **Continue**.

  9. From the **Backup plan** list, click **Select**.

  10. Choose a backup plan that you want to protect the Compute Engine instance with.

  11. Click **Done**.

**Tip:** If the selected Compute Engine instance has one or more CMEK-encrypted disks, the list of available backup plans is automatically filtered to show only CMEK-compatible backup plans.
  12. Review the backup details and click **Schedule**.




###  gcloud 

  1. Get the instance ID.
         
         gcloud compute instances describe VM_NAME --zone=VM_ZONE --format="value(id)"
         

Replace the following:

     * `VM_NAME`: the name of the VM instance.
     * `VM_ZONE`: the location where the VM is located.
  2. Configure a scheduled backup.
         
         gcloud backup-dr backup-plan-associations create BACKUP_PLAN_ASSOCIATION_NAME \
           --location=VM_REGION \
           --resource=projects/VM_PROJECT_ID/zones/VM_ZONE/instances/VM_ID \
           --backup-plan=projects/PROJECT_ID/locations/LOCATION/backupPlans/BACKUP_PLAN
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association.
     * `VM_REGION`: the region where the Compute Engine instance is located.
     * `VM_PROJECT_ID`: the name of the project where the Compute Engine instances are located.
     * `VM_ZONE`: the zone where the Compute Engine instance is located.
     * `VM_ID`: the Compute Engine instance ID.
     * `PROJECT_ID`: the name of the project where backup plans exist.
     * `LOCATION`: the region where your backup plans exist.
     * `BACKUP_PLAN`: the name of the backup plan that you want to associate the Compute Engine instance with.



### Terraform

You can use a [Terraform resource to configure a scheduled backup](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/backup_dr_backup_plan_association).
    
    
    # Before creating a backup plan association, you need to create backup plan (google_backup_dr_backup_plan)
    # and compute instance (google_compute_instance).
    resource "google_backup_dr_backup_plan_association" "default" {
      provider                   = google-beta
      location                   = "us-central1"
      backup_plan_association_id = "my-bpa"
      resource                   = google_compute_instance.default.id
      resource_type              = "compute.googleapis.com/Instance"
      backup_plan                = google_backup_dr_backup_plan.default.name
    }
    

**Note:** Auto-generation of API code for applying a backup plan to a VM is not supported. You can manually write code to apply a backup plan.

## Selective disk backup for Compute Engine instances

By default, when a backup plan protects a Compute Engine instance, all disks attached to the instance are included in the virtual machine (VM) backup.

You can configure selective disk backup in a backup plan to exclude specific disks from VM backups. When you restore an instance from a selective disk backup, only the disks that were protected at the time of backup are restored.

You can configure selective disk backup using two mutually exclusive properties when creating or updating a backup plan:

  * **Boot disk only (`boot-disk-only`)**: backs up only the boot disk of the instance. All attached non-boot disks are excluded from the Compute Engine instance backup.
  * **Disk exclusion labels (`disk-exclusion-labels`)**: excludes any attached disk that matches the specified label key-value pairs. During backup runtime, the backup system checks the labels attached to each disk on the Compute Engine instance and excludes matching disks. If no matching labels are found on an attached disk, the disk is included in the backup.



### Configure selective disk backup in a backup plan

Use the following instructions to configure selective disk backup when creating or updating a backup plan:

###  Console 

  1. Follow steps 1 through 7 in [Create a backup plan with a backup rule](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-plan-create#create-with-rule), selecting **Compute Engine VM** as the **Resource Type**.
  2. Configure selective disk backup using the drop-down menu: 
     * **Include all disks** : backs up all disks attached to the Compute Engine instance.
     * **Include boot disk only** : backs up only the boot disk.
     * **Exclude disks by label** : excludes attached disks matching specific labels. Enter a label key-value pair (`key=value`).
  3. Click **Create**.



###  gcloud 

To configure selective disk backup, specify `boot-disk-only` or `disk-exclusion-labels` within the `--compute-instance-properties` flag when creating or updating a backup plan using the gcloud CLI.

  * Create a backup plan to back up only boot disks:
        
        gcloud backup-dr backup-plans create BACKUP_PLAN_NAME \
            --compute-instance-properties=boot-disk-only=true \
            --resource-type=compute.googleapis.com/Instance \
            --location=REGION \
            --project=PROJECT_ID \
            --backup-vault=BACKUPVAULT_NAME
        

Replace the following:

    * `BACKUP_PLAN_NAME`: the name of the backup plan.
    * `REGION`: the Google Cloud region where you want to create the backup plan.
    * `PROJECT_ID`: the name of the project where the backup vault resides.
    * `BACKUPVAULT_NAME`: the name of the backup vault that you want to use for backup storage.
  * Create a backup plan to exclude disks matching specific labels:
        
        gcloud backup-dr backup-plans create BACKUP_PLAN_NAME \
            --compute-instance-properties=disk-exclusion-labels=env:scratch,data:temp \
            --resource-type=compute.googleapis.com/Instance \
            --location=REGION \
            --project=PROJECT_ID \
            --backup-vault=BACKUPVAULT_NAME
        

Replace the following:

    * `BACKUP_PLAN_NAME`: the name of the backup plan.
    * `REGION`: the Google Cloud region where you want to create the backup plan.
    * `PROJECT_ID`: the name of the project where the backup vault resides.
    * `BACKUPVAULT_NAME`: the name of the backup vault that you want to use for backup storage.



**Note:** The `boot-disk-only` and `disk-exclusion-labels` properties are mutually exclusive.

## Application consistency for Backup and DR Compute Engine backups

[Application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots) capture the state of application data at the time of backup with all application transactions completed and all pending writes flushed to the disk.

Use the following instructions to configure application-consistent backups for Compute Engine instances.

### Before you begin

  1. Read [Application consistent snapshots](https://docs.cloud.google.com/compute/docs/disks/snapshot-best-practices#creating_application_consistent_snapshots).

  2. A backup plan for application-consistent instance backups in a Linux environment requires pre- and post-scripts. [Create the necessary pre and post snapshot scripts for a Linux environment](https://docs.cloud.google.com/compute/docs/disks/creating-linux-application-consistent-pd-snapshots#create-scripts).




### Create a backup plan for application-consistent backups on Compute Engine instances

Use the following instructions to create application-consistent backups for Compute Engine instances.

###  Console 

To create a backup plan that enables application consistency for your Compute Engine instances by using Guest Flush or VSS, do the following:

  1. In the Google Cloud console, go to the Backup and DR page.

[Go to Backup and DR](https://console.cloud.google.com/backupdr)

  2. From the navigation menu, click **Backup Plans**.

  3. Click **Create Backup Plan**.

The **Create a backup plan** page appears.

  4. Using the **Resource type** drop-down menu, select **Compute Engine VMs**.

  5. Enter a unique name in the **Backup plan name** field.

  6. Optional: Enter a description in the **Description** field.

  7. From the **Region** drop-down list, select the **Region** where you want to create the backup plan. This region must be compatible with the region of the Compute Engine instances you intend to back up.

  8. Under **Choose where to store backups** , select the **Backup vault location type**.

  9. Using the **Region** drop-down menu, select the backup vault location.

  10. Using the **Backup vault** drop-down menu, select the existing backup vault.

  11. Optional: to add backup rules, click **Add rule** and do the following:

     1. Using the **Name** field, enter a name for the backup rule.

     2. To select when to create backups, use the **Recurrence** drop-down list and select how often to create backups, either hourly, daily, weekly, monthly, or yearly.

     3. Using the **Time zone** drop-down menu, select the time zone you want to execute backup jobs in.

     4. Using the **Start time** drop-down menu, select the time you want backup jobs to begin.

     5. Using the **End time** drop-down menu, select the time you want backup jobs to complete.

     6. Using the **Delete backups after** field, enter the number of days you want to keep backups before they are deleted.

     7. Click **Save**.

  12. To include pending write operations and perform application-consistent backups, check the **Enable application consistent snapshot** box.

  13. Click **Create**.




Once created, this backup plan can be applied to your Compute Engine instances. Backups taken using this plan will attempt to perform a Guest Flush/VSS operation to achieve application consistency. The consistency type can be viewed in the Backup Plan list and Backup Inventory pages.

###  gcloud 

  1. Create the backup plan.
         
         gcloud backup-dr backup-plans create BACKUP_PLAN_NAME \
         --compute-instance-properties=guest-flush=true \
         --resource-type=compute.googleapis.com/Instance \
         --location=REGION \
         --project=PROJECT_ID \
         --backup-vault=BACKUPVAULT_NAME \
         --backup-rule=rule-id=RULE_NAME,recurrence=RECURRENCE,hourly-frequency=HOURS, \
         time-zone=TIME_ZONE,backup-window-start=START_TIME,backup-window-end=END_TIME,\
         retention-days=BACKUP_RETENTION --max-custom-on-demand-retention-days=MAX_ONDEMAND_RETENTION
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.
     * `REGION`: the Google Cloud region where you want to create the backup plan.
     * `PROJECT_ID`: the name of the project where the backup vault resides.
     * `BACKUPVAULT_NAME`: the name of the backup vault that you want to use for backup storage.
     * `RULE_NAME`: the name of the backup rule.
     * `RECURRENCE`: the frequency at which backups to be created. It can be hourly, daily, weekly, monthly, or yearly.
     * `HOURS`: the frequency of the hourly backups. Specify this value only if you set the recurrence to hourly. The minimum hourly frequency default value is six hours.
     * `TIME_ZONE`: the time zone for the backup plan, such as UTC. Use the [IANA time zone](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones) format to include the timezone for the backup plan.
     * `START_TIME`: the start time is the hour of the day in a 24 hour format. The start time must be before the end time and is inclusive for the backup window.
     * `END_TIME`: the end time is the hour of the day in a 24 hour format. The end time must be after the start time and is exclusive for the backup window.
     * `BACKUP_RETENTION`: the retention period of the backup. Note that the backup retention period must be equal to or greater than the backup vault enforced minimum retention period.
     * `MAX_ONDEMAND_RETENTION`: the maximum allowed custom retention period (in days) for on-demand backups created using this backup plan.
**Note:** All retention periods are capped at 36,135 days (99 years).**Note:** When `guest-flush` is set to true, all backups created with this plan will have `guest-flush` enabled.



**Note:** Application consistency for snapshots isn't supported for Google Cloud Hyperdisk.

### Update an existing backup plan for application-consistent backups of Compute Engine instances

Use the following instructions to update a backup plan to produce application-consistent backups of Compute Engine instances.

###  Console 

To update a backup plan to enable application consistency for your Compute Engine instances using Guest Flush or VSS, use the following instructions:

  1. In the Google Cloud console, go to the Backup and DR **Backup plans** page.

[Go to Backup plans](https://console.cloud.google.com/backupdr/backup-plans/list)

  2. Select the backup plan that you want to edit, or check its box and click the more_vert icon.

  3. Click **Edit**.

  4. Check the **Enable Application Consistency** box.

  5. Click **Save Changes**.




###  gcloud 

  1. Update the backup plan.
         
         gcloud backup-dr backup-plans update BACKUP_PLAN_NAME \
         --compute-instance-properties=guest-flush=true \
         --project=PROJECT_ID \
         --location=REGION \
         --description=DESCRIPTION \
         --backup-rule=BACKUP_RULE \
         --add-backup-rule=ADD_BACKUP_RULE \
         --remove-backup-rule=REMOVE_BACKUP_RULE \
         --max-custom-on-demand-retention-days=MAX_ONDEMAND_RETENTION
         

Replace the following:

     * `BACKUP_PLAN_NAME`: the name of the backup plan.
     * `PROJECT_ID`: the name of the project where the backup vault resides.
     * `REGION`: the location where you want to create the backup plan.
     * `DESCRIPTION`: the updated description of the backup plan.
     * `BACKUP_RULE`: full definition of an existing backup rule with updated values.
     * `ADD_BACKUP_RULE`: parameters of the backup rule to be added to the backup plan. This flag can be repeated to add more backup rules.
     * `REMOVE_BACKUP_RULE`: the existing backup rule to be removed from the backup plan.
     * `MAX_ONDEMAND_RETENTION`: the maximum allowed custom retention period (in days) for on-demand backups created using this backup plan.
**Note:** All retention periods are capped at 36,135 days (99 years).



**Note:** Application consistency for snapshots isn't supported for Google Cloud Hyperdisk.

## Change the backup plan applied to a Compute Engine instance

You can change the backup plan applied to a Compute Engine instance to another backup plan. The other backup plan must meet these criteria:

  * Use the same backup vault
  * Be in the same region as the Compute Engine instance



Use the following instructions to change the backup plan associated with a Compute Engine instance.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

The **Vaulted backups** page lists only the instances that have backup plans applied and their backups stored in a backup vault within a project.

  2. Select the backup that will get a different plan. Either from the backup details page for the backup, or from the more_vert menu, select **Change backup plan**. The **Select a backup plan** window lists only the backup plans that are valid for this instance.

  3. Select a backup plan and click **Apply**.

**Tip:** If the instance has one or more CMEK-encrypted disks, the list of available backup plans is automatically filtered to show only CMEK-compatible backup plans.



###  gcloud 

  * Change the assigned backup plan.
        
        gcloud backup-dr backup-plan-associations update BACKUP_PLAN_ASSOCIATION_NAME \
          --workload-project=VM_PROJECT_ID \
          --location=VM_REGION \
          --backup-plan=BACKUP-PLAN \
          --project=PROJECT_ID
        

Replace the following:

    * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup plan association resource.
    * `VM_PROJECT_ID`: the project-id of the Compute Engine instance.
    * `VM_REGION`: the location of the Compute Engine instance.
    * `BACKUP_PLAN`: the name of the backup plan that you are switching to.
    * `PROJECT_ID`: the project-id of the selected backup plan.



## List scheduled backups

Use the following instructions to list the backed up Compute Engine instances.

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

You can initiate an on-demand backup for a Compute Engine instance with a backup plan by triggering the backup rule of your choice to run immediately. On-demand backups typically capture only the data changed since the last backup (incremental).

When creating an on-demand backup, you can choose a rule from the backup plan associated with the Compute Engine instance. This rule determines when the on-demand backup gets deleted. You can check the backup job status from the **Jobs** page. For more information, see [Monitor backup and restore jobs in Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/monitor-reports/monitor-jobs-console).

**Note:** You can only run one backup job at a time. If an on-demand or scheduled backup job is already in progress, then attempting to start another on-demand backup job, the new job fails with the `Unable to queue the operation` error.

Use the following instructions to create an on-demand backup.

###  Console 

  1. Go to the **VM instances** > **Details** > **Backup Plan** to create an on-demand backup.
  2. Click **Create On-Demand Backup**. You must have the correct permissions to make an on-demand backup.
  3. Choose when to delete this backup. You have these options:

     * **Based on custom retention period** By default, the limit is set as the backup vault's minimum enforced retention period plus 30 days. To set a different limit, add a maximum custom on-demand retention period to your backup plan.
     * **Based on an existing backup rule**. Select a rule from the **Delete backups after** drop-down.
  4. Click **Create** to start the on-demand backup job.

  5. To view the status of the on-demand backup job, click **Notifications**.


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
    * `CUSTOM_RETENTION`: The custom retention period in days for this on-demand backup. This value must be equal to or greater than the backup vault retention time and less than or equal to the `max-custom-on-demand-retention-days` value that is configured in the backup plan (or the vault retention time + 30 days if `max-custom-on-demand-retention-days` is not configured).
    * `LABELS`: optional labels for the backup as comma-separated key-value pairs such as `webserver=backend,media=images`.



## Unprotect a Compute Engine instance

You can unprotect a Compute Engine instance by removing the backup plan applied to the instance. Removing a backup plan from a Compute Engine instance doesn't delete the backup plan or any backups created while the instance was in use. You can still access and manage these existing backups.

Use the following instructions to unprotect a Compute Engine instance.

###  Console 

  1. In the Google Cloud console, go to the **Vaulted backups** page.

[Go to Vaulted backups](https://console.cloud.google.com/backupdr/vaulted-backups)

  2. Click the name of the instance that you want to remove a backup plan.

  3. Select **Remove backup plan**.




###  gcloud 

  1. Unprotect a Compute Engine instance.
         
         gcloud backup-dr backup-plan-associations delete BACKUP_PLAN_ASSOCIATION_NAME\
           --project=PROJECT_ID \
           --location=LOCATION
         

Replace the following:

     * `BACKUP_PLAN_ASSOCIATION_NAME`: the name of the backup you want to delete.
     * `PROJECT_ID`: the name of the project.
     * `LOCATION`: the location of the scheduled backup.



## What's next

  * [Manage data sources in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/backup-datasource-manage)
  * [Manage backups in the Google Cloud console](https://docs.cloud.google.com/backup-disaster-recovery/docs/cloud-console/bv-backup-manage)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
