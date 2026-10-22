---
url: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients/
title: Connect NFS clients \u00a0|\u00a0 NetApp Volumes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:17:56.969020+00:00
---

# Connect NFS clients  |  NetApp Volumes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ NetApp Volumes ](https://docs.cloud.google.com/netapp/volumes/docs)
  * [ Guides ](https://docs.cloud.google.com/netapp/volumes/docs/discover/overview)



Send feedback 

#  Connect NFS clients Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to connect NFS clients.

## Before you begin

If you use a firewall to control network traffic and want to allow NFS traffic, see [Firewall rules for NFS volumes access](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#firewall_rules_for_nfs_volumes_access).

Install NFS client tools based on your Linux distribution type to prepare your client:

### RedHat

Run the following command:
    
    
    sudo yum install -y nfs-utils

### SuSe

Run the following command:
    
    
    sudo yum install -y nfs-utils

### Debian

Run the following command:
    
    
    sudo apt-get install nfs-common

### Ubuntu

Run the following command:
    
    
    sudo apt-get install nfs-common

## Volume access control using export policies

Volume access control in NFSv3 and NFSv4.1 is based on the client's IP address. The volume's export policy contains up to 20 export rules. Each rule is a comma-separated list of IPs or network CIDRs which define **Allowed Clients** enabled to mount the volume. A rule also defines the type of access the clients have such as **Read & Write** or **Read Only**.

Use the following tabs to review policies based on NFS versions:

### NFS without Kerberos

All NFS versions without Kerberos use the `AUTH_SYS` security flavor. In this mode, you must tightly manage the export rules to allow only clients you trust and which can ensure user ID and group ID integrity.

As a security measure, NFS servers automatically map NFS calls with `UID=0` (root) to `UID=65534` (anonymous), which has limited permissions on the file system. For more information, see User ID squashing.

### NFSv4.1 with Kerberos

NFSv4.1 with Kerberos use export policies and additional authentication using Kerberos to access volumes. You can configure export rules to apply for the following:

  * Kerberos only (`krb5`)

  * Kerberos signing (`krb5i`)

  * Kerberos privacy (`krb5p`)




### Best practices for export policies

We recommend the following best practices for export policies:

  * Order the export rules from most specific to least specific.

  * Export only to the trusted clients, such as specific clients or CIDRs with the trusted clients.

  * Limit the root access to a small group of trusted administration clients.


Rule | Allowed clients | Access | Root access | Description  
---|---|---|---|---  
1 | 10.10.5.3,   
10.10.5.9 | Read & Write | On | Administration clients. Root user stays root and can manage   
all the file permissions.  
2 | 10.10.5.0/24 | Read & Write | Off | All other clients from 10.10.5.0/24 network are allowed to mount,   
but root access gets mapped to nobody.  
3 | 10.10.6.0/24 | Read-Only | Off | Another network is allowed to read data from the volume, but   
no writes.  
  
After a client mounts a volume, the file level access determines what a user is allowed to do. For more information, see [NFS file-level access control for UNIX-style volumes](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/security-considerations#nfs_file-level_access_control_for_unix-style_volumes).

### Manage export policies

Use the following instructions to update a volume's export policy using the Google Cloud CLI.

### gcloud

#### Update a volume with one export policy

Update a volume with one export policy rule:
    
    
    gcloud netapp volumes update VOLUME_ID \
      --project=PROJECT_ID \
      --location=LOCATION \
      --export-policy=access-type=ACCESS_TYPE,allowed-clients=ALLOWED_CLIENTS_IP_ADDRESSES,has-root-access=TRUE_OR_FALSE,nfsv3=NFSV3,nfsv4=NFSV4

Replace the following information:

  * `VOLUME_ID`: the ID of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.

  * `ACCESS_TYPE`: the access type must be either one of `READ_WRITE`, `READ_ONLY`, or `READ_NONE`.

  * `ALLOWED_CLIENTS_IP_ADDRESSES`: a list of allowed clients IP addresses or ranges separated by comma.

  * `NFSV3`: set to `true` or `false` to apply this rule to NFSv3.

  * `NFSV4`: set to `true` or `false` to apply this rule to NFSv4.




#### Add multiple export policy rules

To add multiple export rules, repeat the `export-policy` parameter block. Each `export-policy` parameter block consists of multiple key-value pairs in the following format:
    
    
    --export-policy=KEY1=VALUE1,KEY2=VALUE2,KEY3=VALUE3...
    

**Example: Using a colon and comma as a separator**

If you specify multiple IP addresses or CIDRs for `allowed-clients`, Google Cloud CLI might not parse values correctly because the `--export-policy` flag uses commas as the default separator between different keys such as `access-type` and `nfsv3`. If a value, such as `allowed-clients`, also contains commas, the parser can't distinguish between a new key-value pair and an additional IP address within the `allowed-clients` list. To distinguish these commas, configure Google Cloud CLI to use a different parameter separator with [Google Cloud CLI escaping](https://docs.cloud.google.com/sdk/gcloud/reference/topic/escaping).

The following command shows the example from Best practices for export policies. The first rule uses a colon as the parameter separator to correctly parse the comma-separated `allowed-clients` list. The second and third rules use the default comma as separator.
    
    
    gcloud netapp volumes update my_volume --location=us-east4 \
    --export-policy=^:^access-type=READ_WRITE:allowed-clients="10.10.5.3,10.10.5.9":nfsv3=true:nfsv4=true:has-root-access=true \
    --export-policy=access-type=READ_WRITE,allowed-clients=10.0.5.0/24,nfsv3=true,has-root-access=false \
    --export-policy=access-type=READ_ONLY,allowed-clients=10.0.6.0/24,nfsv3=true,has-root-access=false
    

**Example: Using the`squash-mode` as a parameter**

The following example uses the alternative `squash-mode` parameter to create a `NO_ROOT_SQUASH` rule for administrator hosts and an `ALL_SQUASH` rule for a CIDR range.
    
    
    gcloud netapp volumes update my_volume --location=us-east4 \
    --export-policy=^:^allowed-clients="10.10.5.3,10.10.5.9":nfsv3=true:access-type=READ_WRITE:squash-mode=NO_ROOT_SQUASH \
    --export-policy=allowed-clients=10.0.2.0/24,nfsv3=true,access-type=READ_WRITE,squash-mode=ALL_SQUASH,anon-uid=2000
    

For more information about additional optional flags, see [Google Cloud SDK for volumes export policy](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes/update#--export-policy).

## User ID squashing

NFS export policies provide controls for [user and group ID squashing](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#user_and_group_id_squashing), which lets you remap user and group IDs to an anonymous user ID for security purposes.

### Root squashing

NFS servers improve security by remapping the root user (`UID=0`) to nobody (`UID=65534`), which makes root an unprivileged user for file access on the volume. This feature is known as _root squashing_. The option to disable it and retain root's privileges is called `no_root_squash` on NFS servers.

By default, volumes without a defined export policy are inaccessible to client IP addresses. When you create an export policy rule in the Google Cloud console, the default settings include **Read & Write** access and **root squash**. The Google Cloud API, Google Cloud CLI, and Terraform previously supported control over root squashing using the `has-root-access` parameter. While `has-root-access` is still accepted, it has been replaced by the `squash-mode` parameter.

As a best practice, create a dedicated export rule that enables root access for your trusted administrator hosts and disables root access for other clients. Place this rule first, before more generic rules.

### User and group ID squashing

The `squash-mode` parameter provides control over squashing both user and group IDs to an anonymous UID, which can be useful for public SFTP dropbox directories. This parameter also replaces the `has-root-access` parameter and is supported across the API, Google Cloud CLI, and Terraform.

The `squash-mode` parameter accepts the following values:

  * `no-root-squash`: in this mode, the root user remains root and doesn't get remapped to nobody (`UID=65534`).

  * `root-squash`: this setting remaps the root user to nobody.

  * `all-squash`: this option provides anonymous access for all users, including root. All users are remapped to the UID and GID specified by the `anon-uid` parameter. When using `all-squash`, you must also specify `anon-uid`, and set `access-type` to `READ_WRITE`.




### Considerations

Consider the following for export policy rules with `squash mode`:

  * An export policy supports only one `all-squash` rule.

  * When `all-squash` is enabled, the root user is squashed to anonymous. This can be overridden by a higher priority rule that uses `no-root-squash`.

  * Volume replication isn't supported for volumes with a `squash-mode` style export policy rule.

  * For the Flex File service level, `all-squash` doesn't change ownership of the volume's root inode automatically. To achieve this, add a `no-root-squash` export rule, allowing the root user to use `chown` to change ownership of the root inode to the required UID.

  * The `has-root-access` parameter is supported. Use either `has-root-access` or `squash-mode`; don't use both parameters simultaneously.




## Mount instructions for NFS clients

Use the following instructions to get mount instructions for NFS clients using either the Google Cloud console or Google Cloud CLI or ONTAP-mode.

### Console

  1. Go to the **NetApp Volumes** page in the Google Cloud console.

[Go to NetApp Volumes](https://console.cloud.google.com/netapp/volumes)

  2. Click **Volumes**.

  3. Click more_vert **Show more**.

  4. Select **Mount instructions**.

  5. Follow the mount instructions shown in the Google Cloud console.

  6. Start with the mount commands and options in the console. For more information about performance tuning, kernel concurrency, mount options, and read-ahead, see [Optimize Linux NFS clients for NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

**NFSv3 only** : if your application doesn't use locks or you didn't configure your clients to enable NSM communication, we recommend that you add the `nolock` mount option.




### gcloud

Look up the mount instructions for a volume:
    
    
     gcloud netapp volumes describe VOLUME_NAME \
        --project=PROJECT_ID \
        --location=LOCATION \
        --format="value(mountOptions.instructions)"

Replace the following information:

  * `VOLUME_NAME`: the name of the volume.

  * `PROJECT_ID`: the name of the project the volume is in.

  * `LOCATION`: the location of the volume.




For more information about additional optional flags, see [Google Cloud SDK documentation on volumes](https://docs.cloud.google.com/sdk/gcloud/reference/netapp/volumes).

### ONTAP-mode

Use the following steps to identify your volume's hostname or IP address, and the export path:

  1. [Look up all network interfaces](https://docs.netapp.com/us-en/ontap-cli//network-interface-show.html#description) for the `data_cifs` service.

  2. Determine the export path, which corresponds to the [junction path](https://docs.netapp.com/us-en/ontap-cli//volume-show.html#parameters) you specified for your volume.

  3. Create the mount path in the format `IP:junction-path`, and add any required mount options.




After you identify the required commands, see [ONTAP-mode](https://docs.cloud.google.com/netapp/volumes/docs/ontap/overview) for instructions about how to submit ONTAP commands to the storage pool.

## Additional NFSv4.1 instructions

When you enable NFSv4.1 for volumes of the Flex Unified, Standard, Premium, and Extreme service levels, NFSv4.2 is automatically enabled for these volumes. The Linux mount command always mounts the highest available NFS version, unless you specify the version to mount. If you want to mount with NFSv4.1, use the `-o vers=4.1` parameter in your mount command.

In NFSv3, users and groups are identified by user IDs (UID) and group IDs (GID) sent over the NFSv3 protocol. Its important to make sure that the same UID and GID represent the same user and group on all clients accessing the volume. NFSv4 removed the need for explicit UID and GID mapping by using security identifiers. Security identifiers are strings formatted as `<username|groupname>@<full_qualified_domain>`. An example of a security identifier is [bob@example.com](mailto:bob@example.com). The client needs to translate the UIDs and GIDs used internally into a security identifier before sending an NFSv4 request to the server. The server needs to translate the security identifiers into UIDs and GIDs for an incoming request and the other way around for its response. The advantage of using translations is that every client and the server can use different internal UIDs and GIDs. However, the disadvantage is that all clients and the server need to maintain a mapping list between UIDs and GIDs, and user and group names. The mapping information on clients can come from local files like `/etc/passwd` and `/etc/groups` or an LDAP directory. The configuration of this mapping is managed by `rpc.idmapd`, which must run on your client.

On NetApp Volumes, the LDAP must provide mapping information, with Active Directory being the only supported RFC2307bis compatible LDAP server. When using Kerberos for NFSv4, the security identifier stores Kerberos principals in the format `username@DOMAINNAME`, where DOMAINNAME (in capital letters) becomes the realm name.

### Numeric IDs

For users that don't want to configure the name mappings and instead use NFSv4 as a replacement for NFSv3, NFSv4 has introduced an option called `numeric ID`, which sends UID and GID encoded text strings as security identifiers. This simplifies the configuration process for users.

**Note:** The latest Linux distributions enable `numeric ID` option by default.

You can check your client setting using the following command:
    
    
         cat /sys/module/nfs/parameters/nfs4_disable_idmapping
       

The default value is **Y** , which enables numeric IDs. NetApp Volumes supports the use of numeric IDs.

### Configure rpc.idmapd on NFS client

Regardless of the type of IDs or security identifiers you use, it is necessary to configure `rpc.idmapd` on your NFS client. If you followed the installation instructions for client utilities in the [Before you begin](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-nfs-clients#before_you_begin) section, it should already be installed but might not be running. Some distributions start it automatically using `systemd` when you mount the first NFS volumes. The minimum configuration required for `rpc.idmapd` is to set up the domain setting. Otherwise, the user root will be displayed as nobody with `UID=65534 or 4294967295`.

Use the following instructions to configure `rpc.idmapd` on your NFS client:

  1. On your client, open the file `/etc/idmapd.conf` and change the domain parameter to one of the following:

     * If your volume isn't enabled for LDAP, `domain = defaultv4iddomain.com`.

     * If your volume is enabled for LDAP, `domain = <FDQN_of_Windows_Domain>`.

  2. Activate the changes to `rpc.idmapd` by running the following command:
         
         nfsidmap -c




## NFSv4.2 support

The Flex Unified, Standard, Premium, and Extreme service levels now support the NFSv4.2 protocol in addition to NFSv4.1 on volumes that already have NFSv4.1 enabled.

When mounting an NFS volume, the Linux mount command automatically selects the highest available NFS version. Mounting an NFSv4.1 enabled volume automatically defaults to NFSv4.2 unless the `vers=4.1` mount option is explicitly specified.

NetApp Volumes support NFS extended attributes `xattrs` with NFSv4.2. The usage and limitations of `xattrs`, as detailed in [TR-4962](https://www.netapp.com/pdf.html?item=/media/84595-tr-4962.pdf), are also applicable.

## Firewall rules for NFS volumes access

NFS uses multiple ports to communicate between the client and a server. For communication between Google Compute Engine and NetApp Volumes, these ports aren't blocked by default. If you use a firewall, you must enable access to the following ports for the full [NetApp Volume PSA CIDR](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access) or the individual volume IP addresses:

  * `111 TCP/UDP portmapper`

  * `635 TCP/UDP mountd`

  * `2049 TCP/UDP nfsd`

  * `4045 TCP/UDP nlockmgr` (for NFSv3 only)

  * `4046 TCP/UDP status` (for NFSv3 only)




The IP addresses for NetApp Volumes are automatically assigned from the CIDR range you assigned to the service during network peering. For more information, see [Configure private services access](https://docs.cloud.google.com/netapp/volumes/docs/plan-and-prepare/networking#configure_private_services_access).

### Advisory lock use with NFSv3

If you use advisory locks with NFSv3, you must run the `rpc.statd` daemon on your client to support Network Lock Manager, which works with NFS to provide `System V` style advisory file and record locking over the network. Your NFS client must open an ingress port for `rpc.statd` to receive Network Lock Manager callbacks. In most Linux distributions, `rpc.statd` starts when you mount the first NFS share. It uses a random port that you can identify using the `rpcinfo -p` command. To make `rpc.statd` compatible with firewalls, configure it to use a static port.

To set static ports for `rpc.statd`, refer to the following resources:

  * [Debian/Ubuntu](http://wiki.debian.org/SecuringNFS)

  * [SuSE](https://www.suse.com/support/kb/doc/?id=000016649)

  * [RedHat](https://access.redhat.com/solutions/659043)




If you don't use NFSv3 advisory locks or Network Lock Manager, you can mount your NFSv3 shares with the `nolock` mount option.

NFSv4.1 implements the lock function within the NFSv4.1 protocol, which runs over the client-initiated TCP connection to the NFSv4.1 server on port `2049`. The client doesn't need to open firewall ports for ingress traffic.

## Connect Linux to LDAP

If you are using NFSv3 extended groups or NFSv4.1 with security identifiers, you configured NetApp Volumes to use your Active Directory as LDAP server using an Active Directory attached to a storage pool.

To maintain consistent user information between NFS client and server, you might need to configure your client to use Active Directory as LDAP name service for user and group information.

Use the following resources to configure LDAP:

  * [RedHat deployment guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/6/html/deployment_guide/sect-sssd-ad-ldap-proc)

  * [Ubuntu deployment guide](https://ubuntu.com/server/docs/service-sssd-ldap)

  * [SuSe deployment guide](https://documentation.suse.com/sles/15-SP1/html/SLES-all/cha-security-ad.html)




When using Kerberized NFS, you might need to use the deployment guides mentioned in this section to configure LDAP and ensure consistency between the client and server.

## What's next

  * [Optimize Linux NFS clients for NetApp Volumes](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/optimize-linux-nfs-clients).

  * [Connect large capacity volumes with multiple storage endpoints](https://docs.cloud.google.com/netapp/volumes/docs/connect-clients/connect-large-capacity-volumes).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
