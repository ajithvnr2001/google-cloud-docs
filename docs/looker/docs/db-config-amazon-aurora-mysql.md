---
url: https://docs.cloud.google.com/looker/docs/db-config-amazon-aurora-mysql/
title: Amazon Aurora MySQL \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:13.954436+00:00
---

# Amazon Aurora MySQL  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-amazon-aurora-mysql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Amazon Aurora MySQL Stay organized with collections  Save and categorize content based on your preferences. 

To connect Looker to [Amazon Aurora MySQL](https://aws.amazon.com/rds/aurora/), follow the instructions found on the documentation page for connecting to [Amazon RDS for MySQL](https://docs.cloud.google.com/looker/docs/db-config-mysql-on-amazon-rds).

In addition to the steps in the [Amazon RDS instructions](https://docs.cloud.google.com/looker/docs/db-config-mysql-on-amazon-rds), Amazon Aurora may need further setup, depending on your configuration. If you have a redirected read-only endpoint for Amazon Aurora, or if you want to use [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table), see the following sections.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Alternate failover and load balancing modes

Amazon Aurora MySQL can be configured to use [alternate failover and load balancing modes](https://mariadb.com/kb/en/about-mariadb-connector-j/#failover-and-load-balancing-modes) to choose the appropriate JDBC connection behavior you want. Check the linked documentation to see how these alternative parameters change the behavior.

You can set the `lookerFailover` parameter in the **Additional JDBC parameters** field to control these modes.

The options can be used to change the JDBC string as follows:

  * `lookerFailover=false`: `jdbc:mysql:hostname...`
  * `lookerFailover=sequential`: `jdbc:mysql:sequential:hostname...`
    * You can do the same with `lookerFailover=loadbalance`, `lookerFailover=replication`, and `lookerFailover=aurora`
  * If `lookerFailover` is not included, the default behavior is: `jdbc:mysql:aurora:hostname...`
  * If `cluster-ro` is in the hostname, the default behavior is: `jdbc:mysql:hostname...`



## Configuring Amazon Aurora MySQL for PDTs

In order to use [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) with Aurora, you must use MySQL replication, not Amazon Aurora's default replication, which is read-only. You must set the `read_only` parameter to `0` to make the MySQL replica writable, as described in our documentation on [RDS and temporary tables](https://docs.cloud.google.com/looker/docs/db-config-mysql-on-amazon-rds#rds_&_temporary_tables).

If you _don't_ want to grant write access to the database, you can copy and paste the derived table SQL into the `sql_table_name` parameter of a `view` file as shown here. This creates a subquery that is used at query time:
    
    
    view: my_name {
    sql_table_name: (sql_of_derived_table_goes_here) ;;
    }
    

For more details on Aurora replication, see [the AWS documentation](http://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Aurora.Replication.html).

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Amazon Aurora MySQL, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your dialect for information on these parameters.

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

Amazon Aurora MySQL supports the following features as of Looker 26.20:

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
