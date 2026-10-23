---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/plan-ip-addresses/
title: Plan your IP addresses \u00a0|\u00a0 Google Distributed Cloud software only for bare metal \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:29.031390+00:00
---

# Plan your IP addresses  |  Google Distributed Cloud software only for bare metal  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/plan-ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Distributed, hybrid, and multicloud ](https://docs.cloud.google.com/docs/dhm-cloud)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud/docs)
  * [ GDC for bare metal ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/concepts/about-bare-metal)



Send feedback 

#  Plan your IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

This document gives an example of how to allocate IP addresses for a high-availability (HA) admin cluster and two HA user clusters.

## Before you begin

To learn about admin clusters, user clusters, and high availability, see [Choosing a deployment model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/installing/install-prep).

## Example of IP address allocation

This section gives an example of how to allocate IP addresses in an installation that includes these elements:

  * IP addresses for cluster nodes

  * IP addresses for Pods

  * Cluster IP addresses for Services

  * Virtual IP addresses (VIPs) for the control planes and [ingress proxies](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/create-service-ingress#ingress_components)

  * VIPs to be used as external IP addresses for Services


**Caution:** The IP addresses in this example are for illustration only. Use addresses that are appropriate for your network.

### Admin cluster nodes

The admin cluster in this example has three nodes. Each node runs control plane components.

### User cluster nodes

In this example, each user cluster has six nodes: three control-plane nodes and three worker nodes.

### Load balancing

For this example, assume that the clusters are using the bundled MetalLB load balancer. The load balancer runs on the cluster nodes, so no additional machines are needed for load balancing.

### Subnets

For this example, assume that each cluster is in its own Layer 2 domain, and the clusters are in these subnets:

Cluster | Subnet | Default gateway  
---|---|---  
Admin cluster | 172.16.20.0/24 | 172.16.20.1  
User cluster 1 | 172.16.21.0/24 | 172.16.21.1  
User cluster 2 | 172.16.22.0/24 | 172.16.22.1  
  
The following diagram illustrates the three subnets. Notice that VIPs are not shown associated with any particular node in a cluster. That is because the MetalLB load balancer can choose which node announces the VIP for an individual Service. For example, in user cluster 1, one node could announce 172.16.21.52, and a different node could announce 172.16.21.53.

[ ![IP addresses for an admin cluster and two user clusters.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/abm-plan-ips.svg)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/bare-metal/docs/images/abm-plan-ips.svg) IP addresses for an admin cluster and two user clusters (Click to enlarge)

### Example IP addresses: admin cluster nodes

You need three IP addresses for your admin cluster nodes, all of which run control-plane components. For example, you could use the following IP addresses for nodes in your admin cluster. The addresses in this example are consecutive, but that is not a requirement:

IP addresses for nodes in the admin cluster  
---  
172.16.20.2 - 172.16.20.4  
  
### Example IP address: Control plane VIP for the admin cluster

You need to set aside a VIP for the Kubernetes API server of the admin cluster. In the cluster configuration file, this is called `controlPlaneVIP`. For example, you could set aside the following IP address to be used as the control plane VIP for the admin cluster:

Control plane VIP for the admin cluster  
---  
172.16.20.50  
  
### Example IP addresses: User cluster 1 nodes

Example: you could use the following IP addresses for three control-plane nodes and three worker nodes in user cluster 1. The addresses in this example are consecutive, but that is not a requirement:

IP addresses for nodes in the user cluster 1  
---  
172.16.21.2 - 172.16.21.7  
  
### Example IP addresses: VIPs for user cluster 1

The following table gives an example of how you could designate VIPs to be configured on the load balancer for user cluster 1. The VIPs in this example are consecutive, but that is not a requirement:

VIP | Description | IP address  
---|---|---  
Control plane VIP for user cluster 1 | Configured on the load balancer for user cluster 1 | 172.16.21.50  
Ingress VIP for user cluster 1 | Configured on the load balancer for user cluster 1 | 172.16.21.51  
Service VIPs for user cluster 1 | Ten addresses for Services of type `LoadBalancer`.  
Configured as needed on the load balancer for user cluster 1.  
Notice that this range includes the ingress VIP.  
This is a requirement for the MetalLB balancer. | 172.16.21.51 - 172.16.21.60  
  
### Example IP addresses: User cluster 2 nodes

Example: you could use the following IP addresses for nodes in user cluster 2. The addresses in this example are consecutive, but that is not a requirement:

IP addresses for nodes in the user cluster 2  
---  
172.16.22.2 - 172.16.22.7  
  
### Example IP addresses: VIPs for user cluster 2

The following table gives an example of how you could designate VIPs to be configured on the load balancer for user cluster 2. The VIPs in this example are consecutive, but that is not a requirement.

VIP | Description | IP address  
---|---|---  
Control plane VIP for user cluster 2 | Configured on the load balancer for user cluster 2 | 172.16.22.50  
Ingress VIP for user cluster 2 | Configured on the load balancer for user cluster 2 | 172.16.22.51  
Service VIPs for user cluster 2 | Ten addresses for Services of type `LoadBalancer`.  
Configured as needed on the load balancer for user cluster 2.  
Notice that this range includes the ingress VIP.  
This is a requirement for the MetalLB load balancer. | 172.16.22.51 - 172.16.22.60  
  
### Example IP addresses: Pods and Services

Before you create a cluster, you must specify a [CIDR](https://datatracker.ietf.org/doc/html/rfc1519) range to be used for Pod IP addresses and another CIDR range to be used for the `ClusterIP` addresses of Kubernetes Services.

Decide what CIDR ranges you want to use for Pods and Services. For example:

Purpose| CIDR range  
---|---  
Pods in the admin cluster| 192.168.0.0/16  
Pods in user cluster 1| 192.168.0.0/16  
Pods in user cluster 2| 192.168.0.0/16  
Services in the admin cluster| 10.96.0.0/20  
Services in user cluster 1| 10.96.0.0/20  
Services in user cluster 2| 10.96.0.0/20  
  
The preceding examples illustrate these points:

  * The Pod CIDR range can be the same for multiple clusters in the default, island mode network model. In a flat-mode network, pods must have unique IP addresses across all the clusters. For more information about the network models affecting pods, see [Flat vs island mode network models](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network).

  * The Service CIDR range can be the same for multiple clusters.

  * Typically you need more Pods than Services, so for a given cluster, you probably want a Pod CIDR range that is larger than the Service CIDR range. The example Pod range for a user cluster is 192.168.0.0/16, which has 2^(32-16) = 2^16 addresses. But an example Service range for a user cluster is 10.96.0.0/20, which has only 2^(32-20) = 2^12 addresses.




### Avoid overlap

Take care that your CIDR ranges do not overlap with IP addresses that are reachable in your network. The Service and Pod ranges must not overlap with any address outside the cluster that you want to reach from inside the cluster.

For example, suppose your Service range is 10.96.0.0/20, and your Pod range is 192.168.0.0/16. Any traffic sent from a Pod to an address in either of those ranges will be treated as in-cluster traffic and will not reach any destination outside the cluster.

In particular, the Service and Pod ranges must not overlap with:

  * IP addresses of nodes in any cluster

  * IP addresses used by load balancer machines

  * VIPs used by control-plane nodes and load balancers

  * IP addresses of DNS servers, and NTP servers




We recommend that your Service and Pod ranges be in the [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) private address space.

Here is one reason for the recommendation to use RFC 1918 addresses. Suppose your Pod or Service range contains external IP addresses. Any traffic sent from a Pod to one of those external addresses will be treated as in-cluster traffic and will not reach the external destination.

## Variations on allocating IP addresses

The example given in this document shows one way of allocating IP addresses for a particular type of installation. However, there are various ways you can install Google Distributed Cloud, and the variation you choose will affect how you plan your IP addresses.

For example, you might decide to use non-HA clusters, or you might decide to have your cluster nodes spread across multiple Layer 2 domains. You might decide to use a flat mode network instead of an island mode network.

For examples of how IP addresses are specified in cluster configuration files for various kinds of installations, see [Cluster configuration samples](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/config-samples)

For more information about how to plan your IP addresses for different types of installations, see the following documents:

  * [Flat vs. island mode network model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/reference/flat-vs-island-network)

In flat mode, Pods have unique addresses across more than one cluster. Adjust Pod CIDR ranges accordingly.

  * [IPv4/IPv6 dual-stack networking](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/dual-stack-networking)

Nodes, Pods, and Services have both IPv4 and IPv6 addresses. The IPv6 network is in flat mode, but the IPv4 network can be in either island mode or flat mode. For flat mode networks, you must arrange for Pod reachability.

  * [Implement flat IPv4 mode network model](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-network)

You must arrange for Pod reachability. Make the Pod range and node range subsets of a larger range.

  * [Implement flat-mode network model with BGP support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/flat-bgp-network)

You need floating IP addresses for the BGP speakers in your cluster, and you must specify the IP addresses of Peer routers.

  * [Configure bundled load balancers with BGP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/lb-bundled-bgp)

You need floating IP addresses for the BGP speakers in your cluster, and you must specify the IP addresses of peer routers.

  * [Configure Network Connectivity Gateway](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/bare-metal/docs/how-to/network-connectivity-gateway)

You must specify peer IP addresses and local tunnel IP addresses.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
