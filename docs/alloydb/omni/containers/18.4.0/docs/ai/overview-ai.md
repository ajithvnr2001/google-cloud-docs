---
url: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/overview-ai/
title: Build generative AI applications using AlloyDB AI \u00a0|\u00a0 AlloyDB Omni using containers: 18.4.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:56:56.427371+00:00
---

# Build generative AI applications using AlloyDB AI  |  AlloyDB Omni using containers: 18.4.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/overview-ai/

This page documents AlloyDB Omni version **18.4.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/overview)



Send feedback 

#  Build generative AI applications using AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.4.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/overview-ai)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/overview-ai)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/overview-ai)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/overview-ai)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/overview-ai)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/overview-ai)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/overview-ai)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/overview-ai)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/overview-ai)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/overview-ai)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/overview-ai)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/overview-ai)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/overview-ai)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/overview-ai)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/overview-ai)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/overview-ai)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/overview-ai)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/overview-ai)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/overview-ai)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/overview-ai)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/overview-ai)

AlloyDB AI is a suite of features included with AlloyDB for PostgreSQL and AlloyDB Omni that let you apply the semantic and predictive power of machine learning (ML) models to your data. This page provides an overview of the ML-powered AI functions that are available through AlloyDB. **Caution:** The `postgres_ann` extension is renamed to `alloydb_scann`. Before you upgrade to AlloyDB Omni version 15.7.0, you must drop any indexes created using the older `postgres_ann` version. Next, upgrade AlloyDB Omni, and then create the indexes again using the `alloydb_scann` extension. This applies only to AlloyDB Omni.

## Store, index, and query vectors

The stock [`pgvector` PostgreSQL extension](https://github.com/pgvector/pgvector?tab=readme-ov-file#indexing) is customized for AlloyDB, and referred to as `vector`. It supports storing generated embeddings in a vector column. The extension also adds support for scalar quantization feature to create `IVF` indexes. You can also create an `IVFFlat` index or `HNSW` index that are available with stock `pgvector`.

For more information about storing vectors, see [Store vectors](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/store-embeddings).

In addition to the customized `vector` extension, AlloyDB includes the `alloydb_scann` extension that implements a highly efficient nearest-neighbor index powered by the [ScaNN algorithm](https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md).

**Note:** The `alloydb_scann` extension can be used with PostgreSQL 14 and later compatible databases.

For more information about creating indexes and querying vectors, see [Create indexes and query vectors](/alloydb/omni/containers/18.4.0/docs/ai/store-index-query-vectors). 

## Tune your vector query performance

You can tune your indexes for a balance between query-per-second (QPS) and recall with your queries. For more information about tuning your indexes, see [Tune vector query performance](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/tune-indexes).

## Generate embeddings and text predictions

AlloyDB AI extends PostgreSQL syntax with two functions for querying models using the `google_ml_integration` extension:

  * [Invoke predictions](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/invoke-predictions) to call a model using SQL within a transaction.

  * [Generate embeddings](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/work-with-embeddings) to have an LLM translate text prompts into numerical vectors.

You can use the [`embedding()` function](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/work-with-embeddings) to query Vertex AI models, while the [`google_ml.embedding()` function](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/model-endpoint-overview) can be used to query registered Vertex AI, hosted, and third-party models.

You can then apply these vector embeddings as input to `pgvector` functions. This includes methods to compare and sort samples of text according to their relative semantic distance.


**Note:** To generate embeddings for custom hosted or third-party AI models, see [Register and call remote AI models in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/model-endpoint-overview). This feature is available in [Preview](https://cloud.google.com/products#product-launch-stages).

### Use models in the cloud with Vertex AI

You can [configure AlloyDB Omni to work with Vertex AI](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install-with-alloydb-ai).

This gives your applications the following benefits:

  * Your applications can invoke predictions using any model stored in the [Vertex AI Model Garden](https://cloud.google.com/model-garden) that they have access to.

  * Your applications can generate embeddings using [the `text-embedding` English models](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/models/text-embeddings-api) LLM.




## What's next

  * [Install AlloyDB Omni with AlloyDB AI](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/install-with-alloydb-ai).

  * [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/store-index-query-vectors).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
