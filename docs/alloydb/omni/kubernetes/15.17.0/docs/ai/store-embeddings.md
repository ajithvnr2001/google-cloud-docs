---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/store-embeddings/
title: Store vector embeddings \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 15.17.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:55:03.298684+00:00
---

# Store vector embeddings  |  AlloyDB Omni using the container orchestrator: 15.17.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/store-embeddings/

This page documents AlloyDB Omni version **15.17.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/overview)



Send feedback 

#  Store vector embeddings Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.17.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/store-embeddings)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/store-embeddings)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/store-embeddings)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/store-embeddings)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/store-embeddings)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/store-embeddings)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/store-embeddings)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/store-embeddings)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/store-embeddings)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/store-embeddings)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/store-embeddings)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/store-embeddings)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/store-embeddings)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/store-embeddings)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/store-embeddings)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/store-embeddings)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/store-embeddings)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/store-embeddings)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/store-embeddings)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/store-embeddings)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/store-embeddings)

This page shows you how to use AlloyDB as a vector database with the `vector` extension that includes `pgvector` functions and operators. These functions and operators let you store embeddings as vector values. 

## Required database extension

Use the `vector` extension, version `0.5.0.google-1` or later, which includes `pgvector` functions and operators, to store generated embeddings as `vector` values. This is a version of `pgvector` that Google has extended with optimizations specific to AlloyDB.
    
    
    CREATE EXTENSION IF NOT EXISTS vector;
    

## Store generated embeddings

Ensure that you have already created a table in your AlloyDB database.

**Note:** If your application uses the LangChain framework and your dataset has `O(100k)` embeddings, we recommend that you use the `AlloyDBVectorStore` vector class included in the AlloyDB LangChain library to store your embeddings. For more information, see [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/alloydb/docs/ai/langchain#vector_store_procedure_guide).

To store vector embeddings, follow these steps:

  1. Create a `vector[]` column in your table to store your embeddings:
         
         ALTER TABLE TABLE ADD COLUMN EMBEDDING_COLUMN vector(DIMENSIONS);
         

Replace the following:

     * `TABLE`: the table name.

     * `EMBEDDING_COLUMN`: the name of the new embedding column.

     * `DIMENSIONS`: the number of dimensions that the model supports.

For example, if you are using one of the `text-embedding`English models—for example, `text-embedding-005` with Vertex AI, specify `768`.

  2. Copy the vectors to the vector column. The following example assumes that your embeddings are available in a CSV file:
         
         COPY TABLE (EMBEDDING_COLUMN) FROM 'PATH_TO_VECTOR_CSV (FORMAT CSV);
         

Replace the following:

     * `PATH_TO_VECTOR_CSV`: the full path of where you stored your CSV file.



After you store the embeddings, you can use the `vector` extension or the `alloydb_scann` extension to create indexes for faster query performance.

## What's next

  * [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/store-index-query-vectors).
  * Learn [an example embedding workflow](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/example-embeddings).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
