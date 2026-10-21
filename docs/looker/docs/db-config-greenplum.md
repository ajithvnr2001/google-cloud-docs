---
url: https://docs.cloud.google.com/looker/docs/db-config-greenplum/
title: Greenplum \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T17:07:33.157551+00:00
---

# Greenplum  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-greenplum/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Greenplum Stay organized with collections  Save and categorize content based on your preferences. 

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

If you're interested in using SSL encryption, see this [official Greenplum security configuration guide](http://gpdb.docs.pivotal.io/security/pdf/GP_SecurityConfig_A01.pdf).

## Users and security

Change `some_password_here` to a unique, secure password:
    
    
    CREATE USER looker WITH ENCRYPTED PASSWORD 'password';
    GRANT CONNECT ON DATABASE database_name to looker;
    \c database_name
    GRANT SELECT ON ALL SEQUENCES IN SCHEMA public TO looker;
    GRANT SELECT ON ALL TABLES IN SCHEMA public TO looker;
    

To grant Looker the necessary permissions to cancel its queries, run the following command:
    
    
    CREATE OR REPLACE FUNCTION pg_kill_connection(integer) RETURNS boolean AS 'select pg_terminate_backend($1);' LANGUAGE SQL SECURITY DEFINER;
    

## Temp schema setup

Create a schema owned by the Looker user:
    
    
    CREATE SCHEMA looker_scratch AUTHORIZATION looker;
    

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Greenplum** from the **Dialect** drop-down menu.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Greenplum, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

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

Greenplum supports the following features as of Looker 26.18:

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
  
## Next steps

After completing the database configuration, you can [connect to the database from Looker](https://docs.cloud.google.com/looker/docs/connecting-to-your-db).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
