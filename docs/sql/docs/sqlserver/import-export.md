---
url: https://docs.cloud.google.com/sql/docs/sqlserver/import-export/
title: Best practices for importing and exporting data \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:31:12.291326+00:00
---

# Best practices for importing and exporting data  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/import-export/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Best practices for importing and exporting data Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/import-export "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/import-export "View this page for the PostgreSQL database engine") | SQL Server

This page provides best practices for importing and exporting data with Cloud SQL. For step-by-step instructions for importing data into Cloud SQL, see [Importing Data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak). For step-by-step instructions for exporting your data, whether it is in Cloud SQL or an instance you manage, see [Exporting Data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak). 

## Best practices for importing and exporting

The following are best practices to consider when importing and exporting data:

  * Don't use Cloud Storage Requester Pays buckets
  * Compress data to reduce cost.
  * Reduce long-running import and export processes
  * Use the bcp utility for importing and exporting data
  * Use bulk insert for importing data
  * Use SqlPackage for importing and exporting data
  * Use striped import and export
  * Verify the imported database

**Note:** In Cloud SQL, the current SQL Server support for imports and exports consists of the following: 

  * Importing databases using BAK and SQL files.
  * Exporting databases using BAK files.



### Don't use Cloud Storage Requester Pays buckets

You cannot use a Cloud Storage bucket that has [Requester Pays](https://docs.cloud.google.com/storage/docs/requester-pays) enabled for imports and exports from Cloud SQL.

### Compress data to reduce cost

Cloud SQL supports importing and exporting both compressed and uncompressed files. Compression can save significant storage space on Cloud Storage and reduce your storage costs, especially when you are exporting large instances.

**Note:** Compression can degrade export performance.

When you export a BAK file, use a `.gz` file extension to compress the data. When you import a file with an extension of `.gz`, it is decompressed automatically.

### Reduce long-running import and export processes

Imports into Cloud SQL and exports out of Cloud SQL can take a long time to complete, depending on the size of the data being processed. This can have the following impacts: 

  * You can't stop a long-running Cloud SQL instance operation. 
  * You can perform only one import or export operation at a time for each instance, and a long-running import or export blocks other operations, such as daily automated backups. 



You can decrease the amount of time it takes to complete each operation by using the Cloud SQL import or export functionality with smaller batches of data.

For whole database migrations, you generally should use BAK files rather than SQL files for imports. Generally, importing from a SQL file takes much longer than importing from a BAK file. 

### Use SqlPackage for importing and exporting data

You can import and export data in Cloud SQL by using [SqlPackage](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage?view=sql-server-ver16). It lets you to export a SQL database, including database schema and user data, to a BACPAC file (.bacpac) and to import the schema and table data from a BACPAC file into a new user database.

SqlPackage uses your credentials to connect to SQL Server to perform database imports and exports. It makes migrations available for all Cloud SQL users. To perform import and export operations, you must have the following:

  * A workstation that is connected to your instance, where you can run SqlPackage. To learn more about connectivity options, see [About connection options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview).

  * SqlPackage installed on your system. To learn more about downloading and installing SqlPackage, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-download?view=sql-server-ver16).

  * Credentials set up to access your instance. To learn more about setting up credentials, see [How to authenticate to Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#authenticate).


**Important:** Cloud SQL uses self-signed certificates that you create at the time of instance creation. For more information, see [Configure SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/sqlserver/configure-ssl-instance). To allow connectivity to a Cloud SQL instance, provide additional SqlPackage parameters as follows: 
* For imports: `/TargetTrustServerCertificate:True`
* For exports: `/SourceTrustServerCertificate:True`
**Note:** A BACPAC import operation will fail if it contains objects that are not supported by Cloud SQL, such as data sources using [PolyBase](https://learn.microsoft.com/en-us/sql/relational-databases/polybase/polybase-guide?view=sql-server-ver16).

**Examples**

### Import

To import data to a database `AdventureWorks2017`, run the following command:
    
    
    c:\Program Files\Microsoft SQL Server\160\DAC\bin>SqlPackage
    /Action:Import /tsn:myTargetServer /tdn:AdventureWorks2017
    /tu:myUsername /sf:mySourceFile
    /TargetTrustServerCertificate:True /tp:myPassword

Here,

  * `mySourceFile` is a source file that you want to use as the source of action from local storage. If you use this parameter, no other source parameter is valid.
  * `myTargetServer` is the name of the server hosting the target database.
  * `myUsername` is the SQL Server username that you want to use to access the target database.
  * `myPassword` is your password in the credentials.



To learn more, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-import?view=sql-server-ver16).

### Export

To export data from a database `AdventureWorks2017`, run the following command:
    
    
    c:\Program Files\Microsoft SQL Server\160\DAC\bin>SqlPackage
    /Action:Export /TargetFile:"myTargetFile"
    /ssn:mySourceServer /su:myUsername /sdn:AdventureWorks2017
    /SourceTrustServerCertificate:True /sp:myPassword

Here,

  * `myTargetFile` is the target file (a .dacpac file) that you want to use as the target of action instead of a database. If you use this parameter, no other target parameter is valid. This parameter is invalid for actions that only support database targets.
  * `myUsername` is the SQL Server username that you want to use to access the source database.
  * `mySourceServer` is the name of the server hosting the source database.
  * `myPassword` is your password in the credentials.



To learn more, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/sqlpackage/sqlpackage-export?view=sql-server-ver16).

