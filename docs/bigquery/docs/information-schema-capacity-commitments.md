---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-capacity-commitments/
title: CAPACITY_COMMITMENTS view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:43:56.040105+00:00
---

# CAPACITY_COMMITMENTS view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-capacity-commitments/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# CAPACITY_COMMITMENTS view

The `INFORMATION_SCHEMA.CAPACITY_COMMITMENTS` view contains a near real-time list of all current capacity commitments within the administration project. Each row represents a single, current capacity commitment. A current capacity commitment is either pending or active and has not been deleted. For more information about reservation, see [Slot commitments](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management#slot_commitments).

**Note:** The view names `INFORMATION_SCHEMA.CAPACITY_COMMITMENTS` and `INFORMATION_SCHEMA.CAPACITY_COMMITMENTS_BY_PROJECT` are synonymous and can be used interchangeably.

## Required permission

To query the `INFORMATION_SCHEMA.CAPACITY_COMMITMENTS` view, you need the `bigquery.capacityCommitments.list` Identity and Access Management (IAM) permission for the project. Each of the following predefined IAM roles includes the required permission:

  * `roles/bigquery.resourceAdmin`
  * `roles/bigquery.resourceEditor`
  * `roles/bigquery.resourceViewer`
  * `roles/bigquery.user`
  * `roles/bigquery.admin`



For more information about BigQuery permissions, see [Access control with IAM](https://docs.cloud.google.com/bigquery/docs/access-control)

## Schema

The `INFORMATION_SCHEMA.CAPACITY_COMMITMENTS` view has the following schema:

Column name | Data type | Value  
---|---|---  
`ddl` | `STRING` | The DDL statement used to create this capacity commitment.  
`project_id` | `STRING` | ID of the administration project.  
`project_number` | `INTEGER` | Number of the administration project.  
`capacity_commitment_id` | `STRING` | ID that uniquely identifies the capacity commitment.  
`commitment_plan` | `STRING` | Commitment plan of the capacity commitment.  
`state` | `STRING` | State the capacity commitment is in. Can be `PENDING` or `ACTIVE`.  
`slot_count` | `INTEGER` | Slot count associated with the capacity commitment.  
`edition` | `STRING` | The edition associated with this reservation. For more information about editions, see [Introduction to BigQuery editions](https://docs.cloud.google.com/bigquery/docs/editions-intro).  
`is_flat_rate` | `BOOL` | Whether the commitment is associated with the legacy flat-rate capacity model or an edition. If `FALSE`, the current commitment is associated with an edition. If `TRUE`, the commitment is the legacy flat-rate capacity model.  
`renewal_plan` | `STRING` | New commitment plan after the end of current commitment plan. You can change the renewal plan for a commitment at any time until it expires.  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Scope and syntax

Queries against this view must include a [region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax). If you don't specify a regional qualifier, metadata is retrieved from all regions. The following table explains the region scope for this view:

View name | Resource scope | Region scope  
---|---|---  
`[PROJECT_ID.]`region-REGION`.INFORMATION_SCHEMA.CAPACITY_COMMITMENTS[_BY_PROJECT]` | Project level  | `REGION`  
Replace the following: 

  * Optional: `PROJECT_ID`: the ID of your Google Cloud project. If not specified, the default project is used. 
  * `REGION`: any [dataset region name](https://docs.cloud.google.com/bigquery/docs/locations). For example, ``region-us``. 

**Note:** You must use [a region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#region_qualifier) to query `INFORMATION_SCHEMA` views. The location of the query execution must match the region of the `INFORMATION_SCHEMA` view. 




## Example

The following example returns a list of active capacity commitments for the current project:
    
    
    SELECT
      capacity_commitment_id,
      slot_count
    FROM
      `region-us`.INFORMATION_SCHEMA.CAPACITY_COMMITMENTS
    WHERE
      state = 'ACTIVE';

The result is similar to the following:
    
    
    +------------------------+------------+
    | capacity_commitment_id | slot_count |
    +------------------------+------------+
    |    my_commitment_05    |    1000    |
    |    my_commitment_06    |    1000    |
    |    my_commitment_07    |    1500    |
    |    my_commitment_08    |    2000    |
    +------------------------+------------+
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
