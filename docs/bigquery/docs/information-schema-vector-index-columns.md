---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-vector-index-columns/
title: VECTOR_INDEX_COLUMNS view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:22.672892+00:00
---

# VECTOR_INDEX_COLUMNS view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-vector-index-columns/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# VECTOR_INDEX_COLUMNS view

The `INFORMATION_SCHEMA.VECTOR_INDEX_COLUMNS` view contains one row for each vector-indexed column on each table in a dataset.

## Required permissions

To see [vector index](https://docs.cloud.google.com/bigquery/docs/vector-index) metadata, you need the `bigquery.tables.get` or `bigquery.tables.list` Identity and Access Management (IAM) permission on the table with the index. Each of the following predefined IAM roles includes at least one of these permissions:

  * `roles/bigquery.admin`
  * `roles/bigquery.dataEditor`
  * `roles/bigquery.dataOwner`
  * `roles/bigquery.dataViewer`
  * `roles/bigquery.metadataViewer`
  * `roles/bigquery.user`



For more information about BigQuery permissions, see [Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control).

## Schema

When you query the `INFORMATION_SCHEMA.VECTOR_INDEX_COLUMNS` view, the query results contain one row for each indexed column on each table in a dataset. 

The `INFORMATION_SCHEMA.VECTOR_INDEX_COLUMNS` view has the following schema:

Column name | Data type | Value  
---|---|---  
`index_catalog` | `STRING` | The name of the project that contains the dataset.  
`index_schema` | `STRING` | The name of the dataset that contains the vector index.  
`table_name` | `STRING` | The name of the table that the vector index is created on.  
`index_name` | `STRING` | The name of the vector index.  
`index_column_name` | `STRING` | The name of the indexed column.  
`index_field_path` | `STRING` | The full path of the expanded indexed field, starting with the column name. Fields are separated by a period.  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Scope and syntax

Queries against this view must have a [dataset qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax). The following table explains the region scope for this view:

View Name | Resource scope | Region scope  
---|---|---  
`[PROJECT_ID.]DATASET_ID.INFORMATION_SCHEMA.VECTOR_INDEX_COLUMNS` | Dataset level | Dataset location  
Replace the following: 

  * Optional: `PROJECT_ID`: the ID of your Google Cloud project. If not specified, the default project is used. 
  * `DATASET_ID`: the ID of your dataset. For more information, see [Dataset qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#dataset_qualifier). 

**Note:** You must use [a region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#region_qualifier) to query `INFORMATION_SCHEMA` views. The location of the query execution must match the region of the `INFORMATION_SCHEMA` view. 




**Example**
    
    
    -- Returns metadata for vector indexes in a single dataset.
    SELECT * FROM myDataset.INFORMATION_SCHEMA.VECTOR_INDEX_COLUMNS;
    

## Examples

The following query extracts information on columns that have vector indexes:
    
    
    SELECT table_name, index_name, index_column_name, index_field_path
    FROM my_project.dataset.INFORMATION_SCHEMA.VECTOR_INDEX_COLUMNS;

The result is similar to the following:
    
    
    +------------+------------+-------------------+------------------+
    | table_name | index_name | index_column_name | index_field_path |
    +------------+------------+-------------------+------------------+
    | table1     | indexa     | embeddings        | embeddings       |
    | table2     | indexb     | vectors           | vectors          |
    | table3     | indexc     | vectors           | vectors          |
    +------------+------------+-------------------+------------------+
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
