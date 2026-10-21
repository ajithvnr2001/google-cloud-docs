---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/work-with-embeddings/
title: Generate embeddings \u00a0|\u00a0 AlloyDB Omni for containers: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:46:11.360996+00:00
---

# Generate embeddings  |  AlloyDB Omni for containers: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/work-with-embeddings/

This page documents AlloyDB Omni version **16.9.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/overview)



Send feedback 

#  Generate embeddings Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/work-with-embeddings)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/work-with-embeddings)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/work-with-embeddings)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/work-with-embeddings)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/work-with-embeddings)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/work-with-embeddings)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/work-with-embeddings)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/work-with-embeddings)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/work-with-embeddings)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/work-with-embeddings)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/work-with-embeddings)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/work-with-embeddings)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/work-with-embeddings)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/work-with-embeddings)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/work-with-embeddings)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/work-with-embeddings)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/work-with-embeddings)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/work-with-embeddings)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/work-with-embeddings)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/work-with-embeddings)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/work-with-embeddings)



This page shows you how to use AlloyDB Omni as a large language model (LLM) tool and generate vector embeddings based on an LLM.

For more information about using ML models with AlloyDB Omni, see [Build generative AI applications](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/overview-ai).

AlloyDB Omni lets you use an LLM hosted by Vertex AI to translate a text string into an _embedding_ , which is the model's representation of the given text's semantic meaning as a numeric vector. For more information about Vertex AI support for text embeddings, see [Text embeddings](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings).

## Before you begin

To let AlloyDB Omni generate embeddings, make sure you meet the following requirements:

### Regional restrictions

