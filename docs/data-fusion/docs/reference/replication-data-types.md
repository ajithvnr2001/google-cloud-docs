---
url: https://docs.cloud.google.com/data-fusion/docs/reference/replication-data-types/
title: Replication data types \u00a0|\u00a0 Cloud Data Fusion \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:17:15.012125+00:00
---

# Replication data types  |  Cloud Data Fusion  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-fusion/docs/reference/replication-data-types/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Cloud Data Fusion ](https://docs.cloud.google.com/data-fusion/docs)
  * [ Reference ](https://docs.cloud.google.com/data-fusion/docs/reference)



Send feedback 

#  Replication data types Stay organized with collections  Save and categorize content based on your preferences. 

This page lists the data type conversions from supported source databases to the BigQuery destination when using Cloud Data Fusion [Replication](https://docs.cloud.google.com/data-fusion/docs/concepts/replication).

## Data type mappings in Replication

### MySQL

The following table lists data type conversions from the MySQL source database to the BigQuery destination.

MySQL data type | BigQuery data type  
---|---  
`BIGINT` | `INT64`  
`BINARY` | `BYTES`  
`BIT` | `BOOL`  
`BLOB` | `BYTES`  
`CHAR` | `STRING`  
`DATE` | `DATE`  
`DATETIME` | `DATETIME`  
`DECIMAL` | `NUMERIC`  
`DOUBLE` | `FLOAT64`  
`ENUM OF CHARS` | `STRING`  
`FLOAT` | `FLOAT64`  
`INT` | `INT64`  
`JSON` | `STRING`  
`LONGBLOB` | `BYTES`  
`LONGTEXT` | `STRING`  
`MEDIUMBLOB` | `BYTES`  
`MEDIUMINT` | `INT64`  
`MEDIUMTEXT` | `STRING`  
`SET` | `STRING`  
`SMALLINT` | `INT64`  
`TEXT` | `STRING`  
`TIME` | `TIME`  
`TIMESTAMP` | `TIMESTAMP`  
`TINYBLOB` | `BYTES`  
`TINYINT` | `INT64`  
`TINYTEXT` | `STRING`  
`VARBINARY` | `BYTES`  
`VARCHAR` | `STRING`  
`YEAR` | `INT64`  
Complex data types | Supported in BigQuery  
---|---  
`ENUM` | Supported  
`SET` | Supported  
  
### Oracle

The following table lists data type conversions from the Oracle source database to the BigQuery destination.

Oracle data type | BigQuery data type  
---|---  
`BFILE` | `STRING`  
`BINARY_DOUBLE` | Unsupported  
`BINARY_FLOAT` | Unsupported  
`BLOB` | Unsupported  
`CHAR` | `STRING`  
`CLOB` | Unsupported  
`DATE` | `TIMESTAMP`  
`DECIMAL` | `STRING`  
`DECIMAL(p)` | `INT64`  
`DECIMAL(*)` | `STRING`  
`DECIMAL(*,s)` | Unsupported  
`DECIMAL(p,s)` | `INT64`  
`DOUBLE PRECISION` | `FLOAT64`  
`FLOAT` | `FLOAT64`  
`INTEGER` | `STRING`  
`INTERVAL DAY TO SECOND` | Unsupported  
`INTERVAL YEAR TO MONTH` | Unsupported  
`LONG` | Unsupported  
`LONG RAW` | Unsupported  
`NCHAR` | `STRING`  
`NCLOB` | Unsupported  
`NUMBER` | `STRING`  
`NUMBER(p)` | `INT64`  
`NUMBER(*)` | `STRING`  
`NUMBER(*,s)` | Unsupported  
`NUMBER(p,s)` | `INT64`  
`NVARCHAR2` | `STRING`  
`RAW` | `BYTES`  
`REAL` | `FLOAT64`  
`ROWID` | `STRING`  
`SDO_GEOMETRY` | Unsupported  
`SMALLINT` | `STRING`  
`TIMESTAMP` | `TIMESTAMP`  
`TIMESTAMP WITH TIME ZONE` | Unsupported  
`VARCHAR` | `STRING`  
`VARCHAR2` | `STRING`  
**Note:** Cloud Data Fusion Replication doesn't support complex data types, such as arrays, records (similar to structs), and maps.

### SQL Server

The following table lists data type conversions from the Microsoft SQL Server source database to the BigQuery destination.

SQL Server data type | BigQuery data type  
---|---  
`BIGINT` | `INT64`  
`BINARY` | `BYTES`  
`BIT` | `BOOL`  
`CHAR` | `STRING`  
`DATE` | `DATE`  
`DATETIME` | `DATETIME`  
`DATETIME2` | `DATETIME`  
`DATETIMEOFFSET` | Unsupported  
`DECIMAL` | `NUMERIC`  
`FLOAT` | `FLOAT64`  
`GEOGRAPHY` | Unsupported  
`GEOMETRY` | Unsupported  
`HIERARCHYID` | `BYTES`  
`IMAGE` | `BYTES`  
`INT` | `INT64`  
`MONEY` | `NUMERIC`  
`NCHAR` | `STRING`  
`NTEXT` | `STRING`  
`NUMERIC` | `NUMERIC`  
`NVARCHAR` | `STRING`  
`REAL` | `FLOAT64`  
`SMALLINT` | `INT64`  
`SMALLMONEY` | `NUMERIC`  
`TEXT` | `STRING`  
`TIME` | `TIME`  
`TINYINT` | `INT64`  
`UNIQUEIDENTIFIER` | `STRING`  
`VARBINARY` | `BYTES`  
`VARCHAR` | `STRING`  
`XML` | `STRING`  
  
## What's next

  * Learn more about [Replication in Cloud Data Fusion](https://docs.cloud.google.com/data-fusion/docs/concepts/replication).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
