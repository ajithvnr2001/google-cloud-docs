---
url: https://docs.cloud.google.com/sql/docs/postgres/observability/
title: About database observability \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:48.743987+00:00
---

# About database observability  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  About database observability Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/observability "View this page for the MySQL database engine") | PostgreSQL | [SQL Server](https://docs.cloud.google.com/sql/docs/sqlserver/observability "View this page for the SQL Server database engine")

Database observability is a measure of how accurately you can infer the internal state of a database system based on the data, or telemetry, that it generates in logs, metrics, and traces.

Diagnosing and troubleshooting issues in an application can be particularly difficult and time-consuming when a database is involved. Telemetry collection is crucially important. Telemetry, when enriched with application context, can make database instances more understandable, observable, and easier to maintain. You can identify issues and problematic trends easily and remedy them early, without having to incur costly downtime. Moreover, by using such data, you can configure newer database instances to collect the right kind of data from the moment they start.

You can use data effectively and proactively to prevent issues and focus on strategic innovation. Good telemetry collection is particularly useful in the [DevOps model](https://cloud.google.com/devops), where database generalists need to independently analyze telemetry to monitor, evaluate, and optimize the performance and health of their rapidly evolving applications.

Google Cloud offers several powerful features spanning the four iterative observability stages to help you maintain the health of your Cloud SQL database.

![The iterative stages of implementing observability](https://docs.cloud.google.com/sql/images/observe1x.png)

## Automated telemetry collection

To achieve observability goals, we start by collecting telemetry, preferably through an automated process. When collected over a period, telemetry helps establish a baseline for metrics under different load conditions.

Google Cloud services automatically generate observability data, including metrics, logs, and traces, which can help provide a complete observability overview.

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) collects measurements of your service and of the Google Cloud resources that you use. Cloud SQL uses built-in memory custom agents to collect query telemetry, resulting in a lower impact on performance and eliminating the need for agent maintenance or security overhead.

  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) collects logging data from common application components. For Cloud SQL, see also [View instance logs](https://docs.cloud.google.com/sql/docs/postgres/logging).

  * [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) collects latency data and executed query plans from applications to help you track how requests propagate through your application. You can compare these latency distributions over time or across versions. Cloud Trace alerts you when it detects a significant shift in the latency profile of your application when it's instrumented to use Cloud Trace.




[Sqlcommenter](https://google.github.io/sqlcommenter/spec/), an [OpenTelemetry](https://cloud.google.com/learn/what-is-opentelemetry) library for databases helps you monitor your databases through the lens of an application. Sqlcommenter automatically instruments ORMs to augment SQL statements with tags and allows OpenTelemetry trace context information to be propagated to the database.

With tags and trace application context in databases, it's easy to correlate application code with database performance and troubleshoot microservices-based architectures.

## Database monitoring

Proper monitoring helps you determine whether your application is working optimally. Implement monitoring early, such as before you initiate a migration or deploy a new application to a production environment. Disambiguate between application issues and underlying cloud issues.

The [Cloud SQL System Insights dashboard](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights) considers several important signals of overall database health and performance.

The dashboard shows graphs for several important metrics, which help you gain insights into issues, such as throughput, latency, and cost. These insights help you respond proactively as your application needs change. You can compare current performance against past trends and identify anomalies that might need investigation.

The Cloud SQL [Overview page](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance#monitoring-overview) shows graphs for some of the key metrics.

Cloud SQL also helps you [compare metrics](https://docs.cloud.google.com/sql/docs/postgres/monitor-instance#monitoring-multiple) for selected instances.

You can use Cloud Monitoring to create [custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) that help you monitor metrics and to [set up alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#viewing_policies) so that you can receive timely notifications.

## Database and query analysis

The Cloud SQL [Query Insights](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights) tool provides monitoring and diagnostics that let you detect and fix query performance problems.

Query Insights dashboards help you identify query performance problems early and let you move from detection to resolution by using a single interface. Built-in, visual query plans assist you in troubleshooting issues to find the root cause. You can also use in-context, end-to-end application tracing to find the source of a problematic query.

Query Insights provides application-centric monitoring that helps you diagnose performance problems for applications built using object-relational mappings (ORMs). You can tag queries with business logic that the query is associated with, such as payment, inventory, business analytics, or shipping. Query Insights can integrate with your existing APM tools, letting you monitor and troubleshoot query problems using your favorite tool.

The Query Insights tool uses [sqlcommenter](https://google.github.io/sqlcommenter/spec/) to automatically instrument your ORMs. This instrumentation helps you identify the application code that's causing problems. Query Insights supports [OpenTelemetry](https://opentelemetry.io/) standards and makes the query metrics and traces data available for your APM tools through the [Google Cloud Observability](https://cloud.google.com/products/operations) API.

Query Insights integrates with [Cloud Monitoring](https://cloud.google.com/monitoring), letting you create custom dashboards and alerts on query metrics or tags and receive notifications using email, SMS, Slack, PagerDuty, and more.

## Database tuning

You can iteratively [troubleshoot and tune](https://docs.cloud.google.com/sql/docs/postgres/best-practices#tuning-monitoring) your database.

Cloud SQL recommenders help you analyze the current usage of your database and provide [recommendations](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations) and [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights#insights) based on heuristic methods and machine learning.

Cloud SQL recommenders are briefly described as follows:

Name | Description  
---|---  
[Out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender) | Reduce the risk of downtime that might be caused by your Cloud SQL instances running out of disk space.  
[Idle instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle) | Reduce costs by shutting down Cloud SQL instances that are inadvertently idle.  
[Overprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned) | Reduce costs by resizing Cloud SQL instances that are unnecessarily large for a given workload.  
[Underprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-underprovisioned) | Avoid bottlenecks from high CPU and memory usage and minimize the likelihood of out-of-memory events by resizing Cloud SQL instances that have high CPU and/or memory usage.  
[High transaction ID utilization recommender](https://docs.cloud.google.com/sql/docs/postgres/recommender-high-transactionid-utilization) | Optimize the performance of your instance by avoiding potential transaction ID wraparound for Cloud SQL for PostgreSQL instances.  
  
## What's next

  * View the list of [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/postgres/admin-api/metrics). 
  * [Use Query Insights to improve query performance](https://docs.cloud.google.com/sql/docs/postgres/using-query-insights).
  * [Use System Insights to improve instance performance](https://docs.cloud.google.com/sql/docs/postgres/use-system-insights).
  * View the video: [Introducing Cloud SQL insights](https://www.youtube.com/watch?v=qN7x3ngwz1o).
  * Read the launch blog: [Database observability for developers: introducing Cloud SQL insights](https://cloud.google.com/blog/products/databases/get-ahead-of-database-performance-issues-with-cloud-sql-insights).
  * Read the blog: [Boost your query performance troubleshooting skills with Cloud SQL Insights](https://cloud.google.com/blog/topics/developers-practitioners/boost-your-query-performance-troubleshooting-skills-cloud-sql-insights).
  * Read the blog: [Enable query tagging with Sqlcommenter](https://cloud.google.com/blog/topics/developers-practitioners/enable-query-tagging-sqlcommenter-understand-application-impact-database-performance). 
  * Learn more about [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). See also [View instance logs](https://docs.cloud.google.com/sql/docs/postgres/logging).
  * [Troubleshoot and tune](https://docs.cloud.google.com/sql/docs/postgres/best-practices#tuning-monitoring) your database instance.
  * Learn more about [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
