---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/model-endpoint-embeddings/
title: Generate vector embeddings with model endpoint management \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:21.282160+00:00
---

# Generate vector embeddings with model endpoint management  |  AlloyDB Omni for Kubernetes: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/model-endpoint-embeddings/

This page documents AlloyDB Omni version **15.5.5** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/overview)



Send feedback 

#  Generate vector embeddings with model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/model-endpoint-embeddings)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.4/docs/model-endpoint-embeddings)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.2/docs/model-endpoint-embeddings)



**Preview — Model endpoint management**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes a preview that lets you experiment with registering an AI model endpoint and invoking predictions with Model endpoint management. For using AI models in production environments, see [Build generative AI applications using AlloyDB AI](https://docs.cloud.google.com/alloydb/docs/ai) and [Work with vector embeddings](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/work-with-embeddings).

After the model endpoints are added and registered in the Model endpoint management, you can reference them using the model ID to generate embeddings.

## Before you begin

Make sure that you have registered your model endpoint with Model endpoint management. For more information, see [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.5.5/docs/model-endpoint-register-model)

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

#### Text embedding models with in-built support

To generate embeddings for a registered `textembedding-gecko@002` model endpoint, run the following statement:
    
    
        SELECT
          google_ml.embedding(
            model_id => 'textembedding-gecko@002',
            content => 'AlloyDB is a managed, cloud-hosted SQL database service');
    

To generate embeddings for a registered `text-embedding-ada-002` model endpoint by OpenAI, run the following statement:
    
    
        SELECT
          google_ml.embedding(
            model_id => 'text-embedding-ada-002',
            content => 'e-mail spam');
    

#### Other text embedding models

To generate embeddings for a registered `text-embedding-3-small` or `text-embedding-3-large` model endpoints by OpenAI, run the following statement:
    
    
      SELECT
        google_ml.embedding(
          model_id => 'text-embedding-3-small',
          content => 'Vector embeddings in AI');
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