### Use the bcp utility for importing and exporting data

Another option to import and export data in Cloud SQL is using the bulk copy program (bcp) utility. By using the bcp utility, you can export data from a SQL Server database into a data file and import data from a data file into a SQL Server database. The bcp utility uses your credentials to connect to SQL Server to perform database imports and exports. It makes transfers available for all Cloud SQL users. To perform import and export operations, you must have the following:

  * A workstation where you can run the bcp utility, and that has connectivity to your Cloud SQL instance. To learn more about connectivity options, see [About connection options](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview).

  * The bcp utility installed on your system. To learn more about downloading and installing bcp, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver16#download-the-latest-version-of-bcp-utility).

  * Credentials set up to access your instance. To learn more about setting up credentials, see [How to authenticate to Cloud SQL](https://docs.cloud.google.com/sql/docs/sqlserver/connect-overview#authenticate).




**Examples**

### Import

To import data from the `person.csv` file to the `Person` table of the `AdventureWorks2017` database, run the following command:
    
    
    bcp Person.Person in "person.csv" -d AdventureWorks2017 -U myLoginID -S myServer

Here,

  * `myLoginID` is the login ID used to connect to SQL Server.
  * `myServer` is the instance of SQL Server to which you want to connect. If you don't specify a server, the bcp utility connects to the default instance of SQL Server on the local computer.



To learn more, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver16).

### Export

To export data from the `Person` table of the `AdventureWorks2017` database to the `person.dat` file, run the following command:
    
    
    bcp Person.Person out "person.dat" -U myLoginID -S myServer -d AdventureWorks2017

Here,

  * `myLoginID` is the login ID used to connect to SQL Server.
  * `myServer` is the instance of SQL Server to which you want to connect. If you don't specify a server, the bcp utility connects to the default instance of SQL Server on the local computer.



