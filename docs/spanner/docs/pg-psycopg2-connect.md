---
url: https://docs.cloud.google.com/spanner/docs/pg-psycopg2-connect/
title: Connect psycopg2 to a PostgreSQL-dialect database \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:34:23.403122+00:00
---

# Connect psycopg2 to a PostgreSQL-dialect database  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/pg-psycopg2-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Connect psycopg2 to a PostgreSQL-dialect database Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect the PostgreSQL psycopg2 driver to a PostgreSQL-dialect database in Spanner. `psycopg2` is a Python driver for PostgreSQL.

Verify that PGAdapter is running on the same machine as the application that is connecting using the PostgreSQL psycopg2 driver.

For more information, see [Start PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter-start).
    
    
    connection = psycopg2.connect(database="DATABASE_NAME",
                                  host="APPLICATION_HOST",
                                  port=PORT)
    
    cursor = connection.cursor()
    cursor.execute('select \'Hello World\'')
    for row in cursor:
      print(row)
    
    cursor.close()
    connection.close()
    

Replace the following:

  * APPLICATION_HOST: the hostname or IP address of the machine where PGAdapter is running. If running locally, you can use `localhost`.
  * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



### Unix domain sockets

This section explains how to use Unix domain sockets to connect to a PostgreSQL-dialect database database. Use Unix domain socket connections when you need to have the lowest possible latency.

To use Unix domain sockets, PGAdapter must be running on the same host as the client application.
    
    
    connection = psycopg2.connect(database="DATABASE_NAME",
                                  host="/tmp",
                                  port=PORT)
    
    cursor = connection.cursor()
    cursor.execute('select \'Hello World\'')
    for row in cursor:
      print(row)
    
    cursor.close()
    connection.close()
    

Replace the following:

  * /tmp: the default domain socket directory for PGAdapter. This can be changed using the `-dir` command line argument.
  * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



## What's next

  * Learn more about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * For more information about PostgreSQL psycopg2 driver connection options, see [psycopg2 Connection Options](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/docs/psycopg2.md) in the PGAdapter GitHub repository.
  * See an [overview of drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview) supported for Spanner.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
