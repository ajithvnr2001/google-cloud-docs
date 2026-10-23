---
url: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview/
title: Flow Analyzer overview \u00a0|\u00a0 Network Intelligence Center - Flow Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:35:49.187328+00:00
---

# Flow Analyzer overview  |  Network Intelligence Center - Flow Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Flow Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



#  Flow Analyzer overview Stay organized with collections  Save and categorize content based on your preferences. 

Flow Analyzer lets you quickly and efficiently understand your Virtual Private Cloud (VPC) traffic flows without the need to write complex SQL queries for analyzing VPC Flow Logs. Flow Analyzer lets you perform opinionated network traffic analysis with 5-tuple granularity (source IP, destination IP, source port, destination port, and protocol).

Developed using [Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view) and powered by [BigQuery](https://docs.cloud.google.com/bigquery), Flow Analyzer enables in-depth analysis of inbound and outbound traffic of your VM instances. It lets you monitor, troubleshoot, and optimize your networking deployment for better performance and enhanced security which helps ensure compliance, and save on costs.

Flow Analyzer analyzes VPC Flow Logs data stored in a log bucket ([record format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format)). To use Flow Analyzer, you must select a project with a log bucket that contains VPC Flow Logs. For more information, see the [VPC Flow Logs overview](https://docs.cloud.google.com/vpc/docs/flow-logs). VPC Flow Logs can be used for network monitoring, forensics, real-time security analysis, and expense optimization.

Flow Analyzer runs queries on the fields included in VPC Flow Logs. For more information, see [Key properties of VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/flow-logs#key_properties).

In Flow Analyzer, you can do the following:

  * Query logs reported by VPC Flow Logs
  * Use SQL filters to refine your queries
  * Sort query results by total traffic, aggregate packets, packet drops, or latency
  * View traffic for a specific time period
  * View the top five flows with the highest traffic, packet drops, or latency for the selected time period
  * View resources with the highest traffic, packet drops, or latency for the selected time period
  * View traffic details for specific source and destination pairs in your query results



## How it works

VPC Flow Logs samples packets in your VPC network to generate flow logs, which can be stored in [Cloud Logging](https://docs.cloud.google.com/logging/docs/view/logs-viewer-interface) or routed to supported destinations, such as BigQuery or a third-party platform through Pub/Sub.

When flow logs are stored in Observability Analytics-enabled buckets in Cloud Logging, you can use Flow Analyzer to query and visualize your traffic data.

## Query components

To analyze and understand your traffic flows, you must run a query on VPC Flow Logs. Flow Analyzer helps you build the query, customize the display options, and drill down to view and monitor your traffic flows.

### Traffic aggregation

To analyze VPC traffic flows, you must determine the aggregation approach to filter the flows between the resources. Flow Analyzer organizes the flow logs for aggregation in the following ways:

  * **Source and destination** : this option uses the **SRC** and **DEST** information included in VPC Flow Logs. This view aggregates the traffic from source to destination.
  * **Client and server** : this option tries to find the initiator of the connection. A resource with the smaller port number is considered the server. It also considers the resources with **gke_service** definition as the servers because services don't initiate requests. This view aggregates the traffic in both directions.



### Time-range selector

The default time range is one hour, but you can select from preset time options, specify a custom start and end time, or center the time range around a specific timestamp by using the time-range selector. For example, if you want to view the data for the past week, then select **Last 1 week** from the time-range selector.

You can also set your time zone preferences by using the time-range selector.

### Basic filters

Basic filters let you define the scope of a query. Only those flows that match the filters that you select are shown in the query results. You can select filters for the following:

  * **Source** and **Destination** (if **Traffic aggregation** is set to **Source - Destination**)
  * **Client** and **Server** (if **Traffic aggregation** is set to **Client - Server**)
  * **Flow parameters**



In each **Filter** list, you can add multiple filter expressions. If you select more than one value for the same filter, an OR operator is used. If you select more than one filter, an AND operator is used.

For example, if you select two **IP** address values—`10.10.0.10` and `10.10.0.20`—and two **Country** values—`usa` and `fra`—the following filter logic is applied to the query: `(IP=10.10.0.10 OR IP=10.10.0.20) AND (Country=usa OR Country=fra)`.

To build and run queries using basic filters, see [Build and run a query](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows#build-query).

### SQL filters

To build complex queries, you can use SQL filters. Using complex queries, you can perform tasks such as the following:

  1. Comparing field values with each other
  2. Building complex boolean logic using AND/OR and nested OR operations
  3. Performing complex operations on IP addresses using BigQuery functions



The SQL filter queries use BigQuery SQL syntax. For more information, see the [BigQuery SQL syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax).

To view filter expression syntax and examples, click **Filter expression syntax and examples**.

To build and run queries using SQL filters, see [Build and run a SQL query](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows#build-sql-query).

## Query results

By default, the query results include the following components:

  * The **Highest data flows** chart: displays the top five highest traffic flows over time along with the rest of the traffic. You can spot trends like traffic spikes using this chart.
  * The **All data flows** table: shows the top traffic flows up to 5,000 rows aggregated over the selected duration. This table displays the fields selected for organizing the flows while defining the filters for the query.



If you select **Latency** in **Display options**, **Highest latency flows** and **All latency flows** are displayed instead. If you select **Packet drops** , Flow Analyzer displays the **Highest drops** chart and the **All packet drop flows** table.

## Display options

After running a query, you can refine your results by using display options. Your selections update both the chart and the table.

Flow Analyzer provides three modes for customizing how data is displayed:

  * **Data volume** (default): displays bytes and packets sent.
  * **Packet drops**: displays drop rate and drop count for bytes and packets.
  * **Latency**: displays round-trip time (RTT).



For more information, see [Customize display options](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows#customize-display-options).

### Data volume

The following options are available for the **Data volume** display mode.

#### Metric types

You can choose to view one of the following metric types.

  * **Bytes sent** : contains information about the payload volumes and doesn't include headers. This metric value can be zero because some packets have only headers and don't include any payload.

**Note:** You can't use this metric to estimate costs because the data is sampled and it doesn't include headers.
  * **Packets sent** : indicates the number of packets sent from the source to the destination.




For both the metric types, you can choose additional metric aggregations.

#### Metric aggregation

You can view metric aggregation in the following ways.

If you select **Bytes sent** as the metric and **Source and destination** as the traffic aggregation, the following options are available:

  * **Total traffic** : this is always enabled by default and shows the total traffic for the chosen time period.
  * **Average traffic rate** : shows the average traffic rate (in bytes per second) for the chosen time period, calculated only for the alignment periods during which the traffic was observed. For more information, see Alignment period.
  * **Median traffic rate** : displays the median traffic rate (in bytes per second) for the chosen time period, calculated only for the alignment periods during which the traffic was observed. For more information, see Alignment period.
  * **P95 traffic rate** : shows the 95th percentile traffic rate in bytes per second for the chosen time period, calculated only for the alignment periods during which the traffic was observed. For more information, see Alignment period.
  * **Maximum traffic rate** : shows the maximum traffic rate in bytes per second for the chosen time period.



If you select **Packets sent** as the metric and **Source and destination** as the traffic aggregation, the following options are available:

  * **Aggregate packets** : shows the count of packets sent for the chosen time period. Enabled by default.
  * **Average packets rate** : displays the average packets rate for the chosen time period, calculated only for the alignment periods during which the traffic was observed. For more information, see Alignment period.
  * **Median packets rate** : displays the median packets rate for the chosen time period, calculated only for the alignment periods during which the traffic was observed. For more information, see Alignment period.
  * **P95 packets rate** : shows the 95th percentile packets rate for the chosen time period, calculated only for the alignment periods during which the traffic was observed. For more information, see Alignment period.
  * **Maximum packets rate** : shows the maximum packets rate for the chosen time period.



#### Sampling point

For [VM-to-VM network communication](https://docs.cloud.google.com/vpc/docs/about-traffic-flows), flow logs are available (with sampling applied) at both the VMs that send and receive traffic. If both the endpoint VMs are in subnets that have VPC Flow Logs enabled, the same flow gets reported twice. You can choose one of the following four approaches to determine which VPC Flow Logs contribute to the computed metrics and how they are evaluated:

  * **Source endpoint** : the number of bytes sent or packets sent reported at the source endpoint of a flow
  * **Destination endpoint** : the number of bytes sent or packets sent reported at the destination endpoint of a flow
  * **Sum of source and destination endpoint** : the sum of bytes sent or packets sent reported by both endpoints of a flow
  * **Average of source and destination endpoint** : an average of bytes sent or packets sent reported by both endpoints of a flow if both the source and the destination information are available in VPC Flow Logs



#### Traffic deduplication

To prevent traffic reported at the source and destination VMs from being counted twice, you can choose the **Average of source and destination endpoint** sampling option. Flow Analyzer identifies equivalent flows within each alignment period and calculates the averages of the reported metrics values (bytes count and packets count).

For alignment periods where equivalent flows are reported at both SRC and DEST, all traffic attributed to a given alignment period is divided by two.

### Packet drops

The following options are available for the **Packet drops** display mode.

#### Metric types

You can choose to view one of the following metric types:

  * **Packets sent** (default): displays the number of dropped packets.
  * **Bytes sent** : displays the number of dropped bytes.



#### Timeline

You can choose how packet drops are calculated and displayed on the timeline in the **Highest drops** chart:

  * **Drop rate (%)** (default): displays the percentage of packets or bytes that were dropped in the selected alignment period.
  * **Drop count** : displays the number of packets or bytes that were dropped in the selected alignment period.



#### Sampling point

When analyzing packet drops, Flow Analyzer displays packet loss data that is reported by either the source or destination of a flow (default). You can [adjust the sampling points](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows#display-packet-drops) to view data from only the source (egress drops) or destination (ingress drops).

Additionally, the **All packet drop flows** table includes a **Drop reason** column to help you troubleshoot. Click a drop reason to view more information about the dropped traffic, including its underlying cause.

### Latency

The following options are available for the **Latency** display mode.

#### Metric type

Flow Analyzer uses [RTT](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records) data from VPC Flow Logs to provide latency analysis for TCP traffic.

#### Ranking metrics

You can rank your traffic flows using the following metrics. This selection defines the sort order in the **All latency flows** table and determines which flows are displayed in the **Highest latency flows** chart.

  * **Average** : sorts flows by the highest mean latency (includes latency spikes).
  * **Max** : sorts flows by the highest latency spike.
  * **Median** : sorts flows by the highest median latency (excludes latency spikes).
  * **P95** : sorts flows by the highest 95th percentile latency.
  * **P99** : sorts flows by the highest 99th percentile latency.
  * **Standard deviation** : sorts flows by the highest variation (inconsistency) in latency.



#### Sampling point

Latency is reported for both source and destination endpoints. You can view latency values for either side of traffic flows.

#### Metric aggregation

The following options are available for aggregating latency data:

  * **Chart aggregation** : defines the calculation method for the **Highest latency flows** chart and is applied to the data that is selected based on the ranking metric you choose. You can choose **Average** , **Max** , **Median** , **P95** , or **P99** as the latency calculation method.

For example, if you rank flows by **Median** latency while setting the chart aggregation to **Max latency** , the chart displays the highest latency spikes for the five flows that have the highest median latency.

  * **Table aggregation** : selects which metrics, in addition to the chosen ranking metric, are displayed as columns in the **All latency flows** table.




You can also exclude low-volume flows from the latency analysis.

### Alignment period

You can choose from 5 seconds to 1 day for the time range of the details in the chart. Automatic mode selects the optimal alignment period depending on the length of the selected period.

Every point on the timeline represents aggregated data for a specific time period. The length of this period is called the **alignment period**.

The performance declines with the decrease of the value of the alignment period. For higher values of the alignment period, the chart becomes less granular. You might not be able to view short spikes with higher values.

For large time durations, a smaller alignment period is not helpful. For example, if you select 1 minute alignment for a 30 day period, Flow Analyzer generates more than 43,000 data points. Because that's 10 times more than the 4k display pixels, you'll not be able to view all the details and some options are disabled for large time durations.

For more information about how the sampling is done and alignment period is determined to display the query results, see [Metrics and alignment period](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/alignment-period-aggregation).

### View flow details

In the **All data flows** , **All packet drop flows** , or **All latency flows** table, click **Details** for any flow. The **Flow details** panel appears. This panel provides information such as the source, destination, traffic, drill down options, and egress autonomous system (AS) paths.

#### Drill down view

You can drill down by splitting a selected traffic flow using an extra field. For example, if a flow includes generic details about 1,000 GiB traffic from Google Cloud zone X to zone Y, you can drill down using another field such as the source IP address. The results include several IP addresses that make up the original flow.

The fields that appear in the drill down component are selected as follows:

  * When you access the flow details, Flow Analyzer runs several queries. Each query tries to drill down the selected flow using the fields available in the VPC Flow Logs and not yet used in the original query. For example, if the executed query already includes the IP address details, you don't need to run the query with this field again and can't drill down using this field.
  * If any of the additional queries return a single field value, it gets added to the source and destination details section even though it is not fetched earlier.
  * If any of the query results include more than one field value, the corresponding field appears in the drill down list.



As you select a field in the drill down list, the drill down table and the chart get updated to display the top three traffic flows.

You can also use the **Compare to past** toggle. Select this feature to view six lines: three solid lines for the three top talkers from the drill down and three dashed lines in corresponding colors representing the past traffic.

To drill down traffic flows using more fields, see [Drill down traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows#break-down-flows).

#### Egress AS paths view

In the **Egress AS paths** tab, you can view the AS paths that egress packets traverse to reach destinations outside of Google Cloud's network. An AS path can include multiple autonomous system numbers (ASNs).

You control which AS details are displayed in the **Egress AS paths** tab by using the **Egress AS path** filter in the **Flow parameters** list. For example, the **longer than** and **shorter than** options in the **Comparator** field let you specify the number of ASNs per AS path. To view AS paths that include a specific ASN, you can use the **has first ASN** or **contains ASN** option.

Edges on the Egress AS paths graph are weighted by the number of flow logs. In an AS path on the graph, an edge represents the number of flow logs containing both of the ASNs that the edge connects. Data displayed on the Egress AS paths graph changes based on the **Egress AS path** filter options and time period that you select when running a query.

## Explore in Observability Analytics

You can view the raw SQL query in Observability Analytics.

For advanced analysis, you can directly modify SQL code used to visualize the traffic. The **Explore in Log Analytics** feature directs you to the **Log Analytics** page with a prefilled query.

## What's next

  * [Metrics and alignment period](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/alignment-period-aggregation)
  * [Analyze traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows)
  * [Enable Observability Analytics](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/enable-log-analytics)
  * [Configure a central bucket](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/configure-central-bucket)
  * [Run Connectivity Tests from Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/run-connectivity-tests)
  * [Monitor your traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/monitor-traffic-flows)
  * [Troubleshoot data issues in Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/manage-flow-analyzer)



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
