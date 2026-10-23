---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts/
title: Add Linux hosts to the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:50.574166+00:00
---

# Add Linux hosts to the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add Linux hosts to the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR discovers file systems, network file share (NFS) shares, and supported databases on Linux hosts. Before you can discover and back up data from these hosts, you must do the following:

  * [Install the Backup and DR agent on the Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent)

  * Add the Linux host.

  * Check the iSCSI or NFS connectivity




## Add Linux hosts

**Note:** If you have added the Linux server to Backup and DR as a Compute Engine instance or as a VMware VM, then a host for this VM already exists and you don't need to add it again using the following procedure. Instead, find and edit that host and edit it as explained in Add a secret key.

Use the following instructions to add a Linux host: 

  1. In the appliance management console, go to **Manage** > **Hosts**.

  2. Select **\+ Add Host**.

  3. In the **Add Host** form, enter the name and an optional friendly name. The name of a host must start with a letter, and can contain letters and digits (0-9). Note that underscore (___) characters are not valid in host names.

  4. Enter the IP address of the host in **IP Address** and click the **plus sign (+)** to add it.

  5. In the **Appliances** section, select the appliance management console managed appliances that you want to serve this host. If the list is long, you can use the **Search** field to find a specific appliance or group of appliances.

  6. In **Host Type** , select **Generic**.

  7. Enter **Application Discovery Credentials** to discover and protect the database applications on the host. This field is applicable only for MariaDB, MaxDB, MySQL, PostGresSQL, SAP ASE, and SAP IQ databases.

  8. In the Backup and DR agent settings, complete the following steps:

     * The Backup and DR agent port is normally port 5106. If it is anything else, enter the port number here.

     * You need to supply the secret key generated on Linux host using the instructions in [Install the Backup and DR agent on a Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent) or [Regenerate the secret key](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/linux-agent#regenerate) section. You can add the secret key now or later using the Add a secret key instructions but before running the application discovery.

  9. Click **Add**. If you get a partial success message, use the instructions to [Validate backup/recovery appliance to Backup and DR agent connectivity](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-network-settings#validate).




### Add a secret key

If you want to update the secret key or if you didn't add the secret key initially, you can add it in the [Linux host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts).

  1. Go to the appliance management console, select **Manage** and then select **Hosts**.

  2. Right-click the Linux host and choose **Edit**.

  3. Go to **Backup and DR Agent Settings** and find the **Secret** field.

  4. Paste the secret key that you saved earlier in the **Secret** field and click **Save**. Ensure the **Certificate** status changes to **Valid**. If you get a partial success message, use the instructions to [Validate backup/recovery appliance to Backup and DR agent connectivity](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/appliance-network-settings#validate).




## Abnormally long backup jobs and fstrim

Backup and DR CBT technology relies on a bitmap that is generated for every write operation on the protected volume. Utilities like fstrim that modify the file system metadata blocks cause the backup process to copy additional data, increasing the backup time.

## iSCSI connectivity on a Linux host

If the Backup and DR agent is going to write backup data onto the staging disk using iSCSI, then an iSCSI initiator must be installed on the host.

### Install the iSCSI initiator on Linux host

Use the following instructions to install iSCSI initiator on Centos, RHEL, SLES, or Ubuntu hosts.

### CentOS

  1. Make sure you have the `iscsi-initiator-utils` package installed. Use the following command to check the installed package:
         
         yum list installed | grep iscsi
         

You can also use the following command to check the initiator package:
         
         rpm -qa | grep iscsi
         

The output looks similar to the following:
         
         iscsi-initiator-utils-6.2.0.865-6.el5.x86_64.rpm
         

  2. If you see nothing, then you can proceed to install the package with the following command:
         
         yum install iscsi-initiator-utils
         

  3. Validate your iSCSI initiator name with the following command. Each host needs to have a unique initiator name:
         
         cat /etc/iscsi/initiatorname.iscsi
         




### RHEL

  1. Make sure you have the `iscsi-initiator-utils` package installed. Use the following command to check the installed package:
         
         yum list installed | grep iscsi
         

You can also use the following command to check the initiator package:
         
         rpm -qa | grep iscsi
         

The output looks similar to the following:
         
         iscsi-initiator-utils-6.2.0.865-6.el5.x86_64.rpm
         

  2. If you see nothing, then you can proceed to install the package with the following command:
         
         yum install iscsi-initiator-utils
         

  3. Validate your iSCSI initiator name with the following command. Each host needs to have a unique initiator name:
         
         cat /etc/iscsi/initiatorname.iscsi
         




### SLES

  1. Make sure you have the `iopen-iscsi` package installed. Use the following command to check the installed package:
         
         rpm -qa | grep iscsi
         

The output looks similar to the following:
         
         open-iscsi-x.x.x.x
           yast2-iscsi-client-x.x.x.x
         

  2. If you don't see both of these packages, then use the following procedure to install open-iscsi:

     1. Run `yast2 sw_single`

     2. In the search, enter `iscsi`

     3. Select `open-iscsi` and click **Accept**.

  3. Validate your iSCSI initiator name with the following command. Each host needs to have a unique initiator name:
         
         cat /etc/iscsi/initiatorname.iscsi
         




### Ubuntu

  1. Use the following command to install iSCSI initiator on a Ubuntu host:
         
         sudo apt install open-iscsi
         

The output looks similar to the following:
         
         Reading package lists... Done
           Building dependency tree
           Reading state information... Done
           open-iscsi is already the newest version (2.0.874-5ubuntu2.11).
           open-iscsi set to manually installed.
           The following package was automatically installed and is no longer required:
           libnuma1
           Use 'sudo apt autoremove' to remove it.
           0 upgraded, 0 newly installed, 0 to remove and 0 not upgraded.
         




### View and configure host ports

Ports were set at deployment time in [Set up and plan a Backup and DR deployment](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/deployment-plan#firewall_configurations). Use this section to override the backup/recovery appliance provided port information with new iSCSI port on the host for connecting to the appliance. This port information is sent to the appliances.

Use the following instructions if you want to view or override the port information provided by the appliance:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Hosts**.

  2. Right-click a host and click **Edit**.

  3. Click **Add Port**.

  4. In the **Add port** dialog, select the appliance (if multiple appliances connect to the host).

  5. Select **WWPN** or **iSCSI**.

  6. Click **Add** and then **Save** the host setting.




## NFS connectivity on a Linux host

If the Backup and DR agent is going to write backup data onto the staging disk over NFS, then an NFS client must be installed on the host.

### Change staging disk format

Use the following instructions to change the staging disk format:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Hosts**.

  2. Right-click the host that you want to change the staging disk format and click **Edit**.

  3. Change the **Staging Disk Format to Guest** setting from **Block** to **NFS**.

This ensures that the staging disk is presented as an NFS share and the Backup and DR agent consumes this share. When you mount a backup captured with NFS, it must be accessed as an NFS share; it can't be accessed using iSCSI.




### Install the NFS client on a Linux host

Use the following instructions to install NFS client libraries on Centos, RHEL, SLES, or Ubuntu hosts.

### CentOS

  1. Make sure you have the `nfs-utils` package installed. Use the following command to check the installed package:
         
         yum list installed | grep nfs
         

To check the initiator package, run the following command:
         
         rpm -qa | grep nfs
         

The output looks similar to this output:
         
         nfs-utils-lib-1.1.5-9.el6.x86_64
           nfs-utils-1.2.3-54.el6.x86_64
         

  2. If you don't see anything, then you can proceed to install the NFS client package by running the following command:
         
         yum install nfs-utils nfs-utils-lib
         

  3. Make sure `rpcbind` (portmapper) package is installed on the Linux host with the following command:
         
         yum list installed | grep rpcbind
         

To check the initiator package, run the following command:
         
         rpm -qa | grep rpcbind
         

The output looks similar to the following output:
         
         rpcbind-0.2.0-11.el6.x86_64
         

  4. If you don't see anything, then you can proceed to install the `rpcbind` with the following command:
         
         yum install rpcbind
         




### RHEL

  1. Make sure you have the `nfs-utils` package installed. Use the following command to check the installed package:
         
         yum list installed | grep nfs
         

To check the initiator package, run the following command:
         
         rpm -qa | grep nfs
         

The output looks similar to the following output:
         
         nfs-utils-lib-1.1.5-9.el6.x86_64
           nfs-utils-1.2.3-54.el6.x86_64
         

  2. If you don't see anything, then you can proceed to install the NFS client package with the following command:
         
         yum install nfs-utils nfs-utils-lib
         

  3. Make sure `rpcbind` (`portmapper`) package is installed on the Linux host with the following command:
         
         yum list installed | grep rpcbind
         

To check the initiator package, run the following command:
         
         rpm -qa | grep rpcbind
         

The output looks similar to the following output:
         
         rpcbind-0.2.0-11.el6.x86_64
         

  4. If you don't see anything, then you can proceed to install the `rpcbind` with the following command:
         
         yum install rpcbind
         




### SLES

  1. Make sure you have the `nfs-utils-utils` package installed. Use the following command to check the installed package:
         
         rpm -qa | grep nfs
         

The output looks similar to the following:
         
         nfs-client-1.2.1-2.6.6
           yast2-nfs-common-2.17.7-1.1.2
           yast2-nfs-client-2.17.12-0.1.81
         

  2. If you don't see either `nfs-client` or `yast2-nfs-xxxx` packages, then use either `YaST` or `zypper` to install the NFS client packages using the following commands.

     * Using `YaST`, run the following commandL
           
           yast2 --install yast2-nfs-client
            yast2 --install yast2-nfs-common
           

     * Using `zypper`, run the following command:
           
           zypper install nfs-client
           

  3. Make sure `rpcbind` (`portmapper`) package is installed on the Linux host using the following command:
         
         rpm -qa | grep rpcbind
         

The output looks similar to the following:
         
         rpcbind-0.1.6+git20080930-6.15
         

  4. If you see nothing, then you must install the packages using either `YaST` or `zypper`:

     * Using `YaST`, run the following command:
           
           yast2 --install rpcbind
           

     * Using `zypper`, run the following command:
           
           zypper install rpcbind
           




### Ubuntu

  1. Use the following command to install NFS client libraries on a Ubuntu host:
         
         sudo apt install nfs-common
         

The output looks similar to the following:
         
         Reading package lists... Done
           Building dependency tree
           Reading state information... Done
           The following package was automatically installed and is no longer required:
           libnuma1
           Use 'sudo apt autoremove' to remove it.
         




## Set the staging disk I/O path (VMware VMs only)

Linux VMware VMs can also select a staging disk I/O path. You can assign either NFS or SAN (iSCSI) transport either using the ESX host, or bypass it and direct it to the VM. NFS transport mode is the default. This has no effect on the **Staging Disk Format to Guest** setting.

Use the following instructions to configure the staging disk I/O path:

  1. In the appliance management console, expand the **Manage** drop-down menu and select **Hosts**.

The Hosts page appears.

  2. Filter by hosts of type **Generic** and for **Show only** , select **Virtual Machines**.

  3. Select the host for which you want to configure the staging disk I/O path and click **Edit**.

  4. In the **Edit Host** page, go to the **Staging Disk I/O Path** section.

  5. Select one of the following options using information in this table:

Transport | Backup and DR volumes | Where the volumes are presented | What they are attached to VM as  
---|---|---|---  
NFS transport | Over NFS datastore | ESXi host | VMDK  
SAN Transport | Over iSCSI | ESXi host iSCSI initiator | Raw device mapping (RDM)  
SAN to Guest | Over iSCSI | Guest VM iSCSI initiator | Block device  
NFS to Guest | Over NFS | Guest VM NFS client | NFS share  
  6. Click **Save**.




## Find logs and scripts on Linux host

On a Linux host, the agent logs, called `UDSAgent.logs`, are stored in `/var/act/log`. You can create scripts to perform pre- and post- actions on applications on the Linux host. To use scripts, create a folder called `/act/scripts` and store all scripts in it.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
