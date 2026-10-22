---
url: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/manage-volume-migration/
title: Manage your volume migrations \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:32.317862+00:00
---

# Manage your volume migrations  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/manage-volume-migration/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your volume migrations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage your volume migrations.

## View volume migration details

After you create a volume migration and successfully authenticate it, the replication process starts.

A migration's current phase is indicated by its _mirrorState_ :

  * **Preparing** : the baseline transfer is in progress.

  * **Transferring** : an incremental transfer is in progress.

  * **Mirrored** : the migration is idle, waiting for the next hourly incremental transfer to start.

  * **Stopped** : the user stopped the migration.




Use the following instructions to view details of a volume migration using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Migrations**.

  3. From the list of migrations, select the migration you want to view.




### gcloud

To view details of a volume migration:
    
    
    gcloud netapp volumes replications list --volume=DESTINATION_VOLUME --location=REGION
    

## Edit a volume migration

The following parameters of a volume migration can be edited:

  * Cluster-location
  * Description
  * Labels



You can also edit the details of the destination volume using [Edit a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume#edit_a_volume).

Use the following instructions to edit details of a volume migration using the Google Cloud console:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click the name of the destination volume to open its details page.

  4. Click the **Migration** tab.

  5. Click **Edit migration**.




## Stop or pause a volume migration

When you stop a migration, the destination volume becomes read-writeable and can be modified. No incremental transfers occur when the replication is stopped, but a stopped replication can be resumed again.

To stop an active data transfer during baseline migration or if an ongoing incremental transfer is blocked, you must perform a forced stop. A forced stop instructs the migration to save a checkpoint. This checkpoint can be used later by the resume operation to continue where it left off.

Use the following instructions to stop or pause a volume migration using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Migrations**.

  3. From the list of migrations, select the migration you want to stop.

  4. Click **Stop**.

  5. A confirmation dialog with information is displayed. Enter the volume name and click **Stop** to confirm.

  6. If a transfer is running, another dialog is displayed asking if you want to perform a force stop. A force stop cancels the current transfer and reverts the destination volume back to the last successful transfer. You can either cancel the dialog and wait for the transfer to complete or initiate a force stop.

  7. Wait for the **Transfer status** to change to **Stopped**.




### gcloud

To stop or pause a volume migration:
    
    
    gcloud netapp volumes replications stop REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

If the command returns an error due to baseline or incremental transfer that is in progress, you can add the `--force` flag to the command to force a stop and create a checkpoint for a later resume operation.

## Resume a volume migration

When you resume a migration, the destination volume reverts to the latest common checkpoint or snapshot with the source volume. Incremental transfers then start from this point. This action undoes any changes made to the destination volume's content, so make sure this is your required outcome. Destination volume settings such as size, protocol settings, and policies won't be synchronized with the source volume.

Use the following instructions to resume a volume migration using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Migrations**.

  3. From the list of migrations, select the migration you want to resume.

  4. Click **Resume**.

  5. A confirmation dialog with information is displayed. Enter the volume name and click **Resume** to confirm.

  6. Wait for the **Transfer status** to change to **Preparing** or **Mirrored**.




### gcloud

To resume a volume migration:
    
    
    gcloud netapp volumes replications resume REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

## Sync a volume migration

The sync operation lets you run a manual, unscheduled incremental transfer on a migration that is in a mirrored transfer state. This operation is used during cutover to transfer the latest changes from the source to the destination immediately, without waiting for the next scheduled incremental transfer.

The service lets you run up to a maximum of five sync operations per volume per day.

Use the following instructions to sync a volume migration using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Migrations**.

  3. From the list of migrations, select the migration you want to sync.

  4. Click **Sync now**.

  5. A confirmation dialog with information is displayed. Enter the volume name and click **Sync now** to confirm.

  6. Wait for the operation to finish.




### gcloud

To sync a volume migration:
    
    
    gcloud netapp volumes replications sync REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

## Cutover a volume migration

To perform a [cutover](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#cutover), complete the following steps:

  1. Make sure all settings on the destination volume are correct. For more information about protocol options, export, and snapshot policies, see [Volume details](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume#edit_a_volume).

  2. Wait for an ongoing incremental transfer to finish. This is confirmed when the mirrorState shows as **Mirrored** in the [Volume migration details](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/manage-volume-migration#view_volume_migration_details) page.

  3. Stop all write access to the source volume. This can be done by shutting down the applications or removing access permissions for clients.

  4. Run a sync operation to transfer the latest changes from the source to the destination. The _mirrorState_ will change to **Transferring** and back to **Mirrored** after the transfer is complete.

  5. Stop the migration to make the destination volume read-writeable.

  6. Restart clients and applications, this time using the destination volume.

  7. Optional: consider [setting up backups](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/set-up-volume-backups) for the destination volume.

  8. Finally, cleanup the volume migration by deleting it.




## Delete a volume migration

You can delete a volume migration after the migration is complete and you have either cutover your workload or decided to cancel the migration.

The volume migration deletion includes the following cleanup steps:

  1. Make sure the migration status is **Stopped**.

  2. Delete the replication.

  3. Consider deleting the cluster peering to NetApp Volumes on your source ONTAP cluster using the `cluster peer delete` command, but only if this was the last migration from your source ONTAP cluster.

**Caution:** Don't delete cluster peering if other migrations to the same NetApp Volumes cluster are still in progress.
  4. Remove any additional networking set up for the migration once it's completed.


**Note:** If the baseline transfer for your destination volume isn't completed, deleting the replication also deletes the destination volume to prevent it from being left in an _inactive_ state. However, if the baseline transfer has finished, deleting the replication doesn't delete the destination volume.

Use the following instructions to delete a stopped volume migration using the Google Cloud console or Google Cloud CLI:

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Under **Data protection** , click **Migrations**.

  3. From the list of migrations, select the migration you want to delete.

  4. Click **Finish migration**. This action deletes the migration.

  5. A confirmation dialog with information is displayed. Enter the migration name and click **Finish** to confirm.




### gcloud

To delete a stopped volume migration:
    
    
    gcloud netapp volumes replications delete REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

## What's next

[Change volume settings during volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/change-volume-settings-volume-migration).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
