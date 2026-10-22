---
url: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics/
title: View logs and metrics \u00a0|\u00a0 Cloud VPN \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:29:23.896794+00:00
---

# View logs and metrics  |  Cloud VPN  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Connectivity ](https://docs.cloud.google.com/network-connectivity/docs)
  * [ Cloud VPN ](https://docs.cloud.google.com/network-connectivity/docs/vpn)
  * [ Guides ](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview)



Send feedback 

#  View logs and metrics Stay organized with collections  Save and categorize content based on your preferences. 

Cloud VPN gateways send logging information to Cloud Logging, and Cloud VPN tunnels send monitoring metrics to Cloud Monitoring. This page describes logs and metrics and how to view them.

To monitor VPN tunnel utilization, you can define alerts for VPN tunnel bandwidth. This monitoring method is recommended for production workloads.

## View logs

Cloud VPN gateways send certain logs to [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview). Cloud VPN log entries contain useful information for monitoring and debugging your VPN tunnels, such as the following:

  * General information shown in most Google Cloud logs, such as severity, project ID, project number, and timestamp.
  * Other information that varies depending on the log entry.



For a list of useful logs, see [Cloud VPN logs](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting#vpn-logging).

###  Console 

To view logs for Cloud VPN, follow these steps:

  * In the Google Cloud console, go to the **Logs Explorer** page.

[Go to Logs Explorer](https://console.cloud.google.com/logs)

Cloud VPN logs are indexed by the Cloud VPN gateway that created them:

    * To view all Cloud VPN logs, in the **All resources** menu, select **Cloud Cloud VPN gateway** , and then click **All gateway_id**.
    * To view logs for only one gateway, select a single gateway name from the menu.
  * Log fields of type _boolean_ typically only appear if they have a value of `true`. If a boolean field has a value of `false`, that field is omitted from the log.

  * [UTF-8](https://wikipedia.org/wiki/UTF-8) encoding is enforced for log fields. Characters that are not UTF-8 characters are replaced with question marks.




### Route logs

You can configure the routing of [logs-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics) for Cloud VPN resource logs.

Cloud Logging stores Cloud VPN logs for only 30 days. If you want to keep your logs for a longer period, you must [route them](https://docs.cloud.google.com/logging/docs/routing/overview). You can route Cloud VPN logs to Pub/Sub or BigQuery for analysis.

## View metrics

To view metrics and create alerts related to your VPN tunnels, use [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).

In addition to the predefined dashboards in Cloud Monitoring, you can create custom dashboards, set up alerts, and query the metrics by using the [Monitoring API](https://docs.cloud.google.com/monitoring/api) or the Google Cloud console.

### View Monitoring dashboards

The following sections describe the different ways that you can view Monitoring dashboards for Cloud VPN.

**Note:** To view Monitoring metrics for HA VPN gateways, use Metrics Explorer.

#### View predefined dashboards

Monitoring offers predefined dashboards for Cloud VPN. The **Observability** tab includes various metrics that help you monitor your Cloud VPN project's health and performance in a single view.

###  Console 

Perform the following steps to access the predefined dashboards:

  1. In the Google Cloud console, go to the **Cloud VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. Click the **Observability** tab.

The dashboard displays key project-level metrics, including packets sent, packets received, and dropped packets.

  3. You can filter the data by region, Cloud VPN gateway, and Cloud VPN tunnel.

**Note:** With the required Monitoring permissions, you can customize dashboard charts and set alert policies—for example, for dropped packets.



#### View metrics from within a Cloud VPN tunnel

You can view the performance and status of an individual Cloud VPN tunnel from the tunnel's details page. The **Monitoring** tab includes various metrics that help you quickly monitor the selected Cloud VPN tunnel.

###  Console 

Perform the following steps to view metrics for a specific Cloud VPN tunnel:

  1. In the Google Cloud console, go to the **Cloud VPN** page.

[Go to VPN](https://console.cloud.google.com/hybrid/vpn/list)

  2. Select the Cloud VPN tunnel you want to view.

  3. Click the **Monitoring** tab.

The dashboard displays key metrics, such as bytes and packets for that specific tunnel.

**Note:** With the required Monitoring permissions, you can customize dashboard charts and set alert policies—for example, for dropped packets.



#### View metrics in Metrics Explorer

**Note:** For overall project health or specific tunnel monitoring, use the **Observability** dashboard or the Cloud VPN tunnel **Monitoring** tab. Use Metrics Explorer for advanced or custom analysis of Cloud VPN metrics.

###  Console 

To view the metrics for a monitored resource by using the Metrics Explorer, do the following:

  1. In the Google Cloud console, go to the _leaderboard_ **Metrics explorer** page: 

[Go to **Metrics explorer**](https://console.cloud.google.com/monitoring/metrics-explorer)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. In the toolbar of the Google Cloud console, select your Google Cloud project. For [App Hub](https://docs.cloud.google.com/app-hub/docs/overview) configurations, select the App Hub host project or the app-enabled folder's management project.
  3. In the **Metric** element, expand the **Select a metric** menu, enter `Cloud VPN` in the filter bar, and then use the submenus to select a specific resource type and metric: 
     1. In the **Active resources** menu, select **Cloud VPN**. This resource type is valid for either Classic VPN gateways or HA VPN gateways.
     2. To select a metric, use the **Active metric categories** and **Active metrics** menus. For a full list of metrics, see [Cloud VPN metrics list](https://docs.cloud.google.com/network-connectivity/docs/vpn/how-to/viewing-logs-metrics#vpn-monitoring-metrics). 
     3. Click **Apply**.
  4. To add filters, which remove time series from the query results, use the [**Filter** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#filter-option).

  5. To combine time series, use the menus on the [**Aggregation** element](https://docs.cloud.google.com/monitoring/charts/metrics-selector#select_display). For example, to display the CPU utilization for your VMs, based on their zone, set the first menu to **Mean** and the second menu to **zone**.

All time series are displayed when the first menu of the **Aggregation** element is set to **Unaggregated**. The default settings for the **Aggregation** element are determined by the metric type you selected.

  6. For quota and other metrics that report one sample per day, do the following: 
     1. In the **Display** pane, set the **Widget type** to **Stacked bar chart**.
     2. Set the time period to at least one week.



### Define Monitoring alerts

###  Console 

You can create alerting policies to monitor the values of metrics and to notify you when those metrics violate a condition. 

  1. In the Google Cloud console, go to the _notifications_ **Alerting** page: 

[Go to **Alerting**](https://console.cloud.google.com/monitoring/alerting)

If you use the search bar to find this page, then select the result whose subheading is **Monitoring**.

  2. If you haven't created your notification channels and if you want to be notified, then click **Edit Notification Channels** and add your notification channels. Return to the **Alerting** page after you add your channels. 
  3. From the **Alerting** page, select **Create policy**.
  4. To select the metric, expand the **Select a metric** menu and then do the following: 
     1. To limit the menu to relevant entries, enter `Cloud VPN gateway` into the filter bar. If there are no results after you filter the menu, then disable the **Show only active resources & metrics** toggle. 
     2. For the **Resource type** , select [**Cloud VPN gateway**](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway).
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

#### Define alerts for Cloud VPN tunnel bandwidth

To create alerting policies for the bytes per second (bps) and packets per second (pps) limits described in [Network bandwidth](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/overview#network-bandwidth), use Prometheus Query Language (PromQL).

When entering your queries, follow the instructions in [Creating PromQL-based alerting policies (console)](https://docs.cloud.google.com/monitoring/promql/create-promql-alerts-console) and see the following examples.

For active/active tunnel configurations, which are the default, Google recommends setting a 50% usage threshold on your VPN tunnels. Setting 50% alerting policies on your Cloud VPN tunnel bandwidth usage helps to ensure that you have sufficient capacity in the event of tunnel failover.

  * **Query for bps** : this example query notifies you when the sum of `sent_bytes_count` and `received_bytes_count` exceeds 50% of the 3-Gbps (375 MBps) limit for a given VPN tunnel. The align rate should be scaled appropriately to capture the necessary data. It can be set to as low as one second (1s), and scaled higher if more data sampling points over a longer period of days are needed.
        
        (
         rate({"vpn.googleapis.com/network/sent_bytes_count", monitored_resource="vpn_gateway", tunnel_name="TUNNEL_NAME"}[1m]) +
         rate({"vpn.googleapis.com/network/received_bytes_count", monitored_resource="vpn_gateway", tunnel_name="TUNNEL_NAME"}[1m])
        ) > 187500000 # 187.5 MBy/s * 1000000
        

  * **Query for pps** : This example query notifies you when the sum of `sent_packets_count` and `received_packets_count` exceeds 50% of the maximum recommended packet rate of 250,000 pps for a given VPN tunnel.
        
        (
          rate({"vpn.googleapis.com/network/sent_packets_count", monitored_resource="vpn_gateway", tunnel_name="TUNNEL_NAME"}[1m]) +
          rate({"vpn.googleapis.com/network/received_packets_count", monitored_resource="vpn_gateway", tunnel_name="TUNNEL_NAME"}[1m])
        ) > 125000
        




For more information about PromQL, see [PromQL for Cloud Monitoring](https://docs.cloud.google.com/monitoring/promql).

### Define Monitoring custom dashboards

###  Console 

To create custom Monitoring dashboards over Cloud VPN metrics, follow these steps:

  1. In the Google Cloud console, go to the **Monitoring** page.

[Go to Monitoring](https://console.cloud.google.com/monitoring)

  2. In the Monitoring navigation pane, click **Dashboards** , and then click **Create dashboard**.

  3. Ensure that the **Edit** toggle is in the **on** position.

  4. Click the widget in the **Chart library** that you want to add to the dashboard. You can also drag the widget from the library to the graph area.

  5. Configure the widget by using the widget's configuration pane, which is displayed when the dashboard is editable and the widget is selected.

  6. In the dashboard toolbar, to activate the **Chart library** , click **Add chart**. Repeat the previous steps for each widget that you want to add to the dashboard.

  7. Select metrics and filters. For metrics, the resource type is **Cloud VPN gateway**.




For more information about configuring the widget, see [Add dashboard widget](https://docs.cloud.google.com/monitoring/charts).

For more information about setting up custom dashboards, see [Manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards).

### View Monitoring metrics for Cloud VPN

The following metrics for Cloud VPN are [reported into Monitoring](https://docs.cloud.google.com/monitoring/api/metrics). Metrics that are not individual events are for the time interval.

The "metric type" strings in this table must be prefixed with `vpn.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`gateway/connections` GA ** _(project)_**   
Number of connections   
`GAUGE`, `INT64`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Indicates the number of HA connections per VPN gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`configured_for_sla`: (BOOL) Whether the HA connection is fully configured for SLA.   
`gcp_service_health`: (BOOL) Whether the Google Cloud side of the HA connection is fully functional.   
`end_to_end_health`: (BOOL) Whether the HA connection is functional end-to-end.   
`network/dropped_received_packets_count` GA ** _(project)_**   
Incoming packets dropped   
`DELTA`, `INT64`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Ingress (received from peer VPN) packets dropped for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/dropped_sent_packets_count` GA ** _(project)_**   
Outgoing packets dropped   
`DELTA`, `INT64`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Egress (directed to peer VPN) packets dropped for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/received_bytes_count` GA ** _(project)_**   
Received bytes   
`DELTA`, `INT64`, `By`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Ingress (received from peer VPN) bytes for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/received_packets_count` GA ** _(project)_**   
Received packets   
`DELTA`, `INT64`, `{packets}`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Ingress (received from peer VPN) packets for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: Delivery status, for example, [successful, exceeds_mtu, throttled].   
`tunnel_name`: The name of the tunnel.   
`network/sent_bytes_count` GA ** _(project)_**   
Sent bytes   
`DELTA`, `INT64`, `By`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Egress (directed to peer VPN) bytes for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`network/sent_packets_count` GA ** _(project)_**   
Sent packets   
`DELTA`, `INT64`, `{packets}`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Egress (directed to peer VPN) packets for tunnel. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`status`: Delivery status, for example, [successful, exceeds_mtu, throttled].   
`tunnel_name`: The name of the tunnel.   
`tunnel_established` GA ** _(project)_**   
Tunnel established   
`GAUGE`, `DOUBLE`, `1`   
**[vpn_gateway](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_gateway)** |  _Indicates successful tunnel establishment if > 0\. Sampled every 60 seconds. After sampling, data is not visible for up to 180 seconds._   
`tunnel_name`: The name of the tunnel.   
`gateway_name`: The name of the gateway managing the tunnel.   
`vpn_tunnel/gateway_ip_version` GA ** _(project)_**   
Gateway IP version   
`GAUGE`, `BOOL`, ``   
**[vpn_tunnel](https://docs.cloud.google.com/monitoring/api/resources#tag_vpn_tunnel)** |  _The IP version of the HA VPN gateway. Sampled every 60 seconds. After sampling, data is not visible for up to 60 seconds._   
`gateway_ip_version`: The IP version of the HA VPN gateway.   
  
Table generated at 2026-10-14 20:24:33 UTC.

### View HA connection health metrics

The following metrics indicate if the connection for an HA VPN gateway is healthy and if its configuration meets the 99.99% SLA.

When creating a chart, if you specify the resource type and metric as **Cloud VPN gateway** and **Number of connections** , you can find these labels in the **Filter** field. For more information, see [Metrics, filters, and aggregation](https://docs.cloud.google.com/monitoring/charts/selecting-aggregating-metrics).

Status | Description   
---|---  
`configured_for_sla` | Indicates if the HA connection has been fully configured, meaning that the connection contains the necessary number of tunnels and is properly connected to a Cloud Router.  
`gcp_service_health` | Indicates if the HA connection is functioning properly on the Google Cloud side. For example, the tunnel is allocated.  
`end_to_end_health` | Indicates if packets are being successfully sent and received inside the HA connection.  
  
### View metrics in Network Topology

You can use Network Topology to audit your networking configuration and troubleshoot networking issues.

Network Topology overlays throughput values on each connection. This feature lets you quickly see the amount of traffic moving between entities, such as the traffic traversing the VPN tunnels between Google Cloud and the on-premises network.

For information about the supported metrics for each connection, see the [Metrics reference](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/reference/metrics-reference).

Metric values are based on the final five minutes of the selected hour. You can also view historical metrics for six weeks by clicking any of the edges.

For more information, see [Data collection and freshness](https://docs.cloud.google.com/network-intelligence-center/docs/network-topology/concepts/overview#data).

###  Console 

  1. In the Google Cloud console, go to the **Network Topology** page. 

[Go to Network Topology](https://console.cloud.google.com/net-intelligence/topology)

  2. In the entities selection pane, select a metric from the **Edge metric** drop-down menu.

  3. Navigate to a specific entity hierarchy to view traffic that is related to that entity.

For example, if you want to view traffic bandwidth traversing the VPN tunnel between Google Cloud and the on-premises network, expand the entities until you see that VPN tunnel connection.

  4. Click the entity to highlight all its traffic paths.

Network Topology displays metric values for each connection that supports the selected metric.




### View reasons for drops

When a Cloud VPN gateway drops a packet, the gateway provides a reason for the drop.

Reason | Description  | Source of traffic  
---|---|---  
`dont_fragment_icmp` | The dropped packet was an ICMP packet of a size greater than the MTU with the `do not fragment` bit set. Such packets are used for `path-mtu-discovery`.  | Google Cloud VM  
`exceeds_mtu` | The first fragment of a UDP or ESP egress packet is greater than the MTU and has the `do not fragment` bit set. | Google Cloud VM  
`dont_fragment_nonfirst_fragment` | A fragment of a UDP or ESP egress packet that is not the first fragment, and which is greater than the MTU and has the `do not fragment` bit set. | Google Cloud VM  
`Sent packets::invalid` | Packet was invalid or corrupt in some way. For example, the packet might have had an invalid IP header. | Google Cloud VM  
`Sent packets::throttled` | Packet dropped due to [excessive load](https://docs.cloud.google.com/network-connectivity/docs/vpn/concepts/classic-topologies#vpn-throughput) on the Cloud VPN gateway. | Google Cloud VM  
`fragment_received` | Received a fragmented packet from the peer. | Peer Cloud VPN gateway  
`sequence_number_lost` | A packet has arrived at the gateway with a sequence number greater than the expected sequence number, indicating that a packet with an earlier sequence number might have been dropped.  | Peer Cloud VPN gateway  
`suspected_replay` | ESP packet received with a sequence number that had already been received. Peer device needs to be investigated to know the reason so as to why duplicate ESP packets are being sent from the peer end. | Peer Cloud VPN gateway  
`Received packets::invalid` | Packet was invalid or corrupt in some way. For example, the packet might have had an invalid IP header. | Peer Cloud VPN gateway  
`Received packets::throttled` | Packet dropped due to excessive load on the Cloud VPN gateway. | Peer Cloud VPN gateway  
`sa_expired` | Received a packet with unknown Security Association (SA). Could be as a result of using an SA that is already expired or one that was never negotiated. | Peer Cloud VPN gateway  
`unknown` | Packet was dropped for a reason that the gateway wasn't able to categorize. | Either  
  
## What's next

  * To find more information about monitoring, see [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs).
  * To find more information about collecting logs and configuring sinks for Cloud VPN, see [Cloud Logging](https://docs.cloud.google.com/logging/docs).
  * To help you solve common issues that you might encounter when using Cloud VPN, see [Troubleshooting](https://docs.cloud.google.com/network-connectivity/docs/vpn/support/troubleshooting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
