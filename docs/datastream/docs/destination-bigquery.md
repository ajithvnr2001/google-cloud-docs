---
url: https://docs.cloud.google.com/datastream/docs/destination-bigquery/
title: BigQuery destination \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:45:43.240284+00:00
---

# BigQuery destination  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/destination-bigquery/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  BigQuery destination Stay organized with collections  Save and categorize content based on your preferences. 

This page gives you an overview of the BigQuery destination. It describes write behavior and known limitations of Datastream when you replicate data to BigQuery.

## Write behavior

  * The maximum event size when you stream data into BigQuery is 20 MB.

  * When you configure your stream, you can select the way that Datastream writes your change data to BigQuery. For more information, see [Configure write mode](https://docs.cloud.google.com/datastream/docs/configure-bigquery-destination#configure-write-mode).




### Table metadata

Datastream appends a `STRUCT` column named `datastream_metadata` to each table that's written to the BigQuery destination.

#### Merge write mode

If a table has a primary key at the source, then the column contains the following fields:

  * `UUID`: This field has the `STRING` data type.
  * `SOURCE_TIMESTAMP`: This field has the `INTEGER` data type.



If a table doesn't have a primary key, then the column contains an additional field: `IS_DELETED`. This field has the `BOOLEAN` data type, and it indicates whether the data that Datastream streams to the destination is associated with a `DELETE` operation at the source. Tables without primary keys are append-only.

#### Append-only write mode

**Note:** For Oracle, PostgreSQL, and SQL Server sources, when using the append-only write mode with tables containing large object (LOB) columns, intermediate changes might not be captured in scenarios involving rapid, back-to-back updates or a quick delete after an insert. This happens because Datastream streams these columns by explicitly querying the database for missing values point-in-time (in an active lookup process called supplementation). Because `DELETE` operations are never supplemented, their payloads don't trigger intermediate lookups. This limitation does not apply to MySQL or MongoDB sources.

The `datastream_metadata` column contains the same fields for tables with and without primary keys:

  * `UUID`: This field has the `STRING` data type.
  * `SOURCE_TIMESTAMP`: This field has the `INTEGER` data type.
  * `CHANGE_SEQUENCE_NUMBER`: This field has the `STRING` data type. It's an internal sequence number used by Datastream for each change event.
  * `CHANGE_TYPE`: This field has the `STRING` data type. It indicates the type of the change event: `INSERT`, `UPDATE-INSERT`, `UPDATE-DELETE`or `DELETE`.
  * `SORT_KEYS`: This field contains an array of `STRING` values. You can use the values to sort the change events.



### Control BigQuery costs

BigQuery costs are charged separately from Datastream. To learn how to control your BigQuery costs, see [BigQuery CDC pricing](https://docs.cloud.google.com/bigquery/docs/change-data-capture#CDC_pricing).

## Cost management best practices

When using Datastream with BigQuery as a destination, consider the following cost management best practices:

  * **Understand BigQuery CDC costs** : when using Datastream with BigQuery as a destination, change data capture (CDC) involves background merge operations. By default, BigQuery CDC ingestion background jobs performed without a `BACKGROUND` or `BACKGROUND_CHANGE_DATA_CAPTURE` BigQuery reservation assignment use [on-demand pricing](https://docs.cloud.google.com/bigquery/pricing#analysis_pricing).
  * **Use BigQuery reservations** : to manage and cap the costs associated with CDC merge jobs, we recommend that you purchase a [BigQuery](https://docs.cloud.google.com/bigquery/docs/reservations-tasks) slot reservation. This provides a fixed capacity for a fixed price, making your costs more predictable. For more information, see [Configure a BigQuery reservation for use with CDC ingestion](https://docs.cloud.google.com/bigquery/docs/change-data-capture#configure-bigquery-reservation).
  * **Tune`max_staleness`**: The `max_staleness` parameter in BigQuery is a direct trade-off between data freshness and cost. A lower value means more frequent merge operations and higher costs, but fresher data. Tune this parameter to a level that meets your business requirements for data freshness without exceeding your budget. For more information, see [Manage table staleness](https://docs.cloud.google.com/bigquery/docs/change-data-capture#manage_table_staleness).



## Known limitations

**Note:** This section describes limitations for using Datastream with BigQuery as a destination. In addition to these limitations, you need to familiarize yourself with BigQuery change data capture limitations. For more information, see [Stream table updates with change data capture](https://docs.cloud.google.com/bigquery/docs/change-data-capture#limitations).

Known limitations for using BigQuery as a destination include:

  * By default, Datastream doesn't support adding a primary key to a table that's already replicated to BigQuery without a primary key, or removing a primary key from a table that's replicated to BigQuery with a primary key. If you need to perform such changes, contact Google Support. For information about _changing_ the primary key definition for a source table that already has a primary key, see [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues#bq-errors).
  * Primary keys in BigQuery must be of the following data types:

    * `DATE`
    * `BOOL`
    * `GEOGRAPHY`
    * `INT64`
    * `NUMERIC`
    * `BIGNUMERIC`
    * `STRING`
    * `TIMESTAMP`
    * `DATETIME`

Tables that contain primary keys of unsupported data types aren't replicated by Datastream.

  * BigQuery doesn't support table names with `.`, `$`, `/`, `@` , or `+` characters. Datastream replaces such characters with underscores when creating destination tables.

For example, `table.name` in the source database becomes `table_name` in BigQuery.

For more information on table names in BigQuery, see [Table naming](https://docs.cloud.google.com/bigquery/docs/tables#table_naming).

  * BigQuery doesn't support more than four clustering columns. When replicating a table with more than four primary key columns, Datastream uses four primary key columns as the clustering columns.

  * Datastream maps out-of-range date and time literals such as PostgreSQL infinity date types to the following values:

    * Positive `DATE` to the value of `9999-12-31`
    * Negative `DATE` to the value of `0001-01-01`
    * Positive `TIMESTAMP` to the value of `9999-12-31 23:59:59.999000 UTC`
    * Negative `TIMESTAMP` to the value of `0001-01-01 00:00:00 UTC`
  * BigQuery doesn't support streaming tables which have primary keys of `FLOAT` or `REAL` data types. Such tables aren't replicated. To learn more about BigQuery date types and ranges, see [Data types](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-types).

  * If your source is Salesforce or Salesforce Marketing Cloud ([Preview](https://cloud.google.com/products/#product-launch-stages)), the **Dataset for each schema** configuration option isn't supported.




## What's next

  * Learn how to [replicate data from a source database to BigQuery datasets using Datastream](https://docs.cloud.google.com/datastream/docs/quickstart-replication-to-bigquery).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
