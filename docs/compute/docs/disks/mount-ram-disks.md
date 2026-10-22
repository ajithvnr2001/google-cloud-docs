---
url: https://docs.cloud.google.com/compute/docs/disks/mount-ram-disks/
title: Creating in-memory RAM disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:30.992929+00:00
---

# Creating in-memory RAM disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/mount-ram-disks/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Creating in-memory RAM disks Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine instances have high-performance, enterprise-class memory that you can use to run your applications. You can allocate some of this memory to create a RAM disk with exceptionally low latency and high throughput. RAM disks work well when your application expects a file system structure and cannot simply store its data in memory. RAM disks alone do not provide any storage redundancy or flexibility, so it is best to use RAM disks in combination with other [instance storage options](https://docs.cloud.google.com/compute/docs/disks).

RAM disks share instance memory with your applications. If your instances do not have enough memory to contain RAM disks and your applications, create instances with `highmem` machine types, such as [N2](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n2-high-mem) or [upgrade your existing instances](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance) to add more memory.

**Caution:** RAM disks are located in memory, and are **not** automatically replicated. **All data on these devices is erased** in the event of a [host error](https://docs.cloud.google.com/compute/docs/faq#hosterror) or a system restart. Frequently back up your data on replicated storage. Before you restart an instance with an in-memory RAM disk, write data from the RAM disk to replicated storage.

## Before you begin

  * Read about the difference between RAM disks and other [Compute Engine storage options](https://docs.cloud.google.com/compute/docs/disks). 
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




## Creating a RAM disk

You can create a RAM disk with the `tmpfs` filesystem, which is included by default in most [Linux distributions](https://docs.cloud.google.com/compute/docs/images#os-details).

**Caution:** You must ensure that `tmpfs` volumes on your instance do not use up all of your instance memory. By default, Compute Engine instances do not have any swap space. If you use all of the available instance memory in a RAM disk, the instance can crash and potentially cause you to lose your data.

  1. If your instance does not have enough available memory, you can optionally [change the instance machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance#changing_a_machine_type) to a machine type with more memory.

  2. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) through SSH. For this example, go to the [VM instances page](https://console.cloud.google.com/compute/instances) and click the **SSH** button next the instance where you want to add a RAM disk.

  3. Create a mount point for your RAM disk.
         
         $ sudo mkdir /mnt/ram-disk
         

  4. Create and mount a new `tmpfs` RAM disk. You must determine a value for the `size` property that meets your storage requirements without competing with your applications for memory or expending all of the available memory. For this example, the instance has a [`n1-highmem-32`](https://docs.cloud.google.com/compute/docs/general-purpose-machines#n1-high-memory) machine type with 208 GB of memory, so a `50g` RAM disk size is appropriate.
         
         $ sudo mount -t tmpfs -o size=50g tmpfs /mnt/ram-disk
         

  5. Add the RAM disk to the `/etc/fstab` file so that the device automatically mounts again if you restart the instance:
         
         $ echo 'tmpfs /mnt/ram-disk tmpfs nodev,nosuid,noexec,nodiratime,size=50G 0 0' | sudo tee -a /etc/fstab
         




## Deleting a RAM disk

You can unmount a `tmpfs` RAM disk just like any other volume. This deletes the RAM disk and any data that is stored in it. For this example, remove a RAM disk that is mounted at `/mnt/ram-disk`:
    
    
    $ sudo umount /mnt/ram-disk
    

## Automatically backing up RAM disk data between instance restarts

You can back up a RAM disk before your instance restarts to preserve the RAM disk data until the instance starts up again. Back up your data to a Google Cloud Hyperdisk volume, or to a Persistent Disk volume if your VM's machine type doesn't support Hyperdisk.

  1. [Create and mount a Hyperdisk](https://docs.cloud.google.com/compute/docs/disks/add-hyperdisk) volume to use as a backup disk for your RAM disk. Make sure the disk is big enough to contain the information in the RAM disk.

  2. [Create a shutdown script](https://docs.cloud.google.com/compute/docs/shutdownscript) for your instance with an `rsync` command that writes the RAM disk contents to the backup volume. For this example, use the gcloud CLI to add the `shutdown-script` metadata to the instance with the RAM disk mounted at `/mnt/ram-disk` and the Hyperdisk volume mounted at `/mnt/ram-disk-backup`.
         
         gcloud compute instances add-metadata example-instance --metadata shutdown-script="#! /bin/bash
         rsync -a --delete --recursive --force /mnt/ram-disk/ /mnt/ram-disk-backup/
         EOF"
         

  3. Optionally, you can also [create a startup script](https://docs.cloud.google.com/compute/docs/startupscript#startupscriptrunninginstances) that restores the files back to the RAM disk when the instance starts again. Use the gcloud CLI to add the `startup-script` metadata to the instance.
         
         gcloud compute instances add-metadata example-instance --metadata startup-script="#! /bin/bash
         rsync -a --recursive --force /mnt/ram-disk-backup/ /mnt/ram-disk/
         EOF"
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
