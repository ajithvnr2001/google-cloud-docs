---
url: https://docs.cloud.google.com/looker/docs/db-config-clickhouse/
title: ClickHouse \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:18:37.959790+00:00
---

# ClickHouse  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-clickhouse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  ClickHouse Stay organized with collections  Save and categorize content based on your preferences. 

Connect Looker to your ClickHouse database to analyze your data and build interactive dashboards. This connection helps make your ClickHouse data available for reporting and analysis within Looker, supporting direct data-driven decisions.

This page guides you through configuring your ClickHouse instance and Looker connection settings, including how to encrypt network traffic, define user permissions, and review supported features. Looker supports ClickHouse version 0.2 or later, and ClickHouse 26+ using modernized JDBC drivers and symmetric aggregation support.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

To enable SSL encryption on the server side, see the [ClickHouse Global Server Settings documentation](https://clickhouse.com/docs/en/operations/server-configuration-parameters/settings#server_settings-openssl).

## Users and security

First, configure your Looker user on the ClickHouse server. ClickHouse database users can be configured by using SQL (`CREATE USER`) or through the `users` section in the `users.xml` file. Follow the [ClickHouse access rights documentation](https://clickhouse.com/docs/en/operations/access-rights/) to configure user access. The following basic example uses `users.xml`:
    
    
    <!-- Users and ACL. -->
    <users>
        <looker>
            <password>CHANGEIT</password>
            <networks incl="networks" />
            <profile>default</profile>
            <quota>default</quota>
        </looker>
    
        <web>
            <password></password>
            <networks incl="networks" />
            <profile>web</profile>
            <quota>default</quota>
            <allow_databases>
               <database>test</database>
            </allow_databases>
            <allow_dictionaries>
               <dictionary>test</dictionary>
            </allow_dictionaries>
        </web>
    </users>
    

Also within this file, configure the appropriate database access:
    
    
    <allow_databases>
        <database>database_1</database>
        <database>database_2</database>
        <database>database_3</database>
    </allow_databases>
    

## Creating the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next:

  * **Dialect** : Select **ClickHouse 26+** or **ClickHouse**.
  * **Host** : Reachable hostname or IP address of the ClickHouse server.
  * **Port** : Port on which the ClickHouse service is reachable over HTTP(S). 
    * By default, HTTP connections use `8123`, and HTTPS connections use `8443`.
    * Ports `9000` and `9440` are by default used by the ClickHouse native TCP command line client, but HTTP(S) ports must be used by Looker to connect to ClickHouse.
    * Your ClickHouse administrator may have chosen alternate ports with the `http_port` or `https_port` settings in the ClickHouse configuration. Ask your ClickHouse admin for the settings that are appropriate to your configuration.
  * **Database** : Database name (must be one of the databases that's allowed in your ClickHouse permissions).
  * **Username** : Database username.
  * **Password** : Database password.
  * **SSL** : Check to connect to ClickHouse over SSL/TLS.
  * **Verify SSL** : (Optional) Check to enforce strict SSL certificate and hostname verification on the ClickHouse server. Select **Verify SSL** only if you're using an SSL certificate that is signed by a generally trusted Certificate Authority. If you're using a self-signed SSL certificate, leave this setting unchecked.
  * **Additional JDBC parameters** : (Optional) Additional JDBC string parameters. See the Supported JDBC parameters section on this page for the list of parameters that Looker supports.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connection Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For ClickHouse, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

### ClickHouse 26+ parameters

  * `async_insert`
  * `autoCommit`
  * `compress`
  * `compress_algorithm`
  * `compress_level`
  * `connect_timeout`
  * `connection_timeout`
  * `continueBatchOnError`
  * `createDatabaseIfNotExist`
  * `custom_settings`
  * `database`
  * `databaseTerm`
  * `externalDatabase`
  * `fetchSize`
  * `format`
  * `jdbcCompliant`
  * `keep_alive_timeout`
  * `max_buffer_size`
  * `max_execution_time`
  * `max_result_bytes`
  * `max_result_rows`
  * `max_threads`
  * `namedParameter`
  * `query_timeout`
  * `receive_timeout`
  * `result_overflow_mode`
  * `retry`
  * `session_check`
  * `session_id`
  * `session_timeout`
  * `session_timezone`
  * `socket_timeout`
  * `ssl`
  * `sslmode`
  * `transactionSupport`
  * `use_server_time_zone`
  * `use_time_zone`
  * `wait_for_async_insert`
  * `wrapperObject`



### ClickHouse (Legacy) parameters

  * `beta.row_binary_for_simple_insert`
  * `compress`
  * `connection_timeout`
  * `continueBatchOnError`
  * `createDatabaseIfNotExist`
  * `custom_http_headers`
  * `custom_http_params`
  * `default_query_settings`
  * `disable_frameworks_detection`
  * `jdbc_ignore_unsupported_values`
  * `jdbc_resultset_auto_close`
  * `jdbc_sql_parser`
  * `jdbc_use_max_result_rows`
  * `jdbcCompliance`
  * `max_execution_time`
  * `password`
  * `session_timezone`
  * `socket_timeout`
  * `typeMappings`
  * `use_server_time_zone`
  * `use_time_zone`
  * `user`
  * `wrapperObject`



## Feature support

For Looker to support some features, your database dialect must also support them.

### ClickHouse 26+ feature support

ClickHouse 26+ supports the following features as of Looker 26.18:

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
  
### ClickHouse feature support

ClickHouse supports the following features as of Looker 26.18:

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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
