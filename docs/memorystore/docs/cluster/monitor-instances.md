---
url: https://docs.cloud.google.com/memorystore/docs/cluster/monitor-instances/
title: Monitor clusters \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:31:20.983381+00:00
---

# Monitor clusters  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/monitor-instances/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  Monitor clusters Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to monitor your clusters to ensure that they perform as expected.

This page also contains examples of monitoring clusters by using Memorystore for Redis Cluster and Cloud Monitoring. In addition, Memorystore for Redis Cluster is compatible with open-source Redis, so you can use existing Redis monitoring tools from Compute Engine VMs to monitor your clusters.

## Monitor clusters by using Memorystore for Redis Cluster

You can view cluster-level and node-level monitoring [metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics) for your clusters by using the System insights dashboard. This dashboard displays charts with respect to selected clusters or nodes, and provides measures of memory utilization, CPU utilization, received connections, cache hit ratio, the total number of calls, and other performance metrics. By viewing the metrics that are available for your clusters or nodes, you can detect and analyze system performance problems.

### Before you begin

Before you can use the System insights dashboard, you need Identity and Access Management (IAM) roles and permissions.

#### IAM roles

To view or modify the System insights dashboard, including customizing the dashboard to meet your needs, your administrator must grant you the following IAM roles for your Google Cloud project:

  * To create and edit custom dashboards: [Monitoring Dashboard Configuration Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.dashboardEditor) (`roles/monitoring.dashboardEditor`)
  * To open and view custom dashboards: [Monitoring Dashboard Configuration Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.dashboardViewer) (`roles/monitoring.dashboardViewer`)
  * To retrieve data for monitoring metrics and to filter data on the System insights dashboard: [Monitoring Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.viewer) (`roles/monitoring.viewer`)
  * To create and edit Metrics Explorer alerts: [Monitoring Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/monitoring#monitoring.editor) (`roles/monitoring.editor`)



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

These predefined roles contain the permissions required to filter data, and to create, view, and modify customizations on the System insights dashboard. For more information about the exact permissions that are required, see IAM permissions.

#### IAM permissions

You need the following permissions to filter data, and to create, view, and modify customizations on the System insights dashboard:

  * To filter data on the dashboard: `monitoring.metricDescriptors.list` and `monitoring.monitoredResourceDescriptors.list`
  * To create customizations on the dashboard: `monitoring.dashboards.create`
  * To view customizations on the dashboard: `monitoring.dashboards.get` and `monitoring.dashboards.list`
  * To modify customizations on the dashboard: `monitoring.dashboards.update`



### About charts and metrics

The System insights dashboard provides charts and metrics to show a cluster's current and historical status. Most charts and metrics are available at the cluster level. You can also view charts and metrics for a single node within a cluster.

The [metric type](https://docs.cloud.google.com/monitoring/api/v3/metric-model#metric_types) for each chart is listed. The metric type strings follow this prefix: `redis.googleapis.com/cluster`. The _metric type_ describes measurements that you can collect from a monitored resource.

#### Clusters

The following table describes the charts for clusters that appear, by default, on the System insights dashboard.

Chart name | Metric type | Description  
---|---|---  
Memory utilization | [`/memory/average_utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) [`/memory/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) | The total memory that a cluster uses. In a dual-region or multi-region cluster, this metric represents the mean of the memory utilization across the regions.  
CPU utilization | [`/cpu/average_utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) [`/cpu/maximum_utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) | The total CPU that a cluster uses. If a cluster is available in multiple regions, then this metric represents the mean of the CPU utilization across the regions.  
Connected clients | [`/clients/total_connected_clients`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) | The current number of client connections to the cluster.  
Cache hit ratio | [`/stats/total_keyspace_hits_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) [`/stats/total_keyspace_misses_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) | The ratio of the total number of successful lookups of keys to the sum of the total number of failed lookups of keys and the total number of successful lookups of keys across the cluster ((hits/hits + misses)).  
Calls | [`/commandstats/total_calls_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) | The total number of calls that are associated with a command in one minute.  
Execution time - Primary - Commands | [`/commandstats/total_calls_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) [`/commandstats/total_usec_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) | The ratio of the total time that Memorystore for Redis Cluster takes to run read and write commands on the primary nodes of a cluster divided by the total number of commands. You can use the menu in this chart to filter for read commands only, write commands only, or both read and write commands.  
Execution time - Replica - Commands | [`/commandstats/total_calls_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) [`/commandstats/total_usec_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#cluster-level_metrics) | The ratio of the total time that Memorystore for Redis Cluster takes to run read and write commands on the replica nodes of a cluster divided by the total number of commands. You can use the menu in this chart to filter for read commands only, write commands only, or both read and write commands.  
  
#### Nodes

The following table describes the charts for nodes that appear, by default, on the System insights dashboard.

Chart name | Metric type | Description  
---|---|---  
Memory utilization | [`/node/memory/utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) | The amount of memory that a node of the cluster uses.  
CPU utilization | [`/node/cpu/utilization`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) | The amount of CPU that a node of the cluster uses.  
Connected clients | [`/node/clients/connected_clients`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) | The number of clients that are connected to a node of the cluster.  
Cache hit ratio | [`/node/stats/keyspace_hits_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) [`/node/stats/keyspace_misses_count`](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics) | The ratio of the total number of successful lookups of keys to the sum of the total number of failed lookups of keys and the total number of successful lookups of keys across a node in the cluster ((hits/hits + misses)).  
  
### About the **Key performance across nodes** pane

You can use this pane to see the following information about the primary and replica nodes of a cluster:

  * **CPU utilization[(`/node/cpu/utilization`)](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics)**: the average amount of CPU that each node of the cluster uses for the time range that you specify on the System insights dashboard.
  * **Memory utilization[(`/node/memory/utilization`)](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics)**: the average amount of memory that each cluster node uses for the specified time range.
  * **Node uptime[(`/node/server/uptime`)](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics#node-level_metrics)**: the amount of time that each cluster node is up and running for the specified time range. Memorystore for Redis Cluster aligns this time with the closest previous known time.



For more information about using Memorystore for Redis Cluster optimally concerning CPU utilization, memory utilization, and node uptime, see [Best practices for Memorystore for Redis Cluster](https://docs.cloud.google.com/memorystore/docs/cluster/general-best-practices).

### View cluster-level monitoring metrics

You can use the System insights dashboard to view cluster-level monitoring metrics. These metrics appear as charts and provide measures of memory utilization, CPU utilization, received connections, cache hit ratio, and the total number of calls.

To view cluster-level monitoring metrics, follow these steps:

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page. 

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster that you want to monitor.

  3. In the side navigation bar, click **System insights**.

  4. Click the **Cluster** tab. Charts for the cluster appear on the dashboard. For more information about using these charts, see Use charts and metrics.

  5. **Optional**. You can customize the dashboard to meet your needs.




### View node-level monitoring metrics

You can use the System insights dashboard to view node-level monitoring metrics. These metrics appear as charts and provide measures of memory utilization, CPU utilization, received connections, cache hit ratio, and the total number of calls.

To view node-level monitoring metrics, follow these steps:

  1. In the Google Cloud console, go to the **Memorystore for Redis Cluster** page. 

[Memorystore for Redis Cluster](https://console.cloud.google.com/memorystore/redis/clusters)

  2. Click the ID of the cluster that you want to monitor.

  3. In the side navigation bar, click **System insights**.

  4. Click the **Nodes** tab. On the dashboard, the **Key performance across nodes** pane and charts appear for the cluster nodes.

For more information about using these charts, see Use charts and metrics. To learn more about using the pane, see Use the **Key performance across nodes** pane.

  5. **Optional**. You can customize the dashboard to meet your needs. You can also filter the data that appears on the dashboard.




### Use charts and metrics

Each chart that appears on the System insights dashboard has a toolbar that provides you with the following standard options. Some elements are hidden unless you hold the pointer over the chart.

  * To zoom into a section of a chart, drag your pointer across the section that you want to view. This action sets a custom time range, which you can adjust or revert with the time range filter. To zoom out of the section, click **Reset zoom**.

  * To view a description of the chart and its data, click **Help** (_help_).

  * To view the filters and groupings that Memorystore for Redis Cluster applies to the chart, click **Information** (_info_).

  * To create an alert based on the chart's data, click **Create alert policy** (_add_alert_).

  * To explore the data in the chart, click **Explore data** (_query_stats_).

  * To view additional chart options, click **More chart options** (_more_vert_). A menu appears.

    * To view a chart in full-screen mode, select **View in full screen** from the menu. To exit full screen, click **Cancel**.

    * To expand the chart legend, select **Expand chart legend** from the menu. To collapse the legend, select **Collapse chart legend**.

    * To change the visual format of the chart, select **Mode** from the menu, and then select a mode. This mode determines how the chart displays data.

There are three modes that you can select: **X-Ray Mode** , **Color Mode** , and **Stats Mode**. For more information about these modes, see [Set x-ray, color, or statistics mode](https://docs.cloud.google.com/monitoring/charts/chart-view-options#chart-modes).

    * To download the chart, select **Download** from the menu, and then select a download format. You can download the chart as a PNG or CSV file.

    * To view the metric in [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer), select **View in Metrics Explorer** from the menu. In Metrics Explorer, you can view other Memorystore for Redis Cluster metrics.




### Use the **Key performance across nodes** pane

The pane has a toolbar that provides you with the following standard options. Some elements are hidden unless you hold the pointer over the pane.

  * To explore the data in the pane, click **Explore data** (_query_stats_).

  * To view the pane in full-screen mode, click **More chart options** (_more_vert_), and then select **View in full screen** from the menu. To exit full screen, click **Cancel**.

  * To fine-tune the information that appears in the pane, click the **Filter** field, select a property, and then select a value. For example, to view information about the primary node of the cluster only, click the field, select the **Role** property, and then select the **primary** value.

  * To view a description of the pane and its data, click **Help** (_help_).

  * To select which columns in the pane are visible, click **Column display options** (_view_column_).




### Customize the System insights dashboard

The **Predefined** dashboard includes a set of default metrics. You can create additional widgets to add other metrics for Memorystore for Redis Cluster or other Google Cloud products and get a unified monitoring view from within Memorystore for Redis Cluster. For example, if you're using Memorystore for Redis Cluster with Google Kubernetes Engine (GKE) Enterprise edition (GKE Enterprise), then you can customize the predefined dashboard. In addition to Memorystore for Redis Cluster metrics, you can add required GKE Enterprise metrics, such as pod-related metrics.

**Tip** : In addition to the predefined dashboard, you can create only one custom dashboard.

#### Create a custom dashboard

To create a custom dashboard and add a metric to it, follow these steps:

  1. In the **Cluster** or **Nodes** tabs of the System insights dashboard, select the **Predefined** menu, and then click **Customize dashboard**.
  2. In the **Custom view name** field, enter a name for the dashboard (for example,  
`my-custom-dashboard`).
  3. Click **Add widget**.
  4. In the **Add widget** pane, select a widget type to add a metric to the dashboard.
  5. In the **Configure widget** pane, configure the widget.

For example, in the **Add widget** pane, you can select the **Metric** or **Stacked bar** widgets, and then, in the **Configure widget** pane, you can select and configure a Memorystore for Redis Cluster metric.

  6. Click **Apply**. The Memorystore for Redis Cluster metric that you added appears on the System insights dashboard.

  7. Click **Save**.




#### Edit the custom dashboard

To edit the custom dashboard that you created, follow these steps:

  1. In the **Cluster** or **Nodes** tabs of the System insights dashboard, click **Edit dashboard** (_edit_).
  2. To reposition a widget that represents a metric, click the widget header and drag it to a new location.
  3. To edit a widget, do the following: 
     1. Click **Edit widget** (_edit_).
     2. In the **Configure widget** pane, edit the widget.
     3. Click **Apply**.
  4. To clone a widget, do the following: 
     1. Click **More chart options** (_more_vert_).
     2. From the menu, select **Clone widget**.
     3. In the **Clone** dialog, enter a name for the widget that you want to clone, select the dashboard where you want the widget to appear (for example, the current System insights dashboard), and click **Clone**.
  5. To delete a widget, do the following: 
     1. Click **More chart options** (_more_vert_).
     2. From the menu, select **Delete widget**.
     3. In the **Delete widget** dialog, click **Delete**.
  6. Click **Save**.



#### Delete the custom dashboard

To delete the custom dashboard, follow these steps:

  1. In the **Cluster** or **Nodes** tabs of the System insights dashboard, click **Delete customized dashboard** (_delete_).
  2. In the **Are you sure you want to delete?** dialog, click **Delete dashboard**.



### Filter the System insights dashboard

By default, the System insights dashboard displays data for all primary and replica nodes of the cluster that you want to monitor. To fine-tune the data that appears on the charts of this dashboard, you can use the following filters:

  * **Node ID** : specify _which_ primary and replica nodes contain data that you want to appear
  * **Node role** : specify whether the data that appears is associated with primary nodes only, replica nodes only, or both primary and replica nodes



#### Filter by the node ID

To filter the System insights dashboard by the node ID, follow these steps:

  1. In the **Nodes** tab of the System insights dashboard, copy the IDs of the nodes, which contain data that you want to appear. To do this, use the **Key performance across nodes** pane to copy the node IDs.

  2. Select the **Node ID** menu.

  3. In the dialog, paste the ID of a node that you copied, select the checkbox next to the node ID, and click **OK**.

  4. Repeat steps 2 and 3 for all node IDs that you copied.




#### Filter by the node role

To filter the System insights dashboard by the node role, follow these steps:

  1. In the **Nodes** tab of the System insights dashboard, select the **Node role** menu.

  2. In the dialog, do one of the following:

     1. If you want the data that appears on the System insights dashboard to be associated with primary and replica nodes, then select the **Select all** checkbox.

     2. If you want the data to be associated with primary nodes only, then select the **Primary** checkbox.

     3. If you want the data to be associated with replica nodes only, then select the **Replica** checkbox.

  3. Click **OK**.




## Monitor clusters by using Cloud Monitoring

[Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) is a monitoring service that lets you view metrics such as average connected clients for your clusters. For more details about all Memorystore for Redis Cluster metrics available from Cloud Monitoring, see the [Supported monitoring metrics](https://docs.cloud.google.com/memorystore/docs/cluster/supported-monitoring-metrics).

### Sign up for Cloud Monitoring

To access the monitoring console, click **Monitoring** in the Google Cloud console navigation pane:

[Go to Google Cloud console](https://console.cloud.google.com/)

For pricing information, see [Cloud Monitoring pricing](https://cloud.google.com/stackdriver/pricing).

### View cluster memory utilization in Google Cloud Observability

To view cluster memory utilization information, use Metrics Explorer:

  1. Go to the Google Cloud console, login and navigate to the project with your clusters:

[Go to Google Cloud console](https://console.cloud.google.com/)

  2. Select **Monitoring** from the left navigation menu.

  3. In **Monitoring** , if the navigation pane isn't expanded, click **Expand** _last_page_. This button is located on the lower left of the console.

  4. If **Metrics Explorer** is shown in the navigation pane, click **Metrics Explorer**. Otherwise, select **Resources** and then select **Metrics Explorer**.

  5. Select _Cloud Memorystore Redis Cluster_ as the resource type and _Redis cluster average memory utilization_ as the metric.




## Set a Monitoring alert for memory usage

You can set an alert in Monitoring to notify you if the _average memory utilization_ metric exceeds a threshold that you set.

To create an alert for the Used Memory metric:

  1. In the Google Cloud console, select **Monitoring** , or use the following button:

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Alerting > Create a Policy**.

  3. Add a condition for Used Memory threshold:

     1. Use the **Select a metric** dropdown to select the _Redis cluster average memory utilization_ metric for the _Cloud Memorystore Redis Cluster_ resource.
     2. Click the **Next** button.
  4. Configure the alert:

     1. In the **Configure trigger** section, choose **Any time the series violates**.
     2. Set **Threshold position** to **Above threshold**.
     3. Set **Threshold** to the memory usage percentage you want to be notified at.
     4. Click the **Next** button.
  5. In the **Notifications and name** section, select your desired notification channel.

     1. Add a name for your alert policy like "Redis Cluster memory utilization alert"
  6. Click **Create Policy**.




You are now notified anytime the threshold is violated.

You can access this alerting policy from the **Alerting** tab in the Monitoring UI.

## View Memorystore for Redis Cluster logs

Memorystore for Redis Cluster produces logs that Cloud Logging captures.

### View audit logs

  1. Go to the **Logs Explorer** page in the Google Cloud console.

[Logs Explorer](https://console.cloud.google.com/logs)

  2. To view the audit logs, select **Audited Resource > Cloud Redis > CloudRedisCluster** from the resources drop-down.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
