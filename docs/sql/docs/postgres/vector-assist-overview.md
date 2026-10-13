---
url: https://docs.cloud.google.com/sql/docs/postgres/vector-assist-overview/
title: Vector assist overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:25:21.456127+00:00
---

# Vector assist overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/vector-assist-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Vector assist overview Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

**Preview — Vector assist**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). You can process personal data for this feature as outlined in the [Cloud Data Processing Addendum](https://docs.cloud.google.com/terms/data-processing-addendum), subject to the obligations and restrictions described in the agreement under which you access Google Cloud. Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Warning:** Vector assist ([Preview](https://cloud.google.com/products)) is temporarily disabled for all Cloud SQL for PostgreSQL instances.

Vector assist is a Cloud SQL for PostgreSQL extension that simplifies the deployment and management of your Cloud SQL vector workloads. It provides a declarative SQL framework that helps you set up production-ready vector search capabilities, such as embedding generation, query optimization, and index creation. This framework reduces the complexity of vector workloads by:

  * **Simplifying intent declaration** : requirements (such as table, text column, or target recall) are declared using SQL functions.
  * **Automating best practices** : generates optimized SQL commands, also known as recommendations, to set up your vector workload using your defined vector specification and an optimized auto-tuning algorithm that computes optimal index configuration.
  * **Providing transparency and control** : provides clear explanations for each recommendation when automating tasks that let you review, modify, and apply recommendations at your pace.
  * **Enabling rapid prototyping** : lets you quickly deploy a well-tuned vector search setup, reducing the time from concept to production.
  * **Focusing on ease-of-use** : simplifies the complexity of semantic search, bridging the gap between business and engineering requirements.



With vector assist, you can build end-to-end applications with semantic search features with simplified setup.

## How vector assist works

Using vector assist requires you to define your vector specifications. The framework uses these vector specifications, also known as the vector spec, to generate the steps required to create a vector index. Vector assist outputs the steps required to deploy your vector workload as recommendations. Each time you modify your vector spec, vector assist regenerates the recommendations.

Once you generate the vector index using these recommended steps, you can use vector assist to generate optimized search queries.

### Vector assist specification

Setting up your vector index specification, or _vector spec_ , is the first step in using vector assist. A vector spec is an object where you define the intent and requirements for your vector workload. It includes all necessary information, including:

  * The tables and relevant columns (text or vector)
  * Embedding model preferences (if using embedding generation)
  * Preferred index type, such as [`HNSW`](https://en.wikipedia.org/wiki/Hierarchical_navigable_small_world) or [`IVFFlat`](https://github.com/pgvector/pgvector?tab=readme-ov-file#ivfflat).
  * Target recall for search queries
  * Memory limitations or other performance constraints

**Note:** If you define the `target_recall` specification in your vector spec and vector assist is unable to build an index on a given dataset and configuration to achieve the specified `target_recall`, it returns configurations that build a vector workload with the best possible `target_recall`. This might fall below the user-defined `target_recall`.

You define the vector spec using the [`vector_assist.define_spec`](https://docs.cloud.google.com/sql/docs/postgres/vector-assist-reference#define-spec) function, and you can modify it at any time. The system assigns each specification a unique ID and stores it in a table called `vector_assist.vector_specs`.

Vector assist infers the specification inputs and an optimized auto-tuning algorithm that computes optimal index configuration.. Although vector assist uses these values to simplify the development process, you can still customize them to match your preferences.

### Vector assist recommendations

After you define the vector spec, vector assist processes your input and generates recommendations. These recommendations are an ordered list of useful steps, typically SQL commands, that you must execute to deploy your vector workload per your specifications. Each recommendation includes:

  * The SQL query to run.
  * A detailed explanation of what the query does and why it's recommended.
  * Information about potential trade-offs or costs, such as estimated index size or build time.



Vector assist stores recommendations in a table called `vector_assist.recommendation`, and you can review, modify, and apply them individually, or as a whole.

Each time you modify the vector spec for your workload, vector assist regenerates the recommendations to comply with the updated specifications.

## Limitations

When using vector assist with your Cloud SQL for PostgreSQL instances, consider the following limitations:

  * Vector assist only supports PostgreSQL versions 12 and later.
  * Although vector assist supports all `pgvector` versions, we recommend using the most recent version for optimal performance and feature support. For more information, see the [`pgvector` changelog](https://github.com/pgvector/pgvector/blob/master/CHANGELOG.md#080-2024-10-30).
  * If your instance uses the `google_ml_integration` extension to generate embeddings, then its restrictions also apply when you use vector assist. For more information, see [Model endpoint management overview](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-overview).
  * Vector assist only supports `HNSW` and `IVFFlat` index types.
  * Vector assist only supports text embedding models for auto-generating embeddings and uses the `text_column_name` as the input parameter. If your vector workload requires a multimodal embedding model, use the `google_ml_integration` extension, or another extension to manually generate these embeddings before using vector assist to enable semantic search on these embeddings.



## What's next

  * [Use vector assist](https://docs.cloud.google.com/sql/docs/postgres/use-vector-assist)
  * [Vector assist reference](https://docs.cloud.google.com/sql/docs/postgres/vector-assist-reference)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
