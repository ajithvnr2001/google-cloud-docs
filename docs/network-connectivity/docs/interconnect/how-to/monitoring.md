---
url: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring/
title: Monitor connections \u00a0|\u00a0 Cloud Interconnect \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:16:27.134892+00:00
---

# Monitor connections  |  Cloud Interconnect  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/interconnect/how-to/monitoring/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud Interconnect ](https://docs.cloud.google.com/network-connectivity/docs/interconnect)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview)



Send feedback 

#  Monitor connections Stay organized with collections  Save and categorize content based on your preferences. 

To help you monitor connections, Cloud Interconnect reports metrics to [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs). Monitoring these metrics can help you troubleshoot issues with the following:

  * Physical circuits (Cloud Interconnect connections)
  * VLAN attachments
  * Wires in cross-site networks



For Dedicated Interconnect, Cloud Interconnect reports measurements for the connections and VLAN attachments. For Partner Interconnect, Cloud Interconnect reports measurements for VLAN attachments only.

Google starts reporting Cloud Interconnect connection metrics after Google allocates your ports, even before your connection is ready to use. That way, you can monitor the circuits while they're being set up and tested.

For VLAN attachments and wires, Google starts reporting metrics right after you create the attachment or wire group. Google reports the number of packets and bytes sent and received.

Data is reported in one-minute intervals to Monitoring and is retained in Monitoring for 6 weeks.

You can view general information about your Cloud Interconnect connections and VLAN attachments by using the **Observability** tab:

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=observability)

The following sections describe how to monitor specific Cloud Interconnect connections or VLAN attachments.

## Metrics and resource types

