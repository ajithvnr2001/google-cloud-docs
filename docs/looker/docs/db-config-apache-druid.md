---
url: https://docs.cloud.google.com/looker/docs/db-config-apache-druid/
title: Apache Druid \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:58.578866+00:00
---

# Apache Druid  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-apache-druid/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Apache Druid Stay organized with collections  Save and categorize content based on your preferences. 

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Configuring your Apache Druid cluster

`<DRUID_BASE_DIR>` refers to the base directory in which the Apache Druid cluster is installed on a server.

### Enabling SQL

To enable SQL on your Druid database, add this line to the [`broker/runtime.properties`](https://druid.apache.org/docs/latest/configuration/index.html#broker) configuration file:

`<DRUID_BASE_DIR>/conf/druid/broker/runtime.properties`
    
    
    druid.sql.enable=true
    

### Turning off `COUNT DISTINCT` approximation (optional)

By default, Druid approximates `COUNT DISTINCT`. For precise results, add this line to the [`broker/runtime.properties`](https://druid.apache.org/docs/latest/configuration/index.html#broker) configuration file:

`<DRUID_BASE_DIR>/conf/druid/broker/runtime.properties`
    
    
    `druid.sql.planner.useApproximateCountDistinct=false`
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Name** : The name of the connection.
  * **Dialect** : **Apache Druid** , **Apache Druid 0.13+** (Apache Druide 0.13.x - 0.17.x), or **Apache Druid 0.18+**.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  * **Host** : DNS or IP address of the cluster [Broker](https://druid.apache.org/docs/latest/design/broker.html). You can find this in your [`broker/runtime.properties`](https://druid.apache.org/docs/latest/configuration/index.html#broker) file.

  * **Port** : The port of the [Broker](https://druid.apache.org/docs/latest/design/broker.html). The default port is 8082. If your cluster is secured by SSL, the default port is 8182.

  * **Database** : The name of your database. The default is `druid`.

  * **Username** : The database username if your Apache Druid cluster is configured to use [Druid Basic Security](https://druid.apache.org/docs/latest/development/extensions-core/druid-basic-security.html). If it is not, then you can specify any string.

  * **Password** : The user password. If your cluster is not configured to use [Druid Basic Security](https://druid.apache.org/docs/latest/development/extensions-core/druid-basic-security.html), then you can specify any string.

  * **Schema** : The default schema to use when there is no schema specified. Entering a schema is optional. 

  * **Additional JDBC parameters** : Semicolon delimited [Avatica JDBC parameters](https://calcite.apache.org/avatica/docs/client_reference.html). See the Supported JDBC parameters section on this page for the list of parameters that Looker supports.

    * These properties can be set as connection properties: 
      * `useApproximateCountDistinct`
      * `useApproximateTopN`
      * `useFallback`
      * `sqlTimeZone`

Example: `none useApproximateCountDistinct=false;truststore=/path/to/truststore.jks;truststore_password=changeit`

  * **Maintenance Schedule** : A [`cron`](https://en.wikipedia.org/wiki/Cron#CRON_expression) expression that indicates when Looker should check [datagroups](https://docs.cloud.google.com/looker/docs/caching-and-datagroups#specifying_caching_policies_with_datagroup_parameters) and persistent derived tables. Read more about this setting in the [Maintenance Schedule](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#pdt_maintenance_schedule) documentation.

  * **SSL** : Check if your Apache Druid cluster is configured to use [Druid TLS](https://druid.apache.org/docs/latest/operations/tls-support.html).

  * **Verify SSL** : Check to enforce strict hostname verification.

  * **Max connections per node** : The default is 25. This setting can be left at the default value initially. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) documentation page for more information.

  * **Connection Pool Timeout** : The default is 120 seconds.

  * **SQL Runner Precache** : To cause SQL Runner not to preload table information and to load table information only when a table is selected, clear this option. Read more about this setting in the [SQL Runner Precache](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#sql_runner_precache) documentation.

  * **Database Time Zone** : Database timezone. Supported in Apache Druid 0.13+ and Apache Druid 0.18+.




To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

Looker runs a `SELECT 1` query to verify a basic connection and perform a query test. It does not validate that the catalog and schema combination exist or that the user has the required access to that schema.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

Test the connection in SQL Runner. Navigate to [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics), select your connection and schema, then [check if you can see your database tables](https://docs.cloud.google.com/looker/docs/sql-runner-manage-db#getting_table_information).

## Supported JDBC parameters

For Apache Druid, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `authentication`
  * `avatica_password`
  * `avatica_user`
  * `serialization`
  * `sqlTimeZone`
  * `timeZone`
  * `useApproximateCountDistinct`
  * `useApproximateTopN`
  * `useFallback`
  * `url`



## Feature support

For Looker to support some features, your database dialect must also support them.

### Apache Druid

Apache Druid supports the following features as of Looker 26.20:

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
  
### Apache Druid 0.13.x - 0.17.x

Apache Druid 0.13.x - 0.17.x supports the following features as of Looker 26.20:

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
  
### Apache Druid 0.18+

Apache Druid 0.18+ supports the following features as of Looker 26.20:

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

After you have completed the database connection, [configure authentication options](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
