---
url: https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search/
title: Vector search for generative AI applications \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:11:19.192383+00:00
---

# Vector search for generative AI applications  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/about-vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Vector search for generative AI applications Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how Memorystore for Redis supports storing and querying vector data for generative AI applications, such as Retrieval Augmented Generation (RAG) and LangChain, by using vector search capabilities.

**Important:** To use vector search, your instance must use Redis, version 7.2. To use this feature, either [create](https://docs.cloud.google.com/memorystore/docs/redis/create-manage-instances) or [upgrade](https://docs.cloud.google.com/memorystore/docs/redis/upgrade-redis-version) an instance so that it uses this version.

## Use vector search for generative AI with LangChain

Vector search on Memorystore for Redis is compatible with the open-source LLM framework [LangChain](https://python.langchain.com/docs/get_started/introduction). Using vector search with LangChain lets you build solutions for the following use cases:

  * RAG
  * LLM cache
  * Recommendation engine
  * Semantic search
  * Image similarity search



## Benefits of vector search for generative AI in Memorystore for Redis

The advantage of using Memorystore to store your generative AI data, compared to other Google Cloud databases is its speed. Vector search on Memorystore for Redis leverages multi-threaded queries, resulting in high query throughput (QPS) at low latency.

## Approaches to using vector search for generative AI in Memorystore for Redis

Memorystore also provides two distinct search approaches to help you find the right balance between speed and accuracy. The Hierarchical Navigable Small World (`HNSW`) option delivers fast, approximate results — ideal for large datasets where a close match is sufficient. If you require absolute precision, then the `FLAT` approach produces exact answers, though it might take slightly longer to process.

If you want to optimize your application for the fastest vector data read and write speeds, then Memorystore for Redis is likely the best option for you.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
