---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters/
title: Manage cluster lifecycle changes to minimize disruption \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:00:33.691633+00:00
---

# Manage cluster lifecycle changes to minimize disruption  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Manage cluster lifecycle changes to minimize disruption Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how you and Google Kubernetes Engine (GKE) manage changes during the lifecycle of a cluster to maximize performance and availability while minimizing workload disruption.

This page is intended for platform administrators who want to plan and optimize their cluster environment to minimize disruption for their workloads. You can read this page either before or after learning how to perform the basic cluster management tasks described in [Managing clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/managing-clusters) and [Cluster administration overview](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-admin-overview).

## A managed platform and shared responsibility

GKE is a Google-managed implementation of the [Kubernetes](https://kubernetes.io/) open source container orchestration platform. As mentioned in [How GKE works](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview#how_works), a GKE cluster consists of a control plane, which includes management nodes running system components, and worker nodes, where you deploy workloads.

Creating an optimal cluster environment for your workloads to run, with maximum performance, availability, and minimal disruption, is a shared responsibility:

  * GKE's responsibility is to maintain a reliable, available, secure, and performant cluster environment. To do this, GKE manages the control plane, system components, and, for Autopilot mode, the worker nodes.
  * Your responsibility as a platform administrator is to configure your cluster and manage your workloads, including preparing them to handle disruption. With Standard mode, you also create and manage the worker nodes, which are grouped in node pools.



For more information, see [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility).

## How GKE manages changes during the lifecycle of a cluster

As an implementation of Kubernetes, a GKE cluster is a network of processes and systems acting together to maintain the optimal environment to run your workloads. To manage the cluster, GKE performs maintenance tasks, makes changes, initiates operations, updates components, and upgrades the version of the control plane and nodes.

Most of the day-to-day running of your application occurs quietly in the background, keeping your workloads running without disruption. Some critical changes, however, must be completed in ways that could temporarily disrupt your workloads, as described in the next section.

### Some cluster changes can be disruptive to workloads

While GKE strives to keep your workloads running seamlessly, some essential types of changes can require temporary disruptions to your workloads—primarily changes that restart the nodes running your workloads. Using GKE and Kubernetes features, you can specify when and how you want disruption to take place, so that when it does, your workloads can gracefully handle the changes.

The following sections explain what types of changes GKE makes to clusters, what type of disruption they cause, and how you can prepare.

## Upgrades and updates with GKE cluster lifecycle management

In GKE, cluster _upgrades_ and cluster _updates_ have related meanings.

In GKE, the term [_cluster upgrades_](https://docs.cloud.google.com/kubernetes-engine/upgrades)—or just _upgrades_ —refers to updating the Kubernetes version of the control plane (_control plane upgrades_) or nodes (_node upgrades_), or both. When using Standard clusters, node upgrades can also be referred to as _node pool upgrades_ because GKE uses a single operation to upgrade a node pool of nodes.

The term _cluster updates_ —or just _updates_ —is a more general term referring to any type of control plane or node changes, including updating their versions. GKE actively manages your cluster environment by performing upgrades, other types of updates, and necessary maintenance operations. These actions ensure your cluster remains performant, secure, and up-to-date with the latest features and bug fixes. GKE uses tools like [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) and [maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to minimize disruption during these processes.

### Planning for node update disruptions

Certain types of cluster changes—mostly changes to nodes—can cause disruption.

GKE uses [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) to update nodes—both Autopilot nodes or Standard cluster node pools—in a way that's optimized for your workload's needs. These strategies apply to version upgrades and also to some other types of node changes. The strategies allow GKE to minimize disruption while performing node updates, which are important for keeping clusters functional and performant.

**Best practice** : 

Use maintenance windows and exclusions to choose when some cluster maintenance does and doesn't occur, and, for Standard clusters, pick a node upgrade strategy that best fits your workload profile and resource constraints.

For both manual and automatically-initiated changes to nodes, GKE makes changes with the following general characteristics:

  * **Changes typically respect maintenance policies** : When GKE makes changes to the nodes, these changes generally [respect GKE maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#examples_of_automatic_maintenance). Some [exceptions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#gcp-maintenance) include host maintenance for certain types of nodes, such as those with GPUs and TPUs.

Consider the following if you initiate manual changes that require all the nodes in a node pool to be recreated:

    * For some changes, GKE respects maintenance policies and doesn't apply the change you submitted until there is maintenance availability. If GKE is waiting for maintenance availability, and the change is urgent, you can [manually apply](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-recreation-maintenance-windows) the changes to apply the new configuration immediately.
    * For other manual changes including [manual upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes), GKE doesn't respect maintenance policies. For these manual changes, ensure that your workloads are prepared for immediate disruption.
  * **Changes generally use node upgrade strategies** : When GKE applies most automatic or manually-initiated changes to nodes—including node updates other than version upgrades—GKE chooses a node upgrade strategy: [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge), [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy), or [autoscaled blue-green](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)). Autopilot always uses surge upgrades. Changes to Standard cluster node pools [typically use surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-surge-upgrades-are-used), except when you've configured blue-green or autoscaled blue-green upgrades and do [certain types of changes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-blue-green-upgrades-are-used). For more information about which strategy is configured for a node pool, see [Inspect the upgrade settings of a node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies#inspect-upgrade-settings).

  * **Changes require sufficient resources** : When GKE applies a change using a node upgrade strategy, this change requires a certain amount of resources depending on the strategy and its configuration. Your cluster's project must have enough resource quota, resource availability, and reservation capacity (for node pools with specific reservation affinity). For more information, see [Ensure resources for node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota).




For a detailed list of specific changes and their characteristics, see Types of changes to a GKE cluster in this page.

**Important:** Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

### Maximize workload availability by preparing for disruptive changes

To maximize the availability of your workloads running on a GKE cluster, we recommend that you take the actions described in the following sections:

#### Choose your cluster availability

If control plane availability is a priority, choose an Autopilot cluster or regional Standard cluster rather than a zonal Standard cluster. For more information, see [About cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).

#### Control upgrades using GKE tools

You can use the following tools to control when and how [GKE upgrades your cluster](https://docs.cloud.google.com/kubernetes-engine/upgrades), making it possible to implement the [best practices](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters):

  * [**Release channels**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels): Choose a release channel to get cluster versions with your chosen balance of feature availability and stability.
  * [**Maintenance windows**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows): Specify a recurring window of time when [certain types of GKE cluster maintenance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#examples_of_automatic_maintenance), such as upgrades, can occur.
  * [**Maintenance exclusions**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions): Prevent cluster maintenance from occurring for a specific time period.
  * [**Cluster disruption budgets**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget): customize the minimum time interval between specific types of cluster upgrades, including patch or minor upgrades.
  * [**Node upgrade strategies**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies): If using a Standard node pool, choose how your nodes are updated–surge, blue-green, or autoscaled blue-green ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) upgrades–to minimize disruption to your workloads. Additionally, [choose how many node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades) GKE automatically upgrades at the same time in a cluster.
  * [**Rollout sequencing**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing): Qualify upgrades in a pre-production environment before GKE upgrades your production clusters.
  * [**Manual upgrades**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster): Manually upgrade your cluster, and perform such actions as canceling, resuming, rolling back, and completing automatic or manual in-progress upgrades.



#### Manage and monitor your cluster

To manage potential disruption to your clusters, continuously perform the following tasks:

  * Monitor your cluster with [GKE's observability suite](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/observability).
  * Follow the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for announcements.
  * View [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications), such as when upgrades start or complete, when new versions are available, security bulletins, and end of support dates.
  * [Get visibility into cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist) to understand the state of upgrades for your clusters.
  * Check the [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule) for a best-case estimate of when minor versions are available for upgrades, and reach [the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle).
  * Use prescriptive guidance that [identifies potential optimization opportunities and explains how to optimize your cluster usage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders), including guidance for [feature and API deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations).



#### Prepare your workloads

Manage disruption by making your workloads as resilient to disruption as possible:

  * Run [replicas](https://kubernetes.io/docs/concepts/workloads/controllers/replicaset/) of your workloads to ensure redundancy and avoid a single point of failure.
  * [Specify a disruption budget for your application](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) using a [Pod Disruption Budget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#pod-disruption-budgets).
  * Set a [termination grace period](https://cloud.google.com/blog/products/gcp/kubernetes-best-practices-terminating-with-grace) of the right length for your workload to gracefully shut down.
  * If your workload is using GPUs or TPUs, follow the instructions to [manage GKE node disruptions for GPUs and TPUs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).
  * For stateful applications, which often need time to cleanly stop I/O and unmount from storage, follow the steps in [Ensure stateful workloads are disruption-ready](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-disruption-readiness).



For a general discussion of these topics, see the **Manage disruption** section of the [GKE best practices: Day 2 operations for business continuity](https://cloud.google.com/blog/products/containers-kubernetes/ensuring-reliability-and-uptime-for-your-gke-cluster) blog post.

## Types of changes to a GKE cluster

The following tables show the most common types of major changes to a cluster, including characteristics of these changes such as frequency and level of disruption.

### Types of upgrades

Review the following table to understand how upgrades can disrupt a cluster environment.

Change | Automatic or manually initiated | Respects maintenance policies | Frequency | Type of disruption | Level of disruption  
---|---|---|---|---|---  
Control plane upgrade | Automatic or manual |  Automatic upgrades respect maintenance policies until the end of support, except for extremely rare emergency fixes, as necessary. Manual upgrades aren't blocked by maintenance policies. |  Patch upgrades, as often as every week, depending on the release channel. Minor upgrades approximately every four months. For [Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended) clusters, minor upgrades only when the minor version nears the end of support. | Control plane |  For Autopilot and regional Standard clusters, the control plane remains available. For zonal Standard clusters, multiple minutes where you can't communicate with the control plane, meaning that you can't configure the cluster, nodes, and workloads during that time.  
Node upgrade | Automatic or manual |  Automatic upgrades respect maintenance policies until the end of support, except for extremely rare emergency fixes, as necessary. Manual upgrades aren't blocked by maintenance policies. |  Typically the same as the control plane upgrades. If your cluster isn't enrolled in a release channel and you disable node auto-upgrades, you're responsible for manually upgrading your cluster's node pools. | All nodes for Autopilot clusters, or one or more Standard cluster node pools. |  Nodes must be shut down to be recreated, Pods must be replaced. GKE uses surge upgrades for Autopilot, or the configured node upgrade strategy (surge, blue-green, or autoscaled blue-green ([Preview](https://docs.cloud.google.com/products#product-launch-stages))) for Standard clusters.  
  
### Manual changes that recreate the nodes using a node upgrade strategy and respecting maintenance policies

Review the following table to understand how these manual changes can disrupt a cluster environment. This list includes, amongst other changes, [manual changes that respect GKE maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-recreation-maintenance-windows).

Change | Automatic or manually initiated | Respects maintenance policies | Frequency | Type of disruption | Level of disruption  
---|---|---|---|---|---  
[Disabling the kubelet readonly port](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/disable-kubelet-readonly-port) | Manually initiated | Doesn't respect maintenance policies, immediately makes changes. | Once per change of this type. | All nodes in an Autopilot cluster  
All nodes in a Standard cluster node pool. | Nodes must be shut down to be recreated. Pods must be replaced. GKE immediately uses surge upgrades to recreate the nodes, regardless of any active maintenance policies. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Rotating the cluster credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation) | Automatic if [cluster credentials are expiring within 30 days](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#automatic-rotation), can also be manually initiated. | Does respect maintenance policies. However, GKE might override maintenance policies within 30 days of credential expiration. Within 30 days, GKE ignores maintenance availability for the first step, which is [starting the rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#initiating_the_rotation). Also, if you manually trigger specific operations after the first step, that operation doesn't respect maintenance policies. | Once per manual change of this type, or depends on [cluster credential lifetime](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#check_credential_lifetime) for automatic initiation. You can manually invoke operations for [specific steps](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#performing_a_credential_rotation) in the rotation process. | For some steps, the control plane. For other steps, all nodes for Autopilot clusters, all nodes in each Standard cluster node pool. |  When you [initiate the rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#initiating_the_rotation) and [complete the rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#completing_the_rotation), the level of disruption is the following:

  * For Autopilot and regional Standard clusters, the control plane remains available.
  * For zonal Standard clusters, both operations cause brief downtime, meaning multiple minutes where you can't communicate with the control plane to perform operations like configuring the cluster, nodes, and workloads.

When the [nodes are recreated](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation#recreate-nodes), the level of disruption is as follows:

  * Nodes must be shut down to be recreated, Pods must be replaced.
  * GKE uses surge upgrades to recreate the nodes. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.

**Warning:** If GKE can't [complete the rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation#completing_the_rotation) of the cluster credentials before the cluster credentials expire—because of maintenance availability and [related constraints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#unfinished-node-changes)—your cluster and workloads become unrecoverable.  
[Rotating the control plane's IP address](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation) | Manually initiated | Does respect maintenance policies, however if you manually trigger specific operations after the first step, that operation doesn't respect maintenance policies. | Once per manual change of this type. You can manually invoke operations for [specific steps](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation#performing_an_ip_rotation) in the rotation process. | For some steps, the control plane. For other steps, all nodes for Autopilot clusters, all nodes in each Standard cluster node pool. |  When you [initiate the rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation#initiate) and [complete the rotation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation#completing_the_rotation), the level of disruption is the following:

  * For Autopilot and regional Standard clusters, the control plane remains available.
  * For zonal Standard clusters, both operations cause brief downtime, meaning multiple minutes where you can't communicate with the control plane to perform operations like configuring the cluster, nodes, and workloads.

When the [nodes are recreated](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation#recreate-nodes), the level of disruption is as follows:

  * Nodes must be shut down to be recreated, Pods must be replaced.
  * GKE uses surge upgrades to recreate the nodes. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.

  
[Configuring shielded nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes) | Manually initiated |  Recreating the control plane doesn't respect maintenance policies, immediately makes the changes. Recreating the nodes does respect maintenance policies. | Once per change of this type |  The control plane is updated. After the control plane is updated, all nodes in each Standard cluster node pool must be recreated. |  When the control plane is recreated, the level of disruption is the following:

  * For Autopilot and regional Standard clusters, the control plane remains available.
  * For zonal Standard clusters, both operations cause brief downtime, meaning multiple minutes where you can't communicate with the control plane to perform operations like configuring the cluster, nodes, and workloads.

When the nodes are recreated, the level of disruption is as follows:

  * Nodes must be shut down to be recreated, Pods must be replaced.
  * GKE uses surge upgrades to recreate the nodes. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.

**Warning:** If your cluster doesn't have active maintenance availability when you initiate the change, the control plane will be recreated but the nodes won't yet be recreated. The delay between the two steps might cause [failed node registrations](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/node-registration) and disruption to your cluster.  
[Configuring network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy) | Manually initiated | Does respect maintenance policies | Once per change of this type | All nodes for Autopilot clusters, all nodes in each Standard cluster node pool. |  Nodes must be shut down to be recreated, Pods must be replaced. GKE uses surge upgrades to recreate the nodes. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Configuring intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility) | Manually initiated | Does respect maintenance policies | Once per change of this type | All nodes for Autopilot clusters, all nodes in each Standard cluster node pool. |  Nodes must be shut down to be recreated, Pods must be replaced. GKE uses surge upgrades to recreate the nodes. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Configuring NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache) | Manually initiated | Does respect maintenance policies | Once per change of this type | All nodes in the Standard cluster node pool being updated must be updated. |  Nodes must be shut down to be recreated, Pods must be replaced. GKE uses surge upgrades to recreate the nodes. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Enabling Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) | Manually initiated |  When updating at the cluster level, respects maintenance policies. When updating individual node pools, doesn't respect maintenance policies. | Once per change of this type |  If toggled at the node pool level, all nodes in the Standard cluster node pool. If toggled at the cluster level, nodes of any Standard cluster node pools where you haven't individually enabled or disabled the setting for the node pool. | GKE uses surge upgrades to recreate the nodes of a node pool. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
  
### Automatic maintenance that doesn't respect maintenance policies

Review the following table to understand how [automatic maintenance that doesn't respect maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#caveats) can disrupt a cluster environment.

Change | Automatic or manually initiated | Respects maintenance policies | Frequency | Type of disruption | Level of disruption  
---|---|---|---|---|---  
[Control plane repair or resize](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#repairs) | Automatic | Doesn't respect maintenance policies |  Control plane repair frequency is random but has no impact for Autopilot and regional Standard clusters. Control plane resize is infrequent, but increases in frequency with cluster scaling events, and also has no impact for Autopilot and regional Standard clusters. | Control plane |  For Autopilot and regional Standard clusters, the control plane remains available. For zonal Standard clusters, multiple minutes where you can't communicate with the control plane, meaning that you can't configure the cluster, nodes, and workloads during that time.  
[Host maintenance event](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#gcp-maintenance) | Automatic | Doesn't respect maintenance policies | Refer to [Maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) for approximate frequency. | One node |  For most types of nodes, minimal effect. Some nodes, including those with GPUs or TPUs, might experience greater disruption. For more information, see [Other Google Cloud maintenance.](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#gcp-maintenance)  
[Node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) | Automatic | Doesn't respect maintenance policies | Node auto-repair frequency is random. | One node | The node is restarted, so any Pods running on the node are disrupted.  
Reclaim [Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms) and [Preemptible VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms) | Automatic | Doesn't respect maintenance policies |  For preemptible VMs, at least once every 24 hours. For Spot VMs, when Compute Engine needs the resources elsewhere. | One node | See details about the [termination and graceful shutdown of Spot VMs](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/spot-vms#termination-graceful-shutdown), and the [termination and graceful shutdown of preemptible VMs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/preemptible-vms#graceful-shutdown).  
Maintenance of the Spanner-based [cluster state database](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#cluster-state-database) | Automatic | Doesn't respect maintenance policies | Events are random and have no impact on clusters or workloads. | None. The Spanner-based database runs separately from the cluster control plane and nodes in Google's infrastructure. | None. The Spanner-based database is replicated for all types of clusters and remains available during maintenance.  
  
### Manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies

Review the following table to understand how these manual changes can disrupt a cluster environment. This list includes changes from [when GKE uses surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-surge-upgrades-are-used) and [when GKE uses blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-blue-green-upgrades-are-used) that aren't included in the other section as they don't respect maintenance policies.

Change | Automatic or manually initiated | Respects maintenance policies | Frequency | Type of disruption | Level of disruption  
---|---|---|---|---|---  
[Changes to control plane log collection](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/view-logs) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | The control plane is updated. | When the control plane is recreated, the level of disruption is the following:

  * For Autopilot and regional Standard clusters, the control plane remains available.
  * For zonal Standard clusters, the control plane has downtime, meaning multiple minutes where you can't communicate with the control plane to perform operations like configuring the cluster, nodes, and workloads.

  
[Node pool label update](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-managing-labels#update-node-pool-labels) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool | GKE immediately uses surge upgrades to recreate the node pool when you update the node labels on an existing node pool, regardless of any active maintenance policies. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Vertically scaling the nodes by changing the node machine attributes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pools#change-machine-attributes) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool | GKE immediately uses surge upgrades to recreate the nodes on an existing node pool, regardless of any active maintenance policies. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Image type changes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-images#upgrading_an_existing_cluster) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool |  Nodes must be shut down to be recreated, Pods must be replaced. GKE uses the configured node upgrade strategy (surge, blue-green, or autoscaled blue-green ([Preview](https://docs.cloud.google.com/products#product-launch-stages))) for Standard clusters.  
[Add or replace storage pools in a Standard cluster node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/persistent-volumes/hyperdisk-storage-pools#when-updating-node-pool) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool |  Nodes must be shut down to be recreated, Pods must be replaced. GKE uses the configured node upgrade strategy (surge, blue-green, or autoscaled blue-green ([Preview](https://docs.cloud.google.com/products#product-launch-stages))) for Standard clusters.  
[Enabling Image streaming](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/image-streaming) | Manually initiated |  When updating at the cluster level, respects maintenance policies. When updating individual node pools, doesn't respect maintenance policies. | Once per change of this type |  If toggled at the node pool level, all nodes in the Standard cluster node pool. If toggled at the cluster level, nodes of any Standard cluster node pools where you haven't individually enabled or disabled the setting for the node pool. | GKE uses surge upgrades to recreate the nodes of a node pool. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Network performance configuration updates](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update#--network-performance-configs) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool |  Nodes must be shut down to be recreated, Pods must be replaced. GKE immediately uses surge upgrades to recreate the nodes on an existing node pool, regardless of any active maintenance policies. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Enabling gVNIC](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/using-gvnic#update_a_node_pool) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool |  Nodes must be shut down to be recreated, Pods must be replaced. GKE immediately uses surge upgrades to recreate the nodes on an existing node pool, regardless of any active maintenance policies. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Node system configuration changes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-system-config) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool |  Nodes must be shut down to be recreated, Pods must be replaced. GKE immediately uses surge upgrades to recreate the nodes on an existing node pool, regardless of any active maintenance policies. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
[Confidential nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/confidential-gke-nodes#on_an_existing_node_pool) | Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All nodes in a Standard cluster node pool |  Nodes must be shut down to be recreated, Pods must be replaced. GKE immediately uses surge upgrades to recreate the nodes on an existing node pool, regardless of any active maintenance policies. GKE uses surge upgrades regardless of whether a different node upgrade strategy, such as blue-green upgrades, is configured.  
  
### Changes that don't require recreating the nodes

Review the following table to understand which changes to the node configuration don't require recreating the nodes. These changes aren't disruptive, however disruption is still possible if the updated node configuration affects your workload.

Change | Automatic or manually initiated | Respects maintenance policies | Frequency | Type of disruption | Level of disruption  
---|---|---|---|---|---  
Update the following settings:

  * Any types of [tags](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/tags#resource-annotation-gke), including Tags (firewall), Tags (non-firewall), and network tags
  * [Kubernetes node labels and taints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/update-existing-nodepools), including [architecture taints](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment#configure-default-taint)
  * [Cluster autoscaler settings](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-autoscaler)
  * Node pool auto-upgrade [enablement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#enable) and [disablement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable)
  * Node auto-repair [enablement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#enable) and [disablement](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#disable)
  * [Node upgrade strategy settings](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies)

| Manually initiated | Doesn't respect maintenance policies, immediately makes the changes. | Once per change of this type | All relevant nodes are updated. | Pods don't have to be replaced because the node configuration is updated without recreating the nodes.  
  
## What's next

  * [GKE overview](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)
  * [GKE cluster architecture](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture)
  * [GKE shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility)
  * [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning)
  * [GKE Service Level Agreement](https://cloud.google.com/kubernetes-engine/sla)
  * [GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
