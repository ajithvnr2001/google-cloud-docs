---
url: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/manage-external-replication/
title: Manage your external replications \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:34.718712+00:00
---

# Manage your external replications  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/manage-external-replication/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your external replications Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage your external replications.

## View external replication details

To monitor the replication status of an external replication, look up the NetApp Volumes replication resource and the SnapMirror status on ONTAP.

A replication's current phase is indicated by its mirrorState:

  * **Preparing** : the baseline transfer is in progress.

  * **Transferring** : an incremental transfer is in progress.

  * **Mirrored** : the replication is idle, waiting for the next hourly incremental transfer to start.

  * **Stopped** : the user stopped the replication.

  * **Externally managed** : indicates the destination volume is on the ONTAP side.




When the destination volume is on the ONTAP side, the `Externally managed` status is applied. Therefore, ONTAP is responsible for managing the replication and NetApp Volumes doesn't have information on whether the replication is `Stopped` or `Mirrored`. To determine the actual status, you must check ONTAP directly using the `snapmirror show` command.

Use the following instructions to view details of an external replication using the Google Cloud console or Google Cloud CLI or ONTAP CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **External replications** from the **Data protection** menu.

  3. From the list of replications, select the replication you want to view.




### gcloud

To view details of an external replication on NetApp Volumes:
    
    
    gcloud netapp volumes replications list --volume=NETAPP_VOLUMES_VOLUME --location=REGION
    

### ONTAP CLI

To view details of an external replication on ONTAP:
    
    
    ONTAP> snapmirror show -destination-path SVM_NAME:ONTAP_VOLUME_NAME
    

## Edit an external replication

Use the following instructions to edit an external replication using the Google Cloud console.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **External replications** from the **Data protection** menu.

  3. From the list of replications, select the replication you want to edit.

  4. In the **Edit replication** dialog, complete the following steps:

     1. Edit the volume replication description.

     2. Update the **Replication schedule** of the volume replication.

  5. Click **Save**.




### gcloud

Change the cluster location, schedule, description, and labels of a volume replication:
    
    
    gcloud netapp volumes replications update REPLICATION_NAME \
    --volume=DESTINATION_VOLUME --location=REGION \
    --cluster-location=CLUSTER_LOCATION \
    --description=DESCRIPTION \
    --replication-schedule=REPLICATION_SCHEDULE
    

## Stop or pause an external replication

When you stop an external replication, the destination volume becomes read-writable and can be modified. No incremental transfers occur when the replication is stopped, but a stopped replication can be resumed again.

To stop an active data transfer during baseline replication or if an ongoing incremental transfer is blocked, you must perform a forced stop. A forced stop instructs the replication to save a checkpoint. This checkpoint can be used later by the resume operation to continue where it left off.

Use the following instructions to stop or pause an external replication using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **External replications** from the **Data protection** menu.

  3. From the list of replications, select the replication you want to stop.

  4. Click **Stop**.

  5. A confirmation dialog with information is displayed. Enter the destination volume name and click **Stop** to confirm.

     * If the destination volume is on NetApp Volumes, the replication stops immediately.

     * If the destination volume is on ONTAP, a dialog with further instructions is displayed.

  6. If the destination volume is on ONTAP, complete the following steps:

     1. Follow the instructions to run the `snapmirror show` command first to verify the replication state.

     2. In the **Verify external replication state** section, select the `mirror-state` and `relationship-status` values displayed in the command output from the previous step.

     3. Click **Next**.

     4. If the replication is in a valid state as **Snapmirrored** and **Idle** , follow the instructions to run the `snapmirror break` command on the ONTAP system.

**Note:** If the replication states are **Snapmirrored** and **Transferring** , you can perform a force stop.
  7. Wait for the **Transfer status** to change to **Stopped**.




### gcloud

To stop or pause an external replication:
    
    
    gcloud netapp volumes replications stop REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

If the command returns an error due to baseline or incremental transfer that is in progress, you can add the `--force` flag to the command to force a stop and create a checkpoint for a later resume operation.

