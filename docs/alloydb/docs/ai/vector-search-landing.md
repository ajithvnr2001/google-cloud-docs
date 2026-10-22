---
url: https://docs.cloud.google.com/alloydb/docs/ai/vector-search-landing/
title: Vector indexing overview \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:27:11.267618+00:00
---

# Vector indexing overview  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/vector-search-landing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Vector indexing overview Stay organized with collections  Save and categorize content based on your preferences. 

AlloyDB AI extends the open-source `pgvector` extension, providing compatibility with standard index types such as HNSW alongside Google's Scalable Nearest Neighbors (ScaNN) vector search index. Storing and indexing vector embeddings directly in AlloyDB for PostgreSQL lets you build generative AI, semantic search, and recommendation applications without moving your operational data or managing a separate vector database. 

![Visual overview of AlloyDB vector search](https://docs.cloud.google.com/static/alloydb/images/vector-search-card.png)

## Build faster, smarter AI applications

AlloyDB AI eliminates the complexity of managing a separate vector database. Keep operational data and embeddings in one place, and use built-in functions to generate batch embeddings ([Preview](https://cloud.google.com/products#product-launch-stages)) for large tables, scaling your AI pipeline from a single, secure source.

![RAG thumbnail](https://docs.cloud.google.com/static/alloydb/images/rag.png)

###  [ Retrieval-augmented generation (RAG) ](https://docs.cloud.google.com/alloydb/docs/ai/run-hybrid-vector-similarity-search)

Enhance LLM responses by using vector search to find and retrieve the most relevant, up-to-date context from your private data in AlloyDB, directly feeding it into the prompt to reduce hallucinations. 

![Semantic search thumbnail](https://docs.cloud.google.com/static/alloydb/images/semantic-search.png)

###  [ Semantic search ](https://docs.cloud.google.com/alloydb/docs/ai/run-vector-similarity-search)

Enable concept-based search by converting your data into vector embeddings. AlloyDB AI's fast vector queries then find items based on their semantic meaning, not just keyword matches. 

![Recommendation engine thumbnail](https://docs.cloud.google.com/static/alloydb/images/recommendation-engine.png)

###  [ Recommendation engines ](https://docs.cloud.google.com/alloydb/docs/ai/create-scann-index)

Power real-time personalization by using ultra-fast vector search to identify similar items or users (nearest neighbors) directly within your database, enabling dynamic and relevant recommendations. 

## ScaNN vector search performance

![Icon representing speed](https://docs.cloud.google.com/static/alloydb/images/speed-icon.svg)

###  Up to **10x faster** ScaNN index creation and filtered vector search than HNSW. 

![Icon representing memory efficiency](https://docs.cloud.google.com/static/alloydb/images/memory-icon.svg)

###  Uses **3x less memory** than HNSW. 

![Icon representing faster queries](https://docs.cloud.google.com/static/alloydb/images/search-icon.svg)

###  Up to **4x faster** vector search queries than HNSW. 

![Icon representing a filtered search](https://docs.cloud.google.com/static/alloydb/images/info-icon.svg)

###  Up to **10x faster** filtered vector search than HNSW. 

## Learn more

Explore our developer resources to build AI applications with AlloyDB's vector search capabilities.

Video 

###  [ AlloyDB AI: Hybrid search and multimodal capabilities ](https://www.youtube.com/watch?v=WYfHrwYaWjw)

Enhance retail product discovery with AlloyDB's semantic, hybrid, and multimodal search. 

Article 

###  [ ScaNN for AlloyDB whitepaper ](https://docs.cloud.google.com/alloydb/docs/ai/generate-sql-queries-natural-language)

A technical whitepaper on the architecture, algorithms, and performance of the ScaNN index in AlloyDB. 

Codelab 

###  [ Build and deploy a dynamic hybrid retail search with AlloyDB, Gemini and Cloud Run ](https://codelabs.developers.google.com/hybrid-search-on-cloudrun)

Learn how to perform hybrid search on Cloud Run, combining SQL, full-text, and vector search. 

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
