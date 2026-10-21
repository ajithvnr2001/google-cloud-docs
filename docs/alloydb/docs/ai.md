---
url: https://docs.cloud.google.com/alloydb/docs/ai/
title: Build generative AI applications using AlloyDB AI \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T20:46:28.244017+00:00
---

# Build generative AI applications using AlloyDB AI  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Build generative AI applications using AlloyDB AI Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB AI provides an integrated suite of AI and machine learning (ML) capabilities in AlloyDB for PostgreSQL that lets you build generative AI applications using your operational database data. You can run high-speed vector similarity searches, translate natural language questions into SQL queries, and invoke foundation models from Gemini Enterprise Agent Platform, OpenAI, and Anthropic directly from SQL.

To simplify the process of building AI applications, AlloyDB provides the following extensions:

  * **vector** extension: the standard [`pgvector` PostgreSQL extension](https://github.com/pgvector/pgvector?tab=readme-ov-file#indexing) is customized for AlloyDB, and referred to as `vector`. It supports storing generated embeddings in a vector column. The extension also adds support for scalar quantization features to create `IVF` indexes. You can also create an `IVFFlat` index or `HNSW` index that are available with stock `pgvector`.

  * **alloydb_scann** extension: the [`alloydb_scann` extension](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index#create-index) implements a highly efficient nearest-neighbor index powered by the [ScaNN algorithm](https://github.com/google-research/google-research/blob/master/scann/docs/algorithms.md).

You can use the `alloydb_scann` extension with PostgreSQL 14, 15, 16, and 17.

  * **google_columnar_engine** extension: ScaNN index can be loaded into the columnar engine for further accelerating the vector search.

  * **google_ml_integration** extension: the `google_ml_integration` extension provides AI functions for generating embeddings, semantic ranking, and implementing AI-based filters, joins and text generation/summarization. This extension also provides functions to register metadata for AI models. The registered metadata is then used to invoke predictions from these models.

  * **alloydb_ai_nl** extension: the `alloydb_ai_nl` extension enables developers to build applications that accurately and securely answer end user natural language questions about data in the AlloyDB database. This makes the data accessible to users who might not be proficient in writing SQL.




The following are some use cases that these extensions enable:

  * [Vector search](https://docs.cloud.google.com/alloydb/docs/ai/run-vector-similarity-search): use AlloyDB to store vector embeddings and perform highly efficient similarity searches. You can generate a highly efficient nearest-neighbor index powered by the ScaNN algorithm.

  * [Perform intelligent SQL queries using AlloyDB AI functions](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators): use AI directly within your SQL queries. This allows you to re-rank search results for higher relevance, integrate natural language into your SQL queries, and generate multimodal embeddings for vector search.

  * [Call models using model endpoints](https://docs.cloud.google.com/alloydb/docs/ai/model-endpoint-overview): register AI models as model endpoints and call the endpoints from within AlloyDB to generate embeddings, invoke predictions, or perform similarity searches.

  * [Generate embeddings](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings) and [invoke predictions](https://docs.cloud.google.com/alloydb/docs/ai/invoke-predictions): use Gemini Enterprise Agent Platform text embedding models or registered model endpoints to generate text or multimodal embeddings.

  * [Generate SQL statements from natural language](https://docs.cloud.google.com/alloydb/docs/ai/natural-language-overview): add natural language capabilities to your application, and interact with AlloyDB by asking questions in natural language. The natural language questions are then processed by AlloyDB AI to automatically generate an accurate SQL query that retrieve the answer.




## What's next

  * [Perform vector search tutorial](https://docs.cloud.google.com/alloydb/docs/ai/perform-vector-search)

  * [Integrate AlloyDB with Agent Platform](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).

  * [Create a ScaNN index](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
