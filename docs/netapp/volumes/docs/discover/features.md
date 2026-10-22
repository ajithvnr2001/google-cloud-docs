---
url: https://docs.cloud.google.com/netapp/volumes/docs/discover/features/
title: Google Cloud NetApp Volumes features \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:28.876218+00:00
---

# Google Cloud NetApp Volumes features  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/discover/features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Google Cloud NetApp Volumes features Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the features and functionality of Google Cloud NetApp Volumes.

## Network-attached storage

NetApp Volumes shares file systems, or volumes, to network-attached storage (NAS) clients. NAS clients are usually virtual machines (VMs) that run on Windows or Linux operating systems using the industry-standard Network File System (NFS) and Server Message Block (SMB) protocols.

### Client-server model

Both NFS and SMB use a client-server model in which a client sends requests to a server to act on the file system. The server performs operations such as creating or deleting files or folders, modifying files, and browsing and reading files.

File systems are embedded in volumes which can be shared by many clients. Typically, Windows, Linux, and UNIX operating systems include built-in SMB and NFS client software.

### Access permissions

All file system objects must have an owner, but you can grant other users and groups access permissions for objects.

For NFS, ownership specifies user IDs and group IDs, which use standard UNIX-style user and group permissions. NFSv4.1 can use user IDs and group IDs or security principals. When you use NFSv4.1 with Kerberos, the usage of Kerberos principals replaces user ID access, which authenticates user identities. In addition to standard UNIX permissions, NFSv4.1 also offers NFSv4.1 access control lists as an alternative method to manage access.

For SMB, Windows security identifiers specify ownership and use NTFS-style access control lists to manage access to objects.

## Block storage

**Note:** NetApp Volumes provides block storage with iSCSI and NVMe/TCP protocols for the Flex Unified service level. You can use NVMe/TCP only with ONTAP-mode.

The NetApp Volumes Flex Unified service level lets you provision block storage by using the iSCSI and NVMe/TCP protocols. By using block storage, you can run workloads that require direct disk access, such as databases, while the users continue to benefit from a fully managed experience. The integration of block storage with iSCSI and NVMe/TCP protocols increases deployment flexibility, expanding the range of applications that you can host on Google Cloud.

NetApp Volumes presents block devices to hosts over a TCP/IP network by using the industry standard iSCSI and NVMe/TCP protocols. iSCSI allows VMs that are running on both Windows and Linux to access NetApp Volumes as locally attached disks, despite the physical storage being remote. You can use NVMe/TCP only with Linux servers.

### Initiator-target model

iSCSI uses an initiator-target model. The client, known as the iSCSI initiator, sends SCSI commands over IP networks to the storage system, which acts as the iSCSI target. The target receives these commands and performs block level operations such as reading and writing data, formatting disks, and managing partitions.

NetApp Volumes are presented as iSCSI Logical Unit Numbers (LUNs) to initiators as block devices. Each LUN appears to the client as a raw disk, allowing the operating system to create and manage its own file systems, such as NTFS, ext4, or XFS. Most Windows and Linux operating systems have built-in iSCSI initiator software, simplifying connection to iSCSI targets.

NVMe/TCP uses an initiator-target model that functions within the broader host-subsystem architecture model for NVMe over Fabrics (NVMe-oF) to access block storage over IP networks. The client acts as an NVMe host and communicates with the storage system, which exposes one or more NVMe subsystems, by using the NVMe protocol over TCP. The storage system presents NVMe block storage as NVMe namespaces to Linux clients.

