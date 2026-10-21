---
url: https://docs.cloud.google.com/architecture/import-logs-from-storage-to-logging/
title: Import logs from Cloud Storage to Cloud Logging \u00a0|\u00a0 Cloud Architecture Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:22:01.135235+00:00
---

# Import logs from Cloud Storage to Cloud Logging  |  Cloud Architecture Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/architecture/import-logs-from-storage-to-logging/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Cloud Architecture Center ](https://docs.cloud.google.com/architecture)



Send feedback 

#  Import logs from Cloud Storage to Cloud Logging Stay organized with collections  Save and categorize content based on your preferences. 

Last reviewed 2025-02-19 UTC

This reference architecture describes how you can import logs that were previously exported to Cloud Storage back to Cloud Logging.

This reference architecture is intended for engineers and developers, including DevOps, site reliability engineers (SREs), and security investigators, who want to configure and run the log importing job. This document assumes you are familiar with running Cloud Run jobs, and how to use Cloud Storage and Cloud Logging.

## Architecture

The following diagram shows how Google Cloud services are used in this reference architecture:

![Workflow diagram of log import from Cloud Storage to Cloud Logging.](https://docs.cloud.google.com/static/architecture/images/import-logs-from-storage-to-logging.svg)

This workflow includes the following components:

  * **[Cloud Storage](https://docs.cloud.google.com/storage) bucket**: Contains the previously exported logs you want to import back to Cloud Logging. Because these logs were previously exported, they're organized in the expected [export format](https://docs.cloud.google.com/logging/docs/export/storage#gcs-organization).
  * **[Cloud Run](https://docs.cloud.google.com/run/docs/overview/what-is-cloud-run#jobs) job**: Runs the import logs process: 
    * Reads the objects that store log entries from Cloud Storage.
    * Finds exported logs for the specified log ID, in the requested time range, based on the [organization of the exported logs](https://docs.cloud.google.com/logging/docs/export/storage#gcs-organization) in the Cloud Storage bucket.
    * Converts the objects into Cloud Logging API [`LogEntry` structures](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry). Multiple `LogEntry` structures are aggregated into batches, to reduce Cloud Logging API quota consumption. The architecture handles [quota errors](https://docs.cloud.google.com/docs/quotas/troubleshoot) when necessary.
    * Writes the converted log entries to Cloud Logging. If you re-run the same job multiple times, duplicate entries can result. For more information, see [Run the import job](https://docs.cloud.google.com/architecture/import-logs-from-storage-to-logging/deployment#run-import-job).
  * **[Cloud Logging](https://docs.cloud.google.com/logging)** : Ingests and stores the converted log entries. The log entries are processed as described in the [Routing and storage overview](https://docs.cloud.google.com/logging/docs/routing/overview). 
    * The Logging [quotas and limits](https://docs.cloud.google.com/logging/quotas) apply, including the Cloud Logging API quotas and limits and a 30-day [retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods). This reference architecture is designed to work with the default write quotas, with a basic retrying mechanism. If your write quota is lower than the default, the implementation might fail.
    * The imported logs aren't included in [log-based metrics](https://docs.cloud.google.com/logging/docs/logs-based-metrics), because their timestamps are in the past. However, if you opt to [use a label](https://docs.cloud.google.com/logging/docs/logs-based-metrics/labels), the timestamp records the import time, and the logs are included in the metric data.
  * **[BigQuery](https://docs.cloud.google.com/bigquery/docs/introduction-sql)** : Uses SQL to run analytical queries on imported logs (optional). To import audit logs from Cloud Storage, this architecture modifies the log IDs; you must account for this renaming when you query the imported logs.



## Use case

You might choose to deploy this architecture if your organization requires additional log analysis for incident investigations or other audits of past events. For example, you might want to analyze connections to your databases for the first quarter of the last year, as a part of a database access audit.

## Design alternatives

This section describes alternatives to the default design shown in this reference architecture document.

### Retention period and imported logs

Cloud Logging requires incoming log entries to have timestamps that don't exceed a 30-day [retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods). Imported log entries with timestamps older than 30 days from the import time are not stored.

This architecture validates the date range set in the Cloud Run job to avoid importing logs that are older than 29 days, leaving a one-day safety margin.

To import logs older than 29 days, you need to make the [following changes to the implementation code](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/logging/import-logs#importing-log-entries-with-timestamps-older-than-30-days), and then build a new container image to use in the Cloud Run job configuration.

  * Remove the 30-day validation of the date range
  * Add the original timestamp as a user label to the log entry
  * Reset the timestamp label of the log entry to allow it to be ingested with the current timestamp



When you use this modification, you must use the [`labels` field](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.labels) instead of the [`timestamp` field](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.timestamp) in your Observability Analytics queries. For more information about Observability Analytics queries and samples, see [Sample SQL queries](https://docs.cloud.google.com/logging/docs/analyze/examples).

## Design considerations

The following guidelines can help you to develop an architecture that meets your organization's requirements.

### Cost optimization

The cost for importing logs by using this reference architecture has multiple contributing factors.

You use the following billable components of Google Cloud:

  * [Cloud Logging](https://cloud.google.com/stackdriver/pricing#logging-pricing-summary) ([logs retention period](https://docs.cloud.google.com/logging/quotas#logs_retention_periods) costs apply)
  * [Cloud Run](https://cloud.google.com/run/pricing)
  * [Cloud Storage API](https://cloud.google.com/storage/pricing#operations-pricing)



Consider the following factors that might increase costs:

  * **Log duplication** : To avoid additional log storage costs, don't run the import job with the same configuration multiple times.
  * **Storage in additional destinations** : To avoid additional log storage costs, disable routing policies at the destination project to prevent log storage in additional locations or forwarding logs to other destinations such as Pub/Sub or BigQuery.
  * **Additional CPU and memory** : If your import job times out, you might need to increase the import job CPU and memory in your [import job configuration](https://docs.cloud.google.com/architecture/import-logs-from-storage-to-logging/deployment#create-the-cloud-run-import-job). Increasing these values might increase incurred Cloud Run costs.
  * **Additional tasks** : If the expected number of logs to be imported each day within the time range is high, you might need to increase the number of tasks in the [import job configuration](https://docs.cloud.google.com/architecture/import-logs-from-storage-to-logging/deployment#create-the-cloud-run-import-job). The job will split the time range equally between the tasks, so each task will process a similar number of days from the range concurrently. Increasing the number of tasks might increase incurred Cloud Run costs.
  * **Storage class** : If your Cloud Storage bucket's storage class is other than Standard, such as Nearline, Durable Reduced Availability (DRA), or Coldline, you might incur additional charges.
  * **Data traffic between different locations** : Configure the import job to run in the same location as the Cloud Storage bucket from which you import the logs. Otherwise, [network egress costs](https://cloud.google.com/storage/pricing#network-buckets) might be incurred.



To generate a cost estimate based on your projected usage, including Cloud Run jobs, use the [pricing calculator](https://cloud.google.com/products/calculator).

### Operational efficiency

This section describes considerations for managing analytical queries after the solution is deployed.

#### Log names and queries

Logs are stored to the project that is defined in the [`logName` field](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.log_name) of the log entry. To import the logs to the selected project, this architecture modifies the `logName` field of each imported log. The import logs are stored in the selected project's default log bucket that has the log ID `imported_logs` (unless the project has a log routing policy that changes the storage destination). The original value of the `logName` field is preserved in the [`labels` field](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry#FIELDS.labels) with the key `original_logName`.

You must account for the location of the original `logName` value when you query the imported logs. For more information about Observability Analytics queries and samples, see [Sample SQL queries](https://docs.cloud.google.com/logging/docs/analyze/examples).

### Performance optimization

If the volume of logs that you're importing exceeds Cloud Run capacity limits, the job might time out before the import is complete. To prevent an incomplete data import, consider increasing the `tasks` value in the import job. Increasing [CPU](https://docs.cloud.google.com/run/docs/configuring/services/cpu) and [memory](https://docs.cloud.google.com/run/docs/configuring/services/memory-limits) resources can also help improve task performance when you increase the number of tasks.

## Deployment

To deploy this architecture, see [Deploy a job to import logs from Cloud Storage to Cloud Logging](https://docs.cloud.google.com/architecture/import-logs-from-storage-to-logging/deployment).

## What's Next

  * Review the implementation code in the [GitHub repository](https://github.com/GoogleCloudPlatform/python-docs-samples/tree/main/logging/import-logs).
  * Learn how to analyze imported logs by using [Observability Analytics and SQL](https://docs.cloud.google.com/logging/docs/analyze/query-and-view).
  * For more reference architectures, diagrams, and best practices, explore the [Cloud Architecture Center](https://docs.cloud.google.com/architecture). 



## Contributors

Author: [Leonid Yankulin](https://www.linkedin.com/in/minherz) | Developer Relations Engineer

Other contributors: 

  * [Summit Tuladhar](https://www.linkedin.com/in/summitraj) | Senior Staff Software Engineer
  * [Wilton Wong](https://www.linkedin.com/in/wiltwong) | Enterprise Architect
  * [Xiang Shen](https://www.linkedin.com/in/xiangshen07) | Solutions Architect



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-02-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-02-19 UTC."],[],[]] 
