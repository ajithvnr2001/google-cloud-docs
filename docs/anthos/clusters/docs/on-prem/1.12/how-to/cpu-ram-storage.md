---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/cpu-ram-storage/
title: CPU, RAM, and storage requirements \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:06:31.018655+00:00
---

# CPU, RAM, and storage requirements  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/cpu-ram-storage/

**Version 1.12**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.12 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/overview)



Send feedback 

#  CPU, RAM, and storage requirements Stay organized with collections  Save and categorize content based on your preferences. 

Version 1.12 keyboard_arrow_down

  * [ Latest version ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/how-to/cpu-ram-storage)
  * [ Version 1.16 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/cpu-ram-storage)
  * [ Earlier versions (unsupported) ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/latest/version-history#expandable-1)



This document describes the CPU, RAM, and storage requirements for an installation of Google Distributed Cloud.

The requirements given here are suitable for a production environment. For minimum requirements that are suitable for a proof-of-concept demonstration, see [Minimum CPU, RAM, and storage requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/minimum-cpu-ram-storage).

## CPU, RAM, and storage requirements for an admin workstation

Before you create an admin workstation, you fill in an [admin workstation configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/admin-workstation-configuration-file). In the configuration file, you specify a vSphere [cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html), a vSphere [resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) and a vSphere [datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html).

The vSphere cluster is a set of physical hosts running [ESXi](https://www.vmware.com/products/esxi-and-esx.html), and the resource pool has a reservation for a portion of the resources available on those ESXi hosts.

The resource pool must have enough CPU and RAM to support the requirements of your admin workstation and any other VMs that belong to the pool. Likewise, the datastore must have enough storage to support the requirements of your admin workstation and any other VMs that use the datastore.

The admin workstation has the following requirements:

  * 4 vCPUs (virtual CPUs)
  * 8 GiB of RAM
  * 50 GiB



## CPU, RAM, and storage requirements for an admin cluster

Before you create an admin cluster, you fill in an [admin cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/admin-cluster-configuration-file). In the configuration file, you specify a vSphere [cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html), a vSphere [resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) and a vSphere [datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html).

The vSphere cluster is a set of physical hosts running [ESXi](https://www.vmware.com/products/esxi-and-esx.html), and the resource pool has a reservation for a portion of the resources available on those ESXi hosts.

The resource pool must have enough CPU and RAM to support the requirements of your admin cluster and any other VMs that belong to the pool. Likewise, the datastore must have enough storage to support the requirements of your admin cluster and any other VMs that use the datastore.

The admin cluster has one or more associated user clusters. For each associated user cluster, the admin cluster has one or three nodes. These nodes run the control-plane components for the user cluster, and they are called user cluster control-plane nodes.

For a high-availability (HA) user cluster, the admin cluster has three control-plane nodes. For a non-HA user cluster, the admin cluster has one control plane node.

The admin cluster has the following storage requirements:

  * 40 GiB for a VM template

  * 100 GiB to store etcd object data

  * 240 GiB for [Google Cloud Observability](https://cloud.google.com/products/operations) to buffer logs and metrics during a network outage

  * If Prometheus is enabled, 506 GiB for Prometheus to store metrics data

  * For each node, 40 GiB. This includes the nodes that serve as user cluster control planes.

  * For each user cluster control-plane node:

    * An additional 10 GiB to fulfill PVCs created for audit logs
    * An additional 5 GiB to fulfill PVCs created for etcd object data
    * An additional 5 GiB to fulfill PVCs created for etcd event data



The following table gives the CPU, RAM, and storage requirements for nodes in the admin cluster:

Node | Requirements | Purpose  
---|---|---  
**Admin cluster control-plane** | 

  * 2 vCPUs
  * 4 GiB of RAM
  * 40 GiB of storage

|  Runs the control plane for the admin cluster.  
**Add-ons** |  Two VMs, each of which has the following requirements:

  * 4 vCPUs
  * 16 GiB of RAM
  * 40 GiB of storage

|  Runs add-ons for the admin cluster.  
**User cluster control plane** |  For each user cluster, one or three VMs. Each VM has the following requirements:

  * 3 vCPUs
  * 5 GiB of RAM
  * 60 GiB of storage

|  Runs the control plane for a user cluster.   
  
## CPU, RAM, and storage requirements for a user cluster

Before you create a user cluster, you fill in a [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file). In the configuration file, you specify a vSphere [cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-487C09CE-8BE2-4B89-BA30-0E4F7E3C66F7.html), a vSphere [resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) and a vSphere [datastore](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.storage.doc/GUID-3CC7078E-9C30-402C-B2E1-2542BEE67E8F.html).

The vSphere cluster is a set of physical hosts running [ESXi](https://www.vmware.com/products/esxi-and-esx.html), and the resource pool has a reservation for a portion of the resources available on those ESXi hosts.

The resource pool must have enough CPU and RAM to support the requirements of your user cluster and any other VMs that belong to the pool. Likewise, the datastore must have enough storage to support the requirements of your user cluster and any other VMs that use the datastore.

A user cluster has the following storage requirements:

  * For each node, 40 GiB

  * 240 GiB for Google Cloud Observability to buffer logs and metrics during a network outage

  * If Prometheus is enabled, 506 GiB for Prometheus to store metrics data




The following table gives default values for CPU, RAM, and storage for each node in a user cluster. Depending on the needs of your workloads, you might want to adjust the values. To determine how much CPU and RAM are available on a node for your workloads, see [Resources available for your workloads](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/resources-available-pods). You can specify values for CPU and RAM in the `nodePools` section of the [user cluster configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/user-cluster-configuration-file).

Node | Requirements | Purpose  
---|---|---  
**Worker node** | These are the default values for an individual worker node:

  * 4 vCPUs
  * 8 GiB of RAM
  * 40 GiB of storage

|  A user cluster node is a virtual machine where your workloads run. The resources required for your user cluster nodes depend on the workloads you intend to run.  
  
## CPU, RAM, and storage requirements for a Seesaw load balancer

If you intend to create a cluster that uses the Seesaw load balancer, there are additional resource requirements. For details, see [Provision VM resources for Seesaw VMs](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/bundled-load-balance#provision_vm_resources).

## Example of CPU, RAM, and storage requirements

Suppose you have two vSphere [data centers](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-7FDFBDBE-F8AC-4D00-AE5E-3F14D7472FAF.html):

  * Data center 1 has a [vSphere cluster](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vcenterhost.doc/GUID-F7818000-26E3-4E2A-93D2-FCDCE7114508.html) named Cluster 1, and Cluster 1 has a [resource pool](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-60077B40-66FF-4625-934A-641703ED7601.html) named Resource Pool 1. There are four physical hosts running ESXi in Cluster 1.

  * Data center 2 has a vSphere cluster named Cluster 2, and Cluster 2 has a resource pool named Resource Pool 2. There are eight physical hosts running ESXi in Cluster 2.




You decide that your admin workstation and your admin cluster will be in Resource Pool 1 and use Datastore 1.

You decide that your user clusters will be in Resource Pool 2 and use Datastore 2. You do not intend to enable Prometheus in your user clusters.

You decide that you will not use the Seesaw load balancer.

You want to create these two user clusters:

  * A user cluster where you think each worker node will need 6 vCPUs, 16 GiB of RAM, and 40 GiB of storage. This user cluster will have 20 nodes. You want an HA control plane for this user cluster, so there will be three nodes in the admin cluster that serve as control planes for this user cluster. Each user-cluster control plane node will be configured with 4 vCPUs and 8 GiB of RAM.

  * A second user cluster where you think each worker node will need 4 vCPUs, 8 GiB of RAM, and 40 GiB of storage. This user cluster will have eight nodes. You do not need an HA control plane for this user cluster, so there will be only one node in the admin cluster that serves as control plane for this user cluster. The user cluster control-plane node will be configured with 3 vCPUs and 5 GMiB of RAM.




### Requirements for Resource Pool 1 and Datastore 1

Resource Pool 1 has reserved a portion of the CPU and RAM provided by the four ESXi hosts in Cluster 1. Resource Pool 1 must have enough CPU and RAM to meet the requirements of the admin workstation and the admin cluster. And Datastore 1 must have enough storage to meet the requirements of the admin workstation and the admin cluster.

The admin cluster has its own control plane node, two nodes for add-ons, three nodes for the control plane of your first user cluster, and one node for the control plane of your second user cluster. So the admin cluster has seven nodes.

![Diagram showing admin workstation and admin cluster](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.12/images/resource-pool-1.svg)

Recall that the admin workstation has these resource requirements:

Example: Admin workstation requirements  
---  
vCPU | 4 vCPUs  
RAM | 8 GiB  
Storage | 50 GiB  
  
The admin cluster has these resource requirements:

Example: Admin cluster requirements  
---  
vCPU |  1 admin cluster control-plane node x 2 vCPUs/node +  
2 add-on nodes x 4 vCPUs/node +  
3 user cluster control-plane nodes x 4 vCPUs/node +  
1 user cluster control-plane node x 3 vCPUs/node  | 25 vCPUs  
RAM |  1 admin cluster control-plane node x 4 GiB/node +  
2 add-on nodes x 16 GiB/node + 3 user cluster control-plane nodes x 8 GiB/node +  
1 user cluster control-plane node x 5 GiB/node  | 65 GiB  
Storage |  40 GiB for a VM template +  
100 GiB for etcd object data +  
240 GiB for Google Cloud Observability +  
1 admin cluster control-plane node x 40 GiB/node +  
2 add-on nodes x 40 GiB/node +  
4 user cluster control-plane nodes x 60 GiB/node  
| 740 GiB  
  
The following table gives the total CPU, RAM, and storage requirements for the admin workstation and admin cluster. Resource Pool 1 and Datastore 1 must be able to provide these resources:

Example: Total requirements for Resource Pool 1 and Datastore 1  
---  
vCPU | 29 vCPUs  
RAM | 73 GiB  
Storage | 790 GiB  
  
### Requirements for Resource Pool 2 and Datastore 2

Resource Pool 2 has reserved a portion of the CPU and RAM provided by the eight ESXi hosts in Cluster 2. Resource Pool 2 must have enough CPU and RAM to meet the requirements of both user clusters. And Datastore 1 must have enough storage to meet the requirements of both user clusters.

![Diagram showing two user clusters](https://docs.cloud.google.com/static/anthos/clusters/docs/on-prem/1.12/images/resource-pool-2.svg)

The first user cluster has these resource requirements:

Example: First user cluster requirements  
---  
CPU | 20 nodes x 6 vCPUs/node | 120 vCPUs  
RAM | 20 nodes x 16 GiB/node | 320 GiB  
Storage |  240 GiB for Google Cloud Observability +  
20 nodes x 40 GiB/node  | 1,040 GiB  
  
The second user cluster has these resource requirements:

Example: Second user cluster requirements  
---  
CPU | 8 nodes x 4 vCPUs/node | 32 vCPUs  
RAM | 8 nodes x 8 GiB/node | 64 GiB  
Storage |  240 GiB for Google Cloud Observability +  
8 nodes x 40 GiB/node  | 560 GiB  
  
The following table gives the total CPU, RAM, and storage requirements for the two user clusters. Resource Pool 2 and Datastore 2 must be able to provide these resources:

Example: Total requirements for Resource Pool 2 and Datastore 2  
---  
CPU | 152 vCPUs  
RAM | 384 GiB  
Storage | 1,600 GiB  
  
## Resource overcommitment

vSphere supports resource overcommitment, for example [memory overcommitment](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-895D25BA-3929-495A-825B-D2A468741682.html) and [CPU overcommitment](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/vmc-aws-performance/GUID-E0319C4E-07ED-43D7-847E-7A5F89226A57.html). So the total resources reserved by the resource pools in a cluster can be greater than the physical resources provided by the ESXi hosts in the cluster.

The requirements given in this document are for reserved virtual resources. For a description of the physical required for a proof-of-concept demonstration, see [Minimum CPU, RAM, and storage requirements](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/minimum-cpu-ram-storage).

## Monitor resource contention

You should monitor resource contention signals to make sure that your resource pools and datastores can support your configured virtual resources. For more information, see [Create a VM health status dashboard](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.12/how-to/logging-and-monitoring#vm-health-status-dashboard).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
