---
url: https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables/
title: Compare table types \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:33:53.688981+00:00
---

# Compare table types  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Compare table types Stay organized with collections  Save and categorize content based on your preferences. 

Choosing the right table architecture is critical for maximizing performance, reducing costs, and ensuring data access across your analytics tools. This page explains the different table types and serving endpoints available in borderless Lakehouse, helping you choose the best option based on your write engines, read requirements, and management control needs.

**Tip:** For most modern, open lakehouse workloads, we recommend using Apache Iceberg tables managed by the _Lakehouse runtime catalog_ and served through the _Iceberg REST catalog endpoint_. This configuration provides the best interoperability between open source engines and BigQuery.

## Table formats by catalog or engine

Select a catalog or engine to learn about its supported table formats, metastore configuration, storage optimization capabilities, and engine interoperability.

###  Lakehouse runtime catalog 

The Lakehouse runtime catalog manages Apache Iceberg tables through the Iceberg REST catalog endpoint and provides seamless read-write interoperability across Iceberg compatible engines (Spark, Flink, Trino) and BigQuery, while being backed by the industry-standard [Iceberg REST catalog interface](https://iceberg.apache.org/rest-catalog-spec/).

**Supported table formats**

Apache Iceberg V2 tables (GA) and V3 tables (Preview) are supported. Iceberg V1 tables aren't supported. Before you use existing V1 tables with Lakehouse, you must upgrade them to a supported version. For more information, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#upgrade-v1-to-v2).

Key features include:

  * **Metastore** : Lakehouse runtime catalog.
  * **Storage** : Cloud Storage.
  * **Storage optimization** : Managed by you, or optionally by Google (Preview).
  * **Read and write access** : 
    * Open source engines: read and write (GA)
    * BigQuery: read/write (Preview)
  * **Use cases** : Open lakehouse with high-performance, enterprise-grade storage for advanced analytics, streaming, and AI.



###  Hive metastore 

The _Lakehouse runtime catalog_ manages Apache Hive tables through an Apache Hive metastore (HMS) endpoint optimized for Apache Spark `ExternalCatalog` compatibility, letting you seamlessly share data across Apache Spark, Apache Hive, and BigQuery. You create these tables from open source engines and store them in Cloud Storage. This option is best if you want your ETL workflow to be managed by open source engines without needing a separate self-hosted Hive metastore, and only require read access from BigQuery.

Tables managed by the Hive metastore endpoint are standard Apache Hive and Spark tables (using Hive SerDes or Spark data sources), not Apache Iceberg tables. To create and manage Apache Iceberg tables in the Lakehouse runtime catalog, use the Iceberg REST catalog endpoint instead.

Key features include:

  * **Metastore** : Lakehouse runtime catalog (through custom `IMetastoreClient`).
  * **Storage** : Cloud Storage (supporting formats like Parquet, ORC, and Avro).
  * **Storage optimization** : Managed by you or a third party.
  * **Read and write access** : 
    * Open source engines (Spark and Hive): Read and write.
    * BigQuery: read-only.
  * **Use cases** : Migrating existing Spark and Hive workloads to a fully managed, serverless metastore on Google Cloud.



## Table formats by product

Use the following chart to compare table types in the Lakehouse runtime catalog.

###  Lakehouse 

| **Apache Iceberg (GA)** | **Cross-cloud data access (Preview)** | **Apache Hive (Preview)**  
---|---|---|---  
**Metastore** | Lakehouse runtime catalog | Lakehouse runtime catalog | Lakehouse runtime catalog  
**Storage** | Cloud Storage | Cloud Storage / Amazon S3 | Cloud Storage  
**Storage optimization** | Customer, third-party managed, or Google managed (Preview) | Customer or third-party managed | Customer or third-party managed  
**Read/write** |  Open source engines (read/write)  
  
BigQuery (read/write [Preview]) |  Open source engines (read)  
  
BigQuery (read) |  Open source engines (read/write)  
  
BigQuery (read-only)   
**Advanced operations** | None | None | None  
**Access control** |  [Table-level security with IAM](https://docs.cloud.google.com/lakehouse/docs/iam-and-access-control) |  [Table-level security with IAM](https://docs.cloud.google.com/lakehouse/docs/iam-and-access-control) |  [Table-level security with IAM](https://docs.cloud.google.com/lakehouse/docs/iam-and-access-control)  
**Use cases** | Open lakehouse |  Query data in other cloud providers without migrating files or building complex ETL pipelines.  | Migrate existing Spark and Hive workloads to a fully managed, serverless metastore  
  
## Iceberg table capabilities

Use the following table to learn more about capabilities offered in Apache Iceberg tables in the Lakehouse runtime catalog.

To compare capabilities between Apache Iceberg tables managed by the Lakehouse runtime catalog and Apache Iceberg tables managed by BigQuery, see [Iceberg table capabilities comparison](https://docs.cloud.google.com/bigquery/docs/lakehouse-in-bigquery#iceberg_table_capabilities_comparison).

Capability | Support  
---|---  
**Catalog** | Lakehouse runtime catalog (Iceberg REST catalog compatible)  
**Storage** | Cloud Storage  
**Accessible through the Iceberg REST catalog endpoint** | Yes  
**Read/Write interoperability**  
BigQuery read queries (SELECT, BQML, AI functions) | Supported (GA)  
BigQuery DML (INSERT, UPDATE, DELETE, MERGE) | Supported (Preview)  
OSS engine reads | Supported (GA)  
OSS engine writes | Supported (GA)  
OSS engine streaming writes (Kafka, Spark, Dataflow with Iceberg I/O sink) | Supported (GA)  
**Managed and advanced capabilities**  
Table management (compaction, garbage collection) | Supported (Preview)  
BigQuery Change Data Capture (CDC) | Supported (Preview)  
**Time Travel**  
Time travel (using OSS engines) | Flexible (configured through table properties)  
Time travel (using BigQuery) | Limited to 7 days  
Snapshot history and rollback to previous snapshot | Supported (GA)  
**Knowledge catalog capabilities**  
Metadata cataloging, search and discovery | Supported (GA)  
Lineage | Supported (GA)  
Data quality/profiling | Supported (GA)  
Insights | Supported (GA)  
AI based column and table descriptions generation | Supported (GA)  
  
## What's next

  * Learn how to [manage Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables).

  * Learn how to [import external Iceberg tables using Dataflow](https://docs.cloud.google.com/lakehouse/docs/import-iceberg-tables).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
