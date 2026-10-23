---
url: https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud/
title: About VMware Engine private clouds \u00a0|\u00a0 Google Cloud VMware Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:35:24.957753+00:00
---

# About VMware Engine private clouds  |  Google Cloud VMware Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vmware-engine/docs/concepts-private-cloud/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ VMware Engine ](https://docs.cloud.google.com/vmware-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/vmware-engine/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# About VMware Engine private clouds

A Google Cloud VMware Engine private cloud is an isolated VMware stack that consists of the following VMware components:

  * ESXi hosts
  * vCenter Server
  * vSAN
  * NSX
  * HCX



Private clouds help you address a variety of common needs for network infrastructure:

  * **Growth.** Add nodes with no new hardware investment when you reach a hardware refresh point for your existing infrastructure.
  * **Fast expansion.** Create additional capacity immediately when temporary or unplanned capacity needs arise.
  * **Increased protection.** Get automatic redundancy and availability protection when using a private cloud of three or more nodes.
  * **Long-term infrastructure needs.** Retire data centers and migrate to a cloud-based solution while remaining compatible with your enterprise operations. This is especially useful if your data centers are at capacity or you want to restructure to lower costs.



## VMware Engine nodes

VMware Engine provides dedicated isolated bare metal hardware nodes to create VMware Engine private clouds. The nodes provide the compute, memory, and storage required to run VMware ESXi, and are the basic unit of consumption of VMware Engine. Using these nodes, you can create a vSphere cluster and run VMware VMs on the clusters.

## Node types

The following table lists key node types that are available when creating a VMware Engine private cloud. For all available node types and regions, see [VMware Engine nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts-node-types).

Node type | vCPUs/Node | Memory/Node (GiB) | Storage/Node (TB)*  
---|---|---|---  
ve1-standard-72 | 72 | 768 | 19.2  
ve1-standard-so |  \-  |  \-  | 19.2  
ve2-standard-128† | 128 | 2048 | 25.5  
  
* Raw storage, excluding cache, in terabytes.  
† Available in select regions.

## Private cloud environment

You manage your private clouds through the Google Cloud console. Each private cloud has its own vCenter Server in its own management domain, and all nodes in a given private cloud reside in the same region.

The VMware stack runs on dedicated, isolated bare metal hardware nodes in Google Cloud locations. You use the stack through built-in VMware tools, including vCenter Server and NSX Manager.

Private clouds are also designed to eliminate single points of failure:

  * Clusters of ESXi hosts are configured with vSphere High Availability (HA) and sized to have at least one spare node for resilience. vSphere HA protects against node and network failures.
  * vSAN provides redundant primary storage. vSAN requires at least three nodes in a private cloud to provide protection against a single failure. You can configure vSAN to provide higher resilience for larger clusters.



