---
url: https://docs.cloud.google.com/chronicle/docs/ingestion/view-billed-ingestion-volume/
title: View billed ingestion volume \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:37:02.860954+00:00
---

# View billed ingestion volume  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/ingestion/view-billed-ingestion-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# View billed ingestion volume

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

Google Security Operations billing is calculated based on the volume of raw log data ingested into the platform. This document outlines how to utilize specific ingestion metrics that align with the billing system to ensure accurate cost management and forecasting.

The following principles define how ingestion volume is calculated for billing purposes:

  * **Billable volume** : Billing calculations are based exclusively on raw log data bytes. Metadata, internal labels, and enrichment tags associated with the logs are excluded from the billable total.

  * **Authoritative data source** : The ingestion metrics provided within the billing system serve as the sole authoritative source for financial reporting. External metrics or internal dashboards outside of the specific billing module must not be used for budget reconciliation or cost auditing.


**Note:** The Google SecOps interface doesn't display an all-time cumulative ingestion total from when your instance was provisioned. You can query up to 365 days of ingestion volume in Google SecOps dashboards, or up to 24 months in Cloud Monitoring for Bring Your Own Project (BYOP) instances. For details on where to calculate ingestion volume and why totals differ across tools, see Compare ingestion volume calculations and time limits and [Discrepancies between raw log volume and dashboard log volume](https://docs.cloud.google.com/chronicle/docs/ingestion/understand-ingestion-metrics#bytes-ingested-discrepancy).

## View ingestion volume

The ingestion volume data for billing purposes is accessible in three primary locations. Each source uses the same underlying ingestion metrics data to maintain data consistency and alignment with financial statements.

### Method 1: Main dashboard

