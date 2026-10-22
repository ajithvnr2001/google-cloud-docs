---
url: https://docs.cloud.google.com/dataflow/docs/guides/compute-engine-reservations/
title: Use Compute Engine reservations with Dataflow \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:20.873275+00:00
---

# Use Compute Engine reservations with Dataflow  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataflow/docs/guides/compute-engine-reservations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Dataflow ](https://docs.cloud.google.com/dataflow/docs)
  * [ Guides ](https://docs.cloud.google.com/dataflow/docs/overview)



Send feedback 

#  Use Compute Engine reservations with Dataflow Stay organized with collections  Save and categorize content based on your preferences. 

To ensure that VM resources are available when your Dataflow jobs need them, you can use Compute Engine reservations. Reservations provide a high level of assurance in obtaining capacity for Compute Engine zonal resources.

To use [_automatically consumed_](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) Compute Engine reservations with Dataflow, perform the following steps:

  1. Create a Compute Engine reservation. It can be a single-project reservation or a shared reservation. For more information, see the following documents:

     * [Create a reservation for a single project](https://docs.cloud.google.com/compute/docs/instances/reservations-single-project)
     * [Create a shared reservation](https://docs.cloud.google.com/compute/docs/instances/reservations-shared)

The reservation can include GPU or TPU accelerators.

  2. For the reservation to be consumed, the Dataflow worker configuration must match the reservation configuration (such as machine type, and accelerator settings). You might need to set the worker machine type for the job. For more information, see [Configure worker VMs](https://docs.cloud.google.com/dataflow/docs/guides/configure-worker-vm).

  3. Submit your Dataflow job.

  4. You can monitor the current usage of the reservation by Dataflow on the [Reservations](https://console.cloud.google.com/compute/reservations) page in Google Cloud console.




To prevent low-priority workloads in the same project from competing for reservations with Dataflow, set the reservation affinity to `none` when you create VMs for those workloads. For more information, see [Consuming reserved instances](https://docs.cloud.google.com/compute/docs/instances/reserving-zonal-resources#consuming_reserved_instances).

## Limitations

  * All limitations of Compute Engine reservations apply when Dataflow workers consume reservations. See [How reservations work](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#how-reservations-work).

  * Dataflow relies on the [default consumption order](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-order) in Compute Engine. As a result, the following limitations apply:

    * Other workloads in the same project or Organization that don't specify the `--reservation` flag might compete with Dataflow workloads for project-specific or shared reservations.
  * Dataflow Prime jobs don't consume Compute Engine reservations.




## Reservations and accelerators

Dataflow supports [_specifically targeted_ reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-consume#consuming_instances_from_a_specific_reservation) for pipelines using accelerators (GPUs or TPUs). This functionality is generally available with an allowlist. For instructions on using Dataflow accelerators with specific reservations, contact your account team.

## Pricing

Dataflow bills you for VMs from _automatically consumed_ reservations while your Dataflow job runs. When Dataflow isn't using the VMs, Compute Engine bills you.

### Compute Engine pricing model

If your Dataflow usage includes VMs from [_specifically targeted_ reservations](https://docs.cloud.google.com/compute/docs/instances/reservations-overview#consumption-type) that have GPUs or TPUs, then compute resources from those reserved VMs are billed according to [Compute Engine Pricing](https://cloud.google.com/compute/all-pricing). If your _specifically targeted_ reservations are attached to a [Compute Engine resource-based commitment](https://docs.cloud.google.com/compute/docs/instances/signing-up-committed-use-discounts), then you also receive applicable resource-based committed use discounts (CUDs) for your usage. You're also billed a management premium for compute resources consumed in Dataflow. For more pricing details, see [ Dataflow Pricing](https://cloud.google.com/dataflow/pricing).

### Dataflow pricing model

For any other type of Compute Engine reservations that you use with Dataflow, your usage is billed by using the [Dataflow pricing model](https://cloud.google.com/dataflow/pricing). Dataflow usage from those reservations isn't eligible for resource-based CUDs, even if those reservations are attached to a resource-based commitment. This applies to the following Compute Engine reservations:

  * _Specifically targeted_ reservations that don't have GPUs or TPUs
  * All _automatically consumed_ reservations



## What's next

To learn more about Compute Engine reservations, see [Reservations of Compute Engine zonal resources](https://docs.cloud.google.com/compute/docs/instances/reservations-overview).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
