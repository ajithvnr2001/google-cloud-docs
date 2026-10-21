---
url: https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage/
title: Attach durable block storage to a TPU VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T02:39:21.174170+00:00
---

# Attach durable block storage to a TPU VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Attach durable block storage to a TPU VM

**Caution:** This page applies to the Cloud TPU API, which is no longer under active development. The Cloud TPU API will receive bug fixes and security updates only. For the latest features and support for the latest TPU versions, we recommend using Compute Engine or Google Kubernetes Engine to manage TPU resources. For more information, see [TPU resources in Compute Engine](https://docs.cloud.google.com/tpu/docs/tpus-in-compute-engine) and [About TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus). The Cloud TPU API is not supported on TPU7x and later TPU versions. 

A TPU VM includes a 100 GiB boot disk. For some scenarios, your TPU VM might need additional storage for training or preprocessing. You can add a [ Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) or [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) (PD) volume to expand your local disk capacity.

For the highest performance and advanced features, Google recommends using Hyperdisk if it's available for your TPU. Otherwise, use Persistent Disk. For more information about block storage options in Compute Engine, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

## TPU support for Hyperdisk and Persistent Disk

The following table shows the supported disk types for each TPU version:

TPU version | Supported disk types | Maximum disks per VM   
(includes the boot disk)  
---|---|---  
TPU7x | Hyperdisk Balanced  
Hyperdisk ML | 128  
v6e | Hyperdisk Balanced  
Hyperdisk ML | 32  
v5p | Hyperdisk ML  
Balanced Persistent Disk | 128  
v5e | Hyperdisk ML  
Balanced Persistent Disk | 128  
v4 | Balanced Persistent Disk | 128  
v3 | Balanced Persistent Disk | 128  
v2 | Balanced Persistent Disk | 128  
  
## Access modes

You can configure a disk attached to a TPU in single-writer or read-only mode, as shown in the following table:

Access mode | Description | Value in the [Compute Engine API](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create#--access-mode) | Value in the [Cloud TPU API](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/attach-disk#mode) | Supported disk types  
---|---|---|---|---  
Single-writer mode | This is the default access mode. Allows the disk to be attached to at most one instance at any time. The instance has read-write access to the disk. | `READ_WRITE_SINGLE` | `read-write` | 

  * Hyperdisk Balanced
  * Hyperdisk ML
  * Balanced Persistent Disk

  
Read-only mode | Enables simultaneous attachments to multiple instances in read-only mode. Instances can't write to the disk in this mode. Required for read-only sharing. | `READ_ONLY_MANY` | `read-only` | 

  * Hyperdisk ML
  * Balanced Persistent Disk

  
  
You can configure a disk attached to a single-host TPU (for example, v6e-8, v5p-8, or v5litepod-8) in single-writer or read-only mode.

When you attach a disk to a multi-host TPU, the disk is attached to each VM in that TPU. To prevent two or more TPU VMs from writing to a disk at the same time, you must configure all disks attached to a multi-host TPU as read-only. Read-only disks are useful for storing a dataset for processing on a TPU slice.

**Note:** Because Hyperdisk Balanced doesn't support read-only mode, you can only attach a Hyperdisk Balanced volume to a single-host TPU.

## Prerequisites

You need to have a Google Cloud account and project set up before using the following procedures. For more information, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account).

## Create a disk

Use the following command to create a disk:
    
    
    $ gcloud compute disks create DISK_NAME \
        --size DISK_SIZE  \
        --zone ZONE \
        --type DISK_TYPE

#### Command flag descriptions

  * `DISK_NAME`: The name of the new disk.
  * `DISK_SIZE`: The size of the new disk. The value must be a whole number followed by a size unit of GB for gibibyte, or TB for tebibyte. If no size unit is specified, GB is assumed.
  * `ZONE`: The name of the [zone](https://docs.cloud.google.com/tpu/docs/types-zones) in which to create the new disk. This must be the same zone used to create the TPU.
  * `DISK_TYPE`: The [ type of disk](https://docs.cloud.google.com/compute/docs/disks#disk-types). Use one of the following values: `hyperdisk-balanced`, `hyperdisk-ml`, or `pd-balanced`.



For Hyperdisk, you can optionally specify the `--access-mode` flag with one of the following values:

  * `READ_WRITE_SINGLE`: Read-write access from one instance. This is the default.
  * `READ_ONLY_MANY`: (Hyperdisk ML only) Concurrent read-only access from multiple instances.



For more information about creating disks, see [Create a new Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk) and [Create a new Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk).

## Attach a disk

You can attach a disk volume to your TPU VM when you create the TPU VM, or you can attach one after the TPU VM is created.

### Attach a disk when you create a TPU VM

Use the `--data-disk` flag to attach a disk volume when you create a TPU VM.

If you are creating a multi-host TPU, you must specify `mode=read-only` ( Hyperdisk ML and Balanced Persistent Disk only). If you are creating a single-host TPU, you can specify `mode=read-only` ( Hyperdisk ML and Balanced Persistent Disk only) or `mode=read-write`. For more information, see Access modes.

The following example shows how to attach a disk volume when creating a TPU VM using [queued resources](https://docs.cloud.google.com/tpu/docs/queued-resources):
    
    
    $ gcloud compute tpus queued-resources create QR_NAME \
        --node-id=TPU_NAME
        --project PROJECT_ID \
        --zone=ZONE \
        --accelerator-type=ACCELERATOR_TYPE \
        --runtime-version=TPU_SOFTWARE_VERSION \
        --data-disk source=projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME,mode=MODE

#### Command flag descriptions

  * `QR_NAME`: The name of the queued resource request.
  * `TPU_NAME`: The name of the new TPU.
  * `PROJECT_ID`: The ID of the Google Cloud project in which to create the TPU.
  * `ZONE`: The name of the [zone](https://docs.cloud.google.com/tpu/docs/types-zones) in which to create the Cloud TPU.
  * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `TPU_SOFTWARE_VERSION`: The [TPU software version](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions).
  * `DISK_NAME`: The name of the disk to attach to the TPU VM.
  * `MODE`: The mode of the disk. Mode must be one of: `read-only` or `read-write`. If not specified, the default mode is `read-write`. For more information, see Access mode.



You can also attach a disk when you create a TPU VM using the [`gcloud compute tpus tpu-vm create`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/tpus/tpu-vm/create) command:
    
    
    $ gcloud compute tpus tpu-vm create TPU_NAME \
        --project PROJECT_ID \
        --zone=ZONE \
        --accelerator-type=ACCELERATOR_TYPE \
        --version=TPU_SOFTWARE_VERSION \
        --data-disk source=projects/PROJECT_ID/zones/ZONE/disks/DISK_NAME,mode=MODE

#### Command flag descriptions

  * `TPU_NAME`: The name of the new TPU.
  * `PROJECT_ID`: The ID of the Google Cloud project in which to create the TPU.
  * `ZONE`: The name of the [zone](https://docs.cloud.google.com/tpu/docs/types-zones) in which to create the Cloud TPU.
  * `ACCELERATOR_TYPE`: The accelerator type specifies the version and size of the Cloud TPU you want to create. For more information about supported accelerator types for each TPU version, see [TPU versions](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  * `TPU_SOFTWARE_VERSION`: The [TPU software version](https://docs.cloud.google.com/tpu/docs/supported-tpu-versions#tpu_software_versions).
  * `DISK_NAME`: The name of the disk to attach to the TPU VM.
  * `MODE`: The mode of the disk. Mode must be one of: `read-only` or `read-write`. If not specified, the default mode is `read-write`. For more information, see Access modes.



### Attach a disk to an existing TPU VM

Use the [`gcloud alpha compute tpus tpu-vm attach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/compute/tpus/tpu-vm/attach-disk) command to attach a disk to an existing TPU VM.
    
    
    $ gcloud alpha compute tpus tpu-vm attach-disk TPU_NAME \
        --zone=ZONE \
        --disk=DISK_NAME \
        --mode=MODE

#### Command flag descriptions

  * `TPU_NAME`: The name of the TPU.
  * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.
  * `DISK_NAME`: The name of the disk to attach to the TPU VM.
  * `MODE`: The mode of the disk. Mode must be one of: `read-only` or `read-write`. If not specified, the default mode is `read-write`. This must correspond with the access mode of the disk.



If your VM shuts down for any reason, you might need to mount the disk after you restart the VM. For information about enabling your disk to automatically mount on VM restart, see [Configure automatic mounting on system restart](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#configure_automatic_mounting_on_vm_restart).

For more information about automatically deleting a disk, see [Modify a disk's auto-delete setting](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete).

## Format and mount a disk

If you attached a new, blank disk to your TPU VM, before you can use it you must format and mount the disk. If you attached a disk that already contains data, then you must mount the disk before you can use it.

For more information about formatting and mounting a non-boot disk, see [Format and mount a non-boot disk on a Linux VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).

  1. Connect to your TPU VM using SSH:
         
         $ gcloud compute tpus tpu-vm ssh TPU_NAME --zone ZONE

If you are using a multi-host TPU this command will connect you to the first TPU in the TPU slice (also called worker 0).

  2. From the TPU VM, list the disks attached to the TPU VM:
         
         (vm)$ sudo lsblk

The output from the `lsblk` command looks similar to the following:
         
         NAME    MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT
         loop0     7:0    0  55.5M  1 loop /snap/core18/1997
         loop1     7:1    0  67.6M  1 loop /snap/lxd/20326
         loop2     7:2    0  32.3M  1 loop /snap/snapd/11588
         loop3     7:3    0  32.1M  1 loop /snap/snapd/11841
         loop4     7:4    0  55.4M  1 loop /snap/core18/2066
         sda       8:0    0   300G  0 disk
         ├─sda1    8:1    0 299.9G  0 part /
         ├─sda14   8:14   0     4M  0 part
         └─sda15   8:15   0   106M  0 part /boot/efi
         sdb       8:16   0    10G  0 disk
         

In this example, `sda` is the boot disk and `sdb` is the name of the newly attached disk. The name of the attached disk depends on how many disks are attached to the VM.

When using a multi-host TPU, you need to mount the disk on all TPU VMs in the TPU slice. The name of the disk should be the same for all TPU VMs, but it is not guaranteed. For example, if you detach and then re-attach the disk, the device name is incremented, changing from `sdb` to `sdc`.

  3. If the disk hasn't been formatted, format the attached disk using the [`mkfs` tool](https://manpages.ubuntu.com/manpages/xenial/man8/mkfs.8.html). Replace sdb if your disk has a different device name. Replace ext4 if you want to use a different file system.

**Caution:** This command deletes all data from the specified disk, so make sure that you specify the disk device correctly.
         
         (vm)$ sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb

  4. Create a directory to mount the disk on the TPU.

If you are using a single-host TPU, run the following command from your TPU to create a directory to mount the disk:
         
         (vm)$ sudo mkdir -p /mnt/disks/MOUNT_DIR

Replace MOUNT_DIR with the directory at which to mount disk.

If you are using a multi-host TPU, run the following command outside of your TPU VM. This command will create the directory on all TPU VMs in the TPU slice.
         
         (vm)$ gcloud compute tpus tpu-vm ssh TPU_NAME --worker=all --command="sudo mkdir -p /mnt/disks/MOUNT_DIR"

  5. Mount the disk to your TPU using the [`mount` tool](https://manpages.ubuntu.com/manpages/xenial/man8/mount.8.html).

If you are using a single-host TPU, run the following command to mount the disk on your TPU VM:
         
         (vm)$ sudo mount -o discard,defaults /dev/sdb /mnt/disks/MOUNT_DIR

If you are using a multi-host TPU, run the following command outside of your TPU VM. It will mount the disk on all TPU VMs in your TPU slice.
         
         (vm)$ gcloud compute tpus tpu-vm ssh TPU_NAME --worker=all --command="sudo mount -o discard,defaults /dev/sdb /mnt/disks/MOUNT_DIR"

  6. Configure read and write permissions on the disk. For example, the following command grants write access to the disk for all users.
         
         (vm)$ sudo chmod a+w /mnt/disks/MOUNT_DIR




## Unmount a disk

To unmount (detach) a disk from your TPU VM, run the following command:
    
    
    $ gcloud alpha compute tpus tpu-vm detach-disk TPU_NAME \
        --zone=ZONE \
        --disk=DISK_NAME

#### Command flag descriptions

  * `TPU_NAME`: The name of the TPU.
  * `ZONE`: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.
  * `DISK_NAME`: The name of the disk to detach from the TPU VM.



## Clean up

Delete your Cloud TPU and Compute Engine resources when you are done with them.

  1. Disconnect from the Cloud TPU, if you have not already done so:
         
         (vm)$ exit

Your prompt should now be `username@projectname`, showing you are in the Cloud Shell.

  2. Delete your Cloud TPU:
         
         $ gcloud compute tpus tpu-vm delete TPU_NAME \
             --zone=ZONE

  3. Verify that the Cloud TPU has been deleted. The deletion might take several minutes.
         
         $ gcloud compute tpus tpu-vm list --zone=ZONE

  4. Verify that the disk was automatically deleted when the TPU VM was deleted by listing all disks in the zone where you created the disk:
         
         $ gcloud compute disks list --filter="zone:( ZONE )"

If the disk wasn't deleted when the TPU VM was deleted, use the following command to delete it:
         
         $ gcloud compute disks delete DISK_NAME \
             --zone ZONE




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
