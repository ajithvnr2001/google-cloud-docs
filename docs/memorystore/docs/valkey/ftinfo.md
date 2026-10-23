---
url: https://docs.cloud.google.com/memorystore/docs/valkey/ftinfo/
title: FT.INFO \u00a0|\u00a0 Memorystore for Valkey \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:35.989528+00:00
---

# FT.INFO  |  Memorystore for Valkey  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/memorystore/docs/valkey/ftinfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Memorystore ](https://docs.cloud.google.com/memorystore/docs)
  * [ Memorystore for Valkey ](https://docs.cloud.google.com/memorystore/docs/valkey)
  * [ Guides ](https://docs.cloud.google.com/memorystore/docs/valkey/product-overview)



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
num_docs | integer | Total keys in the index partition located on this node  
num_records | integer | Total records in the index partition located on this node  
hash_indexing_failures | integer | Count of unsuccessful indexing attempts  
indexing | integer | Binary value. Shows if background indexing is running or not  
percent_indexed | integer | Progress of background indexing. Percentage is expressed as a value from 0 to 1  
index_definition | array | To see the array provided by this key, see [Index definition](https://docs.cloud.google.com/memorystore/docs/valkey/ftinfo#index_definition).  
  
#### Index definition information

Index definition keys and values are as follows:

Key | Value type | Description  
---|---|---  
key_type | string | HASH. This is the only available key type.  
prefixes | array of strings | Prefixes for keys  
default_score | integer | Unmodifiable. This is the default scoring value for vector search scoring function, which is used for sorting.  
attributes | array | To see the array provided by this key, see [Attribute (field) information](https://docs.cloud.google.com/memorystore/docs/valkey/ftinfo#attribute_information).  
  
#### Attribute (field) information

Attribute (field) keys and values is as follows:

Key | Value type | Description  
---|---|---  
identifier | string | attribute names  
attribute | string | An index field. This is correlated to a specific index HASH field.  
type | string | One of VECTOR, TAG or NUMERIC  
index | array | To see the array provided by this key, see [Index information](https://docs.cloud.google.com/memorystore/docs/valkey/ftinfo#index_information).  
  
#### Vector index information

Index keys and values are follows:

Key | Value type | Description  
---|---|---  
capacity | integer | The current capacity for total number of vectors that the index can store.  
dimensions | integer | Dimension count  
distance_metric | string | Possible values are L2, IP or Cosine  
data_type | string | FLOAT32. This is the only available data type  
algorithm | array | To see the array provided by this key, see [Algorithm keys](https://docs.cloud.google.com/memorystore/docs/valkey/ftinfo#algorithm_keys).  
  
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



### Examples

Input:
    
    
    > FT.CREATE my_index_name SCHEMA my_vector_field_key VECTOR HNSW 10 TYPE FLOAT32 DIM 20 DISTANCE_METRIC COSINE M 4 EF_CONSTRUCTION 100 my_tag_field_key TAG SEPARATOR '@' CASESENSITIVE my_numeric_field_key NUMERIC
    > FT.INFO my_index_name
    

Output:
    
    
     1) index_name
     2) my_index_name
     3) index_options
     4) (empty array)
     5) index_definition
     6) 1) key_type
        2) HASH
        3) prefixes
        4) 1)
        5) default_score
        6) "1"
     7) attributes
     8) 1)  1) identifier
            2) my_tag_field_key
            3) attribute
            4) my_tag_field_key
            5) type
            6) TAG
            7) SEPARATOR
            8) @
            9) CASESENSITIVE
           10) size
           11) "0"
        2) 1) identifier
           2) my_vector_field_key
           3) attribute
           4) my_vector_field_key
           5) type
           6) VECTOR
           7) index
           8)  1) capacity
               2) (integer) 10240
               3) dimensions
               4) (integer) 20
               5) distance_metric
               6) COSINE
               7) size
               8) "0"
               9) data_type
              10) FLOAT32
              11) algorithm
              12) 1) name
                  2) HNSW
                  3) m
                  4) (integer) 4
                  5) ef_construction
                  6) (integer) 100
                  7) ef_runtime
                  8) (integer) 10
        3) 1) identifier
           2) my_numeric_field_key
           3) attribute
           4) my_numeric_field_key
           5) type
           6) NUMERIC
           7) size
           8) "0"
     9) num_docs
    10) "0"
    11) num_terms
    12) "0"
    13) num_records
    14) "0"
    15) hash_indexing_failures
    16) "0"
    17) backfill_in_progress
    18) "0"
    19) backfill_complete_percent
    20) "1.000000"
    21) mutation_queue_size
    22) "0"
    23) recent_mutations_queue_delay
    24) "0 sec"
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
