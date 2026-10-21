---
url: https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy/
title: Compact placement policy and workload policy overview \u00a0|\u00a0 AI Hypercomputer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T05:34:54.400437+00:00
---

# Compact placement policy and workload policy overview  |  AI Hypercomputer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ai-hypercomputer/docs/placement-policy-and-workload-policy/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ AI Hypercomputer ](https://docs.cloud.google.com/ai-hypercomputer/docs)
  * [ Guides ](https://docs.cloud.google.com/ai-hypercomputer/docs/overview)



Send feedback 

#  Compact placement policy and workload policy overview Stay organized with collections  Save and categorize content based on your preferences. 

[ General GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-general-gpus) [ Clustered GPUs ](https://docs.cloud.google.com/ai-hypercomputer/docs/evaluate-clustered-gpus)

This document provides an overview and comparison of compact placement policies and workload policies. Both policies let you configure the placement of Compute Engine instances to minimize network latency.

**Important:** When creating multiple instances for machine series that support partitioning, such as A4X Max and A4X, you must apply a compact placement policy or a workload policy.

By default, you manage the location of your compute instances by specifying only their zones. To create compute instances that are closer to each other, you can use the following options. For more information, also see [AI infrastructure resources colocation](https://docs.cloud.google.com/ai-hypercomputer/docs/cluster-capabilities#dense_colocation_of_accelerator_resources).

  * The following resources are already densely colocated with each other:

    * Resources that consume the same future reservation for capacity blocks.
    * Resources that consume the same future reservation in calendar mode.
    * Resources that you create together through a managed instance group (MIG) resize request.
  * Resources that you create together when you specify the Flex-start consumption option might be densely colocated based on best-effort availability. If you instead require densely colocated resources, apply either a compact placement policy that specifies a max distance or a workload policy that specifies a max distance.

  * Otherwise, to place resources close together, apply a compact placement policy or a workload policy.

    * When you require densely colocated resources, specify a max distance in the policy.
    * When you want densely colocated resources based on best-effort availability, don't specify a max distance in the policy.



For more information about when to use a compact placement policy versus a workload policy, see Comparison of compact placement policy and workload policy in this document.

## Comparison of compact placement policy and workload policy

The following table summarizes the differences between compact placement policies and workload policies:

****| **Compact placement policy** | **Workload policy**  
---|---|---  
**Policy usage** | 

  * Standalone instances
  * Instances deployed using Bulk API
  * MIGs with general GPUs

| MIGs with clustered GPUs  
**Supported machine types** | A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High, A3 Edge, A2, G4, and G2 | 

  * **For Flex-start** : A4 and A3 Ultra
  * **For Spot or reservations** : A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs)

  
**Grouping semantics** | Compute Engine places the instances that use the same compact placement policy closer together. We recommend that you use a different placement policy for each workload. Reusing a placement policy across instances that run different workloads causes all those instances to be placed together. This colocation can make it difficult to create instances that are close together when you scale out a specific workload. | Compute Engine places the instances in a MIG that uses a workload policy closer together. Reusing a workload policy across multiple MIGs that run different workloads places the instances in individual MIGs together. Reusing is ideal for large training models in which each group of instances has to be isolated from each other.  
**Compute instance colocation configuration** | For best-effort compute instance colocation, set the `groupPlacementPolicy.collocation` field to `COLLOCATED`. | For best-effort compute instance colocation, set the `workloadPolicy.type` field to `HIGH_THROUGHPUT`.  
**Additional configurations** | 

  * For strict compute instance placement, specify the `maxDistance` field.
  * For machine series that support partitioning, such as A4X Max and A4X, specify the `gpuTopology` field.

| 

  * For strict compute instance placement, specify the `maxTopologyDistance` field.
  * For machine series that support partitioning, such as A4X Max and A4X, specify the `acceleratorTopology` field.

  
  
For more information, see the following sections:

  * Compact placement policies
  * Workload policies



## Compact placement policies

When you apply compact placement policies to standalone compute instances, or compute instances created in bulk, Compute Engine makes best-effort attempts to create compute instances as close to each other as possible. If your application requires minimal network latency, then specify the `maxDistance` field ([Preview](https://cloud.google.com/products/#product-launch-stages)) when you create a compact placement policy.

For more information, see [About compact placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview#about-compact-policies) in the Compute Engine documentation.

### Comparison of maximum distance values for compact placement policies

A lower maximum distance value ensures closer compute instance placement, but it also increases the chance that some compute instances won't be created.

The following table shows the machine series and number of compute instances that each maximum distance value supports:

`maxDistance` in a compact placement policy | `maxTopologyDistance` in a workload policy | Description | Supported machine series | Maximum number of compute instances  
---|---|---|---|---  
Unspecified (Not recommended) | Unspecified (Not recommended) | Compute Engine makes best-effort attempts to place the compute instances as close to each other as possible, but with no maximum distance among compute instances. | A4X Max, A4X, A4, A3 Ultra, A3 Mega1, A3 High1, A3 Edge1, A2, G4, and G2 | 1500  
`3` | `CLUSTER` | Compute Engine creates compute instances in adjacent blocks. | A4, A3 Mega1, A3 High1, A3 Edge1, A2, G4, and G2 | 1,500  
`2` | `BLOCK` | Compute Engine creates compute instances in the same block. | A4, A3 Ultra, A3 Mega1, A3 High1, A3 Edge1, A2, G4, and G2 | 

  * **For A3 Ultra, A3 Mega 1, A3 High1, and A3 Edge1**: 256
  * **For all other supported machine series** : 150

  
`1` | `SUBBLOCK` | Compute Engine creates compute instances in the same sub-block. | A3 Edge1, A2, G4, and G2 | 22  
  
1 If you want to apply a compact placement policy to an A3 Mega, A3 High, or A3 Edge instance that was created before October 1, 2025, then contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

## Workload policies

Workload policies let you specify the placement and underlying infrastructure for the compute instances in a MIG. Using workload policies with A4X Max, A4X, A4, A3 Ultra, A3 Mega, and A3 High (8 GPUs) helps you minimize network latency among compute instances and optimize performance.

Based on the machine types that the compute instances in your MIG use, workload policies are required or optional in the following situations:

  * To deploy sub-blocks of A4X Max or A4X instances, workload policies are required.

  * To use A4, A3 Ultra, A3 Mega, or A3 High (8 GPUs) instances, workload policies are optional.

  * Workload policy is not supported for A3 Edge, A2, G4, G2, and N1 machine series. For MIGs that use these machine series, you can use compact placement policy for VM colocation.




For more information, see [About workload policies in MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies) in the Compute Engine documentation.

## What's next

  * [Deployment options overview](https://docs.cloud.google.com/ai-hypercomputer/docs/create/create-overview)

  * [View topology of a compute instance](https://docs.cloud.google.com/ai-hypercomputer/docs/manage/instance-topology)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
