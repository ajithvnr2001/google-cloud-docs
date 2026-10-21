---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview/
title: VPC spokes overview \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:02:14.224455+00:00
---

# VPC spokes overview  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  VPC spokes overview Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of Virtual Private Cloud (VPC) spokes support in Network Connectivity Center (NCC). 

## VPC spokes

Network Connectivity Center provides inter-VPC network connectivity at scale with the support for VPC spokes. VPC spokes reduce the operational complexity of managing the individual pair-wise VPC Network Peering connections through the use of VPC spokes and a centralized connectivity management model. VPC spokes can export and import all subnet routes from other spoke VPCs on a Network Connectivity Center hub. This ensures full connectivity between all workloads that reside in all these VPC networks. Inter-VPC network traffic stays within the Google Cloud network and does not travel through the internet, which helps to ensure privacy and security.

VPC spokes can be in the same project and organization or in a different project and organization from the NCC hub. A VPC spoke can be connected to one hub at a time.

For information about how to create a VPC spoke, see [Create a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke).

### Considerations for dynamic route exchange with VPC spokes

  * **Routing VPC networks that are also VPC spokes** : NCC supports two or more [routing VPC networks](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/dynamic-route-exchange-with-vpc-spokes#routing-vpc) on the same hub only if all of the routing VPC networks aren't also VPC spokes. If an NCC hub has a single routing VPC network, that routing VPC network can optionally also be a VPC spoke:

    * If you need to make [propagated Private Service Connect connections](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) available to on-premises networks through the hub's hybrid spokes, the hub's single routing VPC network must also be connected as a VPC spoke.

    * If you don't need to make propagated Private Service Connect connections available to on-premises networks through the hub's hybrid spokes, we recommend not configuring a routing VPC network as a VPC spoke so that the hub can support two or more routing VPC networks.




### Comparison to VPC Network Peering

VPC spokes support medium to large enterprise requirements by:

  * Allowing you to control which IPv4 and IPv6 subnet routes are exported to the hub
  * Importing IPv4 and IPv6 subnet routes from the hub
  * Importing IPv4 and IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages)) dynamic routes that hybrid spokes have exported to the hub
  * Allowing you to [configure static routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/configure-static-routes) with next hop internal passthrough Network Load Balancers in other VPC spokes



