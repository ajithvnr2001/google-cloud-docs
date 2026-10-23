---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/failure-mode-analysis/
title: Understand the impact of failures in Google Distributed Cloud \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:44.504340+00:00
---

# Understand the impact of failures in Google Distributed Cloud  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/troubleshooting/failure-mode-analysis/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Understand the impact of failures in Google Distributed Cloud Stay organized with collections  Save and categorize content based on your preferences. 

Google Distributed Cloud is designed to limit the scope of failures and to prioritize functionality that's critical to business continuity. This document explains how the functionality of your clusters are impacted when there's a failure. This information can help you prioritize areas to troubleshoot if you have a problem.

The core functionality of Google Distributed Cloud includes the following categories:

  * **Run workloads** : Existing workloads can continue to run. This is the most important consideration to maintain business continuity. Even if your cluster has a problem the existing workloads might continue to run without interruption.
  * **Manage workloads** : You can create, update, and delete workloads. This is the second most important consideration to scale workloads when traffic increases, even if the cluster has a problem.
  * **Manage user clusters** : You can manage nodes, update, upgrade, and delete user clusters. This is less important than the application lifecycle considerations. If there's available capacity on the existing nodes, the inability to modify user clusters doesn't affect user workloads.
  * **Manage admin clusters** : You can update and upgrade the admin cluster. This is the least important consideration because the admin cluster doesn't host any user workloads. If your admin cluster has a problem, your application workloads continue to run without interruption.



The following sections use these categories of core functionality to describe the impact of specific types of failure scenarios.

## Failure modes

The following types of failures can affect the performance of Google Distributed Cloud clusters.

### ESXi host failure

In this failure scenario, an [ESXi host](https://www.vmware.com/products/esxi-and-esx.html) that runs virtual machine (VM) instances hosting Kubernetes nodes might stop functioning or become network partitioned.

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption** | Possible disruption and automatic recovery | Possible disruption and automatic recovery | Disruption and automatic recovery | Disruption and automatic recovery  
**Explanation** | The Pods that run on the VMs hosted by the failed host are disrupted, and are automatically rescheduled onto other healthy VMs. If user applications have spare workload capacity and are spread across multiple nodes, the disruption is not observable by clients that implement retries. | If the host failure affects the control-plane VM in a non-HA user cluster or more than one control-plane VM in an HA user cluster, there is disruption. | If the host failure affects the control-plane VM or the worker VMs in the admin cluster, there is disruption. | If the host failure affects the control-plane VM in the admin cluster, there is disruption.  
**Recovery** | vSphere HA automatically restarts the VMs on healthy hosts. | vSphere HA automatically restarts the VMs on healthy hosts. | vSphere HA automatically restarts the VMs on healthy hosts. | vSphere HA automatically restarts the VMs on healthy hosts.  
**Prevention** | Deploy workloads in an HA way to minimize the possibility of disruption. | Use HA user clusters to minimize the possibility of disruption. | — | —  
  
### VM failure

In this failure scenario, a VM might get deleted unexpectedly, a boot disk might become corrupted, or a VM might be compromised because of operating system issues.

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption** | Possible disruption and automatic recovery | Possible disruption and automatic recovery | Disruption and automatic/manual recovery | Disruption and manual recovery  
**Explanation** | The Pods that run on the failed worker VMs are disrupted, and they are automatically rescheduled onto other healthy VMs by Kubernetes. If user applications have spare workload capacity and are spread across multiple nodes, the disruption is not observable by clients that implement retries. | If the control-plane VM in a non-HA user cluster or more than one control-plane VM in an HA user cluster fails, there is disruption. | If the control-plane VM or the worker VMs in the admin cluster fail, there is disruption. | If the control-plane VM in the admin cluster fails, there is disruption.  
**Recovery** | The failed VM is automatically recovered if [node auto-repair](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair) is enabled in the user cluster. | The failed VM is automatically recovered if node auto-repair is enabled in the admin cluster. | The failed worker VM in the admin cluster is automatically recovered if node auto-repair is enabled in the admin cluster. To recover the admin cluster's control-plane VM, see [Repairing the admin cluster's control-plane VM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane). | To recover the admin cluster's control-plane VM, see [Repairing the admin cluster's control-plane VM](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/repair-admin-control-plane).  
**Prevention** | Deploy workloads in an HA way to minimize the possibility of disruption. | Use HA user clusters to minimize the possibility of disruption. | — | —  
  
