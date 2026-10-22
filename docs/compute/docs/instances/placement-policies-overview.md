---
url: https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview/
title: Placement policies overview \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:50:14.116979+00:00
---

# Placement policies overview  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/instances/placement-policies-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Placement policies overview Stay organized with collections  Save and categorize content based on your preferences. 

This document explains the behavior, restrictions, and billing of placement policies.

By default, you manage the location of your Compute Engine instances only by specifying their zones. Placement policies let you further specify the relative placement of your compute instances in a zone. Based on the policy that you apply to your compute instances, you can reduce network latency across compute instances (_compact_ policy) or improve resiliency against location-specific disruptions (_spread_ policy).

If you want to reduce network latency among compute instances in a managed instance group (MIG) with A3 High with 8 GPUs (or later generations) or H4D instances, then use instead [workload policies](https://docs.cloud.google.com/compute/docs/instance-groups/about-workload-policies).

To learn about other ways of controlling instance placement, see the documentation for [sole-tenancy](https://docs.cloud.google.com/compute/docs/nodes/sole-tenant-nodes) and [regional MIGs](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs).

## About placement policies

Each compute instance runs on a physical server—a _host_ —that is within a [cluster](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology#overview) that is located in a data center for a zone. When you have multiple compute instances in the same zone, Compute Engine places these compute instances in different hosts by default. This placement minimizes the impact of potential power failures. However, when you apply a placement policy to compute instances in the same zone, you can further control the relative locations of those compute instances in the zone based on the needs of your workload.

You can create the following types of placement policies:

  * **Compact placement policy**. This policy places compute instances close to each other in a zone, which reduces network latency among the compute instances. A compact placement policy is helpful when your compute instances need to communicate often with each other—for example, when running high performance computing (HPC), machine learning (ML), or database server workloads.

To learn more, see About compact placement policies in this document.

  * **Spread placement policy**. This policy places compute instances on separate, distinct hardware, which you can use to increase your workload's reliability. Specifically, spreading compute instances helps to reduce the number of compute instances that are simultaneously impacted by location-specific disruptions, such as hardware errors. Additionally, if you use a spread placement policy to [overprovision capacity in multiple locations](https://docs.cloud.google.com/compute/docs/instance-groups/regional-migs#overprovision), you can help ensure that you still have sufficient capacity even when one location is disrupted. For this reason, spread placement policies can also be helpful for large-scale, distributed, and replicated workloads, such as Hadoop Distributed File System (HDFS), Cassandra, or Kafka.

To learn more, see About spread placement policies in this document.




### About compact placement policies

When you apply a compact placement policy to compute instances, Compute Engine tries to place the compute instances as close to each other as possible. This placement is subject to the machine type and zone availability of the compute instances, and instance compactness is achieved only on a best-effort basis. If your application is latency-sensitive and requires compute instances to be as close together as possible (maximum compactness) in a zone, then specify a _maximum distance value_ ([Preview](https://cloud.google.com/products/#product-launch-stages)). Lower maximum distance values ensure closer instance placement, but can result in fewer available machines for compute instance placement.

The following table outlines the supported machine series, maximum number of compute instances, and [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#settingoptions) for each maximum distance value:

Maximum distance value | Description | Supported machine series | Maximum number of compute instances | Supported host maintenance policy  
---|---|---|---|---  
Unspecified (Not recommended) | Compute Engine makes best-effort attempts to place the compute instances as close to each other as possible, but with no maximum distance between compute instances in the zone. | 

  * **Accelerator-optimized machines** : A4X Max, A4X, A4, G4, A3 Ultra, A3 Mega1, A3 High1, A3 Edge1, A2, and G2
  * **Compute-optimized machines** : H4D, H3, C2D, and C2
  * **General-purpose machines** : C4D, C4, C3D, C3, N2D, and N2
  * **Network-optimized machines** : C4N, M4N
  * **Memory-optimized machines** : M4N, M4, M3, M2, and M1
  * **Storage-optimized machines** : Z4D, Z4M, and Z3-metal

| 1,500 | 

  * **For Z3-metal, Z4D, and Z4M instances with more than 42,000 GiB of Local SSD** : Terminate
  * **For all other supported machine series** : Migrate or Terminate

  
`3` | Compute Engine places your compute instances in adjacent blocks within a cluster for low latency. | 

  * **Accelerator-optimized machines** : A4, G4, A3 Mega1, A3 High1, A3 Edge1, A2, and G2
  * **Compute-optimized machines** : H4D, H3, C2D, and C2
  * **General-purpose machines** : C4D, C4, C3D, and C3
  * **Network-optimized machines** : C4N, M4N
  * **Memory-optimized machines** : M4N, M4
  * **Storage-optimized machines** : Z4D, Z4M, and Z3-metal

| 1,500 | 

  * **For Z3-metal, Z4D, and Z4M instances with more than 42,000 GiB of Local SSD** : Terminate
  * **For all other supported machine series** : Migrate or Terminate

  
`2` | Compute Engine places your compute instances in the same block within a cluster. The compute instances experience lower network latency than compute instances that are placed in the same cluster, but on adjacent blocks. | 

  * **Accelerator-optimized machines** : A4, G4, A3 Ultra, A3 Mega1, A3 High1, A3 Edge1, A2, and G2
  * **Compute-optimized machines** : H4D, H3, C2D, and C2
  * **General-purpose machines** : C4D, C4, C3D, and C3
  * **Network-optimized machines** : C4N
  * **Memory-optimized machines** : M4N, M4
  * **Storage-optimized machines** : Z4D, Z4M, and Z3-metal

| 

  * **For A3 Ultra, A3 Mega, A3 High, and A3 Edge** : 256
  * **For all other supported machine series** : 150

| Terminate  
`1` | Compute Engine places your compute instances in the same sub-block. This placement minimizes network latency as much as possible. | 

  * **Accelerator-optimized machines** : G4, A3 Edge1, A2, and G2
  * **Compute-optimized machines** : H4D, H3, C2D, and C2
  * **General-purpose machines** : C4D, C4, C3D, and C3
  * **Network-optimized machines** : C4N
  * **Memory-optimized machines** : M4N, M4
  * **Storage-optimized machines** : Z4D, Z4M, and Z3-metal

| 

  * **For Z4M** : 16
  * **For all other supported machine series** : 22

| Terminate  
  
1 If you want to apply a compact placement policy to an A3 Mega, A3 High, or A3 Edge instance that was created before October 1, 2025, then contact your [account team](https://cloud.google.com/tam) or the [sales team](https://cloud.google.com/contact). 

After you create a compact placement policy and apply it to compute instances, you can verify the physical location of the compute instances in relation to other compute instances that specify the same compact placement policy. This information helps you minimize network latency by running latency-sensitive jobs on the compute instances that are closest to each other. For more information, see [View the physical location of a Compute Engine instance](https://docs.cloud.google.com/compute/docs/instances/view-instance-topology).

### About spread placement policies

When creating a spread placement policy, you can specify the number of _availability domains_ —up to eight—to spread its compute instances across. Availability domains provide isolated, distinct hardware to minimize the impact of localized disruptions. However, they're still impacted by shared infrastructure failures, such as data center power outages.

To reduce the proportion of your compute instances that are impacted whenever an availability domain is disrupted, spread your compute instances across at least two availability domains—each additional availability domain further reduces the proportion of your compute instances that are impacted. Alternatively, you might spread your compute instances across a small number of availability domains to try to limit network latency between those compute instances or due to zonal restrictions.

**Note:** A machine type and zone might not support all the availability domains specified in a spread placement policy. Attempting to create or migrate an instance to a domain that the chosen machine type and zone don't support causes errors.

When you apply a spread placement policy to an instance, Compute Engine places the instance in a specific availability domain based on one of the following:

  * **Automatic placement**. By default, Compute Engine automatically places the instance in a domain based on the number of compute instances the placement policy is already applied to:

    * **Eight compute instances or less** : If a spread placement policy is already applied to eight compute instances or less, then Compute Engine places your instance in the domain with the fewest compute instances.

    * **More than eight compute instances** : If a spread placement policy is already applied to more than eight compute instances, then Compute Engine places your instance in a random domain.

  * **Specific placement**. When creating an instance, updating the properties of an instance, or creating an instance template, you can optionally specify the availability domain in which to place your compute instances. Distributing compute instances across domains is helpful to increase the resiliency of your workload. Placing compute instances in the same domain might help reduce network latency among those compute instances.




When you apply a spread placement policy to an existing instance, the instance might need to be relocated to a different availability domain. During this process, Compute Engine stops or live migrates the instance based on its [host maintenance policy](https://docs.cloud.google.com/compute/docs/instances/setting-vm-host-options#available_host_maintenance_properties).

## Restrictions

The following sections outline the restrictions for placement policies.

### Restrictions for all placement policies

For all placement policies, the following restrictions apply:

  * Placement policies are [regional resources](https://docs.cloud.google.com/compute/docs/regions-zones/global-regional-zonal-resources#regionalresources), and they only work in the region where they are located. For example, if you create a placement policy in region `us-central1`, then you can only apply it to Compute Engine resources located in `us-central1` or in a zone in `us-central1`.

  * You can only apply one placement policy per Compute Engine resource.

  * You can replace or remove placement policies only from compute instances. Replacing or removing placement policies from other Compute Engine resources isn't supported.

  * You can only delete a placement policy if it's not applied to any Compute Engine resource.

  * You can't apply placement policies to sole-tenant instances.




### Restrictions for compact placement policies

In addition to the restrictions for all placement policies, compact placement policies have the following restrictions:

  * If a compact placement policy specifies a maximum distance value, then this value affects the maximum number of compute instances that you can apply the placement policy to, as well as the machine series and host maintenance policy that the compute instances can use.

  * If you want to apply a compact placement policy to on-demand reservations when you create it, then the following restrictions apply:

    * You can only apply compact placement policies to on-demand, single-project, standalone reservations. Shared reservations and reservations attached to commitments aren't supported.

    * You can't apply compact placement policies that specify a maximum distance value of `1`.

    * You can only apply a compact placement policy to one reservation at a time.

  * You can't apply compact placement policies to Flex-start VMs in a MIG.




### Restrictions for spread placement policies

In addition to the restrictions for all placement policies, spread placement policies have the following restrictions:

  * You can apply a spread placement policy to 256 compute instances maximum.

  * You can't apply spread placement policies to reservations.

  * You can't apply spread placement policies to Flex-start VMs.




## Billing

There are no additional costs associated with creating, deleting, or applying placement policies to a compute instance.

## What's next

  * Learn how to create and apply placement policies to compute instances:

    * [Create and apply spread placement policies to instances](https://docs.cloud.google.com/compute/docs/instances/use-spread-placement-policies)

    * [Reduce latency by using compact placement policies](https://docs.cloud.google.com/compute/docs/instances/use-compact-placement-policies)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
