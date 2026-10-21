---
url: https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified/
title: Migration to Flex Unified service level \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:27.963809+00:00
---

# Migration to Flex Unified service level  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/get-started/migration-to-flex-unified/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Migration to Flex Unified service level Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to migrate to the [Flex Unified](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#flex_unified_default-mode_versus_ontap-mode) service level. It also helps you to identify the best tools for your migration.

**Important:** As the Flex Unified service level is expanding, the Flex File service level is being phased out. Effective September 15, 2026, you can't create new Flex File storage pools, but existing pools remain supported. If you need assistance migrating to Flex Unified, [send an email to the support team](mailto:flex-file-migration@google.com). If you have specific region requirements or need support for Assured Workloads with Flex Unified, [contact the Google Cloud sales team](https://cloud.google.com/contact).

The Flex Unified service level provides all NetApp ONTAP features on Google Cloud for both file and block storage on a single platform.

The following table compares the features available in the Flex Unified service level against the legacy service levels (Flex File, Standard, Premium, and Extreme).

Feature | Flex Unified | Flex File  
(legacy) | Standard, Premium, and Extreme  
(legacy)  
---|---|---|---  
**Block storage (iSCSI and NVMe/TCP)** | Yes | No | No  
**Dual-protocol volumes (SMB and NFS)** | Yes | No | Yes  
**Auto-tiering** | Yes | Yes | Standard: No   
Premium or Extreme: Yes  
**ONTAP capabilities (ONTAP-mode pools)** | Yes | No | No  
**ONTAP integration (SnapMirror and FlexCache)** | Yes | No | Yes  
**Selective file restore and cross-region backups** | Yes | No | Yes  
**Shared QoS at the pool level** | Yes | Yes | No  
**Thin clones** | Yes | No | No  
**Large capacity pools and volumes** | Yes | No | Standard: No   
Premium or Extreme: Yes  
**Throughput** | Increased throughput  
with large volumes | Standard throughput | Increased throughput  
with large volumes  
**Regional availability** | Yes | Yes | No  
  
## Migration tools

You can use the following tools to migrate volumes to the Flex Unified service level:

  * Host-based data copy

  * Backup and restore

  * Support-assisted replication




Use the following table to select the best tool for your use case.

Tool | Use case | Considerations  
---|---|---  
Host-based data copy | Reorganizing volume data, either by removing or consolidating directories, or moving data from a regular volume to a large capacity volume | 

  * Available for Flex File, Standard, Premium, and Extreme service levels
  * Mount IP address changes

  
Backup and restore | Moving a few small volumes | 

  * Available for Flex File, Standard, Premium, and Extreme service levels
  * Restore at 300 GiB per hour
  * Mount IP address changes

  
Support-assisted replication | Moving a few large volumes | 

  * Available only for Standard, Premium, and Extreme service levels
  * Preserves snapshots and SMB permissions
  * Supports immediate cutover after final incremental sync
  * Mount IP address changes

  
  
## Host-based data copy

To move data to Flex Unified volumes by using host-based copy tools, complete the following steps:

  1. Select one of the data copy tools described in this section to use to create a full copy of the data.

  2. Create a full copy of the data, and then run incremental copies to capture any changes.




### Data copy tools

Select a data copy tool based on your client operating system and protocol:

  * Robocopy: To copy SMB files on a Windows VM.

  * NetApp XCP or rsync: To copy NFS files on a Linux VM.




#### Robocopy

