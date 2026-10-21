---
url: https://docs.cloud.google.com/spanner/docs/pg-node-postgres-connect/
title: Connect node-postgres to a PostgreSQL-dialect database \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:50:11.571397+00:00
---

# Connect node-postgres to a PostgreSQL-dialect database  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/pg-node-postgres-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Connect node-postgres to a PostgreSQL-dialect database Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect the PostgreSQL node-postgres driver to a PostgreSQL-dialect database in Spanner. node-postgres is a Node.js driver for PostgreSQL.

  1. Verify that PGAdapter is running on the same machine as the application that is connecting using the PostgreSQL node-postgres driver.

For more information, see [Start PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter-start).

  2. Specify the database server host and port in the `node-postgres` connection properties:
         
         const { Client } = require('pg');
         const client = new Client({
           host: 'APPLICATION_HOST',
           port: PORT,
           database: 'DATABASE_NAME',
         });
         await client.connect();
         const res = await client.query("select 'Hello world!' as hello");
         console.log(res.rows[0].hello);
         await client.end();
         

Replace the following:

     * APPLICATION_HOST: the hostname or IP address of the machine where PGAdapter is running. If running locally, you can use `localhost`.
     * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



## Unix domain sockets

This section explains how to use Unix domain sockets to connect a PostgreSQL node-postgres driver to a PostgreSQL-dialect database. Use Unix domain socket connections when you need to have the lowest possible latency.

To use Unix domain sockets, PGAdapter must be running on the same host as the client application.
    
    
    const client = new Client({
      host: '/tmp',
      port: PORT,
      database: 'DATABASE_NAME',
    });
    await client.connect();
    const res = await client.query("select 'Hello world!' as hello");
    console.log(res.rows[0].hello);
    await client.end();
    

Replace the following:

  * /tmp: the default domain socket directory for PGAdapter. This can be changed using the `-dir` command line argument.
  * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



## What's next

  * Learn more about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * For more information about PostgreSQL node-postgres driver connection options, see [node-postgres Connection Options](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/docs/node-postgres.md) in the PGAdapter GitHub repository.
  * See an [overview of drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview) supported for Spanner.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
