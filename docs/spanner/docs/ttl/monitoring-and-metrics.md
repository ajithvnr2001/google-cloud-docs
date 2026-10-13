---
url: https://docs.cloud.google.com/spanner/docs/ttl/monitoring-and-metrics/
title: TTL metrics and monitoring \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:32:31.278170+00:00
---

# TTL metrics and monitoring  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/ttl/monitoring-and-metrics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  TTL metrics and monitoring Stay organized with collections  Save and categorize content based on your preferences. 

This page discusses Spanner time to live (TTL) metrics. To learn more, see [About TTL](https://docs.cloud.google.com/spanner/docs/ttl).

## Metrics

Spanner provides information about TTL activities in a system table that can be read with SQL queries, and as metrics accessed through [Cloud Monitoring](https://docs.cloud.google.com/spanner/docs/monitoring-cloud).

The system table reports TTL information per table for a database, while Cloud Monitoring reports metrics at a database level.

### Use a SQL query

Spanner provides a built-in table that tracks information related to TTL. The table is named `SPANNER_SYS.ROW_DELETION_POLICIES` and has the following schema.

Column name | Type | Description  
---|---|---  
TABLE_NAME | STRING | The name of the table that contains this TTL policy.  
PROCESSED_WATERMARK | TIMESTAMP | This policy has run against all rows in the table as of this time. Some table partitions may have been processed more recently, so this timestamp represents the least-recently processed partition. Typically, this is within 72 hours.  
UNDELETABLE_ROWS | INT64 | The number of rows that cannot be deleted by the TTL policy. See Undeletable rows for more details.  
MIN_UNDELETABLE_TIMESTAMP | TIMESTAMP | The oldest timestamp for undeletable rows that was observed during the last processing cycle.  
  
The deletion policy information is returned per table for your database.

You can query this data with a SQL query similar to the following:
    
    
    SELECT TABLE_NAME, UNDELETABLE_ROWS
    FROM SPANNER_SYS.ROW_DELETION_POLICIES
    WHERE UNDELETABLE_ROWS > 0
    

The `SPANNER_SYS` tables are only accessible through SQL interfaces; for example:

  * The **Spanner Studio** page in the Google Cloud console
  * The `gcloud spanner databases execute-sql` command
  * The `executeQuery` API



Other single read methods that Spanner provides don't support `SPANNER_SYS`.

### Use Cloud Monitoring

Spanner provides the following metrics to monitor TTL activity at a database level:

  * `row_deletion_policy/deleted_rows` is the number of rows deleted by the TTL policy.
  * `row_deletion_policy/undeletable_rows` is the number of rows that match the row deletion (GoogleSQL) or `TTL INTERVAL`(PostgreSQL) statement, but that cannot be deleted. This is usually because the row had too many child rows, causing the action to exceed Spanner's [transaction limit](https://docs.cloud.google.com/spanner/quotas#limits_for_creating_reading_updating_and_deleting_data).
  * `row_deletion_policy/processed_watermark_age` is the time between now and the read timestamp used by the last successful cycle (with or without undeletable rows).



These metrics are available through [Cloud Monitoring](https://docs.cloud.google.com/spanner/docs/monitoring-cloud) and the [Google Cloud console](https://docs.cloud.google.com/spanner/docs/monitoring-console).

## Monitor

You can also monitor other TTL activities.

### Find last successful scan

You can find the last snapshot time at which Spanner completed a scan of the table looking for expired rows. To do so as a SQL query:
    
    
    SELECT PROCESSED_WATERMARK
    FROM SPANNER_SYS.ROW_DELETION_POLICIES
    WHERE TABLE_NAME = $name
    

Alternatively, the `row_deletion_policy/process_watermark_age` metric displays similar information, but is expressed as the difference between the current time and the last scan time. The metric is not broken down by table, but represents the oldest scan time of any TTL-enabled tables in the database.

Rows that match a TTL policy are typically deleted within 72 hours of their expiration date. You can [set an alert](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui) on `processed_watermark_age` so that you are notified if it exceeds 72 hours.

If `processed_watermark_age` is older than 72 hours, it may indicate that higher-priority tasks are preventing TTL from running. In this case, we recommend checking [CPU utilization](https://docs.cloud.google.com/spanner/docs/cpu-utilization#recommended-max) and [adding more compute capacity](https://docs.cloud.google.com/spanner/docs/create-manage-instances#change-compute-capacity) if required. If CPU utilization is within the recommended range, check for hotspotting using [Key Visualizer](https://docs.cloud.google.com/spanner/docs/key-visualizer).

### Monitor deleted rows

To monitor TTL activity on your table, graph the `row_deletion_policy/deleted_rows` metric. This metric displays the number of rows deleted over time.

If no data has expired, this metric is empty.

### Monitor undeletable rows

When TTL is unable to delete a row, Spanner automatically retries. If, upon retry, the TTL action cannot be processed, Spanner skips the row and reports it in the `row_deletion_policy/undeletable_rows_count` metric.

You can [set an alert](https://docs.cloud.google.com/monitoring/alerts/using-alerting-ui#create-policy) on the `row_deletion_policy/undeletable_rows_count` to be notified of a non-zero count.

If you find a non-zero count, you can create a query to break down the count by table:
    
    
    SELECT TABLE_NAME, UNDELETABLE_ROWS, MIN_UNDELETABLE_TIMESTAMP
    FROM SPANNER_SYS.ROW_DELETION_POLICIES
    WHERE UNDELETABLE_ROWS > 0
    

To look up the contents of the undeletable row:
    
    
    SELECT *
    FROM $TABLE_NAME
    WHERE $EXPIRE_COL >= $MIN_UNDELETABLE_TIMESTAMP
    

Most commonly, a row deletion failure is due to cascading updates to interleaved tables and indexes such that the resulting transaction size exceeds Spanner's [mutation limits](https://docs.cloud.google.com/spanner/quotas#limits_for_creating_reading_updating_and_deleting_data). You can resolve the issue by updating your schema to add separate [TTL policies on interleaved tables](https://docs.cloud.google.com/spanner/docs/ttl/working-with-ttl#ttl_and_interleaved_tables).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
