---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels/
title: Use release channels \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:39:48.859911+00:00
---

# Use release channels  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Use release channels Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

As a platform administrator, you can choose a specific release channel for your cluster to ensure that GKE automatically upgrades your cluster to versions with your chosen balance between feature availability and stability. To learn more about release channels, see [About release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels).

GKE enrolls all Autopilot clusters in a release channel, and enrolls Standard clusters, by default, in a release channel. For all cluster modes, you can choose a specific release channel. With Standard clusters, you can choose to not enroll your cluster in a release channel, however this configuration option is [deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel) and will be removed on June 14, 2027.

This page explains how to take the following actions related to release channels:

  * Enroll a cluster in a specific release channel.
  * Find a cluster's release channel.
  * View the default and available versions for release channels.
  * Change a cluster's release channel.
  * Unenroll your cluster from release channels.



## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * If you want to enroll a cluster in the Extended channel, ensure that you've reviewed the [pricing for extended support](https://cloud.google.com/kubernetes-engine/pricing#extended-support-period). For GKE clusters, pay-per-use costs apply when your cluster is enrolled in the Extended channel and your cluster's minor version enters the extended support period.



## Enroll a cluster in a release channel

This section shows you how to select a specific release channel for new clusters, or for existing clusters that didn't previously use a release channel. You can also change the release channel for an existing cluster that is already enrolled in a release channel.

### Enroll a new cluster in a specific release channel

