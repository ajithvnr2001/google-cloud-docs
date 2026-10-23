---
url: https://docs.cloud.google.com/looker/docs/db-config-google-cloud-sql/
title: Google Cloud SQL for MySQL \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:53.834219+00:00
---

# Google Cloud SQL for MySQL  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-google-cloud-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Google Cloud SQL for MySQL Stay organized with collections  Save and categorize content based on your preferences. 

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Connect using Application Default Credentials (ADC)

For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances, [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) is supported as a method of authentication for Google Cloud SQL for MySQL. 

When you set up ADC for Google Cloud SQL for MySQL, you must do the following procedures:

  * [Add the impersonated service account to your Cloud SQL database](https://docs.cloud.google.com/looker/docs/looker-core-dialects#add-the-impersonated-service-account)
  * [Set up service account impersonation on your Cloud SQL database](https://docs.cloud.google.com/looker/docs/looker-core-dialects#set-up-service-account-impersonation)
  * [Run additional configuration commands for Cloud SQL for MySQL](https://docs.cloud.google.com/looker/docs/looker-core-dialects#additional-commands-mysql)



See the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#using-application-default-credentials-to-connect-to-a-database) for the full procedure.

## Users and security

To perform actions on your database, Looker needs to have a user account on your database.

**Note:** Skip this procedure if you are on a Looker (Google Cloud core) instance and you want to use Application Default Credentials to authenticate into your database. You will instead use an existing Identity and Access Management (IAM) principal account. See the [Connecting Looker (Google Cloud core) to your database](https://docs.cloud.google.com/looker/docs/looker-core-dialects#using-application-default-credentials-to-connect-to-a-database) documentation page for the procedure.

To configure a database user for Looker to use, perform the following steps on your database:

  1. Create a database user.
         
         CREATE USER USERNAME;
         SET PASSWORD FOR USERNAME = PASSWORD ('PASSWORD');
         

  2. Grant `SELECT` privileges to the database user on the database that you want Looker to query. Replace `database_name` with the name of your database.
         
         GRANT SELECT ON DATABASE_NAME.* TO USERNAME;
         




Once you create the database user, you can enter the database user account credentials in the **Username** and **Password** fields of the Looker UI when you create the Looker connection to your database.

## Creating the Looker connection to your database

To create the connection from Looker to your database, follow these steps:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. From the **Dialect** drop-down menu, select **Google Cloud SQL**.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

     * **Host** : The database hostname that is used to connect to the Google Cloud SQL for MySQL database. For an SSH tunnel, use `localhost`.
     * **Port** : The port used that is to connect to the Google Cloud SQL for MySQL database.
     * **Database** : The name of the Google Cloud SQL for MySQL database instance.
     * **Username** : The username of the account that Looker will use to sign in to Google Cloud SQL for MySQL.

**Note:** [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances also support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials) as a method of authentication for Google Cloud SQL for MySQL. See the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#using-application-default-credentials-to-connect-to-a-database) for more information.
     * **Password** : The password of the account that Looker will use to sign in to Google Cloud SQL for MySQL.

     * **Additional JDBC parameters** : Additional JDBC parameters (optional).

     * **SSL** : If checked, enables an SSL connection; however, SSL connections to Google Cloud SQL for MySQL are not supported by default.

**Note:** Google Cloud SQL for MySQL requires additional steps for configuring SSL connections; see [Configuring SSL/TLS certificates](https://docs.cloud.google.com/sql/docs/mysql/configure-ssl-instance). Google Cloud SQL for MySQL creates a server certificate on the creation of each instance, so the custom certificate must be installed on the Looker server for successful SSL connections. This option is available only for [customer-hosted Looker deployments](https://docs.cloud.google.com/looker/docs/customer-hosted-installation-steps) that have access to the Looker server. 

Because of this requirement, a better alternative to SSL is to connect Looker to Google Cloud SQL for MySQL through a [Cloud SQL for MySQL Proxy](https://docs.cloud.google.com/sql/docs/mysql/sql-proxy).
     * **Verify SSL** : If checked, SSL verification is enforced. However, SSL connections to Google Cloud are not supported by default.

  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## PDT support

Google Cloud SQL for MySQL does not support `CREATE TABLE AS SELECT` statements, so you must use the [`create_process`](https://docs.cloud.google.com/looker/docs/reference/param-view-create-process) LookML parameter to define PDTs.

## Supported JDBC parameters

For Cloud SQL for MySQL, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

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

Google Cloud SQL supports the following features as of Looker 26.20:

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

After you have created your database connection, [set authentication options](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