The following rules apply to a VPC spoke network that's connected to another VPC network using VPC Network Peering except for [producer VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview) :

  * The other VPC network can't be connected to the NCC hub as a VPC spoke.
  * The VPC spoke network cannot export the [peering subnet routes](https://docs.cloud.google.com/vpc/docs/routes#types-of-subnet-routes), that it imported from the other network, to the hub.

Feature | VPC Network Peering | VPC spokes  
---|---|---  
Number of VPC networks |  [Peerings per VPC network](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/peerings_per_vpc_network) quota  |  [Active VPC spokes per hub](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/active_vpc_spokes_per_hub) quota   
Number of subnet ranges (subnet routes) |  [Subnet ranges per peering group](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/subnet_ranges_per_peering_group) quota  |  Subnet [routes per route table](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/routes_per_route_table) quota   
Number of dynamic routes |  [Dynamic routes per region per peering group](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/dynamic_routes_per_region_per_peering_group) quota  |  [ Unique dynamic route prefixes per hub route table per region](https://console.cloud.google.com/iam-admin/quotas?service=networkconnectivity.googleapis.com&metric=networkconnectivity.googleapis.com/dynamic_route_prefixes_per_hub_route_table_per_region) quota   
Number of static routes |  [Static routes per peering group](https://console.cloud.google.com/iam-admin/quotas?service=compute.googleapis.com&metric=compute.googleapis.com/static_routes_per_peering_group) quota  |  Static route exchange isn't supported, but you can [Configure static routes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/configure-static-routes) with next hop internal passthrough Network Load Balancers in a different VPC spoke.   
Export filters |  Specific filters aren't supported; see [Route exchange options](https://docs.cloud.google.com/vpc/docs/vpc-peering#route-exchange-options) in the VPC Network Peering documentation.  |  Supports both include export ranges and exclude export ranges. For more information, see [Export filters](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filters) and [ Export filter rules for VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview#export-filter-rules-vpc-spokes).   
Inter-VPC NAT |  |   
[Private Service Connect endpoint propagation](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/psc-propagated-connection-overview) |  |   
[Producer VPC spoke connectivity in other VPC networks](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview) |  |   
IP addressing |  Internal IPv4 addresses, including private IPv4 addresses and privately used public IPv4 addresses. See [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). Internal and external IPv6 addresses. |  Internal IPv4 addresses, including private IPv4 addresses and privately used public IPv4 addresses. See [Valid IPv4 ranges](https://docs.cloud.google.com/vpc/docs/subnets#valid-ranges). Internal and external IPv6 addresses.  
IP address families |  Supported configurations: 

  * Exchange only IPv4 subnet ranges
  * Exchange both IPv4 and IPv6 subnet ranges

|  Supported configurations: 

  * Exchange only IPv4 subnet ranges
  * Exchange both IPv4 and IPv6 subnet ranges
  * Exchange only IPv6 subnet ranges

  
Performance and throughput (when compared to other VPC connectivity mechanisms) |  Lowest latency, highest throughput (VM-VM equivalent).  |  Lowest latency, highest throughput (VM-VM equivalent).   
  
## VPC spokes in different projects

VPC spokes can be in either the NCC hub project or a different project. When a VPC spoke and an NCC hub are in different projects, the projects can be in either the same organization or different organizations.

  * A hub administrator creates and manages the NCC hub and accepts VPC spoke proposals. 
  * A spoke administrator creates a proposal for a VPC network in a to join the hub as a VPC spoke.



For more information about hub administrators and spoke administrators, see:

  * [Hub administration overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-hub-admin)
  * [Spoke administration overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spoke-admin)



When a spoke administrator [creates a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes#create-vpc-spoke) in the same project as the hub, NCC adds the VPC spoke immediately.

When a spoke administrator creates a VPC spoke in a project different from the NCC hub project, NCC creates a _spoke proposal_ which a hub administrator must approve before the VPC spoke becomes active. For more information, see:

  * [Propose a VPC spoke in a different project](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-propose-a-spoke)
  * [Check the status of a VPC spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-check-spoke-status)
  * [Review proposed VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-review-proposed-spokes)



### Spoke interaction with VPC Service Controls

NCC supports [VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview) for cross project and organization spokes. For a spoke in a different project from the hub, when a new VPC Service Controls perimeter is added, you can't add new spokes that violate the perimeter. However, existing spokes that you added before adding the VPC Service Controls perimeter continue to function.

## VPC connectivity with export filters

NCC lets you limit how other spokes can connect to a VPC spoke by using spoke filters. For detailed information about spoke filters, see [Spoke filters overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/spoke-filters-overview). VPC spokes only support export filters.

## Preset topologies

NCC lets you specify the connectivity configuration across all VPC spokes. You can choose one of the following two preset topologies:

  * [Mesh topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#mesh-topology)
  * [Star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#star-topology)



For detailed information about connectivity topologies, see [Preset connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).

For detailed information about how to configure the mesh or star topology for your VPC spokes, see [Configure a hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/vpc-configure-hub).

## Limitations

This section describes the limitations of VPC spokes in general and when they are attached to a hub in a different project. These limitations also apply to producer VPC spokes. 

### Limitations of VPC spokes

  * You can't use VPC Network Peering between two VPC spokes that are also connected using an NCC hub. However, consider the following: 
    * A _producer VPC spoke_ requires a peering connection to a VPC spoke on the same hub. Connectivity through NCC isn't established between the producer VPC spoke and its peered VPC spoke. 
    * You can have a NCC-connected VPC spoke that is peered through [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering) with a separate VPC that isn't a part of NCC.
    * You can use VPC Network Peering between two VPC spokes in the edge spoke group of a hub configured to use the [star topology](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies#star-topology). This is because NCC doesn't connect spokes in the edge group to each other.
  * Static routes exchange across VPC spokes isn't supported.
  * IPv6-based internal passthrough Network Load Balancers aren't reachable among VPC spokes.
  * Auto mode VPC networks aren't supported as VPC spokes. You can switch from auto mode to a custom VPC network that lets you manually define subnet prefixes for each region in your VPC network. After the network is updated, you can't undo this action.



### Cool-down period after deleting a VPC spoke

For a new spoke for the same VPC network attached to a different hub, you must wait for the cool-down period of at least 10 minutes. If the adequate cool-down period isn't allowed, the new configuration might not take effect. This cool-down period isn't needed if the VPC network is added as a spoke to the same hub.

## Quotas and limits

When using dynamic route exchange, carefully monitor your usage of the [number of dynamic routes per hub](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-quotas). This quota counts usage by destination (prefix) _only_ , without regard to the priority or next hop of a dynamic route. When the usage of this quota exceeds its limit, NCC drops routes by destination. If a destination is dropped, then _all_ dynamic routes with that destination—regardless of priority or next hop—are no longer sent to the hub.

For detailed quota information, see [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas).

## Billing

The following sections outline details of billing for spoke hours and outbound traffic.

### Spoke hours

Spoke hours are charged to the project where the spoke resource lives and follows the standard spoke hours pricing. Spoke hours are only charged when the spoke is in the `ACTIVE` state.

### Outbound traffic

Outbound traffic is charged to the project of the spoke resource from which traffic originates. Pricing is the same regardless of whether traffic crosses project boundaries.

## Service level agreement

For information about the NCC service level agreement, see [Network Connectivity Center Service Level Agreement (SLA)](https://cloud.google.com/ncc/sla). 

## Pricing

For information about pricing, see [NCC pricing](https://cloud.google.com/network-connectivity/pricing#ncc-pricing).

## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for common issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
