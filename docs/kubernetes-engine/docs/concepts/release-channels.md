---
url: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels/
title: About release channels \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:22:43.054220+00:00
---

# About release channels  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  About release channels Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

[Use release channels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels) for Google Kubernetes Engine (GKE) to pick versions for your clusters with your chosen balance between feature availability and stability.

GKE automatically upgrades all clusters over time, including those not enrolled in a release channel, to ensure that they receive security updates, fixes to known issues, new features, and run a supported Kubernetes version. You can control the timing of upgrades with [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions).

We recommend enrolling your cluster in a release channel, as this gives you the most control with regards to the [scope of maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude)—preventing specific types of upgrades instead of all upgrades—and [sequencing the rollout of cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/about-rollout-sequencing). Autopilot clusters can only be enrolled in a release channel.

If you don't enroll your Standard cluster in a release channel, all clusters' control planes are still automatically upgraded, and when a version reaches the [end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle), cluster control planes and nodes are automatically upgraded regardless of release channel enrollment. To learn more, see the comparison between clusters enrolled and not enrolled in a release channel.

## What channels are available

The following table explains the properties of available release channels, each offering a trade-off between feature availability and stability. All channels offer supported releases of GKE and are considered generally available (GA), although individual features might not always be GA, as marked. The Kubernetes releases in these channels are official Kubernetes releases and include both GA and beta Kubernetes APIs.

Channel | Minor version availability | Set as an auto-upgrade target | When to use this channel  
---|---|---|---  
Rapid | 1-2 weeks after upstream open source GA Alpha patch versions are available for only alpha clusters up to four months before GKE makes the minor version available to all clusters in Rapid. | 1-2 months after release to Rapid | Get the latest Kubernetes release as early as possible, and be able to use new GKE features the moment they go GA. GKE upgrades your cluster frequently to stay on the latest available patch version, and deliver newer Kubernetes capabilities. Clusters subscribed to the Rapid channel use GA versions, however we recommend to use the Rapid channel to test newer Kubernetes versions and API on pre-production environments. **Caution:** As Rapid channel provides the newest GKE versions, these versions are excluded from the [GKE SLA](https://cloud.google.com/kubernetes-engine/sla) and may contain issues without known workarounds.The Rapid channel is recommended for [alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters), which enable all Kubernetes alpha feature gates and alpha APIs for testing. Alpha clusters in the Rapid channel can run [alpha patch versions](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) of upcoming minor versions up to four months before GKE makes that minor version available to all clusters in Rapid.  
Regular (default) | Approximately 2 months after release to Rapid | Approximately 3 months after release to Regular | Access GKE and Kubernetes features soon after they go GA, but on a version that has been qualified over a longer period of time. Offers a balance of feature availability and release stability, and is what we recommend for most users.  
Stable | 3-4 months after release to Regular | Approximately 2 months after release to Stable | Prioritize stability over new features. GKE rolls out changes and new versions in this channel last, after being validated on the Rapid and Regular channels, which allows even more time for validation.  
Extended | Aligned with Regular channel | Aligned with Regular channel | Use this channel to get long-term support, keeping a cluster running a minor version for as long as possible. To learn more, see Get long-term support with the Extended channel.  
No channel (deprecated)  | Aligned with Regular channel | Aligned with Stable channel |  **Warning** : This configuration option is deprecated and will be removed on June 14, 2027. For more information, see Clusters not enrolled in a release channel. Control plane and nodes are auto-upgraded in alignment with the Regular and Stable channels. If you need to disable node auto-upgrades at a node pool level, you can instead use a release channel and do either of the following: 

  * Configure a [node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions).
  * [Disable node auto-upgrades at a cluster level](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude).

For more information about No channel, see the comparison between clusters enrolled and not enrolled in a release channel.  
**Note:** Exact release schedules depend on multiple factors, including the open source release and patching schedule, and therefore are subject to change. To stay informed with the latest information, review the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) or subscribe to the RSS feed for your channel.

When you enroll a cluster in a release channel, that cluster is upgraded automatically on or after the date specified in the _Auto Upgrade_ column of the [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).

