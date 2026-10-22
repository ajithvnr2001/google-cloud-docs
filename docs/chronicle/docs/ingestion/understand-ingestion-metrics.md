---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/understand-ingestion-metrics/
title: Ingestion metrics overview \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:29.783232+00:00
---

# Ingestion metrics overview  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/understand-ingestion-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Ingestion metrics overview

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. Use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-methods) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).

Google SecOps provides detailed ingestion metrics to offer visibility into the health, volume, and processing status of your security data pipeline. Monitoring these metrics is crucial for ensuring data is flowing correctly, identifying potential issues, and optimizing your Google SecOps deployment.

### Why Ingestion Metrics Are Important

  * **Health Monitoring:** Track the status of your data feeds and collection agents.
  * **Troubleshooting:** Quickly diagnose issues like data drops, parsing errors, or connectivity problems.
  * **Volume Tracking:** Understand how much data is being ingested from various sources, useful for capacity planning and cost management.
  * **Normalization Insights:** Monitor the success rate of logs being parsed into the Unified Data Model (UDM).
  * **Alerting:** Configure notifications for anomalies in data flow, errors, or volume changes.



### Where to Access Ingestion Metrics

  * **Google Cloud Monitoring** :

    * Integrates Google SecOps metrics into Cloud Monitoring, allowing you to create dashboards and set up alert policies based on thresholds for metrics like ingested log counts, sizes, and normalization events.
    * Metrics are available under prefixes like `Chronicle Collector` and `Chronicle Log Type`.
    * Reference: [Use Cloud Monitoring for ingestion insights](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics)
  * **Google SecOps Health Hub** :

    * The Health Hub provides a centralized view within the Google SecOps platform to monitor data source status, ingestion volumes, and parsing health. It highlights errors and provides links to dig deeper.
    * Reference: [Use the Health Hub](https://docs.cloud.google.com/chronicle/docs/reports/data-health-monitoring-and-troubleshooting-dashboard)
  * **BigQuery Export** :

    * Google SecOps can export detailed `ingestion_metrics` tables to your BigQuery dataset. This allows for in-depth SQL-based analysis, custom reporting, and joining with other data.
    * Reference: [Google SecOps data in BigQuery](https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery)
    * Reference: [Ingestion metrics reference for Looker and BigQuery](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-explore)



### Key Metric Categories and Fields

Ingestion metrics are broken down by different components of the ingestion pipeline (for example, Forwarder, Ingestion API, Normalizer, Feeds). Here are some key fields you'll encounter:

  * **Volume Metrics** :

    * `log_count`: Number of raw log entries received or processed.
    * `log_volume`: Total size of logs received or processed (in bytes).
    * `event_count`: Number of UDM events generated after parsing.
  * **Normalization Metrics** :

    * `state`: The outcome of the normalization process for logs (for example, `parsed`, `failed_parsing`, `failed_validation`).
    * `total_events`: Count of successfully validated UDM events.
    * `total_error_events`: Count of events that failed parsing or validation.
    * `drop_reason_code`: Reason why a log or event was dropped.
  * **Health & Performance**:

    * `last_heartbeat_time`: Indicates the last time a collector or feed was active.
    * `drop_count`: Number of logs dropped by a component.
    * `cpu_used`, `memory_used`, `disk_used`: Resource utilization for on-premise components like the Bindplane Agent or legacy Forwarder.
    * `latency_count`: Metrics related to the time taken between ingestion and normalization.
  * **Quota Metrics (Ingestion API)** :

    * `quota_rejected_long_term_log_volume`: Volume of logs rejected due to exceeding quota limits.



### Understanding Dimensions

Metrics are typically broken down by dimensions, allowing you to filter and group data:

  * `component`: The part of the ingestion pipeline the metric refers to (for example, `Forwarder`, `Ingestion API`, `Normalizer`, `Out-of-Band Processor`).
  * `log_type`: The type of log source (for example, `WINDOWS_DNS`, `CS_EDR`).
  * `collector_id` / `feed_id`: Unique identifier for the specific collector instance or data feed.
  * `namespace`: For organizing logs, often used in API ingestion.



**Note:** As stated in the [Ingestion metrics schema](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema), aggregate ingestion metrics should be treated as indicators of approximate volume rather than exact counts for any given time range.

### Discrepancies between raw log volume and dashboard log volume

The total `ingestion.log_volume` reported in Google SecOps dashboards (for example, when querying `ingestion.component = "Ingestion API"`) can differ significantly from the total volume of raw logs stored in your instance. The Google SecOps interface doesn't display an all-time cumulative ingestion counter from when your instance was provisioned. Because each reporting tool enforces a maximum lookback window, you can't calculate an all-time cumulative total once your instance is older than the tool's retention limit.

These differences occur for the following reasons:

  * **Different time ranges and lookback limits** :

    * **Raw log storage** : Retains data according to your configured instance retention policy. Your instance may have ingested logs over multiple years since provisioning.
    * **Google SecOps dashboards** : Calculate `ingestion.log_volume` only for the selected time range, up to a maximum lookback limit of 365 days (or up to 24 months in Cloud Monitoring for Bring Your Own Project (BYOP) instances). If your instance has ingested data for longer than 365 days, dashboard queries report a lower total than your cumulative historical ingestion volume.
  * **Different data sources and collection pipelines** :

    * **Raw log storage** : Records the direct byte size of ingested raw log batches stored in Google SecOps.
    * **Google SecOps dashboards** : Query `ingestion.log_volume` from the `ingestion_metrics` table, which collects telemetry asynchronously at approximately 5-minute intervals. Because this telemetry pipeline can experience collection latency, sampling, or transient metric drops, dashboard queries provide an approximate volume rather than an exact byte count.



### Where to calculate ingestion volume and how values differ

Because the Google SecOps interface doesn't display an all-time cumulative ingestion counter from the instance start time, use the following locations to calculate ingestion volume depending on the time range you need:

  * **Google SecOps dashboards (up to 365 days)** :

    * **Where to calculate** : Open **Dashboards & Reports** > **Dashboards** , and then view the **Throughput** widget on the **Main** or **Data Ingestion and Health** dashboard (including the **Ingestion - Throughput (All-Time)** chart). You can also run a custom dashboard query for `sum($event.ingestion.log_volume)` filtered by `$event.ingestion.component = "Ingestion API"`.
    * **Maximum time range** : Queries are limited to a maximum of 365 days, even on the curated **Ingestion - Throughput (All-Time)** chart.
    * **How values differ** : Dashboards query the asynchronous `ingestion_metrics` table, which collects telemetry at approximately 5-minute intervals and can experience collection latency or transient metric drops. Values are approximate and reflect only logs ingested through the Ingestion API during the selected time range, rather than all-time raw log bytes or final billed volume.
  * **Cloud Monitoring Metrics explorer (up to 24 months for BYOP instances)** :

    * **Where to calculate** : Open **Monitoring** > **Metrics explorer** in the Google Cloud console, and then run a query for `chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}` (for step-by-step instructions, see [View billed ingestion volume](https://docs.cloud.google.com/chronicle/docs/ingestion/view-billed-ingestion-volume#method-3)).
    * **Maximum time range** : Queries are limited to a maximum of 24 months, based on Cloud Monitoring metric retention.
    * **How values differ** : Cloud Monitoring queries collector-level ingestion byte counts over your selected time window. Values cover a longer lookback window than Google SecOps dashboards (up to 24 months instead of 365 days), but they don't reflect an all-time total if your instance is older than 24 months.
  * **BigQuery export (beyond 365 days, based on your dataset retention)** :

    * **Where to calculate** : Open your BigQuery project after exporting the `ingestion_metrics` table, and then run a query for `SUM(log_volume)` (or `total_size_bytes` in [Looker and BigQuery](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-explore)) filtered by `component = "Ingestion API"`.
    * **Maximum time range** : Queries are limited to the retention period configured for your BigQuery table from when you enabled the export, rather than the 365-day dashboard limit.
    * **How values differ** : BigQuery queries the same asynchronous `ingestion_metrics` table as Google SecOps dashboards. Values match dashboard queries for the same time range, but they remain approximate telemetry indicators rather than all-time raw log bytes or final billed volume.



### Using Ingestion Metrics

  * **Troubleshooting:** Filter by `log_type` and `state` (for example, `failed_parsing`) in the Normalizer metrics to find parsing issues. Check `drop_count` and `drop_reason_code` for data loss.
  * **Alerting** : Set up alerts in Cloud Monitoring to monitor sudden drops in `log_count` for critical log sources, or high rates of `total_error_events`. To monitor your daily ingestion volume against contractual limits, use the **Total ingested log size** (`chronicle.googleapis.com/ingestion/log/bytes_count`) metric. Don't use the `chronicle.googleapis.com/ingestion/quota_limit` metric for daily volume alerts, for the following reasons:

    * The `quota_limit` metric measures proximity to dynamic backend limits rather than actual ingested data volume.
    * Using `quota_limit` for daily volume alerts can cause false alarms when backend thresholds adjust.

For steps to set up a daily volume alert policy, see [Set up a sample policy to monitor daily ingestion volume](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics#monitor-daily-ingestion-volume).

  * **Capacity Planning:** Analyze `log_volume` trends in BigQuery to forecast future needs.

  * **Validating Configuration:** After setting up a new data source, check the metrics to confirm data is flowing and being parsed as expected.




By regularly monitoring and understanding these ingestion metrics, you can ensure a reliable and efficient data pipeline for your Google SecOps instance.

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
