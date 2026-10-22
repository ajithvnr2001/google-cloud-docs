---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-indexes/
title: SEARCH_INDEXES view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:36:11.779571+00:00
---

# SEARCH_INDEXES view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-indexes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SEARCH_INDEXES view

The `INFORMATION_SCHEMA.SEARCH_INDEXES` view contains one row for each search index in a dataset.

## Required permissions

To see [search index](https://docs.cloud.google.com/bigquery/docs/search-index) metadata, you need the `bigquery.tables.get` or `bigquery.tables.list` Identity and Access Management (IAM) permission on the table with the index. Each of the following predefined IAM roles includes at least one of these permissions:

  * `roles/bigquery.admin`
  * `roles/bigquery.dataEditor`
  * `roles/bigquery.dataOwner`
  * `roles/bigquery.dataViewer`
  * `roles/bigquery.metadataViewer`
  * `roles/bigquery.user`



For more information about BigQuery permissions, see [Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control).

## Schema

When you query the `INFORMATION_SCHEMA.SEARCH_INDEXES` view, the query results contain one row for each search index in a dataset. 

The `INFORMATION_SCHEMA.SEARCH_INDEXES` view has the following schema:

Column name | Data type | Value  
---|---|---  
`index_catalog` | `STRING` | The name of the project that contains the dataset.  
`index_schema` | `STRING` | The name of the dataset that contains the index.  
`table_name` | `STRING` | The name of the base table that the index is created on.  
`index_name` | `STRING` | The name of the index.  
`index_status` | `STRING` | The status of the index: `ACTIVE`, `PENDING DISABLEMENT`, `TEMPORARILY DISABLED`, or `PERMANENTLY DISABLED`. 

  * `ACTIVE` means that the index is usable or being created. Refer to the `coverage_percentage ` to see the progress of index creation.
  * `PENDING DISABLEMENT` means that the total size of indexed base tables exceeds your organization's [limit](https://docs.cloud.google.com/bigquery/quotas#index_limits); the index is queued for deletion. While in this state, the index is usable in search queries and you are charged for the search index storage. 
  * `TEMPORARILY DISABLED` means that either the total size of indexed base tables exceeds your organization's [limit](https://docs.cloud.google.com/bigquery/quotas#index_limits), or the base indexed table is smaller than 10GB. While in this state, the index is not used in search queries and you are not charged for the search index storage.
  * `PERMANENTLY DISABLED` means that there is an incompatible schema change on the base table, such as changing the type of an indexed column from `STRING` to `INT64`.

  
`creation_time` | `TIMESTAMP` | The time the index was created.  
`last_modification_time` | `TIMESTAMP` | The last time the index configuration was modified. For example, deleting an indexed column.  
`last_refresh_time` | `TIMESTAMP` | The last time the table data was indexed. A `NULL` value means the index is not yet available.  
`disable_time` | `TIMESTAMP` | The time the status of the index was set to `DISABLED`. The value is `NULL` if the index status is not `DISABLED`.  
`disable_reason` | `STRING` | The reason the index was disabled. `NULL` if the index status is not `DISABLED`.  
`DDL` | `STRING` | The DDL statement used to create the index.  
`coverage_percentage` | `INTEGER` | The approximate percentage of table data that has been indexed. 0% means the index is not usable in a `SEARCH` query, even if some data has already been indexed.  
`unindexed_row_count` | `INTEGER` | The number of rows in the base table that have not been indexed.  
`total_logical_bytes` | `INTEGER` | The number of billable logical bytes for the index.  
`total_storage_bytes` | `INTEGER` | The number of billable storage bytes for the index.  
`analyzer` | `STRING` | The [text analyzer](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/text-analysis) to use to generate tokens for the search index.  
`last_index_alteration_info` | `STRUCT` | The details of the latest user-triggered index alteration, containing following fields: 

  * `status`: a `STRING` value that indicates the alteration status. Possible values are `IN_PROGRESS`, and `FAILED`.
  * `message`: the details of the `FAILED` status as an [ErrorProto](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/ErrorProto). The value is `NULL` for other statuses.
  * `new_coverage_percentage`: an `INT64` value that contains the approximate percentage of table data that has been indexed for the alteration.
  * `start_time`: the timestamp when the alteration is initiated.
  * `end_time`: the timestamp when the alteration enters the `FAILED` status.
  * `ddl`: the data definition language (DDL) statement used to alter the index.

  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Scope and syntax

Queries against this view must have a [dataset qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax). The following table explains the region scope for this view:

View Name | Resource scope | Region scope  
---|---|---  
`[PROJECT_ID.]DATASET_ID.INFORMATION_SCHEMA.SEARCH_INDEXES` | Dataset level | Dataset location  
Replace the following: 

  * Optional: `PROJECT_ID`: the ID of your Google Cloud project. If not specified, the default project is used. 
  * `DATASET_ID`: the ID of your dataset. For more information, see [Dataset qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#dataset_qualifier). 



**Example**
    
    
    -- Returns metadata for search indexes in a single dataset.
    SELECT * FROM myDataset.INFORMATION_SCHEMA.SEARCH_INDEXES;
    

## Example

The following example shows all active search indexes on tables in the dataset `my_dataset`, located in the project `my_project`. It includes their names, the DDL statements used to create them, their coverage percentage, and their text analyzer. If an indexed base table is less than 10GB, then its index is not populated, in which case `coverage_percentage` is 0.
    
    
    SELECT table_name, index_name, ddl, coverage_percentage, analyzer
    FROM my_project.my_dataset.INFORMATION_SCHEMA.SEARCH_INDEXES
    WHERE index_status = 'ACTIVE';
    

The results should look like the following:
    
    
    +-------------+-------------+--------------------------------------------------------------------------------------+---------------------+----------------+
    | table_name  | index_name  | ddl                                                                                  | coverage_percentage | analyzer       |
    +-------------+-------------+--------------------------------------------------------------------------------------+---------------------+----------------+
    | small_table | names_index | CREATE SEARCH INDEX `names_index` ON `my_project.my_dataset.small_table`(names)      | 0                   | NO_OP_ANALYZER |
    | large_table | logs_index  | CREATE SEARCH INDEX `logs_index` ON `my_project.my_dataset.large_table`(ALL COLUMNS) | 100                 | LOG_ANALYZER   |
    +-------------+-------------+--------------------------------------------------------------------------------------+---------------------+----------------+
    

## Troubleshooting

To enable this view, you can set the value of `enable_info_schema_storage` to `TRUE` on your project or organization. For more information on managing your configuration, see [Manage configuration settings](https://docs.cloud.google.com/bigquery/docs/default-configuration).

If you haven't configured this setting, you will see the following error:
    
    
    INFORMATION_SCHEMA.SEARCH_INDEXES hasn't been enabled for project <myproject>.
    Consider using one of the following SQL statements to enable data collection:
    ALTER PROJECT `<myproject>`
    SET OPTIONS (`region-<region>.enable_info_schema_storage` = TRUE)
    
    Or to enable for the entire organization:
    ALTER ORGANIZATION
    SET OPTIONS (`region-<region>.enable_info_schema_storage` = TRUE)
    
    After enabling, please allow around 1 day for the complete historical data to
    become available.
    

Run the SQL statements described in the error message to enable the view.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
