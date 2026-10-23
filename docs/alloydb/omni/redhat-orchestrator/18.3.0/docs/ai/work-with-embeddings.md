---
url: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/work-with-embeddings/
title: Generate embeddings \u00a0|\u00a0 AlloyDB Omni using the RPM orchestrator: 18.3.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T12:54:18.382352+00:00
---

# Generate embeddings  |  AlloyDB Omni using the RPM orchestrator: 18.3.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/work-with-embeddings/

This page documents AlloyDB Omni version **18.3.0** using the **RPM orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ RPM orchestrator: 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/overview)



Send feedback 

#  Generate embeddings Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 18.3.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/current/docs/ai/work-with-embeddings)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.4.0/docs/ai/work-with-embeddings)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/work-with-embeddings)

The `google_ml_integration` extension includes embedding functions in two different namespaces; `public` and `google_ml`. This page describes how to generate text embeddings using functions from these namespaces. 

The `embedding()` function in the `public` schema can be used with any Vertex AI embedding model without registering the endpoint. If you want to pass any custom information such as the task type, register the endpoint, and then use the `google_ml.embedding()` function in the `google_ml` schema. For more information about registering an endpoint, see [Register a model](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/register-model-endpoint).

## How embeddings work

Imagine a database running on AlloyDB Omni with the following characteristics:

  * The database contains a table, `items`. Each row in this table describes an item that your business sells.

  * The `items` table contains a column, `complaints`. This `TEXT` column stores buyer complaints logged about each item.

  * The database integrates with the Vertex AI Model Garden, giving it access to the `gemini-embedding-001` English models.




Even though this database stores complaints about items, these complaints are stored as plain text, making them difficult to query. For example, to see which items have the most complaints from customers who received the wrong color of merchandise, then you can perform ordinary SQL queries on the table, that look for various keyword matches. However, this approach only matches rows that contain those exact keywords.

For example, a basic SQL query such as `SELECT * FROM items WHERE complaints LIKE '%wrong color%'` doesn't return a row whose `complaints` field contains only `The picture shows a blue one, but the one I received was red`.

SQL queries using LLM-powered embeddings can help return semantically similar responses for such queries. By applying embeddings, you can query the table in this example for items whose complaints have semantic similarity to a given text prompt, such as `It was the wrong color`.

**Note:** When monitoring your usage and quotas in the Google Cloud console, remember that the model names might differ from the ones used in the documentation. 

  * For the `text-embedding-005` model, the `base_model` dimension in the Google Cloud console is `textembedding-gecko`.

The relevant quota is `Regional online prediction requests per base model per minute per region per base_model`.

  * For the `gemini-embedding-001` model, the `base_model` dimension is `gemini-embedding`.

The relevant quotas are `Embed content input tokens per minute per region per base_model` and `Regional online prediction requests per base model per minute per region per base_model`.




For basic embedding generation, select one of the following schemas.

google_ml schema public schema

**Note:** You are charged for requests made to the Vertex AI models. For more information, see [Vertex AI pricing](https://cloud.google.com/products/gemini-enterprise-agent-platform/pricing).

## Before you begin

To let AlloyDB Omni generate embeddings, do the following:

  * [Use the PgBouncer connection pooler](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/use-pgbouncer-connection-pooler) to connect to AlloyDB Omni as the `postgres` user. 
  * Verify that the `google_ml_integration` extension is installed. 
        
        CREATE EXTENSION IF NOT EXISTS google_ml_integration CASCADE;

If you don't have the necessary permissions, contact your database administrator to perform the update. Alternatively, you can wait for the new version to be automatically rolled out to your cluster. 

  * [Verify that the `google_ml_integration.enable_model_support` parameter is set to `on`](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/configure-database-parameters). 
  * Before you can generate embeddings from an AlloyDB Omni database, you must configure [AlloyDB Omni to work with Vertex AI](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/install-with-alloydb-ai). 
  * Grant permissions for database users to execute the embedding function to generate embeddings: 
        
        \c DB_NAME
        GRANT EXECUTE ON FUNCTION google_ml.embedding TO USER_NAME;

Replace the following: 

    * DB_NAME: the name of the database on which the permissions should be granted 
    * USER_NAME: the name of the user for whom the permissions should be granted 



## Generate embeddings

Use the `google_ml.embedding()` SQL function to call text embedding models.

To call the model and generate embeddings, run the following query:
    
    
    SELECT
     google_ml.embedding(
       model_id => 'MODEL_ID',
       content => 'CONTENT');
    

Replace the following:

  * `MODEL_ID`: the qualified model ID-for example, `gemini-embedding-001`.
  * `CONTENT`: the text to translate into a vector embedding.

**Note:** If you want to generate and manage vector embeddings for a large table column, you can use auto vector embeddings. For more information, see [Generate and manage auto vector embeddings for large tables](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/generate-manage-auto-embeddings-for-tables).

## Examples for generating embeddings

Some examples for generating embeddings using registered model endpoint are listed in this section.

### Gemini embedding models

To generate embeddings for a registered `gemini-embedding-001` model endpoint, run the following statement:

**Note:** Vertex AI model support is governed by [Vertex AI model versioning, regional availability, and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions) guidelines. Verify that the model you are trying is available in the region where your AlloyDB Omni cluster is created.
    
    
       SELECT
         google_ml.embedding(
           model_id => 'gemini-embedding-001',
           content => 'AlloyDB is a managed, cloud-hosted SQL database service');
    

If your AlloyDB Omni cluster and the Vertex AI endpoint are in different projects, do the following:

  1. Run the following `CALL` statement.

**Note:** If your `google_ml_integration` extension is version 1.5.3 or later, then you don't need to use `model_in_transform_fn` and `model_out_transform_fn` for `gemini-embedding-001`.
         
         CALL
              google_ml.create_model(
                model_id => 'gemini-embedding-001',
                model_request_url => 'https://REGION_ID-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION_ID/publishers/google/models/gemini-embedding-001:predict',
                model_provider => 'google',
                model_type => 'text_embedding',
                model_auth_type => 'alloydb_service_agent_iam',
                model_in_transform_fn => 'google_ml.vertexai_text_embedding_input_transform',
                model_out_transform_fn => 'google_ml.vertexai_text_embedding_output_transform'
              );
         

  2. To generate embeddings for a registered `gemini-embedding-001` model endpoint, run the following statement:
         
         SELECT
             google_ml.embedding(
               model_id => 'gemini-embedding-001',
               content => 'AlloyDB is a managed, cloud-hosted SQL database service');
         




### OpenAI embedding model

To generate embeddings for a [registered `text-embedding-3-small` or `text-embedding-3-large` model endpoint](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/register-model-endpoint#add-openai) by OpenAI, run the following statement:
    
    
     SELECT
       google_ml.embedding(
         model_id => 'text-embedding-3-small',
         content => 'Vector embeddings in AI');
    

## What's next

* [Run vector similarity searches](/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/run-vector-similarity-search). 

  * [Learn how to build a smart shopping assistant with AlloyDB Omni, pgvector, and model endpoint management](https://codelabs.developers.google.com/smart-shop-agent-alloydb#0).

  * [Create indexes and query vectors](https://docs.cloud.google.com/alloydb/omni/redhat-orchestrator/18.3.0/docs/ai/create-scann-index). 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
