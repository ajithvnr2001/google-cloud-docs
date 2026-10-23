---
url: https://docs.cloud.google.com/lakehouse/docs/spark-hive-limitations/
title: Limitations and considerations \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:43:02.310743+00:00
---

# Limitations and considerations  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/spark-hive-limitations/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  Limitations and considerations Stay organized with collections  Save and categorize content based on your preferences. 

Integrating Apache Spark and Apache Hive with the Lakehouse runtime catalog through the **Apache Hive catalog endpoint** lets you share unified metadata and query tables directly in BigQuery without maintaining a self-hosted Hive Metastore (HMS).

Before you migrate or build open-source database pipelines on the Lakehouse runtime catalog, review the functional constraints and service considerations in this document to determine if the integration meets your technical requirements. For setup and query instructions, see [Set up Spark and Hive with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore).

## Lakehouse runtime catalog limitations

This section lists the limitations of using the Lakehouse runtime catalog with various services.

### Metastore limitations

  * Managed Service for Apache Spark supports only PySpark jobs with borderless Lakehouse Metastore.
  * The Dataproc API doesn't support setting Lakehouse Metastore properties in the `properties` field.
  * You can't create Managed Service for Apache Spark clusters that use Kerberos, because Lakehouse runtime catalog doesn't support delegation token or primary key APIs.
  * Databases and tables can use a Cloud Storage `location_uri` that is distinct from their Hive catalog, as long as the Cloud Storage bucket is in the same region as the Hive catalog.
  * The Hive catalog can't contain Iceberg namespaces and tables. To create and use Iceberg namespaces and tables, use the Lakehouse runtime catalog instead.
  * Cascade deletes are not supported for Hive databases and Hive catalogs.
  * Trino support is not available.



### Table limitations

  * Table renaming isn't supported.
  * Partition renaming isn't supported.
  * Deleting tables or databases doesn't remove associated files from Cloud Storage.
  * Case-insensitive search isn't supported.
  * Clustering and bucketing aren't supported.
  * Only virtual views are supported.
  * Delta Lake tables are supported through Apache Spark (read and write) and BigQuery (read-only). Hive clients (such as Hive CLI) don't support Delta Lake tables. All [BigQuery Delta Lake external table limitations](https://docs.cloud.google.com/bigquery/docs/create-delta-lake-table#limitations) and [BigLake table limitations](https://docs.cloud.google.com/bigquery/docs/biglake-tables#limitations) apply. For more details and specific limitations, see [Set up Spark with Delta tables](https://docs.cloud.google.com/lakehouse/docs/use-spark-delta-tables).



### Partition batch size

The Lakehouse runtime catalog supports the storage and retrieval of partitioning information for use in partition pruning. It's optimized for reads over writes, which results in faster query performance through partition pruning.

To optimize partition ingestion performance, the batch partition size is limited to 900.

Set the following configuration for the Hive and Spark properties that determine the batch size of partitioning operations:

  * `SET hive.msck.repair.batch.size = 900;`
  * `SET spark.sql.addPartitionInBatch.size = 900;`



### BigQuery limitations

  * By default, BigQuery doesn't support `ARRAY<ARRAY<>>` or `ARRAY<MAP<>>` data types. Support for `MAP` must be added to an allowlist. Contact [biglake-help@google.com](mailto:biglake-help@google.com) if your workloads use `MAP` extensively.
  * `MAP` key types support only primitive data types. You can't use `ARRAY`, `STRUCT`, or `MAP` as key types.
  * BigQuery can query only data from Cloud Storage. The following limitations apply:

    * Table location URIs can't include a wildcard (`*`).
    * Table location URIs must be directories.



### Cross-region replication and disaster recovery limitations

The Lakehouse runtime catalog provides [cross-region replication and disaster recovery](https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery) to improve your catalog's availability and resilience.

When you use the Lakehouse runtime catalog with Hive catalogs, the following limitations apply:

  * When you create a Hive catalog, you must set its `primary_location` to match your Cloud Storage bucket's region. The Lakehouse runtime catalog then automatically copies the metadata to a secondary region based on your bucket's dual-region or multi-region configuration. This secondary metadata copy is read-only until you promote it to primary using a failover operation.
  * During a failover, the `replication_time` timestamp only tracks catalog metadata replication, not whether underlying Cloud Storage data files have finished replicating to the secondary region. Data redundancy relies on your bucket's dual-region or multi-region settings, which is separate from Lakehouse runtime catalog metadata replication.



## Considerations

The Lakehouse runtime catalog supports a subset of the Hive Metastore interface. This design prioritizes compatibility with the Spark `ExternalCatalog`, which doesn't require full compatibility with the Hive Metastore.

### Resource mapping

The following table maps Hive Metastore resources to the Lakehouse runtime catalog resources and their required Identity and Access Management (IAM) permissions.

Hive Metastore resource | Lakehouse runtime catalog resource | IAM permission  
---|---|---  
Catalog | Catalog | `biglake.catalogs.*`  
Database | Database | `biglake.namespaces.*`  
Table | Table | `biglake.tables.*`  
  
### Governance

The Hive Metastore (HMS) provides governance at the table, column, and partition levels. The Lakehouse runtime catalog provides table-level and partition-level IAM permissions. Column-level governance isn't supported.

### Storage limitations

  * All BigQuery external table limitations apply.



### Partition limitations

  * Tracking column-level statistics at the partition level isn't supported.
  * The `BatchCreateHivePartitions` API limits calls to 900 partitions.



## What's next

  * [Use Spark and Hive with](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore) Lakehouse runtime catalog.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
