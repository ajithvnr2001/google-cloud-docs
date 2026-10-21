---
url: https://docs.cloud.google.com/sql/docs/sqlserver/manage-tempdb/
title: Manage a tempdb database \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:54.537244+00:00
---

# Manage a tempdb database  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/manage-tempdb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Manage a tempdb database Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes management of the tempdb database in Cloud SQL.

The tempdb database is a system database that holds many objects, including temporary tables, stored procedures, and more. In your instances, you can perform common operations on this database.

A tempdb database is recreated each time an instance is restarted. To prevent the loss of user permissions, Cloud SQL provides permissions to the `sqlserver` user after an instance is restarted.

## Overview

The `sqlserver` [user](https://docs.cloud.google.com/sql/docs/sqlserver/users) has the ALTER permission for managing the tempdb database options.

For more information about managing this resource, see the [tempdb database](https://docs.microsoft.com/en-us/sql/relational-databases/databases/tempdb-database) page.

## Manage tempdb files

After you [connect](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) to an instance, the `sqlserver` [user](https://docs.cloud.google.com/sql/docs/sqlserver/users) can manage the tempdb files.

## Number of files

The user has ALTER permission on the tempdb database, which lets them control settings for the number of files and more.

When adding files, you must use the `/var/opt/mssql/data/` directory for the physical path.

Some example operations include the following:

  * Add a file:
        
        ALTER DATABASE [tempdb] ADD FILE (NAME = LOGICAL_FILENAME, FILENAME = PHYSICAL_FILENAME, SIZE = SIZE)
        

Make the following replacements:

    * `LOGICAL_FILENAME`: the logical name of the file. For example, `tempdev4`.
    * `PHYSICAL_FILENAME`: the complete path to the file. For example, `/var/opt/mssql/data/tempdb4.ndf`.
    * `SIZE`: the size of the file. For example, `1GB`.
  * Remove a file:
        
        ALTER DATABASE [tempdb] REMOVE FILE LOGICAL_FILENAME
        

Make the following replacement:

    * `LOGICAL_FILENAME`: the logical name of the file. For example, `tempdev4`.

**Note:** See [Physical properties of tempdb in SQL Server](https://docs.microsoft.com/en-us/sql/relational-databases/databases/tempdb-database?view=sql-server-ver15#physical-properties-of-tempdb-in-sql-server), which includes recommendations related to these settings. Review the information about the number of tempdb data files that would correspond to a given number of logical processors. By default, Cloud SQL creates a minimum of eight files for instances that have greater than or equal to eight logical processors. As included in those recommendations, if the number of logical processors is fewer than or equal to eight, the number of files created is equal to the number of logical processors.

## File size

The following sections describe methods used to control the size of files in the `tempdb` database.

For more information about these methods, see [Shrink the tempdb database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/shrink-tempdb-database?view=sql-server-ver16).

### Change file sizes in tempdb

To control the size of files in the tempdb database, use the `ALTER DATABASE` statement. For more information, see [ALTER DATABASE (Transact-SQL) File and Filegroup Options](https://docs.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-file-and-filegroup-options?redirectedfrom=MSDN&view=sql-server-ver15).

### Shrink individual file size

`msdb.dbo.gcloudsql_tempdb_shrinkfile` is a [stored procedure](https://learn.microsoft.com/en-us/sql/relational-databases/stored-procedures/stored-procedures-database-engine?view=sql-server-ver16) you can use to shrink an individual file in the `tempdb` database.

This stored procedure provides all the same benefits of the [`DBCC SHRINKFILE`](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-shrinkfile-transact-sql?view=sql-server-ver16) command.

**Caution:** Avoid using shrinkfile operations as a part of regular maintenance; only use when necessary. For more information, see [`DBCC SHRINKFILE`](https://learn.microsoft.com/en-us/sql/t-sql/database-console-commands/dbcc-shrinkfile-transact-sql?view=sql-server-ver16) documentation.

The following are example uses of the `msdb.dbo.gcloudsql_tempdb_shrinkfile` stored procedure and its parameters, executed from the [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio):

  1. Default option
         
         msdb.dbo.gcloudsql_tempdb_shrinkfile @filename = 'FILENAME'

Where:

     * FILENAME: the name of the file to be shrunk. For example, `tempdev`.

This command executes the following SQL Server commands:

     * `USE tempdb`
     * `DBCC SHRINKFILE (@filename)`
  2. `EMPTYFILE`
         
         msdb.dbo.gcloudsql_tempdb_shrinkfile @filename = 'FILENAME', @empty_file=EMPTY_FILE_INT

Where:

     * EMPTY_FILE_INT: an integer value that is either 0 or 1. If 1, then `EMPTYFILE` is passed as an option. This option takes priority over other parameters.

This command executes the following SQL Server commands:

     * `USE tempdb`
     * `DBCC SHRINKFILE (@filename, EMPTYFILE)`
  3. Target size
         
         msdb.dbo.gcloudsql_tempdb_shrinkfile @filename = 'FILENAME', @target_size=TARGET_SIZE_INT

Where:

     * TARGET_SIZE_INT: an integer that represents the target size of the file in megabytes. Passes to the `DBCC SHRINKFILE` command any value that is greater than or equal to zero. For example, `10`.

This command executes the following SQL Server commands. The integer 10 is included as an example:

     * `USE tempdb`
     * `DBCC SHRINKFILE (@filename, 10)`
  4. Target size and truncate only
         
         msdb.dbo.gcloudsql_tempdb_shrinkfile @filename = 'FILENAME', @target_size=10, @truncateonly=TRUNCATE_ONLY_INT

Where:

     * TRUNCATE_ONLY_INT: accepts an integer value of either 0 or 1. If set to 1, then `TRUNCATEONLY` is passed as an option. Target size is ignored if `TRUNCATEONLY` is passed. This option takes priority over `NOTRUNCATE`.

This command executes the following SQL Server commands:

     * `USE tempdb`
     * `DBCC SHRINKFILE (@filename, 10, TRUNCATEONLY)`
  5. Target size and no truncate option
         
         msdb.dbo.gcloudsql_tempdb_shrinkfile @filename = 'FILENAME', @target_size=10, @no_truncate=NO_TRUNCATE_INT

Where:

     * NO_TRUNCATE_INT: accepts an integer value of either 0 or 1. If set to 1, then `NOTRUNCATE` is passed as an option.

This command executes the following SQL Server commands:

     * `USE tempdb`
     * `DBCC SHRINKFILE (@filename, 10, NOTRUNCATE)`



## What's next

  * Learn about [Instance settings](https://docs.cloud.google.com/sql/docs/sqlserver/instance-settings).
  * Learn about [Monitoring Cloud SQL instances](https://docs.cloud.google.com/sql/docs/sqlserver/monitor-instance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
