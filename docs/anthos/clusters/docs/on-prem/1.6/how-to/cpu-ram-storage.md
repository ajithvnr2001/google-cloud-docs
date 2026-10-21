---
url: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/cpu-ram-storage/
title: CPU, RAM, and storage requirements \u00a0|\u00a0 Anthos clusters on VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:57:29.665701+00:00
---

# CPU, RAM, and storage requirements  |  Anthos clusters on VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/cpu-ram-storage/

**Version 1.6**. This version is no longer supported. For more information see the [ version support policy](https://cloud.google.com/anthos/clusters/docs/on-prem/latest/getting-support#version_support_policy). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine)
  * [ GKE Enterprise ](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs)
  * [ Clusters ](https://docs.cloud.google.com/anthos/clusters)
  * [ Documentation ](https://docs.cloud.google.com/anthos/clusters/docs)
  * [ Anthos clusters on VMware 1.6 ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6)
  * [ Guides ](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/overview)



Send feedback 

#  CPU, RAM, and storage requirements Stay organized with collections  Save and categorize content based on your preferences. 

This page describes the CPU, RAM, and storage requirements for an Google Distributed Cloud installation.

When you install Google Distributed Cloud, you create:

  * An admin workstation
  * An admin cluster
  * One or more user clusters



The admin cluster runs the Google Distributed Cloud infrastructure, and the user clusters run your workloads.

If you choose to use the Seesaw load balancer, then you must also create VMs to run the load balancer. Each cluster that has a highly available (HA) Seesaw load balancer requires two VMs for Seesaw. Each cluster that has a non-HA Seesaw load balancer requires one VM for Seesaw.

Your vSphere environment must have enough CPU, RAM, and storage resources to fulfill the needs of your admin workstation, your admin cluster, and your user clusters. The resource needs of your user clusters depend on the type of workloads you intend to run.

If your configuration includes a bundled Seesaw load balancer, then you require additional resources. See [Bundled load balancing with Seesaw](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/bundled-load-balance).

## CPU, RAM, and storage requirements for the admin workstation

The physical ESXi hosts in your datacenter must provide enough CPU and RAM to support the needs of your admin workstation. Also, your vSphere environment must provide enough storage to fulfill the needs of your admin workstation. The admin workstation has the following resource needs:

  * 4 vCPUs (virtual CPUs)
  * 8,192 MiB of RAM
  * 50 GiB of storage



## CPU, RAM, and storage requirements for the admin cluster

The physical ESXi hosts in your datacenter must provide enough CPU and RAM to fulfill the needs of your admin cluster. Also, your vSphere environment must provide enough storage to fulfill the needs of the admin cluster.

The admin cluster has one or more associated user clusters. For each associated user cluster, the admin cluster has one or three nodes. These nodes run the control plane components for the user cluster, and they are called user cluster control plane nodes.

If a user cluster is highly available (HA), then the admin cluster has three control plane nodes for that user cluster. If a user cluster is not HA, then the admin cluster has one control plane node for that user cluster.

The admin cluster has the following storage needs:

  * 100 GiB to store etcd object data.

  * 240 GiB for [Google Cloud Observability](https://cloud.google.com/products/operations) to buffer logs and metrics during a network outage.

  * If the Prometheus and Grafana add-on is enabled, 506 GiB for Prometheus to store metrics data for four days.

  * For each node, 40 GiB. This includes the nodes that serve as user cluster control planes.

  * For each user cluster control plane node, an additional 10 GiB to fulfill PVCs created for audit logs.

  * For each user cluster control plane mode, an additional 5 GiB to fulfill PVCs created for etcd object data, and an additional 5 GiB to fulfill PVCs created for etcd event data.




The following table describes the CPU, RAM, and storage requirements for nodes in the admin cluster:

Name | Requirements | Purpose  
---|---|---  
**Admin cluster control plane** | 

  * 4 vCPUs
  * 16,384 MiB of RAM
  * 40 GiB of storage for a boot disk. 100 GiB of storage for a data disk. 40 GiB of storage for a VM template.

|  Runs the control plane for the admin cluster.  
**Add-ons VMs** |  Two VMs, each of which has the following requirements:

  * 4 vCPUs
  * 16,384 MiB of RAM
  * 40 GiB of storage

|  Runs add-ons for the admin cluster.  
**User cluster control plane** |  For each user cluster, one or three VMs. Each VM has the following requirements:

  * 4 vCPUs
  * 8,192 MiB of RAM
  * 40 GiB of storage

|  Each user cluster has its own control plane that runs on a VM called a control plane. The control plane VMs for a user cluster are nodes in the admin cluster. You can choose to create one or three control plane nodes for an individual user cluster.   
**Note:** When you upgrade a cluster, whether it is an admin or user cluster, Google Distributed Cloud creates a temporary node to ensure uninterrupted availability. If your setup uses static IPs, then when you upgrade a cluster, make sure you have configured an additional IP address for this temporary node. If your setup uses DHCP, then when you upgrade a cluster, make sure that your DHCP server can provide enough IP addresses for this temporary node. See [Upgrading Anthos clusters on VMware](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/upgrading).

## CPU, RAM, and storage requirements for a user cluster

For each user cluster that you intend to create, the physical ESXi hosts in your data center must provide enough CPU and RAM to fulfill the needs of the user cluster. Also, for each user cluster that you intend to create, your vSphere environment must provide enough storage to fulfill the needs of the cluster.

A user cluster has the following storage needs:

  * For each node, 40 GiB.

  * 240 GiB for Google Cloud Observability to buffer logs and metrics during a network outage.

  * If the Prometheus and Grafana add-on is enabled, 506 GiB for Prometheus to store metrics data for four days.




The following table describes default values for CPU, RAM, and storage for each node in a user cluster. Depending on the needs of your workloads, you might want to adjust the values. To determine how much CPU and RAM are available on a node for your workloads, see [Resources available for your workloads](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/resources-available-pods). You can specify values for CPU and RAM in the `usercluster.workernode` field of the [Google Distributed Cloud configuration file](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.6/how-to/configuration-file-overview):

Name | Requirements | Purpose  
---|---|---  
**User cluster worker nodes** | These are the default values for an individual worker node:

  * 4 vCPUs
  * 8,192 MiB of RAM
  * 40 GiB of storage

|  A user cluster node is a virtual machine where your workloads run. When you create a user cluster, you decide how many nodes it should have. The resources required for your user cluster nodes depend on the workloads you intend to run.  
  
## Example of CPU, RAM, and storage requirements

Suppose you intend to create the following clusters:

  * An admin cluster

  * A user cluster where you think each node will need 6 vCPUs, 16,384 MiB of RAM, and 40 GiB of storage. This user cluster will have 20 nodes. You want the control plane for this user cluster to be highly available, so there will be three nodes in the admin cluster that serve as control planes for this user cluster. Each user-cluster control plane node will be configured with the default 8,192 MiB of RAM.

  * A second user cluster where you think the default CPU, RAM, and storage values will be appropriate. This user cluster will have eight nodes. You do not need the control plane for this user cluster to be highly available, so there will be only one node in the admin cluster that serves as control plane for this user cluster. The user-cluster control plane node will be configured with the default 8,192 MiB of RAM.




Also suppose that you do not intend to enable the Prometheus and Grafana add-on in any of your clusters.

The admin cluster has a control plane node, two nodes for add-ons, three nodes for the control plane of your first user cluster, and one node for the control plane of your second user cluster. So the admin cluster has seven nodes.

The admin cluster has the following CPU requirements:

  * For each node, 4 vCPUs.



The admin cluster has the following memory requirements:

  * For each of two add-on nodes and the admin cluster control plane, 16,384 MiB.

  * For each of four user-cluster control plane nodes, 8,192 MiB, the default setting.




The admin cluster has the following storage requirements:

  * 100 GiB to store etcd data for the admin cluster.

  * 240 GiB to fulfill PVCs created by [Google Cloud Observability](https://cloud.google.com/products/operations).

  * For each node, 40 GiB.

  * 3 x 5 GiB to store etcd object data for the HA user cluster and 5 GiB to store etcd event data for the HA usercluster.

  * 3 x 10 GiB to store audit logs for the HA user cluster.

  * 5 GiB to store etcd object data for the non-HA user cluster and 5 GiB to store etcd event data for the non-HA user cluster

  * 10 GiB to store audit logs for the non-HA user custer.




The following table summarizes the CPU, RAM, and storage requirements for the admin cluster:

Example: Admin cluster requirements  
---  
vCPU | 7 x 4 | 28 CPUs  
RAM | 3 x 16384 + 4 x 8192 | 81,920 MiB  
Storage | 100 + 240 + 7 x 40 + 3 x 5 + 5 + 3 x 10 + 5 + 5 + 10 | 690 GiB  
  
Each node in the first user cluster requires 6 vCPUs, and 16,384 MiB of RAM, and 40 GiB of storage. Also, the first user cluster requires 240 GiB of storage to fulfill PVCs created by Google Cloud Observability.

The following table summarizes the CPU, RAM, and storage requirements for the first user cluster:

Example: First user cluster requirements  
---  
CPU | 20 x 6 | 120 vCPUs  
RAM | 20 x 16384 | 327,680 MiB  
Storage | 240 + 20 x 40 | 1,040 GiB  
  
Each node in the second user cluster requires 4 vCPUs, 8,192 MiB of RAM, and 40 GiB of storage. Also, the second user cluster requires 240 GiB of storage to fulfill PVCs created by Google Cloud Observability.

The following table summarizes the CPU, RAM, and storage requirements for the second user cluster:

Example: Second user cluster requirements  
---  
CPU | 8 x 4 | 32 vCPUs  
RAM | 8 x 8192 | 65,536 MiB  
Storage | 240 + 8 x 40 | 560 GiB  
  
Total requirements:

Example: Total requirements  
---  
CPU | 180 vCPUs  
RAM | 475,136 MiB  
Storage | 2,290 GiB  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
