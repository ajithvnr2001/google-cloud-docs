---
url: https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state/
title: Monitor replica states and replication status for regional disks \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:48:47.995767+00:00
---

# Monitor replica states and replication status for regional disks  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/disks/monitor-regional-persistent-disk-replica-state/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ Guides ](https://docs.cloud.google.com/compute/docs/overview)



Send feedback 

#  Monitor replica states and replication status for regional disks Stay organized with collections  Save and categorize content based on your preferences. 

Compute Engine maintains copies of each [regional](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk) disk in two Google Cloud zones. Each copy is called a zonal replica. When you write data to your disk, Compute Engine synchronously replicates that data to both replicas to ensure high availability (HA). At any given time, the **disk replication status** of the regional disk tells you about the ability of a disk to synchronously write to both replicas. The disk's replication status is determined by the **replica states** of the disk's zonal replicas. The replica state for a zone is tells you the state of an individual zonal replica in comparison to the latest data on the disk. If a zonal replica contains the latest disk data, then that replica is considered to be _synced_ with the latest disk data. If both zonal replicas are synced, then your Regional Persistent Disk or Hyperdisk Balanced High Availability disk is considered to be _fully replicated_.

This document explains how you can monitor the replica states of your regional disks and their disk replication status over a period of time. You can use this document to do the following:

  1. Check the current and historical replica states of your regional disks. 
     * To only verify whether the zonal replicas for a specific regional disk are synced or not, monitor using the Google Cloud console.
     * To check the exact zonal replica state for replicas of all the disks in a project, monitor using the Cloud Monitoring dashboard.
  2. Use the replica state information from a specific point in time to determine if your disk was fully replicated.