You can generate embeddings in regions where Generative AI on Vertex AI is available. For a list of regions, see [Generative AI on Vertex AI locations ](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/locations#available-regions).

For AlloyDB Omni, ensure that both the AlloyDB Omni cluster and the Vertex AI model you are querying are in the same region.

**Note:** This restriction does not prevent AlloyDB Omni servers from integrating with Vertex AI, no matter where those servers are located. For more information, see [Install AlloyDB Omni with AlloyDB Omni AI](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install-with-alloydb-ai).

### Required database extension

  * Ensure that the `google_ml_integration` extension is installed on your AlloyDB Omni database.
        
        CREATE EXTENSION IF NOT EXISTS google_ml_integration;
        

This extension is included with AlloyDB Omni. You can install it on any database in your cluster.

  * Set the `google_ml_integration.enable_model_support` database flag to `off`.




### Set up model access

Before you can generate embeddings from an AlloyDB Omni database, you must configure AlloyDB Omni to work with a text embedding model.

To work with the cloud-based `text-embedding-005` model, you need to [integrate your database with with Vertex AI](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/install-with-alloydb-ai).

### Grant database users access to generate embeddings

Grant permission for database users to execute the `embedding` function to run predictions:

  1. Connect a `psql` client to the cluster's primary instance, as described in [Connect a `psql` client to an instance](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/run-connect).

  2. At the psql command prompt, connect to the database and grant permissions:
         
         \c DB_NAME
         
         GRANT EXECUTE ON FUNCTION embedding TO USER_NAME;
         

Replace the following:

     * DB_NAME: the name of the database on which the permissions should be granted

     * USER_NAME: the name of the user for whom the permissions should be granted




## Generate an embedding

AlloyDB Omni provides a function that lets you translate text into a vector embedding. You can then store that embedding in your database as vector data, and optionally use `pgvector` functions to base queries on it.

**Note:** To generate embeddings for custom hosted or third-party AI models, see [Register and call remote AI models in AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/model-endpoint-overview). This feature is available in [Preview](https://cloud.google.com/products?e=48754805#product-launch-stages).

To generate an embedding using AlloyDB Omni, use the `embedding()` function provided by the `google_ml_integration` extension:
    
    
    SELECT embedding( 'MODEL_IDVERSION_TAG', 'TEXT');
    

Replace the following:

  * `MODEL_ID`: the ID of the model to query.

If you are using the Vertex AI Model Garden, then specify `text-embedding-005` as the model ID. These are the cloud-based models that AlloyDB Omni can use for text embeddings. For more information, see [Text embeddings](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings).

  * Optional: `VERSION_TAG`: the version tag of the model to query. Prepend the tag with `@`.

If you are using one of the `text-embedding` English models with Vertex AI, then specify one of the version tags—for example, `text-embedding-005`, listed in [Model versions](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings#model_versions).

Google strongly recommends that you always specify the version tag. If you don't specify the version tag, then AlloyDB always uses the latest model version, which might lead to unexpected results.



  * `TEXT`: the text to translate into a vector embedding.



The following example uses version `005` of the `text-embedding` English models to generate an embedding based on a provided literal string:
    
    
    SELECT embedding('text-embedding-005', 'AlloyDB is a managed, cloud-hosted SQL database service.');
    

## Store embeddings

The [embeddings generated using the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/work-with-embeddings) are implemented as arrays of `real` values. These generated embeddings are passed as inputs for `pgvector` extension functions.

To store this value in a table, add a `real[]` column:
    
    
    ALTER TABLE TABLE ADD COLUMN EMBEDDING_COLUMN real[DIMENSIONS];
    

After you create a column to store embeddings, you can populate it based on the values already stored in another column in the same table:

**Note:** If you have more than 100k rows in a table, we don't recommend using the `embedding()` function to generate stored embeddings on existing data in a table. It is best suited for inline embedding generation.
    
    
    UPDATE TABLE SET EMBEDDING_COLUMN = embedding('MODEL_IDVERSION_TAG', SOURCE_TEXT_COLUMN);
    

Replace the following:

  * `TABLE`: the table name

  * `EMBEDDING_COLUMN`: the name of the embedding column




  * `MODEL_ID`: the ID of the model to query.

If you are using the Vertex AI Model Garden, then specify `text-embedding-005` as the model ID. These are the cloud-based models that AlloyDB Omni can use for text embeddings. For more information, see [Text embeddings](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings).

  * Optional: `VERSION_TAG`: the version tag of the model to query. Prepend the tag with `@`.

If you are using one of the `text-embedding` English models with Vertex AI, then specify one of the version tags—for example, `text-embedding-005`, listed in [Model versions](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings#model_versions).

Google strongly recommends that you always specify the version tag. If you don't specify the version tag, then AlloyDB always uses the latest model version, which might lead to unexpected results.



  * `SOURCE_TEXT_COLUMN`: the name of the column storing the text to translate into embeddings



## Perform similarity search

You can use also use the [`embedding()`](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/work-with-embeddings) function to translate the text into a vector. You apply the vector to the `pgvector` nearest-neighbor operator, `<->`, to find the database rows with the most semantically similar embeddings.

Because `embedding()` returns a `real` array, you must explicitly cast the `embedding()` call to `vector` in order to use these values with `pgvector` operators.
    
    
      CREATE EXTENSION IF NOT EXISTS google_ml_integration;
      CREATE EXTENSION IF NOT EXISTS vector;
    
      SELECT * FROM TABLE
        ORDER BY EMBEDDING_COLUMN::vector
        <-> embedding('MODEL_IDVERSION_TAG', 'TEXT')::vector
        LIMIT ROW_COUNT
    

## Use model version tags to avoid errors

**Caution:** To avoid inconsistent results from the `embedding()` function, always specify a stable embeddings model, including a version tag.

Google strongly recommends that you always use a stable version of your chosen embeddings model. For most models, this means explicitly setting a version tag.

Calling the `embedding()` function without specifying the version tag of the model is syntactically valid, but it is also error-prone.

If you omit the version tag when using a model in the Vertex AI Model Garden, then Vertex AI uses the latest version of the model. This might not be the latest stable version. For more information about available Vertex AI model versions, see [Model versions](https://docs.cloud.google.com/vertex-ai/docs/generative-ai/model-reference/text-embeddings#model_versions).

A given Vertex AI model version always return the same `embedding()` response to given text input. If you don't specify model versions in your calls to `embedding()`, then a new published model version can abruptly change the returned vector for a given input, causing errors or other unexpected behavior in your applications.

To avoid these problems, always specify the model version.

## Troubleshoot

### ERROR: Model not found for model_id

#### Error message

When you try to generate an embedding using either `embedding()` or `google_ml.embedding()` function, the following error occurs:

`ERROR: 'Model not found for model_id:`

#### Recommended fix

  * Upgrade the `google_ml_integration` extension and try generating embeddings again.
        
        ALTER EXTENSION IF NOT EXISTS google_ml_integration UPDATE;
        

You can also drop the extension, and then create it again.
        
        DROP extension google_ml_integration;
        CREATE EXTENSION google_ml_integration;
        

  * If you generate embeddings using the `google_ml.embedding()` function, then ensure that the model is registered and you are using the correct `model_id` in the query.




## What's next

  * [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/store-index-query-vectors)
  * [An example embedding workflow](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/example-embeddings)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
