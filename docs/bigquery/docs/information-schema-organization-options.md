---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-organization-options/
title: ORGANIZATION_OPTIONS view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:34:57.446200+00:00
---

# ORGANIZATION_OPTIONS view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-organization-options/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ORGANIZATION_OPTIONS view

You can query the `INFORMATION_SCHEMA.ORGANIZATION_OPTIONS` view to retrieve real-time metadata about BigQuery organization options. This view contains configuration options that are set at the organization level. To view the default values for a configuration option, see [configuration settings](https://docs.cloud.google.com/bigquery/docs/default-configuration#configuration-settings).

## Required permissions

To get organization options metadata, you need the following Identity and Access Management (IAM) permissions:

  * `bigquery.config.get`



The following predefined IAM role includes the permissions that you need in order to get organization options metadata:

  * `roles/bigquery.jobUser`



For more information about granular BigQuery permissions, see [roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control).

## Schema

When you query the `INFORMATION_SCHEMA.ORGANIZATION_OPTIONS` view, the query results contain one row for each configuration option in a project, if that option differs from the default value at the organization level.

The `INFORMATION_SCHEMA.ORGANIZATION_OPTIONS` view has the following schema:

Column name | Data type | Value  
---|---|---  
`option_name` | `STRING` | One of the name values in the options table.  
`option_description` | `STRING` | The option description.  
`option_type` | `STRING` | The data type of the `option_value`.  
`option_value` | `STRING` | The current value of the option.  
  
##### Options table

`option_name` | `option_type` | `option_value`  
---|---|---  
`default_time_zone` | `STRING` | The default time zone for this organization.  
`default_kms_key_name` | `STRING` | The default key name for this organization.  
`default_query_job_timeout_ms` | `STRING` | The default query timeout in milliseconds for this organization.  
`default_interactive_query_queue_timeout_ms` | `STRING` | The default timeout in milliseconds for queued interactive queries for this organization.  
`default_batch_query_queue_timeout_ms` | `STRING` | The default timeout in milliseconds for queued batch queries for this organization.   
`reusable_column_aliases_mode` | `STRING` | Whether reusable column aliases are enabled in this organization.  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Data retention

This view contains currently running sessions and the history of sessions completed in the past 180 days.

## Scope and syntax

Queries against this view must have a [region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax).

View name | Resource scope | Region scope  
---|---|---  
``region-REGION`.INFORMATION_SCHEMA.ORGANIZATION_OPTIONS` | Configuration options within the specified organization. | `REGION`  
  
Replace the following: 

  * `REGION`: any [dataset region name](https://docs.cloud.google.com/bigquery/docs/locations). For example, `region-us`.



## Examples

The following example retrieves the `OPTION_NAME`, `OPTION_TYPE`, and `OPTION_VALUE` columns from the `INFORMATION_SCHEMA.ORGANIZATION_OPTIONS`.
    
    
    SELECT
      option_name, option_type, option_value
    FROM
      `region-us`.INFORMATION_SCHEMA.ORGANIZATION_OPTIONS;

**Note:** `INFORMATION_SCHEMA` view names are case-sensitive.

The result is similar to the following:
    
    
      +--------------------------------------------+-------------+---------------------+
      | option_name                                | option_type | option_value        |
      +--------------------------------------------+-------------+---------------------+
      | default_time_zone                          | STRING      | America/Los_Angeles |
      +--------------------------------------------+-------------+---------------------+
      | default_kms_key_name                       | STRING      | test/testkey1       |
      +--------------------------------------------+-------------+---------------------+
      | default_query_job_timeout_ms               | INT64       | 18000000            |
      +--------------------------------------------+-------------+---------------------+
      | default_interactive_query_queue_timeout_ms | INT64       | 600000              |
      +--------------------------------------------+-------------+---------------------+
      | default_batch_query_queue_timeout_ms       | INT64       | 1200000             |
      +--------------------------------------------+-------------+---------------------+
      

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
