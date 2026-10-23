---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods/
title: About multi-network support for Pods \u00a0|\u00a0 GKE networking \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:51.750659+00:00
---

# About multi-network support for Pods  |  GKE networking  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-multinetwork-support-for-pods/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ GKE networking ](https://docs.cloud.google.com/kubernetes-engine/networking/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/explore-gke-networking-docs-use-cases)



Send feedback 

#  About multi-network support for Pods Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document describes multi-network support for Pods, including use cases, relevant concepts, terminology, and benefits.

## Overview

Google Cloud supports multiple network interfaces at the virtual machine (VM) instance level. You can connect a VM to up to eight networks with multiple network interfaces including the default network plus seven additional networks.

Google Kubernetes Engine (GKE) networking extends multi-network capabilities to Pods that run on the nodes. With multi-network support for Pods, you can enable multiple interfaces on nodes and Pods in a GKE cluster. Multi-network support for Pods removes the single interface limitation for node pools, which limited the nodes to a single VPC for networking.

To use multi-network support for your Pods and nodes, see [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods).

## Terminology and concepts

This page uses the following concepts:

**Primary VPC** : the primary [VPC](https://docs.cloud.google.com/vpc/docs/overview) is a pre-configured VPC that comes with a set of default settings and resources. The GKE cluster is created in this VPC. If you have deleted the pre-configured VPC, you must specify an existing VPC when creating a GKE cluster.

**Subnet** : in Google Cloud, a [subnet](https://docs.cloud.google.com/vpc/docs/subnets) is the way to create Classless Inter-Domain Routing (CIDR) with netmasks in a VPC. A subnet has a single primary IP address range which is assigned to the nodes and can have multiple secondary ranges that can belong to Pods and Services.

**Node-network** : the node-network refers to a dedicated combination of a VPC and subnet pair. Within this node-network, the nodes belonging to the node pool are allocated IP addresses from the primary IP address range.

**Secondary range** : a Google Cloud secondary range is a CIDR and netmask belonging to a subnet. GKE uses this as a Layer 3 Pod-network. A Pod can connect to multiple Pod-networks.

**Pod-network** : a Network object that serves as a connection point for Pods. The connection can either be of type `Layer 3` or of type `Device`. You can configure `Device` type Networks in `netdevice` or Data Plane Development Kit (DPDK) mode.

`Layer 3` networks correspond to a secondary range on a subnet. `Device` network correspond to a subnet on a VPC. The data model for the Pod-network in GKE multi-network is as follows:

  * For `Layer 3` Network: **VPC - > Subnet Name -> Secondary Range Name**

  * For `Device` Network: **VPC - > Subnet Name**




**Default Pod-network** : Google Cloud creates a default Pod-network during cluster creation. The default Pod-network uses the primary VPC as the node-network. The default Pod-network is available on all cluster nodes and Pods, by default.

**Pods with multiple interfaces** : multiple interfaces on the Pods cannot connect to the same Pod network.

The following diagram shows a typical GKE cluster architecture with `Layer 3` Networks:

![GKE cluster architecture with Layer 3 Networks](https://docs.cloud.google.com/static/kubernetes-engine/images/multi-network-cluster.png)

For `Device` typed Networks, which can be configured in `netdevice` or `DPDK` mode, the VM vNIC is managed as a resource and passed to the Pod. The Pod-network maps directly to Node-network in this case. Secondary ranges are not required for `Device` typed Networks.

![Pod and node networks](https://docs.cloud.google.com/static/kubernetes-engine/images/pod-node-networks.png)

## Use cases

Multi-network support for Pods address the following use cases:

  * **Deploy Containerized Network Functions:** if you run the Network Functions in Containers, which have separate data and management planes. Multi-network for Pods isolates networks for different user planes, high performance or low latency from specific interfaces, or network level multi-tenancy. This is needed for compliance, QoS, and security.
  * **Connect VPC within the same organization and project:** you want to create GKE clusters in a VPC and need to connect to services in another VPC. You can use the multi-NIC nodes option for direct connectivity. This might be due to a hub-and-spoke model, in which a centralized service (logging, authentication) operates within a Hub VPC, and the spokes require private connectivity to access it. You can use the multi-network support for Pods to connect the Pods running in the GKE cluster to the hub VPC directly.
  * **Run DPDK applications with VFIO:** you want to run DPDK applications that require access to NIC on the node through the VFIO driver. You can achieve the optimal packet rate by bypassing the kernel, Kubernetes and GKE Dataplane V2 completely.
  * **Enable direct access to vNIC bypassing Kubernetes and GKE Dataplane V2:** you run the Network Functions in Containers that requires direct access to the Network Interface Card (NIC) on the node. For example, High-Performance Computing (HPC) applications that want to bypass Kubernetes and GKE Dataplane V2 to achieve lowest latency. Some applications also want access to PCIe topology information of the NIC to collocate with other devices like GPU.
  * **Expose workloads on secondary networks using load balancers** : you can use external and internal passthrough Network Load Balancers to expose workloads (such as Containerized Network Functions) directly on secondary VPCs. This lets you provide access to your applications on specific network interfaces without using the cluster's default network.



## Benefits

Multi-network support for Pods provide the following benefits:

  * **Traffic isolation** : multi-network support for Pods lets you isolate traffic in a GKE cluster. You can create Pods with multiple network interfaces, to separate traffic based on capability, such as management and dataplane, within Pods running specific Containerized Network Functions (CNFs).
  * **Dual homing** : dual homing lets a Pod to have multiple interfaces and route traffic to different VPCs, allowing the Pod to establish connections with both a primary and secondary VPC. If one VPC experiences issues, the application can fall back to the secondary VPC.
  * **Network segmentation** : Pods can connect to internal or external networks based on workload needs. Depending on the specific requirements of your workloads, you can choose which Pods or groups of Pods connect to each network. For example, you can use an internal network for east-west communication and an external network for internet access. This lets you tailor the network connectivity of your workloads based on their specific needs.
  * **Optimal performance with DPDK** : multi-network support for Pods in GKE lets DPDK applications to run in GKE Pods, which provides optimal packet processing performance.
  * **Host NIC directly available in Pod** : The `netdevice` mode NIC support with multi-network passes VM NIC directly to Pod, bypassing Kubernetes and GKE Dataplane V2. This can achieve the lowest latency for collaboration between devices.
  * **Performance** : to improve your applications' performance, you can connect the applications to the network that is best suited for the applications' needs.
  * **Multi-network load balancing** : multi-network support for Pods lets you provision Google Cloud external and internal passthrough Network Load Balancers for services on secondary networks. This lets you expose your applications to clients on specific VPCs while maintaining strict network isolation between your workloads.



## What's next

  * [Set up multi-network support for Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/setup-multinetwork-support-for-pods)
  * [Read the GKE network overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/network-overview)
  * [Deploy multi-network LoadBalancer services](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/deploy-multinetwork-loadbalancer-services)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
