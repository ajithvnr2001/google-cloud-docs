---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files/
title: Prepare your backup files \u00a0|\u00a0 Database Migration Service for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:42:41.290947+00:00
---

# Prepare your backup files  |  Database Migration Service for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver/export-backup-files/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ Homogeneous migration to SQL Server ](https://docs.cloud.google.com/database-migration/docs/sqlserver/scenario-overview)



Send feedback 

#  Prepare your backup files Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create the backup files required for migrating your self-managed or Amazon RDS SQL Server databases to Cloud SQL for SQL Server, including the following sections:

  * Requirements and limitations lists important limitations for backup files support.
  * Naming conventions explains the requirements around file names for your backup files.
  * Take a full backup contains steps for creating full backup files.
  * Take a differential backup contains steps for creating differential backup files.
  * Transaction log backup files contains steps for creating transaction log backup files.



## Requirements and limitations

The following requirements and limitations apply to the backup files you use for migration:

  * All backup files must names that adhere to their respective naming conventions.

  * Your backup files can have a maximum size of 5 TB.

  * You can stripe your full or differential backup files into smaller files if your database size exceeds 5 TB. Each stripe can have a maximum size of 5 TB.

  * You can use encrypted backup and transaction log files for your migration. If you want to use encrypted backup files, you must encrypt **every backup file** (full, differential, transaction log) you use for a specific database included in your migration. See [ Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption).

  * Database Migration Service doesn't migrate the [ SQL Server `master` database](https://learn.microsoft.com/en-us/sql/relational-databases/databases/master-database).

  * Your source SQL Server instance can't use the **simple recovery model**. For more information on recovery models, see [Recovery Models (SQL Server)](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server) in Microsoft documentation.




## Naming conventions

