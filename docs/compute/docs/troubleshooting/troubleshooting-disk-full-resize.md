---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-full-resize/
title: Troubleshoot full disks and disk resizing \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:09:50.954363+00:00
---

# Troubleshoot full disks and disk resizing  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-disk-full-resize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshoot full disks and disk resizing Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This page describes common issues that you might run into when resizing a persistent disk or when your persistent disk is full, and how to fix each of them.

## Before you begin

  * Always [create a snapshot of your disk](https://docs.cloud.google.com/compute/docs/disks/create-snapshots) before performing any troubleshooting steps to ensure that your data is backed up. 
  * If you haven't already, set up [authentication](https://docs.cloud.google.com/compute/docs/authentication). Authentication verifies your identity for access to Google Cloud services and APIs. To run code or samples from a local development environment, you can authenticate to Compute Engine by selecting one of the following options: 
    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
           
           gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

**Note:** If you installed the gcloud CLI previously, make sure you have the latest version by running `gcloud components update`. 
    2. [ Set a default region and zone](https://docs.cloud.google.com/compute/docs/gcloud-compute#set_default_zone_and_region_in_your_local_client).



## Rate limited error when modifying a disk

The following are common errors you might encounter when you attempt to modify your Extreme Persistent Disk or Google Cloud Hyperdisk. You might see these errors appear in a number of places, such as in your serial console output or in application logs.
    
    Disk cannot be resized due to being rate limited.
    
    
    Cannot update provisioned iops due to being rate limited.
    
    
    Cannot update provisioned throughput due to being rate limited.
    




Review the following time limits for modifying disks:

  * You can resize an Extreme Persistent Disk or Hyperdisk Throughput volume only once in a 6 hour period.
  * You can resize a Hyperdisk Extreme volume only once in a 4 hour period.
  * You can change the provisioned IOPS or throughput for a Hyperdisk volume only once in a 4 hour period.



To resolve these errors, wait the required amount of time since your last modification before attempting to modify the disks again.

## Disk capacity errors

The following sections describe common errors related to disk capacity and how to resolve them.

### Full disks

The following are common errors you might encounter when your persistent disk reaches full capacity. You might see these errors appear in a number of places, such as in your serial console output or in application logs.
    
    No space left on device
    
    
    Not enough storage is available to process this command
    
    
    Error: There isn't enough space on the disk.
    




To resolve this issue, do the following:

  1. [Create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots) of the disk.

  2. Delete files that you don't need on the disk to free up space.

  3. If your disk requires more space after this, [resize the disk](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).




### Inaccessible VM due to full boot disk

Your VM might become inaccessible if its boot disk is full. This scenario can be difficult to identify; it's not always obvious when the VM connectivity issue is due to a full boot disk. The following are examples of common errors you might encounter if you can't access your VM from the Google Cloud CLI or using RDP because the boot disk is full:
    
    Network error: Software caused connection abort
      
    
    Your Remote Desktop Services session has ended. The connection was lost because the remote computer is running low on memory or disk space.
      
    
    ERROR: (gcloud.compute.ssh) Could not SSH into the instance.  It is possible
      that your SSH key has not propagated to the instance yet. Try running this
      command again.  If you still cannot connect, verify that the firewall and
      instance are set to accept ssh traffic.
      
    
    You cannot connect to the VM instance because of an unexpected error. Wait a
      few moments and then try again.
      
    
    No space left on device
      
    
    ERROR Exception calling the response handler. [Errno 2] No usable temporary
      directory found in ['/tmp', '/var/tmp', '/usr/tmp', '/']...
      




To resolve the preceding issues, do the following:

  1. Confirm that the VM's connectivity failure is due to a full boot disk:

     * **For Linux VMs** , inspect the serial port output:
           
           gcloud compute instances tail-serial-port-output VM_NAME
           

If the boot disk is full, the output contains the message `No space left on device`.

     * **For Windows VMs** , use the [Special Administration Console (SAC)](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac):

After you [open a Command Prompt channel in SAC](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac#command-prompt), run the following command to check free space:
           
           wmic logicaldisk get caption,freespace,size
           

  2. If you have not already done so, [create a snapshot](https://docs.cloud.google.com/compute/docs/disks/create-snapshots#creating_snapshots) of the VM's boot disk.

  3. Try to [restart the VM](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_a_vm).

  4. If you still can't access the VM, do the following:

     1. Stop the VM:
            
            gcloud compute instances stop VM_NAME
            

Replace `VM_NAME` with the name of your VM.

     2. Increase the size of the boot disk:
            
            gcloud compute disks resize BOOT_DISK_NAME --size DISK_SIZE
            

Replace the following:

        * `BOOT_DISK_NAME`: the name of your VM's boot disk
        * `DISK_SIZE`: the new larger size, in gigabytes, for the boot disk

For example, to resize a disk named `example-disk-1` to 6GB, run the following command:
    
    gcloud compute disks resize example-disk-1 --size=6GB
    

     3. Start the VM:
            
            gcloud compute instances start VM_NAME
            

  5. Reattempt to [SSH to the VM](https://docs.cloud.google.com/compute/docs/instances/connecting-to-instance). If you still can't access the VM, do one of the following:

     * Create a new disk from a snapshot. For more information, see [Recovering an inaccessible VM or a full boot disk](https://docs.cloud.google.com/compute/docs/disks/recover-vm#inaccessible_instance).

     * **For Linux VMs only** , boot the VM temporarily in rescue mode using the open source [GCE Rescue tool](https://github.com/googlecloudplatform/gce-rescue). Then perform the steps in File system issues.




## File system issues

The following sections describe common file system issues and how to resolve them.

### File system resize

After you resize a VM boot disk, most VMs resize the root file system and restart the VM. However, for some VM images types, you might have to resize the file system manually. If your VM does not support automatic root file system resizing, or if you've resized a data (non-boot) persistent disk, you must manually [resize the file system and partitions](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).

To check if your root file system expanded automatically after you resized your VM boot disk, do the following:

  1. Check if your VM resized the boot disk using one of the following methods:

     * [Inspect your serial port output](https://docs.cloud.google.com/compute/docs/instances/viewing-serial-port-output). Look for a line that indicates the root partition was resized.

For example, on VMs with Debian images, if the automatic resize was successful then the console logs include the line `... expand-root.sh[..]: Resizing ext4 filesystem on /dev/sda1`.

     * If you can connect to a Linux VM using SSH, run the command `df -h` to check if there is free disk space.

For example, this output shows that the root file system is 92% full:
           
           Filesystem                                    Size  Used Avail Use% Mounted on
           udev                                           63G     0   63G   0% /dev
           tmpfs                                          13G  1.4M   13G   1% /run
           /dev/sda1                                     339G  315G   24G  92% /
           

  2. If your VM didn't resize the root file system, manually [resize the file system and partitions](https://docs.cloud.google.com/compute/docs/disks/resize-persistent-disk).




### Storage Spaces Direct (S2D) limitation

When using Storage Spaces Direct (S2D), you can't increase capacity by resizing underlying persistent disks. If you resize disks at the hardware level, S2D won't recognize the added space, and data might become inaccessible. To increase capacity, [add servers or drives](https://learn.microsoft.com/en-us/windows-server/storage/storage-spaces/add-nodes?source=recommendations) instead of resizing existing persistent disks.

To check if the disk is configured as part of an S2D cluster or storage pool, complete the following steps:

  1. In the Google Cloud console, go to the **VM instances** page.

[Go to VM instances](https://console.cloud.google.com/compute/instances)

  2. Next to the instance that has the resized disk, click the **RDP** button. The browser opens an RDP connection to the instance.

  3. Right-click the **Windows Start** button and select **Disk Management** to open the **Disk Management** tool. For example, the following screenshot shows that Disk 1 has a Storage Spaces protective partition in place:




![S2D details from Disk Management.](https://docs.cloud.google.com/static/compute/images/s2d.png)

Alternatively, you can run either of the following PowerShell commands to find any Persistent Disk that are associated with a S2D configuration.
    
    Get-Disk | Where-Object Model -eq "Storage Space"
       
    
    Get-PhysicalDisk | Where-Object {$_.ObjectId -like "*Spaces*"}
       




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
