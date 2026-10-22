---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/use-cases/
title: NCC use cases \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:45.613100+00:00
---

# NCC use cases  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/use-cases/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  NCC use cases Stay organized with collections  Save and categorize content based on your preferences. 

This document describes common Network Connectivity Center (NCC) use cases to help you choose a topology for connecting Virtual Private Cloud (VPC) networks, on-premises networks, and other cloud provider networks.

## Connect different VPC networks with NCC

When you attach two or more Virtual Private Cloud (VPC) spokes to a hub, NCC provides connectivity through subnet routes among all the VPC networks that are represented by the spokes. Using a hub simplifies the management of large-scale mesh subnet connectivity. See [quotas](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas#general-ncc-limits) for how many VPC networks can be connected to a hub.

The following diagram shows two VPC spokes.

[ ![Connect spokes to a VPC network.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/vpc-spokes-connectivity.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/vpc-spokes-connectivity.svg) Connect spokes to a VPC network (click to enlarge).

## Connect VPC spokes to on-premises networks

VPC spokes can connect to on-premises networks by using hybrid spokes located in other routing VPC networks. Each NCC hub supports multiple VPC spokes and Cloud Interconnect VLAN attachments, HA VPN tunnels, or Router appliance VMs added as hybrid spokes.

## Connect networks using Router appliance VMs

NCC can use Router appliance VMs in the following two IPv4 connectivity scenarios:

  * Connecting a VPC network to an on-premises or other cloud provider network using [dynamic routes](https://docs.cloud.google.com/vpc/docs/routes#dynamic_routes)
  * Connecting two VPC networks to each other using dynamic routes



With this option, Cloud Router manages the BGP sessions for Router appliance VMs.

### Connect an external network to Google Cloud

The following diagram uses a hybrid spoke with a Router appliance VM to connect two VPC networks to an external network. The Cloud Router VM has one network interface (NIC) in each VPC network.

[ ![Connect an external network to Google Cloud.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/site-to-cloud.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/site-to-cloud.svg) Connect an external network to Google Cloud (click to enlarge).

For more information about this use case, see [Site-to-cloud topologies that use a third-party appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/site-to-cloud).

### Manage connectivity between VPC networks

The following diagram uses a hybrid spoke with a Router appliance VM running specialized firewall or packet inspection software to connect two VPC networks.

[ ![Use a third-party firewall.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/network-to-network-high-level.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/network-to-network-high-level.svg) Use a third-party firewall (click to enlarge).

For more information, see [VPC-to-VPC topology that uses a third-party appliance](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/connect-vpc-networks).

## Conduct data transfer over Google's network (site-to-site)

_Data transfer_ provides IPv4 and IPv6 ([Preview](https://cloud.google.com/products#product-launch-stages)) connectivity between external networks using a Google Cloud VPC network and hybrid spokes. You can transfer data between multiple on-premises networks or to other cloud networks.

When you create a hybrid spoke, you can enable the data transfer option for that spoke. When data transfer is enabled for hybrid spokes connected to the same hub, the dynamic routes learned by each Router appliance VM, Cloud VPN tunnel, or Cloud Interconnect VLAN attachment are re-advertised to the other VMs, tunnels, or VLAN attachments associated with any hybrid spoke connected to the same hub. Data transfer requires that all hybrid spokes refer to Router appliance VMs, Cloud VPN tunnels, or Cloud Interconnect VLAN attachments in a single VPC network.

For example, suppose you have data centers in New York, Sydney, and Tokyo. After you use supported resources to connect your VPC network to each of these sites, you can create a spoke to represent each network. After you complete this setup, NCC would provide full mesh connectivity between all three sites.

As shown in the following diagram, you can create spokes that rely on connectivity resources such as Cloud VPN, Cloud Interconnect, and Router appliance.

The diagram doesn't show Cross-Cloud Interconnect, but you can also use Cross-Cloud Interconnect VLAN attachments.

[ ![Data transfer over Google's network.](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/data-transfer-topology.svg)](https://docs.cloud.google.com/static/network-connectivity/docs/network-connectivity-center/images/data-transfer-topology.svg) Data transfer over Google's network (click to enlarge).

For more information about this use case, see [Site-to-site data transfer overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/data-transfer).

**Note:** Data transfer is available only in [supported regions](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/locations).

## Secure remote networks with NCC Gateway spokes

NCC Gateway lets you secure your access to private applications hosted in Google Cloud, on-premises, in other cloud providers, and in public applications hosted on internet and SaaS applications. NCC Gateway lets you create regional deployments for optimal data center proximity and manage cross-region traffic on the Google Cloud private backbone.

For detailed information about NCC Gateway use cases, see the [Use cases](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ncc-gateway-overview#use_cases) section in the NCC Gateway overview.

## What's next

  * To learn how to manage hubs and spokes, see [Work with hubs and spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/working-with-hubs-spokes).
  * To learn how to use Cloud VPN spokes, see [Connect two sites by using Cloud VPN spokes](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/tutorials/connecting-two-offices-with-vpns).
  * To obtain a list of partners whose solutions are integrated with NCC, see [NCC partners](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/partners).
  * To check the maximum number of hubs and spokes per project, see [Quotas and limits](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/quotas).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
