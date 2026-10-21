---
url: https://docs.cloud.google.com/datastream/docs/configure-cloudsql-sqlserver/
title: Configure a Cloud SQL for SQL Server database for CDC \u00a0|\u00a0 Datastream \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:50:51.023692+00:00
---

# Configure a Cloud SQL for SQL Server database for CDC  |  Datastream  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/datastream/docs/configure-cloudsql-sqlserver/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Datastream ](https://docs.cloud.google.com/datastream/docs)
  * [ Guides ](https://docs.cloud.google.com/datastream/docs/how-to)



Send feedback 

#  Configure a Cloud SQL for SQL Server database for CDC Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure change data capture (CDC) to stream data from a Cloud SQL for SQL Server database to a [supported destination](https://docs.cloud.google.com/datastream/docs/destinations), such as BigQuery or Cloud Storage.

  1. Connect to your Cloud SQL instance. You can do it using the [`gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command in the Cloud Shell prompt.

  2. Enable CDC on the database by running the following command:
         
         EXEC msdb.dbo.gcloudsql_cdc_enable_db 'DATABASE_NAME'
         

Replace `DATABASE_NAME` with the name of your source database.

  3. Enable CDC on the tables for which you need to capture changes:
         
         USE [DATABASE_NAME]
         EXEC sys.sp_cdc_enable_table
         @source_schema = N'SCHEMA_NAME',
         @source_name = N'TABLE_NAME',
         @role_name = NULL
         GO
         

**Note:** You need to run the command for each table for which you want to enable CDC.
  4. Enable snapshot isolation.

When you backfill data from your SQL Server database, it's important to ensure consistent snapshots. If you don't apply the settings described in this section, changes made to the database during the backfill process might lead to duplicates or incorrect results. Applying snapshot isolation settings is required if your stream includes tables without primary keys.

Enabling snapshot isolation creates a temporary view of your database at the start of the backfill process. This ensures that the data being copied remains consistent, even if other users are making changes to the live tables at the same time. Enabling snapshot isolation might have a slight performance impact, but it's essential for reliable data extraction.

To enable snapshot isolation:

     1. Connect to your database using a SQL Server client.
     2. Run the following command:
    
    ALTER DATABASE DATABASE_NAME SET ALLOW_SNAPSHOT_ISOLATION ON;
    

Replace DATABASE_NAME with the name of you database.

  5. Create a Datastream user:

     1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

     2. [Create a user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users#creating) and assign the `db_owner` and `db_denydatawriter` roles to them:
    
    CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
    
    
    EXEC sp_addrolemember 'db_owner', 'USER_NAME';
    EXEC sp_addrolemember 'db_denydatawriter', 'USER_NAME';
    




## Additional steps required for the transaction logs CDC method

The steps described in this section are only required when you configure your source SQL Server database for use with the transaction logs CDC method.

  1. Set the polling interval for which you want the changes to be available on your source.
         
         USE [DATABASE_NAME]
         EXEC sys.sp_cdc_change_job @job_type = 'capture' , @pollinginterval = 86399
         EXEC sp_cdc_stop_job 'capture'
         EXEC sp_cdc_start_job 'capture'
         

The `@pollinginterval` parameter is measured in seconds with a recommended value set to `86399`. This means that the transaction log retains changes for 86,399 seconds (one day). Executing the `sp_cdc_start_job 'capture` procedure initiates the settings.

  2. Set up a log truncation safeguard.

To make sure that the CDC reader has enough time to read the logs while allowing log truncation to prevent using up the storage space, you can set up a log truncation safeguard:

     1. Connect to the database using a SQL Server client.
     2. Create a dummy table in the database:
            
            USE [DATABASE_NAME];
            CREATE TABLE dbo.gcp_datastream_truncation_safeguard (
              [id] INT IDENTITY(1,1) PRIMARY KEY,
              CreatedDate DATETIME DEFAULT GETDATE(),
              [char_column] CHAR(8)
              );
            

     3. Create a stored procedure that runs an active transaction for a period that you specify to prevent log truncation:
            
            CREATE PROCEDURE [dbo].[DatastreamLogTruncationSafeguard] @transaction_logs_retention_time INT
            AS
            BEGIN
              -- Start a new transaction
              BEGIN TRANSACTION;
              INSERT INTO dbo.gcp_datastream_truncation_safeguard (char_column) VALUES ('a')
            
            DECLARE @formatted_time VARCHAR(5)
            SET @formatted_time = CONVERT(VARCHAR(5), DATEADD(MINUTE, @transaction_logs_retention_time, 0), 108);
              -- Wait for X minutes before ending the transaction
              WAITFOR DELAY @formatted_time;
              -- Commit the transaction
              COMMIT TRANSACTION;
            END;
            

     4. Create another stored procedure. This time, you create a job that runs the stored procedure that you created in the previous step according to a specified cadence:
            
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
            
                -- Add 3 schedules to the job to run again after specified time.
                IF
                  NOT EXISTS(
                    SELECT *
                    FROM msdb.dbo.sysjobs
                    WHERE name = @job_name
                  )
                    BEGIN
                      EXEC
                        msdb.dbo.sp_add_job
                          @job_name
              = @job_name,
              @enabled = 1,
              @description = N'Execute the procedure to run an active transaction for x minutes.';
            
            EXEC msdb.dbo.sp_add_jobstep @job_name = @job_name,
            @step_name = N'Execute_DatastreamLogTruncationSafeguard',
            @subsystem = N'TSQL',
            @command = @command_str;
            
              -- Add a schedule that runs the stored procedure every given minutes starting now.
              DECLARE @schedule_name_1 VARCHAR(MAX);
              SET @schedule_name_1 = CONCAT(@database_name, '_', 'DatastreamEveryGivenMinutesFromNow')
            
              DECLARE @start_time_1 time;
              SET @start_time_1 = DATEADD(SECOND, 1, GETDATE());
              DECLARE @formatted_start_time_1 INT;
              SET @formatted_start_time_1 = CONVERT(INT, REPLACE(CONVERT(VARCHAR(8), @start_time_1, 114), ':' ,''));
            
              EXEC msdb.dbo.sp_add_schedule
              @schedule_name = @schedule_name_1,
              @freq_type = 4,  -- daily start
              @freq_subday_type = 4,  -- every X minutes daily
              @freq_interval = 1,
              @freq_subday_interval = @transaction_logs_retention_time,
              @active_start_time = @formatted_start_time_1;
            
              EXEC msdb.dbo.sp_attach_schedule
              @job_name = @job_name,
              @schedule_name = @schedule_name_1 ;
            
              -- Add a schedule that runs the stored procedure after every given minutes starting after some delay.
              DECLARE @schedule_name_2 VARCHAR(MAX);
              Set @schedule_name_2 = CONCAT(@database_name, '_', 'DatastreamEveryGivenMinutesAfterDelay');
            
              DECLARE @start_time_2 time;
              SET @start_time_2 = DATEADD(MINUTE, @transaction_logs_retention_time / 2, GETDATE());
            
              DECLARE @formatted_start_time_2 INT;
              SET @formatted_start_time_2 = CONVERT(INT, REPLACE(CONVERT(VARCHAR(8), @start_time_2, 114), ':' ,''));
            
              EXEC msdb.dbo.sp_add_schedule
              @schedule_name = @schedule_name_2,
              @freq_type = 4,  -- daily start
              @freq_subday_type = 4,  -- every x minutes daily
              @freq_interval = 1,
              @freq_subday_interval = @transaction_logs_retention_time,
              @active_start_time = @formatted_start_time_2;
            
              EXEC msdb.dbo.sp_attach_schedule
              @job_name = @job_name,
              @schedule_name = @schedule_name_2 ;
            
              -- Add a schedule that runs the stored procedure on the SQL Server Agent startup.
              DECLARE @schedule_name_agent_startup VARCHAR(MAX);
              Set @schedule_name_agent_startup = CONCAT(@database_name, '_', 'DatastreamSqlServerAgentStartupSchedule')
            
              EXEC msdb.dbo.sp_add_schedule
              @schedule_name = @schedule_name_agent_startup,
              @freq_type = 64,  -- start on SQL Server Agent startup
              @active_start_time = @formatted_start_time_1;
            
              EXEC msdb.dbo.sp_attach_schedule
              @job_name = @job_name,
              @schedule_name = @schedule_name_agent_startup ;
            
              EXEC msdb.dbo.sp_add_jobserver
              @job_name = @job_name,
              @server_name = @@servername ;
              END
            END;
            

     5. Execute the stored procedure that creates the Datastream job.
            
            DECLARE @transaction_logs_retention_time INT = (INT)
            EXEC [dbo].[SetUpDatastreamJob] @transaction_logs_retention_time
            

Replace INT with the number of minutes for which you want to retain the logs. For example:

        * The value of `60` sets the retention time to 1 hour
        * The value of `24 * 60` sets the retention time to 1 day
        * The value of `3 * 24 * 60` sets the retention time to 3 days
  3. Enable [point-in-time recovery (PITR)](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/pitr#enablingpitr).




## What's next

  * Learn more about how Datastream works with [SQL Server sources](https://docs.cloud.google.com/datastream/docs/sources-sqlserver).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
