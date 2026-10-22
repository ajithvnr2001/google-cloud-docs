---
url: https://docs.cloud.google.com/memorystore/docs/valkey/vector-search-limitations/
title: Features and limitations \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:13:17.170797+00:00
---

# Features and limitations  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/vector-search-limitations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Features and limitations Stay organized with collections  Save and categorize content based on your preferences. 

This page provides details about vector search features and limitations.

## Availability

Vector search is available on all Memorystore for Valkey versions across all tiers and all the supported regions.

Only instances that you create after September 13, 2024 have vector search enabled.

## Index restrictions

The following outlines the limitations of the index:

  * The maximum number of attributes in an index cannot exceed 10.
  * A vector's dimension cannot exceed 32,768.
  * The M value for HNSW must not go beyond 2M.
  * The EF Construct value for HNSW must not exceed 4096.
  * The EF Runtime value for HNSW must also not surpass 4096.



## Performance impacts

When considering the performance of vector search, there are some important variables to consider.

### Node type

Vector search facilitates vertical scaling through the integration of thread pools dedicated to executing vector search operations. This means that performance will be tied to the number of vCPUs on each node in your instance. For details on the number of vCPUs available on each node type, see [Node characteristics](https://docs.cloud.google.com/memorystore/docs/valkey/instance-node-specification#node_characteristics).

### Number of shards

Memorystore for Valkey implements a local indexing technique for all vectors. This means that the index stored on each shard contains only the documents contained on that shard. Because of this, the speed of indexing and the number of total vectors will scale linearly with the number of shards in the instance.

Since each local index only contains the contents of a single shard, searching the instance requires searching each shard in the instance and aggregating the results. With a stable amount of vectors, increasing the number of shards will improve the search performance logarithmically for HNSW indexes and linearly for FLAT indexes due to fewer vectors being contained on each local index.

Note that due to the increased amount of work needed to search all shards, the observable latency to complete a given search request may increase as more shards are added. Despite this, even the largest instances support single digit millisecond latencies.

### Number of replicas

Adding additional replicas will increase search throughput linearly by allowing load balancing of search requests to read replicas.

## Scaling events

Upon resizing your Memorystore for Valkey instance, the documents within your indexes will be moved to uniformly distribute the data across the new shard count. When this happens, documents that are moved across nodes will be indexed in the background. After the scaling operation completes, you can monitor the value of `mutation_queue_size` in the [FT.INFO](https://docs.cloud.google.com/memorystore/docs/valkey/ftinfo) output to see the progress of re-indexing due to resizing your instance.

## Memory consumption

Vectors are duplicated, being stored both within the keyspace and the vector search algorithm.

## Transactions

Owing to the asynchronous nature of executing tasks by thread pools, vector search operations don't adhere to transactional semantics.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
