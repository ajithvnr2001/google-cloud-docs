---
url: https://docs.cloud.google.com/container-optimized-os/docs/concepts/disks-and-filesystem/
title: Disks and file system overview \u00a0|\u00a0 Container-Optimized OS \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:32:44.747493+00:00
---

# Disks and file system overview  |  Container-Optimized OS  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/container-optimized-os/docs/concepts/disks-and-filesystem/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Container-Optimized OS ](https://docs.cloud.google.com/container-optimized-os/docs)
  * [ Guides ](https://docs.cloud.google.com/container-optimized-os/docs/how-to/create-configure-instance)



Send feedback 

#  Disks and file system overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of the Container-Optimized OS file system and describes how to mount and format disks.

## File system

The Container-Optimized OS node image file system layout is optimized to enhance node security. The boot disk space is split into three types of partitions:

  * **Root partition** , which is mounted as read-only.
  * **Stateful partitions** , which are writable and stateful.
  * **Stateless partitions** , which are writable but the contents do not persist across reboots.



When using Container-Optimized OS, be aware of the partitioning if you run your own services that have certain expectations about the file system layout outside of containers.

The root file system is mounted as read-only to protect system integrity. However, home directories and `/mnt/stateful_partition` are persistent and writable.

### Working with the Container-Optimized OS file system

The following is a list of paths in the Container-Optimized OS node image file system, along with their properties and recommended usage: 

Path | Properties | Purpose  
---|---|---  
/ | 

  * read-only
  * executable

| The root filesystem is mounted as read-only to maintain integrity. The kernel verifies integrity root filesystem during boot up, and refuses to boot in case of errors.  
/home  
/var  
| 

  * writable
  * non-executable
  * stateful

| These paths are meant for storing data that persists for the lifetime of the boot disk. They are mounted from `/mnt/stateful_partition`.  
/var/lib/google  
/var/lib/docker  
/var/lib/toolbox | 

  * writable
  * executable
  * stateful

| These paths are working directories for Compute Engine packages (for example, the accounts manager service), Docker, and [Toolbox](https://docs.cloud.google.com/container-optimized-os/docs/how-to/toolbox) respectively.  
/var/lib/cloud | 

  * writable
  * executable
  * stateless
  * tmpfs

| This path is the working directory of the `cloud-init` package.  
/etc | 

  * writable
  * executable
  * stateless
  * tmpfs

| Typically holds your configuration (for example, `systemd` services defined via `cloud-init`). It's a good idea to capture the desired state of your instances in `cloud-init`, as `cloud-init` is applied when an instance is newly created as well as when an instance is restarted.  
/tmp | 

  * writable
  * non-executable
  * stateless
  * tmpfs

| Typically used as a scratch space and should not be used to store persistent data.  
/mnt/disks | 

  * writable
  * executable
  * stateless
  * tmpfs

| You can mount persistent disks at directories under `/mnt/disks`.  
  
## Mounting and formatting disks

You can attach a persistent disk or create an instance with Local SSDs when using Container-Optimized OS. Follow the instructions on [Formatting and mounting a persistent disk](https://docs.cloud.google.com/compute/docs/disks/format-mount-disk-linux#format_linux) or [Format and mount a local SSD device](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#formatandmount) for the appropriate use-case.

The disks can be mounted by creating a subdirectory under `/mnt/disks` directory. Since `/etc/` is stateless on Container-Optimized OS, you cannot use `/etc/fstab` to automatically fsck (file system consistency check) and mount the disks on boot. But you can achieve the same by doing those operations from the `bootcmd` section in your [`cloud-config`](http://cloudinit.readthedocs.io/en/latest/topics/examples.html).

The following example mounts the disk `DEVICE_ID` under the `/mnt/disks` directory.

  1. Create a script file using the following contents:
         
         #cloud-config
         
         bootcmd:
         - fsck.ext4 -tvy /dev/DEVICE_ID
         - mkdir -p /mnt/disks/MNT_DIR
         - mount -t ext4 -o ... /dev/DEVICE_ID /mnt/disks/MNT_DIR
         

Replace the following:

     * `DEVICE_ID`: the device ID of the disk that you want to format and mount.
     * `MNT_DIR`: the directory in which to mount your disk.

Refer to the Linux documentation for a full set of options supported by the [`fsck.ext4`](http://man7.org/linux/man-pages/man8/e2fsck.8.html) and [`mount`](http://man7.org/linux/man-pages/man8/mount.8.html) commands.

  2. Update the VM metadata to include the script file by using the `--metadata-from-file` flag.

To create a VM, use the following command:
         
         gcloud compute instances create INSTANCE_NAME \
             --metadata-from-file user-data=SCRIPT_FILE_NAME
         

To update an existing instance, use the following command:
         
         gcloud compute instances add-metadata INSTANCE_NAME \
             --metadata-from-file user-data=SCRIPT_FILE_NAME
         

Replace the following:

     * `INSTANCE_NAME`: the name of your VM instance.
     * `SCRIPT_FILE_NAME`: the name of the metadata script file.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
