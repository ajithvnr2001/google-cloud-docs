---
url: https://docs.cloud.google.com/bigtable/docs/keep-only-latest-value/
title: Keep only the most recent value \u00a0|\u00a0 Bigtable \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:54:20.764177+00:00
---

# Keep only the most recent value  |  Bigtable  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigtable/docs/keep-only-latest-value/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Bigtable ](https://docs.cloud.google.com/bigtable/docs)
  * [ Guides ](https://docs.cloud.google.com/bigtable/docs/overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Keep only the most recent value

This page describes a strategy that lets you keep only the most recent value in a column in a Bigtable table.

All Cloud Bigtable client libraries let you use filters to read the most recent value, or _cell_ , at a given row and column. In some cases, however, you might not ever need to read older versions of your data. You can use a [version-based garbage collection policy](https://docs.cloud.google.com/bigtable/docs/garbage-collection#version-based) that specifies to only keep one cell in a column, but because [it can take up to a week](https://docs.cloud.google.com/bigtable/docs/garbage-collection#overview) for garbage collection to occur, in practice your table might contain older data that you never plan to read.

To keep only the most recent value, we recommend that you use a _delete-then-write_ approach to limit columns in your table to only one cell.

## Delete, then write

To retain only one value in a column, you can send a request that deletes the column and then recreates it with a new value and timestamp in one atomic action.

The following Java pseudocode example shows how this would work. The order is important: the deletion must occur before the write.
    
    
    RowMutation mutation = RowMutation.create(TABLE, ROW_KEY)
                    .deleteCells(COLUMN_FAMILY, COLUMN_QUALIFIER, Range.TimestampRange.unbounded())
                    .setCell((COLUMN_FAMILY, COLUMN_QUALIFIER, TIMESTAMP, VALUE);
    dataClient.mutateRow(mutation);
    

Provide the following: 

  * `TABLE`: the ID of the table
  * `COLUMN_FAMILY`: the column family that contains the column
  * `COLUMN_QUALIFIER`: the column qualifier to delete and recreate
  * `TIMESTAMP`: the new timestamp
  * `VALUE`: the new value for the column



## Timestamp of zero

Previously, we recommended a strategy of always sending writes with a timestamp of 0. You can still use that approach, but because valid timestamps are useful, we recommend the delete-then-write approach instead.

If you set the timestamp for a cell to 0 or any value less than the current time in milliseconds and also use an age-based garbage collection policy, your cell might be deleted the next time garbage collection occurs.

## What's next

  * [Read the overview of write requests.](https://docs.cloud.google.com/bigtable/docs/writes)
  * [View additional examples of write requests.](https://docs.cloud.google.com/bigtable/docs/writing-data)
  * [Explore the Cloud Bigtable client for Java reference documentation.](https://docs.cloud.google.com/java/docs/reference/google-cloud-bigtable/latest/overview)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
