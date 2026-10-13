---
url: https://docs.cloud.google.com/looker/docs/db-config-teradata/
title: Teradata \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:12:42.943916+00:00
---

# Teradata  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-teradata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Teradata Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** See the [Teradata end-user license agreement](https://docs.cloud.google.com/looker/docs/db-teradata-eula).

The procedures that are required to connect Looker to a Teradata database depend on your Looker deployment:

  * For Looker-hosted, Looker (original) instances, contact [Looker Support](https://docs.cloud.google.com/looker/docs/best-practices/looker-support-details) if you want to enable the Teradata driver.

  * For [customer-hosted](https://docs.cloud.google.com/looker/docs/glossary#customer-hosted) Looker (original) instances, perform the following procedures:

    1. Install the `hash_md5` user-defined function (UDF) on your Teradata server.
    2. Install the Teradata JDBC driver.
    3. Create the Looker connection to your database.
  * For [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instances, perform the following procedures:

    1. Install the `hash_md5` user-defined function (UDF) on your Teradata server.
    2. Create the Looker connection to your database.



## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Installing the `hash_md5` user-defined function (UDF)

Before configuring Looker to work with Teradata, you must install the `hash_md5` user-defined function (UDF) on your Teradata server. You can find instructions for installing the UDF on this [Teradata downloads](https://downloads.teradata.com/download/extensibility/md5-message-digest-udf) page.

## Installing the Teradata JDBC driver

If you have a Looker (original) instance, you will need to configure a Teradata driver before creating the Looker connection. These instructions describe that process, assuming use of a startup script that is similar to the examples that are provided on the [looker-open-source GitHub page](https://github.com/looker-open-source/customer-scripts/tree/master/startup_scripts).

**Note:** If you have a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance, you can create a connection to a Teradata database without configuring a Teradata driver. After you install the `hash_md5` user-defined function (UDF) on your Teradata server, you can go right to the Creating the Looker connection to your database procedure on this page.

To install the driver, you will need to acquire two Teradata files, include them as part of the startup process, and add an option to tell Looker to access the driver.

Follow the steps on the [Unpackaged JDBC drivers](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers) documentation page using the following values:

**driver symbol** : `teradata`

**driver entry** :
    
    
    - name: teradata
      dir_name: teradata
      module_path: com.teradata.jdbc.TeraDriver
    

For the [step to put the driver in your dialect's directory](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers#driver_directory), the paths to these files will look like this:

  * `looker/custom_jdbc_drivers/teradata/tdgssconfig.jar`
  * `looker/custom_jdbc_drivers/teradata/terajdbc4.jar`



## Creating the Looker connection to your database

To create the connection from Looker to your database, follow these steps:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Teradata** from the **Dialect** drop-down menu.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.
  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.
  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 



Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Teradata, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `ACCOUNT`
  * `CHARSET`
  * `COLUMN_NAME`
  * `COP`
  * `DATABASE`
  * `DBS_PORT`
  * `ENCRYPTDATA`
  * `LOG`
  * `LOGDATA`
  * `LOGMECH`: The supported values for the `LOGMECH` parameter are `NTLM`, `KRB5`, `LDAP`, `CODE`, and `BEARER`.
  * `REDRIVE`
  * `SESSIONS`
  * `TMODE`
  * `USEXVIEWS`



## Feature support

For Looker to support some features, your database dialect must also support them.

Teradata supports the following features as of Looker 26.18:

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

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
