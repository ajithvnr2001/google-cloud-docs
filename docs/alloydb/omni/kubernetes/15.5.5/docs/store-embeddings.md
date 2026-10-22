---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/store-embeddings/
title: Store vector embeddings \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:25:44.121164+00:00
---

# Store vector embeddings  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/store-embeddings/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Store vector embeddings Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/store-embeddings)

This page shows you how to use AlloyDB as a vector database with the `vector` extension that includes `pgvector` functions and operators. These functions and operators let you store embeddings as vector values. 

## Required database extension

Use the `vector` extension, version `0.5.0.google-1` or later, which includes `pgvector` functions and operators, to store generated embeddings as `vector` values. This is a version of `pgvector` that Google has extended with optimizations specific to AlloyDB.
    
    
    CREATE EXTENSION IF NOT EXISTS vector;
    

## Store generated embeddings

Ensure that you have already created a table in your AlloyDB database.

**Note:** If your application uses the LangChain framework and your dataset has `O(100k)` embeddings, we recommend that you use the `AlloyDBVectorStore` vector class included in the AlloyDB LangChain library to store your embeddings. For more information, see [Build LLM-powered applications using LangChain](https://docs.cloud.google.com/alloydb/docs/ai/langchain#vector_store_procedure_guide).

To store vector embeddings, do the following:

  1. Create a `vector[]` column in your table to store your embeddings:
         
         ALTER TABLE TABLE ADD COLUMN EMBEDDING_COLUMN vector(DIMENSIONS);
         

Replace the following:

     * `TABLE`: the table name

     * `EMBEDDING_COLUMN`: the name of the new embedding column

     * `DIMENSIONS`: the number of dimensions that the model supports.

For example, if you are using one of the `textembedding-gecko`English models—for example, `textembedding-gecko@003` with Vertex AI, specify `768`.

  2. Copy the vectors to the vector column. The following example assumes your embeddings are available in a `CSV` file:
         
         COPY TABLE (EMBEDDING_COLUMN) FROM 'PATH_TO_VECTOR_CSV (FORMAT CSV);
         

Replace the following:

     * `PATH_TO_VECTOR_CSV`: the full path of where you have stored your `CSV` file.



**Preview — AlloyDB ScaNN index**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

After you store the embeddings, you can use the `vector` extension or the `alloydb_scann` extension to create indexes for faster query performance.

## What's next

  * [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/store-index-query-vectors)
  * [An example embedding workflow](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/example-embeddings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
