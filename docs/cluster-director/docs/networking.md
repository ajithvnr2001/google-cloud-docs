---
url: https://docs.cloud.google.com/cluster-director/docs/networking/
title: Supported networking services in Cluster Director \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:42:52.694359+00:00
---

# Supported networking services in Cluster Director  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cluster-director/docs/networking/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Cluster Director ](https://docs.cloud.google.com/cluster-director/docs)
  * [ Guides ](https://docs.cloud.google.com/cluster-director/docs/overview)



Send feedback 

#  Supported networking services in Cluster Director Stay organized with collections  Save and categorize content based on your preferences. 

This document provides a conceptual overview of the high-performance network architecture and mandatory Virtual Private Cloud (VPC) network requirements for the clusters that you deploy in Cluster Director. This information helps you understand how Cluster Director minimizes potential downtimes.

For the tightly coupled, distributed workloads that run on Cluster Director clusters, even minor increases in network latency can lead to significant downtimes. The networks services that Cluster Director uses are designed to minimize any potential downtimes.

## Cluster Director network architecture

Cluster Director uses hierarchical, rail-aligned network architecture to provide predictable, high-performance connectivity that minimizes communication overhead. This design helps allow GPUs to spend more time on computation by decreasing the time spent waiting for data.

Cluster Director network architecture is organized as follows to help ensure low-latency communication:

  * **Node** or **host** : a single physical server machine in the data center. Each host has its associated compute resources such as accelerators. The number and configuration of these compute resources depend on the machine family. Compute Engine provisions compute instances on top of a physical host.

  * **Sub-blocks** : a sub-block consists of hosts physically located on a single rack and connected by a top-of-rack (ToR) switch. This setup enables efficient, single-hop communication between any two GPUs in the sub-block.

  * **Blocks** : a block consists of multiple sub-blocks interconnected with a non-blocking fabric, providing high-bandwidth connectivity. Any GPU in a block can be reached in a maximum of two network hops.

  * **Clusters** : clusters are formed by multiple interconnected blocks. Clusters can scale to thousands of GPUs for large-scale training workloads.




## Network traffic separation

To help ensure that different types of traffic don't compete for the same system resources, the network architecture separates high-performance GPU communication from general-purpose host traffic.

  * **GPU-to-GPU communication** : this traffic uses dedicated high-speed network interfaces. For accelerator-optimized machine series, this traffic is handled by NVIDIA NICs using technologies like RDMA over Converged Ethernet (RoCE) for efficient, low-latency data exchange directly between GPUs.

  * **Host and storage data plane** : all other traffic, including access to Google Cloud services like Cloud Storage, host-level management, and storage access, flows through Titanium NICs on a separate network path.




## VPC network and firewall requirements

When you create a cluster, you can either have Cluster Director create a new VPC network for you or use an existing one.

  * **New network** : if you let Cluster Director create a VPC network, then it automatically configures the necessary firewall rules for you.

  * **Existing network** : if you use an existing VPC or Shared VPC network, then you must manually configure your network to meet the mandatory requirements that are described in the following section.




### Mandatory configuration for existing networks

If you use an existing VPC or Shared VPC network for your cluster, then the network must meet all of the following mandatory requirements:

  * **Private Google Access** : the subnetwork must have Private Google Access enabled for the compute nodes to function correctly. For instructions, see [Configure Private Google Access](https://docs.cloud.google.com/vpc/docs/configure-private-google-access).

  * **Firewall rules** : you must manually configure the network's firewall rules to allow two types of traffic:

    * **SSH access from IAP** : this configuration allows users to connect to login nodes by using SSH. Configure a firewall rule to allow ingress traffic on TCP port 22 from the specific IP address range used by Identity-Aware Proxy (IAP).

    * **Internal communication** : this configuration allows nodes within your cluster to communicate with each other. A firewall rule must be in place to permit all ingress traffic (TCP, UDP, and ICMP) from the cluster's own subnetwork IP address range.

For more information, see [Use VPC firewall rules](https://docs.cloud.google.com/firewall/docs/using-firewalls).




### Multi-VPC configuration

Some high-performance machine types, such as A4 and A3 Ultra machine types, must separate traffic across a multi-VPC environment. This separation is due to a specialized hardware design that physically separates high-speed GPU traffic from general-purpose traffic. Cluster Director handles the complexity of managing the default VPC for general traffic and additional VPCs for GPU-to-GPU traffic.

### Protect sensitive data

To enhance the security of your cluster, you can optionally use VPC Service Controls. VPC Service Controls lets you define a service perimeter around the projects where your cluster resources reside. By default, a service perimeter blocks communication across its boundary. This block is useful when, for example, you want to prevent sensitive data from being copied to unauthorized resources that are outside of the perimeter.

For more information, see [Overview of VPC Service Controls](https://docs.cloud.google.com/vpc-service-controls/docs/overview).

## What's next

  * [Supported storage services in Cluster Director](https://docs.cloud.google.com/cluster-director/docs/storage)

  * [Try out Cluster Director](https://docs.cloud.google.com/cluster-director/docs/create/quickstart)




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
