---
url: https://docs.cloud.google.com/compute/docs/disks/optimizing-local-ssd-performance/
title: Optimizing local SSD performance \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:28:59.786253+00:00
---

# Optimizing local SSD performance  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/optimizing-local-ssd-performance/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Optimizing local SSD performance Stay organized with collections  Save and categorize content based on your preferences. 

Linux 

The [performance by disk type chart](https://docs.cloud.google.com/compute/docs/disks/local-ssd#performance) describes the maximum achievable performance for local SSD partitions. To optimize your apps and VM instances to achieve these speeds, use the following best practices:

### Use guest environment optimizations for Local SSDs

By default, most Compute Engine-provided Linux images automatically run an optimization script that configures the instance for peak Local SSD performance. The script enables certain [queue `sysfs` settings](https://www.kernel.org/doc/Documentation/block/queue-sysfs.rst) that enhance the overall performance of your machine and mask [interrupt requests (IRQs)](https://en.wikipedia.org/wiki/Interrupt_request) to specific virtual CPUs (vCPUs). This script only optimizes performance for Compute Engine local SSD partitions.

Ubuntu, SLES, and other earlier images might not be configured to include this performance optimization. If you are using any of these images or an image that is earlier than **v20141218** , you can [install the guest environment](https://docs.cloud.google.com/compute/docs/images/install-guest-environment) to enable these optimizations.

### Choose an interface to connect your local SSDs

You can connect Local SSDs to your VMs using either the NVMe interface or the SCSI interface. The best choice depends on the operating system (OS) you are using. For most workload configurations involving Local SSDs, using the NVMe interface leads to better performance.

**Note:** Newer machine series (third generation) support only the NVMe disk interface.

  * **If you need to use a specific OS** , [choose an interface](https://docs.cloud.google.com/compute/docs/disks/local-ssd#choose_an_interface) for your local SSD partitions that works best with your boot disk image.

  * **If you have an existing setup that requires using a SCSI interface** , use an image that supports multi-queue SCSI to achieve better performance over the standard SCSI interface.




### Enable multi-queue SCSI

Some public images support multi-queue SCSI. To use multi-queue SCSI on custom images that you import to your project, you must enable it yourself. Your imported Linux images can use multi-queue SCSI only if they include kernel version `3.19` or later.

To enable multi-queue SCSI on a custom image, import the image with the `VIRTIO_SCSI_MULTIQUEUE` guest OS feature enabled and add an entry to your GRUB config:

###  CentOS 

For CentOS7 only.

  1. Import your custom image using the [API](https://docs.cloud.google.com/compute/docs/reference/latest/instances) and include a `guestOsFeatures` item with a `type` value of `VIRTIO_SCSI_MULTIQUEUE`.

  2. Create an instance using your custom image and [attach one or more local SSDs](https://docs.cloud.google.com/compute/docs/disks/add-local-ssd#create_local_ssd).

  3. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) through SSH.

  4. Check the value of the `/sys/module/scsi_mod/parameters/use_blk_mq` file
         
         $ cat /sys/module/scsi_mod/parameters/use_blk_mq
         

If the value of this file is `Y`, then multi-queue SCSI is already enabled on your imported image. If the value of the file is `N`, include `scsi_mod.use_blk_mq=Y` in the `GRUB_CMDLINE_LINUX` entry in your GRUB config file and restart the system.

     1. Open the `/etc/default/grub` GRUB config file in a text editor.
            
            $ sudo vi /etc/default/grub
            

     2. Add `scsi_mod.use_blk_mq=Y` to the `GRUB_CMDLINE_LINUX` entry.
            
            GRUB_CMDLINE_LINUX=" vconsole.keymap=us console=ttyS0,38400n8 vconsole.font=latarcyrheb-sun16 scsi_mod.use_blk_mq=Y"
            

     3. Save the config file.

     4. Run the `grub2-mkconfig` command to regenerate the GRUB file and complete the configuration.
            
            $ sudo grub2-mkconfig -o /boot/grub2/grub.cfg
            

     5. Reboot the instance.
            
            $ sudo reboot
            




###  Ubuntu 

  1. Import your custom image using the [Compute Engine API](https://docs.cloud.google.com/compute/docs/reference/latest/instances) and include a `guestOsFeatures` item with a `type` value of `VIRTIO_SCSI_MULTIQUEUE`.

  2. Create an instance using your custom image and [attach one or more local SSDs](https://docs.cloud.google.com/compute/docs/disks/local-ssd#create_local_ssd) using the SCSI interface.

  3. [Connect to your instance](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance) through SSH.

  4. Check the value of the `/sys/module/scsi_mod/parameters/use_blk_mq` file.
         
         $ cat /sys/module/scsi_mod/parameters/use_blk_mq
         

If the value of this file is `Y`, then multi-queue SCSI is already enabled on your imported image. If the value of the file is `N`, include `scsi_mod.use_blk_mq=Y` in the `GRUB_CMDLINE_LINUX` entry in your GRUB config file and restart the system.

     1. Open the `sudo nano /etc/default/grub` GRUB config file in a text editor.
            
            $ sudo nano /etc/default/grub
            

     2. Add `scsi_mod.use_blk_mq=Y` to the `GRUB_CMDLINE_LINUX` entry.
            
            GRUB_CMDLINE_LINUX="scsi_mod.use_blk_mq=Y"
            

     3. Save the config file.

     4. Run the `update-grub` command to regenerate the GRUB file and complete the configuration.
            
            $ sudo update-grub
            

     5. Reboot the instance.
            
            $ sudo reboot
            




## What's next

  * [Benchmark your local SSDs](https://docs.cloud.google.com/compute/docs/disks/benchmarking-local-ssd-performance).
  * [Learn about local SSD pricing](https://docs.cloud.google.com/compute/disks-image-pricing#localssdpricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
