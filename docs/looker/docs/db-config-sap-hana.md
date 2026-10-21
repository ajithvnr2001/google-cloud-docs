---
url: https://docs.cloud.google.com/looker/docs/db-config-sap-hana/
title: SAP HANA \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:15:13.786406+00:00
---

# SAP HANA  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-sap-hana/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  SAP HANA Stay organized with collections  Save and categorize content based on your preferences. 

This page contains information about connecting Looker to SAP HANA and SAP HANA 2+.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Creating the Looker user

Create a Looker database user with a secure password.
    
    
    CREATE USER LOOKER PASSWORD <SOME_PASSWORD>
    

### Granting permissions

Grant read permissions on the schema(s) that you would like to use in Looker.
    
    
    GRANT SELECT ON SCHEMA <YOUR_SCHEMA> TO LOOKER
    

### Setting up a PDT schema

If using PDTs, create a scratch schema for PDTs to be written into.
    
    
    CREATE SCHEMA LOOKER_SCRATCH OWNED BY LOOKER
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : The name of the connection. This is how you will refer to the connection in LookML projects.
  * **Dialect** : **SAP HANA** or **SAP HANA 2+**.
  * **Port** : The database port. The default port is 30015.
  * **Host** : Hostname.
  * **Database** : The name of your database.
  * **Username** : The database username.
  * **Password** : The user password.
  * **Schema** : The default schema to use when none is specified. Entering a schema is optional.
  * **Enable PDTs** : Use this toggle to enable [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables). This reveals additional PDT fields and the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt-overrides) section for the connection.
  * **Temp Database** : Schema to use for PDTs.
  * **Additional JDBC parameters** : Add any additional JDBC parameters. See the Supported JDBC parameters section on this page for the list of parameters that Looker supports. See the [SAP HANA JDBC connection properties](https://help.sap.com/viewer/0eec0d68141541d1b07893a39944924e/2.0.02/en-US/109397c2206a4ab2a5386d494f4cf75e.html) documentation for details.
  * **Maintenance Schedule** : A [`cron`](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression that indicates when Looker should check [datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) and PDTs. Read more about this setting in the [Maintenance Schedule](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) documentation.
  * **SSL** : Check to enable SSL.
  * **Verify SSL** : Check to enforce strict hostname verification.
  * **Max connections per node** : The default is 25. This value can be left at the default value initially. Read more about this setting in the [Max connections per node](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) section of the **Connecting Looker to your database** documentation page.
  * **Connection Pool Timeout** : The default is 120 seconds.
  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, clear this option. Read more about this setting in the [SQL Runner Precache](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#sql_runner_precache) documentation.
  * **Database Time Zone** : Specify the time zone used in the database. Leave this field blank if you do not want time zone conversion. See the [Using time zone settings](https://docs.cloud.google.com/looker/docs/using-time-zone-settings) documentation page for more information.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

Test the connection in SQL Runner. Navigate to [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics), select your connection and schema, and then [check if you can see your database tables](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#getting_table_information).

## Supported JDBC parameters

For SAP HANA, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `autocommit`
  * `communicationTimeout`
  * `compress`
  * `connectTimeout`
  * `currentSchema`
  * `databaseName`
  * `distribution`
  * `encrypt`
  * `hostNameInCertificate`
  * `instanceNumber`
  * `isolation`
  * `locale`
  * `packetSize`
  * `password`
  * `proxyPassword`
  * `proxyPort`
  * `reconnect`
  * `SESSIONVARIABLE:APPLICATIONUSER`
  * `user`
  * `validateCertificate`



## Feature support

For Looker to support some features, your database dialect must also support them. The following sections show the feature support for SAP HANA and SAP HANA 2+.

### SAP HANA

SAP HANA supports the following features as of Looker 26.18:

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
  
### SAP HANA 2+

SAP HANA 2+ supports the following features as of Looker 26.18:

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

After completing the database connection, [configure authentication options](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
