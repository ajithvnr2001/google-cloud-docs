---
url: https://docs.cloud.google.com/lakehouse/docs/lakehouse-basics/
title: How borderless Lakehouse works \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:19:41.508319+00:00
---

# How borderless Lakehouse works  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/lakehouse-basics/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  How borderless Lakehouse works Stay organized with collections  Save and categorize content based on your preferences. 

The technical architecture of _borderless Lakehouse_ supports interoperability between engines by centralizing metadata management and handling queries through specific paths.

## Architecture

Building Google Cloud's _Lakehouse_ consists of the following technical components:

  * **Storage:** Cloud Storage and BigQuery storage serve as the storage layer, with Apache Iceberg as the recommended open table format for high-performance, interoperable storage in Cloud Storage. With borderless Lakehouse, your data doesn't need to reside in Google Cloud. By setting up [cross-cloud connections](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access) (Preview) to supported remote catalogs, you can keep your data in other cloud storage systems, such as Amazon S3, and query it without migrating files or building ETL pipelines.

  * **Catalog:** The Lakehouse runtime catalog provides a single source of truth for managing metadata. It centralizes metadata discovery across multiple engines using various compatibility options, such as the Apache Iceberg REST catalog endpoint. Table registrations into the catalog automatically register entries into the business metadata knowledge catalog.

  * **Query engine:** BigQuery and open-source engines—including Apache Spark, Apache Flink, and Trino—interoperate seamlessly by connecting to the Lakehouse runtime catalog. Compute engines like Managed Service for Apache Spark use open-source Apache Spark with execution optimizations to help ensure workload portability and avoid vendor lock-in.

  * **Governance:** Knowledge Catalog provides centralized security, lineage, and governance policies across your entire lakehouse.

  * **Data writing and analytics tools:** Integrated engines and tools provide multiple paths for data ingestion and analysis, helping ensure consistent data access for both data scientists and analysts.




## Resource hierarchy

Google Cloud's Lakehouse organizes data using a hierarchy that aligns with Apache Iceberg standards and standard database concepts. This structure lets the Lakehouse runtime catalog map logical identities to physical storage paths. To interact with this resource hierarchy and connect your query engines to the catalog, you use specific endpoints, as described in the following list.

  1. **Lakehouse runtime catalog** : The top-level regional service resource in Google Cloud that hosts your metadata. To connect query engines to this service and manage underlying catalogs, you configure client applications using a specific catalog endpoint, such as the Apache Iceberg REST catalog endpoint.
  2. **Catalog** : A logical container within the runtime catalog service. In the Project/Catalog/Namespace/Table (P.C.N.T) naming structure, this represents the specific catalog instance you are querying.
  3. **Namespace** : A logical grouping of tables within a catalog. For users familiar with BigQuery, a namespace is functionally similar to a _dataset_.
  4. **Table** : The specific entity pointing to data in Cloud Storage. The table metadata contains the schema, partitioning information, and a pointer to the current table state through an Apache Iceberg `metadata.json` file.



#### Supported endpoints

