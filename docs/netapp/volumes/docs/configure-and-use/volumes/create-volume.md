---
url: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume/
title: Create a volume \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:44:29.551061+00:00
---

# Create a volume  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/create-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Create a volume Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a [volume](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/overview).

You can also create a new volume by cloning an existing volume. For more information, see [Create a volume clone](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume-clones#create_a_volume_clone).

## Before you begin

Review the following prerequisites before you create a volume:

  * You must have an existing storage pool connected to the network you intend to share the volumes to. For more information, see [Storage pools overview](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/overview).

  * The pool you intend to share volumes to must have enough available capacity to host the volumes.

  * If you intend to use Active Directory, make sure the correct Active Directory policy is attached to the storage pool.

  * If you want to encrypt your volume using a customer-managed encryption key (CMEK), make sure that the pool has a CMEK policy.

  * If you require LDAP access, make sure you enable the LDAP option on the pool.

  * If the existing pool doesn't meet your requirements, create a new pool.




## Capacity adjustments and constraints

  * The minimum and maximum size of a volume depends on the service level. For more information, see the [volume capacity](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels) limits.

  * The capacity of a volume can be increased or decreased in 1 GiB increments between its capacity limits.

  * Volume capacities are subject to the remaining available capacity in the hosting storage pool. If you run out of space, increase the capacity of the storage pool.

  * The service level of the pool has a significant impact on the performance you can expect from your volume. To determine the appropriate service level for your performance objectives, see [Volume performance sizing](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/volume-performance-sizing).




## Volume and share naming rules

Volume and share names can't contain spaces or special characters other than hyphens and underscores.

Use the following separator characters for your volumes and shares:

  * Flex Unified volumes: use only underscores, not hyphens, for ONTAP compatibility

  * Standard, Premium, Extreme, and Flex File volumes: use only hyphens, not underscores

  * Shares and exports: use hyphens and underscores




## Create a volume

Use the following instructions to create a volume using the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click **Create**.

  4. In the **Storage pool details** section, complete the following steps:

     1. Click **Select storage pool**.

     2. Choose a storage pool to host the volume.

The volume you create inherits the settings of the storage pool you select.

     3. Click **Select**.

If the storage pools in the list don't have the settings you want, click [Create new storage pool](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/storage-pools/create-storage-pool).

  5. In the **Volume details** section, complete the following steps:

     1. Enter a name for the volume in the **Volume name** field. The name must be unique for each project within a location.

     2. Optional: enter a description in the **Description** field for the volume.




### For storage pools with Flex (File type), Standard, Premium, or Extreme service level

Complete the following steps:

  1. Enter the share name of the volume in the **Share name** field. The name must be unique for each project within a location.

For NFS exports, the share name corresponds to the export path.

  2. Enter the capacity of the volume in the **Capacity** field.

The minimum and maximum size of a volume depends on the service level. For more information about the limits, see [Service levels](https://docs.cloud.google.com/netapp/volumes/docs/discover/service-levels).

For more information about volume capacities, see Capacity adjustments and constraints.

  3. Optional: if the selected storage pool allows auto-tiering, complete the following steps:

     1. Click **Enable auto-tiering** if you want to enable auto-tiering for the volume.

     2. Specify a **Cooling threshold** between 2 to 183 days for Premium, Extreme, or custom-performance Flex zonal pools. The default cooling threshold value is 31 days.

     3. Volumes in Flex Unified and Flex File custom-performance pools offer the option to enable or disable the **Hot tier bypass**. For more information, see [Manage auto-tiering](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-auto-tiering).

  4. Click the **Protocol(s)** drop-down list, and select the protocol you want to use. Protocol options depend on protocol choice.

**Note:** For the Flex File service level, you can't create volumes with dual-protocol, for example, NFS and SMB.

Some protocol choices require an Active Directory. For more information, see [Use cases for using Active Directory](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#use_cases_for_active_directory).

|  Protocol types  
---|---  
Protocol options | NFSv3 | NFSv4.1 | Both (NFSv3 and NFSv4.1) | SMB | Dual-protocol  
**Enable Kerberos:** choose between Kerberos with or without signing and NFS encryption in transit in the volumes export rules. |  | check |  |  |   
**Security style:** choose the permission model (NTFS or UNIX) for the volume. For more information, see [Multi-protocol user mapping.](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#multi-protocol_user_mapping) |  |  |  |  | check  
**Enable SMB encryption:** enable SMB3 transport encryption.   
  
When enabled, clients that don't support SMB3 encryption can't access the share. |  |  |  | check | check  
**Hide SMB share:** disable discoverability for the share using network browsing. |  |  |  | check | check  
**Enable access-based enumeration:** access-based enumeration hides files and folders that users don't have permissions to access. |  |  |  | check | check  
**Enable continuous availability share support for SQL Server, FSLogix** : enable this option only for SQL Server and FSLogix workloads that require continuous availability (CA). |  |  |  | check |   
  5. Click **Block volume from deletion when clients are connected** in the **Configuration for selected protocol(s)** for volumes used as GCVE datastores. This setting is permanent.

  6. Specify the Export Policy for NFSv3, NFSv4.1, and dual-protocol types to allow client access. Settings depend on your protocol choices. Export policy definition is only required for any protocol combination that contains NFSv3 or v4.1. You can't define export policies for SMB volumes.

If required, you can add up to 20 additional export rules. For more information, see [NFS volume access control through export rules](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#volume_access_controls_for_nfs_protocols).

     1. Click to expand **Export rules**.

     2. Click **Add rule**.

     3. In **Allowed Clients** , specify the IPv4 addresses of the clients the export rule applies to. Enter a comma-separated list of IP addresses or CIDRs with a maximum length of 4,096 characters.

     4. In **Access** , select **Read & Write** or **Read Only**.

     5. In **Root Access (no_root_squash)** , Select **On** or **Off**.

An important security mechanism of NFS is to map the root user, `UID 0`, to nobody, `UID 65534`. We recommend that you disable root access for all of your clients, except for a few management hosts. Create a dedicated export rule with root access enabled for the management hosts.

     6. Apply protocol-specific settings based on your protocol type:

        * **NFSv3** , **NFSv4.1** , **without Kerberos** , and **dual-protocol** : Specify if the rule is **Read & Write** or **Read-Only**.

        * **NFSv4.1 with Kerberos enabled** : Specify if access is **not enabled** , **read only** , or **read & write** for `kerberos5` (krb5), `kerberos5i` (krb5i), and `kerberos5p` (krb5p).

        * **Both** (NFSv3 or NFSv4.1): Specify if the rule applies to NFSv3 only, NFSv4.1 only, or both.

     7. Click **Done**.




### For storage pools of the Flex service level of the Unified type

Complete the following steps:

  1. Enter the capacity of the volume in the **Capacity** field.

  2. In the **Protocol(s) configuration** section, select the **Operating system** from the drop-down list. This specifies the operating system to which the volume will be attached.

  3. Click **Block volume from deletion when clients are connected** in the **Configuration for selected protocol(s)** for volumes used as GCVE datastores. This setting is permanent.

  4. In the **Host groups** section, you can either select an existing host group or click **Add a host group** to create a new one. This initiates the host group creation workflow.




### Optional settings

  1. Optional: define a snapshot schedule:

     1. Select **Make snapshot directory visible** to enable file system access to snapshot versions by clients. For more information, see [NetApp Volumes volume snapshots overview](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volume-snapshots/overview).

     2. Select **Allow scheduled snapshots** to configure the volume to automatically take snapshots. You can specify the number of snapshots to keep at hourly, daily, weekly, and monthly snapshot intervals. Times are specified in UTC. If you reach the maximum number of snapshots, the oldest snapshot deletes.

     3. Review your snapshot selections.

  2. Optional: define a backup schedule:

     1. Select **Allow scheduled backups** to configure automatic daily, weekly, or monthly backups.

     2. Select or create a [backup policy](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#backup_policies).

     3. Select or create a [backup vault](https://docs.cloud.google.com/netapp/volumes/docs/protect-data/about-backups#backup_vaults).

  3. Optional: in the **Labels** section, click **Add label** to enter relevant labels for reporting and querying purposes.

  4. Click **Create**.




The new volume is listed on the **Volumes** page. Volumes take up to 20 minutes to create the first volume that appears in the **Creating** state. Additional volumes generate within a few seconds to a few minutes.

### gcloud

### Create a volume

Create a volume using the following command:
    
    
    gcloud netapp volumes create VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --storage-pool=STORAGE_POOL \
      --capacity=CAPACITY \
      --protocols=PROTOCOLS \
      --share-name=SHARE_NAME

Replace the following information:

  * `VOLUME_NAME`: the name of the volume. This name must be unique per location.

  * `PROJECT_ID`: the name of the project to create the volume in.

  * `LOCATION`: the location for the volume.

  * `STORAGE_POOL`: the storage pool to create the volume in.

  * `CAPACITY`: the capacity of the volume. It defines the capacity that NAS clients see.

  * `PROTOCOLS`: the NAS protocols the volume is exported with.

The following are the valid protocol choices:

    * `smb`
    * `nfsv3`
    * `nfsv4`
    * `nfsv3,nfsv4`
    * `nfsv3,smb` (not applicable for the Flex File volumes)
    * `nfsv4,smb` (not applicable for the Flex File volumes)

Depending on the protocol type you choose, we recommend that you add the protocol-specific parameters, such as `export-policy` or `smb-settings`.

  * `SHARE_NAME`: the NFS export path or SMB share name of the volume.




### Create a Flex Unified large capacity volume

Create a Flex Unified large capacity volume with the default constituent count:
    
    
    gcloud netapp volumes create VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --storage-pool=STORAGE_POOL \
      --capacity=CAPACITY \
      --protocols=PROTOCOLS \
      --share-name=SHARE_NAME \
      --large-capacity-config

Replace the following information:

  * `VOLUME_NAME`: the name of the volume. This name must be unique for each location.

  * `PROJECT_ID`: the name of the project to create the volume in.

  * `LOCATION`: the location for the volume.

  * `STORAGE_POOL`: the storage pool to create the volume in.

  * `CAPACITY`: the capacity of the volume. It defines the capacity that NAS clients see.

  * `PROTOCOLS`: the NAS protocols the volume is exported with.

The following are the valid protocol choices:

    * `smb`
    * `nfsv3`
    * `nfsv4`
    * `nfsv3,nfsv4`
    * `nfsv3,smb`
    * `nfsv4,smb`

Depending on the protocol type you choose, we recommend that you add the protocol-specific parameters, such as `export-policy` or `smb-settings`.

  * `SHARE_NAME`: the NFS export path or SMB share name of the volume.

  * `CONSTITUENT_COUNT`: Optional: the number of constituents for a large capacity volume.

To create a large capacity volume with a specific constituent count, replace the `--large-capacity-config` parameter with `--large-capacity-config=constituent-count=CONSTITUENT_COUNT`.




### Create an iSCSI volume

Create an iSCSI volume in the Flex service level of the **Unified** type pool:
    
    
    gcloud netapp volumes create VOLUME_NAME \
      --project=PROJECT_ID \
      --location=LOCATION \
      --storage-pool=STORAGE_POOL \
      --capacity=CAPACITY \
      --protocols=ISCSI \
      --block-devices=name=LUN_NAME,host-groups=HOST_GROUP_NAME,os-type=OS_TYPE \
      --snapshot-directory=false

Replace the following information:

  * `VOLUME_NAME`: the name of the volume. This name must be unique per location.

  * `PROJECT_ID`: the name of the project to create the volume in.

  * `LOCATION`: the location for the volume.

  * `STORAGE_POOL`: the storage pool to create the volume in.

  * `CAPACITY`: the capacity of the volume. It defines the capacity that iSCSI clients see.

  * `LUN_NAME`: Optional: if a name is provided, the LUN will be assigned that name. Otherwise, the LUN will be named as `lun_<VOLUME_NAME>`.

  * `HOST_GROUP_NAME`: the name of the host group to which the volume needs to be attached. Multiple host groups can be specified with a # sign separating each host group.

  * `OS_TYPE`: the operating system of the hosts. The supported values include `LINUX`, `WINDOWS`, and `ESXI`.




For more information about additional optional flags like enabling large capacity volumes, delete protection for volumes, and auto-tiering, see [Google Cloud SDK documentation on volume creation](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/create).

### ONTAP-mode

Identify the required ONTAP commands in the [ONTAP documentation](https://docs.netapp.com/us-en/ontap/).

Complete the following steps:

  1. [Create a volume](https://docs.netapp.com/us-en/ontap/volumes/create-volume-task.html) and mount it into the namespace. To enable tiering on enabled pools, see the [tiering-policy](https://docs.netapp.com/us-en/ontap/fabricpool/create-volume-task.html).

  2. For SMB volumes, [create a SMB share](https://docs.netapp.com/us-en/ontap/smb-config/create-share-task.html) and set share-level permissions.

  3. For NFS volumes, create an export policy.




After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## What's next

[Manage volumes](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/volumes/manage-volume).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
