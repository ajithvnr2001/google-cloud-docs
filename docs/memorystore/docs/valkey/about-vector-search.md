---
url: https://docs.cloud.google.com/memorystore/docs/valkey/about-vector-search/
title: Vector search for generative AI applications \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:23.384636+00:00
---

# Vector search for generative AI applications  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/about-vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Vector search for generative AI applications Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Memorystore for Valkey supports storing and querying vector data for generative AI applications, such as Retrieval Augmented Generation (RAG) and LangChain, by using vector search capabilities.

**Important:** If you [created your instance](https://docs.cloud.google.com/memorystore/docs/valkey/create-instances) before the feature launch date of September 13, 2024, then to use vector search, you must create another instance.

## Use vector search for generative AI with LangChain

Vector search on Memorystore for Valkey is compatible with the open-source LLM framework [LangChain](https://python.langchain.com/docs/get_started/introduction). Using vector search with LangChain lets you build solutions for the following use cases:

  * RAG
  * LLM cache
  * Recommendation engine
  * Semantic search
  * Image similarity search



## Benefits of vector search for generative AI in Memorystore for Valkey

The advantage of using Memorystore to store your generative AI data, compared to other Google Cloud databases is its speed. Vector search on Memorystore for Valkey leverages multi-threaded queries, resulting in high query throughput (QPS) at low latency.

## Approaches to using vector search for generative AI in Memorystore for Valkey

Memorystore also provides two distinct search approaches to help you find the right balance between speed and accuracy. The Hierarchical Navigable Small World (`HNSW`) option delivers fast, approximate results — ideal for large datasets where a close match is sufficient. If you require absolute precision, then the `FLAT` approach produces exact answers, though it might take slightly longer to process.

If you want to optimize your application for the fastest vector data read and write speeds, then Memorystore for Valkey is likely the best option for you.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
