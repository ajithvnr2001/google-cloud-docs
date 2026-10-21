---
url: https://docs.cloud.google.com/looker/docs/db-config-ibm-db2-on-as400/
title: IBM DB2 on AS400 \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T21:46:40.745788+00:00
---

# IBM DB2 on AS400  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-ibm-db2-on-as400/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  IBM DB2 on AS400 Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** As of Looker 23.14, Looker does not support new connections to IBM DB2. Existing connections will continue to work as expected.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Supported JDBC parameters

For IBM DB2 on AS400, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `access`
  * `auto commit`
  * `batch style`
  * `block size`
  * `blocking enabled`
  * `commit hold`
  * `concurrent access resolution`
  * `cursor hold`
  * `cursor sensitivity`
  * `data truncation`
  * `date format`
  * `date separator`
  * `decfloat rounding mode`
  * `decimal separator`
  * `direct map`
  * `errors`
  * `libraries`
  * `lob threshold`
  * `maximum blocked input rows`
  * `naming`
  * `password`
  * `user`



## Feature support

For Looker to support some features, your database dialect must also support them.

IBM DB2 for AS400 and System i supports the following features as of Looker 23.12:

Feature | Supported?  
---|---  
Support Level | Integration  
Looker (Google Cloud core) |   
Symmetric Aggregates |   
Derived Tables |   
Persistent SQL Derived Tables |   
Persistent Native Derived Tables |   
Stable Views |   
Query Killing |   
SQL-based Pivots |   
Timezones |   
SSL |   
Subtotals |   
JDBC Additional Params |   
Case Sensitive |   
Location Type |   
List Type |   
Percentile |   
Distinct Percentile |   
SQL Runner Show Processes |   
SQL Runner Describe Table |   
SQL Runner Show Indexes |   
SQL Runner Select 10 |   
SQL Runner Count |   
SQL Explain |   
Oauth Credentials |   
Context Comments |   
Connection Pooling |   
HLL Sketches |   
Aggregate Awareness |   
Incremental PDTs |   
Milliseconds |   
Microseconds |   
Materialized Views |   
Approximate Count Distinct |   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
