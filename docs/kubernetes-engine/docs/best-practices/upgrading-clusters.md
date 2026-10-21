---
url: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters/
title: Best practices for GKE cluster upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T13:52:12.385479+00:00
---

# Best practices for GKE cluster upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Best practices for GKE cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document provides best practices for platform administrators to manage Google Kubernetes Engine (GKE) cluster upgrades. By default, GKE automatically upgrades the version of your cluster's control plane and nodes to provide new features, bug fixes, and security patches to keep your environment performant and secure.

To help ensure that these automatic upgrades align with your operational needs and minimize workload disruption, GKE offers tools so that you can assert maximal control. This guide explains how to effectively use these tools to maintain high performance and availability. For a foundational understanding, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades).

In addition to cluster upgrades, which are only updates to the GKE version of the control plane and nodes, GKE periodically performs additional updates to the cluster. Implementing the best practices in this document can help prepare for some of these types of changes. For more information, see [Manage cluster lifecycle changes to minimize disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters).

For a consolidated overview of all GKE best practices, see [Best practices for GKE](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices). **Important:** AI/ML workloads, capacity-constrained workloads, stateful workloads, and other workload profiles require additional consideration. For more information, see Additional considerations for specific workload profiles.

## Checklist

The following table summarizes the tasks that are explained in detail in the following sections. We recommend that you do these tasks when you prepare your environment for cluster upgrades.

Best Practice | Tasks  
---|---  
Choose your balance between feature velocity and upgrade stability with release channels | 

  * Assess whether the default Regular channel is right for your clusters.
  * Assess whether your clusters need long-term support from the Extended channel.

  
Choose the timing of upgrades with maintenance policies | 

  * Use maintenance windows to choose when upgrades can happen during the week.
  * Use maintenance exclusions to choose periods of time when upgrades can't happen, or to temporarily prevent upgrades for a cluster.
  * For advanced use cases, consider customizing the cluster disruption budget.

  
Control the rollout of upgrades across clusters | 

  * Configure rollout environments, including, at minimum, production and pre-production environments.
  * Use rollout sequencing to choose the order in which environments get automatically upgraded.
  * Perform checks before cluster upgrades.

  
Control how upgrades are triggered | 

  * Use manual upgrades to proactively upgrade clusters, if needed.

  
Monitor cluster upgrades | 

  * Stay up-to-date on the status of cluster upgrades.

  
Minimize disruption to existing workloads during node upgrades | 

  * Understand which types of workloads require additional considerations when preparing for cluster upgrades.
  * Choose a node upgrade strategy for your Standard node pools.
  * Configure Pod Disruption Budgets (PDBs).
  * Configure graceful termination.

  
  
## Choose your balance between feature velocity and upgrade stability with release channels

With [release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), you choose a balance between feature velocity and upgrade stability. GKE clusters are enrolled in the Regular release channel, by default. When GKE upgrades your cluster's control plane and nodes to deliver security patches, fix known issues, and introduce new features, the release channel determines which GKE versions your cluster runs. For example, if you want new features sooner, you can choose the Rapid channel, and if you want versions with more demonstrated stability, choose the Stable channel. For more information about choosing between specific channels, see [What channels are available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#channels).

If you want to manually upgrade your clusters, you can still benefit from choosing your release channel by reviewing the available versions and auto-upgrade targets for the channel before selecting a new version.

