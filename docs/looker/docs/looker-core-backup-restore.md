---
url: https://docs.cloud.google.com/looker/docs/looker-core-backup-restore/
title: Back up and restore a Looker (Google Cloud core) instance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T08:40:52.227009+00:00
---

# Back up and restore a Looker (Google Cloud core) instance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/looker-core-backup-restore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Back up and restore a Looker (Google Cloud core) instance Stay organized with collections  Save and categorize content based on your preferences. 

Backups of a Looker (Google Cloud core) instance contain a point-in-time snapshot of an instance's data, and they allow restoration of that instance's data to the time that the backup was created. Restoring a Looker (Google Cloud core) version doesn't upgrade or downgrade the Looker version for the instance. If a version change has occurred between the time of backup and the time of restore, the Looker (Google Cloud core) instance retains the Looker version that the instance is already using.

Backups can be restored only to the same instance that the backup was taken from; if you want to move data from one instance to another, use [import and export](https://docs.cloud.google.com/looker/docs/looker-core-import-export).

Each backup, whether automatic or manual, contains a record of all the data in the instance's internal database and in the instance's file server, which is most of the operational data for the Looker (Google Cloud core) instance. However, the data for [Elite System Activity](https://docs.cloud.google.com/looker/docs/elite-system-activity) is not backed up.

There is no disruption to Looker (Google Cloud core) performance during a backup.

## Required roles

To get the permissions that you need to back up or restore a Looker (Google Cloud core) instance, ask your administrator to grant you the [Looker Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.admin) (`roles/looker.admin`) IAM role on the project the instance resides in. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

**Note:** [IAM basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) might also contain permissions to back up or restore a Looker (Google Cloud core) instance. You shouldn't grant basic roles in a production environment, but you can grant them in a development or test environment. 

## Requirements and cautions

Your Looker (Google Cloud core) instance must meet several criteria to successfully back up and restore:

  * The Looker API must be enabled. Disabling the Looker API disables the ability to create manual or automatic instance backups.

[ Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=looker.googleapis.com)

  * If your Looker (Google Cloud core) instance uses a [Google-owned and Google-managed encryption key](https://docs.cloud.google.com/docs/security/encryption/default-encryption), which is the default for Looker (Google Cloud core) instances, the local key used by the Looker (Google Cloud core) instance must be the same at the time that the backup was created as it is when the backup gets restored.



Additionally, be aware of the following things before taking manual backups or restoring:

  * Restoring a backup overwrites the existing database and fileserver data, with the data as it was at the time of backup creation. For that reason, restoring an instance can result in the loss of data that was created after the time of backup creation.
  * If your Looker (Google Cloud core) instance uses [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/looker/docs/looker-core-cmek), see the Backups and CMEK section.
  * If your Looker (Google Cloud core) instance is enabled for [Looker reports](https://docs.cloud.google.com/looker/docs/enabling-looker-reports), see the Backups and Looker reports section.
  * Restoration takes minutes to hours, depending on instance size, and during that time, users cannot log into or use the instance.
  * You can't cancel a backup or restore operation once it has started.



## Automatic backups

Looker (Google Cloud core) instances are backed up automatically every 24 hours.

## Manual backups

You can take manual backups of your Looker (Google Cloud core) instance at any time.

Complete the following steps to manually back up your instance:

### console

  1. In the Google Cloud console, navigate to the [instance details page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#instance_tabs) for your instance.
  2. On the instance details page, select the **Backups** tab.
  3. On the **Backups** tab, click the **Create backup** button.
  4. A backup of your instance begins and is shown in the list of backups on the page. The status of the backup shows as in progress until the backup is completed. The **Notifications** menu of the Google Cloud console also displays the status of the backup.



### gcloud

Use the [`gcloud looker backups create` command](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/create).
    
    
    gcloud looker backups create --instance=INSTANCE_NAME --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance you want to back up; it is not associated with the instance URL.
  * `REGION`: the [region](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) the instance was created in.



To see the status of a backup after you have taken one, view the backups. The status of the backup will show as ACTIVE or FAILED.

## View backups

You can view all automatic and manual backups for your Looker (Google Cloud core) instance for the last 30 days. Complete the following steps to view backups:

### console

  1. In the Google Cloud console, navigate to the [instance details page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#instance_tabs) for your instance.
  2. On the instance details page, select the **Backups** tab.
  3. The backups for the last 30 days appear in the list on this tab, showing the following information:

     * **Status** : check_circle active, progress_activity updating, or errorfailed
     * **Created Time** : a timestamp of the creation start time of the backup
     * **Backup ID** : the alphanumeric ID of the backup
     * **Region** : the region of the instance that is being backed up
     * **Restore** : a button that lets you restore the backup
     * more_vert **Actions** menu: Click this menu and select **Delete Backup** to delete the backup
  4. You can use the **Filter** field at the top of the table to filter backups based on name, value, or the properties **Created on** , **Created before** , or **Created after**. You can also use the **OR** operator to search for multiple terms. Select **Clear filters** to remove your filter from the list of backups.




### gcloud

Use the [`gcloud looker backups list` command](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/list).
    
    
    gcloud looker backups list --instance=INSTANCE_NAME --region=REGION
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance for which you want to list backups; it is not associated with the instance URL.
  * `REGION`: the [region](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) the instance was created in.



This command returns the following information:

  * **NAME** : the alphanumeric ID of the backup
  * **STATUS** : **ACTIVE** or **FAILED**
  * **CREATE TIME** : a timestamp of the creation of the backup
  * **EXPIRE TIME** : a timestamp of the time the backup will be automatically deleted 



## Backup retention

Automated and manual backups are retained for 30 days.

## Delete backups

You can manually delete a manual or an automatic backup. Deleting a backup can't be undone.

### console

  1. In the Google Cloud console, navigate to the [instance details page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#instance_tabs) for your instance.
  2. On the instance details page, select the **Backups** tab.
  3. In the list of backups, click the more_vert **Actions** menu in the row for the backup that you want to delete.
  4. Select **Delete Backup**.
  5. A dialog appears that confirms the backup ID and created time for the backup to be deleted. To confirm that you want to delete the backup, type the last 4 characters of the backup ID.
  6. Click **Confirm Delete** to delete the backup. Click **Cancel** to cancel the deletion.
  7. During deletion, the backup shows an progress_activity updating status in the list of backups and in the **Notifications** menu of the Google Cloud console. Once deleted, the backup is removed from the list of backups.



### gcloud

Use the [`gcloud looker backups delete` command](https://docs.cloud.google.com/sdk/gcloud/reference/looker/backups/delete).
    
    
    gcloud looker backups delete BACKUP_ID --instance=INSTANCE_NAME --region=REGION
    

Replace the following:

  * `BACKUP_ID`: the ID of the backup. This ID can be found by viewing the backups.
  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance that the backup was created from; it is not associated with the instance URL.
  * `REGION`: the [region](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) the instance was created in.



After you delete a backup, you can view your backups to confirm the deletion.

## Restore a backup

**Warning:** Restoring a backup overwrites the existing database and fileserver data, with the data as it was at the time of backup creation. For that reason, restoring an instance can result in the loss of data that was created after the time of backup creation. See the Requirements and cautions section for more things to be aware of before restoring a backup.

A backup can be restored to only the Looker (Google Cloud core) instance from which it was created.

If you restore a backup, Looker (Google Cloud core) retains any backups that were made before or after the backup that was used for restoration.

If your Looker (Google Cloud core) instance uses [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek), see the Backups and CMEK section.

Complete the following steps to restore a backup:

**Note:** Google recommends that you create a backup before initiating a restore operation.

### console

  1. In the Google Cloud console, navigate to the [instance details page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#instance_tabs) for your instance.
  2. On the instance details page, select the **Backups** tab.
  3. In the list of backups, click the **Restore** button in the row of the backup that you want to restore.
  4. A dialog appears that confirms the backup ID and created time for the backup to be restored. To confirm that you want to restore the backup, type the last 4 characters of the backup ID.
  5. Click **Confirm Restore** to restore the backup. Click **Cancel** to cancel the restore.
  6. While the backup is being restored, a notice appears indicating that the instance is updating.



### gcloud

Use the [`gcloud looker instances restore` command](https://docs.cloud.google.com/sdk/gcloud/reference/looker/instances/restore).
    
    
    gcloud looker instances restore INSTANCE_NAME --backup=BACKUP_ID --region=REGION --async
    

Replace the following:

  * `INSTANCE_NAME`: the name of the Looker (Google Cloud core) instance that you want to restore; it is not associated with the instance URL.
  * `BACKUP_ID`: the ID of the backup. This ID can be found by viewing the backups.
  * `REGION`: the [region](https://docs.cloud.google.com/looker/docs/looker-core-view-console#the_instances_page) the instance was created in.



The `--async` flag must be included.

The restoration process may take several hours, depending on instance size. The restoration process can be monitored on the **Backups** tab, in the **Notifications** menu of the Google Cloud console, or by checking the **Status** of the instance on the [**Details** tab of the instance details page](https://docs.cloud.google.com/looker/docs/looker-core-view-console#instance_tabs) in the Google Cloud console.

  * An **Updating** status means that the restoration is in progress.
  * An **Active** status indicates that the restoration has been completed.

**Warning:** During restoration, Looker (Google Cloud core) users cannot log into or use the instance. Once a restore is initiated, it cannot be undone.

If you experience any issues with a restoration, [contact technical support](https://docs.cloud.google.com/looker/docs/looker-core-support).

## Backups and CMEK

If your Looker (Google Cloud core) instance uses [CMEK](https://docs.cloud.google.com/looker/docs/looker-core-cmek) for encryption, you can see the CMEK key version used in your instance on the [**Details** tab of the **Instances** page in the Google Cloud console](https://docs.cloud.google.com/looker/docs/looker-core-view-console#details_tab). You can see the CMEK key version that the backup uses when you view your backups.

When you want to back up or restore a Looker (Google Cloud core) instance that uses CMEK, keep the following requirements in mind:

  * For a restoration to be successful when CMEK is in use, the CMEK key version that was enabled at the time of backup must still be enabled at the time of restoration.
  * If the CMEK key version that is used by the backup is no longer enabled, make sure to [enable the key again](https://docs.cloud.google.com/kms/docs/enable-disable#enable) before restoration, or the restoration will fail.
  * If the CMEK key version that is used by the backup is deleted or no longer enabled, and if the key version cannot be re-enabled, the backup cannot be restored.
  * If you [rotate your CMEK key](https://docs.cloud.google.com/looker/docs/looker-core-cmek#rotate_your_key), Google recommends that you keep your previous key version enabled for 45 days to help ensure that your backups remain accessible.



If an instance is restored with a backup that uses a different key version, the instance will update to use the key version that is current for the instance at the time of restoration. The data in the Looker (Google Cloud core) instance remains encrypted with the instance's CMEK key version after the restore has completed.

## Backups and Looker reports

If your Looker (Google Cloud core) instance has the [Looker reports feature](https://docs.cloud.google.com/looker/docs/enabling-looker-reports) enabled, backup and restore actions have the following effects for Looker reports data.

  * **Deleted Looker reports can't be restored.** Even if a backup was taken before a report was deleted, the report won't be recovered after the backup is restored.
  * **Looker[folder access](https://docs.cloud.google.com/looker/docs/access-levels#types_of_access_to_folders) changes won't propagate to Data Studio.** Restoring a backup that was taken when folder access settings were different than the current settings may update folder access within Looker (Google Cloud core), but not within Data Studio.
  * **Changes to the Looker reports option won't propagate to Data Studio.** Restoring a backup that was taken when the [setting for the **Looker reports** option](https://docs.cloud.google.com/looker/docs/enabling-looker-reports#enabling) was different than the current setting will update the setting within Looker (Google Cloud core), but not within Data Studio, and the restoration won't change the enablement status of Looker reports.
  * **Hidden Looker reports can be accessed through its URL.** If a Looker report is created after a backup is taken, and then that backup is restored, the report is hidden. However, you can access the report through its URL.



## Disabling backups

**Caution:** The actions described in this section disable instance backups.

Instance backups are disabled if any of the following actions occur:

  * The Looker API is disabled in the Google Cloud project that the instance is hosted in.
  * The [Looker service account](https://docs.cloud.google.com/looker/docs/looker-core-service-account) loses access to the Google Cloud project that the instance is hosted in.
  * The [**Looker Service Agent**](https://docs.cloud.google.com/iam/docs/roles-permissions/looker#looker.serviceAgent) IAM role is removed from the Looker service account.



## What's next

  * [Delete and restart a Looker (Google Cloud core) instance](https://docs.cloud.google.com/looker/docs/looker-core-delete-restart)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
