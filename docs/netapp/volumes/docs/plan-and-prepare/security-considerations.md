---
url: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations/
title: Security considerations \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:56:03.258345+00:00
---

# Security considerations  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Security considerations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of security considerations for Google Cloud NetApp Volumes. These considerations include network protection, access control, and data encryption.

## Security considerations for networking

Google Cloud NetApp Volumes provides a protected architectural framework with the following isolated security layers:

  * **Project-level security** : the administrative security layer that administrators use to manage NetApp Volumes resources like storage pools or volumes using the Google Cloud console, Google Cloud SDK, or APIs. IAM roles and permissions guard this layer. For more information about project-level security, see [Set up IAM permissions](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/iam).

  * **Network-level security** : the network layer used to access data volumes with network-attached storage (NAS) protocols (Server Message Block (SMB) and Network File System (NFS)).

You can access data within volumes using NAS protocols through a Virtual Private Cloud (VPC) network. All data access to NetApp Volumes is possible only through your VPC, unless you explicitly use a third-party solution to replace VPC peering routing to your VPCs.

Within the VPC, you can limit access further with firewalls and through the setup of protocol-specific access control mechanisms.




## Firewall rules for volumes access

Firewall rules protect Google Cloud VPC. To enable access from clients to NetApp Volumes, you need to allow specific network traffic.