### Storage failure

In this failure scenario, the content in a VMDK file might be corrupted due to ungraceful power down of a VM, or a datastore failure might cause [etcd](https://kubernetes.io/docs/concepts/overview/components/#etcd) data and [PersistentVolumes (PVs)](https://kubernetes.io/docs/concepts/storage/persistent-volumes/) to be lost.

#### etcd failure

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption** | No disruption | Possible disruption and Manual recovery | Disruption and manual recovery | Disruption and manual recovery  
**Explanation** | — | If the etcd store in a non-HA user cluster or more than one etcd replica in an HA user cluster fails, there is disruption. | If the etcd store in a non-HA user cluster or more than one etcd replica in an HA user cluster fails, there is disruption. If the etcd replica in an admin cluster fails, there is disruption. | If the etcd replica in an admin cluster fails, there is disruption.  
**Prevention** | — | Google Distributed Cloud provides a [manual process](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/replacing-etcd-replica-ha) to recover from the failure. | Google Distributed Cloud provides a manual process to recover from the failure. | Google Distributed Cloud provides a manual process to recover from the failure.  
  
#### User application PV failure

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
**Disruption** | Possible disruption | No disruption | No disruption | No disruption  
**Explanation** | The workloads using the failed PV are affected. Deploy workloads in the HA way to minimize the possibility of disruption. | — | — | —  
  
### Load balancer failure

In this failure scenario, a load balancer failure might affect user workloads that expose Services of type `LoadBalancer`.

| Run workloads | Manage workloads | Manage user clusters | Manage admin clusters  
---|---|---|---|---  
| Disruption and manual recovery  
**Explanation** |  There are a few seconds of disruption until the standby load balancer recovers the admin control plane VIP connection. The service disruption might be up to 2 seconds when using Seesaw, and [ up to 300 seconds when using F5](https://techdocs.f5.com/kb/en-us/products/big-ip_ltm/manuals/product/bigip-device-service-clustering-admin-11-5-0/8.html). The duration of failover disruption of MetalLB grows as number of load balancer nodes increases. With less than 5 nodes, the disruption is within 10 seconds.  
**Recovery** | Seesaw HA automatically detects the failure and fails over to using the backup instance. Google Distributed Cloud provides a manual process to recover from a Seesaw failure.  
  
## Recovering a broken cluster

The following sections describe how to recover a broken cluster.

### Recovery from ESXi host failures

Google Distributed Cloud relies on vSphere HA to provide recovery from an ESXi host failure. vSphere HA can continuously monitor ESXi hosts and automatically restart the VMs on other hosts when needed. This is transparent to Google Distributed Cloud users.

### Recovery from VM failures

VM failures can include the following:

  * Unexpected deletion of a VM.

  * VM boot disk corruption, like a boot disk that becomes read-only due to spam journal logs.

  * VM boot failure due to low performance disk or network setup issues, like a that VM can't boot because an IP address cannot be allocated to it.

  * Docker overlay file system corruption.

  * Loss of admin control-plane VM due to an upgrade failure.

  * Operating system issues.




Google Distributed Cloud provides an automatic recovery mechanism for the admin add-on nodes, user control planes, and user nodes. This node auto-repair feature can be enabled per admin cluster and user cluster.

The admin control-plane VM is special in the sense that it's not managed by a Kubernetes cluster, and its availability does not affect business continuity. For the recovery of admin control-plane VM failures, contact Cloud Customer Care.

### Recovery from storage failures

Some of the storage failures can be mitigated by vSphere HA and vSAN without affecting Google Distributed Cloud. However, certain storage failures might surface from the vSphere level causing data corruption or loss on various Google Distributed Cloud components.

The stateful information of a cluster and user workloads is stored in the following places:

  * **etcd** : Each cluster (admin cluster and user cluster) has an etcd database that stores the state (Kubernetes objects) of the cluster.
  * **PersistentVolumes** : Used by both system components and user workloads.



#### Recovery from etcd data corruption or loss

etcd is the database used by Kubernetes to store all cluster state, including user application manifests. The application lifecycle operations would stop functioning if the etcd database of the user cluster is corrupted or lost. The user cluster lifecycle operations would stop functioning if the etcd database of the admin cluster is corrupted or lost.

etcd doesn't provide a reliable built-in mechanism for detecting data corruption. You need to look at the logs of the etcd Pods if you suspect that the etcd data is corrupted or lost.

A pending/error/crash-looping etcd Pod doesn't always mean that the etcd data is corrupted or lost. It could be due to the errors on the VMs that host the etcd Pods. You should perform the following etcd recovery only for data corruption or loss.

To be able to recover (to a recent cluster state) from etcd data corruption or loss, the etcd data must be backed up after any lifecycle operation in the cluster (for example, creating, updating, or upgrading). To back up the etcd data, see [Backing up an admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-admin-cluster#backing_up_an_admin_cluster) and [Backing up a user cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-user-cluster#user_backup).

Restoring etcd data takes the cluster into a previous state. If a backup is taken before an application is deployed and then that backup is used to restore the cluster, the recently deployed application won't be running in the restored cluster. For example, if you use the etcd snapshot of an admin cluster that's snapshotted before creating a user cluster, then the restored admin cluster has the user cluster control plane removed. Therefore, we recommend that you back up the cluster after each critical cluster operation.

The etcd data corruption or loss failure can happen in the following scenarios:

  * **A single node of a three-node etcd cluster (HA user cluster) is permanently broken due to data corruption or loss.** In this case, only a single node is broken and the etcd quorum still exists. This scenario might happen in an HA cluster, where the data of one of the etcd replicas is corrupted or lost. The problem can be fixed without any data loss by replacing the failed etcd replica with a new one in the clean state. For more information, see [Replacing a failed etcd replica](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/replacing-etcd-replica-ha).

  * **Two nodes of a three-node etcd cluster (HA user cluster) are permanently broken due to data corruption or loss.** The quorum is lost, so replacing the failed etcd replicas with new ones doesn't help. The cluster state must be restored from backup data. For more information, see [Restoring a user cluster from a backup (HA)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-user-cluster#ha_user_restore).

  * **A single-node etcd cluster (admin cluster or non-HA user cluster) is permanently broken due to data corruption or loss.** The quorum is lost, so you must create a new cluster from the backup. For more information, see [Restoring a user cluster from a backup (non-HA)](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/back-up-user-cluster#user_restore).




#### Recovery from user application PV corruption or loss

You can use certain partner storage solutions to back up and restore user application PersistentVolumes. For the list of storage partners that have been qualified for Google Distributed Cloud, see [GDC Ready Storage Partners](https://docs.cloud.google.com/kubernetes-engine/enterprise/docs/resources/partner-storage).

### Recovery from load balancer failures

For bundled Seesaw load balancer, you can recover from failures by recreating the load balancer. To recreate the load balancer, upgrade Seesaw to the same version as shown in the version 1.16 documentation [Upgrading the load balancer for your admin cluster](https://docs.cloud.google.com/anthos/clusters/docs/on-prem/1.16/how-to/bundled-load-balance#upgrade-load-balancer).

In the case of admin cluster load balancer failures, the control plane might be out of reach. Run the upgrade on the admin control-plane VM where there is control plane access.

For integrated load balancers (F5), contact [F5 Support](https://www.f5.com/services/support).

For bundled MetalLB load balancer, it uses cluster nodes as load balancers. Automatic node repair is not triggered on load balancer issues. You can follow the [manual process](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/node-auto-repair#manual_node_repair) to repair the node.

## What's next

If you need additional assistance, reach out to [Cloud Customer Care](https://cloud.google.com/support-hub). 

You can also see [Getting support](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support) for more information about support resources, including the following:

  * [Requirements](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_requirements) for opening a support case.
  * [Tools](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#support_tools) to help you troubleshoot, such as logs and metrics.
  * Supported [components](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#whats_supported), [versions](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#version-support), and [features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/getting-support#supported_features) of Google Distributed Cloud for VMware (software only).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
