---
url: https://docs.cloud.google.com/spanner/docs/use-gorm/
title: Integrate Spanner with GORM (GoogleSQL dialect) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:40:13.992823+00:00
---

# Integrate Spanner with GORM (GoogleSQL dialect)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner/docs/use-gorm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner ](https://docs.cloud.google.com/spanner/docs)
  * [ Guides ](https://docs.cloud.google.com/spanner/docs/create-query-database-console)



Send feedback 

#  Integrate Spanner with GORM (GoogleSQL dialect) Stay organized with collections  Save and categorize content based on your preferences. 

GORM is an object-relational mapping tool for the Go programming language. It provides a framework for mapping an object-oriented domain model to a relational database.

You can integrate GoogleSQL-dialect databases with GORM using the open source [Spanner Dialect](https://github.com/googleapis/go-gorm-spanner) (`SpannerDialect`).

## Set up GORM with Spanner GoogleSQL-dialect databases

To use the GoogleSQL GORM dialect in your application, add the following code to the file where GORM is initialized:
    
    
    import (
      "fmt"
    
      "gorm.io/gorm"
      _ "github.com/googleapis/go-sql-spanner"
      spannergorm "github.com/googleapis/go-gorm-spanner"
    )
    
    dsn := fmt.Sprintf("projects/%s/instances/%s/databases/%s", projectId, instanceId, databaseId)
    db, err := gorm.Open(spannergorm.New(spannergorm.Config{DriverName: "spanner", DSN: dsn}), &gorm.Config{})
    

For more connection options for Spanner, see the [GORM with GoogleSQL documentation](https://github.com/googleapis/go-sql-spanner/blob/-/driver.go).

## Use GORM with Spanner GoogleSQL-dialect databases

For more information about the features and recommendations for using GORM with Spanner, consult the [reference documentation](https://github.com/googleapis/go-gorm-spanner) on GitHub.

## What's next

  * Checkout the [sample application](https://github.com/googleapis/go-gorm-spanner/blob/-/samples/helloworld/main.go) using GORM with GoogleSQL and Spanner.
  * Learn more about [GORM](https://gorm.io/).
  * [File a GitHub issue](https://github.com/googleapis/go-gorm-spanner/issues) to report a bug or ask a question about using GORM with Spanner with GoogleSQL.
  * Learn more about [Integrate Spanner with GORM ( PostgreSQL dialect)](https://docs.cloud.google.com/spanner/docs/use-gorm-postgresql).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