For more information about firewall rules for NFS, SMB, and iSCSI volumes access, see the following sections:

  * [Firewall rules for NFS volumes access](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#firewall_rules_for_nfs_volumes_access)

  * [Firewall rules for SMB volumes access](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-smb-clients#firewall_rules_for_smb_volumes_access)

  * [Firewall rules for iSCSI volumes access](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-iscsi-clients#firewall_rules_for_iscsi_volumes_access)




### Firewall rules for Active Directory access

NetApp Volumes needs access to the following ports on the DNS servers configured in your [Active Directory policy](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/create-ad-policy) to identify [Active Directory domain controllers](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#active_directory_domain_controllers). NetApp Volumes uses DNS lookups for Active Directory domain controller discovery.

  * `ICMPV4`

  * `DNS 53 TCP`

  * `DNS 53 UDP`




Open the following ports on all your Active Directory domain controllers to traffic originating from the CIDR range for NetApp Volumes:

  * `ICMPV4`

  * `LDAP 389 TCP`

  * `SMB over IP 445 TCP`

  * `Secure LDAP 636 TCP`

  * `Kerberos 464 TCP`

  * `Kerberos 464 UDP`

  * `Kerberos 88 TCP`

  * `Kerberos 88 UDP`




To specify a source range for your firewalls, use the full CIDR range that you provided when configuring private service access. For more information, see [Configure private services access](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access).

**Note:** Active Directory DNS servers also serve as domain controllers which require two sets of rules to be applied.

#### Attach firewall tag to Active Directory servers

Use the following instructions to attach the firewall tag to your Active Directory servers.

  1. Attach the firewall rule to your Active Directory DNS servers:
         
         gcloud compute firewall-rules create netappvolumes-to-dns \
           --allow=icmp,TCP:53,UDP:53 \
           --direction=ingress \
           --target-tags=allow-netappvolumes-to-dns \
           --source-ranges=NETAPP_VOLUMES_CIDR \
           --network=VPC_NAME

  2. Attach the firewall rule to your Active Directory domain controllers:
         
         gcloud compute firewall-rules create netappvolumes-to-activedirectory \
           --allow=icmp,TCP:88,UDP:88,TCP:389,TCP:445,TCP:464,UDP:464,TCP:636 \
           --direction=ingress \
           --target-tags=allow-netappvolumes-to-activedirectory \
           --source-ranges=NETAPP_VOLUMES_CIDR \
           --network=VPC_NAME

Replace the following information:

     * `NETAPP_VOLUMES_CIDR`: The NetApp Volumes CIDR

     * `VPC_NAME`: The name of the VPC

  3. Attach the following tag to your DNS servers:
         
         allow-netappvolumes-to-dns

  4. Attach the following tag to your domain controllers:
         
         allow-netappvolumes-to-activedirectory




## Volume access controls for NFS protocols

NetApp Volumes guards access by NFS protocols with a single export policy with up to 20 export rules. Export rules are comma-separated lists of IPv4 addresses and IPv4 CIDRs that specify which clients have permission to mount volumes. NetApp Volumes evaluates export rules in sequential order and stops after the first match. We recommend ordering export rules from most specific to most generic for best results. For more information about export rules, see [Volume access control using export policies](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#volume_access_control_using_export_policies).

## Volume access controls for SMB protocol

SMB uses share-level permissions to guard volume access and require authentication against Active Directory. These permissions let you control who has access to shares over the network.

Volumes are created with **Everyone** and **Full Control** share-level permissions. You can modify share-level permissions using Windows console or Windows CLI.

Use the following instructions to modify SMB share-level permissions using the Windows console or Windows CLI:

### Windows console

  1. Right-click **Windows start** icon and select **Computer Management**.

  2. After the **Computer Management** console opens, click **Action** > **Connect to another computer**.

  3. In the **Select Computer** dialog, enter the netbios name of your SMB share and click **OK**.

  4. Once you are connected to the file share, go to **System Tools** > **Shared Folders** > **Shares** to look up your share.

  5. Double-click **Share Name** and select the **Share Permissions** tab to control the permissions of the share.




### Windows CLI

  1. Open a Windows command line.

  2. Connect to the file share.
         
         fsmgmt.msc /computer=<netbios_name_of_share>

  3. Once you are connected to the file share, go to **System Tools** > **Shared Folders** > **Shares** to look up your share.

  4. Double-click **Share Name** and select the **Share Permissions** tab to control the permissions of the share.




## Volume access controls for iSCSI protocol

Access to iSCSI NetApp Volumes is managed using [Host groups](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/host-groups/overview#about_host_groups), which are regional objects that contain one or more iSCSI initiator IQNs. An iSCSI initiator is typically a client system or server that connects to storage targets over a network using the iSCSI protocol.

When an iSCSI volume is created, it is attached to a host group. This relationship grants access of the iSCSI volume to the iSCSI clients (initiators) within that host group, which allows them to discover the LUN and consume the storage resource. Only initiators that are members of the host group can view and connect to the assigned iSCSI volume.

The following are the key characteristics of host groups and iSCSI access:

  * **Visibility control** : the host groups restrict which iSCSI clients can view and access specific volumes. If an initiator isn't part of a host group, it can't discover or connect to the LUN.

  * **Regional scope** : the host groups are regional objects, with their configuration and membership limited to a specific region within your Google Cloud environment.

  * **Client-side security** : while host groups control volume visibility, the iSCSI client administrator is responsible for implementing user-level access controls on the client system. This includes managing who can mount the iSCSI volume and who can access the file system created on it.




### Host-based file system permissions

Once a LUN is mapped to a host, the host's operating system is responsible for managing file system permissions and access controls. For example, Windows hosts use NTFS permissions and ACLs, while Linux and UNIX hosts use standard UNIX file permissions, and optionally, ACLs to protect files and directories.

This two-layered security approach helps ensure that only authorized hosts can access storage at the block level, while the host operating system manages file-level security according to organizational policies.

## File access control

The following sections provide details on NetApp Volumes file-level access control.

### Volume security style

NetApp Volumes offers two security styles for volumes, UNIX and NTFS, to accommodate the different permission sets of Linux and Windows platforms.

  * **UNIX** : volumes configured with the UNIX security style use UNIX mode bits and NFSv4 ACLs to control file access.

  * **NTFS** : volumes configured with NTFS security style use NTFS ACLs to control file access.




The security style of the volume depends on the protocol choice for the volume:

Protocol type | Volume security style  
---|---  
NFSv3 | UNIX  
NFSv4.1 | UNIX  
Both (NFSv3 and NFSv4.1) | UNIX  
SMB | NTFS  
Dual (SMB and NFSv3) | UNIX or NTFS  
Dual (SMB and NFSv4.1) | UNIX or NTFS  
  
For dual protocols, you can only choose security style during volume creation.

### NFS file-level access control for UNIX-style volumes

After a client mounts a volume successfully, NetApp Volumes checks access permissions to files and directories using the standard UNIX permission model called mode bits. You can set and modify permissions using `chmod`.

NFSv4.1 volumes can also use NFSv4 access control lists (ACLs). If a file or directory has both mode bits and an NFSv4 ACL, the ACL is used for permission checking. The same applies to volumes which use both NFSv3 and NFSv4.1 protocol types. You can set and modify NFSv4 ACLs using `nfs4_getfacl` and `nfs4_setfacl`.

When you create a new UNIX-style volume, the `root:root` has ownership of root inode and `0770` permissions. Due to this ownership and permission setting, a non-root user gets a `permission denied` error while accessing the volume after mounting. To enable access to the volume for non-root users, a root user must change the ownership of the root inode using `chown` and modify the file permissions using `chmod`.

### SMB file access control for NTFS-style volumes

For NTFS-style volumes, we recommend that you use an NTFS permission model. Every file and directory has an NTFS ACL which you can modify using File Explorer, the `icacls` command line tool, or PowerShell. In the NTFS permission model, new files and folders inherit permissions from their parent folder.

### Multi-protocol user mapping

For dual-protocol volumes, clients can use NFS and SMB to access the same data. A volume is configured by setting the security style of the volume to either have UNIX or NTFS permissions.

When you create a dual-protocol SMB and NFS volume, we strongly recommend that Active Directory contains a default user. The default user is used when an NFS client sends an NFS call with a user ID that isn't available in Active Directory. NetApp Volumes then tries to look up a user called `pcuser`, which acts as a default UNIX user. If that user isn't found, access is denied to the NFS call.

We recommend that you create a default user in Active Directory with the following attributes:

  * `uid` = `pcuser`

  * `uidnumber` = `65534`

  * `cn` = `pcuser`

  * `gidNumber` = `65534`

  * `objectClass` = `user`




Depending on the protocol used by the client (NFS or SMB) and the security style of the volume (UNIX or NTFS), NetApp Volumes can directly check access permissions of the user or requires mapping the user to the other platform's identity first.

Access protocol | Security style | Identity used by protocol | Required mapping  
---|---|---|---  
NFSv3 | UNIX | User ID and group ID | N/A  
NFSv3 | NTFS | User ID and group ID | User ID to username to security identifier  
SMB | UNIX | Security identifier | Security identifier to username to user ID  
SMB | NTFS | Security Identifier | N/A  
  
When mapping is required, NetApp Volumes relies on data stored in Active Directory LDAP. For more information, see [Active Directory use cases](https://docs.cloud.google.com/netapp/volumes/docs/configure-and-use/active-directory/about-ad#use_cases_for_active_directory).

### Multi-protocol user mapping scenario: SMB access to a UNIX volume

Scientist Charlie E. (charliee) wants to access a NetApp Volumes volume using SMB from a Windows client. Because the volume contains machine generated results provided by a Linux compute cluster, the volume is configured to store UNIX permissions.

The Windows client sends an SMB call to the volume. The SMB call contains the user identity as a security identifier. The security identifier isn't comparable against the user ID and group ID file permissions and requires mapping.

To complete the required mapping, NetApp Volumes takes the following steps:

  1. NetApp Volumes asks Active Directory to resolve the security identifier to a username, for example, `S-1-5-21-2761044393-2226150802-3019316526-1224` to `charliee`.

  2. NetApp Volumes asks Active Directory to return the user ID and group ID for `charliee`.

  3. NetApp Volumes checks access against the ownership user ID and group ID of the file using the returned user ID and group ID.




### Multi-protocol user mapping scenario: NFS access to an NTFS volume

Engineer Amal L. needs to access some data on a volume from a Linux client using NFS. Because the volume is mainly used to store Windows data, it is configured with the NTFS security style.

The Linux client sends an NFS call to NetApp Volumes. The NFS call contains user ID and group ID identifiers which can't be matched to a security identifier without mapping.

To complete the required mapping, NetApp Volumes asks Active Directory for the username of the user ID and to return the security identifier for the username, and then checks access against the owner security identifier of the accessed file using the returned security identifier.

## Encryption in Transit

Encryption in transit protects data from interception over a network. Traffic for volume replication, integrated backup, and volume migration is encrypted by default using TLS 1.2. For NFS and SMB traffic, you can configure protocol-specific encryption settings for added protection.

### NFS

For NFS volumes, use NFSv4.1 with Kerberos krb5p encryption enabled for maximum security.

### SMB

For SMB volumes, enable AES encryption in your Active Directory policy and SMB encryption on your volume for maximum security.

### Volume replication

NetApp Volumes can replicate volumes across Google Cloud regions to provide data protection. Since the traffic resides in the Google Cloud, Google's network infrastructure protects the transfer process, which has limited access to prevent unauthorized interception. Additionally, the replication traffic is encrypted using FIPS 140-2 compliant TLS 1.2 standards.

### Integrated backup

An integrated backup creates backups of NetApp Volumes within the service. The backup traffic stays within Google's network infrastructure and is encrypted using the FIPS 140-2 compliant TLS 1.2 standard. The backup vaults can store these backups using Google-managed encryption key by default or customer-managed encryption key (CMEK) for added security.

### Volume migration

Volume migration sends data from the source ONTAP or Cloud Volumes ONTAP system to NetApp Volumes. The communication between the source system and NetApp Volumes is encrypted using FIPS 140-2 compliant TLS 1.2 standards.

NetApp Volumes starts the migration and uses the following protocols and ports:

  * ICMP

  * 10000/TCP

  * 11104/TCP

  * 11105/TCP




Make sure that any firewall between the intercluster logical interface (LIF) of your ONTAP system and the migration IP address of NetApp Volumes allows these ports.

## What's next

[Secure NetApp Volumes with a service perimeter](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/service-perimeter).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
