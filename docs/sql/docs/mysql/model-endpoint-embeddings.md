---
url: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-embeddings/
title: Generate vector embeddings with model endpoint management \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:29:08.891503+00:00
---

# Generate vector embeddings with model endpoint management  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Generate vector embeddings with model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-embeddings "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to register an AI model endpoint and generate vector embeddings with model endpoint management. To use AI models in production environments, see [Generate and manage vector embeddings](https://docs.cloud.google.com/sql/docs/mysql/generate-manage-vector-embeddings). 

After the model endpoints are added and registered in model endpoint management, you can reference them using the model ID to generate embeddings.

## Before you begin

Make sure that you complete the following actions:

  * Register your model endpoint with model endpoint management. For more information, see [Register and call remote AI models using model endpoint management](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-register-model).
  * Create or update your Cloud SQL instance so that the instance can integrate with Vertex AI. For more information, see [Enable database integration with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai#enable-database-integration-with-vertex-ai).



## Generate embeddings

Use the `mysql.ml_embedding()` SQL function to call the registered model endpoint with the text embedding model type to generate embeddings.

To call the model and generate embeddings, use the following SQL query:
    
    
    SELECT
      mysql.ml_embedding(
        'MODEL_ID',
        'CONTENT');
    

Replace the following:

  * `MODEL_ID`: the model ID you defined when registering the model endpoint
  * `CONTENT`: the text to translate into a vector embedding



## Examples

Some examples for generating embeddings using registered model endpoints are listed in this section.

### Text embedding models with built-in support

Vertex AI embedding models are supported by default. You don't need to register them. To generate embeddings for a registered `gemini-embedding-001` model endpoint, run the following statement:
    
    
        SELECT
          mysql.ml_embedding(
            'gemini-embedding-001',
            'Cloud SQL is a managed, cloud-hosted SQL database service');
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