When a version has accumulated usage and demonstrated stability across clusters in the _Rapid_ channel, it is promoted to the _Regular_ channel. Eventually, the version is promoted to the _Stable_ channel, which only receives high-priority updates. Each promotion signals a graduating level of stability and production-readiness, based on observed performance of clusters running that version.

Critical security patches are delivered to all release channels, to protect your clusters and Google's infrastructure. In rare emergency situations, GKE might auto-upgrade clusters to versions that aren't yet available in their release channel.

## What versions are available in a channel

Each release channel offers multiple minor versions. These versions have met the qualification standards for that specific channel. This set of available versions includes a default version for cluster creation, which is selected from a set of available versions from that channel. To see what versions are available in a release channel, follow the instructions to [view the default and available versions for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#viewing_the_default_and_available_versions_for_release_channels).

  * New patch versions become available in the following amount of time: 
    * _At least one week_ prior to becoming an auto-upgrade target in the respective channel
    * _At least two weeks_ after having been made available in the prior channel
  * New minor versions become available in the following amount of time: 
    * _At least four weeks_ prior to becoming an auto-upgrade target in the Rapid channel
    * _At least eight weeks_ prior to becoming an auto-upgrade target in the Regular and Stable channels



If you're interested in testing upcoming Kubernetes minor versions, then [alpha patch versions](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) become available in the Rapid channel _up to four months_ prior to when GKE makes that minor version available to all clusters in the Rapid channel. Alpha patch versions are exclusive to alpha clusters.

You can test a newly available GKE version prior to upgrading your production environment. For example, you can subscribe to [upgrade notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications) to be informed of newly available versions, and then proactively upgrade a pre-production environment to the new version before it becomes the auto-upgrade target for clusters in your production environment.

If you need to keep a cluster on a specific version, for example to validate or test newer versions prior to upgrading, we recommend using [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).

After a minor version has been made available in a release channel, it will remain available in that release channel for new or existing clusters until it reaches its [end of support date](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).

**Note:** When you create a cluster in a release channel, if you specify a patch version which has a newer eligible auto-upgrade target in that release channel, GKE might automatically upgrade the cluster. If you want to temporarily prevent the cluster from being automatically upgraded when you select the new channel, [configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) before selecting the new channel.

### What happens when a version becomes an auto-upgrade target in a release channel

GKE automatically upgrades clusters over time to new auto-upgrade targets. When new auto-upgrade targets are available, GKE assesses if your specific cluster should be upgraded to that new version. GKE considers if your cluster has maintenance policies or other constraints that prevent automatic upgrades, and it won't ignore those reasons except in rare emergency situations.

You can find auto-upgrade targets for your clusters in the following ways:

  * To get auto-upgrade targets for a specific cluster, see [Get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).
  * The [Current versions table](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) provides a list of current auto-upgrade targets for each release channel. The specific version that applies to your cluster depends on the cluster's minor version and specific constraints.
  * The [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) lists new auto-upgrade targets for clusters that run specific minor versions with _Version updates_ such as the [2024-R33 note](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#2024-r33_version_updates).



If 10 days have passed after a new version became an auto-upgrade target for your cluster's minor version in the release channel, and automatic upgrades haven't started for your cluster, the delay might be due to one of the following reasons:

  * Your cluster is temporarily ineligible for automatic upgrades. This might occur because: 
    * The cluster is outside the timeframe of a configured [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows).
    * The cluster is within the timeframe of a [maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions).
    * Automatic upgrades are [paused](https://docs.cloud.google.com/kubernetes-engine/docs/deprecations#auto-upgrade-pause) because your cluster uses deprecated Kubernetes features that are removed in the next minor version.
    * The cluster was automatically upgraded to a [patch version](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme) less than 24 hours ago.
    * The cluster was automatically upgraded to a [minor version](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle) less than 30 days ago and the auto-upgrade target is a new minor version.
  * GKE paused the rollout of the new auto-upgrade target for technical or business reasons: 
    * Technical issues were discovered with the new version.
    * A production freeze is in place due to a critical business season, such as Black Friday.



#### What is the recommended auto-upgrade target?

The recommended auto-upgrade target is the version GKE gradually upgrades your clusters to over time. Of all the auto-upgrade targets in a release channel, GKE moves your clusters closer towards this version when it performs auto-upgrades.

Over multiple auto-upgrades, barring constraints preventing auto-upgrades, GKE upgrades your clusters progressively closer to the release channel's recommended auto-upgrade target, until your cluster reaches the target. After reaching the target, your cluster continuously uses the existing recommended auto-upgrade target, moving to the new recommended target when it's released.

#### What is the default version?

When you create a cluster in a release channel, by default, the cluster uses the [default patch version for cluster creation](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) in the selected release channel. However, you can specify a different available version when you create a cluster in the release channel.

Release channels have multiple minor versions available in a release channel, and the default version can sometimes be one of the auto-upgrade targets for a release channel.

## About getting patch versions earlier

You can get patch versions earlier with automatic or manual upgrades by using the methods described in this section.

### Accelerated patch auto-upgrades

GKE first introduces a new patch version to a release channel by making the version available for new cluster creation and manual upgrades. After GKE determines that the patch version is qualified, GKE sets the new patch version as an auto-upgrade target, meaning GKE begins automatically upgrading clusters to this new patch version. The length of time from version availability to auto-upgrades is typically at least one week, but depends on the release channel and specific circumstances of qualifying the version.

For more information about current version availability, do the following:

  * See the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) page, including the [Current versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#current_versions) table, and the _Version updates_ entries, such as the [2025-R26 note](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#2025-r26_version_updates).
  * [Check the available and default versions](https://docs.cloud.google.com/kubernetes-engine/versioning#available_versions) for which versions are available in your release channel.



If you want to receive patch upgrades as soon as the version is available and before GKE sets the version as an auto-upgrade target in the channel, you can use accelerated patch auto-upgrades. This setting can be useful if you want to receive security patches as soon as possible through automatic upgrades.

You must understand the risks associated with automatically upgrading the cluster on an accelerated schedule before GKE determines that clusters in the channel should be automatically upgraded to the new patch version. This accelerated schedule skips a step in the qualification process for patch versions in release channels. All patch versions, not just patch versions with security patches, are upgraded with this accelerated schedule. This setting doesn't affect minor version upgrades, and is only available for clusters enrolled in a release channel.

This setting only affects the timing of when GKE auto-upgrades a cluster to a new patch version. GKE still adheres to maintenance windows and exclusions, follows the order of a rollout sequence, and applies any other standard practices that are typically used for automatic upgrades.

For more information about setting this feature, see [Use accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#use-accelerated-patch).

Alternatively, you can [manually upgrade your clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster) if you want to upgrade to a specific patch version as soon as the version is available, and before it's set as an auto-upgrade target.

### Run patch versions from a newer channel

In addition to the listed [available patch versions](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#viewing_the_default_and_available_versions_for_release_channels) for a release channel, you can run patch versions from newer release channels than the one where your cluster is enrolled if the [minor version](https://docs.cloud.google.com/kubernetes-engine/versioning) is available in the cluster's release channel and you use the gcloud CLI or the GKE API.

For example, if the following versions were available in the Rapid and Regular channels:

  * Rapid: 1.23.2-gke.700, 1.22.4-gke.1500
  * Regular: 1.21.4-gke.400, 1.22.1-gke.400



A cluster enrolled in the Regular channel that is running GKE version 1.22.1-gke.400 could manually upgrade to 1.22.4-gke.1500, but not to 1.23.2-gke.700 as it is a different minor version.

To manually upgrade to a patch version on a newer channel, your cluster's control plane must run a patch release with the same minor version. For example, if the cluster is running 1.21.3-gke.200, you must first manually upgrade the cluster to a patch version available in its current release channel, 1.22.1-gke.400. You can then upgrade the cluster to 1.22.4-gke.1500.

You can also create a new cluster that runs 1.22.4-gke.1500 and is enrolled in the Regular channel.

GKE keeps the cluster on the patch version from the newer channel until a newer auto-upgrade target becomes available in the enrolled channel for the cluster.

### Learn what's new in a channel

To learn what's new in a release channel, review the release notes. There are separate release notes for each release channel, in addition to the overall [release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes).

Release channel | Release notes   
---|---  
Rapid channel | [HTML](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-rapid) or [Atom feed](https://docs.cloud.google.com/static/feeds/kubernetes-engine-rapid-channel-release-notes.xml).  
Regular channel | [HTML](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-regular) or [Atom feed](https://docs.cloud.google.com/static/feeds/kubernetes-engine-regular-channel-release-notes.xml).  
Stable channel | [HTML](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes-stable) or [Atom feed](https://docs.cloud.google.com/static/feeds/kubernetes-engine-stable-channel-release-notes.xml).  
  
## Choose the best release channel for your cluster

Each channel represents a different level of quality and maturity of the Kubernetes and GKE releases. The following diagram illustrates the adoption cycle for release channels:

![Release channels adoption cycle](https://docs.cloud.google.com/static/kubernetes-engine/images/release-channel-adoption-cycle.svg)

As this diagram shows, the available release channels use versions in the middle of the adoption cycle, including _Early adopters_ (Rapid channel), _Early majority_ (Regular channel), and _Majority_ (Stable channel). The earliest part of the adoption cycle is the _Innovators_ , who test the newest features using the upstream Kubernetes release. The last part of the adoption cycle is the _Late majority_ , where you are using a version that is nearing deprecation and need to transition to a supported version.

In your pre-production environments, use the Rapid channel for newer versions where you can test features as soon as they are generally available.

For production workloads that require maturity over newer features, we recommend using the Regular (default) channel or the Stable channel.

  * If you need to closely track new features, consider using the Regular channel, which offers a balance between stability and freshness of the Kubernetes OSS version.
  * If your requirement is maturity, especially for production clusters, use the Stable channel.



GKE upgrades clusters to a newer version that meets the channel's quality standards. However, we recommend upgrading your clusters ahead of time because this provides you with:

  * Better control of your upgrades, and alignment with your working hours.
  * Better predictability because GKE skips auto-upgrading clusters that meet the release target (i.e., clusters that were manually upgraded to the next target version). Nodes are automatically upgraded to the recommended version in their selected channel to align with the control plane version and to protect you from vulnerabilities and [unsupported version skew](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew).



## Get long-term support with the Extended channel

GKE provides [long-term support](https://en.wikipedia.org/wiki/Long-term_support) for Kubernetes minor versions through the Extended channel. With this channel, you can stay on a minor version for up to 24 months. After the 14-month standard support period, your cluster receives security patches for [approximately](https://docs.cloud.google.com/kubernetes-engine/versioning#adjustments_of_version_availability) 10 more months during the [extended support period](https://docs.cloud.google.com/kubernetes-engine/versioning#extended-support).

### How GKE automatically upgrades clusters in the Extended channel

For clusters enrolled in the Extended channel, GKE automatically upgrades clusters in the following way:

  * **During the standard support period** : GKE upgrades clusters to newer patch versions of the same minor version following the same cadence as the Regular channel.
  * **During the extended support period** : GKE continues to provide security patch updates for the minor version. Around 2 months before the end of extended support, GKE begins upgrading clusters to the next minor version, unless the cluster is using deprecated features or APIs. You can use maintenance exclusions to prevent minor version upgrades until the end of extended support.
  * **At the end of extended support** : GKE upgrades all clusters still running the now-unsupported minor version, regardless of blocking issues. You can't configure maintenance exclusions past this date, except as a [temporary, emergency measure with the "No upgrades" scope](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#temporary-no-upgrades-exclusion).



To learn more about the different periods of availability and what upgrades GKE provides during the extended support period, see [ GKE minor version lifecycle](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle).

### Limitations for enrolling a cluster in the Extended channel

Review the following limitations for clusters that are enrolled in the Extended channel:

  * During the extended support period, GKE updates the Container-Optimized OS milestone that the GKE minor version uses when the milestone reaches the end of support. GKE pauses patch node auto-upgrades and sends a [cluster notification](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#extended-patch-new-cos-milestone). For more information about this change, see [Container-Optimized OS updates during the extended support period](https://docs.cloud.google.com/kubernetes-engine/versioning#cos-extended).
  * The extended support period doesn't extend your cluster's credential expiry date. [Rotate your cluster credentials](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/credential-rotation) before they expire.
  * You can't enroll a cluster that uses the following features in the Extended channel:

    * [Autopilot cluster mode](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview)
    * [Alpha clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters)
    * [Explicitly-enabled Kubernetes beta APIs](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/use-beta-apis#configure-beta-apis)
    * [Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/gateway-api) (only supported in the Extended channel with GKE version 1.30 or later)
    * [Windows Server node pools](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-cluster-windows)
    * [Config Connector](https://docs.cloud.google.com/config-connector/docs/how-to/install-upgrade-uninstall)
    * The following multi-cluster features: 
      * [Managed Cloud Service Mesh](https://docs.cloud.google.com/service-mesh/docs/overview#managed)
      * [Service Directory for GKE](https://docs.cloud.google.com/service-directory/docs/sd-gke-overview)
      * [Config Sync](https://docs.cloud.google.com/kubernetes-engine/config-sync/docs/overview)
      * [Policy Controller](https://docs.cloud.google.com/kubernetes-engine/policy-controller/docs/overview)
      * [Multi-cluster Gateway](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/enabling-multi-cluster-gateways)
      * [Multi Cluster Ingress](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-ingress)
      * [Multi-cluster Services](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/multi-cluster-services)



### Pricing for extended support

If you want to enroll a cluster in the Extended channel, ensure that you've reviewed the [pricing for extended support](https://cloud.google.com/kubernetes-engine/pricing#extended-support-period). Pay-per-use costs apply when your cluster is enrolled in the Extended channel and your cluster's minor version enters the extended support period.

### Best practices for the Extended channel

Review the following scenarios to understand how you can use the Extended channel to minimize disruption from minor version upgrades.

The supported scenarios require some manual action over time to get the most benefit from the channel. We don't recommend that you enroll a cluster in the channel without plans to move to the next minor version, as GKE will eventually upgrade the cluster to newer minor versions with the same frequency as other channels, and your cluster will potentially incur greater cost and receive new features last.

#### Supported and unsupported scenarios

To learn more about supported and unsupported scenarios, review the following table, and see [Use the Extended channel when you need long-term support](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#extended-scenarios-yes) for more details. A checkmark () indicates a supported scenario:

Upgrade scenario | Supported | Summary | Time between minor version changes | Manual action required  
---|---|---|---|---  
[Temporarily stay on minor version for longer](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#exceptional-extension-minor) |  | Stay on a minor version to mitigate an issue preventing upgrades. | Same average frequency, with interruption for extra time on one minor version. | 

  * Temporarily move a cluster to and from the Extended channel.
  * Manually upgrade cluster to the new minor version when ready.

  
[Manually upgrade minor version 1-2 times a year](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#infrequent-minor-upgrade) |  | Get new features but with less frequent minor upgrades, when it's optimal for the workloads in the cluster. | 1-2 times per year. | 

  * Manually upgrade cluster to newer minor version.

  
[Do nothing and receive minor upgrades with same frequency](https://docs.cloud.google.com/kubernetes-engine/docs/best-practices/upgrading-clusters#do_nothing_and_receive_minor_upgrades_with_same_frequency) |  | Get minor version upgrades with the same frequency as other channels, and new features as late as possible. | Every 4 months, on average. | 

  * Monitoring automatic minor version upgrades from unsupported versions.

  
  
## Clusters not enrolled in a release channel

**Warning:** Not enrolling your cluster in a release channel (known as _No channel_ , and formerly as _Static_) is a deprecated configuration option, only allowed for existing customers, and will be removed on June 14, 2027. New customers can't create or update their cluster to use this configuration option. For any clusters not enrolled in a release channel, we recommend that you [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster) before this date. After the removal date, GKE enrolls all remaining clusters in the Stable channel.

You can choose not to enroll a Standard cluster in a release channel. However, not enrolling limits your cluster's access to certain features, and this is a deprecated configuration option which will be removed. Regardless of release channel enrollment, all clusters' control planes are automatically upgraded, and when a version reaches the [end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle), cluster control planes and nodes are automatically upgraded.

**To migrate from this configuration option, see[Enroll an existing cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster).**

If you're considering not enrolling a cluster in a release channel because you have individual node pools that can't be automatically upgraded, and you must manually upgrade those nodes instead, you can achieve the same behavior with release channels. With release channels, if you need to disable node auto-upgrades for all node pools until the end of support, you can use a [cluster maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude) with the scope of "No minor or node upgrades". Or, if you have a cluster where you want to disable auto-upgrades for some, but not all, node pools, use a [node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions).

### Comparison between clusters enrolled and not enrolled in a release channel

Review the following table to understand the similarities and differences between enrolling and not enrolling your cluster in a release channel:

Feature | Cluster enrolled in a release channel | Cluster not enrolled in a release channel  
---|---|---  
Shared upgrade behavior | 

  * GKE [automatically upgrades the cluster control plane](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades), and, by default, automatically upgrades the nodes when [new versions are scheduled for auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes), following the [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).
  * GKE automatically upgrades the cluster control plane and nodes after their version reaches end of support.

| Upgrade timing | Aligned with the respective release channel | 

  * Same auto-upgrade start date as the Stable channel for minor versions
  * Same available minor versions, patch auto-upgrade versions, and default version as the Regular channel
  * Same available patch versions as the Rapid channel for those minor versions available in the Regular channel

  
Accelerated patch auto-upgrades | Available | Not available  
Control of node pool disruption | 

  * [Node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) by default
  * You can disable node auto-upgrades in the following ways: 
    * At the cluster level until the minor version end of support date by [creating a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) with the "No minor or node upgrades" scope
    * At the cluster level for up to 90 days by [creating a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) with the "No upgrades" scope
    * At the node pool level until the minor version end of support date by creating a [node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions).
    * At the node pool level until the minor version end of support date by [disabling node-auto upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable). This legacy configuration is not recommended, and you can achieve the same result by creating a node pool maintenance exclusion.
  * You can [disable node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair#disable) for a Standard cluster node pool

| 

  * [Node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) by default
  * You can disable node auto-upgrades in the following ways: 
    * At the cluster level for up to 90 days by [creating a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) with the "No upgrades" scope
    * At the node pool level until the minor version end of support date by [disabling node-auto upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable). You can achieve the same result with release channels by creating a node pool maintenance exclusion.

| [Maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows) | Available | Available  
[Maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions) | 

  * Available [maintenance exclusion scopes](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude): 
    * "No upgrades" (up to 90 days)
    * "No minor upgrades" (until the end of support)
    * "No minor or node upgrades" (until the end of support)
  * [Node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions)

| Restricted to "No upgrades" scope (up to 90 days)  
[Rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing) | Available | Not available  
Long-term support | Available with the Extended release channel only | Not available  
[Autopilot](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) | Available | Not available  
  
## Choose the Rapid channel for alpha clusters

**Best practice** :

Enroll alpha clusters in the Rapid channel. With this channel, alpha clusters can get access to new features from new versions as early as possible.

The Rapid channel provides your GKE cluster with access to new versions as early as possible, including [alpha patch versions](https://docs.cloud.google.com/kubernetes-engine/versioning#alpha-versions) of upcoming minor versions. Alpha clusters let you test new features that first become available in newer versions. In an alpha cluster, all Kubernetes APIs, including alpha APIs, are enabled. All Kubernetes alpha feature gates are enabled by default, and you can toggle specific alpha and beta feature gates. Before you deploy alpha clusters, understand the [limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/alpha-clusters#limitations).

You can also enroll your alpha cluster in the Regular or Stable release channels, but you can't access the latest Kubernetes versions, including alpha patch versions, in these channels. Choosing not to enroll your cluster in a release channel is a deprecated configuration option that will be removed. For more information, see the previous section, Clusters not enrolled in a release channel.

## What's next

  * Learn how to [use release channels](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels).
  * Learn more about [upgrading clusters](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster).
  * Learn how to [get visibility into cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist).
  * Learn about [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).
  * Learn about managing automatic cluster upgrades across environments with [rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
