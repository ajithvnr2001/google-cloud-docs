---
url: https://docs.cloud.google.com/spanner/docs/pg-pgx-connect/
title: Connect pgx to a PostgreSQL-dialect database \u00a0|\u00a0 Spanner \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:29:57.128103+00:00
---

# Connect pgx to a PostgreSQL-dialect database  |  Spanner  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/pg-pgx-connect/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Reference ](https://docs.cloud.google.com/spanner/docs/apis)



Send feedback 

#  Connect pgx to a PostgreSQL-dialect database Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to connect the PostgreSQL pgx driver to a PostgreSQL-dialect database in Spanner. `pgx` is a Golang driver for PostgreSQL.

Verify that PGAdapter is running on the same machine as the application that is connecting using the PostgreSQL pgx driver.

For more information, see [Start PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter-start).

  * `pgx` requires a username and password in the connection string. PGAdapter ignores these.
  * By default, PGAdapter disables SSL. `pgx` by default first tries to connect with SSL enabled. Disabling SSL in the connection request speeds up the connection process, as it requires one fewer round trip.


    
    
    connString := "postgres://uid:pwd@APPLICATION_HOST:PORT/DATABASE_NAME?sslmode=disable"
    ctx := context.Background()
    conn, err := pgx.Connect(ctx, connString)
    if err != nil {
      return err
    }
    defer conn.Close(ctx)
    
    var greeting string
    err = conn.QueryRow(ctx, "select 'Hello world!' as hello").Scan(&greeting)
    if err != nil {
      return err
    }
    fmt.Printf("Greeting from Cloud Spanner PostgreSQL: %v\n", greeting)
    

Replace the following:

  * APPLICATION_HOST: the hostname or IP address of the machine where PGAdapter is running. If running locally, you can use `localhost`.
  * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



### Unix domain sockets

This section explains how to use Unix domain sockets to connect the PostgreSQL pgx driver to a PostgreSQL-dialect database. Use Unix domain sockets for the lowest possible latency.

To use Unix domain sockets, PGAdapter must be running on the same host as the client application.
    
    
    connString := "host=/tmp port=PORT database=DATABASE_NAME"
    ctx := context.Background()
    conn, err := pgx.Connect(ctx, connString)
    if err != nil {
        return err
    }
    defer conn.Close(ctx)
    
    var greeting string
    err = conn.QueryRow(ctx, "select 'Hello world!' as hello").Scan(&greeting)
    if err != nil {
        return err
    }
    fmt.Printf("Greeting from Cloud Spanner PostgreSQL: %v\n", greeting)
    

Replace the following:

  * /tmp: the default domain socket directory for PGAdapter. This can be changed using the `-dir` command line argument.
  * PORT: the port number where PGAdapter is running. Change this in the connection string if PGAdapter is running on a custom port. Otherwise, use the default port, `5432`.



## What's next

  * Learn more about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * Learn more about [pgx Connection Options](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/docs/pgx.md) in the PGAdapter GitHub repository.
  * See an [overview of drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview) supported for Spanner.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
