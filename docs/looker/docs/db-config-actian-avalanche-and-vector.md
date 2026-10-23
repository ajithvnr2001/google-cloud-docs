---
url: https://docs.cloud.google.com/looker/docs/db-config-actian-avalanche-and-vector/
title: Actian Avalanche and Vector \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:58.012984+00:00
---

# Actian Avalanche and Vector  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-actian-avalanche-and-vector/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Actian Avalanche and Vector Stay organized with collections  Save and categorize content based on your preferences. 

To use Looker with Actian Avalanche or Vector, you will need to configure an Ingres driver. These instructions describe that process, assuming use of a startup script that is similar to the examples that are provided on the [looker-open-source GitHub page](https://github.com/looker-open-source/customer-scripts/tree/master/startup_scripts).

You will need to acquire an Ingres driver JAR, include it as part of the startup process, and add an option to tell Looker to access it.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Installing the Ingres JDBC driver

Follow the steps on the [Unpackaged JDBC drivers](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers) documentation page using the following values:

**driver symbol** : `ingres`

**driver entry** :
    
    
    - name: ingres
      dir_name: ingres
      module_path: com.ingres.jdbc.IngresDriver
    

For the [step to put the driver in your dialect's directory](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers#driver_directory), the path to this file will look like this: `looker/custom_jdbc_drivers/ingres/iijdbc.jar`.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **Actian Avalanche** or **Vector** from the **Dialect** drop-down menu.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Enabling PDT support

It is possible to use [persistent derived tables (PDTs)](https://docs.cloud.google.com/looker/docs/derived-tables#persistent_derived_table) on your database using the [**PDT Overrides**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#configuring_separate_login_credentials_for_pdt_processes) section in the [**Connection Settings** page](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections#adding_connections).

To enable PDTs:

  1. Create a PDT user in your database for use with the scratch schema, for example `looker_scratch`.

  2. Create a group in your database such as `looker_pdt_group`.

  3. Add both the regular Looker user and the Looker PDT user to the new group.

  4. GRANT SELECT on all tables in the regular Looker user's schema to the PDT user.

  5. In the Looker **Connection Settings** page, in the **PDT Overrides** section, enter the PDT user information.

  6. The PDT user then runs a GRANT SELECT to the `looker_pdt_group` for every table it creates.




## Supported JDBC parameters

The following sections provide a list of JDBC parameters that are allowed for each dialect:

  * Actian Avalanche
  * Vector



### Actian Avalanche JDBC parameters

For Actian Avalanche, Looker supports the following JDBC parameter in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `autocommit_mode`
  * `encryption`
  * `password`
  * `send_ingres_dates`
  * `serverName`: For public Looker instances, the value for the `serverName` parameter must be the public IP address of the instance.
  * `user`



### Vector JDBC parameters

For Vector, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `autocommit_mode`
  * `encryption`
  * `password`
  * `send_ingres_dates`
  * `serverName`: For public Looker instances, the value for the `serverName` parameter must be the public IP address of the instance.
  * `user`



## Feature support

For Looker to support some features, your database dialect must also support them.

### Actian Avalanche

Actian Avalanche supports the following features as of Looker 26.20:

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
  
### Vector

Vector supports the following features as of Looker 26.20:

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
