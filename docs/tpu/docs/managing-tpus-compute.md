---
url: https://docs.cloud.google.com/tpu/docs/managing-tpus-compute/
title: Manage TPU resources with Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:26:16.727143+00:00
---

# Manage TPU resources with Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/tpu/docs/managing-tpus-compute/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud TPU ](https://docs.cloud.google.com/tpu/docs)
  * [ Guides ](https://docs.cloud.google.com/tpu/docs/intro-to-tpu)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage TPU resources with Compute Engine

This page describes how to connect to, view information about, delete, or reset a TPU VM using Compute Engine.

## Manage TPU VMs

You interact with your TPU VMs like any Compute Engine VM. However, you cannot suspend or stop TPU VMs. You also cannot reset multi-host TPU VMs.

## Connect to a TPU VM

You connect to TPU VMs the same way you connect to any other Compute Engine instance. For more information, see [Connect to Linux VMs](https://docs.cloud.google.com/compute/docs/connect/standard-ssh).

## View information about TPU VMs

You can view information about TPU VMs and MIGs in the same way as any Compute Engine instance or MIG.

  * To list all VMs in your project, see [Get a list of VMs](https://docs.cloud.google.com/compute/docs/instances/get-list).
  * To list all of your MIGs, see [List MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#list_migs).
  * To view the details of a TPU VM, see [View the details of a VM](https://docs.cloud.google.com/compute/docs/instances/view-vm-details).
  * To view information about a MIG, see [View a MIG's properties](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#getting_a_migs_properties).
  * To view the status of a multi-host TPU slice, see [View the status of a TPU slice](https://docs.cloud.google.com/compute/docs/instance-groups/getting-info-about-migs#view_the_status_of_a_tpu_slice).
  * To view the topology and health of All Capacity mode TPU instances, see [View the topology and health of All Capacity mode TPUs](https://docs.cloud.google.com/tpu/docs/view-all-capacity-topology-tpus).



## Reset a TPU VM instance

Resetting a TPU VM instance is similar to resetting your computer, for example, by pressing a reset button or holding the power button. A reset operation doesn't perform a graceful reboot, and you might lose unsaved data. We recommend that you reset an instance in the following scenarios:

  * You want to re-initialize the instance to its boot state to help ensure optimal performance and stability.
  * You want to resume your workload after your guest OS has crashed and is unresponsive, and you have no other options than resetting the instance.



For more information on resetting a TPU VM instance, see [Reset operation](https://docs.cloud.google.com/compute/docs/instances/suspend-stop-reset-instances-overview#resetting-instance) in the Compute Engine documentation.

## Delete a TPU VM instance

To learn how to delete a TPU VM instance, see [Delete a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/deleting-instance) in the Compute Engine documentation.

## Update a TPU VM instance properties

You can update instance properties for running TPU VM instances. For more information, see [Update instance properties](https://docs.cloud.google.com/compute/docs/instances/update-instance-properties).

## Apply new VM configurations in a MIG

For information about applying new TPU VM configurations in a managed instance group (MIG), see [Apply new VM configurations in a MIG](https://docs.cloud.google.com/compute/docs/instance-groups/updating-migs).

## What's next

  * Learn how to [Create a MIG with single-host TPU slices](https://docs.cloud.google.com/tpu/docs/create-single-host-mig).
  * Learn how to [Create a MIG with a multi-host TPU slice](https://docs.cloud.google.com/tpu/docs/create-multi-host-mig).
  * Learn about [TPUs in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/tpus).
  * Learn how to run an ML workload on TPUs, for example, [Serve Qwen2-7B-Instruct with vLLM on TPUs](https://docs.cloud.google.com/ai-hypercomputer/docs/tutorials/tpu/serve-qwen2-7b-instruct).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
