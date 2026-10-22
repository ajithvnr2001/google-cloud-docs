---
url: https://docs.cloud.google.com/bigquery/docs/information-schema-reservation-changes/
title: RESERVATION_CHANGES view \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:16.057566+00:00
---

# RESERVATION_CHANGES view  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/information-schema-reservation-changes/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# RESERVATION_CHANGES view

The `INFORMATION_SCHEMA.RESERVATION_CHANGES` view contains a near real-time list of all changes to reservations within the administration project. Each row represents a change to a single reservation. For more information, see [Introduction to reservations](https://docs.cloud.google.com/bigquery/docs/reservations-intro).

**Note:** The view names `INFORMATION_SCHEMA.RESERVATION_CHANGES` and `INFORMATION_SCHEMA.RESERVATION_CHANGES_BY_PROJECT` are synonymous and can be used interchangeably.

## Required permission

To query the `INFORMATION_SCHEMA.RESERVATION_CHANGES` view, you need the `bigquery.reservations.list` Identity and Access Management (IAM) permission on the project. Each of the following predefined IAM roles includes the required permission:

  * BigQuery Resource Admin (`roles/bigquery.resourceAdmin`)
  * BigQuery Resource Editor (`roles/bigquery.resourceEditor`)
  * BigQuery Resource Viewer (`roles/bigquery.resourceViewer`)
  * BigQuery User (`roles/bigquery.user`)
  * BigQuery Admin (`roles/bigquery.admin`)



For more information about BigQuery permissions, see [BigQuery IAM roles and permissions](https://docs.cloud.google.com/bigquery/docs/access-control).

## Schema

The `INFORMATION_SCHEMA.RESERVATION_CHANGES` view has the following schema:

Column name | Data type | Value  
---|---|---  
`change_timestamp` | `TIMESTAMP` | Time when the change occurred.  
`project_id` | `STRING` | ID of the administration project.  
`project_number` | `INTEGER` | Number of the administration project.  
`reservation_name` | `STRING` | User provided reservation name.  
`ignore_idle_slots` | `BOOL` | If false, any query using this reservation can use unused idle slots from other capacity commitments.  
`action` | `STRING` | Type of event that occurred with the reservation. Can be `CREATE`, `UPDATE`, or `DELETE`.  
`slot_capacity` | `INTEGER` | The baseline slot capacity of the reservation.  
`user_email` | `STRING` | Email address of the user or subject of the [workforce identity federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) that made the change. `google` for changes made by Google. `NULL` if the email address is unknown.   
`target_job_concurrency` | `INTEGER` | The target number of queries that can execute simultaneously, which is limited by available resources. If zero, then this value is computed automatically based on available resources.  
`autoscale` | `STRUCT` |  Information about the autoscale capacity of the reservation. Fields include the following:

  * `current_slots`: the number of slots added to the reservation by autoscaling. **Note:** After users reduce `max_slots`, it may take a while before it can be propagated, so `current_slots` may stay in the original value and could be larger than `max_slots` for that brief period (less than one minute). 
  * `max_slots`: the maximum number of slots that could be added to the reservation by autoscaling.

  
`edition` | `STRING` | The edition associated with this reservation. For more information about editions, see [Introduction to BigQuery editions](https://docs.cloud.google.com/bigquery/docs/editions-intro).  
`primary_location` | `STRING` |  The current location of the reservation's primary replica. This field is only set for reservations using the [managed disaster recovery feature](https://docs.cloud.google.com/bigquery/docs/managed-disaster-recovery).   
`secondary_location` | `STRING` | The current location of the reservation's secondary replica. This field is only set for reservations using the [managed disaster recovery feature](https://docs.cloud.google.com/bigquery/docs/managed-disaster-recovery).  
`original_primary_location` | `STRING` | The location where the reservation was originally created.  
`labels` | `RECORD` | Array of labels associated with the reservation.  
`reservation_group_path` | `ARRAY<STRING>` | The reservation group to which the reservation is linked. For example, if the reservation is linked to group `my-group`, the `reservation_group_path` field contains a list such as: `[my-group]`.  
`max_slots` | `INTEGER` | The maximum number of slots that this reservation can use, which includes baseline slots (`slot_capacity`), idle slots (if `ignore_idle_slots` is false), and autoscale slots. This field is specified by users for using the [reservation predictability feature](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management#predictable).  
`scaling_mode` | `STRING` | The scaling mode for the reservation, which determines how the reservation scales from baseline to `max_slots`. This field is specified by users for using the [reservation predictability feature](https://docs.cloud.google.com/bigquery/docs/reservations-workload-management#predictable).  
  
For stability, we recommend that you explicitly list columns in your information schema queries instead of using a wildcard (`SELECT *`). Explicitly listing columns prevents queries from breaking if the underlying schema changes.

## Data retention

This view contains current reservations and deleted reservations that are kept for a maximum of 41 days after which they are removed from the view.

## Scope and syntax

Queries against this view must include a [region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#syntax). If you do not specify a regional qualifier, metadata is retrieved from all regions. The following table explains the region scope for this view:

View name | Resource scope | Region scope  
---|---|---  
`[PROJECT_ID].`region-REGION`.INFORMATION_SCHEMA.RESERVATION_CHANGES[_BY_PROJECT]` | Project level  | `REGION`  
Replace the following: 

  * Optional: `PROJECT_ID`: the ID of your Google Cloud project. If not specified, the default project is used. 
  * `REGION`: any [dataset region name](https://docs.cloud.google.com/bigquery/docs/locations). For example, ``region-us``. 

**Note:** You must use [a region qualifier](https://docs.cloud.google.com/bigquery/docs/information-schema-intro#region_qualifier) to query `INFORMATION_SCHEMA` views. The location of the query execution must match the region of the `INFORMATION_SCHEMA` view. 




## Example

The following example gets the history of changes for a given reservation. Use this information to see the list of changes made to a specific reservation, such as creating or deleting the reservation.
    
    
    SELECT
      *
    FROM
      reservation-admin-project.`region-us`.
      INFORMATION_SCHEMA.RESERVATION_CHANGES
    WHERE
      reservation_name = "my-reservation"
    ORDER BY
      change_timestamp DESC;

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
