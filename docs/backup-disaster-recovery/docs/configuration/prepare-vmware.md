---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware/
title: Configure Google Cloud VMware Engine for Backup and DR on a backup/recovery appliance \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:44:50.834522+00:00
---

# Configure Google Cloud VMware Engine for Backup and DR on a backup/recovery appliance  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Configure Google Cloud VMware Engine for Backup and DR on a backup/recovery appliance Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Before you begin, it's a good idea to review [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro).

Before you add, discover, and protect a VMware VM, you must do the following in the Google Cloud VMware Engine:

  * Create a Google Cloud VMware Engine private cloud

  * Configure Google Cloud VMware Engine private cloud and the VPC connection

  * Set NFS ingress firewall rules for the backup/recovery appliance

  * Set permissions to manage VMware Engine instances




## Create a Google Cloud VMware Engine private cloud

This procedure assumes you've already created a Google Cloud VMware Engine private cloud, deployed Google Cloud VMware Engine, and have the VMware VMs that you want to back up. If you haven't yet deployed Google Cloud VMware Engine, see [Create a Google Cloud VMware Engine private cloud](https://docs.cloud.google.com/vmware-engine/docs/private-clouds/howto-create-private-cloud).

## Google Cloud VMware Engine private cloud and the VPC connection

After you create a Google Cloud VMware Engine private cloud, you need to add a private connection between your Google Cloud VMware Engine private cloud and the VPC where your backup/recovery appliance is deployed. See [Complete private connection creation in the Google Cloud VMware Engine portal](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-setup-private-service-access#complete-private-connection-creation-in-the-vmware-engine-portal).

## Set administrator permissions to manage VMware Engine instances

To manage VMware Engine instances with administrator privileges:

  1. Elevate the permissions first.
  2. Create a user that is not associated with any group.
  3. Create a role with the permissions in the following list.
  4. Assign the role to the newly-created user.
  5. Assign the role in the vCenter Server Appliance.



### Required permissions

**Datastore**

  * Allocate space
  * Browse datastore
  * Low level file operations
  * Removefile
  * Update virtual machine files



**Folder**

  * Create folder



**Global**

  * Cancel task
  * Disable methods
  * Enable methods
  * Licenses
  * Log event



**Host**

  * Configuration

    * Storage partition configuration
  * Local operations

    * Create virtual machine
    * Delete virtual machine
    * Reconfigure virtual machine



**Network**

  * Assign network

  * Host profile

    * Clear
    * Create
    * Delete
    * Edit
    * Export
    * View



**Resource**

  * Assign virtual machine to resource pool



**Tasks**

  * Create task
  * Update task



**vApp**

  * Export
  * View OVF environment
  * vApp application configuration
  * vApp instance configuration
  * vApp managedBy configuration
  * vApp resource configuration



**Virtual machine**

  * Change Configuration

    * Acquire disk lease
    * Add existing disk
    * Add new disk
    * Add or remove device
    * Advanced configuration
    * Change Settings
    * Change resource
    * Configure Raw device
    * Modify device settings
    * Query unowned files
    * Remove disk
    * Rename
    * Toggle disk change tracking
  * Edit Inventory

    * Create from existing
    * Create new
    * Remove
  * Guest operations

    * Guest operation modifications
    * Guest operation program execution
    * Guest operation queries
  * Interaction

    * Configure CD media
    * Connect devices
    * Power off
    * Power on
    * Suspend
  * Provisioning

    * Allow disk access
    * Allow read-only disk access
    * Allow virtual machine download
    * Clone virtual machine
    * Deploy template
  * Snapshot management

    * Create snapshot
    * Remove snapshot
    * Rename snapshot
    * Revert to snapshot 



## Configure Backup and DR to use Google Cloud VMware Engine DNS

During VMware VM backup jobs, the backup/recovery appliance needs to resolve the fully qualified names of the ESX servers running in your Google Cloud VMware Engine private cloud. The easiest way to achieve this is to add a DNS from your private cloud to the backup/recovery appliance. If you don't want to do this, you need to manually add a host entry for each ESX host in the **Host Resolution** tab on the **System Management** page which is accessed as defined in step two.

  1. On Google Cloud VMware Engine, complete the following:

     1. Select **Resources** , then select your private cloud.
     2. Under **Private Cloud DNS Servers** copy either one or both IPs.
  2. In the appliance management console, complete the following:

     1. Go to **Manage** and select **Appliances**.
     2. Right-click the appliance and choose **Configure Appliance Networking**.

The **System Management** page opens in a new window.

     3. Under **DNS,NTP** page, complete the following:

        * Add the DNS as either primary or secondary.
        * Remove any unneeded DNS suffix searches.
     4. Under **Troubleshooting** , complete the following:

     5. Click **Utility** and select **Test DNS**.

     6. Click **Resolve** and select **IP** , then enter the IP in the **IP to resolve** field. It resolves to a name. If it doesn't, validate the connectivity between Google Cloud VMware Engine private cloud and the Backup and DR VPC.




## Set NFS ingress firewall rules for the backup/recovery appliance

When you perform VMware VM mounts using NFS, the backup/recovery appliance provides access to the VMDKs using an NFS datastore. You need to set the ingress firewall rules for the backup appliance to ensure NFS mounts don't encounter unexpected errors.

  1. In the Google Cloud console, go to the **Firewall** page.

[Firewalls](https://console.cloud.google.com/networking/firewalls/list)

  2. Find the VPC firewall rule for your backup/recovery appliance.

It contains the following:

     * **Target** : Service account for your backup appliance.

For example: my-service-account@my-project.iam.gserviceaccount.com

     * **tcp ports** : 
       * 26
       * 443
       * 3260
       * 5107
  3. Edit the firewall rules and add the following:

     * In the **Source IPv4 range** , add the system management subnet of your Google Cloud VMware Engine private cloud. You can find the system management subnet in Google Cloud VMware Engine portal by navigating to **Resources** , then **Select your private cloud** , then **Subnets**.

     * **tcp** :

       * 26
       * 111
       * 443
       * 756
       * 2049
       * 3260
       * 4001
       * 4045
       * 5107
     * **udp** :

       * 111
       * 756
       * 2049
       * 4001
       * 4045
  4. Click **Save**.




### Configure a solution user account

To perform backup, the backup/recovery appliance needs to connect to the vCenter server using an authenticated user that has the correct permissions. The easiest way to set this up is by using a [solution user account](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-solution-user-accounts).

You need to set the solution user account password beforehand:

  1. [Access the VMware Engine portal](https://docs.cloud.google.com/vmware-engine/docs/howto-access-portal)

  2. Select **Resources** , then select your private cloud.

  3. Select **Change your vSphere privileges**.

  4. Leave the user type and time interval to the default option, and select **I Understand**.

  5. Click **Confirm**.

  6. Click [Launch vSphere client (HTML5)](https://docs.cloud.google.com/vmware-engine/docs/vmware-platform/howto-access-vsphere-client).

  7. Go to **Menu** and click **Administration**.

  8. Click **Single Sign On**.

  9. Click **Users and Groups**.

  10. From the main panel, select the `gve.local` domain and select the solution user account.

  11. Click **Edit**.

  12. Enter a strong password in the **Password** and **Confirm Password** fields for the solution user account. Optionally, add the description. Take a note of which solution user you use, for example solution-user-01, and the password you set, as you need to use it when [configuring the vCenter host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host).

  13. Click **Save**.




## What's next

  * [Add vCenter/ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)

  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)




## The VMware administrator's guide

This page is one in a series of pages specific to protecting and recovering VMware VMs with Backup and DR. You can find additional information at:

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)

  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)

  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)

  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)

  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)

  * [Configure application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)

  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)

  * [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)

  * [Clone an image of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)

  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)

  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
