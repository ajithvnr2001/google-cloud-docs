---
url: https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology/
title: Hub-and-spoke network architecture \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:36:01.168403+00:00
---

# Hub-and-spoke network architecture  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/deploy-hub-spoke-vpc-network-topology/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Hub-and-spoke network architecture Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-04-30 UTC

This document presents three architectural options for setting up a hub-and-spoke network topology in Google Cloud. The first option uses Network Connectivity Center, the second uses VPC Network Peering, and the third uses Cloud VPN.

An enterprise can separate workloads into individual VPC networks for the purposes of billing, environment isolation, and other considerations. However, the enterprise might also need to share specific resources across these networks, such as a shared service or a connection to on-premises. In such cases, it can be useful to place the shared resource in a hub network (referred to as the _routing_ network in the rest of this document) and to attach the other VPC networks as spoke networks (referred to as _workload_ networks in the rest of this document). The following diagram shows a hub-and-spoke network with two workload VPCs, though more workload VPCs can be added.

![Hub-and-spoke network schema.](https://docs.cloud.google.com/static/architecture/images/hub-spoke-departmental-segmentation.svg)

In this example, separate workload VPC networks are used for the workloads of individual business units within a large enterprise. Each workload VPC network is connected to a central routing VPC network that contains shared services and can serve as the sole entry point to the cloud from the enterprise's on-premises network.

## Summary of options

When you choose one of the architectures discussed in this document, consider the relative merits of NCC, VPC Network Peering, and Cloud VPN:

  * NCC provides full bandwidth between workload VPCs and provides transitivity between workload VPCs.
  * VPC Network Peering provides full bandwidth between workload VPCs and the routing VPC. It does not provide transitivity among workload VPCs. VPC Network Peering supports routing to NVAs in other VPCs.
  * Cloud VPN allows transitive routing, but the total bandwidth (ingress plus egress) between networks is limited to the bandwidths of the tunnels. Additional tunnels can be added to increase bandwidth.



## Architecture using NCC

The following diagram shows a hub-and-spoke network that uses [NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

![Hub-and-spoke architecture using NCC.](https://docs.cloud.google.com/static/architecture/images/hub-spoke-architecture-ncc.svg)

NCC has a hub resource that provides control plane management, but it's not a hub network for the data plane.

  * NCC can connect the networks together by using a star (hub-and-spoke) or mesh topology. Using a star topology prevents inter-VPC-spoke (workload VPC) communication while the mesh topology does not.
  * The routing (hub) VPC network has a connection to on-premises using Cloud VPN or Cloud Interconnect connections.
  * Dynamic routes can be propagated across VPC networks.
  * Private Service Connect routes are transitive between workload VPCs.
  * Private services access routes are transitive between workload VPCs through the use of [producer spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-overview) for [many Google-provided services](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/producer-vpc-spokes-supported-services). For services where routes are not transitive, a workaround is to connect the consumer VPC network to the routing VPC network by using Cloud VPN instead of NCC.
  * All of the VMs in the peered networks can communicate at the [full bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth) of the VMs.
  * Each workload VPC and the routing VPC network has a Cloud NAT gateway for outbound communication with the internet.
  * DNS peering and forwarding is set up so that workloads in workload VPCs can be reached from on-premises.



## Architecture using VPC Network Peering

The following diagram shows a hub-and-spoke network that uses [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering). VPC Network Peering enables communication using internal IP addresses between resources in separate VPC networks. Traffic stays on Google's internal network and does not traverse the public internet.

![Hub-and-spoke architecture using VPC Network Peering](https://docs.cloud.google.com/static/architecture/images/hub-spoke-architecture-vpc-peering.svg)

  * Each workload (spoke) VPC network in this architecture has a peering relationship with a central routing (hub) VPC network.
  * The routing VPC network has a connection to on-premises using Cloud VPN or Cloud Interconnect connections.
  * All of the VMs in the peered networks can communicate at the [full bandwidth](https://docs.cloud.google.com/compute/docs/network-bandwidth) of the VMs.
  * VPC Network Peering connections are not transitive. In this architecture, the on-premises and workload VPC networks can exchange traffic with the routing network, but not with each other. To provide shared services, either put them in the routing network or connect them to the routing network by using Cloud VPN.
  * Each workload VPC and the routing VPC network has a Cloud NAT gateway for outbound communication with the internet.
  * DNS peering and forwarding is set up so that workloads in workloads VPCs can be reached from on-premises.



## Architecture using Cloud VPN

The scalability of a hub-and-spoke topology that uses VPC Network Peering is subject to [VPC Network Peering limits](https://docs.cloud.google.com/vpc/docs/quota#vpc-peering). And as noted earlier, VPC Network Peering connections don't allow transitive traffic beyond the two VPC networks that are in a peering relationship. The following diagram shows an alternative hub-and-spoke network architecture that uses [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview) to overcome the limitations of VPC Network Peering.

![Hub-and-spoke architecture using Cloud VPN](https://docs.cloud.google.com/static/architecture/images/hub-spoke-architecture-vpn.svg)

  * IPsec VPN tunnels connect each workload (spoke) VPC network to a routing (hub) VPC network.
  * A DNS private zone in the routing network and a DNS peering zone and private zone exist in each workload network.
  * Connections are transitive. The on-premises and spoke VPC networks can reach each other through the routing network, though this can be restricted.
  * Bandwidth between networks is limited by the total [bandwidths of the tunnels](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#network-bandwidth).
  * Each workload (spoke) VPC and the routing VPC network has a Cloud NAT gateway for outbound communication with the internet.
  * VPC Network Peering does not provide for transitive route announcements.
  * DNS peering and forwarding is set up so that workloads in workload VPCs can be reached from on-premises.



## Design alternatives

Consider the following architectural alternatives for interconnecting resources that are deployed in separate VPC networks in Google Cloud:

**Inter-spoke connectivity using a gateway in the routing VPC network**

To enable inter-spoke communication, you can deploy a network virtual appliance (NVA) or a next-generation firewall (NGFW) on the routing VPC network, to serve as a gateway for spoke-to-spoke traffic.

**Multiple Shared VPC networks**

Create a Shared VPC network for each group of resources that you want to isolate at the network level. For example, to separate the resources used for production and development environments, create a Shared VPC network for production and another Shared VPC network for development. Then, peer the two VPC networks to enable inter-VPC network communication. Resources in individual projects for each application or department can use services from the appropriate Shared VPC network.

For connectivity between the VPC networks and your on-premises network, you can use either separate VPN tunnels for each VPC network, or separate VLAN attachments on the same Dedicated Interconnect connection.

## What's next

  * Deploy a hub-and-spoke network [terraform](https://github.com/GoogleCloudPlatform/cloud-foundation-fabric/tree/master/fast/stages/2-networking).
  * Learn about connecting your hub-and-spoke topology to on-premises and other clouds in the [Cross-Cloud Network design guide](https://docs.cloud.google.com/architecture/ccn-distributed-apps-design).
  * Learn about more design options for [connecting multiple VPC networks](https://docs.cloud.google.com/architecture/best-practices-vpc-design#connecting_multiple_networks).
  * Learn about the [best practices](https://docs.cloud.google.com/architecture/framework) for building a secure and resilient cloud topology that's optimized for cost and performance.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-04-30 UTC."],[],[]] 
