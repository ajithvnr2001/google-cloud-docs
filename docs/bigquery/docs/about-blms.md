---
url: https://docs.cloud.google.com/bigquery/docs/about-blms/
title: About the Lakehouse runtime catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-16T14:41:41.730282+00:00
---

# About the Lakehouse runtime catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/bigquery/docs/about-blms/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  About the Lakehouse runtime catalog Stay organized with collections  Save and categorize content based on your preferences. 

The Lakehouse runtime catalog lets you centralize table metadata in a fully-managed, serverless metastore that serves as a single source of truth for your data in borderless Lakehouse. With centralized metadata, processing engines—including Apache Spark, Apache Flink, Apache Hive, and BigQuery—can share tables directly without duplicating files.

When you configure a client endpoint such as the Apache Iceberg REST catalog, it acts as a management interface that connects query engines to the Lakehouse runtime catalog. The endpoint handles table metadata, and Cloud Storage stores the underlying metadata and data files.

As a core component of Lakehouse, the Lakehouse runtime catalog provides open API interoperability and supports analytics, streaming, and AI workloads when paired with BigQuery. For more information about these architectural benefits, see [What is borderless Lakehouse?](https://docs.cloud.google.com/lakehouse/docs/introduction)

## How Lakehouse integrates with Google Cloud

To understand how Lakehouse manages your data, see how the Lakehouse architecture integrates with Google Cloud services. Apache Iceberg doesn't store data in monolithic tables. Instead, it uses a layered architecture of metadata files to organize data files into a cohesive table structure with ACID transaction support.

The following diagram illustrates how compute engines like Managed Service for Apache Spark use the Lakehouse runtime catalog to manage table metadata to read and write underlying Parquet data files directly in Cloud Storage.

![Components of a lakehouse architecture, including Managed Service for Apache Spark, Cloud Storage, and the Lakehouse REST Catalog.](https://docs.cloud.google.com/static/lakehouse/images/lakehouse-diagram.png)Lakehouse architecture diagram.

When you use Lakehouse, the technical architecture consists of three distinct layers:

  1. **Catalog layer** :

     * **Core Iceberg concept** : The catalog stores the current state of the table by maintaining a pointer to the latest metadata file. This layer facilitates ACID compliance and transaction isolation to ensure that concurrent writes don't interfere with each other.
     * **Lakehouse implementation** : The _Lakehouse runtime catalog_ acts as the top-level regional metastore service. Within this service, you create individual [_catalogs_](https://docs.cloud.google.com/lakehouse/docs/create-catalog) to manage your data hierarchy. Client query engines connect to these catalogs by using specific [endpoint catalog types](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), such as the _Apache Iceberg REST catalog_ endpoint. The metastore manages transaction commits, [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending) for storage access delegation, and pointer management across your catalogs.
  2. **Metadata layer** :

     * **Core Iceberg concept** : This layer tracks the table structure, snapshots, and file locations by using a hierarchy of three file types: 
       * _Metadata files_ : Store the table's schema, partition specification, and a log of snapshot pointers.
       * _Manifest lists_ : Represent a single snapshot of the table by grouping a collection of manifest files.
       * _Manifest files_ : Track data at the individual file level, storing file paths, partition information, and column-level statistics, for example, row counts and minimum and maximum values, which are used for query optimization and partition pruning.
     * **Lakehouse implementation** : Within a catalog container, you organize your data into logical [_namespaces_](https://docs.cloud.google.com/lakehouse/docs/create-namespace) (similar to datasets) and [_tables_](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables). For each table, the Lakehouse runtime catalog generates and manages the underlying Iceberg metadata hierarchy, starting with a root `metadata.json` file that points to the manifest lists and manifest files. The Lakehouse runtime catalog persists these files directly in your designated warehouse storage location.
  3. **Data layer** :

     * **Core Iceberg concept** : This component is the underlying storage where the actual raw data records reside, typically in optimized columnar or row-based open file formats such as Parquet, ORC, or Avro.
     * **Lakehouse implementation** : When you configure Cloud Storage warehouse locations (`gs://`), the physical data files referenced by your tables are stored securely within your buckets. The Lakehouse runtime catalog manages access through _storage access delegation_ ([credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending)), vending short-lived access tokens directly to client engines. This lets engines read and write data files securely without requiring broad, direct [IAM permissions](https://docs.cloud.google.com/lakehouse/docs/iam-and-access-control) on the underlying buckets.



## How Lakehouse implements the Apache Iceberg REST Catalog API

The _Lakehouse runtime catalog_ implements the open source [Apache Iceberg REST Catalog API](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml) to manage namespaces and tables. It also provides an [extensions API](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs) specifically for catalog management.

Client query engines interact with the metastore using these standard REST catalog APIs. For details about Google Cloud resources and endpoints, see the [Lakehouse REST API reference](https://docs.cloud.google.com/lakehouse/docs/reference/rest).

You can create, configure, and manage these resources using the Google Cloud console, the gcloud CLI, the REST API, or Terraform. For more information, see the following pages:

  * [Manage Iceberg REST catalog resources](https://docs.cloud.google.com/lakehouse/docs/manage-catalogs)
  * [Manage Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables)
  * [Use Terraform with Lakehouse](https://docs.cloud.google.com/lakehouse/docs/terraform-support)
  * [Use regional endpoints with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints)



## Query engine compatibility and configuration

To analyze and manage data in the Lakehouse runtime catalog, you can connect different open source and enterprise query engines. Depending on your existing architecture and workload requirements, you can choose from several supported engines and configure the appropriate catalog endpoint.

### Supported engines

The Lakehouse runtime catalog is compatible with several query engines including (but not limited to) Apache Spark, Apache Flink, Apache Hive, and Trino. The following table provides links to documentation for each engine:

**Engine** | **Documentation**  
---|---  
Apache Spark |  [Use with Apache Spark](https://docs.cloud.google.com/lakehouse/docs/spark-support)  
Apache Hive |  [Use with Spark and the Hive catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore)  
Apache Flink |  [Use with Apache Flink](https://docs.cloud.google.com/lakehouse/docs/flink-support)  
Trino |  [Use with Trino](https://docs.cloud.google.com/lakehouse/docs/trino-support)  
  
### Catalog types and endpoint configuration

When configuring client engines to connect to the Lakehouse runtime catalog metastore, you select a specific _catalog_ endpoint, such as the _Apache Iceberg REST catalog_ endpoint or the Apache Hive endpoint. The best option depends on your use case, as shown in the following table:

**Use case** | **Recommendation**  
---|---  
New Lakehouse runtime catalog users that want their open source engine to access data in Cloud Storage and need interoperability with other engines, including BigQuery and AlloyDB for PostgreSQL.  |  Use the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint).   
Users running Apache Hive or Spark workloads that depend on the Hive Metastore interface and want a fully managed metastore service.  |  Use the [Apache Hive catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore).   
Existing Lakehouse runtime catalog users that have current tables created with the custom Apache Iceberg catalog for BigQuery endpoint.  |  Continue using the [custom Apache Iceberg catalog for BigQuery endpoint](https://docs.cloud.google.com/lakehouse/docs/about-custom-iceberg-catalog-endpoint), but use the [Apache Iceberg REST catalog](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint) for new workflows.   
  
## Lakehouse runtime catalog limitations

The following general limitations apply to tables in the Lakehouse runtime catalog when querying them through BigQuery. Individual catalog endpoints (such as Apache Iceberg REST or Apache Hive) might have additional endpoint-specific limitations.

**Table management**

  * Apache Iceberg V2 tables (GA) and V3 tables (Preview) are supported. Iceberg V1 tables aren't supported. Before you use existing V1 tables with the Lakehouse runtime catalog, you must upgrade them to a supported version. For more information, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/update-tables).
  * Tables in the Lakehouse runtime catalog don't support [renaming operations](https://docs.cloud.google.com/bigquery/docs/managing-tables#renaming-table) or the `ALTER TABLE ... RENAME TO` Spark SQL statement.
  * Tables in the Lakehouse runtime catalog don't support [clustering](https://docs.cloud.google.com/bigquery/docs/clustered-tables).
  * Tables in the Lakehouse runtime catalog don't support [extract jobs](https://docs.cloud.google.com/bigquery/docs/export-intro). This limitation applies to both `EXPORT DATA` statements and the `bq extract` CLI command.
  * The Lakehouse runtime catalog doesn't support database or metastore views.
  * The Lakehouse runtime catalog doesn't support Apache Iceberg views.



**Querying**

  * Query performance for tables in the Lakehouse runtime catalog from the BigQuery engine might be slow compared to querying data in standard BigQuery tables. In general, query speed should be equivalent to reading data from Cloud Storage.
  * A [BigQuery dry run](https://docs.cloud.google.com/bigquery/docs/running-queries#dry-run) of a query that uses a table in the Lakehouse runtime catalog might report a lower bound of 0 bytes of data, even if rows are returned. This result occurs because the amount of data that is processed from the table can't be determined until the full query is run. Running the query incurs a cost for processing this data.
  * You can't reference a table in the Lakehouse runtime catalog in a [wildcard table](https://docs.cloud.google.com/bigquery/docs/querying-wildcard-tables) query.



**API and metadata**

  * You can't use the [`tabledata.list` method](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/tabledata/list) to retrieve data from tables in the Lakehouse runtime catalog. Instead, you can save query results to a BigQuery table, and then use the `tabledata.list` method on that table.
  * The display of table storage statistics for tables in the Lakehouse runtime catalog isn't supported.



**Quotas and limits**

  * Tables in the Lakehouse runtime catalog in BigQuery are subject to the same [quotas and limits](https://docs.cloud.google.com/bigquery/quotas#standard_tables) as standard tables.



## Differences with BigLake metastore (classic)

**Warning:** [BigLake metastore (classic)](https://docs.cloud.google.com/bigquery/docs/manage-open-source-metadata) is considered a legacy feature and is no longer recommended. Use the Lakehouse runtime catalog as the recommended metastore on Google Cloud. 

The core differences between the Lakehouse runtime catalog and BigLake metastore (classic) include the following:

  * The Lakehouse runtime catalog supports a direct integration with open source engines like Spark, which helps reduce redundancy when you store metadata and run jobs. Tables in the Lakehouse runtime catalog are directly accessible from multiple open source engines and BigQuery.
  * The Lakehouse runtime catalog supports the Apache Iceberg REST catalog endpoint, while BigLake metastore (classic) doesn't.



## What's next

  * Understand the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint).
  * Configure [regional endpoints](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
