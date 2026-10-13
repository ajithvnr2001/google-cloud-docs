---
url: https://docs.cloud.google.com/sql/docs/mysql/information-schema/
title: Cloud SQL information schema \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:41:20.425899+00:00
---

# Cloud SQL information schema  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/information-schema/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Reference ](https://docs.cloud.google.com/sql/docs/mysql/apis)



Send feedback 

#  Cloud SQL information schema Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | PostgreSQL | SQL Server

This page lists the Cloud SQL information schema table additions.

## information_schema.innodb_vector_indexes

Gives all the vector indexes that are opened in the memory after restart.

Column name | Description  
---|---  
INDEX_NAME | Name of the index  
TABLE_NAME | Qualified table name in db_name.table_name format  
INDEX_TYPE | TREE_SQ is supported  
DIMENSION | Dimensionality of the vector column  
DIST_MEASURE | Distance Measure on which index is built  
STATUS | A string describing the current state of the index  
STATE | Internal state of the index  
NUM_LEAVES | Number of leaves as configured by the user or computed internally based on the size of the base table  
NUM_LEAVES_TO_SEARCH | Number of leaves to search in ANN. Can be overridden at query time  
QUERIES | Number of ANN queries on this index since server start  
MUTATIONS | Number of DML operations on base table that resulted in updating the vector index  
TREE_MEMORY | Memory occupied by the non-leaf part of the vector index  
  
## information_schema.innodb_all_vector_indexes

Contains all the vector indexes that exists on the instance (even if they are not opened in the memory yet).

Column name | Description  
---|---  
id | same as innodb_indexes.index_id  
table_id | An identifier representing the table associated with the index  
sub_table_id | An identifier representing the sub table associated with the vector index  
state | Internal state of the index. Same as `information_schema.innodb_vector_indexes`  
corrupted | Indicates whether the index is corrupted or not. `1` means corrupted, `0` means not corrupted.  
config | A json value showing index configuration. In configuration:

  * "D" implies it is a static default value of this parameter.
  * "G" implies that the value is generated or computed internally.
  * "C" means that the value is explicitly specified by the user. The order of precedence is C > G > D.

  
  
## information_schema.innodb_vector_indexes_memory

Provides information about overall memory usage of vector indexes in the instance.

Column name | Description  
---|---  
STATE | Memory management for vector indexes is enabled.  
TOTAL_MEMORY | cloudsql_vector_max_mem_size  
INDEX_MEMORY | Amount of memory that is used to load `index_tree` into the memory.  
TRAINING_MEMORY | Amount of memory that is allocated for training during index build.  
LOADED_INDEX  | Number of indexes that are loaded in the memory.  
  
## What's next

  * Read the [overview about vector search on Cloud SQL](https://docs.cloud.google.com/sql/docs/mysql/vector-search).
  * Learn how to [enable and disable vector embeddings on your instance](https://docs.cloud.google.com/sql/docs/mysql/enable-vector-search).
  * Learn how to [generate vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings#generate_vector_embeddings_based_on_row_data).
  * Learn how to [create vector indexes](https://docs.cloud.google.com/sql/docs/mysql/create-manage-vector-indexes).
  * Learn how to [perform searches on vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/search-filter-vector-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
