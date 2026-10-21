---
url: https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery/
title: Export to a Google-managed BigQuery project \u00a0|\u00a0 Google Security Operations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T13:12:09.175340+00:00
---

# Export to a Google-managed BigQuery project  |  Google Security Operations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/chronicle/docs/reports/overview-chronicle-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Google Security Operations ](https://docs.cloud.google.com/chronicle/docs)
  * [ Guides ](https://docs.cloud.google.com/chronicle/docs/secops/secops-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Export to a Google-managed BigQuery project

Supported in:

Google SecOps  [ SIEM ](https://docs.cloud.google.com/chronicle/docs/secops/google-secops-siem-toc)

**Caution:** The Ingestion API is [deprecated](https://docs.cloud.google.com/chronicle/docs/deprecations) and will be discontinued on July 20, 2027. To ingest logs into Google SecOps, use the [Chronicle API](https://docs.cloud.google.com/chronicle/docs/reference/rest) instead. For details on how to migrate, see [Migrate from legacy SIEM API to Chronicle API](https://docs.cloud.google.com/chronicle/docs/administration/migrate-from-legacy-api-to-chronicle-api).**Note:** This option is available for Google SecOps Enterprise Plus customers only. For all other customers, see [Configure data export to BigQuery in a self-managed Google Cloud project](https://docs.cloud.google.com/chronicle/docs/preview/cloud-integration/export-to-customer-managed-project).

Google SecOps provides a managed data lake of normalized and threat intelligence enriched telemetry by exporting data to BigQuery. This lets you do the following:

  * Run ad-hoc queries directly in BigQuery.
  * Use your own business intelligence tools, such as Looker or Microsoft Power BI, to create dashboards, reports, and analytics.
  * Join Google SecOps data with third-party datasets.
  * Run analytics using data science or machine learning tools.
  * Run reports using predefined default dashboards and custom dashboards.



Google SecOps exports the following categories of data to BigQuery:

  * **UDM event records:** UDM records created from log data ingested by customers. These records are enriched with aliasing information.
  * **Rules matches (detections)** : instances where a rule matches one or more events.
  * **IoC matches** : artifacts (for example domains, IP addresses) from events that match Indicator of Compromise (IoC) feeds. This includes matches to from global feeds and customer-specific feeds.
  * **Ingestion metrics:** include statistics, such as number of log lines ingested, number of events produced from logs, number of log errors indicating that logs couldn't be parsed, and the state of Google SecOps forwarders. For more information, see [Ingestion metrics BigQuery schema](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema).
  * **Entity graph and entity relationships** : stores the description of entities and their relationships with other entities.



## Overview of the tables

Google SecOps creates the `datalake` dataset in BigQuery and the following tables:

  * `entity_enum_value_to_name_mapping`: for enumerated types in the `entity_graph` table, maps the numerical values to the string values.
  * `entity_graph`: stores data about UDM entities.
  * [`events`](https://docs.cloud.google.com/chronicle/docs/reports/events-schema-overview): stores data about UDM events.
  * [`ingestion_metrics`](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema): stores statistics related to ingestion and normalization of data from specific ingestion sources, such as Google SecOps forwarders, feeds, and Ingestion API.
  * `ioc_matches`: stores IOC matches found against UDM events.
  * `job_metadata`: an internal table used to track the export of data to BigQuery.
  * `rule_detections`: stores detections returned by rules run in Google SecOps. This table only includes detections from rules that were live (for example, enabled and not deleted) at the time the export process ran. Detections from rules that were disabled or deleted before the export job executed won't be included in this table, even if the detection time falls within the query range.
  * `rulesets`: stores information about Google SecOps curated detections, including the category each rule set belongs to, whether it is enabled, and the current alerting status.
  * `udm_enum_value_to_name_mapping`: For enumerated types in the events table, maps the numerical values to the string values.
  * `udm_events_aggregates`: stores aggregated data summarized by hour of normalized events. This table is populated on a best effort basis. Data for every hour may not be immediately available, and there can be delays in population.



### Data Freshness and Export Schedule

The data in the BigQuery tables is updated at different intervals. Understanding these can help set expectations for data availability:

  * **UDM Events (`events` table):** Typically updated frequently, with data usually available within approximately two hours of ingestion.
  * **Best Effort Exports:** Many other datasets are exported on a **best effort** basis. This includes, but is not limited to: 
    * `udm_events_aggregates`
    * `rule_detections`
    * `ioc_matches`
    * `entity_graph`
    * `ingestion_metrics`



For tables exported on a best effort basis, while updates are regular, there is no strictly committed latency or timing. Delays can occur, and for hourly aggregations like `udm_events_aggregates`, data for every hour may not be immediately available at the end of the hour. Data is generally expected to be updated within a day.

## Access data in BigQuery

You can run queries directly in BigQuery or connect your own business intelligence tool, such as Looker or Microsoft Power BI, to BigQuery.

To enable access to the BigQuery instance, use the [Google SecOps BigQuery Access API](https://docs.cloud.google.com/chronicle/docs/reference/bigquery-access-api#access_api_reference). You can provide an email address for either a user or a group that you own. If you configure access to a group, use the group to manage which team members can access the BigQuery instance.

To connect Looker or another business intelligence tool to BigQuery, contact your Google SecOps representative for service account credentials that enable you to connect an application to the Google SecOps BigQuery dataset. The service account will have IAM BigQuery Data Viewer role (`roles/bigquery.dataViewer`) and BigQuery Job Viewer role (`roles/bigquery.jobUser`).

## Data retention

For Google SecOps Enterprise Plus customers using Google-managed BigQuery, the following retention settings apply:

  * Legacy Google SecOps Enterprise Plus customers (on deprecation path):

    * `ioc_matches` and `rule_detections` tables: no retention limit is set, due to low volume.
    * `entity_graph`, `udm_events_aggregates`, and other partitioned tables except the `events` table: 180 days.
    * `events` table (UDM events): data is retained according to your Google SecOps contract, or the default of 366 days if not specified in the contract.
  * New customers: retention duration is governed by the Google SecOps contract (consistent with the Advanced BigQuery Export feature).




## What's next

  * Learn more about the following schemas: 
    * [`events`](https://docs.cloud.google.com/chronicle/docs/reports/events-schema-overview)
    * [`ingestion_metrics`](https://docs.cloud.google.com/chronicle/docs/reference/ingestion-metrics-schema)
  * For information about accessing and running queries in BigQuery, see [Run interactive and batch query jobs](https://docs.cloud.google.com/bigquery/docs/running-queries).
  * For information about how to query partitioned tables, see [Query partitioned tables](https://docs.cloud.google.com/bigquery/docs/querying-partitioned-tables).
  * For information about how to connect Looker to BigQuery, see Looker documentation about [connecting to BigQuery](https://docs.cloud.google.com/looker/docs/db-config-google-bigquery).



**Need more help?** [Get answers from Community members and Google SecOps professionals.](https://security.googlecloudcommunity.com/)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
