---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm/
title: Rescue an inaccessible VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:59.729774+00:00
---

# Rescue an inaccessible VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/rescue-vm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Rescue an inaccessible VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

If your Linux VM is inaccessible due to any reason, you can try rescue the VM using the following steps.

To identify why a compute instance fails to boot before you rescue it, see [Troubleshoot Linux Compute Engine instance boot issues](https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-linux-boot-issues).

## Required roles

To get the permissions that you need to rescue a VM, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * VMs that use a service account: [Service account user ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to rescue a VM. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to rescue a VM:

  * `compute.instances.create` on project
  * `compute.disks.create` on project
  * `compute.instances.get` on project
  * `compute.disks.createSnapshot` on disks
  * `compute.instances.attachDisk` on new VM
  * `compute.disks.use` on disk
  * `compute.instances.start` on new and inaccessible VM
  * `compute.instances.stop` on new and inaccessible VM



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Rescue a VM

If you can't connect to your VM, or your boot disk is full, you must create a temporary VM to rescue the inaccessible VM.

  1. (Optional) Stop the inaccessible VM.
  2. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots) from the boot disk of the inaccessible VM. If the root file system is split across multiple disks, you must snapshot each disk.
  3. [Create a temporary VM using a public image closest to inaccessible VM's OS](https://docs.cloud.google.com/compute/docs/images#list_of_public_images_available_on). In some cases a trusted image policy might restrict you from creating boot disks from public images. In such cases you must ask an administrator to temporarily lift this restriction before you can create a rescue VM. See [Set image access constraints](https://docs.cloud.google.com/compute/docs/images/restricting-image-access#trusted_images) for more information.
  4. For each of the snapshots of the inaccessible VM's boot disks you previously created, create a new disk from the snapshot and attach it to the rescue VM by following these steps:

**Caution:** Before proceeding, ensure that the rescue VM is running. If you attach the inaccessible VM's boot disk before starting the rescue VM, the rescue VM might fail to start because of conflicting disk labels.
     1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     2. Click the name of the temporary VM that you created.

     3. Click edit **Edit**.

     4. Under **Additional disks** , click add**Add new disk** , and then do the following:

        1. Add the disk name, like my-recovery-disk
        2. For **Source type** , select the **Snapshot** tab.
        3. In the **Source snapshot** drop-down menu, select the snapshot of the source VM that you created earlier in these steps.
        4. Click **Done**.
     5. Click **Save**.

  5. [Connect to the temporary VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#connecting_to_vms) using SSH.

  6. Identify the name of each of the disks that you previously attached to the VM by running the following command:
         
         lsblk -d -o NAME,SERIAL

The output is similar to the following:
         
         NAME SERIAL
          sda  rescue-vm
          sdb  my-recovery-disk
          

In this example, `rescue-vm` is the boot disk of the rescue VM and `my-recovery-disk` is the boot disk from the snapshot of the inaccessible VM. Note the `NAME` of the inaccessible VM for use in the next step.

  7. For each of the disks that you previously attached to the VM, do the following:

     1. Identify the file system of each partition by running the following command:
            
            fdisk -l /dev/NAME -o Device,Size,Type
            

Replace `NAME` with the name of the inaccessible VM's boot disk from the previous step. In this example, the name would be `sdb`.

The output is similar to the following:
            
            Disk /dev/sdb: 10 GiB, 10737418240 bytes, 20971520 sectors
            Disk model: PersistentDisk
            Units: sectors of 1 * 512 = 512 bytes
            Sector size (logical/physical): 512 bytes / 4096 bytes
            I/O size (minimum/optimal): 4096 bytes / 4096 bytes
            Disklabel type: gpt
            Disk identifier: B31430F1-F041-4555-96B9-B2F43DC057AD
            
            Device     Size Type
            /dev/sdb1    2M BIOS boot
            /dev/sdb2   20M EFI System
            /dev/sdb3   10G Linux filesystem
            

The `Type` column lists the file system of each partition. If the file system type is missing for any partitions, run the following command:
            
            file -sL /dev/PARTITION_NAME
            

Replace `NAME` with the name of the partition.

The output differs depending on the file system type:

        * **No file system** : If the output only displays `data`, the partition doesn't contain a file system. Example output:
              
              /dev/sdb1: data
              

        * **EFI file system** : If the output describes a DOS/MBR boot sector, the partition has an EFI file system. Example output:
              
              dev/sdb2: DOS/MBR boot sector, code offset 0x3c+2, OEM-ID "mkfs.fat", sectors/cluster 4, reserved sectors
              4, root entries 512, sectors 40960 (volumes <=32 MB), Media descriptor 0xf8, sectors/FAT 40, sectors/
              track 32, heads 64, serial number 0xf2af2664, label: "EFI        ", FAT (16 bit)
              

        * **Linux file system** : If the output describes file system data, the partition is a Linux file system. Example output:
              
              /dev/sdb3: SGI XFS filesystem data (blksz 4096, inosz 512, v2 dirs)
              

Note the partition name of the Linux file system.

     2. Create a mount point at `/rescue`:
            
            sudo mkdir /rescue

     3. Mount the Linux file system partition to `/rescue`:
            
            sudo mount PARTITION_NAME /rescue
            

Replace PARTITION_NAME with the name of the Linux file system you previously noted.

     4. Mount the virtual file systems and devices so that you can modify the root directory of the file system by using the `chroot` command:
            
            sudo mount -t proc /proc /rescue/proc
            sudo mount -t sysfs /sys /rescue/sys
            sudo mount -o bind /dev /rescue/dev
            sudo mount -o bind /dev/pts /rescue/dev/pts
            sudo mount -o bind /run /rescue/run
            

     5. Change the root directory to the mounted file system:
            
            sudo chroot /rescue
            

The file system of the inaccessible boot disk is now mounted at `/rescue`, and your shell runs in a `chroot` environment on that file system. You can navigate the file system, change configuration files, fix issues, or retrieve data.




## Revert the changes and restart the inaccessible VM

After you fix the issue or retrieve your data, use the following steps to restore the original VM:

  1. After you finish troubleshooting, exit the `chroot` environment:
         
         exit
          

  2. Unmount the virtual file systems, devices, and the file system of the inaccessible VM from the temporary VM:
         
         cd /
          sudo umount /rescue/run
          sudo umount /rescue/dev/pts
          sudo umount /rescue/dev
          sudo umount /rescue/sys
          sudo umount /rescue/proc
          sudo umount /rescue
          

  3. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     1. Select the temporary VM that you created.

     2. Click edit**Edit**.

     3. Under **Additional disks** , click close for the disk created in earlier steps to detach the additional disk from the temporary VM.

     4. Click **Save**.

  4. Go to the **VM instances** page in the Google Cloud console.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

     1. If the inaccessible VM is still running, [stop the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).

     2. Click the name of the VM you just stopped, and then click edit**Edit**.

     3. Under **Boot disk** , click close **Detach book disk** to detach the exiting boot disk from the inaccessible VM.

     4. Next, click edit **CONFIGURE BOOT DISK** to attach the disk you created and fixed previously in Rescue a VM on this page.

        1. In the **Boot Disk** section, click the **Existing disks** tab.
        2. In the drop-down list, select the disk that you created in the previous section, for example `my-recovery-disk`.
        3. Click **Select** and then click **Save**.
     5. [Start the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#starting_a_stopped_instance).

  5. You should now be able to [connect to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance#connecting_to_vms) using SSH. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