To learn more, see the [Microsoft documentation](https://learn.microsoft.com/en-us/sql/tools/bcp-utility?view=sql-server-ver16).

### Use bulk insert for importing data

Bulk insert lets you import data into your Cloud SQL for SQL Server database from a file stored in Cloud Storage.

This section describes the following:

  * [Required roles and permissions](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#roles_permissions)
  * [Considerations when using bulk insert](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#considerations)
  * [Perform bulk insert](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#perform_bulk_insert)
  * [View the imported data](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#view_data)
  * [Disable bulk insert](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#disable_bulk_insert)



#### Required roles and permissions

To configure bulk insert, you need the following:

  * The `CONTROL` permission on the database where you want to import the data.
  * An [HMAC access key](https://docs.cloud.google.com/storage/docs/authentication/hmackeys) and a secret mapped to an IAM account with the following permissions:

    * `storage.buckets.get`
    * `storage.objects.create` and `storage.multipartUploads.create` for writing error logs and examples of bad data.

Alternatively, you can also use following roles:

    * `Storage Object Viewer`
    * `Storage Object Creator` for writing error logs and examples of bad data.



To use bulk insert, you need the following:

  * The `EXECUTE` permission on the `msdb.dbo.gcloudsql_bulk_insert` stored procedure. Cloud SQL creates the stored procedure after bulk insert is enabled on the instance. Cloud SQL grants the `EXECUTE` permission to the `sqlserver` administrator account by default.
  * The `INSERT` permission on the object where you want to import the data.



For more information on creating users for bulk insert, see [Create and manage users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).

#### Considerations when using bulk insert

This section has recommendations for handling security, performance, and reliability on instances while using bulk insert.

##### Security

Cloud SQL encrypts and stores the HMAC access key and secret in an instance as a [database scoped credential](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-scoped-credential-transact-sql?view=sql-server-ver16). Their values cannot be accessed after they are saved. You can delete the key and secret from an instance by [dropping the database scoped credential using a T-SQL command](https://learn.microsoft.com/en-us/sql/t-sql/statements/drop-database-scoped-credential-transact-sql?view=azuresqldb-current&viewFallbackFrom=sql-server-ver16). If you take any backup while the key and secret are stored on the instance, then that backup would contain that key and secret. You can also render the key invalid by [deactivating and deleting the HMAC key](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys#delete).

The following operations can inadvertently transfer the access key and secret and make them available:

  * Cloning the instance: the key and secret are available on the cloned instance.
  * Creating a read replica: the key and secret are available on the created read replica.
  * Restoring from a backup: the key and secret are available on the instance restored from a backup.



We recommend that you drop the key and secret from the target instance after performing these operations.

Bulk insert can write data that it can't parse to a file stored in a Cloud Storage bucket. If you want to protect data that bulk insert has access to, then configure [VPC service controls](https://docs.cloud.google.com/sql/docs/sqlserver/admin-api/configure-service-controls).

##### Performance

We recommend doing the following to mitigate performance impacts while using bulk insert:

  * Test and set an appropriate value for `@batchsize` because by default, all data is imported in a single batch.
  * For large inserts, disable indexes temporarily to speed up data insertion.
  * If possible, use the `@tablock` option because this can reduce contention and increase data load performance.
  * Use the `@ordercolumnsjson` parameter to specify data sorted in the order of the clustered index. This helps with better instance performance.



##### Reliability

We recommend doing the following to mitigate impact on instance reliability while using bulk insert:

  * If a failure occurs and `@batchsize` is used, this can lead to partially loaded data. You might need to manually clean up this data on your instance.
  * Use the `@errorfile` option to keep a log of errors and examples of bad data detected during the load process. This makes it easier to identify rows that have failed to load.



#### Perform bulk insert

You can perform the bulk insert operation using the following stored procedure:
    
    
    msdb.dbo.gcloudsql_bulk_insert
    

For more information, see [Stored procedure for using bulk insert](https://docs.cloud.google.com/sql/docs/sqlserver/stored-procedures#stored_procedure_for_bulk_insert).

##### Example: Import data from a file in Cloud Storage and specify an error file

###### 1\. Enable bulk insert

To enable bulk insert on your instance, enable the `cloud sql enable bulk insert` flag.
    
    
    gcloud sql instances patch INSTANCE_NAME --database-flags="cloud sql enable bulk insert"=on

Replace `INSTANCE_NAME` with the name of the instance that you want to use for bulk insert.

For more information, see [configure database flags](https://docs.cloud.google.com/sql/docs/sqlserver/flags#config).

After you enable this flag on your instance, Cloud SQL installs the bulk insert stored procedure on your instance and gives the `sqlserver` administrator account permissions to execute.

###### 2\. Create an HMAC key

You require an HMAC key to access your Cloud Storage bucket. We recommend that you [create an HMAC key](https://docs.cloud.google.com/storage/docs/authentication/managing-hmackeys#create) for a service account and grant the service account permissions to the buckets that you want to use for bulk insert. For more information and security considerations, see [Considerations when using bulk insert](https://docs.cloud.google.com/sql/docs/sqlserver/import-export#considerations).

###### 3\. Create sample data to import

  1. Using a text editor, create a file with ANSI or UTF-16 encoding that has the following sample data. Save the file in your Cloud Storage bucket and name it as `bulkinsert.bcp`, for example.
         
         1,Elijah,Johnson,1962-03-21
         2,Anya,Smith,1982-01-15
         3,Daniel,Jones,1990-05-21
         

  2. Create a format file using the following sample data. Save the file in your Cloud Storage bucket and name it as `bulkinsert.fmt`, for example. For more information about XML and non-XML format files in SQL Server, see [Create a Format File](https://learn.microsoft.com/en-us/sql/relational-databases/import-export/create-a-format-file-sql-server?view=sql-server-ver16).
         
         13.0
         4
         1       SQLCHAR             0       7       ","      1     PersonID               ""
         2       SQLCHAR             0       25      ","      2     FirstName            SQL_Latin1_General_CP1_CI_AS
         3       SQLCHAR             0       30      ","      3     LastName            SQL_Latin1_General_CP1_CI_AS
         4       SQLCHAR             0       11      "\r\n"   4     BirthDate             ""
         




###### 4\. Execute the stored procedure

  1. Connect to your instance using the `sqlserver` user and create a sample database and table for bulk insert.
         
         USE MASTER
         GO
         -- create test database
         DROP DATABASE IF EXISTS bulktest
         CREATE DATABASE bulktest
         GO
         
         -- create table to insert
         USE bulktest;
         GO
         CREATE TABLE dbo.myfirstimport(
         PersonID smallint,
         FirstName varchar(25),
         LastName varchar(30),
         BirthDate Date
         );
         

  2. Create a [database master key](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-master-key-transact-sql?view=sql-server-ver16), a [database scoped credential](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-database-scoped-credential-transact-sql?view=sql-server-ver16), and an [external data source](https://learn.microsoft.com/en-us/sql/t-sql/statements/create-external-data-source-transact-sql?view=sql-server-ver16). Set the identity as `S3 Access Key`.
         
         -- create master key
         CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'YourStrongPassword1';
         
         -- create database scoped credential
         CREATE DATABASE SCOPED CREDENTIAL GCSCredential
         WITH IDENTITY = 'S3 Access Key',
         SECRET = '<Access key>:<Secret>';
         
         --create external data source
         CREATE EXTERNAL DATA SOURCE GCSStorage
         WITH ( TYPE = BLOB_STORAGE,
         LOCATION = 's3://storage.googleapis.com/bulk-insert-demo/'
         , CREDENTIAL = GCSCredential
         );
         
         CREATE EXTERNAL DATA SOURCE GCSStorageError
         WITH ( TYPE = BLOB_STORAGE,
         LOCATION = 's3://storage.googleapis.com/bulk-insert-demo/'
         , CREDENTIAL = GCSCredential
         );
         

  3. Execute the bulk insert stored procedure to import the sample data.
         
         EXEC msdb.dbo.gcloudsql_bulk_insert
         @database = 'bulktest',
         @schema = 'dbo',
         @object = 'myfirstimport',
         @file = 's3://storage.googleapis.com/bulk-insert-demo/bulkinsert.bcp',
         @formatfile = 's3://storage.googleapis.com/bulk-insert-demo/bulkinsert.fmt',
         @fieldquote = '"',
         @formatfiledatasource = 'GCSStorage',
         @ROWTERMINATOR = '0x0A',
         @fieldterminator = ',',
         @datasource ='GCSStorage',
         @errorfiledatasource = 'GCSStorageError',
         @errorfile = 's3://storage.googleapis.com/oom-data/bulkinsert/bulkinsert_sampleimport.log',
         @ordercolumnsjson =
         '[{"name": "PersonID","order": " asc "},{"name": "BirthDate","order": "asc"}]'
         




#### View the imported data

You can view the imported data by using one of the following methods:

  * Run the following query:
        
        SELECT * FROM dbo.myfirstimport
        

  * Cloud SQL adds a record of this procedure to the SQL error log. You can view this in [Cloud Logging](https://docs.cloud.google.com/sql/docs/sqlserver/logging). You can also view this in the SQL error log data on [SQL Server Management Studio (SSMS)](https://learn.microsoft.com/en-us/sql/ssms/sql-server-management-studio-ssms?view=sql-server-ver16).




#### Disable bulk insert

To disable bulk insert, remove the `cloud sql enable bulk insert` flag:
    
    
      gcloud sql instances patch INSTANCE_NAME --database-flags="cloudsql enable bulk insert"=off
      

Replace `INSTANCE_NAME` with the name of the instance where you want to remove bulk insert.

Alternatively, you can run the following command to clear all database flags:
    
    
      gcloud sql instances patch INSTANCE_NAME --clear-database-flags
      

Replace `INSTANCE_NAME` with the name of the instance where you want to remove bulk insert.

### Use striped import and export

When you perform a striped import or export, you reduce the time it takes for the operation to complete, and enable databases larger than 5 TB to be imported and exported. For more information, see [Export and import using BAK files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak). 

### Verify the imported database

After an import operation is complete, connect to your database and run the appropriate database commands to make sure the contents are correct. For example, [connect](https://docs.cloud.google.com/sql/docs/sqlserver/quickstart#connect) and list the databases, tables, and specific entries.

## Known limitations

For a list of known limitations, see [Issues with importing and exporting data](https://docs.cloud.google.com/sql/docs/sqlserver/known-issues#import-export).

## Security risks

Importing a SQL Server backup file (`.bak`) from an untrusted source can introduce potentially serious security risks.

While backup files that remain within a trusted boundary can generally be trusted, importing a malicious backup file can compromise the security of the entire environment.

A malicious backup file (`.bak`) can potentially expose your applications to the following security risks:

  * The imported backup file can take over much of the SQL Server instance.
  * The imported backup file can escalate privileges and gain unauthorized access.



This attack occurs before any validating scripts or security checks can execute, which makes it extremely dangerous.

Importing an untrusted backup file is equivalent to running untrusted applications on a critical server or virtual machine, and introducing arbitrary code execution into your environment.

### Best practices

Use the following security best practices to help reduce the threat of malicious backup files to your Cloud SQL for SQL Server environments:

  * Treat a backup file import operation as a "high-risk" operation.
  * Use isolated instances to help reduce the threat service area.
  * Only use trusted backup files. Never import backup files from unknown or external sources.
  * Only use backup files that have remained within a trusted boundary. Make sure backup files originate from within your trusted boundary.
  * Never bypass security controls for convenience.
  * Enable server-level auditing to capture backup file and import events and to help mitigate audit evasion.



For more information, see [Security risk of restoring backups from untrusted sources](https://learn.microsoft.com/en-us/sql/relational-databases/backup-restore/back-up-and-restore-of-sql-server-databases?view=sql-server-ver17#security-risk-of-restoring-backups-from-untrusted-sources).

## Automating export operations

Although Cloud SQL doesn't provide a built-in way to automate database exports, you can build your own automation tool using several Google Cloud components. To learn more, see [ this tutorial](https://docs.cloud.google.com/architecture/scheduling-cloud-sql-database-exports-using-cloud-scheduler). 

## Troubleshooting

The following sections cover troubleshooting related to both import and export operations.

### Troubleshooting import operations

Issue | Troubleshooting | `HTTP Error 409: Operation failed because another operation was already in progress`. | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
---|---  
The import operation is taking too long. | Too many active connections can interfere with import operations. Close unused operations. Check the CPU and memory usage of your Cloud SQL instance to make sure there are plenty of resources available. The best way to ensure maximum resources for the import is to restart the instance before beginning the operation. A restart:

  * Closes all connections.
  * Ends any tasks that may be consuming resources.

  
An import operation can fail when one or more users referenced in the dump file don't exist. | Before importing a dump file, all the database users who own objects or were granted permissions on objects in the dumped database must exist in the target database. If they don't, the import operation fails to recreate the objects with the original ownership or permissions. [ Create the database users](https://docs.cloud.google.com/sql/docs/mysql/create-manage-users#creating) before importing.  
LSN mismatch | The order of the import of transaction log backups is incorrect or the transaction log chain is broken. Import the transaction log backups in the same order as that in the [backup set table](https://learn.microsoft.com/en-us/sql/relational-databases/system-tables/backupset-transact-sql?view=sql-server-ver16).   
StopAt too early | This error indicates that the first log in the transaction log file is after the `StopAt` timestamp. For example, if the first log in the transaction log file is at 2023-09-01T12:00:00 and the `StopAt` field has value of 2023-09-01T11:00:00, then Cloud SQL returns this error.  
Ensure that you use the correct `StopAt` timestamp and the correct transaction log file.  
  
### Troubleshooting export operations

Issue | Troubleshooting | `HTTP Error 409: Operation failed because another operation was already in progress.` | There is already a pending operation for your instance. Only one operation is allowed at a time. Try your request after the current operation is complete.  
---|---  
`HTTP Error 403: The service account does not have the required permissions for the bucket.` | Ensure that the bucket exists and the service account for the Cloud SQL instance (which is performing the export) has the `Storage Object Creator` role (`roles/storage.objectCreator`) to allow export to the bucket. See [IAM roles for Cloud Storage](https://docs.cloud.google.com/storage/docs/access-control/iam-roles).  
You want exports to be automated. | Cloud SQL does not provide a way to automate exports. You could build your own automated export system using Google Cloud products such as Cloud Scheduler, Pub/Sub, and Cloud Run functions, similar to this article on [ automating backups](https://betterprogramming.pub/how-to-automate-google-cloud-sql-backups-2de6d3cc7d01).  
  
## What's next

  * [Learn how to import and export data using BAK files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-bak).
  * [Learn how to import data using SQL dump files](https://docs.cloud.google.com/sql/docs/sqlserver/import-export/import-export-sql).
  * [Learn how to enable automatic backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/backups).
  * [Learn how to restore from backups](https://docs.cloud.google.com/sql/docs/sqlserver/backup-recovery/restore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
