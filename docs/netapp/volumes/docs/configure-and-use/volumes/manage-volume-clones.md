---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume-clones/
title: Manage volume clones \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:48.366078+00:00
---

# Manage volume clones  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume-clones/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage volume clones Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage volume clones.

## About volume cloning

Cloning is the creation of a new volume from a snapshot in NetApp Volumes. If you create a volume from a snapshot with the Flex Unified service level, NetApp Volumes creates thin clones. For other service levels, NetApp Volumes creates a regular clone.

You can clone or copy entire volumes within a few seconds, regardless of volume size. The newly created clone represents a new volume. The process for snapshot-driven volume creation is similar to the procedure for new volume creation. NetApp Volumes assigns the clone to the same storage pool as the source volume. The host storage pool must have enough available capacity to accommodate the volume clone. The new volume inherits settings from the source volume. During volume creation, you can overwrite some settings, such as protocols in the creation workflow.

## Thin clones in Flex Unified service levels

For the Flex Unified service level, clones are thin by default. A thin clone initially shares the same underlying data blocks as its source volume. Because most data blocks are shared, thin clones are created quickly and consume little additional capacity at first.

As data is written to the source volume or the clone, shared blocks diverge over time and the clone consumes more capacity.

Source dependency is a factor because while a thin clone exists, the source volume can't be deleted as the two volumes share data. If you need the clone to be fully independent, split the clone. Splitting copies any shared blocks into the clone until no blocks are shared and the volumes become independent. For more information, see Split a thin clone.

## Thick clones in Standard, Premium, Extreme, and Flex File service levels

In the Standard, Premium, Extreme, and Flex File service levels, clones are always thick. NetApp Volumes creates a thin clone and then immediately splits the clone. The clone is created as quickly as a thin clone, but the clone consumes its own share of pool capacity independent of the source volume.

## When to use clones

Clones are useful for testing changes such as upgrades, configuration changes, or data transformations before you apply them to production data.

## Create a volume clone

To create a clone, complete the following steps:

  1. [Create a manual snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/create-manual-snapshots).

  2. [Create a new volume from that snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/new-volume-from-snapshot).




## View clone volume details

The volume details page for a clone includes the following fields:

  * **Capacity** : the volume's allocated capacity.

  * **Used capacity** : includes the shared space and any new data written to the volume.

  * **Shared capacity** : the snapshot data that is linked to the source volume.

    * **Source volume** : the source volume information is displayed with the shared capacity value and represents the relationship between the volumes.



The volume details page for a newly created volume from a snapshot displays a message with source volume details.

The source volume includes the **Associated clones** section. The **Delete** operation for this volume is disabled because it has associated clones.

## Edit a clone volume

After volume creation, you can modify the capacity of the clone volume as follows:

  * For NFS and SMB protocols, you can increase or decrease the clone volume's capacity. However, the capacity must be at least the total used capacity, including shared capacity and incrementally added data.

  * For the iSCSI protocol, you can only increase the capacity; you can't decrease it.




## Split a thin clone

This section provides instructions for how to split a thin clone.

### Before you begin

Before you split a thin clone, complete the following requirements:

  * The storage pool must have sufficient free capacity to accommodate the clone volume's full provisioned size after the split.

  * Delete any child clones of the clone volume you're splitting.

  * Delete any backups of the clone volume you're splitting.

  * Stop and delete any replications on the clone volume you're splitting.




### Considerations

You can't perform the following actions during volume splitting:

  * Create, manage, and run scheduled snapshots and backups.

  * Create new thin clones or replications.

  * Revert the volume you are splitting.




Use the following instructions to split a thin clone into a thick clone using the Google Cloud console or Google Cloud CLI.

### Console

  1. Go to the **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Choose one of the following methods to split the clone volume:

     * In the volumes list, select the clone volume that you want to split. Click the more_vert **Show more** icon on the clone volume, and then click **Split clone**.

     * Go to the source volume details page. In the **Associated clones** section, click the more_vert **Show more** icon on the clone volume, and then click **Split clone**.

     * Go to the clone volume details page, and then click **Split clone volume** in the information banner.

  4. In the **Split clone** dialog, enter the volume name in the **Name** field.

  5. Click **Split**.

**Note:** If there isn't enough available capacity in the storage pool, you will be notified. Increase the pool capacity, and then run the split operation again.

After you start the split clone action, the volumes list page opens. The status of the split action appears on the volumes list page and the **Notifications** bar. You can access the volume details page during the split, but with restrictions.




### gcloud

To split a clone:
    
    
     gcloud netapp volumes start-split CLONE_VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --source-volume=SOURCE_VOLUME_NAME

Replace the following information:

  * `CLONE_VOLUME_NAME`: the name of the clone volume you want to split.

  * `PROJECT_ID`: the name of the project that contains the volumes.

  * `LOCATION`: the location of the volumes.

  * `SOURCE_VOLUME_NAME`: the name of the source volume that the clone was created from.




To monitor a clone split:
    
    
     gcloud netapp volumes get-split-status CLONE_VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --source-volume=SOURCE_VOLUME_NAME

Replace the following information:

  * `CLONE_VOLUME_NAME`: the name of the clone volume you want to monitor.

  * `PROJECT_ID`: the name of the project that contains the volumes.

  * `LOCATION`: the location of the volumes.

  * `SOURCE_VOLUME_NAME`: the name of the source volume that the clone was created from.




## Delete a clone volume

Consider the following when you delete a clone volume:

  * A clone volume that has no associated child volumes can be deleted like a standard volume.

  * The source volume can be deleted only after all its associated clones are deleted.




You delete a thick clone volume the same way that you delete a regular volume. For more information, see [Delete a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume#delete_a_volume).

## What's next

[Manage quota rules](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
