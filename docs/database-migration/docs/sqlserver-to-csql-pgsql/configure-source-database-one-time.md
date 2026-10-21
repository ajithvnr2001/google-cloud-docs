---
url: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-source-database-one-time/
title: Configure your source SQL Server database for a one-time migration \u00a0|\u00a0 Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:01:18.680933+00:00
---

# Configure your source SQL Server database for a one-time migration  |  Database Migration Service for heterogeneous SQL Server to Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-source-database-one-time/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ SQL Server to Cloud SQL for PostgreSQL ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql)
  * [ Guides ](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/scenario-overview)



Send feedback 

#  Configure your source SQL Server database for a one-time migration Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to configure the following source database instances for one-time heterogeneous SQL Server migrations:

  * Cloud SQL for SQL Server
  * Self-hosted SQL Server
  * Amazon RDS for SQL Server
  * Microsoft Azure sources: Microsoft Azure SQL Managed Instance and Microsoft Azure SQL Database



## Configure a Cloud SQL for SQL Server instance

To configure a Cloud SQL for SQL Server source instance for your migration process, do the following:

  1. Create a dedicated migration user account in your instance. See [ Create a user](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users#creating) in the Cloud SQL documentation. 
  2. Connect to your Cloud SQL instance with a SQL client. You can use the following methods: 
     * [ `sqlcmd` client](https://docs.cloud.google.com/sql/docs/sqlserver/connect-admin-ip). You can use this method to connect to your instance private IP, but it might require that you create a Compute Engine virtual machine. 
     * [ `gcloud sql connect`](https://docs.cloud.google.com/sdk/gcloud/reference/sql/connect) command. This command works only for Cloud SQL instances that have a public IP address enabled. 
  3. Assign the `db_datareader` role to the migration user you created in step 1. 
         
         EXEC sp_addrolemember 'db_datareader', 'USER_NAME';

  4. Grant the `VIEW DATABASE STATE` permission to the migration user: 
         
         GRANT VIEW DATABASE STATE TO USER_NAME;

  5. At this stage, we also recommend that you check for objects defined with `EXECUTE AS DATABASE_USER` statements. 

Database Migration Service doesn't migrate user and server login data. If your source database contains objects defined with the `EXECUTE AS DATABASE_USER` clause, these objects might not function properly after the migration because the destination database won't have these users. 

You can check for such objects in your source database ahead of migration with the following SQL query: 
         
         SELECT s.name AS schema_name, o.name AS object_name, p.name AS user_name
         FROM sys.sql_modules m
         INNER JOIN sys.objects o ON o.object_id = m.object_id
         INNER JOIN sys.schemas s ON s.schema_id = o.schema_id
         INNER JOIN sys.database_principals p ON p.principal_id = m.execute_as_principal_id

If the query returns any results, you have to create the same user logins in the destination database when you [ Create and configure the destination Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database). 




## Configure a self-hosted database

To configure a self-hosted SQL Server source instance for your migration process, do the following:

  1. Connect to your source instance with a SQL client, for example the [ `sqlcmd`](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility) utility. 
  2. At the SQL prompt, create a login in the master database. Run the following command: 
         
         USE master;
         CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';

  3. In each database you want to migrate, create a dedicated migration user account for the login from the previous step. Grant the `db_datareader` role and the `VIEW DATABASE STATE` permissions to the dedicated account. 
         
         USE DATABASE_NAME;
         CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
         EXEC sp_addrolemember 'db_datareader', 'USER_NAME';
         GRANT VIEW DATABASE STATE TO USER_NAME;

  4. Start SQL Server Agent and make sure it's running at all times. See [ Start, stop, or restart an instance of SQL Server Agent](https://learn.microsoft.com/en-us/sql/database-engine/configure-windows/start-stop-pause-resume-restart-sql-server-services#start-stop-or-restart-an-instance-of-the-sql-server-agent) in Microsoft documentation. 
  5. At this stage, we also recommend that you check for objects defined with `EXECUTE AS DATABASE_USER` statements. 

Database Migration Service doesn't migrate user and server login data. If your source database contains objects defined with the `EXECUTE AS DATABASE_USER` clause, these objects might not function properly after the migration because the destination database won't have these users. 

You can check for such objects in your source database ahead of migration with the following SQL query: 
         
         SELECT s.name AS schema_name, o.name AS object_name, p.name AS user_name
         FROM sys.sql_modules m
         INNER JOIN sys.objects o ON o.object_id = m.object_id
         INNER JOIN sys.schemas s ON s.schema_id = o.schema_id
         INNER JOIN sys.database_principals p ON p.principal_id = m.execute_as_principal_id

If the query returns any results, you have to create the same user logins in the destination database when you [ Create and configure the destination Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database). 




## Configure an Amazon RDS for SQL Server database

To configure an Amazon RDS for SQL Server source instance for your migration process, do the following:

  1. Connect to your source instance with a SQL client. See [ Connecting to a DB instance running the Microsoft SQL Server database engine](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/USER_ConnectToMicrosoftSQLServerInstance.html) in Amazon RDS documentation. 
  2. At the SQL prompt, create a login in the master database. Run the following command: 
         
         USE master;
         CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';

  3. In each database you want to migrate, create a dedicated migration user account for the login from the previous step. Grant the `db_datareader` role and the `VIEW DATABASE STATE` permissions to the dedicated account. 
         
         USE DATABASE_NAME;
         CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
         EXEC sp_addrolemember 'db_datareader', 'USER_NAME';
         GRANT VIEW DATABASE STATE TO USER_NAME;

  4. Database Migration Service requires that SQL Server Agent is running at all times in your source instance. Amazon RDS databases run SQL Server Agent by default, so you don't have to configure anything. See [ Use SQL Server Agent](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.CommonDBATasks.Agent.html) in Amazon RDS documentation. 
  5. At this stage, we also recommend that you check for objects defined with `EXECUTE AS DATABASE_USER` statements. 

Database Migration Service doesn't migrate user and server login data. If your source database contains objects defined with the `EXECUTE AS DATABASE_USER` clause, these objects might not function properly after the migration because the destination database won't have these users. 

You can check for such objects in your source database ahead of migration with the following SQL query: 
         
         SELECT s.name AS schema_name, o.name AS object_name, p.name AS user_name
         FROM sys.sql_modules m
         INNER JOIN sys.objects o ON o.object_id = m.object_id
         INNER JOIN sys.schemas s ON s.schema_id = o.schema_id
         INNER JOIN sys.database_principals p ON p.principal_id = m.execute_as_principal_id

If the query returns any results, you have to create the same user logins in the destination database when you [ Create and configure the destination Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database). 




## Configure a Microsoft Azure database

To configure a Microsoft Azure SQL Managed Instance or Microsoft Azure SQL Database source instance for your migration process, do the following:

  1. Connect to your source instance with a SQL client, for example the [ `sqlcmd`](https://learn.microsoft.com/en-us/sql/tools/sqlcmd/sqlcmd-utility) utility, [ Azure Data Studio](https://learn.microsoft.com/en-us/azure-data-studio/connect), or [ SQL Server Management Studio](https://learn.microsoft.com/en-us/azure-data-studio/connect). 
  2. At the SQL prompt, create a login in the master database. Run the following command: 
         
         USE master;
         CREATE LOGIN YOUR_LOGIN WITH PASSWORD = 'PASSWORD';

  3. In each database you want to migrate, create a dedicated migration user account for the login from the previous step. Grant the `db_datareader` role and the `VIEW DATABASE STATE` permissions to the dedicated account. 
         
         USE DATABASE_NAME;
         CREATE USER USER_NAME FOR LOGIN YOUR_LOGIN;
         EXEC sp_addrolemember 'db_datareader', 'USER_NAME';
         GRANT VIEW DATABASE STATE TO USER_NAME;

  4. At this stage, we also recommend that you check for objects defined with `EXECUTE AS DATABASE_USER` statements. 

Database Migration Service doesn't migrate user and server login data. If your source database contains objects defined with the `EXECUTE AS DATABASE_USER` clause, these objects might not function properly after the migration because the destination database won't have these users. 

You can check for such objects in your source database ahead of migration with the following SQL query: 
         
         SELECT s.name AS schema_name, o.name AS object_name, p.name AS user_name
         FROM sys.sql_modules m
         INNER JOIN sys.objects o ON o.object_id = m.object_id
         INNER JOIN sys.schemas s ON s.schema_id = o.schema_id
         INNER JOIN sys.database_principals p ON p.principal_id = m.execute_as_principal_id

If the query returns any results, you have to create the same user logins in the destination database when you [ Create and configure the destination Cloud SQL instance](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/configure-destination-database). 




## What's next

  * Learn about source database network connectivity. See [ Source database networking methods](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/networking-methods-source).

  * To get a complete, step-by-step migration walkthrough, see [ SQL Server to Cloud SQL for PostgreSQL migration guide](https://docs.cloud.google.com/database-migration/docs/sqlserver-to-csql-pgsql/guide).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