All clusters are enrolled in the _Regular_ release channel, by default. You can choose a specific release channel for a cluster when you create the cluster, or change the release channel after the cluster is created. Autopilot clusters must be enrolled in a release channel. Standard clusters can be enrolled or unenrolled in a release channel. For the Extended channel, review [Get long-term support with the Extended channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#extended) before selecting this channel.

You can create and enroll a new cluster in a specific release channel using the Google Cloud console or the gcloud CLI.

### Console

Create a cluster with the following steps, depending on the cluster mode:

  * **For Autopilot clusters** :

    1. On the Autopilot cluster creation page, from the navigation pane, click **Advanced settings** :

[Create an Autopilot cluster](https://console.cloud.google.com/kubernetes/auto/add)

    2. In the **Release channel** drop-down list, select a release channel to enroll the cluster in, or leave the default value of **Regular channel**.

  * **For Standard clusters** :

    1. On the Standard cluster creation page, in the **Cluster basics** section, navigate to the **Release channel** subsection:

[Create a Kubernetes cluster](https://console.cloud.google.com/kubernetes/add)

    2. In the **Release channel** drop-down list, select a release channel to enroll the cluster in, or leave the default value of **Regular channel**.

**Note:** [Node auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades) and [node auto-repair](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-repair) are enabled by default. Node auto-upgrade can't be disabled for a cluster subscribed to a release channel, however you can use [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to control the timing and scope of automatic upgrades. Node auto-repair can be disabled, however we recommend keeping the default configuration.



### gcloud

To create and enroll an **Autopilot cluster** in a specific release channel, run the following command:
    
    
    gcloud container clusters create-auto CLUSTER_NAME \
        --location=COMPUTE_LOCATION
        **--release-channel= CHANNEL**
    

To create and enroll a **Standard cluster** in a specific release channel, run the following command:
    
    
    gcloud container clusters create CLUSTER_NAME \
        --location=COMPUTE_LOCATION \
        **--release-channel= CHANNEL**
    

Replace the following:

  * `CLUSTER_NAME`: the name of your new cluster.
  * `CLUSTER_LOCATION`: the [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones#available) for the new cluster.
  * `CHANNEL`: the type of release channel: one of `rapid`, `regular`, `stable`, or, for Standard only, `extended`.



For a list of other options that you can specify, see the [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto) and [`gcloud container clusters create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create) reference documentation.

You can also create a cluster with a specific version using the `--cluster-version` flag. If you don't specify a release channel, GKE enrolls your cluster in the most mature release channel where that version is available.

Or, if you don't specify the release channel or cluster version, the cluster defaults to the Regular release channel on the default version.

### Enroll an existing cluster in a specific release channel

The following instructions explain how to enroll an existing cluster that isn't enrolled in a release channel into a release channel. If your cluster has node auto-upgrade disabled, instead see Enroll an existing cluster not enrolled in a release channel that has disabled node auto-upgrade.

Enroll your cluster in a release channel with the following steps:

  1. **Choose a release channel** : choose either the Stable channel, or a different channel that better suits your needs. The Stable channel is the most mature channel and has all minor versions available to clusters not enrolled in a channel. If you want new features sooner, or need extended support for a minor version, do the following: 
     1. [Choose the best release channel for your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_channel_should_i_use).
     2. Check if your cluster's control plane minor version is available in the target release channel, by viewing the default and available versions for release channels. You can enroll an existing cluster, as long as the cluster's control plane minor version is available in the target release channel. To learn more about aligning your cluster's control plane version with the available versions for your target release channel, see Change your cluster's release channel.
  2. **Consider using maintenance windows and exclusions** : GKE doesn't require any downtime to change the release channel enrollment of a cluster. However, GKE might have different automatic upgrades available in a different release channel, meaning that, after the change, GKE might automatically upgrade the cluster. We recommend using [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to control the timing of upgrades.
  3. **Update the cluster release channel to the target `CHANNEL`**: select the target release channel, which can be any option other than `None`.



GKE doesn't immediately upgrade the cluster control plane and nodes to the minor version's auto-upgrade target in that release channel when enrolling. Instead, they are gradually upgraded by the GKE auto-upgrade process. To get auto-upgrade targets for a specific cluster, see [Get information about a cluster's upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info).

#### Enroll an existing cluster that has disabled node auto-upgrade

Use the following instructions if you have an existing Standard cluster that is not enrolled in a release channel and you've [disabled node auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#disable_node_auto-upgrades_for_an_existing_node_pool) for one or more of the cluster's node pools. If you want to access the [additional features of release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel) and migrate from this [deprecated](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel) configuration option, _you can enroll your cluster in a release channel without any additional changes_.

GKE doesn't automatically enable the node auto-upgrades setting for the node pools when enrolling the cluster in a channel. Regardless, this setting is a legacy configuration, and when you enroll the cluster in a channel, we also recommend that you use [node pool maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions) to prevent node pool upgrades at the node pool level in the same way.

Do the following steps to enroll an existing cluster in a release channel:

  1. **Enroll the existing cluster in the target release channel** by [updating the channel](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#updating_the_cluster_release_channel), specifying `stable`. The Stable channel is the most mature channel and has all minor versions available to clusters not enrolled in a channel.
  2. **Optional** : do the following additional steps to migrate to using maintenance exclusions instead of the legacy configuration of disabling node auto-upgrades with the setting. You can perform these steps anytime after enrolling your cluster in a release channel: 
     1. Prevent node auto-upgrades in one of the following ways: 
        1. **For some node pools only** : [configure a node pool maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configure-node-pool-maintenance-exclusion-existing) for all node pools where you have node auto-upgrades disabled. Disabling node auto-upgrades with this exclusion prevents all node pool auto-upgrades, except for [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support), which happen regardless of release channel enrollment and how you've disabled node auto-upgrades.
        2. **For all node pools** : [configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#existing-maintenance-exclusion) with the scope of "No minor or node upgrades". This exclusion prevents all upgrades except for patch upgrades to the control plane. Now that your cluster is enrolled in a release channel, you can use this scope of maintenance exclusion, which can last to the end of support date for the minor version in your cluster's release channel.
     2. Remove use of the legacy field for disabling node auto-upgrades, because the maintenance exclusions that you configured in the previous step now perform this function. For each node pool, follow the instructions to [enable node auto-upgrades for an existing node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#enable).



## Find your cluster's release channel

You can determine your cluster's release channel using the Google Cloud console or the gcloud CLI.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to inspect.

  3. Under **Cluster basics** , check the value in the **Release Channel** field (for example, **Regular Channel**).




If the value is **None** , the cluster isn't enrolled in a release channel.

### gcloud
    
    
    gcloud container clusters describe CLUSTER_NAME \
        --location=COMPUTE_LOCATION --format="value(releaseChannel.channel)"
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `COMPUTE_LOCATION`: A [Compute Engine location](https://docs.cloud.google.com/compute/docs/regions-zones#available) for your cluster.



If the output is empty, the cluster isn't enrolled in a release channel.

## View the default and available versions for release channels

To check what versions are available in a specific release channel with the Google Cloud console or gcloud CLI, follow the instructions to [check available and default versions](https://docs.cloud.google.com/kubernetes-engine/versioning#available_versions).

## Change your cluster's release channel

You can change the release channel of your cluster if the control plane's minor version is available in the target release channel. You might need to upgrade or downgrade your cluster's control plane to an available version.

To check if your cluster's control plane version is available in the target release channel, view the default and available versions for release channels. The version must be available in the target channel.

  * If your cluster's control plane version is already available in the target release channel, you can select the new release channel.
  * If your cluster's control plane version is not available in the target release channel, you can upgrade the cluster's control plane to an available version. Alternatively, if the target channel only has earlier versions available, you can [downgrade the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#downgrading_clusters), provided that the target version is an [earlier patch release from the same minor version](https://docs.cloud.google.com/kubernetes-engine/versioning#versioning_scheme).



To select a new release channel, update the cluster release channel to the target `CHANNEL`. If you want to temporarily prevent the cluster from being automatically upgraded when you select the new channel, [configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) before selecting the new channel.

If you can't select the target release channel because your cluster is running a version that is not available in that release channel, you can do the following:

  1. [Configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion) with a scope of "No minor upgrades".
  2. Wait for the [target release channel to make available](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#what_versions_are_available_in_a_channel) the Kubernetes minor version of your cluster.
  3. Enroll the existing cluster in the target release channel.



Alternatively, you can [create a new cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-a-regional-cluster) in the target channel and migrate your workloads.

### Change your cluster to the Extended channel

To get [long-term support](https://en.wikipedia.org/wiki/Long-term_support), keeping your cluster on that version for as long as possible, you can enroll your cluster in the Extended channel.

Ensure that you review the [pricing](https://cloud.google.com/kubernetes-engine/pricing#extended-support-period) for enrolling your cluster in the Extended channel, and the [feature limitations](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#limitations-for-extended). You can't enroll your cluster in the Extended channel if your cluster is using certain features.

### Change your cluster from the Extended channel

If a cluster is enrolled in the Extended channel during the extended support period, the cluster can continue to run a minor version that is unsupported in other channels. If you want to change your cluster from the Extended channel, where the minor version is unsupported, you must take the following steps:

  1. Complete these two steps, which can be done in either order: 
     1. [Manually upgrade your cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) to a minor version in the [standard support period](https://docs.cloud.google.com/kubernetes-engine/versioning#standard-support) available on the target release channel.
     2. [Remove](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#remove-exclusions) or modify any maintenance exclusion with an end date that exceeds the end of standard support date for that newer, supported minor version.
  2. Update the cluster's release channel.



### Update the cluster release channel

You can change your cluster's release channel using the Google Cloud console or gcloud CLI.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to inspect.

  3. Under **Cluster basics** , in the **Release channel** field, click _edit_.

  4. In the **Release channel** drop-down, select the target release channel.

  5. Read and acknowledge the warning by selecting **I understand there may be downtime during version upgrades.**

  6. Click **Save Changes**.




### gcloud

Change the release channel property of an existing cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --release-channel CHANNEL
    

Replace the following:

  * `CLUSTER_NAME`: the name of your cluster.
  * `CHANNEL`: the target release channel, which can be one of `rapid`, `regular`, `stable`, and, for Standard only, `extended` or `None`.



## Unsubscribe from a release channel

**Warning:** Not enrolling your cluster in a release channel (known as _No channel_ , and formerly as _Static_) is a deprecated configuration option, only allowed for existing customers, and will be removed on June 14, 2027. New customers can't create or update their cluster to use this configuration option. For any clusters not enrolled in a release channel, we recommend that you [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster) before this date. After the removal date, GKE enrolls all remaining clusters in the Stable channel. For more information about this deprecation and how you can achieve the same functionality with release channels, see [Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel).

While you can unsubscribe your Standard cluster from a release channel until June 14, 2027, this is a deprecated configuration option and we strongly recommend that you review the [comparison between clusters enrolled and not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#comparison-table-no-channel). Ensure that you understand the tradeoffs between enrolling and not enrolling your cluster in a release channel.

You can perform this action with the Google Cloud console, the gcloud CLI, or the GKE API. You can also specify that you don't want to enroll your Standard cluster in a release channel during cluster creation. You can't unsubscribe [Autopilot clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/types-of-clusters#modes) from a release channel.

### Console

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click the name of the cluster you want to inspect.

  3. Under **Cluster basics** , in the **Release channel** field, click _edit_.

  4. Select the **No channel** version from the drop-down menu.

  5. Read and acknowledge the warning by selecting **I understand there may be downtime during version upgrades.**

  6. Click **Save Changes**.




### gcloud

Update the cluster's release channel to a value of `None`:
    
    
    gcloud container clusters update CLUSTER_NAME \
      --release-channel None
    

### API

Specify `"releaseChannel": { "channel": UNSPECIFIED}` when you create or update a cluster.

## Identify clusters not enrolled in a release channel

**Warning:** Not enrolling your cluster in a release channel (known as _No channel_ , and formerly as _Static_) is a deprecated configuration option, only allowed for existing customers, and will be removed on June 14, 2027. New customers can't create or update their cluster to use this configuration option. For any clusters not enrolled in a release channel, we recommend that you [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster) before this date. After the removal date, GKE enrolls all remaining clusters in the Stable channel. For more information about this deprecation and how you can achieve the same functionality with release channels, see [Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel).

If you have a GKE Standard cluster that isn't enrolled in a release channel, and all node pools have [node auto-upgrade enabled](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#check_the_state_of_auto-upgrade_for_an_existing_node_pool), GKE recommends that you enroll the cluster in a release channel, delivering this guidance with an insight and recommendation through the [ Recommender](https://docs.cloud.google.com/recommender/docs/overview) service. This guidance doesn't apply to Autopilot clusters, which are always enrolled in a release channel.

To find clusters not enrolled in a release channel, you can use the one of the following ways:

  * Use the Google Cloud console.
  * Use the gcloud CLI or Recommender API, by specifying the `CLUSTER_RELEASE_CHANNEL_UNSPECIFIED` [recommender subtype](https://docs.cloud.google.com/recommender/docs/key-concepts#recommender_subtype).



For instructions, see how to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

To implement this recommendation, follow the instructions to enroll existing clusters. To learn more about whether you want to implement this recommendation, see [About release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels). For a comparison of capabilities between a cluster enrolled or not enrolled in a release channel, review the [comparison between clusters enrolled and not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#comparison-table-no-channel).

## Use accelerated patch auto-upgrades

You can use [accelerated patch auto-upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#accelerated-patch) so GKE automatically upgrades your cluster to patch versions as soon as they're available in a release channel, rather than when GKE sets the versions as an auto-upgrade target at least one week later.

To use accelerated patch auto-upgrades, set the `--patch-update=accelerated` flag with the gcloud CLI when you [create the cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create#--patch-update), or [update the cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--patch-update).

This setting is available only for clusters enrolled in a release channel, and doesn't affect minor version upgrades.

### Disable accelerated patch auto-upgrades

You can update the cluster to disable accelerated patch auto-upgrades for your cluster, so that the cluster receives patch versions only after GKE sets the patch version as an auto-upgrade target. This action reverts the cluster back to the default setting, and doesn't disable auto-upgrades.

To [update the cluster](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update#--patch-update), set the `--patch-update=default` flag.

## What's next

  * [About release channels](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
