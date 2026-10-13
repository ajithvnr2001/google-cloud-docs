---
url: https://docs.cloud.google.com/sql/docs/sqlserver/replication/enable-cdc/
title: Enable change data capture (CDC) \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:25:12.399996+00:00
---

# Enable change data capture (CDC)  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/replication/enable-cdc/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Enable change data capture (CDC) Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page describes how to enable [change data capture (CDC)](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/about-change-data-capture-sql-server?view=sql-server-ver16) in Cloud SQL for SQL Server. This feature is available for the databases of your instances.

CDC enables you to capture many types of changes. For information about enabling and disabling CDC, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-data-capture-sql-server?view=sql-server-ver16).

After you [connect](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview) to an instance, the `sqlserver` [user](https://docs.cloud.google.com/sql/docs/sqlserver/users) can do many [CDC operations](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-data-capture-sql-server?view=sql-server-ver16).

Also see [Work with Change Data](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/work-with-change-data-sql-server?view=sql-server-ver16).

## Before you begin

Before you implement CDC on an instance, review all of the information on this page.

### Confirm feature availability

CDC is available for the following Cloud SQL for SQL Server database versions:

  * SQL Server 2022 Standard
  * SQL Server 2022 Enterprise
  * SQL Server 2019 Standard
  * SQL Server 2019 Enterprise
  * SQL Server 2017 Standard
  * SQL Server 2017 Enterprise

**Note:** Beginning April 12, 2027, you won't be able to create new instances of Cloud SQL for SQL Server 2017. Starting on October 13, 2027, SQL Server 2017 will reach end of life (EOL) and Microsoft will stop releasing [security updates](https://learn.microsoft.com/en-us/sql/sql-server/end-of-support/sql-server-end-of-support-overview?view=sql-server-ver17#understand-the-sql-server-lifecycle). Cloud SQL for SQL Server will stop supporting SQL Server 2017 after this date.

## Enabling CDC and starting CDC capture jobs

Your database has the following stored procedures, for use by the `sqlserver` user:

  * `msdb.dbo.gcloudsql_cdc_enable_db`
  * `msdb.dbo.gcloudsql_cdc_disable_db`



### Turn CDC on

To turn this feature on for a database, execute the necessary stored procedure and pass in the database name. For example:
    
    
    EXEC msdb.dbo.gcloudsql_cdc_enable_db 'DATABASE_NAME'

### Turn CDC off

To turn this feature off for a database, run a command such as the following:
    
    
    EXEC msdb.dbo.gcloudsql_cdc_disable_db 'DATABASE_NAME'

### Start CDC capture jobs

After CDC is enabled, jobs are created for capture and cleanup. The jobs are invisible to the `sqlserver` user in SQL Server Management Studio (SSMS). However, you can modify the jobs using built-in stored procedures. Additionally, the jobs are viewable via the following stored procedure:

  * `[sys.sp_cdc_help_jobs](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sys-sp-cdc-help-jobs-transact-sql?view=sql-server-ver16)`



To start a cleanup job, you could use the following command:
    
    
    EXEC sys.sp_cdc_start_job @job_type = N'cleanup'
    

To change the job parameters, you could use a command similar to the following, for example:
    
    
    EXEC sys.sp_cdc_change_job  @job_type = N'capture',
            @maxtrans = 20,
            @pollinginterval = NULL,
            @maxscans = NULL,
            @continuous = NULL
    

For more information about starting and changing jobs, see the following:

  * `[sys.sp_cdc_start_job](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sys-sp-cdc-start-job-transact-sql?view=sql-server-ver16)`
  * `[sys.sp_cdc_change_job](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sys-sp-cdc-change-job-transact-sql?view=sql-server-ver16)`



Also see `[sys.sp_cdc_add_job](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sys-sp-cdc-add-job-transact-sql?view=sql-server-ver16)`.

## Enabling CDC for a table

After you turn on CDC for a database, any user with dbo (database owner) access can set up tracking for tables in the database.

For information about the standard CDC commands and options, see [Enable and Disable Change Data Capture](https://docs.microsoft.com/en-us/sql/relational-databases/track-changes/enable-and-disable-change-data-capture-sql-server?view=sql-server-ver16).

### Track changes in a table

To track a table, use the `sys.sp_cdc_enable_table` stored procedure.

For example, you could specify a command similar to the following:
    
    
    EXEC sys.sp_cdc_enable_table
      @source_schema = N'dbo',
      @source_name = N'customer',
      @role_name = N'CDC'
    

### Check if CDC is enabled on a table

To check if CDC is enabled on a table, use the `sys.sp_cdc_help_change_data_capture` stored procedure.

For example, you could specify a command similar to the following:
    
    
    EXECUTE sys.sp_cdc_help_change_data_capture
      @source_schema = N'dbo',
      @source_name = N'customer'
    

### Query changes via a CDC change table

To view CDC changes made on a table, use a `SELECT` query on the table that automatically is created when CDC is enabled on that table.

The table is named as follows:
    
    
    <schema>_<table_name>_CT
    

For example, you could specify a command similar to the following:
    
    
    SELECT * FROM cdc.dbo_customer_CT
    

### Enable CDC on a table with a capture instance specified

To track a table with a "capture instance", use the `sys.sp_cdc_enable_table` stored procedure.

For example, you could specify a command similar to the following:
    
    
    EXEC sys.sp_cdc_enable_table
        @source_schema = N'dbo',
        @source_name = N'customer',
        @role_name = N'CDC',
        @capture_instance = N'customer_cdc',
        @supports_net_changes = 1
    

### Query all changes within a capture instance

To view CDC changes made on a table within a "capture instance", use the `cdc.fn_cdc_get_all_changes_<capture_instance>` stored procedure.

For example, you could specify a SQL statement similar to the following:
    
    
    DECLARE @from_lsn binary(10), @to_lsn binary(10)
    SET @from_lsn = sys.fn_cdc_get_min_lsn(N'customer_cdc')
    SET @to_lsn = sys.fn_cdc_get_max_lsn()
    SELECT * FROM cdc.fn_cdc_get_all_changes_customer_cdc(@from_lsn, @to_lsn, N'all');
    

## Disabling CDC for a table

To disable CDC tracking for a table, use the `sys.sp_cdc_disable_table` stored procedure. Specify a capture instance to disable it. Alternatively, specify a capture instance as `'all'`.

For example, you could specify a command similar to the following to disable CDC for the table:
    
    
    EXEC sys.sp_cdc_disable_table
      @source_schema = N'dbo',
      @source_name = N'customer',
      @capture_instance = N'all'
    

## Deleting a CDC-enabled database

If CDC is enabled for a database and you try to delete it, then you may encounter errors. If this occurs, disable CDC for the database, and then delete the database.

For example, you can specify a command similar to the following to disable and delete a database:
    
    
    EXEC msdb.dbo.gcloudsql_cdc_disable_db 'DATABASE_NAME'
    DROP DATABASE 'DATABASE_NAME'

If you can't delete the database because it has open connections, then use the following query to see those connections:
    
    
    select db_name(dbid),* from sys.sysprocesses where db_name(dbid)= 'DATABASE_NAME'

Close all open connections. Disable CDC for the database, and then delete the database.

## Importing a CDC-enabled database

When importing a CDC-enabled database, Cloud SQL for SQL Server keeps the [KEEP_CDC](https://docs.microsoft.com/en-us/sql/t-sql/statements/restore-statements-arguments-transact-sql?view=sql-server-ver15#change_data_capture_with_option) flag enabled and automatically creates capture and cleanup jobs with default parameters.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
