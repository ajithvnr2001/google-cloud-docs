---
url: https://docs.cloud.google.com/vpc/docs/overview/
title: Virtual Private Cloud (VPC) overview \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:15:59.848779+00:00
---

# Virtual Private Cloud (VPC) overview  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Virtual Private Cloud (VPC) overview

Virtual Private Cloud (VPC) provides networking functionality to [Compute Engine virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances), [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs), and [serverless workloads](https://docs.cloud.google.com/serverless#section-3).

VPC provides networking for your cloud-based resources and services that is global, scalable, and flexible.

This page provides a high-level overview of VPC concepts and features.

## VPC networks

You can think of a VPC network the same way you'd think of a physical network, except that it is virtualized within Google Cloud. A VPC network is a global resource that consists of a list of regional virtual subnetworks (subnets) in data centers, all connected by a global wide area network. VPC networks are logically isolated from each other in Google Cloud.

[ ![VPC network example.](https://docs.cloud.google.com/static/vpc/images/vpc-overview-example.svg)](https://docs.cloud.google.com/static/vpc/images/vpc-overview-example.svg) VPC network example (click to enlarge).

A VPC network does the following:

  * Provides connectivity for your [Compute Engine virtual machine (VM) instances](https://docs.cloud.google.com/compute/docs/instances), including [Google Kubernetes Engine (GKE) clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture), [serverless workloads](https://docs.cloud.google.com/serverless#section-3), and other Google Cloud products built on Compute Engine VMs.
  * Offers built-in internal passthrough Network Load Balancers and proxy systems for internal Application Load Balancers.
  * Connects to on-premises networks by using Cloud VPN tunnels and VLAN attachments for Cloud Interconnect.
  * Distributes traffic from Google Cloud external load balancers to backends.



For more information, see [VPC networks](https://docs.cloud.google.com/vpc/docs/vpc).

### Firewall rules

Each VPC network implements a distributed virtual firewall that you can configure. Firewall rules let you control which packets are allowed to travel to which destinations. Every VPC network has two [implied firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#default_firewall_rules) that block all incoming connections and allow all outgoing connections.

The `default` network has [additional firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls#more_rules_default_vpc), including the `default-allow-internal` rule, which permit communication among instances in the network. 

For more information, see [VPC firewall rules](https://docs.cloud.google.com/vpc/docs/firewalls).

### Routes

Routes tell VM instances and the VPC network how to send traffic from an instance to a destination, either inside the network or outside of Google Cloud. Each VPC network comes with some [system-generated routes](https://docs.cloud.google.com/vpc/docs/vpc#system-generated-routes) to route traffic among its subnets and send traffic from [eligible instances](https://docs.cloud.google.com/vpc/docs/vpc#internet_access_reqs) to the internet.

You can create custom static routes to direct some packets to specific destinations.

For more information, see [Routes](https://docs.cloud.google.com/vpc/docs/routes).

### Forwarding rules

While routes govern traffic leaving an instance, forwarding rules direct traffic _to_ a Google Cloud resource in a VPC network based on IP address, protocol, and port.

Some forwarding rules direct traffic from outside of Google Cloud to a destination in the network; others direct traffic from inside the network. Destinations for forwarding rules are [target instances](https://docs.cloud.google.com/load-balancing/docs/protocol-forwarding), [load balancer targets (backend services, target proxies, and target pools)](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts), and [Classic VPN gateways](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies).

For more information, see [Forwarding rules overview](https://docs.cloud.google.com/load-balancing/docs/forwarding-rule-concepts).

## Interfaces and IP addresses

VPC networks provide the following configurations for IP addresses and VM network interfaces.

### IP addresses

Google Cloud resources, such as Compute Engine VM instances, forwarding rules, and GKE containers, rely on IP addresses to communicate.

For more information, see [IP addresses](https://docs.cloud.google.com/vpc/docs/ip-addresses).

### Alias IP ranges

If you have multiple services running on a single VM instance, you can give each service a different internal IP address by using alias IP ranges. The VPC network forwards packets that are destined to a particular service to the corresponding VM.

For more information, see [Alias IP ranges](https://docs.cloud.google.com/vpc/docs/alias-ip).

### Multiple network interfaces

You can add multiple network interfaces to a VM instance. Multiple network interfaces enable use cases such as using a network appliance VM to act as a gateway for securing traffic among different VPC networks or to and from the internet.

For more information, see [Multiple network interfaces](https://docs.cloud.google.com/vpc/docs/multiple-interfaces-concepts).

## VPC sharing and peering

Google Cloud provides the following configurations for sharing VPC networks across projects and connecting VPC networks to each other.

### Network Connectivity Center

You can use Network Connectivity Center (NCC) to connect VPC networks by using a hub and spoke connectivity model. VPC spokes let you connect two or more VPC networks to an NCC hub so that the networks exchange [subnet routes](https://docs.cloud.google.com/vpc/docs/routes#subnet-routes). You can connect and manage hundreds of VPC spokes from a single hub.

For more information, see [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).

### VPC Network Peering

VPC Network Peering lets you build [software as a service (SaaS)](https://wikipedia.org/wiki/Software_as_a_service) ecosystems in Google Cloud, making services available privately across different VPC networks, whether the networks are in the same project, different projects, or projects in different organizations.

With VPC Network Peering, all communication happens by using internal IP addresses. Subject to firewall rules, VM instances in each peered network can communicate with one another without using external IP addresses.

Peered networks automatically exchange subnet routes for private IP address ranges. VPC Network Peering lets you configure whether the following types of routes are exchanged:

  * Subnet routes for privately re-used public IP ranges
  * Custom static and dynamic routes



Network administration for each peered network is unchanged: IAM policies are never exchanged by VPC Network Peering. For example, Network and Security Admins for one VPC network don't automatically get those roles for the peered network.

For more information, see [VPC Network Peering](https://docs.cloud.google.com/vpc/docs/vpc-peering).

### Shared VPC

You can share a VPC network from one project (called a host project) to other projects in your Google Cloud organization. You can grant access to entire Shared VPC networks or select subnets therein by using [specific IAM permissions](https://docs.cloud.google.com/vpc/docs/shared-vpc#iam_in_shared_vpc). This lets you provide centralized control over a common network while maintaining organizational flexibility. Shared VPC is especially useful in large organizations.

For more information, see [Shared VPC](https://docs.cloud.google.com/vpc/docs/shared-vpc).

## Hybrid cloud

Google Cloud provides the following configurations that let you connect your VPC networks to on-premises networks and networks from other cloud providers.

### Cloud VPN

Cloud VPN lets you connect your VPC network to your physical, on-premises network or another cloud provider by using a secure [virtual private network](https://wikipedia.org/wiki/Virtual_private_network).

For more information, see [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn).

### Cloud Interconnect

Cloud Interconnect lets you connect your VPC network to your on-premises network by using a high speed physical connection.

For more information, see [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect).

### Hybrid Subnets

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Hybrid Subnets helps you migrate workloads to Google Cloud without needing to change any IP addresses. A hybrid subnet is a single logical subnet that combines a segment of an on-premises network with a subnet in a VPC network.

For more information, see [Hybrid Subnets](https://docs.cloud.google.com/vpc/docs/hybrid-subnets).

## Cloud Load Balancing

Google Cloud offers several load balancing configurations to distribute traffic and workloads across many backend types.

For more information, see [Cloud Load Balancing overview](https://docs.cloud.google.com/load-balancing/docs/load-balancing-overview).

## Private access to services

You can use [Private Service Connect](https://docs.cloud.google.com/vpc/docs/private-service-connect) and [Private Google Access](https://docs.cloud.google.com/vpc/docs/private-google-access), and [private services access](https://docs.cloud.google.com/vpc/docs/private-services-access) to let VMs that don't have an external IP address communicate with supported services. 

For more information, see [Private access options for services](https://docs.cloud.google.com/vpc/docs/private-access-options). 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
