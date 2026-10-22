---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-policy/
title: Manage your backup policies \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:32.880675+00:00
---

# Manage your backup policies  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/manage-backup-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your backup policies Stay organized with collections  Save and categorize content based on your preferences. 

This page provides instructions for how to manage your volumes' backup policies.

Google Cloud NetApp Volumes supports the following management features:

  * **Edit backup policy** : edit existing backup policies, including changing descriptions, backup schedules, and labels.

  * **Assign volume** : assign eligible volumes to existing backup policies.

  * **Create similar backup policy** : a convenient way to copy a policy to a different region.

  * **Resume** : resume a paused backup policy to re-activate the configured backup schedule configurations and all automatic backup schedules.

  * **Pause** : pause a backup policy to temporarily disable the backup policy's automatic backup schedule.

  * **Delete** : delete a backup policy. Before you can delete a backup policy, you need to unassign all volumes.

  * **Unassign volume** : Unassign volumes associated with a backup policy to stop scheduled backups for the volumes.




## Considerations

  * Pausing a backup policy stops backups for all associated volumes.

  * Resuming a backup policy reactivates scheduled backups for all associated volumes.

  * To delete a backup policy, you must unassign all associated volumes.

  * Destination volumes of a volume replication can't create scheduled backups. Scheduled backups can be created only on the source volume. Before running [reverse and resume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/reverse-and-resume-replication), you need to disable scheduled backups from the volume that becomes new destination volume. This disables the backups. Its recommended to configure the scheduled backups on the volume that becomes new source volume.




## View backup policy details

Use the following instructions to view backup policy details using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup policies** from the **Policies** menu.

  3. Click the backup policy you want to see details for.

The backup policies page opens. You can view the following details:

     * **Resource type** : displays which NetApp Volumes feature you're viewing details for.

     * **State** : the current status of your backup policy.

     * **Resource state** : the state of your backup policy.

     * **Description** : the description you provided for the backup policy.

     * **Name** : the name of your backup policy.

     * **Region** : the location of your backup policy.

     * **Created** : the date and time your backup policy was created.

     * **Labels** : lists labels associated with your volume.

     * **Backup schedule** : displays the appointed backup schedule of your backup policy.

     * **Associated volumes** : lists the volumes you associated with the backup policy.

       * **Status** : the backup policy status, including whether it is enabled or disabled.

       * **Name** : the name of the backup policy.

       * **Backup policy allowed** : displays whether the backup policy is allowed on the volume or disallowed.

       * **Location** : location of your volume.

       * **Utilization** : displays how much space has been consumed by the volume.

       * **Labels** : the list of labels associated with the backup policy.

       * **Show more menu** : actions you can perform on the volume including unassigning the volume or viewing more details.




### gcloud

To view all the backup policies:
    
    
      gcloud netapp backup-policies list

To lookup a specific backup policy:
    
    
      gcloud netapp backup-policies describe POLICY_NAME \
       --location=LOCATION
     

Replace the following information:

  * `POLICY_NAME`: the name of the backup policy.

  * `LOCATION`: the location of the backup policy.




## Edit an existing backup policy

Use the following instructions to edit an existing backup policy using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup policies** from the **Policies** menu.

  3. In the **Backup policies** page, click the backup policy you want to edit.

  4. Select the volume you want to change backup policy details for.

  5. In the backup policy's details page, click **Edit**.

  6. In the **Edit backup policy** page, make the following changes to your backup policy:

     * **Description** : use the **Description** field update the description of the backup policy.

     * **Backup schedule** : use the **Backup schedule** tabs to update the number of daily, weekly, and monthly backups to retain.

     * **Labels** : use the **Labels** section and click **Add label** to edit existing labels or create new labels.

  7. Click **Save**.




### gcloud

Update a backup policy:
    
    
      gcloud netapp backup-policies update BACKUP_POLICY_NAME \
       --location=LOCATION \
       --description=DESCRIPTION \
       --enabled=TRUE_OR_FALSE \
       --daily-backup-limit=DAILY_BACKUP_LIMIT \
       --weekly-backup-limit=WEEKLY_BACKUP_LIMIT \
       --monthly-backup-limit=MONTHLY_BACKUP_LIMIT \
       --update-labels=foo=bar \
       --remove-labels=foo=bar

Replace the following information:

  * `BACKUP_POLICY_NAME`: the name of the backup policy.

  * `LOCATION`: the location in which you want to create the backup policy.

  * `DESCRIPTION`: the description for the backup policy.

  * `ENABLED`: lets the backup policy update as directed.

  * `DAILY_BACKUP_LIMIT`: the number of daily backups in the backup policy.

  * `WEEKLY_BACKUP_LIMIT`: the number of weekly backups in the backup policy.

  * `MONTHLY_BACKUP_LIMIT`: the number of monthly backups in the backup policy.




## Assign a volume to an existing backup policy

