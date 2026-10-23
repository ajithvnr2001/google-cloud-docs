---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-vm/
title: Clone VMware VMs in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:12.601618+00:00
---

# Clone VMware VMs in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Clone VMware VMs in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Use these instructions to clone an image of a virtual machine in the appliance management console.

  1. From the Backup and DR appliance management console, click **App Manager** > **Applications**.

The **Applications** page opens.

  2. Select the application with the image you want to clone, then choose **Access** from the dialog list at the right corner of the **Applications** page.

The **Access** page opens listing backup images using the timeline ramp view. Image types that support clone creation include OnVault, snapshot, and remote snapshot—StreamSnap images.

  3. Select an image and then select **Clone** from the list of access operations. 

The **Clone** page opens.

  4. Enter a name for the VM that you want to clone in **VM Name**.

  5. Select a vCenter from the **VCENTER** drop-down for the VM you want to clone.

  6. Select an ESX host from the **Choose Server** drop-down where you want to clone the VM.

  7. Select a datastore from the **Datastore** drop-down that has the required storage available.

**Note:** A clone is a full copy of the VMware VM written to the specified datastores including all configuration files.
  8. If you need to change the volume provisioning for the clone image for space allocation of the image, specify one of the selections under **Provisioning Type**.

**Note:** The appliance management console maintains thin and thick provisioning of the original host while cloning or restoring an image.
     * **Original Setting** : Default provisioning setting of the image.
     * **Thin** : A volume with a virtual capacity that differs from its real capacity—a logical capacity size that is larger than the actual physical capacity that is assigned to the volume.
     * **Thick** : A volume that uses a fully allocated—thick—amount of capacity that is reset to zero prior to new data being written.
     * **Thick Lazy** : A volume that uses a fully allocated—thick—amount of capacity, but only the used space is initially reset to zero. The remaining unallocated space is reset to zero during the first write to that space.
  9. Enter a unique name for the new clone in the **Label** field.

  10. Select a single volume or multiple volumes from **Select Volumes To Clone**. By default all volumes are selected, and the first volume cannot be deselected. For an individual file system there may be only one volume.

Specify the **Datastore** and **Provisioning Type** for each volume you want to mount—see steps 9 and 10.

**Note:** Backup and DR assumes that the first volume of the VM is the boot volume. If the first volume is not the boot volume, contact customer support for assistance.

A job is submitted to clone the image to the selected host.

When the clone job is complete, the image is not available in the [Manage active mounts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts) view of the **App Manager** as it is not dependent on the backup/recovery appliance. The new VM needs to be managed from the vSphere client.




## The VMware administrator's guide

This page is one in a series of pages specific to protecting and recovering VMware VMs with Backup and DR. You can find additional information at:

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)
  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)
  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)
  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)
  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)
  * [Configure Application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)
  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)
  * [Mount a VMware image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)
  * [Clone an image of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)
  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)
  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
