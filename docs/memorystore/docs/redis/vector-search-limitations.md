---
url: https://docs.cloud.google.com/memorystore/docs/redis/vector-search-limitations/
title: Features and limitations \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:54:43.587218+00:00
---

# Features and limitations  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/vector-search-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  Features and limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details about vector search features and limitations.

## Availability

Vector search is available on standalone versions from 7.2 across all tiers and all the supported regions.

## Index Restrictions

The following outlines the limitations of the index:

  * The maximum number of attributes in an index cannot exceed 10.
  * A vector's dimension cannot exceed 32,768.
  * The M value for HNSW must not go beyond 2M.
  * The EF Construct value for HNSW must not exceed 4096.
  * The EF Runtime value for HNSW must also not surpass 4096.



## Scaling

Vector search facilitates vertical scaling through the integration of thread pools dedicated to executing vector search operations.

## Memory Consumption

Vectors are duplicated, being stored both within the Redis keyspace and the vector search algorithm.

## Transactions

Owing to the asynchronous nature of executing tasks by thread pools, vector search operations don't adhere to transactional semantics.

## RDB Snapshots

  * Vector search RDB snapshots are incompatible with non-vector search Redis instances due to specialized index formatting.
  * Importing vector search RDB snapshots from other vector search solutions other than Memorystore for Redis is not supported.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