If the destination volume resides on NetApp Volumes, the replication will stop automatically. However, if the destination volume is on ONTAP, you must run a `snapmirror break` command on the ONTAP system. To determine the correct command for ONTAP, use the following:
    
    
    gcloud netapp volumes replications list --volume=NETAPP_VOLUMES_VOLUME --location=REGION
    

Look for the `hybridReplicationUserCommands` output. After running these ONTAP commands, the replication will be stopped. You can check the status on ONTAP by running:
    
    
    ONTAP> snapmirror show -destination-path SVM_NAME:ONTAP_VOLUME_NAME
    

NetApp Volumes can't detect if the command has been run. It will assume the replication is now externally managed, which is indicated by mirrorState as `Externally managed`.

## Resume an external replication

When you resume a stopped external replication, the destination volume reverts to the latest common checkpoint or snapshot with the source volume. Incremental transfers then start from this point. This action undoes any changes made to the destination volume's content, so make sure this is your required outcome. Destination volume settings such as size, protocol settings, and policies won't be synchronized with the source volume.

Use the following instructions to resume an external replication using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **External replications** from the **Data protection** menu.

  3. From the list of replications, select the replication you want to resume.

  4. Click **Resume**.

  5. A confirmation dialog with information is displayed. Enter the destination volume name and click **Resume** to confirm.

     * If the destination volume is on NetApp Volumes, the replication resumes automatically.

     * If the destination volume is on ONTAP, a dialog with further instructions is displayed.

  6. If the destination is on ONTAP, complete the following steps:

     1. Follow the instructions to run the `snapmirror show` command first to verify the replication state.

     2. In the **Verify external replication state** section, select the `mirror-state` and `relationship-status` values displayed in the command output from the previous step.

     3. Click **Next**.

     4. If the `mirror-state` is **Broken-off** and the `relationship-status` is either **Idle** or **Quiesced** , follow the instructions to run the `snapmirror resync` command on the ONTAP system.

  7. Wait for the **Transfer status** to change to **Preparing** or **Mirrored**.




### gcloud

To resume an external replication:
    
    
    gcloud netapp volumes replications resume REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

If the destination volume is hosted on NetApp Volumes, the replication will resume automatically. However, if the destination is on ONTAP, you must run a `snapmirror resync` command on the ONTAP system:
    
    
    ONTAP> snapmirror resync -destination-path SVM_NAME:ONTAP_VOLUME_NAME
    

Check the status of the mirror on ONTAP:
    
    
    ONTAP> snapmirror show -destination-path SVM_NAME:ONTAP_VOLUME_NAME
    

## Reverse and resume an external replication

The direction of the external replication can be reversed, making the current destination volume the new source volume and the other way around. The new destination volume will revert to its most recent common checkpoint or snapshot, and incremental transfers will start from that point. Make sure that this action will undo all changes made to the content on the new destination volume. The destination volume settings such as size, protocol configurations, and policies won't be synchronized with the new source volume.

Before reversing a replication, it must be stopped.

**Warning:** If ONTAP is the destination, NetApp Volumes doesn't prevent reversing and resuming a replication without first stopping it, which can lead to unintended data loss. Always make sure the replication is stopped before performing a reverse and resume operation.

The direction reversal must be initiated on the NetApp Volumes volume.

Use the following instructions to reverse and resume an external replication using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **External replications** from the **Data protection** menu.

  3. From the list of replications, select the replication you want to reverse and resume.

  4. Click **Reverse and resume**.

  5. A confirmation dialog with information is displayed. Enter the new destination volume name and click **Reverse and resume** to confirm.

     * If NetApp Volumes is the new destination, the replication reverses and resumes automatically.

     * If ONTAP is the new destination, a dialog with further instructions is displayed.

  6. If the destination is on ONTAP, complete the following steps:

     1. Follow the instructions to run the `snapmirror show` command first to verify the replication state.

     2. In the **Verify external replication state** section, select the `mirror-state` and `relationship-status` values displayed in the command output from the previous step.

**Note:** To reverse and resume the replication, the `mirror-state` must be **Broken-off** and the `relationship-status` must be either **Idle** or **Quiesced**.
     3. Click **Next**.

     4. If the replication is in a valid state, click **Reverse and resume**.




