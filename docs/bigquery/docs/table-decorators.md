---
url: https://docs.cloud.google.com/bigquery/docs/table-decorators/
title: Table decorators in legacy SQL \u00a0|\u00a0 BigQuery \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:45:16.016126+00:00
---

# Table decorators in legacy SQL  |  BigQuery  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/table-decorators/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ BigQuery ](https://docs.cloud.google.com/bigquery/docs)
  * [ Reference ](https://docs.cloud.google.com/bigquery/quotas)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Table decorators in legacy SQL

**Caution:** This document describes table decorators in legacy SQL query syntax. The preferred query syntax for BigQuery is GoogleSQL. Standard SQL does not support table decorators, but the [`FOR SYSTEM_TIME AS OF`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/query-syntax#for_system_time_as_of) clause in GoogleSQL provides functionality equivalent to time decorators. For range decorators, you can achieve similar semantics in GoogleSQL by using time-partitioned tables. For more information, see [Table decorators](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/migrating-from-legacy-sql#table_decorators) in the GoogleSQL migration guide and [Legacy SQL feature availability](https://docs.cloud.google.com/bigquery/docs/legacy-sql-feature-availability).

Normally, BigQuery performs a full column scan when [running a query](https://docs.cloud.google.com/bigquery/docs/running-queries). You can use table decorators in legacy SQL to perform a more cost-effective query of a subset of your data. Table decorators can be used whenever a table is read, such as when copying a table, [exporting a table](https://docs.cloud.google.com/bigquery/docs/export-intro), or listing data using `tabledata.list`.

**Note:** Range decorators aren't supported in GoogleSQL. To view the status of this feature request, see the [BigQuery feature request tracker](https://issuetracker.google.com/issues/35905931). You can click the **Vote for this issue and get email notifications** icon (the star) to register your support for the feature.

Table decorators support relative and absolute `<time>` values. Relative values are indicated by a negative number, and absolute values are indicated by a positive number. For example, `-3600000` indicates one hour ago in milliseconds, relative to the current time; `3600000` indicates one hour in milliseconds after 1/1/1970.

## Time decorators

Time decorators (formerly known as _snapshot decorators_) reference a table's historical data at a point in time.

### Syntax
    
    
    @_< time>_

  * References a table's historical data at `_< time>_`, in milliseconds since the epoch.
  * `_< time>_` must be within the last seven days and greater than or equal to the table's creation time, but less than the table's deletion or expiration time.
  * `@0` is a special case that references the oldest data available for the table.



Time decorators are also used outside of legacy SQL. You can use them in the [`bq cp` command](https://docs.cloud.google.com/bigquery/docs/reference/bq-cli-reference#bq_cp) to [restore deleted tables](https://docs.cloud.google.com/bigquery/docs/restore-deleted-tables) within seven days of table deletion.

### Examples

To get the historical data for a table at one hour ago:

**Relative value example**
    
    
    #legacySQL
    SELECT COUNT(*) FROM [PROJECT_ID:DATASET.TABLE@-3600000]
    

**Absolute value example**

  1. Get `_< time>_` for one hour ago:
         
         #legacySQL
         SELECT INTEGER(DATE_ADD(USEC_TO_TIMESTAMP(NOW()), -1, 'HOUR')/1000)
         

  2. Then, replace `_< time>_` in the following query:
         
         #legacySQL
         SELECT COUNT(*) FROM [PROJECT_ID:DATASET.TABLE@time]
         




## Range decorators

### Syntax
    
    
    @_< time1>_-_< time2>_

  * References table data added between `_< time1>_` and `_< time2>_`, in milliseconds since the epoch.
  * `_< time1>_` and `_< time2>_` must be within the last seven days.
  * `_< time2>_` is optional and defaults to 'now'.



### Examples

**Relative value examples**

To get table data added between one hour and half an hour ago:
    
    
    #legacySQL
    SELECT COUNT(*) FROM [PROJECT_ID:DATASET.TABLE@-3600000--1800000]
    

To get data from the last 10 minutes:
    
    
    #legacySQL
    SELECT COUNT(*) FROM [PROJECT_ID:DATASET.TABLE@-600000-]
    

**Absolute value example**

To get table data added between one hour and half an hour ago:

  1. Get `_< time1>_` for one hour ago:
         
         #legacySQL
         SELECT INTEGER(DATE_ADD(USEC_TO_TIMESTAMP(NOW()), -1, 'HOUR')/1000)
         

  2. Get `_< time2>_` for a half hour ago:
         
         #legacySQL
         SELECT INTEGER(DATE_ADD(USEC_TO_TIMESTAMP(NOW()), -30, 'MINUTE')/1000)
         

  3. Replace `_< time1>_` and `_< time2>_` in the following query:
         
         #legacySQL
         SELECT COUNT(*) FROM [PROJECT_ID:DATASET.TABLE@time1-time2]
         




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
