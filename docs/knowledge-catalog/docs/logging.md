---
url: https://docs.cloud.google.com/knowledge-catalog/docs/logging/
title: Monitor Knowledge Catalog logs \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:41.989794+00:00
---

# Monitor Knowledge Catalog logs  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/logging/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Monitor Knowledge Catalog logs Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to access, query, and interpret Knowledge Catalog (formerly Dataplex Universal Catalog) logs using Cloud Logging. Accessing Knowledge Catalog job and service logs lets you troubleshoot issues and monitor data management activities, including AI-powered data discovery and data quality scanning.

**Note:** For administrative actions and data access logs, see the [Audit Logging](https://docs.cloud.google.com/knowledge-catalog/docs/audit-logging) page.

By centralizing logs in Logging, you can analyze job performance, set up alerts for failures or anomalies, and route logs to other Google Cloud services like BigQuery for long-term retention and analysis.

To understand the costs, see [Google Cloud Observability pricing](https://cloud.google.com/stackdriver/pricing).

For more information about logging retention, see [Logs retention periods](https://docs.cloud.google.com/logging/quotas#logs_retention_periods).

To disable all logs or exclude logs from Logging, see [Exclusion filters](https://docs.cloud.google.com/logging/docs/exclusions).

To route logs from Logging to Cloud Storage, BigQuery, or Pub/Sub, see [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview).

## Use cases

Knowledge Catalog logging supports use cases across different industries:

  * **Troubleshoot data pipeline failures:** When a Knowledge Catalog task for data processing fails, `process` logs provide detailed error messages that help data engineers identify and resolve issues in their Spark jobs or custom tasks.
  * **Monitor data quality:** A financial services company can monitor `data_quality_scan_rule_result` logs to track data quality trends over time, get alerts on quality degradations for critical data assets, and provide auditors with evidence of data quality checks for regulatory compliance.
  * **Track metadata enrichment:** A retail company using metadata import jobs to enrich their catalog can use `metadata_job` logs to verify that imports are completing successfully and that all metadata items are being processed correctly.
  * **Audit data discovery:** Organizations can use `discovery` logs to monitor how and when new data sources are being discovered and registered within Knowledge Catalog, providing an audit trail for data onboarding processes.



## How Knowledge Catalog logging works

Knowledge Catalog sends logs for service operations and job executions to Cloud Logging. Each log entry contains details about the operation or job, such as its status, start and end time, associated resources (like a data scan or task), and outcome. Different types of operations, such as data scanning, discovery, metadata import, and data processing, generate different log types, which you can query using `logName` or the [logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) in Logging.

You can access and analyze these logs using the [Logs Explorer](https://docs.cloud.google.com/logging/docs/view/logs-explorer-interface) in the Google Cloud console or by routing them to other destinations like Cloud Storage buckets or BigQuery tables for further analysis.

## Knowledge Catalog log types

Knowledge Catalog publishes the following service logs to Cloud Logging.

Log type | Log name | `logName` query | Log description  
---|---|---|---  
Data scan event logs | `dataplex.googleapis.com/data_scan` | `logName=(projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fdata_scan)` | Job-level event logs for data scan jobs (data quality, data profile, and data insights scans) indicating job state, results, and statistics  
Data quality scan rule result logs | `dataplex.googleapis.com/data_quality_scan_rule_result` | `logName=(projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fdata_quality_scan_rule_result)` | Detailed rule-level evaluation results for each rule evaluated in a data quality scan job  
Discovery logs | `dataplex.googleapis.com/discovery` | `logName=(projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fdiscovery)` | Discovery progress and updates over assets in a zone  
Metadata job logs | `dataplex.googleapis.com/metadata_job` | `logName=(projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fmetadata_job)` | Logs about metadata import jobs and import items in the metadata import file  
Process logs | `dataplex.googleapis.com/process` | `logName=(projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fprocess)` | Job runs resulting from data processing tasks  
  
## Access Knowledge Catalog service logs

To access Logging, use the Logs Explorer in the Google Cloud console, the [`gcloud logging` commands](https://docs.cloud.google.com/sdk/gcloud/reference/logging), or the [Logging API](https://docs.cloud.google.com/logging/docs/apis). You can use the [logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) to build detailed queries.

### Required IAM permissions

To view and query logs, you must have the Logs Viewer (`roles/logging.viewer`) role, or equivalent permissions on the project.

### View logs in the Google Cloud console

  1. In the Google Cloud console, go to the **Observability > Logging > Logs explorer** page.

[Go to Logs explorer](https://console.cloud.google.com/logs/query)

  2. Configure the **Resource** and **Log name** filters based on the following table:

Log type | Resource selection | Log name selection  
---|---|---  
**Data scan events** | **Audited Resource** > Service: **Cloud Dataplex** | `dataplex.googleapis.com/data_scan`  
**Data quality scan rule results** | **Audited Resource** > Service: **Cloud Dataplex** | `dataplex.googleapis.com/data_quality_scan_rule_result`  
**Discovery logs** | **Cloud Dataplex Zone** | `dataplex.googleapis.com/discovery`  
**Metadata job logs** | **Cloud Dataplex Metadata Job** | `dataplex.googleapis.com/metadata_job`  
**Process logs** | **Cloud Dataplex Task** | `dataplex.googleapis.com/process`  
**Note:** You might need to click **Apply** after selecting the resource before the corresponding log names become available in the drop-down.
  3. _(Optional)_ Select specific sub-filters (such as a specific task ID) to narrow your query.

  4. Click **Apply** , then click **Run query**.




### Log filtering examples

You can use the [logging query language](https://docs.cloud.google.com/logging/docs/view/logging-query-language) in the Logs Explorer query editor or with the Google Cloud CLI. The following examples demonstrate how to read logs using the gcloud CLI.

#### Example: Read data scan events

To read event log entries for data quality or data profile scans, use the [`gcloud logging read` command](https://cloud.google.com/sdk/gcloud/reference/logging/read) with the following query:
    
    
    gcloud logging read \
        'resource.type="dataplex.googleapis.com/DataScan" AND
        logName=projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fdata_scan AND
        resource.labels.location=LOCATION AND
        resource.labels.datascan_id=DATA_SCAN_ID'
        --limit 10
    

#### Example: Read process log entries

To read process log entries, use the [`gcloud logging read` command](https://cloud.google.com/sdk/gcloud/reference/logging/read) with the following query:
    
    
    gcloud logging read \
        'resource.type="dataplex.googleapis.com/Task" AND
        logName=projects/PROJECT_ID/logs/dataplex.googleapis.com%2Fprocess AND
        resource.labels.location=LOCATION AND
        resource.labels.lake_id=LAKE_ID AND
        resource.labels.task_id=TASK_ID'
        --limit 10
    

## Sample log payloads

The following examples show the JSON payload structures for different types of Knowledge Catalog logs. You can use these examples to understand the structure of the logs and build log filters.

### Data scan event logs

In Knowledge Catalog, data scans encompass [data quality scans](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview), [data profile scans](https://docs.cloud.google.com/knowledge-catalog/docs/data-profiling-overview), and [data insights scans](https://docs.cloud.google.com/knowledge-catalog/docs/data-insights-structured-data). When you run a data scan job, Knowledge Catalog produces a `data_scan` event log in Logging that summarizes the overall job execution. For succeeded data insights scans (`jsonPayload.type="DATA_DOCUMENTATION"`), the event log also includes a `billableTokenUsage` block. For information about querying and charting data insights token consumption, see [Monitor data insights token usage](https://docs.cloud.google.com/knowledge-catalog/docs/monitor-insights-token-usage).

The following example shows an event log payload for a data quality scan:
    
    
    {
      "insertId": "123456abcdef",
      "jsonPayload": {
        "dataQuality": {
          "passed": false,
          "rowsAnalyzed": "5000"
        },
        "dataSource": "//bigquery.googleapis.com/projects/my-project/datasets/my_dataset/tables/my_table"
      },
      "resource": {
        "type": "dataplex.googleapis.com/DataScan",
        "labels": {
          "datascan_id": "my-data-quality-scan",
          "location": "us-central1",
          "resource_container": "projects/1234567890"
        }
      },
      "severity": "INFO"
    }
    

### Data quality scan rule result logs

When a [data quality scan](https://docs.cloud.google.com/knowledge-catalog/docs/auto-data-quality-overview) runs, Knowledge Catalog generates a data scan event log and a separate data quality scan rule result log for each individual rule evaluated in the job.

Each `data_quality_scan_rule_result` log entry contains information about the specific rule, including the rule configuration, evaluation dimension, status, and row counts.

The following example shows a data quality scan rule result log payload:
    
    
    {
      "insertId": "123456abcdef",
      "jsonPayload": {
        "jobId": "my-data-quality-scan-job-123",
        "dataSource": "//bigquery.googleapis.com/projects/my-project/datasets/my_dataset/tables/my_table",
        "column": "user_id",
        "ruleName": "user-id-not-null",
        "ruleType": "NON_NULL_EXPECTATION",
        "ruleDimension": "COMPLETENESS",
        "thresholdPercent": 100,
        "result": "PASSED",
        "evaluatedRowCount": "5000",
        "passedRowCount": "5000",
        "nullRowCount": "0"
      },
      "resource": {
        "type": "dataplex.googleapis.com/DataScan",
        "labels": {
          "datascan_id": "my-data-quality-scan",
          "location": "us-central1",
          "resource_container": "projects/1234567890"
        }
      },
      "severity": "INFO"
    }
    

### Discovery logs

The following example shows a discovery log payload:
    
    
    {
      "insertId": "123456abcdef",
      "jsonPayload": {
        "message": "BigQuery table published successfully.",
        "lakeId": "my-lake",
        "zoneId": "my-zone",
        "assetId": "my-asset",
        "dataLocation": "gs://my-bucket/path/to/data",
        "type": "TABLE_PUBLISHED",
        "table": {
          "table": "projects/my-project/datasets/my_dataset/tables/my_table",
          "type": "EXTERNAL_TABLE"
        }
      },
      "resource": {
        "type": "dataplex.googleapis.com/Zone",
        "labels": {
          "lake_id": "my-lake",
          "zone_id": "my-zone",
          "location": "us-central1",
          "resource_container": "projects/1234567890"
        }
      },
      "severity": "INFO"
    }
    

### Metadata job logs

The following example shows a metadata job log payload:
    
    
    {
      "insertId": "123456abcdef",
      "jsonPayload": {
        "resource": "projects/my-project/locations/us-central1/metadataJobs/my-metadata-job",
        "message": "Metadata import job completed successfully.",
        "type": "IMPORT",
        "importResult": {
          "state": "SUCCEEDED",
          "stage": "INGESTION",
          "mutatedEntryGroups": "1",
          "createdEntries": "50",
          "updatedEntries": "10",
          "deletedEntries": "5"
        }
      },
      "resource": {
        "type": "dataplex.googleapis.com/MetadataJob",
        "labels": {
          "metadata_job_id": "my-metadata-job",
          "location": "us-central1",
          "resource_container": "projects/1234567890"
        }
      },
      "severity": "INFO"
    }
    

### Process logs

The following example shows a process log payload:
    
    
    {
      "insertId": "123456abcdef",
      "jsonPayload": {
        "message": "Spark job completed successfully.",
        "jobId": "my-task-job-123",
        "startTime": "2026-08-13T10:00:00Z",
        "endTime": "2026-08-13T10:05:00Z",
        "state": "SUCCEEDED",
        "type": "SPARK",
        "service": "DATAPROC",
        "serviceJob": "projects/my-project/regions/us-central1/jobs/dataproc-job-123",
        "executionTrigger": "TASK_CONFIG"
      },
      "resource": {
        "type": "dataplex.googleapis.com/Task",
        "labels": {
          "task_id": "my-task",
          "lake_id": "my-lake",
          "location": "us-central1",
          "resource_container": "projects/1234567890"
        }
      },
      "severity": "INFO"
    }
    

## Set up log-based alerts

You can set up log-based alerts to get notified whenever specific Knowledge Catalog events occur (such as a failed data quality scan).

To create log-based alerts, you must have the Logs Configuration Writer (`roles/logging.configWriter`) and Monitoring AlertPolicy Editor (`roles/monitoring.alertPolicyEditor`) roles, or equivalent permissions.

  1. Run a query in the **Logs Explorer** that targets the failure condition (for example: `resource.type="dataplex.googleapis.com/DataScan" AND NOT jsonPayload.dataQuality.passed=true`).
  2. Above the query results pane, click **Create alert**.
  3. In the **Create log-based alert** panel, enter an alert policy name and a description.
  4. Click **Next** and configure your notification channels.
  5. Click **Save**.



For more detailed information, see [Create log-based alerts](https://cloud.google.com/logging/docs/alerting/log-based-alerts).

## What's next

  * Learn how to [monitor data insights token usage](https://docs.cloud.google.com/knowledge-catalog/docs/monitor-insights-token-usage).
  * Learn more about [Cloud Logging](https://docs.cloud.google.com/logging/docs).
  * Learn about [Knowledge Catalog monitoring](https://docs.cloud.google.com/knowledge-catalog/docs/monitoring).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
