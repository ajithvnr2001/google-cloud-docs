---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage/
title: CPU, RAM, and storage requirements \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:21:33.453223+00:00
---

# CPU, RAM, and storage requirements  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/cpu-ram-storage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  CPU, RAM, and storage requirements Stay organized with collections  Save and categorize content based on your preferences. 

This document describes the CPU, RAM, and storage requirements for an installation of Google Distributed Cloud (software only) on VMware. This page is for Admins and architects who define IT solutions and system architecture in accordance with company strategy. To learn more about common roles and example tasks that we reference in Google Cloud content, see [Common GKE user roles and tasks](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/concepts/roles-tasks).

This document describes requirements for an installation where the user clusters have [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) enabled.

The requirements given here are suitable for a production environment. For the minimum CPU, RAM, and storage requirements for a proof-of-concept demonstration, see [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure).

## CPU, RAM, and storage requirements for an admin workstation

Before you create an admin workstation, you fill in an [admin workstation configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-workstation-configuration-file). In the configuration file, you specify a vSphere [cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html), a vSphere [resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html), and a vSphere [datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html).

The vSphere cluster is a set of physical hosts running [ESXi](https://www.vmware.com/products/esxi-and-esx.html), and the resource pool has a reservation for a portion of the resources available on those ESXi hosts.

The resource pool must have enough CPU and RAM to support the requirements of your admin workstation and any other VMs that belong to the pool. Likewise, the datastore must have enough storage to support the requirements of your admin workstation and any other VMs that use the datastore.

The admin workstation has the following requirements:

  * 4 vCPUs (virtual CPUs)
  * 8 GiB of RAM
  * 100 GiB



Google Distributed Cloud supports only x86-64 vCPUs at the CPU microarchitecture level v3 (x86-64-v3) and higher.

## CPU, RAM, and storage requirements for an admin cluster

Before you create an admin cluster, you fill in an [admin cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest). In the configuration file, you specify a vSphere [cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html), a vSphere [resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html), and a vSphere [datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.html).

The vSphere cluster is a set of physical hosts running [ESXi](https://www.vmware.com/products/esxi-and-esx.html), and the resource pool has a reservation for a portion of the resources available on those ESXi hosts.

The resource pool must have enough CPU and RAM to support the requirements of your admin cluster and any other VMs that belong to the pool. Likewise, the datastore must have enough storage to support the requirements of your admin cluster and any other VMs that use the datastore.

An admin cluster has one or three nodes. These are the control-plane nodes for the admin cluster: three for a high-availability (HA) admin cluster and one for a non-HA admin cluster.

The admin cluster has the following storage requirements:

  * If advanced clusters isn't enabled:

    * For each node, 40 GiB for a VM template

    * For each node, 25 GiB to store etcd object data

    * For each node, 240 GiB for [Google Cloud Observability](https://cloud.google.com/products/operations) to buffer logs and metrics during a network outage

  * If advanced clusters is enabled

    * For each node, 50 GiB for a VM template

    * For each node, 25 GiB to store etcd object data

    * For each node, 20 GiB for [Google Cloud Observability](https://cloud.google.com/products/operations) to buffer logs and metrics during a network outage




The following table gives the CPU, RAM, and storage requirements for nodes in the admin cluster, the requirements depends on whether you will [enabled advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) when you create the admin cluster.

Node | Requirements | Purpose  
---|---|---  
**Admin cluster control-plane** | 

  * 2 vCPUs
  * 4 GiB of RAM
  * 40 GiB of storage

|  Runs the control plane for the admin cluster.  
**Advanced admin cluster control-plane** | 

  * 3 vCPUs
  * 7 GiB of RAM
  * 50 GiB of storage

|  Runs the control plane for the admin cluster.  
  
* Google Distributed Cloud supports only x86-64 vCPUs at the CPU microarchitecture level v3 (x86-64-v3) and higher.

## CPU, RAM, and storage requirements for a user cluster

Before you create a user cluster, you fill in a [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest). In the configuration file, you specify a vSphere [cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html), a vSphere [resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html) and a vSphere [datastore](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-storage.htmle).

The vSphere cluster is a set of physical hosts running [ESXi](https://www.vmware.com/products/esxi-and-esx.html), and the resource pool has a reservation for a portion of the resources available on those ESXi hosts.

The resource pool must have enough CPU and RAM to support the requirements of your user cluster and any other VMs that belong to the pool. Likewise, the datastore must have enough storage to support the requirements of your user cluster and any other VMs that use the datastore.

A user cluster has the following storage requirements:

  * If advanced clusters isn't enabled:

    * For each control-plane node, 60 GiB

    * For each worker node, 40 GiB

    * For each node, 120 GiB for [Google Cloud Observability](https://cloud.google.com/products/operations) to buffer logs and metrics during a network outage

  * If advanced clusters is enabled

    * For each control-plane node, 50 GiB

    * For each worker node, 40 GiB

    * For each node, 20 GiB for [Google Cloud Observability](https://cloud.google.com/products/operations) to buffer logs and metrics during a network outage




The following table gives the required CPU, RAM, and storage for each control-plane node in a user cluster, the requirements depends on whether you will [enabled advanced clusters](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field) when you create the admin cluster. It also gives the default CPU, RAM, and storage values for each worker node in a user cluster. Depending on the needs of your workloads, you might want to adjust the values for your worker nodes. To determine how much CPU and RAM are available on a node for your workloads, see [Resources available for your workloads](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/resources-available-pods). You can specify values for CPU and RAM in the `nodePools` section of the [user cluster configuration file](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest).

Node | Requirements | Purpose  
---|---|---  
**Control-plane node** |  One or three VMs. Each VM has the following requirements:

  * 3 vCPUs
  * 5 GiB of RAM
  * 60 GiB of storage

|  Runs the control plane for a user cluster.  
**Advanced control-plane node** |  Three VMs. Each VM has the following requirements:

  * 3 vCPUs
  * 5 GiB of RAM
  * 50 GiB of storage

|  Runs the control plane for a user cluster, has [advanced cluster enabled](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-latest#enable-advanced-cluster-field)  
**Worker node** | These are the default values for an individual worker node:

  * 4 vCPUs
  * 8 GiB of RAM
  * 40 GiB of storage

|  A user cluster worker node is a virtual machine where your workloads run. The resources required for your user cluster nodes depend on the workloads you intend to run.  
  
* Google Distributed Cloud supports only x86-64 vCPUs at the CPU microarchitecture level v3 (x86-64-v3) and higher.

## Example of CPU, RAM, and storage requirements when advanced clusters isn't enabled

Suppose you have two vSphere [data centers](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html):

  * Data center 1 has a [vSphere cluster](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management.html) named Cluster 1, and Cluster 1 has a [resource pool](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-resource-management.html) named Resource Pool 1. There are four physical hosts running ESXi in Cluster 1.

  * Data center 2 has a vSphere cluster named Cluster 2, and Cluster 2 has a resource pool named Resource Pool 2. There are eight physical hosts running ESXi in Cluster 2.




You decide that your admin workstation and your admin cluster will be in Resource Pool 1 and use Datastore 1.

You decide that your user clusters will be in Resource Pool 2 and use Datastore 2. You don't intend to enable Prometheus in your user clusters.

You want to create these two user clusters:

  * A user cluster where you think each worker node will need 6 vCPUs, 16 GiB of RAM, and 40 GiB of storage. This user cluster will have 20 worker nodes. You want an HA control plane for this user cluster, so there will be three control-plane nodes in the user cluster.

  * A second user cluster where you think each worker node will need 4 vCPUs, 8 GiB of RAM, and 40 GiB of storage. This user cluster will have eight worker nodes. You don't need an HA control plane for this user cluster, so there will be only one control-plane node in the user cluster.




### Requirements for Resource Pool 1 and Datastore 1

Resource Pool 1 has reserved a portion of the CPU and RAM provided by the four ESXi hosts in Cluster 1. Resource Pool 1 must have enough CPU and RAM to meet the requirements of the admin workstation and the admin cluster. And Datastore 1 must have enough storage to meet the requirements of the admin workstation and the admin cluster.

The admin cluster has three nodes, each of which is a control-plane node.

![Diagram showing admin workstation and admin cluster](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/resource-pool-1.svg)

Recall that the admin workstation has these resource requirements:

Example: Admin workstation requirements  
---  
vCPU | 4 vCPUs  
RAM | 8 GiB  
Storage | 50 GiB  
  
The admin cluster has these resource requirements:

Example: Admin cluster requirements  
---  
vCPU |  3 admin cluster control-plane node x 2 vCPUs/node  | 6 vCPUs  
RAM |  3 admin cluster control-plane node x 4 GiB/node | 12 GiB  
Storage |  40 GiB for a VM template +  
100 GiB for etcd object data +  
240 GiB for Google Cloud Observability +  
3 admin cluster control-plane nodes x 40 GiB/node | 500 GiB  
  
The following table gives the total CPU, RAM, and storage requirements for the admin workstation and admin cluster. Resource Pool 1 and Datastore 1 must be able to provide these resources:

Example: Total requirements for Resource Pool 1 and Datastore 1  
---  
vCPU | 29 vCPUs  
RAM | 73 GiB  
Storage | 790 GiB  
  
### Requirements for Resource Pool 2 and Datastore 2

Resource Pool 2 has reserved a portion of the CPU and RAM provided by the eight ESXi hosts in Cluster 2. Resource Pool 2 must have enough CPU and RAM to meet the requirements of both user clusters. And Datastore 2 must have enough storage to meet the requirements of both user clusters.

![Diagram showing two user clusters](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/resource-pool-2.svg)

The first user cluster has these resource requirements:

Example: First user cluster requirements  
---  
CPU | 3 control-plane nodes x 3 vCPUs/node +  
20 worker nodes x 6 vCPUs/node | 129 vCPUs  
RAM | 3 control-plane nodes x 5 GiB/node +  
20 worker nodes x 16 GiB/node | 335 GiB  
Storage |  240 GiB for Google Cloud Observability +  
3 control-plane nodes x 60 GiB/node +  
20 worker nodes x 40 GiB/node  | 1,220 GiB  
  
The second user cluster has these resource requirements:

Example: Second user cluster requirements  
---  
CPU | 1 control-plane node x 3 vCPUs/node +   
8 worker nodes x 4 vCPUs/node | 35 vCPUs  
RAM | 1 control-plane node x 5 GiB/node +   
8 worker nodes x 8 GiB/node | 69 GiB  
Storage |  240 GiB for Google Cloud Observability +  
1 control-plane node x 60 GiB/node +   
8 worker nodes x 40 GiB/node  | 620 GiB  
  
The following table gives the total CPU, RAM, and storage requirements for the two user clusters. Resource Pool 2 and Datastore 2 must be able to provide these resources:

Example: Total requirements for Resource Pool 2 and Datastore 2  
---  
CPU | 164 vCPUs  
RAM | 404 GiB  
Storage | 1,840 GiB  
  
## Resource overcommitment

vSphere supports resource overcommitment, for example [memory overcommitment](https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.resmgmt.doc/GUID-895D25BA-3929-495A-825B-D2A468741682.html) and [CPU overcommitment](https://docs.vmware.com/en/VMware-Cloud-on-AWS/services/vmc-aws-performance/GUID-E0319C4E-07ED-43D7-847E-7A5F89226A57.html). So the total resources reserved by the resource pools in a cluster can be greater than the physical resources provided by the ESXi hosts in the cluster.

The requirements given in this document are for reserved virtual resources. For a description of the physical resources required for a proof-of-concept demonstration, see [Set up minimal infrastructure](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/minimal-infrastructure).

## Monitor resource contention

You should monitor resource contention signals to make sure that your resource pools and datastores can support your configured virtual resources. For more information, see [Create a VM health status dashboard](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/logging-and-monitoring#vm-health-status-dashboard).

## Disk provisioning

The following table shows the VMware thin and thick disk provisioning policies for different storage disks.

Storage disks | Size | Disk provision policy  
---|---|---  
Default | User choice  
Admin etcd | 100 GB | Thin | No  
User etcd | 40 GB | Thin | No  
Node OS/boot disk | 40 GB - default and minimum  
(user configurable) | Thick  
(lazy zeroed) | No  
Other (for example, logs) | 240 GB | Thin | No  
User workloads | — | Thin | Yes  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
