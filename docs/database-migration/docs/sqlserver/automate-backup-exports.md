---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/automate-backup-exports/
title: Schedule transaction log file exports \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:42.507616+00:00
---

# Schedule transaction log file exports  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/automate-backup-exports/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Schedule transaction log file exports Stay organized with collections  Save and categorize content based on your preferences. 

Transaction log backup files contain the changes changes that occur in your source database after you take the full backup. Transaction log backups are required for the continuous load phase of your migration job.

This page describes how to schedule regular transaction log exports and uploads for migrating from self-managed and Amazon RDS sources.

## Schedule transaction log file uploads for Amazon RDS

You can schedule regular transfers of your transaction log files from the Amazon RDS source instance to the Cloud Storage bucket where you store the transaction log files.

Perform the following steps:

  1. Ensure automated backups are enabled on your Amazon RDS instance. See [ Enable automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.html#USER_WorkingWithAutomatedBackups.Enabling) in the Amazon RDS documentation.
  2. Enable access to transaction log files in your Amazon RDS instance. See [ Access to transaction log backups with RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.html). You can also check the following sample command: 

#### Example stored procedure call to enable transaction log access in Amazon RDS
         
         export DATABASE=YOUR_DATABASE_NAME;
         export S3_Bucket=YOUR_S3_BUCKET;
         exec msdb.dbo.rds_tlog_copy_setup
         @target_s3_arn='arn:aws:s3:::${S3_Bucket}/${DATABASE}/log/';

  3. Create a SQL Agent job that runs on a regular schedule. The job should execute the following script: 
         
         declare @DATABASE varchar(100);
         SELECT @DATABASE=YOUR_DATABASE_NAME;
         
         USE @DATABASE;
         declare @startTime varchar(100);
         declare @endTime varchar(100);
         SELECT
           @startTime = CONVERT(VARCHAR(100), DATEADD(hour, -1, GETUTCDATE()), 120),
           @endTime = CONVERT(VARCHAR(100), GETUTCDATE(), 120);
         
         exec msdb.dbo.rds_tlog_backup_copy_to_S3 
           @db_name=@DATABASE,
           @backup_file_start_time=@startTime,
           @backup_file_end_time=@endTime;

  4. Configure continuous file transfers from your S3 bucket to the Cloud Storage bucket. You can use any solution to move your files, for example event-driven transfer jobs in Storage Transfer Service. See [Set up event-driven transfers from AWS S3](https://docs.cloud.google.com/storage-transfer/docs/event-driven-transfers#set_up_event-driven_transfers_from_aws_s3). 



## Schedule transaction log file uploads for on-premise SQL Server instances

You can schedule regular transfers of your transaction log files from your self-managed source instance to the Cloud Storage bucket where you store the transaction log files. One of the recommended solutions is

Perform the following steps:

  1. On the system where you want to run the script, ensure you have initialized the Google Cloud CLI with authentication and a project by running either [ gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [ gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [ gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set).
  2. Save the following script to a file on your source SQL Server instance. 

This script automates creating a transaction log file and uploading it to your Cloud Storage bucket by using the [ `gcloud storage cp`](https://docs.cloud.google.com/sdk/gcloud/reference/storage/cp) command.

### Bash
         
         #!/bin/bash
         
         NOW="$(date +%s)"
         
         EXT=".trn"
         if [[ "$1" == "final" ]]
         then
           EXT='.trn.final'
         fi
         
         NAME="{DATABASE}.${NOW}.${EXT}"
         FULL_NAME="/SQLServerBackups/log/${NAME}"
         
         
         QUERY="BACKUP LOG ${DATABASE} TO DISK = '${FULL_NAME}'"
         /opt/mssql-tools/bin/sqlcmd -S localhost -U SA -P "${SA_PASSWORD}" -d master -Q "${QUERY}"
         
         gcloud storage cp "${FULL_NAME}" "${GCS_BACKUPS}/log/"

### PowerShell
         
         # Get the current timestamp
         $NOW = [int](Get-Date -UFormat '%s')
         
         # Set the file extension based on the command-line argument
         $EXT = '.trn'
         if ($args[0] -eq 'final') {
             $EXT = '.trn.final'
         }
         
         # Construct the backup file name
         $NAME = "{0}.{1}{2}" -f $DATABASE, $NOW, $EXT
         $FULL_NAME = "X:\SQLServerBackups\log\$NAME"
         
         # Construct the SQL backup query
         $QUERY = "BACKUP LOG $DATABASE TO DISK = '$FULL_NAME'"
         
         # Execute the SQL backup command
         Invoke-Sqlcmd -ServerInstance 'localhost' -Username 'SA' -Password $env:SA_PASSWORD -Database 'master' -Query $QUERY
         
         # Upload the backup file to Google Cloud Storage
         gcloud storage cp "$FULL_NAME" "$GCS_BACKUPS/log/"

  3. Configure a scheduling tool of your choice to regularly run the script. 

You can also use this script manually and pass the `"final"` positional argument to create the transaction log file whose name ends in the `.trn.final` suffix. This is useful when you want to finish your migration and [ promote the migration job](https://docs.cloud.google.com/database-migration/docs/sqlserver/finalize-migration). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
