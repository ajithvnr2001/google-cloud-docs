---
url: https://docs.cloud.google.com/bigquery/docs/klaviyo-transfer-intro/
title: Introduction to Klaviyo data transfers \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:01.989476+00:00
---

# Introduction to Klaviyo data transfers  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/klaviyo-transfer-intro/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Introduction to Klaviyo data transfers

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** To get support or provide feedback for this feature, contact [dts-preview-support@google.com](mailto:dts-preview-support@google.com).

You can load data from Klaviyo to BigQuery using the [BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction) for Klaviyo connector. With the BigQuery Data Transfer Service, you can schedule recurring transfer jobs that add your latest data from Klaviyo to BigQuery.

To learn how to schedule a Klaviyo transfer, see [Load Klaviyo data into BigQuery](https://docs.cloud.google.com/bigquery/docs/klaviyo-transfer).

## Data ingestion options

These sections describe the data ingestion options for setting up a Klaviyo data transfer.

### Full or incremental transfers

You specify how data loads into BigQuery by selecting the **Full** or **Incremental** write preference in the transfer configuration when you [set up a Klaviyo transfer](https://docs.cloud.google.com/bigquery/docs/klaviyo-transfer#klaviyo-transfer-setup). Incremental transfers are supported in [preview](https://cloud.google.com/products#product-launch-stages).

**Note:** To request feedback or support for incremental transfers, send email to [dts-preview-support@google.com](mailto:dts-preview-support@google.com). You can configure a _full_ data transfer to transfer all data from your Klaviyo datasets with each data transfer. 

Alternatively, you can configure an _incremental_ data transfer ([Preview](https://cloud.google.com/products#product-launch-stages)) to only transfer data that was changed since the last data transfer, instead of loading the entire dataset with each data transfer. If you select **Incremental** for your data transfer, you must specify either the **Append** or **Upsert** write modes to define how data is written to BigQuery during an incremental data transfer. The following sections describe the available write modes.

#### Append write mode

The append write mode only inserts new rows to your destination table. This option strictly appends transferred data without checking for existing records, so this mode can potentially cause data duplication in the destination table.

When you select the append mode, you must select a watermark column. A watermark column is required for the Klaviyo connector to track changes in the source table.

For Klaviyo transfers, we recommend selecting a column that is only updated when the record was created, and won't change with subsequent updates—for example, the `CREATED_AT` column. 

#### Upsert write mode

The upsert write mode either updates a row or inserts a new row in your destination table by checking for a primary key. You can specify a primary key to let the Klaviyo connector determine what changes are needed to keep your destination table up to date with your source table. If the specified primary key is present in the destination BigQuery table during a data transfer, then the Klaviyo connector updates that row with new data from the source table. If a primary key is not present during a data transfer, then the Klaviyo connector inserts a new row.

When you select the upsert mode, you must select a watermark column and a primary key:

  * A watermark column is required for the Klaviyo connector to track changes in the source table. 
    * Select a watermark column that updates every time a row is modified. We recommend columns similar to the `UPDATED_AT` or `LAST_MODIFIED` column.


  * The primary key can be one or more columns on your table that are required for the Klaviyo connector to determine if it needs to insert or update a row.

Select columns that contain non-null values that are unique across all rows of the table. We recommend columns that include system-generated identifiers, unique reference codes (for example, auto-incrementing IDs), or immutable time-based sequence IDs.

To prevent potential data loss or data corruption, the primary key columns that you select must have unique values. If you have doubts about the uniqueness of your chosen primary key column, then we recommend that you use the append write mode instead.




## Data type mapping

The following table maps Klaviyo data types to the corresponding BigQuery data types:

Klaviyo data type | BigQuery data type  
---|---  
`String` | `STRING`  
`Text` | `STRING`  
`Integer` | `INTEGER`  
`Boolean` | `BOOLEAN`  
`Date (YYYY-MM-DD HH:MM:SS)` | `TIMESTAMP`  
`List` | `ARRAY`  
  
## Pricing

There is no cost to transfer Klaviyo data into BigQuery while this feature is in [Preview](https://cloud.google.com/products#product-launch-stages).

## What's next

  * For an overview of the BigQuery Data Transfer Service, see [What is BigQuery Data Transfer Service](https://docs.cloud.google.com/bigquery/docs/dts-introduction).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
