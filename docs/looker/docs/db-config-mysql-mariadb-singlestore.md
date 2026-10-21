---
url: https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore/
title: MySQL, MariaDB, and SingleStore \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:13.566099+00:00
---

# MySQL, MariaDB, and SingleStore  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-mysql-mariadb-singlestore/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  MySQL, MariaDB, and SingleStore Stay organized with collections  Save and categorize content based on your preferences. 

## Dialects that use these instructions

MySQL, MariaDB, and SingleStore (formerly MemSQL) share the database setup requirements described on this page.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

If you're interested in using SSL encryption, see this [MySQL documentation page](https://dev.mysql.com/doc/refman/5.7/en/encrypted-connections.html).

## Users and security

To create and grant the required access to the Looker user, follow the instructions in the section appropriate to your database dialect and version:

### MySQL 8.0.X:

**Note:** The Looker MySQL 8.0.X dialect option is implemented with the patch version 8.0.12+ because of a [MySQL deprecation](https://dev.mysql.com/worklog/task/?id=8693) in implicit sorting in the `GROUP BY` clause. This affects Looker subtotals for MySQL versions 8.0.0 through 8.0.11, causing SQL generation errors. Looker suggests upgrading any MySQL 8.0.X databases to at least 8.0.12 to fully integrate. However, earlier MySQL versions will still work, aside from [subtotals](https://docs.cloud.google.com/looker/docs/table-options#subtotals).

In MySQL 8.0.X, the default authentication plugin is `caching_sha2_password`. Looker uses the `mysql_native_password` plugin to attempt to authenticate to MySQL databases through the JDBC driver. For this version of MySQL to work properly, you must take the following additional steps:

  1. Configure the MySQL database to use the `mysql_native_password` plugin. This can be done in multiple ways, and will depend on how your MySQL 8 database is deployed and what type of access you have to the configuration:

     * Start the process with the flag `--default-auth=mysql_native_password`

     * Set the property in the [`my.cnf`](https://dev.mysql.com/doc/refman/8.0/en/option-files.html) configuration file:
    
    [mysqld]
    default-authentication-plugin=mysql_native_password
    

     * If your database instance is hosted through AWS RDS, set the `default_authentication_plugin` parameter through an RDS Parameter Group that is applied to this database instance.
  2. Run the following commands, replacing `some_password_here` with a unique, secure password:
         
         CREATE USER looker IDENTIFIED WITH mysql_native_password BY 'some_password_here';
         GRANT SELECT ON database_name.* TO 'looker'@'%';
         




### MySQL 5.7.X and earlier, MariaDB, and SingleStore:

Run the following commands, replacing `some_password_here` with a unique, secure password:
    
    
    CREATE USER looker;
    SET PASSWORD FOR looker = PASSWORD ('some_password_here');
    GRANT SELECT ON database_name.* TO 'looker'@'%';
    

## Temp schema setup for persistent derived tables

These database dialects support the creation of [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). This feature can be very useful, and we recommend enabling it when possible.

To enable PDTs, you need to configure a temp schema. The following commands show an example of creating a temp database and granting the required privileges to the `looker` user.

> You can specify the name of the temp database in the [**Temp Database**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#temp_database) field when [creating your database connection](https://docs.cloud.google.com/looker/docs/connecting-to-your-db). If you don't specify a temp database name, Looker generates a scratch database named `looker_tmp`. The following commands use `looker_tmp`, but if you specified a different temp database name, use your temp database name instead of `looker_tmp`.
    
    
    CREATE SCHEMA looker_tmp;
    GRANT
      SELECT,
      INDEX,
      INSERT,
      UPDATE,
      DELETE,
      CREATE,
      DROP,
      ALTER,
      CREATE TEMPORARY TABLES
    ON looker_tmp.* TO 'looker'@'%';
    

For SingleStore, or if your database uses GTID-based replication, you must use the [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) LookML parameter to use PDTs, because GTID does not support `CREATE TABLE AS SELECT` statements.

## Alternative setup for regular derived tables

If you don't want to allow the creation of [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables), you can still use [regular derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#regular-or-ephemeral-derived-tables). To use regular derived tables, you still need to add certain permissions to a schema called `looker_tmp`. However, the `looker_tmp` schema does not actually need to exist in your database!
    
    
    GRANT
      SELECT,
      INDEX,
      INSERT,
      DROP,
      CREATE TEMPORARY TABLES
    ON looker_tmp.* TO 'looker'@'%';
    -- Note that the looker_tmp schema does not need to actually exist,
    -- even though these permission grants are still needed
    

## Setting the `max_allowed_packet` variable

For MySQL, set the MySQL `max_allowed_packet` variable to its maximum value, 1073741824, to prevent "SQLException: Packet for query is too large" errors.

## Creating the Looker connection to your database

After completing the database configuration, you can connect to the database from Looker. Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select your database dialect name: **MySQL** , **MySQL 8.0.12+** , **MariaDB** , **SingleStore** , or **SingleStore 7+**.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For MySQL, MariaDB, and SingleStore, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `allowMultiQueries`
  * `autocommit`
  * `characterSetResults`
  * `clientCertificateKeyStorePassword`
  * `clientCertificateKeyStoreUrl`
  * `connectionAttributes`
  * `connectionCollation`
  * `connectionTimeZone`
  * `connectTimeout`
  * `defaultAuthenticationPlugin`
  * `disableSslHostnameVerification`
  * `disconnectOnExpiredPasswords`
  * `enabledSslCipherSuites`
  * `failOverReadOnly`
  * `fallbackToSystemTrustStore`
  * `forceConnectionTimeZoneToSession`
  * `interactiveClient`
  * `lookerFailover`
  * `maxIdleTime`
  * `maxQuerySizeToLog`
  * `oldModeNoPrecisionTimestamp`
  * `password`
  * `passwordCharacterEncoding`
  * `permitMysqlScheme`
  * `pinGlobalTxToPhysicalConnection`
  * `preserveInstants`
  * `queryInterceptors`
  * `restrictedAuth`
  * `rewriteBatchedStatements`
  * `socketTimeout`
  * `sslMode`
  * `tcpKeepAlive`
  * `trustCertificateKeyStorePassword`
  * `trustCertificateKeyStoreUrl`
  * `useCompression`
  * `usePipelineAuth`
  * `user`
  * `useServerPrepStmts`
  * `verifyServerCertificate`
  * `yearIsDateType`



## Feature support

For Looker to support some features, your database dialect must also support them.

MySQL supports the following features as of Looker 26.20:

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
  
MySQL 8.0.12+ supports the following features as of Looker 26.20:

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
  
MariaDB supports the following features as of Looker 26.20:

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
  
SingleStore supports the following features as of Looker 26.20:

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
  
SingleStore 7+ supports the following features as of Looker 26.20:

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

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
