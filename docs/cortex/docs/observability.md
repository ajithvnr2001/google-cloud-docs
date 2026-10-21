---
url: https://docs.cloud.google.com/cortex/docs/observability/
title: Cortex Framework Observability \u00a0|\u00a0 Google Cloud Cortex Framework \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:36:58.639395+00:00
---

# Cortex Framework Observability  |  Google Cloud Cortex Framework  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cortex/docs/observability/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Google Cloud Cortex Framework ](https://docs.cloud.google.com/cortex/docs)
  * [ Version 7 Guides ](https://docs.cloud.google.com/cortex/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Cortex Framework Observability

To successfully run and operate enterprise-grade data platforms, having visibility into pipeline execution, data quality, and operational errors is critical. 

Cortex Framework categorizes observability across its two distinct life cycles:

  1. **Deploy-Time Observability** : Tracking configuration load, template compilation, validation checks, deployment actions, and API telemetry during the execution of CLI tools.
  2. **Run-Time Observability** : Tracking execution, pipeline progress, query performance, data quality assertions, and automated alerting for the deployed data pipelines running inside Google Cloud.



* * *

## Deploy-Time Observability

Deploy-time observability focuses on the execution of the CLI tools (e.g., `uv run cortex-build`, `uv run cortex-deploy`, `uv run cortex-build-and-deploy`, `uv run cortex-demo`, `uv run cortex-kc-sync`).

### Local Console Logging

When you run CLI commands, Cortex Framework logs progress directly to the console (`stdout`). 

  * **Log Level** : By default, logs are output at the `INFO` level.
  * **Visual Highlights** : Messages are color-coded to highlight errors and warnings dynamically: 
    * ❌ **Errors** (Red) indicating critical failures that halt execution.
    * ⚠️ **Warnings** (Orange) indicating potential configuration anomalies or non-blocking issues.
  * **Timestamp and Source** : Every log line displays execution time and the active Python class or module names for precise tracing.



### Persistent Local Log Files

On every command execution, the Python orchestrator automatically streams the complete execution log to a temporary log file in your system's temp directory:
    
    
    /tmp/cortex-framework-logs-<YYYYMMDD-HHMM>.log
    

The precise path is printed to the console during startup of the CLI tools. These files contain comprehensive log details (including stack traces for unexpected errors) and are invaluable for debugging issues encountered during the execution of the CLI tools or when you are attaching to support requests.

### Google Cloud Environment Validation

Prior to performing build, deploy, or sync actions, the orchestration engine executes the `GcpEnvironmentChecker` utility. This check validates:

  1. **Required APIs** : Confirms that crucial Google Cloud APIs are enabled (e.g. `bigquery.googleapis.com`, `dataform.googleapis.com`).
  2. **Dataset Existence** : Verifies that the required raw and target datasets exist or can be created.
  3. **Locations & Regions**: Ensures target datasets match the geographical regions of the source datasets.
  4. **Capacity and Settings** : Validates reservation settings and catalog configurations.



Any mismatch is logged as an error with recommended hints on how to resolve them before making Google Cloud service calls.

### Telemetry

During deployment and synchronization processes, Cortex Framework logs anonymous adoption, variant, and framework version telemetry to Google Cloud. For details on how this works and instructions on how to opt out, see [Telemetry](https://docs.cloud.google.com/cortex/docs/telemetry).

* * *

## Run-Time Observability

Once built and deployed, the Cortex Framework conformed data layers and data products run entirely within **Dataform** and **BigQuery**. As a result, runtime observability integrates directly with Google Cloud operational suites.

### Pipeline Execution Logging

All deployed pipelines are tracked using [**Cloud Logging**](https://docs.cloud.google.com/logging/docs) and execution tools:

  * **Dataform Execution Logs** : Dataform logs every compilation and execution event. These details can be accessed in the Google Cloud console or programmatically using the [Dataform API](https://docs.cloud.google.com/dataform/docs/reference/rest).
  * **BigQuery Job History** : Each table and view materialized by your Dataform pipelines executes SQL queries inside BigQuery. Detailed resource usage, query performance, processed bytes, and execution timestamps are logged in the [BigQuery Job History](https://docs.cloud.google.com/bigquery/docs/managing-jobs#view_job_details).



### Pipeline Monitoring

You can monitor pipeline health, release configurations, and run history visually or programmatically:

  1. **Dataform Web UI** : Navigate to the [Dataform console](https://console.cloud.google.com/bigquery/dataform) to: 
     * Inspect compiled data models and visualize the compiled graph.
     * Verify the status of release configurations, compiled templates, and active environments.
     * Monitor the history and details of current and past workflow executions.
  2. **[Cloud Monitoring integration](https://docs.cloud.google.com/monitoring/docs)** : Track Dataform pipeline metrics, such as execution durations, active compilations, and workflow job failure rates, through custom dashboard panels.



### Alerting & Data Quality

To ensure data integrity and flag pipeline failures automatically, configure alerting using the following mechanisms:

#### Data Quality Assertions

You can define custom data validation rules (e.g., ensuring a column is never null, checking that primary keys are unique, or validating numeric ranges) by creating `.sqlx` assertion files.

  * You can supply a custom assertions file using the `--assertions` parameter: `bash uv run cortex-deploy --config config/config.yaml --assertions config/assertions.sqlx`
  * During pipeline execution, Dataform runs these validation queries. If an assertion query returns one or more rows, the validation fails, and the pipeline execution is immediately marked as failed.
  * For more information on writing data validation rules, see the [official Dataform assertions documentation](https://docs.cloud.google.com/dataform/docs/assertions).



#### Example Assertion File (`assertions.sqlx`)

Example of a Dataform assertion query that checks for `NULL` values and duplicate customer records. If this query returns any rows, the assertion will fail and stop the execution workflow:
    
    
    config {
      type: "assertion",
      description: "Ensure customer_number_kunnr is not null and unique"
    }
    
    -- Check for NULL values
    (
      SELECT
        "customer_number_kunnr is NULL" AS error_message
      FROM
        ${ref("customers")}
      WHERE
        customer_number_kunnr IS NULL
    )
    UNION ALL
    -- Check for duplicate keys
    (
      SELECT
        CONCAT("Duplicate customer number found: ", customer_number_kunnr) AS error_message
      FROM
        ${ref("customers")}
      GROUP BY
        customer_number_kunnr,
        client_mandt
      HAVING
        COUNT(*) > 1
    )
    

#### Cloud Alerting Policies

Set up standard [Google Cloud Alerting Policies](https://docs.cloud.google.com/monitoring/alerts) to notify your engineering or operations teams when issues arise:

  * **[Log-based Alerts](https://docs.cloud.google.com/logging/docs/alerting/log-based-alerts)** : Create alerts in [Cloud Logging](https://docs.cloud.google.com/logging/docs) that trigger when error events, failed workflow executions, or compiler issues are detected in your logs.
  * **Metric-based Alerts** : Define thresholds in [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs) based on execution duration or compilation failures.
  * **Notification Channels** : Configure these alerts to route issues to your team's preferred [communication channels](https://docs.cloud.google.com/monitoring/support/notification-options)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
