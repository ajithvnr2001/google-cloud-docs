---
url: https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview/
title: Graceful shutdown overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T12:03:19.689399+00:00
---

# Graceful shutdown overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Graceful shutdown overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document gives an overview of the graceful shutdown process in Compute Engine instances. To learn more about the states that an instance can go through during its lifecycle, see [Compute Engine instance lifecycle](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle).

When stopping or deleting an instance, Compute Engine allows a [short time](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance) for the guest OS to fully shut down. If the guest OS doesn't finish running tasks within this time, then Compute Engine forces a shutdown, which can potentially lead to data loss or corrupt file systems.

To prevent these issues, you can enable graceful shutdown in an instance. With this setting enabled, the guest OS has up to one hour to finish running tasks before Compute Engine shuts it down. Graceful shutdown is useful for scenarios when you want to achieve the following:

  * Allowing a high performance computing (HPC) job to fully shut down.

  * Allowing a database to finish submitting active transactions.

  * Allowing an email server to finish processing before shutdown.

  * Allowing a multiplayer game session to finish running.


**Important:** If you use [shutdown scripts](https://docs.cloud.google.com/compute/docs/shutdownscript) with graceful shutdown, then your scripts run after the graceful shutdown process ends. To give your scripts enough time to complete, and avoid potential data loss or incomplete tasks, we recommend running your scripts during the graceful shutdown period.

## About graceful shutdown

The following sections explain how graceful shutdown works.

### Shutdown period

In a compute instance, graceful shutdown is disabled by default. You can enable it when creating or updating an instance. When you enable graceful shutdown, you can specify a shutdown period as follows:

  * **Default period** : if you don't specify a shutdown period, then Compute Engine uses a default period of 10 minutes.

  * **Custom period** : from one second up to one hour.




We recommend choosing a shutdown period that gives your applications enough time to finish running tasks. For example, if you estimate that your applications need 10 minutes to finish running tasks, we recommend specifying a 15-minute shutdown period. This approach prevents tasks from being forcefully stopped and the potential corruption of data. After all tasks in the guest OS have finished running, you can manually end the graceful shutdown to save costs, as described in the next section.

### Shutdown process

When you stop or delete a compute instance that has graceful shutdown enabled, or if Compute Engine stops or deletes it for a scheduled stop or deletion, the instance state changes to `PENDING_STOP`. The graceful shutdown begins, allowing your applications to finish running their tasks.

Compute Engine ends the graceful shutdown of an instance when the graceful shutdown period times out, or you manually end the graceful shutdown as follows:

  * **From within the guest OS**. You stop the instance using the shutdown command of the guest OS; for example, `sudo shutdown -h now`.

  * **From Google Cloud**. You stop or delete the instance using one of the following methods:

    * **Google Cloud console** : complete the following steps:

      1. Go to the **VM instances** page.

      2. Select the instance, and then click stop **Stop** or delete **Delete**. If there is no **Stop** or **Delete** option, click more_vert **More actions >** stop **Stop** or delete **Delete**.

      3. In the dialog that appears, select the **Skip graceful shutdown (if applicable)** checkbox before confirming to stop or delete the instance.

    * **Google Cloud CLI** : include the `--no-graceful-shutdown` flag in the command.

    * **REST API** : include the `noGracefulShutdown=true` query parameter in the request URL.


**Caution:** Ensure that all tasks in the guest OS have finished running before the graceful shutdown period times out, or you manually end the graceful shutdown. Otherwise, Compute Engine forcefully stops any running tasks, which can potentially lead to data loss or corrupt file systems.

When the graceful shutdown process ends, Compute Engine sends the [Advanced Configuration and Power Interface (ACPI) G2 Soft Off signal](https://en.wikipedia.org/wiki/ACPI#Global_states) to the guest OS, sets the instance state to `STOPPING`, and then continues with the stop or delete operation.

### Stopping or deleting without graceful shutdown

After you've enabled graceful shutdown in an instance, you can still stop or delete it without going through the graceful shutdown process. This approach helps you save costs when, for example, you don't need to gracefully shut down your instance on a specific day, or if the workload running on the instance has changed.

To skip graceful shutdown, do one of the following:

  * **Skip graceful shutdown for single operations**. Keep graceful shutdown enabled, but bypass it for specific stop or delete operations. To do this, follow the manual shutdown process.

  * **Disable graceful shutdown entirely**. If you no longer need to gracefully shut down an instance, then you can disable this feature. For more information, see [Disable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/disable-graceful-shutdown).




## Limitations

Graceful shutdown has the following limitations:

  * You can't enable graceful shutdown in the following compute instances:

    * Instances that are part of a managed instance group (MIG).

    * Instances that specify a [limited runtime](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime).

  * After you enable graceful shutdown in an instance, you can't do the following:

    * You can't update instance properties that [require a restart](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties#updatable-properties).

    * If the instance is a TPU VM, then you can't simulate host maintenance events.

  * If a graceful shutdown is in progress (`PENDING_STOP`), then you can't do the following:

    * You can't update instance properties.

    * If the instance is being deleted, then you can't enable or disable [deletion protection](https://docs.cloud.google.com/compute/docs/instances/preventing-accidental-vm-deletion).

  * Your instance doesn't gracefully shut down, or a graceful shutdown is interrupted, if the following occurs:

    * Your Spot VM or preemptible instance is [preempted](https://docs.cloud.google.com/compute/docs/instances/spot#preemption-process).

    * Your instance has a [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties) set to `TERMINATE`, and Compute Engine stops the instance for a host event.

  * You can only gracefully shut down and delete up to 8,000 instances at a time per project and per region.

  * You can gracefully shut down or modify graceful shutdown settings for instances created in bulk only after Compute Engine finishes creating all instances.




## Pricing

There is no cost to enable or disable graceful shutdown in a compute instance. However, when you stop or delete an instance that has graceful shutdown enabled, you continue to incur charges for the instance as if it was running. These charges stop when the graceful shutdown period ends and the instance state changes to `STOPPING`.

For more detailed pricing information, see [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing).

## What's next

  * [Enable graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/enable-graceful-shutdown)

  * [View graceful shutdown in a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/view-graceful-shutdown)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
