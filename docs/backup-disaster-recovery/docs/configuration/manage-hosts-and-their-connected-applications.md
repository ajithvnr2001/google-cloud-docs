---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications/
title: Manage application hosts in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T09:10:41.677072+00:00
---

# Manage application hosts in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage application hosts in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The **Hosts** page lists all of the hosts managed by the backup/recovery appliances and known to the appliance management console.

If you choose to protect databases and file systems within VMs, then each VM that hosts a database or file system to be protected is called a **host** and each host needs a [Backup and DR agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector).

## Host page features

From the **Hosts** page, you can:

  * View information related to the imported hosts, such as hostname, friendly path to the host, appliance, IP address, and type of host (such as Generic, vCenter or ESX).

  * View a more granular level of detail related to each host, such as unique name, OS release, OS version, and OS type.

  * Select Block versus NFS protocol. All applications on that host use one or the other.




## Backup and DR agent

For the appliance management console to discover applications on a host, the host must have the Backup and DR agent installed. The Backup and DR agent is used to back up selected applications. It is a small-footprint, operating system-specific, lightweight service that can be installed on servers that run supported operating systems and allows the appliance to find file shares, file systems, and supported databases.

Refer to [Install the Backup and DR agent on the hosts](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector) to learn more about the Backup and DR agent.

**Note:** The Backup and DR agent is not required for backing up entire VMware VMs or entire Compute Engine instances.

## Add a host

**Note:** If you added the host to Backup and DR as a Compute Engine instance or as a VMware VM, then a host already exists and you don't need to add it again using the following procedure. Instead, find and edit that host where required.

Use the following instructions to add a new host:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Hosts**.

  2. Select **Add Host**. The upper portion is for network and other identification information. Following that is a dynamic section for host connections.

  3. Enter the hostname and a friendly path for the host in the **Name** field. The name of a host must start with a letter and can contain letters, digits (0-9), and an underscore (___).

