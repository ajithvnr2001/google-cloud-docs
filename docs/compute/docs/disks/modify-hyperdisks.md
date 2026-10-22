---
url: https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks/
title: Modify the size and provisioned performance of a Hyperdisk volume \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:49.359312+00:00
---

# Modify the size and provisioned performance of a Hyperdisk volume  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/modify-hyperdisks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Modify the size and provisioned performance of a Hyperdisk volume Stay organized with collections  Save and categorize content based on your preferences. 

You can modify the size and performance of your Google Cloud Hyperdisk volumes as your workload's needs change. For example, you can increase a volume's provisioned size to store more data. You can also reduce or increase the provisioned performance to reduce costs or increase performance, respectively.

This page discusses how to modify a Hyperdisk volume's provisioned size and performance.

To modify other properties of a Hyperdisk volume, see [Modify the settings for Persistent Disk or Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk).

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




### Required roles and permissions

To get the permission that you need to modify a Hyperdisk, ask your administrator to grant you the following IAM roles on the project: 

  * [Compute Instance Admin (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/compute#compute.instanceAdmin.v1) (`roles/compute.instanceAdmin.v1`)
  * To connect to a compute instance that can run as a service account: [Service Account User (v1) ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `compute.disks.update` permission, which is required to modify a Hyperdisk. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Access mode changes

To set the access mode for a Hyperdisk volume so that you can attach it to multiple instances, see [Access mode for Hyperdisk volumes](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#access_mode).

## Limitations

  * You can only increase the size of a Hyperdisk volume. You can't reduce the size of a Hyperdisk volume.
  * The size and performance that you specify must be within the ranges specified in Size limit and Performance limits, respectively.
  * There are limits to how often you can modify Hyperdisk size and performance, as follows:

    * Size modifications:

      * For Hyperdisk Throughput: once every 6 hours
      * For Hyperdisk Balanced and Hyperdisk Balanced High Availability: twice within a 4-hour window
      * For all other Hyperdisk types: once every 4 hours
    * Modifications to provisioned IOPS or throughput:

      * For Hyperdisk ML: once every 6 hours
      * For all other Hyperdisk types: once every 4 hours

If you try to modify a Hyperdisk volume more than once within the specified limits, then you see an error message like `Cannot update provisioned throughput due to being rate limited.`

  * If you increase the size of a Hyperdisk volume that is in multi-writer mode, then the following limitations apply:

    * You can't change the size of a Hyperdisk Balanced High Availability volume that's in multi-writer mode if any of the instances that the volume is attached to is in a zone that's experiencing an outage.
    * You can't use the Terraform provider for Google Cloud to change the size of the volume; you must use the Google Cloud console, gcloud CLI, or REST.
    * You must wait for the size change operation to complete before you attempt to access the disk from any of the attached instances.
    * Before you can use the added disk space, you must verify that the updated disk size is visible in all the instances that the disk is attached to.



## Best practices

Because there are limits to how often you can change disk properties, we recommend the following best practices:

  * We recommend that you modify size and performance at the same time. For example, if you plan to modify both a disk's size and provisioned IOPS within a short period, plan to make both changes in a single request.

  * When choosing a new value for a disk's provisioned performance or size, remember that you can't make any further changes until the required time has passed.

For example, suppose you want to increase the size of a 500 GiB Hyperdisk Balanced High Availability volume to 1 TiB. Ensure that your workload won't require more than 1 TiB of disk space within the next 4 hours, since you can't increase the size again until 4 hours have passed.




## Modifications to a Hyperdisk volume's size

You can increase the size of a Hyperdisk volume, but you can't directly decrease its size. To reduce the size of a Hyperdisk volume, replace the volume with a smaller one as described in Move data to a smaller Hyperdisk volume.

### Move data to a smaller Hyperdisk volume

You can't directly decrease the size of a Hyperdisk volume. If the provisioned size of a Hyperdisk volume volume is too large, then you must replace the volume with a new, smaller volume. To do so, create a blank volume that has a smaller size, then copy the contents from the original volume to the new volume. You can then use the new volume instead of the original.

To replace a volume with a smaller volume, follow these steps: 

  1. [Create a blank Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk) and specify the size you want. Make sure the new disk is large enough to contain the data from the source disk.
  2. Attach both volumes to the same instance. For instructions, see [Attach a non-boot disk to a VM](https://docs.cloud.google.com/compute/docs/disks/attach-disks).
  3. Format and mount the new volume. See the instructions for [Linux](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux) and [Windows](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-windows) instances.
  4. Copy the data from the original volume to the new volume using utilities available for your operating system (OS). For example, for Linux, you can use `rsync` or `dd`. For Windows instances, you can use `robocopy`.
  5. Verify that the new volume has all the data and is working as expected.
  6. Update your application or OS to use the new volume.
  7. After you confirm that the migration is successful, you can detach and delete the original, larger volume.

You are charged for the original volume until you delete it. 

### Prepare to increase the size of a Hyperdisk volume

You can resize, or increase the size of, a Hyperdisk volume even if it is attached to a running instance.

You can resize your Hyperdisk volumes at the following frequencies:

  * Hyperdisk Throughput: once every 6 hours
  * Hyperdisk Balanced and Hyperdisk Balanced High Availability: twice within a 4-hour window
  * All other Hyperdisk types: once every 4 hours



### Size limits for Hyperdisk volumes

The size that you specify for a Hyperdisk volume must be within the following ranges:

Disk type | Minimum size | Maximum size | Default size  
---|---|---|---  
Hyperdisk Balanced | 4 GiB | 64 TiB1 | 100 GiB  
Hyperdisk Balanced High Availability | 4 GiB | 64 TiB | 100 GiB  
Hyperdisk Extreme | 64 GiB | 64 TiB | 1 TiB  
Hyperdisk Throughput | 2 TiB | 32 TiB | 2 TiB  
Hyperdisk ML | 4 GiB | 64 TiB | 100 GiB  
1**[Preview](https://cloud.google.com/products#product-launch-stages)** : C4 supports a maximum disk size of 128 TiB. For access to this feature, contact [hyperdisk-questions@google.com](https://mail.google.com/mail/?view=cm&fs=1&tf=1&to=hyperdisk-questions@google.com). 

However, the total size of all the Hyperdisk volumes that's attached to an instance can't exceed the [ instance's Hyperdisk size and attachment limits](https://docs.cloud.google.com/compute/docs/disks/hyperdisk-perf-limits#limits-instance).

### Recommended process to increase a Hyperdisk volume's size

To increase the size of a Hyperdisk volume, follow these steps:

  1. Review the information in Best practices.
  2. Increase the size of the volume.
  3. Backup the volume.
  4. If the disk is in multi-writer mode, then verify that the updated size is visible to the guest OS of all the instances the disk is attached to.
  5. Resize the disk partitions. If the disk is in multi-writer mode, then you must resize the file system from one of the instances to which the disk is attached.



## Modifications to a Hyperdisk volume's provisioned performance

You can modify a volume's provisioned IOPS or throughput as your workload's needs change. For example, if you anticipate higher traffic for a period of time, you can increase the provisioned IOPS of your Hyperdisk volumes, and then reduce the provisioned performance at the end of the busy period.

You can change a volume's provisioned performance even if it is attached to a running instance. Changing the provisioned performance for a Hyperdisk volume doesn't affect the data on the disk.

The following table summarizes the supported performance changes for each Hyperdisk type.

Hyperdisk type | Customizable throughput | Customizable IOPS | Shareable between VMs  
---|---|---|---  
Hyperdisk Balanced | Yes | Yes | Yes  
Hyperdisk Balanced High Availability  
| Yes | Yes | Yes  
Hyperdisk Extreme | No | Yes | Yes  
Hyperdisk ML | Yes | No | Yes, in  
read-only mode  
Hyperdisk Throughput | Yes | No | No  
  
### Prepare to modify a Hyperdisk volume's provisioned performance

You can change the provisioned IOPS or throughput once every 4 hours for all Hyperdisk types except Hyperdisk ML. For Hyperdisk ML volumes, you can change the provisioned throughput once every 6 hours.

After you change the provisioned IOPS or throughput, it can take up to 15 minutes for the changes to take effect. However, the following exceptions apply:

  * For disks in multi-writer mode, performance changes can take up to 6 hours to become effective if the disk was attached to multiple VMs when you made the change.
  * For Hyperdisk ML volumes, it can take up to 20 minutes for the changes to take effect.
  * For all Hyperdisk types except Hyperdisk ML, you can change the provisioned IOPS or provisioned throughput once every 4 hours.
  * For Hyperdisk ML volumes, you can change the provisioned throughput once every 6 hours.
  * For Hyperdisk Balanced and Hyperdisk Balanced High Availability volumes, provisioned IOPS and throughput have separate cooldown periods. This means that if you change the provisioned IOPS at 10:00 AM, then you can still change throughput at 10:01 AM.



To modify a Hyperdisk's provisioned performance, follow the procedure in Increase a Hyperdisk's size or change its provisioned performance.

### Performance limits for Hyperdisk volumes

The following table lists the limits for the performance you can specify for each Hyperdisk type. However, the IOPS and throughput levels you can specify also depend on the volume's size. For a detailed summary of each limit, see the **Size and performance limits** section for [Hyperdisk Balanced](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced#size_limits), [Hyperdisk Balanced High Availability](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-balanced-ha#size_limits), [Hyperdisk Extreme](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-extreme#size_limits), [Hyperdisk ML](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-ml#size_limits), and [Hyperdisk Throughput](https://docs.cloud.google.com/compute/docs/disks/hd-types/hyperdisk-throughput#size_limits).

Hyperdisk type | IOPS limit | Throughput limit (MiB/s)  
---|---|---  
Hyperdisk Balanced | 160,000 | 2,400  
Hyperdisk Balanced High Availability | 100,000 | 2,400  
Hyperdisk Extreme | 350,000 |  You can't provision a throughput level for Hyperdisk Extreme volumes. Each volume gets 250 MiB/s of throughput with every 1,000 IOPS, up to 5,000 MiB/s.  
Hyperdisk ML | You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 16 IOPS, up to 33,554,432 IOPS. | 2,097,152  
Hyperdisk Throughput | You can't provision an IOPS level, but each MiB/s of provisioned throughput comes with 4 IOPS, up to 9,600 IOPS. | 2,400  
  
## Increase a Hyperdisk's size or change its provisioned performance

There are limits to how often you can modify Hyperdisk size and performance. Therefore, to avoid delays, review the Limitations and Best practices.

You can change the provisioned size and performance for a Hyperdisk volume with the Google Cloud console, gcloud CLI, or REST.

**Caution:** If you increase the size of a Hyperdisk volume that's in multi-writer mode, then you must wait for the operation to complete. Don't attempt to access the disk from the guest OS of any of the instances that the disk is attached to before the operation completes.

###  Console 

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. In the list of disks in your project, click the name of the Hyperdisk volume for which you want to change the size or provisioned performance.

  3. On the disk details page, click **Edit**.

     1. In the **Size** field, enter the new size for your disk. The disk size must be in the range of supported values.
     2. For Hyperdisk Extreme, Hyperdisk Balanced, and Hyperdisk Balanced High Availability: In the **Provisioned IOPS** field, enter the new IOPS value for your volume.
     3. For Hyperdisk Throughput, Hyperdisk ML, Hyperdisk Balanced, and Hyperdisk Balanced High Availability: In the **Provisioned throughput** field, enter the new throughput value for your volume.

The throughput and IOPS values you specify must be in the range of supported values.

  4. Click **Save** to apply your changes to the disk.




###  gcloud 

Use the [`disks update` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/update) and specify the `--size`, `--provisioned-iops`, or `--provisioned-throughput` flags.

To modify a zonal Hyperdisk volume, use the following command:
    
    
    gcloud compute disks update DISK_NAME  \
        --size=DISK_SIZE  \
        --zone=ZONE \
        --provisioned-iops=IOPS_LIMIT  \
        --provisioned-throughput=THROUGHPUT_LIMIT
    

Replace the following:

  * DISK_NAME: the name of the Hyperdisk volume that you are modifying.
  * DISK_SIZE: Optional: The new size of the disk. The value must be a whole number followed by a size unit of GB for gibibyte, or TB for tebibyte. The disk size must be in the range of supported values.
  * ZONE: Optional. The zone where the disk is located. Omit this flag for Hyperdisk Balanced High Availability volumes.
  * IOPS_LIMIT: Optional: The IOPS configuration for Hyperdisk Extreme, Hyperdisk Balanced, and Hyperdisk Balanced High Availability volumes. The value must be in the range of supported values.
  * THROUGHPUT_LIMIT: Optional: The throughput configuration for the Hyperdisk Throughput, Hyperdisk ML, Hyperdisk Balanced, or Hyperdisk Balanced High Availability volume, specified as an integer that represents the throughput measured in MiB per second. The value must be in the range of supported values.



To change the size of a Hyperdisk Balanced High Availability volume, include the `--region` flag instead of the `--zone` flag:
    
    
      gcloud compute disks update DISK_NAME  \
       --size=DISK_SIZE  \
       --region=REGION \
       --provisioned-iops=IOPS_LIMIT  \
       --provisioned-throughput=THROUGHPUT_LIMIT
    

Replace REGION with the region where the Hyperdisk Balanced High Availability volume, is located, for example, `us-central1`.

###  REST 

Construct a `PATCH` request to the [`compute.disks.update` method](https://docs.cloud.google.com/compute/docs/reference/rest/v1/disks/update). In the request body, specify the `sizeGb`, `provisionedIops` or `provisionedThroughput` parameters.
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME
    {
       "sizeGb": "DISK_SIZE,
       "provisionedIops": "IOPS_LIMIT",
       "provisionedThroughput": "THROUGHPUT_LIMIT"
    }
    

To modify a Hyperdisk Balanced High Availability volume, construct a `PATCH` request to the [`compute.regionDisks.update` method](https://docs.cloud.google.com/compute/docs/reference/v1/regionDisks/update).
    
    
    PATCH https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/regions/REGION/disks/DISK_NAME
    {
       "sizeGb": "DISK_SIZE,
       "provisionedIops": "IOPS_LIMIT",
       "provisionedThroughput": "THROUGHPUT_LIMIT"
    }
    

Replace the following:

  * `PROJECT_ID`: your project ID.
  * `ZONE`: the zone where your Hyperdisk volume is located.
  * `REGION`: For Hyperdisk Balanced High Availability disks, this is the region where the disk is located.
  * `DISK_NAME`: the name of the Hyperdisk volume to modify.
  * `DISK_SIZE`: Optional: The new size of the disk. The value must be a whole number followed by a size unit of GB for gibibyte, or TB for tebibyte. The disk size must be in the range of supported values.
  * `IOPS_LIMIT`: Optional: The IOPS configuration for the Hyperdisk Extreme, Hyperdisk Balanced, or Hyperdisk Balanced High Availability volume. The value must be in the range of supported values.
  * `THROUGHPUT_LIMIT`: Optional: The throughput configuration for the Hyperdisk Balanced, Hyperdisk ML, Hyperdisk Balanced, or Hyperdisk Balanced High Availability volume, specified as an integer that represents the throughput measured in MiB per second. The value must be in the range of supported values.



Before you can use the added space, follow these steps:

  1. Back up the disk.
  2. If the disk is in multi-writer mode, then verify that the updated size is visible to the guest OS of all the instances the disk is attached to.
  3. Resize the disk partitions. If the disk is in multi-writer mode, then you must resize the file system from one of the instances to which the disk is attached.



## Back up the Hyperdisk volume

Resizing a disk doesn't delete or modify disk data, but as a best practice, always backup your disk by [creating a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) before you make any changes to the file system or partitions.

## Resize the file system and partitions

After you increase the size of a disk, you might need to resize both the file system and partitions. The following is additional information for boot and non-boot disks:

  * **Boot disks** : If you're using [a custom Linux image](https://docs.cloud.google.com/compute/docs/images/create-custom), [custom Windows image](https://docs.cloud.google.com/compute/docs/instances/windows/creating-windows-os-image), or a [Fedora CoreOS image](https://docs.cloud.google.com/compute/docs/images/os-details#fedora_coreos), you must manually resize the root partition and file system. For instances with [public images](https://docs.cloud.google.com/compute/docs/images) (except for Fedora CoreOS images), Compute Engine automatically resizes the root partition and file system after you increase the size of the boot disk and you don't need to restart the instance.

  * **Non-boot disks** : After increasing the size of the disk, you must extend the file system on the disk to use the added space.




If the disk is a Hyperdisk volume that's in multi-writer mode, then you must follow these steps before you resize the partition and file system:

  1. Wait for the change operation to complete. For example, if you used the gcloud CLI to change the disk size, wait for the operation to complete.
  2. Connect to each instance to verify that the updated disk size is visible to the OS. If you resize the file system before all the instances have registered the updated disk size, you might lose or corrupt your data. After you verify the updated disk size, you can resize the file system.
  3. Resize the file system from one of the instances following the instructions in this section.



The following examples shows how to manually resize the root partition and file system of a boot disk, and how to manually resize the file system of a non-boot data disk with no partition table. Both examples assume that the attached disks were previously formatted and mounted.

###  Linux instances 

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Find the instance that the disk that you resized is attached to. Click **SSH**. The browser opens a terminal connection to the instance.

  3. Use the `df` and `lsblk` commands to list the size of the file system and find the device names for your disks.
         
         $ sudo df -Th
         
         Filesystem      Type      Size  Used Avail Use% Mounted on
         udev            devtmpfs  3.9G     0  3.9G   0% /dev
         /dev/nvme0n1p1  ext4      9.7G  2.0G  7.2G  22% /
         /dev/nvme0n1p15 vfat      124M   12M  113M  10% /boot/efi
         /dev/nvme0n2    ext4       98G   24K   98G   1% /mnt/disks/data
         
         
         
         $ sudo lsblk
         
         NAME        MAJ:MIN   RM  SIZE RO TYPE MOUNTPOINT
         nvme0n1      259:0    0   20G  0 disk
         ├─nvme0n1p1  259:5    0  9.9G  0 part /
         ├─nvme0n1p14 259:6    0    3M  0 part
         └─nvme0n1p15 259:7    0  124M  0 part /boot/efi
         nvme0n2      259:4    0  100G  0 disk /mnt/disks/data
         
         

This example includes the following disks:

     * **Boot disk** : The `/dev/nvme0n1p1` partition is on a boot disk that has been resized to 20 GB. The partition table and the file system provide only 9.9 GB to the operating system.
     * **Non-boot data disk** : The `/dev/nvme0n2` non-boot data disk has no partition table, but the file system on that disk provides 100 GB to the operating system. The mount directory for this disk is `/mnt/disks/data`.

Make note of the **Type** column in the `df` command output, which indicates if your disk uses an `ext4` or `xfs` file system.

**Note:** This example assumes the disk is attached to the instance using the NVMe interface. If the disk is attached using the SCSI interface, the partition names for a single disk are of the form `/dev/sda1`, `/dev/sda2`, and not `/dev/nvme0n1p1`, `/dev/nvme0n1p14`.
  4. Verify the partition type: 
         
         sudo parted -l
         

The first time you run this command after resizing a disk, you might see a message similar to the following:
         
         Warning: Not all of the space available to /dev/nvme0n1 appears to be
         used, you can fix the GPT to use all of the space (an extra 20971520
         blocks) or continue with the current setting?
         Fix/Ignore?
         

If you enter `Fix`, the OS will automatically repartition the disk to make the additional space available to the OS. Skip ahead to the last step if you don't have any additional disks to modify.

  5. If you choose not to use the automatic fix option, or it isn't available, view the information for the disk you want to repartition:
         
         sudo parted -l /dev/DEVICE_NAME
         

Look for field: **Partition Table** , if the value is **`msdos`** then the disk has an MBR partition type. This means the maximum size of such a disk would be 2 TB.

  6. For a boot disk, resize the root partition and file system on the disk. This example assumes the VM image does not support automatic root partitioning and file system resizing.

     1. Resize the root partition by using `parted`. For example, the following commands expand partition 1 of the device to the maximum possible size:

        1. Open `parted` on the device:
               
               sudo parted /dev/DEVICE_NAME
               

Replace `DEVICE_NAME` with the device name for the boot disk, for example, `nvme0n1`

        2. At the prompt, enter:
               
               (parted) resizepart
               

        3. At the `Partition number?` prompt, enter:
               
               1
               

        4. At the `Warning: Partition /dev/DEVICE_NAMEp1 is being used. Are you sure you want to continue?` prompt, enter:
               
               Yes
               

        5. At the `End?` prompt, enter
               
               100%
               

        6. At the `(parted)` prompt, enter:
               
               (parted) quit
               

     2. View the new partition table using `parted -l`.
            
            sudo parted -l /dev/DEVICE_NAME
            
            Model: nvme_card-pd (nvme)
            Disk /dev/DEVICE_NAME: 21.5GB
            Sector size (logical/physical): 512B/512B
            Partition Table: gpt
            Disk Flags:
            
            Number  Start   End     Size    File system  Name  Flags
            14      1049kB  4194kB  3146kB                     bios_grub
            15      4194kB  134MB   130MB   fat16              boot, esp
            1       134MB   21.5GB  21.3GB  ext4
            

     3. Extend the file system:

        * If you are using `ext4`, then use the `resize2fs` command:
              
              sudo resize2fs /dev/PARTITION_NAME
              

Replace `PARTITION_NAME` with the partition name for the boot disk, for example, `nvme0n1p1`.

        * If you are using `xfs`, then use the `xfs_growfs` command:
              
              sudo xfs_growfs -d /
              

        * If you are using [btrfs](https://en.wikipedia.org/wiki/Btrfs), then use the `btrfs` command:
              
              sudo btrfs filesystem resize max /
              

  7. For a non-boot data disk, resize the file system on the disk.

     * If you are using `ext4`, then use the `resize2fs` command to extend the file system:
           
           sudo resize2fs /dev/PARTITION_NAME
           

Replace `PARTITION_NAME` with the partition name for the data disk. In this example, the partition name is `/dev/nvme0n2p1`.

     * If you are using `xfs`, use the `xfs_growfs` command to extend the file system:
           
           sudo xfs_growfs MOUNT_DIR
           

     * If you are using [btrfs](https://en.wikipedia.org/wiki/Btrfs), use the `btrfs` command to extend the file system:
           
           sudo btrfs filesystem resize max MOUNT_DIR
           

Replace MOUNT_DIR with the mount point of the device. You can find the mount point listed in the `MOUNTPOINT` column in the output of the `lsblk` command.

  8. Use the `df` command to verify that the file system is extended. For example:
         
         df -h /dev/PARTITION_NAME
         
         Filesystem       Size  Used  Avail    Use%     Mounted on
         /dev/nvme0n2p1   118G  70M   118G     1%     /mnt/disks/data
         




###  Windows VMs 

Use the [Windows Disk Management utility](https://learn.microsoft.com/windows-server/storage/disk-management/overview-of-disk-management) to resize partitions on a Windows instance.

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Find the instance that has the resized disk. Click the **RDP** button for the instance. The browser opens an RDP connection to the instance.

  3. Right-click the Windows Start button and select **Disk Management** to open the **Disk Management** tool.

![Selecting the Windows Disk Manager tool from the right-click menu on the Windows Start button.](https://docs.cloud.google.com/static/compute/images/start_disk_manager_windows.png)

  4. Show the disks partition type by running the following command in Powershell: 
         
         Get-Disk
         

In the **Partition Style** column, if the value is **MBR** then the disk has an MBR partition type. This means the _maximum size of such a disk would be 2 TB_.

  5. Refresh the **Disk Management** tool so that it recognizes the additional space on the disk. At the top of the **Disk Management** window, click **Action** and select **Refresh**.

![Clicking the Action menu and selecting Refresh to update the disk information in the Disk Management tool.](https://docs.cloud.google.com/static/compute/images/rescan_volumes_windows.png)

  6. On the disk that you resized, right-click the formatted partition and select **Extend Volume**.

![Right-clicking the formatted portion of the disk and selecting the Extend Volume option.](https://docs.cloud.google.com/static/compute/images/pd_extend_volume_windows.png)

  7. Follow the instructions in the **Extend Volume Wizard** to extend your existing partition to include the extra disk space. If the existing partition is formatted in NTFS, then the maximum partition size is [limited by its cluster size settings](https://learn.microsoft.com/en-us/windows-server/storage/file-server/ntfs-overview).

  8. After you complete the **Extend Volume Wizard** and the volume finishes formatting, check the **Status** column on the list of attached disks to ensure that the new disk has a **Healthy** status.

![Viewing the list of disks that are recognized by Windows, verify that the instance is Online with a Healthy status.](https://docs.cloud.google.com/static/compute/images/pd_healthy_windows.png)




You don't need to restart your instance after you complete this process. You can now use the added disk space.

## What's next

  * Learn more about [Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks).
  * Learn how to [analyze the current IOPS level](https://docs.cloud.google.com/compute/docs/disks/analyze-iops-hyperdisk) for a Hyperdisk volume.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