You can connect the private cloud to your on-premises environment using the following connections:

  * [Cloud VPN](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [Cloud Interconnect](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [Point-to-site VPN](https://docs.cloud.google.com/vmware-engine/docs/networking/howto-vpn-connect)



### Single-node private clouds

For pilot testing and proofs of concept with VMware Engine, you can create a private cloud that contains only a single node and cluster in any region where VMware Engine is available. All VMware Engine features are available in a single-node private cloud, but there are specific limitations on VMware stack features due to cluster size.

The following are common use cases for a single-node private cloud:

  * **Proof of concept:** evaluating VMware Engine and its capabilities
  * **Disaster recovery testing:** deploying your application from recent backups to periodically validate disaster recovery preparedness
  * **Application upgrade testing:** test and validate application component upgrades before upgrading your application in production



VMware Engine permits single-node private clouds without a time limit. However, single-node private clouds are not eligible for [SLA](https://docs.cloud.google.com/vmware-engine/sla) coverage. You can upgrade a single-node private cloud to a standard private cloud by expanding to at least 3 nodes. The expansion process won't disturb your VMs or access to vCenter, and it initializes vSAN data replication after the nodes are successfully added to the cluster.

For single-node private clouds, the default vSAN storage policy uses a Failures to Tolerate (FTT) value of FTT=0. When you expand a single-node private cloud, VMware Engine changes the default vSAN storage policy. The default vSAN storage policy changes to use FTT=1 for 3–4 node private clouds and to use FTT=2 for private clouds with at least 5 nodes.

Single-node private clouds are not upgraded with new software like a standard private cloud. You must delete and recreate single-node private clouds to obtain the latest software and security updates.

### Custom core counts

Some licensing agreements charge you based on the number of CPU cores on the underlying physical node or in the cluster. Whenever you create a new cluster, you can reduce the number of available cores for each node in the cluster to meet the application license requirements. VMware Engine also creates any new nodes added to that cluster with the same number of cores per node, including when replacing a failed node. Confirm how the cores are counted (physically present or made available by BIOS) as stated in your contract to manage licensing costs using this feature.

Custom core counts are available for both the initial cluster as well as for any other clusters created in a private cloud. Reducing the number of available cores doesn't affect node pricing.

## Limitations

Each private cloud has resource limits for its nodes and clusters. Refer to [VMware in a private cloud](https://docs.cloud.google.com/vmware-engine/docs/concepts-vmware-components#vsphere-limits) for a list of these limits.

### Node limits

When planning your VMware Engine resource needs, consider the number of nodes you need in your private cloud. The following table describes vSphere cluster limits in private clouds that meet [SLA](https://docs.cloud.google.com/vmware-engine/sla) requirements:

Resource | Limit  
---|---  
Minimum number of nodes to create a private cloud (first cluster) | 3  
Minimum number of nodes to create a cluster | 3  
Maximum number of nodes per cluster | 32  
Maximum number of nodes per private cloud | 128  
Maximum number of clusters per private cloud | 32  
  
### Private cloud and cluster limitations

The following limitations apply to private clouds and clusters:

  * You can create private clouds with mixed node types, combining `ve1` and `ve2` nodes in a single private cloud.
  * All nodes in a given cluster must be of the same node type. For example, a cluster can contain only `ve1-standard-72` nodes or only `ve2-standard-128` nodes, but not a mix of both in the same cluster.
  * Within a cluster, you can mix storage-only nodes with compute nodes of the same node family (for example, `ve2-standard-128` with `ve2-standard-so`). For more information, see [Storage-only nodes](https://docs.cloud.google.com/vmware-engine/docs/concepts-storage-only-nodes).
  * To create a new cluster of a different node family in an existing private cloud, contact Cloud Customer Care.



This flexibility lets you to optimize resource utilization and costs by tailoring clusters to meet specific workload requirements.

### Single-node private cloud limitations

For single-node private clouds, the following limitations apply to the VMware stack:

  * Features or operations that require more than 1 node won't work. For example, you won't be able to use vSphere Distributed Resource Scheduler (DRS) or HA.
  * The default vSAN storage policy uses FTT=0, so node failure results in data loss.



Additionally, the following VMware Engine limitations apply:

  * You can't add a single-node cluster to an existing private cloud.
  * An existing private cloud can't be converted to a single-node private cloud.
  * Node adjustments by autoscale policies aren't supported with a single-node private cloud.
  * VMware stack upgrades involve a downtime for your single-node private cloud.
  * VMware Engine doesn't encrypt data on vSAN on a single-node private cloud by default.
  * A private cloud must contain at least 3 nodes and complete vSAN data replication to be eligible for coverage based on the [SLA](https://docs.cloud.google.com/vmware-engine/sla).
  * You can't adjust the number of cores per node with a single-node private cloud.



### Custom core count limitations

The following limitations apply to a cluster that has a custom core count:

  * All nodes added to the cluster after initial creation also use the custom core count.
  * The number of cores per node can't be changed after cluster creation. To change the number of cores per nodes in the cluster, you must delete the cluster and create a new one.
  * The number of cores per node must be a multiple of 4 with a minimum of 8 (for example 8, 12, or 16).
  * Custom core counts aren't available for single-node private clouds.



## What's next

  * Learn about [VLANs and subnets](https://docs.cloud.google.com/vmware-engine/docs/concepts-vlans-subnets).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
