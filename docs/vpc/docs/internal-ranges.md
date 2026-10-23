---
url: https://docs.cloud.google.com/vpc/docs/internal-ranges/
title: Internal ranges overview \u00a0|\u00a0 Virtual Private Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:36:51.571401+00:00
---

# Internal ranges overview  |  Virtual Private Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/internal-ranges/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Internal ranges overview

Internal ranges let you reserve blocks of internal IP addresses and specify how those addresses can be used. You can use internal ranges to help you manage Virtual Private Cloud (VPC) network topology as networks grow more complex with features like [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering), [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc), [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview), and [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

## Specifications

  * An internal range resource represents an internal IPv4 or IPv6 CIDR block that is allocated from within a VPC network.
  * When you reserve an internal range, you configure the following: 
    * If the range can be used by Google Cloud resources in its VPC network or is reserved for external use.
    * How the range can be used if VPC Network Peering is configured.
    * If the range can overlap with subnets or routes in its parent VPC network.
    * If the range's address block or overlap behavior can be modified.
  * By default, you can't reserve an internal range that contains IP addresses that are used by other Google Cloud resources in the range's VPC network.
  * If you enable overlap with subnets, routes, or both, you can create internal ranges with CIDR blocks that overlap with the IP address range of the specified resource types.
  * You can't create Google Cloud resources that use IP addresses from an existing internal range, unless you explicitly associate the resource with the internal range (for subnets) or allow overlapping (for routes).
  * If an internal range is immutable, you can only modify the range's description. If the range is mutable (the default), you can modify the range's CIDR block, overlap behavior, and description. Immutability can't be changed after the range is created.



For example, consider a mutable internal range for `10.0.0.0/24` with no overlap specified.

If you try to create a subnet in the same VPC network that uses the range `10.0.0.0/25`, the subnet creation fails, unless you [associate the subnet with the internal range](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges#create-subnets-with-ranges).

If you try to create a route in the same VPC network that uses the range `10.0.0.0/25`, the route creation fails, unless you update the internal range by [setting the `overlaps` property](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges#update-overlap) to `OVERLAP_ROUTE_RANGE`.

## Peering types

The peering type of an internal range specifies the range's behavior with respect to VPC Network Peering. It determines which VPC networks—the parent, its peers, or both—can use IP addresses from an internal range's CIDR block, as well as how those addresses must be assigned.

The following peering types are possible:

  * `FOR_SELF`: the internal range's CIDR block can only be used in the VPC network where it was created (the parent network). 
    * In the parent VPC network, you assign IP addresses by referencing the internal range resource.
    * Peered VPC networks can't assign IP addresses from the range's CIDR block to resources.
  * `FOR_PEER`: the internal range's CIDR block can only be used in peer networks. 
    * The parent VPC network can't assign IP addresses from the range's CIDR block to resources.
    * In peered VPC networks, you can assign IP addresses from the range's CIDR block without referencing the internal range.
  * `NOT_SHARED`: the internal range's CIDR block can be used by both the parent VPC network and peer networks. 
    * In the parent VPC network, you assign IP addresses by referencing the internal range.
    * In a peered VPC network, you assign IP addresses without referencing the internal range, but the addresses must be used in a way that isn't visible to the parent VPC network. For example, two peered VPC networks can create an internal range that uses the same CIDR block, as long as the peering type is `NOT_SHARED` in both networks.



## Usage types

The usage type of an internal range resource specifies whether the allocated CIDR block can be associated with other Google Cloud resources in its parent VPC network. The usage type for an internal range can be one of the following:

  * `FOR_VPC`: the range can be associated with other Google Cloud resources in its parent VPC network. This is the default setting.

  * `EXTERNAL_TO_VPC`: the range cannot be associated with other Google Cloud resources in its parent VPC network.

  * `FOR_MIGRATION`: the range can be used to migrate a subnet range, including from one peered VPC network to another.




### Migrating IPv4 subnet ranges

To migrate a CIDR range from one subnet to another, you must delete the subnet and then recreate it. Normally, when you delete a subnet, its CIDR range is released and can be used by any other resource. To reserve the CIDR range during a migration—after the original subnet is deleted but before the new subnet is created—you can [reserve an IPv4 internal range that has the `FOR_MIGRATION` usage type](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges#create-migration-range).

An internal range for migration specifies a CIDR range, a source subnet, and a target subnet.

  * The IPv4 CIDR range must match or contain the source subnet range.
  * The source and target subnets can be in the same project or in different projects.
  * The source subnet must be in the same project as the internal range resource.
  * The target subnet doesn't need to exist at the time that you create the internal range.



When you delete the source subnet, the CIDR range can only be assigned to a subnet that matches the target subnet.

After you've migrated the subnet, you can delete the internal range.

Internal ranges with usage type `FOR_MIGRATION` must have the peering type `FOR_SELF`.

## Example use cases

The following table describes use cases for internal ranges with different usage and peering combinations. IPv6 internal ranges have specific usage and peering requirements and don't support all of the use cases listed here.

Purpose | Usage type | Peering type | IP version  
---|---|---|---  
Reserve a range for use only within the range's VPC network. | `FOR_VPC` | `NOT_SHARED` | IPv4  
Reserve a range specifically for peer VPC networks, preventing resources in the local VPC network from using it. In peer networks, you can assign IP addresses from the range's CIDR block without referring to the internal range resource. | `FOR_VPC` | `FOR_PEER` | IPv4  
Reserve a range for use outside the range's VPC network, preventing resources in the range's VPC network from using those IP addresses. For IPv6 ranges, prevent [automatic assignment](https://docs.cloud.google.com/vpc/docs/subnets#ipv6-specifications) of the range's IP addresses to new IPv6-only or dual-stack subnets. | `EXTERNAL_TO_VPC` | `FOR_SELF` | IPv4 or IPv6  
Reserve a range for on-premises use only, preventing resources in the range's VPC network from using those IP addresses. | `EXTERNAL_TO_VPC` | `NOT_SHARED` | IPv4  
Reserve a range temporarily for migrating a subnet from one VPC network to another. | `FOR_MIGRATION` | `FOR_SELF` | IPv4  
  
## IPv4 address allocation strategies

When you reserve an IPv4 internal range, you can either specify a CIDR block or let Google Cloud allocate one automatically. For automatic allocation, you specify a prefix length and optional target CIDR blocks. Google Cloud accounts for existing IP address allocations and allocates the internal range a free CIDR block of the chosen size from within the target or default CIDR blocks.

If you use automatic allocation, you can specify the allocation strategy that Google Cloud uses to select a free block. Allocation strategies are only available for automatically allocated IPv4 internal ranges. The following table describes the allocation strategies that you can choose from:

Strategy | Description | Advantages and disadvantages  
---|---|---  
`RANDOM` |  Randomly allocate a free CIDR block. This is the default strategy.  |  Fastest for concurrently reserving multiple CIDR blocks that have the same prefix length. Can lead to fragmentation in your IP address space.  
`FIRST_AVAILABLE` |  Allocate the free CIDR block that has the numerically lowest starting IP address.  |  Most predictable IP range allocation. Maximizes the remaining contiguous unused IP address space within your target CIDR blocks. Causes contention when concurrently reserving internal ranges, leading to slower allocation times.  
`RANDOM_FIRST_N_AVAILABLE` |  You specify a number, N. Google Cloud finds N free CIDR blocks of the requested prefix length, prioritizing blocks with the lowest starting IP addresses. Allocate a random CIDR block from that set.  |  Best for reducing contention during concurrent allocations while maintaining your contiguous unused IP address space. You can improve performance for concurrent allocations by increasing N. However, this might lead to increased fragmentation of the IP address space.   
`FIRST_SMALLEST_FITTING` |  Find the smallest free CIDR blocks (longest prefix length) that can contain the requested prefix length. From that set, allocate the block that has the lowest starting IP address.  |  Best for minimizing IP address fragmentation. Experiences the most contention for concurrent reservations, leading to slower allocation times.  
  
For example, suppose that you want to reserve a `/24` CIDR block from the target block `10.0.0.0/8`. Within the target block, only the following IP address ranges are available: `10.1.0.0/25`, `10.2.0.0/16`, and `10.3.0.0/23`. The following list describes the blocks that might be selected for each allocation strategy:

  * `RANDOM`: Google Cloud randomly determines any available `/24` block, such as `10.2.179.0/24`.
  * `FIRST_AVAILABLE`: Google Cloud finds the lowest available `/24` block, which is `10.2.0.0/24`.
  * `RANDOM_FIRST_N_AVAILABLE`: Suppose you specify `3` for N. Google Cloud creates a set of the three lowest available `/24` blocks—`10.2.0.0/24`, `10.2.1.0/24`, and `10.2.2.0/24`. From that set, Google Cloud randomly chooses one of the three blocks, such as `10.2.2.0/24`.
  * `FIRST_SMALLEST_FITTING`: Google Cloud finds the smallest available blocks (highest prefix) that can contain the specified prefix of `/24`. The smallest available block is `10.3.0.0/23`. Google Cloud allocates the lowest block from within that range, which is `10.3.0.0/24`.



## Quota

There is a limit to how many internal range resources you can create in a single project. For more information, see the per-project [quotas](https://docs.cloud.google.com/vpc/docs/quota#internal-ranges-quota) in the VPC documentation.

## What's next

  * [Create and use internal ranges](https://docs.cloud.google.com/vpc/docs/create-use-internal-ranges)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
