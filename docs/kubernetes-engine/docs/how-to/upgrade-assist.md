---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist/
title: Get visibility into cluster upgrades \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:21:39.100305+00:00
---

# Get visibility into cluster upgrades  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Get visibility into cluster upgrades Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

This page explains how you can get information about upgrades for your Google Kubernetes Engine (GKE) clusters. GKE automatically upgrades all clusters over time. When GKE upgrades a cluster, GKE updates the version of the Kubernetes control plane and worker nodes in separate operations.

GKE aggregates information about cluster upgrades to help you better understand the status of your cluster. You can get the following information for a cluster:

  * **Scheduled upgrades ([Preview](https://cloud.google.com/products#product-launch-stages))**: GKE notifies you at least 72 hours in advance of [automatic cluster control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades) and [automatic cluster node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades). When you enable scheduled upgrades, GKE still automatically upgrades a cluster on a regular basis, but only after providing this advanced notice. If you're not notified in advance, your cluster isn't automatically upgraded.
  * **Auto-upgrade targets** : Find which new versions GKE is targeting for your cluster, which could be patches or new minor versions, depending on your cluster's existing version and constraints. If there is no auto-upgrade target, the cluster is on the latest upgrade target already, or GKE hasn't assigned an auto-upgrade target for technical or business reasons. You can also retrieve general auto-upgrade targets based on a cluster's minor version in the [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes) _Version updates_ , such as the [2024-R33 note](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes#2024-r33_version_updates).
  * **Auto-upgrade status** : GKE clusters have a status for cluster upgrades. Use this status to learn more about current upgrades, and the constraints GKE considers when choosing when to automatically upgrade your cluster, including factors such as maintenance exclusions or reasons preventing upgrades. To learn more, see Cluster auto-upgrade status.
  * **Upgrade history** : GKE provides a snapshot into recent control plane upgrades and node upgrades for your cluster, including both automatic and manual upgrades. For recent control plane and node upgrades, you can see details such as the following:

    * **Versions** : the initial and target version.
    * **State** : whether the upgrade is still running, or if it succeeded, failed, or was canceled.
    * **Time** : the start and end time.
    * **Start type** : whether the upgrade was triggered automatically or manually.
  * **End of support dates** : GKE supports minor versions for up to 24 months. To learn more, see the [GKE minor version lifecycle](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle). For end of support dates for all current minor versions, see the [Estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels).

  * **Cluster events** : GKE sends cluster notifications to Cloud Logging for certain events, such as when upgrades start or complete, when new versions are available, security bulletins, and end of support dates. In addition to GKE surfacing these events automatically with Cloud Logging, you can also route these notifications to Pub/Sub. To learn more, see [Cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).




## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.



## Get notified about scheduled cluster upgrades

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

You can enable scheduled upgrades for GKE to notify you in advance about the following types of automatic cluster upgrades:

  * [Control plane upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_cp_upgrades)
  * [Node upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades), with one notification per [auto-upgrade target](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#auto-upgrade-target)



After you enable this opt-in feature, GKE publishes a cluster notification to Cloud Logging, or, optionally, to Pub/Sub, informing you of the following:

  * The cluster name.
  * The start time of the upgrade window. The window is 8 hours for the control plane, and 10 days for the nodes.
  * The target version.
  * Affected node pools (for node upgrades): Each notification is for a single auto-upgrade target and lists up to 10 node pools that are scheduled for upgrade. Note that all node pools sharing this auto-upgrade target will be upgraded, not only the listed ones. To confirm if a specific node pool is affected, verify that its auto-upgrade target matches the one in the notification by getting upgrade information for the node pools.



GKE notifies you between 72 and 96 hours in advance of the start time. GKE starts the control plane upgrade or node upgrades within the 8 hour (control plane) or 10 day (nodes) start time window to one of the following:

  * The GKE version stated in the notification
  * A later patch in the same minor version if a patch becomes an auto-upgrade target in your cluster's release channel before the upgrade



Scheduled upgrade notifications provide certainty about when GKE would start an upgrade of a control plane or node pool. However, this notification doesn't guarantee that GKE upgrades your cluster at the provided time. And, the notification only informs you about when the upgrade starts, and doesn't guarantee whether the upgrade completes.

If you enable this feature and have many nodes in your cluster, we recommend that you also [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#concurrent-upgrades) so that node upgrades can complete as quickly as is acceptable for your cluster environment.

If you don't enable this feature, GKE still automatically upgrades your cluster control plane. However, the default behavior without this feature is that you don't receive a scheduled upgrade notification in advance.

Review the following sections to understand what actions you can take, or not take, when you receive a scheduled upgrade notification, and other reasons why GKE might not upgrade a cluster at the given time.

### What to do when you get a scheduled upgrade notification

If you're ready for the scheduled upgrade to proceed at the time given in the notification, you don't need to take any further action, other than monitoring the health of your cluster environment and workloads when GKE initiates the automatic upgrade.

Or, you can take some of the following actions, which would affect the timing of the upgrade:

  * **Maintenance exclusion** : If you aren't ready for GKE to automatically upgrade the control plane or node pool, you can [configure a maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#configuring_a_maintenance_exclusion), which prevents the upgrade from happening when it was scheduled to take place.
  * **Maintenance window** : You could also [configure a maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions#maintenance-window), which could designate a different time of the week for GKE to automatically upgrade your cluster.
  * **Manual upgrade** : If you want the upgrade to take place sooner, you can [manually upgrade the cluster's control plane](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrading_the_cluster) or [manually upgrade the node pool](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-cluster#upgrade_nodes), depending on the type of scheduled upgrade.



### Reasons that GKE might not perform a scheduled upgrade

GKE might not perform a scheduled upgrade in the given time window if an issue with the version was observed between when the notification was sent and when the upgrade was scheduled to start. For more information, see Find what is blocking your cluster's next upgrade.

For node upgrades, where GKE sends a notification aggregating all node pools with the same auto-upgrade target, GKE might not be able to start all upgrades before the end of the 10 day time window. For clusters with many node pools, or node pools that take longer to upgrade—such as large node pools with many nodes—this scenario is more likely. For these clusters where node upgrades might take longer to complete, we recommend that you [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#concurrent-upgrades) so that GKE can upgrade multiple node pools at the same time within the 10 day window.

If GKE cancels or is not able to perform the scheduled upgrade, either because of your actions, time limitations, or other unforeseen circumstances, GKE sends another cluster notification when the upgrade is rescheduled.

### Limitations

  * You can't enable scheduled upgrades with [rollout sequencing](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/rollout-sequencing/about-rollout-sequencing).
  * GKE doesn't send a notification for a scheduled upgrade being canceled. GKE only sends a notification for a new scheduled upgrade.
  * If you enable scheduled upgrades, this enablement might cause automatic upgrades to be completed more slowly than without the notifications enabled. This effect occurs because, for each upgrade, GKE needs to provide the minimum 72 hours of notice, adhere to the start window, and adhere to any [maintenance window](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance_windows), if you've configured one for the cluster. If you need upgrades to proceed in your cluster with maximum efficiency, and especially if you have a large number of node pools or large node pools, we also recommend [configuring concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#concurrent-upgrades). Additionally, you can use manual upgrades to advance upgrades when needed.
  * Don't enable scheduled upgrades for clusters with more than 1,000 node pools.
  * GKE only provides advanced notice for version upgrades—including control plane and node upgrades—and not for other types of node updates. For more information about the difference between upgrades (version updates) and other types of updates, see [Manage cluster lifecycle changes to minimize disruption](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters).
  * You can't enable or disable scheduled upgrades with Terraform.
  * Scheduled upgrade notifications only provide assurance that automatic cluster control plane or node upgrades don't start without prior notification. However, the notification doesn't guarantee the following:

    * It isn't guaranteed that upgrades start at an exact time, only within an 8 hour start window for control plane upgrades, or a 10 day start window for node upgrades.
    * It isn't guaranteed that GKE starts the upgrade within that window of time. For more information, see Reasons that GKE might not perform a scheduled upgrade.
    * It isn't guaranteed that GKE automatically upgrades your control plane or node pools to the exact patch version, if there is a later patch auto-upgrade target of the same minor version in the release channel.



### Enable scheduled upgrades

Enable scheduled upgrades, replacing `CLUSTER_NAME` with the name of the cluster:
    
    
    gcloud beta container clusters update CLUSTER_NAME
       --enable-scheduled-upgrades
    

After you enable scheduled upgrades, you can view the notifications with Cloud Logging, or configure notifications with Pub/Sub. For more information, see [Cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).

Additionally, if you have many nodes in your cluster, we also recommend that you [configure concurrent node pool upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades#concurrent-upgrades) so that node upgrades can complete as quickly as is acceptable for your cluster environment.

When you get a scheduled upgrade notification, review What to do when you get a scheduled upgrade notification.

### Disable scheduled upgrades

Disable scheduled upgrades, replacing `CLUSTER_NAME` with the name of the cluster:
    
    
    gcloud beta container clusters update CLUSTER_NAME
       --disable-scheduled-upgrades
    

After you disable this feature, GKE doesn't notify you anymore about scheduled upgrades.

## Get information about a cluster's upgrades

You can get information proactively about a cluster's upgrades by using the Google Cloud console, or the gcloud CLI.

### Get information about upgrades at the project level

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To get aggregated information about cluster upgrades across a project, you can use the **Upgrades** dashboard.

In the Google Cloud console, go to the **Upgrades** dashboard:

[Go to Upgrades](https://console.cloud.google.com/kubernetes/upgrades/overview)

The tabs included in this dashboard aggregate relevant information about upgrades such as the following:

  * Statuses of recent control plane and node upgrades
  * Cluster notification logs for upgrades
  * Recommendations that are related to upgrades
  * End of support timelines for specific minor versions
  * The number of clusters in each release channel



### Get upgrades information at the cluster level

### Console

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Select the name of your cluster to view its **Cluster Details** page.

  3. On the **Cluster Details** page, see the **Cluster upgrades** section.




### gcloud

Run the following command:
    
    
    gcloud container clusters get-upgrade-info CLUSTER_NAME
    

Replace `CLUSTER_NAME` with the name of the cluster.

### Get upgrades information for Standard cluster node pools

You can get visibility into individual node pools for Standard clusters. This section doesn't apply to Autopilot clusters, where GKE manages the nodes, so there are no node pools for you to manage.

### Console

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

  1. In the Google Cloud console, go to the **Kubernetes clusters** page.

[Go to Kubernetes clusters](https://console.cloud.google.com/kubernetes/list/overview)

  2. Click the name of your cluster to view its details.

  3. Click the **Nodes** tab.

  4. In the **Node Pools** section, click the name of the node pool for which you want to get upgrades information.

  5. On the **Node pool details** page, see the **Upgrades** section.




### gcloud

Run the following command:
    
    
    gcloud container node-pools get-upgrade-info POOL_NAME
        --cluster=CLUSTER_NAME
    

Replace `POOL_NAME` with the name of the node pool.

## Cluster auto-upgrade status

The following are the potential statuses of automatic upgrades for a cluster:

  * `ACTIVE`: An active upgrade status.
  * `UNKNOWN`: The upgrade status is unknown.
  * `MINOR_UPGRADE_PAUSED`: Minor version upgrades are paused.
  * `UPGRADE_PAUSED`: All automatic upgrades are paused.



The following are the potential reasons that GKE pauses automatic upgrades for a cluster:

  * `MAINTENANCE_WINDOW`: A maintenance window is preventing cluster upgrades.
  * `MAINTENANCE_EXCLUSION_`: A paused reason with this prefix indicates that a maintenance exclusion is preventing cluster upgrades. The suffix indicates the [scope of the maintenance exclusion](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#scope_of_maintenance_to_exclude), such as `MAINTENANCE_EXCLUSION_NO_UPGRADES`.
  * `CLUSTER_DISRUPTION_BUDGET`: After certain operations, such as cluster creation or upgrades, clusters require a cooldown period to protect the stability and availability of the cluster and its applications.
  * `CLUSTER_DISRUPTION_BUDGET_MINOR_UPGRADE`: The cluster is outside of the cluster disruption budget for minor version upgrades.
  * `SYSTEM_CONFIG`: Automatic upgrades are temporarily paused for technical or business reasons. With this status, we recommend not performing a manual upgrade unless it's required.
  * `AUTO_UPGRADE_PAUSED_REASON_UNSPECIFIED`: An unspecified reason.



## Find information about common scenarios for cluster upgrades

Find information about common scenarios you might encounter when managing cluster upgrades.

### Find when to expect your cluster's next upgrade

To learn when to expect your cluster's next upgrade so that you can plan for and qualify the upgrade to the new version, use the following resources:

  * **Release schedule** : In the [estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels), find the estimated auto-upgrade date that corresponds with your cluster's minor version and release channel.
  * **Get upgrades information at the cluster level**: Find your cluster's auto-upgrade target.
  * **Cluster notifications** : GKE sends a notification when a new version becomes available in a channel. After a new version becomes available, with the timing depending on the channel, GKE designates the version as an auto-upgrade target in the channel. To view these notifications, filter for the `UpgradeAvailableEvent` when you [view cluster notifications in Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#viewing-logging).
  * [**Release notes**](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes): Follow the release notes to learn when GKE sets the new minor version as an auto-upgrade target in the channel.



### Find what is blocking your cluster's next upgrade

To learn what is blocking an upgrade so that you can unblock it, find your cluster's auto-upgrade status. If auto-upgrades are paused, see the reason. Use one of the following methods:

  * Get upgrades information at the project level (Preview). Click the **Upgrades** tab, where you can see the [Upgrade statuses](https://console.cloud.google.com/kubernetes/upgrades/list) table. Look for your cluster in the table, and see the cluster's **Auto-upgrade** column.
  * Get upgrades information at the cluster level to find your cluster's auto-upgrade status.



### Find when your cluster's upgrade completes

To learn when your cluster's control plane and node upgrades complete so that you can verify that your workloads are working as expected, use the following resources:

  * **Cluster notifications** : GKE sends a notification when GKE finishes an operation to upgrade a cluster. To view these notifications, filter for the `UpgradeInfoEvent` when you [view cluster notifications in Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#viewing-logging).
  * **Upgrades dashboard** (Preview): Go to the [Upgrade statuses](https://console.cloud.google.com/kubernetes/upgrades/list) table in the Google Cloud console. Find your cluster. If the **Status** column says _Upgraded_ , see from the **Latest update** column when the upgrade completed.
  * **Get upgrades information at the cluster level**: Use the gcloud CLI to find your cluster's upgrade history, which includes recent upgrades.



### Find how long your upgrade is expected to take

To learn how long your upgrade is expected to take, you can find the duration of past upgrades by getting upgrades information at the cluster level. See the upgrade history for recent examples.

The length of an upgrade depends on whether the control plane or nodes are being upgraded, the upgrade strategy, Pod Disruption Budgets (PDBs), active maintenance policies, and other factors.

### Find when your cluster's minor version reaches the end of support

GKE automatically upgrades clusters that are still running minor versions past their end of support date. For more information, see [Automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support).

To learn when your cluster's minor version reaches the end of support—for example, to set a maintenance exclusion or understand when deprecated APIs won't be usable anymore—use the following resources:

  * **Release schedule** : In the [estimated schedule for release channels](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels), find the end of support date that corresponds with your cluster's minor version and release channel. For clusters that are not in the Extended channel, see the end of standard support date. For clusters that are in the Extended channel, see the end of extended support date.
  * **Cluster notifications** : GKE sends a notification for when a cluster runs a minor version at or near the end of support. To view these notifications, filter for the `UpgradeInfoEvent` when you [view cluster notifications in Cloud Logging](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications#viewing-logging).
  * **Insights and recommendations** : GKE informs you when your cluster is running a minor version past the end of standard support. For more information, see [Identify clusters running a minor version past the end of standard support](https://docs.cloud.google.com/kubernetes-engine/versioning#recommender-end-of-support).
  * [**Get upgrades information at the cluster level**](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrade-assist#get-info-cluster): Find your cluster's minor version end of support date.
  * **Upgrades dashboard** (Preview): The **Upgrades** dashboard includes a **Version end of support** section with specific versions and their days remaining until end of support.



## What's next

  * [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule)
  * [GKE release notes](https://docs.cloud.google.com/kubernetes-engine/docs/release-notes)
  * [Cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
