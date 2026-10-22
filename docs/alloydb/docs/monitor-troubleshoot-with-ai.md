---
url: https://docs.cloud.google.com/alloydb/docs/monitor-troubleshoot-with-ai/
title: Monitor and troubleshoot with AI assistance \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:37:59.901111+00:00
---

# Monitor and troubleshoot with AI assistance  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/monitor-troubleshoot-with-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Monitor and troubleshoot with AI assistance Stay organized with collections  Save and categorize content based on your preferences. 

**Important** : As of April 10, 2026, you can create, run, and edit [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) only if you have a [Premium Support contract](https://cloud.google.com/support/premium). If you ran an investigation prior to April 10, 2026, then the results of the investigation continue to be available to you in the Google Cloud console.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use AI assistance to help you monitor and troubleshoot your AlloyDB for PostgreSQL resources. You can use the AI-assisted troubleshooting tools of AlloyDB and [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) to troubleshoot slow queries and troubleshoot high database load. 

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Limitations

The following limitations apply to AI-assisted troubleshooting in AlloyDB:

  * AI-assisted troubleshooting offers valuable insights based on standard PostgreSQL configurations. AlloyDB's unique architecture, including its disaggregated storage, caching, columnar engine, and optimized background processes, means that certain checks and recommendations can differ from actual AlloyDB performance metrics. We recommend that you consider AI-assisted troubleshooting recommendations as starting points and refer to the [AlloyDB documentation](https://docs.cloud.google.com/alloydb/docs/overview) for definitive guidance. 
  * AI-assisted troubleshooting isn't supported for the following AlloyDB configurations:
    * Instances inside a [VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview)
    * Instances enabled with [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)



## Before you begin

[Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini). 

After you set up Gemini Cloud Assist, the service can take a few minutes to propagate. Wait for propagation to complete before you enable AI-assisted troubleshooting in AlloyDB.

### Required roles and permissions

To get the permissions that you need to use AI-assisted troubleshooting, ask your administrator to grant you the following IAM roles on the project that hosts the AlloyDB instance: 

  * [Database insights viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/databaseinsights#databaseinsights.viewer) (`roles/databaseinsights.viewer`)
  * Use Gemini Cloud Assist investigations: [Gemini Cloud Assist Investigation Owner ](https://docs.cloud.google.com/iam/docs/roles-permissions/geminicloudassist#geminicloudassist.investigationOwner) (`roles/geminicloudassist.investigationOwner`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use AI-assisted troubleshooting. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use AI-assisted troubleshooting:

  * `databaseinsights.performanceIssues.detect`
  * `databaseinsights.performanceIssues.investigate`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information about required roles and permissions for using Gemini Cloud Assist investigations, see [Troubleshoot issues with Gemini Cloud Assist Investigations](https://docs.cloud.google.com/cloud-assist/investigations#consideration).

## Enable AI-assisted troubleshooting

When you enable AI-assisted troubleshooting for your AlloyDB instance, AlloyDB can analyze the performance of your databases and detect anomalies in the execution of your queries. When AlloyDB detects anomalies in query performance or identifies high system load, AI-assisted troubleshooting helps you analyze the situation with evidence and provides recommendations.

To enable AI-assisted troubleshooting for your AlloyDB instance, do the following:

  1. In the Google Cloud console, go to the **Clusters** page.

[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)

  2. From the list of clusters and instances, click an instance.

  3. Click **Query insights**.

  4. Click either **Enable** or **Edit settings**.

  5. In the **Edit query insights settings** tab, select **Enable advanced query insights features for AlloyDB**.

By default, this turns on the **AI-assisted troubleshooting** checkbox.

**Note:** Enabling advanced query insights features requires you to restart your instance.
  6. Click **Save**.

  7. For the best results, wait 24 hours after you enable AI-assisted troubleshooting in the Google Cloud console to let AlloyDB build a baseline of the average performance of your instance, database, and queries.




For more information about enabling advanced query insights, see [Improve query performance using advanced query insights](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights#enable-advanced-features). 

## Open Gemini Cloud Assist

To use Gemini Cloud Assist with AlloyDB, do the following:

  1. In the Google Cloud console, go to the **Clusters** page.
[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)
  2. From the list of clusters and instances, click an instance.
  3. Click **Query insights**.
  4. To open the **[Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel)** , click auto_awesome**Open or close Gemini Cloud Assist chat**.
  5. In the **Cloud Assist panel** , enter a prompt that describes the information that you're interested in.
  6. After you enter the prompt, click send **Send prompt**. 

Gemini returns a response to your prompt based on information from the last hour.




## Troubleshoot slow queries

To use AI assistance with troubleshooting your slow queries, go to the **Query insights** dashboard for your AlloyDB instance in Google Cloud console.

### Top queries table

You can start troubleshooting slow queries with AI assistance in the **Top queries table** section of the **Query insights** dashboard.

AlloyDB can help you identify which queries are performing slower than average during a specific detection time period. After you select a time range in the **Query insights** dashboard, AlloyDB checks whether any queries are performing slower than average by using a detection time period of 24 hours before the end of your selected time range.

When you adjust the time range filter of the **Database load** chart, or any other filter such as database or user, AlloyDB refreshes the **Top queries table** and reruns anomaly detection based on the new list of queries and an updated detection time period.

When AlloyDB detects an anomaly: 

  * AlloyDB performs baseline performance analysis for your query.

  * Every listed query in the table has either an **Investigate** auto_awesome icon or **Warning** warning_spark icon displayed next to the query's **Avg execution time (ms)** value. 




If a query is running slower than expected, then a **Warning** warning_spark icon is displayed. When you click either icon, [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/investigations) is used to help analyze the query execution and offers observations about what might have caused any issue. Based on these observations, Gemini Cloud Assist generates a hypothesis that can help you address the issue.

To troubleshoot slow queries in the **Top queries** table in the **Query insights** dashboard, do the following:

  1. In the Google Cloud console, go to the **Clusters** page.
[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)
  2. From the list of clusters and instances, click an instance.
  3. Click **Query Insights**.
  4. In the **Executed queries** chart, use the **Time range** filter to select either 1 hour, 6 hours, 1 day, 7 days, 30 days or a custom range.
  5. In the **Top queries** table, under the **Queries** tab, review the list of queries for your database.
  6. If a **Warning** warning_spark icon appears next to the query's **Avg execution time (ms)** value for a query, then AlloyDB has detected an anomaly in your query performance. AlloyDB checks for anomalies within the 24-hour time period that occurs before the end of your selected time range.
  7. Click the **Warning** warning_spark icon.
  8. In the **Query is slower than usual** dialog, click **New Investigation** to start troubleshooting with AI assistance from Gemini Cloud Assist. After about two minutes, the **Investigation details** pane opens with the following sections: 
     * **Issue**. A description of the issue being investigated, including the investigation’s start and stop time. 
     * **Observations**. A list of observations about the issue. For example, these can include lock contention details, such as a longer than expected lock wait ratio for the query.
     * **Hypotheses**. A list of AI-recommended actions to take to help address the slow running query.
  9. If you want to see all investigations associated with the query, in the **Query is slower than usual** dialog, click **View all investigations**. The **Gemini Cloud Assist** page opens where you can view all currently running and previously completed investigations. You can filter the page by project or label, for example, to find the specific investigation you need.

Alternatively, to see all previous investigations, click the **Notifications** add_alert icon, then select a notification associated with any investigation to open the **Gemini Cloud Assist** page.

  10. Alternatively, if you want to investigate the latency of any query, complete the following steps:
     1. Identify the specific query you want to investigate.
     2. In the **Actions** column, click the **Actions** add_alert icon associated with that query.
     3. Select **Investigate latency** in the menu to run a Gemini Cloud Assist investigation.



### Query details

You can also troubleshoot a slow query with AI assistance from the **Query details** page.

  1. In the Google Cloud console, go to the **Clusters** page.
[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)
  2. From the list of clusters and instances, click an instance.
  3. Click **Query insights** to open the **Query insights** dashboard.
  4. In the **Query insights** dashboard, click the query in the **Top queries** that you want to view. The **Query details** page appears.
  5. Optional: Use the **Time range filter** to select either 1 hour, 6 hours, 1 day, 7 days, 30 days or a custom range. When you adjust the **Time range filter** of the **Query details** page AlloyDB reruns anomaly detection. While the **Time range filter** you choose applies to most results, the **Analysis time period** is always set to 48 hours.
  6. If AlloyDB doesn't detect an anomaly for the query, then you can still run an analysis on the query by clicking the **Investigate** button in the **Query latency** card.



### Analyze query latency

Using AI assistance, you can analyze and troubleshoot the details of your query latency.

#### Analysis time period

The analysis time period consists of the 24 hours that occur before the end of the time range that you select in the **Database load** chart of the **Query insights** dashboard or the **Query details** page. AlloyDB uses this time period to compare baseline metrics with the metrics retrieved during the time period of the anomaly.

On the **Query details** page, if AlloyDB has detected an anomaly with the query, then after you select the query from the **Query insights** dashboard, AlloyDB performs a baseline performance analysis for the query using the last 24 hours from the end of the anomaly. If AlloyDB hasn't detected an anomaly with the query and runs anomaly detection on the query again, then AlloyDB uses 48 hours before the end of the selected time range as the performance baseline for the analysis time period.

#### Detected anomaly period

The detected anomaly period represents a time period when AlloyDB finds an anomalous change in query performance. AlloyDB uses the baseline performance measured for the query during the analysis time period.

If AlloyDB detects multiple anomalies for a query within a selected time period, then AlloyDB uses the last detected anomaly.

### Examples of query performance prompts

You can also use Gemini Cloud Assist to enter prompts to help you improve the performance of your queries. Gemini Cloud Assist answers questions for the selected AlloyDB instance and database.

Prompt | Type of response  
---|---  
What are the top queries by latency in my database?  | 

Summaries of queries sorted by latency. Gemini scopes the response by the time range filter selected in the query insights database load chart. 
  
What is the slowest query in this database instance?  | Guidance on how to identify the slowest query by latency.   
  
## Troubleshoot high database load

By accessing the **Query insights** dashboard in the Google Cloud console, you can analyze your database and troubleshoot events when your system experiences a higher database load than average. AlloyDB uses the 24 hours of data that occurs prior to your selected time range to calculate the expected load of your database. You can look into the reasons for the higher load events and analyze the evidence behind reduced performance. AlloyDB also provides recommendations for optimizing your database to improve performance.

To use AI assistance with troubleshooting high database load, go to the **Instance Overview** page or the **Query insights** dashboard in the Google Cloud console.

### Instance overview page

Troubleshoot high database load with AI assistance in the **Instance overview** page by using the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.
[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)
  2. From the list of clusters and instances, click an instance.
  3. In the **Overview** page, from the **Chart** menu, select a metric for the database. You can select any metric, for example, **CPU utilization**.
  4. Optional: To select a specific analysis time period, use the **Time range** filter to select either 1 hour, 6 hours, 1 day, 7 days, 30 days or a custom range. 

You can zoom in to specific sections of the chart where you notice areas of high load that you want to analyze. For example, an area of high load might display CPU utilization levels closer to 100%. To zoom in, you can click and select a portion of the chart.

Click the **Investigate performance** button to start troubleshooting high database load with AI assistance from [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/investigations).

After about two minutes, the **Investigation details** pane opens with the following sections: 

     * **Issue**. A description of the issue being investigated, including the investigation’s start and stop time. 
     * **Observations**. A list of observations about the issue. For example, these can include lock contention details, such as a longer than expected lock wait ratio for the query.
     * **Hypotheses**. A list of AI-recommended actions to take to help address the slow running query.



### Query insights dashboard

Troubleshoot high database load with AI assistance in the **Query insights** dashboard using the following steps:

  1. In the Google Cloud console, go to the **Clusters** page.
[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)
  2. From the list of clusters and instances, click an instance.
  3. Click **Query insights** to open the **Query insights** dashboard.
  4. Optional: Use the **Time range** filter to select either 1 hour, 6 hours, 1 day, 7 days, 30 days or a custom range.

You can zoom in to specific sections of the chart where you notice areas of higher database load by query execution time. To zoom in, you can click and select a portion of the chart.

In the **Database load chart** , click the **Investigate performance** button to start troubleshooting high database load with AI assistance from [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/investigations).

After about two minutes, the **Investigation details** pane opens with the following sections:

     * **Issue**. A description of the issue being investigated, including the investigation’s start and stop time. 
     * **Observations**. A list of observations about the issue. For example, these can include lock contention details, such as a longer than expected lock wait ratio for the query.
     * **Hypotheses**. A list of AI-recommended actions to take to help address the slow running query.



### Analyze high database load

Using AI assistance, you can analyze and troubleshoot the details of your database load.

#### Analysis time period

AlloyDB analyzes your database for the time period that you select in your database load chart from the **Query insights** dashboard or the **Instance overview** page. If you select a time period of less than 24 hours, then AlloyDB analyzes the entire time period. If you select a time period greater than 24 hours, then AlloyDB selects only the last 24 hours of the time period for analysis.

To calculate the baseline performance analysis of your database, AlloyDB includes 24 hours of a baseline time period in its analysis time period. If your selected time period occurs on a day other than Monday, then AlloyDB uses a baseline time period of the _24 hours previous_ to your selected time period. If your selected time period occurs on a Monday, then AlloyDB uses a baseline time period of the _7th day previous_ to your selected time period.

#### Metrics analysis

When AlloyDB starts the analysis, AlloyDB checks for significant changes in the various metrics, including but not limited to the following:

  * Queries per second (QPS)
  * CPU
  * Memory
  * Disk I/O 



AlloyDB compares the baseline aggregated data for your database within the performance data of your analysis time window. If AlloyDB detects a significant change in threshold for a key metric, then AlloyDB indicates a possible situation with your database. The identified situation might explain a root cause for the high load on your database over the selected time period.

#### Recommendations

When Gemini Cloud Assist completes analysis, the **Hypotheses** section of the **Investigation details** pane lists actionable insights to help remediate the issue.

For some situations, based on the analysis, there might not be a recommendation.

### Examples of system performance prompts

You can also use Gemini Cloud Assist to enter prompts to gather information about your system performance. Gemini Cloud Assist answers questions for the selected AlloyDB instance.

Prompt | Type of response  
---|---  
How many error log entries are there for this database instance in the last 7 days?  | 

  * Summary of log entries grouped by their severity type. Gemini scopes the response by the time range filter selected in the instance performance chart.
  * Guidance on how to identify and sort queries by latency.

  
What was the CPU utilization for this database instance around 2 PM today?  |  Metrics results in percentage range for CPU utilization within the time interval.   
  
## Get index recommendations

**Note:** You don't need to enable AI-assisted troubleshooting to obtain index recommendations.

You can obtain index recommendations from AlloyDB in query insights. For more information, see [Index advisor overview](https://docs.cloud.google.com/alloydb/docs/index-advisor-overview). 

### Examples of index recommendation prompts

Use Gemini Cloud Assist to get more information about how to use indexes in your databases. Gemini Cloud Assist answers questions for the selected AlloyDB instance.

Prompt | Type of response  
---|---  
Show index recommendations for queries run in the last 7 days.  | Guidance on the types of queries that can benefit from an index.   
  
## Monitor active queries

**Note:** You don't need to enable AI-assisted troubleshooting to monitor active queries.

Use the **Query insights** dashboard to monitor active queries, and if necessary, terminate long-running processes. For more information, see [Monitor active queries](https://docs.cloud.google.com/alloydb/docs/monitor-active-queries). 

### Examples of active query prompts

Use Gemini Cloud Assist to find out more information about queries that cause high latency or CPU load. Gemini Cloud Assist answers questions for the selected AlloyDB instance.

Prompt | Type of response  
---|---  
What are the top queries currently running in my database?  |  Guidance on how to find the longest running and most resource-intensive queries.   
  
## Troubleshoot read replica lag

You can analyze replication lag by using Gemini Cloud Assist or the **Overview** dashboard in the Google Cloud console.

AI assistance evaluates the following factors to determine why a read replica is falling behind a primary instance.

  * **Primary instance write volume**

High rates of data modification on the primary instance can generate WAL logs faster than the replica can replay them. Gemini checks for "bursty" write patterns that correlate with lag spikes.

  * **Resource constraints (CPU/Memory)**

Replication replay is a CPU-intensive process. Gemini analyzes if the replica's machine tier is insufficient to handle the current replay load or if concurrent read queries are starving the replay process of resources.

  * **Network and storage performance**

In cross-region deployments, network throughput can impact how quickly logs are sent to the replica. The AI assesses internal operation metadata to identify if the bottleneck is in the transport or the application of logs.




### Investigate read replica lag

To use AI assistance with troubleshooting read replica lag, do the following:

  1. In the Google Cloud console, go to the **Clusters** page.
[Go to Clusters](https://console.cloud.google.com/alloydb/clusters)
  2. Navigate to **System Insights**. From the **Instance** menu, select your read replica.
  3. In the **Resolve database issues with AI-assisted troubleshooting** pane, click **Explore investigations**.
  4. In the **Investigation options** window, look for the **Read replica lag** section.
  5. Optional: Select a specific analysis time period using the **Time range** filter, either 1 hour, 6 hours, 1 day, 7 days, or a custom range.
  6. Click **Investigate**. 

Gemini initiates an analysis of replication-specific signals, including WAL (Write Ahead Log) generation rates and replica replay speed. After the analysis is complete, the **Investigation details** pane displays the following sections:

     * **Issue** : A summary of the lag duration and the current "byte lag" or "time lag" between the primary and replica.
     * **Observations** : Specific metrics such as high CPU utilization on the replica or lock contention during WAL replay.
     * **Hypotheses** : AI-recommended steps, such as optimizing heavy write transactions on the primary or upscaling the replica machine tier.



### Examples of read replica lag prompts

You can also use Gemini Cloud Assist and a natural language query to troubleshoot lag between your read replica and your primary instance.

Prompt | Type of response  
---|---  
Why is my AlloyDB read replica lag so high?  |  Guidance on how to reduce replica lag by tuning your database or configuring your cluster.   
  
## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Read [Use Gemini for AI assistance and development](https://docs.cloud.google.com/gemini/docs/overview)
  * Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

  * [Optimize underprovisioned instances](https://docs.cloud.google.com/alloydb/docs/recommender-optimize-underprovisioned-cluster)
  * [Monitor instances](https://docs.cloud.google.com/alloydb/docs/monitor-instance)
  * [Use index advisor](https://docs.cloud.google.com/alloydb/docs/use-index-advisor)
  * [Monitor active queries](https://docs.cloud.google.com/alloydb/docs/monitor-active-queries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
