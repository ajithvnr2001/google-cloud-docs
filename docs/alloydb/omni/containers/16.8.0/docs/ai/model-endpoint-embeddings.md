---
url: https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/model-endpoint-embeddings/
title: Generate vector embeddings with model endpoint management \u00a0|\u00a0 AlloyDB Omni for containers: 16.8.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T10:40:34.182802+00:00
---

# Generate vector embeddings with model endpoint management  |  AlloyDB Omni for containers: 16.8.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/model-endpoint-embeddings/

This page documents AlloyDB Omni version **16.8.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/overview)



Send feedback 

#  Generate vector embeddings with model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.8.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/model-endpoint-embeddings)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.4.0/docs/ai/model-endpoint-embeddings)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/model-endpoint-embeddings)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/model-endpoint-embeddings)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.10.0/docs/ai/model-endpoint-embeddings)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/model-endpoint-embeddings)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/model-endpoint-embeddings)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/model-endpoint-embeddings)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.14.0/docs/ai/model-endpoint-embeddings)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/model-endpoint-embeddings)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/model-endpoint-embeddings)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/model-endpoint-embeddings)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/model-endpoint-embeddings)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/model-endpoint-embeddings)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.18.0/docs/ai/model-endpoint-embeddings)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/model-endpoint-embeddings)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/model-endpoint-embeddings)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/model-endpoint-embeddings)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/model-endpoint-embeddings)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/model-endpoint-embeddings)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/model-endpoint-embeddings)

This page describes how to generate embeddings using registered model endpoints. 

## Before you begin

Make sure that you have registered your model endpoint with Model endpoint management. For more information, see [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint)

## Generate embeddings

Use the `google_ml.embedding()` SQL function to call the registered model endpoint with the text embedding model type to generate embeddings.

To call the model and generate embeddings, use the following SQL query:
    
    
    SELECT
      google_ml.embedding(
        model_id => 'MODEL_ID',
        content => 'CONTENT');
    

Replace the following:

  * `MODEL_ID`: the model ID you defined when registering the model endpoint.
  * `CONTENT`: the text to translate into a vector embedding.



## Examples

Some examples for generating embeddings using registered model endpoint are listed in this section.

#### Text embedding models with built-in support

To generate embeddings for a registered `text-embedding-005` model endpoint, run the following statement:
    
    
        SELECT
          google_ml.embedding(
            model_id => 'text-embedding-005',
            content => 'AlloyDB is a managed, cloud-hosted SQL database service');
    

To generate embeddings for a registered `text-embedding-ada-002` model endpoint by OpenAI, run the following statement:
    
    
        SELECT
          google_ml.embedding(
            model_id => 'text-embedding-ada-002',
            content => 'e-mail spam');
    

To generate embeddings for a registered `text-embedding-3-small` or `text-embedding-3-large` model endpoints by OpenAI, run the following statement:
    
    
      SELECT
        google_ml.embedding(
          model_id => 'text-embedding-3-small',
          content => 'Vector embeddings in AI');
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
