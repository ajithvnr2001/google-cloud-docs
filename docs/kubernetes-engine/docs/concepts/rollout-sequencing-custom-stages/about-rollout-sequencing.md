---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing/
title: About rollout sequencing with custom stages \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:02.032921+00:00
---

# About rollout sequencing with custom stages  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About rollout sequencing with custom stages Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Rollout sequencing with custom stageskeyboard_arrow_down

  * [ Rollout sequencing with custom stages ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing)
  * [ Fleet-based rollout sequencing ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing)



You can manage the order of automatic cluster upgrades across Google Kubernetes Engine (GKE) clusters in multiple environments by using rollout sequencing. For example, you can qualify a new version in pre-production clusters before upgrading production clusters. GKE also provides an earlier version of this feature, [fleet-based rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing), which has more limited functionality and isn't recommended for new environments. 

This document assumes that you know about the following:

  * [Cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot)
  * [Fleet management overview](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs)
  * [Release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels)
  * [Versioning scheme in GKE](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme)
  * [Soak testing](https://en.wikipedia.org/wiki/Soak_testing)

To configure a rollout sequence, see [Sequence the rollout of cluster upgrades with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing). 

## Overview

GKE rollout sequencing lets you define a specific, ordered sequence for cluster upgrades across environments—such as first upgrading the clusters in the development environment, then the testing environment, and finally production. This progressive strategy provides built-in bake time, letting you discover and mitigate potential issues before the upgrade reaches your most critical systems.

Rollout sequencing is built on the concept of fleets, which are logical groupings of GKE clusters that are mapped to an environment (for example, testing). To use this feature, you define a sequence made up of fleets and set the soak time between each group. When GKE selects a new version, your clusters are upgraded in the defined order, letting you validate workloads before the version is fully deployed to your production environment.

Fleets support lightweight memberships, which let you group clusters logically for rollout sequencing without enabling all fleet-level configurations and features. Lightweight membership is a good choice if you want to use rollout sequencing without some of the other implications of full fleet management, such as fleet-level namespace sameness. For more information, see [Lightweight memberships](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/fleet-creation#lightweight_memberships).

## Choose a rollout sequencing strategy

GKE offers two versions of rollout sequencing. Both versions are built on the same core principles of progressive, fleet-based upgrades, but we recommend using rollout sequencing with custom stages for new environments:

  * **[Rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing) (recommended for new environments):** this version is an evolution of the fleet-based model, offering more granular control and flexibility, but lacking Google Cloud console support. With custom stages, you can define specific stages within a fleet by using labels, making it a good choice for more complex rollout strategies like deploying a new version on a small subset of production clusters before a wider rollout. Additionally, you have more control over rollouts, such as initiating a rollout to a specific version, choosing the types of upgrades to roll out in a sequence, and pausing or canceling rollouts. Choose this option if you're creating a rollout sequence for the first time.
  * **[Fleet-based rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing#fleet-based-sequence):** is the only version of this feature usable with the Google Cloud console, but otherwise has more limited functionality and isn't recommended if you're creating a rollout sequence for the first time.



**The rest of this document pertains only to rollout sequencing with custom stages.**

### Rollout sequencing with custom stages

When you use rollout sequencing with custom stages, you define the order of fleet upgrades and set soak times. Additionally, you can also do the following:

  * Define a sequence with granular stages that can target specific subsets of clusters within a fleet by using labels, making it a good choice for strategies like phased rollouts.
  * Gain more control and observability through the new `RolloutSequence` and `Rollout` API objects.



This method provides the most flexibility and granular control over your cluster upgrades. To target specific subsets of clusters within a fleet, you use a `label-selector` to target only the clusters that have specific Kubernetes labels.

The following diagram illustrates how GKE automatically upgrades clusters in a rollout sequence that uses custom stages. The stage targets clusters with a `label-selector` named `canary` in the `prod` fleet:

![Rollout sequence with custom stages in GKE.](https://docs.cloud.google.com/static/kubernetes-engine/images/rollout-sequence-stages.png)**Figure:** A rollout sequence with custom stages

When GKE rolls out a new version, GKE upgrades the clusters in the Testing fleet first, followed by clusters in the Staging fleet. Then, in the Production fleet, GKE prioritizes clusters that match the `label-selector`. Because `prod-cluster-1` is labeled with `canary: true`, GKE upgrades this cluster next. GKE upgrades all remaining clusters in the Production fleet (in the Main stage) at the end of the process because this stage doesn't have any label selector.

During the configured soak time between stages, you can confirm that your workloads are running as expected on the upgraded clusters. The preceding example shows one custom stage in the Production fleet, but you can add multiple stages to any fleet or use only one fleet with multiple stages.

### Key concepts

  * **Soak time** : a configurable waiting period that occurs after all clusters in a stage are upgraded. This soak time lets you validate the new version in one environment and catch potential issues before the upgrade proceeds to the next environment. You can configure a soak time of up to 30 days for each stage in your sequence. A longer soak time in a pre-production stage gives you more time for validation.
  * **`RolloutSequence`** : this object is the primary resource that you use to define your upgrade sequence. `RolloutSequence` contains an ordered series of stages, which verifies that clusters in earlier stages are fully upgraded and have completed their soak period before the upgrade proceeds to the next stage. Each `RolloutSequence` has one `Rollout` for each new version rolled out.
  * **`Rollout`** : this object lets you observe the progress of a single version upgrade through your sequence. You can use `Rollout` to view the status of the rollout, track the progress, and see if and why any clusters are ineligible for upgrade. Each `Rollout` is associated with a specific `RolloutSequence` representing the sequence where the version rolls out.
  * **Dedicated host project** : we recommend that you use a dedicated Google Cloud project to host your `RolloutSequence` object. Placing the sequence in a dedicated project provides a neutral, central point of control for your rollout sequence, which is a similar best practice for managing CI/CD pipelines.

**Best practice** : 

Create and manage your `RolloutSequence` resource in a dedicated host project.

  * **Stages** : a stage is a step in the rollout sequence. Each stage contains a group of clusters that are upgraded together.
  * **Fleets** : fleets are the primary way to group clusters. A stage in a rollout sequence can reference one or more fleets. A single rollout sequence can include fleets that are hosted across multiple Google Cloud organizations.
  * **Label selectors** : a rollout sequence is composed of one or more stages. Each stage contains clusters from one or more fleets, and you can use label selectors on clusters to further split a fleet into multiple stages. This approach allows for strategies like phased rollouts, where a small subset of production clusters are upgraded first.



## How GKE upgrades clusters in a rollout sequence

When GKE upgrades a cluster, first the control plane is upgraded, then the nodes are upgraded. In a rollout sequence, clusters are still upgraded using this process, but you also control the order in which groups (fleets) of clusters are upgraded. You also specify a soak time that defines how long GKE pauses before upgrades proceed from one group to the next group.

Cluster upgrades in a rollout sequence proceed with the following steps:

  1. GKE starts a new rollout in the rollout sequence. A rollout, by default, is started when GKE sets a new [automatic upgrade target](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#auto-upgrade-target) for clusters on a minor version in a specific release channel. For rollout sequencing with custom stages, you can alternatively [trigger a new rollout](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rolling-out-specific-version) across a rollout sequence to a specific version that you choose.
  2. GKE begins upgrading cluster control planes to the new version in the first group of clusters. After GKE upgrades a cluster's control plane, GKE begins upgrading the cluster's nodes. GKE respects [maintenance availability](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#interaction-with-upgrade-features) when upgrading clusters in a rollout sequence. 

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

**Warning:** GKE might be unable to proceed with automatic upgrades in a rollout sequence if there are version discrepancies between clusters across the groups in the sequence. For more information, see [Rollout eligibility](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing#rollout-eligibility). 

Clusters might also be prevented from upgrading due to maintenance windows or exclusions, deprecated API usage, or other reasons.

### How to control upgrades in a rollout sequence

With cluster upgrades in a rollout sequence, groups of clusters are upgraded in the order that you defined, and are soaked in each group for the amount of time that you chose. For more information about controlling this process, see the following:

  * To learn about managing the rollout of a specific version, see Managing a rollout.
  * To learn about managing the rollout sequence for all rollouts, see Managing a rollout sequence. 



## Example: Community bank gradually rolls out changes from Testing to Production

A platform administrator at a community bank manages three main deployment environments: Testing, Staging, and Production. The Production clusters are distributed across multiple regions, with varying levels of criticality. To manage upgrades effectively, the administrator groups the clusters in each environment into fleets. As required for rollout sequencing, each cluster across all three fleets is enrolled in the same release channel—in this case, the Regular channel—and all clusters run the same minor version.

The administrator's primary goal is to ensure that new GKE versions are thoroughly vetted before reaching the bank's critical production environment. They also want to progressively upgrade clusters in a lower-traffic region first, then move to a higher-traffic region, and finally to their most critical region. To achieve this, they use rollout sequencing with custom stages to define a progressive upgrade strategy that includes labeling the production clusters according to their region. This approach lets them validate a new version on a small subset of production traffic before a full rollout.

To implement this plan, the administrator applies the following labels to the clusters in the Production fleet:

  * Clusters in `us-west1` (lower traffic) are labeled with `prod-region: us-west1`.
  * Clusters in `europe-west1` (higher traffic) are labeled with `prod-region: europe-west1`.
  * Clusters in `us-east1` (most critical traffic) are not labeled. The final stage for a fleet within a sequence must act as a 'catch-all' for all remaining clusters. Therefore, the administrator doesn't need to add labels to these remaining clusters.



Next, in a dedicated host project used for managing CI/CD configurations, they define a `RolloutSequence` object. This new sequence has five distinct stages:

  1. **Testing** : this stage includes all clusters in the `testing` fleet. The administrator sets a three-day soak time to allow for thorough validation.
  2. **Staging** : this stage includes all clusters in the `staging` fleet, with a three-day soak time.
  3. **Production in region`us-west1`**: this stage targets the production fleet, but uses a `label-selector` to include only the clusters with the `prod-region: us-west1` label. This stage lets the administrator to monitor for any issues on a small subset of production clusters with a three-day soak time.
  4. **Production in region`europe-west1`**: this stage includes the clusters in the `production` fleet that have the `prod-region: europe-west1` label. The administrator sets a longer four-day soak time for more thorough validation.
  5. **Production in region`us-east1`**: this final stage includes the remaining clusters in the `production` fleet; that is, all clusters in `us-east1`.



This approach gives the administrator granular control over their production upgrades, significantly improving the safety and reliability of their upgrade process by catching potential issues before they can impact the entire production environment.

During a routine patch upgrade, the bank's automated tests complete successfully in the staging environment much faster than anticipated. The administrator observes that the new version is stable and decides that the three-day soak time after the Staging fleet upgrade is unnecessarily long for this type of routine update.

To accelerate this rollout, the administrator modifies the `RolloutSequence` definition and reduces the soak duration for the `us-west1` stage of the Production fleet. Because this change to the `RolloutSequence` definition updates the default soak time for all current and future rollouts, the administrator makes a note to revert the soak time back to the original three-day period after this specific patch rollout is complete. This approach helps ensure that their standard, more cautious soak time is in place for future minor version upgrades.

The administrator uses [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) so that GKE upgrades clusters when it is least disruptive for the bank. GKE respects maintenance availability for clusters upgraded in a rollout sequence:

  * The administrator configured maintenance windows for their clusters so that GKE upgrades clusters only after business hours.
  * The administrator also uses maintenance exclusions to temporarily prevent clusters from being upgraded if they detect issues with the cluster's workloads.



Additionally, the administrator can manage a rollout through actions such as pausing a rollout if they detect issues, or completing a stage if they're confident with the changes in that stage and are ready to proceed immediately.

The administrator uses a mix of [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge) and [blue-green](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) upgrades for their nodes, balancing between speed and risk tolerance depending on the workloads running on those nodes.

## How GKE starts the rollout of a new version

By default, GKE creates a new rollout when setting a new automatic upgrade target. The version that GKE selects to roll out depends on the minor version and release channel of the clusters in the sequence. For example, if your clusters are running GKE version 1.35 in the Regular channel and GKE sets an auto-upgrade target to 1.35.5-gke.1000000, GKE creates a new `Rollout`.

However, you can also choose a version that you'd like GKE to roll out.

### Rolling out a specific version

You can also initiate a rollout to a specific version, if, for example, you want to quickly patch a security vulnerability, or fix a critical issue with your GKE clusters. This action creates a `Rollout` object, initiating a rollout across your rollout sequence in the same way as when GKE sets an automatic upgrade target. To roll out a new version, see [Roll out a specific version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#roll-out-specific-version).

If you need to roll out a new version to a cluster as quickly as possible, you can alternatively perform [manual cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) for the individual clusters. Manual cluster upgrades are performed at the cluster level.

## Choosing what types of upgrades GKE performs in a rollout sequence

By default, GKE rolls out all types of cluster upgrades to a rollout sequence, including both patch version and minor version upgrades to the control plane and nodes.

There are four main types of upgrades:

  * Patch version upgrades of the control plane
  * Patch version upgrades of the nodes
  * Minor version upgrades of the control plane
  * Minor version upgrades of the nodes



You can restrict the scope of cluster upgrades in a rollout sequence to only perform specific types of upgrades. For example, if you want GKE to roll out only control plane upgrades, and not node upgrades, you can specify this for your rollout sequence.

If you restrict the scope of cluster upgrades for a rollout sequence, GKE won't perform that type of automatic upgrade for any clusters in the rollout sequence, except for mandatory automatic upgrades as required. For more information, see Rollouts for mandatory automatic upgrades. Restricting the scope of cluster upgrades doesn't cancel ongoing rollouts of the type that you restrict, it only prevents GKE from creating future rollouts of that type.

Because GKE won't upgrade the nodes of a cluster to a version later than the control plane, restricting the scope of control plane upgrades can also restrict node upgrades.

To restrict the scope of automatic upgrades in a rollout sequence, see [Choose what types of upgrades GKE performs in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#choose-type-of-upgrades-scope).

Restricting the scope of a rollout sequence works similarly to [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions), but maintenance exclusions are either set for individual clusters or node pools within a cluster.

## Rollouts for mandatory automatic upgrades

Whether your cluster is enrolled in a rollout sequence, GKE performs [automatic cluster upgrades for security and compatibility](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades_for_security_and_compatibility). If the clusters in your rollout sequence haven't had their control planes upgraded in 90 days, or if the clusters are running a minor version that has reached the end of support, GKE creates a mandatory rollout to perform auto-upgrades. These rollouts help to ensure that your cluster remains performant, available, and secure. GKE creates rollouts for these scenarios, regardless of restrictions on the scope of rollouts, [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions), or any other reasons for delay.

You can't pause or cancel these types of rollouts. GKE performs these types of cluster upgrades regardless of rollout sequence enrollment.

For more information about these policies, see the following sections:

  * [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support)
  * [Control plane patch 90-day policy](https://docs.cloud.google.com/kubernetes-engine/versioning#kcp-patch-policy)



## Rollout eligibility

For a version to be rolled out through a sequence that uses custom stages, clusters must be eligible for an upgrade target from their release channel. When a new GKE version becomes available, the system creates a `Rollout` object if clusters in the sequence are eligible for the new version. Although we recommend that all clusters are enrolled in the same release channel, if they are not, GKE selects a version from the most conservative channel in the sequence. For example, if clusters are mixed between Stable and Regular channels, GKE chooses the version from the Stable channel.

The `Rollout` then progresses through the stages defined in your `RolloutSequence`. Within a given stage, the control plane rollout and node pool rollout can run in parallel. A key rule governing this progression is that while a stage is in a `SOAKING` state with a particular version, the stage is not eligible to begin a new `Rollout` for a newer version. This practice helps ensure that a version is fully validated before the next upgrade begins. You can observe the progress and eligibility of each cluster by monitoring the `Rollout` object. If you find version discrepancies that make a cluster ineligible, you might need to take action, such as manually upgrading the cluster or ignoring a cluster in a rollout sequence, to allow the rollout to proceed. If a cluster is not eligible for any rollouts, GKE won't automatically upgrade the cluster until it needs to create rollouts for mandatory automatic upgrades, as described in the previous section.

### Clusters running versions later than the upgrade target don't prevent upgrades

If a stage in the sequence contains clusters that run a later version than the target version of a rollout, GKE upgrades the clusters eligible for the target version and ignores the clusters that are already on a later version. This behavior doesn't prevent the rollout sequence from progressing to the next stage.

For example, if the target version of a rollout for a stage is 1.32, and that stage has clusters that run both 1.31 and 1.33, GKE upgrades the clusters on version 1.31 to 1.32, and ignores the clusters that are already on version 1.33.

### The preceding stage qualified multiple upgrade targets for the subsequent stage

A preceding stage in a sequence might complete rollouts for multiple new versions while a subsequent stage is paused (for example, by a maintenance exclusion) or is still processing a previous upgrade. In this case, when the subsequent stage becomes ready to accept a new upgrade, GKE upgrades the stage to the latest version that was qualified. For control plane upgrades, this version can be at most one minor version later than the control plane version of the clusters in the subsequent stage. For node upgrades, this version can be equal to, but not later than, the control plane version of the clusters in the subsequent stage.

For example, this scenario is relevant if you configured maintenance exclusions to temporarily prevent upgrades on your production clusters. If your pre-production clusters didn't have the same maintenance exclusions, these clusters might be upgraded multiple times, qualifying several new versions, but your production stages are not upgraded.

## Forced soaking after 30 days

To help ensure that a rollout sequence finishes upgrading clusters, GKE starts the soaking period for a group if the control plane or node upgrades, respectively, are not completed across all clusters within the maximum upgrade time (30 days). The upgrades for any remaining clusters in the group can still continue during the soaking period.

## How rollout sequencing works with other upgrade features

Rollout sequencing works together with other GKE upgrade features:

  * **Maintenance windows and exclusions** : you can still use maintenance windows and exclusions to control when upgrades can and cannot occur on your clusters. GKE starts a cluster upgrade only within a cluster's maintenance window. You can use a maintenance exclusion to temporarily prevent a cluster from being upgraded. Both of the following methods can restrict GKE to performing certain types of upgrades:

    * **Cluster or node pool level** : maintenance exclusions
    * **Rollout sequence level** : choosing what types of upgrades GKE performs in a rollout sequence

However, neither of these methods that restrict the scope of cluster upgrades prevent mandatory automatic upgrades. If GKE cannot upgrade a cluster due to a maintenance window or exclusion, this circumstance can prevent cluster upgrades from finishing in a stage. If a cluster upgrade cannot be completed within 30 days due to maintenance windows or exclusions, the stage will enter its soak phase regardless of whether all clusters have finished upgrading.

  * **Node upgrade strategies** : rollout sequencing does not affect your configured [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) (for example, blue-green upgrades). Similar to cluster upgrades that don't have rollout sequencing, GKE uses surge upgrades for Autopilot nodes. For more information, see [Automatic node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#node_pool_upgrades).

If node upgrades cannot complete within 30 days, the group will enter its soak phase regardless of whether all clusters have finished upgrading. This behavior can happen if the node upgrade strategy causes a Standard cluster's node upgrade to take longer to complete, especially if it is a large node pool. The situation can also be exacerbated by maintenance windows that aren't big enough for a node upgrade to complete.

  * **Release channels** : we recommend that you enroll all clusters in a rollout sequence in the same release channel.

  * **Deprecation usage detection** : GKE's deprecation usage detection still functions as expected, potentially pausing upgrades on clusters that use a deprecated API.

  * **Manual upgrades** : manually upgrading clusters in the first stage of a sequence does not, by itself, qualify that version or trigger a rollout to proceed. The automated rollout process is driven by the official auto-upgrade targets set for the release channel. A manual upgrade updates the clusters, but the sequence begins to advance for that version only after it becomes the designated auto-upgrade target.

  * **Cluster notifications** : GKE provides notifications for rollout sequencing, in addition to other available cluster notifications. For more information, see Notifications for rollout sequencing.




## Receiving multiple upgrades across a sequence

A release channel selects an upgrade target for the cluster. If a new version becomes available while upgrades to a previous target are still in progress, the first stage can begin the rollout of a new version even when later stages still receive the previous upgrade. For example, if the third group in a sequence is rolling out version 1.31.12-gke.1265000, the first group in the sequence can concurrently roll out version 1.31.13-gke.1008000.

## Considerations when choosing rollout sequencing

Consider using rollout sequencing if you want to manage cluster upgrades by qualifying new versions in one environment before you roll it out to another.

However, this strategy might not be the right choice for your environment if any of the following statements are true:

  * You have clusters that are not on the same release channel or minor version in the same production environment.
  * You frequently perform manual upgrades that cause clusters in one group to have different automatic upgrade target versions.



## Notifications for rollout sequencing

GKE sends cluster notifications, which provide critical information about cluster upgrades at the cluster level. Additionally, GKE provides notifications about rollout sequences with custom stages, and the rollouts that take place with those rollout sequences. For example, GKE sends notifications when a rollout stage starts, completes, or is blocked. Or, GKE sends a notification if you've misconfigured a rollout sequence. For more information, see the [Cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications) document, and its respective sections for [`RolloutEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#rollout-event) and [`RolloutSequenceEvent`](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#rollout-sequence-event).

## Managing a rollout

When GKE rolls out a new version across the clusters in your rollout sequence, you can use the following actions to exercise control over the process while you assess how your cluster and workloads respond to the change. Additionally, you can create a new rollout to roll out a specific version.

While upgrades are in progress, you can [check their status](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#check-status-rollout-sequence). Based on how the upgrade is proceeding, you can use the actions explained in the following subsections.

### Pausing a rollout

You can pause an in-progress rollout. If, for example, you noticed a potential issue with your clusters and the new version being rolled out, you can temporarily pause the rollout. GKE won't start new upgrade operations to this version, letting you investigate any issue, as needed. GKE won't stop ongoing upgrade operations, but it won't start new ones, including for subsequent stages.

To pause a rollout, see [Pause a rollout](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#pause-a-rollout).

After you pause a rollout, you can either resume or cancel the rollout. A rollout can be paused for up to 90 days. After 90 days, GKE cancels the rollout.

Pausing a rollout doesn't prevent subsequent rollouts from starting. However, these rollouts won't overtake the paused rollout stage. For example, if GKE already rolled out 1.34.8-gke.1000000 to the first and second stages, and you pause the rollout on the third stage, GKE can start a new rollout to 1.35.5-gke.1163000 and upgrade clusters in the first two stages. However, GKE won't start upgrades to 1.35.5-gke.1163000 on the third stage until the rollout of 1.34.8-gke.1000000 completes on the third stage or is cancelled.

If there are multiple rollouts in progress for a rollout sequence, and you want to pause all of them, you must pause each rollout individually. If you want to prevent GKE from starting additional rollouts, you can choose what types of upgrades GKE performs in a rollout sequence.

### Resuming a rollout

You can resume a paused rollout that's been paused for less than 90 days, after you've investigated any potential issues and are ready for upgrades to proceed. You can only resume a paused rollout if another rollout of the same type (control plane rollout or node rollout) isn't running at the same time on the same stage. You can also resume a rollout that was automatically paused by GKE for technical or business reasons, although we recommend caution before doing so.

If you resume the rollout, GKE starts new upgrade operations to continue rolling out the new version across the stages of the rollout sequence.

To resume a rollout, see [Resume a rollout](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#resume-a-rollout).

### Canceling a rollout

You can cancel a rollout, including rollouts that are active or have been paused. When you cancel a rollout, GKE won't automatically create a new rollout to the same version. However, canceling a rollout doesn't prevent GKE from rolling out later versions. If you want to stop GKE from also rolling out any later versions, cancel all ongoing rollouts and restrict the scope of cluster upgrades in the rollout sequence.

To cancel a rollout, see [Cancel a rollout](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#cancel-a-rollout).

If you need to roll out the same version that was canceled, [roll out a specific version](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#roll-out-specific-version).

### Completing a rollout stage

If you're confident that the rollout of a version can proceed to the next stage in the rollout sequence because, for example, you've completed your testing at that stage, you can manually progress your rollout by completing the stage. If you complete the stage, any clusters that GKE hasn't yet upgraded won't be upgraded as part of that rollout. Completing the stage also skips any remaining soaking time. This action also means that you don't have to change the soak time at the rollout sequence level.

To complete a rollout stage, see [Complete a rollout stage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#complete-a-rollout-stage).

### Managing a rollout through changing the rollout sequence

You can also manage a rollout by taking actions that affect the entire rollout sequence. However, consider taking the actions described in the previous sections before doing so, such as pausing a rollout. Some changes to a rollout sequence can cause ongoing rollouts to be cancelled, in addition to affecting how future rollouts work in the sequence. If you want to change only one rollout, use the provided tools to manage one rollout, instead of changing the entire sequence.

However, if you do want to change how a rollout sequence functions for all rollouts—not only the rollout of one new version—see the following section, Managing a rollout sequence.

### Control individual cluster upgrades to manage the rollout

For individual cluster upgrades, you can use the following tools to manage upgrades:

  * [Manually control upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) by taking actions such as canceling, resuming, rolling back, or completing node pool upgrades.
  * Use maintenance windows and exclusions to decide when a cluster can and cannot be upgraded.
  * Configure [node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) to balance between speed and risk tolerance, depending on the workloads running on those nodes.



For more information, see How rollout sequencing works with other upgrade features.

## Managing a rollout sequence

To [manage a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#managing-rollout-sequence), you can do basic actions such as the following:

  * List your rollout sequence
  * Describe a rollout sequence



Additionally, you can perform actions such as modifying a rollout sequence, and ignoring a cluster in a rollout sequence. These actions are described in the following subsections.

To learn more about managing a rollout of one version instead of the entire rollout sequence, see the previous section, Managing a rollout.

### Ignoring a cluster in a rollout sequence

By default, any clusters that are part of a fleet in a rollout sequence are upgraded as part of the rollout sequence. You can add clusters to specific stages, or any clusters that are in a fleet and are not labeled will be upgraded together.

However, if you have a cluster that you don't want to include in the rollout sequence, you can label it so that GKE ignores the cluster when rolling out new versions. You might need to do this, if, for example, you need additional time before upgrading that specific cluster. You can ignore one or more clusters in a rollout sequence.

If you ignore a cluster in a rollout sequence, GKE won't consider it when rolling out a new version, and won't perform automatic upgrades for the cluster, except for mandatory automatic upgrades including [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support) and [automatic upgrades for control planes that haven't been upgraded in 90 days](https://docs.cloud.google.com/kubernetes-engine/versioning#kcp-patch-policy).

To ignore a cluster in a rollout sequence, see [Ignore a cluster in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#ignore-cluster).

### Modifying a rollout sequence

If you want to change how rollouts proceed in an existing rollout sequence, you can modify the sequence in one of two ways:

  * Modify a rollout sequence by editing the YAML configuration file where you defined the sequence.
  * Modify the clusters in the sequence.



The following happens if you modify a rollout sequence:

  * If you add a stage, remove a stage, change the order of stages, or edit a stage—for example, to change the project ID or label selectors of that stage—in a rollout sequence, GKE cancels all active rollouts.
  * If you change the soak time of a stage, GKE doesn't cancel active rollouts.



To modify a rollout sequence, see [Modify a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#modifying-rollout-sequence).

The following happens if you modify the clusters in a sequence:

  * If you remove a cluster from a rollout sequence by removing it from a fleet, active rollouts continue. GKE can automatically upgrade the cluster based on typical procedures for clusters not enrolled in a sequence.
  * If you add a cluster to a fleet in a rollout sequence, GKE upgrades this cluster as part of any active rollouts that haven't yet passed the stage where you added it. However, if the stage has been completed for the rollout, GKE won't upgrade the cluster in that rollout.

To create a cluster that immediately matches the target version of a rollout stage, set the `--cluster-version` flag to `upgrade-target` ([Preview](https://cloud.google.com/products#product-launch-stages)) when creating the cluster. If you [register this cluster to a specific stage in a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#configure-rollout-sequence) when you create the cluster, GKE identifies the target version for that stage and creates the cluster with that version.

For instructions, see [Create a cluster that matches the target version of a rollout stage](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing#create-cluster-target-version-rollout-stage).

  * If you move a cluster to a different stage without editing the rollout sequence configuration, the following happens, depending on whether the stage you move the cluster to has completed:

    * If you move a cluster to a stage that already completed its rollout, GKE doesn't upgrade the cluster in that rollout.
    * If you move a cluster that was already upgraded in a rollout to a later unfinished stage, GKE ignores the cluster and won't interrupt the progress of the rollout.



To modify the clusters in a sequence, see [Register a cluster on Google Cloud to your fleet](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/register/gke).

## Limitations

The following limitations apply when you upgrade your clusters by using rollout sequencing with custom stages:

  * You can't use the Google Cloud console to create or view rollout sequences with custom stages.
  * When a rollout sequence references a fleet, you must include the _entire_ fleet. This constraint means that if you define a stage to target only a subset of clusters from a fleet with a `label-selector` (for example, for a phased deployment), you must also define a subsequent "catch-all" stage that includes all remaining clusters from that same fleet. This catch-all stage targets the same fleet but doesn't include a `label-selector`, thereby automatically including all clusters that were not selected by earlier stages in the sequence.
  * If you modify a sequence during a rollout, specifically changes that affect the participating clusters, GKE immediately cancels all existing rollouts. If you modify only the soak time of a sequence, GKE doesn't cancel the rollout.
  * A single fleet can be referenced only in one rollout sequence. Two rollout sequences can't reference the same fleet.
  * You can only create one RolloutSequence object per host project.
  * You can't upgrade clusters with rollout sequencing that use [accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch).
  * You can create a rollout sequence with up to 15 stages.
  * You can include up to 250 clusters in a fleet. For clusters with [lightweight memberships](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-fleets#lightweight_memberships), you can request an increase in quota for up to 2,000 clusters in a fleet. For more information, see [Quotas and limits](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/quotas).
  * You can configure a maximum soak time per sequence of up to 90 days across all stages.



## Known issues

This section outlines the known issues for rollout sequencing with custom stages.

  * If a stage in your rollout sequence contains no clusters, the stage is skipped, but the soak time defined for that stage still passes before the rollout proceeds to the next stage.



## What's next

  * [Sequence the rollout of cluster upgrades with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/rollout-sequencing-custom-stages/manage-upgrades-with-rollout-sequencing)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
