---
url: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-mssql-timeout/
title: Set the connection timeout when using Node.js \u00a0|\u00a0 Cloud SQL for SQL Server \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:11:46.232071+00:00
---

# Set the connection timeout when using Node.js  |  Cloud SQL for SQL Server  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/sqlserver/samples/cloud-sql-sqlserver-mssql-timeout/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ SQL Server ](https://docs.cloud.google.com/sql/docs/sqlserver)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/sqlserver/samples)



#  Set the connection timeout when using Node.js Stay organized with collections  Save and categorize content based on your preferences. 

Demonstrates configuring the connection timeout when connecting to Cloud SQL for SQL Server using the Node.js mssql module.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage database connections](https://docs.cloud.google.com/sql/docs/sqlserver/manage-connections)



## Code sample

### Node.js

To authenticate to Cloud SQL for SQL Server, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // 'connectionTimeout` is the maximum number of milliseconds to wait trying to establish an
    // initial connection. After the specified amount of time, an exception will be thrown.
    config.connectionTimeout = 30000;
    // 'acquireTimeoutMillis' is the number of milliseconds before a timeout occurs when acquiring a
    // connection from the pool.
    config.pool.acquireTimeoutMillis = 30000;
    // 'idleTimeoutMillis' is the number of milliseconds a connection must sit idle in the pool
    // and not be checked out before it is automatically closed
    (config.pool.idleTimeoutMillis = 600000),

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlforsqlserver). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
