---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/move-vmware/
title: Move VMware VMs from one backup/recovery appliance to another \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:50.610598+00:00
---

# Move VMware VMs from one backup/recovery appliance to another  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/move-vmware/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Move VMware VMs from one backup/recovery appliance to another Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The appliance management console lets you move the management of a VM from one backup/recovery appliance to a target appliance. This process moves management of that VM to the specified target backup/recovery appliance as defined in the **Move Backup Plan** window.

The movement of VM management between two appliances is limited to VMs located within the same vCenter or ESX host. Only appliances that manage VMs in the same vCenter or ESX host can be target appliances for backup plan movement. Those appliances are shown in the list of possible target appliances.

## Move VM management to another appliance

Use these instructions to move a VM from one appliance to another appliance:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the VM that you want to move, then choose **Move Backup Plan** from the drop-down list at the bottom right corner of the window.

The **Move Backup Plan** window opens. The VM you select can be managed or unmanaged. You can move a VM without first applying a backup plan to manage it.

  3. Choose the target appliance, resource profile, and policy template.

  4. Click **Move Backup Plan**.

The moving backup message opens during the move.

**Note:** If the VM on the source appliance is managed with a StreamSnap replication policy, and the replication target—including the VM to move—exists on the target appliance, then appliance management console prevents the backup plan move and generates an error message. This occurs because the VM already exists on the target appliance as part of the replication process, where a full copy of data is created at the remote site.

Once migration is complete, the migration complete message displays.

**Note:** If the move is not successful, the appliance management console displays a **Move Backup Plan Failed** message along with an explanation of the failure as related to the target appliance. If possible, resolve the issue and attempt to move the backup plan again.



## Rename a vCenter

If you change the name of a vCenter, then remember to rename the vCenter within the appliance management console.

Use these instructions to rename a vCenter in the appliance management console:

  1. Click **Manage** and select **Hosts**.
  2. Find your vCenter host and select the **Edit** option.
  3. Update the **Name** field, and select **Save**.



### Effect of changing the UUID of a VM.

If the UUID of a managed VM changes, then a new full copy occurs on the next backup job. This is because the UUID is a key identifier and a changed UUID could mean this is a totally new VM.

## The VMware administrator's guide

  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)
  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)
  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)
  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)
  * [Configure application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)
  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)
  * [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)
  * [Clone a backup of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)
  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)
  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
