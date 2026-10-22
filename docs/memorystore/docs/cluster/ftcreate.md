---
url: https://docs.cloud.google.com/memorystore/docs/cluster/ftcreate/
title: FT.CREATE \u00a0|\u00a0 Memorystore for Redis Cluster \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:10:43.335651+00:00
---

# FT.CREATE  |  Memorystore for Redis Cluster  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/cluster/ftcreate/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis Cluster ](https://docs.cloud.google.com/memorystore/docs/cluster)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/cluster/memorystore-for-redis-cluster-overview)



Send feedback 

#  FT.CREATE Stay organized with collections  Save and categorize content based on your preferences. 

`FT.CREATE` creates a searchable index. With Memorystore for Redis Cluster, indexes are created at the cluster level. Creating an index on any node will cause creation of the index across all nodes in the cluster.

## Syntax
    
    
    FT.CREATE index
      ON HASH
      [PREFIX count prefix [prefix ...]]
      SCHEMA field_name [AS alias] VECTOR [HNSW|FLAT] attribute_count [attribute_name attribute_value]
      [field_name [AS alias] NUMERIC]
      [field_name [AS alias] TAG [SEPARATOR ...] [CASESENSITIVE]]
    

  * `index` (required): This is the name you give to your index. If an index with the same name exists already, an error is returned.

  * `ON HASH` (optional): This indicates the HASH data type. Only the HASH data type is supported.

  * `PREFIX [count] [prefix]` (optional): This indicates which hash keys to index.

  * `SCHEMA hash_field_name` (required): The hash_field_name after SCHEMA identifies the field name in the hash. `[AS alias]` assigns the name `alias` as an alias for the field name attribute.




### Field types

  * `VECTOR` (required): Vector field for vector search:

    * `[HNSW|FLAT]` (required): Designated algorithm. Either `FLAT` (brute force) or HNSW (Hierarchical Navigable Small World).

    * `attribute_count` (required): Total attribute count of names and values passed in the algorithm config.

    * `attribute_name attribute_value`: Key-value pairs that define the index configuration, but are specific to one of the two available algorithms.

      * Required HNSW algorithm attributes:

        * `DIM` (required): Vector dimensions count. Accepted values are `1`-`32768`.

        * `TYPE` (required): The vector type. Only `FLOAT32` is supported.

        * `DISTANCE_METRIC` (required): Must be one of the following - `L2`, `IP`, or `COSINE`.

      * Optional HNSW algorithm attributes:

        * `EF_RUNTIME` (optional): Sets the count of vectors to be examined during a query operation. The default is `10`, and the max is `4096`. You can set this parameter value for each query you run. Higher values increase query times, but improve query recall.

        * `M` (optional): The count of maximum permitted outgoing edges for each node in the graph in each layer. The maximum number of outgoing edges is 2M for layer 0. The Default is 16. The maximum is 512.

        * `EF_CONSTRUCTION` (optional): Sets count for vectors to be examined during index construction. The default is `200`, and the max is `4096`. Higher values increase the time needed to create indexes, but improve the recall ratio.

        * `INITIAL_CAP` (optional): Determines the starting vector capacity of the index. The default is `1024`. This parameter determines the index memory allocation.

      * Required FLAT algorithm attributes:

        * `DIM` (required): Vector dimensions count.

        * `TYPE` (required): The vector type. Only `FLOAT32` is supported.

        * `DISTANCE_METRIC` (required): Must be one of the following - `L2`, `IP`, or `COSINE`.

      * Optional FLAT algorithm attributes:

        * `INITIAL_CAP` (optional): Determines the starting vector capacity of the index. This parameter determines the index memory allocation.
  * `NUMERIC` (optional) - Numeric field for numeric search.

  * `TAG` (optional) - Tag field for TAG based search.

    * `SEPARATOR` (optional): A character utilized to divide the tag string into individual tags. The default option is `,`. The specified value must be a singular character. For example, the tag string "hello, world" will be interpreted as "hello" and "world" and will be indexed accordingly. Allowed values are `,.<>{}[]"':;!@#$%^&*()-+=~`

    * `CASESENSITIVE` (optional): Denotes the case sensitivity of tag fields. By default, tags are not case-sensitive. A tag string "HeLLo" will be indexed as "hello," and a query for "Hello" and "HeLlo" will yield the same result.




### Notes

  * Within the FT.CREATE command, VECTOR, NUMERIC, and TAG indexes can appear in any sequence.

  * A field can only be indexed once. In the example provided, the field `my_vector_field_key` cannot be repeated within the same index.

  * In a single FT.CREATE command, a maximum of 10 fields can be indexed.

  * By default, TAGs are case insensitive.

  * By default, TAGs are delimited by `,`.

  * Individual queries on tag and numeric queries are not supported. These fields can only be utilized along with vector-based searches.




### Examples

HNSW example:
    
    
    FT.CREATE my_index_name SCHEMA my_hash_field_key VECTOR HNSW 10 TYPE FLOAT32 DIM 20 DISTANCE_METRIC COSINE M 4 EF_CONSTRUCTION 100
    

FLAT example:
    
    
    FT.CREATE my_index_name SCHEMA my_hash_field_key VECTOR Flat 8 TYPE FLOAT32 DIM 20 DISTANCE_METRIC COSINE INITIAL_CAP 15000
    

HNSW example with a numeric field:
    
    
    FT.CREATE my_index_name SCHEMA my_vector_field_key VECTOR HNSW 10 TYPE FLOAT32 DIM 20 DISTANCE_METRIC COSINE M 4 EF_CONSTRUCTION 100 my_numeric_field_key NUMERIC
    

HNSW example with a tag field:
    
    
    FT.CREATE my_index_name SCHEMA my_vector_field_key VECTOR HNSW 10 TYPE FLOAT32 DIM 20 DISTANCE_METRIC COSINE M 4 EF_CONSTRUCTION 100 my_tag_field_key TAG SEPARATOR '@' CASESENSITIVE 
    

HNSW example with a tag and a numeric field:
    
    
    FT.CREATE my_index_name SCHEMA my_vector_field_key VECTOR HNSW 10 TYPE FLOAT32 DIM 20 DISTANCE_METRIC COSINE M 4 EF_CONSTRUCTION 100 my_tag_field_key TAG SEPARATOR '@' CASESENSITIVE my_numeric_field_key NUMERIC
    

HNSW example with multiple tag and numeric fields:
    
    
    FT.CREATE my_index_name SCHEMA my_vector_field_key VECTOR HNSW 10 TYPE FLOAT32 DIM 20 DISTANCE_METRIC COSINE M 4 EF_CONSTRUCTION 100 my_tag_field_key_1 TAG SEPARATOR '@' CASESENSITIVE my_numeric_field_key_1 NUMERIC my_numeric_field_key_2 NUMERIC my_tag_field_key_2 TAG
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
