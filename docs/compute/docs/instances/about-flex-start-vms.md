---
url: https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms/
title: About Flex-start VMs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:41.464461+00:00
---

# About Flex-start VMs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/about-flex-start-vms/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About Flex-start VMs Stay organized with collections  Save and categorize content based on your preferences. 

This document provides an overview of Flex-start VMs, detailing their key characteristics, as well as the requirements and limitations that you apply when you create them.

Flex-start VMs are virtual machine (VM) instances that you create by using the flex-start provisioning model. This model uses the [Dynamic Workload Scheduler (DWS)](https://cloud.google.com/blog/products/compute/introducing-dynamic-workload-scheduler) to provision compute resources from a secure pool of capacity, improving your chances of obtaining high-demand resources like GPUs or TPUs. After you create Flex-start VMs, Compute Engine attempts to allocate your requested resources within a specific timeframe. If it succeeds, then your Flex-start VMs start running and keep running for a maximum of seven days.

For workloads that require resources for longer than seven days, or with a higher capacity assurance, you can [create a future reservation request in calendar mode](https://docs.cloud.google.com/compute/docs/instances/future-reservations-calendar-mode-overview).

## Flex-start VMs use cases

Flex-start VMs are ideal for running workloads that can start at any time, such as the following:

  * Small model pre-training

  * Model fine-tuning

  * High performance computing (HPC) simulation

  * Batch inference




## Flex-start VMs key characteristics

Compared to other types of Compute Engine instances, Flex-start VMs have the following characteristics:

  * **A wait time for allocating resources** : you can create Flex-start VMs before Compute Engine can allocate the requested resources. However, VMs only start if resources become available within your specified timeframe. If resources aren't available, then the VM creation request fails.

For more information, see Flex-start VM wait time in this document.

  * **A limited run duration** : Flex-start VMs run uninterrupted for up to seven days. After that time, Compute Engine automatically stops or deletes the VMs based on the termination action that is specified in the VM properties.

For more information, see Flex-start VM limited run duration in this document.

  * **How Compute Engine allocates VMs** : Compute Engine makes best-effort attempts to create Flex-start VMs in close proximity to minimize network latency. To control the placement of your Flex-start VMs, you can optionally use compact placement policies or workload policies.

For more information, see Flex-start VM allocation in this document.

  * **The flex-start provisioning model** : you create Flex-start VMs by using the flex-start provisioning model. This provisioning model provides improved resource availability compared to VMs that you create by using the standard provisioning model.

For more information about each provisioning model, see [Compute Engine instances provisioning models](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).




### Flex-start VM wait time

When you create a Flex-start VM, the VM doesn't immediately start. Compute Engine attempts to allocate your requested resources and start the VM within a specific timeframe. If you have sufficient quota for your requested resources and Compute Engine allocates them by the end of the wait time, then the Flex-start VM starts within two minutes of capacity becoming available. Otherwise, the VM creation request fails.

The wait time varies based on the method that you use to create VMs:

  * Standalone Flex-start VMs wait time

  * MIGs with Flex-start VMs wait time




#### Standalone Flex-start VMs wait time

To create a standalone Flex-start VM, you must specify a wait time by using the `requestValidForDuration` field. You can set a wait time of either zero seconds, or between 90 seconds and 7,200 seconds (two hours).

Based on your workload's zonal requirements, we recommend the following wait times to help increase the chances that your Flex-start VM creation request succeeds:

  * **Strict zonal requirements** : if your workload requires you to create a Flex-start VM in a specific zone, then we recommend that you set the `requestValidForDuration` field to 90 seconds or higher, up to two hours. Longer wait times help increase your chances of obtaining resources. The VM remains in the [`PENDING` state](https://docs.cloud.google.com/compute/docs/instances/instance-lifecycle#instance-states) throughout this time.

  * **No zonal requirements** : if the Flex-start VM can run in any zone in the region, then we recommend that you set the `requestValidForDuration` field to zero seconds. This value specifies that Compute Engine only allocates resources if they are immediately available. If your request fails because resources are unavailable, then try creating the Flex-start VM in a different zone.




To stop a VM creation request while Compute Engine attempts to allocate resources, delete the Flex-start VM.

#### MIGs with Flex-start VMs wait time

If you add Flex-start VMs to a managed instance group (MIG), then Compute Engine keeps attempting to provision your requested resources until it succeeds or you cancel the request. The way Compute Engine adds VMs to your MIG varies based on the creation method:

  * **MIG resize requests** : Compute Engine adds the requested VMs to the MIG all at once when _all_ resources become available. Unless you delete VMs before the end of their run duration, Compute Engine deletes the VMs at the same time. For more information, see [About MIG resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig).

  * **MIGs with a target size** : Compute Engine individually creates each VM when capacity becomes available. Thus, the MIG might initially create only a portion of the requested VMs, and then add the remaining VMs later as capacity permits. Unless you delete the VMs before the end of their run duration, Compute Engine deletes each VM relative to its own creation time. For more information, see [Create a MIG that uses Flex-start VMs](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms).




### Flex-start VM limited run duration

When you create a Flex-start VM, you must specify the following:

  * **The VM run duration** : you must specify how long the VMs can run. The run duration can be up to seven days. If your workload completes before the VMs' run duration ends, then you can stop or delete the standalone VMs, or delete the VMs in a MIG to avoid unnecessary costs.

  * **The VM termination action** : you must choose whether Compute Engine automatically stops or deletes the VMs at the end of their run duration. For Flex-start VMs in a MIG, you can only specify to delete VMs at the end of their run duration.

**Caution:** After Compute Engine stops a VM, you keep incurring charges for any resources that are attached to the VM, such as disks or IP addresses. To avoid unnecessary costs, detach and delete any resources that you no longer need, or delete the VM. For more information, see the [pricing for a VM's uptime](https://docs.cloud.google.com/compute/vm-instance-pricing#instanceuptime).



### Flex-start VM allocation

Compute Engine makes best-effort attempts to densely create your Flex-start VMs based on availability. This _dense_ placement minimizes network hops and optimizes for low latency, which is ideal for workloads that require constant VM communication, such as AI or ML workloads. If you want to control the placement of your Flex-start VMs to avoid them being unexpectedly created far apart, do the following:

  * For standalone Flex-start VMs, apply a [compact placement policy to your VMs](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies).

  * For MIGs with a target size, apply a [workload policy with a high throughput type to your MIG](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies).




## Quota

To create or restart Flex-start VMs, your project must have sufficient [preemptible quota](https://docs.cloud.google.com/compute/docs/gpus/create-vm-with-gpus#preemptible-quotas) for the requested vCPUs, memory, and any attached accelerators or Local SSD disks.

If you attempt to create or restart a Flex-start VM without sufficient quota, then one of the following scenarios occurs:

  * **VM creation requests** : the request remains pending until your project has sufficient quota. If your project lacks the required quota when the wait time expires, then the creation request fails.

  * **VM restart requests** : the request fails immediately.




## Pricing

For Flex-start VMs, you pay as you go (PAYG). For more information, see [DWS pricing](https://cloud.google.com/products/dws/pricing).

## Limitations

The following sections describe the limitations for Flex-start VMs.

### Limitations for all Flex-start VMs

All Flex-start VMs have the following limitations:

  * Flex-start VMs can only use the following machine types:

    * Any GPU machine types, except A4X Max and A4X

    * TPU7x, TPU v6e, and TPU v5p machine types 

    * H4D machine types

  * You must create Flex-start VMs by using the [flex-start provisioning model](https://docs.cloud.google.com/compute/docs/instances/provisioning-models).

  * You must specify whether to stop or delete Flex-start VMs at the end of their run duration by using the [`instanceTerminationAction` and `maxRunDuration` fields](https://docs.cloud.google.com/compute/docs/instances/limit-vm-runtime#set-duration). For MIGs, you can only specify to delete Flex-start VMs.

  * You must stop Flex-start VMs during [host maintenance events](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties).

  * You can only apply compact placement policies to standalone Flex-start VMs.

  * You can't apply spread placement policies to Flex-start VMs.

  * You can't use reservations.




### Limitations for MIGs with Flex-start VMs

All MIGs with Flex-start VMs have the following limitations:

  * You can use TPU machine types in Flex-start VMs only if you [create VMs in a MIG individually](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms) or by [using bulk mode](https://docs.cloud.google.com/compute/docs/instance-groups/about-bulk-mode).

  * You must [turn off repairs](https://docs.cloud.google.com/compute/docs/instance-groups/turn-off-vm-repairs-in-mig) in the MIG.

  * You must [delete the autoscaling configuration](https://docs.cloud.google.com/compute/docs/autoscaler/managing-autoscalers#delete_an_autoscaler).

  * You can only create Flex-start VMs in regional MIGs by using the following [target distribution shapes](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape):

    * For MIGs with a target size, you can only use `ANY` or `ANY_SINGLE_ZONE`.

    * For MIG resize requests, you can only use `ANY_SINGLE_ZONE`.

  * You can only set the [standby pool mode of the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/suspended-and-stopped-vms-in-mig#standby_policy) to `manual` (default).

  * You can't use [instance flexibility](https://docs.cloud.google.com/compute/docs/instance-groups/about-instance-flexibility).

  * You can't add a second instance template to initiate a [canary update in the MIG](https://docs.cloud.google.com/compute/docs/instance-groups/rolling-out-updates-to-managed-instance-groups#canary_updates).




Additionally, if you want to create Flex-start VMs by using MIG resize requests, see the [limitations for MIG resize requests](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig#limitations).

## What's next

  * To learn how to create standalone Flex-start VMs, see [Create a Flex-start VM](https://docs.cloud.google.com/compute/docs/instances/create-flex-start-vm).

  * To learn how to create Flex-start VMs in a MIG, see the following:

    * [Create Flex-start VMs in a MIG individually](https://docs.cloud.google.com/compute/docs/instance-groups/create-mig-with-flex-start-vms)

    * [Create GPU or H4D Flex-start VMs in a MIG all at once](https://docs.cloud.google.com/compute/docs/instance-groups/about-resize-requests-mig)

    * [Create TPU Flex-start VMs in a MIG all at once](https://docs.cloud.google.com/compute/docs/instance-groups/bulk-create-instances-in-mig)




##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how Compute Engine performs in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Try Compute Engine free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
