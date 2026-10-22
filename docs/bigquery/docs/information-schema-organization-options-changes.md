---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-organization-options-changes/
title: ORGANIZATION_OPTIONS_CHANGES view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:35:48.929983+00:00
---

# ORGANIZATION_OPTIONS_CHANGES view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-organization-options-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# ORGANIZATION_OPTIONS_CHANGES view

You can query the `INFORMATION_SCHEMA.ORGANIZATION_OPTIONS_CHANGES` view to retrieve real-time metadata about BigQuery configuration changes in an organization. This view reflects organization-level and project-level configuration changes made after January 31, 2024.

## Required permissions

To get the permission that you need to get the configuration changes, ask your administrator to grant you the [BigQuery Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/bigquery#bigquery.admin) (`roles/bigquery.admin`) IAM role on your organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `bigquery.config.update` permission, which is required to get the configuration changes. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Schema

When you query the `INFORMATION_SCHEMA.ORGANIZATION_OPTIONS_CHANGES` view, the query results contain one row for each configuration change in an organization.

The `INFORMATION_SCHEMA.ORGANIZATION_OPTIONS_CHANGES` view has the following schema:

Column name | Data type | Value  
---|---|---  
`update_time` | `TIMESTAMP` | The time the configuration change occurred.  
`username` | `STRING` | For first-party users, it's their user email. For third-party users, it's the name that users set in the third-party identity provider.  
`updated_options` | `JSON` | A JSON object of the configuration options users updated in the change, containing the previous and the new values of updated fields.  
`project_id` | `STRING` | The project ID. This field is empty for organization-level configuration changes.  
`project_number` | `INTEGER` | The project number. This field is empty for the organization-level configuration changes.  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Data retention

This view contains sessions that are running, and the history of sessions completed in the past 180 days.

## Scope and syntax

Queries against this view must have a [region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax).

View name | Resource scope | Region scope  
---|---|---  
``region-REGION`.INFORMATION_SCHEMA.ORGANIZATION_OPTIONS_CHANGES` | Configuration changes within the specified organization. | `REGION`  
  
Replace the following: 

  * `REGION`: any [dataset region name](https://docs.cloud.google.com/bigquery/docs/locations). For example, `US`, or `us-west2`.



## Examples

The following example retrieves all changes of the `default_query_job_timeout_ms option` option:
    
    
    SELECT
      *
    FROM
      `region-REGION`.INFORMATION_SCHEMA.ORGANIZATION_OPTIONS_CHANGES
    WHERE
      updated_options.default_query_job_timeout_ms is not null;

**Note:** `INFORMATION_SCHEMA` view names are case-sensitive.

The result is similar to the following:
    
    
    +----------------+------------+-------------------------+-----------------+------------------------------------------------------------------------------------------------------------------+
    | project_number | project_id | update_time             | username        | updated_options                                                                                                  |
    |----------------|------------|-------------------------|-----------------|------------------------------------------------------------------------------------------------------------------|
    | 4471534625     | myproject1 | 2023-08-22 06:57:49 UTC | user1@gmail.com | {"default_query_job_timeout_ms":{"new":0,"old":1860369},"default_time_zone":{"new":"America/New_York","old":""}} |
    |----------------|------------|-------------------------|-----------------|------------------------------------------------------------------------------------------------------------------|
    | 5027725474     | myproject2 | 2022-08-01 00:00:00 UTC | user2@gmail.com | {"default_query_job_timeout_ms":{"new":1860369,"old":1860008}}                                                   |
    +----------------+------------+-------------------------+-----------------+------------------------------------------------------------------------------------------------------------------+
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
