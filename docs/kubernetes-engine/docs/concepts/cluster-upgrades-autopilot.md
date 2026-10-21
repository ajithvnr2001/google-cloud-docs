---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot/
title: Autopilot cluster upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T10:37:56.314431+00:00
---

# Autopilot cluster upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Autopilot cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)

This document discusses how automatic upgrades work on Google Kubernetes Engine (GKE) Autopilot clusters, including links to more information about related tasks and settings. You can use this information to keep your clusters updated for stability and security with minimal disruptions to your workloads.

For a general overview of cluster upgrades, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades). For information on how cluster upgrades work specifically for Standard clusters, including with [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pools#autopilot-node-pools), see [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).

## Automatic control plane and node upgrades

Automatic upgrades are enabled on all Autopilot clusters. GKE initiates automatic upgrades when GKE versions are selected for auto-upgrade, observes automatic upgrades across all clusters, and intervenes if problems such as unhealthy nodes occur. You can't disable automatic upgrades, however you can control their timing with [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

To upgrade a cluster, GKE updates the version the control plane and nodes are running. Clusters are upgraded to either a newer minor version (for example, 1.24 to 1.25) or newer patch version (for example, 1.24.2-gke.100 to 1.24.5-gke.200). For more information, see [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

All Autopilot clusters are enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), so GKE automatically upgrades the control plane and nodes to run the same GKE version.

GKE upgrades a cluster's control plane before upgrading nodes.

### Automatic control plane upgrades

All Autopilot clusters are [regional](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#regional_clusters) clusters. Regional clusters have multiple replicas of the control plane, and only one replica is upgraded at a time, in an undefined order. This approach helps ensure that the cluster remains highly available during automatic upgrades. Each control plane replica is only unavailable while the upgrade is in progress.

If you configure a [maintenance window or exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), GKE honors the configuration if possible.

GKE can't create new nodes when a control plane upgrade is in progress. If you deploy Pods that require new node types while a control plane upgrade is in progress, you might experience delays until the control plane upgrade completes.

GKE performs automatic control plane upgrades by using the following methods, depending on upgrade type:

  * **Patch version upgrades** : GKE uses a one-step upgrade, which upgrades your control plane directly to a later patch version.
  * **Minor version upgrades** : for upgrading to GKE minor version 1.33 or later, GKE uses a two-step process where you can validate the new minor version for a period of soak time, and roll back if needed. For more information, see [Two-step control plane minor upgrade with rollback safety](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#two-step-cp-upgrade). For upgrading to earlier versions, GKE uses the one-step upgrade process instead.



### Automatic node upgrades

After GKE upgrades your Autopilot cluster control plane, GKE upgrades the nodes to the same GKE version.

In Autopilot, GKE groups nodes that share similar characteristics together. GKE uses _surge upgrades_ for Autopilot nodes, upgrading up to 20 nodes in a group at the same time. The precise number of nodes that are upgraded at the same time varies to ensure continued high availability of nodes and workloads.

Node upgrades might take several hours depending on the number of nodes and the configuration of workloads running in the nodes. For example, the following configurations could contribute to longer upgrades:

  * A high value of [`terminationGracePeriodSeconds`](https://v1-30.docs.kubernetes.io/docs/reference/generated/kubernetes-api/v1.30/#podtemplatespec-v1-core) in a Pod's configuration.
  * A conservative [`PodDisruptionBudget`](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#how-disruption-budgets-work).
  * [Node affinity](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity) interactions.
  * Attached [`PersistentVolumes`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/persistent-volumes).



If you configure a [maintenance window or exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), GKE honors the configuration if possible.

When GKE upgrades a node, the following steps happen:

  1. GKE creates a new _surge node_ with the new GKE version and waits for the surge node to register with the control plane.
  2. GKE selects an existing node, the _target node_ , to upgrade.
  3. GKE _cordons_ the target node, preventing new Pods from being placed on the target node.
  4. GKE _drains_ the target node, evicting existing Pods from the target node. 
     * [`PodDisruptionBudget`](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) is respected for 1 hour.
     * [`terminationGracePeriodSeconds`](https://kubernetes.io/docs/concepts/workloads/pods/pod/#termination-of-pods) is limited to 10 minutes (600 seconds) for most Pods except for [Spot Pods](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/autopilot-spot-pods), which are limited to 25 seconds.
  5. GKE reschedules Pods that are managed by a [workload controller](https://kubernetes.io/docs/concepts/workloads/controllers/) onto other available nodes. Pods that can't be rescheduled remain in `PENDING` state until GKE can reschedule them.

**Note:** During the node drain process, Kubernetes ignores any Pods that aren't managed by a workload controller. Any configured `terminationGracePeriodSeconds` values and `preStop` hooks for these Pods aren't honored during the node drain. When GKE deletes the node, these Pods terminate immediately and aren't re-created on new nodes.
  6. GKE deletes the target node.




If a significant number of automatic upgrades to a specific GKE version result in unhealthy nodes across the GKE fleet, GKE stops upgrades to that version while we investigate the issue.

### How versions are selected for auto-upgrade

GKE releases new minor versions regularly, but a released version isn't immediately selected for automatic upgrades. To qualify as an auto-upgrade target, the GKE version must accumulate enough usage to prove stability over time.

Google Cloud then selects that version as an auto-upgrade target for clusters that run a specific subset of older GKE versions. For example, soon after a new minor version becomes available, the oldest available minor version [typically becomes unsupported](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle). GKE upgrades clusters that run unsupported minor versions to the auto-upgrade target version.

GKE announces new auto-upgrade target versions in the [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes). Occasionally, a version is selected for control plane auto-upgrades and node auto-upgrades during different weeks. GKE automatically upgrades to new patch releases within a minor version (such as v1.21.x). To get auto-upgrade targets for a specific cluster, see [Get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).

For information about the version lifecycle and versioning scheme, refer to [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

#### Factors that affect version rollout timing

To help ensure the stability and reliability of clusters on new versions, GKE follows certain practices during version rollouts.

These practices include, but are not limited to:

  * GKE gradually rolls out changes across Google Cloud regions and zones.
  * GKE gradually rolls out [patch versions](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) across [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). A patch is given soak time in the Rapid release channel, then the Regular release channel, before being promoted to the Stable release channel once it has accumulated usage and continued to demonstrate stability. If an issue is found with a patch version during the soaking time on a release channel, that version is not promoted to the next channel and the issue is fixed on a newer patch version.
  * GKE gradually rolls out [minor versions](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme), following a similar soaking process to patch versions. Minor versions have longer soaking periods as they introduce more significant changes.
  * GKE may delay automatic upgrades when a new version impacts a group of clusters. For example, [GKE pauses automatic upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#auto-upgrade-pause) for clusters that it detects are exposed to a deprecated API or feature that will be removed in the next minor version.
  * GKE might delay the rollout of new versions during peak times (for example, major holidays) to ensure business continuity.



### Configuring when auto-upgrades can occur

By default, auto-upgrades can occur at any time. Auto-upgrades are minimally disruptive, especially for Autopilot clusters. However, some workloads might require finer-grained control. You can configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions) to manage when auto-upgrades can and must not occur.

If you configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions), the upgrade does not occur until the current time is within a maintenance window. If a maintenance window expires before the upgrade completes, GKE attempts to pause the upgrade. GKE resumes the upgrade during the next available maintenance window.

## Manually upgrade an Autopilot cluster

You can manually upgrade the GKE version of your cluster's control plane to a supported minor or patch version in the same release channel, or to a patch version of the same minor version as your cluster in a different release channel.

For example, consider an Autopilot cluster running GKE version 1.35.6-gke.1250000 in the Regular release channel. The following behavior applies:

  * You can upgrade to any patch version available in Regular.
  * You can upgrade to any patch version of 1.35 in the Rapid channel. For more information about upgrading outside your channel, refer to [Running patch versions from a newer channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#newer-patch-versions).
  * You can upgrade to a new minor version available in Regular. For example, you can upgrade to 1.36.



You can use the following methods to upgrade your control plane version, depending on upgrade type:

  * **Patch version upgrades** : you can use a one-step upgrade.
  * **Minor version upgrades** : you can use either the one-step upgrade, or the two-step upgrade.



For more information about these methods and how to use them, see [Upgrade the cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster).

GKE automatically upgrades your nodes to match the control plane version as soon as possible, subject to [maintenance availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions). You can't manually manage the node version for Autopilot clusters.

## Surge upgrades

Autopilot clusters use _surge upgrades_ to upgrade multiple nodes at the same time. Surge upgrades let GKE reduce how disruptive version upgrades are to your running workloads by maintaining enough compute capacity for your running workloads. Autopilot manages the number of _surge nodes_ that are added to the cluster during the upgrade. This number varies based on the total size of the cluster. GKE also manages the total number of _target nodes_ that can be simultaneously unavailable during the upgrade.

The number of new surge nodes and unavailable target nodes varies to ensure that your cluster always has enough compute capacity for all running workloads. You might experience minor disruptions as GKE migrates workloads from target nodes to surge nodes during the upgrade.

For a description of how surge upgrades occur, refer to Automatic node upgrades.

### Quota requirements for surge upgrades

Unlike node recreation, surge upgrades require additional Compute Engine resources. Resource allocation depends on your available [Compute Engine quota](https://docs.cloud.google.com/compute/quotas). Depending on your configuration, this quota can limit the number of parallel upgrades or even cause the upgrade to fail. As a good practice to avoid scaling issues and for more predictable upgrades, ensure that your Compute Engine instance quota doesn't exceed 90%.

For more information about quota, refer to [Ensure resources for node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota).

## Receive upgrade notifications

GKE publishes upgrade notifications to [Pub/Sub](https://docs.cloud.google.com/pubsub/docs/overview), providing you with a channel to receive information from GKE about your clusters.

For more information, see [Receiving cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-notifications).

## Component upgrades

GKE runs system workloads on worker nodes to support specific capabilities for clusters. For example, the `gke-metadata-server` system workload supports [Workload Identity Federation for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-identity). GKE is [responsible](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility#googles_responsibilities) for the health of these workloads. To learn more about these components, refer to the documentation for the associated capabilities.

When new features or fixes become available for a component, GKE indicates the patch version in which they are included. To obtain the latest version of a component, refer to the associated documentation or [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for instructions on upgrading your control plane or nodes to the appropriate version.

## What's next

  * Configure [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions).
  * Learn about managing automatic cluster upgrades across environments with [rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing).
  * Watch [GKE cluster upgrades: Best practices for GKE cluster stability, security, and performance](https://www.youtube.com/watch?v=RFp61C3YEXw)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
