---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/configure-disk-cache/
title: Accelerate database performance using disk cache \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.1 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:36:27.538170+00:00
---

# Accelerate database performance using disk cache  |  AlloyDB Omni using RPM: 18.1.1  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/configure-disk-cache/

This page documents AlloyDB Omni version **18.1.1** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/overview)



Send feedback 

#  Accelerate database performance using disk cache Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.1.1keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/configure-disk-cache)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.4.0/docs/configure-disk-cache)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.3.0/docs/configure-disk-cache)
  * [ 18.1.1 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/configure-disk-cache)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/configure-disk-cache)

This page describes how to provision, set up, and use disk caching on AlloyDB Omni to increase performance of your AlloyDB Omni installation. 

In addition to the standard PostgreSQL in-memory shared buffers, AlloyDB Omni disk cache enables storing buffers on fast storage such as solid-state drives (SSDs). Disk caching accelerates data retrieval in AlloyDB Omni installations with data directories located on slower storage.

Like PostgreSQL shared buffers, AlloyDB Omni disk cache is non-persistent, which means cached data is lost on restart.

By default, AlloyDB Omni disk cache uses all storage reported by the file system. You can define the amount of storage reserved for caching data using the `omni_disk_cache_file_size` parameter.

## Enable AlloyDB Omni disk cache

To enable disk cache, complete all of the following subsections:

  1. Provision disks and create a file system
  2. Enable AlloyDB Omni disk cache for AlloyDB Omni



### Provision disks and create a file system

For AlloyDB Omni disk cache, you create a file system on a disk or multiple disks and mount it. Additionally, you can use utilities like `mdadm` or `lvm` to pool capacity together using multiple disks and use any file system.

The following steps demonstrate using `lvm` and `ext4` using NVMe SSDs.

  1. Create a volume group from all available physical devices:
         
         nvme_prefix="STORAGE_PREFIX"
         nvme_list=$(ls "$nvme_prefix"*)
         sudo vgcreate VOLUME_GROUP ${nvme_list}

Replace the following:

     * `STORAGE_PREFIX`: the prefix of the target local disks path that are attached to a virtual machine using the nonvolatile memory express (NVMe) interface—for example, on Google Cloud, the NVMe device paths always start with `/dev/nvme0n`.
     * `VOLUME_GROUP`: the name of a volume group where your SSDs are combined—for example, `omni-disk-cache-volume`.
  2. To create a logical volume from the free capacity of the volume group from the preceding step, use the following command:
         
         sudo lvcreate -n LOGICAL_VOLUME -l 100%FREE VOLUME_GROUP

Replace `LOGICAL_VOLUME` with the name of a logical volume that is treated as a partition by the LVM—for example, `omni_disk_cache_device`.

  3. Create the `ext4` file system on the logical volume. If needed, you can specify other `ext4` options subject to data safety. 
         
         sudo mkfs.ext4 /dev/VOLUME_GROUP/LOGICAL_VOLUME

  4. To create a directory that serves as a mount point on the host machine and mount the file system, use the following command:
         
         sudo mkdir /OMNI_DISK_CACHE_DIRECTORY
         sudo mount /dev/VOLUME_GROUP/LOGICAL_VOLUME /OMNI_DISK_CACHE_DIRECTORY

Replace `OMNI_DISK_CACHE_DIRECTORY` with the name of the directory or a path to the directory serving as a mount point—for example, `omni_disk_cache_directory`.




### Grant permissions to the disk cache directory

Before enabling disk cache for AlloyDB Omni, you must grant full access permissions to the disk cache directory. To grant permissions, run the following commands:
    
    
    sudo chown postgres:postgres /OMNI_DISK_CACHE_DIRECTORY
    sudo chmod -R a+rw  /OMNI_DISK_CACHE_DIRECTORY

Replace `OMNI_DISK_CACHE_DIRECTORY` with the path to your disk cache directory.

### Enable disk cache

To enable disk caching for your database, complete the following steps:

  1. Connect to your database as a `SUPERUSER`.
         
         /usr/lib/postgresql/18/bin/psql -h localhost -U postgres

  2. Set the `omni_disk_cache_enabled` and `omni_disk_cache_directory` Grand Unified Configuration (GUC) flags.
         
         ALTER SYSTEM SET omni_disk_cache_enabled=on;
         ALTER SYSTEM SET omni_disk_cache_directory='/OMNI_DISK_CACHE_DIRECTORY';
         

  3. (Optional) By default, AlloyDB Omni uses all available space in the file system. If needed, you can override this by updating the `omni_disk_cache_file_size` GUC flag.
         
         ALTER SYSTEM SET omni_disk_cache_file_size=SIZE_IN_MB;
         

Replace `SIZE_IN_MB` with the amount of disk space, in MB, you want the disk cache to use.

  4. Restart AlloyDB Omni.
         
         sudo systemctl restart alloydbomni18




## Verify the disk cache configuration

After enabling AlloyDB Omni disk cache, verify that the disk cache is accessed by monitoring read and write activity to the disks using available utilities like `iotop` or `iostat`.

Additionally, you can check if the AlloyDB Omni disk cache is open. 

To verify the disk cache configuration for AlloyDB Omni, use the following command.
    
    
    sudo journalctl -u alloydbomni18 | grep "opened omni disk cache"

If your disk caching is configured correctly, the `Successfully opened omni disk cache ...` message displays in the logs.

## What's next

* [About automatic memory management](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/automatic-memory-management) * [About local SSD disks](https://docs.cloud.google.com/compute/docs/disks/local-ssd) * [Creating and starting a VM instance](https://docs.cloud.google.com/compute/docs/instances/create-start-instance)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
