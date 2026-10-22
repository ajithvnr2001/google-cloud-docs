---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-sessions-by-project/
title: SESSIONS_BY_PROJECT view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:36.987721+00:00
---

# SESSIONS_BY_PROJECT view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-sessions-by-project/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# SESSIONS_BY_PROJECT view

The `INFORMATION_SCHEMA.SESSIONS_BY_PROJECT` view contains real-time metadata about all BigQuery sessions in the current project.

**Note:** The view names `INFORMATION_SCHEMA.SESSIONS` and `INFORMATION_SCHEMA.SESSIONS_BY_PROJECT` are synonymous and can be used interchangeably.

## Required permissions

To query the `INFORMATION_SCHEMA.SESSIONS_BY_PROJECT` view, you need the `bigquery.jobs.listAll` Identity and Access Management (IAM) permission for the project. Each of the following predefined IAM roles includes the required permission:

  * Project Owner
  * BigQuery Admin



For more information about BigQuery permissions, see [Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control).

## Schema

When you query the `INFORMATION_SCHEMA.SESSIONS_BY_*` views, the query results contain one row for each BigQuery session.

The `INFORMATION_SCHEMA.SESSIONS_BY_*` view has the following schema:

**Note:** The underlying data is partitioned by the `creation_time` column and clustered by `project_id` and `user_email`.Column name | Data type | Value  
---|---|---  
`creation_time` | `TIMESTAMP` |  (_Partitioning column_) Creation time of this session. Partitioning is based on the UTC time of this timestamp.   
`expiration_time` | `TIMESTAMP` |  (_Partitioning column_) Expiration time of this session. Partitioning is based on the UTC time of this timestamp.   
`is_active` | `BOOL` |  Is the session is still active? `TRUE` if yes, otherwise `FALSE`.   
`last_modified_time` | `TIMESTAMP` |  (_Partitioning column_) Time when the session was last modified. Partitioning is based on the UTC time of this timestamp.   
`project_id` | `STRING` | (_Clustering column_) ID of the project.  
`project_number` | `INTEGER` | Number of the project.  
`session_id` | `STRING` | ID of the session. For example, `bquxsession_1234`.  
`user_email` | `STRING` |  (_Clustering column_) Email address or service account of the user who ran the session.   
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Data retention

This view contains currently running sessions and the history of sessions completed in the past 180 days.

## Scope and syntax

Queries against this view must include a [region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax). If you do not specify a regional qualifier, metadata is retrieved from all regions. The following table explains the region scope for this view:

View name | Resource scope | Region scope  
---|---|---  
`[PROJECT_ID.]`region-REGION`.INFORMATION_SCHEMA.SESSIONS_BY_PROJECT` | Project level  | `REGION`  
Replace the following: 

  * Optional: `PROJECT_ID`: the ID of your Google Cloud project. If not specified, the default project is used. 
  * `REGION`: any [dataset region name](https://docs.cloud.google.com/bigquery/docs/locations). For example, ``region-us``. 

**Note:** You must use [a region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#region_qualifier) to query `INFORMATION_SCHEMA` views. The location of the query execution must match the region of the `INFORMATION_SCHEMA` view. 




## Example

To run the query against a project other than your default project, add the project ID in the following format: 
    
    
    `PROJECT_ID`.`region-REGION_NAME`.INFORMATION_SCHEMA.SESSIONS_BY_PROJECT

For example, ``myproject`.`region-us`.INFORMATION_SCHEMA.SESSIONS_BY_PROJECT`. The following example lists all users or service accounts that created sessions for a given project within the last day: 
    
    
    SELECT
      DISTINCT(user_email) AS user
    FROM
      `region-us`.INFORMATION_SCHEMA.SESSIONS_BY_PROJECT
    WHERE
      is_active = true
      AND creation_time >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 1 DAY);

**Note:** `INFORMATION_SCHEMA` view names are case-sensitive.

The result is similar to the following:
    
    
    +--------------+
    | user         |
    +--------------+
    | abc@xyz.com  |
    +--------------+
    | def@xyz.com  |
    +--------------+
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
