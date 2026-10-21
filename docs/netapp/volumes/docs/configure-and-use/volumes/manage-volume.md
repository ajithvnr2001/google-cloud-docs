---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume/
title: Manage your volume \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:29.791790+00:00
---

# Manage your volume  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Manage your volume Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage your volumes.

## Edit a volume

This section provides details about which volume settings are editable and instructions for how to edit a volume.

### Editable settings

You can change the following settings of a volume after it's created:

  * **Storage pool settings** : you can re-assign the volumes of Premium and Extreme service levels to a different pool to change its service level. Note that this option isn't available for the Flex and Standard service levels. For example, if the storage pool hosts a Premium service level volume, you can re-assign the volume to an Extreme service level storage pool and the other way around. The change to service levels lets you manage volume throughput limits and per GiB costs.

  * **Host groups** : the volume can be detached from their existing host groups or added to additional host groups.

  * **Volume details** : the capacity of a volume is adjustable up and down in 1 GiB increments. The size of the file data in the volume must be smaller than the volume capacity. When you increase the volume capacity, the pool that hosts the volume must have enough available capacity to accommodate the additional capacity requirement.

Changing the volume capacity can impact the maximum achievable throughput of volumes of Standard, Premium, or Extreme service level.

If the storage pool doesn't have enough capacity to accommodate the additional capacity requirement, you can increase the capacity of the pool, see [Storage pool capacity](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview#capacity).

  * **Protocol configurations** : you can change the configuration for selected protocols, but you can't change the protocol itself. For example, if the volume's protocol type is Server Message Block (SMB), you can choose to enable or disable SMB encryption, hide or show the SMB share, and enable or disable access-based enumeration.

  * **Export rules** : for volumes that use NFSv3 or NFSv4.1 protocol types, you can edit the export rules.

  * **Auto-tiering** : for volumes in storage pools that allow auto-tiering, you can enable auto-tiering. Once auto-tiering is enabled, it can be paused and resumed, but can't be disabled. You can change the cooling threshold value for each volume. For volumes in Flex Unified or Flex File custom-performance pools, you can enable or disable the hot tier bypass. For more information, see [Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

  * **Snapshot schedules** : you can modify the snapshot schedule. You can either make the snapshot directory visible if you want to enable file system access to snapshot versions by clients or allow scheduled snapshots to configure the volume to automatically take snapshots.

  * **Backup configuration** : you can do the following in backup configuration:

    * Attach a volume to a [backup vault](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#backup_vaults).

    * Remove a volume from a [backup vault](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#backup_vaults).

    * Set a schedule for automatic backups by attaching a [backup policy](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#backup_policies).

  * **Labels** : you can add, modify, or delete labels.




### Considerations

Consider the following before you edit a volume:

  * For volumes in an active volume replication, changes to either the source or destination volume also apply to the replication partner. For volumes in a [stopped replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/stop-or-resume-replication), changes apply independently from the replication partner. For volume capacity changes, the source and destination pools need enough available capacity to accommodate the change.

  * You can only move volumes to pools that are in the same location and have the same Active Directory policy, customer-managed encryption key (CMEK) policy, LDAP, and Virtual Private Cloud (VPC) settings as the pool that hosts the volume. Auto-tiered volumes can only be moved to a storage pool that allows auto-tiering, regardless of whether auto-tiering is enabled or paused for the volume.

  * Only pools that satisfy the conditional criteria are listed for selections. The target storage pool needs enough available capacity to accommodate the volume.

  * The maximum throughput for Standard, Premium, and Extreme service level volumes depends on the capacity of the volume and the service level you chose. An Extreme volume goes twice as fast as a Premium volume of the same capacity. A larger volume provides higher performance based on additional IOPS or throughput.




### Edit a volume

Use the following instructions to edit a volume using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Identify the volume you want to edit.

  3. Click more_vert **Show more** icon on the volume and click **Edit**.

  4. Edit volume details and save your changes.




### gcloud

Edit a volume:
    
    
    gcloud netapp volumes update VOLUME_NAME \
      --location=LOCATION \
      --PARAMETER=VALUE

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location for the volume.

  * `PARAMETER` and `VALUE`: the setting you want to change. For a list of all parameters you can update, see [Google Cloud SDK volume update documentation](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/update).




### Example to change a volume size

The following example shows you how to change a volume size:
    
    
    gcloud netapp volumes update VOLUME_NAME \
      --location=LOCATION \
      --capacity=CAPACITY

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location for the volume.

  * `CAPACITY`: the size of the volume.




### Example to change service level of a volume

Volumes in Premium or Extreme service levels can be moved to other pools.

The following example shows you how to change the service level of a volume:
    
    
    gcloud netapp volumes update VOLUME_NAME \
      --location=LOCATION \
      --storage-pool="projects/PROJECT_ID/locations/LOCATION/storagePools/POOL_NAME"

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location for the volume.

  * `PROJECT_ID`: the name of the project.

  * `POOL_NAME`: the name of the storage pool.




The `--storage-pool` parameter requires the full resource name of the target pool.

You can retrieve a list of all storage pool resource names in your project:
    
    
    gcloud netapp storage-pools list --format="value(NAME)"

### Example to edit auto-tiering settings of a volume

The following example shows you how to edit auto-tiering settings of a volume:
    
    
    gcloud netapp volumes update VOLUME_NAME \
    --location=LOCATION \
    --tiering-policy=tier-action=ENABLED,cooling-threshold-days=31

### Example to edit host-group settings of an iSCSI volume

Edit host-group settings of an iSCSI volume:
    
    
    gcloud netapp volumes update VOLUME_NAME \
      --location=LOCATION \
      --capacity=CAPACITY \
      --block-devices=name=LUN_NAME,host-groups=projects/PROJECT_ID/locations/REGION/hostGroups/HOST_GROUP_NAME

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `LOCATION`: the location of the volume where the volume was created.

  * `CAPACITY`: the new capacity of the volume. Volume capacity can only be increased.

  * `LUN_NAME`: the value of the `name` field from the `volume describe` command.

  * `PROJECT_ID`: the project where the host group resides.

  * `REGION`: the region name where the host group was created.

  * `HOST_GROUP_NAME`: the name of the host group.




For more information about additional optional flags, see [Google Cloud SDK documentation on volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/update).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [Volume modify](https://docs.netapp.com/us-en/ontap-cli//volume-modify.html#description).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## Revert a volume

Reverting a volume restores the volume's contents to the point-in-time state captured by a snapshot. Any changes made after that snapshot was created are lost, including snapshots created after that point.

Reverting a volume takes only a few seconds, similar to restoring a full-volume backup, but much faster. Use the reverting process when you need to roll back large-scale changes to an entire file system, such as after a ransomware event or after a script malfunction that deletes or modifies many files.

For more information, see [About volume reversion](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume). For instructions about how to revert a volume, see [Revert a volume from a snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/revert-volume-instructions).

## Change the access protocol of a volume

Changing the protocol of a volume can cause file-permission issues that you must resolve manually. This workflow is intended for experienced users.

When you create a volume, you select which access protocols (NFSv3, NFSv4.1, and SMB) are enabled for client access. You can't change this protocol selection after the volume is created. This protocol design prevents common permission and user-mapping problems. Different protocols use different security styles and permission models, which can lead to unexpected access denied behavior if user mapping and ACLs aren't configured correctly. For more information, see [File access control](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#file_access_control).

### Clone to a new volume with a different protocol

To change a volume's protocol, create a snapshot, clone the volume, and choose the required protocol for the new volume. Then, remount or remap clients to use the new volume.

**Important:** You can't change the volume security style when cloning.

Use the following guidance when changing a volume's protocol:

  * Changing from NFSv3 to NFSv4.1 or NFSv3+NFSv4.1 is supported.

  * Changing from NFSv4.1 to NFSv3+NFSv4.1 is supported. If you use NFSv4 ACLs, they're enforced in NFSv3 too. You can only manage NFSv4 ACLs through NFSv4.1, or you can overwrite the ACLs by using the `chmod` command through NFSv3 or NFSv4.1.

  * Changing from NFSv4.1 to NFSv3 is supported. If you use NFSv4 ACLs, they're enforced in NFSv3 too. You can overwrite the ACLs by using the `chmod` command.




Switching between SMB and NFS, or switching from single-protocol to multi-protocol, is likely to cause permission mismatches. You might need to reset permissions across the file system:

  * For NFS, use the following commands:

    * `chown`

    * `chmod`

    * `nfs4_setfacl`

  * For Windows, use the following tools:

    * Windows Explorer

    * `icacls`

    * PowerShell




## Delete a volume

This section provides instructions for how to delete a volume.

### Before you begin

When you delete a volume, all of the data and volume snapshots within the volume get deleted and the capacity of the pool returns. Before you delete a volume, you must [delete the replication relationship](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/delete-replication).

### Delete a volume

Use the following instructions to delete a volume using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Identify the volume you want to delete.

  3. Click the more_vert **Show more** icon on the volume and click **Delete**.

  4. A confirmation dialog appears. Read through the warnings.

  5. To proceed, enter the name of the volume and click **Delete**.




### gcloud

Run the following command:
    
    
      gcloud netapp volumes delete VOLUME_NAME \
       --project=PROJECT_ID \
       --location=LOCATION

Replace the following information:

  * `VOLUME_NAME`: the name of the volume to delete

  * `PROJECT_ID`: the name of the project the volume is in

  * `LOCATION`: The location of the volume




For more information about additional optional flags, see [Google Cloud SDK documentation on deleting volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/delete).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

For example, see [Volume delete](https://docs.netapp.com/us-en/ontap-cli//volume-delete.html).

After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## What's next

  * [Manage quota rules](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-quota-rules).

  * [Monitor volume performance and usage](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/monitor-volume-performance-usage).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
