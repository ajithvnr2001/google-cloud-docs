---
url: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image/
title: Mount VMware VMs in the appliance management console \u00a0|\u00a0 Backup and DR \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:03.415353+00:00
---

# Mount VMware VMs in the appliance management console  |  Backup and DR  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Storage ](https://docs.cloud.google.com/docs/storage)
  * [ Backup and DR ](https://docs.cloud.google.com/backup-disaster-recovery/docs)
  * [ Guides ](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/backup-dr)



Send feedback 

#  Mount VMware VMs in the appliance management console Stay organized with collections  Save and categorize content based on your preferences. 

**Caution:** Support for backing up and restoring workloads managed using the legacy appliance management console is deprecated. For more information, see [Feature deprecations](https://docs.cloud.google.com/backup-disaster-recovery/docs/deprecations).

VMware VM backups can be accessed in either of two ways:

  * Mount to an existing host
  * Mount as a new VM



## Mount to an existing host

Mount a VMware image to an existing physical or virtual host. A virtual host is any VMware VM or Compute Engine instance added to the system through the discovery of applications. A physical host is any host added to the system from **Manage** > **Host** page. See instructions to [Add a host](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications).

**Note:** OnVault pools pointing to backup vaults don't support mount operations.

To mount a VMware VM backup to a host, follow these steps:

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the VMware application with the backup you want to mount, then choose **Access** from the menu at the bottom of the **Applications** page.

  3. The **Access** page opens listing backups using the timeline ramp view. For more information on the view, see [Access the timeline ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

  4. Select the backup, then select **Mount** from the list of access operations to open the **Mount** page.

  5. Leave the default setting to **Existing Host**.

  6. Select a physical host that is manually added from [**Manage** > **Host**](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications) page or virtual host from **Host** drop-down list. If you need a host that has not yet been added, add it from the [**Manage** > **Host**](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/manage-hosts-and-their-connected-applications) menu, or run Compute Engine or VMware discovery wizard.

  7. Enter a unique name associated with the mount in **Label**.

  8. In the selection for **Mount Mode** , select one of the following. These options only appear if the selected host is a VMware VM.

     * **NFS** : This is the preferred method. The VMDKs for the new VM is presented by the backup/recovery appliance to the ESX host using an NFS Datastore.
     * **vRDM (virtual raw device mapping)** : This presents the backups over iSCSI. Note that by default GCVE does not support iSCSI. VMware snapshots treat mounted vRDMs as **Independent** and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as **Dependent**. Although rarely used, when this option is enabled, vRDMs will be included in VMware snapshots. Backup templates can capture vRDMs marked as **Dependent**.
     * **pRDM (physical raw device mapping)** : This presents the backups over iSCSI. Note that by default GCVE does not support iSCSI.
**Note:** These options appear whenever the selected target host is a VMware VM. The default selection is determined based on your choices on the vCenter and the target VM itself. Either NFS or vRDM is the default based on those choices.
     1. From **Map to ESX Hosts** , select one of the following options:

        * **One** : Select **One** if you want to map only to the ESX host running the target VM.
        * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select choose the second host based on logical pairs of ESX hosts and always selects the partner ESX host for the one running the target VM.
        * **All.** Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job.

**Note:** You can see the **Map to ESX Hosts** option only when one or more target hosts are VMware VMs and when you have selected vRDM or pRDM in the **Mount Mode** field.
  9. Specify the following additional mount selections:

     * **Mount Drive** : Windows only. Specifies a drive letter to be assigned to the volume. If the drive letter is not available, the job fails. If multiple volumes are found, then it assigns subsequent drive letters. If no **Mount Drive** is specified, the Backup and DR agent chooses a drive letter itself, if available.
     * **Mount Point** : The full path at which you want to mount the volume. If the path exists as an empty folder, the Backup and DR agent uses it. If it does not exist, the Backup and DR agent creates it. If it exists as a file or as a folder that is not empty, then the job fails. If there are multiple volumes to be mounted, the Backup and DR agent chooses the user specified for one of the volumes and for the remaining it appends an underscore (_) followed by a number, for example, `user_specified_#`.
  10. From **Select Volumes To Mount** , select a single volume or multiple volumes. By default, all volumes are selected, and the first volume cannot be deselected. For an individual file system there may be only one volume. [Performance and consumption option](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/create-onvault-pool#balance_performance_and_consumption_for_onvault_images).

  11. For **Existing Host** option only, expand the **Scripts** section and apply post-scripts and post-scripts to the backup before mounting.

     * In the **Pre-Script** and **Post-Script** fields, enter the path and relative filenames. Enter the timeout values to prevent hanging, 300 seconds is a good default timeout value.
  12. If required, change the default **Storage pool** to be used for the mount from the drop-down list. This only applies to mounts where there is no existing staging disk, such as direct to OnVault and imported OnVault images. Otherwise the default pool where the source image disks are located are always used.

  13. Specify the **Mount Drive** and **Mount Point** for each volume you want to mount.

  14. Click **Submit**. A job is submitted to mount the backup to the selected host. You can verify that the mount operation is successful by viewing the job status in **Monitor**. Once the mount job is complete, the backup becomes active and is available in the [Active mounts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) view of the **App Manager**.




## Mount as a new VM

Rather than mount to an existing host, you can also create an entirely new VM using a backup. Use the instructions to mount a backup as a new VM.

  1. From the Backup and DR appliance management console, click **App Manager** and select **Applications** from the drop-down list.

The **Applications** page opens.

  2. Select the VMware application with the backup you want to mount, then choose **Access** from the menu at the bottom of the **Applications** page.

The **Access** page opens listing backups using the timeline ramp view. For more information on the view, see [Access the timeline ramp view](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/access-image-copy-data-list#access-time).

  3. Select a backup, then select **Mount** from the list of access operations.

The **Mount** page opens.

  4. Change the default setting to **New Virtual Machine**.

  5. Use the following selections to configure the virtual machine:

     * **VM Name** : Enter a name for the new VM that you want to mount.
     * **VCENTER** : Select a vCenter from the drop-down list for the new VM you want to mount.
     * **ESX HOST** : Select an ESX Host from the drop-down list for the new VM you want to mount.
     * **DATASTORE** : Select a datastore that has the required storage available from the drop-down list for the new VM you want to mount.

**Note:** The target backup/recovery appliance must write configuration data—known as the VMX file—and the VM swap file to the selected datastore.**Note:** When mounting as a new VM, the VM version, Guest Id, Number of CPUs, Memory, Hardware details are preserved. Backed up VMDK volumes are presented to the new VM using an NFS Datastore or as vRDM or pRDM disks using iSCSI.
  6. Enter a unique name associated with the mount in **Label**.

  7. For **Mount Mode** , select one of the following:

     * **NFS** : This is the preferred method. The VMDKs for the new VM will be presented by the backup/recovery appliance to the ESX host using an NFS Datastore.
     * **vRDM (virtual raw device mapping)** : This presents the backups over iSCSI. Note that by default GCVE does not support iSCSI. VMware snapshots treat mounted vRDMs as **Independent** and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Backup and DR does provide an option where you can mark vRDMs as **Dependent**. Although rarely used, when this option is enabled, vRDMs will be included in VMware snapshots. Backup templates will capture vRDMs marked as **Dependent**.
     * **pRDM (physical raw device mapping).** This presents the backups over iSCSI. Note that by default GCVE does not support iSCSI.
**Note:** These options appear whenever the selected target host is a VMware VM. The default selection is determined by user choices on the vCenter, and the target VM itself. Either NFS or vRDM is the default based on those choices.
  8. From **Map to ESX Hosts** , select one of the following options:

     * **One** : Select **One** if you want to map only to the ESX host running the target VM.
     * **Two** : Select **Two** if you want to map to two ESX hosts, but not all ESX hosts in the cluster. On selecting **Two** , you are given the option to choose the second host, or choose **Auto-select**. Auto-select choose the second host based on logical pairs of ESX hosts and always selects the partner ESX host for the one running the target VM.
     * **All** : Select **All** if you want to map to all the ESX hosts present in the cluster. Note that selecting **All** may increase the duration for the job.
**Note:** You can see the **Map to ESX Hosts** option only when one or more target hosts are VMware VMs and when you have selected vRDM or pRDM in the **Mount Mode** field.
  9. For **Mark Dependent** , VMware snapshots treat mounted vRDMs as **Independent** and are not included in snapshots. Because of this, by default, Backup and DR does not include vRDMs when protecting a mounted VM. Use this setting to mark vRDMs as **Dependent**. Although rarely used, when this option is enabled, vRDMs will be included in VMware snapshots. Backup templates will capture vRDMs marked as **Dependent**.

  10. If required, change the default storage pool to be used for the mount from the **Storage Pool** drop-down list.

This only applies to mounts where there is no existing staging disk, such as direct to OnVault and imported OnVault images, otherwise the pool where the source image disks are located always used regardless of what is set here.

  11. From **Select Volumes To Mount** , select a single volume or multiple volumes. By default, all volumes are selected, and the first volume cannot be deselected. For an individual file system there may be only one volume.

**Note:** The appliance management console assumes that the first volume of the VM is the boot volume. If the selected first volume is not the boot volume, contact support for further assistance.
  12. Click **Submit**. A job is submitted to mount the backup to the selected host. You can verify that the mount operation is successful by viewing the job status in **Monitor**. Once the mount job is complete, the backup becomes active and is available in the [Active mounts](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) view of the **App Manager**.




## Recover a mounted VMware VM to production storage

After you create a new VMware VM using mount as new VM, you have the option to migrate the VMs VMDK data onto the local datastore so that it is no longer dependent on the backup/recovery appliance. You can do this using the VMware migration function. Use the following instructions to migrate the VMs VMDK data onto the local datastore.

  1. First mount the VMware VM as a new VM or an existing VM.
  2. From the vSphere client, choose the datastore for the VMDK files and VM configuration files. For GCVE this would normally be the vSAN Datastore.
  3. From the vSphere client select the mounted VM you want to migrate and then use the **Migrate** function in the vSphere client to migrate the VM to the production storage:

Use the **Migrate** function in the vSphere client to migrate the VM to the production storage:

     * Select the option to change the storage. The new datastore cannot be the same as the source datastore.
     * Change the format of the virtual disk. Leaving it as **Same format as source** does not work. This option doesn't appear if you are migrating from NFS to vSAN Datastore.
**Note:** If both of the criteria are not met, you can have a very fast vMotion that only moves RDM files, or has no action because the source datastore and destination datastore are the same.
  4. After the migrate is completed, you can find the mount image in Active Mounts.




## Management of the active mounts

Once you have created a mount, you can track the backup from the **App Manager** > **Active Mounts**. Ideally, don't leave any image mounted indefinitely. This is because the backup that the mount was created from cannot expire until all its mounts have been deleted. When you have finished using the mounted image then either:

  * [Unmount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount) the backup. You can [remount](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#remount) it if needed. You can then [delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#delete) the backup later when you are certain it is no longer needed.
  * [Unmount and delete](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/manage-active-mounts#unmount-delete) the backup. This deletes the mounted image, not the backup that the mount is based on.



## The VMware administrator's guide

This page is one in a series of pages specific to protecting and recovering VMware VMs with Backup and DR. You can find additional information at:

  * [Backup and DR for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/concepts/vmware-intro)
  * [Configure Google Cloud VMware Engine for Backup and DR protection](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/prepare-vmware)
  * [Add vCenter and ESX server hosts to the appliance management console](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/add-vcenter-host)
  * [Discover and protect VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/discover-and-protect-vms)
  * [Apply a backup template to protect a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/create-plan/apply-backup-template-to-manage-a-VM)
  * [Configure Application settings for VMware VMs](https://docs.cloud.google.com/backup-disaster-recovery/docs/backup/configure-application-settings-for-vmware-vm)
  * [Restore a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/restore-data/restore-vm)
  * [Mount a VMware image](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/mount-vmware-image)
  * [Clone a backup of a VMware VM](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/clone-image-of-a-vm)
  * [Create LiveClone workflows](https://docs.cloud.google.com/backup-disaster-recovery/docs/access-data/create-liveclone-workflows)
  * [Move VM management between two backup/recovery appliances](https://docs.cloud.google.com/backup-disaster-recovery/docs/configuration/supported-vmware)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
