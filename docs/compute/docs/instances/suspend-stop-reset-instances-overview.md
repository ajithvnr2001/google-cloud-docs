---
url: https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview/
title: Suspend, stop, or reset Compute Engine instances \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T15:14:11.204186+00:00
---

# Suspend, stop, or reset Compute Engine instances  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Suspend, stop, or reset Compute Engine instances Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an overview of the suspend, stop, or reset operations that you can use on a Compute Engine instance. To learn how to perform these operations, see instead the following:

  * [Suspend or resume an instance](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)

  * [Stop or restart an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)

  * [Reboot or reset an instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance)




You can suspend, stop, or reset an instance to do the following:

  * Save costs.

  * Perform maintenance.

  * Troubleshoot issues.

  * Free up resources.




You can repeatedly suspend and resume, stop and restart, or reset a running instance throughout its lifecycle until the instance is deleted.

## Understand instance operations

Based on your workload and cost needs, you can suspend, stop, or reset a compute instance:

Suspend an instance
    

When you suspend an instance, this action is similar to closing the lid of your laptop. We recommend that you suspend an instance in the following scenarios:

  * You want to save money by no longer paying for the core and memory costs of running an instance, but still pay for storage to preserve its state.

  * You don't need the instance at this time, but you want to be able to bring it back up quickly with its OS and application state where you left it.



    

For more information, see Suspend operation in this document.

Stop an instance
    

When you stop an instance, this action is similar to shutting down your laptop. We recommend that you stop an instance in the following scenarios:

  * You no longer need the instance, but you want to remove and reuse the resources attached to the instance—such as its internal IP addresses or Google Cloud Hyperdisk volumes.

  * You don't need to preserve the guest OS memory, device state, or application state.

  * You want to change certain properties of the instance and you need to stop the instance to make these changes.



    

For more information, see Stop operation in this document.

Reset an instance
    

When you reset an instance, this action is similar to doing a reset of your computer, such as when you press a reset button or press and hold the power button. A reset operation doesn't perform a graceful reboot, and loss of unsaved data is possible. We recommend that you reset an instance in the following scenarios:

  * You want to re-initialize the instance to its boot state to help ensure optimal performance and stability.

  * You want to resume your workload after your guest OS has crashed and is unresponsive, and you have no other options than resetting the instance.



    

For more information, see Reset operation in this document.

For an overview of the differences between the stop, suspend, and reset operations for an instance, see the comparison table in this document.

### Suspend operation