For more information about Cloud Interconnect metrics, see the following links from the Cloud Monitoring documentation:

  * [View a list of Cloud Interconnect metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-interconnect)
  * View details for the following monitored resource types: 
    * [`interconnect`](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect)
    * [`interconnect_attachment`](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect_attachment)
    * [`wire_endpoint`](https://docs.cloud.google.com/monitoring/api/resources#tag_wire_endpoint)



You can view metrics for the `transport` resource for partner Cross-Cloud Interconnect for AWS in Cloud Monitoring ([Preview](https://cloud.google.com/products#product-launch-stages)).

## View metrics in the Google Cloud console

On the **Cloud Interconnect** page in the Google Cloud console, you can view the activity for the following, depending on your connection type:

  * Cloud Interconnect connections, except Partner Interconnect
  * VLAN attachments
  * Cross-site networks




###  Console 

To view the monitoring information for a Cloud Interconnect connection, follow these steps:

  1. In the Google Cloud console, go to the Cloud Interconnect **Physical connections** tab.

[Go to Physical connections](https://console.cloud.google.com/hybrid/interconnects/list?tab=interconnects)

  2. Select the connection to view.

  3. On the **Interconnect connection details** page, select the **Monitoring** tab.

Depending on your connection type, the Google Cloud console shows some or all of the following activity for the selected timeframe (by default, the Google Cloud console shows the past hour's activity):

     * Utilization rate (bytes received and sent) compared to its overall capacity.
     * Received bytes by VLAN attachment.
     * Sent bytes by VLAN attachment.
     * Number of outbound drops and number of inbound and outbound errors.



To view the monitoring information for a VLAN attachment, follow these steps:

  1. In the Google Cloud console, go to the Cloud Interconnect **VLAN attachments** tab.

[Go to VLAN attachments](https://console.cloud.google.com/hybrid/interconnects/list)

  2. Select the VLAN attachment to view.

  3. On the **VLAN attachment details** page, select the **Monitoring** tab.

For each VLAN attachment, the Google Cloud console shows the bytes received and sent compared to its total capacity for the selected timeframe (by default, the Google Cloud console shows the past hour's activity).




To view the monitoring information for a cross-site network, follow these steps:

  1. In the Google Cloud console, go to the **Interconnect** page.

[Go to Interconnect](https://console.cloud.google.com/hybrid/interconnects/list?tab=cross-site)

  2. On the **Cross-site networks** tab, select the cross-site network to view.

  3. On the **Cross-site network details** page, select the **Monitoring** tab.

The Google Cloud console shows the following information:

     * The bytes received and sent by each wire group endpoint and wire endpoint
     * The operational status of each wire endpoint
     * The latency of each wire, measured by out of band probes



## View metrics in Cloud Monitoring

###  Console 

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Interconnect` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select [interconnect](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect).
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. For a list of metrics, see [interconnect metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-interconnect). 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To view the monitoring information for a `transport` resource for partner Cross-Cloud Interconnect for AWS connection, follow these steps:

  1. In the Google Cloud console, go to the **Metrics explorer** tab.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. Under **Select a metric** , click **Transport**.

  3. Choose the metric that you want to view.




You can view the following traffic metrics for a `transport` resource:

  * Transport sent packets
  * Transport received packets
  * Transport sent bytes
  * Transport received bytes
  * Transport dropped sent packets
  * Transport dropped received packets



## Define alerting policies

###  Console 

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Interconnect` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select [**Interconnect**](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect).
     3. For the **Metric category** , select **Network**.
     4. For the **Metric** , select a metric from the [**list of interconnect metrics**](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-interconnect).
     5. Select **Apply**.
  5. Click **Next**.
  6. The settings in the **Configure alert trigger** page determine when the alert is triggered. Select a condition type and, if necessary, specify a threshold. For more information, see [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). 
  7. Click **Next**.
  8. Optional: To add notifications to your alerting policy, click **Notification channels**. In the dialog, select one or more notification channels from the menu, and then click **OK**.
  9. Optional: Update the **Alert autoclose duration**. This field determines when Monitoring closes alerts in the absence of metric data.
  10. Optional: Click **Documentation** , and then add any information that you want included in a notification message.
  11. Click **Alert name** and enter a name for the alerting policy.
  12. Click **Create Policy**.

For more information, see [Alerting overview](https://docs.cloud.google.com/monitoring/alerts). 

## Create custom Monitoring dashboards

You can create custom Monitoring dashboards over Cloud Interconnect metrics by adding [custom charts](https://docs.cloud.google.com/monitoring/charts).

###  Console 

To create custom Monitoring dashboards, follow these steps:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Dashboards** , and then click **Create dashboard**.

  3. Name the dashboard, and then click **Add chart**.

  4. Specify a name for the chart.

  5. Select the metrics and filters to use. For a list of Cloud Interconnect resource types and metrics that you can monitor, see [Monitored resource types](https://docs.cloud.google.com/monitoring/api/resources#tag_interconnect) or [Metrics list](https://docs.cloud.google.com/monitoring/api/metrics_gcp_i_o#gcp-interconnect).

  6. Click **Save**.




## View metrics in Network Topology

You can use Network Topology to audit your networking configuration and troubleshoot networking issues.

Network Topology overlays throughput values on each connection so that you can quickly see the amount of traffic between entities. For example, you can see the traffic traversing the VLAN attachment that connects Google Cloud to an on-premises network.

**Note:** Network Topology isn't available for cross-site networks.

For information about the supported metrics for each connection, see the [Metrics reference](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/reference/metrics-reference).

Metric values are based on the final five minutes of the selected hour. You can also view historical date for six weeks by clicking on any of the edges.

For more information, see [Data collection and freshness](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#data).

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the entities selection pane, select a metric from the **Edge metric** drop-down menu.

  3. Navigate to a specific entity hierarchy to view traffic that is related to that entity.

For example, if you want to view traffic bandwidth traversing the VLAN attachment between Google Cloud and the on-premises network, expand the entities until you see that connection.

  4. Click the entity to highlight all of its traffic paths.

Network Topology displays metric values for each connection that supports the selected metric.




## What's next

  * To query and view metrics for your Cloud Interconnect resources, see the [Cloud Monitoring API](https://docs.cloud.google.com/monitoring/api/v3).

  * To view records of samples of packets sent through VLAN attachments, see [VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs).

  * To learn more about Cloud Interconnect options, see the [Cloud Interconnect overview](https://docs.cloud.google.com/network-connectivity/docs/interconnect/concepts/overview).

  * To help you solve common issues that you might encounter when using Cloud Interconnect, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/interconnect/support/troubleshooting).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
