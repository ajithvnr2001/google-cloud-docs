---
url: https://docs.cloud.google.com/knowledge-catalog/docs/monitoring/
title: Monitor Knowledge Catalog metrics \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:42.336613+00:00
---

# Monitor Knowledge Catalog metrics  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/monitoring/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Monitor Knowledge Catalog metrics Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to use Cloud Monitoring to track Knowledge Catalog (formerly Dataplex Universal Catalog) service health, optimize performance, and gain visibility into your data platform. Proactive monitoring helps you ensure the reliability of data applications and make informed decisions about resource allocation and cost management.

To understand the costs, see [Monitoring pricing](https://cloud.google.com/stackdriver/pricing).

For more information about metric data retention, see [Monitoring quotas and limits](https://docs.cloud.google.com/monitoring/quotas#data_retention_policy).

## Use cases

You can use Knowledge Catalog metrics in Cloud Monitoring to support the following use cases:

  * **Ensure data pipeline reliability** : Monitor success and failure rates of Knowledge Catalog tasks, such as data ingestion or data quality jobs. Configure alerts for failures or unusual durations to minimize downtime for critical workloads.
  * **Optimize performance** : Track job durations and resource utilization metrics to identify and resolve performance bottlenecks in your data processing, data quality, and data discovery workloads.
  * **Manage costs** : Monitor Knowledge Catalog resource consumption (such as lakes, zones, and assets) in Monitoring, and use Cloud Billing export to BigQuery to attribute serverless compute (DCU) costs for Data Quality, Data Profiling, and Data Lineage workloads.
  * **Maintain data governance** : Track metrics related to metadata discovery and catalog enrichment to ensure that data assets are being scanned and tagged according to your governance policies.



## How it works

Knowledge Catalog is integrated with Cloud Monitoring, which collects metrics, events, and metadata from Knowledge Catalog services. These metrics provide insights into areas such as job execution status, API usage, and resource health. You can analyze these metrics using tools in Cloud Monitoring, such as Metrics Explorer, custom dashboards, and alerting. These tools let you visualize your service's behavior, identify performance trends, and create alerting policies that notify you when performance deviates from defined thresholds or when failures happen.

## Access service metrics in Monitoring

Knowledge Catalog service resource metrics are automatically enabled on Knowledge Catalog services. To view these metrics, use Monitoring.

You can access Monitoring from the [Google Cloud console](https://console.cloud.google.com/monitoring) or by using the [Monitoring API](https://docs.cloud.google.com/monitoring/api/v3).

If you're unable to view the monitoring graphs or create alerts, you might need additional [Monitoring permissions](https://docs.cloud.google.com/monitoring/access-control).

### Console

  1. In the Google Cloud console, go to the **Metrics explorer** page.

[Go to Metrics explorer](https://console.cloud.google.com/monitoring/metrics-explorer)

  2. In the **Select a metric** menu, select a `Cloud Dataplex` resource.

  3. Select a metric category, and then select a metric from the list.

To display information about a metric, hold the pointer over the metric name.

  4. Click **Apply**.

  5. Optional: Select filters, group by metric labels, perform aggregations, and select chart display options.




### REST

To capture and list metrics defined by a `filter` expression, Use the Monitoring [timeSeries.list](https://docs.cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.timeSeries/list) method.

To send an API request and display the response, on the API page, use the **Try this API** template.

## Knowledge Catalog service metrics in Monitoring

Knowledge Catalog service metrics facilitates monitoring of service health.

**Note:** Dataplex DataScan compute (such as auto data quality scans and data profiling scans) and data lineage Data Compute Units (DCUs) execute on serverless compute in Dataplex-managed infrastructure and do not emit real-time time-series metrics under `dataplex.googleapis.com/*` to Cloud Monitoring. Only lakes, zones, and assets emit time-series metrics to Cloud Monitoring. To monitor, track, and attribute Dataplex SKU consumption and DCU costs across projects and scans, query Cloud Billing export tables in BigQuery using Dataplex system labels. For details and example queries, see Monitor and attribute Dataplex DCU costs with Cloud Billing export. 

The "metric type" strings in this table must be prefixed with `dataplex.googleapis.com/`. That prefix has been omitted from the entries in the table. When querying a label, use the `metric.labels.` prefix; for example, `metric.labels.LABEL="VALUE"`. 

Metric type Launch stage  _(Resource hierarchy levels)_  
Display name  
---  
Kind, Type, Unit  
Monitored resources | _Description_  
Labels  
`asset/active` BETA ** _(project)_**   
Active   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Whether the asset is active._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/data_items` BETA ** _(project)_**   
Data items   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The count of items within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/data_size` BETA ** _(project)_**   
Data size   
`GAUGE`, `INT64`, `By`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The number of stored bytes within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/entities_pending_bigquery_iampolicy_updates` BETA ** _(project)_**   
Entities with BigQuery IAM policy updates pending   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Number of Entities associated with the Asset with BigQuery IAM policy updates pending._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/entities_pending_bigquery_metadata_updates` BETA ** _(project)_**   
Entities with BigQuery metadata updates pending   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Number of Entities associated with the Asset with BigQuery metadata updates pending._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/filesets` BETA ** _(project)_**   
Filesets   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The count of fileset entities within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/requires_action` BETA ** _(project)_**   
Requires action   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _Whether the asset has unresolved admin actions._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`asset/tables` BETA ** _(project)_**   
Tables   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Asset](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Asset)** |  _The count of table entities within the referenced resource._   
`resource_type`: The type of the referenced resource.   
`zone_type`: The type of the parent zone.   
`lake/requires_action` BETA ** _(project)_**   
Requires action   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Lake](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Lake)** |  _Whether the lake has unresolved admin actions._  
`zone/requires_action` BETA ** _(project)_**   
Requires action   
`GAUGE`, `INT64`, `1`   
**[dataplex.googleapis.com/Zone](https://docs.cloud.google.com/monitoring/api/resources#tag_dataplex.googleapis.com/Zone)** |  _Whether the zone has unresolved admin actions._   
`type`: The type of the zone.   
  
Table generated at 2026-10-08 15:22:12 UTC.

## Monitor and attribute Dataplex DCU costs with Cloud Billing export

Because Knowledge Catalog data scans (including auto data quality and data profiling) and data lineage do not publish time-series metrics to Cloud Monitoring, you can use [Cloud Billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery) to track, monitor, and attribute Data Compute Unit (DCU) usage and costs across projects, scans, and data resources.

### Dataplex billing labels

Knowledge Catalog automatically attaches system labels to billing records emitted for data scans and data lineage. You can query these labels in the `labels` array in your Cloud Billing export table:

Label key | Workload | Description  
---|---|---  
`goog-dataplex-datascan-id` | Data Quality, Data Profiling | The ID or name of the data scan.  
`goog-dataplex-datascan-job-id` | Data Quality, Data Profiling | The specific execution ID for the data scan job.  
`goog-dataplex-datascan-data-source-project` | Data Quality, Data Profiling | The Google Cloud project containing the scanned data source.  
`goog-dataplex-datascan-data-source-region` | Data Quality, Data Profiling | The Google Cloud region of the scanned data source.  
`goog-dataplex-datascan-data-source-bigquery-dataset` | Data Quality, Data Profiling | The BigQuery dataset ID of the scanned table.  
`goog-dataplex-datascan-data-source-bigquery-table` | Data Quality, Data Profiling | The BigQuery table ID scanned.  
`goog-dataplex-datascan-data-source-dataplex-lake` | Data Quality, Data Profiling | The Dataplex lake ID (if applicable).  
`goog-dataplex-datascan-data-source-dataplex-zone` | Data Quality, Data Profiling | The Dataplex data zone ID (if applicable).  
`goog-dataplex-datascan-data-source-dataplex-entity` | Data Quality, Data Profiling | The Dataplex entity ID (if applicable).  
`goog-dataplex-datascan-data-source-biglake-catalog` | Data Quality, Data Profiling | The BigLake catalog ID (if applicable).  
`goog-dataplex-datascan-data-source-biglake-namespace` | Data Quality, Data Profiling | The BigLake namespace (if applicable).  
`goog-dataplex-datascan-data-source-biglake-table` | Data Quality, Data Profiling | The BigLake table ID (if applicable).  
`goog-dataplex-workload-type` | Data Lineage | Identifies the workload. Set to `LINEAGE` for data lineage processing charges.  
  
### Example queries

Before running these queries, ensure that you have [enabled Cloud Billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery). In the example queries, replace the following placeholders:

  * `PROJECT_ID`: The Google Cloud project ID that hosts your BigQuery billing export dataset.
  * `DATASET_NAME`: The name of the BigQuery dataset containing your billing export table.
  * `BILLING_ACCOUNT_ID`: Your Cloud Billing account ID (formatted with underscores, for example, `012345_567890_ABCDEF`).



#### Query 1: Attribute DCU costs and usage by DataScan and target table

This query aggregates Dataplex Processing and Premium Processing costs by DataScan ID and target BigQuery table over the last 30 days:
    
    
    SELECT
      project.id AS project_id,
      (SELECT value FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-id') AS datascan_id,
      (SELECT value FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-data-source-project') AS data_source_project,
      (SELECT value FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-data-source-bigquery-dataset') AS data_source_dataset,
      (SELECT value FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-data-source-bigquery-table') AS data_source_table,
      sku.description AS sku_description,
      SUM(usage.amount) AS total_usage,
      usage.unit AS usage_unit,
      SUM(cost) AS total_cost,
      currency
    FROM
      `PROJECT_ID.DATASET_NAME.gcp_billing_export_v1_BILLING_ACCOUNT_ID`
    WHERE
      service.description = 'Dataplex'
      AND EXISTS (SELECT 1 FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-id')
      AND _PARTITIONDATE >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    GROUP BY
      project_id,
      datascan_id,
      data_source_project,
      data_source_dataset,
      data_source_table,
      sku_description,
      usage_unit,
      currency
    ORDER BY
      total_cost DESC;

#### Query 2: Attribute Dataplex costs by workload type (Lineage vs DataScan)

This query breaks down Dataplex SKU costs by workload category (such as Data Lineage versus DataScan) across all projects:
    
    
    SELECT
      project.id AS project_id,
      sku.description AS sku_description,
      COALESCE(
        (SELECT value FROM UNNEST(labels) WHERE key = 'goog-dataplex-workload-type'),
        IF(EXISTS(SELECT 1 FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-id'), 'DATASCAN', 'OTHER')
      ) AS workload_type,
      SUM(usage.amount) AS total_usage,
      usage.unit AS usage_unit,
      SUM(cost) AS total_cost,
      currency
    FROM
      `PROJECT_ID.DATASET_NAME.gcp_billing_export_v1_BILLING_ACCOUNT_ID`
    WHERE
      service.description = 'Dataplex'
      AND _PARTITIONDATE >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
    GROUP BY
      project_id,
      sku_description,
      workload_type,
      usage_unit,
      currency
    ORDER BY
      total_cost DESC;

#### Query 3: Daily DCU usage and cost trend per DataScan job execution

This query tracks daily DCU consumption and costs for individual DataScan job executions over the last 7 days:
    
    
    SELECT
      DATE(usage_start_time) AS usage_date,
      project.id AS project_id,
      (SELECT value FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-id') AS datascan_id,
      (SELECT value FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-job-id') AS job_id,
      SUM(usage.amount) AS total_usage,
      usage.unit AS usage_unit,
      SUM(cost) AS total_cost,
      currency
    FROM
      `PROJECT_ID.DATASET_NAME.gcp_billing_export_v1_BILLING_ACCOUNT_ID`
    WHERE
      service.description = 'Dataplex'
      AND EXISTS (SELECT 1 FROM UNNEST(labels) WHERE key = 'goog-dataplex-datascan-id')
      AND _PARTITIONDATE >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    GROUP BY
      usage_date,
      project_id,
      datascan_id,
      job_id,
      usage_unit,
      currency
    ORDER BY
      usage_date DESC,
      total_cost DESC;

## Build a custom Monitoring dashboard

You can build a custom Monitoring dashboard that displays charts of selected Knowledge Catalog service metrics. For more information about how to create a dashboard, see [Create and manage custom dashboards](https://docs.cloud.google.com/monitoring/charts/dashboards). When you select a metric for a widget on your dashboard, select a `Cloud Dataplex` resource and then choose a Knowledge Catalog metric.

## Use Monitoring alerts

You can create a Monitoring alert that notifies you when a Knowledge Catalog service or job metric crosses a specified threshold.

### Create an alert

To create an alert, follow the instructions in [Create metric-threshold alerting policies](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui). When you select a time series to be monitored, select a `Cloud Dataplex` resource and then choose a Knowledge Catalog metric.

### View alerts

When an alert is triggered by a metric threshold condition, Monitoring creates an incident and a corresponding event.

To view an incident, follow this step:

  * In the Google Cloud console, go to the **Alerting** page.

[Go to Alerting](https://console.cloud.google.com/monitoring/alerting)




If you defined a notification mechanism in the alert policy, such as an email or SMS notification, Monitoring also sends a notification of the incident.

For more information about alerts, see [Incidents for metric-based alerts](https://docs.cloud.google.com/monitoring/alerts/incidents-events).

## What's next

  * Learn more about [Cloud Monitoring](https://docs.cloud.google.com/monitoring/docs/monitoring-overview).
  * Learn about [Cloud Billing export to BigQuery](https://docs.cloud.google.com/billing/docs/how-to/export-data-bigquery).
  * Learn how to [use auto data quality](https://docs.cloud.google.com/knowledge-catalog/docs/use-auto-data-quality).
  * Learn how to [use data profiling](https://docs.cloud.google.com/knowledge-catalog/docs/use-data-profiling).
  * Learn how to [use data lineage](https://docs.cloud.google.com/knowledge-catalog/docs/use-lineage).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
