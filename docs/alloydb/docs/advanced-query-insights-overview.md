---
url: https://docs.cloud.google.com/alloydb/docs/advanced-query-insights-overview/
title: Advanced query insights features overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:08:33.673124+00:00
---

# Advanced query insights features overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/advanced-query-insights-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Advanced query insights features overview Stay organized with collections  Save and categorize content based on your preferences. 

To detect, troubleshoot, and prevent database and query performance problems in near real time, you can use advanced query insights features in AlloyDB for PostgreSQL. These features provide enhanced query performance diagnostics in addition to all capabilities included in [standard query insights](https://docs.cloud.google.com/alloydb/docs/query-insights-overview). For information about setting up and using these features, see [Improve query performance using advanced query insights features](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights).

Based on the previous 30 days of query insights data, you can monitor query performance at the application level and trace the source of problematic queries across the application stack by action, controller, framework, route, application, and database driver. Advanced query insights features capture query plans for all queries and sample up to 20 query plans per minute by default. You can configure this sampling rate to capture up to 200 query plans per minute.

To help you proactively identify and troubleshoot root causes of query performance issues, advanced query insights features let you do the following:

  * Perform ad hoc analysis to diagnose difficult problems using near real-time query stats and correlation analysis across multiple dimensions like users, hosts, and databases.
  * View your query execution plan using complete SQL statements, along with accompanying comments. You can opt in to view comments associated with a query, where applicable.
  * Troubleshoot complex performance issues by analyzing telemetry, like wait events. A _wait event_ is a component that causes a delay in processing a query-related operation. Wait event metrics, enabled by default, help you diagnose and debug performance issues for long-running queries and their associated wait times.
  * View [index advisor recommendations](https://docs.cloud.google.com/alloydb/docs/use-index-advisor-with-query-insights) about creating indexes.
  * Configure your query insight settings. For example, you can customize query lengths, enable wait event analysis, and store query comments and application tags. You can access historical and near real-time data.
  * Analyze data for up to a 30-day period for a long term performance view.



## Benefits of advanced query insights features

The following advanced query insights features are available to help you detect and fix query performance problems:

  * Prebuilt dashboards that help you identify query performance problems early and let you identify, diagnose, and resolve issues in a single page on the Google Cloud console.
  * Visual query plans that help you identify root causes and troubleshoot issues. You can trace the source of a problematic query with in-context, end-to-end application tracing.
  * Insights based on Google Cloud's enterprise security, privacy and compliance offerings, which might reduce operational overhead.
  * Application-centric monitoring and simplified performance diagnosis of applications built using object relational mappers (ORM). You can monitor database performance with an application-centric view by tagging queries with business logic. [Sqlcommenter](https://google.github.io/sqlcommenter/spec/), an open source library, auto-instruments your ORMs to help identify the application code causing performance problems.



## How advanced query insights features work

Advanced query insights features are fully managed, which means you don't need to install or actively manage the feature.

Advanced query insights features load an extension that records query metrics and execution plans that are implemented using hooks. The metrics are stored in AlloyDB tables, and normalized execution plans are stored in [Cloud Trace](https://docs.cloud.google.com/trace/docs).

You can access these metrics in the AlloyDB Query Insights page of the Google Cloud console. Metrics are expected to be available in advanced query insights features within 30 seconds of query completion. Metrics are encrypted at rest in the same way as database storage.

Advanced query insights features store and display only normalized queries. All the constant values from the query string are removed. Query comments are preserved only on demand, it is an opt-in feature. Query plan traces don't collect and store constant values.

### Storage

Advanced query insights features store and display only normalized queries. All the constant values from the query string are removed. Query plan traces don't collect and store any constant values. By default, advanced query insights features don't collect tags information. If enabled at a later stage, they can be disabled from advanced query insights features per instance setting.

The **Query insights** dashboard provides 30 days of data. The storage requirement for 30 days' worth of data is approximately 180 GB for a primary instance (up to 700 GB maximum for a cluster). Advanced query insights features use up to 10 MB of RAM (shared memory). Metrics are expected to be available in insights within 30 seconds of query completion. In addition, standard query insights metrics are available in system metrics in Cloud Monitoring to keep the functionalities of the standard query insights intact. For more information about the Cloud Monitoring system metrics retention policy, see [Data retention](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

Traces from advanced query insights features are stored in Cloud Trace and have a 30-day retention period. For more information about the Cloud Trace data retention policy, see [Quotas and limits](https://docs.cloud.google.com/trace/docs/quotas).

## Limitations

  * The metrics exposed by advanced query insights features aren't available using the Cloud Monitoring API.
  * Client IP address support is in [Preview](https://cloud.google.com/products#product-launch-stages) and can only be configured using `gcloud beta`, Terraform, or the `v1beta` REST API.
  * You cannot enable advanced query insights features on secondary clusters.
  * AlloyDB stores query insights data for its primary and read pool instances for 30 days. Storing data for primary instances consumes about 180 GB and might increase based on the number of read pool nodes present in the cluster. The maximum consumed storage size is 700 GB.
  * You must [enable advanced query insights features](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights#enable-advanced-features) on a primary instance before enabling them on a read pool instance.
  * The query insights dashboard resets after you enable advanced query insights features. However, you can still access the standard query insights metrics using the [Metrics Explorer](https://docs.cloud.google.com/monitoring/charts/metrics-explorer).



## What's next

  * [Improve query performance using query insights](https://docs.cloud.google.com/alloydb/docs/using-advanced-query-insights).
  * Learn about [AlloyDB metrics](https://docs.cloud.google.com/monitoring/api/metrics_gcp_a_b#gcp-alloydb).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-23 UTC."],[],[]] 