When you suspend a compute instance, the following occurs:

  1. Compute Engine sends an [Advanced Configuration and Power Interface (ACPI) G1 Sleeping signal](https://en.wikipedia.org/wiki/ACPI#Global_states) to the guest OS and changes the instance state to `SUSPENDING`. Then, Compute Engine uses persistent storage to store the following:

     * The guest OS memory

     * The device state

     * The application state of the instance

The storing operation might take some time to complete, depending on the amount of data to store.

  2. After Compute Engine has completed storing the data, the instance state transitions to `SUSPENDED` within a few seconds, and the suspend operation completes. All resources attached to the instance, like disks and static IP addresses, remain attached to the instance. However, any ephemeral IP addresses are released unless you promote them to a static IP address.




Unless you [resume](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance#resume_a_suspended_instance) or [delete the instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance), the instance remains in the `SUSPENDED` state for up to 60 days. After that time, Compute Engine transitions the instance state to `TERMINATED`, and the instance loses the preserved guest OS memory, device state, and application state.

### Stop operation

When you stop or delete a compute instance, or Compute Engine does so for a scheduled stop or deletion, the following occurs:

  1. If [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview) is enabled, then the instance enters the `PENDING_STOP` state, giving you time to finish running tasks before the shutdown process begins. The instance remains in this state until the graceful shutdown process times out or you manually end it.

  2. Compute Engine sends the [ACPI G2 Soft Off signal](https://en.wikipedia.org/wiki/ACPI#Global_states) to the guest OS in the instance, and then sets the instance state to `STOPPING`. Unless you specified to [skip the guest OS shutdown](https://docs.cloud.google.com/compute/docs/instances/decrease-shutdown-time), the time that the guest OS has to cleanly shut down depends on the instance type as follows:

     * **Spot VMs** : for Spot VMs and preemptible instances, the guest OS shuts down in a maximum of 30 seconds. This period is the same length as the [preemption process](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-process).

     * **Other instance types** : for any other instance types, Compute Engine gives the guest OS up to a maximum of 120 seconds to shut down.

**Caution:** If a shutdown script is still running at the end of the allowed guest OS shutdown period, then Compute Engine forcefully stops it. If you're concerned that a shutdown script may not finish on time, then to help ensure that the guest OS shuts down only after all shutdown scripts have finished running, [stop an instance from the guest OS](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stop-vm-guest-os).
  3. After the guest OS has shut down, Compute Engine sends the ACPI G3 Mechanical Off signal to instance, and, depending on the operation that is running, does one of the following:

     * **For stop operations** : Compute Engine sets the instance state to `TERMINATED` within a few seconds, and the stop operation completes. The instance retains its attached disks, configuration settings, IP addresses, MAC addresses, and instance metadata.

     * **For delete operations** : Compute Engine deletes the instance and all attached resources within a few seconds.




### Reset operation

When you reset a compute instance, Compute Engine immediately restarts the instance without sending an ACPI shutdown signal to the guest OS, bypassing any shutdown procedure. When your reset an instance, Compute Engine does the following:

  * Compute Engine re-initializes the instance to its initial boot state, but doesn't modify instance metadata or attached disks.

  * Compute Engine wipes the contents of the instance's memory.

  * Compute Engine keeps the instance state to `RUNNING` throughout the reset operation.




The reset operation doesn't change any instance properties. The instance retains its ephemeral IPs, static external IPs, attached disks, machine type, and Local SSD disks (if any).

**Warning:** Only reset an instance as a last resort when the guest OS has crashed and is unresponsive. This action forces an abrupt shutdown of the guest OS, which can cause data loss or file system corruption. To cleanly restart an instance, see instead [Reboot the instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance#reboot-instance).

### Comparison table

The following table shows how stop, suspend, and reset operations affect a compute instance and its attached resources:

| **Suspend an instance** | **Stop an instance** | **Reset an instance**  
---|---|---|---  
**Billing** | While an instance is in the `SUSPENDING` or `SUSPENDED` state, you don't incur charges for CPU usage. However, you keep incurring charges for the resources attached to the instance until you delete them. | While an instance is in the `STOPPING` or `TERMINATED` state, you don't incur charges for CPU usage. However, you keep incurring charges for the resources attached to the instance until you delete them. | Because the instance remains in the `RUNNING` state when it's resetting, you keep incurring charges for the instance at the same rate as a running instance.  
**Instance state** | `SUSPENDED` | `TERMINATED` | `RUNNING`  
**Attached disks** | Attached disks are maintained and you keep incurring charges for them.  | Attached disks are maintained and you keep incurring charges for them.  | Attached disks are maintained and you keep incurring charges for them.   
**Memory and instance state** | The guest OS and application state are preserved and restored when the instance is resumed.  
  
You incur charges at a specific rate for storing the preserved data. For more information, see the [pricing for suspended instances](https://docs.cloud.google.com/compute/vm-instance-pricing#suspended_vm_instances). | The instance resets to power-on state and no data is saved. | The instance resets to power-on state and no data is saved.  
**GPUs** | Not supported. If a GPU is attached to an instance, then you can't suspend the instance. | As GPUs don't remain attached to an instance when its state changes to `TERMINATED`, you don't incur charges. | You incur charges at standard GPU prices.  
**TPUs** | Not supported. If a TPU is attached to an instance, then you can't suspend the instance. | Not supported. If a TPU is attached to an instance, then you can't stop the instance. | You incur charges at standard TPU prices.  
**Local SSD disks** | When you suspend an instance, you can choose whether to discard or preserve the data on the attached Local SSD disks.  
  
If you opt to [preserve Local SSD data](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance) ([Preview](https://cloud.google.com/products#product-launch-stages)), then Compute Engine migrates the Local SSD data to durable storage, and you incur charges for the used storage space until you resume or delete the instance.  | When you stop an instance, you can choose whether to discard or preserve the data on the attached Local SSD disks.  
  
If you opt to [preserve Local SSD data](https://docs.cloud.google.com/compute/docs/disks/local-ssd#stop_instance) ([Preview](https://cloud.google.com/products#product-launch-stages)), then Compute Engine migrates the Local SSD data to durable storage, and you incur charges for the used storage space until you restart or delete the instance. | Local SSD disks and their data are maintained; however, resetting an instance can cause data loss or corrupt file systems.  
**External ephemeral IP addresses** | Compute Engine releases ephemeral IP addresses when an instance is suspended, and it assigns a new ephemeral IP address to the instance when the instance resumes. To retain an external IP address, promote it to a static IP address.  | Compute Engine releases ephemeral IP addresses when an instance is stopped, and it assigns a new ephemeral IP address to the instance when the instance restarts. To retain an external IP address, promote it to a static IP address.  | Ephemeral IP addresses are maintained.  
**External static IP addresses** | Static external IP addresses are maintained.  
  
If you reserve a static external IP address and don't assign it to an instance, then you're charged at a higher rate than for static and ephemeral external IP addresses that are in use. For more information, see [External IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).  | Static external IP addresses are maintained.  
  
If you reserve a static external IP address and don't assign it to an instance, or you assign it an instance in the `TERMINATED` state, then you're charged at a higher rate than for static and ephemeral external IP addresses that are in use. For more information, see [External IP address pricing](https://docs.cloud.google.com/vpc/network-pricing#ipaddress).  | Static external IP addresses are maintained.  
**Internal IP or MAC addresses** | Internal IP and MAC addresses are maintained. | Internal IP and MAC addresses are maintained. | Internal IP and MAC addresses are maintained.  
**VM metadata** | VM metadata is maintained. | VM metadata is maintained. | VM metadata is maintained.  
  
## Pricing

The following sections outlines the pricing for stop, suspend, or reset operations for a compute instance.

### Pricing for suspending an instance

After a compute instance state transitions to `SUSPENDING`, you no longer incur charges for CPU usage. However, you continue incurring charges for the following resources attached to the instance until you delete them:

  * The instance's memory.

  * Any disks attached to the instance.

  * Any static IP addresses assigned to the instance.




Additionally, you might still incur charges for your software license fees. For example, if you suspend Windows Server instances, you don't incur charges for Windows Server license fees. However, you might still incur charges for other types of licenses.

For more information, see the [pricing for suspended instances](https://docs.cloud.google.com/compute/vm-instance-pricing#suspended_vm_instances).

### Pricing for stopping an instance

After a compute instance state transitions to `STOPPING`, you no longer incur charges for CPU usage. However, you continue incurring charges for any resources attached to the instance, such as disks and external IP addresses, until you delete them.

For more information, see [Instance uptime](https://docs.cloud.google.com/compute/vm-instance-pricing#instanceuptime).

### Pricing for resetting an instance

Since the state of a compute instance remains `RUNNING` when you reset it, you continue to incur charges for the instance at the same rate as a running instance.

For more information, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).

## What's next

  * [Suspend or resume an instance](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance)

  * [Stop or restart an instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance)

  * [Schedule an instance to start and stop](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop)

  * [Limit the runtime of an instance](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime)

  * [Reboot or reset an instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
