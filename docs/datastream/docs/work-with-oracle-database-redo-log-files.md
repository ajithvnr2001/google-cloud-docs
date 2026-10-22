---
url: https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files/
title: Work with Oracle database redo log files \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:00.200395+00:00
---

# Work with Oracle database redo log files  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/work-with-oracle-database-redo-log-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Work with Oracle database redo log files Stay organized with collections  Save and categorize content based on your preferences. 

During change data capture, Datastream reads Oracle redo log files to monitor your source databases for changes and replicate them to the destination instance. Each Oracle database has a set of online redo log files. All transaction records on the database are recorded in the files. When the current redo log file is rotated (or switched), the archive process [copies this file into an archive storage](https://docs.oracle.com/cd/B19306_01/server.102/b14231/archredo.htm#i1006148). Meanwhile, the database promotes another file to serve as the current file.

Datastream Oracle connector extracts change data capture (CDC) events from Oracle redo log files.

## Access redo log files

Datastream can use the Oracle LogMiner API or the binary reader method to access the redo log files:

  * **Oracle LogMiner** : an out-of-the-box utility included in Oracle databases. If you configure Datastream to use Oracle LogMiner API, Datastream can only work with _archived_ redo log files, online redo log files aren't supported. The LogMiner API method is single-threaded and is subject to higher latency and lower throughput when working with large transaction number source databases. LogMiner supports most data types and Oracle database features.

  * **Binary reader** ([Preview](https://cloud.google.com/products/#product-launch-stages)): a specialized, high-performance utility that works with both online and archived redo log files. Binary reader can access the log files using Automatic Storage Management (ASM) or by reading the files directly using database directory objects. Binary reader is multithreaded and supports low-latency CDC. It also creates low impact on the source database as redo logs are parsed outside of the database operations. The binary reader CDC method has limited support for certain data types or features. For more information, see [Known limitations](https://docs.cloud.google.com/datastream/docs/sources-oracle#binary-reader-limitations).




## Set configuration parameters for Oracle redo log files

When using the **LogMiner** CDC method, this design has profound implications on Datastream's potential latency. Since LogMiner only reads from archived logs, if Oracle's redo log files are switched frequently or kept to a smaller size (for example, < 256MB), Datastream can replicate changes faster. This does not apply to the **binary reader** method, which reads actively from online redo log files.

There are configuration parameters that you can set to control the log file rotation frequency:

  * **Size:** Online redo log files have a minimum size of 4 MB, and the default size is dependent on your operating system. You can modify the size of the log files by creating new online log files and dropping the older log files.

To find the size of the online redo log files, run the following query:
        
        SELECT GROUP#, STATUS, BYTES/1024/1024 MB FROM V$LOG

When using the **Oracle LogMiner** CDC method, generating very large log files might cause Datastream to time out, which can lead to stream failure. The recommended redo log file size is less than 1GB. This recommendation doesn't apply to the **binary reader** method.

For information about resizing redo logs for a self-hosted Oracle instance, see [How to resize redo logs in Oracle](https://logic.edchen.org/how-to-resize-redo-logs-in-oracle).

For information about resizing redo logs for an Amazon RDS Oracle instance, see [Resizing online redo logs](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.Oracle.CommonDBATasks.Log.html#Appendix.Oracle.CommonDBATasks.ResizingRedoLogs).

  * **Time:** The `ARCHIVE_LAG_TARGET` parameter provides an upper limit of how long (in seconds) the current log of the primary database can span.

This isn't the exact log switch time, because it takes into account how long it will take to archive the log. The default value is `0` (no upper bound), and a reasonable value of `1800` (or 30 minutes) or less is suggested.

You can use the following commands to set the `ARCHIVE_LAG_TARGET` parameter, either during initialization or while the database is up:

    * `SHOW PARAMETER ARCHIVE_LAG_TARGET;` This command displays how many seconds it will take for the current log to span.
    * `ALTER SYSTEM SET ARCHIVE_LAG_TARGET = number-of-seconds;` Use this command to change the upper limit.

For example, to set the upper limit to 10 minutes (or 600 seconds), enter `ALTER SYSTEM SET ARCHIVE_LAG_TARGET = 600;`

You can switch the redo log files manually by running the following command:

`ALTER SYSTEM SWITCH LOGFILE;`

Although using this command is effective for testing purposes, we don't recommend it for production use-cases because of the privileges it requires and the significant performance impact on the database.




## What's next

  * Learn more about [Oracle as a source](https://docs.cloud.google.com/datastream/docs/sources-oracle).
  * Learn more about [configuring a source Oracle database](https://docs.cloud.google.com/datastream/docs/configure-your-source-oracle-database).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
