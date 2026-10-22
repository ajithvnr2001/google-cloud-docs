---
url: https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle/
title: Compute Engine instance lifecycle \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:49:13.402079+00:00
---

# Compute Engine instance lifecycle  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Compute Engine instance lifecycle Stay organized with collections  Save and categorize content based on your preferences. 

A Compute Engine instance transitions through different states from the time you create it until you delete it. This document explains the compute instance lifecycle to help you troubleshoot issues, manage resources, plan migrations, and understand costs.

To check the current state of your compute instances, see instead the following:

  * [View a list of compute instances](https://docs.cloud.google.com/compute/docs/instances/get-list)

  * [View the details of a single compute instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)




## Compute instance states

When you create a compute instance, it starts in the `PROVISIONING` state, moves to `STAGING`, and then enters the `RUNNING` state. Flex-start virtual machine (VM) instances with a wait time (`requestValidForDuration`) and TPU instances start instead in the `PENDING` state. From the `RUNNING` state, you can move a compute instance to the `SUSPENDED` or `TERMINATED` states, or you can delete it.

**Important:** You control the lifecycle of your compute instances. However, [scheduled operations](https://docs.cloud.google.com/compute/docs/instances/schedule-instance-start-stop), [provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models), or [host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#hosterror) can also trigger state changes.

The following diagram shows the different states that Compute Engine can set a compute instance to:

![A flowchart of the different states for a compute instance.](https://docs.cloud.google.com/static/compute/images/instance-lifecycle.png)

The states shown in the preceding diagram are described in the following sections:

  * `PENDING` state

  * `PROVISIONING` state

  * `STAGING` state

  * `RUNNING` state

  * `PENDING_STOP` state

  * `STOPPING` state

  * `TERMINATED` state

  * `REPAIRING` state

  * `SUSPENDING` state

  * `SUSPENDED` state




### `PENDING` state

After you create a compute instance, it enters the `PENDING` state if it's one of the following. Otherwise, the compute instance directly transitions to the `PROVISIONING` state.

  * A [Flex-start VM](https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms) with a wait time (`requestValidForDuration`) that is 90 seconds or longer.

  * A standalone TPU instance.

  * A Flex-start VM or TPU instance that is part of a managed instance group (MIG), unless the MIG has [creation retries disabled](https://docs.cloud.google.com/compute/docs/instance-groups/add-remove-vms-in-mig#disabling_creation_retries_mode_during_resize).




In the `PENDING` state, Compute Engine attempts to acquire the necessary resources to start your compute instance until its wait time ends. If Compute Engine acquires the resources within this time and you have sufficient quota for those resources, then the compute instance state changes to `PROVISIONING`. Otherwise, you encounter an error and Compute Engine deletes the compute instance. You can optionally delete the compute instance before the wait time ends if you no longer need it.

### `PROVISIONING` state

After you create, restart, or resume a compute instance, Compute Engine starts allocating resources for the compute instance and sets its state to `PROVISIONING`. When Compute Engine finishes allocating resources, the compute instance transitions to the `STAGING` state.

### `STAGING` state

In the `STAGING` state, Compute Engine prepares the compute instance for first boot due to one of the following reasons:

  * Compute Engine is still creating and configuring the compute instance.

  * You, or a scheduled operation, restart or resume the compute instance.




In this state, the compute instance isn't running yet. When it does start running or starts booting up, the compute instance enters the `RUNNING` state.

### `RUNNING` state

In the `RUNNING` state, Compute Engine is booting up the compute instance or the compute instance is running. From the `RUNNING` state, a compute instance can transition to `PENDING_STOP`, `STOPPING`, `SUSPENDING`, or `REPAIRING` depending on the action taken, system events, or compute instance configuration.

### `PENDING_STOP` state

In the `PENDING_STOP` state, the compute instance starts to gracefully shut down. This shutdown process happens only if you've enabled [graceful shutdown](https://docs.cloud.google.com/compute/docs/instances/graceful-shutdown-overview). The compute instance enters this state if you stop or delete the compute instance, or Compute Engine is doing so automatically for a scheduled stop or deletion. The compute instance state changes to `STOPPING` when one of the following happens:

  * You manually end the graceful shutdown.

  * The graceful shutdown period times out. If any tasks are still running, then Compute Engine forcefully stops them.




### `STOPPING` state

In the `STOPPING` state, the compute instance is shutting down its guest OS. This process happens in the following scenarios:

  * You, or a scheduled operation, stop or delete the compute instance.

  * A host error occurs.




Unless you configure the compute instance to [skip the guest OS shutdown](https://docs.cloud.google.com/compute/docs/instances/decrease-shutdown-time), the shutdown time depends on the [compute instance type](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#stopping-instance). However, if the compute instance stops due to a host error, the shutdown time might differ from the expected length. After the guest OS shuts down, the ongoing stop or delete operation ends as follows:

  * **Stop operation** : the compute instance state changes to `TERMINATED`.

  * **Delete operation** : Compute Engine permanently deletes the compute instance and all its attached resources.




### `TERMINATED` state

When a compute instance enters the `TERMINATED` state, Compute Engine completes the stop operation. The compute instance remains in the `TERMINATED` state until you, or a scheduled operation, restart or delete it. If you request to restart the compute instance, but Compute Engine can't allocate your requested resources, then the restart request fails and the compute instance remains in the `TERMINATED` state. Otherwise, the restart request succeeds and the compute instance state changes to `PROVISIONING`.

### `REPAIRING` state

In the `REPAIRING` state, Compute Engine starts a [repair operation on the compute instance](https://docs.cloud.google.com/compute/docs/instance-groups/about-repair). Compute Engine repairs a compute instance if it encounters an internal error or the compute instance's host server is unavailable due to maintenance. While a compute instance is in repair, the following happens:

  * You can't use the compute instance.

  * The [service level agreement (SLA)](https://cloud.google.com/compute/sla) doesn't cover the compute instance.




If Compute Engine successfully repairs the compute instance, then it returns the compute instance state to its original state before the repair operation began. This state can be `STAGING`, `RUNNING`, `SUSPENDING`, or `STOPPING`. If your compute instance is configured to automatically restart (`automaticRestart`) after the repair operation completes, then you can optionally stop the compute instance during the repair process. This action prevents the compute instance from automatically restarting after the repair completes, leaving the compute instance in the `TERMINATED` state.

### `SUSPENDING` state

In the `SUSPENDING` state, Compute Engine starts the suspend operation for the compute instance. You can only suspend [specific compute instances](https://docs.cloud.google.com/compute/docs/instances/suspend-resume-instance#limitations). When the suspend operation completes, the compute instance state changes to `SUSPENDED`.

### `SUSPENDED` state

In the `SUSPENDED` state, Compute Engine completes the suspend operation. You can resume or delete the compute instance. If you request to resume the compute instance, but Compute Engine can't allocate your requested resources, then the resume request fails and the compute instance remains in the `SUSPENDED` state. Otherwise, the resume request succeeds and the compute instance state changes to `PROVISIONING`.

A compute instance can remain in the `SUSPENDED` state for up to 60 days. After that time, Compute Engine changes the compute instance state to `TERMINATED`.

## Compute instance pricing

During a compute instance lifecycle, you incur charges for the compute instance as follows:

  * For CPU usage, you incur charges when the compute instance is in the following states:

    * `RUNNING`

    * `PENDING_STOP`

  * For memory usage, you incur charges when the compute instance is in the following states:

    * `RUNNING`

    * `PENDING_STOP`

    * `SUSPENDING`

    * `SUSPENDED`

  * For attached resources like disks or external IP addresses, you incur charges while the resources exist, regardless of the compute instance state.




For more information, see the [pricing for compute instances](https://cloud.google.com/compute/vm-instance-pricing).

## What's next

  * Learn how to view the state of one or more compute instances by doing the following:

    * [View a list of compute instances](https://docs.cloud.google.com/compute/docs/instances/get-list)

    * [View the details of a single compute instance](https://docs.cloud.google.com/compute/docs/instances/view-vm-details)

  * Learn more about [suspending, stopping, or resetting compute instances](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview).

  * Learn more about [host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview).

  * Learn how to [delete a compute instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
