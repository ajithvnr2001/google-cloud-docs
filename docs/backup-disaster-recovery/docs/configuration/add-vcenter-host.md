---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host/
title: Add vCenter/ESX server hosts to the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:55.085688+00:00
---

# Add vCenter/ESX server hosts to the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Add vCenter/ESX server hosts to the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Backup and DR uses [VMware vSphere storage APIs](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3FD5AB1E-47B3-49B5-845E-5224BE062A59.html) data protection to create backups of VMware VMs, placing backups either in the snapshot pool of the backup/recovery appliance or in OnVault pools.

To make API calls, the backup/recovery appliance needs to connect to the vCenter or ESX server host with a username and password that has authority to perform the required actions. This page explains how to add a vCenter or ESX server host in the appliance management console.

## Before you begin

  * Be sure to review [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware).

  * Make sure that the vCenter server is accessible from the appliance as described in [Third-party service certificate](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/certificate).

  * Backup and DR establishes a secure connection with the vCenter. If a secure connection is not established, backup and restore jobs fail. The connection to vCenter fails in either of the following scenarios:

    * If there is a mismatch between the name of the vCenter and the name in the vCenter certificate.
    * If the vCenter certificate is not trusted by OS trust anchors or if vCenter has self-signed certificates.



## Add a new vCenter or ESX Server host

Use these instructions to add a new vCenter or ESX server host to the appliance management console:

  1. Click **Manage** > **Hosts**.

  2. Select **\+ Add Host**.

  3. In the **Name** field, enter the _fully qualified domain name_ of the vCenter host. Ensure that the name in the host's **Name** field is the same as in the vCenter certificate. The connection fails if there is a mismatch.

  4. Optional: In the **Friendly Name** field, enter a user-friendly name for the host. The name of a host must start with a letter, and can contain letters and digits (0-9). Don't use underscore (___) characters in hostnames. You can also add a friendly name for the vCenter host in the **Friendly Name** field.

**Note:** For existing vCenter hosts, if the hostname does not match the fully qualified domain name (FQDN) of the server, then the backup/recovery appliance automatically updates the hostname during the appliance upgrade. The existing hostname is moved to the **Name** column if the **Friendly Path** column is empty.
  5. Enter the IP address of the host in **IP Address**. Click **+** to add multiple IP addresses.

  6. In the **Appliances** section, select one or more appliances that serve this host. If the list is long, you can use the search field to find a specific appliance or group of appliances.

  7. In **Host Type** , select either **vCenter** or **ESX Server**.

**Note:** You normally don't need to add ESX servers as they are auto-discovered when you add the vCenter host that manages them.
  8. Select the data transport mode, either **NFS** or **SAN**. NFS is the recommended and default setting. Enter the username and password to connect to the host and then use the **Test** button to validate them. You only need to enter a port if a non-standard port is being used. 

Host settings To protect | Select host type | Connection type  
---|---|---  
vCenter with ESXi VMs | vCenter | The default vCenter management port is 443. If you use a different port, then enter it here. Enter the **vCenter User Name** and **vCenter Password** and then select **Test**.   
ESXi standalone | ESX Server | The default ESX Server management port is 902. If you use a different port, then enter it here. Enter the **ESX User Name** and **ESX Password** and then select **Test**.   
  9. Click **Add**.




## What's next

  * To discover and protect VM, see [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)



## The VMware administrator's guide

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)
  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)

  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)

  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)

  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)

  * [Configure application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)

  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)

  * [Mount a VMware image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)

  * [Clone an image of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)

  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)

  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
