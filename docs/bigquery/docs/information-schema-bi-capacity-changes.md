---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-bi-capacity-changes/
title: INFORMATION_SCHEMA.BI_CAPACITY_CHANGES view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:57.916643+00:00
---

# INFORMATION_SCHEMA.BI_CAPACITY_CHANGES view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-bi-capacity-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# INFORMATION_SCHEMA.BI_CAPACITY_CHANGES view

The `INFORMATION_SCHEMA.BI_CAPACITY_CHANGES` view contains history of changes to the BI Engine capacity. If you want to view the current state of BI Engine reservation, see the [`INFORMATION_SCHEMA.BI_CAPACITIES` view](https://docs.cloud.google.com/bigquery/docs/information-schema-bi-capacities).

## Required permission

To query the `INFORMATION_SCHEMA.BI_CAPACITY_CHANGES` view, you need the `bigquery.bireservations.get` Identity and Access Management (IAM) permission for BI Engine reservations.

For more information about BigQuery permissions, see [Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control).

## Schema

When you query the `INFORMATION_SCHEMA.BI_CAPACITY_CHANGES` view, the query results contain one row for each update of BI Engine capacity, including the current state.

The `INFORMATION_SCHEMA.BI_CAPACITY_CHANGES` view has the following schema:

Column name | Data type | Value  
---|---|---  
`change_timestamp` | `TIMESTAMP` | Timestamp when the current update to BI Engine capacity was made.  
`project_id` | `STRING` | The project ID of the project that contains BI Engine capacity.  
`project_number` | `INTEGER` | The project number of the project that contains BI Engine capacity.  
`bi_capacity_name` | `STRING` | The name of the object. There can only be one capacity per project, hence the name is always `default`.  
`size` | `INTEGER` | BI Engine RAM in bytes.  
`user_email` | `STRING` | Email address of the user or subject of the [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) that made the change. `google` for changes made by Google. `NULL` if the email address is unknown.   
`preferred_tables` | `REPEATED STRING` | The set of preferred tables this BI Engine capacity must be used for. If set to `null`, BI Engine capacity is used for all queries in the current project.  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Syntax

Queries against this view must include a [region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax). A project ID is optional. If no project ID is specified, the project that the query runs in is used.

View name | Resource scope | Region scope  
---|---|---  
`[PROJECT_ID.]`region-REGION`.INFORMATION_SCHEMA.BI_CAPACITY_CHANGES` | Project level | `REGION`  
Replace the following: 

  * Optional: `PROJECT_ID`: the ID of your Google Cloud project. If not specified, the default project is used. 
  * `REGION`: any [dataset region name](https://docs.cloud.google.com/bigquery/docs/locations). For example, ``region-us``. 

**Note:** You must use [a region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#region_qualifier) to query `INFORMATION_SCHEMA` views. The location of the query execution must match the region of the `INFORMATION_SCHEMA` view. 



    
    
    -- Returns the history of BI Engine capacity.
    SELECT * FROM myproject.`region-us`.INFORMATION_SCHEMA.BI_CAPACITY_CHANGES;
    

## Examples

The following example retrieves the current BI Engine capacity changes from the `INFORMATION_SCHEMA.BI_CAPACITY_CHANGES` view.

To run the query against a project other than the project that the query is running in, add the project ID to the region in the following format: ``project_id`.`region_id`.INFORMATION_SCHEMA.BI_CAPACITY_CHANGES`.

The following example gets all changes made to BI Engine capacity by a user with email `email@mycompanymail.com`:
    
    
    SELECT *
    FROM `my-project-id.region-us`.INFORMATION_SCHEMA.BI_CAPACITY_CHANGES
    WHERE user_email = "email@mycompanymail.com"
    

The result looks similar to the following:
    
    
      +---------------------+---------------+----------------+------------------+--------------+---------------------+----------------------------------------------------------------------------------------+
      |  change_timestamp   |  project_id   | project_number | bi_capacity_name |     size     |     user_email      |                                               preferred_tables                         |
      +---------------------+---------------+----------------+------------------+--------------+---------------------+----------------------------------------------------------------------------------------+
      | 2022-06-14 02:22:18 | my-project-id |   123456789000 | default          | 268435456000 | email@mycompany.com | ["my-project-id.dataset1.table1","bigquery-public-data.chicago_taxi_trips.taxi_trips"] |
      | 2022-06-08 20:25:51 | my-project-id |   123456789000 | default          | 268435456000 | email@mycompany.com | ["bigquery-public-data.chicago_taxi_trips.taxi_trips"]                                 |
      | 2022-04-01 21:06:49 | my-project-id |   123456789000 | default          | 161061273600 | email@mycompany.com | [""]                                                                                   |
      +---------------------+---------------+----------------+------------------+--------------+---------------------+----------------------------------------------------------------------------------------+
      

The following example gets BI Engine capacity changes for the last seven days:
    
    
    SELECT
      change_timestamp,
      size,
      user_email,
      preferred_tables
    FROM `my-project-id.region-us`.INFORMATION_SCHEMA.BI_CAPACITY_CHANGES
    WHERE change_timestamp > TIMESTAMP_SUB(CURRENT_DATE(), INTERVAL 7 DAY)
    

The result looks similar to the following:
    
    
      +---------------------+--------------+----------------------+-------------------+
      |  change_timestamp   |     size     |     user_email       |  preferred_tables |                                                                                    |
      +---------------------+--------------+----------------------+-------------------+
      | 2023-07-08 18:25:09 | 268435456000 | sundar@mycompany.com | [""]              |
      | 2023-07-09 17:47:26 | 161061273600 | pichai@mycompany.com | ["pr.dataset.t1"] |
      +---------------------+--------------+----------------------+-------------------+
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
