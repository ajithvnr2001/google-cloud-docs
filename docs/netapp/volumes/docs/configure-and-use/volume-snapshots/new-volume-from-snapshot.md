---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/new-volume-from-snapshot/
title: Create a new volume from a snapshot \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:43:11.964534+00:00
---

# Create a new volume from a snapshot  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/new-volume-from-snapshot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a new volume from a snapshot Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details and instructions for how to create a volume from a snapshot.

## Considerations

Consider the following limitations before you create a volume from a snapshot:

  * **Changes to permission models** : if you use the cloning mechanism to switch the network-attached storage (NAS) protocol type, it might also switch the permission model that the security style provides. You might experience file access permission issues, which you can only fix manually with administrator access by using the NAS client tools to set permissions. For the Flex Unified service level volumes, you can't change the protocol when creating a volume from a snapshot; it's inherited from the source volume.

  * **Increased volume consumption** : after you create a volume from a snapshot, you have two independent volumes and both consume capacity from the host storage pool.

For Flex Unified service level volumes, thin clones initially share data blocks with the source volume and consume additional capacity only for new or modified data, while thick clones require additional storage because they hold their own full dataset over time. As a result, splitting a thin clone into a thick clone can significantly increase capacity usage in the storage pool and can increase costs.

  * **Replication capabilities** : volumes in Standard, Premium, Extreme, and Flex File service levels that are created from a snapshot don't support volume replication. While a Flex Unified volume is being split, volume replication isn't supported. Replication can be used only after the split is complete.

  * **Thin clones** : if you create a volume from a snapshot with the Flex Unified service level, the following considerations apply to thin clones:

    * The new volumes depend on the source volume. You can't delete the source volume until you delete all associated clone volumes, which are created from the source volume's snapshots.

    * You can't delete a snapshot until you delete the thin clone created from that snapshot.

    * You can create nested clones by creating a clone from a snapshot of an existing clone volume.




## Create a new volume from a snapshot

Use the following instructions to create a new volume from a snapshot using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

Use the following instructions to clone the latest state of the volume:

  1. Go to the **NetApp Volumes page** in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Select the volume to clone.

  4. Select the **Snapshots** tab.

  5. Click **Create Snapshot**.




To clone from a previous snapshot, complete the following instructions:

  1. Find the snapshot you want to clone.

  2. Click more_vert **Show more**.

  3. Click **Create new volume from snapshot**.

  4. Enter a volume name in the **Volume name** field for the cloned volume.

  5. Optional: Enter a description in the **Description** field.

  6. Enter a share name in the **Share name** field.

  7. Select the NAS protocol from the **Protocol(s)** drop-down list to use for the clone. We recommend that you choose the same protocol as the source volume. For more information, see [Change the access protocol of a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume#change_the_access_protocol_of_a_volume).

  8. Select the protocol-specific options to apply to the clone. Protocol options depend on the protocol choice. For more information, see [Create a volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

  9. Click **Block volume from deletion when clients are connected** in the **Configuration for selected protocol(s)** for volumes used as GCVE datastores. This setting is permanent.

  10. Optional: Define a **snapshot schedule**.

  11. Select **Make snapshot directory visible** if you want to enable file system access to snapshot versions by clients.

  12. Select **Allow scheduled snapshots** if you want to configure the volume to automatically take snapshots. You can specify the number of snapshots to keep at hourly, daily, weekly, and monthly snapshots intervals. NetApp Volumes specifies time in the UTC format. If you reach the maximum number of snapshots, the older snapshot deletes automatically.

  13. Review your snapshot selections.

  14. Optional: under the **Labels** section, click **Add label** to enter relevant labels for reporting and querying purposes.

  15. Click **Create**.

NetApp Volumes creates the volume within a few seconds. You can find the new volume in the **Volumes** page.

For the Flex Unified thin clones, the **Source volume** column represents the hierarchy of source and clone volumes. The **Source volume** column isn't shown by default. To add the **Source volume** column, select it from the **Displayed Column** option. This column displays the source volume name as a link to the source volume details page. For more information about how to manage clone volumes, see [Manage clone volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume-clones).

You can mount the volume with clients using the [NetApp Volumes instructions for how to mount a volume](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/mount-volume).




### gcloud

Create a new volume from an existing snapshot:
    
    
     gcloud netapp volumes create VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --storage-pool=STORAGE_POOL \
      --capacity=CAPACITY \
      --protocols=PROTOCOLS \
      --share-name=SHARE_NAME \
      --source-snapshot=SOURCE_SNAPSHOT

Replace the following information:

  * `VOLUME_NAME`: the name of the volume you want to create the snapshot in. This name must be unique per location.

  * `PROJECT_ID`: the name of the project you want to create the new volume in.

  * `LOCATION`: the location of the existing volume.

  * `STORAGE_POOL`: the name of the storage pool you want to create the volume in.

  * `CAPACITY`: the capacity of the volume. It defines the capacity that NAS clients see.

  * `PROTOCOLS`: choose the NAS protocols you want to export the new volume with. Valid choices include the following:

    * NFSV3 and NFSV4.1

    * NFSV3 and SMB

    * NFSV4.1 and SMB

We strongly recommend that you choose the same protocol as the source volume.

  * `SHARE_NAME`: the NFS export path or SMB share name of the new volume.

  * `SOURCE_SNAPSHOT`: the ID of the snapshot or fully qualified identifier for the snapshot.




For more options, see [Google Cloud SDK documentation for NetApp Volumes volume snapshots](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/snapshots).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [FlexClone volume use overview](https://docs.netapp.com/us-en/ontap/volumes/flexclone-efficient-copies-concept.html).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## What's next

[Restore your data using snapshots](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/restore-specific-data-with-snapshots).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
