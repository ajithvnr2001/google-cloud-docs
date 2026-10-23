---
url: https://docs.cloud.google.com/spanner/docs/use-gorm-postgresql/
title: Integrate Spanner with GORM (PostgreSQL dialect) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:14.264096+00:00
---

# Integrate Spanner with GORM (PostgreSQL dialect)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-gorm-postgresql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with GORM (PostgreSQL dialect) Stay organized with collections  Save and categorize content based on your preferences. 

GORM is an object-relational mapping tool for the Go programming language. It provides a framework for mapping an object-oriented domain model to a relational database.

You can integrate Spanner PostgreSQL databases with GORM using the standard PostgreSQL pgx driver and PGAdapter.

## Set up GORM with Spanner PostgreSQL-dialect databases

  1. Ensure that PGAdapter is running on the same machine as the application that is connecting using GORM with Spanner.

For more information, see [Start PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter-start).

  2. Add an import statement for the PostgreSQL GORM dialect to your application. This is the same driver as you would normally use with a PostgreSQL database.

  3. Specify `localhost` and `5432` as the database server host and port in the GORM connection string. GORM requires a username and password in the connection string. PGAdapter ignores these.

     * Optionally, specify a different port number if PGAdapter is configured to listen on a port other than the default PostgreSQL port (5432).
     * PGAdapter does not support SSL. GORM by default first tries to connect with SSL enabled. Disabling SSL in the connection request speeds up the connection process, because it requires one fewer round trip.
    
    import (
      "gorm.io/driver/postgres"
      "gorm.io/gorm"
    )
    
    dsn := "host=localhost user=gorm password=gorm dbname=gorm port=5432 sslmode=disable"
    db, err := gorm.Open(postgres.Open(dsn), &gorm.Config{})
    




See the [GORM with PostgreSQL documentation](https://gorm.io/docs/connecting_to_the_database.html#PostgreSQL) for more connection options for PostgreSQL.

## Use GORM with Spanner PostgreSQL-dialect databases

For more information about the features and recommendations for using GORM with Spanner, consult the [reference documentation](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/samples/golang/gorm) on GitHub.

## What's next

  * Checkout the [sample application](https://github.com/GoogleCloudPlatform/pgadapter/blob/-/samples/golang/gorm/sample.go) using GORM with PGAdapter and Spanner.
  * Learn more about [GORM](https://gorm.io/).
  * Learn more about [PGAdapter](https://docs.cloud.google.com/spanner/docs/pgadapter).
  * [File a GitHub issue](https://github.com/GoogleCloudPlatform/pgadapter/issues) to report a bug or ask a question about using GORM with Spanner with PGAdapter.
  * See an [overview of drivers and ORMs](https://docs.cloud.google.com/spanner/docs/drivers-overview) supported for Spanner.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