The Lakehouse runtime catalog provides several endpoints to connect your data across Cloud Storage and BigQuery.

  * **Apache Iceberg REST catalog endpoint:** Provides a standard [REST interface](https://iceberg.apache.org/rest-catalog-spec/) for wide compatibility with open-source engines like Apache Spark, Apache Flink, and Trino. This is the recommended interface for new workloads and offers full read and write interoperability.

  * **Custom Apache Iceberg catalog for BigQuery endpoint:** Lets engines interoperate directly with the BigQuery catalog. This interface is used primarily for _Apache Iceberg tables_ managed by BigQuery and existing workloads transitioning to the _Lakehouse_ architecture.

  * **Apache Hive catalog endpoint (Preview):** Provides compatibility for open-source workloads that depend on the Apache Hive metastore (HMS) interface. This lets you run Apache Hive or Spark workloads against a fully managed metastore service on Google Cloud.




### Lakehouse runtime catalog

Within the resource hierarchy, the Lakehouse runtime catalog serves as the top-level regional metadata service in Google Cloud. It acts as the root container that hosts your individual catalog instances, centralizing metadata discovery across disparate query engines.

It implements the open-source [Apache Iceberg REST Catalog API](https://github.com/apache/iceberg/blob/main/open-api/rest-catalog-open-api.yaml) to manage namespaces and tables, and provides extensions specifically for catalog management.

For a deeper dive into the metastore service, including key capabilities, supported engines, endpoint configuration, and limitations, see [About the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs).

### Catalog

A catalog is a logical metastore container backed by Cloud Storage warehouse locations. In the `Project.Catalog.Namespace.Table` (P.C.N.T) naming structure, the catalog represents the unique metastore instance that connects your open table metadata with query engines.

Key characteristics of catalogs include the following:

  * **Storage association:** The relationship between a catalog and its underlying storage depends on the catalog type you configure.
  * **Regional replication:** A catalog's region automatically matches the underlying bucket's region.
  * **Access delegation:** Administrators can enable credential vending on the catalog to delegate access, letting short-lived credentials with reduced scope be autogenerated instead of granting users direct bucket permissions.



### Namespace

A namespace is a logical grouping of tables within a catalog, functioning similarly to a database, schema, or a BigQuery dataset. It provides a structure to organize and manage access controls for tables.

Key characteristics of namespaces include the following:

  * **Regionality:** When you create a namespace, it automatically uses the same region as its parent catalog.
  * **Location flexibility:** The options for specifying custom namespace locations are determined by the catalog's warehouse type.
  * **Nesting limitations:** Nested namespaces (sub-namespaces) are not supported.
  * **Security boundaries:** You can grant IAM roles at the namespace level to manage access to all tables contained within it.



### Tables

When building with Google Cloud's Lakehouse, you can choose from the following table types:

#### Supported by the Lakehouse runtime catalog

**Recommended**

  * **Apache Iceberg tables:** Apache Iceberg tables created from open-source engines and stored in Cloud Storage. These offer open compatibility and management through the Lakehouse runtime catalog REST endpoint. To ensure no two tables occupy the same location, custom table paths must be nested under the parent namespace path, and resulting table locations automatically receive a random string suffix to prevent conflicts.

#### Supported table formats

Apache Iceberg V2 tables (GA) and V3 tables (Preview) are supported. Iceberg V1 tables aren't supported. Before you use existing V1 tables with Lakehouse, you must upgrade them to a supported version. For more information, see [Upgrade Iceberg V1 tables to V2](https://docs.cloud.google.com/lakehouse/docs/lakehouse-iceberg-rest-catalog#upgrade-v1-to-v2).




#### Supported by BigQuery

  * **Apache Iceberg tables:** Apache Iceberg tables created and managed by BigQuery. The metadata for these tables is stored in the BigQuery catalog, and table data and physical metadata are stored in Cloud Storage.
  * **Native tables:** Tables fully managed by BigQuery that can be connected to the Lakehouse runtime catalog to let you interoperate with open-source engines.
  * **External tables:** Tables outside of the Lakehouse runtime catalog where data and metadata are self-managed. These support delegated access through connections for data stored in Cloud Storage, Amazon S3, or Azure Blob Storage.



For a detailed comparison of these options, see [Understand table types and capabilities](https://docs.cloud.google.com/lakehouse/docs/lakehouse-tables).

## Query processing sequence

When you submit a query to an Apache Iceberg table managed by Lakehouse, the request follows a specific path to enforce policies and retrieve metadata before data is processed.

  1. **Submission:** You submit a SQL query to a compatible engine such as Apache Spark, Trino, or BigQuery.
  2. **Metadata request:** The engine requests table metadata from the Lakehouse runtime catalog to identify the table and its metadata location.
  3. **Authorization:** If supported by the [endpoint you are using](https://docs.cloud.google.com/lakehouse/docs/lakehouse-basics#endpoints), the catalog validates the request against Identity and Access Management (IAM) and fine-grained security policies.
  4. **Metadata response:** The catalog returns the metadata. If credential vending is enabled, it also provides a short-lived token to help with secure storage access.
  5. **Data retrieval:** The engine uses the metadata and optional token to read data files directly from Cloud Storage.
  6. **Execution:** The engine processes the data and returns the results.



## Best practices

When architecting and operating a data lakehouse on Google Cloud, consider the following best practices:

  * **Adopt a medallion architecture:** Structure your data warehouse into progressive logical layers (bronze for raw ingestion, silver for cleansed and conformed data, and gold for curated business-level aggregations). Use BigQuery for the gold consumption layer to maximize query performance and concurrency.
  * **Use session templates for interactive workloads:** For exploratory analytics and notebook authoring, use session templates to standardize environment configurations across development teams and reduce repetitive setup.
  * **Assign custom batch identifiers:** When submitting non-interactive serverless Apache Spark batch workloads, assign custom batch and job names. This improves observability, which helps you filter and track job executions within Cloud Logging and the Google Cloud console.
  * **Enable diagnostic logging:** For complex data engineering pipelines, enable diagnostic bundles and help ensure driver and executor logs are retained to help with troubleshooting and supportability.



## What's next

  * For a deeper dive into the metastore service, see [About the Lakehouse runtime catalog](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs).
  * [Use the Lakehouse runtime catalog with Apache Spark, BigQuery and the Apache Iceberg REST catalog endpoint](https://docs.cloud.google.com/lakehouse/docs/use-lakehouse-metastore-iceberg-rest-catalog).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
