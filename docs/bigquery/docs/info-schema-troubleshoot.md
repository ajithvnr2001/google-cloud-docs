---
url: https://docs.cloud.google.com/bigquery/docs/info-schema-troubleshoot/
title: Troubleshoot with information schema \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:56.104901+00:00
---

# Troubleshoot with information schema  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/info-schema-troubleshoot/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Guides ](https://docs.cloud.google.com/bigquery/docs/introduction)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Troubleshoot with information schema

As a BigQuery administrator or data analyst, managing enterprise workloads requires a reliable, scalable way to diagnose performance bottlenecks, query failures, capacity limits, and storage growth. BigQuery information schema views serve as an observability foundation, providing near real-time and historical metadata accessible through standard GoogleSQL queries.

This document outlines the core principles of troubleshooting BigQuery using information schema, provides a structured overview of the administrative troubleshooting toolbox, and directs you to specific views in the BigQuery library.

## Information schema troubleshooting by task

The following table summarizes useful information schema views categorized by task and diagnostic use case:

Task | Use cases | Information schema views  
---|---|---  
**Query performance and errors** | 

  * Identify top slot-consuming and expensive queries.
  * Aggregate job error reasons and failure patterns.
  * Analyze per-stage execution times and spilled bytes.

| 

  * [`JOBS_BY_PROJECT`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs)
  * [`JOBS_BY_ORGANIZATION`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-by-organization)
  * [`JOBS_BY_FOLDER`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-by-folder)
  * [`JOBS_BY_USER`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-by-user)

  
**Workload capacity and contention** | 

  * Detect slot contention, throttling, and queue times.
  * Monitor in-memory shuffle memory saturation.
  * Audit reservation baseline and autoscaling slot usage.
  * Verify project and folder reservation assignments.

| 

  * [`JOBS_TIMELINE_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-timeline)
  * [`RESERVATIONS_TIMELINE_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-reservation-timeline)
  * [`RESERVATIONS_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-reservations)
  * [`ASSIGNMENTS_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-assignments)
  * [`CAPACITY_COMMITMENTS_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-capacity-commitments)

  
**Storage costs and data architecture** | 

  * Identify tables with runaway physical or logical storage.
  * Detect time-travel and fail-safe storage bloat.
  * Diagnose partition skew and tables nearing partition limits.
  * Discover expired or deleted tables in time-travel windows.

| 

  * [`TABLE_STORAGE_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-table-storage)
  * [`PARTITIONS`](https://docs.cloud.google.com/bigquery/docs/information-schema-partitions)
  * [`TABLES`](https://docs.cloud.google.com/bigquery/docs/information-schema-tables)
  * [`TABLE_OPTIONS`](https://docs.cloud.google.com/bigquery/docs/information-schema-table-options)

  
**Access control and governance** | 

  * Audit explicit Identity and Access Management (IAM) role grants on tables and datasets.
  * Troubleshoot access denied errors for users and service accounts.
  * Track cross-project dataset sharing and analytical usage.

| 

  * [`OBJECT_PRIVILEGES`](https://docs.cloud.google.com/bigquery/docs/information-schema-object-privileges)
  * [`SHARED_DATASET_USAGE`](https://docs.cloud.google.com/bigquery/docs/information-schema-shared-dataset-usage)

  
**Data ingestion pipelines** | 

  * Monitor Storage Write API ingestion throughput and errors.
  * Diagnose streaming insert latency and rate limits.
  * Identify failing streams by stream type and error code.

| 

  * [`WRITE_API_TIMELINE_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-write-api)
  * [`STREAMING_TIMELINE_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-streaming)

  
**Machine learning and vector search** | 

  * Track model training duration and resource consumption.
  * Audit vector index build status and coverage percentage.
  * Troubleshoot stored procedure and Python UDF builds.

| 

  * [`VECTOR_INDEXES`](https://docs.cloud.google.com/bigquery/docs/information-schema-vector-indexes)
  * [`ROUTINES`](https://docs.cloud.google.com/bigquery/docs/information-schema-routines)
  * [`JOBS_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs) (filter on ML statement types)

  
**Workload optimization insights** | 

  * Review automated partitioning and clustering recommendations.
  * Identify materialized view candidate tables.

| 

  * [`RECOMMENDATIONS_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-recommendations)
  * [`INSIGHTS_BY_*`](https://docs.cloud.google.com/bigquery/docs/information-schema-insights)

  
  
## Principles of troubleshooting with information schema

When you diagnose workload or environment issues in BigQuery, apply the following core principles:

  * **Scope by region, dataset, and project.** BigQuery workload management and compute resources execute within regional boundaries. Consider the following:

    * Always specify the correct regional qualifier (for example, `region-REGION.INFORMATION_SCHEMA.JOBS_BY_PROJECT`) or dataset qualifier.

    * Choose the appropriate hierarchy level ([`BY_PROJECT`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs), [`BY_USER`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-by-user), [`BY_FOLDER`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-by-folder), or [`BY_ORGANIZATION`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-by-organization)) based on whether you are investigating a single user issue, a project-specific workload, or a tenant-wide issue.

  * **Correlate compute demand with capacity.** Slow query performance is often the result of slot contention rather than inefficient SQL alone. Compare job resource requests (`period_estimated_runnable_units`) against allocated reservation slots (`period_slot_ms`) over identical time windows to distinguish between query tuning opportunities and issues caused by insufficient capacity.

  * **Account for telemetry granularity and retention boundaries.** Different information schema views operate on distinct refresh intervals and data retention windows. Job metadata in the `JOBS` view is available for 180 days, whereas high-resolution timeline metrics in the [`JOBS_TIMELINE`](https://docs.cloud.google.com/bigquery/docs/information-schema-jobs-timeline) and [`RESERVATIONS_TIMELINE`](https://docs.cloud.google.com/bigquery/docs/information-schema-reservation-timeline) views are retained for shorter periods (typically 14 to 30 days). For long-term audit and trend analysis, you should export telemetry to partitioned tables.

  * **Avoid metric distortion in multi-statement queries.** Multi-statement scripts (procedural SQL containing `DECLARE`, `IF`, or `WHILE`) generate a parent job with `statement_type = 'SCRIPT'` and individual child jobs for each statement. When aggregating metrics such as `total_slot_ms` or `total_bytes_billed`, filter out `statement_type = 'SCRIPT'` to prevent double-counting.

  * **Filter on partition columns.** To minimize query execution time and avoid unnecessary scan costs on on-demand analysis, always include restrictive time filters on partition columns such as `creation_time`, `job_start_time`, or `period_start`.




## What's next

  * For more information about information schema syntax and a list of available views, see [Introduction to INFORMATION_SCHEMA](https://docs.cloud.google.com/bigquery/docs/information-schema-intro).
  * To learn how to view job details, list active jobs, and cancel running jobs, see [Manage jobs](https://docs.cloud.google.com/bigquery/docs/managing-jobs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
