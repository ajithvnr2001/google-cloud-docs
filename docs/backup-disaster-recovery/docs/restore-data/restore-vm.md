---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm/
title: Restore and recover VMware vSphere VMs in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:03.691811+00:00
---

# Restore and recover VMware vSphere VMs in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Restore and recover VMware vSphere VMs in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The restore function reverts production data to a specified point in time. Restoring replaces the original production application data with the specified point-in-time backup. This restoration results in the loss of all current application data as the application will be restored to its status at the point-in-time when the backup was created. 

**Note:** OnVaults using backup vault don't support instant mount.

Use this procedure to restore a VMware VM to a specific point-in-time.

To restore a point-in-time backup from a managed VMware VM:

  1. Click the **App Manager** tab and select **Applications** from the drop-down menu. The Applications page opens. Restore from a backup vault or from a successful backup job that has run through a scheduled or on-demand backup.
  2. Select the managed VMware VM that you want to restore, and then choose **Access** from the drop-down list at the bottom of the Applications page. The Access page opens listing captured backups appear in the Timeline ramp view.
  3. Select the backup, then select **Restore** from the list of access operations. The Restore page opens.
  4. Clear the **Power On Virtual Machine After Restore** checkbox if you don't want the restored VM to be powered on after the restore operation is complete.
  5. Select a single volume or multiple volumes to restore. By default all the volumes are selected.
  6. Click **Submit**. A warning dialog appears. Read it and then enter **DATA LOSS** to confirm.
  7. Depending on your configuration, a second warning may appear. If so, you need to enter **OVERWRITE OTHER APPS** to confirm the restore operation.

The restore job starts. You can verify that the restore operation is successful by viewing the job status in the Monitor.




## The VMware administrator's guide

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)
  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)
  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)
  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)
  * [Apply a backup template to protect a VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)
  * [Configure Application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)
  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)
  * [Mount a VMware backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)
  * [Clone an image of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-backup-of-a-vm)
  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)
  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
