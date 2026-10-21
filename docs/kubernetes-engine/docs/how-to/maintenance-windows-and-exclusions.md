---
url: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions/
title: Configure maintenance windows and exclusions \u00a0|\u00a0 Google Kubernetes Engine (GKE) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:31:24.043790+00:00
---

# Configure maintenance windows and exclusions  |  Google Kubernetes Engine (GKE)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/docs/how-to/maintenance-windows-and-exclusions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ Google Kubernetes Engine (GKE) ](https://docs.cloud.google.com/kubernetes-engine/docs)
  * [ Guides ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/kubernetes-engine-overview)



Send feedback 

#  Configure maintenance windows and exclusions Stay organized with collections  Save and categorize content based on your preferences. 

[ Autopilot ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/autopilot-overview) [ Standard ](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/choose-cluster-mode)

Use [maintenance windows and maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions) to control when automatic cluster maintenance, such as auto-upgrades, can and can't occur on your Google Kubernetes Engine (GKE) clusters. Before configuring these maintenance policies, ensure that you review what [changes do and don't respect GKE maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#what-changes-maintenance-policies).

## Before you begin

Before you start, make sure that you have performed the following tasks: 

  * Enable the Google Kubernetes Engine API. 
[ Enable Google Kubernetes Engine API ](https://console.cloud.google.com/apis/enableflow?apiid=container.googleapis.com)
  * To use the Google Cloud CLI for this task, [install](https://docs.cloud.google.com/sdk/docs/install) and then [initialize](https://docs.cloud.google.com/sdk/docs/initialize) the gcloud CLI. If you previously installed the gcloud CLI, get the latest version by running the `gcloud components update` command. Earlier gcloud CLI versions might not support running the commands in this document. **Note:** For existing gcloud CLI installations, make sure to set the `compute/region` [property](https://docs.cloud.google.com/sdk/docs/properties#setting_properties). If you use primarily zonal clusters, set the `compute/zone` instead. By setting a default location, you can avoid errors in the gcloud CLI like the following: `One of [--zone, --region] must be supplied: Please specify location`. You might need to specify the location in certain commands if the location of your cluster differs from the default that you set.


  * Ensure that you have an existing Autopilot or Standard cluster. If you need one, [create an Autopilot cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/creating-an-autopilot-cluster).



## Configure a maintenance window

To configure a maintenance window, specify when it starts, how long it lasts, and how often it repeats. For example, you can configure a maintenance window that recurs weekly on Monday through Friday for four hours each day.

You can configure a maintenance window by using the Google Cloud console or the Google Cloud CLI.

### Considerations when configuring a maintenance window

When configuring a maintenance window, follow this guidance:

  * Understand which types of maintenance events do and don't respect GKE maintenance windows. To learn more, see [Automatic maintenance that respects GKE maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#examples_of_automatic_maintenance) and [Automatic maintenance that doesn't respect GKE maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#caveats).
  * You can only configure one maintenance window for a cluster, and configuring a new window overwrites the previous one.
  * You must allow at least 48 hours of maintenance availability in a 92-day rolling window. Only contiguous availability windows of at least four hours are considered.
  * When using the Google Cloud console, times are always displayed using the local time zone.
  * Day of the week recurrences are always based on UTC. As a result, we recommend setting maintenance windows involving such recurrences entirely in UTC, through the gcloud CLI. While local time can be used when setting flags, the time zone won't be stored. For example, if your time zone is UTC+6 and you want a maintenance window to start at 02:00 on Wednesdays in your time zone, then specify a UTC value of 20:00 on Tuesdays. To learn more, see [Time zones for maintenance windows](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#caveat-timezones).



### Configure a maintenance window

You can configure a maintenance window on an existing cluster by using the Google Cloud console or the gcloud CLI. Maintenance windows continue recurring until you remove the maintenance window.

### gcloud

Create or update a maintenance window for an existing cluster:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --maintenance-window-start START_TIME \
        --maintenance-window-duration DURATION \
        --maintenance-window-recurrence RRULE
    

Replace the following:

  * `CLUSTER_NAME`: the name of the cluster.
  * `START_TIME`: the time of day that the recurring maintenance window starts, expressed as an [RFC-5545](https://tools.ietf.org/html/rfc5545) DTSTART value. You can also include a future date, if you want the maintenance window to start repeating according to the `RRULE` only after a future date. If you provide the date but not the time, the time defaults to midnight at the start of the day.
  * `DURATION`: the duration of the maintenance window, expressed as an [ISO 8601 duration](https://en.wikipedia.org/wiki/ISO_8601#Durations) in hours, minutes, and seconds. You must set a maintenance window to at least 4 hours (`4H`).
  * `RRULE`: the recurrence of the maintenance window, as expressed by an [RFC-5545](https://tools.ietf.org/html/rfc5545) RRULE. This is a flexible format with multiple ways to specify recurrence rules, determining what day the maintenance window starts. For example, you can specify a recurrence of certain times a week or month. If the `END_TIME` date is greater than the `START_TIME` date, the maintenance window spans multiple days. For example, a maintenance window starting on Sunday would continue to Monday.



For example, the following command edits a cluster named `my-cluster` with a maintenance window enabled at 2:00 AM UTC on Friday, August 23, 2024. This maintenance window recurs weekly every Monday and Friday, and ends 30 hours later. The first occurrence of the maintenance window starts on Friday, August 23 at 2:00 AM and ends on Saturday, August 24, at 8:00 AM. You can learn more about [formatting dates and times](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).
    
    
    gcloud container clusters update my-cluster \
        --maintenance-window-start 2024-08-23T02:00:00Z \
        --maintenance-window-duration 30H \
        --maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=MO,FR'
    

For more scenarios, see the example maintenance windows.

### Console

To create or modify a maintenance window for an existing cluster:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Automation** , click _edit_ **Edit maintenance policy** next to the **Maintenance window** field.

  4. Select the **Enable Maintenance Window** checkbox.

  5. Select the start time and length, then select the days of the week on which the maintenance window occurs. To edit the **RRule** directly, select **Custom editor**.

  6. Click **Save Changes**.




### Manually finish incomplete maintenance

If an upgrade or other automatic maintenance takes longer than the maintenance window to complete, GKE attempts to stop ongoing maintenance tasks and resumes them during the next occurrence of the maintenance window. If an automatic upgrade is canceled, and you have node auto-upgrades enabled, your nodes might be in a mixed-version state but your cluster should operate normally.

To manually upgrade your cluster, or cancel or roll back a partial upgrade, visit [Manually upgrading a cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/upgrading-a-container-cluster).

### Remove a maintenance window

### gcloud

Remove a maintenance window from a cluster:
    
    
    gcloud container clusters update CLUSTER_NAME --clear-maintenance-window
    

Replace `CLUSTER_NAME` with the name of the existing cluster.

### Console

To remove a maintenance window:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Automation** , click _edit_ **Edit maintenance policy** next to the **Maintenance window** field.

  4. Clear the **Enable Maintenance Window** checkbox.

  5. Click **Save Changes**.




### Example maintenance windows

The following examples illustrate some of the different ways you can configure a maintenance window. Only the relevant flags are shown, because the flags use the same syntax for creating a new cluster or updating an existing one.

#### Weekends, starting August 22, 2026

In this example, the difference between the start and end timestamps is two full days, so the maintenance window runs for the entire weekend, throughout Saturdays and Sundays. If you want the window to be a different length than exactly 48 hours, modify the value set for the `--maintenance-window-duration` flag.
    
    
      --maintenance-window-start 2026-08-22T00:00:00Z \
      --maintenance-window-duration 48H \
      --maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=SA'
    

#### Daily on weekdays from 9:00-17:00 UTC-4

This example shows how to have a daily maintenance window, but skip weekends. This example specifies a non-UTC time zone.
    
    
       --maintenance-window-start 2026-09-02T09:00:00-04:00 \
       --maintenance-window-duration 8H \
       --maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=MO,TU,WE,TH,FR'
    

#### Weekly at 4PM for 8 hours, UTC-7

If you don't specify a time zone for `--maintenance-window-start`, local time is used, as configured in your Google Cloud account. _The Google Cloud console always uses local time._
    
    
       --maintenance-window-start 2026-08-13T16:00:00-7:00 \
       --maintenance-window-duration 8H \
       --maintenance-window-recurrence 'FREQ=WEEKLY'
    

#### Weekdays at night

This example shows a daily maintenance window that runs overnight between workdays in the UTC-7 time zone. In this example, the window runs from 20:00 in the evening until 4:00 the next morning.
    
    
       --maintenance-window-start 2026-08-15T20:00:00-7:00 \
       --maintenance-window-duration 8H \
       --maintenance-window-recurrence 'FREQ=WEEKLY;BYDAY=MO,TU,WE,TH'
    

## Configure a maintenance exclusion

With GKE, you can configure two types of [maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#exclusions): cluster maintenance exclusions and node pool maintenance exclusions. For more information, see [Types of maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#types-of-exclusions).

The following information applies to cluster maintenance exclusions. For more information about the requirements for node pool maintenance exclusions, see [Node pool maintenance exclusions](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#node-pool-exclusions).

**Note:** If you want to restrict what types of automatic cluster upgrades that GKE performs for entire rollout sequences, you can use rollout sequencing with custom stages and set the scope of upgrades for that sequence. For more information, see [How maintenance exclusions work with setting the scope of a rollout sequence](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#maintenance-exclusion-rs).

To set up a cluster maintenance exclusion for your cluster, you need to specify the following:

  * **Name** : the name of the exclusion (optional).
  * **Start time** : the date and time for when the exclusion period should start. The start time must be now or in the future.
  * **End time** : the date and time for when the exclusion period should end. Refer to the following table for restrictions on the length of an exclusion period for each of the available scopes. For certain scopes of maintenance exclusion, you can set the end time to track the [end of support date](https://docs.cloud.google.com/kubernetes-engine/versioning#lifecycle) for your cluster's minor version.
  * **Scope** : the scope of automatic upgrades to restrict. Refer to the following table that lists the available exclusion scopes.

Scope | Control plane | Nodes | Maximum exclusion length  
---|---|---|---  
Automatic minor upgrade | Automatic patch upgrade | Automatic minor upgrade | Automatic patch upgrade  
No upgrades (default) | Not allowed | Not allowed | Not allowed | Not allowed |  Cannot exceed 90 days. We recommend limiting the length of this type of maintenance exclusion to less than 30 days. Only set the maintenance exclusion for greater than 30 days if you have a specific version qualification process which takes longer than this, or a high-impact event which requires restricted changes for more than 30 days. You might miss critical patches if you upgrade with less frequency than 30 days.  
No minor upgrades | Not allowed | Allowed | Not allowed | Allowed |  You can configure the maintenance exclusion in one of the following ways:

  * **Fixed end time** : set the end time up until the end of support for the cluster's minor version and respective release channel. For clusters enrolled in the Rapid, Regular, or Stable channels, this is the [end of standard support](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule), and for the Extended channel, the [end of extended support](https://docs.cloud.google.com/kubernetes-engine/versioning#end-of-extended-support).
  * **Track the end of support** : configure the end time to track the end of support for your cluster's minor version. If you don't manually upgrade the cluster to the next minor version before the end of support, GKE performs the required [automatic upgrades at the end of support](https://docs.cloud.google.com/kubernetes-engine/versioning#auto-upgrades-end-of-support) and then reactivates the maintenance exclusion with the end time tracking the new minor version's end of support. For more information, see [How a maintenance exclusion tracks the end of support](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#how-exclusion-tracks-eos).

We recommend limiting the length of maintenance exclusions to less than six months. Long maintenance exclusions postpone minor version upgrades and can result in GKE needing to perform multiple minor version upgrades in a row to ensure that your cluster continues to run a supported version.  
No minor or node upgrades | Not allowed | Allowed | Not allowed | Not allowed  
  
### How to configure a maintenance exclusion

You can create a cluster with a cluster maintenance exclusion with the Google Cloud console, or configure a cluster maintenance exclusion for an existing cluster with the Google Cloud console or the gcloud CLI. With the gcloud CLI, you can optionally configure the end time of a cluster maintenance exclusion to track the end of support date of your cluster's minor version.

You can create a node pool maintenance exclusion with the gcloud CLI.

**Caution:** If you use maintenance exclusions to prevent node auto-upgrades, you must manually upgrade those node pools to help ensure that your cluster adheres to the [GKE version skew policy](https://docs.cloud.google.com/kubernetes-engine/versioning#version-skew), and uses [supported GKE versions](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule#schedule-for-release-channels). GKE automatically upgrades the node pools at the end of support to maintain the supportability and reliability of your cluster.

#### Create a cluster with a cluster maintenance exclusion

You can configure a cluster maintenance exclusion when creating a new cluster by using the Google Cloud console. This task cannot be performed in the gcloud CLI.

To create a new cluster with a cluster maintenance exclusion:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. Click add_box **Create** , and then in the Standard or Autopilot section, click **Configure**.

  3. Configure your cluster basics, such as the cluster name and location.

  4. In the navigation pane, click **Advanced settings** , and then do one of the following:

     * **Autopilot** : Expand **Automation**. Click _add_ **Add maintenance exclusion** , and select the **Exclusion type** , a **Start time** , and an **End time**.
     * **Standard** : In the **Maintenance policy** row, click _edit_ **Edit configuration**. Click _add_ **Add maintenance exclusion** , select the **Exclusion type** , a **Start time** , and an **End time** , and then click **Save**.
  5. Click **Create**.




You can see an example maintenance exclusion for Black Friday.

#### Configure a cluster maintenance exclusion for an existing cluster

You can configure a cluster maintenance exclusion on an existing cluster by using the Google Cloud console or the gcloud CLI. With the gcloud CLI, you can optionally configure the end time of a maintenance exclusion to track the end of support date of your cluster's minor version.

###  gcloud 

  * **Fixed end time** : configure a maintenance exclusion for an existing cluster with a fixed end time:
        
        gcloud container clusters update CLUSTER_NAME \
            --add-maintenance-exclusion-name EXCLUSION_NAME \
            [--add-maintenance-exclusion-start START_DATE_TIME \]
            --add-maintenance-exclusion-end END_DATE_TIME \
            --add-maintenance-exclusion-scope SCOPE
        

Replace the following:

    * `CLUSTER_NAME`: the name of your cluster.
    * `EXCLUSION_NAME`: the name of the maintenance exclusion.
    * `START_DATE_TIME`: optionally, set the start date and time for the exclusion for a time in the future. If you omit this flag, the maintenance exclusion starts immediately.
    * `END_DATE_TIME`: the end date and time for the exclusion.
    * `SCOPE`: the scope of upgrade to exclude, which can be one of the following values: `no_upgrades`, `no_minor_upgrades`, or `no_minor_or_node_upgrades`.

To view supported date and time formats, run [`gcloud topic datetimes`](https://docs.cloud.google.com/sdk/gcloud/reference/topic/datetimes).

  * **Ends at end of support** : configure a maintenance exclusion which tracks the end of support date of your cluster's minor version:
        
        gcloud container clusters update CLUSTER_NAME \
            --add-maintenance-exclusion-name EXCLUSION_NAME \
            [--add-maintenance-exclusion-start START_DATE_TIME \]
            --add-maintenance-exclusion-until-end-of-support \
            --add-maintenance-exclusion-scope SCOPE
        




###  Console 

To configure a maintenance exclusion for an existing cluster:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Automation** , next to the **Maintenance exclusions** field, click _edit_ **Edit maintenance exclusions**.

  4. Under **Maintenance exclusions** , click _add_ **Add Maintenance Exclusion**.

  5. Select the **Scope** , a **Start time** , and an **End time**.

  6. Click **Save Changes**.




#### Create a node pool with a node pool maintenance exclusion

Create a node pool with a node pool maintenance exclusion by using the gcloud CLI:
    
    
    gcloud container node-pools create POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --add-maintenance-exclusion-until-end-of-support
    

Replace the following:

  * `POOL_NAME`: the name of the new node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



For more information about configuring a node pool with this command, see the [`gcloud container node-pools create`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/create) reference.

#### Add a node pool maintenance exclusion for an existing node pool

Configure a node pool maintenance exclusion for an existing node pool by using the gcloud CLI:
    
    
    gcloud container node-pools update POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --add-maintenance-exclusion-until-end-of-support
    

Replace the following:

  * `POOL_NAME`: the name of the existing node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



For more information about configuring a node pool with this command, see the [`gcloud container node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update) reference.

### Remove a maintenance exclusion

You can remove cluster maintenance exclusions by using the Google Cloud console or the gcloud CLI. To remove a node pool maintenance exclusion, use the gcloud CLI.

#### Remove a cluster maintenance exclusion

### gcloud

To remove an existing cluster maintenance exclusion, run the following command:
    
    
    gcloud container clusters update CLUSTER_NAME \
        --remove-maintenance-exclusion EXCLUSION_NAME
    

Replace the following:

  * `CLUSTER_NAME`: the name of the existing cluster.
  * `EXCLUSION_NAME`: the name of the maintenance exclusion to remove.



### Console

To remove a maintenance exclusion from an existing cluster:

  1. Go to the **Google Kubernetes Engine** page in the Google Cloud console.

[Go to Google Kubernetes Engine](https://console.cloud.google.com/kubernetes/list)

  2. In the cluster list, click the name of the cluster you want to modify.

  3. Under **Automation** , next to the **Maintenance exclusions** field, click _edit_ **Edit maintenance exclusions**.

  4. Under **Maintenance exclusions** , click _delete_ **Delete item** next to the **End time** field for the exclusion you want to remove.

  5. Click **Save Changes**.




To see all maintenance exclusions on a cluster, you can view the cluster's maintenance policy.

#### Remove a node pool maintenance exclusion

Remove a node pool maintenance exclusion for an existing node pool:
    
    
    gcloud container node-pools update POOL_NAME \
        --cluster CLUSTER_NAME \
        --location=CONTROL_PLANE_LOCATION \
        --remove-maintenance-exclusion-until-end-of-support
    

Replace the following:

  * `POOL_NAME`: the name of the existing node pool.
  * `CLUSTER_NAME`: the name of your cluster.
  * `CONTROL_PLANE_LOCATION`: the Compute Engine [location](https://docs.cloud.google.com/compute/docs/regions-zones#available) of the control plane of your cluster. Provide a region for regional clusters, or a zone for zonal clusters.



For more information about configuring a node pool with this command, see the [`gcloud container node-pools update`](https://docs.cloud.google.com/sdk/gcloud/reference/container/node-pools/update) reference.

### Example maintenance exclusion

The following example prevents maintenance over the four days encompassing [Black Friday](https://en.wikipedia.org/wiki/Black_Friday_\(shopping\)) through [Cyber Monday](https://en.wikipedia.org/wiki/Cyber_Monday), the highest-volume sales period of the year for many retail businesses. This example shows how to prevent a maintenance window from occurring from Black Friday 2021 (November 26, 2021) to Cyber Monday 2021 (November 29, 2021), from midnight Eastern (UTC-5) to 23:59:59 Pacific (UTC-8).
    
    
    gcloud container clusters update sample-cluster \
        --add-maintenance-exclusion-name black-friday \
        --add-maintenance-exclusion-start 2021-11-26T00:00:00-05:00 \
        --add-maintenance-exclusion-end 2021-11-29T23:59:59-08:00 \
        --add-maintenance-exclusion-scope no_upgrades
    

## View a cluster's maintenance policy

To view a cluster's maintenance policy, including whether it has a maintenance window and all of its maintenance exclusions, use the following command:
    
    
    gcloud container clusters describe CLUSTER_NAME
    

## Identify clusters without a configured maintenance window

GKE identifies clusters for which you haven't configured a maintenance window so that you can choose a recurring window in which GKE can perform cluster maintenance. We recommend that you configure a maintenance window to ensure that GKE performs automatic upgrades and [other cluster maintenance that respects maintenance policies](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/maintenance-windows-and-exclusions#examples_of_automatic_maintenance) when it's most convenient for your cluster environment.

GKE delivers this guidance with an insight and recommendation through the [Recommender service](https://docs.cloud.google.com/recommender/docs/overview). To learn more about how to manage insights and recommendations from Recommender, see [Optimize your usage of GKE with insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders).

To find clusters without a configured maintenance window, you can use one of the following ways:

  * Use the Google Cloud console.
  * Use the gcloud CLI or Recommender API, by specifying the `CLUSTER_MAINTENANCE_WINDOW_AND_EXCLUSIONS` [recommender subtype](https://docs.cloud.google.com/recommender/docs/key-concepts#recommender_subtype).



For instructions, see how to [view insights and recommendations](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/optimize-with-recommenders#view-insights-recs).

To implement this recommendation, configure a maintenance window.

## Troubleshooting

Use the following information to troubleshoot common issues about maintenance windows and exclusions.

### Maintenance window preventing node update completion

If your cluster can't finish [node updates](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/managing-clusters#plan-node-disruption), such as [node version upgrades](https://docs.cloud.google.com/kubernetes-engine/upgrades#automatic_node_upgrades), within the scheduled maintenance window, this can slow down the rate of upgrades, or delay changes to the nodes from completing. You might need to experiment with your configuration to find the optimal balance between speed and disruption for your environment. Factors that can affect the upgrade rate include:

  * Low maintenance availability (for example, short maintenance windows).
  * Large Standard node pools.
  * [Node upgrade strategy](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/node-pool-upgrade-strategies) configuration prioritizing minimal disruption versus speed.
  * Some Pod configuration choices. See [Considerations for node upgrade duration](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades#considerations-node-upgrade) for more information.



### Restricting the scope of maintenance exclusions can only apply to release channels

**Warning:** Not enrolling your cluster in a release channel (known as _No channel_ , and formerly as _Static_) is a deprecated configuration option, only allowed for existing customers, and will be removed on June 14, 2027. New customers can't create or update their cluster to use this configuration option. For any clusters not enrolled in a release channel, we recommend that you [enroll the cluster](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/release-channels#existing-cluster) before this date. After the removal date, GKE enrolls all remaining clusters in the Stable channel. For more information about this deprecation and how you can achieve the same functionality with release channels, see [Clusters not enrolled in a release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels#no_channel).

When you restrict the scope of automatic upgrades in a maintenance exclusion, the cluster must be enrolled in a [release channel](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/release-channels), otherwise you might encounter the following errors:
    
    
    ERROR: (gcloud.container.clusters.update) INVALID_ARGUMENT: Cannot update to
    STATIC channel since following maintenancePolicy.maintenanceExclusions can only
    apply to release channels. Please remove those maintenance exclusions.
    
    
    
    ERROR: (gcloud.container.clusters.update) ResponseError: code=400,
    message=MaintenancePolicy.maintenanceExclusions["no"] could not apply to cluster
    in STATIC channel, only no_upgrades exclusions are allowed in STATIC channel.
    

### Maintenance exclusions exceeds limit

You can only specify a maximum of 3 maintenance exclusions that exclude all upgrades (that is, a scope of "no upgrades"), otherwise you receive the following error:
    
    
    ERROR: (gcloud.container.clusters.update) ResponseError: code=400,
    message=Number of active maintenance exclusions exceeds limit (3).
    

You can only specify a maximum of 20 maintenance exclusions in total, otherwise you receive the following error:
    
    
    ERROR: (gcloud.container.clusters.update) ResponseError: code=400,
    message=Number of total maintenance exclusions exceeds limit (20).
    

## What's next

  * Learn more about [cluster and node upgrades](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-upgrades).
  * Learn how to [enable node auto-upgrade](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/node-auto-upgrades).
  * Learn about [cluster notifications](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/cluster-notifications).
  * Learn more about the [GKE release schedule](https://docs.cloud.google.com/kubernetes-engine/docs/release-schedule).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
