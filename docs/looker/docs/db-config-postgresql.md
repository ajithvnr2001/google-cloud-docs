---
url: https://docs.cloud.google.com/looker/docs/db-config-postgresql/
title: PostgreSQL \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T03:31:26.922824+00:00
---

# PostgreSQL  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  PostgreSQL Stay organized with collections  Save and categorize content based on your preferences. 

To connect Looker to a PostgreSQL database, you must configure your database. This document explains how to set up user accounts, grant required permissions, and define schema and connection parameters. For information about PostgreSQL on Heroku or Cloud SQL for PostgreSQL, see their documentation.

## Dialects that use these instructions

The following dialects share database setup requirements as described on this page:

  * PostgreSQL
  * Microsoft Azure PostgreSQL
  * Amazon Aurora PostgreSQL
  * Amazon RDS for PostgreSQL



For Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL, Looker includes [integration support](https://docs.cloud.google.com/looker/docs/dialects#support_levels).

For PostgreSQL on Heroku, see the [Heroku documentation](https://devcenter.heroku.com/articles/heroku-postgresql).

For Google Cloud SQL for PostgreSQL, see our dedicated [Google Cloud SQL for PostgreSQL](https://docs.cloud.google.com/looker/docs/db-config-cloud-sql-postgresql) page.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

If you're interested in using SSL encryption, see the [PostgreSQL documentation](https://www.postgresql.org/docs/).

## Users and security

To perform actions on your database, Looker needs to have a user account on your database.

To configure a database user for Looker to use, perform the following steps on your database:

  1. Create a database user and password.
         
         CREATE USER USERNAME WITH ENCRYPTED PASSWORD 'PASSWORD';
         

  2. Grant permissions to the database user so that Looker can perform actions on your database:
         
         GRANT CONNECT ON DATABASE DATABASE_NAME to USERNAME;
         \c DATABASE_NAME
         GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO USERNAME;
         GRANT SELECT ON ALL TABLES IN SCHEMA public TO USERNAME;
         

  3. If you're using a schema other than `public`, run this command to grant usage permissions to Looker:
         
         GRANT USAGE ON SCHEMA SCHEMA_NAME TO USERNAME;
         

  4. To make sure that future tables that you add to the public schema are also available to the Looker user, run these commands:
         
         ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON tables TO USERNAME;
         ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON sequences TO USERNAME;
         




Depending on your setup, the preceding commands may need to be altered. If another user or role is creating tables that the Looker user needs future permissions for, you must specify a _target_ role or user to apply the Looker user's permission grants to:
    
    
    ALTER DEFAULT PRIVILEGES FOR USER ANOTHER_USERNAME IN SCHEMA SCHEMA_NAME GRANT SELECT ON tables TO USERNAME;
    ALTER DEFAULT PRIVILEGES FOR ROLE TARGET_ROLE IN SCHEMA SCHEMA_NAME GRANT SELECT ON sequences TO USERNAME;
    

For example, if a `web_app` user creates tables and you want the `looker` user to be able to use those tables, you must run a `GRANT` statement to give the `looker` user permissions on tables that are created by the `web_app` user. The target role or user in this case is the `web_app` user, which means that you want to alter privileges on tables that are created by `web_app` so that the `looker` user can have permissions to read the tables. Here is an example:
    
    
    ALTER DEFAULT PRIVILEGES FOR USER web_app IN SCHEMA public GRANT SELECT ON tables TO looker;
    

See [`ALTER DEFAULT PRIVILEGES`](https://www.postgresql.org/docs/9.4/sql-alterdefaultprivileges.html) on PostgreSQL's website for more information.

## Temp schema setup

### Self-hosted Postgres

Create a schema owned by the Looker user:
    
    
    CREATE SCHEMA SCHEMA_NAME AUTHORIZATION USERNAME;
    

### Postgres on Amazon RDS

Create a scratch schema:
    
    
    CREATE SCHEMA SCHEMA_NAME;
    

Change the ownership of the scratch schema to the Looker user:
    
    
    ALTER SCHEMA SCHEMA_NAME OWNER TO USERNAME;
    

**Note:** For PostgreSQL persistent derived tables to work, you must not be using Looker on top of a "hot swap" streaming replication database. You must be able to write to the database from outside the application.

## Setting the `search_path`

Before connecting Looker to your database, you should set an appropriate `search_path`, which the Looker SQL Runner can use to retrieve certain metadata from your database:
    
    
    ALTER USER USERNAME SET search_path TO '$user',SCHEMA_NAME,SCHEMA_NAME_2,SCHEMA_NAME_3
                                                                ^^^^^^^^^^^^^^^^^^
                                                                ^^^^^^^^^^^^^^^^^^
                                                 include a comma-separated list of
                                                all schemas that you'll use with Looker
    

**Note:** If you're on a Looker (Google Cloud core) instance and you want to use ADC, use the impersonated service account username that you [added to your Cloud SQL database](https://docs.cloud.google.com/looker/docs/looker-core-dialects#add-the-impersonated-service-account). The service account username will have the format `service-<project number>@gcp-sa-looker.iam.gserviceaccount.com`. If the service account username ends with `.gserviceaccount.com`, remove the `.gserviceaccount.com` portion of the username. After it's truncated, the username would look like `service-<project number>@gcp-sa-looker.iam`.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. Open the **Connect your database to Looker** page by doing one of the following:

     * Click the menu **Main menu** icon and select **Admin** , and then select **Connections** from the **Database** section in the **Admin** panel. On the **Connections** page, click the **Add Connection** button.
     * Click the **Create** button in the [main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content#using_the_main_navigation_menu), and then select the **Connection** menu item.
  2. From the **Dialect** drop-down menu, select your database dialect name:

     * For Microsoft Azure PostgreSQL, select **Microsoft Azure PostgreSQL**.
     * For PostgreSQL, select **PostgreSQL 9.5+** or **PostgreSQL pre-9.5** , depending on your version of PostgreSQL.
     * For Amazon RDS for PostgreSQL and Amazon Aurora PostgreSQL, select **PostgreSQL 9.5+**.
**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for more information.

  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For PostgreSQL, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `allowEncodingChanges`
  * `ApplicationName`
  * `assumeMinServerVersion`
  * `binaryTransfer`
  * `binaryTransferDisable`
  * `binaryTransferEnable`
  * `cancelSignalTimeout`
  * `connectTimeout`
  * `currentSchema`
  * `databaseMetadataCacheFields`
  * `defaultRowFetchSize`
  * `escapeSyntaxCallMode`
  * `gssEncMode`
  * `hostRecheckSeconds`
  * `jaasApplicationName`
  * `jaasLogin`
  * `kerberosServerName`
  * `loadBalanceHosts`
  * `loginTimeout`
  * `logServerErrorDetail`
  * `options`
  * `password`
  * `preferQueryMode`
  * `preparedStatementCacheQueries`
  * `prepareThreshold`
  * `queryTimeout`
  * `readOnly`
  * `reWriteBatchedInserts`
  * `socketTimeout`
  * `ssl`
  * `sslfactory`
  * `sslhostnameverifier`
  * `sslmode`
  * `sslNegotiation`
  * `sslpassword`
  * `sslpasswordcallback`
  * `stringtype`
  * `targetServerType`
  * `tcpKeepAlive`
  * `unknownLength`
  * `user`



## Feature support

For Looker to support some features, your database dialect must also support them.

PostgreSQL 9.5+ supports the following features as of Looker 26.18:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
Microsoft Azure PostgreSQL supports the following features as of Looker 26.18:

Feature | Supported?  
---|---  
Looker (Google Cloud core)|   
Symmetric aggregates|   
Derived tables|   
Persistent SQL derived tables|   
Persistent native derived tables|   
Stable views|   
Query killing|   
SQL-based pivots|   
Time zones|   
SSL|   
Subtotals|   
JDBC additional params|   
Case-sensitive|   
Location type|   
List type|   
Percentile|   
Distinct percentile|   
SQL Runner Show Processes|   
SQL Runner Describe Table|   
SQL Runner Show Indexes|   
SQL Runner Select 10|   
SQL Runner Count|   
SQL Explain|   
OAuth 2.0 credentials|   
Context comments|   
Connection pooling|   
HLL sketches|   
Aggregate awareness|   
Incremental PDTs|   
Milliseconds|   
Microseconds|   
Materialized views|   
Period-over-period measures|   
Approximate count distinct|   
In-database analytic models|   
Custom calendars|   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
