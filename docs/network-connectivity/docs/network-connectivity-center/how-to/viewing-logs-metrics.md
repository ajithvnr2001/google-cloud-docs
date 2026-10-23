---
url: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/viewing-logs-metrics/
title: Viewing logs and metrics \u00a0|\u00a0 Network Connectivity Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:59:51.666609+00:00
---

# Viewing logs and metrics  |  Network Connectivity Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/how-to/viewing-logs-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Network Connectivity Center ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview)



Send feedback 

#  Viewing logs and metrics Stay organized with collections  Save and categorize content based on your preferences. 

This page describes logs and metrics for Network Connectivity Center (NCC) , NCC Gateway spokes, and metrics for Router appliance. Logs and metrics help you understand data transfer, diagnose connectivity issues across interconnected VPC networks and on-premises environments, and manage secure access for hybrid workforces.

Logging for Router appliance is handled by Cloud Router; for more information, see [View logs and metrics](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

## How metrics work

The `local_resource_type` label reports the number of data transfer bytes on the Google Cloud side of the resource monitored. That is, the label reports when the resource attached to a spoke sends traffic to another Google Cloud resource.

The `local_resource_type` label can take one of the following values:

  * A Compute Engine virtual machine (VM) value called `GCE_VM`
  * An HA VPN gateway value called `VPN`
  * An Cloud Interconnect VLAN attachment called `ICA`
  * A value for traffic to all other resources called `OTHER`
  * A value for the router appliance instance called `ROUTER_APPLIANCE`



If the `local_resource_type` is `VPN`, `ICA`, or `ROUTER_APPLIANCE`, the metric reports data transfer information. For more information about data transfer, see [NCC use cases](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/use-cases#data-transfer).

## Logs

NCC hubs send logs to [Logging](https://docs.cloud.google.com/logging/docs). Because hybrid spokes always use Cloud Routers, review [the Cloud Router logs and metrics documentation](https://docs.cloud.google.com/network-connectivity/docs/router/how-to/viewing-logs-metrics).

### How to view logs

To view logs for NCC, follow these steps.

### Console

  1. In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

  2. To see all NCC logs, on the first pull-down menu, select the metric for the spoke resource attached to the spoke. For example, HA VPN.

To see logs for just one hub, on the menu, select a single hub name.

Log fields of type _boolean_ typically only appear if they have a value of `true`. If a boolean field has a value of `false`, that field is omitted from the log.

[UTF-8](https://wikipedia.org/wiki/UTF-8) encoding is enforced for log fields. Characters that are not UTF-8 characters are replaced with question marks.




### Routing logs

You can configure the sinks of [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) for NCC resource logs.

Logging stores NCC logs for only 30 days. If you want to keep your logs for a longer period, you must [route them](https://docs.cloud.google.com/logging/docs/routing/overview).

You can route NCC logs to [Pub/Sub](https://docs.cloud.google.com/pubsub) or [BigQuery](https://docs.cloud.google.com/bigquery) for analysis.

### What is logged

NCC log entries contain the following types of information that is useful for monitoring and debugging your hubs:

  * General information shown in most Google Cloud logs, such as severity, project ID, project number, and timestamp.
  * Other information that varies depending on the log entry.



## Monitoring metrics

To view metrics and create alerts related to your NCC and NCC Gateway spokes, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).

In addition to the predefined dashboards in Monitoring, you can create custom dashboards, set up alerts, and query the metrics through the [Monitoring API](https://docs.cloud.google.com/monitoring/api).

### Monitoring metrics for NCC

The following metrics for the `connectivity_hub` resource type are [reported into Monitoring](https://docs.cloud.google.com/monitoring/api/metrics).

All of the metrics in the following table measure _user payload_. They measure the bytes that were sent by the user, rather than the encapsulated traffic, which includes transport and network protocol headers. Also, depending on the type of transport, traffic might be compressed as part of transport.

Metric name | Metric name in the Monitoring API | Description  
---|---|---  
Cloud Interconnect egress bytes  | `networking.googleapis.com/interconnect_attachment/egress_bytes_count` | Indicates the number of bytes sent (user payload) from Google Cloud through the VLAN attachment to locations outside of Google Cloud—for example, to on-premises hosts or to other cloud providers. Sampled every 60 seconds. After sampling, data is not visible for up to five minutes.  
Cloud Interconnect ingress bytes  | `networking.googleapis.com/interconnect_attachment/ingress_bytes_count` | Indicates the number of bytes sent (user payload) to Google Cloud, through the VLAN attachment from locations outside of Google Cloud—for example, from on-premises hosts or from other cloud providers. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds.  
VPN tunnel egress bytes  | `networking.googleapis.com/vpn_tunnel/egress_bytes_count` | Indicates the number of bytes sent (user payload) from Google Cloud through the HA VPN tunnel to the other side of the tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds.  
VPN tunnel ingress bytes  | `networking.googleapis.com/vpn_tunnel/ingress_bytes_count` | Indicates the number of bytes sent (user payload) to Google Cloud through the HA VPN tunnel from the other side of the tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds.  
Router appliance egress bytes  | `networking.googleapis.com/router_appliance/gateway/egress_bytes_count` | Indicates the number of bytes sent (user payload) through and from the router appliance instance to locations outside of Google Cloud. For example, to on-premises hosts or to other cloud providers. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds.  
Router appliance ingress bytes  | `networking.googleapis.com/router_appliance/gateway/ingress_bytes_count` | Indicates the number of bytes sent (user payload) to the router appliance instance from locations outside of Google Cloud. For example, from on-premises hosts or from other cloud providers. Sampled every 60 seconds. After sampling, data is not visible for up to 150 seconds.  
  
### Monitoring metrics for NCC Gateway

You can access the following metrics for NCC Gateway spokes in Cloud Monitoring:

  * Packet count that is sent and received from the NCC Gateway.
  * Byte count that is sent and received from the NCC Gateway.
  * Relevant packet processing events and health of the NCC Gateway routing plane.

Metric name | Metric name in the Monitoring API | Description  
---|---|---  
NCC Gateway spoke received bytes  | `networking.googleapis.com/spoke/gateway/received_bytes_count` | Indicates the number of bytes received by NCC Gateway spokes.  
NCC Gateway spoke received packets  | `networking.googleapis.com/spoke/gateway/received_packets_count` | Indicates the number of packets received by NCC Gateway spokes.  
NCC Gateway spoke sent bytes  | `networking.googleapis.com/spoke/gateway/sent_bytes_count` | Indicates the number of bytes sent by NCC Gateway spokes.  
NCC Gateway spoke sent packets  | `networking.googleapis.com/spoke/gateway/sent_packets_count` | Indicates the number of packets sent by NCC Gateway spokes.  
  
### View metrics in Metrics Explorer

To view Monitoring metrics in Metrics Explorer, follow these steps.

###  Console 

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `networking` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select a resource.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. For a list of metrics, see NCC metrics list. 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



### Define custom dashboards

To create custom Monitoring dashboards over NCC metrics, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. Select **Dashboards** , and then select **Create Dashboard**.

  3. Click **Add Chart**.

  4. Give the chart a title.

  5. Select metrics and filters. For metrics, the resource type is **Connectivity Hub**.

  6. Click **Save**.




## What's next

  * To learn more about NCC, see the [NCC overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/overview).
  * To learn more about Router appliance, see the [Router appliance overview](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/concepts/ra-overview).
  * To find solutions for NCC and Router appliance issues, see [Troubleshoot NCC](https://docs.cloud.google.com/network-connectivity/docs/network-connectivity-center/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