For more information about how to create and manage host groups, see [About host groups](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/overview#about_host_groups).

## Storage pools

[Storage pools](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview) provide capacity for volumes, and you can divide a pool's capacity among the volumes in that pool. _Logical capacity_ refers to the capacity that you provision for volumes within the storage pool, which includes user data (files and LUNs), snapshots, and metadata.

All volumes in a storage pool share the following information:

  * Location

  * Service level

  * Virtual Private Cloud (VPC) network

  * Active Directory policy

  * LDAP use for NFS volumes, if applicable

  * Customer-managed encryption key (CMEK) policy

  * Zonal or regional pool availability

  * Auto-tiering capability

**Note:** If auto-tiering is enabled for the pool, you can turn it on or off for a volume.



Storage pools also provide performance capabilities to volumes:

  * Volumes in storage pools for the Standard, Premium, and Extreme service levels provide 16, 64, and 128 MiBps of throughput, respectively, per TiB of provisioned volume capacity.

  * Volumes in storage pools for the Flex File default performance service level share the pool's performance, which is 16 MiBps per TiB of provisioned pool capacity.

  * Volumes in storage pools for the Flex Unified or Flex File custom performance service levels share the pool's performance. You can configure the pool's performance independently of the capacity.




### Billing

You're billed for the logical capacity that you allocate to a storage pool, rather than the actual physical disk space or individual volume usage. Billing depends on the pool's location, service level, and total allocated size, regardless of how much capacity the volumes physically consume.

For more information about billing, see [NetApp Volumes pricing](https://cloud.google.com/netapp/volumes/pricing).

If you enable auto-tiering on a storage pool, billing depends on the pool's service level. For more information, see the following sections:

  * Flex Unified storage pools with auto-tiering

  * Premium and Extreme storage pools with auto-tiering




### Flex Unified storage pools with auto-tiering

For Flex Unified storage pools with auto-tiering enabled, cold data automatically moves to lower-cost storage. Capacity and billing for these pools depend on the following values:

  * **Hot tier size** : The capacity allocated for active data, which is billed at the hot tier rate.

  * **Pool size** : The total capacity of the pool, which includes both the hot tier size and the actual cold tier usage.


**Important:** The combined hot tier size and actual cold tier usage can't exceed your total pool size.

This billing model lets you optimize costs based on your workload:

  * You're billed for the full allocated hot tier size at the Flex Unified rate.

  * You're billed only for the actual cold tier usage.

  * You aren't billed for unused pool capacity.




For example, suppose that you create a 12 TiB pool with 1 TiB allocated to the hot tier, and over time you write 5 TiB of data to the pool. After 4.5 TiB of cold data moves to the cold tier, 0.5 TiB remains in the hot tier. In this scenario, you're billed as follows:

  * **Hot tier** : You're billed for the full 1 TiB hot tier allocation at the Flex Unified rate, even though only 0.5 TiB remains in the hot tier.

  * **Cold tier** : You're billed for the 4.5 TiB stored in the cold tier, plus any applicable network operation charges for moving the data.

  * **Unused capacity** : You aren't billed for the remaining 6.5 TiB of unused pool capacity.




### Premium and Extreme storage pools with auto-tiering

For Premium and Extreme storage pools with auto-tiering enabled, cold data automatically moves to lower-cost storage. Capacity and billing for these pools depend on the following values:

  * **Pool size** : The total allocated capacity of the pool.

  * **Cold tier size** : The capacity used by data in cold storage.

  * **Hot tier size** : The remaining pool capacity, which is automatically calculated as the pool size minus the cold tier size. The hot tier includes both active data and any unused pool capacity. You're billed for a minimum of 2 TiB of hot tier capacity for each pool.




You're billed for the full allocated pool capacity across the hot and cold tiers:

  * You're billed for the hot tier size (active data and unused pool capacity) at the Premium or Extreme rate.

  * You're billed for the cold tier size at the lower cold tier rate.




For example, suppose that you create a 12 TiB pool and write 5 TiB of data to the pool. After 4.5 TiB of cold data moves to the cold tier, 0.5 TiB of active data and 7 TiB of unused capacity remain in the hot tier. In this scenario, you're billed as follows:

  * **Hot tier** : You're billed for 7.5 TiB of hot tier capacity (12 TiB pool size minus 4.5 TiB cold tier size) at the Premium or Extreme rate.

  * **Cold tier** : You're billed for the 4.5 TiB stored in the cold tier at the lower cold tier rate, plus any applicable network operation charges for moving the data.




## Flex Unified: Default-mode versus ONTAP-mode

The Flex Unified service level offers two ways to provision storage pools:

  * Default-mode

  * ONTAP-mode




Unless otherwise specified, all information in this documentation applies to both modes.

### Default-mode

  * Default-mode is fully managed by Google. All resources are managed through Google Cloud console, Google Cloud CLI, and the Google Terraform provider, all of which operate through Google APIs, similar to Standard, Premium, and Extreme service levels.

  * Designed for users who prefer a simplified management and might have limited storage expertise.

  * Powered by Google Cloud NetApp ONTAP; however, only ONTAP features that are exposed through Google APIs are available. You can't access or modify ONTAP features that Google APIs don't support.




### ONTAP-mode

  * Provides advanced control of the ONTAP storage operating system, which lets you use most ONTAP features and settings for SVMs, volumes, and protocols.

  * Designed for users experienced with configuring and operating ONTAP storage systems.

  * Google manages only storage pools, networking, and CMEK, while ONTAP APIs control all other resources, such as volumes, protocols, and snapshots.

  * You can use the [Terraform provider for Google Cloud](https://registry.terraform.io/providers/hashicorp/google/latest/docs) to manage the pool and the [NetApp ONTAP](https://registry.terraform.io/providers/NetApp/netapp-ontap/latest/docs/guides/gcnv-ontap-mode) provider to manage resources within the pool. For more information, see [Use Terraform to manage ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/manage-ontap#use_terraform_to_manage_ontap-mode).

  * You are responsible for monitoring all resources except storage pools, for example, volumes.


**Note:** In ONTAP-mode, most features except storage pools and CMEK policies are managed outside of the Google Cloud console. For more information, see [About ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview#about_ontap-mode).

## Volumes

A [volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview) is a file system container in a storage pool that stores application, database, and user data.

You can create a volume's capacity using the available capacity in the storage pool and you can define and resize the capacity without disruption to any processes.

Storage pool settings apply to the volumes contained within them automatically.

## Snapshots and snapshot-based data management

NetApp Volumes helps you manage your data usage using [snapshot](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview) capabilities. This lets you take snapshots of your data in seconds without requiring additional storage space.

NetApp Volumes snapshots aren't a separate physical copy of your data. Instead, NetApp Volumes snapshots capture only the data that's been changed since the last snapshot. Note that when you overwrite all of your data, snapshots can consume significant volume capacity.

## Volume replication

You can protect your data through cross-location [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication), which asynchronously replicates a source volume in one location to a destination volume in a different location. This capability lets you use the other volume for critical application activity in case of a location-wide outage or disaster.

Volume replication moves only used data blocks during the initial transfer. During subsequent incremental transfers, only changed blocks transfer. Charges incur only for bytes transferred, which optimizes transfer times and lowers costs.

## Backups

A [backup](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups) is a copy of a volume stored independently from the volume in a backup vault. If a volume is unavailable or deleted, you can use backups to restore your data to a new volume. NetApp Volumes supports manual and scheduled volume backups.

The first backup of a volume contains all the volume's data. Subsequent backups capture only incremental changes which allows for fast incremental-forever backups and reduces the required capacity inside the backup vault.

## Active Directory integration

File sharing protocols like SMB (CIFS), NFSv3 with extended groups, and NFSv4.1, rely on external directory services to provide user identity information using security principals. NetApp Volumes relies on [Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad) for directory services. Active Directory provides services like LDAP servers for looking up the following objects:

  * Users

  * Groups

  * Machine accounts

  * DNS servers (for hostname resolution)

  * Kerberos servers (for authentication purposes)




## Data encryption

NetApp Volumes always encrypts your data at rest using volume-specific keys.

With [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek), volume-specific keys are wrapped using your keys stored in [Cloud Key Management Service](https://docs.cloud.google.com/kms/docs/key-management-service). This feature gives you greater control over the encryption keys you use and adds an additional layer of security by storing the keys on a system or in a location different from the data. NetApp Volumes supports Cloud Key Management Service capabilities such as hardware security modules, Encryption Key Management, and the full key management lifecycle of generate, use, rotate, and destroy.

## Auto-tiering

Users who have large amounts of inactive data can reduce their overall storage cost by using auto-tiering. Auto-tiering moves inactive data to a cheaper storage tier. This process is transparent for NFS and SMB clients, and the users have full visibility and accessibility to the data. Accessing cold data is slower than accessing hot data. For more information, see [Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

## SnapMirror

SnapMirror copies data from a primary source volume to a secondary destination volume. The destination can be on the same site or at a remote location. This copy is used for backup and disaster recovery to restore data if the primary system is unavailable.

SnapMirror supports asynchronous replication between an ONTAP-based source system and NetApp Volumes destination volumes. Volumes in Flex Unified storage pools can also serve as source volumes. Synchronous SnapMirror isn't supported.

After the first full copy, SnapMirror transfers only changed data, which reduces bandwidth and accelerates updates. It also supports storage features such as deduplication and compression.

SnapMirror lets you temporarily pause replication to test disaster recovery. After a disaster, SnapMirror can also reverse the replication direction to quickly resynchronize systems.

For more information, see [SnapMirror between ONTAP and Google Cloud NetApp Volumes](https://community.netapp.com/t5/Tech-ONTAP-Blogs/SnapMirror-between-ONTAP-and-Google-Cloud-NetApp-Volumes/ba-p/461292).

### Supported migration and replication methods

The following table describes the migration and replication methods that support source and destination volume types.

**Note:** All ONTAP refers to all ONTAP-based systems, including on-premises ONTAP, Amazon FSx for NetApp ONTAP (FSxN), and Cloud Volumes ONTAP (CVO).Source volume | Destination volume | Replication method  
---|---|---  
All ONTAP | Standard, Premium, Extreme, or Flex Unified Default-mode | [Volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview) or [External replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview)  
All ONTAP | Flex Unified ONTAP-mode | [SnapMirror](https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-disaster-recovery-concept.html)  
Flex Unified ONTAP-mode | Standard, Premium, Extreme, or Flex Unified Default-mode | [Volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview) or [External replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview)  
Flex Unified ONTAP-mode | All ONTAP | [SnapMirror](https://docs.netapp.com/us-en/ontap/data-protection/snapmirror-disaster-recovery-concept.html)  
Standard, Premium, or Extreme | Standard, Premium, or Extreme | [Volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication)  
Flex Unified Default-mode | Flex Unified Default-mode | [Volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication)  
Flex File | Flex File | [Volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication)  
  
## Volume migration

**Note:** For the Standard, Premium, and Extreme service levels, this feature is available in allow-listed General Availability (GA) and isn't open by default. To request access to this feature, contact [sales](https://cloud.google.com/contact).

The [volume migration](https://docs.cloud.google.com/netapp/volumes/docs/migrate/ontap/overview#about_volume_migration) feature lets you migrate ONTAP-based Flex volumes to NetApp Volumes using a SnapMirror-based migration. SnapMirror uses baseline and asynchronous incremental transfers to minimize the downtime required during transition of your workloads to NetApp Volumes.

This feature is intended for time-limited migrations. For ongoing replications between ONTAP systems and NetApp Volumes, see [External replication](https://docs.cloud.google.com/netapp/volumes/docs/discover/features#external_replication).

## External replication

**Note:** For Standard, Premium, and Extreme service levels, this feature is available in allow-listed General Availability (GA) and isn't open by default. To request access to this feature, contact [sales](https://cloud.google.com/contact).

[External replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/replicate-ontap/overview#about_external_replication) lets you set up volume replications between ONTAP-based source systems and NetApp Volumes using SnapMirror. SnapMirror uses baseline and asynchronous incremental transfers to keep source and destination volumes in sync. Like [volume replication](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-volume-replication), external replications can be stopped, resumed, and their replication direction reversed. This functionality lets you use NetApp Volumes as disaster recovery targets for on-premise ONTAP systems.

## FlexCache

**Note:** For Premium and Extreme service levels, this feature is available in allow-listed General Availability (GA) and isn't open by default. To request access to this feature, contact [sales](https://cloud.google.com/contact).

[FlexCache](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/cache-ontap-volumes/overview#about_flexcache) is a NetApp technology that optimizes data access by creating writable, sparse, and persistent copies of volumes in remote locations, bringing data closer to users. This feature improves performance for read-intensive workloads by reducing latency and increasing throughput. FlexCache also simplifies data management in hybrid cloud environments, enabling data caching in the cloud without requiring a complete data migration.

Additionally, NetApp Volumes lets you create cache volumes from origin volumes hosted on ONTAP-based source systems, including Flex Unified volumes in ONTAP-mode.

## ONTAP-mode S3 multiprotocol support

In ONTAP-mode, you can configure clusters to provide S3 access alongside NAS protocols such as NFS and SMB for applications that need to access data through both S3 and NAS protocols. Although file (NAS) and block (iSCSI) volumes can coexist in ONTAP-mode enabled storage pools, S3 multiprotocol support is available only for file volumes within those pools.

Standalone S3 buckets aren't supported. S3 access is available only as part of an ONTAP-mode configuration that also supports NAS protocols.

For more information about ONTAP-mode S3 multiprotocol, see [ONTAP S3 multiprotocol support](https://docs.netapp.com/us-en/ontap/s3-multiprotocol/index.html#how-s3-multiprotocol-support-works).

## NetApp Volumes integration with NetApp Console

NetApp Volumes is integrated with the NetApp Console agent. This integration is intended to simplify your storage management, offering you a unified platform that simplifies the handling of all your Cloud Storage requirements. For more information about the NetApp Console agent, see [NetApp Console](https://docs.netapp.com/us-en/storage-management-google-cloud-netapp-volumes/index.html).

## What's next

Read about [service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels) of Google Cloud NetApp Volumes.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
