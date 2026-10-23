---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-mysql-connect-tcp/
title: Create a TCP connection when using Node.js \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:08.743794+00:00
---

# Create a TCP connection when using Node.js  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-mysql-connect-tcp/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  Create a TCP connection when using Node.js Stay organized with collections  Save and categorize content based on your preferences. 

Open a TCP connection to Cloud SQL for MySQL by using the Node.js npm mysql module.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Connect from App Engine flexible environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-flexible)
  * [Connect from App Engine standard environment](https://docs.cloud.google.com/sql/docs/mysql/connect-app-engine-standard)
  * [Connect from Cloud Build](https://docs.cloud.google.com/sql/docs/mysql/connect-build)
  * [Connect from Cloud Run](https://docs.cloud.google.com/sql/docs/mysql/connect-run)
  * [Connect from Cloud Run functions](https://docs.cloud.google.com/sql/docs/mysql/connect-functions)
  * [Connect using the Cloud SQL Auth Proxy](https://docs.cloud.google.com/sql/docs/mysql/connect-auth-proxy)
  * [Manage database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections)



## Code sample

### Node.js

To authenticate to Cloud SQL for MySQL, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    const mysql = require('promise-mysql');
    const fs = require('fs');
    
    // createTcpPool initializes a TCP connection pool for a Cloud SQL
    // instance of MySQL.
    const createTcpPool = async config => {
      // Note: Saving credentials in environment variables is convenient, but not
      // secure - consider a more secure solution such as
      // Cloud Secret Manager (https://cloud.google.com/secret-manager) to help
      // keep secrets safe.
      const dbConfig = {
        host: process.env.INSTANCE_HOST, // e.g. '127.0.0.1'
        port: process.env.DB_PORT, // e.g. '3306'
        user: process.env.DB_USER, // e.g. 'my-db-user'
        password: process.env.DB_PASS, // e.g. 'my-db-password'
        database: process.env.DB_NAME, // e.g. 'my-database'
        // ... Specify additional properties here.
        ...config,
      };
      // Establish a connection to the database.
      return mysql.createPool(dbConfig);
    };

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
