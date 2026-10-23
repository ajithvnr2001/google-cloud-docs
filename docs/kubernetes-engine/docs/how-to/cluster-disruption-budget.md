---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget/
title: Control the frequency of disruption from auto-upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:23:33.920462+00:00
---

# Control the frequency of disruption from auto-upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/cluster-disruption-budget/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Control the frequency of disruption from auto-upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This document introduces the concept of _cluster disruption budgets_ , and explains how you can optionally customize them to fit your environment's needs. Cluster disruption budgets are one tool in a suite of features which empower a platform administrator to minimize disruption to workloads while enhancing their performance, reliability, and security.

Cluster upgrades—which are when GKE updates the version used by your cluster's control plane and nodes—can be a primary source of disruption for a GKE cluster. For more information about what upgrades are, see [About GKE cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades). To learn about all of the other features for minimizing disruption during cluster upgrades, see that document's [Control cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#how-to-control-upgrades) section. For more general information about cluster lifecycle changes beyond cluster upgrades, see [Manage cluster lifecycle changes to minimize disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters).

## What is a cluster disruption budget

To help ensure that your cluster isn't disrupted by automatic upgrades too frequently, GKE, by default, applies a _cluster disruption budget_ to set a minimum interval between [automatic cluster control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades). GKE also applies this budget between cluster creation and the first automatic control plane upgrade. Also, if you manually upgrade the cluster control plane, GKE respects the cluster disruption budget when performing the next automatic upgrade. You can always manually upgrade the cluster, even if this upgrade violates the cluster disruption budget.

In a cluster, GKE automatically upgrades the control plane before the nodes. So, this budget also sets the minimum cadence of [automatic cluster node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades).

GKE has default cluster disruption budgets for [different types of version upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_upgrades):

  * **Patch version upgrades** : 24 hours
  * **Minor version upgrades** : 30 days



GKE applies the budget between the same types of upgrades. For example, GKE waits 24 hours between upgrading a cluster between the patch versions 1.35.0-gke.1403000 and 1.35.0-gke.1624000, and 30 days between 1.34 and 1.35. However, GKE waits 24 hours after a minor upgrade before performing a patch upgrade.

GKE uses a cluster disruption budget only for cluster upgrades, and not for other [types of changes to a GKE cluster](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#types-of-changes).

The cluster disruption budget is distinct from, but can pair well with, [maintenance windows and exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions). Maintenance policies control when GKE cluster maintenance can and can't happen, whereas the cluster disruption budget sets a specific interval of time between cluster upgrades.

## When to customize your cluster's disruption budget

GKE's default cluster disruption budgets reflect a balance between timeliness of upgrades, while also avoiding back-to-back upgrades and optimizing for stability. However, these general values might not be ideal for your cluster environment.

If you want to control this minimum amount of time between automatic cluster upgrades, you can configure the cluster disruption budget. Consider, for example, the following scenarios:

  * You have a custom process for evaluating a GKE control plane patch version before pushing the version to production, and this process takes a specific amount of time greater than the default cluster budget.
  * You have large clusters which take a longer amount of time to upgrade all of the node pools. You want to maintain relative consistency of versions across these node pools. So, you lower the frequency of patch upgrades, upgrading monthly, while allowing frequent maintenance windows to help ensure that node pool upgrades complete in a timely manner.



## Set the cluster disruption budget for automatic upgrades

If you have a specific need for controlling the interval between two minor upgrades or two patch upgrades, you can set your own cluster disruption budgets. First, however, we recommend that you start by configuring a [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows) to set a recurring time for GKE cluster maintenance. Then, you can optionally customize the interval between upgrades with the cluster disruption budget.

We recommend that you use the cluster disruption budget along with [the other available tools GKE offers to control cluster upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#how-to-control-upgrades). These settings, which work with all other upgrade tools, affect only the timing of when GKE auto-upgrades a cluster to a new version. GKE still adheres to maintenance windows and exclusions, follows the order of a rollout sequence, and applies any other standard practices that are typically used for automatic upgrades.

The default cluster disruption budget is 24 hours for patch upgrades, and 30 days for minor upgrades. You can configure the intervals for any amount of time between 0 and 90 days. However, you should be aware of the following considerations when updating these values:

  * We recommend that you don't set the patch upgrades interval for greater than 30 days, unless you have a specific version qualification process which takes longer than this. You might miss critical patches if you upgrade with less frequency than 30 days.
  * We recommend that you allow for minor upgrades as frequently as is acceptable for your cluster environment. If you set the minor upgrades interval for the maximum of 90 days, you increase the chance that GKE must upgrade your cluster from the minor version when it reaches the end of support. GKE adheres to a separate cluster disruption budget for minor upgrades of 7 days when a minor version reaches the end of support, and doesn't adhere to any cluster disruption budget that you configured. For more information, see [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).
  * We recommend that you set the patch upgrades interval for a shorter period of time than the minor upgrades interval.



### Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



### Configure the cluster disruption budget

First, if you haven't already done so, we recommend that you [configure a maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window).

Then, to set a custom cluster disruption budget, use the following flags when you create or update a cluster using the gcloud CLI:

  * **Minor upgrades** : `--maintenance-minor-version-disruption-interval=MINOR_INTERVAL`
  * **Patch upgrades** : `--maintenance-patch-version-disruption-interval=PATCH_INTERVAL`



For these flags, replace `MINOR_INTERVAL` or `PATCH_INTERVAL`, respectively, with a duration expressed in seconds between 0 days (`0s`) and 90 days (`7776000s`).

You can use these flags in the following situations:

  * **Create a cluster** : 
    * **Autopilot** : [`gcloud container clusters create-auto`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create-auto)
    * **Standard** : [`gcloud container cluster create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/create)
  * **Update a cluster** : [`gcloud container cluster update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update)



You can use the flags at the same time or independently.

### Reset the cluster disruption budget to the default values

To reset the cluster disruption budget to the default values of 24 hours for patch upgrades and 30 days for minor upgrades, you can use the following flags:

  * **Minor upgrades** : `--clear-maintenance-minor-version-disruption-interval`
  * **Patch upgrades** : `--clear-maintenance-patch-version-disruption-interval`



Use these flags when you update a cluster with the [`gcloud container cluster update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/clusters/update) command.

You can use the flags at the same time or independently.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
