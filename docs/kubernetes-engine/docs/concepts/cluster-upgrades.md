---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades/
title: Standard cluster upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:48.826764+00:00
---

# Standard cluster upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Standard cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document discusses how automatic and manual upgrades work for Google Kubernetes Engine (GKE) Standard clusters, including links to more information about related tasks and settings. You can use this information to keep your clusters updated for stability and security with minimal disruptions to your workloads.

For a general overview of cluster upgrades, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades). For information on how cluster upgrades work specifically for Autopilot clusters, see [Autopilot cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot).

## How control plane and node pool upgrades work

This section discusses what happens in your cluster during automatic or manual upgrades. For auto-upgrades, GKE initiates the auto-upgrade. GKE observes automatic and manual upgrades across all GKE clusters, and intervenes if problems are observed.

To upgrade a cluster, GKE updates the version the control plane and nodes are running. Clusters are upgraded to either a newer minor version (for example, 1.24 to 1.25) or newer patch version (for example, 1.24.2-gke.100 to 1.24.5-gke.200). For more information, see [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

**Note:** A cluster's control plane and nodes don't necessarily run the same version at all times, however they must adhere to the [GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew). In this document, _cluster upgrade_ and _control plane upgrade_ are used interchangeably, and are differentiated from _node upgrades_. For more information about how versions work, see [Versioning](https://docs.cloud.google.com/kubernetes-engine/versioning).

If you enroll your cluster in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), nodes run the same version of GKE as the cluster, except during a brief period (typically a few days, depending on the current release) between completing the cluster's control plane upgrade and starting the node pool upgrade, or if the control plane was manually upgraded. Check the [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for more information.

### Control plane upgrades

This section discusses what to expect when GKE auto-upgrades your control plane or you [initiate a manual upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).

GKE cluster availability during control plane upgrades depends on the type of Standard cluster you run:

  * **[Zonal](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters) clusters** have only a single control plane. During the upgrade, your workloads continue to run, but you cannot deploy new workloads, modify existing workloads, or make other changes to the cluster's configuration until the upgrade is complete.

  * **[Regional](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters) clusters** have multiple replicas of the control plane, and only one replica is upgraded at a time, in an undefined order. During the upgrade, the cluster remains highly available, and each control plane replica is unavailable only while it is being upgraded.


**Note:** Cluster control planes are always [upgraded](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) on a regular basis, regardless of whether your cluster is enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) or not.

If you configure a [maintenance window or exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), the maintenance window or exclusion is honored for automatic upgrades, if possible.

#### Control plane upgrade methods

