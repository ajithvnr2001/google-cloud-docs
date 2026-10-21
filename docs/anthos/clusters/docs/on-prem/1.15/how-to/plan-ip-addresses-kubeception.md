---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses-kubeception/
title: Plan your IP addresses (kubeception) \u00a0|\u00a0 Google Distributed Cloud Virtual for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T17:11:51.893857+00:00
---

# Plan your IP addresses (kubeception)  |  Google Distributed Cloud Virtual for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/plan-ip-addresses-kubeception/

**Version 1.15**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDCV for VMware 1.15 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview)



Send feedback 

#  Plan your IP addresses (kubeception) Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.15 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/plan-ip-addresses-kubeception)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/plan-ip-addresses-kubeception)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document shows how to plan your IP addresses for an installation of Google Distributed Cloud that includes user clusters that use kubeception.

## What is kubeception?

The term [_kubeception_](https://kubernetes.io/blog/2017/01/how-we-run-kubernetes-in-kubernetes-kubeception/) is used to convey the idea that a Kubernetes cluster is used to create and manage other Kubernetes clusters. In the context of Google Distributed Cloud, kubeception refers to the case where the control plane for a user cluster runs on one or more nodes in an admin cluster.

We don't recommend using kubeception. Instead, we recommend using [Controlplane V2](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/create-user-cluster-controlplane-v2). With Controlplane V2, the control-plane nodes for the user cluster are in the user cluster itself.

## Before you begin

Read the [Google Distributed Cloud overview](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/overview) and the [overview of installation](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/install-overview).

## Example of IP address allocation

This section gives an example of how to allocate static IP addresses in an installation that includes these elements:

  * An admin workstation

  * An admin cluster

  * One high-availability (HA) user cluster that has five worker nodes

  * One non-HA user cluster that has four worker nodes




### Admin cluster nodes

The admin cluster has seven nodes:

  * One node that runs the control plane for the admin cluster
  * Two nodes that run add-ons for the admin cluster
  * Three nodes that run the control plane for the HA user cluster
  * One node that runs the control plane for the non-HA user cluster



### Load balancing

For this example, assume that the clusters are using the [MetalLB](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/bundled-load-balance-metallb) load balancer. This load balancer runs on the cluster nodes, so no additional VMs are needed for load balancing.

### Subnets

For this example, assume that each cluster is on its own VLAN, and the clusters are in these subnets:

VMs | Subnet | Default gateway  
---|---|---  
Admin workstation and admin cluster | 172.16.20.0/24 | 172.16.20.1  
User cluster 1 | 172.16.21.0/24 | 172.16.21.1  
User cluster 2 | 172.16.22.0/24 | 172.16.22.1  
  
The following diagram illustrates the three VLANs and subnets. Notice that VIPs are not shown associated with any particular node in a cluster. That is because the MetalLB load balancer can choose which node announces the VIP for an individual Service. For example, in user cluster 1, one worker node could announce 172.16.21.31, and a different worker node could announce 172.16.21.32.

[ ![IP addresses for an admin cluster and two user clusters.](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/images/ip-addresses-production.svg)](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.15/images/ip-addresses-production.svg) IP addresses for an admin cluster and two user clusters (Click to enlarge)

### Example IP address: admin workstation

In this example, the admin workstation is in the same subnet as the admin cluster: 172.16.20.0/24. An address near the node addresses would be suitable for the admin workstation. For example, 172.16.20.20.

### Example IP addresses: admin cluster nodes

For an admin cluster that has seven nodes, you need to set aside eight IP addresses. The extra address is required, because it is needed during cluster upgrade, update, and auto repair. For example, you could set aside the following IP addresses for nodes in your admin cluster:

IP addresses for nodes in the admin cluster  
---  
172.16.20.2 - 172.16.20.9  
  
### Example IP addresses: VIPs in the admin cluster subnet

The following table gives an example of how you could designate VIPs to be configured on the load balancer for the admin cluster. Notice that the VIPs for the Kubernetes API servers of the user clusters are on the admin cluster subnet. That is because in this example, the Kubernetes API server for a user cluster runs on a node in the admin cluster. Note that in the cluster configuration files, the field where you specify the VIP for a Kubernetes API server is called `controlPlaneVIP`:

VIP | IP address  
---|---  
VIP for the Kubernetes API server of the admin cluster | 172.16.20.30  
Admin cluster add-ons VIP | 172.16.20.31  
VIP for the Kubernetes API server of user cluster 1 | 172.16.20.32  
VIP for the Kubernetes API server of user cluster 2 | 172.16.20.33  
  
### Example IP addresses: User cluster 1 nodes

For a user cluster that has five nodes, you need to set aside six IP addresses. The extra address is required, because it is needed during cluster upgrade, update, and auto repair. For example, you could set aside the following IP addresses for nodes in user cluster 1:

IP addresses for nodes in the user cluster 1  
---  
172.16.21.2 - 172.16.21.7  
  
### Example IP addresses: VIPs in the user cluster 1 subnet

The following table gives an example of how you could designate VIPs to be configured on the load balancer for user cluster 1:

VIP | Description | IP address  
---|---|---  
Ingress VIP for user cluster 1 | Configured on the load balancer for user cluster 1 | 172.16.21.30  
Service VIPs for user cluster 1 | Ten addresses for Services of type `LoadBalancer`.  
Configured as needed on the load balancer for user cluster 1.  
Notice that this range includes the ingress VIP.  
This is a requirement for the MetalLB load balancer. | 172.16.21.30 - 172.16.21.39  
  
### Example IP addresses: User cluster 2 nodes

For a user cluster that has four nodes, you need to set aside five IP addresses. The extra address is required, because it is needed during cluster upgrade, update, and auto repair. For example, you could set aside the following IP addresses for nodes in user cluster 2:

IP addresses for nodes in the user cluster 2  
---  
172.16.22.2 - 172.16.22.6  
  
### Example IP addresses: VIPs in the user cluster 2 subnet

The following table gives an example of how you could designate VIPs to be configured on the load balancer for user cluster 2:

VIP | Description | IP address  
---|---|---  
Ingress VIP for user cluster 2 | Configured on the load balancer for user cluster 2 | 172.16.22.30  
Service VIPs for user cluster 2 | Ten addresses for Services of type `LoadBalancer`.  
Configured as needed on the load balancer for user cluster 2.  
Notice that this range includes the ingress VIP.  
This is a requirement for the MetalLB load balancer. | 172.16.22.30 - 172.16.22.39  
  
### Example IP addresses: Pods and Services

Before you create a cluster, you must specify a [CIDR](https://datatracker.ietf.org/doc/html/rfc1519) range to be used for Pod IP addresses and another CIDR range to be used for the `ClusterIP` addresses of Kubernetes Services.

Decide what CIDR ranges you want to use for Pods and Services. For example:

Purpose| CIDR range  
---|---  
Pods in the admin cluster| 192.168.0.0/16  
Pods in user cluster 1| 192.168.0.0/16  
Pods in user cluster 2| 192.168.0.0/16  
Services in the admin cluster| 10.96.232.0/24  
Services in user cluster 1| 10.96.0.0/20  
Services in user cluster 2| 10.96.128.0/20  
  
The preceding examples illustrate these points:

  * The Pod CIDR range can be the same for multiple clusters.

  * Typically you need more Pods than Services, so for a given cluster, you probably want a Pod CIDR range that is larger than the Service CIDR range. The example Pod range for a user cluster is 192.168.0.0/16, which has 2^(32-16) = 2^16 addresses. But an example Service range for a user cluster is 10.96.0.0/20, which has only 2^(32-20) = 2^12 addresses.




### Avoid overlap

You might want to use non-default CIDR ranges to avoid overlapping with IP addresses that are reachable in your network. The Service and Pod ranges must not overlap with any address outside the cluster that you want to reach from inside the cluster.

For example, suppose your Service range is 10.96.232.0/24, and your Pod range is 192.168.0.0/16 (192.168.0.1 - 192.168.255.254). Any traffic sent from a Pod to an address in either of those ranges will be treated as in-cluster traffic and will not reach any destination outside the cluster.

In particular, the Service and Pod ranges must not overlap with:

  * IP addresses of nodes in any cluster

  * IP addresses used by load balancer machines

  * VIPs used by control-plane nodes and load balancers

  * IP addresses of vCenter servers, DNS servers, and NTP servers




We recommend that your Service and Pod ranges be in the [RFC 1918](https://datatracker.ietf.org/doc/html/rfc1918) private address space.

Here is one reason for the recommendation to use RFC 1918 addresses. Suppose your Pod or Service range contains external IP addresses. Any traffic sent from a Pod to one of those external addresses will be treated as in-cluster traffic and will not reach the external destination.

### DNS server and default gateway

Before you fill in your configuration files, you must know the IP address of a DNS server that can be used by your admin workstation and cluster nodes.

You must also know the IP address of the default gateway for each of your subnets. In the preceding examples, the default gateway for each subnet is the first address in the range. For example, in the subnet for the admin cluster, the default gateway is shown as 172.16.20.1.

## More information

[Manage node IP addresses](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.15/how-to/manage-node-ip-addresses)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
