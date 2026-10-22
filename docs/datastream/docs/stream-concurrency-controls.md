---
url: https://docs.cloud.google.com/datastream/docs/stream-concurrency-controls/
title: Stream concurrency controls \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:02.238606+00:00
---

# Stream concurrency controls  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/stream-concurrency-controls/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Stream concurrency controls Stay organized with collections  Save and categorize content based on your preferences. 

This page provides an overview of stream concurrency controls, such as the maximum number of concurrent change data capture (CDC) tasks and backfill tasks. You can control stream performance by increasing or decreasing the values of these parameters.

## Concurrency controls overview

By using the concurrency controls, you can either achieve faster backfill and CDC, or balance the load on the source database. If you require higher throughputs, and can afford a higher load on the database, then you can increase the concurrency of CDC and backfill tasks. Conversely, if your database is experiencing a high load, and you want to protect it from being overloaded, then you can reduce the values of these parameters.

**Note:** The maximum number of concurrent CDC and backfill tasks parameters are independent of each other. Because of the potential impact that the parameters can have on the source database, we recommend that you modify their values incrementally to see how your system responds.

### Maximum number of CDC tasks

**Note:** This configuration is only available for MySQL and Oracle sources. CDC in PostgreSQL and SQL Server is single-threaded. For information about how to overcome this limitation for PostgreSQL, see [Diagnose issues](https://docs.cloud.google.com/datastream/docs/diagnose-issues#psql-errors).

The `maxConcurrentCdcTasks` parameter lets you control the number of CDC tasks that a stream runs in parallel. To extend the CDC throughput, increase the value of this parameter and allow Datastream to process more CDC log files at the same time.

The key characteristics of the parameter include:

  * The default value is `5`. You can set this parameter to any value between `1` and `50`, inclusive.
  * The parameter is applicable only to Oracle and MySQL sources.
  * The parameter has impact only if there are more database log files available to read than there are CDC tasks. The log files settings are controlled by the source database configuration parameters: the maximum log file size and the maximum log rotation time interval. For more information about these parameters, refer to Oracle and MySQL documentation.
  * If you decrease the number of concurrent CDC tasks, Datastream might lag behind the database logs, which might eventually lead to log position loss and stream failure.



### Maximum number of backfill tasks

The `maxConcurrentBackfillTasks` parameter lets you control the number of backfill tasks that a stream can run in parallel. You can increase or decrease this value to control the backfill throughput.

The key characteristics of the parameter include:

  * The default value is `15`. You can set this parameter to any value between `1` and `50`, inclusive.
  * There is a high risk associated with increasing the backfill concurrency, because backfill tasks have significant impact on the database performance. Each backfill task runs an unfiltered `SELECT` query on a table, and for large tables, such queries return a large number of rows.
  * If you decrease the backfill concurrency, it has no negative impact on the source database except for the backfill taking a longer time to complete.



## Change the values of concurrency controls

You can change the values of concurrency control parameters using the Datastream API.

  * To learn how to increase or decrease the number of concurrent CDC tasks, see [Change the number of maximum concurrent CDC tasks](https://docs.cloud.google.com/datastream/docs/manage-streams#change_the_number_of_maximum_concurrent_cdc_tasks).
  * To learn how to increase or decrease the number of concurrent backfill tasks, see [Change the number of maximum concurrent backfill tasks](https://docs.cloud.google.com/datastream/docs/manage-streams#change_the_number_of_maximum_concurrent_backfill_tasks)



## What's next

  * See [managing streams](https://docs.cloud.google.com/datastream/docs/manage-streams) to learn more about how to use the Datastream API.
  * See the [Datastream API reference documentation](https://docs.cloud.google.com/datastream/docs/reference/rest/v1/projects.locations.streams) to learn more about the `Stream` resource.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