GKE uses the following methods when performing control plane upgrades:

  * **Automatic upgrades** : GKE performs automatic upgrades by using the following methods, depending on upgrade type:

    * **Patch version upgrades** : GKE uses a one-step upgrade, which upgrades your control plane directly to a later patch version.
    * **Minor version upgrades** : for upgrading to GKE minor version 1.33 or later, GKE uses a two-step process where you can validate the new minor version for a period of soak time, and roll back if needed. For more information, see [Two-step control plane minor upgrade with rollback safety](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#two-step-cp-upgrade). For upgrading to earlier versions, GKE uses the one-step upgrade process instead.
  * **Manual upgrades** : you can [upgrade the cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) depending on upgrade type:

    * **Patch version upgrades** : you can use a one-step upgrade.
    * **Minor version upgrades** : you can use either the one-step upgrade, or the two-step upgrade.



### Node pool upgrades

This section discusses what to expect when GKE auto-upgrades your node pool or you initiate a manual node pool upgrade. This information is relevant to both Standard node pools, and [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools).

By default, GKE automatically upgrades one node pool at a time in a cluster. To reduce the overall upgrade time for clusters with multiple node pools, you can [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades) ([Preview](https://cloud.google.com/products#product-launch-stages)), which lets GKE automatically upgrade multiple node pools simultaneously. Alternatively, you can manually upgrade one or more node pools in parallel. By default, nodes within a node pool are upgraded one at a time in an arbitrary order. In a [node pool spread across multiple zones](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#multiple-zones), upgrades take place zone-by-zone. Within a zone, the nodes will be upgraded in an undefined order.

With GKE Standard node pool upgrades, you can choose between the following node upgrade strategies:

  * Surge upgrades
  * Blue-green upgrades
  * Autoscaled blue-green upgrades ([Preview](https://cloud.google.com/products#product-launch-stages))



For each of these node upgrade strategies, you can tune the upgrade process based on the needs of your cluster environment. Autopilot-managed node pools in Standard clusters always use surge upgrades, and you can't modify the configuration of the strategy or its settings.

GKE honors [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) during automatic upgrades when possible. Manual upgrades bypass your configured maintenance windows and exclusions.

**Note:** Cluster Autoscaler scale-up events may still occur during a node pool upgrade. For a multi-zone node pool, a node may be created running the older node version if the zone's nodes have not yet been upgraded.

#### Disruptive upgrades for node pools that use accelerators and run AI/ML workloads

Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, we recommend that you perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

#### How nodes are upgraded

During a node pool upgrade, how the nodes are upgraded depends on the node pool upgrade strategy and [how you configure it](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-pool-upgrade-strategies), if possible. However, the basic steps remain consistent. To upgrade a node, GKE removes Pods from the node so that it can be upgraded.

When a node is upgraded, the following happens with the Pods:

  1. The node is cordoned so that Kubernetes does not schedule new Pods on it.
  2. The node is then drained, meaning that the Pods are removed. For surge upgrades, GKE respects the Pod's [PodDisruptionBudget](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) and [GracefulTerminationPeriod](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/#pod-termination) settings for up to one hour. With blue-green upgrades, this can be extended if you configure a longer soaking time.
  3. The control plane reschedules Pods managed by controllers onto other nodes. Pods that cannot be rescheduled stay in the Pending phase until they can be rescheduled.

**Note:** During the node drain process, Kubernetes ignores any Pods that aren't managed by a workload controller.Any configured `PodDisruptionBudget`, `terminationGracePeriodSeconds` values, and `preStop` hooks for these Pods aren't honored during the node drain. When GKE deletes the node, these Pods terminate immediately and aren't re-created on new nodes. To help ensure graceful termination during node upgrades, manage your Pods by using a workload controller.



The node pool upgrade process may take up to a few hours depending on the upgrade strategy, the number of nodes, and their workload configurations.

##### Considerations affecting node upgrade duration

Configurations that can cause a node upgrade to take longer to complete include:

  * A high value of [terminationGracePeriodSeconds](https://v1-30.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#podtemplatespec-v1-core) in a Pod's configuration.
  * A conservative [Pod Disruption Budget](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-disruption-budgets-work).
  * [Node affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity) interactions.
  * Attached [PersistentVolumes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).



#### Node upgrade strategies

GKE offers built-in configurable strategies which determine how the node pool is upgraded. For more information about types of changes that use a node upgrade strategy, see the following:

  * [When GKE uses surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-surge-upgrades-are-used)
  * [When GKE uses blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-blue-green-upgrades-are-used)
  * [When GKE uses autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#when-autoscaled-blue-green-upgrades-are-used)



##### Surge upgrades

By default, the [surge upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) is used for node pool upgrades. This strategy is always used for Autopilot-managed node pools. Surge upgrades use a rolling method to upgrade nodes. This strategy is best for applications that can handle incremental, non-disruptive changes. With this strategy, nodes are upgraded in a rolling window. For Standard node pools, you can change settings like how many nodes can be upgraded at once, and how disruptive the upgrades can be, finding the optimal balance of speed and disruption for your environment's needs.

##### Blue-green upgrades

An alternative approach for Standard node pools is [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy), where two sets of environments (the original and new environments) are maintained at once, making rolling back as straightforward as possible. Blue-green is more resource intensive and better for applications that are more sensitive to changes. With this strategy, workloads are gradually migrated from the original "blue" environment to the new "green" environment, and given soak time to validate them with the new configuration. If needed, the workloads can be quickly rolled back to the existing "blue" environment.

For more information about how the node upgrade strategies work, see [Node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).

##### Autoscaled Blue-green upgrades

[Autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy) ([Preview](https://cloud.google.com/products#product-launch-stages)) are a node upgrade strategy where workloads can run for longer, while you minimize cost from idle or underutilized nodes.

#### Resource requirements for node upgrade strategies

Surge upgrades create extra nodes if `maxSurge` is set to more than 0, and blue-green upgrades temporarily double the number of nodes in a node pool. This requires additional resources, which is subject to [ Compute Engine quota](https://docs.cloud.google.com/compute/quotas), [resource availability](https://docs.cloud.google.com/compute/resource-usage#quotas_and_resource_availability), and [reservation](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/consuming-reservations) capacity. If your node pool doesn't have sufficient resources, upgrades can take longer or fail.

For more information about how to ensure your project has enough resources for node upgrades, and what to do if your environment is resource-constrained, see [Ensure resources for node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota).

## Upgrading automatically

When you create a Standard cluster, by default, auto-upgrade is enabled on the cluster and its node pools.

GKE is responsible for [securing your cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/control-plane-security), and upgrades your clusters when a new GKE version is selected for auto-upgrade. Infrastructure security is high priority for GKE, and as such control planes are upgraded on a regular basis, and cannot be disabled. However, you can use maintenance windows and exclusions to temporarily suspend upgrades for control planes.

As part of the [GKE shared responsibility model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility), you are responsible for securing your nodes, containers, and Pods. Node auto-upgrade is enabled by default, and you can use maintenance windows and exclusions to control when an auto-upgrade can or can't occur. If you prevent node auto-upgrades, you are responsible for ensuring that the cluster's nodes run a version compatible with the control plane's version, and that the version adheres to the [GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew). Regardless of your cluster's settings, GKE performs [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).

A cluster's node pools can be no more than two minor versions behind the control plane version, to maintain compatibility with the cluster API. The node pool version also determines the versions of software packages installed on each node. It is recommended to keep node pools updated to the cluster version.

If you keep your cluster enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), nodes generally run the same version of GKE as the cluster itself, except during a brief period (typically a few days, depending on the current release) between completing the cluster's control plane upgrade and beginning to upgrade a given node pool. Check the [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for more information.

### How versions are selected for auto-upgrade

New GKE versions are released [regularly](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes), but a version is not selected for auto-upgrade right away. When a GKE version has accumulated enough cluster usage to prove stability over time, GKE selects it as an auto-upgrade target for clusters running a subset of earlier versions. To get auto-upgrade targets for a specific cluster, see [Get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).

New auto-upgrade targets are announced in the release notes. Until an available version is selected for auto-upgrade, you can upgrade to it manually. Occasionally, a version is selected for cluster auto-upgrade and node auto-upgrade during different weeks.

Soon after a new minor version becomes generally available, the oldest available minor version typically becomes unsupported. Clusters running minor versions that become unsupported are automatically upgraded to the next minor version.

Within a minor version (such as v1.14.x), clusters can be automatically upgraded to a new patch release.

[Release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) allow you to control your cluster and node pool version based on a version's stability rather than managing the version directly.

**Note:** Node auto-upgrade is not available for [Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters). Also, alpha clusters cannot be enrolled in release channels.

#### Factors that affect version rollout timing

To help ensure the stability and reliability of clusters on new versions, GKE follows certain practices during version rollouts.

These practices include, but are not limited to:

  * GKE gradually rolls out changes across Google Cloud regions and zones.
  * GKE gradually rolls out [patch versions](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) across [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). A patch is given soak time in the Rapid release channel, then the Regular release channel, before being promoted to the Stable release channel once it has accumulated usage and continued to demonstrate stability. If an issue is found with a patch version during the soaking time on a release channel, that version is not promoted to the next channel and the issue is fixed on a newer patch version.
  * GKE gradually rolls out [minor versions](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme), following a similar soaking process to patch versions. Minor versions have longer soaking periods as they introduce more significant changes.
  * GKE may delay automatic upgrades when a new version impacts a group of clusters. For example, [GKE pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#auto-upgrade-pause) for clusters that it detects are exposed to a deprecated API or feature that will be removed in the next minor version.
  * GKE might delay the rollout of new versions during peak times (for example, major holidays) to ensure business continuity.



### Configuring when auto-upgrades can occur

By default, auto-upgrades can occur at any time to preserve infrastructure security. Auto-upgrades are minimally disruptive, especially for regional clusters. However, some workloads may require finer-grained control. You can configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions) to manage when auto-upgrades can and must not occur.

**Note:** If you configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), the upgrade does not occur until the current time is within a maintenance window. If a maintenance window expires before the upgrade completes, an attempt is made to pause it. During the next occurrence maintenance window, an attempt is made to resume the upgrade.

## Upgrading manually

You can request to [manually upgrade your cluster's control plane or its node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) to an available and compatible version at any time. In Standard clusters, you can manually upgrade both Standard node pools and Autopilot-managed node pools. Manual upgrades bypass any configured maintenance windows and maintenance exclusions.

**Note:** You cannot upgrade your cluster more than one minor version at a time. For example, you can upgrade a cluster from version 1.12.x to 1.13.x, but not directly from 1.11.x to 1.13.x. For more information, see [Versioning and upgrades](https://docs.cloud.google.com/kubernetes-engine/versioning-and-upgrades).

When you [manually upgrade a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster), its availability depends on whether the cluster is regional or not:

  * **For zonal clusters** , the control plane is unavailable while it is being upgraded. For the most part, workloads run normally but cannot be modified during the upgrade.

  * **For regional clusters** , one replica of the control plane is unavailable at a time while it is upgraded, but the cluster remains highly available during the upgrade.




You can [manually initiate a node upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) to a version compatible with the control plane.

## How GKE responds to auto-upgrade failure

Node pool auto-upgrades can fail because of issues with the underlying Compute Engine instances, or because of issues with Kubernetes. For example, auto-upgrades fail in the following situations:

  * Your configured `maxSurge` setting exceeds your Compute Engine resource quota.
  * New surge nodes didn't register with the cluster control plane.
  * Nodes took too long to drain, or took too long to delete.



When issues occur with individual node upgrades, GKE retries the upgrade a few times, with an increasing interval between retries. If nodes in the node pool fail to upgrade, GKE does not roll back the upgraded nodes. Instead, GKE tries the node pool auto-upgrade again until all the nodes are successfully upgraded.

If your node upgrades fail because your surge node requests exceed your Compute Engine quota, GKE reduces the number of concurrent surge nodes to attempt to meet the quota and continue the upgrade.

**Note:** GKE maintains the existing node capacity during a surge upgrade, as long as `maxSurge` is more than `0` and `maxUnavailable=0`. Your workloads continue to run even when the node upgrade fails.

## Receiving upgrade notifications

GKE publishes notifications about events relevant to your cluster, such as version upgrades and security bulletins, to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), providing you with a channel to receive information from GKE about your clusters.

For more information, see [Receiving cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).

## Check upgrade logs

GKE logs control plane and node pool upgrade events to Cloud Logging by default. Upgrade events log provides visibility into the upgrade process, and includes valuable information for troubleshooting if needed.

### Control plane upgrade logs

Cluster upgrade events can be queried using the following filter:
    
    
    resource.type="gke_cluster"
    protoPayload.metadata.operationType=~"(UPDATE_CLUSTER|UPGRADE_MASTER)"
    resource.labels.cluster_name="CLUSTER_NAME"
    

These logs are recorded as structured logging formats. You can use the following fields for the details of the upgrade events:

Field | Description  
---|---  
protoPayload.metadata.operationType | There are two types of cluster upgrade events:

  * `UPGRADE_MASTER`: an upgrade to the Kubernetes control plane version.
  * `UPDATE_CLUSTER`: an update which doesn't change the Kubernetes control plane version.

Both cluster upgrade types can cause the loss of control plane availability for zonal clusters. For more information, see How cluster and node pool upgrades work.  
protoPayload.methodName | This field shows which API triggered the cluster upgrade.

  * `google.container.v1.ClusterManager.UpdateCluster`: [manual control plane upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_cp)
  * `google.container.internal.ClusterManagerInternal.UpdateClusterInternal`: [automatic control plane upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel)
  * `google.container.v1.ClusterManager.PatchCluster`: cluster configuration change

  
protoPayload.metadata.previousMasterVersion | This field is used only for the `MASTER_UPGRADE` operation type, and contains the previous control plane version used before the upgrade.   
protoPayload.metadata.currentMasterVersion | This field is used only for the `MASTER_UPGRADE` operation type, and contains the new control plane version number used after the upgrade.   
  
### Node pool upgrade logs

Use the following query to view node pool upgrade events: 
    
    
    resource.type="gke_nodepool"
    protoPayload.metadata.operationType="UPGRADE_NODES"
    resource.labels.cluster_name="CLUSTER_NAME"
    

Use the following field for details about the upgrade event:

`protoPayload.methodName` field shows whether the upgrade was triggered manually or triggered automatically as follows.

  * `google.container.v1.ClusterManager.UpdateNodePool`: [manual node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes)
  * `google.container.internal.ClusterManagerInternal.UpdateClusterInternal`: [automatic node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades)



## Component upgrades

GKE runs system workloads on worker nodes to support specific capabilities for clusters. For example, the `gke-metadata-server` system workload supports [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). GKE is [responsible](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility#googles_responsibilities) for the health of these workloads. To learn more about these components, refer to the documentation for the associated capabilities.

When new features or fixes become available for a component, GKE indicates the patch version in which they are included. To obtain the latest version of a component, refer to the associated documentation or [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for instructions on upgrading your control plane or nodes to the appropriate version.

## What's next

  * Learn more [about cluster configuration choices](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters).
  * Learn more about [upgrading a cluster or its nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  * Configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions).
  * Learn about managing automatic cluster upgrades across environments with [rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing).
  * [Best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).
  * Watch [GKE cluster upgrades: Best practices for GKE cluster stability, security, and performance](https://www.youtube.com/watch?v=RFp61C3YEXw)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