To learn more about replica state and disk replication status, see [About synchronous disk replication](https://docs.cloud.google.com/compute/docs/disks/about-regional-persistent-disk#zonal_replication).

### Required roles

To get the permissions that you need to view replication states using Cloud Monitoring, ask your administrator to grant you the following IAM roles: 

  * To view regional disk metrics (one of the following): 
    * [](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer)[Monitoring viewer](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) (`roles/monitoring.viewer`) on the project
    * [](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor)[Monitoring editor](https://docs.cloud.google.com/monitoring/access-control#predefined_roles) (`roles/monitoring.editor`) on the project



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Monitor using the Google Cloud console

This section explains how you can monitor the replica states and disk replication status of a Hyperdisk Balanced High Availability or Regional Persistent Disk volume using the Google Cloud console.

### Check if zonal replicas are synced for a single disk

You can use the Google Cloud console to check whether the zonal replicas of a regional disk are synced with the latest disk data.

To see detailed information about the exact zonal replica states for all regional disks in a project, check the zonal replica states using the Cloud Monitoring dashboard.

###  Console 

To monitor the zonal replica states for your regional disks, do the following:

  1. In the Google Cloud console, go to the **Disks** page.

[Go to Disks](https://console.cloud.google.com/compute/disks)

  2. On the **Disks** page, in the **Name** column, select the disk for which you want to check the replica states.

The **Manage disk** page opens for the selected disk and displays the **Details** tab for that disk.

  3. Click the **Observability** tab.

The **Manage disk** page displays the monitoring information for the disk.

  4. To see the historical replica state information for your disk, on the **Observability** tab, navigate to the **Regional Persistent Disk Replication State** graph.

The graph displays the replica state values for your zonal replicas over the preceding hour in the form of two separate graph lines.

The replica state value can be one of the following:

     * `0`: The replica is not in sync with the latest disk data.
     * `1`. The replica is synced with the latest disk data.
  5. To check the replica state value for your zonal replicas at a specific point in time, do the following:

     * Hold the pointer on the graph for the time value at which you want to check the replica state.
     * To see the replica state values for your zonal replicas, navigate to the bottom of the graph.
     * Optional: To see the name and replica state value denoted by a graph line, hold the pointer over the graph line for any specific time value. The graph highlights the name and time-specific state of that replica inside a tooltip.
  6. Optional: To modify the time period over which you want to see the replica state data, select a time period at the top of the **Observability** tab. The following options are available:

     * **1 hour** : the preceding hour. This is the default value.
     * **6 hours** : the preceding 6 hours.
     * **1 day** : the preceding day.
     * **1 week** : the preceding week.
     * **1 month** : the preceding month.
     * **6 weeks** : the preceding 6 weeks.
     * **Custom** : a specific time period of your choice. To specify a custom monitoring time period, click **Custom** and then do the following:

       * In the **Start date and time** field, specify the beginning of your monitoring time period. You must specify a time in the past.
       * In the **End date and time** field, specify the end of your monitoring time period. You must specify a time in the past.
       * To save your custom monitoring time period, click **Apply**.



### Determine if the disk is fully replicated

After you determine whether or not your zonal replicas are synced with the latest disk data, you can use that information to determine whether or not your disk is fully replicated.

At any given time, the disk was _fully replicated_ if the replica state value for both zonal replicas was `1`. If that was not the case, check for the exact replica states at that time to know whether your disk was _degraded_ or _catching up_. For more information, see Monitor using Cloud Monitoring metrics.

## Monitor using Cloud Monitoring metrics

You can check detailed information about the exact zonal replica states for all your regional disks by using the `Regional disk replica state` metric in Cloud Monitoring.

### About the `Regional disk replica state` metric

You can see the current and historical disk replica states of your zonal replicas on the Cloud Monitoring dashboard. Compute Engine captures the replica states of your disks every minute and reports it using the `Regional disk replica state` metric. However, if there is a zonal outage that impacts the compute instance to which a zonal replica is attached, you won't see any `Regional disk replica state` metric data for either zonal replica.

The following are the possible values of the `Regional disk replica state` metric. Your zonal replicas are always in one of these disk replica states.

  * `Synced`: The replica is available, synchronously receives all the writes performed to the disk, and is up to date with all the data on the disk.
  * `CatchingUp`: The replica is available but is still catching up with the data on the disk from the other replica.
  * `OutOfSync`: The replica is temporarily unavailable and out of sync with the data on the disk.



For information about the metric definition, see the [Compute Engine Monitoring metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_c#gcp-compute) section.

**Note:** You can use the `Regional disk replica state` metric to track the replica state data only for attached Hyperdisk Balanced High Availability or Regional Persistent Disk volumes.

You can use the `Regional disk replica state` metric data to do the following:

  * Determine the replication status of your regional disk.
  * Review the replica state history of your regional disk to understand whether your failover architecture works as intended and take necessary action in case the state of your regional disk changes.
  * Create alerts based on the `Regional disk replica state` metric data, detect any changes in your replica states, and take the necessary actions. For more information about how to create metric-based alerts, see [How to add an alerting policy](https://docs.cloud.google.com/monitoring/alerts#types-of-policies).



### Check the `Regional disk replica state` metric data

To see the status of the zonal replicas of an attached regional disk, build a query and create a temporary chart for the `Regional disk replica state` metric. You can do this on Metrics Explorer by using the menu-driven interface or [PromQL](https://docs.cloud.google.com/monitoring/promql).

###  Menu-driven interface 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

The **Metrics explorer** page opens and displays the **Queries** tab.

  2. To see the replica state data for each zonal replica in a project, select the time series data for the `Regional disk replica state` metric and then remove the aggregation filter by doing the following in the toolbar of the query pane:

     1. In the **Metric** menu, click **Select a metric** and then select **Disk > Disk > Regional disk replica state**.

     2. Click **Apply**.

     3. In the **Aggregation** menu, select **Unaggregated by None**.

A chart appears and displays the metric data from the preceding hour for each replica as a time series. You see the metric data only for zonal replicas of attached disks.

For more information about selecting time series for a metric, see [Select metrics when using Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-selector).

  3. To view chart and table views simultaneously, at the top of the chart, click **Both**.

  4. To view data for all available regional disk properties, at the top of the table view, click view_column **Column display options...** , select all the columns and then click **Ok**.

The dashboard displays the following fields for every row in the table, along with their current values:

     * `disk_id`: ID of the disk
     * `zone`: The region where the regional disk was created.
     * `replica_zone`: Replica zone
     * `state`: Replica state
     * `storage_type`: Storage type of the disk
     * `value`: Value for the replica state

To view this data on the corresponding time series in the chart view, hold the pointer on the chart at the current time. The chart displays these values inside a tooltip.

**Note:** The chart view doesn't display the names of the fields.
  5. To check the historical replica states at a specific point in time, do the following:

     1. Hold the pointer over the chart at a specific time value of your choice. The dashboard displays the metric data for all replica states of all the zonal replicas in your project at that specific point in time.

In the chart view, this information appears inside a tooltip.

In the table view, this information appears as individual rows.

     2. Note the replica states and their corresponding values. At any given time, if a particular state has a value of `1`, then the replica was in that state.

In the chart view, check the replica states and values inside the tooltip for the disk IDs and replica zones that you want.

In the table view, check the **state** and **value** columns for the specific disk IDs and replica zones that you want.

To learn more about what the replica states and their values mean, see Understand the `Regional disk replica state` metric data.

  6. Optional: To view the replica state information for a specific label, in the **Filter** menu, select the label for which you want to view the data and then complete the dialogue. You can add multiple filters.

The dashboard displays the metric data only for the filtered labels. For more information about filters, see [Filter charted data](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

For example, to view the replica state data for a specific disk, do the following:

     1. In the **Filter** menu, select either the **name** label.
     2. In the **Comparator** menu, select **= (equals)**.
     3. In the **Value** menu, select the name of the disk that you want.
  7. Optional: To determine what percentage of the time a specific disk's replicas were synced, filter the data for the specific disk and state and then use the aggregation menu:

     1. In the **Filter** menu, select the **name** label.
     2. In the **Comparator** menu, select **= (equals)**.
     3. In the **Value** menu, select the name of the disk.
     4. In the **Filter** menu, select the **state** label.
     5. In the **Comparator** menu, select **= (equals)**.
     6. In the **Value** menu, select **Synced**.
     7. In the **Aggregation** menu, select **Mean by replica_zone**.
     8. Select the time period for which you want to see the data.

The dashboard displays the data about the average `synced` status for your disk's replicas over the specified time period. Multiple this data by 100 to determine the percentage of the time for which the replicas were synced. If the value for the average value shows as `1` for that time period, then the replica was always up to date with the latest data. An average value that is less than `1` indicates that the replica was not synced at some point of time during the specified time period.

For more information about grouping and alignment, see [Choose how to display charted data](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display).

  8. Optional: To modify the time period over which you want to monitor the metric data, at the top of the dashboard, click **Last 1 hour** select the time period that you want.

You can select a relative time period to the current time, or specify start and end times of your choice. By default, you see the metric data for the preceding hour.




###  PromQL 

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

The **Metrics explorer** page opens and displays the **Queries** tab.

  2. In the toolbar of your query pane, click the button whose name starts with **< >**.

  3. In the **Language** field, select **PromQL** as your query language. This field is in the same toolbar that lets you format your query.

  4. Optional: Disable the **Auto-run** toggle.

  5. Enter your query and then click **Run query**.

When the **Auto-run** toggle is enabled, the **Run query** button isn't displayed.

For example, to view the replica state data for a disk called `disk-1`, run the following query:
         
         avg_over_time(compute_googleapis_com:disk_regional_replica_state{monitored_resource="gce_disk",metadata_system_name="disk-1"}[${__interval}])
         

As another example, to determine what percentage of the time the replicas were synced for a disk called `disk-1`, run the following query:
         
         avg by (replica_zone)(avg_over_time(compute_googleapis_com:disk_regional_replica_state{monitored_resource="gce_disk",state="Synced",metadata_system_name="disk-1"}[${__interval}]))
         

  6. To modify the time period over which you want to monitor the metric data, at the top of the dashboard, click **Last 1 hour** select the time period and time zone that you want.

You can select a relative time period to the current time, or specify start and end times of your choice. By default, you see the metric data for the preceding hour.




### Determine the exact zonal replica states using metric data

To understand the `Regional disk replica state` metric data for a regional disk, you must check the **state** and **value** columns for the zonal replicas in your generated chart. If you don't add any filters to your query, the following things happen:

  * The **state** column displays all the possible disk replica states for a zonal replica, one of `Synced`, `CatchingUp`, and `OutOfSync`. The chart displays each of these states in the form of a time series for all zonal replicas of all regional disks in your project.
  * The **value** column indicates whether the zonal replica is in a specific disk replica state or not. This column shows a corresponding binary value (either `0` or `1`) for every value of **state** for all zonal replica of all regional disks in your project.



For any zonal replica, if the **value** column shows `1` for a specific disk replica state, then that zonal replica is in that specific state. If the **value** column shows `0` for a specific state, then that replica is not in that specific state. At any given time, a zonal replica has exactly one of the disk replica states with `1` in the **value** column. The other two disk replica states have `0` in their respective **value** columns.

For every zonal replica, the chart and table display a separate entry for each disk replica state: `Synced`, `CatchingUp`, and `OutOfSync`. The **value** column for each entry is a binary value (either `0` or `1`) that indicates whether or not the replica is in that state. At any given time, a zonal replica has exactly one replica state with its value as `1`.

### Determine the exact disk replication status

You can use the replica states of your zonal replicas to determine the replication state of your regional disks in the following way:

  * If both the zonal replicas have `1` as the value for the `Synced` state, then the disk is **fully replicated**.
  * If one of the zonal replicas has `1` as the value for the `Synced` state and the other zonal replica has `1` as the value for the `CatchingUp` state, then the disk is **catching up**.
  * If one of the zonal replicas has `1` as the value for the `Synced` state and the other zonal replica has `1` as the value for the `OutOfSync` state, then the disk is **degraded**.



For example, consider a disk named `my-disk1` that has replicas in `us-central1-a` and `us-central1-b`. The following scenarios shows the values of the **state** and **value** columns for the zonal replicas for each possible replication state of `my-disk1`:

###  **Fully replicated**

In this scenario, the replica in `us-central1-a` and the replica in `us-central1-b` are both updated with the latest data on the disk. The chart displays the following values for each disk replica state for the zonal replicas of `my-disk1`:

**replica_zone** | **state** | **value**  
---|---|---  
`us-central1-a` | `Synced` | **`1`**  
`us-central1-a` | `CatchingUp` | `0`  
`us-central1-a` | `OutOfSync` | `0`  
`us-central1-b` | `Synced` | **`1`**  
`us-central1-b` | `CatchingUp` | `0`  
`us-central1-b` | `OutOfSync` | `0`  
  
###  **Catching up**

In this scenario, the replica in `us-central1-a` is updated with the data on the disk and the replica in `us-central1-b` is catching up with the data on the disk. The chart displays the following values for each disk replica state for the zonal replicas of `my-disk1`:

**replica_zone** | **state** | **value**  
---|---|---  
`us-central1-a` | `Synced` | **`1`**  
`us-central1-a` | `CatchingUp` | `0`  
`us-central1-a` | `OutOfSync` | `0`  
`us-central1-b` | `Synced` | `0`  
`us-central1-b` | `CatchingUp` | **`1`**  
`us-central1-b` | `OutOfSync` | `0`  
  
###  **Degraded**

In this scenario, the replica in `us-central1-a` is updated with the data on the disk and the replica in `us-central1-b` is out of sync. The chart displays the following values for each disk replica state for the zonal replicas of `my-disk1`:

**replica_zone** | **state** | **value**  
---|---|---  
`us-central1-a` | `Synced` | **`1`**  
`us-central1-a` | `CatchingUp` | `0`  
`us-central1-a` | `OutOfSync` | `0`  
`us-central1-b` | `Synced` | `0`  
`us-central1-b` | `CatchingUp` | `0`  
`us-central1-b` | `OutOfSync` | **`1`**  
  
## What's next

  * [Create and manage regional disks](https://docs.cloud.google.com/compute/docs/disks/regional-persistent-disk).
  * Learn how to [build HA services using regional disks](https://docs.cloud.google.com/compute/docs/disks/high-availability-regional-persistent-disk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
