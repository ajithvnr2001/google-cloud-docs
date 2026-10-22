---
url: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows/
title: Analyze your traffic flows \u00a0|\u00a0 Network Intelligence Center - Flow Analyzer \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:14:27.955555+00:00
---

# Analyze your traffic flows  |  Network Intelligence Center - Flow Analyzer  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/analyze-traffic-flows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Networking ](https://docs.cloud.google.com/docs/networking)
  * [ Network Intelligence Center ](https://docs.cloud.google.com/network-intelligence-center/docs)
  * [ Flow Analyzer ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer)
  * [ Guides ](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview)



#  Analyze your traffic flows Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to query and analyze traffic flows.

## Before you begin

  1. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  2. [Enable VPC Flow Logs](https://docs.cloud.google.com/vpc/docs/using-flow-logs#enabling-vpc-flow-logs).




### Required roles and permissions

Because Flow Analyzer reads data on behalf of the user, ensure that you have sufficient permissions to read the bucket containing the logs. The bucket must also be upgraded to use Observability Analytics.

  * To let a user read logs in the buckets, use the Logs Explorer page. Use the Observability Analytics page to grant one of the following roles:

    * For access to the `_Default` view on the `_Default` bucket, grant the Logs Viewer role (`roles/logging.viewer`).
    * For access to all logs in the `_Default` log bucket, including data access logs, grant the Private Logs Viewer role (`roles/logging.privateLogViewer`).

For more information, see [Logging roles](https://docs.cloud.google.com/logging/docs/access-control#considerations).

  * To let a user read logs that are stored in a user-defined bucket, grant the Logs View Accessor role (`roles/logging.viewAccessor`). You can restrict authorization to a specific [log view](https://docs.cloud.google.com/logging/docs/logs-views). For more information, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).

  * Alternatively, create a custom role that grants the following permissions:

    * `logging.buckets.get`
    * `logging.buckets.list`
    * `logging.logEntries.list`
    * `logging.logs.list`
    * `resourcemanager.projects.get`



## Build and run a query

To build and run a query using basic filters, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Flow Analyzer** page.

[Go to Flow Analyzer](https://console.cloud.google.com/net-intelligence/flow-analyzer)

  2. Click settings**Source bucket** and do the following:

     1. In the **Log bucket** field, select the log bucket containing the flow logs that you want to query. By default, flow logs are stored in the **_Default** log bucket.
     2. In the **Log bucket view** field, select a log view.
     3. Optional: If you want to query flow logs associated with a specific VPC Flow Logs configuration, do the following: 
        1. Select the **Select specific configuration** checkbox.
        2. In the **Log configurations** list, select one or more VPC Flow Logs configurations. The **Flow logs configured for subnetworks** option selects all flow logs for all subnets in the log bucket.
  3. In the **Traffic aggregation** menu, select one of the following options:

     * **Source - Destination** : aggregate the traffic from the source to the destination.
     * **Client - Server** : aggregate the traffic in both directions by considering the resources with lower port numbers and service definitions or having GKE service properties as servers.

For more information, see [Traffic aggregation](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#traffic-aggregation).

  4. In the time-range selector, set the time range of your query. The default time range is one hour. You can select a preset time range, specify a custom start and end time, or select a time range around a specific time.

  5. In the **Filter** lists, select one or more query filters. Each filter corresponds to a VPC Flow Logs field. For more information about these fields, see [Record format](https://docs.cloud.google.com/vpc/docs/about-flow-logs-records#record_format). If you don't select any filters, Flow Analyzer shows the query results for all flows within the selected period of time.

If you select more than one value for the same filter, an `OR` operator is used. If you select more than one filter in the same **Filter** list, an `AND` operator is used. For example, if you select two **IP** address values—`10.10.0.10` and `10.10.0.20`—and two **Country** values—`usa` and `fra`—the following filter logic is applied to the query: `(IP=10.10.0.10 OR IP=10.10.0.20) AND (Country=usa OR Country=fra)`.

  6. Select how to organize your query results by using the **Organize flows by** lists or leave the default values.

  7. Click **Run new query**.

The **Highest data flows** chart and the **All data flows** table are updated.

You can use the **Display options** panel to customize your query results. For more information, see [Display options](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#display-options). To select custom options, see Customize display options.




## Build and run a SQL query

To build and run a query in Flow Analyzer using SQL filters, do the following:

###  Console 

  1. In the Google Cloud console, go to the **Flow Analyzer** page.

[Go to Flow Analyzer](https://console.cloud.google.com/net-intelligence/flow-analyzer)

  2. Select a log bucket. If you plan to use the **_Default** log bucket, you can skip this step.

  3. To set the time range of your query, use the time-range selector or select **Re-run selected period**.

  4. In the **Traffic aggregation** menu, select one of the following options:

     * **Source - Destination** : aggregate the traffic from the source to the destination.
     * **Client - Server** : aggregate the traffic in both directions by considering the resources with lower port numbers and service definitions as servers.

For more information, see [Traffic aggregation](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#traffic-aggregation).

  5. Click **SQL Filters**.

  6. Enter the SQL filter query using [BigQuery SQL syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax).

  7. To view filter expression syntax and examples, click **Filter expression syntax and examples**.

  8. Organize flow by using the fields. Select a field to organize the flow details.

  9. Click **Run new query**.

The **Highest data flows** chart and the **All data flows** table are updated.

You can use the **Display options** panel to customize your query results. For more information, see [Display options](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#display-options). To select custom options, see Customize display options.




## Customize display options

You can use the following modes to display and analyze data about your traffic flows:

  * **Data volume** (default): displays bytes and packets sent.
  * **Packet drops** : displays drop rate and drop count for bytes and packets.
  * **Latency** : displays round-trip time.



For more information, see [Display options](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#display-options).

### Display flows in data volume mode

###  Console 

  1. Build and run a query.
  2. In the **Display options** panel, review and optionally modify the **Alignment period**. For more information, see [Alignment period](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#alignment-period).
  3. Select **Data volume** as the display mode.
  4. For **Metric type** , select **Bytes sent** or **Packets sent**.
  5. Review and optionally modify the **Advanced settings** section:

     * The **Table aggregation** option: use to select which metrics are displayed as columns in the **All data flows** table.

       * If you select **Bytes sent** as the metric type, you can choose from the following options:

         * **Total traffic** : the total traffic for the selected time period. Enabled by default.
         * **Avg traffic rate** : the average traffic rate for the selected time period. Calculated only for the alignment periods during which the traffic was observed.
         * **Median traffic rate** : the median traffic rate for the selected time period. Calculated only for the alignment periods during which the traffic was observed.
         * **P95 traffic rate** : the 95th percentile traffic rate for the selected time period. Calculated only for the alignment periods during which the traffic was observed.
         * **Max traffic rate** : the maximum traffic rate for the selected time period.
       * If you select **Packets sent** as the metric, you can choose from the following options:

         * **Aggregate packets** : the aggregate number of packets for the selected time period. Enabled by default.
         * **Avg packets rate** : the average packet rate for the selected time period. Calculated only for the alignment periods during which the traffic was observed.
         * **Median packets rate** : the median packet rate for the selected time period. Calculated only for the alignment periods during which the traffic was observed.
         * **P95 packets rate** : the 95th percentile packet rate for the selected time period. Calculated only for the alignment periods during which the traffic was observed.
         * **Max packets rate** : the maximum packet rate for the selected time period.

For more information, see [Metric aggregations](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#metric-aggregation).

     * The **Sampling points** option: use to select the reporting endpoint or a combination of both endpoints:

       * **Source endpoint** : the number of bytes sent or packets sent as reported at the source endpoint of a flow.
       * **Destination endpoint** : the number of bytes sent or packets sent as reported at the destination endpoint of a flow.
       * **Sum of source and destination** : the sum of bytes sent or packets sent as reported by both endpoints of a flow.
       * **Avg of source and destination** : an average of bytes sent or packets sent as reported by both endpoints of a flow if both source and destination details are available in VPC Flow Logs.

For more information, see [Sampling point](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#sampling-point).

  6. Click **Run new query**.




### Display flows in packet drop mode

###  Console 

  1. Build and run a query.
  2. In the **Display options** panel, review and optionally modify the **Alignment period**. For more information, see [Alignment period](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#alignment-period).
  3. Select **Packet drops** as the display mode.
  4. For **Metric type** , select **Packets sent** or **Bytes sent**.
  5. For **Show timeline** , select **Drop rate (%)** or **Drop count**.
  6. In the **Advanced settings** section, use the **Sampling points** option to display packet loss from the **Source endpoint** , the **Destination endpoint** , or **Source and destination** (either endpoint). For more information, see [Sampling point](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#packet-drops-sampling-point).
  7. Click **Run new query**.



### Display flows in latency mode

###  Console 

  1. Build and run a query.
  2. In the **Display options** panel, review and optionally modify the **Alignment period**. For more information, see [Alignment period](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#alignment-period).
  3. Select **Latency** as the display mode.
  4. For **Metric type** , select **Round-trip time (median)**.
  5. For **Rank flows by** , select a ranking metric. This metric defines the sort order in the **All latency flows** table and determines which flows are displayed in the **Highest latency flows** chart. You can choose from the following ranking metrics:

     * **Average** : sorts flows by the highest mean latency (includes latency spikes).
     * **Max** : sorts flows by the highest latency spike.
     * **Median** : sorts flows by the highest median latency (excludes latency spikes).
     * **P95** : sorts flows by the highest 95th percentile latency.
     * **P99** : sorts flows by the highest 99th percentile latency.
     * **Standard deviation** : sorts flows by the highest variation (inconsistency) in latency.
  6. Review and optionally modify the **Advanced settings** section:

     * The **Sampling points** option: use to select the reporting endpoint, which can be either the source or the destination.
     * The **Chart aggregation** option: use to specify the calculation method for the **Highest latency flows** chart. This method is applied to the data that is selected based on the ranking metric you choose in the **Rank flows by** list. You can choose from the following calculation methods:

       * **Average latency** : calculates the mean latency (includes latency spikes).
       * **Max latency** : calculates the highest latency spikes.
       * **Median latency** : calculates the median latency (excludes latency spikes).
       * **P95 latency** : calculates the 95th percentile latency.
       * **P99 latency** : calculates the 99th percentile latency.
     * The **Table aggregation** option: use to select which metrics, in addition to your ranking metric, are displayed as columns in the **All latency flows** table.

     * The **Hide flows that contributed less than** option: use to exclude low-volume flows from the query.

For example, if your query filtered a total of 1,000 logs, setting this option to **1%** hides any flow that contributed fewer than 10 logs. Setting it to **0%** applies no filtering and displays every flow regardless of its contribution.

  7. Click **Run new query**.




## View flow details

To view flow details for a selected flow in the data flows table, do the following:

###  Console 

  1. Build the query. 
     1. Select a log bucket. If you plan to use the **_Default** log bucket, you can skip this step.
     2. To set the time range of your query, use the time-range selector or select **Re-run selected period**.
     3. Select the filters.
     4. Select the fields to organize the results.
  2. Run the query.
  3. In the **All data flows** , **All packet drop flows** , or **All latency flows** table, click **Details** for any flow. The **Flow details** page that appears shows all the resources matching the selected filters and the traffic of these resources. For packet drops, you can also click the drop reason in the **All packet drop flows** table to view more information about the drop.



## Drill down traffic flows

You can further refine the traffic of the selected resources. Using Flow Analyzer, you can drill down into the query results by using the remaining fields available in VPC Flow Logs. For more information, see [View flow details](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/overview#break-down-flow-details).

To drill down traffic flows using more fields, do the following:

###  Console 

  1. Build the query. 
     1. Select a log bucket. If you plan to use the **_Default** log bucket, you can skip this step.
     2. To set the time range of your query, use the time-range selector or select **Re-run selected period**.
     3. Select the filters.
     4. Select the fields to organize the results.
  2. Run the query.
  3. In the **All data flows** , **All packet drop flows** , or **All latency flows** table, click **Details** for any flow.

The **Flow details** page that appears shows all the resources matching the selected filters and the traffic of these resources.

  4. In the **Drill down by** list, select a field to do a drill down.

  5. To compare with past traffic, click the **Compare to past** toggle. This feature lets you view six lines: three solid lines for the three top traffic flows from the drill down and three dashed lines in corresponding colors representing the past traffic.




## What's next

  * [Metrics and alignment period](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/alignment-period-aggregation)
  * [Run Connectivity Tests](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/run-connectivity-tests)
  * [Monitor your traffic flows](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/monitor-traffic-flows)
  * [Troubleshoot data issues in Flow Analyzer](https://docs.cloud.google.com/network-intelligence-center/docs/flow-analyzer/manage-flow-analyzer)



Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
