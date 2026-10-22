---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses/
title: Plan your IP addresses \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:14:37.522539+00:00
---

# Plan your IP addresses  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Plan your IP addresses Stay organized with collections  Save and categorize content based on your preferences. 

This document shows how to plan your IP addresses for an installation of Google Distributed Cloud.

## Before you begin

Read the [Google Distributed Cloud overview](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview) and the [overview of installation](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/install-overview).

## Example of IP address allocation

This section gives an example of how to allocate static IP addresses in an installation that includes these elements:

  * An admin workstation

  * A high-availability (HA) admin cluster

  * One HA user cluster that has five worker nodes

  * One non-HA user cluster that has four worker nodes




In this example, the user clusters have [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) enabled. With Controlplane V2, the control-plane nodes for a user cluster are in the user cluster itself.

If you don't want to enable Controlplane V2 for your user clusters, see [Plan your IP addresses (kubeception)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/plan-ip-addresses-kubeception). The term _kubeception_ refers to the case where the control plane for a user cluster runs on one or more nodes in the admin cluster. We don't recommend using kubeception. We recommend enabling Controlplane V2.

### Admin cluster nodes

An admin cluster has three nodes, each of which runs control-plane components.

### Load balancing

For this example, assume that the clusters are using the [MetalLB](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb) load balancer. This load balancer runs on the cluster nodes, so no additional VMs are needed for load balancing.

### Subnets

For this example, assume that each cluster is on its own VLAN, and the clusters are in these subnets:

VMs | Subnet | Default gateway  
---|---|---  
Admin workstation and admin cluster | 172.16.20.0/24 | 172.16.20.1  
User cluster 1 | 172.16.21.0/24 | 172.16.21.1  
User cluster 2 | 172.16.22.0/24 | 172.16.22.1  
  
The following diagram illustrates the three VLANs and subnets. Notice that VIPs are not shown associated with any particular node in a cluster. That is because the MetalLB load balancer can choose which node announces the VIP for an individual Service. For example, in user cluster 1, one worker node could announce 172.16.21.31, and a different worker node could announce 172.16.21.32.

[ ![IP addresses for an admin cluster and two user clusters.](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/ip-addresses-production-cpv2-ha.svg)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/ip-addresses-production-cpv2-ha.svg) IP addresses for an admin cluster and two user clusters (Click to enlarge)

### Example IP address: admin workstation

In this example, the admin workstation is in the same subnet as the admin cluster: 172.16.20.0/24. An address near the node addresses would be suitable for the admin workstation. For example, 172.16.20.20.

### Example IP addresses: admin cluster nodes

The admin cluster in this example has three nodes, so you need to set three IP addresses. For example, you could set aside the following IP addresses for nodes in the admin cluster:

Admin cluster | IP addresses  
---|---  
HA admin cluster | 172.16.20.2 - 172.16.20.4  
  
### Example IP addresses: VIP for the admin cluster

You need to set aside a VIP for the Kubernetes API server of the admin cluster. Note that in the cluster configuration file, the field for this VIP is called `controlPlaneVIP`. For example, you could set aside the following VIP for the Kubernetes API server of the admin cluster:

VIP | IP address  
---|---  
VIP for the Kubernetes API server of the admin cluster | 172.16.20.30  
  
Note that for HA admin clusters, the `controlPlaneVIP` needs to be in the same VLAN as the control-plane node IPs specified in [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#network-controlplaneipblock-section).

### Example IP addresses: User cluster 1 nodes

For a user cluster that has eight nodes, you need to set aside nine IP addresses. The extra address is required, because it is needed during cluster upgrade, update, and auto repair. For example, you could set aside the following IP addresses for nodes in user cluster 1:

IP addresses for nodes in the user cluster 1  
---  
172.16.21.2 - 172.16.21.10  
  
### Example IP addresses: VIPs for user cluster 1

The following table gives an example of how you could designate VIPs to be configured on the load balancer for user cluster 1:

VIP | Description | IP address  
---|---|---  
VIP for the Kubernetes API server of user cluster 1 | Configured on the load balancer for user cluster 1 | 172.16.21.30  
Ingress VIP for user cluster 1 | Configured on the load balancer for user cluster 1 | 172.16.21.31  
Service VIPs for user cluster 1 | Ten addresses for Services of type `LoadBalancer`.  
Configured as needed on the load balancer for user cluster 1.  
Notice that this range includes the ingress VIP.  
This is a requirement for the MetalLB load balancer. | 172.16.21.31 - 172.16.21.40  
  
Note that the VIP for the Kubernetes API server is specified in [loadBalancer.vips.controlPlaneVIP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) of the cluster configuration file. When ControlPlane V2 is enabled, the `controlPlaneVIP` needs to be in the same VLAN as the control-plane node IPs specified in [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section).

### Example IP addresses: User cluster 2 nodes

For a user cluster that has five nodes, you need to set aside six IP addresses. The extra address is required, because it is needed during cluster upgrade, update, and auto repair. For example, you could set aside the following IP addresses for nodes in user cluster 2:

IP addresses for nodes in the user cluster 2  
---  
172.16.22.2 - 172.16.22.7  
  
### Example IP addresses: VIPs for user cluster 2

The following table gives an example of how you could designate VIPs to be configured on the load balancer for user cluster 2:

VIP | Description | IP address  
---|---|---  
VIP for the Kubernetes API server for user cluster 2 | Configured on the load balancer for user cluster 2 | 172.16.22.30  
Ingress VIP for user cluster 2 | Configured on the load balancer for user cluster 2 | 172.16.22.31  
Service VIPs for user cluster 2 | Ten addresses for Services of type `LoadBalancer`.  
Configured as needed on the load balancer for user cluster 2.  
Notice that this range includes the ingress VIP.  
This is a requirement for the MetalLB load balancer. | 172.16.22.31 - 172.16.22.40  
  
Note that the VIP for the Kubernetes API server is specified in [loadBalancer.vips.controlPlaneVIP](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#loadbalancer-vips-controlplanevip-field) of the cluster configuration file. When ControlPlane V2 is enabled, the `controlPlaneVIP` needs to be in the same VLAN as the control-plane node IPs specified in [network.controlPlaneIPBlock](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#network-controlplaneipblock-section).

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

[Manage node IP addresses](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manage-node-ip-addresses)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