This section covers the file name requirements for your full, differential, and transaction log backup files.

  * For information on Cloud Storage bucket folder name and structure requirements, see [ Create and configure Cloud Storage buckets](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets).

  * For information on how Database Migration Service uses different types of backup files in homogeneous SQL Server migrations, see [ Supported backup file types](https://docs.cloud.google.com/database-migration/docs/sqlserver/supported-backup-files).




### Backup file naming conventions for on-premise SQL Server instances

#### Full backup file names

The naming convention for full backup files depends on whether you use a single backup file, or if you divide it into multiple stripes. In both scenarios, Database Migration Service requires that you include an epoch timestamp (expressed as a Unix timestamp in seconds) that represents the approximate time when you took the full backup.

  * If your full backup is a single file, the file name must use the `db_name.epoch.bak` format, where:

    * `db_name` is the name of your database
    * `epoch` is a Unix timestamp in seconds
    * `.bak` is the file extension

Valid examples include:

    * `my-business-database.1712649600.bak`
    * `my-other-database.1712649600.bak`
  * If you divide your full backup into separate stripes, each stripe can use any name you choose but they must be uploaded to a Cloud Storage folder whose name is a Unix timestamp in seconds:
        
        Cloud Storage bucket root/
        |- my-business-database/
        |  |- full/
        |  |  |- 1712649600/
        |  |  |  |- mystripe-full_backup_file.bak
        |  |  |  |- otherStripefull-bkp.bak
        |  |- diff/
        |  |  |- ...
        |  |- log/
        |  |  |- ...
        |- my-other-database/
        |  |- full/
        |  |  |- 1715250742/
        |  |  |  |- cool-stripe-file.bak
        |  |  |  |- secondStripeFile.bak
        |  |- diff/
        |  |  |- ...
        |  |- log/
        |  |  |- ...
        




#### Differential backup file names

The naming convention for differential backup files depends on whether you use a single backup file, or if you divide it into multiple stripes. In both scenarios, Database Migration Service requires that you include an epoch timestamp (expressed as a Unix timestamp in seconds) that represents the approximate time when you took the differential backup.

  * If your differential backup is a single file, the file name must use the `db_name.epoch.ext` format, where:

    * `db_name` is the name of your database
    * `epoch` is a Unix timestamp in seconds
    * `.ext` is the file extension; differential backup files can use the following extensions: `.bak`, `.dif`, `.diff`.

Valid examples include:

    * `my-business-database.1731159833.bak`
    * `my-other-database.1731159833.dif`
  * If you divide your differential backup into separate stripes, each stripe can use any name you choose but they must be uploaded to a Cloud Storage folder whose name is a Unix timestamp in seconds:
        
        Cloud Storage bucket root/
        |- my-business-database/
        |  |- full/
        |  |  |- ...
        |  |- diff/
        |  |  |- 1731159833/
        |  |  |  |- mydiffstripe-diff_backup_file.dif
        |  |  |  |- mySeconddiffstripe-diff_backup_file.bak
        |  |- log/
        |  |  |- ...
        |- my-other-database/
        |  |- full/
        |  |  |- ...
        |  |- diff/
        |  |  |- 1731159833/
        |  |  |  |- firstDiffStripe.bak
        |  |  |  |- other_diff_stripe.diff
        |  |- log/
        |  |  |- ...
        




#### Transaction log file names

Your transaction log file names must use the `db_name.epoch.trn` format, where:

  * `db_name` is the name of your database
  * `epoch` is a Unix timestamp in seconds
  * `.trn` is the file extension



Valid examples include:

  * `my-business-database.1712649600.trn`
  * `my-other-database.1712649600.trn`



### Backup file naming conventions for Amazon RDS

#### Full backup file names

The naming convention for full backup files depends on whether you use a single backup file, or if you divide it into multiple stripes. In both scenarios, Database Migration Service requires that you include an epoch timestamp (expressed as a Unix timestamp in seconds) that represents the approximate time when you took the full backup.

  * If your full backup is a single file, the file name must use the `db_id.family_guid.rds_backup_seq_id.epoch.bak` format, where:

    * `db_id` is the Amazon RDS internal database identifier
    * `family_guid` is the Amazon RDS unique identifier of the original database at creation
    * `rds_backup_seq_id` is the identifier that Amazon RDS uses internally to maintain a sequence number for each transaction log backup file
    * `epoch` is a Unix timestamp in seconds
    * `.bak` is the file extension

Valid examples include:

    * `3.CX11CB3D-G2E4-46D9-B462-CE40CDA97E89.22.1712649600.bak`
    * `1.FD21CD3F-B5E4-27Z9-B462-CE40CDA97E89.21.1712649600.bak`
  * If you divide your full backup into separate stripes, each stripe can use any name you choose but they must be uploaded to a Cloud Storage folder whose name is a Unix timestamp in seconds:
        
        Cloud Storage bucket root/
        |- my-business-database/
        |  |- full/
        |  |  |- 1712649600/
        |  |  |  |- mystripe-full_backup_file.bak
        |  |  |  |- otherStripefull-bkp.bak
        |  |- diff/
        |  |  |- ...
        |  |- log/
        |  |  |- ...
        |- my-other-database/
        |  |- full/
        |  |  |- 1715250742/
        |  |  |  |- cool-stripe-file.bak
        |  |  |  |- secondStripeFile.bak
        |  |- log/
        |  |  |- ...
        




#### Differential backup file names

The naming convention for differential backup files depends on whether you use a single backup file, or if you divide it into multiple stripes. In both scenarios, Database Migration Service requires that you include an epoch timestamp (expressed as a Unix timestamp in seconds) that represents the approximate time when you took the differential backup.

  * If your differential backup is a single file, the file name must use the `db_id.family_guid.rds_backup_seq_id.epoch.ext` format, where:

    * `db_id` is the Amazon RDS internal database identifier
    * `family_guid` is the Amazon RDS unique identifier of the original database at creation
    * `rds_backup_seq_id` is the identifier that Amazon RDS uses internally to maintain a sequence number for each transaction log backup file
    * `epoch` is a Unix timestamp in seconds
    * `.bak` is the file extension; differential backup files can use the following extensions: `.bak`, `.dif`, `.diff`.

Valid examples include:

    * `3.CX11CB3D-G2E4-46D9-B462-CE40CDA97E89.22.1731159833.bak`
    * `1.FD21CD3F-B5E4-27Z9-B462-CE40CDA97E89.21.1731159833.dif`
  * If you divide your full backup into separate stripes, each stripe can use any name you choose but they must be uploaded to a Cloud Storage folder whose name is a Unix timestamp in seconds:
        
        Cloud Storage bucket root/
        |- my-business-database/
        |  |- full/
        |  |  |- ...
        |  |- diff/
        |  |  |- 1731159833/
        |  |  |  |- mydiffstripe-diff_backup_file.dif
        |  |  |  |- mySeconddiffstripe-diff_backup_file.bak
        |  |- log/
        |  |  |- ...
        |- my-other-database/
        |  |- full/
        |  |  |- ...
        |  |- diff/
        |  |  |- 1731159833/
        |  |  |  |- firstDiffStripe.bak
        |  |  |  |- other_diff_stripe.diff
        |  |- log/
        |  |  |- ...
        




#### Transaction log file names

In Amazon RDS, transaction log backup files are generated automatically and they include all the required database identifiers. These default names include the epoch timestamp and are fully supported in Database Migration Service. You can upload these files to your `/log/` folder directly.

## Take the full backup of your source instance

The full database backup file is required for the initial load phase of your migration job. If you want to encrypt your backups, make sure you store the encryption key so that you can later upload it to Cloud Storage when you create the migration job. See [ Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption).

### Take full backup for on-premise SQL Server instances

You can take the full backup of your on-premise SQL Server instance by using T-SQL or SQL Server Management Studio (SSMS). Follow these steps:

  1. Make sure you meet the following requirements: 
     * You use the correct  naming requirements  for your backup files.
     * Your source databases don't use the **simple** recovery model. See [Recovery Models (SQL Server) ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server) in Microsoft documentation.
     * If your database size exceeds 5 TB, make sure you divide the full backup into separate stripes. Each stripe can have a maximum size of 5 TB. See [ Backup devices in a striped media set](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?view=sql-server-ver16#backup-devices-in-a-striped-media-set-a-stripe-set).
  2. Take the full backup of your source instance. See [ Quickstart: Backup and restore a SQL Server database with SSMS](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/quickstart-backup-restore-database?view=sql-server-ver16) in Microsoft documentation. You can also check the following sample commands: 

#### Example T-SQL command for a single full backup file

This sample command takes a full backup of the `AdventureWorks2022` database. The resulting backup file uses the required naming convention.
         
         declare @DATABASE varchar(1000);
         SELECT @DATABASE = 'AdventureWorks2022';
         
         declare @unixTimestamp varchar(1000);
         SELECT @unixTimestamp = CAST(DATEDIFF(s, '1970-01-01', GETUTCDATE()) AS VARCHAR(50));
         
         DECLARE @BackupPath NVARCHAR(2000);
         SET @BackupPath = 'X:\SQLServerBackups\full\' + @DATABASE + '.' + @unixTimestamp + '.bak';
         
         DECLARE @SQL NVARCHAR(MAX);
         SET @SQL = 'BACKUP DATABASE [' + @DATABASE + '] TO DISK = N''' + @BackupPath + '''';
         EXEC sp_executesql @SQL;
         GO

#### Example T-SQL command for striped full backup files

This sample command takes a full backup of the `AdventureWorks2022` database. The resulting backup file uses the required naming convention.
         
         declare @DATABASE varchar(1000);
         SELECT @DATABASE = 'AdventureWorks2022';
         
         declare @unixTimestamp varchar(1000);
         SELECT @unixTimestamp = CAST(DATEDIFF(s, '1970-01-01', GETUTCDATE()) AS VARCHAR(50));
         
         DECLARE @BackupPath1 NVARCHAR(2000);
         DECLARE @BackupPath2 NVARCHAR(2000);
         DECLARE @BackupPath3 NVARCHAR(2000);
         
         SET @BackupPath1 = 'X:\SQLServerBackups\full\' + @DATABASE + '.' + @unixTimestamp + '\stripe1.bak';
         SET @BackupPath2 = 'X:\SQLServerBackups\full\' + @DATABASE + '.' + @unixTimestamp + '\stripe2.bak';
         SET @BackupPath3 = 'X:\SQLServerBackups\full\' + @DATABASE + '.' + @unixTimestamp + '\stripe3.bak';
         
         DECLARE @SQL NVARCHAR(MAX);
         SET @SQL = 'BACKUP DATABASE [' + @DATABASE + '] '
                    + 'TO DISK = N''' + @BackupPath1 + ''', '
                    + 'DISK = N''' + @BackupPath2 + ''', '
                    + 'DISK = N''' + @BackupPath3 + ''' '
                    + 'WITH FORMAT, '
                    + 'MEDIANAME = N''AdventureWorksStripedSet0'', '
                    + 'MEDIADESCRIPTION = N''Striped media set for ' + @DATABASE + ' database''';
         EXEC sp_executesql @SQL;
         GO

  3. Upload your backup file to a Cloud Storage bucket. See [ Create and configure a Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets). 



### Take full backup for Amazon RDS

To take the full backup of your Amazon RDS source, follow these steps:

  1. Make sure you meet the following requirements: 
     * You use the correct  naming requirements  for your backup files.
     * Your source databases don't use the **simple** recovery model. See [Determining a recovery model for your Microsoft SQL Server database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.DatabaseRecovery.html) in the Amazon RDS documentation.
     * If you want to use transaction log backup after you take the full backup, [ enable automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.html#USER_WorkingWithAutomatedBackups.Enabling) on your Amazon RDS instance. 
  2. Set up the native backup capability. See [ Setting up for native backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Enabling) in the Amazon RDS documentation. 
  3. Take the full backup of your source instance. If your database size exceeds 5 TB, make sure you divide the full backup into separate stripes by using the `@number_of_files` parameter. Each stripe can have a maximum size of 5 TB. See [Backing up a database ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Using.Backup) in Amazon RDS documentation. 

You can also check the following sample command:

#### Example query to take a full backup on Amazon RDS

This sample command takes a full backup of the `AdventureWorks2022` database. The resulting backup file uses the required naming convention.
         
         declare @DATABASE varchar(1000);
         declare @S3Bucket varchar(1000);
         declare @unixTimestamp varchar(30);
         declare @fileName varchar(1000);
         
         SELECT @S3Bucket = 'dms-sqlserver-exports';
         SELECT @DATABASE = 'AdventureWorks2022';
         
         SELECT @unixTimestamp=CAST(DATEDIFF(s, '1970-01-01', GETUTCDATE()) AS VARCHAR(50));
         SELECT @fileName = ('arn:aws:s3:::' + @S3Bucket + '/' + @DATABASE + '/full/' + @DATABASE + '.' + @unixTimestamp + '/' + CAST(database_id AS VARCHAR(10)) + '.' + CAST(family_guid AS VARCHAR(50)) + '.*.' + @unixTimestamp) FROM master.sys.database_recovery_status WHERE DB_NAME(database_id)=@DATABASE;
         
         exec msdb.dbo.rds_backup_database
           @source_db_name=@DATABASE,
           @s3_arn_to_backup_to=@fileName,
           @overwrite_s3_backup_file=1,
           @type='FULL',
           @number_of_files=1;

  4. Upload your backup file to a Cloud Storage bucket. See [ Create and configure a Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets). 



## Take the differential backup of your source instance

You can use a differential database backup file during the incremental load phase of your migration job. You can use encrypted differential backup files if you also encrypt the full backup file and transaction log files for the same database. All backup and transaction log files must use the same encryption key per database. See [ Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption).

### Take differential backup for on-premise SQL Server instances

You can take the differential backup of your on-premise SQL Server instance by using T-SQL or SQL Server Management Studio (SSMS). Follow these steps:

  1. Make sure you meet the following requirements: 
     * You use the correct  naming requirements  for your backup files.
     * Your source databases don't use the **simple** recovery model. See [Recovery Models (SQL Server) ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server) in Microsoft documentation.
     * If your database size exceeds 5 TB, make sure you divide the differential backup into separate stripes. Each stripe can have a maximum size of 5 TB. See [ Backup devices in a striped media set](https://learn.microsoft.com/en-us/sql/t-sql/statements/backup-transact-sql?view=sql-server-ver16#backup-devices-in-a-striped-media-set-a-stripe-set).
  2. Take the differential backup of your source instance. See [ Create a Differential Database Backup](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/create-a-differential-database-backup-sql-server) in Microsoft documentation. You can also check the following sample commands: 

#### Example T-SQL command for a single differential backup file

This sample command takes a differential backup of the `AdventureWorks2022` database. The resulting backup file uses the required naming convention.
         
         declare @DATABASE varchar(1000);
         SELECT @DATABASE = 'AdventureWorks2022';
         
         declare @unixTimestamp varchar(1000);
         SELECT @unixTimestamp = CAST(DATEDIFF(s, '1970-01-01', GETUTCDATE()) AS VARCHAR(50));
         
         DECLARE @BackupPath NVARCHAR(2000);
         SET @BackupPath = 'X:\SQLServerBackups\diff\' + @DATABASE + '.' + @unixTimestamp + '.bak';
         
         DECLARE @SQL NVARCHAR(MAX);
         SET @SQL = 'BACKUP DATABASE [' + @DATABASE + '] TO DISK = N''' + @BackupPath + ''' WITH DIFFERENTIAL';
         EXEC sp_executesql @SQL;
         GO

#### Example T-SQL command for striped differential backup files

This sample command takes a differential backup of the `AdventureWorks2022` database. The resulting backup file uses the required naming convention.
         
         declare @DATABASE varchar(1000);
         SELECT @DATABASE = 'AdventureWorks2022';
         
         declare @unixTimestamp varchar(1000);
         SELECT @unixTimestamp = CAST(DATEDIFF(s, '1970-01-01', GETUTCDATE()) AS VARCHAR(50));
         
         DECLARE @BackupPath1 NVARCHAR(2000);
         DECLARE @BackupPath2 NVARCHAR(2000);
         DECLARE @BackupPath3 NVARCHAR(2000);
         
         SET @BackupPath1 = 'X:\SQLServerBackups\diff\' + @DATABASE + '.' + @unixTimestamp + '\stripe1.bak';
         SET @BackupPath2 = 'X:\SQLServerBackups\diff\' + @DATABASE + '.' + @unixTimestamp + '\stripe2.bak';
         SET @BackupPath3 = 'X:\SQLServerBackups\diff\' + @DATABASE + '.' + @unixTimestamp + '\stripe3.bak';
         
         DECLARE @SQL NVARCHAR(MAX);
         SET @SQL = 'BACKUP DATABASE [' + @DATABASE + '] '
                    + 'TO DISK = N''' + @BackupPath1 + ''', '
                    + 'DISK = N''' + @BackupPath2 + ''', '
                    + 'DISK = N''' + @BackupPath3 + ''' '
                    + 'WITH DIFFERENTIAL, FORMAT, '
                    + 'MEDIANAME = N''AdventureWorksStripedSet0'', '
                    + 'MEDIADESCRIPTION = N''Striped differential media set for ' + @DATABASE + ' database''';
         EXEC sp_executesql @SQL;
         GO

  3. Upload your backup file to a Cloud Storage bucket. See [ Create and configure a Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets). 



### Take differential backup for Amazon RDS

To take the differential backup of your Amazon RDS source, follow these steps:

  1. Make sure you meet the following requirements: 
     * You use the correct  naming requirements  for your backup files.
     * Your source databases don't use the **simple** recovery model. See [Determining a recovery model for your Microsoft SQL Server database](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.DatabaseRecovery.html) in the Amazon RDS documentation.
  2. Set up the native backup capability. See [ Setting up for native backup and restore](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Enabling) in the Amazon RDS documentation. 
  3. Take the differential backup of your source instance. Use the `rds_backup_database` stored procedure with the `type` parameter set to `DIFFERENTIAL`. 

If your database size exceeds 5 TB, make sure you divide the full backup into separate stripes by using the `@number_of_files` parameter. Each stripe can have a maximum size of 5 TB. 

See [Backing up a database ](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SQLServer.Procedural.Importing.html#SQLServer.Procedural.Importing.Native.Using.Backup) in Amazon RDS documentation. You can also check the following sample command:

####  Example query to take a differential backup on Amazon RDS

This sample command takes a differential backup of the `AdventureWorks2022` database. The resulting backup file uses the required naming convention.
         
         declare @DATABASE varchar(1000);
         declare @S3Bucket varchar(1000);
         declare @unixTimestamp varchar(30);
         declare @fileName varchar(1000);
         
         SELECT @S3Bucket = 'dms-sqlserver-exports';
         SELECT @DATABASE = 'AdventureWorks2022';
         
         SELECT @unixTimestamp=CAST(DATEDIFF(s, '1970-01-01', GETUTCDATE()) AS VARCHAR(50));
         SELECT @fileName = ('arn:aws:s3:::' + @S3Bucket + '/' + @DATABASE + '/full/' + @DATABASE + '.' + @unixTimestamp + '/' + CAST(database_id AS VARCHAR(10)) + '.' + CAST(family_guid AS VARCHAR(50)) + '.*.' + @unixTimestamp) FROM master.sys.database_recovery_status WHERE DB_NAME(database_id)=@DATABASE;
         
         exec msdb.dbo.rds_backup_database
           @source_db_name=@DATABASE,
           @s3_arn_to_backup_to=@fileName,
           @overwrite_s3_backup_file=1,
           @type='DIFFERENTIAL',
           @number_of_files=1;

  4. Upload your backup file to a Cloud Storage bucket. See [ Create and configure a Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets). 



## Take transaction log backups

Transaction log backup files contain the changes changes that occur in your source database after you take the full backup. Transaction log backups are required for the continuous load phase of your migration job. You can schedule regular transaction log exports and uploads, to ensure data updates are continuously replicated to your destination Cloud SQL for SQL Server instance. See [ Schedule transaction log backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/automate-backup-exports).

If you use encrypted backup files, you must also encrypt the transaction log files for the same database. See [ Use encrypted backups](https://docs.cloud.google.com/database-migration/docs/sqlserver/backup-file-encryption).

### Take a transaction log backup for on-premise SQL Server instances

To take a transaction log backup of your on-premise SQL Server databases, follow these steps:

  1. Make sure you meet the following requirements: 
     * You use the correct  naming requirements  for your backup files.
     * Your source databases don't use the **simple** recovery model. See [Recovery Models (SQL Server) ](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/recovery-models-sql-server)in Microsoft documentation.
  2. Export the transaction log files from your SQL Server source databases. See [ Back up a transaction log](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-a-transaction-log-sql-server) in Microsoft documentation. You can also check the following sample command: 

#### Example T-SQL command to export transaction log files to local disk

This sample command creates a transaction log backup of the `AdventureWorks2022` database and saves the file on local disk. The resulting backup file uses the required naming convention.
         
         declare @DATABASE varchar(1000);
         SELECT @DATABASE = 'AdventureWorks2022';
         declare @unixTimestamp varchar(1000);
         SELECT @unixTimestamp = CAST(DATEDIFF(s, '1970-01-01', GETUTCDATE()) AS VARCHAR(50));
         
         DECLARE @BackupPath NVARCHAR(2000);
         SET @BackupPath = 'X:\SQLServerBackups\log\' + @DATABASE + '.' + @unixTimestamp + '.trn';
         
         DECLARE @SQL NVARCHAR(MAX);
         SET @SQL = 'BACKUP LOG [' + @DATABASE + '] TO DISK = N''' + @BackupPath + '''';
         EXEC sp_executesql @SQL;
         GO

  3. Upload the transaction log backup files to [ the Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets) you created for your migration. 



### Take a transaction log backup for Amazon RDS

Transaction log backups are created automatically if automated backups are enabled on your Amazon RDS instance. See [ Enable automated backups](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ManagingAutomatedBackups.html#USER_WorkingWithAutomatedBackups.Enabling) in Amazon RDS documentation.

To use transaction log backup files for your migration, follow these steps:

  1. Enable access to transaction log files in your Amazon RDS instance. See [ Access to transaction log backups with RDS for SQL Server](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER.SQLServer.AddlFeat.TransactionLogAccess.html). You can also check the following sample command: 

#### Example stored procedure call to enable transaction log access in Amazon RDS
         
         declare @DATABASE varchar(1000);
         declare @S3Bucket varchar(1000);
         declare @targetS3Arn varchar(1000);
         
         
         
         SELECT @S3Bucket = 'dms-sqlserver-exports';
         SELECT @DATABASE = 'AdventureWorks2022';
         SELECT @targetS3Arn = ('arn:aws:s3:::' + @S3Bucket + '/' + @DATABASE + '/log/');
         
         
         
         
         
         USE @DATABASE;
         exec msdb.dbo.rds_tlog_copy_setup
         @target_s3_arn=@targetS3Arn;

  2. Copy the transaction log backup files from your S3 bucket to [ the Cloud Storage bucket](https://docs.cloud.google.com/database-migration/docs/sqlserver/storage-buckets) you created for your migration. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
