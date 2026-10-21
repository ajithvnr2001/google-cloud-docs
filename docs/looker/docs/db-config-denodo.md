---
url: https://docs.cloud.google.com/looker/docs/db-config-denodo/
title: Denodo 7, Denodo 8, and Denodo 9 \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:25:10.084750+00:00
---

# Denodo 7, Denodo 8, and Denodo 9  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-denodo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Denodo 7, Denodo 8, and Denodo 9 Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Looker supports Denodo 7, Denodo 8, and Denodo 9. Looker does not support the earlier version of Denodo, which is referred to as just "Denodo."

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Configuring Denodo 7, Denodo 8, or Denodo 9 for Looker

Preparing Denodo 7, Denodo 8, or Denodo 9 for Looker requires a few steps:

### Import a custom function

To support [symmetric aggregates](https://docs.cloud.google.com/looker/docs/working-with-joins#symmetric_aggregates), a custom function (BASE64_TO_BASE10) has to be added to the Denodo VDP Server. For instructions, see Denodo's Knowledge Base article on [Connecting Looker to Denodo](https://community.denodo.com/kb/en/view/document/Connecting%20Looker%20to%20Denodo?category=Northbound+Connections).

### Grant the database user appropriate permissions

Looker will require `SELECT` access to any tables or databases that you would like to query with Looker. Ensure that the database user account that you are using to connect to Looker can access these tables.

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. Click the Looker **Main menu** icon menu and select **Admin** , if the **Admin** menu isn't already displayed. (You may have to click the back arrow if the **Explore** or **Develop** menu is displayed.)
  2. In the **Admin** menu, select **Connections** , and then click **Add Connection**.
  3. Select **Denodo 7** or **Denodo 8** from the **Dialect** drop-down menu.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  4. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

  5. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  6. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Denodo 7, Denodo 8, and Denodo 9, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `autoCommit`
  * `chunkSize`
  * `chunkTimeout`
  * `connectTimeout`
  * `i18n`
  * `password`
  * `pingQuery`
  * `pingQueryTimeout`
  * `queryTimeout`
  * `ssl`
  * `sslTrustServerCertificate`
  * `user`
  * `userAgent`



## Feature support

For Looker to support some features, your database dialect must also support them.

### Denodo 7

Denodo 7 supports the following features as of Looker 26.20:

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
  
### Denodo 8 and Denodo 9

Denodo 8 & 9 supports the following features as of Looker 26.20:

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
