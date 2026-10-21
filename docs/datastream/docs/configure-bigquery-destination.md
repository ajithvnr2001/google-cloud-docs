---
url: https://docs.cloud.google.com/datastream/docs/configure-bigquery-destination/
title: Configure a BigQuery destination \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:53.226868+00:00
---

# Configure a BigQuery destination  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-bigquery-destination/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a BigQuery destination Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure Datastream so that you can write data to BigQuery datasets.

## Required permissions

Datastream uses the BigQuery built-in support for change data capture (CDC) updates. Datastream updates the BigQuery tables by processing and applying streamed changes using the BigQuery Storage Write API (gRPC).

The permissions required for using the API and ingesting data to BigQuery are granted to the [Datastream Service Agent](https://docs.cloud.google.com/iam/docs/roles-permissions/datastream#datastream.serviceAgent) role.

## Configure BigQuery as a destination

To configure Datastream for streaming to BigQuery, perform the following steps:

  1. Make sure that the BigQuery API is enabled in your Google Cloud project.
  2. If you want to use the **Single dataset for all schemas** option, [create a dataset in BigQuery](https://docs.cloud.google.com/bigquery/docs/datasets#create-dataset).
  3. Configure the destination dataset for your stream.
  4. Configure write mode.
  5. Specify the maximum data staleness limit for your stream.



### Configure the destination datasets

Datasets are top-level containers that are used to organize and control access to your BigQuery tables.

When you configure datasets for the BigQuery destination using Datastream, you can select one of the following options:

  * **Dataset for each schema** : The dataset is selected or automatically created by Datastream in the [BigQuery location](https://docs.cloud.google.com/bigquery/docs/locations) specified, based on the schema name of the source. As a result, each schema in the source has a corresponding dataset in BigQuery. For example, if you have a MySQL source, and this source has a `mydb` database and an `employees` table within the database, then Datastream creates the `mydb` dataset and `employees` table in BigQuery.

Datastream creates datasets in the project that you select. By default, your current project is selected. The list of datasets shows the datasets available in the selected project. Although you don't need to create the datasets in the same region as your stream, we recommend to keep all resources for the stream, as well as datasets, in the same region for cost and performance optimization.

**Note:** The **Dataset for each schema** option isn't supported for Salesforce sources.
  * **Single dataset for all schemas** : You select a BigQuery dataset for the stream. Datastream streams all data into this dataset. For the dataset that you select, Datastream creates all tables as `<schema>_<table>`.

For example, if you have a MySQL source, and this source has a `mydb` database and an `employees` table within the database, then Datastream creates the `mydb_employees` table in the dataset that you select.

You can select a dataset from any Google Cloud project. By default, datasets from the current project are shown. You can also create a new dataset in the selected project.

**Note:** If your source is Salesforce, Datastream uses the customer domain as the dataset name.



### Configure write mode

There are two modes you can use to define how you want your data written to BigQuery:

  * **Merge** : This is the default write mode. When selected, BigQuery reflects the way your data is stored in the source database. This means that Datastream writes all changes to your data to BigQuery, and BigQuery then consolidates the changes with existing data, thus creating final tables that are replicas of the source tables. With merge mode, no historical record of the change events is kept. For example, if you insert and then update a row, BigQuery only keeps the updated data. If you then delete the row from the source table, BigQuery no longer keeps any record of that row.

**Note:** Merge mode is only applicable for tables with primary keys. Tables without primary keys are append-only.
  * **Append-only** : The append-only write mode lets you add data to BigQuery as a stream of changes (`INSERT`, `UPDATE-INSERT`, `UPDATE-DELETE` and `DELETE` events). Use this mode when you need to retain the historical state of your data.

**Note:** For Oracle, PostgreSQL, and SQL Server sources, when using the append-only write mode with tables containing large object (LOB, TOAST etc.) columns, intermediate changes might not be captured in scenarios involving rapid, back-to-back updates or a quick delete after an insert. This happens because Datastream streams these columns by explicitly querying the database for missing values point-in-time (in an active lookup process called supplementation). Because `DELETE` operations are never supplemented, their payloads don't trigger intermediate lookups. This limitation doesn't apply to MySQL or MongoDB sources.

To get a better understanding of the append-only write mode, consider the following scenarios:

    * _Initial backfill_ : after the initial backfill, all events are written to BigQuery as `INSERT` type events, with the same timestamp, universally unique identifier (UUID), and change sequence number.
    * _Primary key update_ : when a primary key changes, two rows are written to BigQuery: 
      * An `UPDATE-DELETE` row with the original primary key
      * An `UPDATE-INSERT` row with the new primary key
    * _Row update_ : when you update a row, a single `UPDATE-INSERT` row is written to BigQuery
    * _Row deletion_ : when you delete a row, a single `DELETE` row is written to BigQuery



### Specify data staleness limit

BigQuery applies source modifications in the background on an ongoing basis, or at query run time, according to the configured data staleness limit. When Datastream creates a new table in BigQuery, the table's `max_staleness` option is set according to the current data staleness limit value for the stream. This ensures that the table never exceeds the applied staleness limit. The data staleness limit doesn't affect the frequency of the BigQuery merge jobs.

For more information about using BigQuery tables with the `max_staleness` option, see [Table staleness](https://docs.cloud.google.com/bigquery/docs/change-data-capture#manage_table_staleness).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
