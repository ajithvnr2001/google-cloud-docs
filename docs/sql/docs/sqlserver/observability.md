---
url: https://docs.cloud.google.com/sql/docs/sqlserver/observability/
title: About database observability \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:36.379728+00:00
---

# About database observability  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  About database observability Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/observability "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/observability "View this page for the PostgreSQL database engine") | SQL Server

Database observability is a measure of how accurately you can infer the internal state of a database system based on the data, or telemetry, that it generates in logs, metrics, and traces.

Diagnosing and troubleshooting issues in an application can be particularly difficult and time-consuming when a database is involved. Telemetry collection is crucially important. Telemetry, when enriched with application context, can make database instances more understandable, observable, and easier to maintain. You can identify issues and problematic trends easily and remedy them early, without having to incur costly downtime. Moreover, by using such data, you can configure newer database instances to collect the right kind of data from the moment they start.

You can use data effectively and proactively to prevent issues and focus on strategic innovation. Good telemetry collection is particularly useful in the [DevOps model](https://cloud.google.com/devops), where database generalists need to independently analyze telemetry to monitor, evaluate, and optimize the performance and health of their rapidly evolving applications.

Google Cloud offers several powerful features spanning the four iterative observability stages to help you maintain the health of your Cloud SQL database.

![The iterative stages of implementing observability](https://docs.cloud.google.com/sql/images/observe1x.png)

## Automated telemetry collection

To achieve observability goals, we start by collecting telemetry, preferably through an automated process. When collected over a period, telemetry helps establish a baseline for metrics under different load conditions.

Google Cloud services automatically generate observability data, including metrics, logs, and traces, which can help provide a complete observability overview.

  * [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview) collects measurements of your service and of the Google Cloud resources that you use. Cloud SQL uses built-in memory custom agents to collect query telemetry, resulting in a lower impact on performance and eliminating the need for agent maintenance or security overhead.

  * [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) collects logging data from common application components. For Cloud SQL, see also [View instance logs](https://docs.cloud.google.com/sql/docs/sqlserver/logging).

  * [Cloud Trace](https://docs.cloud.google.com/trace/docs/overview) collects latency data and executed query plans from applications to help you track how requests propagate through your application. You can compare these latency distributions over time or across versions. Cloud Trace alerts you when it detects a significant shift in the latency profile of your application when it's instrumented to use Cloud Trace.




[Sqlcommenter](https://google.github.io/sqlcommenter/spec/), an [OpenTelemetry](https://cloud.google.com/learn/what-is-opentelemetry) library for databases helps you monitor your databases through the lens of an application. Sqlcommenter automatically instruments ORMs to augment SQL statements with tags and allows OpenTelemetry trace context information to be propagated to the database.

With tags and trace application context in databases, it's easy to correlate application code with database performance and troubleshoot microservices-based architectures.

## Database monitoring

Proper monitoring helps you determine whether your application is working optimally. Implement monitoring early, such as before you initiate a migration or deploy a new application to a production environment. Disambiguate between application issues and underlying cloud issues.

The Cloud SQL [Overview page](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance#monitoring-overview) shows graphs for some of the key metrics.

Cloud SQL also helps you [compare metrics](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance#monitoring-multiple) for selected instances.

You can use Cloud Monitoring to create [custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards) that help you monitor metrics and to [set up alert policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#viewing_policies) so that you can receive timely notifications.

## Database tuning

You can iteratively [troubleshoot and tune](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices#tuning-monitoring) your database.

Cloud SQL recommenders help you analyze the current usage of your database and provide [recommendations](https://docs.cloud.google.com/recommender/docs/key-concepts#recommendations) and [insights](https://docs.cloud.google.com/recommender/docs/insights/using-insights#insights) based on heuristic methods and machine learning.

Cloud SQL recommenders are briefly described as follows:

Name | Description  
---|---  
[Out-of-disk recommender](https://docs.cloud.google.com/sql/docs/mysql/using-ood-recommender) | Reduce the risk of downtime that might be caused by your Cloud SQL instances running out of disk space.  
[Idle instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-idle) | Reduce costs by shutting down Cloud SQL instances that are inadvertently idle.  
[Overprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-sql-overprovisioned) | Reduce costs by resizing Cloud SQL instances that are unnecessarily large for a given workload.  
[Underprovisioned instance recommender](https://docs.cloud.google.com/sql/docs/mysql/recommender-underprovisioned) | Avoid bottlenecks from high CPU and memory usage and minimize the likelihood of out-of-memory events by resizing Cloud SQL instances that have high CPU and/or memory usage.  
  
## What's next

  * View the list of [Cloud SQL metrics](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/metrics). 
  * Learn more about [Cloud Logging](https://docs.cloud.google.com/logging/docs/overview) and [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview). See also [View instance logs](https://docs.cloud.google.com/sql/docs/sqlserver/logging).
  * [Troubleshoot and tune](https://docs.cloud.google.com/sql/docs/sqlserver/best-practices#tuning-monitoring) your database instance.
  * Learn more about [Google Cloud recommenders](https://docs.cloud.google.com/recommender/docs/overview).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
