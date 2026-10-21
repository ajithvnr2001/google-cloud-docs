---
url: https://docs.cloud.google.com/datastream/docs/configure-self-managed-sqlserver/
title: Configure a self-managed SQL Server database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:24:10.650933+00:00
---

# Configure a self-managed SQL Server database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-self-managed-sqlserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a self-managed SQL Server database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

To stream change data capture (CDC) updates from a self-managed SQL Server database with Datastream, you can use either change tables or transaction logs. Both methods replicate changes to [supported destinations](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage. Before creating a stream, you turn on CDC and snapshot isolation, run SQL Server Agent, create a Datastream user, and configure log retention.

## Configure your source database

To configure your source database:

  1. Make sure that your database uses the full recovery model. Connect to the database and run the following command at a SQL prompt or in a terminal:
         
         USE master
         GO
         ALTER DATABASE [DATABASE_NAME] SET RECOVERY FULL
         GO
         

Replace `DATABASE_NAME` with the name of your source database.

**Note:** After setting the recovery model to `FULL`, the database remains in a pseudo-simple recovery state until you take a full database backup. You must perform a full database backup before the transaction log begins retaining records for change data capture.
  2. Enable CDC for your source database. To do it, connect to the database and run the following command at a SQL prompt or in a terminal:
         
         USE [DATABASE_NAME]
         GO
         EXEC sys.sp_cdc_enable_db
         GO
         

Replace `DATABASE_NAME` with the name of your source database.

  3. Enable CDC on the tables for which you need to capture changes:
         
         USE [DATABASE_NAME]
         EXEC sys.sp_cdc_enable_table
         @source_schema = N'SCHEMA_NAME',
         @source_name = N'TABLE_NAME',
         @role_name = NULL
         GO
         

**Note:** You need to run the command for each table for which you want to enable CDC.

Replace the following:

     * `DATABASE_NAME`: the name of your source database
     * `SCHEMA_NAME`: the name of the schema to which the tables belong
     * `TABLE_NAME`: the name of the table for which you want to enable CDC
  4. Start the SQL Server Agent and make sure it's running at all times. If the SQL Server Agent remains down for an extended period, the logs might get truncated, leading to a permanent loss of the change data that wasn't read by Datastream.

For information about running the SQL Server Agent, see [Start, stop, or restart an instance of the SQL Server Agent](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/start-stop-pause-resume-restart-sql-server-services?view=sql-server-ver16#start-stop-or-restart-an-instance-of-the-sql-server-agent).

**Note:** We recommend [setting the automatic restart](https://learn.microsoft.com/en-us/sql/ssms/agent/autorestart-sql-server-agent-sql-server-management-studio?view=sql-server-ver16) on for the SQL Server Agent service to prevent the agent from being down for a longer time.
  5. Enable snapshot isolation.

When you backfill data from your SQL Server database, it's important to ensure consistent snapshots. If you don't apply the settings described in this section, changes made to the database during the backfill process might lead to duplicates or incorrect results. Applying snapshot isolation settings is required if your stream includes tables without primary keys.

Enabling snapshot isolation creates a temporary view of your database at the start of the backfill process. This ensures that the data being copied remains consistent, even if other users are making changes to the live tables at the same time. Enabling snapshot isolation might have a slight performance impact, but it's essential for reliable data extraction.

To enable snapshot isolation:

     1. Connect to your database using a SQL Server client.
     2. Run the following command:
    
    ALTER DATABASE DATABASE_NAME SET ALLOW_SNAPSHOT_ISOLATION ON;
    

Replace DATABASE_NAME with the name of you database.

  6. Create a Datastream user:

     1. Connect to the source database and enter the following command:
            
            USE DATABASE_NAME;
            

     2. Create a login to use while setting up the connection profile in Datastream.
            
            CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';
            

     3. Create a user:
            
            CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
            

     4. Assign the `db_datareader` role to them:
            
            EXEC sp_addrolemember 'db_datareader', 'USER_NAME';
            

     5. Grant the `VIEW DATABASE STATE` permission to them:
            
            GRANT VIEW DATABASE STATE TO USER_NAME;
            

     6. Add this user to the `master` database:
            
            USE master;
            CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
            




## Additional steps required for the transaction logs CDC method

The steps described in this section are only required when you configure your source SQL Server database for use with the transaction logs CDC method.

  1. Connect to the source database and assign the `db_owner` and `db_denydatawriter` roles to your user:
         
         USE DATABASE_NAME;
         EXEC sp_addrolemember 'db_owner', 'USER_NAME';
         EXEC sp_addrolemember 'db_denydatawriter', 'USER_NAME';
         

  2. Grant `SELECT` permissions for the `sys.fn_dblog` function.
         
         USE master;
         GRANT SELECT ON sys.fn_dblog TO USER_NAME;
         

  3. Add your user to the msdb database and assign the following permissions to them:
         
         USE msdb;
         CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
         GRANT SELECT ON dbo.sysjobs TO USER_NAME;
         

  4. Assign the following permissions to your user in the `master` database:
         
         USE master;
           GRANT VIEW SERVER STATE TO YOUR_LOGIN;
         

  5. Set the polling interval for which you want the changes to be available on your source.
         
         USE [DATABASE_NAME]
         EXEC sys.sp_cdc_change_job @job_type = 'capture' , @pollinginterval = 86399
         EXEC sp_cdc_stop_job 'capture'
         EXEC sp_cdc_start_job 'capture'
         

The `@pollinginterval` parameter is measured in seconds with a recommended value set to `86399`. This means that the transaction log retains changes for 86,399 seconds (one day). Executing the `sp_cdc_start_job 'capture` procedure initiates the settings.

  6. If there are any cleanup or capture jobs running on your database, stop them. For more information, see [Administer and monitor change data capture](https://learn.microsoft.com/en-us/sql/relational-databases/track-changes/administer-and-monitor-change-data-capture-sql-server).

  7. Set up a log truncation safeguard.

To make sure that the CDC reader has enough time to read the logs while allowing log truncation to prevent using up the storage space, you can set up a log truncation safeguard:

     1. Connect to the database using a SQL Server client.
     2. Create a stored procedure that runs an active transaction for a period that you specify to prevent log truncation:
            
            CREATE PROCEDURE dbo.DatastreamLogTruncationSafeguard @transaction_logs_retention_time INT
            AS
            BEGIN
            
            DECLARE @transactionLog TABLE (beginLSN BINARY(10), endLSN BINARY(10))
            INSERT @transactionLog EXEC sp_repltrans
            
            DECLARE @currentDateTime DATETIME = GETDATE()
            DECLARE @cutoffDateTime DATETIME = DATEADD(MINUTE, -@transaction_logs_retention_time, @currentDateTime)
            
            DECLARE @firstValidLSN BINARY(10) = NULL
            DECLARE @lastValidLSN BINARY(10) = NULL
            DECLARE @firstTxnTime DATETIME = NULL
            DECLARE @lastTxnTime DATETIME = NULL
            
            SELECT TOP 1
                @lastTxnTime = t.logStartTime,
                @lastValidLSN = t.beginLSN
            FROM (
              SELECT
                beginLSN AS beginLSN,
                (SELECT TOP 1 [begin time]
                FROM fn_dblog(stuff(stuff(CONVERT(CHAR(24), beginLSN, 1), 19, 0, ':'), 11, 0, ':'), DEFAULT)) AS logStartTime
              FROM @transactionLog
            ) t
            ORDER BY t.beginLSN DESC
            
            -- If all transactions are before cutoff, clear everything
            IF (@lastTxnTime < @cutoffDateTime)
            BEGIN
                EXEC sp_repldone NULL, NULL, 0, 0, 1
            END
            ELSE
            BEGIN
                -- Find the earliest transaction
                SELECT TOP 1
                  @firstTxnTime = t.logStartTime,
                  @firstValidLSN = ISNULL(@firstValidLSN, t.beginLSN)
                FROM (
                  SELECT
                    beginLSN AS beginLSN,
                    (SELECT TOP 1 [begin time]
                    FROM fn_dblog(stuff(stuff(CONVERT(CHAR(24), beginLSN, 1), 19, 0, ':'), 11, 0, ':'), DEFAULT)) AS logStartTime
                  FROM @transactionLog
                ) t
                ORDER BY t.beginLSN ASC
            
                IF (@firstTxnTime < @cutoffDateTime)
                BEGIN
                    -- Identify the earliest and latest LSNs within VLogs before cutoff
                    SELECT
                      @firstValidLSN = SUBSTRING(MAX(t.lsnMarkers), 1, 10),
                      @lastValidLSN = SUBSTRING(MAX(t.lsnMarkers), 11, 10)
                    FROM (
                      SELECT MIN(beginLSN + endLSN) AS lsnMarkers
                      FROM @transactionLog
                      GROUP BY SUBSTRING(beginLSN, 1, 4)
                    ) t
                    WHERE (
                      SELECT TOP 1 [begin time]
                      FROM fn_dblog(stuff(stuff(CONVERT(CHAR(24), SUBSTRING(t.lsnMarkers, 1, 10), 1), 19, 0, ':'), 11, 0, ':'), DEFAULT)
                      WHERE Operation = 'LOP_BEGIN_XACT'
                    ) < @cutoffDateTime
            
                    EXEC sp_repldone @firstValidLSN, @lastValidLSN, 0, 0, 0
                END
              END
            END;
            

     3. Create another stored procedure. This time, you create a job that runs the stored procedure that you created in the previous step according to a specified cadence:
            
            CREATE PROCEDURE [dbo].[SetUpDatastreamJob] @transaction_logs_retention_time INT
            AS
            BEGIN
            
            DECLARE @database_name VARCHAR(MAX)
              SET @database_name =  (SELECT DB_NAME());;
            
              DECLARE @command_str VARCHAR(MAX);
              SET @command_str = CONCAT('Use ', @database_name,'; exec dbo.DatastreamLogTruncationSafeguard @transaction_logs_retention_time = ' + CAST(@transaction_logs_retention_time AS VARCHAR(10)));
            
              DECLARE @job_name VARCHAR(MAX);
            SET @job_name =
              CONCAT(@database_name, '_', 'DatastreamLogTruncationSafeguardJob1')
                DECLARE @current_time INT
              = CAST(FORMAT(GETDATE(), 'HHmmss') AS INT);
            
              -- Schedule the procedure to run after every 5 minutes.
              IF NOT EXISTS (
                SELECT * FROM msdb.dbo.sysjobs
                WHERE name = @job_name
              )
              BEGIN
                EXEC msdb.dbo.sp_add_job
                @job_name = @job_name,
                @enabled = 1,
                @description = N'Execute the procedure every 5 minutes.' ;
            
                EXEC msdb.dbo.sp_add_jobstep
                @job_name =  @job_name,
                @step_name = N'Execute_DatastreamLogTruncationSafeguard',
                @subsystem = N'TSQL',
                @command = @command_str;
            
                  DECLARE @schedule_name_1 VARCHAR(MAX);
                SET @schedule_name_1 = CONCAT(@database_name, '_', 'DatastreamEveryFiveMinutesSchedule')
            
                EXEC msdb.dbo.sp_add_schedule
                @schedule_name = @schedule_name_1,
                @freq_type = 4,  -- daily start
                @freq_subday_type = 4,  -- every X minutes daily
                @freq_interval = 1,
                @freq_subday_interval = 5,
                @active_start_time = @current_time;
            
                EXEC msdb.dbo.sp_attach_schedule
                @job_name = @job_name,
                @schedule_name = @schedule_name_1 ;
            
                -- Add a schedule that runs the stored procedure on the SQL Server Agent startup.
                DECLARE @schedule_name_agent_startup VARCHAR(MAX);
                SET @schedule_name_agent_startup = CONCAT(@database_name, '_', 'DatastreamSqlServerAgentStartupSchedule')
            
                EXEC msdb.dbo.sp_add_schedule
                @schedule_name = @schedule_name_agent_startup,
                @freq_type = 64,  -- start on SQL Server Agent startup
                @active_start_time = @current_time;
            
                EXEC msdb.dbo.sp_attach_schedule
                @job_name = @job_name,
                @schedule_name = @schedule_name_agent_startup ;
            
                EXEC msdb.dbo.sp_add_jobserver
                @job_name = @job_name,
                @server_name = @@servername ;
              END
            END;
            

     4. Execute the stored procedure that creates the Datastream job.
            
            DECLARE @transaction_logs_retention_time INT = (INT)
            EXEC [dbo].[SetUpDatastreamJob] @transaction_logs_retention_time
            

Replace INT with the number of minutes for which you want to retain the logs. For example:

        * The value of `60` sets the retention time to 1 hour
        * The value of `24 * 60` sets the retention time to 1 day
        * The value of `3 * 24 * 60` sets the retention time to 3 days



## What's next

  * Learn more about how Datastream works with [SQL Server sources](https://docs.cloud.google.com/datastream/docs/sources-sqlserver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
