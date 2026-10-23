---
url: https://docs.cloud.google.com/logging/docs/analyze/log-volume/
title: Analyze log volume with Observability Analytics \u00a0|\u00a0 Cloud Logging \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:27.775327+00:00
---

# Analyze log volume with Observability Analytics  |  Cloud Logging  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/logging/docs/analyze/log-volume/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Observability ](https://docs.cloud.google.com/docs/observability)
  * [ Cloud Logging ](https://docs.cloud.google.com/logging/docs)
  * [ Guides ](https://docs.cloud.google.com/logging/docs/overview)



Send feedback 

#  Analyze log volume with Observability Analytics Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Observability Analytics lets you estimate the billable volume of your log entries so that you can understand and manage your logging costs. You can write SQL queries to aggregate log volume by dimensions such as resource type or application name, and then view or chart the results.

## How to query for billable volume

The billable volume of a log entry, which is the size that is reported to Cloud Billing, is available through the `storage_bytes` field. In your queries, you can use the `storage_bytes` field in the same way that you use any schema field whose data type is `INTEGER`. For example, you can include it in `SELECT` clauses, in `CASE` statements, and in common table expressions. For more information about querying your logs, see the following documents:

  * [Query and view logs in Observability Analytics](https://docs.cloud.google.com/logging/docs/analyze/query-and-view)
  * [Sample SQL queries](https://docs.cloud.google.com/logging/docs/analyze/examples)



Because Cloud Billing uses the billable volume when determining your costs, you can write queries that help you understand the sources of your costs. For example, you can write queries that help you determine which applications are writing the most log entries. To learn how to relate billable volume to cost, see the Cloud Logging sections of the [Google Cloud Observability pricing](https://cloud.google.com/products/observability/pricing) page.

The billable volume of a log entry isn't the size of the [`LogEntry`](https://docs.cloud.google.com/logging/docs/reference/v2/rest/v2/LogEntry) object that was sent to the Cloud Logging API. The billable volume includes bytes that are required for serialization and metadata.

## Before you begin

This section describes steps that you must complete before you can use Observability Analytics.

### Configure log buckets

Ensure that your log buckets have been upgraded to use Observability Analytics:

  1. In the Google Cloud console, go to the **Logs Storage** page: 

[Go to **Logs Storage**](https://console.cloud.google.com/logs/storage)

If you use the search bar to find this page, then select the result whose subheading is **Logging**.

  2. For each log bucket that has a log view that you want to query, ensure that the **Observability Analytics available** column displays **Open**. If **Upgrade** is shown, then click **Upgrade** and complete the dialog.



### Configure IAM roles and permissions

This section describes the IAM roles or permissions that are required to use Observability Analytics:

  * To get the permissions that you need to use Observability Analytics and query log views, ask your administrator to grant you the following IAM roles on your project: 

    * To query the `_Required` and `_Default` log buckets: [Logs Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logging.viewer`) 
    * To query all log views in a project: [Logs View Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewAccessor) (`roles/logging.viewAccessor`) 

You can restrict a principal to a specific log view either by adding an IAM condition to the Logs View Accessor role grant made at the project level, or by adding an IAM binding to the policy file of the log view. For more information, see [Control access to a log view](https://docs.cloud.google.com/logging/docs/logs-views#about-iam-policies).

These are the same permissions that you need to view log entries on the **Logs Explorer** page. For information about additional roles that you need to query views on user-defined buckets or to query the `_AllLogs` view of the `_Default` log bucket, see [Cloud Logging roles](https://docs.cloud.google.com/logging/docs/access-control#considerations).

  * To get the permissions that you need to query analytics views, ask your administrator to grant you the [Observability Analytics User ](https://docs.cloud.google.com/iam/docs/roles-permissions/observability#observability.analyticsUser) (`roles/observability.analyticsUser`) IAM role on your project. 




## Sample queries

This section provides example queries that analyze data from a single log view. If you store data in multiple log views and if you want to compute aggregate values for data stored in those views, then you need to use the `UNION` statement.

You can query your log entries by using the **Observability Analytics** page or anywhere you can query BigQuery datasets, which includes the **BigQuery Studio** and **Looker Studio** pages, and the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference).

To use the sample queries, do the following:

  * **Observability Analytics** page: Replace VIEW with the name of the log view. The format is `project_ID.region.bucket_ID.view_ID`.

[Go to **Log Analytics**](https://console.cloud.google.com/logs/analytics)

  * BigQuery datasets: Replace VIEW with the [path to the table](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#table_path) in the linked BigQuery dataset.

[Go to **BigQuery Studio**](https://console.cloud.google.com/bigquery)




### Query for log volume by app

To compute the total bytes per day, per app, for your log entries that were written against a Google Kubernetes Engine resource and that have a JSON payload, use the following query:
    
    
    SELECT
      timestamp_trunc(timestamp,DAY) as day,
      JSON_VALUE(labels["k8s-pod/app"]) as app_id,
      SUM(storage_bytes) as total_bytes
    FROM
      `VIEW`
    WHERE
      json_payload IS NOT NULL
      AND resource.type="k8s_container"
    GROUP BY ALL
    

To visualize the data, you can create a chart.

**Note:** The previous query aggregates the data over one-day intervals. To create a chart which displays data for multiple days, you might need to modify the time-range selector. In the following example, the query evaluates data over a time range of `14 days`.

In the following example, the data is displayed as a stacked bar chart. Each bar on the chart displays the total number of bytes stored, organized by app. In this example, the `frontend` app is generating the most log data:

![Example chart showing results of querying for log volume by app.](https://docs.cloud.google.com/static/logging/docs/images/query-log-volume-by-app.png)

### Query for log volume by log name

To list the number of stored bytes and the log name for each log entry that has a JSON payload and that was written against a Google Kubernetes Engine resource, use the following query:
    
    
    SELECT
      log_id AS log_name,
      storage_bytes
    FROM
      `VIEW`
    WHERE
      json_payload IS NOT NULL
      AND resource.type="k8s_container"
    

The previous query doesn't aggregate the results, instead there is one row for each log entry, and that row contains a log name and the number of stored bytes. If you chart this data, then you can visualize the portion of your log data as written to different logs:

![Example chart showing results of querying for log volume by log name.](https://docs.cloud.google.com/static/logging/docs/images/query-log-volume-by-log-name.png)

The previous chart shows that most log data is written to the log named `stdout`.

### Use the bq command-line tool to query for log volume by log name

You can include the `storage_bytes` field in queries that you run through the **BigQuery Studio** page or by using the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference).

The following query reports the log name and the number of stored bytes for each log entry:
    
    
    bq query --use_legacy_sql=false  'SELECT log_id as log_name,
      storage_bytes FROM `VIEW`'
    

The result of this query is similar to the following:
    
    
    +----------+---------------+
    | log_name | storage_bytes |
    +----------+---------------+
    | stdout   |           716 |
    | stdout   |           699 |
    | stdout   |           917 |
    | stdout   |           704 |
    

Each row corresponds to one log entry. The value of the `storage_bytes` column is the billable volume for that log entry.

## Limitations

The `storage_bytes` field is available only when the following are true:

  * The log bucket is upgraded to use Observability Analytics.
  * Your query is executed on the **Observability Analytics** page or anywhere you can query BigQuery datasets, which includes the **BigQuery Studio** and **Looker Studio** pages, and the [bq command-line tool](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference).

  * The log entry was written on or after January 1, 2024.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
