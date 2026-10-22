---
url: https://docs.cloud.google.com/datastream/docs/best-practices-cdc-existing-table/
title: Use Datastream with an existing BigQuery table \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:19.040388+00:00
---

# Use Datastream with an existing BigQuery table  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/best-practices-cdc-existing-table/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Resources ](https://docs.cloud.google.com/datastream/docs/quotas)



Send feedback 

#  Use Datastream with an existing BigQuery table Stay organized with collections  Save and categorize content based on your preferences. 

When a standard Datastream backfill takes too long or has product limitations, you can copy initial data into an existing BigQuery table separately. Streaming change data capture (CDC) updates into BigQuery from a specific log position lets you keep the table synchronized without running a built-in backfill.

## Problem

A BigQuery table that's populated using the [BigQuery Storage Write API](https://docs.cloud.google.com/bigquery/docs/change-data-capture) doesn't allow regular data manipulation language (DML) operations. This means that after a CDC stream starts writing to a BigQuery table, there's no way to add historical data that wasn't already prepopulated in the table.

Consider the following scenario:

  1. **TIMESTAMP 1** : the table copy operation is initiated.
  2. **TIMESTAMP 2** : while the table is being copied, DML operations at the source result in changes to the data (rows are added, updated, or removed).
  3. **TIMESTAMP 3** : CDC starts, but changes that occurred during **TIMESTAMP 2** aren't captured, resulting in a data discrepancy.



## Solution

To ensure data integrity, the CDC process must capture all the changes in the source that occurred from the moment immediately following the last update made that was copied into the BigQuery table.

The solution that follows lets you ensure that the CDC process captures all the changes from **TIMESTAMP 2** , without blocking the copy operation from writing data into the BigQuery table.

### Prerequisites

  * The target table in BigQuery must have the exact same schema and configuration as if the table was created by Datastream. You can use the [Datastream BigQuery Migration Toolkit](https://docs.cloud.google.com/datastream/docs/best-practices-migration-toolkit) to accomplish this.
  * For MySQL and Oracle sources, you must be able to identify the log position at the time when the copy operation is initiated.
  * The database must have sufficient storage and an adequate log retention policy to allow the table copy process to complete.



### MySQL and Oracle sources

  1. Create, but don't start the stream that you intend to use for the ongoing CDC replication. The stream needs to be in the **CREATED** state.
  2. When you're ready to start the table copy operation, identify the current log position of the database: 
     * For MySQL, see the [MySQL documentation](https://dev.mysql.com/doc/refman/8.0/en/replication-howto-masterstatus.html) to learn how to obtain the replication binary log coordinates. After you identify the log position, close the session to release any locks on the database.
     * For Oracle, run the following query: `SELECT current_scn FROM V$DATABASE`.
  3. Copy the table from the source database into BigQuery.
  4. After the copy operation completes, follow the steps described on the [Manage streams](https://docs.cloud.google.com/datastream/docs/manage-streams#startastreamfromspecific) page to start the stream from the log position that you identified earlier.



### PostgreSQL sources

  1. When you're ready to start copying the table, create the replication slot. For more information, see [Configure a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).
  2. Copy the table from the source database into BigQuery.
  3. After the copy operation completes, create and start the stream.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
