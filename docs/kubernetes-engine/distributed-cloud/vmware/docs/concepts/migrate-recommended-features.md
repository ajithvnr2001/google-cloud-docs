---
url: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features/
title: Plan cluster migration to recommended features \u00a0|\u00a0 Google Distributed Cloud software only for VMware \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:15.590497+00:00
---

# Plan cluster migration to recommended features  |  Google Distributed Cloud software only for VMware  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/migrate-recommended-features/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Google Distributed Cloud ](https://docs.cloud.google.com/distributed-cloud)
  * [ Documentation ](https://docs.cloud.google.com/kubernetes-engine/enterprise/clusters/docs)
  * [ GDC for VMware ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/overview)



Send feedback 

#  Plan cluster migration to recommended features Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

Google Distributed Cloud is based on Kubernetes and many other related technologies, which are continuously being updated and improved to provide better scalability, performance, security, and integration capabilities. Accordingly, Google Distributed Cloud is constantly adapting and improving.

In version 1.30, the changes and updates have reached a point where we strongly recommend that you migrate legacy deployments to take advantage of significant improvements. This page describes the benefits of migrating from outdated features to the latest recommended features.

You have the following options for each feature area:

**Feature area** | **Recommended options** | **Original options**  
---|---|---  
Container Network Interface (CNI) | 

  * Dataplane V2  
(`enableDataplaneV2: true`)

| 

  * Dataplane V1 (Calico)  
(`enableDataplaneV2: false`)

  
Load balancer | 

  * `ManualLB` (works with F5 Big IP agents)  
(`loadBalancer.kind: "ManualLB"`)
  * MetalLB  
(`loadBalancer.kind: "MetalLB"`)

| 

  * integrated F5 Big IP1  
(`loadBalancer.kind: "F5BigIP"`)
  * Seesaw  
(`loadBalancer.kind: "Seesaw"`)

  
Admin cluster control plane | 

  * High availability (HA) admin cluster  
(`adminMaster.replicas: 3`)

| 

  * Non-HA admin cluster  
(`adminMaster.replicas: 1`)

  
User cluster control plane | 

  * Controlplane V2  
(`enableControlplaneV2: true`)

| 

  * Kubeception user cluster  
(`enableControlplaneV2: false`)

  
  
**1** _Integrated F5 BIG-IP_ refers to `loadBalancer.kind: "F5BigIP"` and related settings in the `loadBalancer.f5BigIP` section in your cluster configuration file.

The following tables show the support matrix for these features in admin and user clusters:

Cluster type | Outdated feature | Add for new cluster | Allow for cluster upgrade | Migration to new feature  
---|---|---|---|---  
**Version 1.32 and higher**  
Admin | Non-HA | No | No | N/A  
Seesaw | No | No | N/A  
Integrated F5 Big IP | No | No | N/A  
User | Kubeception | No | No | N/A  
Seesaw | No | No | N/A  
Integrated F5 Big IP | No | No | N/A  
Dataplane V1 | No | No | N/A  
**Version 1.30 and 1.31**  
Admin | Non-HA | No | Yes | Yes  
Seesaw | No | Yes | Yes  
Integrated F5 Big IP | No | Yes | Yes  
User | Kubeception | No | Yes | Yes  
Seesaw | No | Yes | Yes  
Integrated F5 Big IP | No | Yes | Yes  
Dataplane V1 | No | Yes | Yes  
**Version 1.29**  
Admin | Non-HA | No | Yes | Yes ([Preview](https://cloud.google.com/products/#product-launch-stages))  
Seesaw | No | Yes | Yes  
Integrated F5 Big IP | Yes | Yes | Yes ([Preview](https://cloud.google.com/products/#product-launch-stages))  
User | Kubeception | Yes | Yes | Yes ([Preview](https://cloud.google.com/products/#product-launch-stages))  
Seesaw | Yes | Yes | Yes  
Integrated F5 Big IP | Yes | Yes | Yes ([Preview](https://cloud.google.com/products/#product-launch-stages))  
Dataplane V1 | Yes | Yes | No  
**Version 1.28**  
Admin | Non-HA | No | Yes | No  
Seesaw | No | Yes | Yes  
Integrated F5 Big IP | Yes | Yes | No  
User | Kubeception | Yes | Yes | No  
Seesaw | Yes | Yes | Yes  
Integrated F5 Big IP | Yes | Yes | No  
Dataplane V1 | Yes | Yes | No  
  
**Key points** :

  * Starting with version 1.30, all migration solutions are available to migrate clusters to their recommended alternatives.
  * When creating new clusters, here are the versions where original features aren't allowed:

    * Admin clusters:

      * Non-HA control plane: 1.28 and higher
      * Seesaw load balancing: 1.28 and higher
      * Integrated F5 Big IP: 1.30 and higher
    * User clusters:

      * Kubeception: 1.30 and higher
      * Seesaw: 1.30 and higher
      * Integrated F5 Big IP: 1.30 and higher
      * Dataplane V1: 1.30 and higher
  * You can still upgrade existing clusters with the original features.




## Migrate user clusters to Dataplane V2

You can choose a Container Network Interface (CNI) that offers container networking features, either [Calico](https://github.com/projectcalico/calico) or [Dataplane V2](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/dataplane-v2). Dataplane V2, Google's CNI implementation, is based on [Cilium](https://github.com/cilium/cilium) and is used in both Google Kubernetes Engine (GKE) and Google Distributed Cloud.

Dataplane V2 provides an optimized design and efficient resource utilization, leading to improved network performance and better scalability, particularly for large clusters or environments with high network traffic demands. We strongly recommend that you migrate clusters to Dataplane V2 for the latest features, networking innovations, and capabilities.

Starting with version 1.30, Dataplane V2 is the only CNI option for creating new clusters.

The transition from Calico to Dataplane V2 requires planning and coordination, but it's designed to involve no downtime for existing workloads. By proactively migrating to Dataplane V2, you can benefit from:

  * **Enhanced Performance and Scalability:** Dataplane V2's optimized design and efficient resource utilization can lead to improved network performance and better scalability, particularly in large clusters or environments with high network traffic demands. This is due to the use of EBPF instead of IPTables, which lets the cluster scale using BPF maps.

  * **Simplified Management and Support:** Standardizing on Dataplane V2 across Google Distributed Cloud and GKE can simplify cluster management and troubleshooting, as you can rely on a consistent set of tools and documentation.

  * **Advanced Networking Features** : [EgressNAT](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/egress-nat-gateway) and other advanced networking features are only supported on Dataplane V2. Any future networking requests will be implemented in the Dataplane V2 layer.


| Before migration | After migration  
---|---|---  
kube-proxy | Required and automatically deployed | Not required and not deployed  
Routing | kube-proxy + iptables | eBPF  
  
Remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation from both the `OnPremUserCluster` custom resource and the `OnPremAdminCluster` custom resource (if your admin cluster was migrated from Calico during the upgrade from version 1.29 to 1.30) after you verify that the migration from Calico to Dataplane V2 is complete and you don't need to roll back to Calico. Removing this annotation before you scale or upgrade the cluster lets the cluster controller permanently delete the dormant `calico-node` and `calico-route-daemon` DaemonSets. You don't need to perform this step for clusters that were created with Dataplane V2 enabled. For more information, see [Remove dormant Calico DaemonSets](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features#remove-dormant-calico-daemonsets).

## Migrate load balancer type

The recommended load balancer types (`loadBalancer.kind`) are `"ManualLB"` and `"MetalLB"`. Use `"ManualLB"` if you have a third-party load balancer such as F5 BIG-IP or Citrix. Use `"MetalLB"` for our bundled load balancing solution using the [MetalLB load balancer](https://metallb.universe.tf/).

Starting with version 1.30, these are the only options for creating new clusters. For existing clusters that use the integrated F5 Big IP or the bundled Seesaw load balancer, we provide migration guides to migrate the `"F5BigIP"` configuration settings to `"ManualLB"`, and to migrate the bundled load balancer from Seesaw to MetalLB.

### Migrate configuration settings for your F5 BIG-IP load balancer

Plan to migrate any clusters that use the integrated F5 Big IP to `ManualLB`. The integrated F5 Big IP uses F5 BIG-IP with load balancer agents, which consist of the following two controllers:

  * F5 Controller (`pod prefix: load-balancer-f5`): reconciles LoadBalancer type Kubernetes Services into [F5 Common Controller Core Library (CCCL) ConfigMap](https://community.f5.com/kb/technicalarticles/introduction-to-f5-common-controller-core-library-cccl/281882) format.
  * F5 BIG-IP CIS Controller v1.14 (`pod prefix: k8s-bigip-ctlr-deployment`): translates ConfigMaps into F5 load balancer configurations.



The original integrated F5 Big IP has the following limitations:

  * **Limited Expressiveness** : The integrated F5 Big IP restricts the full potential of the F5 BIG-IP by limiting the expressiveness of the Service API. This can prevent you from configuring the BIG-IP controller to your specific needs or leveraging advanced F5 features that might be crucial for your application.
  * **Legacy Component** : The current implementation relies on older technologies like the CCCL ConfigMap API and 1.x CIS. These legacy components might not be compatible with the latest advancements in F5's offerings, potentially leading to missed opportunities for performance improvements and security enhancements.



The changes after migrating from the integrated F5 BIG-IP to `ManualLB` include:

| Before migration | After migration  
---|---|---  
F5 agents components | 

  * F5 Controller
  * OSS CIS Controller

| 

  * F5 Controller (no change)
  * OSS CIS Controller (no change)

  
F5 component version upgrade |  You must upgrade clusters to upgrade F5 components. Available component versions are limited as previously explained.  |  You can upgrade F5 component versions as needed.   
Service creation | Handled by F5 agents | Handled by F5 agents (no change)  
**Note:** After migration, you can continue to create Services the same way because the F5 agents still will be running as workloads in your cluster. The only difference is that after migration, you manage the lifecycle of the F5 agents.

### Migrate from Seesaw to MetalLB

MetalLB provides the following advantages compared with Seesaw:

  * **Simplified management and reduced resources** : Unlike Seesaw, MetalLB runs directly on cluster nodes, allowing for dynamic use of cluster resources for load balancing.
  * **Automatic IP assignment** : The MetalLB controller does IP address management for Services, so you don't have to manually choose an IP address for each Service.
  * **Load distribution among LB nodes** : Active instances of MetalLB for different Services can run on different nodes.
  * **Enhanced features and future-proofing** : MetalLB's active development and integration with the broader Kubernetes ecosystem makes it a more future-proof solution compared to Seesaw. Using MetalLB ensures that you can take advantage of the latest advancements in load balancing technology.

| Before migration | After migration  
---|---|---  
LB nodes | Extra Seesaw VMs (outside of cluster) | In-cluster LB nodes with customer choices  
Client IP Preservation | Can be achieved via `externalTrafficPolicy: Local` | Can be achieved via DataplaneV2 DSR mode  
Service creation | Manually specified Service IP | Auto-assigned Service IP from address pool  
  
## Migrate user clusters to Controlplane V2 and admin clusters to HA

The recommended control plane for user clusters is Controlplane V2. With Controlplane V2, the control plane runs on one or more nodes in the user cluster itself. With the legacy control plane, referred to as _kubeception_ , the control plane for a user cluster runs in an admin cluster. To create a high-availability (HA) admin cluster, your user clusters must have Controlplane V2 enabled.

As of version 1.30, new user clusters are required to have Controlplane V2 enabled, and new admin clusters will be HA. Upgrades of user clusters with the legacy control plane are still supported, as are upgrades of non-HA admin clusters.

### Migrate user clusters to Controlplane V2

Historically, user clusters have used kubeception. Version 1.13 introduced Controlplane V2 as a preview feature, which transitioned to GA in version 1.14. Since version 1.15, Controlplane V2 has been the default option for creating user clusters, and Controlplane V2 is the only option in version 1.30.

Compared with kubeception, the benefits of Controlplane V2 include:

  * **Architectural consistency** : Admin clusters and user clusters use the same architecture.
  * **Failure isolation:** An admin cluster failure does not affect user clusters.
  * **Operational separation:** An admin cluster upgrade doesn't cause downtime for user clusters.
  * **Deployment separation:** You can put the admin and user clusters in different topology domains or multiple locations. For example, in an edge computing deployment model, a user cluster might be in a different location than the admin cluster.



During the migration, there's zero downtime for the existing user cluster workloads. Depending on your underlying vSphere environment, the control plane will experience minimal downtime during the switchover to Controlplane V2. The migration process does the following:

  * Creates a new control plane in the user cluster.
  * Copies the etcd data from the old control plane.
  * Transitions the existing node pool nodes (also called worker nodes) to the new control plane.

| Before migration | After migration  
---|---|---  
Control Plane Kubernetes Node Objects | Admin cluster Node | User cluster Node  
Kubernetes Control Plane Pods | Admin cluster Statefulsets/Deployments (user cluster namespace) | User cluster [static pods](https://kubernetes.io/docs/tasks/configure-pod-container/static-pod/) (kube-system namespace)  
Other Control Plane Pods | Admin cluster Statefulsets/Deployments (user cluster namespace) | User cluster Statefulsets/Deployments (kube-system namespace)  
Control Plane VIP | Admin cluster Load Balancer Service | [keepalived](http://keepalived.readthedocs.io) \+ [haproxy](http://www.haproxy.org/) (user cluster static pods)  
Etcd Data | Admin cluster Persistent Volume | Data disk  
Control Plane Machine IP Management | IPAM or DHCP | IPAM  
Control Plane Network | Admin cluster VLAN | User cluster VLAN  
  
### Migrate to an HA admin cluster

Historically, the admin cluster could only run a single control-plane node, creating an inherent risk of a single point of failure. In addition to the one control-plane node, Non-HA admin clusters also have two add-on nodes. An HA admin cluster has three control-plane nodes with no add-on nodes, so the number of VMs that a new admin cluster requires hasn't changed, but availability is significantly improved. Starting with version 1.16, you can use a high availability (HA) admin cluster, which became the only option for new cluster creation in version 1.28.

Migrating to an HA admin cluster provides the following benefits:

  * **Enhanced reliability and uptime:** The HA configuration eliminates the single point of failure, enabling the admin cluster to remain operational even if one of the control-plane nodes experiences an issue.
  * **Enhanced upgrade and update experience** : All necessary steps to upgrade and update an admin cluster are now run in-cluster, instead of in a separate admin workstation. This makes sure upgrades and updates continue even if the initial session to the admin workstation might be interrupted.
  * **Reliable source of truth for cluster states** : Non-HA admin clusters rely on an out-of-band "checkpoint file" to store the admin cluster state. In contrast, the HA admin cluster stores the up-to-date cluster state inside the admin cluster itself, providing a more reliable source of truth for the cluster state.



You can choose to migrate your Non-HA admin cluster to an HA admin cluster, which involves no downtime for user workloads. The process causes minimal downtime and disruption to existing user clusters, primarily associated with the control plane switchover. The migration process does the following:

  * Creates a new HA control plane.
  * Restores the etcd data from the existing Non-HA cluster.
  * Transitions the user clusters to the new HA admin cluster.

| Before migration | After migration  
---|---|---  
Control-plane node replicas | 1 | 3  
Add-on nodes | 2 | 0  
Data disk size | 100GB * 1 | 25GB * 3  
Data disks path | Set by [vCenter.dataDisk](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-1.29#vcenter-datadisk-field) in the admin cluster configuration file | Auto generated under the directory: `/anthos/[ADMIN_CLUSTER_NAME]/default/[MACHINE_NAME]-data.vmdk`  
Control Plane VIP | Set by [loadBalancer.kind](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-1.29#loadbalancerkind) in the admin cluster configuration file | keepalived + haproxy  
Allocation of IP addresses for admin cluster control-plane nodes | DHCP or static, depending on [network.ipMode.type](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/admin-cluster-configuration-file-1.29#network-ipmode-type-field) | 3 static IP addresses  
  
## Group load balancer and control plane migrations

Typically, when updating clusters, we recommend that you [update only one feature or setting at a time](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/updating-general#update_one_thing_at_a_time). In version 1.30 and higher, however, you can group the configuration changes to migration for both your load balancer and control plane, then update the cluster just once to make both changes.

If you have user clusters using an old CNI, you first need to migrate to DataPlane V2. After that, you can group the migration for the load balancer and control plane. Grouping the migration provides the following benefits:

  * A simpler process: If you need to migrate both a control plane and load balancer, typically you only update the cluster once. And you don't need to decide which features you need to migrate first.
  * Reduce overall downtime: Certain migrations involve control plane downtime, so grouping these migrations into one update operation reduces overall downtime compared to doing sequential individual updates.



The process varies depending on the cluster configurations. Overall, perform the migration for each cluster as described in the following steps:

  1. Migrate each user cluster to use the recommended CNI, Dataplane V2.

     1. Make the configuration changes and update the user cluster to trigger a migration of the user cluster from the old CNI, Calico, to Dataplane V2.

**Note:** This step isn't needed for the admin cluster. When you upgrade the admin cluster to version 1.30, the cluster is automatically migrated to Dataplane V2.
     2. After you verify that you completed the Dataplane V2 migration and you don't need to roll back to Calico, remove the `features.onprem.cluster.gke.io/dpv2-migration` annotation from the `OnPremUserCluster` custom resource (and from `OnPremAdminCluster` if your admin cluster was migrated from Calico during the upgrade from version 1.29 to 1.30). Removing this annotation before you scale or upgrade the cluster lets the cluster controller permanently delete the dormant `calico-node` and `calico-route-daemon` DaemonSets. For instructions, see [Remove dormant Calico DaemonSets](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features#remove-dormant-calico-daemonsets).

  2. Migrate each user cluster from the old load balancer (LB) and old control plane (CP) to use the recommended load balancer and Controlplane V2.

     1. Make configuration changes to use the recommended load balancer (`MetalLB` or `ManualLB`).
     2. Make configuration changes to enable Controlplane V2.
     3. Update the user cluster to migrate the load balancer and control plane.
  3. Migrate the admin cluster to use the recommended load balancer and to make the control plane highly available.

     1. Make configuration changes to use the recommended load balancer (`MetalLB` or `ManualLB`).
     2. Make configuration changes to migrate the admin cluster's control plane from Non-HA to HA.
     3. Update the admin cluster to migrate the load balancer and control plane.
  4. Perform optional cleanup steps, such as cleaning up the Non-HA control plane VM.




The following diagram illustrates the migration steps:

![Steps for migrating to recommended features](https://docs.cloud.google.com/static/kubernetes-engine/distributed-cloud/vmware/docs/images/migration-to-recommended-features.svg)

If your admin cluster and all of your user clusters are at version 1.30 or higher, you can use the group migration process. For detailed steps, see the following guides:

  * [Migrate user clusters to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-user-cluster-recommended-features)
  * [Migrate admin cluster to recommended features](https://docs.cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/how-to/migrate-admin-cluster-recommended-features)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
