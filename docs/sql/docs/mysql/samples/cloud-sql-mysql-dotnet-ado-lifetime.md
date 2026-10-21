---
url: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-dotnet-ado-lifetime/
title: Set the connection duration when using ADO.NET \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:30:06.551540+00:00
---

# Set the connection duration when using ADO.NET  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/samples/cloud-sql-mysql-dotnet-ado-lifetime/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Samples ](https://docs.cloud.google.com/sql/docs/mysql/samples)



#  Set the connection duration when using ADO.NET Stay organized with collections  Save and categorize content based on your preferences. 

Configure the maximum number of seconds a connection can persist when connecting to Cloud SQL for MySQL by using the ADO.NET Connection object.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Manage database connections](https://docs.cloud.google.com/sql/docs/mysql/manage-connections)



## Code sample

### C#

To authenticate to Cloud SQL for MySQL, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    // ConnectionLifeTime sets the lifetime of a pooled connection
    // (in seconds) that a connection lives before it is destroyed
    // and recreated. Connections that are returned to the pool are
    // destroyed if it's been more than the number of seconds
    // specified by ConnectionLifeTime since the connection was
    // created. The default value is zero (0) which means the
    // connection always returns to pool.
    connectionString.ConnectionLifeTime = 1800; // 30 minutes
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=cloudsqlformysql). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
