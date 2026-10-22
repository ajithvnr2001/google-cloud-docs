---
url: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/work-with-oracle-database-redo-log-files/
title: Work with Oracle database redo log files \u00a0|\u00a0 Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:41:08.101890+00:00
---

# Work with Oracle database redo log files  |  Database Migration Service for heterogeneous Oracle to AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/work-with-oracle-database-redo-log-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Oracle to AlloyDB for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/oracle-to-alloydb/scenario-overview)



Send feedback 

#  Work with Oracle database redo log files Stay organized with collections  Save and categorize content based on your preferences. 

Database Migration Service leverages the Oracle LogMiner API, which is part of Oracle Database, to query archived redo log files. These files contain information about the history of activity on a database. Each Oracle database has a set of online redo log files. All transaction records on the database are recorded in the files.

When the current redo log file is rotated (or switched), the archive process [ copies this file into an archive storage](https://docs.oracle.com/en/database/oracle/oracle-database/19/admin/managing-archived-redo-log-files.html#GUID-9BD00F2E-DC98-4871-8D26-FDB40623909C). Meanwhile, the database promotes another file to serve as the current file.

When Database Migration Service uses the Oracle LogMiner API, it doesn't access the online redo log files but only works with the archived log files. Accessing archived redo log files inherently adds some latency to the migration process. This page describes suggested configuration for your Oracle source databases to control the latency impact.

## Set configuration parameters for Oracle redo log files

This design has profound implications on Database Migration Service's potential latency. If Oracle redo log files are switched frequently or kept to a smaller size (for example, < 256MB), Database Migration Service can replicate changes faster.

There are configuration parameters that you can set to control the log file rotation frequency:

  * **Size:** Online redo log files have a minimum size of 4 MB, and the default size is dependent on your operating system. You can modify the size of the log files by creating new online log files and dropping the older log files.

To find the size of the online redo log files, run the following query:
        
        SELECT GROUP#, STATUS, BYTES/1024/1024 MB FROM V$LOG

For self-hosted Oracle, use [ this guide](https://logic.edchen.org/how-to-resize-redo-logs-in-oracle/). For Amazon RDS Oracle, use [ Performing common log-related tasks for Oracle DB instances](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Log.html#Appendix.Oracle.CommonDBATasks.ResizingRedoLogs) in the Amazon RDS documentation.
  * **Time:** The `ARCHIVE_LAG_TARGET` parameter provides an upper limit of how long (in seconds) the current log of the primary database can span. 

This isn't the exact log switch time, because it takes into account how long it will take to archive the log. The default value is `0` (no upper bound), and a reasonable value of `1800` (or 30 minutes) or less is suggested.

You can use the following commands to set the `ARCHIVE_LAG_TARGET` parameter, either during initialization or while the database is up:

    * `SHOW PARAMETER ARCHIVE_LAG_TARGET;` This command displays how many seconds it will take for the current log to span.
    * `ALTER SYSTEM SET ARCHIVE_LAG_TARGET = number-of-seconds;` Use this command to change the upper limit. 

For example, to set the upper limit to 10 minutes (or 600 seconds), enter `ALTER SYSTEM SET ARCHIVE_LAG_TARGET = 600;`


You can switch the redo log files manually by running the following command: 

`ALTER SYSTEM SWITCH LOGFILE;`

Although using this command is effective for testing purposes, we don't recommend it for production use-cases because of the privileges it requires and the significant performance impact on the database.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
