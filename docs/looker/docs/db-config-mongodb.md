---
url: https://docs.cloud.google.com/looker/docs/db-config-mongodb/
title: MongoDB Connector for BI \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:46.625564+00:00
---

# MongoDB Connector for BI  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-mongodb/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  MongoDB Connector for BI Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** Looker can now query MongoSQL directly by using [MongoSQL](https://docs.cloud.google.com/looker/docs/db-config-mongosql). The MongoDB Connector for BI is being deprecated (Looker will send out a deprecation notice with a year's notice before the deprecation date). See the MongoDB documentation [Transition from Atlas BI Connector to MongoSQL](https://www.mongodb.com/docs/sql-interface/transition-bic-to-atlas-sql/) and the Migrating to MongoSQL section on this page for information on migrating from the Atlas BI Connector to the newer SQL Interface.

## Migrating to MongoSQL from MongoBI

Looker now supports MongoSQL and recommends migrating to MongoSQL from the MongoDB Connector for BI.

Because of SQL syntax differences between MongoDB Connector for BI (MongoBI) and MongoSQL, existing LookML models that use custom SQL blocks, date formatting, or database functions might require syntax adjustments. Don't switch an existing production connection directly to MongoSQL without first validating your LookML code, as this can break dashboards, Looks, and schedules or alerts.

