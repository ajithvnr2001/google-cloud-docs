---
url: https://docs.cloud.google.com/kubernetes-engine/upgrades/
title: About GKE cluster upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:03:27.174328+00:00
---

# About GKE cluster upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/upgrades/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About GKE cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page introduces the concept of _cluster upgrades_ for Google Kubernetes Engine (GKE) clusters. If you're familiar with how cluster upgrades work, instead see [implementing the best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).

## What are cluster upgrades?

A [Kubernetes cluster in GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture) is composed of a control plane and worker nodes, which run user workloads. Both the control plane and worker nodes run a version of Kubernetes. GKE automatically upgrades the version of the control plane and nodes to ensure that the cluster receives new features, bug fixes, and security patches. To learn more about how GKE chooses the version for your cluster, see [ GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).

GKE performs the following types of cluster upgrades, which include both _control plane upgrades_ and _node upgrades_:

  * **Patch version upgrades** : GKE automatically upgrades clusters to a new [patch](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) as often as every week, depending on the [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).
  * **Minor version upgrades** : Minor upgrades occur approximately three times a year. For [Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended) clusters, minor upgrades occur only when the minor version nears the [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#periods_of_availability_in_the_minor_version_lifecycle).



For clusters not enrolled in a release channel ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)), GKE also automatically upgrades both the control plane and nodes. To learn how GKE chooses auto-upgrade targets for those clusters, see the _Upgrade timing_ row in [a table comparing clusters enrolled and not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#comparison-table-no-channel).

You can also [manually upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) a cluster's control plane and nodes to an available version, rather than GKE performing an automatic upgrade. Use GKE features to choose when and how GKE upgrades your clusters. To learn more, see Control cluster upgrades.

### Get information about cluster upgrades

Use the following resources for details about current upgrades:

  * For information about upgrades for specific clusters, including current auto-upgrade targets, see [Get visibility into cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist).
  * To retrieve general auto-upgrade targets, see the [Current versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) table. For a specific mapping to a cluster's minor version, see the _Version updates_ release notes.
  * Check the [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule) for a best-case estimate of when minor versions are available for upgrades, and reach [the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle).
  * Use [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications) to stay informed about upgrade events—such as scheduled cluster upgrades ([Preview](https://cloud.google.com/products#product-launch-stages))—for your clusters by using Cloud Logging or Pub/Sub.
  * Use [insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders) to get the following cluster-specific recommendations:

    * [Use release channels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#identify-recommend)
    * [Set maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#recommender-maintenance-window)
    * [Upgrade to supported versions](https://docs.cloud.google.com/kubernetes-engine/versioning#recommender-end-of-support)
    * [Maintain supported version skew](https://docs.cloud.google.com/kubernetes-engine/versioning#recommender-version-skew)
    * [Ensure workloads are disruption-ready](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-disruption-readiness)



## Control cluster upgrades

As a platform administrator, you want to minimize disruption to your workloads while keeping them performant, reliable, and secure. GKE's responsibility as part of the [GKE shared responsibility model](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility) is to upgrade your cluster to keep it running to serve your workloads.

As part of [your shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/shared-responsibility#customers_responsibilities) with GKE, you must prepare your workloads for cluster upgrades. You can't completely disable automatic upgrades, but you can control when and how GKE performs the upgrades.

To manage GKE cluster upgrades, optimized for your workloads, use the following capabilities:

  * [**Release channels**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels): Choose a release channel to get cluster versions with your chosen balance of feature availability and stability.
  * [**Maintenance windows**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows): Specify a recurring window of time when [certain types of GKE cluster maintenance](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#examples_of_automatic_maintenance), such as upgrades, can occur.
  * [**Maintenance exclusions**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions): Prevent cluster maintenance from occurring for a specific time period.
  * [**Cluster disruption budgets**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget): customize the minimum time interval between specific types of cluster upgrades, including patch or minor upgrades.
  * [**Node upgrade strategies**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies): If using a Standard node pool, choose how your nodes are updated–surge, blue-green, or autoscaled blue-green ([Preview](https://docs.cloud.google.com/products#product-launch-stages)) upgrades–to minimize disruption to your workloads. Additionally, [choose how many node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#concurrent-upgrades) GKE automatically upgrades at the same time in a cluster.
  * [**Rollout sequencing**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing): Qualify upgrades in a pre-production environment before GKE upgrades your production clusters.
  * [**Manual upgrades**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster): Manually upgrade your cluster, and perform such actions as canceling, resuming, rolling back, and completing automatic or manual in-progress upgrades.



After learning about the preceding capabilities, you'll be able to implement the [Best practices for upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters).

To maximize your workload availability, also use the recommendations and techniques described in [managing and monitoring your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#manage-monitor-cluster), and [preparing your workloads](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#prepare-workloads).

## What are automatic cluster control plane upgrades?

On a regular basis, GKE automatically upgrades the [control plane](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#control_plane) of a cluster to newer stable minor versions and patches of Kubernetes. GKE chooses new versions for your cluster based on the cluster's release channel enrollment.

For patch version upgrades, GKE directly upgrades the control plane to a later version with a one-step upgrade. For minor version upgrades to GKE version 1.33 or later, GKE uses a two-step upgrade, where you can validate the new minor version for a period of soak time, and roll back if needed. For more information about these methods, see [Upgrade the cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster).

Across the entire fleet of GKE clusters, automatic upgrades are typically performed in stages over multiple weeks. As infrastructure security is a high priority for GKE, control planes upgrades happen regularly and can't be disabled.

Although you can't disable control plane upgrades, you can use [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) to temporarily prevent all control plane upgrades—including minor and patch upgrades—for up to 90 days, regardless of whether your cluster is enrolled in a release channel. For clusters enrolled in a release channel, you can prevent minor version upgrades until the minor version reaches the end of support.

You can use [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows) to set a recurring period of time when GKE can upgrade the control plane.

## What are automatic cluster node upgrades?

GKE performs automatic cluster node upgrades in the following ways, depending on the type of cluster and nodes:

  * For Autopilot clusters, [nodes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-architecture#nodes) are always [upgraded automatically](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) to the version of the control plane.
  * For Standard clusters, GKE does the following:

    * For Standard node pools, by default, nodes are upgraded automatically to the appropriate [auto-upgrade target](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#auto-upgrade-target), like the control plane. If needed, you can disable node auto-upgrades by using maintenance exclusions. You can also manually upgrade this type of node pool.
    * For [Autopilot-managed node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-autopilot-mode-standard-clusters), nodes are automatically upgraded to the version of the control plane over time. You can also manually upgrade this type of node pool.



For both modes of clusters, you can use maintenance windows and exclusions to control the timing and scope of node upgrades, as follows:

  * For clusters enrolled in a release channel, you can use maintenance exclusions to prevent node auto-upgrades until the minor version of the nodes reaches the end of support. You can do this for all nodes in a GKE cluster, or only for specific node pools in Standard clusters with a [node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions).
  * For Standard clusters not enrolled in a release channel ([deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel)), at the cluster level, you can prevent node auto-upgrades for up to 90 days. At the Standard node pool level, you can [disable auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable) until the minor version of the node pool reaches the end of standard support.



Whenever planning to postpone node auto-upgrades, consider the following constraints for the nodes of a GKE cluster:

  * Nodes can't be more than two minor versions behind the control plane version.
  * Nodes can't run a version newer than the cluster's current control plane version.
  * Nodes can't run a minor version that has reached the end of support. For clusters in most release channels, this means the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-standard-support). For clusters enrolled in the Extended channel, this means the [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-extended-support). To check whether a minor version is still supported in your cluster's channel, see the [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).



For more details about these constraints, see the [GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew).

## Automatic cluster upgrades for security and compatibility

If you're preventing cluster upgrades with maintenance windows and exclusions, or you've disabled node auto-upgrades for a specific Standard node pool when your cluster isn't enrolled in a release channel, GKE might automatically upgrade your cluster for security and compatibility purposes in certain cases. Some of the reasons for GKE to upgrade your cluster regardless of these blockers include the following:

  * Cluster control planes running an [end of support version](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).
  * Cluster nodes running end of support versions.
  * State-looping clusters, defined as clusters with looping states from running to degraded, repairing, or suspended and back to running.



For more details, see [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support), and [A managed platform and shared responsibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#managed-shared).

## Upgrades and updates with GKE cluster lifecycle management

In GKE, cluster _upgrades_ and cluster _updates_ have related meanings.

In GKE, the term [_cluster upgrades_](https://docs.cloud.google.com/kubernetes-engine/upgrades)—or just _upgrades_ —refers to updating the Kubernetes version of the control plane (_control plane upgrades_) or nodes (_node upgrades_), or both. When using Standard clusters, node upgrades can also be referred to as _node pool upgrades_ because GKE uses a single operation to upgrade a node pool of nodes.

The term _cluster updates_ —or just _updates_ —is a more general term referring to any type of control plane or node changes, including updating their versions. GKE actively manages your cluster environment by performing upgrades, other types of updates, and necessary maintenance operations. These actions ensure your cluster remains performant, secure, and up-to-date with the latest features and bug fixes. GKE uses tools like [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) and [maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to minimize disruption during these processes.

To learn more about managing all cluster lifecycle changes, including upgrades, see [Manage cluster lifecycle changes to minimize disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters).

## What's next

  * Learn more about [Autopilot cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot).
  * Learn more about [Standard cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).
  * Learn more about [GKE versioning and support](https://docs.cloud.google.com/kubernetes-engine/versioning).
  * Learn more about [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).
  * Learn how to [configure node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
