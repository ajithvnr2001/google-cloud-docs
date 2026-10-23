---
url: https://docs.cloud.google.com/looker/docs/db-config-microsoft-azure-synapse-analytics/
title: Microsoft Azure Synapse Analytics \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:43.549838+00:00
---

# Microsoft Azure Synapse Analytics  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-microsoft-azure-synapse-analytics/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Microsoft Azure Synapse Analytics Stay organized with collections  Save and categorize content based on your preferences. 

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

To learn more about using SSL encryption, see the [Microsoft documentation](https://azure.microsoft.com/en-us/documentation/articles/cloud-services-configure-ssl-certificate/).

## Users and security

First, connect to the `master` database on your server with your server admin login:
    
    
    CREATE LOGIN looker
    WITH PASSWORD = '<strong_password>';
    

Connect to your Microsoft Azure Synapse Analytics database and create a database user:
    
    
    CREATE USER looker FOR LOGIN looker;
    

Looker must be authorized to detect and stop running queries, which requires the following permissions:
    
    
    ALTER ANY CONNECTION
    VIEW SERVER STATE
    

To grant these permissions, run the following:
    
    
    GRANT CONTROL ON DATABASE::userDatabase TO looker;
    

> Depending on the Microsoft Azure Synapse Analytics tier being used, you may also need to explicitly grant the `VIEW DATABASE STATE` permission.

To grant `VIEW DATABASE STATE` permission, run the following:
    
    
    GRANT VIEW DATABASE STATE TO looker;
    

## Temp schema setup

Create a schema owned by the Looker user:
    
    
    CREATE SCHEMA looker_scratch AUTHORIZATION looker;
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. The following fields have additional information that applies to Microsoft Azure Synapse Analytics:

  * **Dialect** : Select **Microsoft Azure Synapse Analytics**.
  * **Remote Host** and **Port** : Enter the hostname and port (the default port is 1433).

If you need to specify a non-default port other than 1433 and your database requires the use of a comma instead of a colon, you can add `useCommaHostPortSeparator=true` in the **Additional JDBC parameters** field further down in the connection settings, which will allow you to use a comma in the **Remote Host:Port** field. For example:

`jdbc:sqlserver://hostname,1434`




To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Microsoft Azure Synapse Analytics, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `accessToken`
  * `ApplicationIntent`
  * `applicationName`
  * `authentication`
  * `authenticationScheme`
  * `cancelQueryTimeout`
  * `columnEncryptionSetting`
  * `database`
  * `databaseName`
  * `disableStatementPooling`
  * `domain`
  * `enablePrepareOnFirstPreparedStatementCall`
  * `Encrypt`
  * `failoverPartner`
  * `fips`
  * `gsscredential`
  * `hostNameInCertificate`
  * `instanceName`
  * `Integrated Security`
  * `integratedSecurity`
  * `jaasConfigurationName`
  * `keyStoreAuthentication`
  * `lastUpdateCount`
  * `locktimeout`
  * `loginTimeout`
  * `msiClientId`
  * `multiSubnetFailover`
  * `packetSize`
  * `password`
  * `portNumber`
  * `queryTimeout`
  * `realm`
  * `responseBuffering`
  * `selectMethod`
  * `sendStringParametersAsUnicode`
  * `sendTimeAsDatetime`
  * `serverName`
  * `serverPreparedStatementDiscardThreshold`
  * `serverSpn`
  * `transparentNetworkIPResolution`
  * `trustServerCertificate`
  * `useBulkCopyForBatchInsert`
  * `useCommaHostPortSeparator`
  * `user`
  * `workstationID`
  * `xopenStates`



## Feature support

For Looker to support some features, your database dialect must also support them.

Microsoft Azure Synapse Analytics supports the following features as of Looker 26.20:

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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
