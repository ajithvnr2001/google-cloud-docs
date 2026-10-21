---
url: https://docs.cloud.google.com/looker/docs/db-config-vertica/
title: Vertica \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:15:57.312045+00:00
---

# Vertica  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-vertica/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Vertica Stay organized with collections  Save and categorize content based on your preferences. 

Configure your Vertica database to work with Looker. With this setup, you can use your Vertica data for operational workflows, analysis, and building dashboards in Looker. This integration helps you provide timely data to your employees, customers, and services, leveraging features like persistent derived tables for effective business reporting.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Database configuration

Before you create a connection to Vertica, create a new database user and schema that is exclusive to your Looker applications. The Looker user needs read and write permissions into a separate schema to store PDTs and read-only privileges to other schemas in the Vertica database. This is optional but recommended.

The following is an example of creating a user and schema for Looker:
    
    
    CREATE USER looker Identified BY 'mypassword';
    CREATE SCHEMA looker_scratch;
    GRANT CREATE ON SCHEMA looker_scratch to looker;
    

## Create the Looker connection to your database

In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.

Fill out the connection details. The majority of the settings are common to most database dialects. See [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) for information. Some of the settings are described next:

  * **Name** : Give a name to the connection. This is how the LookML model will reference the connection.
  * **Dialect** : Select **Vertica** from the drop-down of dialects.
  * **Host** : Enter the Vertica server name or IP address.
  * **Port** : The default is 5433.
  * **Database** : Enter Vertica's database name.
  * **Username and Password** : Enter the username and password of the user that will connect to Looker.
  * **Schema** : Enter the schema that contains the tables that you want to explore in Looker.
  * **Temp Database** : This is the scratch schema where you want Looker to create any temporal derived tables to improve performance. It is optional but recommended, and should be created beforehand.
  * **Max connections per node** : This setting can be left at the default value initially. See [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#max_connections) for more information.
  * **Connection Pool Timeout** : This is optional. Use the default value.
  * **Database Time Zone** : The time zone your Vertica database uses to store dates and times. For example, UTC. This is optional.
  * **Query Time Zone** : The time zone you want your queries to display. For example, US Eastern (America - New York). This is optional.
  * **Additional JDBC parameters** : This is optional. Use this field to enable additional database settings. For example, to enable Vertica's built-in load balancing, use the JDBC connection parameter `ConnectionLoadBalance=1`. To assign a label to identify the Looker sessions, use the JDBC connection parameter `label=<mylabel>`. You can pass several parameters one after the other using `&`, as shown on this page. See the Supported JDBC parameters section on this page for the list of parameters that Looker supports. See [Vertica's documentation](https://www.vertica.com/docs/9.1.x/HTML/index.htm#Authoring/ConnectingToVertica/ClientJDBC/JDBCConnectionProperties.htm) for information on Vertica's JDBC parameters.



To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

If Looker displays **Can Connect** , press **Connect** to create the connection. 

Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For Vertica, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `AutoCommit`
  * `BackupServerNode`
  * `ConnectionLoadBalance`
  * `connsettings`
  * `DirectBatchInsert`
  * `label`
  * `LoginTimeout`
  * `LogLevel`
  * `Password`
  * `ReadOnly`
  * `ResultBufferSize`
  * `ssl`
  * `TransactionIsolation`
  * `User`



## Feature support

For Looker to support some features, your database dialect must also support them.

Vertica supports the following features as of Looker 26.18:

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
