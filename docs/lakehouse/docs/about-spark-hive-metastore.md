---
url: https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore/
title: About Hive Catalogs in Lakehouse runtime catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:43.977851+00:00
---

# About Hive Catalogs in Lakehouse runtime catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  About Hive Catalogs in Lakehouse runtime catalog Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

The Lakehouse runtime catalog is a serverless, unified metastore that simplifies managing self-hosted Hive metastores. This single, fully managed metadata layer eliminates the need for separate metadata stores for open-source workloads. It lets you seamlessly share data across Apache Spark, Apache Hive, and BigQuery.

**Important:** If you would like to upgrade from Dataproc Metastore to the Lakehouse runtime catalog, contact [Dataproc Metastore support](https://docs.cloud.google.com/dataproc-metastore/docs/support/getting-support). 

Optimized for Apache Spark `ExternalCatalog` compatibility, this integration supports a subset of the Hive Metastore interface. To see if your workloads depend on unsupported features like transactions, compactions, or Kerberos, review the feature comparison and [limitations](https://docs.cloud.google.com/lakehouse/docs/spark-hive-limitations).

## How Hive integrates with the Lakehouse runtime catalog

The Hive metastore endpoint manages standard Apache Hive and Spark tables (using Hive SerDes or Spark data sources) rather than Apache Iceberg tables. To simplify connecting your Spark jobs to this endpoint, Managed Service for Apache Spark images are preconfigured with the necessary client libraries and dependencies.

The following sequence describes how Spark connects to the metastore:

  1. Apache Spark connects to external metadata catalogs by using the standard Apache Hive `IMetastoreClient` interface.
  2. The Lakehouse runtime catalog implements a custom `IMetastoreClient` to provide a fully managed metastore service for your Spark and Hive metadata.
  3. Preconfigured Managed Service for Apache Spark runtimes automatically use this custom client to route metadata operations directly to the metastore.



After setup, you can query your Spark-created tables directly in BigQuery. This integration supports various storage formats—such as Parquet, ORC, and Avro—along with specific data type mappings between Spark and BigQuery.

## How the Hive catalog integrates with Google Cloud services

To understand how borderless Lakehouse manages your data, see how the Hive catalog architecture integrates with Google Cloud services. Rather than maintaining self-hosted metastores, your open-source workloads connect to the Lakehouse runtime catalog to manage Hive database and table definitions, while storing the underlying data files directly in Cloud Storage warehouse directories.

The following diagram illustrates how compute engines like Managed Service for Apache Spark use the Lakehouse runtime catalog to manage table metadata while reading and writing underlying data files directly in Hive.

![Components of a Lakehouse architecture, including Managed Service for Apache Spark, Cloud Storage, and the Apache Hive catalog.](https://docs.cloud.google.com/static/lakehouse/images/hivecatalog-lakehouse.png)Lakehouse Hive catalog architecture diagram.

## Feature comparison with Hive Metastore

The following table compares entities and operations in Hive Metastore and Lakehouse:

Entity or operation | Hive Metastore | Lakehouse runtime catalog  
---|---|---  
Catalog | ✅ | ✅  
Database (create, delete, update) | ✅ | ✅  
Table (create, delete, update) | ✅ | ✅  
Partition (add, drop, update) | ✅ | ✅  
Table privileges | ✅ | ✅ (through Identity and Access Management (IAM))  
Partition privileges | ✅ | ✅ (through IAM)  
User-defined functions | ✅ | Not supported  
Bucketing / Skewing columns | ✅ | Not supported  
Table and partition column stats | ✅ | Not supported  
Key constraints | ✅ | Not supported  
Delegation tokens (Kerberos) | ✅ | Not supported  
Column privileges | ✅ | Not supported  
Roles | ✅ | Not supported  
Workload manager resource plans | ✅ | Not supported  
Transactions and compactions | ✅ | Not supported  
  
## What's next

  * [Use Spark and Hive with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore).
  * [Use Lakehouse regional endpoints](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
