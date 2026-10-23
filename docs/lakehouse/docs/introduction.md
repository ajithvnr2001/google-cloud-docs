---
url: https://docs.cloud.google.com/lakehouse/docs/introduction/
title: What is borderless Lakehouse? \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:34:21.693287+00:00
---

# What is borderless Lakehouse?  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/lakehouse/docs/introduction/

As of April 20th, 2026, BigLake is now called Lakehouse. BigLake metastore is now called the Lakehouse runtime catalog. Lakehouse APIs, client libraries, CLI commands, and IAM names remain unchanged and still reference BigLake. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Lakehouse ](https://docs.cloud.google.com/lakehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/lakehouse/docs/introduction)



Send feedback 

#  What is borderless Lakehouse? Stay organized with collections  Save and categorize content based on your preferences. 

_Borderless Lakehouse_ is a high-performance storage engine designed for building open data lakehouses. By integrating the Apache Iceberg open table format with fully managed, enterprise-grade storage on Google Cloud, it provides a unified interface for advanced analytics and AI.

To manage open table metadata, Lakehouse uses the [_Lakehouse runtime catalog_](https://docs.cloud.google.com/lakehouse/docs/about-lakehouse-catalogs). This fully managed, serverless metadata service provides a single source of truth across disparate systems, centralizing discovery and removing the need to synchronize metadata between different repositories.

By decoupling storage from compute, Google Cloud's _Lakehouse_ ensures seamless interoperability across analytical and transactional systems. This architecture allows multiple engines—including Apache Spark, Apache Flink, Apache Hive, Trino, and BigQuery—to access a single source of truth, eliminating data duplication and ensuring consistent insights.

## Key benefits

  * **Serverless architecture:** Google Cloud's Lakehouse eliminates the need for server or cluster management, reducing operational overhead and automatically scaling based on demand. For compute workloads, serverless batch and interactive sessions remove resource contention between jobs and automate infrastructure maintenance.
  * **Unified data management and governance:** Integration with [Knowledge Catalog](https://docs.cloud.google.com/dataplex/docs/introduction) ensures central definition and enforcement of governance policies across multiple engines, and enables semantic search, data lineage, and quality checks.
  * **Storage extensions:** Google Cloud's Lakehouse extends Cloud Storage management capabilities to include features such as Autoclass tiering and customer-managed encryption keys (CMEK).
  * **Fully managed experience:** When integrated with BigQuery, Google Cloud's Lakehouse provides a fully managed analytics and AI experience.
  * **High availability and disaster recovery:** Google Cloud's Lakehouse offers options for cross-region replication and disaster recovery ([Preview](https://docs.cloud.google.com/lakehouse/docs/about-managed-disaster-recovery)) to support high availability of your data.



## Use cases

  * **Open lakehouse:** Use Cloud Storage as the storage layer, and Google Cloud's Lakehouse provides the management and governance interface for Apache Iceberg data.
  * **Analytical and transactional integration:** Access analytical Apache Iceberg tables directly within AlloyDB for PostgreSQL ([Preview](https://docs.cloud.google.com/alloydb/docs/bigquery-view-alloydb-overview)) to combine analytical data with transactional workloads.
  * **Unified access:** Let different engines (Apache Spark, Apache Flink, BigQuery) interact with the same Apache Iceberg tables with consistent metadata.
  * **Cross-cloud analytics and AI:** Access cross-cloud data ([Preview](https://docs.cloud.google.com/lakehouse/docs/about-cross-cloud-data-access)) to synchronize metadata from other cloud providers, allowing you to query data with BigQuery or external open source engines through the Apache Iceberg REST catalog endpoint, all without migrating the data.
  * **Public dataset exploration:** Easily query high-quality public datasets using the Apache Iceberg REST catalog endpoint without managing infrastructure.
  * **Hive Metastore:** Connect open-source engines such as Apache Spark and Apache Hive to the Lakehouse runtime catalog using the [Hive catalog](https://docs.cloud.google.com/lakehouse/docs/about-spark-hive-metastore). This eliminates the operational overhead of maintaining a self-hosted Hive Metastore (HMS) while enabling seamless data sharing and direct table queries in BigQuery.



## Interfaces and tools

You can interact with Google Cloud's Lakehouse resources using the following tools:

  * **Google Cloud console** : Use the console to create catalogs, view catalog properties, view audit logs, and configure permissions.
  * **BigQuery SQL:** Use standard SQL DDL (Data Definition Language) to create and manage Apache Iceberg tables and external tables integrated with the Lakehouse runtime catalog.
  * **Open source engines:** Use engines such as Apache Spark, Apache Flink, and Apache Hive with the Lakehouse runtime catalog to read and write data.
  * **IDEs and notebooks:** Use interactive Apache Spark notebooks and IDE extensions, such as the Data Agent Kit (DAK) extension for VS Code, to authenticate to Google Cloud, author code interactively, and manage notebook sessions directly within your development environment.
  * **Orchestration and MLOps tools:** Integrate serverless batch pipelines and catalog operations with orchestration workflows using Managed Service for Apache Airflow (formerly Cloud Composer) and Kubeflow Pipelines in Vertex AI.
  * **Lakehouse runtime catalog API:** Use the Apache Iceberg REST catalog endpoint to interact with the service using tools that are compatible with the open Apache Iceberg REST specification.
  * **Apache Iceberg table support:** Apache Iceberg V2 tables (General Availability) and V3 tables (Preview) are supported. Iceberg V1 tables aren't supported.



## What's next

  * Understand the architecture of [Google Cloud's borderless Lakehouse](https://docs.cloud.google.com/lakehouse/docs/lakehouse-basics).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
