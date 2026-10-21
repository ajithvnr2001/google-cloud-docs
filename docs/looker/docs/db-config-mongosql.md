---
url: https://docs.cloud.google.com/looker/docs/db-config-mongosql/
title: MongoSQL \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:48:00.741087+00:00
---

# MongoSQL  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-mongosql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  MongoSQL Stay organized with collections  Save and categorize content based on your preferences. 

Connect Looker to your MongoSQL cluster directly by using the **MongoSQL** dialect (powered by the [MongoSQL Interface](https://www.mongodb.com/docs/sql-interface/)). Connecting Looker to MongoSQL lets you analyze document data by using relational SQL queries and build interactive Looker dashboards.

**Note:** The **MongoSQL** dialect succeeds and replaces the legacy [**MongoDB Connector for BI**](https://docs.cloud.google.com/looker/docs/db-config-mongodb). If you're using the legacy MongoDB Connector for BI, update your connection to use the **MongoSQL** dialect. See the MongoDB documentation [Transition from Atlas BI Connector to MongoSQL](https://www.mongodb.com/docs/sql-interface/transition-bic-to-atlas-sql/) for information on migrating from the Atlas BI Connector to the newer SQL Interface.

Looker includes an officially bundled, Apache-2.0 licensed JDBC driver for the MongoSQL Interface out of the box. Unlike the legacy MongoBI dialect, no manual installation of custom unpackaged JDBC driver JAR files is required.

## Prerequisites and MongoSQL configuration

Before creating a connection in Looker, complete the following configuration steps in MongoSQL:

  * Build a relational schema by using SQL Schema Builder
  * Add Looker IP addresses to the Atlas IP access list
  * Create a MongoDB user account for Looker
  * Obtain Atlas SQL connection parameters



### Build a relational schema by using SQL Schema Builder

**Important:** **This is a required step.**

MongoDB stores data in a flexible, non-relational document format (JSON/BSON). Before Looker can query your MongoDB collections by using standard SQL, you must use the SQL Schema Builder in MongoSQL to construct a SQL schema.

The MongoSQL Interface relies on the relational schema that's created by the SQL Schema Builder to map document structures, nested fields, and arrays to standard SQL tables, rows, and columns. Without an active SQL schema, the SQL Interface won't be able to translate SQL queries against your MongoDB collections.

Refer to the [MongoSQL Schema Builder documentation](https://www.mongodb.com/docs/sql-interface) to define and publish your tabular schemas before creating the connection in Looker.

For MongoDB Enterprise on-premise instances, use the [MongoDB SQL Schema Builder CLI](https://www.mongodb.com/docs/sql-interface/schema/schema-builder-cli) to define your schemas.

### Add Looker IP addresses to the Atlas IP access list

MongoSQL restricts client connections to authorized IP addresses. To query MongoSQL from your Looker instance, you must add your Looker IP addresses to the Atlas IP access list by performing the following steps:

  1. Obtain the list of [Looker IP addresses](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) for your Looker instance's region.
  2. Add these IP addresses to your Atlas project's IP access list according to the [Atlas IP access list documentation](https://docs.atlas.mongodb.com/security/ip-access-list/).



### Create a MongoDB user account for Looker

Use the MongoDB Atlas Web Console to create a database user account for Looker by performing the following steps:

  1. Log in to the [MongoDB Atlas Console](https://cloud.mongodb.com/).
  2. In the main navigation menu under **Security** , select **Database Access**.
  3. Click **Add New Database User**.
  4. Select **Password** as the Authentication Method. Enter a **Username** (for example, `looker`) and a secure password.
  5. Under **Database User Privileges** , select **Built-in Role** and assign the `read` role (or custom read permissions) for the database that Looker will access.
  6. Click **Add User** to save the user credentials.



### Obtain Atlas SQL connection parameters

To create the Looker connection, you will need to enter connection parameters for the Atlas SQL connection. You can get the parameter information by performing the following steps:

  1. Log in to the [MongoDB Atlas Console](https://cloud.mongodb.com/).
  2. Navigate to your cluster and click **Connect**.
  3. Select **Atlas SQL** (or **Connect your application using SQL**).
  4. Select **JDBC Driver**.
  5. Note the generated **Host** , **Port** (typically `27017`), **Database** , and SSL requirements. You will enter these details when you create the Looker connection.



## Create the Looker connection to your database

Follow these steps to establish the connection from Looker to MongoSQL:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information. Some of the settings are described next. Use the default values in all the other fields, or leave them blank.

     * **Name** : Enter a unique connection name.
     * **Dialect** : Select **MongoSQL** from the drop-down menu.
     * **Host** : Hostname provided by MongoSQL Interface (for example, `<cluster-name>.a.query.mongodb.net`).
     * **Port** : Port number for Atlas SQL (default: `27017`).
     * **Database** : Name of the database for which you created a schema by using SQL Schema Builder.
     * **Username** : Database username created for Looker.
     * **Password** : Database user password.
     * **SSL** : Enable **SSL** (`ssl=true`).
     * **Additional JDBC parameters** : (Optional) Additional JDBC parameters that are supported by the MongoDB driver, such as `authSource=admin` or `connectTimeoutMS=10000`. See Supported JDBC parameters.
  3. To verify database connectivity, click **Test Connection**. 

  4. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Supported JDBC parameters

For the **MongoSQL** dialect, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field:

  * `appName`
  * `authSource`
  * `clientinfo`
  * `connectTimeoutMS`
  * `directConnection`
  * `disableclientcache`
  * `extjsonmode`
  * `heartbeatFrequencyMS`
  * `journal`
  * `localThresholdMS`
  * `maxIdleTimeMS`
  * `maxWaitTimeMS`
  * `readPreference`
  * `replicaSet`
  * `retryReads`
  * `retryWrites`
  * `serverSelectionTimeoutMS`
  * `socketTimeoutMS`
  * `ssl`
  * `tls`
  * `tlsAllowInvalidHostnames`
  * `tlsInsecure`
  * `w`
  * `wtimeoutMS`



## Querying limitations and SQL behavior

When building LookML models and querying MongoSQL by using the SQL Interface, keep the following dialect characteristics in mind:

  * **SQL Schema Builder requirement** : As noted in the prerequisites, SQL queries require a pre-configured relational schema defined in Atlas SQL Schema Builder.
  * **Derived tables** : Ephemeral (regular) derived tables are supported, but persistent derived tables (PDTs) are not supported.
  * **Date and timestamp types** : The `date` data type is not supported; standard practice is to store and model dates as `timestamp` fields.
  * **Timezones** : All timestamps that are accessed from MongoSQL Interface are treated in UTC. Looker does not convert timezones in-database for MongoDB connections.



## Feature support

For Looker to support some features, your database dialect must also support them.

MongoSQL supports the following features as of Looker 26.18:

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

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
