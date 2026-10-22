---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery/
title: High availability and disaster recovery \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:46.221819+00:00
---

# High availability and disaster recovery  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/high-availability-disaster-recovery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  High availability and disaster recovery Stay organized with collections  Save and categorize content based on your preferences. 

This page describes high availability options in Google Distributed Cloud (software only) for VMware.

## Core functionality

[ ![Architecture with highly-available user clusters](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/architecture_ha_09302019.png)](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/architecture_ha_09302019.png) Architecture with highly-available user clusters (Click to enlarge)

A software-only installation of Google Distributed Cloud for VMware includes an admin cluster and one or more user clusters.

The admin cluster manages the lifecycle of the user clusters, including user cluster creation, updates, upgrades, and deletion. In the admin cluster, the admin master manages the admin worker nodes, which include user masters (nodes running the control plane of the managed user clusters) and addon nodes (nodes running the addon components supporting the admin cluster's functionality).

For each user cluster, the admin cluster has one non-HA node or three HA nodes that run the control plane. The control plane includes the Kubernetes API server, the Kubernetes scheduler, the Kubernetes controller manager, and several critical controllers for the user cluster.

The user cluster's control plane availability is critical to workload operations such as workload creation, scaling up and down, and termination. In other words, a control plane outage does not interfere with the running workloads, but the existing workloads lose management capabilities from the Kubernetes API server if its control plane is absent.

Containerized workloads and services are deployed in the user cluster worker nodes. Any single worker node should not be critical to application availability as long as the application is deployed with redundant pods scheduled across multiple worker nodes.

## Enabling high availability

vSphere and Google Distributed Cloud provide a number of features that contribute to high availability (HA).

### vSphere HA and vMotion

We recommend enabling the following two features in the vCenter cluster that hosts your Google Distributed Cloud clusters:

  * [vCenter High Availability (HA)](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-availability/vcenter-server-high-availability.html)
  * [vMotion](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vcenter-and-host-management/migrating-virtual-machines/migration-with-vmotion/host-configuration-for-vmotion.html)



These features enhance availability and recovery in case an ESXi host fails.

vCenter HA uses multiple ESXi hosts configured as a cluster to provide rapid recovery from outages and cost-effective HA for applications running in virtual machines. We recommend that you provision your vCenter cluster with extra hosts and [enable vSphere HA Host Monitoring](https://techdocs.broadcom.com/us/en/vmware-cis/vsphere/vsphere/9-1/vsphere-availability/creating-and-using-vsphere-ha-clusters/creating-a-vsphere-ha-cluster/create-vsphere-ha-cluster.html) with `Host Failure Response` set to `Restart VMs`. Your VMs can then be automatically restarted on other available hosts in case of an ESXi host failure.

vMotion allows zero-downtime live migration of VMs from one ESXi host to another. For planned host maintenance, you can use vMotion live migration to avoid application downtime entirely and ensure business continuity.

**Note:** Storage vMotion is not supported. Refer to [vSphere Functionality Supported by vSphere Container Storage Plug-in](https://docs.vmware.com/en/VMware-vSphere-Container-Storage-Plug-in/2.0/vmware-vsphere-csp-getting-started/GUID-5B7955AA-E720-4C73-8330-1C34A0B054B3.html) Note: Don't enable vSphere Storage DRS because it's incompatible with Google Distributed Cloud.

### Admin cluster

Google Distributed Cloud supports creating high-availability (HA) admin clusters. A HA admin cluster has three nodes that run control-plane components. For information on requirements and limitations, see [High-availability admin cluster](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/create-admin-cluster#high-availability_admin_cluster).

Note that unavailability of the admin cluster control plane doesn't affect existing user cluster functionality or any workloads running in user clusters.

There are two add-on nodes in an admin cluster. If one is down, the other one can still serve the admin cluster operations. For redundancy, Google Distributed Cloud spreads critical add-on Services, such as `kube-dns`, across both of the add-on nodes.

If you set `antiAffinityGroups.enabled` to `true` in the admin cluster configuration file, Google Distributed Cloud automatically creates [vSphere DRS](https://www.vmware.com/products/vsphere/drs-dpm.html) anti-affinity rules for the add-on nodes, which causes them to be spread across two physical hosts for HA.

### User cluster

You can enable HA for a user cluster by setting `masterNode.replicas` to `3` in the user cluster configuration file. If the user cluster has [Controlplane V2](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/user-cluster-configuration-file-latest#enablecontrolplanev2-field) enabled (recommended), the 3 control plane nodes run in the user cluster. Legacy HA user clusters that don't have Controlplane V2 enabled run the three control plane nodes in the admin cluster. Each control plane node also runs an etcd replica. The user cluster continues to work as long as there is one control plane running and an etcd quorum. An etcd quorum requires that two of the three etcd replicas are functioning.

If you set `antiAffinityGroups.enabled` to `true` in the admin cluster configuration file, Google Distributed Cloud automatically creates vSphere DRS anti-affinity rules for the three nodes that run the user cluster control plane. This causes those VMs to be spread across three physical hosts.

Google Distributed Cloud also creates vSphere DRS anti-affinity rules for the worker nodes in your user cluster, which causes those nodes to be spread across at least three physical hosts. Multiple DRS anti-affinity rules are used per user cluster node-pool based on the number of nodes. This ensures that the worker nodes can find hosts to run on, even when the number of hosts is less than the number of VMs in the user cluster node-pool. We recommend that you include extra physical hosts in your vCenter cluster. Also configure DRS to be fully automated so that in case a host becomes unavailable, DRS can automatically restart VMs on other available hosts without violating the VMs' anti-affinity rules.

Google Distributed Cloud maintains a special node label, `onprem.gke.io/failure-domain-name`, whose value is set to the underlying ESXi host name. User applications that want high availability can set up `podAntiAffinity` rules with this label as the `topologyKey` to ensure that their application Pods are spread across different VMs as well as physical hosts. You can also configure multiple node pools for a user cluster with different datastores and special node labels. Similarly, you can set up `podAntiAffinity` rules with that special node label as the `topologyKey` to achieve higher availability upon datastore failures.

To have HA for user workloads, ensure that the user cluster has a sufficient number of replicas under `nodePools.replicas`, which ensures the desired number of user cluster worker nodes in running condition.

You can use separate datastores for admin clusters and user clusters to isolate their failures.

### Load balancer

There are two types of load balancers that you can use for high availability.

#### Bundled MetalLB load balancer

For the [bundled MetalLB load balancer](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/bundled-load-balance-metallb), you achieve HA by having more than one node with `enableLoadBalancer: true`.

MetalLB distributes services onto the load balancer nodes but for a single service, there is only one leader node handling all traffic for that service.

During the cluster upgrade, there is some downtime when the load balancer nodes are upgraded. The duration of failover disruption of MetalLB grows as the number of load balancer nodes increases. With less than 5 nodes, the disruption is within 10 seconds.

#### Manual load balancing

With [manual load balancing](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/manual-load-balance), you configure Google Distributed Cloud to use a load balancer of your choice, such as F5 BIG-IP or Citrix. You configure high availability on your load balancer, not in Google Distributed Cloud.

## Using multiple clusters for disaster recovery

Deploying applications in multiple clusters across multiple vCenters servers can provide higher global availability and limit the blast radius during outages.

This setup uses the existing cluster in the secondary data center for disaster recovery rather than setting up a new cluster. Following is a high-level summary to achieve this:

  * Create another admin cluster and user cluster in the secondary data center. In this multi-cluster architecture, we require users to have two admin clusters in each data center, and each admin cluster runs a user cluster.

  * The secondary user cluster has a minimal number of worker nodes (three) and is a hot standby (always running).

  * Application deployments can be replicated across the two vCenters by using Config Sync, or the preferred approach is to use an existing application DevOps (CI/CD, Spinnaker) toolchain.

  * In the event of a disaster, the user cluster can be resized to the number of nodes.

  * Additionally, a DNS switchover is required to route traffic between the clusters to the secondary data center.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
