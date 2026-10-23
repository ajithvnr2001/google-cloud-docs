---
url: https://docs.cloud.google.com/looker/docs/db-config-ibm-db2-for-luw/
title: IBM DB2 for Linux, UNIX, and Windows (LUW) \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:42:43.846115+00:00
---

# IBM DB2 for Linux, UNIX, and Windows (LUW)  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/db-config-ibm-db2-for-luw/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)



Send feedback 

#  IBM DB2 for Linux, UNIX, and Windows (LUW) Stay organized with collections  Save and categorize content based on your preferences. 

Manage your existing IBM DB2 for Linux, UNIX, and Windows (LUW) connections in Looker. As of Looker 23.14, you cannot create new connections to IBM DB2, but you can continue to manage existing connections. Use this page to review supported JDBC parameters and feature compatibility for existing connections.

## Encrypting network traffic

It is a best practice to encrypt network traffic between the Looker application and your database. Consider one of the options that are described on the [Enabling secure database access](https://docs.cloud.google.com/looker/docs/enabling-secure-db-access) documentation page.

## Supported JDBC parameters

For existing connections to IBM DB2, Looker supports the following JDBC parameters in the [**Additional JDBC parameters**](https://docs.cloud.google.com/looker/docs/connecting-to-your-db#additional_jdbc_parameters) field for the connection. See the documentation for your database for information on these parameters.

  * `accountingInterval`
  * `allowSqljDuplicateStaticQueries`
  * `alternateUTF8Encoding`
  * `charOutputSize`
  * `clientApplcompat`
  * `currentFunctionPath`
  * `currentPackageSet`
  * `currentSQLID`
  * `currentSchema`
  * `customerId`
  * `decimalRoundingMode`
  * `defaultSQLState`
  * `diagLevelExceptionCode`
  * `disableClientInputDataConversion`
  * `disableSQLJProfileCaching`
  * `disableTimezone`
  * `enableDualTransportUsingDifferentProcess`
  * `enableInetAddressGetHostName`
  * `enableMultirowInsertSupport`
  * `enableSeamlessFailoverErrorCodes`
  * `enableSysplexWLB`
  * `enableT2zosLBF`
  * `enableT2zosLBFSPResultSets`
  * `enableT2zosLBFSwitchWithIDAA`
  * `encryptionAlgorithm`
  * `extendedTableInfo`
  * `indexName`
  * `instanceId`
  * `jmxEnabled`
  * `keyword`
  * `lobOutputSize`
  * `maxRefreshInterval`
  * `maxTransportObjectIdleTime`
  * `maxTransportObjectWaitTime`
  * `maxTransportObjects`
  * `minTransportObjects`
  * `onDataTruncation`
  * `pkList`
  * `planName`
  * `progressiveStreaming`
  * `queryPrefetch`
  * `rollbackOnShutdown`
  * `securityMechanism`
  * `sendCharInputsUTF8`
  * `ssid`



## Feature support

For Looker to support some features, your database dialect must also support them.

IBM DB2 supports the following features as of Looker 23.14:

Feature | Supported?  
---|---  
Support Level | Supported  
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
OAuth Credentials |   
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

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