Use the following instructions to assign a volume to an existing backup policy using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes** from the **Storage** menu.

  3. In the **Volumes** page, select the volume you want to create a backup for.

  4. In the volume details page, click the **Backups** tab.

  5. Click **Assign backup policy**.

  6. Select the backup policy you want to assign to the volume from the **Backup policy** menu.

  7. Select the backup vault you want to store your backups in from the **Backup vault** menu.

**Note:** CMEK-enabled backup vaults aren't available for the Flex File service level.**Note:** If the backup vault assigned to the volume has a specified minimum retention period, any manual backups performed are also assigned that minimum retention value. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).
  8. Click **Assign**.




### gcloud

To assign a backup policy to a volume, add the backup policy to the volume configuration:
    
    
      gcloud netapp volumes update VOLUME_NAME \
       --location=LOCATION \
       --backup-config=backup-policies=POLICY_RESOURCE_PATH,enable-scheduled-backups=TRUE_OR_FALSE

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location of the volume.

  * `POLICY_RESOURCE_PATH`: full resource path of the backup policy. Format as `projects/PROJECT_ID/locations/POLICY_LOCATION/backupPolicies/POLICY_NAME`




### ONTAP-mode

To assign a volume to an existing backup policy:
    
    
    gcloud netapp storage-pools update-backup-config STORAGE_POOL \
      --project=PROJECT_ID \
      --location=LOCATION \
      --volume-uuid=VOLUME_UUID \
      --backup-config=backup-vault=BACKUP_VAULT_PATH,backup-policies=POLICY_RESOURCE_PATH,enable-scheduled-backups=TRUE_OR_FALSE

Replace the following information:

  * `STORAGE_POOL`: the name of the ONTAP-mode storage pool where the volume resides.

  * `PROJECT_ID`: the name of your project.

  * `LOCATION`: the region where the volume resides.

  * `VOLUME_UUID`: the universally unique identifier (UUID) of the volume to which you want to attach a backup policy.

  * `BACKUP_VAULT_PATH`: the full resource path of the backup vault. Format as `projects/PROJECT_ID/locations/VAULT_LOCATION/backupVaults/BACKUP_VAULT_NAME`.

  * `POLICY_RESOURCE_PATH`: the full resource path of the backup policy. Format as `projects/PROJECT_ID/locations/POLICY_LOCATION/backupPolicies/BACKUP_POLICY_NAME`.




## Assign a backup policy for a new volume

Use the following instructions to assign a backup policy for a new volume using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes** from the **Storage** menu.

  3. In the **Volumes** page, click **Create**.

  4. Configure all volume settings as required.

  5. Check the **Allow scheduled backups** checkbox from the **Backup configuration** section.

  6. Use the **Backup policy** menu to select an existing backup policy or [create a new backup policy](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/create-backup-policy).

  7. Use the **Backup vault** menu to select a backup location from the **Backup location** section.

**Note:** CMEK-enabled backup vaults aren't available for the Flex File service level.**Note:** If the backup vault assigned to the volume has a specified minimum retention period, any manual backups performed are also assigned that minimum retention value. For more information, see [Prevent backup deletion](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#prevent_backup_deletion).
  8. Optional: click **Add label** to add relevant labels from the **Labels** section.

  9. Click **Create**.




### gcloud

If you want to configure backup as part of the volume creation, add the `backup-config` parameter to your volume creation command:
    
    
      gcloud netapp volumes create VOLUME_NAME \
       --location=LOCATION \
       --storage-pool=STORAGE_POOL \
       --capacity=1024 \
       --share-name=SHARE_NAME \
       --protocols=PROTOCOL \
       --backup-config=backup-policies=POLICY_RESOURCE_PATH,backup-vault=VAULT_RESOURCE_PATH,enable-scheduled-backups=TRUE_OR_FALSE

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location of the volume.

  * `STORAGE_POOL`: the storage pool to create the volume in.

  * `CAPACITY`: the capacity of the volume.

  * `SHARE_NAME`: the NFS export path or SMB share name of the volume.

  * `PROTOCOLS`: the protocol for the volume.

  * `VAULT_RESOURCE_PATH`: full resource path of the backup vault. Format as `projects/PROJECT_ID/locations/VAULT_LOCATION/backupVaults/VAULT_NAME`

  * `POLICY_RESOURCE_PATH`: full resource path of the backup policy. Format as `projects/PROJECT_ID/locations/POLICY_LOCATION/backupPolicies/POLICY_NAME`




For more information, see [Google Cloud SDK documentation for NetApp Volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/create).

## Unassign a backup policy from a volume

Use the following instructions to unassign a backup policy from a volume using the Google Cloud console or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes** from the **Storage** menu.

  3. In the **Volumes** page, select the volume you want to change backup policy details for.

  4. In the volume details page, click the **Backups** tab.

  5. Select **Manage backup policy**.

  6. Click **Unassign backup policy**.

