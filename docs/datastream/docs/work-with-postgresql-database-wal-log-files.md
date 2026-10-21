---
url: https://docs.cloud.google.com/datastream/docs/work-with-postgresql-database-wal-log-files/
title: Work with PostgreSQL database WAL log files \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:49.843152+00:00
---

# Work with PostgreSQL database WAL log files  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/work-with-postgresql-database-wal-log-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Work with PostgreSQL database WAL log files Stay organized with collections  Save and categorize content based on your preferences. 

Datastream uses the PostgreSQL WAL (Write Ahead Log) transaction log to read PostgreSQL streams. The log is stored in WAL files on the database server. Each record in the WAL log represents a single change to the actual data in one of the tables in the database.

## Set configuration parameters for PostgreSQL WAL files

It is recommended that you apply the following configuration settings to your PostgreSQL database:

  * `max_slot_wal_keep_size`: set this parameter (available only for PostgreSQL 13 and above) to limit the amount of storage used by the replication slot. This is particularly important for long-running transactions, which, in extreme cases, can lead to the WAL file size taking up the entire storage and crashing the database.

**Note:** Some managed databases, such as Cloud SQL and AlloyDB for PostgreSQL, don't support `max_slot_wal_keep_size`.
  * `statement_timeout`: set this parameter to a selected value to reduce latency caused by long-running transactions. You can also use `statement_timeout` as an alternative precaution measure for databases that don't support `max_slot_wal_keep_size`.

  * `wal_sender_timeout`: set this parameter to `0` (to disable the timeout) or to a value greater than or equal to 10 minutes.




If you plan to create more than 10 streams, or the number of logical replication slots that is used by other resources in addition to the number of planned streams exceeds 10, make sure to modify the following parameters:

  * `max_replication_slots`: increase the value of this parameter, depending on the number of replication slots set for your database (you need 1 replication slot per stream). You can only set `max_replication_slots` at server start.

  * `max_wal_senders`: increase the value of this parameter, so that it's greater than the value of the `max_replication_slots` parameter. You can only set `max_wal_senders` when you start the server.




## Optimize WAL log files

To avoid high latency of your streams and rapid growth in the size of WAL log files when replicating data from a PostgreSQL source, consider applying the following precautions:

  * Avoid large long-running operations because they can significantly increase the size of your WAL file.
  * Use `UNLOGGED` or `TEMPORARY` tables during batch operations.
  * Check your WAL configuration and consider reducing the checkpoint frequency. For more information, see [WAL configuration](https://www.postgresql.org/docs/current/wal-configuration.html)
  * Check for large `DELETE` operations and consider replacing them with `TRUNCATE` operations. Doing this can significantly reduce WAL file data, however you need to be cautious, because Datastream doesn't replicate `TRUNCATE` operations.



## What's next

  * Learn more about [PostgreSQL as a source](https://docs.cloud.google.com/datastream/docs/sources-postgresql).
  * Learn more about [configuring a source PostgreSQL database](https://docs.cloud.google.com/datastream/docs/configure-your-source-postgresql-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
