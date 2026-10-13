---
url: https://docs.cloud.google.com/spanner/docs/pg-psycopg3-connect/
title: Connect psycopg3 to a PostgreSQL-dialect database \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:57.844229+00:00
---

# Connect psycopg3 to a PostgreSQL-dialect database  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/pg-psycopg3-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Connect psycopg3 to a PostgreSQL-dialect database Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect the [PostgreSQL psycopg3 driver](https://www.psycopg.org/psycopg3/) to a PostgreSQL-dialect database in Spanner. `psycopg3` is a Python driver for PostgreSQL.

  1. Verify that PGAdapter is running on the same machine as the application that is connecting using the PostgreSQL psycopg3 driver.
         
         export GOOGLE_APPLICATION_CREDENTIALS=/CREDENTIALS_FILE_PATH/credentials.json
         docker pull gcr.io/cloud-spanner-pg-adapter/pgadapter
         docker run \
           -d -p 5432:5432 \
           -v ${GOOGLE_APPLICATION_CREDENTIALS}:${GOOGLE_APPLICATION_CREDENTIALS}:ro \
           -e GOOGLE_APPLICATION_CREDENTIALS \
           gcr.io/cloud-spanner-pg-adapter/pgadapter \
           -p PROJECT_NAME -i INSTANCE_NAME \
           -x
         

For more information, see [Start PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter-start).

  2. Connect to PGAdapter using TCP.
         
         import psycopg
         
         with psycopg.connect("host=APPLICATION_HOST port=PORT dbname=DATABASE_NAME sslmode=disable") as conn:
           conn.autocommit = True
           with conn.cursor() as cur:
             cur.execute("select 'Hello world!' as hello")
             print("Greeting from Cloud Spanner PostgreSQL:", cur.fetchone()[0])
         

Replace the following:

     * APPLICATION_HOST: the hostname or IP address of the machine where PGAdapter is running. If running locally, use `localhost`.
     * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



### Unix domain sockets

This section explains how to use Unix domain sockets to connect to a PostgreSQL-dialect database. Use Unix domain sockets for the lowest possible latency.

To use Unix domain sockets, PGAdapter must be running on the same host as the client application.

Verify the PostgreSQL JDBC driver is loaded.
    
    
    import psycopg
    
    with psycopg.connect("host=/tmp
                          port=PORT
                          dbname=DATABASE_NAME") as conn:
    conn.autocommit = True
    with conn.cursor() as cur:
      cur.execute("select 'Hello world!' as hello")
      print("Greetings from Cloud Spanner PostgreSQL:", cur.fetchone()[0])
    

Replace the following:

  * /tmp: the default domain socket directory for PGAdapter. This can be changed using the `-dir` command-line argument.
  * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



## What's next

  * Learn more about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * For more information about PostgreSQL psycopg3 driver connection options, see [psycopg3 Connection Options](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/docs/psycopg3.md) in the PGAdapter GitHub repository.
  * See an [overview of drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview) supported for Spanner.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
