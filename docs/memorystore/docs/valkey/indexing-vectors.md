---
url: https://docs.cloud.google.com/memorystore/docs/valkey/indexing-vectors/
title: Store vectors \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T18:35:02.931978+00:00
---

# Store vectors  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/indexing-vectors/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



Send feedback 

#  Store vectors Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to store vectors in hashes. Hashes provide an efficient way to store vectors in Memorystore for Valkey.

## Data serialization

Before storing vectors in a hash data type, vectors need to be converted into a format that Memorystore for Valkey understands. It requires vector serialization into binary blobs where the size equals the data type's byte size (for example, 4 for `FLOAT32`) multiplied by the vector's number of dimensions. A popular choice for numerical vectors is the Python [NumPy library](https://numpy.org/).

## Connect to Memorystore for Valkey

Before storing the vector in a hash, establish a connection to your Memorystore for Valkey instance by using a OSS Redis compatible client like [redis-py](https://github.com/redis/redis-py).

## Store the vector in a hash

Hashes are like dictionaries, with key-value pairs. Use the `HSET` command store your serialized vector:
    
    
    import numpy as np
    import redis
    
    # Sample vector
    vector = np.array([1.2, 3.5, -0.8], dtype=np.float32) # 3-dimensional vector
    
    # Serialize to a binary blob
    serialized_vector = vector.tobytes()
    
    redis_client = redis.cluster.RedisCluster(host='your_server_host', port=6379)
    
    redis_client.hset('vector_storage', 'vector_key', serialized_vector)  # 'vector_key' is a unique identifier
    

  * For successful indexing, your vector data must adhere to the dimensions and data type set in the index schema.



## Backfill indexes

Backfilling indexes may occur in one of the following scenarios:

  * Once an index is created, the backfilling procedure scans through keyspace for entries that meet the index filter criteria.
  * Vector indexes and their data are persisted in [RDB snapshots](https://docs.cloud.google.com/memorystore/docs/valkey/about-rdb-snapshots). When an RDB file is loaded, an automatic index backfilling process is triggered. This process actively detects and integrates any new or modified entries into the index since the RDB snapshot was created, maintaining index integrity and ensuring current results.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