To safely migrate from MongoBI to MongoSQL, follow these steps:

  1. Review the SQL syntax differences between MongoBI and MongoSQL in the MongoDB documentation [Transition from Atlas BI Connector to MongoSQL](https://www.mongodb.com/docs/sql-interface/transition-bic-to-atlas-sql/).
  2. [Create a new connection](https://docs.cloud.google.com/looker/docs/db-config-mongosql#creating-the-connection-to-your-database) for MongoSQL in Looker as a secondary connection.
  3. In a new development branch in your LookML project, update the `connection` parameter in your model file to point to the new MongoSQL connection.
  4. In [SQL Runner](https://docs.cloud.google.com/looker/docs/sql-runner-basics), test and run sample queries from your Explores to verify query syntax and results.
  5. Validate your project and content: 
     * Use the [Content Validator](https://docs.cloud.google.com/looker/docs/content-validation) to scan all dashboards and Looks for broken fields or references.
     * Use the [SQL Validator](https://docs.cloud.google.com/looker/docs/ci-sql-validator) of [Looker CI](https://docs.cloud.google.com/looker/docs/continuous-integration) to validate the dimensions in your Explores against the database.
  6. After resolving any validation errors, deploy your changes to production.



## Using MongoDB Connector for BI (MongoBI)

**Note:** Looker requires at least MongoDB version 4.0+ and MongoDB Connector for BI version 2.6.0+ (where the [`type_conversion_mode`](https://docs.mongodb.com/bi-connector/master/reference/type-conversion/#type-conversion-modes) session variable was introduced).

Looker can access MongoDB using the MongoDB Connector for BI using two options:

  * Using the MongoDB Connector for BI in [MongoDB Atlas](https://docs.atlas.mongodb.com/bi-connection/).
  * Using a MongoDB Connector for BI installed on the same server as the MongoDB database.



## MongoDB Atlas

Your MongoDB Atlas must use an M10+ cluster. For Looker to use a MongoDB database running on MongoDB Atlas, you must use the [MongoDB Connector for BI (MongoBI)](https://docs.atlas.mongodb.com/bi-connection/). Enabling the BI Connector for Atlas requires that MongoDB Atlas use a M10+ cluster.

You must also create a user account that has read permissions for the chosen database.

### Configuring the MongoDB Connector for BI

Before creating a connection in Looker, your MongoDB or Atlas administrator needs to set up the MongoDB Connector for BI using the following steps, which are explained on this page:

  * Add the Looker server to the Atlas IP access list
  * Enable the MongoDB Connector for BI
  * Allow use of regular derived tables (recommended)



### Adding the Looker server to the Atlas IP access list

Atlas only allows client connections from entries in the project's IP access list. Add the Looker IP address to the Atlas project's IP access list:

  1. [Get the Looker IP address](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access).
  2. Follow the [Atlas IP access list setup](https://docs.atlas.mongodb.com/security/ip-access-list/) instructions to add the Looker IP address to the Atlas IP access list.



### Enabling the MongoDB Connector for BI

Enable the MongoDB Connector for BI:

  1. Verify that you are on a [M10+ cluster](https://docs.atlas.mongodb.com/scale-cluster/#a-open-the-editing-cluster-dialog).
  2. In Atlas, [open the Connect page for the cluster](https://docs.atlas.mongodb.com/bi-connection/). Make a note of the hostname, port, and user. You'll need to use that information when configuring the connection in Looker.



## MongoDB on the same server

Before creating a connection in Looker, your MongoDB administrator should set up MongoDB and the Mongo Connector for BI using the following steps, which are explained on this page:

  * Installing the Mongo Connector for BI
  * Encrypting network traffic
  * Setting up the Looker user and permissions
  * Allowing use of regular derived tables (recommended)



### Installing the Mongo Connector for BI

Install the MongoDB Connector for BI on the same server as the MongoDB database, as explained on the [Install BI Connector On Premises ](https://docs.mongodb.com/bi-connector/master/installation/) MongoDB documentation page.

### Encrypting network traffic

The MongoDB Connector for BI requires using SSL encryption between MongoDB's server and the Looker application. Follow the SSL setup instructions on the [Configure SSL for BI Connector](https://docs.mongodb.com/bi-connector/master/tutorial/ssl-setup/) MongoDB documentation page.

### Setting up the Looker user and permissions

In the [MongoDB shell](https://docs.mongodb.com/manual/mongo/), enter the `use` command to switch to the database that Looker will connect to. Then, create a user for Looker with [`db.createUser()`](https://docs.mongodb.com/manual/reference/method/db.createUser/) with the role `readWrite`:
    
    
    use looker_database
    
    db.createUser({ user: looker,
                    pwd: `some_password_here`,
                    roles: [ "readWrite" ]
                  })
    

## Installing the MongoBI JDBC driver files

For both MongoDB Connector for BI options, Looker requires configuring JDBC driver files by doing the following steps:

Download these two JAR files:

  * [mongosql auth 1.0.0](https://mvnrepository.com/artifact/org.mongodb/mongosql-auth/1.0.0-rc0)
  * [mysql connector java 5.1.47](https://mvnrepository.com/artifact/mysql/mysql-connector-java/5.1.47)



Follow the steps on the [Unpackaged JDBC drivers](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers) documentation page using the following values:

**driver symbol** : `mongobi`

**driver entry** :
    
    
    - name: mongobi
      dir_name: mongobi
      module_path: com.mysql.jdbc.Driver
      override_jdbc_url_subprotocol: mysql
    

**If you are on Looker 6.2 or earlier** :
    
    
    - name: maria15x
      dir_name: mongobi
      module_path: com.mysql.jdbc.Driver
      override_jdbc_url_subprotocol: mysql
    

For the [step to put the driver in your dialect's directory](https://docs.cloud.google.com/looker/docs/unpackaged-jdbc-drivers#driver_directory), the paths to these files will look like this:

  * `looker/custom_jdbc_drivers/mongobi/mongosql-auth-1.0.0-rc0.jar`
  * `looker/custom_jdbc_drivers/mongobi/mysql-connector-java-5.1.47.jar`



### Allowing use of regular derived tables (recommended)

[Derived tables](https://docs.cloud.google.com/looker/docs/derived-tables) are important tools in Looker that enable you to expand the sophistication of your analyses. They can also play a valuable role in enhancing query performance. At a high level, the Looker derived table capability provides a way to create new tables that don't already exist in your database.

The MongoDB Connector for BI supports temporary [regular derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#regular-or-ephemeral-derived-tables) but does not support [persistent derived tables](https://docs.cloud.google.com/looker/docs/derived-tables#persistent-derived-tables).

Since regular derived tables are temporary, they don't need to be stored. Thus, you don't need to create a schema for them. However, you need to grant the `dbOwner` role to `looker_tmp` schema, even if that schema does not exist.

Follow the Modify MongoDB Users section on this [MongoDB documentation page about configuring database users](https://docs.atlas.mongodb.com/security-add-mongodb-users/#modify-mongodb-users) to add the `dbOwner` role on `looker_tmp` for the user Looker will use to connect.
    
    
    db.grantRolesToUser("looker", [ {role: "dbOwner", db: "looker_tmp"} ])
    

## Creating the Looker connection to your database

Follow these steps to create the connection from Looker to your database:

  1. In the **Admin** section of Looker, select **Connections** , and then click **Add Connection**.
  2. Select **MongoBI** from the **Dialect** drop-down menu.

**Note:** If you are on a [Looker (Google Cloud core)](https://docs.cloud.google.com/looker/docs/looker-core-overview) instance and you don't see your dialect listed in the **Dialect** drop-down menu, see the [Looker (Google Cloud core) documentation](https://docs.cloud.google.com/looker/docs/looker-core-dialects#supported_dialects_for) to verify that the dialect is supported for Looker (Google Cloud core) instances.
  3. Fill out the connection details. The majority of the settings are common to most database dialects. See the [Connecting Looker to your database](https://docs.cloud.google.com/looker/docs/connecting-to-your-db) documentation page for information.

  4. To verify that the connection is successful, click the **Test Connection** button in the **Status details** section at the bottom of the **Connections Settings** page.

  5. If Looker displays **Can Connect** , press **Connect** to create the connection. 




Your database connection is then added to the list on the Looker [**Connections**](https://docs.cloud.google.com/looker/docs/admin-panel-database-connections) **Admin** page.

## Using SQL functions and operators with MongoDB Connector for BI

When developing using a MongoDB Connector for BI connection, you can use the [SQL functions and operators listed in the MongoDB documentation](https://docs.mongodb.com/bi-connector/master/supported-operations/).

## Supported JDBC parameters

For MongoDB Connector for BI, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `allowMultiQueries`
  * `appName`
  * `authSource`
  * `autoReconnect`
  * `cachePrepStmts`
  * `characterEncoding`
  * `connectTimeout`
  * `connectTimeoutMS`
  * `elideSetAutoCommits`
  * `enabledSslProtocolSuites`
  * `enabledTLSProtocols`
  * `explainSlowQueries`
  * `maxAllowedPacket`
  * `password`
  * `queryInterceptors`
  * `queryTimeoutKillsConnection`
  * `replicaSet`
  * `rewriteBatchedStatements`
  * `socketTimeout`
  * `ssl`
  * `sslMode`
  * `tcpKeepAlive`
  * `useCompression`
  * `useCursorFetch`
  * `useLocalSessionState`
  * `user`
  * `useServerPrepStmts`
  * `useSSL`
  * `verifyServerCertificate`
  * `zeroDateTimeBehavior`



## Feature support

For Looker to support some features, your database dialect must also support them.

MongoBI supports the following features as of Looker 26.20:

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
  
In addition:

  * MongoDB does not support [millisecond and microsecond timeframes for dimension groups](https://docs.cloud.google.com/looker/docs/reference/param-field-dimension-group#timeframe_options).
  * MongoDB does not support [millisecond, millisecondX, and microsecond types for dimensions](https://docs.cloud.google.com/looker/docs/reference/param-dimension-filter-parameter-types#time).
  * Looker treats all timestamps accessed from MongoBI as being in the coordinated universal time (UTC) time zone.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
