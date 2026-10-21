---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/site-to-cloud/
title: Site-to-cloud topologies that use a third-party appliance \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:19:05.650736+00:00
---

# Site-to-cloud topologies that use a third-party appliance  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/site-to-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Site-to-cloud topologies that use a third-party appliance Stay organized with collections  Save and categorize content based on your preferences. 

Network Connectivity Center (NCC) lets you use a third-party network virtual appliance to establish connectivity between an external site and your Virtual Private Cloud (VPC) network resources. To establish this type of connectivity, you use the Router appliance feature. Using Router appliance in this way is supported in all Google Cloud regions.

### Router appliance

The Router appliance feature lets you install a network virtual appliance within Google Cloud and use it as the backing resource for a spoke.

To create a router appliance instance, you install a virtual appliance image on a Compute Engine virtual machine (VM) and complete additional setup steps. This setup includes establishing Border Gateway Protocol (BGP) peering between the VM and a Cloud Router. BGP enables the dynamic exchange of routes between the Cloud Router and the Router appliance instance. Route exchange lets you establish connectivity between your VPC network and other networks. We recommend using an image provided by a [supported NCC partner](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners). For more information about Router appliance, see the [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).

NCC lets you use a hub-and-spoke architecture for network connectivity. For information about NCC, see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview). For more information about Router appliance, see the [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).

## Connect a site to a VPC network

In the following topology, a router appliance instance serves as the backing resource for a NCC spoke. The router appliance instance connects with a peer router in an on-premises network. The router appliance instance also peers with a Cloud Router. Routes from the on-premises network are dynamically exchanged with the VPC network.

[ ![Use a Router appliance spoke to connect to a VPC network](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/site-to-cloud-one-network.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/site-to-cloud-one-network.svg) Use a Router appliance spoke to connect a site to a VPC network (click to enlarge)

## Connect a site to two VPC networks

In the following topology, a router appliance instance has interfaces in two VPC networks. Each interface has been used to create a Router appliance spoke. In this case, routes from the on-premises network are propagated to each VPC network. Connectivity between the two VPC networks is determined by the features of the network virtual appliance.

[ ![Creating BGP sessions for router appliances](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/site-to-cloud-sample-topology.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/site-to-cloud-sample-topology.svg) Use Router appliance spokes to connect a site to two VPC networks (click to enlarge)

For a detailed description of this topology and instructions about how to configure it, see [Establish connectivity by using a third-party appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/connect-site-to-cloud).

## Enable cross-region failover for multicloud deployments

The following topology shows automatic failover through router appliances across two regions by using [dynamic routing](https://docs.cloud.google.com/vpc/docs/vpc#routing_for_hybrid_networks). The router instance hosts a router appliance image. The Router appliance mediates connectivity between on-premises and multiple VPC networks for hybrid or multicloud scenarios.

[ ![Cross-region failover site-to-cloud topology](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/cross-region-failover-site-to-cloud-topology.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/cross-region-failover-site-to-cloud-topology.svg) Cross-region failover site-to-cloud topology (click to enlarge)

In this topology, Router appliances are added to two NCC hubs, `hub 1` for route exchange with on-premises, and `hub 2` for route exchange with [VPC spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/vpc-spokes-overview). The numerical values in the diagram depict the following connections:

  1. On-premises data centers are connected to Google Cloud through the external VPC network by using an Cloud Interconnect or Cloud VPN associated with the Cloud Router in the local region. The hybrid connections are added to the NCC hub, `hub 1` as hybrid spokes.
  2. The VMs that host the router appliance instances are added to the NCC hub, `hub 1`, which is configured to use mesh topology using `nic0` as a [Router appliance spoke](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview). The VMs that host the router appliances are created in pairs across multiple regions for high-availability purposes. Each region is added as a single router appliance spoke to the NCC hub.
  3. In each region, the router appliance instance establishes Border Gateway Protocol (BGP) peering with the local `Cloud Router 1` or `Cloud Router 2`. Each Cloud Router receives and advertises route prefixes from the peered appliance. Because the Router appliance has to exchange data with the on-premises connections, site-to-site data transfer field must be enabled for all spokes in NCC `hub 1`. The dynamic routing mode for the external VPC network must be set to global. 
  4. To allow communication with spoke VPC networks, the VMs that host the router appliance instances are connected to NCC `hub 2` through `nic1` as a Router appliance spoke in the center group.
  5. In each region, the router appliance instance establishes BGP peering with the local `Cloud Router 3` or `Cloud Router 4`. Each Cloud Router receives and advertises route prefixes from the peered appliance. To enable cross-region failover for appliances in case of region failures, the dynamic routing mode for the internal VPC network must be set to global.
  6. VPC spokes A, B, and C are all connected to the NCC `hub 2` in star topology through VPC spokes in an edge group to prevent direct communication between VPCs.

For supported locations, see [Locations supported for data transfer](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations). For detailed information about connectivity topologies, see [Preset connectivity topologies](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connectivity-topologies).




## What's next

  * To create hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To view a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To find solutions for Router appliance issues, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting#troubleshooting-ra).
  * To get details about API and `gcloud` commands, see [APIs and reference](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/apis).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
