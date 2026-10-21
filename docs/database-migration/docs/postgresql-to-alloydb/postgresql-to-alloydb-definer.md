---
url: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/postgresql-to-alloydb-definer/
title: Create and run a SQL Server migration job containing metadata with an EXECUTE AS clause \u00a0|\u00a0 Database Migration Service for PostgreSQL to AlloyDB \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T11:59:51.805420+00:00
---

# Create and run a SQL Server migration job containing metadata with an EXECUTE AS clause  |  Database Migration Service for PostgreSQL to AlloyDB  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb/postgresql-to-alloydb-definer/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ PostgreSQL to AlloyDB ](https://docs.cloud.google.com/database-migration/docs/postgresql-to-alloydb)



Send feedback 

#  Create and run a SQL Server migration job containing metadata with an EXECUTE AS clause Stay organized with collections  Save and categorize content based on your preferences. 

## Overview

A SQL Server migration job [doesn't migrate database user and server login data](https://docs.cloud.google.com/database-migration/docs/sqlserver/migration-fidelity). Therefore, sources which contain objects defined by users with the `EXECUTE AS '[database_user_name]'` clause won't be migrated to the new Cloud SQL replica, because the users don't yet exist there. As a result, the overall migration process will fail.

For example: 
    
    
    CREATE OR ALTER PROCEDURE dbo.example
    WITH EXECUTE AS 'some_user'
    AS BEGIN
    …
    END
    

This stored procedure won't be migrated because the `some_user` user can't be migrated. This is because the user doesn't exist on the target database.

To identify which objects are using the `EXECUTE AS '[database_user_name]'` clause in your source database, use these queries and check if there are users for them in the destination database.
    
    
    SELECT s.name AS schema_name, o.name AS object_name, p.name AS user_name
    FROM sys.sql_modules m  
    INNER JOIN sys.objects o ON o.object_id = m.object_id
    INNER JOIN sys.schemas s ON s.schema_id = o.schema_id
    INNER JOIN sys.database_principals p ON p.principal_id = m.execute_as_principal_id
    

To run a migration job from a source which includes such metadata, create the users on your destination Cloud SQL instance before starting your migration job.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-19 UTC."],[],[]] 
