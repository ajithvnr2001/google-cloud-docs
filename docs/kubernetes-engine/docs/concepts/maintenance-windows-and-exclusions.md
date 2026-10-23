---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions/
title: Maintenance windows and exclusions \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:11.790712+00:00
---

# Maintenance windows and exclusions  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Maintenance windows and exclusions Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page describes maintenance windows and maintenance exclusions, which are policies that provide control over when some cluster maintenance, such as auto-upgrades, can and can't occur on your Google Kubernetes Engine (GKE) clusters. For example, a retail business could limit maintenance to only occur on weekday evenings, and could prevent automated maintenance during a key industry sales event.

**Note:** Maintenance windows and exclusions only control the timing of certain types of GKE cluster maintenance, and don't impact the timing of maintenance for services on which GKE depends, including Compute Engine. To learn more, see Automatic maintenance that doesn't respect GKE maintenance policies.

## About GKE maintenance policies

GKE maintenance policies, which include maintenance windows and exclusions, give you control over when certain automatic maintenance can occur on your clusters, including cluster upgrades and other changes to the node configuration, or the cluster's network topology.

A _maintenance window_ is a repeating window of time during which GKE automatic maintenance is permitted.

A _maintenance exclusion_ is a non-repeating window of time during which GKE automatic maintenance is forbidden.

GKE makes automatic changes that respect your cluster's maintenance policies when there is an open maintenance window and no active maintenance exclusion. For each cluster, you can configure one recurring maintenance window, and multiple maintenance exclusions.

Other types of maintenance aren't dependent on GKE maintenance policies, including control plane repair operations, and maintenance of services on which GKE depends, like Compute Engine. To learn more, see Automatic maintenance that doesn't respect maintenance policies.

## What changes do and don't respect GKE maintenance policies

Before configuring GKE maintenance policies—maintenance windows and exclusions—review the following sections to understand how GKE and related services do and don't respect them.

### Automatic maintenance that respects GKE maintenance policies

With GKE maintenance policies, you can control the timing of the following types of events, which cause temporary disruption to your cluster:

  * Automatic cluster upgrades, including control plane upgrades and node upgrades. To learn more about these changes and how they might cause temporary disruption to your environment, see [Autopilot cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot) and [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).
  * User-initiated configuration changes that cause nodes to be re-created or significantly change the cluster's internal network topology. To learn more, see Manual changes that respect GKE maintenance policies.



Other types of automatic maintenance aren't dependent on maintenance policies. To learn more, see Automatic maintenance that doesn't respect maintenance policies.

### Automatic maintenance that doesn't respect GKE maintenance policies

GKE maintenance windows and exclusions don't block all types of automatic maintenance. Before configuring your GKE cluster's maintenance policies, ensure that you understand what types of changes don't respect maintenance windows and exclusions.

#### Other Google Cloud maintenance

GKE maintenance windows and exclusions don't prevent automatic maintenance of underlying Google Cloud services, primarily Compute Engine, or services which install applications to the cluster, such as Cloud Deploy.

