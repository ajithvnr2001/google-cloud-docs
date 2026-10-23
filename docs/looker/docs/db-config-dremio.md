---
url: https://docs.cloud.google.com/looker/docs/db-config-dremio/
title: Dremio \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:58.674554+00:00
---

# Dremio  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-dremio/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Dremio Stay organized with collections  Save and categorize content based on your preferences. 

Connect your Looker instance to a Dremio database to analyze your data. This document describes how to set connection parameters in Looker and configure options to encrypt network traffic. Looker tests dialect compatibility against [Dremio](https://www.dremio.com/) version 1.4.9 Enterprise Edition, Dremio 11+, and Dremio 26+ (Enterprise & Cloud).

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next. Use the default values in all the other fields, or leave them blank.

     * **Name** : Assign a unique name to the connection. The name is how LookML refers to this connection.
     * **Dialect** : Select **Dremio 26.0+ (Arrow Flight SQL)** , **Dremio 11+** , or **Dremio**.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
     * **Host** : Enter the IP address or hostname of the server where Dremio is running. For Dremio Cloud, enter the Flight endpoint (for example, `data.dremio.cloud` or `data.eu.dremio.cloud`).

     * **Port** :

       * For **Dremio 26.0+ (Arrow Flight SQL)** : The default port is `32010` (or `443` for Dremio Cloud).
       * For **Dremio 11+** and **Dremio** : The default port is `31010`.
     * **Database** : The default value is `DREMIO` (or your target catalog name).

     * **Schema** : (Optional, **Dremio 26.0+ (Arrow Flight SQL)** only) Enter the default space or schema to use for queries (for example, `my_space` or `my_catalog.my_schema`).

     * **Username** : Enter the username that Looker uses to access Dremio.

     * **Password** : Enter the password (or personal access token) that's associated with the username.

     * **Enable SSL** : Toggle on to enable encrypted communication over Arrow Flight / TLS.

     * **Verify SSL Certificate** : If you're using self-signed or internal certificates without standard Certificate Authority (CA) verification, toggle this off to disable certificate verification.

     * **Additional JDBC parameters** : Add any additional JDBC parameters. See the Supported JDBC parameters section on this page for the list of parameters that Looker supports.

  3. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  4. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Debugging

Connect your web browser to `dremio_host:9047` on the server. From the SQL Editor, run `SELECT 1 FROM (VALUES(1))` to verify that Dremio is installed correctly and that queries are able to execute.

## Supported JDBC parameters

For Dremio, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

### Dremio 26.0+ (Arrow Flight SQL) parameters

  * `useEncryption`
  * `disableCertificateVerification`
  * `schema`
  * `catalog`
  * `token`
  * `useKerberos`
  * `threadPoolSize`



### Dremio & Dremio 11+ parameters

  * `disableCertificateVerification`
  * `impersonation_target`
  * `password`
  * `projectId`
  * `routing_queue`
  * `routing_tag`
  * `socksProxyHost`: For public Looker instances, the value for the `socksProxyHost` parameter must be the public IP address of the instance.
  * `socksProxyPassword`
  * `socksProxyPort`
  * `socksProxyUsername`
  * `ssl`
  * `token_type`
  * `user`



## Feature support

For Looker to support some features, your database dialect must also support them.

### Dremio 26.0+ (Arrow Flight SQL) feature support

Dremio 26+ with Arrow Flight SQL supports the following features as of Looker 26.20:

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
  
### Dremio 11+ feature support

Dremio 11+ supports the following features as of Looker 26.20:

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
  
### Dremio feature support

Dremio supports the following features as of Looker 26.20:

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
  
## Native Arrow Flight SQL compared to the legacy custom driver

Looker includes native out-of-the-box support for **Dremio 26.0+ (Arrow Flight SQL)** using the bundled Apache Arrow Flight SQL JDBC driver. Installing unpackaged custom JDBC driver JAR files is no longer required for Dremio 26+ instances.

For older Dremio deployments on customer-hosted instances that use legacy Dremio versions without native Arrow Flight support, refer to the [Unpackaged JDBC drivers](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers) documentation page.

## Next steps

After you have completed the database connection, [configure authentication options](https://docs.cloud.google.com/looker/docs/getting-started-with-users).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
