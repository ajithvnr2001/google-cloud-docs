---
url: https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint/
title: About the Apache Iceberg REST catalog endpoint \u00a0|\u00a0 Lakehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:26:01.296354+00:00
---

# About the Apache Iceberg REST catalog endpoint  |  Lakehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/about-iceberg-rest-catalog-endpoint/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  About the Apache Iceberg REST catalog endpoint Stay organized with collections  Save and categorize content based on your preferences. 

_Borderless Lakehouse_ manages metadata through the _Lakehouse runtime catalog_. When you use the _Apache Iceberg REST catalog_ endpoint, the system organizes data into a strict resource hierarchy. The catalog configuration determines the supported storage types and regional routing behaviors.

## Capabilities and compliance

The Lakehouse runtime catalog is built to integrate with Iceberg compliant query engines by supporting standard table formats and complying with open APIs.

### Supported table formats

Apache Iceberg V2 tables (GA) and V3 tables (Preview) are supported. Iceberg V1 tables aren't supported. Before you use existing V1 tables with the Apache Iceberg REST catalog endpoint, you must upgrade them to a supported version. For more information, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#upgrade-v1-to-v2).

### API compliance and REST operations

The _Lakehouse runtime catalog_ implements the open standard Apache Iceberg REST Catalog API. Client query engines interact with the catalog using standard REST catalog APIs. For more information, see [How Lakehouse implements the Apache Iceberg REST Catalog API](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs#rest-api-compliance).

## Resource hierarchy

The Apache Iceberg REST catalog endpoint uses a hierarchy of resources to organize your data. The following table provides a high-level look at these resources:

Resource | Description  
---|---  
Catalog | The top-level container, a catalog lets you organize namespaces and tables into logical groups by splitting them up into different catalogs. Each catalog is backed by designated warehouse storage locations (such as one or more Cloud Storage buckets) that store its underlying metadata and data files.  
Namespace | A logical grouping used to organize tables within a catalog, this functions like databases, schemas, or directories.  
Table | Tables contain definitions of rows and columns that can be queried.   
  
## Catalogs and storage locations

The configuration of a catalog determines how it operates and integrates with Google Cloud services. You can configure a multiple-bucket catalog (recommended) or a single-bucket catalog.

Both options support credential vending.

When configuring client query engines (such as Spark or Trino) to connect to the Apache Iceberg REST catalog endpoint, you specify the warehouse path based on the catalog type:

  * **Multiple-bucket catalog** : Set the warehouse path to `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`.
  * **Single-bucket catalog** : Set the warehouse path to `gs://CLOUD_STORAGE_BUCKET_NAME`.



### Multiple-bucket catalog (recommended)

This approach lets you name your catalog independently of any bucket name, and lets you configure multiple buckets for a single catalog. In the underlying API, this corresponds to the [`CATALOG_TYPE_BIGLAKE`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs#CatalogType) configuration.

**Considerations:**

  * **Client warehouse configuration (`bl://`)**: When configuring an Iceberg client to connect to a multiple-bucket catalog, specify the warehouse path using the `bl://` URI format: `bl://projects/PROJECT_ID/catalogs/CATALOG_ID`. The `bl://` format is used exclusively during client configuration to identify the catalog. When creating or configuring the catalog itself in Google Cloud, the storage locations (`default_location` and `restricted_locations`) are always specified as Cloud Storage paths (`gs://`).
  * **Maximum buckets** : You can specify a maximum of 15 buckets per catalog.
  * **Default location** : You provide a path to a bucket (`default_location`) or a subpath (such as `gs://my-bucket/path`) to act as the default storage location. All catalog resources (namespaces and tables) must be located under the specified path. For example, if you specify `gs://my-bucket/path`, you cannot host namespaces or tables under `gs://my-bucket/another/path`. For namespaces created without a specified location, the `default_location` is used.
  * **Restricted locations** : You can also provide an optional `restricted_locations` configuration for additional buckets or paths where namespaces and tables can be created. If you specify a subpath (such as `gs://my-bucket/path`), any resources created using that configuration must be under that path (for example, `gs://my-bucket/another/path` cannot host namespaces or tables).
  * **Geographic region group requirements** : Although buckets can be cross-project, cross-region, and have different configurations (such as single-region, dual-region, or multi-region), all Cloud Storage locations across the default location and restricted locations must be in the same geographic region group (such as the US, Europe, Canada, or Asia). For example, you can't configure a US multi-region bucket with a bucket in Europe or Canada.
  * **Multiple catalogs per bucket** : You can have multiple catalogs point to the same bucket (for example, using different default locations or restricted locations). However, this configuration is highly discouraged because it can lead to metadata conflicts, accidental data overwrites, or security issues like permission leakage.
  * **Namespaces** : allow specifying custom namespace locations, as long as they are under a path configured in the default or restricted locations. Note that tables created in these catalogs will have a random string suffix automatically appended to their physical paths to prevent conflicts (for example, `gs://{bucket_name}/{namespace_name}/{table_name}/{random_suffix}`). For more information, see [Table management and security rules](https://docs.cloud.google.com/lakehouse/docs/table-rules).



### Single-bucket catalog

This is the legacy approach where the catalog directly manages Apache Iceberg metadata and data files in a single Cloud Storage bucket (`gs://`) that you specify. In the underlying API, this corresponds to the [`CATALOG_TYPE_GCS_BUCKET`](https://docs.cloud.google.com/lakehouse/docs/reference/rest/v1/iceberg.v1.restcatalog.extensions.projects.catalogs#CatalogType) configuration.

For single-bucket catalogs, the catalog name is set to the name of your bucket.

For example, if you name your bucket `iceberg-bucket`, both your catalog and bucket share that name. Use this name when querying your catalog in BigQuery using P.C.N.T syntax, for example, `my-project.lakehouse-catalog-id.quickstart_namespace.quickstart_table`.

**Considerations:**

  * **Legacy catalog type limitations**. Using the legacy single-bucket configuration is highly discouraged for new projects. This configuration comes with several critical limitations:

    * **Catalog name** : Locked to the underlying Cloud Storage bucket name.
    * **Project** : Locked to the bucket's project (cross-project catalogs are not supported).
    * **Region** : Strictly derived from the bucket's location and cannot be customized.
    * **Storage** : Restricts your catalog to a single bucket (no restricted locations).
  * **Client warehouse configuration (`gs://`)**: When configuring an Iceberg client for a single-bucket catalog, specify the Cloud Storage bucket path (`gs://CLOUD_STORAGE_BUCKET_NAME`) as the warehouse location.

  * **One catalog per bucket restriction** : For this legacy catalog type, you can only have one catalog per bucket, and the catalog name must match the bucket name.

  * **Upgrade to multiple-bucket catalog (recommended)** : you can [upgrade an existing single-bucket catalog](https://docs.cloud.google.com/lakehouse/docs/update-catalog) to a multiple-bucket catalog (recommended). The upgraded catalog retains the original bucket's name. After that, you can associate multiple buckets with the catalog and configure restricted locations.




## Bucket and catalog regions

The region of a catalog endpoint in the Lakehouse runtime catalog is determined by the region of its underlying Cloud Storage bucket:

  * **Multiple-bucket catalog** : (recommended): The catalog region is derived from the bucket configured in `default_location`.
  * **Single-bucket catalog** : The catalog region is strictly derived from the bucket associated with the catalog and cannot be customized.



The mapped catalog region varies depending on the bucket's region type:

  * **Single-region** : The catalog region matches the bucket's region exactly.
  * **Dual-region** : The catalog region matches the bucket's dual-region (such as `ASIA1` or `NAM4`).
  * **Multi-region** : The catalog region is set to a specific regional location within the multi-region's geographic domain. By default, this might not align with common BigQuery multi-regions like `US` and `EU` (for example, a `US` multi-region bucket maps to `us-central1` or `us-east4`).



When BigQuery runs a query over tables in these catalogs, it routes the query to the catalog's primary region. If you query tables in a specific virtual region (such as `US` or `EU`) and the catalog metadata is not present in that location, the query fails.

### Primary regions for multi-regions

To allow BigQuery to query your catalog tables from the `US` or `EU` multi-region, specify `US` or `EU` as the primary region when you create the catalog.

You can specify a multi-region (`US` or `EU`) as the primary region in the following configurations:

If the `default_location` bucket is:

  * A `US` or `EU` multi-region bucket.
  * A single-region bucket within those multi-regions (such as `us-central1` or `europe-west4`).
  * A dual-region or custom dual-region bucket within those areas (such as `NAM4` or `EUR4`).



The primary replica is defined when you create the catalog, but you can dynamically perform a failover by calling `FailoverCatalog`. For more information, see [Create a catalog](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog).

To route requests directly to a specific region for data residency and sovereignty requirements, you can use regional endpoints (`biglake.LOCATION.rep.googleapis.com`). For more information, see [Lakehouse regional endpoints](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints).

## Querying catalogs from BigQuery

When querying Lakehouse runtime catalog tables from BigQuery, you use a four-part naming structure, often referred to as **P.C.N.T** :

  * **P** roject: The Google Cloud project ID that owns the catalog.
  * **C** atalog: The name of the Lakehouse runtime catalog.
  * **N** amespace: The Apache Iceberg namespace (equivalent to a BigQuery dataset).
  * **T** able: The name of the table.



For example, `my-project.lakehouse-catalog-id.my-namespace.my-table`.

## What's Next

  * [Set up the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/set-up-lakehouse-iceberg-rest-catalog)
  * [Use Lakehouse regional endpoints](https://docs.cloud.google.com/lakehouse/docs/regional-endpoints)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-15 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-15 UTC."],[],[]] 