For example, [GKE nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) are Compute Engine VMs that GKE manages for your cluster. Compute Engine VMs sometimes experience [host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview), which can include [maintenance events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#maintenanceevents) or [host errors](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#hosterror). The way VMs behave during these events is determined by the VM's host maintenance policy, which, by default for most VMs, means to [live migrate](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#live_migrate). This typically means little-to-no downtime for the nodes, and, for most workloads, the default policies are sufficient. For some VM machine families, you can [monitor and plan for a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/monitor-plan-host-maintenance-event) and [trigger a host maintenance event](https://docs.cloud.google.com/compute/docs/instances/trigger-host-maintenance-event) to time it with your GKE maintenance policies.

We recommend that you review information about [host events](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview), [host maintenance policies](https://docs.cloud.google.com/compute/docs/instances/host-maintenance-overview#schedulingoptions), and confirm that your workloads are prepared for disruption, especially if they're running on nodes that can't perform a live migration.

**Important:** Because Compute Engine instances with accelerators (GPUs or TPUs) don't support live migration, Compute Engine must shut down and re-create the nodes during host maintenance. This process can disrupt workloads such as AI/ML training or inference jobs. To minimize disruption, perform both Compute Engine host maintenance and GKE node upgrades at the same time. For more information, see [Perform host maintenance for nodes running training and inference workloads](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/perform-host-maintenance-accelerators).

#### Automated repairs and resizing

GKE performs automated repairs on [control planes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane). This includes processes like upscaling the control plane to an appropriate size or restarting the control plane to resolve issues. Most repairs ignore maintenance windows and exclusions because failing to perform the repairs can result in non-functional clusters.

You can't disable control plane repairs. However, most types of clusters, including [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) and [ Standard regional clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters) have multiple replicas of the control planes, which allows for high availability of the Kubernetes API server even during maintenance events. [Standard zonal clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#zonal_clusters), which only have a single control plane, can't be modified during control plane configuration changes and cluster maintenance. This includes deploying workloads.

Nodes also have [auto-repair functionality](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair), which you can [disable](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#disable) for Standard clusters.

#### Critical security vulnerability patching

Maintenance windows and exclusions can cause security patches to be delayed. However, GKE [reserves the right](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility) to override maintenance policies for [critical security vulnerabilities](https://docs.cloud.google.com/kubernetes-engine/docs/resources/security-patching#how_vulnerabilities_are_classified).

#### Maintenance of the Spanner-based cluster state database

Some GKE clusters use a Spanner key-value database to store the state of Kubernetes API resources. Maintenance operations on this database ignore any active maintenance windows and exclusions. However, the Spanner-based cluster state database is replicated and remains available during maintenance events.

### Manual changes that respect GKE maintenance policies

Some changes to the nodes or networking configuration require the nodes to be recreated to apply the new configuration, including some of the following changes:

  * [Rotating the control plane's IP address](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/ip-rotation)
  * [Rotating the control plane's credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation)
  * [Configuring shielded nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/shielded-gke-nodes)
  * [Configuring network policies](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/network-policy)
  * [Configuring intranode visibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/intranode-visibility)
  * [Configuring NodeLocal DNSCache](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/nodelocal-dns-cache)
  * [Configuring GKE Sandbox](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/sandbox-pods)



These changes respect GKE maintenance policies, meaning that GKE waits for an open maintenance window and waits for no active maintenance exclusion preventing node maintenance. To manually apply the changes to the nodes, use the Google Cloud CLI to call the [`gcloud container clusters upgrade`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/upgrade) command and passing the `--cluster-version` flag with the same GKE version that the node pool is already running.

### Manual changes that don't respect GKE maintenance policies

Some manual changes recreate the nodes using a node upgrade strategy immediately without respecting maintenance policies. For more details, see [Manual changes that recreate the nodes using a node upgrade strategy without respecting maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manual-changes-strategy-but-no-respect-policies).

## Maintenance windows

_Maintenance windows_ allow you to control when applicable automatic maintenance—including automatic upgrades of control planes and nodes—can occur, to mitigate potential transient disruptions to your workloads. Maintenance windows are useful for the following types of scenarios, among others:

  * **Off-peak hours:** You want to minimize the chance of downtime by scheduling automatic upgrades during off-peak hours when traffic is reduced.
  * **On-call:** You want to ensure that upgrades happen during working hours so that someone can monitor the upgrades and manage any unanticipated issues.
  * **Multi-cluster upgrades:** You want to roll out upgrades across multiple clusters in different regions one at a time at specified intervals.



In addition to automatic upgrades, Google may occasionally need to perform other maintenance tasks, and honors a cluster's maintenance window if possible.

If tasks run beyond the maintenance window, GKE attempts to pause the tasks, and attempts to resume those tasks during the next maintenance window.

GKE reserves the right to roll out unplanned emergency upgrades outside of maintenance windows. Additionally, mandatory upgrades from deprecated or outdated software might automatically occur outside of maintenance windows.

**Note:** You can also [manually upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) at any time. Manually-initiated upgrades begin immediately and ignore any maintenance windows.

To learn how to set up maintenance window for a new or existing cluster, see [Configure a maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window).

You can, for advanced use cases, additionally use [cluster disruption budgets](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget) to customize the minimum time interval between specific types of cluster upgrades, including patch or minor upgrades.

### Time zones for maintenance windows

When configuring and viewing maintenance windows, times are shown differently depending on the tool you are using:

#### When configuring maintenance windows

Times are always stored in UTC. However, when configuring the maintenance window, you either use UTC or your local time zone.

When configuring maintenance windows using the more generic `--maintenance-window` flag, you cannot specify a time zone. UTC is used when using the gcloud CLI or the API, and the Google Cloud console displays times using the local time zone.

When using more granular flags, such as `--maintenance-window-start`, you can specify the time zone as part of the value. If you omit the time zone, your local time zone is used.

#### When viewing maintenance windows

When viewing information about your cluster, timestamps for maintenance windows may be shown in UTC or in your local time zone, depending on how you are viewing the information:

  * When using the Google Cloud console to view information about your cluster, times are always displayed in your local time zone.
  * When using the gcloud CLI to view information about your cluster, times are always shown in UTC.



In both cases, the `RRULE` is always in UTC. That means that if specifying, for example, days of the week, then those days are in UTC.

## Maintenance exclusions

With _maintenance exclusions_ , you can prevent applicable automatic maintenance from occurring during a specific time period. For example, many retail businesses have business guidelines prohibiting infrastructure changes during the end-of-year holidays. As another example, if a company is using an API that is scheduled for deprecation, they can use maintenance exclusions to pause [minor upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_upgrades) to give them time to migrate applications.

For known high-impact events, we recommend that you match any internal change restrictions with a maintenance exclusion that starts one week before the event and lasts for the duration of the event.

Exclusions have no recurrence. Instead, create each instance of a periodic exclusion separately.

When exclusions and maintenance windows overlap, exclusions have precedence.

To learn how to set up maintenance exclusions for a new or existing cluster, see [Configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion).

**Caution:** If you use maintenance exclusions to prevent node auto-upgrades, you must manually upgrade those node pools to ensure that your cluster adheres to the [GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew), and uses [supported GKE versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels). GKE automatically upgrades the node pools at the end of support to maintain the supportability and reliability of your cluster.

### Types of maintenance exclusions

You can set a maintenance exclusion for the entire cluster, or, if you require additional granularity, you can set a maintenance exclusion for only an individual node pool. Review the following sections to understand how the different types of maintenance exclusions work.

#### Cluster maintenance exclusions

At the cluster level, you can specify both _when_ to prevent automatic maintenance on your cluster, and the _scope_ of automatic updates that might occur. See the following cluster maintenance exclusion scopes, and example relevant scenarios:

  * **No upgrades - avoid any maintenance:** You want to temporarily avoid any change to your cluster during a specific period of time. This is the default scope.
  * **No minor upgrades - maintain current Kubernetes minor version** : You want to maintain the minor version of a cluster to, for example, avoid [API changes](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations) or validate the next minor version.
  * **No minor or node upgrades - prevent node disruption** : You want to avoid any eviction and rescheduling of your workloads because of node upgrades.



The following table lists how each of these scopes restricts [minor or patch](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) upgrades for cluster control planes or nodes.

Scope | Control plane | Nodes | Maximum exclusion length  
---|---|---|---  
Automatic minor upgrade | Automatic patch upgrade | Automatic minor upgrade | Automatic patch upgrade  
No upgrades (default) | Not allowed | Not allowed | Not allowed | Not allowed |  Cannot exceed 90 days. We recommend limiting the length of this type of maintenance exclusion to less than 30 days. Only set the maintenance exclusion for greater than 30 days if you have a specific version qualification process which takes longer than this, or a high-impact event which requires restricted changes for more than 30 days. You might miss critical patches if you upgrade with less frequency than 30 days.  
No minor upgrades | Not allowed | Allowed | Not allowed | Allowed |  You can configure the maintenance exclusion in one of the following ways:

  * **Fixed end time** : set the end time up until the end of support for the cluster's minor version and respective release channel. For clusters enrolled in the Rapid, Regular, or Stable channels, this is the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule), and for the Extended channel, the [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-extended-support).
  * **Track the end of support** : configure the end time to track the end of support for your cluster's minor version. If you don't manually upgrade the cluster to the next minor version before the end of support, GKE performs the required [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support) and then reactivates the maintenance exclusion with the end time tracking the new minor version's end of support. For more information, see [How a maintenance exclusion tracks the end of support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#how-exclusion-tracks-eos).

We recommend limiting the length of maintenance exclusions to less than six months. Long maintenance exclusions postpone minor version upgrades and can result in GKE needing to perform multiple minor version upgrades in a row to ensure that your cluster continues to run a supported version.  
No minor or node upgrades | Not allowed | Allowed | Not allowed | Not allowed  
  
When GKE upgrades a cluster, VMs for the control plane and node restart. For control planes, Autopilot and regional Standard clusters maintain Kubernetes API server availability. In zonal clusters, which have a single control plane node, VM restarts make the control plane temporarily unavailable. For nodes, VM restarts trigger Pod rescheduling which can temporarily disrupt existing workloads. You can [set your tolerance for workload disruption](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#set-tolerance) using a [Pod Disruption Budget (PDB)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).

#### Node pool maintenance exclusions

If you want to prevent [automatic cluster node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades) for some, but not all, of the node pools in your Standard cluster, you can use a node pool maintenance exclusion. For example, if you have some node pools in your cluster where you want GKE to automatically upgrade the nodes, but other node pools where you want to manage node pool upgrades, you can set node pool exclusions for only the node pools requiring more manual control.

When you enable this type of maintenance exclusion, GKE only automatically upgrades your cluster as required when the node pool's minor version reaches the end of support. For more information, see [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).

The following table explains how this maintenance exclusion prevents node pool auto-upgrades:

Type of maintenance exclusion | Nodes | Maximum exclusion length  
---|---|---  
Automatic minor upgrade | Automatic patch upgrade  
Node pool | Not allowed | Not allowed | The end time tracks the end of support for your cluster's minor version. If you don't manually upgrade the cluster to the next minor version before the end of support, GKE performs the required [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support) and then reactivates the maintenance exclusion with the end time tracking the new minor version's end of support. For more information, see [How a maintenance exclusion tracks the end of support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#how-exclusion-tracks-eos).   
  
To use this type of maintenance exclusion, you can do any of the following:

  * [Create a node pool with a node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#create-node-pool-maintenance-exclusion).
  * [Add a node pool maintenance exclusion for an existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configure-node-pool-maintenance-exclusion-existing).
  * Configure the `nodePoolConfig.maintenanceExclusion` field in a [custom ComputeClass](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-custom-compute-classes). After you set this field, GKE adds a node pool maintenance exclusion when creating new Standard node pools, or groups of nodes for Autopilot mode. For more information, see the field in the [`nodePoolConfig`](https://docs.cloud.google.com/kubernetes-engine/docs/reference/crds/computeclass#nodepoolconfig) section of the ComputeClass specification.



### Exclusion expiration and activation

A cluster maintenance exclusion becomes active immediately, or at the time and date that you specify when you configure the exclusion.

A maintenance exclusion expires or becomes inactive at the following time:

  * **Fixed end time** : when the fixed end time that you specified for the exclusion passes.
  * **Track the end of support** : the maintenance exclusion becomes temporarily inactive at the start of the end of support date if your cluster hasn't yet been upgraded to the next minor version and you use a maintenance exclusion in either of the following ways:

    * Configure a cluster maintenance exclusion for the end time to track the [end of support date](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle) for your cluster's minor version.
    * Set a node pool maintenance exclusion.

GKE reactivates the maintenance exclusion after either of the following:

    * GKE performs the required [automatic upgrade at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).
    * You [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) the cluster to the next minor version.



When a maintenance exclusion expires (that is, the current time has moved beyond the end time specified for the exclusion) or becomes temporarily inactive, that exclusion no longer prevents GKE updates. Other exclusions that are still valid will continue to prevent GKE updates.

When no exclusions or other factors remain that prevent cluster upgrades, GKE gradually upgrades your cluster to eligible auto-upgrade targets.

If your cluster missed multiple minor version upgrades because of the exclusion, GKE schedules approximately one minor version upgrade per month, upgrading both the cluster control plane and nodes, to ensure that your cluster runs a supported version. You can always execute manual upgrades to get your cluster to a specific minor version sooner.

#### How a maintenance exclusion tracks the end of support

You can configure cluster maintenance exclusions with the scope of "No minor upgrades" or "No minor or node upgrades" to track the end of support of your cluster's minor version, instead of manually setting a date as an end time. Node pool maintenance exclusions also track the end of support.

If you set one of these types of maintenance exclusions to track the end of support date, then in the following situations, GKE updates the end time of your maintenance exclusion to reflect the new date of the end of support:

  * You or GKE upgrade your cluster to a new minor version.
  * You change your cluster's enrollment to or from the Extended channel.
  * GKE updates the end of support date of your cluster's minor version.



With these types of maintenance exclusions, if you haven't manually upgraded your cluster to the next minor version, GKE performs the required [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support) and then reactivates the maintenance exclusion with the end time tracking the new minor version's end of support.

For more information about the end of support, see the [GKE minor version lifecycle](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle). To see the end of support date for your cluster's minor version, see [Find when your cluster's minor version reaches the end of support](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#when-eos).

##### Temporary, emergency prevention of automatic upgrades at the end of support

As a temporary measure, to be used only in emergencies where no other options are available, you can delay the automatic upgrades at the end of support for up to 90 days after the end of support date by [configuring a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configure-maintenance-exclusion) with the default scope of "No upgrades". We don't recommend this practice because of the risks associated with running an unsupported version. After the maintenance exclusion expires, GKE upgrades the cluster.

Operating a cluster that uses an unsupported GKE version carries significant security, reliability, and compatibility risk because GKE doesn't provide security patches or bug fixes for end of support versions. GKE can't commit to providing patches or updates for versions at the end of support.

For more information, see [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).

### How maintenance exclusions work with setting the scope of a rollout sequence

If you use rollout sequencing with custom stages, you can designate which scope of automatic cluster upgrades you'd like GKE to perform, similar to maintenance exclusions. However, with rollout sequencing, you set these scopes for all clusters in the rollout sequence, instead of for individual clusters with maintenance exclusions. If you have a cluster in a rollout sequence and you also configure maintenance exclusions, GKE adheres to the more-restrictive scope when performing automatic cluster upgrades. For example, if you let GKE perform control plane patch upgrades with a maintenance exclusion, but not with the scopes in the rollout sequence, it won't perform this type of upgrade. For more information, see [Choosing what types of upgrades GKE performs in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#what-type-of-upgrades-scope).

### Limitations on configuring maintenance exclusions

Cluster maintenance exclusions have the following limitations:

  * You can only restrict the scope of automatic upgrades in a maintenance exclusion for clusters that are enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For [clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel) ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)), you can only create a maintenance exclusion with the default "No upgrades" scope.
  * You can add a maximum of three maintenance exclusions that exclude all upgrades (that is, a scope of "no upgrades"). These exclusions must be configured to allow for at least 48 hours of maintenance availability in a 92-day rolling window.
  * You can have a maximum of 20 cluster maintenance exclusions for each cluster.
  * If you don't specify a scope in your exclusion, the scope defaults to "no upgrades".
  * You can't configure a maintenance exclusion to include or exceed the [end of support date](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule) of the minor version corresponding to the cluster's release channel enrollment, except as a temporary, emergency measure with the "No upgrades" scope. For setting a fixed end time around the end of support, see the following examples:

    * A cluster is running a [minor version](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) in the Stable channel where the GKE release schedule states that the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-standard-support) date is June 5, 2025. You must set the end time of the maintenance exclusion to `2025-06-05T00:00:00Z` or earlier.
    * A cluster is running a minor version in the Extended channel where the GKE release schedule states the end of extended support date is April 5, 2026. You must set the end time of the maintenance exclusion to `2026-04-0500:00:00Z` or earlier. If you want to change the release channel of the cluster to another channel, you must change the end time of the maintenance exclusion if it exceeds the end of standard support. To learn more, see [Change your cluster from the Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#change-from-extended).

The exclusion can, optionally, track the end of support date, and it becomes temporarily inactive at the start of the end of support date until the cluster is upgraded to the next minor version.




Node pool maintenance exclusions have the following limitations:

  * The cluster must be enrolled in a release channel.
  * You can only set one node pool maintenance exclusion per node pool.
  * You can't set a node pool maintenance exclusion to start at a future date and time. The maintenance exclusion starts immediately when you enable it.
  * You can't use node pool maintenance exclusions with Autopilot clusters, because GKE manages the nodes for Autopilot clusters.
  * The node pool maintenance exclusion prevents only node upgrades (version updates), and doesn't prevent other types of [node updates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption).



### Maintenance exclusions don't affect manual upgrades and the versions of new nodes

Maintenance exclusions prevent existing control planes and nodes from being automatically upgraded, depending on the scope of the maintenance exclusion. However, maintenance exclusions don't prevent the following changes:

  * [Manually upgrading](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) the cluster's control plane or nodes.
  * Creating a new Standard node pool with a later version than existing Standard node pools where a maintenance exclusion is preventing automatic upgrades.
  * Having node auto-provisioning create the following resources with a later version than existing nodes where a maintenance exclusion is preventing automatic upgrades: 
    * New Standard node pools.
    * New nodes in an Autopilot cluster.



Say that you created a maintenance exclusion for your cluster with a scope where GKE automatically upgrades the control plane, but not the nodes, to later patch versions. In this scenario, GKE might create new node pools, or nodes that are created through auto-provisioning, that run the later patch version of the control plane.

Cluster nodes can only run the same or earlier versions of GKE than the control plane. Maintenance exclusions prevent automatic upgrades of existing nodes. If the control plane has a newer version than the existing nodes, newly created or manually upgraded nodes might run a more recent version of GKE than nodes that are restricted from automatic upgrades by maintenance exclusions.

### Multiple exclusions

You can set multiple exclusions for a cluster, including node pool exclusions. These exclusions can have different scopes and overlapping time ranges. The end-of-year holiday season use case is an example of overlapping exclusions, where both the "No upgrades" and "No minor upgrades" scopes are in use.

When exclusions overlap, if any active exclusion (that is, current time is within the exclusion time period) blocks an upgrade, the upgrade will be postponed.

Using the end-of-year holiday season use case, a cluster has the following exclusions specified:

  * No minor upgrades: September 30 - January 15
  * No upgrades: November 19 - December 4
  * No upgrades: December 15 - January 5



As a result of these overlapping exclusions, the following upgrades will be blocked on the cluster:

  * Patch upgrade to the node pool on November 25 (rejected by "No upgrades" exclusion)
  * Minor upgrade to the control plane on December 20 (rejected by "No minor upgrades" and "No upgrades" exclusion)
  * Patch upgrade to the control plane on December 25 (rejected by "No upgrades" exclusion)
  * Minor upgrade to the node pool on January 1 (rejected by "No minor upgrades" and "No upgrades" exclusion)



The following maintenance would be permitted on the cluster:

  * Patch upgrade to the control plane on November 10 (permitted by "No minor upgrades" exclusion)
  * VM disruption due to GKE maintenance on December 10 (permitted by "No minor upgrades" exclusion)



### Usage examples

Here are some example use cases for restricting the scope of updates that can occur.

#### Example: Retailer preparing for the end-of-year holiday season

In this example, the retail business does not want disruptions during the highest-volume sales periods, which is the four days encompassing [Black Friday](https://wikipedia.org/wiki/Black_Friday_\(shopping\)) through [Cyber Monday](https://wikipedia.org/wiki/Cyber_Monday), and the month of December until the start of the new year. In preparation for the shopping season, the cluster administrator sets up the following exclusions:

  * **No minor upgrades** : Allow only patch updates on the control plane and nodes between September 30 - January 15.
  * **No upgrades** : Freeze all upgrades between November 19 - December 4.
  * **No upgrades** : Freeze all upgrades between December 15 - January 5.



If no other exclusion windows apply when the maintenance exclusion expires, the cluster is upgraded to a new GKE minor version if one was made available between September 30 and January 6.

#### Example: Company using a beta API in Kubernetes that's being removed

In this example, a company is using the `CustomResourceDefinition` `apiextensions.k8s.io/v1beta1` API, which [will be removed in version 1.22](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations/apis-1-22#customresourcedefinition-v122). While the company is running versions earlier than 1.22, the cluster administrator sets up the following exclusion:

  * **No minor upgrades** : Freeze minor upgrades for three months while migrating customer applications from `apiextensions.k8s.io/v1beta1` to `apiextensions.k8s.io/v1`.



#### Example: Company's legacy database not resilient to node pool upgrades

In this example, a company is running a database that does not respond well to Pod evictions and rescheduling that occurs during a node pool upgrade. The cluster administrator sets up the following exclusion:

  * **No minor or node upgrades** : Freeze node upgrades for three months. When the company is ready to accept downtime for the database, they trigger a manual node upgrade.



#### Example: Company runs a mix of general-purpose and fault-intolerant workloads

In this example, a company is using one cluster to run a mixture of workloads that can and can't tolerate automatic upgrades to the nodes. The cluster administrator wants GKE to handle node upgrades for some node pools, but not others. The cluster administrator uses a node pool maintenance exclusion for any node pools that can only be manually upgraded.

## What's next

  * Learn more about [upgrading a cluster or its nodes](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  * Learn more about [Node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies).
  * Learn how to [Receive cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
