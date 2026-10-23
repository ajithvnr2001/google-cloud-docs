---
url: https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures/
title: Cloud SQL stored procedures \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:31.055435+00:00
---

# Cloud SQL stored procedures  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/sqlserver/apis)



Send feedback 

#  Cloud SQL stored procedures Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/stored-procedures "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/stored-procedures "View this page for the PostgreSQL database engine") | SQL Server

This section describes stored procedures for Cloud SQL instances.

A stored procedure contains SQL code that you can reuse.

You cannot drop or alter system stored procedures.

To execute a stored procedure, you use the `EXEC` command and replace the following variables:

  * procedure_name is the name of the stored procedure.
  * database_name is the name of the database where you want to run the procedure.
  * schema_name is the name of the schema where you want to run the procedure.


    
    
    EXEC database_name.schema_name.procedure_name @param1, @param2;

For more information, see the [EXECUTE (Transact-SQL)](https://docs.microsoft.com/en-us/sql/t-sql/language-elements/execute-transact-sql) reference page. 

To create your own stored procedure, see [Create a Stored Procedure](https://docs.microsoft.com/en-us/sql/relational-databases/stored-procedures/create-a-stored-procedure?view=sql-server-ver15). 

**Note:** You cannot run some stored procedures because they require a `sysadmin` role, which isn't available in Cloud SQL. 

## Cloud SQL for SQL Server stored procedures

### Stored procedure for using bulk insert

For information about bulk insert, see [Use bulk insert for importing data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#bulk-insert).

#### msdb.dbo.gcloudsql_bulk_insert

**Syntax**
    
    
    EXEC msdb.dbo.gcloudsql_bulk_insert @database @schema @object @file ...

**Description**

This stored procedure has similar parameters and behavior to the [BULK INSERT](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16) command.

The stored procedure imports data to a Cloud SQL instance from a file stored in a Cloud Storage bucket. It uses [Cloud Storage interoperable API](https://docs.cloud.google.com/storage/docs/interoperability#xml_api) and [HMAC keys](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) to authenticate access to the Cloud Storage bucket.

This stored procedure has the following parameters:

Parameter | Type | Description  
---|---|---  
`@database` | `SYSNAME` | Specifies the name of the target database to which the data is to be imported.  
`@schema` | `SYSNAME` | Specifies the name of the schema to which the table belongs.  
`@object` | `NVARCHAR` | Specifies the name of the table where the data is to be inserted.  
[`@file`](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#from-data_file) | `NVARCHAR` | Specifies the path to the import file in the Cloud Storage bucket. The path must have the following format: 
    
    
     s3://storage.googleapis.com/BUCKET_NAME/FILE_PATH
     

Replace the following: 

  * BUCKET_NAME: specifies the Cloud Storage bucket name.
  * FILE_PATH: specifies the path to the file stored in the Cloud Storage bucket.

  
[`@batchsize`](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#batchsize--batch_size) | `INT` | Specifies the number of rows in a batch.  
`[@checkconstraints](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#check_constraints)` | `BIT` | Specifies that all constraints on the target table must be checked.  
`[@codepage](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#codepage---acp--oem--raw--code_page-)` | `NVARCHAR` | Specifies the code page of the data in the file. `RAW` is the default and only option.  
`[@datafiletype](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#datafiletype---char--native--widechar--widenative-)` | `NVARCHAR` | Specifies the bulk insert file type.  
`[@datasource](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#data_source--data_source_name)` | `NVARCHAR` | Specifies the name of the external data source from which you want to import the data.  
`[@errorfile](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#errorfile--error_file_path)` | `NVARCHAR` | Specifies the path to the file used to collect rows that have formatting errors. The path must have the following format: 
    
    
     s3://storage.googleapis.com/BUCKET_NAME/FILE_PATH
     

Replace the following: 

  * BUCKET_NAME: specifies the Cloud Storage bucket name.
  * FILE_PATH: specifies the path to the file stored in the Cloud Storage bucket.

Additionally, Cloud SQL creates a file with the extension `.ERROR.txt`. This file contains references to each row in the error file and provides error diagnostics.   
`[@errorfiledatasource](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#errorfile_data_source--errorfile_data_source_name)` | `NVARCHAR` | Specifies the name of the external data source in which you want to create the error file.  
`[@firstrow](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#firstrow--first_row)` | `INT` | Specifies the numeric identifier of the first row to load.  
`[@firetriggers](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#fire_triggers)` | `BIT` | Indicates that any insert triggers defined on the target table would execute during the bulk insert operations.  
`[@formatfiledatasource](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#formatfile_data_source--data_source_name)` | `NVARCHAR` | Specifies the name of the external data source from which you should load the format file.  
`[@keepidentity](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#keepidentity)` | `BIT` | Specifies the use of identity data from the import file for the identity column. The values are `0`, which means false, and `1`, which means true.  
`[@keepnulls](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#keepnulls)` | `BIT` | Specifies whether empty columns should retain a null value during the bulk import operation, instead of having any default values for the columns inserted. The values are `0`, which means false, and `1`, which means true.  
`[@kilobytesperbatch](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#kilobytes_per_batch--kilobytes_per_batch)` | `INT` | Specifies the amount of data per batch, in KB.  
`[@lastrow](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#lastrow--last_row)` | `INT` | Specifies the numeric identifier of the last row to load.  
`[@maxerrors](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#maxerrors--max_errors)` | `INT` | Specifies the number of errors allowed, before Cloud SQL cancels the operation.  
`[@ordercolumnsjson](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#order---column--asc--desc-----n--)` | `NVARCHAR` | Specifies the sort order and columns, in JSON format. For example: 
    
    
    [{"name": "COLUMN_NAME","order": "ORDER"},{"name": "COLUMN_NAME","order": "ORDER"}]

Replace the following: 

  * COLUMN_NAME: the name of the column.
  * ORDER: the sort order. The value of this parameter can be `asc` for ascending or `desc` for descending.

  
`[@rowsperbatch](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#rows_per_batch--rows_per_batch)` | `INT` | Specifies the number of rows per batch. For more information about selecting a batch size, see [Performance considerations](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#performance-considerations)  
`[@tablock](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#tablock)` | `BIT` | Specifies that a table lock is taken for the duration of the bulk insert operation.  
`[@format](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#format--csv)` | `NVARCHAR` | Specifies the format of the file. Use `CSV` as the value of this parameter.  
`[@fieldquote](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#fieldquote--field_quote)` | `NVARCHAR` | Specifies the character to be used as the quote character in the CSV file. If you don't specify a value, then Cloud SQL uses `"` as the default value.  
`[@formatfile](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#formatfile--format_file_path)` | `NVARCHAR` | Specifies the path of the file in Cloud Storage describing the format of the data to be imported. The path should have the following format: 
    
    
     s3://storage.googleapis.com/BUCKET_NAME/FILE_PATH
     

Replace the following: 

  * BUCKET_NAME: specifies the Cloud Storage bucket name.
  * FILE_PATH: specifies the path to the file stored in the Cloud Storage bucket.

  
`[@fieldterminator](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#fieldterminator--field_terminator)` | `NVARCHAR` | Specifies the field terminator for char and widechar data files.  
`[@rowterminator](https://learn.microsoft.com/en-us/sql/t-sql/statements/bulk-insert-transact-sql?view=sql-server-ver16#rowterminator--row_terminator)` | `NVARCHAR` | Specifies the row terminator for char and widechar data files.  
  
### Stored procedures for SQL Server Audit functionality

For information about using the functionality of SQL Server Audit, see [SQL Server database auditing](https://docs.cloud.google.com/sql/docs/sqlserver/db-audit).

#### msdb.dbo.gcloudsql_fn_get_audit_file

**Syntax**
    
    
    msdb.dbo.gcloudsql_fn_get_audit_file

**Description**

Retrieves the data from an audit file that was created by SQL Server Audit functionality.

This stored procedure accepts the same parameters as the `sys.fn_get_audit_file` function. See the [documentation for that function](https://docs.microsoft.com/en-us/sql/relational-databases/system-functions/sys-fn-get-audit-file-transact-sql?view=sql-server-ver15) for more information related to `msdb.dbo.gcloudsql_fn_get_audit_file`.

### Stored procedures for change data capture (CDC)

For more information about CDC, see [Enable change data capture](https://docs.cloud.google.com/sql/docs/sqlserver/replication/enable-cdc).

#### msdb.dbo.gcloudsql_cdc_enable_db

**Syntax**
    
    
    exec msdb.dbo.gcloudsql_cdc_enable_db databaseName

**Description**

Turns change data capture on for a database.

  * **`databaseName`** \- Name of the database to run this stored procedure on.



#### msdb.dbo.gcloudsql_cdc_disable_db

**Syntax**
    
    
    exec msdb.dbo.gcloudsql_cdc_disable_db databaseName

**Description**

Turns CDC off for a database.

  * **`databaseName`** \- Name of the database to run this stored procedure on.



### Stored procedures for external replication with Cloud SQL as a publisher

For more information about publishing to an external subscriber, or to another Cloud SQL instance, see [Configure external replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).

#### msdb.dbo.gcloudsql_transrepl_setup_distribution

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_setup_distribution @login,@password
    

**Description**

A wrapper stored procedure that sets up a distribution database. The wrapper calls the following: [sp_adddistributor](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-adddistributor-transact-sql?view=sql-server-ver15), [sp_adddistributiondb](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-adddistributiondb-transact-sql?view=sql-server-ver15), and [sp_adddistpublisher](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-adddistpublisher-transact-sql?view=sql-server-ver15).

  * **login** \- An existing login used to connect and create the distribution database.
  * **password** \- The password used when connecting to the distributor.



#### msdb.dbo.gcloudsql_transrepl_replicationdboption

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_replicationdboption @db,@value
    

**Description**

Enables or disables the publishing option of a database for the publisher that uses [sp_replicationdboption](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-replicationdboption-transact-sql?view=sql-server-ver15).

  * **db** \- The database for which the replication option is being set.
  * **value** \- Allows you to specify `True` to enable the publishing option, or `False` to disable the publishing option.



#### msdb.dbo.gcloudsql_transrepl_addlogreader_agent

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_addlogreader_agent @db,@login,@password
    

**Description**

Sets up the log reader agent for a database that uses [sp_addlogreader_agent](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addlogreader-agent-transact-sql?view=sql-server-ver15).

  * **db** \- Database to be published.
  * **login** \- Login used when connecting to the publisher.
  * **password** \- The password used when connecting.



#### msdb.dbo.gcloudsql_transrepl_addpublication

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_addpublication @db,@publication
    

**Description**

Creates the transactional publication, and acts as a wrapper stored procedure for [sp_addpublication](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addpublication-transact-sql?view=sql-server-ver15).

  * **db** \- Database being published.
  * **publication** \- Name of the new publication created.



#### msdb.dbo.gcloudsql_transrepl_droppublication

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_droppublication @db,@publication
    

**Description**

Drops the transactional publication, and acts as a wrapper stored procedure for [sp_droppublication](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-droppublication-transact-sql?view=sql-server-ver15).

  * **db** \- Database for which publication is dropped.
  * **publication** \- Name of the publication dropped.



#### msdb.dbo.gcloudsql_transrepl_addpublication_snapshot

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_addpublication_snapshot  @db,@publication,@login,@password
    

**Description**

Creates a snapshot agent for the database that is being published, acting as a wrapper stored procedure for [sp_addpublication_snapshot](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addpublication-snapshot-transact-sql?view=sql-server-ver15).

  * **db** \- Database for which publication is dropped.
  * **publication** \- Name of the publication dropped.
  * **login** \- Login used when connecting to the publisher.
  * **password** \- The password used when connecting.



#### msdb.dbo.gcloudsql_transrepl_addpushsubscription_agent

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_addpushsubscription_agent
          @db,@publication,@subscriber_db,@subscriber_login,
            @subscriber_password,@subscriber
    

**Description**

Creates a new scheduled agent job to synchronize the push subscription, acting as a wrapper stored procedure for [sp_addpushsubscription_agent](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-addpushsubscription-agent-transact-sql?view=sql-server-ver15).

  * **db** \- Database that is published.
  * **publication** \- Name of the publication to which to add a push subscription agent.
  * **subscriber_db** \- The database on the subscriber.
  * **subscriber_login** \- The login used when connecting to the subscriber.
  * **subscriber_password** \- The password used when connecting to the subscriber.
  * **subscriber** \- The IP name of the subscriber instance. This value can specified as: `<Hostname>,<PortNumber>`



#### msdb.dbo.gcloudsql_transrepl_addmonitoraccess

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_addmonitoraccess @login
    

**Description**

Provides access to the Replication Monitor and the `SELECT` statement on replication-related tables on the distribution database.

  * **login** \- The login used to access the replication monitor.



#### msdb.dbo.gcloudsql_transrepl_changedistributor_property

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_changedistributor_property @property,@value
    

**Description**

This stored procedure changes the `heartbeat_interval`, and wraps `sp_changedistributor_property`. For more information, see the [documentation](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-changedistributor-property-transact-sql?view=sql-server-ver16) for `sp_changedistributor_property`. Also see that documentation for more information about the `heartbeat_interval` value.

  * **property** \- The property for a distribution database.
  * **value** \- The value to provide for the specified property.



#### msdb.dbo.gcloudsql_transrepl_dropsubscriber

**Syntax**
    
    
        exec msdb.dbo.gcloudsql_transrepl_dropsubscriber @subscriber
    

**Description**

Removes the subscriber, acting as a wrapper stored procedure for [sp_dropsubscriber](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-dropsubscriber-transact-sql?view=sql-server-ver15).

  * **subscriber** \- The IP name of the subscriber to be dropped. This value can specified as: `<Hostname>,<PortNumber>`



#### msdb.dbo.gcloudsql_transrepl_remove_distribution

**Syntax**
    
    
         exec msdb.dbo.gcloudsql_transrepl_remove_distribution
    

**Description**

Removes the distribution setup, acting as a wrapper stored procedure for the following: [sp_dropdistpublisher](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-dropdistpublisher-transact-sql?view=sql-server-ver15), [sp_dropdistributiondb](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-dropdistributiondb-transact-sql?view=sql-server-ver15), and [sp_dropdistributor](https://docs.microsoft.com/en-us/sql/relational-databases/system-stored-procedures/sp-dropdistributor-transact-sql?view=sql-server-ver15).

### Stored procedure for configuring database compatibility levels

For information about database compatibility levels, see [`ALTER DATABASE` (Transact-SQL) Compatibility Level](https://learn.microsoft.com/en-us/sql/t-sql/statements/alter-database-transact-sql-compatibility-level).

#### msdb.dbo.gcloudsql_set_compat_level_for_master_db

**Syntax**
    
    
    EXEC msdb.dbo.gcloudsql_set_compat_level_for_master_db @compatibility_level
    

**Description**

Sets the compatibility level for the `master` database. In Cloud SQL for SQL Server, users don't have the permissions required to modify the `master` database directly. This stored procedure lets you change its compatibility level, acting as a wrapper for the `ALTER DATABASE [master] SET COMPATIBILITY_LEVEL` command.

  * **compatibility_level** : an integer value specifying the compatibility level to apply (for example, 130, 140, or 150). The value must be 130 or greater.



### Stored procedure for exporting logins

For information about exporting logins, see [Export SQL Server logins](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins).

#### msdb.dbo.sp_help_revlogin

**Syntax**
    
    
    EXEC msdb.dbo.sp_help_revlogin [@login_name = 'LOGIN_NAME']
    

**Description**

Generates Transact-SQL (T-SQL) scripts containing `CREATE LOGIN` statements to transfer logins, security identifiers (SIDs), and password hashes from a Cloud SQL for SQL Server instance.

To install the `sp_help_revlogin` stored procedure in the `msdb` database, enable the `cloud sql enable sp_help_revlogin` database flag on your instance.

  * **login_name** : (Optional) Specifies the name of a specific login to export. If omitted or set to `NULL`, the stored procedure generates scripts for all eligible logins.



The stored procedure outputs generated scripts by using T-SQL `PRINT` statements rather than tabular result sets. Because Cloud SQL Studio only displays tabular query results, use a client tool such as SQL Server Management Studio (SSMS), Visual Studio Code with the MSSQL extension, or `sqlcmd` to view and export the generated scripts.

`sp_help_revlogin` automatically excludes Google Cloud service accounts, internal SQL Server system accounts (such as logins prefixed with `##`), and logins assigned to `sysadmin` or other restricted administrative server roles.

## What's next

  * Learn how to [export SQL Server logins](https://docs.cloud.google.com/sql/docs/sqlserver/export-logins).
  * Learn how to [enable change data capture (CDC)](https://docs.cloud.google.com/sql/docs/sqlserver/replication/enable-cdc).
  * Learn how to [configure external replicas](https://docs.cloud.google.com/sql/docs/sqlserver/replication/configure-external-replica).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
