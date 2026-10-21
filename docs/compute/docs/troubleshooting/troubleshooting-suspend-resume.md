---
url: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume/
title: Troubleshooting Compute Engine instance suspension \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:37:24.041929+00:00
---

# Troubleshooting Compute Engine instance suspension  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/troubleshooting/troubleshooting-suspend-resume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Troubleshooting Compute Engine instance suspension Stay organized with collections  Save and categorize content based on your preferences. 

Linux  Windows 

This document describes common issues or errors when suspending or resuming a Compute Engine instance, and how you can resolve them. To learn about how suspending an instance works, see [Suspend operation](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#suspending-instance).

## Excessive suspension time

In some cases, it might take a while for Compute Engine to finish suspending an instance after you requested to suspend the instance. Because Compute Engine saves the memory of the guest OS on a disk, it might take several minutes to save the data and transition the instance state to `SUSPENDED`.

For Compute Engine instances that have Local SSD disks attached and that a user requested to suspend while preserving the instances' Local SSD data, suspension could take significantly longer as the Local SSD data has to be copied to a disk. For more information, see how [stopping an instance that has Local SSD disks attached works](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance_restrictions).

## Invalid instance state

You can only suspend a compute instance in the `RUNNING` state. If you attempt to suspend an instance in another state, then you encounter errors.

**Error messages** :
    
    
    UNSUPPORTED_OPERATION
    
    
    
    You cannot suspend an instance that is stopped or terminated.
    
    
    
    You cannot suspend an instance that is being repaired.
    
    
    
    You cannot suspend an already suspended instance.
    

**Resolution** : You can only suspend an instance in the `RUNNING` state. Based on the state of the instance, do one of the following:

  * For an instance in the `TERMINATED` state, [restart the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm) before suspending it.

  * For an instance in the `REPAIRING` state, wait for Compute Engine to finish repairing the instance, and then try suspending it again later.




## Invalid instance configurations

The following sections outline issues with instance properties' configurations.

### Confidential VM isn't supported

This error occurs when you try to suspend a [Confidential VM](https://docs.cloud.google.com/confidential-computing/confidential-vm/docs/confidential-vm-overview).

**Error messages** :
    
    
    UNSUPPORTED_OPERATION
    

**Resolution** : You can't suspend a Confidential VM. Instead, do one of the following:

  * Create a new instance as a regular instance, and then [delete the existing instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance).




### Guest OS timeout

This error occurs when the guest OS doesn't respond to the ACPI S3 signal within three minutes.

**Error messages** :
    
    
    UNSUPPORTED_OPERATION
    
    
    
    Instance suspend failed due to guest timeout.
    

**Resolution** : The guest OS must be able to handle the ACPI S3 signal to begin the suspend operation of the instance. To verify if the OS supports this operation, see [Operating system details](https://docs.cloud.google.com/compute/docs/images/os-details).

If the OS doesn't support suspend operations, then do one of the following:

  * Create a new instance that uses a guest OS that supports suspend operations, and then [delete the existing instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).




### Insufficient disk quota

This error occurs when you have insufficient disk quota when you suspend an instance.

**Error messages** :
    
    
    QUOTA_EXCEEDED
    
    
    
    Quota 'DISKS_TOTAL_GB' exceeded. Limit: NUMBER_OF_DISKS in region REGION.
    

**Resolution** : When you suspend an instance, Compute Engine stores the data for guest OS memory, device state, and application state in a disk. Thus, before suspending an instance, ensure that your project and region in which your instance is located have enough persistent disk quota. For more information, see [Allocation quotas](https://docs.cloud.google.com/compute/resource-usage).

### Preserve Local SSD data for more than 48 Local SSD disks

This error occurs when you try to suspend an instance that has more than 48 Local SSD disks attached and preserve the disks' data.

**Error messages** :
    
    
    INVALID_USAGE
    
    
    
    Suspend with Local SSD feature is not available for this project.
    

**Resolution** : You can't suspend an instance that has more than 48 Local SSD disks attached and preserve the disks' data. Instead, do one of the following:

  * Copy the disk's data to an attached (mounted and formatted) disk, and then suspend the instance while discarding Local SSD data.

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm-local-ssd).




### Suspend an instance with a GPU

This error occurs when you try to suspend an instance that has one or more GPUs attached.

**Error messages** :
    
    
    UNSUPPORTED_OPERATION
    
    
    
    Suspend is not supported on GPU Instances. You may delete and recreate the instances without GPU.
    

**Resolution** : You can't suspend an instance that has GPUs attached. Instead, do one of the following:

  * Create a new instance that doesn't have GPUs attached, and then [delete the existing instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).




### The instance was preempted

This error occurs because Compute Engine preempted the instance that you tried to suspend.

**Error messages** :
    
    
    FAILED_WITH_INSTANCE_PREEMPTED
    
    
    
    You cannot suspend an instance that is preempted.
    

**Resolution** : [Restart the Spot VM or preemptible instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#restart-vm), and then suspend it.

### Too much memory

This error occurs when you try to suspend an instance with more than 208 GB of memory.

**Error messages** :
    
    
    UNSUPPORTED_OPERATION
    
    
    
    Suspend is not supported on Instances with more than 208 GB memory.
    

**Resolution** : You can't suspend instances with more than 208 GB of memory. Instead, do one of the following:

  * Reduce the instance's memory by [changing the machine type](https://docs.cloud.google.com/compute/docs/instances/changing-machine-type-of-stopped-instance).

  * [Stop the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm).




### Unknown reasons

This error occurs when you try to suspend an instance, but an unknown error occurs.

**Error messages** :
    
    
    FAILED_WITH_INSTANCE_RUNNING
    
    
    
    FAILED_WITH_INSTANCE_RUNNING
    
    
    
    Suspend failed with instance in state RUNNING.
    

**Resolution** : Suspend the instance again at a later time. If you still encounter issues, then [contact support](https://docs.cloud.google.com/support).

## Windows instance with display timeout or disabled sleep button

A Windows instance that has power policy configurations set to high performance, and a display timeout set to a value greater than 0, may turn off the display after the timeout. When you send a suspend request to an instance that has a display that was turned off, the suspend request restarts the display instead of suspending the instance.

**Resolution** : To resolve this issue, do the following:

  1. If you haven't already, then connect to the instance using one of the following methods:

     * [PowerShell](https://docs.cloud.google.com/compute/docs/instances/windows/connecting-powershell)

     * [Remote Desktop Protocol (RDP)](https://docs.cloud.google.com/compute/docs/instances/connecting-to-windows)

     * [Secure Shell (SSH)](https://docs.cloud.google.com/compute/docs/connect/windows-ssh)

     * [Special Administration Console (SAC)](https://docs.cloud.google.com/compute/docs/instances/connecting-to-sac)

  2. Disable the display timeout:
         
         powercfg /change monitor-timeout-ac 0
         

  3. Enable the sleep button:
         
         powercfg -setacvalueindex SCHEME_CURRENT 4f971e89-eebd-4455-a8de-9e59040e7347 96996bc0-ad50-47ec-923b-6f41874dd9eb 1
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