### gcloud

To reverse and resume an external replication:
    
    
    gcloud netapp volumes replications reverse REPLICATION_NAME \
     --volume=NETAPP_VOLUMES_VOLUME --location=REGION
    

If NetApp Volumes becomes the new destination, the replication reverses automatically. However, if ONTAP is the new destination, you must run a `snapmirror resync` command on the ONTAP system. You can determine the correct command for ONTAP by using:
    
    
    gcloud netapp volumes replications list --volume=NETAPP_VOLUMES_VOLUME --location=REGION
    

Look for the `hybridReplicationUserCommands` section in the output. If you don't run the ONTAP commands within 120 minutes, the replication will revert to its previous state.

Example commands you might expect:
    
    
    job schedule cron create -name replication-yyy -hour all -minute 0
    snapmirror resync -destination-path svm_src:sourcevol -source-path svm_dst:vol_dst
    snapmirror modify -destination-path svm_src:sourcevol -source-path svm_dst:vol_dst -schedule replication-yyy
    

## Sync an external replication

The sync operation lets you run a manual, unscheduled, and incremental transfer on a replication that is in a mirrored transfer state. This operation lets you send the latest changes from the source to the destination before stopping a replication and moving clients to the destination volume.

The service lets you run up to a maximum of five sync operations per volume per day.

**Note:** You can only sync an external replication using the Google Cloud CLI.

Use the following instructions to sync an external replication using the Google Cloud CLI.

### gcloud

To sync an external replication:
    
    
    gcloud netapp volumes replications sync REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

## Delete an external replication

The external replication deletion includes the following steps:

  1. Make sure the replication status is **Stopped**.

  2. Delete the replication.

  3. Consider deleting the cluster peering to NetApp Volumes on your external ONTAP cluster using the `cluster peer delete` command, but only if this was the last replication from the external ONTAP cluster.

**Caution:** Don't delete cluster peering if other replications or migrations to the same NetApp Volumes cluster are still in progress.
  4. If any additional networking was configured for the replication, you can remove it once the replication is complete.


**Note:** If the baseline transfer for your destination volume isn't completed, deleting the replication also deletes the destination volume to prevent it from being left in an _inactive_ state. However, if the baseline transfer has finished, deleting the replication doesn't delete the destination volume.

Use the following instructions to delete an external replication using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **External replications** from the **Data protection** menu.

  3. From the list of replications, select the replication you want to delete.

  4. Click **Delete replication**.

  5. A confirmation dialog with information is displayed. Enter the destination volume name and click **Delete** to confirm.

     * If the destination volume is on NetApp Volumes, the replication is deleted automatically.

     * If the destination is on ONTAP, a dialog with further instructions is displayed.

  6. If the destination is on ONTAP, complete the following steps:

     1. Run the `snapmirror show` command on the ONTAP system to check for any outdated snapmirror connections.

     2. In the **Verify external replication state** section, select the `mirror-state` and `relationship-status` values displayed in the command output from the previous step.

**Note:** To delete the replication, the `mirror-state` must be **Broken-off** and the `relationship-status` must be either **Idle** or **Quiesced**.
     3. Click **Next**.

     4. Click **Delete replication** to remove all references to the replication in NetApp Volumes.




### gcloud

To delete an external replication, first check if an outdated SnapMirror connection is configured on the ONTAP side:
    
    
    ONTAP> snapmirror show -destination-path SVM_NAME:ONTAP_VOLUME_NAME
    

You should either see no SnapMirror connection or one with mirrorState as **Broken-off**. If a connection is in the **Broken-off** state, proceed to delete it:
    
    
    ONTAP> snapmirror delete -destination-path SVM_NAME:ONTAP_VOLUME_NAME
    

Next, delete the replication within NetApp Volumes:
    
    
    gcloud netapp volumes replications delete REPLICATION_NAME \
     --volume=DESTINATION_VOLUME --location=REGION
    

## What's next

[Change volume settings during external replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/change-volume-settings-external-replication).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
