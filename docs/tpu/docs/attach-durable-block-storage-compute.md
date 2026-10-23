---
url: https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute/
title: Attach durable block storage to a TPU VM \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:36:26.276771+00:00
---

# Attach durable block storage to a TPU VM  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/attach-durable-block-storage-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Attach durable block storage to a TPU VM

A TPU VM includes a 10 GB boot disk. Some scenarios require additional storage for training or preprocessing. Add a [Google Cloud Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/hyperdisks) or a [Persistent Disk](https://docs.cloud.google.com/compute/docs/disks/persistent-disks) (PD) volume to expand local disk capacity.

For the highest performance and advanced features, use Hyperdisk if it is available for your TPU version. Otherwise, use Persistent Disk. For more information about block storage options in Compute Engine, see [Choose a disk type](https://docs.cloud.google.com/compute/docs/disks).

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
  
## Access modes

Configure a disk attached to a single TPU VM (also called a single-host TPU slice), for example, `ct6e-standard-4t`, in read-write (`rw`) or read-only (`ro`) mode.

When you attach a disk to a multi-host TPU slice, the disk attaches to each VM in the slice. To prevent multiple TPU VMs from writing to a disk simultaneously, you must configure all disks attached to a multi-host TPU slice as read-only (`ro`). Read-only disks are useful for storing a dataset for processing on a TPU slice.

**Note:** Because Hyperdisk Balanced doesn't support read-only mode, you can only attach a Hyperdisk Balanced volume to a single TPU VM.

## Prerequisites

Before using these procedures, set up a Google Cloud account and project. For more information, see [Set up the Cloud TPU environment](https://docs.cloud.google.com/tpu/docs/setup-gcp-account-compute).

## Create a disk

To create a disk, use the following command:
    
    
    gcloud compute disks create DISK_NAME \
        --size DISK_SIZE  \
        --zone ZONE \
        --type DISK_TYPE
    

Replace the following placeholders:

  * DISK_NAME: The name of the new disk.
  * DISK_SIZE: The size of the new disk. The value must be a whole number followed by a size unit of GB for gibibyte, or TB for tebibyte. If you don't specify a size unit, the system assumes GB.
  * ZONE: The name of the [zone](https://docs.cloud.google.com/tpu/docs/types-zones) in which to create the new disk. This must be the same zone where you create the TPU.
  * DISK_TYPE: The [type of disk](https://docs.cloud.google.com/compute/docs/disks#disk-types). Use one of these values: `hyperdisk-balanced`, `hyperdisk-ml`, or `pd-balanced`.



For Hyperdisk, you can optionally specify the `--access-mode` flag with one of these values:

  * READ_WRITE_SINGLE: Read-write access from one instance (default).
  * READ_ONLY_MANY: (Hyperdisk ML only) Concurrent read-only access from multiple instances.



For more information about creating disks, see [Create a new Hyperdisk volume](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk) and [Create a new Persistent Disk volume](https://docs.cloud.google.com/compute/docs/disks/add-persistent-disk).

## Attach a disk

Attach a disk volume to your TPU VM or slice when you create it, or attach one after creation.

### Attach a disk when you create a TPU VM

When you create a TPU VM or instance template, use the `--disk` flag to attach a disk volume.

#### Attach a disk when creating a single TPU VM

The following example shows how to attach a disk volume when you create a single TPU VM:
    
    
      gcloud compute instances create TPU_NAME \
        --machine-type=MACHINE_TYPE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --zone=ZONE \
        --maintenance-policy=TERMINATE \
        --disk=name=DISK_NAME,device-name=DEVICE_NAME,mode=MODE
    

Replace the following placeholders:

  * TPU_NAME: A name for your TPU VM.
  * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM (for example `ct6e-standard-8t`).
  * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
  * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) for the TPU VM.
  * DEVICE_NAME: The name of the device to use for the disk. This name identifies the disk in the OS.
  * MODE: The mode for the disk. This can be `rw` (read-write) or `ro` (read-only). For more information, see Access modes.



#### Attach a disk when creating a multi-host TPU slice

When you create a multi-host TPU slice, you must specify `mode=read-only` ( Hyperdisk ML and Balanced Persistent Disk only). For more information, see Access modes.

To attach a disk across a multi-host TPU slice, create an instance template with the attached disk, create a workload policy, and then create a MIG:

  1. Create an instance template
         
         gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME
         --machine-type=MACHINE_TYPE \
         --maintenance-policy=TERMINATE \
         --image-family=IMAGE_FAMILY \
         --image-project=IMAGE_PROJECT \
         --disk=name=DISK_NAME,mode=MODE
         

Replace the following placeholders:

     * INSTANCE_TEMPLATE_NAME: The name for your instance template.
     * MACHINE_TYPE: The [machine type](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_machine_types) for the TPU VM, for example, `ct6e-standard-8t`.
     * IMAGE_FAMILY: The [OS image family](https://docs.cloud.google.com/compute/docs/images#image_families) for the TPU VM. If you want to install a specific OS version, use the `--image` flag. For more information about OS images, see [OS images](https://docs.cloud.google.com/compute/docs/images).
     * IMAGE_PROJECT: The project that contains the OS image. For TPU images, this is `ubuntu-os-accelerator-images`.
     * DISK_NAME: The name of the disk to attach to the TPU VM.
     * MODE: The mode for the disk. The mode must be `ro` (read-only) for multi-host TPU slices.
  2. Create a workload policy
         
         gcloud compute resource-policies create workload WORKLOAD_POLICY_NAME \
         --type=high-throughput \
         --accelerator-topology=TOPOLOGY
         

Replace the following placeholders:

     * WORKLOAD_POLICY_NAME: The name of your workload policy.
     * TOPOLOGY: The topology of the TPU VMs, for example, `4x4x8`. For more information about topology for each version of TPU, see [System architecture](https://docs.cloud.google.com/tpu/docs/system-architecture-tpu-vm#versions).
  3. Create a MIG:
         
         gcloud compute instance-groups managed create MIG_NAME \
             --project=PROJECT_ID \
             --zone=ZONE \
             --template=TEMPLATE_NAME \
             --size=SIZE \
             --workload-policy=WORKLOAD_POLICY_NAME
         

Replace the following placeholders:

     * MIG_NAME: The name for your MIG.
     * PROJECT_ID: The project ID.
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.
     * TEMPLATE_NAME: The name for your instance template.
     * SIZE: The number of VMs for your multi-host TPU slice.
     * WORKLOAD_POLICY_NAME: The name of your workload policy.



#### Attach a disk when creating a MIG with multiple single-host TPU slices

If you create a single-host TPU slice, you can specify `mode=read-only` (Hyperdisk ML and Balanced Persistent Disk only) or `mode=read-write`.

To attach durable storage to a MIG with independent single-host TPU slices, configure the instance template to create a new disk for each instance using the `--create-disk` flag:
    
    
    gcloud compute instance-templates create INSTANCE_TEMPLATE_NAME \
        --machine-type=MACHINE_TYPE \
        --maintenance-policy=TERMINATE \
        --image-family=IMAGE_FAMILY \
        --image-project=IMAGE_PROJECT \
        --disk=name=DISK_NAME,mode=MODE
    

Replace the following placeholders:

  * INSTANCE_TEMPLATE_NAME: The name for your instance template.
  * MACHINE_TYPE: The machine type for the TPU VM (for example, `ct6e-standard-8t`).
  * IMAGE_FAMILY: The OS image family for the TPU VM.
  * IMAGE_PROJECT: The project that contains the OS image (`ubuntu-os-accelerator-images`).
  * DISK_NAME: The base name of the disk to create and attach to each TPU VM.
  * DISK_SIZE: The size of the disk in GB.
  * DISK_TYPE: The disk type (for example, `pd-balanced`, `hyperdisk-balanced`).



Then, create the MIG as shown in the previous section, setting `--size` to the your chosen number of TPU VMs.

### Attach a disk to an existing TPU VM

To attach a disk to an existing TPU VM, use the [`gcloud compute instances attach-disk`](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) command.
    
    
    gcloud compute instances attach-disk VM_NAME \
        --zone=ZONE \
        --disk=DISK_NAME \
        --mode=MODE
    

Replace the following placeholders:

  * VM_NAME: The name of the TPU VM.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.
  * DISK_NAME: The name of the disk to attach to the TPU VM.
  * MODE: The mode for the disk. For more information, see Access modes.



If your VM shuts down for any reason, you might need to mount the disk after you restart the VM. For information about enabling your disk to automatically mount on VM restart, see [Configure automatic mounting on system restart](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#configure_automatic_mounting_on_vm_restart).

For more information about automatically deleting a disk, see [Modify a disk's auto-delete setting](https://docs.cloud.google.com/compute/docs/disks/modify-persistent-disk#updateautodelete).

## Format and mount a disk

If you attach a new, blank disk to your TPU VM, you must format and mount the disk before you can use it. If you attach a disk that already contains data, you must mount it before you can use it.

For more information about formatting and mounting a non-boot disk, see [Format and mount a non-boot disk on a Linux VM](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux).

## Detach a disk

To detach a disk from your TPU VM, run the following command:
    
    
    gcloud compute instances detach-disk VM_NAME \
        --zone=ZONE \
        --disk=DISK_NAME
    

Replace the following placeholders:

  * VM_NAME: The name of the TPU VM.
  * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.
  * DISK_NAME: The name of the disk to detach from the TPU VM.



For more information about detaching a disk, see [Detach a disk](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk).

## Clean up

Delete your Cloud TPU and Compute Engine resources when you finish using them.

  1. Disconnect from the Cloud TPU, if you have not already done so:
         
         exit
         

  2. Delete your TPU VM:
         
         gcloud compute instances delete VM_NAME \
             --zone=ZONE
         

Replace the following placeholders:

     * VM_NAME: The name of the TPU VM.
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.

If you created a multi-host TPU slice using a MIG, delete the instance group instead:
    
    gcloud compute instance-groups managed delete MIG_NAME \
        --zone=ZONE
    

Replace the following placeholders:

     * MIG_NAME: The name of the MIG.
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.
  3. Verify the Cloud TPU deletion. Deletion might take several minutes.
         
         gcloud compute instances list --zone=ZONE
         

  4. Verify that the disk automatically deletes when the TPU VM deletes by listing all disks in the zone where you created the disk:
         
         gcloud compute disks list --filter="zone:( ZONE )"
         

Replace the following placeholders:

     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.

If the disk does not delete when the TPU VM deletes, use the following command to delete it:
    
    gcloud compute disks delete DISK_NAME \
        --zone=ZONE
    

Replace the following placeholders:

     * DISK_NAME: The name of the disk to delete.
     * ZONE: The [zone](https://docs.cloud.google.com/tpu/docs/types-zones) where the Cloud TPU is located.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
