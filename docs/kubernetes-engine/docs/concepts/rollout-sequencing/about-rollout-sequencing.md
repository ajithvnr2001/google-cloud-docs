---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing/
title: About cluster upgrades with rollout sequencing \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T14:30:27.120083+00:00
---

# About cluster upgrades with rollout sequencing  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About cluster upgrades with rollout sequencing Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Fleet-based rollout sequencingkeyboard_arrow_down

  * [ Rollout sequencing with custom stages ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing)
  * [ Fleet-based rollout sequencing ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing)



You can manage the order of automatic cluster upgrades across Google Kubernetes Engine (GKE) clusters in multiple environments by using rollout sequencing. For example, you can qualify a new version in pre-production clusters before upgrading production clusters. GKE also provides a newer version of this feature, [rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing), which has greater functionality. That version includes more granular control over cluster upgrades, and is recommended for new environments. 

This document assumes that you know about the following:

  * [Cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot)
  * [Fleet management overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)
  * [Release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
  * [Versioning scheme in GKE](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme)
  * [Soak testing](https://en.wikipedia.org/wiki/Soak_testing)

To configure a rollout sequence, see [Sequence the rollout of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing). 

## Overview

GKE rollout sequencing lets you define a specific, ordered sequence for cluster upgrades across environments—such as first upgrading the clusters in the development environment, then the testing environment, and finally production. This progressive strategy provides built-in bake time, letting you discover and mitigate potential issues before the upgrade reaches your most critical systems.

Rollout sequencing is built on the concept of fleets, which are logical groupings of GKE clusters that are mapped to an environment (for example, testing). To use this feature, you define a sequence made up of fleets and set the soak time between each group. When GKE selects a new version, your clusters are upgraded in the defined order, letting you validate workloads before the version is fully deployed to your production environment.

Fleets support lightweight memberships, which let you group clusters logically for rollout sequencing without enabling all fleet-level configurations and features. Lightweight membership is a good choice if you want to use rollout sequencing without some of the other implications of full fleet management, such as fleet-level namespace sameness. For more information, see [Lightweight memberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#lightweight_memberships).

## Choose a rollout sequencing strategy

GKE offers two versions of rollout sequencing. Both versions are built on the same core principles of progressive, fleet-based upgrades, but we recommend using rollout sequencing with custom stages for new environments:

  * **[Rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing) (recommended for new environments):** this version is an evolution of the fleet-based model, offering more granular control and flexibility, but lacking Google Cloud console support. With custom stages, you can define specific stages within a fleet by using labels, making it a good choice for more complex rollout strategies like deploying a new version on a small subset of production clusters before a wider rollout. Additionally, you have more control over rollouts, such as initiating a rollout to a specific version, choosing the types of upgrades to roll out in a sequence, and pausing or canceling rollouts. Choose this option if you're creating a rollout sequence for the first time.
  * **[Fleet-based rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing#fleet-based-sequence):** is the only version of this feature usable with the Google Cloud console, but otherwise has more limited functionality and isn't recommended if you're creating a rollout sequence for the first time.



**The rest of this document pertains only to fleet-based rollout sequencing.**

### Fleet-based rollout sequencing

To automatically upgrade clusters with rollout sequencing, use fleets where you've grouped your clusters with the same release channel and minor version into stages of deployment. Define the sequence of fleets and the soak time that you want between each group of clusters. Then, when GKE selects a new version for automatic upgrades in the release channel, your groups of clusters are upgraded in the sequence you've defined, and you can validate that workloads run as expected with a new version before upgrades begin with your production clusters.

The following diagram illustrates how GKE automatically upgrades clusters in a rollout sequence organized with fleets:

![Fleet-based rollout sequence where you group clusters into fleets.](https://docs.cloud.google.com/static/kubernetes-engine/images/fleet-based-rollout-sequence.svg)**Figure:** A fleet-based rollout sequence

With a fleet-based sequence, when GKE makes available a new upgrade target in the release channel where all clusters in this sequence are enrolled, GKE upgrades these fleets of clusters in this sequence, with the upstream fleet's clusters qualifying the new version for clusters in the downstream fleet, for up to five fleets. Upstream, in a rollout sequence, refers to the previous group, and downstream refers to the next group.

During the configured soak time between fleets, you can confirm that your workloads are running as expected on the upgraded clusters.

## How GKE upgrades clusters in a rollout sequence

When GKE upgrades a cluster, first the control plane is upgraded, then the nodes are upgraded. In a rollout sequence, clusters are still upgraded using this process, but you also control the order in which groups (fleets) of clusters are upgraded. You also specify a soak time that defines how long GKE pauses before upgrades proceed from one group to the next group.

Cluster upgrades in a rollout sequence proceed with the following steps:

  1. GKE starts a new rollout in the rollout sequence. A rollout, by default, is started when GKE sets a new [automatic upgrade target](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#auto-upgrade-target) for clusters on a minor version in a specific release channel. For rollout sequencing with custom stages, you can alternatively [trigger a new rollout](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rolling-out-specific-version) across a rollout sequence to a specific version that you choose.
  2. GKE begins upgrading cluster control planes to the new version in the first group of clusters. After GKE upgrades a cluster's control plane, GKE begins upgrading the cluster's nodes. GKE respects [maintenance availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing#interaction-with-maintenance) when upgrading clusters in a rollout sequence. 

  3. GKE takes the following steps for control plane upgrades:

     1. After all cluster control plane upgrades in the first group finish, GKE begins the soaking period for control plane upgrades. GKE also begins the soaking period if more than 30 days have passed since control plane upgrades began.
     2. After the completion of the soaking period for the first group's cluster control plane upgrades, GKE begins upgrading the second group's control planes to the new version. However, note the following considerations:

        * In some cases, GKE might upgrade the first group's cluster control planes multiple times before it upgrades the second group's cluster control planes. When this situation occurs, GKE chooses the latest version that also has the following attributes: 
          * The version is qualified by the first group.
          * The version is at most one minor version later than the control plane version of the second group's clusters.
        * GKE doesn't upgrade the control plane of clusters in the second group that have a later version than the version qualified by the first group.
  4. In parallel to control plane upgrades, GKE takes the following steps for node upgrades:

     1. After all clusters' node upgrades in the first group finish, GKE begins the soaking period for node upgrades. GKE also begins the soaking period if more than 30 days have passed since node upgrades began.
     2. After the completion of the soaking period for the first group's node upgrades, GKE begins upgrading the second group's nodes to the new version. However, note the following considerations: 
        * In some cases, GKE might upgrade the first group's cluster nodes multiple times before it upgrades the second group's cluster nodes. When this situation occurs, GKE chooses the latest version that also has the following attributes: 
          * The version is qualified by the first group.
          * The version is no later than the second group's cluster control plane version.
        * GKE doesn't upgrade the nodes of clusters in the second group that have a later version than the version qualified by the first group.
  5. GKE repeats these steps from the second group to the third group, until clusters in all groups in the rollout sequence have been upgraded to the new version.




While clusters are upgraded in each group, during the soak time, verify that your workloads with clusters running the new GKE version work as expected.

**Warning:** GKE might be unable to proceed with automatic upgrades in a rollout sequence if there are version discrepancies between clusters across the groups in the sequence. For more information, see [Fleet-based rollout eligibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing#rollout-eligibility). 

Clusters might also be prevented from upgrading due to maintenance windows or exclusions, deprecated API usage, or other reasons.

### How to control upgrades in a rollout sequence

With cluster upgrades in a rollout sequence, groups of clusters are upgraded in the order that you defined, and are soaked in each group for the amount of time that you chose. While upgrades are in progress, you can [check the status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#check-status) and [manage the rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#control-version-rollout) as needed. You can also control the process in the following ways:

  * For a group in a rollout sequence, you can [override the default soak time](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/manage-upgrades-with-rollout-sequencing#change-soak-time) if you need more or less soaking for a specific version.
  * For individual cluster upgrades, you can use the following tools: 
    * [Manually control upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) by taking actions such as canceling, resuming, rolling back, or completing node pool upgrades.
    * Use [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to decide when a cluster can and cannot be upgraded.
    * Configure [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) to balance between speed and risk tolerance, depending on the workloads running on those nodes.



## Example: Community bank gradually rolls out changes from Testing to Production

As an example, the platform administrator at a community bank manages three main deployment environments: Testing, Staging, and Production. Each environment has a group of clusters that is organized in a fleet. As is required for rollout sequencing, the administrator has enrolled each cluster across all three fleets in the same release channel—in these fleets, the [Regular channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels)—with all clusters running the same minor version.

The administrator uses rollout sequencing to define the order in which GKE upgrades clusters in these environments. Ordering the rollout gives the administrator the opportunity to verify that their workloads run as expected with clusters on a new version of GKE before the Production environment is upgraded to the new version. This sequence is illustrated by the fleet-based rollout sequence diagram.

The administrator uses the soak time between the fleets to verify that their workloads run as expected on the new version of GKE. For the Testing fleet, the administrator sets the soak time to 14 days so that they have two full weeks to test out how the workloads run. For Staging, they set the soak time to 7 days as they don't need as much additional time after the workloads have already been running in Testing.

The administrator can also override the default soak time for upgrades to specific versions, which they might want to do in one of the following situations:

  * The administrator finishes qualifying the version before the soak time is complete and wants upgrades to proceed to the next fleet, so they set the soak time to zero.
  * The administrator needs more time to qualify the new version before upgrades proceed to the next fleet as they've noticed an issue with some of their workloads, so they set the soak time to the maximum 30 days.



The administrator uses maintenance windows and exclusions to let GKE upgrade clusters when it is least disruptive for the bank. GKE respects maintenance availability for clusters upgraded in a rollout sequence.

  * The administrator has configured maintenance windows for their clusters so that GKE only upgrades clusters after business hours.
  * The administrator also uses maintenance exclusions to temporarily prevent clusters from being upgraded if they detect issues with the cluster's workloads.



The administrator uses a mix of [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) and [blue-green](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) upgrades for their nodes, balancing between speed and risk tolerance depending on the workloads running on those nodes.

## Fleet-based rollout eligibility

For clusters to be automatically upgraded with rollout sequencing, all clusters across all fleets in a rollout sequence must receive the same upgrade target. Clusters must be enrolled in the same release channel, and we recommend that clusters run the same minor version as upgrade targets are set per-minor version. However, for some releases, like the release in the following example, clusters from multiple minor versions received the same target, meaning that the clusters could be upgraded successfully in the rollout sequence running multiple minor versions.

You can [check the status of version rollout in a sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#check-status) to get more information about the status and if version eligibility issues are preventing upgrades from proceeding. Depending on the version discrepancies, you might need to take actions such as manually upgrading a cluster or removing it from a group for cluster upgrades to proceed. If a cluster in a rollout sequence doesn't have an eligible upgrade target, GKE won't auto-upgrade the cluster until the cluster's existing minor version reaches [end of support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).

To troubleshoot rollout eligibility, see [Troubleshoot rollout eligibility](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#troubleshoot-rollout-eligibility).

#### Example GKE release

As an example, the [2025-R45](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#2025-r45-version-updates) release set an upgrade target for multiple minor versions in clusters enrolled in the Regular channel. An upgrade target can be a new minor version (1.30 to 1.31), or just a new patch version (1.31.x-gke.x to 1.31.13-gke.1023000). In this release, in the Regular channel, the following new versions were made available for clusters on specific minor versions:

  * Clusters on 1.30 were upgraded to 1.31.13-gke.1023000.
  * Clusters on 1.31 were upgraded to 1.32.9-gke.1108000.
  * Clusters on 1.32 were upgraded to 1.33.5-gke.1162000.



### The most-upstream group receives all upgrade targets

For clusters in the first group in a sequence, which does not have an upstream group to qualify new versions, GKE upgrades any clusters with eligible upgrade targets, regardless of if those upgrade targets are different from each other. For example, in the first group of a sequence, if some clusters were running 1.30, those clusters could be upgraded to 1.31.13-gke.1023000, and clusters running 1.32 could be upgraded to 1.33.5-gke.1162000. This is because, for the first group in a sequence, GKE considers all upgrade targets to be qualified for these clusters as there is no upstream group to qualify a new version.

### An upstream group must qualify only one version

For clusters in any downstream group to begin upgrading, the upstream group must have successfully qualified a single, common upgrade target for which all clusters in the downstream group are eligible. If the upstream group has clusters that have successfully upgraded to two different versions (as can happen when the upstream group is the first group in a sequence), then the upstream group qualifies the lower of the two versions as the common upgrade target for the downstream group. For example, if the upstream group has some clusters that upgraded to 1.31.13-gke.1023000 and other clusters upgraded to 1.33.5-gke.1162000, then the group qualifies 1.31.13-gke.1023000 as the common upgrade target for the downstream group.

### Clusters running versions later than the upgrade target don't prevent upgrades

If a downstream group has clusters which run a later version than the upgrade target qualified by an upstream group, GKE upgrades the clusters eligible for the upgrade target and ignores the clusters already on a later version. This behavior doesn't prevent the rollout sequence from progressing, as long as at least one cluster in the downstream group is eligible for the upgrade target.

For example, if the upstream group qualified the upgrade to 1.32, and the downstream group has clusters running 1.31 and 1.33, GKE upgrades the clusters running 1.31 to 1.32, and ignores the clusters running 1.33.

### An upstream group must qualify a version matching with the next group's clusters

If clusters in an upstream group qualified a different version than the one for which clusters in the next group were eligible, GKE also cannot automatically upgrade the clusters in any downstream groups.

For example, if all clusters in the first group were upgraded to 1.31.13-gke.1023000, but the clusters in the second group were running a newer version, such as 1.32.9-gke.1108000, the second group's clusters wouldn't be automatically upgraded. The first group qualified 1.31.13-gke.1023000, but the clusters in the second group (currently on 1.32) are only eligible for the upgrade target 1.33.5-gke.1162000, so GKE cannot automatically upgrade these clusters. To advance upgrades in this situation, see [Fix eligibility between groups](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/manage-upgrades-with-rollout-sequencing#eligibility-between-groups).

### The upstream group qualified multiple upgrade targets for the downstream group

If GKE upgraded the clusters in the upstream group multiple times before upgrading the clusters in the downstream group, GKE upgrades the clusters in the downstream group to the latest version qualified by the upstream group, for which the clusters in the downstream group are eligible. For control plane upgrades, this version can be at most one minor version later than the control plane version of the clusters in the downstream group. For node upgrades, this version can be equal to, but not later than the control plane version of the clusters in the downstream group.

For example, this scenario is relevant if you've configured maintenance exclusions to temporarily prevent upgrades for your downstream group, which includes your production clusters. However your upstream group, which includes pre-production clusters, didn't also use maintenance exclusions to prevent upgrades. So, your upstream group was upgraded multiple times, qualifying multiple potential upgrade targets, while your downstream group wasn't upgraded.

## Upgrades not completed within 30 days will be force soaked to unblock the sequence

To ensure that a rollout sequence finishes upgrading clusters, GKE starts the soaking period for a group if the control plane or node upgrades, respectively, are not completed across all clusters within the maximum upgrade time (30 days). The upgrades for any remaining clusters in the group can still continue during the soaking period. For more information, see the row for `FORCED_SOAKING` in [Status information for a rollout sequence table](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#status-details).

## How fleet-based rollout sequencing works with other upgrade features

Rollout sequencing is one feature in a collection of features that give you control over the upgrade aspect of the cluster lifecycle. This section explains how this feature works with some of the other available features related to cluster upgrades.

### How fleet-based rollout sequencing works with maintenance windows and exclusions

GKE respects [maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows) and [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) when upgrading clusters with rollout sequencing. GKE only starts a cluster upgrade within a cluster's maintenance window. You can use a maintenance exclusion to temporarily prevent a cluster from being upgraded. If GKE cannot upgrade a cluster due to a maintenance window or exclusion, this circumstance can prevent cluster upgrades from finishing in a group. If a cluster upgrade cannot be completed within 30 days due to maintenance windows or exclusions, the group will enter its soak phase regardless of whether all clusters have finished upgrading.

You can use maintenance exclusions as a temporary measure to prevent a sequence from completing a rollout to a group and moving onto the next group. For more information, see [Delay the completion of group's version rollout](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing#delay-rollout).

### How fleet-based rollout sequencing works with deprecation usage detection

GKE pauses cluster upgrades when it detects usage of certain deprecated APIs and features. Automatic upgrades are also paused for clusters in a group in a rollout sequence. For more information, see How [Kubernetes deprecations work with GKE](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#how_kubernetes_deprecations_work_with).

### How rollout sequencing works with node upgrade strategies

Node upgrades will use their configured node upgrade strategy when being upgraded in a rollout sequence. As with cluster upgrades without rollout sequencing, GKE uses surge upgrades for Autopilot nodes. For more information, see [Automatic node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#node_pool_upgrades).

If node upgrades cannot complete within 30 days, the group will enter its soak phase regardless of whether all clusters have finished upgrading. This behavior can happen if the node upgrade strategy causes a Standard cluster's node upgrade to take longer to complete, especially if it is a large node pool. It can also be exacerbated by maintenance windows not big enough for a node upgrade to complete.

### How rollout sequencing works with release channels

[Release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels) are required to use rollout sequencing. All clusters in all groups in a rollout sequence must be on the same release channel.

## Receiving multiple upgrades across a sequence

If a new version becomes an upgrade target on the release channel while cluster upgrades to a previous upgrade target are still proceeding in the rollout sequence, an upstream group can begin the rollout of a new version while a downstream group is still receiving the previous upgrade. For example, if the third group in a sequence is rolling out 1.31.12-gke.1265000, the first group in the sequence can concurrently be rolling out 1.31.13-gke.1008000.

## Considerations when choosing fleet-based rollout sequencing

Consider using rollout sequencing if you want to manage cluster upgrades by qualifying new versions in one environment before rolling it out to another.

However, this strategy might not be the right choice for your environment if any of the following statements are true:

  * You have clusters that are not on the same release channel or minor version in the same production environment.
  * You need to automate upgrades that cannot be mapped to only five stages of deployment, as you can only create a rollout sequence with up to five groups of clusters. You cannot link groups in multiple rollout sequences to create a rollout sequence with more than five groups. Fleet-based sequences can include up to five fleets.
  * You frequently perform manual upgrades that cause clusters in one group to have different automatic upgrade target versions.



## Limitations of fleet-based rollout sequencing

To successfully upgrade your clusters with rollout sequencing, you must adhere to the following limitations:

  * Ensure that all clusters in a rollout sequence are enrolled in the same release channel and don't use [accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch). We also recommend that all clusters run the same minor version, in order to qualify one upgrade target. For more information, see Rollout eligibility.
  * Create a linear rollout sequence without cycles (a group has a downstream group as its upstream group) or branches (a group has more than one downstream group).
  * Create a rollout sequence between clusters in the same organization. You can't create sequences with clusters across multiple organizations.



## Known issues with fleet-based rollout sequencing

  * If a group contains clusters from different locations, a cluster upgrade might temporarily only be available to some of the clusters due to the gradual rollout of the new version. This behavior is more likely to happen to the first group of clusters and should resolve within a week.
  * If there is an empty group in a rollout sequence, how this affects version qualification depends on the following conditions: 
    * If the empty group has no upstream group, then cluster upgrades do not proceed to the downstream group as the empty group cannot qualify versions.
    * If the empty group has an upstream group, all pending cluster upgrades enter the `COMPLETE` status and propagate to the downstream group.



## What's next

  * [Sequence the rollout of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing/manage-upgrades-with-rollout-sequencing).
  * Learn about [rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
