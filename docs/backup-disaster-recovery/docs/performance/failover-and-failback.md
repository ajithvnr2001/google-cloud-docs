---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/performance/failover-and-failback/
title: Recover from a failover state in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:51.836027+00:00
---

# Recover from a failover state in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/performance/failover-and-failback/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Recover from a failover state in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

Based on your production to mirror requirements for replicating a copy of your data to a second backup/recovery appliance, you can execute the failover of a StreamSnap replication image to a mirrored data production site at a second backup/recovery appliance. Changes made at the DR site can be replicated back—failback—to your production environment at the local backup/recovery appliance.

  * Multiple syncback images can be used to replicate cumulative changes made at the DR site back to production.
  * Syncback images can be mounted, cloned, or restored at the production site to restore access.

**Note:** For background on production to mirroring replication, see [StreamSnap replication](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/policy-overview#prod-mirror).



## Test failover

After you configure a production to mirror replication policy to perform StreamSnap replication, and you then apply a backup template to manage an application or VM, you can test the failover to determine the readiness of the remote backup/recovery appliance. When you test a failover operation, a virtual copy of the most recently replicated image of the application is created and presented to the host that you select. You can log on to the host and verify that the image is consistent. Test failover mounts to the target without stopping replication.

**Note:** When a test failover occurs on the remote backup/recovery appliance, a staging VDisk is created to quickly mount up the latest snapshot. This staging VDisk can be mounted to a new VM on the remote site or to an existing VM.

Before performing a test failover, note the following usage considerations:

  * Ensure that the iSCSI port of the target host where the backup image is to be mounted is accessible by the remote appliance.
  * You can have only one image test-failed-over to one host at one time. For example, when a failover image is available on the remote appliance and the local appliance is managing hosts A and B, you can host the image on either A or B but not both.
  * You cannot failover a virtual machine application to the same virtual machine.
  * For VMware VM failover, you must have an ESX server and vCenter server up and running at the remote site to test failover.



Use these instructions to test failover on the remote appliance from the appliance management console:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application or VM that you want to failover, and then choose **Access** from the drop-down list at the bottom right corner of the page.

The **Access** page opens.

  3. Select a remote snapshot image and then select **Test Failover** from the list of operations.

The **Test Failover** page opens.

  4. Select **Test Failover** from the list of access operations.

**The Test Failover** page opens.

  5. Select a location to perform the test failover, either **Existing Host** or **New Virtual Machine**.

When failing over to an existing host, select **Existing Host** , select a host from **Host** drop-down list. The selected host must be a SAN host or a Virtual Machine on ESX Server that is connected to the appliance.

When failing over to a new VMware VM, select **New Virtual Machine** and make the following selections specific to the virtual machine.

**Note:** You can only failover a VM to a new VM.
     * **VM Name** : Enter a name for the new VM that you want to mount.
     * **VCENTER** : Select a vCenter from the drop-down list for the new VM you want to mount.
     * **ESX HOST** : Select an ESX Host from the drop-down list for the new VM you want to mount.
     * **DATASTORE** : Select a datastore that has the required storage available from the drop-down list for the new VM you want to mount.
  6. For **Mount Mode** , select one of the following:

     * **vRDM (virtual raw device mapping)** : By default vRDM mode is selected. VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option to mark vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates can capture vRDMs marked as **Dependent**.
     * **pRDM (physical raw device mapping)** : For file-level restore operations, select pRDM mode.

If you select pRDM the following additional mount selections appear:

     * **Mount Drive** : Specifies a drive letter to be assigned to the volume. If the drive letter is not available, the job fails. If multiple volumes are found, then it assigns subsequent drive letters. If no mount drive is specified, the Backup and DR agent chooses a drive letter itself, if available.
     * **Mount Point** : The full path at which you want to mount the volume. If the path exists as an empty folder, the Backup and DR agent uses it. If it does not exist, the Backup and DR agent can create it. If it exists as a file or as a folder that is not empty, then the job fails. If there are multiple volumes to be mounted, the Backup and DR agent chooses the user specified for one of the volumes and for the remaining volumes it appends an underscore (_) followed by a number—for example, user _specified_ #.

If you are mounting a generic application—LVM—you are given additional **Mapping Options**.

     * Select from the **Mount Action** drop-down menu to maintain the original folder structure—**Keep Source Path** —specify a specific location to mount the application—**Specify Mount Location** —or map the volumes to a host without mounting in to the file system—**Map Only**.
  7. If required, change the default **Storage pool** to be used for the mount from the drop-down list. This only applies to mounts where there is no existing staging disk, such as Direct to OnVault and imported OnVault images, otherwise the pool where the source image disks are located are always be used regardless of what is set here.

  8. Click **Continue**. The latest image of the application is used to create a virtual copy and presents it to the host you have selected. Since it is a virtual copy of the image, the host can use it without affecting the actual StreamSnap replication image.

  9. Open the **Monitor** service in the appliance management console to view the job status.

  10. When the job completes in the **Monitor** with the job status **Succeeded** , return to the **App Manager** and verify that the image was successfully mounted.

You can log onto the host, and view the failover image to ensure the consistency of data and your complete DR procedure.

  11. When you are satisfied with the failover test results, delete the active test failover image.




## Fail over a managed application or VM

At the time of failover, StreamSnap replication of the data from the local backup/recovery appliance is stopped to make use of the most recent copy of the application or VM image at the remote appliance. The most recent image of the data is made available as a snapshot to any available host. The backup/recovery appliance internally maintains another reference copy so the mounted snapshot can be used to write data as applications continue to run at the remote appliance.

While in the failed over state, the application or VM accesses the remote image directly, so replication to the remote backup/recovery appliance is paused. When the application or VM is ready to operate from the local appliance, you can syncback the data back to the local appliance and then perform a failback operation.

**Note:** Before performing a failover task, ensure that the iSCSI port of the host where the image is to be mounted is accessible to the remote appliance.

Use these instructions to failover a StreamSnap managed application or VM:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the application or VM that you want to failover, and then choose **Access** from the drop-down list at the bottom right corner of the page.

The **Access** page opens.

  3. Select a **Remote Snapshot** image. By default, the latest image is selected for failover.

  4. Select **Failover** from the list of access operations.

The **Failover** page opens.

  5. If you selected an application image to failover, select a host from **Host** drop-down list. The selected host must be a SAN host or a virtual machine on ESX server that is connected to the appliance.

  6. If you selected a VM image to failover, select a location to perform the failover, either **Existing Host** or **New Virtual Machine**.

If you select **Existing Host** , select a host from **Host** drop-down list. The selected host must be a SAN host or a virtual machine on ESX server that is connected to the appliance.

If you select **New Virtual Machine** , make the following selections specific to the virtual machine:

**Note:** You can only failover a VM to a new VM.
     * **VM Name** : Enter a name for the new VM that you want to mount.
     * **VCENTER** : Select a vCenter from the drop-down list for the new VM you want to mount.
     * **ESX HOST** : Select an ESX Host from the drop-down list for the new VM you want to mount.
     * **DATASTORE** : Select a datastore that has the required storage available from the drop-down list for the new VM you want to mount.
  7. For **Mount Mode** , select one of the following:

     * **vRDM (virtual raw device mapping)** : By default vRDM mode is selected. VMware snapshots treat mounted vRDMs as independent and are not included in snapshots. Because of this, by default, Backup and DR doesn't include vRDMs when protecting a mounted VM. Backup and DR does provide an option to vRDMs as dependent. Although rarely used, when this option is enabled, vRDMs are included in VMware snapshots. Backup templates capture vRDMs marked as dependent.
     * **pRDM (physical raw device mapping)** : For file-level restore operations, select this mode.
  8. If you select pRDM the following additional mount selections appear:

     * **Mount drive** : Specifies a drive letter to be assigned to the volume. If the drive letter is not available, the job fails. If multiple volumes are found, then it assigns subsequent drive letters. If no mount drive is specified, the Backup and DR agent chooses a drive letter itself, if available.
     * **Mount point** : The full path at which you want to mount the volume. If the path exists as an empty folder, the Backup and DR agent uses it. If it does not exist, the Backup and DR agent creates it. If it exists as a file or as a folder that is not empty, then the job fails. If there are multiple volumes to be mounted, the Backup and DR agent chooses the user specified for one of the volumes and for the remaining it appends an underscore (_) followed by a number—for example, user _specified_ #.
  9. If required, change the default **Storage pool** to be used for the mount from the drop-down list. This only applies to mounts where there is no existing staging disk, such as Direct to OnVault and imported OnVault images, otherwise the pool where the source image disks are located is always used regardless of what is set here.

  10. If required, enter a label for the failover operation.

  11. From **Map to ESX Hosts** , select one of the following options:

     * **One** : Select **One** if you want to map only to the ESX host that is running the target VM.
     * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select choose the second host based on logical pairs of ESX hosts and can always select the partner ESX host for the one that is running the target VM.
     * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job
**Note:** You will see the **Map to ESX Hosts** option only when one or more target hosts are VMware VMs and when you have selected vRDM or pRDM in the **Mount Mode** field.
  12. Click **Continue**.

A confirm failover warning message appears.

  13. Enter **FAILOVER** in the field to confirm the operation, then click **Failover**. A failover job is initiated. This job stops any replication job in progress for this application, and presents the latest replicated image to the selected host.

  14. Open the monitor service in the appliance management console to view the job status. When the job completes in the **Monitor** with the job status **Succeeded** , return to the **App Manager** and see that the image has been successfully mounted.

  15. Log onto the host, bring up the application, and direct all the external clients to use this copy of the application.

When you are ready to bring back the data generated at the remote site to the local site, start the failback from the remote appliance.




## Failback from the remote appliance to production

In a failover situation, users of the appliance management console might continue to use and generate data on the application but the Backup and DR application is running from a image on the remote site. After an application fails over to a remote backup/recovery appliance, you can failback the application to the local backup/recovery appliance.

Failback involves restoring the latest data from the backup image to the production application, restoring the application from the latest data, and then cleaning up. After failback, the application state changes to protected and the replication to the remote appliance resumes.

To minimize application downtime during a failback from the remote backup/recovery appliance back to the local appliance, follow these procedures in order.

  1. Perform a catch-up syncback
  2. Stop the failed-over application
  3. Perform the final syncback
  4. Restore a syncback image
  5. Failback to the local appliance
  6. Delete failover and syncback images



### Perform a catch-up syncback

At the time you begin the failback process, your users are accessing the application on the remote site. The first syncback copies all the data generated at the remote site since the failover to the local site. This first syncback can take some time depending upon how active the application is and how long it has been in a failover state.

To perform a syncback on the remote backup/recovery appliance, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the application or VM with the image you want to sync back, then choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing captured images in the timeline ramp view.

  3. From the **Access** window, select the image.

  4. Select **Syncback** from the list of operations.

The **Syncback** page opens.

  5. Optionally, enter a unique name associated with the syncback image in **Label**.

  6. Click **Submit**.

A syncback job is initiated.

  7. Go to the **System** to view the job status.

  8. When the job completes in the **Monitor** with the job status _Succeeded_ , return to the **App Manager**.

The newly generated data from the remote application is brought back to the local backup/recovery appliance, but it is not automatically applied to the original image of the application. Instead, it is made available on the local backup/recovery appliance as a syncback image in the **Access** window. You can mount, clone, or restore a synchronized image.

  9. The next step requires stopping the failed-over application during the restore operation.

If you are not yet ready to perform the restore operation, you can perform syncback operations until you are ready to failback. Each one creates a new syncback image on the local backup/recovery appliance. There is no limit to the number of times syncback can be carried out.




### Stop failed-over application

This step in the process marks the start of the time that the application is out of service. Stop the application on the remote site to prevent new data from coming in after the final syncback has begun. The application is out of service for the final syncback step and through the restoration step, coming back online at the end of the restoration step.

**Note:** If you do not require the remote data, you can skip directly to step five: Failback to the local appliance

After failback, the application state changes to **Managed** and the replication to the remote site is resumed.

### Perform the final syncback

Because the application is in service on the remote backup/recovery appliance, the data on the remote appliance may have changed during the catchup syncback. The final syncback is faster because it includes less data.

  1. Repeat the procedure outlined in Perform a catch-up syncback. The final data from the remote application is brought back to the local backup/recovery appliance.
  2. Restore the Syncback image as described in Restore a syncback image.



### Restore a syncback image

After synchronizing back the failed-over application or VM image, you may either perform a restore operation to put the data back to its original location or perform a mount operation to access the data more quickly. Note the following guidelines to assist in determining the ideal approach, based on data type and your needs.

  * For a non-VM application, we recommend that you perform a restore of the application data from the synchronized image instead of performing a mount operation—see Restore an application or VM syncback image. With non-VM application types, the subsequent copy back to production disk is a manual operation and typically needs to be performed while users doesn't require access to this data. In this case, an image restore is often the best choice. The restoration replaces the application's image in use prior to failover with the latest image that includes changes from the remote backup/recovery appliance.
  * For a VM, you have the following options:

    * You can perform a restore to bring the VM back to the original location, see Restore an application or VM syncback image. If a restore operation takes time for the data movement. During this time, the VM is offline. In this case, the network settings and MAC address are preserved when performing a restore because the operation updates the disks, instead of recreating the VM. Protection remains intact, but performs a low splash job during the next snapshot job due to the loss of VMware change back tracking data that results from any restore operation.

You can mount the VM to either a new VM or to an existing VM, see Mount a VM syncback image. This provides immediate access to the VM and its data without having to wait for a restore window. Note the following usage considerations if you intend to perform a mount operation for the VM: If you mount to an existing VM, If you get new disks in the existing VM, which may not be desirable for your environment. However, if you delete the original disks first you may be able to then boot from the VM and use Storage vMotion. In this case, the primary benefit is that the previous discovery and protection are retained. If you mount to a new VM, you can have a recoverable VM. You may want to manually update the MAC addresses to match the original VM so the network settings are preserved. You can then use storage vMotion to migrate the VM to a datastore. You have to re-discover and re-protect using this method.




To restore an application or VM syncback image, follow these steps: 

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the application or VM with the image you want to sync back, then choose **Access** from the drop-down list at the bottom of the Applications page.

The **Access** page opens listing captured images in the timeline ramp view.

Note the following considerations prior to restoring:

     * If you are restoring a non-VM application, be sure to shut down the application and unmount the file system.
     * If you are restoring a VM, the restore procedure automatically powers down the virtual machine.
  3. Select the latest syncback image, then select **Restore** from the list of access operations.

The **Restore** page opens.

  4. Click **Submit**. A warning dialog opens. Read it and then enter **DATA LOSS** to confirm. A second warning appears. Enter **OVERWRITE OTHER APPS** to confirm the restore operation.

The restore job starts.

  5. Go to the **Monitor** to verify that the restore operation is successful. When the job completes in the **Monitor** with the job status **Succeeded** , return to the **App Manager**.

  6. After the restore operation is completed successfully:

     * For a non-VM application, mount the file system and restart the application.
     * For a VM application, power on the virtual machine.
  7. The production application is back in service, but it is not yet managed again. Proceed to the failback operation, described in Failback to the local appliance.




## Failback to the local appliance

Failback deletes the syncback images brought back from the remote backup/recovery appliance and the failover image that may still be mounted on the remote backup/recovery appliance. Failback also deletes any test failover images that remain on the remote backup/recovery appliance. After these steps are complete, the application resumes the StreamSnap replication of the application data from the local appliance to the remote appliance.

Use these instructions to failback an application from the remote appliance to the local appliance.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the application or VM you want to fail back, then choose **Access** from the drop-down list at the bottom of the **Applications** page.

The **Access** page opens listing captured images in the timeline ramp view.

  3. Select the latest image and select **Failback** from the list of access operations.

The **Failback** page opens.

  4. Click **Submit**.

  5. Go to the **Monitor** to view the job status. When the job completes in the **Monitor** with the job status **Succeeded** , return to the **App Manager**.

  6. On successful fail-back, StreamSnap replication to the remote appliance resumes.

After failback, the application state changes to **Managed** and the replication to the remote site resumes.




## Mount a VM syncback image

Use these instructions to mount a VM syncback image.

  1. From the Backup and DR appliance management console, click the **App Manager** tab and select **Applications** from the drop-down menu.

The **Applications** page opens.

  2. Select the application or VM with the image you want to sync back.

  3. Choose **Access** from the drop-down list at the bottom of the Applications page.

The **Access** page opens listing captured images in the timeline ramp view.

  4. Select the latest sync-back image.

  5. Select **Mount** from the list of operations. The **Mount** window appears. For details on mounting a VM image, see [Mount images](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-images).

  6. Go to the **Monitor** to verify that the VM image mount operation is successful.

  7. After the VM image mount operation is completed successfully, power on the virtual machine, if necessary, and perform a **Storage vMotion** to move the mounted disks or VM to the datastore you want.

  8. If you mounted to a new VM, this VM must be discovered before it may be protected again. Follow the VM discovery procedure in [Discover VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms).

  9. The production VM is back in service, but it is not yet protected again. Proceed to the failback operation, described in Failback to the local appliance.




### Delete failover and syncback images

Normally, all failover, test-failover, and syncback images of an application are deleted when the fail-back operation is executed. In rare cases, some images created as part of StreamSnap replication of an application may not be deleted.

Use the following instructions to delete a failover, test-failover, or syncback image from the remote backup/recovery appliance.

  1. In the **Access** page, select the failover, test-failover, or syncback image that you want to delete, then select **Delete** from the drop-down list at the bottom right corner of the page.

**Note:** You can also right-click on the item in the list and select **Delete** from the menu.
  2. In the **Delete** dialog that opens, click **Submit** to confirm your changes.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