A message appears confirming that you are unassigning the backup policy for the specific volume. To confirm, click **Unassign**.




### ONTAP-mode

To unassign a backup policy from a volume, set the backup policy name to empty. This action disassociates the volume from any backup policy.
    
    
    gcloud netapp storage-pools update-backup-config STORAGE_POOL \
      --location=LOCATION \
      --volume-uuid=VOLUME_UUID \
      --backup-vault=projects/PROJECT_NAME/locations/LOCATION/backupVaults/BACKUP_VAULT_NAME \
      --backup-policies=""

Replace the following information:

  * `STORAGE_POOL`: the name of the ONTAP-mode storage pool where the volume resides.

  * `LOCATION`: the region where the volume resides.

  * `VOLUME_UUID`: the universally unique identifier (UUID) of the volume whose backup you want to perform.

  * `PROJECT_NAME`: the name of your project.

  * `BACKUP_VAULT_NAME`: the name of the backup vault where you want to create the backup.




## Pause backup policy for volume

Use the following instructions to pause a backup policy for volume using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes** from the **Storage** menu.

  3. In the **Volumes** page, select the volume you want to change backup policy details for.

  4. In the volume details page, click the **Backups** tab.

  5. Select **Manage backup policy**.

  6. Clear the **Allow scheduled backups** checkbox.

The policy pauses for the volume.

  7. Click **Save**.




### gcloud
    
    
      gcloud netapp volumes update VOLUME_NAME \
       --location=LOCATION \
       --backup-config=enable-scheduled-backups=FALSE

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location of the volume.




### ONTAP-mode

To pause an active backup policy for a volume, set the `enable scheduled backups` parameter to `false` in the update backup policy command:
    
    
    gcloud netapp storage-pools update-backup-config STORAGE_POOL \
      --location=LOCATION \
      --volume-uuid=VOLUME_UUID \
      --backup-vault=projects/PROJECT_NAME/locations/LOCATION/backupVaults/BACKUP_VAULT_NAME \
      --backup-policies=projects/PROJECT_NAME/locations/LOCATION/backupPolicies/BACKUP_POLICY \
      --enable-scheduled-backups=false

Replace the following information:

  * `STORAGE_POOL`: the name of the ONTAP-mode storage pool where the volume resides.

  * `LOCATION`: the region where the volume resides.

  * `VOLUME_UUID`: the universally unique identifier (UUID) of the volume whose backup you want to perform.

  * `PROJECT_NAME`: the name of your project.

  * `BACKUP_VAULT_NAME`: the name of the backup vault where you want to create the backup.

  * `BACKUP_POLICY`: the backup policy to use to update the configuration.




## Resume a paused backup policy

Use the following instructions to resume a paused backup policy using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup policies** from the **Policies** menu.

  3. In the **Backup policies** page, select the paused backup policy you want to resume.

  4. Click **Resume**.




### gcloud
    
    
      gcloud netapp volumes update VOLUME_NAME \
       --location=LOCATION \
       --backup-config=enable-scheduled-backups=TRUE

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location of the volume.




### ONTAP-mode

To resume a paused backup policy for a volume, set the `enable scheduled backups` parameter to `true` in the update backup policy command.
    
    
    gcloud netapp storage-pools update-backup-config STORAGE_POOL \
      --location=LOCATION \
      --volume-uuid=VOLUME_UUID \
      --backup-vault=projects/PROJECT_NAME/locations/LOCATION/backupVaults/BACKUP_VAULT_NAME \
      --backup-policies=projects/PROJECT_NAME/locations/LOCATION/backupPolicies/BACKUP_POLICY \
      --enable-scheduled-backups=true

Replace the following information:

  * `STORAGE_POOL`: the name of the ONTAP-mode storage pool where the volume resides.

  * `LOCATION`: the region where the volume resides.

  * `VOLUME_UUID`: the universally unique identifier (UUID) of the volume whose backup you want to perform.

  * `PROJECT_NAME`: the name of your project.

  * `BACKUP_VAULT_NAME`: the name of the backup vault where you want to create the backup.

  * `BACKUP_POLICY`: the backup policy to use to update the configuration.




## Delete a backup policy

You can delete a backup policy if the policy has no associated volumes. Use the following instructions to delete a backup policy using either the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to NetApp Volumes in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Backup policies** from the **Policies** menu.

  3. In the **Backup policies** page, select the backup policy you want to delete.

  4. In the backup policy details page, click **Delete**.

A message appears that prompts you to confirm deletion.

  5. In the **Backup policy name** field, enter the name of the backup policy you want to delete.

  6. Click **Delete**.




### gcloud

Delete a backup policy:
    
    
      gcloud netapp backup-policies delete BACKUP_POLICY_NAME \
       --location=LOCATION

Replace the following information:

  * `BACKUP_POLICY_NAME`: the name of the backup policy.

  * `LOCATION`: the location from which you want to delete the policy.




## What's next

Read about [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
