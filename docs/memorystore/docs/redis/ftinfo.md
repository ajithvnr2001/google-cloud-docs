---
url: https://docs.cloud.google.com/memorystore/docs/redis/ftinfo/
title: FT.INFO \u00a0|\u00a0 Memorystore for Redis \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:33:54.568317+00:00
---

# FT.INFO  |  Memorystore for Redis  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/redis/ftinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Redis ](https://docs.cloud.google.com/memorystore/docs/redis)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/redis/redis-overview)



Send feedback 

#  FT.INFO Stay organized with collections  Save and categorize content based on your preferences. 

This command provides information on the requested index.

## Syntax
    
    
    FT.INFO index
    

  * `index` (required): This is the name of the index whose information you want to retrieve.



### Command returns

The array returned by the `FT.INFO` command has the keys and values seen in the following tables.

#### General

Keys and values for general information for the index are as follows:

Key | Value type | Description  
---|---|---  
index_name | string | The index name  
num_docs | integer | Total keys in the index  
num_records | integer | Total records in the index  
hash_indexing_failures | integer | Count of unsuccessful indexing attempts  
indexing | integer | Binary value. Shows if background indexing is running or not  
percent_indexed | integer | Progress of background indexing. Percentage is expressed as a value from 0 to 1  
index_definition | array | To see the array provided by this key, see [Index definition](https://docs.cloud.google.com/memorystore/docs/redis/ftinfo#index_definition).  
  
#### Index definition information

Index definition keys and values are as follows:

Key | Value type | Description  
---|---|---  
key_type | string | HASH. This is the only available key type.  
prefixes | array of strings | Prefixes for keys  
default_score | integer | Unmodifiable. This is the default scoring value for vector search scoring function, which is used for sorting.  
attributes | array | To see the array provided by this key, see [Attribute (field) information](https://docs.cloud.google.com/memorystore/docs/redis/ftinfo#attribute_information).  
  
#### Attribute (field) information

Attribute (field) keys and values is as follows:

Key | Value type | Description  
---|---|---  
identifier | string | attribute names  
attribute | string | An index field. This is correlated to a specific index HASH field.  
type | string | VECTOR. This is the only available type  
index | array | To see the array provided by this key, see [Index information](https://docs.cloud.google.com/memorystore/docs/redis/ftinfo#index_information).  
  
#### Vector index information

Index keys and values are follows:

Key | Value type | Description  
---|---|---  
capacity | integer | The current capacity for total number of vectors that the index can store.  
dimensions | integer | Dimension count  
distance_metric | string | Possible values are L2, IP or Cosine  
data_type | string | FLOAT32. This is the only available data type  
algorithm | array | To see the array provided by this key, see [Algorithm keys](https://docs.cloud.google.com/memorystore/docs/redis/ftinfo#algorithm_keys).  
  
#### Vector algorithm keys

Algorithm keys and values are as follows:

Key | Value type | Description  
---|---|---  
name | string | HNSW or FLAT  
m | integer | Displays the count of maximum permitted outgoing edges for each node in the graph in each layer. The maximum number of outgoing edges is 2M for layer 0. The Default is 16. The maximum is 512.  
ef_construction | integer | Displays the count of vectors in the index. The default is 200, and the max is 4096. Higher values increase the time needed to create indexes, but improve the recall ratio.  
ef_runtime | integer | Displays the count of vectors to be examined during a query operation. The default is 10, and the max is 4096.  
  
### Required arguments

  * `index` \- This is the name of the index that you want to get details for.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
