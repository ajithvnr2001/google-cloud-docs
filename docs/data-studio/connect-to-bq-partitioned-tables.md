---
url: https://docs.cloud.google.com/data-studio/connect-to-bq-partitioned-tables/
title: Connect to BigQuery date partitioned tables \u00a0|\u00a0 Data Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:24:20.128455+00:00
---

# Connect to BigQuery date partitioned tables  |  Data Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/connect-to-bq-partitioned-tables/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Connect to BigQuery date partitioned tables Stay organized with collections  Save and categorize content based on your preferences. 

Data Studio can fetch data from BigQuery tables that are partitioned on a `DATE`, `DATETIME`, or `TIMESTAMP` field. A partitioned table is divided into segments, called _partitions_ , that make it easier to manage and query your data. When you divide a large table into smaller partitions, you can improve query performance and control costs by reducing the number of bytes that are read by a query. For more information, see [Introduction to partitioned tables](https://docs.cloud.google.com/bigquery/docs/partitioned-tables).

## How Data Studio uses a BigQuery date partition field

Connecting Data Studio to a date partitioned BigQuery table lets you assign the partition field to be the governing date dimension for reports that use this data source. Learn more about [setting report date ranges](https://docs.cloud.google.com/data-studio/set-report-date-ranges).

### Connect a Data Studio data source to a date partitioned table

To connect to a date partitioned table, follow these steps:

  1. [Create a new BigQuery data source](https://docs.cloud.google.com/data-studio/connect-to-google-bigquery) or [edit the connection](https://docs.cloud.google.com/data-studio/edit-the-data-source-connection) for an existing data source.
  2. Enter the connection details for your date partitioned table.
  3. In the **Configuration** column in the data source connection page, select the **Use** _fieldname_ **as date range dimension** checkbox (where _fieldname_ is the name of the partition field in the BigQuery table).



For example, suppose you have a table in BigQuery that has two date fields, `order_date` and `ship_date`. The table is partitioned by `order_date`. When you connect to this table in Data Studio, you'll see an option that lets you assign this field as the date range dimension for charts that are based on this data source.

![Looker Studio data source configuration for a BigQuery partitioned table. The order_date partition field has a checkbox option to Use order_date as date range dimension.](https://docs.cloud.google.com/static/data-studio/images/partition-table-ds-config-2024-07-25.png)

## Effects of required partition filters

BigQuery tables can require the partition field to be used as a filter on the data. This requirement determines whether or not you can edit the **Use** _fieldname_ **as date range dimension** option.

### No partition filter required in the BigQuery table

If the table doesn't require a partition filter in the BigQuery table, the **Use** _fieldname_ **as date range dimension** option is cleared by default.

Selecting the **Use** _fieldname_ **as date range dimension** checkbox has the following effects:

  * Data Studio automatically uses the partition field as the **Date Range Dimension** for charts that are based on this data source.
  * You won't be able to select a different field to use as the **Date Range Dimension** when you configure the charts.
  * Charts using this data source will always have a **Default date range** filter applied. You can apply a custom date range, or you can use the **Auto** option to filter for the last 28 days.



When the **Use** _fieldname_ **as date range dimension** option is not enabled:

  * You can select any field that you want to use as the **Date Range Dimension** when you configure charts that are based on this data source.
  * The date range for charts that use this data source can be unfiltered (**Auto** date range) or you can apply a custom date range.



### Partition filter is required in the BigQuery table

If the BigQuery table requires a **Partition filter** , then the **Use** _fieldname_ **as date range dimension** checkbox is automatically selected and can't be cleared. The effects on charts that are based on this data source are the same as described in the previous section when the checkbox is selected.

## Limits of connecting to partitioned tables

Because the date partition feature sets the date range dimension for a chart, Data Studio can use only partitions that are based on a `DATE`, `DATETIME`, or `TIMESTAMP` field to provide date filtering in your reports.

Data Studio supports date partitions only when the **Partition by** option in BigQuery is set to **DAY**.

![BigQuery table details showing the table is partitioned by DAY on the order_date field.](https://docs.cloud.google.com/static/data-studio/images/partition-table-details-2024-07-26.png)

If the BigQuery table has a partition that is based on other data types, such as `INTEGER`, and the partition filter is required, you must explicitly filter on that field in a custom query. Otherwise, Data Studio will display an error. [Learn more about required filters](https://docs.cloud.google.com/bigquery/docs/managing-partitioned-tables#require-filter).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
