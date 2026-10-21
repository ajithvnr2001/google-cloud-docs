---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/liveclone/
title: LiveClone backups in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T07:45:02.927733+00:00
---

# LiveClone backups in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/liveclone/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  LiveClone backups in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

A LiveClone is an independent clone of an active backup that consumes full storage resources and can be mounted to a host. A LiveClone can be refreshed incrementally from another backup, allowing fast and efficient data refreshes for extract, transform, and load processes and test and development purposes. A LiveClone can also be mounted for direct modification to support operations such as data masking.

Because a LiveClone can be created in a different snapshot pool to the source backup, a LiveClone can consume a different class of storage to the source backup. This is useful if you want to simulate workloads on the same class of storage as production data, while leaving the backups on a different class of storage.

LiveClones jobs are commonly run by Backup and DR Workflows and can be used to do the following:

  * **Refresh** : Create multiple, re-mountable copies of an active backup that can be refreshed from the most recent backup of the same application. See [Refresh a LiveClone](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/liveclone#refresh).
  * **PrepMount** : Mount the LiveClone backup to a specific host for a pre-processing operation—such as sanitizing data—even if some copies of this same LiveClone may already be mounted. You can prep-mount a LiveClone backup to scrub confidential or sensitive data.

**Note:** While the LiveClone backup is prep-mounted, it is busy. It cannot be deleted, refreshed, or mounted. If you mount application backups before prep-mounting another backup of the same application, the mounted backups continue to be usable.
  * **PrepUnmount** : A prep-unmount operation on a LiveClone lets you decide if your changes are to be preserved or not. By default changes are tracked and preserved.




LiveClones provide a crucial building block in managing copy data lifecycle as they combine the performance and independence of a full clone with the efficiency and speed of incremental refreshes of data.

## Create LiveClones

Use these instructions to create a LiveClone of a host.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application or VM with the backup that you want to clone, then choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing backups in the timeline ramp view. Backup types that support LiveClone creation include snapshot and remote snapshot—StreamSnap backups. The timeline ramp view is a time-based visualization of seven days of captured backups for the selected application. You can use your mouse scroll wheel or the up and down arrows in the bottom left corner of the page to move the timeline through the captured backups and make a selection. See [Access the timeline ramp view of a backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time) for details.

  3. Select the backup, then select **LiveClone** from the list of access operations. The LiveClone page opens.

  4. Select a snapshot storage pool from the **Choose Pool** drop-down list. If you have multiple pools, each consuming different classes of persistent disk, make sure you select the target pool.

  5. In **Label** , enter a unique name for the new LiveClone.

  6. Click **Submit**. The creation of a LiveClone can take some time depending on the backup size. Once completed, you can see the LiveClone backup in the **Access** page. The LiveClone backup appears adjacent to the original data in the ramp view of the **Access** page with a numeric one. Unlike snapshot backups which are yellow, LiveClone backups are purple.




## Direct mount a LiveClone to a host

Direct-mount a LiveClone to present refreshed backups to work from. If the LiveClone does not already exist, it is must be created first, see Create LiveClones.

To mount a LiveClone to a host follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application with the LiveClone backup that you want to mount, then choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing LiveClone backups in the timeline ramp view. Backup types that support LiveClone creation include snapshot and remote snapshot—StreamSnap backups. The timeline ramp view is a time-based visualization of seven days of captured backups for the selected application. You can use your mouse scroll wheel or the up and down arrows in the bottom left corner of the page to move the timeline through the captured backups and make a selection. See [Access the timeline ramp view of a backup](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time) for details.

  3. Select the LiveClone backup to mount, then select **Mount** from the drop-down list. Unlike snapshot backups which are yellow, LiveClone backups are purple.

The **Mount** page opens.

  4. Select a host from **Host** drop-down list.

  5. This setting only appears if the targeted host is a VMware VM. For **Mount Mode** , select one of the following:

     * **NFS** : By default NFS mode is selected.
     * **vRDM (virtual raw device mapping)** :VMware snapshots treat mounted vRDMs as Independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates capture vRDMs marked as dependent.
     * **pRDM (physical raw device mapping)** : For file-level restore operations, select pRDM mode.
     * This setting only appears if the targeted host is a VMware VM and RDM mount mode is selected. From **Map to ESX Hosts** , select one of the following options:

       * **One** : Select **One** if you want to map only to the ESX host running the target VM.
       * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select choose the second host based on logical pairs of ESX hosts and always selects the partner ESX host for the one running the target VM.
       * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Selecting **All** may increase the duration for the job.

**Note:** You can see the **Map to ESX Hosts** option only when one or more target hosts are VMware VMs and when you have selected vRDM or pRDM in the **Mount Mode** field.
  6. For **Mount Drive** (Windows only), specify a drive letter to be assigned to the volume. If the drive letter is not available, the job fails. If multiple volumes are found, then it assigns subsequent drive letters. If no mount drive is specified, the Backup and DR agent chooses a drive letter itself, if available.

  7. For **Mount Point** , specify the full path at which you want to mount the volume. If the path exists as an empty folder, the Backup and DR agent uses it. If it does not exist, the Backup and DR agent creates it. If it exists as a file or as a folder that is not empty, then the job fails. If there are multiple volumes to be mounted, the Backup and DR agent chooses the user specified drive for one of the volumes and for the remaining it appends an underscore (_) followed by a number, for example, user _specified_ #.

  8. Enter a unique name associated with the LiveClone mount in **Label**.

  9. Select a single volume or multiple volumes from the **Select Volumes To Mount** area of the page. By default, all volumes are selected, and the first volume cannot be deselected. For an individual file system there may be only one volume.

  10. Specify the storage pool, mount drive, and mount point for each volume you want to mount.

  11. Click **Submit**. A job is submitted to mount the LiveClone backup to the selected host. You can verify that the clone operation is successful by viewing the job status in **System Monitor**. Once completed, the backup becomes active and is available for use.




## Refresh a LiveClone backup

Refresh a LiveClone from another backup to allow fast and efficient data refreshes for extract, transform, and load processes and test and development purposes.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application or VM that has the LiveClone backup that you want to refresh, then choose **Access** from the drop-down list at the bottom of the **Applications** page.

  3. Select a LiveClone, then select **Refresh** from the drop-down list. Unlike snapshot backups which are yellow, LiveClone backups are purple.

The **Refresh** page opens.

  4. From the **Refresh to Backup** drop-down list select the backup you want to use to refresh.

  5. Click **Submit** to refresh the LiveClone backup.




## Perform a prep mount for a LiveClone

You can prep-mount a LiveClone if you want to present a sanitized or otherwise processed snapshot before mounting the LiveClone backup to target hosts. You can prep-mount a LiveClone backup to scrub confidential or sensitive data.

**Note:** While the LiveClone backup is prep-mounted, it is busy. It cannot be deleted, refreshed, or mounted. If you mount application backups before prep-mounting another backup of the same application, the mounted backups continue to be usable.

Use these instructions to prep-mount a LiveClone.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application or VM that contains the LiveClone backup that you want to mount, then choose **Access** from the drop-down list at the bottom of the **Applications** page.

  3. Select the LiveClone backup to prep mount, then select **Prep Mount** from the drop-down list.

The **Prep Mount** page opens.

  4. Select a host from **Host** drop-down list.

  5. To apply pre- and post-scripts to the LiveClone before mounting, from the **Pre-Script** and **Post-Script** fields enter the path and relative filenames. Also enter the timeout values to prevent hanging. We recommend 300 seconds as a default timeout value.

  6. This setting only appears if the targeted host is a VMware VM. For **Mount Mode** , select one of the following:

     * **NFS** : By default NFS mode is selected.
     * **vRDM (virtual raw device mapping)** : VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs is included in VMware snapshots. Backup templates captures vRDMs marked as dependent.
     * **pRDM (physical raw device mapping)** : For file-level restore operations, select pRDM mode.
  7. For **Mount Drive** : (Windows only). Specify a drive letter to be assigned to the volume. If the drive letter is not available, the job fails. If multiple volumes are found, then it assigns subsequent drive letters. If no Mount Drive is specified, the Backup and DR agent chooses a drive letter itself, if available.

  8. For **Mount Point** : Specify the full path at which you want to mount the volume. If the path exists as an empty folder, the Backup and DR agent uses it. If it does not exist, the Backup and DR agent creates it. If it exist as a file or as a folder that is not empty, then the job fails. If there are multiple volumes to be mounted, the Backup and DR agent chooses the user specified for one of the volumes and for the remaining it appends an underscore (_) followed by a number, for example, user _specified_ #.

  9. Select a single volume or multiple volumes from the **Select Volumes To Mount** section. By default, all volumes are selected, and the first volume cannot be deselected. For an individual file system there may be only one volume. Specify the **Storage Pool** , **Mount Drive** , and **Mount Point** for each volume you want to mount.

  10. Click **Submit**. A job is submitted to mount the LiveClone backup to the selected host. You can verify that the clone operation is successful by viewing the job status in **Monitor**. Once completed, the backup becomes active and is available for use.




## Delete a LiveClone

You can delete a LiveClone when you are done with it in order to recover storage space.

Use these instructions to delete a LiveClone:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application or VM that contains the LiveClone backup that you want to delete, then choose **Access** from the drop-down list at the bottom of the **Applications** page.

  3. Select the LiveClone backup, then select **Delete** from the list of access operations.

The **Delete** page opens.

  4. Click **Submit** to delete the LiveClone backup.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
