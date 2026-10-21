---
url: https://docs.cloud.google.com/lakehouse/docs/about-custom-iceberg-catalog-endpoint/
title: About the custom Apache Iceberg catalog for BigQuery endpoint \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-19T05:47:10.946839+00:00
---

# About the custom Apache Iceberg catalog for BigQuery endpoint  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/about-custom-iceberg-catalog-endpoint/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  About the custom Apache Iceberg catalog for BigQuery endpoint Stay organized with collections  Save and categorize content based on your preferences. 

The _custom Apache Iceberg catalog for BigQuery_ endpoint connects open source query engines like Apache Spark and Apache Flink to the _Lakehouse runtime catalog_. By integrating a custom catalog plugin (`BigQueryMetastoreCatalog`), this endpoint lets you manage and query Apache Iceberg table metadata directly through BigQuery while storing data and metadata files in Cloud Storage.

**Note:** The custom Apache Iceberg catalog for BigQuery is a legacy integration option. If you're building new workloads, we recommend using the [Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint), which implements the open standard Apache Iceberg REST Catalog API, supports multiple-bucket catalogs, and offers features such as [credential vending](https://docs.cloud.google.com/lakehouse/docs/credential-vending).

## How the custom Iceberg catalog works

The custom Apache Iceberg catalog uses a custom catalog implementation (`org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog`) provided in a JAR library. When your compute workloads run on Managed Service for Apache Spark, the engine uses this plugin to interact with BigQuery as the metadata store for your Apache Iceberg tables.

The workflow operates as follows:

  1. **Catalog implementation:** Query engines load the BigQuery Metastore catalog JAR and configure Spark session catalog properties to use `org.apache.iceberg.gcp.bigquery.BigQueryMetastoreCatalog`.
  2. **Metadata management:** When you create or modify tables using Spark SQL or DataFrame APIs, the plugin stores dataset and table definitions in BigQuery.
  3. **Data storage:** Apache Iceberg metadata files (`metadata.json`, manifest lists, manifests) and data files (such as Parquet files) are stored directly in your specified Cloud Storage warehouse path.
  4. **Cross-engine access:** Because metadata is registered with BigQuery, you can query tables both from open source engines like Spark and directly from BigQuery.



## Resource hierarchy

The custom Apache Iceberg catalog for BigQuery endpoint organizes metadata into the following hierarchy:

Resource | Description  
---|---  
Project | The Google Cloud project that contains your BigQuery resources and Cloud Storage warehouse storage.  
Namespace (Dataset) | A BigQuery dataset configured to act as an Iceberg namespace, defining the default Cloud Storage location for tables created within it.  
Table | An Apache Iceberg table whose schema, snapshots, and metadata pointers are tracked in BigQuery and whose data files reside in Cloud Storage.  
  
## Compare custom Iceberg catalogs and Iceberg REST catalogs

The following table summarizes key differences between the custom Apache Iceberg catalog for BigQuery endpoint and the Apache Iceberg REST catalog endpoint:

Feature | Custom Iceberg catalog for BigQuery | Apache Iceberg REST catalog endpoint (Recommended)  
---|---|---  
**Catalog API standard** | Custom plugin (`BigQueryMetastoreCatalog`) | Open standard Apache Iceberg REST Catalog API  
**Catalog hierarchy** | Project > BigQuery Dataset > Table | Project > Catalog > Namespace > Table (P.C.N.T)  
**Storage configuration** | Cloud Storage paths specified per dataset or table | Multiple-bucket or single-bucket catalogs  
**Credential vending** | Not supported (uses direct IAM credentials) | Supported (vends short-lived storage access tokens)  
**Disaster recovery** | Not supported | Supported (cross-region replication and failover)  
**Recommended for** | Existing deployments and workflows | New workloads and standard Iceberg REST client integrations  
  
## What's next

  * [Configure the runtime catalog using Apache Iceberg 1.10 and higher](https://docs.cloud.google.com/lakehouse/docs/configure-lakehouse-catalog-iceberg-1-10).
  * [Configure the runtime catalog using Apache Iceberg 1.9 and lower](https://docs.cloud.google.com/lakehouse/docs/configure-lakehouse-catalog-iceberg-1-9).
  * [Create and manage catalog resources](https://docs.cloud.google.com/lakehouse/docs/manage-lakehouse-catalog-resources).
  * [Use the runtime catalog with BigQuery tables](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-tables).
  * [Use Apache Spark stored procedures](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-stored-procedures).
  * [Customize additional catalog features](https://docs.cloud.google.com/lakehouse/docs/lakehouse-catalog-features).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-17 UTC."],[],[]] 
