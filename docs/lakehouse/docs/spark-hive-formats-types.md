---
url: https://docs.cloud.google.com/lakehouse/docs/spark-hive-formats-types/
title: Supported storage formats and data types \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:44.388062+00:00
---

# Supported storage formats and data types  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/spark-hive-formats-types/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Supported storage formats and data types Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document details how data types and storage formats behave when integrating Spark and Hive with BigQuery through the Lakehouse runtime catalog.

Specifically, this document provides:

  * **Supported storage formats** : A compatibility breakdown of formats like Parquet, ORC, Avro, CSV, and JSON across Hive SerDe and Spark data sources.
  * **Data type mappings** : The precise conversion rules between Spark and BigQuery data types.



Use this page to verify that your table schemas and storage formats align with the metastore before you run workloads or query tables across engines.

## Supported storage formats between Hive and Spark

The following sections describe the storage format and data source compatibility between Hive, Spark, and BigQuery.

### Detailed storage format mapping

BigQuery determines the storage format of a table based on the `input_format`, `output_format`, and `SerDe` library in the metadata. The following table maps these properties to the BigQuery storage format.

Input format, output format, and SerDe library | BigQuery storage format  
---|---  
`org.apache.hadoop.hive.ql.io.parquet.MapredParquetInputFormat`   
`org.apache.hadoop.hive.ql.io.parquet.MapredParquetOutputFormat`   
`org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe` | Parquet  
`org.apache.hadoop.hive.ql.io.orc.OrcInputFormat`   
`org.apache.hadoop.hive.ql.io.orc.OrcOutputFormat`   
`org.apache.hadoop.hive.ql.io.orc.OrcSerde` | ORC  
`org.apache.hadoop.hive.ql.io.avro.AvroContainerInputFormat`   
`org.apache.hadoop.hive.ql.io.avro.AvroContainerOutputFormat`   
`org.apache.hadoop.hive.serde2.avro.AvroSerDe` | Avro  
`org.apache.hadoop.mapred.TextInputFormat`   
`org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat`   
`org.apache.hadoop.hive.serde2.OpenCSVSerde` | CSV  
`org.apache.hadoop.mapred.TextInputFormat`   
`org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat`   
`org.openx.data.jsonserde.JsonSerDe` | JSON  
`org.apache.hadoop.mapred.TextInputFormat`   
`org.apache.hadoop.hive.ql.io.HiveIgnoreKeyTextOutputFormat`   
`org.apache.hive.hcatalog.data.JsonSerDe` | JSON  
  
### Hive SerDe compatibility

The following table lists the compatibility of Hive SerDe table formats with BigQuery.

Format | Spark SQL DDL syntax | Queryable from BigQuery  
---|---|---  
Parquet | `CREATE TABLE ... STORED AS PARQUET` | Yes  
ORC | `CREATE TABLE ... STORED AS ORC` | Yes  
Avro | `CREATE TABLE ... STORED AS AVRO` | Yes  
CSV | `CREATE TABLE ... ROW FORMAT 'org.apache.hadoop.hive.serde2.OpenCSVSerde'` | Yes  
JSON | `CREATE TABLE ... ROW FORMAT 'org.openx.data.jsonserde.JsonSerDe'` | Yes  
  
### Spark data source compatibility

The following table lists the compatibility of Spark data source table formats with BigQuery.

CSV and JSON SerDe tables are queryable from BigQuery. However, CSV and JSON Spark data source tables are not.

Format | Spark SQL DDL syntax | Queryable from BigQuery  
---|---|---  
Parquet | `CREATE TABLE ... USING PARQUET` | Yes  
ORC | `CREATE TABLE ... USING ORC` | Yes  
Avro | `CREATE TABLE ... USING AVRO` | Yes  
CSV | `CREATE TABLE ... USING CSV` | No  
JSON | `CREATE TABLE ... USING JSON` | No  
  
## Supported data types from Spark to BigQuery

The following table maps Spark data types to BigQuery data types.

Spark data type | BigQuery data type  
---|---  
`BYTE` or `TINYINT` | `INT64`  
`SMALLINT` or `SHORT` | `INT64`  
`INT` or `INTEGER` | `INT64`  
`BIGINT` or `LONG` | `INT64`  
`DECIMAL` or `NUMERIC` | `BIGNUMERIC`  
`FLOAT` | `FLOAT64`  
`DOUBLE` | `FLOAT64`  
`REAL` | `FLOAT64`  
`BOOLEAN` | `BOOL`  
`STRING` | `STRING`  
`VARCHAR` | `STRING`  
`CHAR` or `CHARACTER` | `STRING`  
`BINARY` | `BYTES`  
`DATE` | `DATE`  
`TIMESTAMP` or `TIMESTAMP_LTZ` | `TIMESTAMP`  
`ARRAY` | `ARRAY`  
`STRUCT<col_name: type1, ...>` | `STRUCT<col_name: type1, ...>`  
`MAP<key_type, value_type>` | `ARRAY<STRUCT<key: key_type, value: value_type>>`  
To enable this feature, send an email to biglake-help@google.com. This is only necessary if your workloads use `MAP`.  
  
## What's next

  * [Use Spark and Hive with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