Additionally, if you want to get patch versions in a release channel as soon as possible—for example, to receive critical security patches—see [About getting patch versions earlier](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#patch-versions-earlier).

### Choose how much support you need for a minor version

GKE provides a total of up to 24 months of support for a minor version after the version has been made available in the Regular channel. This support includes 14 months of standard support, and approximately 10 months of extended support available with the Extended channel. For more information about how GKE supports a minor version, see [Minor version support](https://docs.cloud.google.com/kubernetes-engine/versioning#version-support).

If you need to keep your cluster on a minor version for longer while still receiving security patches past the end of standard support date, or you want to prevent end of standard support enforcement, you can also use the Extended channel. For more information, see the later section, Use the Extended channel when you need long-term support.

When the minor version reaches the end of support, depending on which release channel the cluster is enrolled in, GKE automatically upgrades your cluster to help ensure that the cluster remains performant and secure. For more information, see [Automatic cluster upgrades for security and compatibility](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades_for_security_and_compatibility). If you're using the tools described in this document to prevent or delay automatic cluster upgrades from proceeding, we recommend that you manually upgrade your clusters before the minor version that they run reaches the end of support. Otherwise, GKE automatically upgrades your cluster.

## Choose the timing of upgrades with maintenance policies

To control when upgrades can and can't happen, use the following:

  * [**Maintenance windows**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows): choose a recurring window of time when GKE can upgrade your cluster, such as off-peak business hours. If the upgrade process runs beyond the maintenance window, GKE attempts to pause the operation and resume it during the next maintenance window.
  * [**Maintenance exclusions**](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions): choose a specific time period when GKE can't upgrade your cluster, such as during a major sales event for a retail business. You can also use maintenance exclusions to temporarily postpone automatic upgrades of a cluster when, for example, you notice an issue with other clusters being upgraded to a new version. 
    * For advanced use cases, you might need to manually perform certain types of upgrades instead of GKE performing them. You can use maintenance exclusions to disable these types of auto-upgrades. For example, you can use the scope of "No minor or node upgrades" to disable all minor upgrades and all node upgrades. You must manually perform those upgrades yourself, or GKE upgrades your clusters at the end of support for the minor version.
  * [**Maintenance frequency**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget): for advanced use cases, control the minimum interval between two consecutive auto-upgrades with the cluster disruption budget.



By configuring maintenance policies, you can increase upgrade predictability and help ensure that upgrades happen when it is most convenient for your workloads.

## Control the rollout of upgrades across clusters

We recommend that you use multiple environments to minimize risk and unwanted downtime by testing software and infrastructure changes separately from your production environment. At minimum, we recommend that you have a production environment and a pre-production or test environment.

Consider the following recommended environments:

Environment | Description  
---|---  
Production | Serve live traffic to end users for mission-critical business applications.  
Canary | Test a small fraction of the production environment before all clusters are upgraded.  
Staging | Check that all new changes deployed from previous environments are working as intended before the changes are deployed to production.  
Testing | Perform benchmarking, testing, and quality assurance (QA) for workloads with the GKE version that you will use in production.  
Development | Use the same version running in production for active development. In this environment, you create fixes and incremental changes to be deployed in production.  
  
GKE provides features like rollout sequencing to help you control how upgrades are deployed across these different environments, as detailed in the following section.

### Use rollout sequencing to roll out across environments

To progressively roll out new GKE versions within and across these environments, we recommend that you use _rollout sequencing_. With rollout sequencing, all clusters use the same release channel and minor version throughout the stages of deployment. GKE progressively rolls out new versions across the sequence that you configure. When GKE rolls out the new version across your environments, you can verify that your cluster environment and workloads are running as expected with the new version.

If you're configuring a new environment, use [rollout sequencing with custom stages](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing-custom-stages/about-rollout-sequencing). This newer version of rollout sequencing lets you divide the rollout of a new version to a fleet in multiple stages. With this approach, GKE can, for example, upgrade a canary environment in production before upgrading the rest of production.

Although we don't recommend it for new environments, you can also use an earlier version of the feature, [fleet-based rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing). This version of the feature is the only one with support in the Google Cloud console, but otherwise has more limited functionality.

### Testing GKE patch and minor upgrades

GKE automatically upgrades clusters to a new patch as often as every week. Minor version upgrades, however, occur only approximately three times a year. New Kubernetes minor versions introduce a greater volume of changes compared to patches of the same minor version. We recommend that you apply additional scrutiny during the rollout of minor version upgrades across your environments, to help ensure that the new minor version works as expected with your clusters and workloads.

#### Perform checks before upgrading your cluster

Before performing automatic cluster upgrades, GKE qualifies new versions—for an amount of time that depends on the release channel—and reviews the readiness of the cluster.

Before cluster upgrades, we recommend that you do the following:

  * For all upgrades, including patch and minor upgrades: 
    * Check the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) for issues, and to find the changelog for new minor and patch versions.
    * Check the [GKE known issues](https://docs.cloud.google.com/kubernetes-engine/docs/troubleshooting/known-issues) for any issues relevant to your cluster environment and the new version.
  * For minor upgrades, additionally review the following: 
    * Check API deprecations. For more information, see the GKE release note for the new version, the Kubernetes changelog, and [Feature and API deprecations](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations).
    * Ensure that the version skew between the control plane and the nodes is supported. GKE supports running nodes up two minor versions earlier than the control plane. For more information, see [ GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew).
  * For node upgrades: 
    * Check that you have sufficient resources for the node upgrade strategy that your nodes use. For more information, see [Ensure resources for node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota).



## Control how upgrades are triggered

GKE, by default, automatically upgrades clusters to new versions on a regular basis. However, you can also use manual upgrades to upgrade your cluster exactly when you want, and control the version that your cluster runs.

You can do the following:

  * Manually upgrade your cluster.
  * Perform actions for in-progress automatic or manual node upgrades, including the following:

    * Cancel an upgrade.
    * Resume an upgrade.
    * Roll back an upgrade.
    * Complete an in-progress upgrade.



If you want to take more control of the upgrade process, we recommend that you configure maintenance exclusions, and then perform manual upgrades as needed. For more information about manual upgrades and other actions that you can take for in-progress upgrades, see [Manually upgrading a cluster or node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).

## Monitor cluster upgrades

To help ensure that GKE upgrades proceed as expected and that your cluster environment remains performant and available, use the following tools to monitor cluster upgrades. To remain aware of the status of your clusters, use tools such as notifications, insights and recommendations, and logs. We particularly recommend paying attention to end of support notifications, upgrade start notifications, and the opt-in scheduled upgrade notifications for minor version upgrades. Set up alert policies to help ensure that you see these notifications.

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



## Minimize disruption to existing workloads during node upgrades

In addition to the general best practices described in the previous sections, we recommend that you consider additional, advanced configuration to further customize the upgrade process to fit your cluster environment and your workloads' needs.

### Additional considerations for specific workload profiles

Certain types of workloads and cluster environments require additional preparation for cluster upgrades. If your workload fits one or more of the following categories, take these additional considerations:

  * **Workloads that run on machines that don't live migrate** : GKE nodes, which are Compute Engine instances that GKE creates on your behalf, periodically require maintenance on the underlying infrastructure. Most Compute Engine instances can live migrate, meaning that running workloads don't experience interruptions when this maintenance occurs. However, certain machine types can't live migrate, meaning that workloads running on the GKE nodes can be disrupted. Critically, accelerators, such as GPUs and TPUs for AI/ML workloads, can't live migrate. For more information, see [Understand how to do host maintenance on GKE](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu).
  * **Capacity-constrained workloads** : if your workloads use machine types which are capacity-constrained, additional consideration is required when performing cluster upgrades. For more information, see [Ensure resources for node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota).
  * **Stateful workloads** : if your workloads are stateful and have specific requirements for healthily shutting down and restarting, additional consideration is required when performing cluster upgrades. For more information, see [Ensure workloads are disruption-ready](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/workload-disruption-readiness).



Review the following sections to understand how you can use the available tools to upgrade these types of workloads.

### Choose a node upgrade strategy

In GKE Standard mode, GKE offers different node upgrade strategies that determine how the individual nodes in your node pool are upgraded. By choosing an upgrade strategy for your Standard node pool, you can pick the process with the right balance of speed, workload disruption, risk mitigation, resource capacity, and cost optimization. You can also configure the parameters of the strategy to best fit your needs. For more information, see [About node upgrade strategies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) and [Upgrade in a resource-constrained environment](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-upgrades-quota#upgrade-resource-constrained).

In GKE Autopilot mode, GKE manages the node upgrades and you don't need to choose the specific strategy used. For more information, see [Surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades-autopilot#surge) for Autopilot clusters.

### Set your tolerance for disruption

Use [Pod Disruption Budgets (PDBs)](https://kubernetes.io/docs/tasks/run-application/configure-pdb/) to help ensure that when GKE re-creates the nodes during upgrades, which can temporarily reduce the number of replicas for a workload, your workloads maintain sufficient redundancy.

If a PDB is set, GKE won't shut down Pods in your application [if the number of Pods is equal to or less than a configured limit](https://kubernetes.io/docs/tasks/run-application/configure-pdb/#specifying-a-poddisruptionbudget). GKE upgrades respect a PDB for up to 60 minutes. Additionally, GKE notifies you if a node drain is being blocked by a PDB, or the PDB timeout is reached and the Pods will be force deleted despite the PDB violation. For more information, see [Disruptive events during a node pool upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#disruption-event).

**Note:** The PDB only protects against [voluntary](https://kubernetes.io/docs/concepts/workloads/pods/disruptions/#voluntary-and-involuntary-disruptions) disruptions (for example, an upgrade). However, a PDB does not offer protection against involuntary disruptions (for example, a hardware failure).

### Use graceful termination to shut down an application

You can configure graceful termination to help ensure that workloads have sufficient time to prepare for shutdown. During node upgrades, GKE respects graceful termination settings for up to 60 minutes with the default [surge upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#surge), and up to 24 hours with [blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#blue-green-upgrade-strategy) and [autoscaled blue-green upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies#autoscaled-blue-green-upgrade-strategy) ([Preview](https://docs.cloud.google.com/products#product-launch-stages)).

For more information about configuring graceful termination settings, see [Configure GKE to terminate your workloads gracefully](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/handle-disruption-gpu-tpu#configure-gke).

## Use the Extended channel when you need long-term support

If you want to keep your cluster on a [minor version](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) for longer, follow the best practice of enrolling your cluster in the Extended channel. With this channel, GKE supports a minor version for approximately 24 months. With the Extended channel, you control minor version upgrades, with GKE only performing [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support), if you don't initiate the upgrade yourself. For more information, see [Get long-term support with the Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended).

If you don't need to stay on a minor version for longer than the standard support period, but you still want to control minor version upgrades, instead use [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) with the "No minor upgrades" scope.

To get the most benefit from the channel, we recommend that you adhere to the following best practices. Some of these best practices require taking some manual action, including [manually upgrading a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) and [changing the release channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#selecting_a_new_release_channel) of a cluster. Review the following supported scenarios, as well as When not to use the Extended channel.

### Temporarily stay on a minor version for longer

If you need to temporarily keep a cluster on a minor version for longer than the 14-month standard support period, for example, to mitigate the use of deprecated APIs removed in the next minor version, use the following process. You can temporarily move the cluster from another release channel to the Extended channel to continue to receive security patches while preparing to upgrade to the next minor version. When you're ready to upgrade to the next minor version, you manually upgrade the cluster, then move the cluster back to the original release channel.

### Minor version upgrades one or two times per year

If you want minimal disruption for your cluster while still receiving some new features when your cluster is ready to be upgraded to a new minor version, do the following:

  * Enroll a cluster in the Extended channel.
  * Perform two successive minor version upgrades one or two times per year. For example, upgrade from 1.33 to 1.34 to 1.35.



This process helps to ensure that the cluster stays on an available minor version, receives features from new minor versions, but only receives minor version upgrades when you decide the cluster is ready.

### When not to use the Extended channel

To use the Extended channel for its intended purpose requires manual action. The following scenario illustrates the consequences of using the Extended channel without active management of your cluster's minor version.

#### Do nothing and receive minor upgrades with same frequency

If you want to keep your cluster on a minor version forever, you enroll your cluster in the Extended channel and take no further action. All minor versions eventually become unsupported and [GKE automatically upgrades clusters from unsupported minor versions](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support). So, GKE upgrades this cluster from one unsupported minor version to a soon-to-be unsupported minor version, which averages out to [approximately every four months](https://docs.cloud.google.com/kubernetes-engine/versioning#kubernetes-minor-version-support). This approach means that the cluster receives minor version upgrades just as frequently on other release channels but receives new features later.

## What's next

  * For more information about the different modes of GKE, see [Compare features in Autopilot and Standard clusters](https://docs.cloud.google.com/kubernetes-engine/docs/resources/autopilot-standard-feature-comparison). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
