---
url: https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk/
title: Detaching and reattaching disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:46:58.973862+00:00
---

# Detaching and reattaching disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/detach-reattach-boot-disk/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Detaching and reattaching disks Stay organized with collections  Save and categorize content based on your preferences. 

This document discusses how to attach and reattach boot and non-boot disks to Compute Engine bare metal and virtual machine (VM) instances.

Detaching an instance's boot disk helps you complete the following tasks without having to recreate the instance:

  * Replace the boot disk for an instance with a different disk
  * Repair an instance's boot disk by temporarily attaching it to another instance



Detaching a non-boot disk from one instance and attaching it to another lets you use the data on the disk from the second instance without having to copy the data to a new disk.

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




#### Permissions required for this task

To perform this task, you must have the following [permissions](https://docs.cloud.google.com/iam/docs/overview#permissions):

  * `compute.instances.detachDisk` on the instance
  * `compute.instances.attachDisk` on the instance



## Move a boot disk between instances

Before you move a boot disk between instances that use different machine series, confirm the boot disk architecture of both instances match For example, you can't attach a boot disk from a C4A instance to a C4 instance because C4A and C4 use Arm and x86 architectures, respectively. To determine the architecture of a machine series, see the **Architecture** row in the [Machine series comparison](https://docs.cloud.google.com/compute/docs/machine-resource#machine_type_comparison) table.

For additional factors to consider when moving a boot disk between machine series, see [Move your workload to a new compute instance](https://docs.cloud.google.com/compute/docs/import/migrate-to-new-vm#storage-resources).

## Restrictions

  * The boot disk's architecture must match the architecture of the instance. For example, you can't attach a boot disk that uses x86 to an Arm instance.
  * You can attach or detach a boot disk only from a [stopped VM instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).
  * You can attach only one boot disk per VM instance.
  * If using the gcloud CLI or REST, you can attach only existing boot disks to a VM instance.
  * You can't detach a Local SSD disk from an instance. You can only attach Local SSD disks to an instance when you create the instance.



## Detach a boot disk

Before detaching the boot disk from the VM instance, you must [stop the instance](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#stop_an_instance). You don't need to unmount the disk.

###  Console 

  1. Go to the VM instances page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If prompted, select your project and click **Continue**.
  3. Click the instance for which you want to detach the boot disk.
  4. Click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.
  5. Click **Edit**.
  6. In the **Boot Disk** section, clickclose **Detach boot disk**.
  7. Click **Save**.



###  gcloud 

Use the [`gcloud compute instances detach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk) to detach the boot disk from the instance:
    
    
    gcloud compute instances detach-disk INSTANCE_NAME \
        --disk=DISK_NAME
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `DISK_NAME`: the name of the disk to detach. The disk name is usually the same as the instance name.



###  REST 

Construct a `POST` request to detach the disk:
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/detachDisk?deviceName=DISK_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `INSTANCE_NAME`: the name of the instance.
  * `ZONE`: the zone where your instances is located.
  * `DISK_NAME`: the name of the disk to detach. The disk name is usually the same as the instance name.



## Reattach a boot disk

Any disk can be reattached as a boot disk to an instance as long as the instance does not already have a boot disk attached and the boot disk is in the same zone as the VM instance. If you customize a boot disk, you must ensure that the boot disk boots properly after it is attached.

Both the existing disk and the new disk must either be UEFI-compatible or not. To create a UEFI-compatible disk, use the [`gcloud compute disk create` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/disks/create) with the `--guest-os-features` flag set to `UEFI_COMPATIBLE`.

###  Console 

  1. Go to the VM instances page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If prompted, select your project and click **Continue**.
  3. Click the instance for which you want to attach the boot disk.
  4. If the VM is running, click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.
  5. Click **Edit**.
  6. Go to the **Boot Disk** section.
  7. Click **Add item**.
  8. Select a boot disk from the drop-down menu.
  9. Click **Save**.



###  gcloud 

Use the [`gcloud compute instances attach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/attach-disk) to attach or reattach a boot disk to a VM instance. Include the `--boot` flag to indicate that the disk is used as the boot disk for the instance. If this flag is absent, the disk is attached as a non-boot data disk.
    
    
    gcloud compute instances attach-disk INSTANCE_NAME \
        --disk=DISK_NAME \
        --boot
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `DISK_NAME`: the name of the disk to attach. The disk name may be the same as the instance name.



###  REST 

Construct a `POST` request to attach the disk. Include the optional `"boot": true` parameter to indicate that this disk is the boot disk. If this parameter is absent, the disk is attached as a non-boot data disk. 
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/attachDisk
    {
     "boot": true,
     "source": "zones/ZONE/disks/DISK_NAME"
    }
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `INSTANCE_NAME`: the name of the instance to which you're attaching the new Persistent Disk.
  * `ZONE`: the zone where your instance and new disk are located.
  * `DISK_NAME`: the name of the new disk.



After you attach the disk to your VM instance, [restart the instance](https://docs.cloud.google.com/compute/docs/instances/restarting-an-instance).

## Update a boot disk for an instance

You can use only the Google Cloud console to update the boot disk for a VM in one step. Specifically, you can detach an existing boot disk and attach a new boot disk as one action.

This feature is not available through the gcloud CLI or REST.

  1. Go to the VM instances page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. If prompted, select your project and click **Continue**.
  3. Click the instance for which you want to attach the boot disk.
  4. If the VM is running, click stop **Stop** to stop the VM. If there is no **Stop** option, click more_vert **More actions >** stop **Stop**.
  5. Click **Edit** at the top of the page.
  6. In the **Boot Disk** section, clickclose **Detach boot disk**.
  7. Click **Add item**.
  8. Select a boot disk from the drop-down menu.
  9. Click **Save**.



The Google Cloud console proceeds to detach your existing boot disk and attach the new boot disk that you specified. When this process is complete, [restart the VM instance](https://docs.cloud.google.com/compute/docs/instances/restarting-an-instance).

## Attach a non-boot disk to an instance

For detailed instructions on attaching a new or existing non-boot disk to a running instance, see [Attach a disk to an instance](https://docs.cloud.google.com/compute/docs/disks/attach-disks).

## Detach a non-boot disk from an instance

You don't need to stop an instance to detach a non-boot disk. You can perform these operations while the instance is running.

**Caution:** Keep the following in mind before you detach a non-boot disk from an instance: 

  * You don't need to unmount a disk before you detach it from an instance, but Google recommends that you do so to avoid incomplete I/O operations and data corruption.
  * After you detach a data disk from a Linux instance, you must remove or comment out the corresponding entry in the `/etc/fstab` file. If you don't, the instance might not boot successfully the next time you restart the instance even though the OS might continue to run without error until the next reboot.



###  Console 

  1. Go to the VM instances page. 

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Click the instance from which you want to detach the disk.
  3. Click edit**Edit**.
  4. In the **Additional disks** section, find the disk you want to detach and click close**Remove disk**.
  5. Click **Save**.



###  gcloud 

Use the [`gcloud compute instances detach-disk` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/detach-disk):
    
    
     gcloud compute instances detach-disk INSTANCE_NAME \
       DISK_OR_DEVICE_NAME --disk-scope DISK_SCOPE
    

Replace the following:

  * `INSTANCE_NAME`: the name of the instance.
  * `DISK_OR_DEVICE_NAME`: the name of the disk or the device name specified when the disk was created. The device name is the name the OS uses to identify the disk. If you provided a device name for the disk, you must specify the device name with the `--device-name` flag.

    * To specify the disk name, specify `--disk=DISK_NAME`, where `DISK_NAME` is the name of the disk, for example, `my-data-disk`.
    * To specify the device name, specify `--device-name=DEVICE_NAME`, where `DEVICE_NAME` is the device name you provided for the disk.

To find the disk's device name, run the [`gcloud compute instances describe` command](https://docs.cloud.google.com/sdk/gcloud/reference/compute/instances/describe). For example, to print a list of the instance's attached disks in JSON format, run `gcloud compute instances describe INSTANCE_NAME --format="json(disks)"`.

  * `DISK_SCOPE`: the scope of the disk. For a zonal disk, specify `zonal`. For a regional disk, specify `regional`.




###  REST 

Construct a `POST` request to the [`instances.detachDisk`](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/detachDisk) method.
    
    
    POST https://compute.googleapis.com/compute/v1/projects/PROJECT_ID/zones/ZONE/instances/INSTANCE_NAME/detachDisk?deviceName=DEVICE_NAME
    

Replace the following:

  * `PROJECT_ID`: the ID of your project.
  * `INSTANCE_NAME`: the name of the instance.
  * `ZONE`: the zone where your instance is located.
  * `DEVICE_NAME`: the device name of the disk. To find the disk's device name, make a `GET` request to the [`instances` resource](https://docs.cloud.google.com/compute/docs/reference/rest/v1/instances/get) to view its attached disks and device names.



## What's next?

  * [Create a new disk from a snapshot](https://docs.cloud.google.com/compute/docs/disks/restore-and-delete-snapshots#restoresnapshotlargersize)
  * [Transfer files to VM instances](https://docs.cloud.google.com/compute/docs/instances/transfer-files)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
