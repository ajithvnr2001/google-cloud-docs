---
url: https://docs.cloud.google.com/sql/docs/sqlserver/monitor-troubleshoot-with-ai/
title: Monitor and troubleshoot Cloud SQL with AI assistance \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:12:00.778245+00:00
---

# Monitor and troubleshoot Cloud SQL with AI assistance  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/monitor-troubleshoot-with-ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Monitor and troubleshoot Cloud SQL with AI assistance Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/monitor-troubleshoot-with-ai "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/monitor-troubleshoot-with-ai "View this page for the PostgreSQL database engine") | SQL Server

**Important** : As of April 10, 2026, you can create, run, and edit [Gemini Cloud Assist investigations](https://docs.cloud.google.com/cloud-assist/investigations) only if you have a [Premium Support contract](https://cloud.google.com/support/premium). If you ran an investigation prior to April 10, 2026, then the results of the investigation continue to be available to you in the Google Cloud console.

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how you can use AI assistance to help you monitor and troubleshoot your Cloud SQL resources. You can use the AI-assisted troubleshooting tools of Cloud SQL and [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) to troubleshoot slow queries and troubleshoot high database load. 

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Limitations

The following limitations apply to AI-assisted troubleshooting in Cloud SQL:

  * AI-assisted troubleshooting isn't supported for the following Cloud SQL configurations:
    * Cloud SQL Enterprise edition instances
    * Instances that use the [old network architecture](https://docs.cloud.google.com/sql/docs/mysql/upgrade-cloud-sql-instance-new-network-architecture) for Cloud SQL
    * Instances inside a [VPC Service Controls perimeter](https://docs.cloud.google.com/vpc-service-controls/docs/overview)
    * Instances enabled with [Access Transparency](https://docs.cloud.google.com/assured-workloads/access-transparency/docs/overview)
  * Query anomaly detection is available only for Cloud SQL Enterprise Plus edition instances.



## Before you begin

  1. [Ensure that Gemini Cloud Assist is set up for your Google Cloud user account and project](https://docs.cloud.google.com/cloud-assist/set-up-gemini). 

After you set up Gemini Cloud Assist, the service can take a few minutes to propagate. Wait for propagation to complete before you enable AI-assisted troubleshooting in Cloud SQL.

  2. Ensure that your instance is a [Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/editions-intro) instance. 
  3. Ensure that your Cloud SQL instance is using the [new network architecture](https://docs.cloud.google.com/sql/docs/sqlserver/upgrade-cloud-sql-instance-new-network-architecture#check-single-instance).
  4. Enable [query insights for Cloud SQL Enterprise Plus edition](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-insights) and Cloud SQL Enterprise edition.



### Required roles and permissions

To get the permissions that you need to use AI-assisted troubleshooting, ask your administrator to grant you the following IAM roles on the project that hosts the Cloud SQL instance: 

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

When you enable AI-assisted troubleshooting for your Cloud SQL instance, Cloud SQL can analyze the performance of your databases and detect anomalies in the execution of your queries. When Cloud SQL detects anomalies in query performance or identifies high system load, AI-assisted troubleshooting helps you analyze the situation with evidence and provides recommendations.

To enable AI-assisted troubleshooting for your Cloud SQL instance, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Configuration** tile, click **Edit configuration**.
  4. In the **Customize your instance** section, expand **Query insights**.
     1. If not already selected, select **Enable Query insights**.
     2. For Cloud SQL Enterprise Plus edition only, if not already selected, select **Enable Enterprise Plus features**.
  5. For Cloud SQL Enterprise Plus edition only, select **Enable AI-assisted troubleshooting**. For Cloud SQL Enterprise edition instances, troubleshooting with AI assistance is only available if you enable Gemini Cloud Assist.
  6. Click **Save**.
  7. For the best results, wait 24 hours after you enable AI-assisted troubleshooting in the Google Cloud console to let Cloud SQL build a baseline of the average performance of your instance, database, and queries.



For more information about enabling query insights for Cloud SQL Enterprise Plus edition, see [Use query insights to improve query performance](https://docs.cloud.google.com/sql/docs/sqlserver/using-query-insights#enable-insights).

## Open Gemini Cloud Assist

To use Gemini Cloud Assist with Cloud SQL, do the following:

  1. To open the **[Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel)** , click auto_awesome**Open or close Gemini Cloud Assist chat**.
  2. In the **Cloud Assist panel** , enter a prompt that describes the information that you're interested in.
  3. After you enter the prompt, click send **Send prompt**. 

Gemini returns a response to your prompt based on information from the last hour.




## Troubleshoot slow queries

To use AI assistance with troubleshooting your slow queries, go to the **Query insights** dashboard for your Cloud SQL instance in Google Cloud console.

### Top queries table

You can start troubleshooting slow queries with AI assistance in the **Top queries table** section of the **Query insights** dashboard.

Cloud SQL can help you identify which queries are performing slower than average during a specific detection time period. After you select a time range in the **Query insights** dashboard, Cloud SQL checks whether any queries are performing slower than average by using a detection time period of 24 hours before the end of your selected time range.

When you adjust the time range filter of the **Database load** chart, or any other filter such as database or user, Cloud SQL refreshes the **Top queries table** and reruns anomaly detection based on the new list of queries and an updated detection time period.

For Cloud SQL Enterprise Plus edition instances, the following occurs when Cloud SQL detects an anomaly: 

If a query is running slower than expected, then a **Warning** warning_spark icon is displayed. When you click either icon, [Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/investigations) is used to help analyze the query execution and offers observations about what might have caused any issue. Based on these observations, Gemini Cloud Assist generates a hypothesis that can help you address the issue.

To troubleshoot slow queries in the **Top queries** table in the **Query insights** dashboard, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the SQL navigation menu, click **Query insights**.
  4. In the **Executed queries** chart, use the **Time range** filter to select either 1 hour, 6 hours, 1 day, 7 days, 30 days or a custom range.
  5. In the **Top queries** table, under the **Queries** tab, review the list of queries for your database.
  6. If a **Warning** warning_spark icon appears next to the query's **Avg execution time (ms)** value for a query, then Cloud SQL has detected an anomaly in your query performance. Cloud SQL checks for anomalies within the 24-hour time period that occurs before the end of your selected time range.
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

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. Click **Query insights** to open the **Query insights** dashboard.
  4. In the **Query insights** dashboard, click the query in the **Top queries** that you want to view. The **Query details** page appears.
  5. >For Cloud SQL Enterprise Plus edition, if Cloud SQL detects an anomaly for the query, then one or more of the following indicators appears in the **Query details** page:
     * A message on the details screen that says `This query is slower than usual` and an **Investigate** option.
     * A message in the **Query latency** chart that says `Query slower than usual`. If this message appears, then click **Investigate** button to start troubleshooting with AI assistance from Gemini Cloud Assist.

After about two minutes, the **Investigation details** pane opens with the following sections:

       * **Issue**. A description of the issue being investigated, including the investigation’s start and stop time. 
       * **Observations**. A list of observations about the issue. For example, these can include lock contention details, such as a longer than expected lock wait ratio for the query.
       * **Hypotheses**. A list of AI-recommended actions to take to help address the slow running query.
  6. Optional: Use the **Time range filter** to select either 1 hour, 6 hours, 1 day, 7 days, 30 days or a custom range. When you adjust the **Time range filter** of the **Query details** page Cloud SQL reruns anomaly detection. While the **Time range filter** you choose applies to most results, the **Analysis time period** is always set to 48 hours.
  7. If Cloud SQL doesn't detect an anomaly for the query, then you can still run an analysis on the query by clicking the **Investigate** button in the **Query latency** card.



### Analyze query latency

Using AI assistance, you can analyze and troubleshoot the details of your query latency.

#### Analysis time period

The analysis time period consists of the 24 hours that occur before the end of the time range that you select in the **Database load** chart of the **Query insights** dashboard or the **Query details** page. Cloud SQL uses this time period to compare baseline metrics with the metrics retrieved during the time period of the anomaly.

On the **Query details** page, for Cloud SQL Enterprise Plus edition, if Cloud SQL has detected an anomaly with the query, then after you select the query from the **Query insights** dashboard, Cloud SQL performs a baseline performance analysis for the query using the last 24 hours from the end of the anomaly. If Cloud SQL hasn't detected an anomaly with the query and runs anomaly detection on the query again, then Cloud SQL uses 48 hours before the end of the selected time range as the performance baseline for the analysis time period.

#### Detected anomaly period

The detected anomaly period is applicable to Cloud SQL Enterprise Plus edition instances only. 

The detected anomaly period represents a time period when Cloud SQL finds an anomalous change in query performance. Cloud SQL uses the baseline performance measured for the query during the analysis time period.

If Cloud SQL detects multiple anomalies for a query within a selected time period, then Cloud SQL uses the last detected anomaly.

### Blocked active queries

**Preview —[Blocked active queries](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries#blocked-active-queries) **

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

If a specific active query is blocked or running much longer than expected, then it can block other dependent queries.

Cloud SQL gives you the option to terminate specific long-running or blocked active queries.

For more information, see [Blocked active queries](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries#blocked-active-queries).

### Examples of query performance prompts

You can also use Gemini Cloud Assist to enter prompts to help you improve the performance of your queries. Gemini Cloud Assist answers questions for the selected Cloud SQL instance and database.

Prompt | Type of response  
---|---  
What are the top queries by latency in my database?  | 

Summaries of queries sorted by latency. Gemini scopes the response by the time range filter selected in the query insights database load chart. 
  
What is the slowest query in this database instance?  | Guidance on how to identify the slowest query by latency.   
  
## Troubleshoot high database load

By accessing the **Query insights** dashboard in the Google Cloud console, you can analyze your database and troubleshoot events when your system experiences a higher database load than average. Cloud SQL uses the 24 hours of data that occurs prior to your selected time range to calculate the expected load of your database. You can look into the reasons for the higher load events and analyze the evidence behind reduced performance. Cloud SQL also provides recommendations for optimizing your database to improve performance.

To use AI assistance with troubleshooting high database load, go to the **Instance Overview** page or the **Query insights** dashboard in the Google Cloud console.

### Instance overview page

Troubleshoot high database load with AI assistance in the **Instance overview** page by using the following steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
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

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
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

Cloud SQL analyzes your database for the time period that you select in your database load chart from the **Query insights** dashboard or the **Instance overview** page. If you select a time period of less than 24 hours, then Cloud SQL analyzes the entire time period. If you select a time period greater than 24 hours, then Cloud SQL selects only the last 24 hours of the time period for analysis.

To calculate the baseline performance analysis of your database, Cloud SQL includes 24 hours of a baseline time period in its analysis time period. If your selected time period occurs on a day other than Monday, then Cloud SQL uses a baseline time period of the _24 hours previous_ to your selected time period. If your selected time period occurs on a Monday, then Cloud SQL uses a baseline time period of the _7th day previous_ to your selected time period.

#### Metrics analysis

When Cloud SQL starts the analysis, Cloud SQL checks for significant changes in the various metrics, including but not limited to the following:

  * Queries per second (QPS)
  * CPU
  * Memory
  * Disk I/O 



Cloud SQL compares the baseline aggregated data for your database within the performance data of your analysis time window. If Cloud SQL detects a significant change in threshold for a key metric, then Cloud SQL indicates a possible situation with your database. The identified situation might explain a root cause for the high load on your database over the selected time period.

#### Recommendations

When Gemini Cloud Assist completes analysis, the **Hypotheses** section of the **Investigation details** pane lists actionable insights to help remediate the issue.

For some situations, based on the analysis, there might not be a recommendation.

### Examples of system performance prompts

You can also use Gemini Cloud Assist to enter prompts to gather information about your system performance. Gemini Cloud Assist answers questions for the selected Cloud SQL instance.

Prompt | Type of response  
---|---  
How many error log entries are there for this database instance in the last 7 days?  | 

  * Summary of log entries grouped by their severity type. Gemini scopes the response by the time range filter selected in the instance performance chart.
  * Guidance on how to identify and sort queries by latency.

  
What was the CPU utilization for this database instance around 2 PM today?  |  Metrics results in percentage range for CPU utilization within the time interval.   
  
## Troubleshoot connectivity issues

You can start troubleshooting connectivity issues by using Gemini Cloud Assist or by initiating an investigation when connection errors occur. AI assistance evaluates several sources to identify why a client might encounter issues when trying to connect to a Cloud SQL database.

### Investigate connectivity issues

To use AI assistance with troubleshooting connectivity issues, do the following:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. To open the **Overview** page of an instance, click the instance name. 
  3. In the **Resolve database issues with AI-assisted troubleshooting** pane, click **Explore investigations**.
  4. In the **Investigation options** window, look for the **Connection usage** section.
  5. Optional: Select a specific analysis time period using the **Time range** filter, either 1 hour, 6 hours, 1 day, 7 days, or a custom range.
  6. Click **Investigate**. 

Gemini initiates an automated analysis of your instance metadata, logs, and networking configuration. After the analysis is complete, the **Investigation details** pane displays the following sections:

     * **Issue** : A summary of the connectivity failure, including affected resources and timestamps.
     * **Observations** : Evidence gathered from signals such as when a database has reached its `max_connections` limit or active concurrent connections cross-referenced with instance metadata. Evidence can be used to determine whether a traffic spike or unclosed sessions might be the cause of instance downtime.
     * **Hypotheses** : AI-generated root causes and remediation steps.



### Examples of connectivity issue prompts

You can also use Gemini Cloud Assist to troubleshoot connectivity issues between a client and your Cloud SQL instance.

Prompt | Type of response  
---|---  
Why am I seeing connection errors?  |  Gemini evaluates connections to your database and recommends improvements such as enabling managed connection pooling.   
  
## Get index recommendations

**Note:** You don't need to enable AI-assisted troubleshooting to obtain index recommendations.

You can obtain index recommendations from Cloud SQL in query insights. For more information about obtaining index recommendations, see [Use index advisor](https://docs.cloud.google.com/sql/docs/sqlserver/use-index-advisor). 

### Examples of index recommendation prompts

Use Gemini Cloud Assist to get more information about how to use indexes in your databases. Gemini Cloud Assist answers questions for the selected Cloud SQL instance.

Prompt | Type of response  
---|---  
Show index recommendations for queries run in the last 7 days.  | Guidance on the types of queries that can benefit from an index.   
  
## Monitor active queries

**Note:** You don't need to enable AI-assisted troubleshooting to monitor active queries.

Use the **Query insights** dashboard to monitor active queries, and if necessary, terminate long-running processes. For more information, see [Monitor active queries](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries). 

### Examples of active query prompts

Use Gemini Cloud Assist to find out more information about queries that cause high latency or CPU load. Gemini Cloud Assist answers questions for the selected Cloud SQL instance.

Prompt | Type of response  
---|---  
What are the top queries currently running in my database?  |  Guidance on how to find the longest running and most resource-intensive queries.   
  
## What's next

  * Learn how to [write better prompts](https://docs.cloud.google.com/gemini/docs/discover/write-prompts).
  * Learn how to use the [Gemini Cloud Assist panel](https://docs.cloud.google.com/cloud-assist/chat-panel).
  * Read [Use Gemini for AI assistance and development](https://docs.cloud.google.com/gemini/docs/overview)
  * Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

  * [Optimize high CPU usage](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-cpu-usage)
  * [Optimize high memory usage](https://docs.cloud.google.com/sql/docs/sqlserver/optimize-high-memory-usage)
  * [Use system insights to improve system performance](https://docs.cloud.google.com/sql/docs/sqlserver/use-system-insights)
  * [Use index advisor](https://docs.cloud.google.com/sql/docs/sqlserver/use-index-advisor)
  * [Monitor active queries](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-active-queries)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
