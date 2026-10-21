---
url: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/release-notes/
title: AlloyDB Omni (RPM) version 18.1.0 release notes \u00a0|\u00a0 AlloyDB Omni using RPM: 18.1.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T01:34:05.976430+00:00
---

# AlloyDB Omni (RPM) version 18.1.0 release notes  |  AlloyDB Omni using RPM: 18.1.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/release-notes/

This page documents AlloyDB Omni version **18.1.0** using the **RPM** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM: 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/overview)
  * [ Resources ](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/resources)



Send feedback 

#  AlloyDB Omni (RPM) version 18.1.0 release notes Stay organized with collections  Save and categorize content based on your preferences. 

This page contains release notes for features and updates to AlloyDB Omni. 

You can see the latest product updates for all of Google Cloud on the [ Google Cloud](https://docs.cloud.google.com/release-notes) page, browse and filter all release notes in the [Google Cloud console](https://console.cloud.google.com/release-notes), or programmatically access release notes in [BigQuery](https://console.cloud.google.com/bigquery?p=bigquery-public-data&d=google_cloud_release_notes&t=release_notes&page=table). 

To get the latest product updates delivered to you, add the URL of this page to your [feed reader](https://wikipedia.org/wiki/Comparison_of_feed_aggregators), or add the [feed URL](https://docs.cloud.google.com/feeds/alloydbomni-release-notes.xml) directly. 

## September 08, 2026

Announcement

AlloyDB Omni using RPM version 18.3.0 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Version 18.3.0 includes the following features and changes:

  * AlloyDB Omni includes support for [PostgreSQL version 18.3](https://www.postgresql.org/docs/release/18.3/).
  * [Transparent data encryption](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/transparent-data-encryption-omni) generally available (GA) and includes the following features:

    * Integration with the columnar engine
    * Integration with the ultra fast cache
    * Performance improvements

For more information, see [Transparent data encryption for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/transparent-data-encryption-omni).




## August 17, 2026

Change

Updated the [Database version policies](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/db-version-policies) to reflect support for version 18.3.0.

## July 07, 2026

Feature

AlloyDB Omni using RPM now supports the following features:

  * AlloyDB AI: full support for AlloyDB AI features is now available, including [natural language queries](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/generate-sql-queries-natural-language), [adaptive filtering](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/adaptive-filtering), [vector index maintenance](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/maintain-vector-indexes), and [online predictions](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/ai/invoke-predictions). Natural language queries and adaptive filtering are in [Preview](https://cloud.google.com/products#product-launch-stages).
  * Logical replication: use the pglogical extension to replicate data between AlloyDB Omni and other PostgreSQL-compatible databases. For more information, see [About the `pglogical` extension](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/about-pglogical).
  * Columnar engine: configure, monitor, and tune the AlloyDB Omni columnar engine to accelerate analytical queries. For more information, see [Columnar engine overview](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/columnar-engine/overview).
  * Performance: run [performance tests](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-testing) and [interpret those results](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/interpret-results), and improve AlloyDB Omni performance using [performance tuning parameters](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/performance-tuning-parameters).



## June 18, 2026

Feature

AlloyDB Omni documentation now includes documentation for the following AlloyDB AI features available in [GA](https://cloud.google.com/products#product-launch-stages):

  * [Auto vector embeddings](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/generate-manage-auto-embeddings-for-tables) automate the lifecycle of vector embeddings for large datasets, keeping them in sync with transactional data using real-time or batch updates. This feature includes a bulk mode that performs refreshes and migrations up to 130x faster than row-by-row processing."

  * [AI functions](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/evaluate-semantic-queries-ai-operators) integrate LLMs like Gemini to bring world knowledge to your AlloyDB data and incorporate advanced semantic search and ranking capabilities directly into your SQL workflows.

  * Use array-based AI functions to improve the efficiency of large-scale AI operations by enabling batch processing of natural language prompts in your SQL queries. For more information, see [Perform intelligent SQL queries using AI functions](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/evaluate-semantic-queries-ai-operators).




Feature

AlloyDB Omni documentation includes documentation for the following AlloyDB AI features, which are available in [Preview](https://cloud.google.com/products#product-launch-stages):

AlloyDB Omni documentation includes documentation for the following AlloyDB AI features, which are available in [Preview](https://cloud.google.com/products#product-launch-stages):

  * The AlloyDB columnar engine provides a read-optimized, in-memory cache for HNSW indexes, increasing the number of queries per second (QPS) that your database can handle for vector search workloads. For more information, see [Accelerate vector search with the columnar engine](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/accelerate-with-ce).
  * The sentiment analysis and summarization functions let you process and analyze unstructured data in your database. For more information, see [Analyze text sentiment](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/analyze-sentiment) and [Summarize content](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/summarize-content).
  * AlloyDB supports Vector assist, an AlloyDB extension that simplifies the deployment and management of your AlloyDB vector workloads. For more information, see [Vector assist overview](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/vector-assist-overview).
  * You can defer ScaNN index creation on an empty table or a table with insufficient rows until the table has sufficient data. For more information, see [Create a ScaNN index](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/create-scann-index).
  * The alloydb_scann extension now supports four-level tree indexes, providing support for tables with up to 10 billion vector rows. For more information, see [Four-level ScaNN tree indexes](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/create-scann-index#create-scann-index-manual).



## May 27, 2026

Announcement

AlloyDB Omni using RPM version 18.1.1 is generally available ([GA](https://cloud.google.com/products#product-launch-stages)). Version 18.1.1 includes the following features and changes:

  * AlloyDB Omni supports PostgreSQL version [18.1](https://www.postgresql.org/docs/release/18.1/) in [GA](https://cloud.google.com/products#product-launch-stages).

  * Adds support for Transparent Data Encryption (TDE) ([Preview](https://cloud.google.com/products#product-launch-stages)), enabling at-rest encryption for database clusters. This is available beginning with AlloyDB Omni using RPM version 18.1.1. For more information, see [Transparent Data Encryption for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.1/docs/transparent-data-encryption-omni).

  * Reduced the RPM bundle size resulting in faster download times and improved deployment efficiency.




## April 22, 2026

Change

The naming conventions for AlloyDB Omni deployment options are updated to more accurately reflect their respective installation and orchestration methods.  
The following table summarizes the primary name changes:

**Original name** |  **New name**  
---|---  
AlloyDB Omni for containers |  AlloyDB Omni using containers  
AlloyDB Omni for Kubernetes |  AlloyDB Omni using the container orchestrator  
AlloyDB Omni for Linux |  AlloyDB Omni using RPM  
Red Hat RPM orchestrator |  AlloyDB Omni using the RPM orchestrator  
  
This update clarifies the distinction between AlloyDB Omni deployment environments (such as Kubernetes or standalone Linux) and the packaging and orchestration technologies used to manage them. For more information, see [Choose your deployment environment](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment).

## April 07, 2026

Announcement

AlloyDB Omni version 18.1.0 is available in [Preview](https://cloud.google.com/products#product-launch-stages). Version 18.1.0 is available as a Docker image and as an RPM package for Linux. To get started, [submit this form to request access](https://forms.gle/zxuHekMtV67Bw9Av9).

Version 18.1.0 includes the following features and changes:

  * AlloyDB Omni supports PostgreSQL version [18.1](https://www.postgresql.org/docs/release/18.1/) in [Preview](https://cloud.google.com/products#product-launch-stages).

  * To automate the process of vacuuming and collectively update the table statistics, AlloyDB Omni supports adaptive autovacuum. For more information, see [Configure adaptive autovacuum](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/adaptive-autovacuum).

  * AlloyDB AI lets you query remote ML models using the `google_ml_integration` extension to work with online predictions and text embeddings generated from ML models. For more information, see [Install AlloyDB Omni with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-with-alloydb-ai).

  * Connect your AlloyDB Omni instance to agents that support the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/docs/getting-started/intro), which help you with development workflows. For more information, see [Use AlloyDB Omni with MCP, Gemini CLI, and other agents](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/connect-ide-using-mcp-toolbox).

  * Build LLM-powered applications using LlamaIndex. For more information, see [Build LLM-powered applications using LlamaIndex](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/build-llm-apps-using-llamaindex).

  * Generate vector embeddings using an LLM hosted by Vertex AI that translates a text string into an embedding, which is the model's representation of the given text's semantic meaning as a numeric vector. For more information, see [Generate embeddings](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/work-with-embeddings).

  * Set up, configure, and generate SQL statements using AlloyDB AI natural language, which lets you create user-facing generative AI applications using natural language to query databases. For more information, see [Generate SQL queries from natural language](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/ai/generate-sql-queries-natural-language).

  * Protect your data by configuring AlloyDB Omni to work with Barman or pgBackRest, which are open-source database backup servers. For more information, see [Set up Barman for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/install-configure-barman) and [Set up pgBackRest for AlloyDB Omni on Linux](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/set-up-pgbackrest).

  * Parameterized secure views provide application data security and row access control using SQL views. This helps ensure that application users can view only the data that they're supposed to access. For more information, see [Parameterized secure views overview](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/parameterized-secure-views-overview).

  * Set up a high availability configuration for AlloyDB Omni. This only covers creating a new AlloyDB Omni instance in a high availability configuration. For more information, see [Create a high availability setup](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/high-availability/setup). Then, [Test your high availability setup](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/high-availability/test).

  * Use the AlloyDB Omni monitor to manage AlloyDB Omni user roles, monitor the activity of your AlloyDB Omni server, and update or remove your AlloyDB Omni installation. For more information, see [Manage and monitor AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/linux/18.1.0/docs/manage).

  * AlloyDB Omni only supports the `io_method` of worker and sync mode, with worker as default.




## December 16, 2025

Announcement

AlloyDB Omni for Linux is now available in [Preview](https://cloud.google.com/products#product-launch-stages) with AlloyDB Omni version 17.5.0. AlloyDB Omni is a downloadable, self-managed version of AlloyDB for PostgreSQL. AlloyDB Omni for Linux is suitable for deployment in non-containerized environments such as virtual machines or on bare metal. Available as an RPM package, you can [install](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/available-download-install-options) AlloyDB Omni directly on Red Hat Enterprise Linux (RHEL) 9 and Rocky Linux 9.

AlloyDB Omni for Linux is well suited for modernizing legacy applications, edge computing scenarios, and development environments where you need a powerful database that mirrors the managed AlloyDB service. For more information, see the [AlloyDB Omni for Linux overview](https://docs.cloud.google.com/alloydb/omni/linux/current/docs/overview).

To get started with this deployment model, [submit this form to request access](https://forms.gle/zxuHekMtV67Bw9Av9).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
