---
url: https://docs.cloud.google.com/compute/docs/disks/recover-vm/
title: Recover a VM with a corrupted or full disk \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T23:14:39.635138+00:00
---

# Recover a VM with a corrupted or full disk  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/recover-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Recover a VM with a corrupted or full disk Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

If your Compute Engine instance is inaccessible or doesn't boot because its boot disk is full or corrupted, then you can restore access by following the steps described in this document.

## Recovering an inaccessible VM or a full boot disk

If you can't connect to your instance, or your boot disk is full and you can't resize it, you must create an instance and recreate the boot disk from a snapshot to resize it. You must know the size of the boot disk you're recreating.

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.create` on the project to be able to create a new instance
  * `compute.disks.create` on the project to be able to create a new disk
  * `compute.disks.createSnapshot` on the disk
  * `compute.instances.attachDisk` on the new VM instance
  * `compute.disks.use` permission on the disk to attach



  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     1. Click the instance name to open the **VM instance details** page.
     2. Click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.
     3. In the **Boot disk** section, note the boot disk's size and name.
  2. In the Google Cloud console, go to the **Create a snapshot** page.

[Go to Create a snapshot](https://console.cloud.google.com/compute/snapshotsAdd)

     1. Enter a snapshot **Name**.
     2. Select the boot disk from the **Source disk** drop-down list.
     3. Click **Create**.
  3. In the Google Cloud console, go to the **Create an instance** page.

[Go to Create an instance](https://console.cloud.google.com/compute/instancesAdd)

  4. Enter the instance details.

  5. Create a new boot disk from the snapshot of the old boot disk.

     1. Under **Boot disk** , select **Change**.
     2. Select **Snapshots**.
     3. Select the snapshot of the old boot disk from the **Snapshot** drop-down list.
     4. Select the **Boot disk type**.
     5. Enter the new size for the disk.
     6. Click **Select** to confirm your disk options.
  6. Click **Create**.




## Recovering a corrupted VM

If a VM's OS is corrupted, you can retrieve the boot disk data to recover the VM. To recover the boot disk, you must first create a temporary VM using a [Google-provided image](https://docs.cloud.google.com/compute/docs/images), because the snapshot of the source VM might be corrupted.

To retrieve data from the VM, follow these steps:

  1. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots) from the boot disk of the source VM.
  2. [Create a temporary VM using a public image](https://docs.cloud.google.com/compute/docs/images#os-compute-support).
  3. Check if you're able to [connect to the temporary VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) using SSH.
  4. Add an additional disk to the temporary VM by following these steps:

     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Select the temporary VM that you created.

     3. Click edit **Edit**.

     4. Under **Additional disks** , click **Add new disk** , and then do the following:

        1. Add the disk name.
        2. For **Source type** , select the **Snapshot** tab.
        3. In the **Source snapshot** drop-down menu, select the snapshot of the source VM that you created earlier in these steps.
        4. Click **Done**.
     5. Click **Save**.

  5. Connect to the VM and mount the disk:

     * For Windows instances, follow the steps in [Format and mount a non-boot disk on a Windows VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows).

     * For Linux instances, follow these steps:

       1. [Connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#connecting_to_vms) using SSH.
       2. Check the disk and partitions in the VM and make a note of the disk name—for example `/dev/sdb1`:
              
              lsblk
              

The output is similar to the following:
              
              NAME   MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
              sda      8:0    0   10G  0 disk
              └─sda1   8:1    0   10G  0 part /
              sdb      8:16   0  100G  0 disk
              ├─sdb1   8:17   0   96G  0 part
              ├─sdb2   8:18   0    1K  0 part
              └─sdb5   8:21   0    4G  0 part
              

       3. Create a mount point at `/mnt/newdisk`:
              
              sudo mkdir /mnt/newdisk
              

       4. Mount the additional disk partition to the mount point `/mnt/newdisk`:
              
              sudo mount -o discard,defaults DISK_NAME /mnt/newdisk
              

Replace DISK_NAME with the disk name that you noted earlier in these steps—for example, `/dev/sdb1`.

The snapshot's file system is mounted at `/mnt/newdisk`. You can navigate the directories and retrieve data.




To create a VM with the recovered boot disk, follow these steps:

  1. [Create an image from the disk](https://docs.cloud.google.com/compute/docs/images/create-delete-deprecate-private-images#creating_a_custom_image) of the temporary VM.
  2. [Create a VM with the image](https://docs.cloud.google.com/compute/docs/instances/create-start-instance#create_a_vm_from_a_custom_image) of the temporary VM.



After the VM is created, you can transfer the recovered data to the VM. You incur costs for the temporary VM and the disk snapshot until you delete them. To delete these resources after you have recovered your data, see [Delete an instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance#delete_an_instance) and [Delete a snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot). 

## Recover a Windows VM that requires a BitLocker recovery key

If a Windows VM fails to boot or is restored from a snapshot and requires a BitLocker recovery key, then you can unlock the disk by attaching the disk to a temporary VM. To do so, follow these steps:

  1. Back up the disk by [taking a standard snapshot of the disk](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots).
  2. [Create a temporary Windows VM](https://docs.cloud.google.com/compute/docs/instances/create-vm-from-public-image) that's in the same zone as the failed VM.
  3. Attach the encrypted disk as a data disk to the temporary VM: 
     1. [Stop the failed VM](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#stop_an_instance).
     2. [Detach the boot disk from the failed VM](https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk#detach_disk).
     3. [Attach the boot disk as a secondary data disk](https://docs.cloud.google.com/compute/docs/disks/attach-disks#attach_disk) to the temporary VM.
  4. Connect to the temporary VM and mount the attached disk.
  5. [Retrieve the BitLocker recovery key from Active Directory](https://learn.microsoft.com/en-us/windows/security/operating-system-security/data-protection/bitlocker/recovery-process#helpdesk-recovery-in-active-directory-domain-services) using the BitLocker Recovery Password Viewer tool or PowerShell.
  6. Use the recovery key to [unlock the disk](https://learn.microsoft.com/en-us/windows-server/security/data-protection/encryption/manage-bde-commands).



You incur costs for the temporary VM and the disk snapshot until you delete them. To delete these resources after you have recovered your data, see [Delete an instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance#delete_an_instance) and [Delete a snapshot](https://docs.cloud.google.com/compute/docs/disks/manage-snapshots#delete_a_snapshot). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
