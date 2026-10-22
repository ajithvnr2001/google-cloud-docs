---
url: https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies/
title: About workload policies in MIGs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:19:29.698748+00:00
---

# About workload policies in MIGs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  About workload policies in MIGs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the requirements and limitations that you apply when using workload policies with managed instance groups (MIGs). By default, you manage the location of your Compute Engine instances only by specifying their zones. Workload policies let you define the physical placement and topology of your compute instances within a zone. This approach helps you, for example, minimize network latency across your compute instances by placing them closer to each other.

You can only apply workload policies to MIGs that use A4X Max, A4X, A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), H4D, or TPU (TPU7x, v6e, or v5p) instances. If you use A4X Max or A4X instances, or create a MIG with a multi-host TPU slice, then a workload policy is required unless you create a single compute instance for testing purposes. For the other supported machine series, workload policies are optional.

To control the placement of compute instances that use other machine series, use [placement policies](https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview).

## Understand workload policies

The following sections describe workload policy use cases and the properties that you specify when you create workload policies.

### Manage compute instance placement and topology

After you create a workload policy and apply it to a MIG, workload policies help you achieve the following:

  * **Create compute instances close to each other** : if capacity is available, then Compute Engine creates compute instances close to each other. Otherwise, Compute Engine creates only some or none of your requested compute instances.

  * **Gain visibility into your compute instance topology** : after you apply a workload policy with a high throughput (`HIGH_THROUGHPUT`) type to a MIG, and the MIG creates compute instances, you can view the position of the compute instances in relation to each other. This information helps you minimize network latency and troubleshoot errors. For more information, see [View the physical location of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).




You can apply the same workload policy to multiple MIGs. When you do so, Compute Engine applies the placement rules to each MIG independently.

The following section describes the properties that you must specify when you create workload policies.

### Configure workload policy properties

When you create a workload policy, you must specify the following properties:

  * **Workload type (`type`)**: this field defines the high-level goal of your cluster. You can only specify `HIGH_THROUGHPUT`, which instructs Compute Engine to place compute instances as close together as possible to speed up communication.

  * Based on the machine series that the compute instances in your MIG use, you can optionally specify one of the following properties:

    * **Accelerator topology (`acceleratorTopology`)**: this property helps you to achieve high performance for distributed workloads that run across multiple A4X Max or A4X instances, or multi-host TPU slices, that use a specialized inter-accelerator network configuration. For more information, see Accelerator topology property.

    * **Maximum topology distance (`maxTopologyDistance`)**: this property defines the strictest physical boundary for creating your A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D instances, such as the same block or sub-block. If Compute Engine can't meet this strict limit due to resource availability errors, then it creates only part, or none, of your requested compute instances. For more information, see Maximum topology distance property.




#### Accelerator topology property

To achieve large-scale, non-blocking network performance, Compute Engine organizes A4X Max and A4X instances into a physical hierarchy of [_blocks_ and _sub-blocks_](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology#overview).

To create a MIG with A4X Max or A4X instances, or multi-host TPU slices, you must apply a workload policy to the MIG that specifies the accelerator topology (`acceleratorTopology`) property. This property defines the physical network configuration for a _slice_ of compute instances. A slice acts as a single, massive accelerator that provides maximum throughput for your distributed AI or ML workloads.

The following table shows the accelerator topology values for A4X Max and A4X. For more information about topology values for multi-host TPU slices, see [TPU topology](https://docs.cloud.google.com/compute/docs/tpus/tpu-machines#tpu_topology).

Accelerator topology value | Description | Supported machine series | Maximum number of compute instances  
---|---|---|---  
`1x72` | Compute Engine organizes compute instances into densely allocated sub-blocks of 18 compute instances, totaling 72 GPUs. Because each sub-block requires its own MIG, you can create a maximum of 18 compute instances per MIG. A full block consists of 25 MIGs, totaling 450 compute instances.  | A4X Max and A4X | 18  
  
For more information about A4X Max and A4X instances, see [The A4X Max and A4X machine series](https://docs.cloud.google.com/compute/docs/accelerator-optimized-machines#a4x-vms).

#### Maximum topology distance property

When you create and apply a workload policy to a MIG, Compute Engine makes best-effort attempts to create your compute instances close together. If you require maximum compactness in a zone, then we recommend that you specify the maximum topology distance (`maxTopologyDistance`) property. A maximum topology distance value specifies to create A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D instances in the same [_cluster_ , _block_ , or _sub-block_](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology#overview).

**Important:** If you have strict requirements for placing compute instances in your workload, then you might encounter errors due to resource availability. If you do encounter such errors, then use a workload policy with less strict placement requirements.

The following table shows the maximum topology distance values and the machine series that they support:

Maximum topology distance value | Description | Supported machine series | Maximum number of compute instances  
---|---|---|---  
Unspecified (Not recommended) | Compute Engine makes best-effort attempts to place the compute instances as close to each other as possible, but with no maximum distance guarantee among compute instances in a zone. | A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), and H4D | 1,500  
`CLUSTER` | Compute Engine creates compute instances in adjacent blocks within a cluster. | A4 and H4D | 1,500  
`BLOCK` | Compute Engine creates compute instances in the same block. | A4, A3 Ultra, A3 Mega, A3 High (8 GPUs), or H4D | 

  * **For A4 or H4D** : 150
  * **For A3 Ultra, A3 Mega, or A3 High (8 GPUs)** : 256

  
`SUBBLOCK` | Compute Engine creates compute instances in the same sub-block, minimizing network latency as much as possible. | A4, A3 Ultra, and H4D | 22  
  
## Pricing

There are no additional costs associated with creating, deleting, or applying workload policies to a MIG.

## Supported machine series

You can only apply workload policies to MIGs with compute instances that use the following combinations of machine series and provisioning models:

Machine series | Flex-start | Spot | Reservation-bound | Standard  
---|---|---|---|---  
**A4X Max** | No | No | Yes | No  
**A4X** | No | No | Yes | No  
**A4** | Yes | Yes | Yes | No  
**A3 Ultra** | Yes | Yes | Yes | No  
**A3 Mega** | No | Yes | Yes | No  
**A3 High (8 GPUs)** | No | Yes | Yes | No  
**H4D** | Yes | Yes | Yes | No  
**TPU7x** | Yes | Yes | Yes | Yes  
**TPU v6e** | Yes | Yes | Yes | Yes  
**TPU v5p** | Yes | Yes | Yes | Yes  
  
## Limitations

For workload policies in MIGs, the following limitations apply:

  * You can only apply a workload policy to an existing MIG, or change its workload policy, if there are no compute instances in the MIG.

  * You can apply workload policies to regional MIGs only if the MIGs use the following [distribution target shapes](https://docs.cloud.google.com/compute/docs/instance-groups/regional-mig-distribution-shape):

    * **For MIGs with a target size** : `ANY` or `ANY_SINGLE_ZONE`

    * **For MIG resize requests** : `ANY_SINGLE_ZONE`

  * You can't update a workload policy after you create it.

  * You can't configure a second instance template if your MIG uses a workload policy.

  * You can't use workload policies together with placement policies.




## What's next

  * Learn how to [create workload policies for MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/create-workload-policies).

  * Learn how to [view workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/view-workload-policies).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
