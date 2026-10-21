---
url: https://docs.cloud.google.com/vpc/docs/multicast/monitor-metrics/
title: Monitor metrics for multicast \u00a0|\u00a0 Cloud Multicast \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T01:27:44.140532+00:00
---

# Monitor metrics for multicast  |  Cloud Multicast  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/vpc/docs/multicast/monitor-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Virtual Private Cloud ](https://docs.cloud.google.com/vpc/docs)
  * [ Cloud Multicast ](https://docs.cloud.google.com/vpc/docs/multicast)
  * [ Guides ](https://docs.cloud.google.com/vpc/docs/multicast/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Monitor metrics for multicast

**GA with allowlist:** Access to Cloud Multicast is available to select Google Cloud customers. If you are interested, submit an [access request form](https://forms.gle/G6o6wXTBqijoEHs26). 

This page describes the metrics that are available to multicast administrators for monitoring multicast domains and groups for Cloud Multicast.

You can use these metrics to help you understand performance and actions in a multicast domain or group, such as how many multicast consumers are joining, leaving, or are in a group, as well as traffic packet counts and latency distributions within a multicast domain.

The metrics on this page are available in multicast administrator projects that contain multicast domain and group range configurations. The metrics aren't available in multicast consumer projects, such as in the Network Connectivity Center (NCC) star topology that supports multicast consumers in separate projects.

## About Cloud Monitoring metrics for Cloud Multicast

Google Cloud reports monitoring metrics for Cloud Multicast to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

Data is reported in one-minute intervals to Monitoring and is retained in Monitoring for six weeks.

The following section describes the corresponding monitored resource types and the available metrics.

### Multicast metrics reference

This section describes the available metric types for Cloud Multicast that are reported to Monitoring.

  * The following metrics are reported for the [`MulticastGroup`](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/MulticastGroup) monitored resource type:

    * `/multicast/admin/group_control_messages`

    * `/multicast/admin/number_of_active_consumers`

  * The following metrics are reported for the [`MulticastDomain`](https://docs.cloud.google.com/monitoring/api/resources#tag_networkservices.googleapis.com/MulticastDomain) monitored resource type:

    * `/multicast/domain/intra_zone_sampled_packets`

    * `/multicast/domain/cross_zone_sampled_packets`

    * `/multicast/domain/intra_zone_latencies`

    * `/multicast/domain/intra_zone_latency_variance`




For detailed information about these metrics, see the [networkservices](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-networkservices) section in the Google Cloud metrics reference.

## Use Cloud Monitoring metrics

The following sections describe how to use Cloud Monitoring metrics.

In addition to the predefined dashboards in Monitoring, you can create custom dashboards, set up alerts, and query the metrics through the [Monitoring API](https://docs.cloud.google.com/monitoring/api).

### View metrics in Monitoring

###  Console 

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Multicast` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Multicast Group** or **Multicast Domain**.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



### Define alerting policies

###  Console 

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Multicast` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select **Multicast Group** or **Multicast Domain**.
     3. Select a **Metric category** and a **Metric** , and then select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

### Create custom Monitoring dashboards

###  Console 

  1. In the Google Cloud console, go to the dashboard **Dashboards** page: 

[Go to **Dashboards**](https://console.cloud.google.com/monitoring/dashboards)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. Click **Create dashboard**
  3. Optional: Update the dashboard title with a descriptive name for your dashboard.
  4. Click **Add Widget** and then select **Metric**.
  5. Expand the **Metric** menu, enter `Multicast` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Multicast Group** or **Multicast Domain**.
     2. In the **Active metric categories** menu, select **Multicast**.
     3. In the **Active metrics** menu, select the metric that you want to view.
     4. Click **Apply**.
  6. Combine time series: 
     * To display every time series, in the **Aggregation** element, ensure the first menu is set to **Unaggregated** and the second menu is set to **None**.
     * To combine time series, in the **Aggregation** element, use the first menu to select a function and the second menu to select the labels. If the second menu is set to **None** , then the chart displays one time series.

For example, to display the average value of time series after grouping by zone, set the first menu to **Mean** and the second to **zone**.

For information about combining time series, see [Choose how to display charted data](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display).

  7. For each additional widget that you want to add to your dashboard, click **Add widget** , complete the dialog, and then select **Apply**.

For more information about adding widgets, see the following pages:

     * [Add charts and tables](https://docs.cloud.google.com/monitoring/charts#add_chart).
     * [Display alerts and charts for alerting policies](https://docs.cloud.google.com/monitoring/dashboards/alerts-and-incidents).
     * [Display logs](https://docs.cloud.google.com/monitoring/charts/view-logs).
     * [Add text and groupings](https://docs.cloud.google.com/monitoring/dashboards/text-and-grouping).



## What's next

  * [Get an overview of Cloud Multicast observability](https://docs.cloud.google.com/vpc/docs/multicast/observability)
  * [View multicast group membership event logs](https://docs.cloud.google.com/vpc/docs/multicast/view-membership-logs)
  * [View flow logs for multicast](https://docs.cloud.google.com/vpc/docs/multicast/view-flow-logs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
