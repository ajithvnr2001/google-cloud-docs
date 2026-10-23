---
url: https://docs.cloud.google.com/lakehouse/docs/release-notes/
title: Lakehouse release notes \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:42:05.189485+00:00
---

# Lakehouse release notes  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/release-notes/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Resources ](https://docs.cloud.google.com/lakehouse/docs/release-notes)



Send feedback 

#  Lakehouse release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page documents production updates to _Lakehouse_. Check this page for announcements about new or updated features, bug fixes, known issues, and deprecated functionality. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

## October 14, 2026

Feature

The Apache Hive catalog endpoint in the Lakehouse runtime catalog is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). This integration lets you use the metastore as a serverless, central metadata layer, enabling seamless data sharing and unified querying across Apache Spark, Apache Hive, and BigQuery.

For more information, see [About the Hive catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore) and [Set up Spark and Hive with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore).

Feature

Metadata migration from Dataproc Metastore to Lakehouse is now [generally available](https://cloud.google.com/products#product-launch-stages) (GA). You can perform a one-time backfill migration or dry run to migrate metadata from a Dataproc Metastore service to an Apache Iceberg REST catalog endpoint or a Hive catalog endpoint using the Google Cloud console, the gcloud CLI, or the REST API.

For more information, see [Migrate metadata from Dataproc Metastore to Lakehouse](https://docs.cloud.google.com/lakehouse/docs/migrate-dataproc-metastore).

## October 08, 2026

Feature

The following table types now support [flexible column names](https://docs.cloud.google.com/bigquery/docs/schemas#flexible-column-names) by default:

  * [Iceberg external tables](https://docs.cloud.google.com/bigquery/docs/iceberg-external-tables) and [Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/iceberg-tables) in BigQuery
  * [Apache Iceberg tables managed by the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/manage-tables)



This feature is [generally available](https://cloud.google.com/products#product-launch-stages) (GA).

## October 06, 2026

Feature

Lakehouse now supports change data capture (CDC) ingestion from Delta Lake and Apache Iceberg tables ([Preview](https://cloud.google.com/products#product-launch-stages)).

You can now synchronize CDC transaction logs (inserts, updates, deletes) from Delta Lake and Apache Iceberg tables into Lakehouse Apache Iceberg tables using Dataflow batch jobs (for Delta Lake) or batch and streaming jobs (for Apache Iceberg). For more information, see [Migrate Delta Lake CDC data into Lakehouse using Dataflow](https://docs.cloud.google.com/lakehouse/docs/migrate-delta-lake-cdc) and [Migrate Apache Iceberg CDC data into Lakehouse using Dataflow](https://docs.cloud.google.com/lakehouse/docs/migrate-iceberg-cdc).

## September 28, 2026

Feature

You can now write the output rows produced by [BigQuery continuous queries](https://docs.cloud.google.com/bigquery/docs/continuous-queries-introduction) directly into [Apache Iceberg managed tables](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery). This lets you continuously process streaming data from BigQuery and write it into your open-format lakehouse by using an [`INSERT` DML statement](https://docs.cloud.google.com/bigquery/docs/continuous-queries#write-bigquery).

## September 21, 2026

Feature

_Lakehouse_ now supports Workday Data Lake as a remote catalog provider for cross-cloud data access ([Preview](https://cloud.google.com/products#product-launch-stages)). You can configure federated catalogs to query data stored in Workday Data Lake directly from Google Cloud using BigQuery or Apache Spark without migrating data or building complex ETL pipelines.

For more information, see [Set up cross-cloud connection for Workday Data Lake](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-connection-workday).

## August 31, 2026

Feature

_Lakehouse_ supports change data capture (CDC) ingestion (Preview) in regions where the Apache Iceberg REST catalog is supported.

This feature lets you synchronize your source databases with Apache Iceberg managed tables in real time.

For more information, see [Change data capture ingestion](https://docs.cloud.google.com/lakehouse/docs/change-data-capture).

Feature

_Lakehouse caching_ is now available in Preview for borderless Lakehouse.

Lakehouse caching automatically caches data blocks locally within Google Cloud when running cross-cloud queries against remote data (such as AWS S3 or SAP BDC). Caching helps reduce cross-cloud egress fees for repeated query patterns.

For more information, see [Intelligent caching](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access#intelligent-caching) and [Monitor cache usage and egress cost savings](https://docs.cloud.google.com/lakehouse/docs/query-remote-data#caching-stats).

## August 19, 2026

Feature

You can now import existing Delta Lake tables from Cloud Storage (`gs://BUCKET_NAME`) directly into Lakehouse using Dataflow's job builder UI without writing code. For more information, see [Import Delta Lake tables into Lakehouse using Dataflow](https://docs.cloud.google.com/lakehouse/docs/import-delta-lake-tables).

## July 31, 2026

Announcement

_Cross-cloud Lakehouse_ is now called _borderless Lakehouse_.

For more information, see [About borderless Lakehouse](https://docs.cloud.google.com/lakehouse/docs/about-borderless-lakehouse).

## July 27, 2026

Feature

_Lakehouse_ supports the BigQuery Storage Write API (gRPC) (Preview) in regions where the Apache Iceberg REST catalog is supported.

This feature lets you stream data efficiently using high-performance, transactionally consistent ingestion into Apache Iceberg managed tables.

For more information, see [Stream data with the Storage Write API (gRPC)](https://docs.cloud.google.com/lakehouse/docs/bigquery-storage-api).

## July 20, 2026

Issue

Data products with special characters, such as "/" or "-", are not supported and will not be available in BigQuery even if shared from SAP BDC to BigQuery. If you share a data product with special characters, this could cause the refresh to stop on the Google side and require re-enrollment. Known SAP systems producing these data products include BW sources and SuccessFactors.

Feature

_Cross-cloud Lakehouse_ now supports integration with SAP Business Data Cloud (BDC) (GA).

This update includes the following features:

  * **Federation from SAP BDC:** Create Delta Sharing catalogs in Lakehouse to automatically synchronize shares, schemas, and tables from SAP BDC.
  * **Querying SAP data:** Query synchronized SAP BDC tables directly from BigQuery without data migration.
  * **Publishing to SAP BDC:** Publish Apache Iceberg tables or Knowledge Catalog Data Products from Lakehouse directly to SAP BDC, allowing SAP users and applications to consume Google Cloud data directly as remote tables in SAP Datasphere without migrating data.



For more information, see [Set up cross-cloud Lakehouse for SAP BDC](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse-sap-bdc), [Query SAP BDC data](https://docs.cloud.google.com/lakehouse/docs/query-sap-data), and [Publish Data Products to SAP BDC](https://docs.cloud.google.com/lakehouse/docs/publish-data-to-sap-bdc).

## July 13, 2026

Feature

_Cross-cloud Lakehouse_ now supports Snowflake Horizon Catalog as a remote catalog provider (Preview). You can configure federated catalogs to query data stored in Snowflake Horizon Catalog directly from Google Cloud using BigQuery or Apache Spark without migrating data or building complex ETL pipelines.

For more information, see [Set up cross-cloud Lakehouse for Snowflake Horizon Catalog](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse-snowflake).

## June 25, 2026

Feature

_Lakehouse_ now supports BigQuery writes (DML, DDL) and automatic table management for Apache Iceberg tables in the Lakehouse runtime catalog (Preview).

This update introduces the following features:

**Read/write interoperability:** Full read and write (DML) support across Managed Service for Apache Spark, open source engines (such as Spark, Flink, and Trino).

**BigQuery SQL DDL and DML:** Create, alter, and delete tables, or modify data using standard SQL DDL and DML statements (`INSERT`, `UPDATE`, `DELETE`, and `MERGE`) directly in BigQuery.

**Automatic table management:** Opt in to automatic storage optimization, including compaction and garbage collection.

For more information, see [Apache Iceberg tables](https://docs.cloud.google.com/lakehouse/docs/manage-tables) and [Configure table options](https://docs.cloud.google.com/lakehouse/docs/table-options).

## June 12, 2026

Feature

_Lakehouse_ now supports custom catalog names and data distributed across multiple buckets. For more information, see [Create a catalog](https://docs.cloud.google.com/lakehouse/docs/create-catalog).

## June 11, 2026

Feature

_Lakehouse runtime catalog_ now supports Apache Iceberg V3 tables with Binary Deletion Vectors (BDV) (Preview). This feature is useful for handling high-volume updates and deletes by deleting specific rows without the overhead of rewriting entire data files.

For more information, see [Use Binary Deletion Vectors in Iceberg V3 tables](https://docs.cloud.google.com/lakehouse/docs/use-iceberg-v3-binary-deletion-vectors).

## June 05, 2026

Feature

_Cross-cloud Lakehouse_ now supports AWS Glue as a remote catalog provider (Preview). You can configure federated catalogs to query data stored in AWS Glue directly from Google Cloud using BigQuery or Apache Spark without migrating data or building complex ETL pipelines.

For more information, see [Set up cross-cloud Lakehouse for AWS Glue](https://docs.cloud.google.com/lakehouse/docs/set-up-cross-cloud-lakehouse-aws-glue).

## May 26, 2026

Feature

_Lakehouse_ now supports using Apache Spark and Apache Hive with the Lakehouse runtime catalog and the Hive catalog. This integration lets you use the metastore as a serverless, central metadata layer, enabling seamless data sharing and unified querying across Spark, Hive, and BigQuery using supported environments (such as Managed Service for Apache Spark).

For more information, see [About Hive Catalogs in Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore) and [Use Spark and Hive with the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/use-spark-hive-metastore).

## May 15, 2026

Feature

_Lakehouse_ now supports the [BigQuery advanced runtime](https://docs.cloud.google.com/bigquery/docs/advanced-runtime) for Apache Iceberg tables.

For more information, see [BigQuery Iceberg tables overview](https://docs.cloud.google.com/bigquery/docs/biglake-iceberg-tables-in-bigquery).

## May 07, 2026

Feature

_Google Cloud Lakehouse_ now supports the Apache Iceberg REST [Metrics Reporting](https://iceberg.apache.org/docs/latest/metrics-reporting/) endpoint.

You no longer have to [configure your clients](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#configure-catalog) to use the `rest-metrics-reporting-enabled=false` option.

## April 22, 2026

Feature

_Cross-cloud Lakehouse_ is now available in Preview. This feature extends _Lakehouse_ , letting you query data in other cloud providers (such as Databricks Unity Catalog on AWS) directly from Google Cloud using BigQuery, Managed Service for Apache Spark, and Apache Spark without migrating data or complex ETL.

For more information, see [About cross-cloud Lakehouse](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-lakehouse).

Feature

You can now add existing Apache Parquet files from cloud-based storage, for example, Cloud Storage or Amazon S3, to an Apache Iceberg table in Lakehouse using the Dataflow job builder. This process registers the files without moving or rewriting the underlying data. For more information, see [Import Parquet files in storage into Lakehouse runtime catalog using Dataflow](https://docs.cloud.google.com/lakehouse/docs/blms-import-parquet).

Feature

You can now ingest data from external Apache Iceberg REST catalogs (IRC) directly into _Lakehouse_ tables using Dataflow's job builder UI without writing code. For more information, see [Import external Iceberg tables into Lakehouse runtime catalog using Dataflow](https://docs.cloud.google.com/lakehouse/docs/blms-import-iceberg).

## April 21, 2026

Announcement

_Lakehouse_ `gcloud` commands for Iceberg namespace and table operations are now Generally Available (GA). Note that the command group remains `gcloud biglake`.

Feature

_Lakehouse_ APIs now support Terraform configurations.

Feature

When querying tables in a catalog with credential vending enabled, BigQuery now uses vended credentials for storage access instead of end-user credentials.

For more information, see [Credential vending overview](https://docs.cloud.google.com/lakehouse/docs/credential-vending).

## April 20, 2026

Announcement

As of April 20, 2026, BigLake is now called _Lakehouse_. BigLake metastore is now called the _Lakehouse runtime catalog_. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake.

## April 16, 2026

Feature

Conversational analytics now supports querying _Lakehouse_ tables that connect to the Apache Iceberg REST catalog or are federated to an external catalog.

For more information, see [Query Lakehouse data with natural language](https://docs.cloud.google.com/lakehouse/docs/conversational-analytics).

## April 03, 2026

Feature

_Lakehouse_ supports Identity and Access Management (IAM) policies at the table level for Apache Iceberg tables (Preview).

For more information, see [Manage Lakehouse Apache Iceberg table ACLs](https://docs.cloud.google.com/lakehouse/docs/manage-tables-acl).

## March 31, 2026

Feature

The Lakehouse runtime catalog Iceberg REST catalogs now support `US` and `EU` Cloud Storage multi-region buckets.

When creating a catalog with a `US` or `EU` multi-region bucket, you can now specify the primary location (US or EU) to ensure the catalog is accessible from the corresponding BigQuery regions. For more information, see [Bucket and catalog regions](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint#bucket_and_catalog_regions).

## March 17, 2026

Feature

_The Lakehouse runtime catalog_ offers cross-region replication and disaster recovery (Preview) to improve your catalog's availability and resilience.

This feature improves your catalog's availability and resilience by ensuring continuous access, protecting against regional outages, preventing data loss, and enabling failover for Apache Iceberg tables that use the Apache Iceberg REST catalog. For more information, see [About cross-region replication and disaster recovery](https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
