---
url: https://docs.cloud.google.com/compute/docs/instances/preemptible/
title: Preemptible VM instances \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:18:00.464236+00:00
---

# Preemptible VM instances  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/preemptible/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Preemptible VM instances Stay organized with collections  Save and categorize content based on your preferences. 

**Important:** Spot VMs are the latest version of preemptible VMs, and we recommend using Spot VMs instead of preemptible VMs. New and existing preemptible VMs continue to be available, and preemptible VMs use the same pricing model as Spot VMs. However, Spot VMs provide new features that preemptible VMs don't support. For example, preemptible VMs can only run for up to 24 hours at a time, but Spot VMs don't have a maximum runtime unless you [limit the runtime](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime). Learn more about [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot) and how to [create Spot VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-spot).

This page describes preemptible virtual machine (VM) instances. To learn how to create a preemptible instance, read [Create and use preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible). To learn more about instances in general, read the [Virtual machine instances](https://docs.cloud.google.com/compute/docs/instances) documentation.

## What is a preemptible instance?

Preemptible VM instances are available at much lower price—a up to 91% discount—compared to the price of standard VMs. However, Compute Engine might stop (preempt) these instances if it needs to reclaim the compute capacity for allocation to other VMs. Preemptible instances use excess Compute Engine capacity, so their availability varies with usage.

If your apps are fault-tolerant and can withstand possible instance preemptions, then preemptible instances can reduce your Compute Engine costs significantly. For example, batch processing jobs can run on preemptible instances. If some of those instances stop during processing, the job slows but does not completely stop. Preemptible instances complete your batch processing tasks without placing additional workload on your existing instances and without requiring you to pay full price for additional normal instances.

## Preemptible instance limitations

Preemptible instances function like normal instances but have the following limitations:

  * Compute Engine might stop preemptible instances at any time due to system events. The probability that Compute Engine stops a preemptible instance for a system event is generally low, but might vary from day to day and from zone to zone depending on current conditions.
  * Compute Engine always stops preemptible instances after they run for 24 hours. Certain actions reset this 24-hour counter.
  * Preemptible instances are finite Compute Engine resources, so they might not always be available.
  * Preemptible instances can't [live migrate](https://docs.cloud.google.com/compute/docs/instances/live-migration-process#limitations) to a regular VM instance, or be set to [automatically restart](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#limitations) when there is a maintenance event.
  * Due to the preceding limitations, preemptible instances are not covered by any Service Level Agreement and are excluded from the [Compute Engine SLA](https://cloud.google.com/compute/sla).
  * The [Google Cloud Free Tier](https://docs.cloud.google.com/free/docs/free-cloud-features) credits for Compute Engine do not apply to preemptible instances.



## Preemption of preemptible VMs

This section describes how preemptible VMs are preempted by Compute Engine and which VMs are selected for preemption.

### Preemption process

Compute Engine performs the following steps to preempt an instance:

  1. Compute Engine sends a preemption notice to the instance in the form of an [ACPI G2 Soft Off](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states) signal. You can use a [shutdown script](https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible#handle_preemption) to handle the preemption notice and complete cleanup actions before the instance stops. The shutdown period for a preemption notice is best effort and up to 30 seconds.
  2. If the instance has not stopped after the shutdown period for the preemption notice, Compute Engine sends an [ACPI G3 Mechanical Off](https://en.wikipedia.org/wiki/Advanced_Configuration_and_Power_Interface#Power_states) signal to the operating system.
  3. Compute Engine transitions the instance to a `TERMINATED` state.



You can simulate an instance preemption by [stopping the instance](https://docs.cloud.google.com/compute/docs/instances/stop-start-instance#stopping_an_instance).

Preempted instances still appear in your project, but you are not charged for the instance hours while it remains in a `TERMINATED` state. You can access and recover data from any persistent disks that are attached to the instance, but those disks still incur storage charges until you delete them. As with normal instances, persistent disks that are marked for auto-delete are deleted when you delete the preemptible instance. You can restart a preempted instance as many times as you would like, as long as there is capacity. Restarting a preemptible instance resets the preemptible process.

If Compute Engine stops a preemptible instance less than one minute after it is created, you are not billed for the use of that VM instance. This ensures that you don't pay for preemptible instances unless they have had time to complete a significant amount of work. However, the charges for premium operating systems are still calculated as normal.

### Preemption selection

See our [best practices](https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible#best_practices) for suggestions on reducing your preemption rate. Note that Compute Engine doesn't charge you for instances if they are preempted in the first minute after they start running.

Certain actions reset the 24-hour counter for preemptible instances. Specifically, if you [stop](https://docs.cloud.google.com/compute/docs/instances/stopping-or-deleting-an-instance#stop_an_instance) and [start](https://docs.cloud.google.com/compute/docs/instances/restarting-an-instance#restarting_a_stopped_instance) an instance, Compute Engine resets the counter because the instance transitions into a `TERMINATED` state. However, other actions, where the instance remains in `RUNNING` state, don't reset the counter, for example, [resetting or rebooting an instance](https://docs.cloud.google.com/compute/docs/instances/reset-instance).

## Pricing

Preemptible VMs use spot prices, the same pricing model as Spot VMs. For more information about the pricing of preemptible VMs, see [pricing for Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot#pricing).

## Using preemptible VMs with Compute Engine

This section provides notable information about using preemptible VMs with other Compute Engine offerings. Learn about using preemptible VMs with managed instance groups, premium operating systems, local SSDs, and GPUs. Additionally, understand how preemptible VMs affect your quotas for Compute Engine resources.

### Preemptible instances in a managed instance group

You can create preemptible instances in a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/manager). Specify the preemptible option in the [instance template](https://docs.cloud.google.com/compute/docs/instance-templates) before you create or update the group.

Managed instance groups can create or add new preemptible instances only when additional Compute Engine resources are available. If these resources are limited, managed instance groups are unable to resize or automatically scale the number of preemptible instances in the group.

Managed instance groups always attempt to maintain their target size or the size specified by the [autoscaler](https://docs.cloud.google.com/compute/docs/autoscaler) for that group. If Compute Engine stops a preemptible instance in a managed instance group, the group repeatedly tries to recreate that instance using the specified [instance template](https://docs.cloud.google.com/compute/docs/instance-templates). If the necessary resources become available again, the group recreates the instance and maintains the target group size.

### Premium operating systems on preemptible instances

Preemptible instances don't reduce the cost of [premium operating systems](https://cloud.google.com/compute/disks-image-pricing#premiumimages) and don't change the way that you're billed for the use of those operating systems. If Compute Engine stops a preemptible instance that runs a premium operating system, you are billed for that operating system as if you stopped the instance yourself. The charges for minimum usage still apply, and bills for premium operating systems are still calculated by rounding up to the nearest usage increment.

The machine types on preemptible instances that run premium operating systems are always billed by the second, and follow the prices listed on the [VM instance pricing](https://cloud.google.com/compute/vm-instance-pricing) page.

### Local SSDs on preemptible instances

If you start a [Spot VM](https://docs.cloud.google.com/compute/docs/instances/spot) or preemptible VM with a Local SSD disk, Compute Engine charges discounted [spot prices](https://docs.cloud.google.com/compute/disks-image-pricing#localssdpricing) for the Local SSD usage. Local SSD disks that are attached to Spot VMs or preemptible VMs work like normal Local SSD disks, retain the same [data persistence characteristics](https://docs.cloud.google.com/compute/docs/disks/local-ssd#data_persistence), and remain attached for the life of the VM.

Compute Engine doesn't charge you for Local SSD disk usage on a Spot VM or preemptible VM if the VM is preempted within a minute after it starts running.

### GPUs on preemptible instances

You can add GPUs to your preemptible VM instances at lower [spot prices](https://cloud.google.com/compute/gpus-pricing) for the GPUs. GPUs attached to preemptible instances work like normal GPUs but persist only for the life of the instance. Preemptible instances with GPUs follow the same [preemption process](https://docs.cloud.google.com/compute/docs/instances/preemptible#preemption_process) as all preemptible instances.

Consider requesting dedicated `Preemptible GPU` quota to use for GPUs on preemptible instances. For more information, see [Quotas for preemptible VM instances](https://docs.cloud.google.com/compute/docs/instances/preemptible#quotas).

During maintenance events, preemptible instances with GPUs are preempted by default and cannot be automatically restarted. If you want to recreate your instances after they have been preempted, use a [managed instance group](https://docs.cloud.google.com/compute/docs/instance-groups/manager). Managed instance groups recreate your instances if the vCPU, memory, and GPU resources are available.

If you want a warning before your instance is preempted, or want to configure your instance to automatically restart after a maintenance event, use a standard instance with a GPU. For standard instances with GPUs, Google provides [one hour advance notice](https://docs.cloud.google.com/compute/docs/gpus/gpu-host-maintenance) before preemption.

Compute Engine does not charge you for GPUs if their instances are preempted in the first minute after they start running.

For steps to automatically restart a standard instance, see [Updating options for an instance](https://docs.cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#updatingoption).

To learn how to create preemptible instances with GPUs attached, read [Create a VM with attached GPUs](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus).

### Quotas for preemptible VM instances

Like other VMs, preemptible VMs require available [CPU quotas](https://docs.cloud.google.com/compute/resource-usage#cpu_quota). Additionally, if you plan to use preemptible VMs with local SSDs or with GPUs, preemptible VMs also require [disk quota](https://docs.cloud.google.com/compute/resource-usage#disk_quota) and [GPU quota](https://docs.cloud.google.com/compute/resource-usage#gpu_quota) respectively.

If you use preemptible VMs with these resources and have not requested preemptible quota, then preemptible VMs consume your standard quota for these resources. If you plan to use preemptible VMs, consider requesting preemptible quota for those resources to prevent preemptible VMs from consuming your quotas.

After Compute Engine grants you preemptible quota in a region, all preemptible VMs (and any [Spot VMs](https://docs.cloud.google.com/compute/docs/instances/spot)) in that region count against that quota. All standard VMs in that region continue to count against the standard quota. In regions where you don't have preemptible quota, you can use standard quota to launch preemptible VMs.

**Note:** Once you request preemptible quota in a region, you are limited to using that quota for preemptible VMs in that region. You can't consume standard quota in its place.

Preemptible quota is not visible in the gcloud CLI or Google Cloud console quota pages unless Compute Engine has granted the quota. For more information, see [Allocation quotas for preemptible resources](https://docs.cloud.google.com/compute/resource-usage#allocation_quotas_for_preemptible_resources).

## What's next?

  * [Create and use preemptible VMs](https://docs.cloud.google.com/compute/docs/instances/create-use-preemptible).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