The main dashboard provides a high-level visualization of ingestion trends over time. This view facilitates the monitoring of daily volume spikes and the identification of long-term ingestion patterns.

  1. Sign in to [Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Dashboards & Reports** > **Dashboards**.

  3. Use the **Search** tab to find and select the **Main** dashboard.

  4. Go to the **Throughput** widget to monitor data ingestion rates. You can use the time range selector to calculate the total throughput over specific intervals.


**Note:** The Throughput widget only displays ingestion volume metrics for logs sent using the Ingestion API. It doesn't reflect total raw log bytes that make up the final billed ingestion volume across all ingestion methods.

### Method 2: Data Health and Ingestion dashboard

The **Data Health and Ingestion** dashboard gives a granular view of ingestion telemetry, categorized by _log type_ and _source_. This dashboard facilitates the auditing of ingestion volumes at a _per-log-source level_ , which aids in identifying specific contributors to the total billable volume.

  1. Sign in to [Google SecOps](https://docs.cloud.google.com/chronicle/docs/log-in-to-ui).

  2. Click **Dashboards & Reports** > **Dashboards**.

  3. Use the **Search** tab to find and select the **Data Ingestion and Health** dashboard. 

  4. Go to the **Throughput** widget to analyze data ingestion rates. You can use the time range selector to calculate the total throughput over specific intervals.


**Note:** The Throughput widget only displays ingestion volume metrics for logs sent using the Ingestion API. It doesn't reflect total raw log bytes that make up the final billed ingestion volume across all ingestion methods.

### Method 3: Cloud Monitoring

The Cloud Monitoring method is available to customers who use a Bring Your Own Project (BYOP) setup. This approach permits the use of external monitoring tools to query ingestion telemetry directly from the underlying project infrastructure.

  1. Go to the Google Cloud console and in the search bar, enter **Metrics Explorer**. Alternatively, click  menu  **Menu** , select **Monitoring** > **Metrics explorer**.

  2. Select your Cloud Monitoring profile.

  3. On the **Profile** page's search bar, enter **Integrations**.

  4. Select **Metrics explorer**.

  5. Click **promQL** to switch to promQL query mode.

  6. View the results in a table format: Find **Results** and then select **Table**.

  7. View the ingestion volume (`ingestion_log_byte_count`): Copy and paste the following ingestion metric query into the query editor, and then run the query:
         
         sum (increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}[1h]))
         

  8. Optional: Filter a specific log type and include it in the query. For example, to view ingestion for the log type `GCP_CLOUDAUDIT`, run the following query:
         
         sum(increase(chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector",log_type="GCP_CLOUDAUDIT"}[1h]))
         




## Compare ingestion volume calculations and time limits

The Google SecOps interface doesn't display an all-time cumulative counter of raw logs ingested since your instance was provisioned. Because each reporting tool uses a different lookback window and data pipeline, you can't calculate an all-time total from instance start time once your instance exceeds the retention limit of the tool you are querying.

The following breakdown shows where you can calculate ingestion volume and how the values differ across locations:

  * **Google SecOps dashboards (up to 365 days)** :

    * **Where to calculate** : Open **Dashboards & Reports** > **Dashboards** , and then view the **Throughput** widget on the **Main** or **Data Ingestion and Health** dashboard (including the **Ingestion - Throughput (All-Time)** chart). You can also run a custom dashboard query for `sum($event.ingestion.log_volume)` filtered by `$event.ingestion.component = "Ingestion API"`.
    * **Maximum time range** : Queries are limited to a maximum of 365 days, even on the curated **Ingestion - Throughput (All-Time)** chart.
    * **How values differ** : Dashboards query the asynchronous `ingestion_metrics` table, which collects telemetry at approximately 5-minute intervals and can experience collection latency or transient metric drops. Values are approximate and reflect only logs ingested through the Ingestion API during the selected time range, rather than all-time raw log bytes or final billed volume across all ingestion methods.
  * **Cloud Monitoring Metrics explorer (up to 24 months for BYOP instances)** :

    * **Where to calculate** : Open **Monitoring** > **Metrics explorer** in the Google Cloud console, and then run a query for `chronicle_googleapis_com:ingestion_log_bytes_count{monitored_resource="chronicle.googleapis.com/Collector"}` (as shown in Method 3).
    * **Maximum time range** : Queries are limited to a maximum of 24 months, based on Cloud Monitoring metric retention.
    * **How values differ** : Cloud Monitoring queries collector-level ingestion byte counts over your selected time window. Values cover a longer lookback window than Google SecOps dashboards (up to 24 months instead of 365 days), but they don't reflect an all-time total if your instance is older than 24 months.
  * **BigQuery export (beyond 365 days, based on your dataset retention)** :

    * **Where to calculate** : Open your BigQuery project after exporting the `ingestion_metrics` table, and then run a query for `SUM(log_volume)` (or `total_size_bytes` in [Looker and BigQuery](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-explore)) filtered by `component = "Ingestion API"`.
    * **Maximum time range** : Queries are limited to the retention period configured for your BigQuery table from when you enabled the export, rather than the 365-day dashboard limit.
    * **How values differ** : BigQuery queries the same asynchronous `ingestion_metrics` table as Google SecOps dashboards. Values match dashboard queries for the same time range, but they remain approximate telemetry indicators rather than all-time raw log bytes or authoritative billing statements.



## Create alerts on the amount of data ingested

Creating alerts for ingestion volume helps you manage costs and respond to unexpected spikes. Cloud Monitoring handles the alerting workflow.

To monitor your daily ingestion volume against contractual limits, use the **Total ingested log size** (`chronicle.googleapis.com/ingestion/log/bytes_count`) metric.

**Note:** Don't use the `chronicle.googleapis.com/ingestion/quota_limit` metric to track your daily contractual ingestion volume, for the following reasons: 

  * The `quota_limit` metric measures proximity to dynamic backend limits rather than actual ingested data volume.
  * Using `quota_limit` for daily volume alerts can cause false alarms when backend thresholds adjust.



For step-by-step configuration instructions, see [Set up a sample policy to monitor daily ingestion volume](https://docs.cloud.google.com/chronicle/docs/ingestion/ingestion-notifications-for-health-metrics#monitor-daily-ingestion-volume).

## Monitor ingestion metrics across managed tenants

Cloud Monitoring scopes give you a centralized visibility into ingestion volumes across managed projects (tenants).

Metric scopes let you monitor data from multiple managed Google Cloud tenants within a single console. The functionality requires the following configuration:

  * Managed tenants must provide the necessary permissions to the central Cloud Monitoring project.
  * The primary account must be configured as a _scoping project_. 



With this configuration, the centralized view facilitates monitoring the total ingestion volume (`log_byte_count`) across the entire environment.

For more information, see [Metrics scopes overview](https://docs.cloud.google.com/monitoring/settings). To set up this view, see [Configure a metrics scope](https://docs.cloud.google.com/monitoring/settings/multiple-projects).

**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
