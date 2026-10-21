---
url: https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux/
title: Format and mount a non-boot disk on a Linux VM \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:29.426501+00:00
---

# Format and mount a non-boot disk on a Linux VM  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Format and mount a non-boot disk on a Linux VM Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

If you attached a new, blank Google Cloud Hyperdisk or Persistent Disk to your instance, before you can use it you must format and mount the disk. If you attached a disk that already contains data, then you must mount the disk before you can use it.

## Before you begin

  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




## Connect to the VM

  1. Go to the **VM instances** page.

[Go to the VM instances page](https://console.cloud.google.com/compute/instances)

  2. Click the **SSH** button next to the instance that has the new attached disk. The browser opens a terminal connection to the VM.




## Format a non-boot disk on a Linux VM

#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions): 

  * `compute.instances.setMetadata` on the instance, so that you can connect using SSH



If you are connecting to a VM instance that can run as a service account, you must also grant the `roles/iam.serviceAccountUser` role.

**Warning:** formatting a disk by following the steps in this section deletes all the data on the disk. Only format blank disks or disks that you're sure that you want to overwrite.

  1. In the terminal, use the [symlink](https://docs.cloud.google.com/compute/docs/disks/disk-symlinks) created for your attached disk to determine which device to format.
         
         ls -l /dev/disk/by-id/google-*
         

Unformatted disks don't have additional symlinks with `-partN` in the name.
         
         google-extra-scsi-disk -> ../../sdb
          google-instance-2 -> ../../sda
          google-instance-2-part1 -> ../../sda1
          google-instance-2-part14 -> ../../sda14
          google-instance-2-part15 -> ../../sda15
          google-local-nvme-ssd-0 -> ../../nvme0n1
          google-local-nvme-ssd-1 -> ../../nvme0n2
         

In this example, the new disk was created with the name `extra-scsi-disk`. The device name for the new disk is `sdb`.

  2. Verify that the [`mkfs.<type>`](http://manpages.ubuntu.com/manpages/xenial/man8/mkfs.8.html) utility is installed, where `<type>` is the file that system you want to use, like `xfs` or `ext4`.

For example, to format the disk with the `xfs` file system, `mkfs.xfs` must be installed on the operating system.

     1. To list which `mkfs` utilities are installed, run the following command:
            
            ls -l /usr/sbin/mkfs.*
            

The output is similar to the following:
            
            /usr/sbin/mkfs.bfs
            /usr/sbin/mkfs.cramfs
            /usr/sbin/mkfs.ext2 -> mke2fs
            /usr/sbin/mkfs.ext3 -> mke2fs
            /usr/sbin/mkfs.ext4 -> mke2fs
            /usr/sbin/mkfs.minix
            

In this example,`mkfs.xfs` isn't listed, so you can't format the disk with `xfs` unless you install `mkfs.xfs`.

     2. Optional: If the file system that you want to use isn't available, install it with the following command. For example, install `mkfs.xfs` with the following sample commands.

        * To install on Ubuntu and Debian: 
              
              sudo apt update && sudo apt install xfsprogs
              

        * To install on CentOS, Fedora, and Red Hat Enterprise Linux: 
              
              sudo yum install xfsprogs
              

  3. Format the disk with the appropriate `mkfs.<type>` command. This command **deletes** all data from the specified disk, so make sure that you specify the disk device correctly.

You can use any file format that you need, but we recommend a single `ext4` file system without a partition table. You can [increase the size of your disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk) later without having to modify disk partitions.

To maximize disk performance, use the [recommended formatting options](https://docs.cloud.google.com/compute/docs/disks/optimizing-pd-performance#formatting_parameters).

The following commands format the entire disk with no partition table.

     * **For`ext4`**, it is not necessary to reserve space for the root volume on this secondary disk, so specify `-m 0` to use all of the available disk space. Use the following command:
           
           $ sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/DEVICE_NAME
           

     * **For`xfs`**, specify `-s size=4096` to set the sector size to 4096 bytes for improved performance. Use the following command: 
           
           $ sudo mkfs.xfs -s size=4096 /dev/DEVICE_NAME
           

Replace `DEVICE_NAME` with the device name of the disk that you are formatting. For example, using the example output from the first step, you would use `sdb` for the device name.




## Mount the disk

  1. Create a directory that serves as the mount point for the new disk on the VM. You can use any directory. The following example creates a directory under `/mnt/disks/`.
         
         $ sudo mkdir -p /mnt/disks/MOUNT_DIR
         

Replace `MOUNT_DIR` with the directory at which to mount disk.

  2. Use the [mount tool](http://manpages.ubuntu.com/manpages/xenial/man8/mount.8.html) to mount the disk to the instance, and enable the `discard` option:
         
         $ sudo mount -o discard,defaults /dev/DEVICE_NAME /mnt/disks/MOUNT_DIR
         

Replace the following:

     * `DEVICE_NAME`: the device name of the disk to mount.
     * `MOUNT_DIR`: the directory in which to mount your disk.
  3. Configure read and write permissions on the disk. For this example, grant write access to the disk for all users.
         
         $ sudo chmod a+w /mnt/disks/MOUNT_DIR
         

Replace `MOUNT_DIR` with the directory where you mounted your disk.




### Configure automatic mounting on VM restart

Add the disk to your `/etc/fstab` file, so that the disk automatically mounts again when the VM restarts. On Linux operating systems, the _device name_ can change with each reboot, but the _device UUID_ always points to the same volume, even when you move disks between systems. Because of this, we recommend using the device UUID instead of the device name to configure automatic mounting on VM restart.

**Note:** If you use Container-Optimized OS, modifications to `/etc/fstab` don't persist across system reboots. To ensure the device is checked and mounted during boot, run the `fsck` and `mount` operations on the disk from your cloud-config's `bootcmd` section. See [Mounting and formatting disks](https://docs.cloud.google.com/container-optimized-os/docs/concepts/disks-and-filesystem#mounting_and_formatting_disks) in the Container-Optimized OS documentation.

  1. Create a backup of your current `/etc/fstab` file.
         
         $ sudo cp /etc/fstab /etc/fstab.backup
         

  2. Use the `blkid` command to list the UUID for the disk.
         
         $ sudo blkid /dev/DEVICE_NAME
         
         
         /dev/DEVICE_NAME: UUID="a9e1c14b-f06a-47eb-adb7-622226fee060" BLOCK_SIZE="4096"
         TYPE="ext4" PARTUUID="593b3b75-108f-bd41-823d-b7e87d2a04d1"
         

Replace the following:

     * `DEVICE_NAME`: the device name of the disk that you want to automatically mount. If you created a partition table on the disk, specify the partition that you want to mount by adding the suffix appended to the device name. For example, if `sdb` is the device name for the disk, `sdb1` might be the name for the partition.
  3. Open the `/etc/fstab` file in a text editor and create an entry that includes the UUID. For example:
         
         UUID=UUID_VALUE /mnt/disks/MOUNT_DIR FILE_SYSTEM_TYPE discard,MOUNT_OPTION 0 2
         

Replace the following:

     * `UUID_VALUE`: the UUID of the disk, listed in the output of the previous step
     * `MOUNT_DIR`: the directory where you mounted your disk
     * `FILE_SYSTEM_TYPE`: the file system type. For example, `ext2`, `ext3`, `ext4`, or `xfs`.
     * `MOUNT_OPTION`: specifies what the operating system does if it cannot mount the zonal persistent disk at boot time. For valid values, see **The fourth field** in the [Linux `fstab` documentation](https://man7.org/linux/man-pages/man5/fstab.5.html). To let the system boot even if the disk is unavailable, use the `nofail` mount option.
  4. Use the `cat` command to verify that your `/etc/fstab` entries are correct:
         
         $ cat /etc/fstab
         
         UUID=6B33-A686 /boot/efi vfat defaults 0 0
         UUID=UUID_VALUE /mnt/disks/MOUNT_DIR FILE_SYSTEM_TYPE discard,MOUNT_OPTION 0 2
         
         


**Caution:** When detaching a disk from a Linux VM, you **must** remove or comment out the corresponding entry in the `/etc/fstab` file. Not removing the entry won't cause immediate issues but will likely prevent the VM from booting successfully after a restart. The system might run without error until the next reboot. Even if you set `MOUNT_OPTION` to `nofail` or `nobootwait`, remove the entry before you create your boot disk snapshot or detach the disk.

## What's next

  * [Configure persistent device names](https://docs.cloud.google.com/compute/docs/disks/set-persistent-device-name-in-linux-vm) for your added disks.
  * Learn how to [resize your persistent disks](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).
  * Learn how to regularly [back up your disks using snapshots](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) to prevent unintended data loss.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
