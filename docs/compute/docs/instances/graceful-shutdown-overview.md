---
url: https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview/
title: About graceful shutdown \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:45.421524+00:00
---

# About graceful shutdown  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About graceful shutdown Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the requirements and limitations that apply when you gracefully shut down Compute Engine instances.

When you stop or delete a compute instance, Compute Engine allows a [short time](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance) for the guest OS to fully shut down. If the guest OS doesn't finish running tasks within this time, then Compute Engine forces a shutdown, which can potentially lead to data loss or corrupt file systems. To prevent these issues, you can enable graceful shutdown in a compute instance. When a compute instance gracefully shuts down, the guest OS has up to six hours to finish running tasks before Compute Engine shuts it down.

Graceful shutdown is useful for scenarios such as the following:

  * Letting a high performance computing (HPC) job fully shut down.

  * Letting a database finish submitting active transactions.

  * Letting an email server finish processing before shutdown.

  * Letting a multiplayer game session finish running.


**Important:** If you want to run a shutdown script with graceful shutdown, then your script runs _after_ the graceful shutdown ends. To give your script enough time to complete and avoid potential data loss or incomplete tasks, we recommend that you run your script during the graceful shutdown. For more information, see [Run a script during a graceful shutdown](https://docs.cloud.google.com/compute/docs/shutdownscript#graceful-shutdown).

## Understand graceful shutdown

The following sections explain how graceful shutdown works.

### Graceful shutdown period

In a compute instance, graceful shutdown is disabled by default. You can enable it when you create or update a compute instance. When you enable graceful shutdown, you can specify a shutdown period from one second up to six hours.

We recommend that you choose a duration for the graceful shutdown that gives your applications enough time to finish running tasks. For example, if you estimate that your applications need 10 minutes to finish, we recommend that you specify a custom duration of 15 minutes. After all tasks in the guest OS have finished running, you can manually end the graceful shutdown to save costs, as described in the next section.

### Graceful shutdown process

When you stop or delete a compute instance that has graceful shutdown enabled, or if Compute Engine stops or deletes it for a scheduled stop or deletion, the compute instance state changes to `PENDING_STOP`. The graceful shutdown begins, allowing your applications to finish running their tasks.

Compute Engine ends the graceful shutdown of a compute instance when the time limit expires, or if you manually end the graceful shutdown by using one of the following methods:

  * **From within the guest OS**. You stop the compute instance by using the shutdown command of the guest OS; for example, `sudo shutdown -h now`.

  * **From Google Cloud**. You stop or delete the compute instance by using one of the following methods:

    * **Google Cloud console** : complete the following steps:

      1. Go to the **VM instances** page.

      2. Select the row that contains the compute instance, and then click stop **Stop** or delete **Delete**. If there is no **Stop** or **Delete** option, then click **More actions** , and then select **Stop** or **Delete**.

      3. In the dialog that appears, select the **Skip graceful shutdown (if applicable)** checkbox before confirming to stop or delete the compute instance.

    * **Google Cloud CLI** : include the `--no-graceful-shutdown` flag in the command.

    * **REST API** : include the `noGracefulShutdown=true` query parameter in the request URL.


**Caution:** Before the graceful shutdown period times out or you manually end the graceful shutdown, verify that all tasks in the guest OS have finished running. Otherwise, Compute Engine forcefully stops any running tasks, which can cause data loss or corrupt file systems.

When the graceful shutdown process ends, Compute Engine sends the [Advanced Configuration and Power Interface (ACPI) G2 Soft Off signal](https://en.wikipedia.org/wiki/ACPI#Global_states) to the guest OS, sets the compute instance state to `STOPPING`, and then continues with the stop or delete operation.

### Stopping or deleting compute instances without graceful shutdown

After you've enabled graceful shutdown in a compute instance, you can still stop or delete the compute instance without going through the graceful shutdown process. This approach helps you save costs when, for example, you don't need to gracefully shut down your compute instance on a specific day, or if the workload running on the compute instance has changed.

To skip graceful shutdown in a compute instance, do one of the following:

  * **Skip graceful shutdown for single operations**. Keep graceful shutdown enabled, but bypass it for specific stop or delete operations. To do so, follow the manual shutdown process.

  * **Disable graceful shutdown entirely**. If you no longer need to gracefully shut down a compute instance, then you can disable graceful shutdown entirely. For more information, see [Disable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown).




## Pricing

There are no costs associated with enabling or disabling graceful shutdown in a compute instance. However, when you stop or delete a compute instance that has graceful shutdown enabled, you continue to incur charges for CPU and memory during the graceful shutdown period. These charges stop when the graceful shutdown period ends and the compute instance state changes to `STOPPING`.

For more detailed pricing information, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).

## Limitations

When you enable graceful shutdown in a compute instance, the following limitations apply:

  * After you enable graceful shutdown for a compute instance, you can't simulate host maintenance events on TPU VMs.

  * After a stop or delete operation starts and a graceful shutdown is in progress (`PENDING_STOP`), you can't do the following:

    * You can't reset, restart, or suspend the compute instance.

    * You can't update the compute instance properties.

    * You can't enable or disable [deletion protection](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion) for a compute instance that Compute Engine is deleting.

    * You can't [collect core dumps](https://docs.cloud.google.com/compute/docs/troubleshooting/collecting-core-dumps).

  * Compute Engine doesn't start a graceful shutdown, or it abruptly stops a graceful shutdown that is in progress (`PENDING_STOP`), when one of the following events occurs:

    * Compute Engine stops or deletes a Spot VM or preemptible instance due to [preemption](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-process).

    * Compute Engine stops a compute instance after a host maintenance event starts, and the [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) of the compute instance is set to `TERMINATE`.

    * Compute Engine stops a compute instance after it encounters a host error.

  * You can gracefully shut down and delete a maximum of 8,000 compute instances at a time, per project and region.

  * You can gracefully shut down compute instances that you created in bulk, or modify their graceful shutdown settings, only after Compute Engine finishes creating all compute instances.

  * You can't skip or end a graceful shutdown for a compute instance in a managed instance group (MIG) in the following cases:

    * The MIG deletes the compute instance during [autoscaling](https://docs.cloud.google.com/compute/docs/autoscaler).

    * Compute Engine [applies configuration updates](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups).




## What's next

  * [Enable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/enable-graceful-shutdown)

  * [View graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/view-graceful-shutdown)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