Robocopy is a Microsoft file copy [tool](https://learn.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy) for Windows systems.

Consider the following options when you use robocopy:

  * `/mir`: Copies all subdirectories, including the empty subdirectories.

  * `/sec /secfix`: Copies security information, such as access control lists (ACLs), including information about the unchanged files with security changes. For more information, see [robocopy mirroring file permissions](https://techcommunity.microsoft.com/blog/filecab/robocopy-mir-switch-8211-mirroring-file-permissions/423662).

  * `/z`: Enables restartable mode, which allows robocopy to resume if interrupted.

  * `/mt:32`: Uses 32 threads for multi-threaded copies.

  * `/b`: Uses backup mode to override file and directory ACLs. Robocopy users must be members of the backup operators group on both the source and destination volumes.

  * `/r:2 /w:1`: Retries failed copies with a one-second wait.

  * `/log:<var>logfile</var>`: Logs robocopy status output.




#### NetApp XCP

XCP is a NetApp data migration [tool](https://xcp.netapp.com/) that copies files during data migrations. You can use it to migrate data to Flex Unified service level volumes. For additional assistance in using this tool, contact your NetApp sales specialist.

### Copy data using host-based tools

To copy data using a host-based copy tool, complete the following steps:

  1. Create a NetApp Volumes Flex Unified [pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool) and a [volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume).

  2. [Mount](https://docs.cloud.google.com/netapp/volumes/docs/get-started/quickstarts/mount-volume#mount_your_volume_on_a_client) the existing volume and the new Flex Unified volume to a virtual machine (VM) in your VPC. Use a data copy tool to transfer the data to the Flex Unified volume.

  3. To perform a final incremental copy of the data to the Flex Unified volume, disconnect clients from the current volume during scheduled maintenance. Verify that you have copied all files by checking file counts, checksums, and similar validation methods.

  4. Connect the clients to the Flex Unified volume and test access.




## Copy data using backup and restore

The [backup and restore](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups) feature in NetApp Volumes is available with Standard, Premium, Extreme, Flex File, and Flex Unified service levels. You can use this feature to back up a volume and restore it to a new Flex Unified storage pool.

### Limitations

The following limitations apply when you migrate using the backup and restore feature:

  * The backup features, such as cross-region backups and CMEK, aren't supported with Flex File, and you shouldn't use them during migrations.

  * The Flex File service level doesn't support large capacity volumes. You can't use the backup and restore feature to migrate data from a Flex File volume to a large capacity Flex Unified volume. Use a host-based data copy instead.

  * You can't choose a specific time for scheduled backups. If you have scheduled backups configured, check when previous backups ran to estimate the next backup time. For more control over backup timing, use manual backups.

  * Snapshot history isn't migrated using backup and restore feature. You must create export policies or set SMB NTFS permissions for the new volume. You must also create data protection policies for snapshots, backups, and replications on the new volume.




### Migrate a volume using backup and restore

To migrate a volume using the backup and restore feature, complete the following steps:

  1. Create a baseline backup of the Standard, Premium, Extreme, or Flex File volume before migration. If the volume has scheduled backups, you can use one of them. This backup serves as a baseline and helps reduce the time needed for the final incremental backup.

  2. Create a NetApp Volumes Flex Unified [pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool) if needed.

  3. During a maintenance window, complete the following steps:

     1. Disconnect the clients from the existing volume and perform a final incremental manual backup of the data.

     2. After the incremental backup completes, select **Create volume from backup** using the latest incremental backup, and then choose the Flex Unified storage pool where you want to create the new volume.

**Note:** For planning purposes, assume a restore rate of approximately 300 GiB per hour. You can track the progress in **Notifications** in the Google Cloud console.
     3. After the restore completes, connect a client to the Flex Unified volume, and then verify the volume using your application.

  4. Connect your remaining clients to the Flex Unified volume.




## Copy data using support-assisted replication

**Note:** Support-assisted replication is only available for volumes in the Standard, Premium, and Extreme service levels.

To copy data using the support-assisted replication tool, contact your NetApp sales specialist.

## What's next

For more information, see the following resources:

  * [Connect SMB clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-smb-clients).

  * [Connect NFS clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients).

  * [Connect iSCSI clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-iscsi-clients).

  * [Connect NVMe/TCP clients](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nvme-tcp-clients).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
