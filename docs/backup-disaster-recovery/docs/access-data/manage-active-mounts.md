---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts/
title: Manage active mounts in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T19:08:31.230487+00:00
---

# Manage active mounts in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Manage active mounts in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

The **Active Mounts** page in **App Manager** lists all active backups (mounts) available in the appliance management console. From this page, you can view information such as the application name, application type, source and mounted hostname, label, source backup, and the name associated with an active backup. You can also check if an active backup is marked sensitive and its expiration date.

From the **Active Mounts** page, you can perform the following actions:

  * Forget an active mount
  * Unmount an active backup
  * Unmount and delete an active backup
  * Remount a backup that was previously unmounted
  * Delete a mount that was previously unmounted
  * [Mount and migrate operations from the active mounts page](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-and-migrate)



After you are finished with a mounted backup, you can remove it from the appliance without deleting the instance from the cloud.

Active backups are handled differently depending on how they were mounted:

  * **Persistent Disk** : Backups on Persistent Disk (Compute Engine, Cloud SQL, and HANA and Db2 databases backed up to Persistent Disk) are mounted on a new Persistent Disk or Google Cloud Hyperdisk and attached to the selected VM. These backups can be forgotten or unmounted and deleted.
  * **Backup and DR snapshot** : Backups are mounted on a new volume (virtual snapshot) in the backup/recovery appliance snapshot pool and attached to the selected VM. These backups can only be unmounted.



## Forget active mount (only for backups on Persistent Disk)

The disk remains attached to the VM but Backup and DR no longer manages it. You will still be billed for the storage under Persistent Disk in Compute Engine. To delete the disk and avoid charges, choose **Unmount and delete**.

Use these instructions to forget an active mount:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Active Mounts** from the drop-down menu.

The **Active Mounts** page opens.

  2. Select the active mount that you want to forget.

  3. Select **Forget Active Mount** from the drop-down menu at the bottom of the page.

The **Forget Active Mount** page opens.

  4. Click **Submit**. You can view the status of the job in the **Monitor**. Go to **Monitor Jobs**.




## Unmount an active mount

To remove a mount from a host and retain it for later use, you can choose to unmount it without deleting it.

Use these instructions to unmount an active backup:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Active Mounts** from the drop-down menu.

The **Active Mounts** page opens.

  2. Select one or more active backups that you either want to unmount.

  3. Select **Unmount** from the drop-down menu at the bottom of the page.

  4. Click **Submit** to complete the unmount operation. You can view the status of the unmount and delete job in the **Monitor**. Only use the force option if advised by Support.




## Unmount and delete an active backup

When you no longer require an active backup, you can unmount and delete it.

  * For mounts from a Backup and DR snapshot, the volume is unmounted from the VM and the snapshot is deleted from the backup/recovery appliance snapshot pool.
  * For mounts from Persistent Disk, the disk is detached from the VM and deleted.



In both cases, there will be no further cost for the disk.

Use these instructions to unmount and delete an active backup:

  1. Go to **App Manager** menu and select **Active Mounts**.

The **Active Mounts** page opens.

  2. Select one or more active backups that you want to unmount and delete.

  3. Select **Unmount and delete** from the drop-down menu.

  4. Click **Submit** to complete the unmount operation. You can view the status of the unmount and delete job in the **Monitor**. Only use the force option if advised by Support.




## Remount an unmounted backup

Remounting an unmounted backup re-attaches the volume to the target VM. This can only be performed on a backup that was previously unmounted.

When you unmount a backup, the underlying storage (either a snapshot in the appliance pool or a persistent disk) is retained, and you continue to be billed for it. Remounting does not incur additional storage costs, but you are still responsible for the cost of the retained storage.

To remount an unmounted backup, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Active Mounts** from the drop-down menu.

The **Active Mounts** page opens.

  2. Select one or more backups that you want to remount, they should have the **Image Status** of **Unmounted**.

  3. Select **Remount** from the drop-down menu.

The **Remount** page opens.

  4. From the **Host** drop-down list, select a target host.

  5. For VMware hosts only:

     1. For **Mount Mode** , select from the **NFS (default)** , **vRDM** (virtual raw device mapping) or **pRDM** (physical raw device mapping) options.

**Note:** VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs is included in VMware snapshots. Backup templates captures vRDMs marked as dependent. Note that vRDM and pRDM uses iSCSI, which Google Cloud Google Cloud VMware Engine does not support by default.
     2. From **Map to ESX Hosts** , select one of the following options:

        * **One** : Select **One** if you want to map only to the ESX host running the target VM.
        * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select chooses the second host based on logical pairs of ESX hosts and always selects the partner ESX host for the one running the target VM.
        * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration of the job.
  6. Enter a unique name in **Label**.

  7. Enter an unused drive letter in **Mount Drive**. The **Mount Drive** is where backup/recovery appliance tries to put the data. If the selected drive letter is occupied, then the data is put in the next available letter approaching A.

  8. Enter a **Mount Point**. This is where the new data exists after it is mounted to the host.

  9. Click **Submit**. A job is submitted to mount the backup to the selected host, and the backup becomes **Active**.




## Delete an unmounted backup

Images take up storage space, so if you find there are unmounted backups that are no longer required, you can delete them to free up that space. Periodically check for and delete unused backups.

Use these instructions to delete an unmounted backup:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Active Mounts** from the drop-down menu.

The **Active Mounts** page opens.

  2. Select one or more unmounted active backups that you want to delete.

  3. Select **Delete** from the drop-down list at the bottom of the page. You can also right-click on the item in the list and select **Delete** from the menu.

  4. Click **Submit**. You can view the status of the delete job in the **Monitor**.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
