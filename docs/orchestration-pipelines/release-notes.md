---
url: https://docs.cloud.google.com/orchestration-pipelines/release-notes/
title: Orchestration Pipelines release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T04:13:10.367684+00:00
---

# Orchestration Pipelines release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/orchestration-pipelines/release-notes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Orchestration Pipelines ](https://docs.cloud.google.com/orchestration-pipelines)
  * [ Resources ](https://docs.cloud.google.com/orchestration-pipelines/resources)



Send feedback 

#  Orchestration Pipelines release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to Orchestration Pipelines. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## August 28, 2026

Feature

Orchestration Pipelines are now **generally available (GA)**.

## August 24, 2026

Feature

Release of orchestration-pipelines package version **v1.0.0**.

Feature

In the Google Cloud console, the Orchestration Pipelines tab now displays pipeline statuses and execution history for the runner environment.

Feature

Added observability metrics:

  * Observability metrics for pipeline runs via DAG callbacks (success/failure counters).
  * Observability metrics for action execution using a custom operator.
  * Observability metrics for internal pipeline metadata population.



Fixed

Placeholder DAG indicating parsing errors now fails by default with an `AirflowFailException` showing the parsing error message.

Fixed

Actions running on Dataproc Ephemeral Cluster as engine are now properly marked as success/failed based on the job status, abstracting the cleanup step result.

## August 18, 2026

Feature

Release of orchestration-pipelines package version **v0.4.1**.

Fixed

Serialization compatibility with Airflow 3.2+.

## August 12, 2026

Feature

Release of orchestration-pipelines package version **v0.4.0**.

Feature

Added support for `.yaml` extension for pipeline definition files in addition to `.yml`.

Feature

Added `doc_md` documentation generation for unversioned pipeline workflows.

Feature

Source pipeline definition file path is now included in DAG `doc_md` metadata.

Feature

Added support for Agent Platform upload model in `AIAction`.

Feature

Added support for triggering batch inference on Agent Platform in `AIAction`.

Feature

Emiting metrics with respect to count and duration of parsing pipeline.

Change

Migrated local Dataform file staging command from `gsutil` to `gcloud storage`.

Fixed

Added detection of circular dependencies between actions during pipeline validation.

Fixed

Fixed path resolution in `FileManager` for non-versioned pipelines.

Fixed

Fixed `dag_id` verification check in `globals()`.

## July 08, 2026

Feature

Release of orchestration-pipelines package version **v0.3.0**.

Feature

Params support for SQL, Pyspark and Notebook actions.

Feature

Params support for DBT pipeline and Dataform pipeline local (on Airflow) executions.

Feature

Support for custom labels in Dataproc, SQL, and Dataform local execution.

Feature

Inline requirements support for Notebook/PySpark run on Dataproc.

Feature

Support for trigger rules in all actions.

Feature

New action supporting triggering another orchestration pipeline.

Change

Replaced `runtime_params` from BigQuery DTS action with two specific fields: `requested_run_time` and `requested_time_range`.

Fixed

Improved error messages for datetime/cron/duration/timezone validation.

Fixed

Adjusted examples to comply with validation rules.

## May 15, 2026

Feature

Release of orchestration-pipelines package version **v0.2.0**.

Feature

Added an action for triggering existing BigQuery DTS configuration.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
