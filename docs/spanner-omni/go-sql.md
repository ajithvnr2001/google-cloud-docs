---
url: https://docs.cloud.google.com/spanner-omni/go-sql/
title: Use the Go SQL package to connect to Spanner Omni \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:49:53.603693+00:00
---

# Use the Go SQL package to connect to Spanner Omni  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/spanner-omni/go-sql/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Spanner Omni ](https://docs.cloud.google.com/spanner-omni)
  * [ Guides ](https://docs.cloud.google.com/spanner-omni/overview)



Send feedback 

#  Use the Go SQL package to connect to Spanner Omni Stay organized with collections  Save and categorize content based on your preferences. 

The [Go SQL package](https://pkg.go.dev/database/sql) is a generic interface around SQL (or SQL-like) databases for the Go programming language. The Spanner driver for the Go SQL package lets you use this standard interface to interact with your Spanner databases.

This document describes how to configure the Go SQL package driver to connect to Spanner Omni. The driver works with Spanner Omni in the same way it works with Spanner, supporting both GoogleSQL and PostgreSQL database dialects.

## Prerequisites

To use the Go SQL package to connect to Spanner Omni, ensure you meet the following requirements:

  * Use [version 1.23.0](https://pkg.go.dev/database/sql@go1.23.0) or later of the Go SQL package. 

  * Add the following module to your `go.mod` file to use the driver in your application:
        
        go get github.com/googleapis/go-sql-spanner
        




## Establish a connection

Run one of the following commands to establish a connection with Spanner Omni:

###  Plain-text communication 

To establish a plain-text communication channel, run the following command:
    
    
    db, err := sql.Open("spanner", "ENDPOINT/databases/DATABASE_ID?use_plain_text=true;is_experimental_host=true")
    

###  TLS connection 

To establish a secure TLS connection, run the following command:
    
    
    db, err := sql.Open("spanner", "ENDPOINT/databases/DATABASE_ID?ca_cert_file=PATH_TO_CA_CRT;is_experimental_host=true")
    

###  mTLS connection 

To establish a mutual TLS (mTLS) connection, run the following command:
    
    
    db, err := sql.Open("spanner", "ENDPOINT/databases/DATABASE_ID?ca_cert_file=PATH_TO_CA_CRT;client_cert_file=PATH_TO_CLIENT_CRT;client_cert_key=PATH_TO_CLIENT_KEY;is_experimental_host=true")
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