**Note:** (SAP MaxDB 7.9.10.06 and earlier only) The database connection fails if the hostname length exceeds 64 characters. For a workaround, use a short hostname alias in the /etc/hosts file. For the dbmcli command use the -n option and assign the hostname with localhost as a workaround: `dbmcli -n localhost -d <DBID> -u control,password`  
See this [SAP Note](https://me.sap.com/notes/0003198983).
  4. Enter the IP address of the host in the **IP Address** , then click the **plus sign (+)** to add it.

  5. Optionally, add a description of this host in the **Description** field.

  6. Select the appliance management console managed appliances that serve this host in the **Appliances** section. If the list is long, you can use the **Search** field to find a specific appliance or group of appliances.

  7. Select the **Host Type** —vCenter, ESX Server, or Generic. Select **Generic** for all host types that are not vCenter or ESX hosts. This includes Windows and Linux hosts. Generic hosts require a Backup and DR agent of the type that matches their OS.

For vCenter or ESX Server selections, you also get the option to select a **Transport Mode**. You see the **Transport Mode** option only while adding a host. This option cannot be edited after the host has been added.

     * **NFS** (default): The appliance shares disks with the ESXi hosts using an NFS Datastore.

     * **SAN** : The appliance shares disks with the ESXi hosts using Raw Device Mappings (RDM) over iSCSI.

  8. Fill in either **vCenter Settings** , **ESX Settings** , or **Application Discovery Credentials** as needed for this host. Application discovery credentials are used for database discovery where the agents default permissions are not sufficient. This **Application Discovery Credentials** field is applicable only for MaxDB, PostgreSQL, SAP ASE, and SAP IQ databases.

  9. In the **Backup and DR Agent Settings** section, complete the following:

     * Backup and DR agent port is normally port 5106. If it is anything else, enter that port here.
     * Only add credentials for the host if SMB shares need to be discovered. This is different from **Application Discovery Credentials**.

     * You need to supply a secret key generated on [Windows](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-windows) and [Linux](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector#antivirus) host servers by the Backup and DR agent, to initialize trusted communications between the backup/recovery appliance and Backup and DR agent. If you don't have a secret key that was generated in the last two hours, then generate the [Linux](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-linux-hosts#regenerate) and [Windows](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-windows#regenerate) secret keys.

  10. Click **Add** to save the host information.

The **Edit Host** page opens where additional steps are required if you are adding a host that uses NFS storage or Oracle database authentication. If the new host is defined on multiple appliances and if the information is not identical for them all, then you see the [Host Reconciliation page](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications#reconcile) first.




The appliance management console relies on synchronization between the backup/recovery appliance and its discovered hosts. Hosts that are not connected to an NTP server can drift, resulting in differences between the host's record and the appliance's record of the time snapshots were taken or other actions were performed by the backup/recovery appliance.

## View information about your connected hosts

Use these instructions to display the hosts known to the backup/recovery appliances:

  1. In the appliance management console, select the **Manage** drop-down menu and select **Hosts**.

  2. To modify the display, you can do the following:

     * **Adjust Fields** : To modify the fields that appear in the table, right-click within the table header row and click the checkboxes for the fields you want displayed or those fields you don't want to view.

     * **Sort Content** : To sort the content listed in a table column by alphanumeric order, select a column header and then click the **Up** or **Down** arrow to change the order.

     * **Adjust Column Width** : To adjust the width of a table column to show more content in the table, drag the column divider in a column header to the left or right to resize the column width. Column dividers are marked by a pair of thin gray lines.

     * **Filter By** : To filter the list of hosts make a selection from the left-hand list of filter options.

  3. Click the export icon to export the list. You can export in PDF format.

  4. To modify the number of rows displayed in a table page, you can select from the drop-down list.




## Edit host properties

Use the following instructions to edit a host's properties:

  1. In the appliance management console, select the **Manage** drop-down menu and click **Hosts**.

  2. Click **Hosts** to view the hosts list.

  3. Right-click on a specific host.

  4. From the drop-down menu, select **Edit**. The **Edit Host** page displays.

The **Edit Host** page is similar to the **Add Host** page, but it lets you add additional information.

     * **Name** : The name, fully qualified domain name, or the IP address of the host.

     * **Friendly Path** : The URL alias for the host.

     * **IP Address** : The internal IP address for the host. Enter it in the text field, then click the **plus sign (+)**.

     * **Description** (Optional): additional information related to the host or related to modifications made to the host.

     * **Appliances** : These are the backup/recovery appliances that are connected to the host.


Property | Description  
---|---  
Host Type  | Host type is set when you add the host. It can't be changed from the Edit Host page. It is either Generic, ESX Server, or vCenter  
Staging Disk Format to Guest  | Select the Disk Preference, either Block or NFS. NFS appears for Linux hosts only. All applications on that host use the same protocol. Images of an application captured over NFS can only be accessed over NFS.  
Transport Mode | vCenter host only. This setting controls the default protocol used for presenting the staging disk (when applicable) and mount disks. There are two choices: NFS or SAN.   
When NFS is selected then VMDKs are presented to the VMs through an NFS datastore that is accessed by the ESX servers.   
When SAN is selected then VMDKs are presented to the VMs using iSCSI volumes shared to the VMs as RDMs (Raw Device Mappings) using the ESX servers.  
Enable Auto Discovery  | You can set the host to auto-discover applications from here, including VMware VMs if set on the vCenter host.  
Oracle Database Authentication  | Select this if you want the host to require Oracle database authentication.   
If this is not selected, then OS integrated authentication is used.  
  
At the bottom of the **Edit Host** page, you're given the options for editing.

Property | Description  
---|---  
NFS Settings  | The NFS settings is displayed only when the **Staging Disk Format to Guest** is set to **NFS**. We recommend you keep the default NFS settings.  
Application Discovery Credentials | Enter **Application Discovery Credentials** to discover and protect the database applications on the host. This field is applicable only for MaxDB, PostgreSQL, SAP ASE, and SAP IQ databases.  
Backup and DR Agent Settings  | Change the Backup and DR agent settings of this host by updating the Backup and DR agent port and login credentials. Login credentials are used to discover SMB shares.  
Discovered Applications  | Selecting an application on this host. Apply or update backup templates.  
  
## Configure hosts to auto-discover their applications

You can enable your appliances to auto-discover new applications on a configured host. You can only enable this feature after the host has been added.

  1. Click **Manage** > **Hosts**. The **Hosts** page appears.

  2. Right-click the host to enable auto-discovery on and select **Edit**.

  3. Slide the **Enable Auto Discovery** button to the right and click **Save**.




## Reconcile inconsistent host information across multiple appliances

A host can be defined on multiple appliances intentionally or unintentionally which is common with VMware VMs. If the host is managed by two appliances, then the name is preceded by a multiple-appliances icon and the entry in the **Appliance** column shows a link to the other appliance.

When records of the same host reside on multiple backup/recovery appliances, the host information can be slightly different from one appliance to another. In that case, when you edit the host record, a **Host Reconciliation** section at the top of the host record appears. Review the information in the table and select the host record that has the most up-to-date information. Then, click **Submit**. All other host records in the table are reset to match the selected host record. After this, you can see the **Edit Host** page detailed in [Edit host properties](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications).

## Security software on hosts

Security software, including antivirus and other disk monitoring software, can interfere with mount, clone LiveClone, or restore operations for any non-VM application to a host. Consider exempting the target disk from the interfering software for the duration of the operation. For more information, see the antivirus software discussion in [About the Backup and DR agent](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/about-connector#antivirus).

## NFS settings overrides

Some appliance-side and host-side settings can be overridden for NFS type hosts from the appliance management console. Consult your network administrator before you change these settings.

### Appliance-side

The following settings can be overridden from the appliance management console:

  * `insecure`

  * `wdelay`

  * `NFS serverip`




The following settings can't be overridden from the appliance management console:

  * `sec`

  * `insecurelocks`

  * `readonly`

  * `rootsquash`

  * `sync`

  * `anonuid`

  * `subtreecheck`

  * `anonuid`




### Host-side

The following settings can be overridden from the appliance management console:

  * `retrans`

  * `async`

  * `acregmin`

  * `rsize(bytes)`

  * `acregmax`

  * `wsize(bytes)`

  * `acdirmin`

  * `timeo(deciseconds)`

  * `acdirmax`




The following settings can't be overridden from the appliance management console:

  * hard

  * lock

  * ro

  * proto

  * sec

  * vers




Use the **Test** button to make sure that the new settings can still connect to the host.

## Set staging disk I/O path (for VMware VMs only)

You can use the staging disk I/O path setting to control the data transport path for agent based backups where the agent is running in a VMware VM.

Use the following instructions to configure staging disk I/O path:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Hosts**.

  2. Filter by hosts of type **Generic** and for "Show only", select **Virtual Machines**.

  3. Select the host for which you want to configure the staging disk I/O path and click **Edit**.

  4. Go to the Staging Disk I/O Path section in the **Edit Host** page.

  5. Select one of the following options using information in the following table:

Transport | Backup and DR volumes are presented | to the | attached to VM as  
---|---|---|---  
NFS transport | Over NFS datastore | ESXi host | VMDK  
SAN Transport | Over iSCSI | ESXi host iSCSI initiator | Raw device mapping (RDM)  
SAN to Guest | Over iSCSI | Guest VM iSCSI initiator | Block device  
NFS to Guest | Over NFS | Guest VM NFS client | NFS share  



## Revoke a host certificate

A certificate should be revoked immediately when its private key shows signs of compromise.

When you revoke the certificate on a host, the appliance management console and the backup/recovery appliance can no longer communicate with the Backup and DR agent on the host with the following effects:

  * Existing scheduled and on-demand backups on the host fail.

  * Backup and DR agent upgrade fails on the host.

  * Active mounts on the host are still accessible.




Use the following instructions to revoke a host's certificate:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Hosts**.

  2. Right-click the host and select **Revoke Certificate**.

  3. Click **OK** to confirm the operation.




## Restore trust in a host

If a host certificate has been revoked, the appliance management console and the backup/recovery appliance can no longer communicate with the Backup and DR agent on the host. You can restore trust when appropriate.

Use the following instructions to restore trust in a host:

  1. In the appliance management console, click the **Manage** drop-down menu and select **Hosts**.

The **Hosts** page appears listing known hosts, including their certificate status.

  2. Right-click the host and select **Edit**.

  3. Go to **Backup and DR Agent Settings** in the **Edit Host** page.

Open the section by clicking the label.

  4. On the host, change directory to where the `UDSagent` binary is located and run the following command:
         
         udsagent secret --reset
         

  5. Copy the output and paste it into the **Secret** field.

  6. Click **Save**.




## Delete hosts

You can delete a host if there are no managed applications on that host. Use the following instructions to delete a host:

  1. In the appliance management console, expand the **Manage** drop-down menu and select **Hosts**. The **Hosts** page appears.

  2. Right-click the host that you want to delete and select **Delete**.

  3. Click **OK** in the **Delete Host** window.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
