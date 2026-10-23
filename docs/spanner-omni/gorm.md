---
url: https://docs.cloud.google.com/spanner-omni/gorm/
title: Use GORM to connect to Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:10:42.206006+00:00
---

# Use GORM to connect to Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/gorm/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use GORM to connect to Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

[GORM](https://gorm.io/) is an object-relational mapping (ORM) tool for the Go programming language. It provides a framework for mapping an object-oriented domain model to a relational database. You can integrate GoogleSQL-dialect databases with GORM using the open source [Spanner Dialect](https://github.com/googleapis/go-gorm-spanner) (`SpannerDialect`).

This document describes how to configure GORM to connect to Spanner Omni. GORM integrates with Spanner Omni in the same way it integrates with Spanner. Note that GORM supports integration with Spanner Omni using the GoogleSQL dialect, but not the PostgreSQL dialect.

For more information, see [Integrate Spanner with GORM](https://docs.cloud.google.com/spanner/docs/use-gorm) in the Spanner documentation.

## Prerequisites

Spanner Omni requires [`go-gorm-spanner`](https://github.com/googleapis/go-gorm-spanner) version 1.10.0 or later. To use the Spanner GORM dialect in your application, add the following modules to your `go.mod` file:
    
    
    go get github.com/googleapis/go-sql-spanner
    go get github.com/googleapis/go-gorm-spanner
    

## Configure GORM for GoogleSQL databases

To use the GoogleSQL GORM dialect in your application, add the following import statements to the file where GORM is initialized:
    
    
    import (
        "fmt"
    
        "gorm.io/gorm"
        _ "github.com/googleapis/go-sql-spanner"
        spannergorm "github.com/googleapis/go-gorm-spanner"
    )
    
    dsn := fmt.Sprintf("%s/databases/%s?use_plain_text=true", SPANNER_OMNI_ENDPOINT, DATABASE_ID)
    db, err := gorm.Open(spannergorm.New(spannergorm.Config{DriverName: "spanner", DSN: dsn}), &gorm.Config{})
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
