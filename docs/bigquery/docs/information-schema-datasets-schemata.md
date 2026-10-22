---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-datasets-schemata/
title: SCHEMATA view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:14:56.528574+00:00
---

# SCHEMATA view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-datasets-schemata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SCHEMATA view

The `INFORMATION_SCHEMA.SCHEMATA` view provides information about the datasets in a project or region. The view returns one row for each dataset.

## Before you begin

To query the `SCHEMATA` view for dataset metadata, you need the `bigquery.datasets.get` Identity and Access Management (IAM) permission at the project level.

Each of the following predefined IAM roles includes the permissions that you need in order to get the `SCHEMATA` view:

  * `roles/bigquery.admin`
  * `roles/bigquery.dataEditor`
  * `roles/bigquery.dataOwner`
  * `roles/bigquery.dataViewer`



For more information about BigQuery permissions, see [Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control).

## Schema

When you query the `INFORMATION_SCHEMA.SCHEMATA` view, the query results contain one row for each dataset in the specified project. 

The `INFORMATION_SCHEMA.SCHEMATA` view has the following schema:

Column name | Data type | Value  
---|---|---  
`catalog_name` | `STRING` | The name of the project that contains the dataset  
`schema_name` | `STRING` | The dataset's name also referred to as the `datasetId`  
`schema_owner` | `STRING` | The value is always `NULL`  
`creation_time` | `TIMESTAMP` | The dataset's creation time  
`last_modified_time` | `TIMESTAMP` | The dataset's last modified time  
`location` | `STRING` | The dataset's geographic location  
`ddl` | `STRING` | The `[CREATE SCHEMA](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/data-definition-language#create_schema_statement)` DDL statement that can be used to create the dataset  
`default_collation_name` | `STRING` |  The name of the default [collation specification](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/collation-concepts) if it exists; otherwise, `NULL`.   
`sync_status` | `JSON` | The status of the sync between the primary and secondary replicas for [cross-region replication](https://docs.cloud.google.com/bigquery/docs/data-replication) and [disaster recovery](https://docs.cloud.google.com/bigquery/docs/managed-disaster-recovery) datasets. Returns `NULL` if the replica is a primary replica or the dataset doesn't use replication.  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Scope and syntax

Queries against this view must include a [region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax). If you do not specify a regional qualifier, metadata is retrieved from the US region. The following table explains the region scope for this view:

View Name | Resource scope | Region scope  
---|---|---  
`[PROJECT_ID.]INFORMATION_SCHEMA.SCHEMATA` | Project level | US region   
`[PROJECT_ID.]`region-REGION`.INFORMATION_SCHEMA.SCHEMATA` | Project level | `REGION`  
Replace the following: 

  * Optional: `PROJECT_ID`: the ID of your Google Cloud project. If not specified, the default project is used. 
  * `REGION`: any [dataset region name](https://docs.cloud.google.com/bigquery/docs/locations). For example, ``region-us``. 

**Note:** You must use [a region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#region_qualifier) to query `INFORMATION_SCHEMA` views. The location of the query execution must match the region of the `INFORMATION_SCHEMA` view. 




**Example**
    
    
    -- Returns metadata for datasets in a region.
    SELECT * FROM region-us.INFORMATION_SCHEMA.SCHEMATA;
    

## Example

To run the query against a project other than your default project, add the project ID to the dataset in the following format: 
    
    
    `PROJECT_ID`.INFORMATION_SCHEMA.SCHEMATA

for example, ``myproject`.INFORMATION_SCHEMA.SCHEMATA`. 
    
    
    SELECT
      * EXCEPT (schema_owner)
    FROM
      INFORMATION_SCHEMA.SCHEMATA;

**Note:** `INFORMATION_SCHEMA` view names are case-sensitive.

The result is similar to the following. For readability, some columns are excluded from the result.
    
    
    +----------------+---------------+---------------------+---------------------+------------+------------------------------------------+
    |  catalog_name  |  schema_name  |    creation_time    | last_modified_time  |  location  |                   ddl                    |
    +----------------+---------------+---------------------+---------------------+------------+------------------------------------------+
    | myproject      | mydataset1    | 2018-11-07 19:50:24 | 2018-11-07 19:50:24 | US         | CREATE SCHEMA `myproject.mydataset1`     |
    |                |               |                     |                     |            | OPTIONS(                                 |
    |                |               |                     |                     |            |   location="us"                          |
    |                |               |                     |                     |            | );                                       |
    +----------------+---------------+---------------------+---------------------+------------+------------------------------------------+
    | myproject      | mydataset2    | 2018-07-16 04:24:22 | 2018-07-16 04:24:22 | US         | CREATE SCHEMA `myproject.mydataset2`     |
    |                |               |                     |                     |            | OPTIONS(                                 |
    |                |               |                     |                     |            |   default_partition_expiration_days=3.0, |
    |                |               |                     |                     |            |   location="us"                          |
    |                |               |                     |                     |            | );                                       |
    +----------------+---------------+---------------------+---------------------+------------+------------------------------------------+
    | myproject      | mydataset3    | 2018-02-07 21:08:45 | 2018-05-01 23:32:53 | US         | CREATE SCHEMA `myproject.mydataset3`     |
    |                |               |                     |                     |            | OPTIONS(                                 |
    |                |               |                     |                     |            |   description="My dataset",              |
    |                |               |                     |                     |            |   location="us"                          |
    |                |               |                     |                     |            | );                                       |
    +----------------+---------------+---------------------+---------------------+------------+------------------------------------------+
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
