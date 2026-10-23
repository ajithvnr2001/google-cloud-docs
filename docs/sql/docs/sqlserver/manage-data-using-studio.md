---
url: https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio/
title: Manage your data using Cloud SQL Studio \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:19:29.274214+00:00
---

# Manage your data using Cloud SQL Studio  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/manage-data-using-studio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/sqlserver/features)



Send feedback 

#  Manage your data using Cloud SQL Studio Stay organized with collections  Save and categorize content based on your preferences. 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio "View this page for the MySQL database engine") | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/manage-data-using-studio "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to explore and manage your Cloud SQL data using Cloud SQL Studio in the Google Cloud console.

Cloud SQL Studio lets authorized users interact directly with the SQL database and run SQL queries from the Google Cloud console to access and manipulate data. You can perform a range of actions that you would perform on a SQL command line client, such as creating tables and indexes, modifying tables, or setting up views.

Cloud SQL Studio includes an **Explorer** pane that integrates with a query editor and a SQL query results table. You can run DDL, DML, and DQL statements from this one interface. For example, instead of configuring a third-party database query tool, you can create a table and query your data using the query editor in Cloud SQL Studio.

You can use the **Explorer** pane to view and interact with your database objects. You create, alter, and delete the database objects, such as the following:

  * Tables
  * Columns
  * Indexes and keys
  * Functions



You can also use the **Explorer** pane to seed `SELECT` queries for tables.

Cloud SQL Studio automatically validates the syntax when you type a query or select part of a query.

**Note:** System-level views in the `INFORMATION_SCHEMA` schema is read-only.

If you're new to Cloud SQL, see [Cloud SQL overview](https://docs.cloud.google.com/sql/docs/sqlserver/introduction).

### Required roles and permissions

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the [Cloud SQL Studio User ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudsql#cloudsql.studioUser) (`roles/cloudsql.studioUser`) IAM role on the project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

To use Cloud SQL Studio, you must have the following permissions:

  * `cloudsql.databases.list`
  * `cloudsql.instances.executeSql`
  * `cloudsql.instances.get`
  * `cloudsql.users.list`



Additionally, ensure that you have database-level permissions for the database that you're using for authentication, and the password for the privileged database user that you're using.

### Authenticate to Cloud SQL Studio

Before you can access a database in Cloud SQL Studio, you must first authenticate to the database. To sign in to your database using Cloud SQL Studio, use built-in database authentication. For more information, see [Create and manage users](https://docs.cloud.google.com/sql/docs/sqlserver/create-manage-users).

Cloud SQL Studio doesn't support Active Directory authentication.

### Explore your data

To access the **Explorer** pane, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select an instance from the list.
  3. In the navigation menu, click **Cloud SQL Studio**.
  4. Sign in to Cloud SQL Studio using the name of your database, username, and password. The **Explorer** pane displays a list of the objects in your database.



### Create, modify, and query your data

Using the SQL editor, you can run a combination of DDL, DML, and DQL statements. You can compose a query yourself, or you can populate the query editor with a template using the explorer.

To structure, modify, or query your data, follow these steps:

  1. In the Google Cloud console, go to the **Cloud SQL Instances** page.

[Go to Cloud SQL Instances](https://console.cloud.google.com/sql)

  2. Select an instance from the list.
  3. In the navigation menu, click **Cloud SQL Studio**.
  4. Sign in to Cloud SQL Studio using the name of your database, username, and password.
  5. Compose a query using one of the following methods: 
     * To compose your own query, follow these steps: 
       1. Open a new tab by clicking add.
       2. When the query editor appears, write your query.
     * To compose a query starting with a template, follow these steps: 
       1. In the **Explorer** pane, next to a database object or collection, click more_vert **View actions**. One or more available actions appear.
       2. Click an action. The query editor populates with a template.
       3. Replace any placeholders in the template.
  6. Run your queries using either of the following approaches:

     * To execute all the statements in the query editor, click **Run**.
     * To run specific statements, select one or multiple statements, and click **Run selected**.
  7. The results of your queries appear in the **Results** tab. If multiple result sets are available, select a result from the **All results** drop-down list.




### Validate query syntax

When you enter your query into the query editor, Cloud SQL Studio validates the statements automatically to check for syntax errors.

### Limitations

  * Cloud SQL Studio supports lightweight queries. If the SQL response is over 10MB, then the response will be truncated. Cloud SQL Studio indicates when partial results are returned.
  * You can only run queries for Cloud SQL instances that are running.
  * Cloud SQL Studio doesn't support external servers.
  * Requests taking longer than five minutes are canceled. Setting a higher query timeout using `SET LOCK_TIMEOUT` isn't supported. 
  * Cloud SQL Studio doesn't keep a database connection open after execution of a SQL script is completed. Similarly, editor tabs don't share a common session and every execution starts a new session.
  * When you run a mix of DML, DQL, and DDL statements, only results from the DQL queries will be displayed.
  * Closing your browser or browser tab doesn't stop the query execution in Cloud SQL Studio. The query will run until it completes or times out.
  * Cloud SQL Studio uses the `executeSql` API to execute the queries. Cloud SQL limits the number of concurrent `executeSql` requests per instance to prevent overload. If the limit is reached, subsequent requests fail and return one of the following errors:

    * `At most 'x' concurrent queries may be run on this instance. Try again later.`
    * `Maximum concurrent reads 'x' reached.`

The limit (`x`) is 5 queries for instances with less than 10 GB of [total memory](https://docs.cloud.google.com/sql/docs/sqlserver/machine-series-overview), and 10 queries for instances with at least 10 GB of total memory. 



  * Cloud SQL Studio doesn't support the `GO` command. This command is used in Microsoft SQL Server utilities to indicate that a batch of statements have ended and can be sent to SQL Server.
  * If a query includes a binary column, Cloud SQL Studio can't show it. Convert binary values to a string instead.

For example, replace:
        
        SELECT my_binary_column from my_table2;
        

with:
        
        SELECT CONVERT(NVARCHAR(4000), my_binary_column, 1) from my_table2;
        

  * When running multiple queries and one of them fails, the first encountered error is returned. Some of the statements in the batch prior to the error might have executed successfully. You can wrap multiple queries in a `transaction` statement to prevent this issue:
        
        BEGIN TRANSACTION
            YOUR_SQL_STATEMENTS
        COMMIT;
        

Replace the following:

    * YOUR_SQL_STATEMENTS: the statements you want to run as part of this query
  * Cloud SQL Studio only displays tabular query results (`SELECT` statements) and doesn't display output returned by T-SQL `PRINT` statements or informational messages. Stored procedures that output scripts using `PRINT` statements (such as `sp_help_revlogin`) execute successfully in Cloud SQL Studio but return an empty results pane. To view or export output from these procedures, use client tools such as SQL Server Management Studio (SSMS), Visual Studio Code with the MSSQL extension (in the **Messages** tab), or the `sqlcmd` command-line utility.



  * The SQL script and its execution response might transit through intermediate locations between your client and the location of the target instance.



## What's next

  * [Write SQL with Gemini assistance](https://docs.cloud.google.com/sql/docs/sqlserver/write-sql-gemini)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
