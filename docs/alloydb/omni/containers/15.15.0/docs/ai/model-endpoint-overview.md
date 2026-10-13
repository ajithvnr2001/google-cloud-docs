---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/model-endpoint-overview/
title: Register and call remote AI models in AlloyDB Omni overview \u00a0|\u00a0 AlloyDB Omni using containers: 15.15.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:45:12.200234+00:00
---

# Register and call remote AI models in AlloyDB Omni overview  |  AlloyDB Omni using containers: 15.15.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/model-endpoint-overview/

This page documents AlloyDB Omni version **15.15.0** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Containers: 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/overview)



Send feedback 

#  Register and call remote AI models in AlloyDB Omni overview Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.15.0keyboard_arrow_down

  * [ Current (18.3.0) ](https://docs.cloud.google.com/alloydb/omni/containers/current/docs/ai/model-endpoint-overview)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.3.0/docs/ai/model-endpoint-overview)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/containers/18.1.0/docs/ai/model-endpoint-overview)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.9.0/docs/ai/model-endpoint-overview)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.7.0/docs/ai/model-endpoint-overview)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/containers/17.5.0/docs/ai/model-endpoint-overview)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.13.0/docs/ai/model-endpoint-overview)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.11.0/docs/ai/model-endpoint-overview)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.9.0/docs/ai/model-endpoint-overview)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.8.0/docs/ai/model-endpoint-overview)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/containers/16.3.0/docs/ai/model-endpoint-overview)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.17.0/docs/ai/model-endpoint-overview)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/model-endpoint-overview)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.13.0/docs/ai/model-endpoint-overview)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.12.0/docs/ai/model-endpoint-overview)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.1/docs/ai/model-endpoint-overview)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/containers/15.7.0/docs/ai/model-endpoint-overview)



This page gives an understanding of key concepts that you must know before registering an AI model endpoint and invoking predictions with Model endpoint management.

To register remote model endpoints with AlloyDB for PostgreSQL, see [Register and call remote AI models in AlloyDB](https://docs.cloud.google.com/alloydb/docs/ai/model-endpoint-overview).

## Overview

_Model endpoint management_ lets you register a model endpoint, manage model endpoint metadata in your database cluster, and make calls to the remote model endpoints using SQL queries. It provides the [`google_ml_integration`](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/model-endpoint) extension that includes functions that let you register the metadata related to AI models with AlloyDB. This registered metadata is used to generate vector embeddings or invoke predictions.

Some of the example model types that you can register using model endpoint management are as follows:

  * [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) text embedding and generic models
  * Embedding models provided by third-party providers, such as Hugging Face or OpenAI
  * Custom-hosted text embedding models, including self-hosted models or models available through private endpoints
  * Generic models with a JSON-based API—for example, `facebook/bart-large-mnli` model hosted on Hugging Face, `gemini-pro` model from the Vertex AI Model Garden, or `claude` models by Anthropic



## How it works

You can use model endpoint management to register a model endpoint that complies to the following:

  * Model input and output supports JSON format.
  * Model can be called using the REST protocol.



When you [register a model endpoint with the model endpoint management](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/register-model-endpoint), it registers each endpoint with a unique model ID that you provided as a reference to the model.

You can use the model endpoint ID to query models to:

  * Generate embeddings to translate text prompts to numerical vectors. You can store generated embeddings as vector data when the `vector` extension is enabled in the database. For more information, see [Store vector embeddings](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/store-embeddings).

  * Invoke predictions using sql.




Your applications can access model endpoint management using the `google_ml_integration` extension. This extension provides the following functions:

  * The `google_ml.create_model()` SQL function, which is used to register the model endpoint that is used in the prediction or embedding function.
  * The `google_ml.create_sm_secret()` SQL function, which uses secrets in the Google Cloud Secret Manager, where the API keys are stored.
  * The `google_ml.embedding()` SQL function, which is a prediction function that generates text embeddings. The return type of the embedding function is `REAL[]`.
  * The `google_ml.predict_row()` SQL function that generates predictions when you call generic models that support JSON input and output format.
  * Other helper functions that handle generating custom URL, generating HTTP headers, or passing transform functions.
  * Functions to manage the registered model endpoints and secrets.



## Key concepts

Before you start using model endpoint management, understand the concepts required to connect to and use the models.

### Model provider

_Model provider_ indicates the supported model hosting providers. Setting the model provider is optional, but helps model endpoint management in identifying the provider, and automatically formatting headers for supported models. The following table shows the model provider value you can set based on the model provider you use:

Model provider | Set in function as…  
---|---  
Vertex AI | `google`  
Hugging Face models | `hugging_face`  
Anthropic models | `anthropic`  
OpenAI | `open_ai`  
Other models | `custom`  
  
The default model provider is `custom`.

Based on the provider type, the supported authentication method differs. The Vertex AI models use the service account used to install AlloyDB Omni to authenticate, while other providers can use the Secret Manager or pass authentication details through headers. For more information, see [Set up authentication](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/register-model-endpoint#set-up-auth).

### Model type

_Model type_ indicates the type of the AI model. The extension supports text embedding as well as any generic model type. The supported model type you can set when registering a model endpoint are `text-embedding` and `generic`.

Setting model type is optional when registering generic model endpoints as `generic` is the default model type.

Pre-registered Vertex AI models
    The model endpoint management supports some text embedding and generic Vertex AI models as pre-registered model IDs. You can directly use the model ID to generate embeddings or invoke predictions, based on the model type.  
For more information about supported pre-registered models, see [Pre-registered Vertex AI models](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/model-endpoint#pre-registered-models).  
  
For example, to call the pre-registered `textembedding-gecko` model, you can directly call the model using the embedding function:  
  

    
    
    SELECT
          google_ml.embedding(
            model_id => 'textembedding-gecko',
            content => 'AlloyDB is a managed, cloud-hosted SQL database service');
    

Models with built-in support
    The model endpoint management provides built-in support for some models by Vertex AI, Anthropic, and OpenAI. For text embedding models with built-in support, AlloyDB automatically sets up default transform functions.
    When you register these model endpoints, set the qualified name explicitly. For more information about a list of model with built-in support, see [Models with built-in support](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/model-endpoint#models-builtin-support).  

    The model type for these models can be `text-embedding` or `generic`.
Other text embedding models
    To register a text embedding model endpoint without built-in support, we recommend that you create transform functions to handle the input and output formats that the model supports. Optionally, depending on the model requirements, you might also need to create custom header function to specify the header.
    The model type for these models is `text-embedding`.
Generic models
    The model endpoint management also supports registering of all other model types apart from text embedding models. To invoke predictions for generic models, use the `google_ml.predict_row()` function. You can set model endpoint metadata, such as a request endpoint and HTTP headers that are specific to your model.
     You cannot pass transform functions when you are registering a generic model endpoint. Ensure that when you invoke predictions the input to the function is in the JSON format, and that you parse the JSON output to derive the final output.
    The model type for these models is `generic`.

### Authentication

_Auth types_ indicate the authentication type that you can use to connect to the model endpoint management using the `google_ml_integration` extension. Setting authentication is optional and is required only if you need to authenticate to access your model.

For Vertex AI models, the AlloyDB service account is used for authentication. For other models, API key or bearer token that is stored as a secret in the Secret Manager can be used with the `google_ml.create_sm_secret()` SQL function. If you are passing authentication through headers, then you can skip setting the authentication method.

The following table shows the auth types that you can set:

Authentication method | Set in function as… | Model provider  
---|---|---  
AlloyDB service agent | `alloydb_service_agent_iam` | Vertex AI provider  
Secret Manager | `secret_manager` | third-party providers, such as Anthropic, Hugging Face, or OpenAI  
  
### Prediction functions

The `google_ml_integration` extension includes the following prediction functions:

`google_ml.embedding()`
    Used to call a registered text embedding model endpoint to generate embeddings.
    For text embedding models without built-in support, the input and output parameters are unique to a model and need to be transformed for the function to call the model. You must create a transform input function to transform input of the prediction function to the model specific input, and a transform output function to transform model specific output to the prediction function output. 
`google_ml.predict_row()`
    Used to call a registered generic model endpoint, as long as the model supports a JSON-based API, to invoke predictions.

### Transform functions

Transform functions modify the input to a format that the model understands, and converts the model response to the format that the prediction function expects. The transform functions are used when registering the `text-embedding` model endpoint without built-in support. The signature of the transform functions depends on the input expected by the model.

You cannot use transform functions when registering a `generic` model endpoint.

The following shows the signatures for the prediction function for text embedding models:
    
    
    // define custom model specific input/output transform functions.
    CREATE OR REPLACE FUNCTION input_transform_function(model_id VARCHAR(100), input_text TEXT) RETURNS JSON;
    
    CREATE OR REPLACE FUNCTION output_transform_function(model_id VARCHAR(100), response_json JSON) RETURNS real[];
    

For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/model-endpoint#transform-func-example).

### HTTP header generation function

The HTTP header generation function generates the output in JSON key value pairs that are used as HTTP headers. The signature of the prediction function defines the signatures of the header generation function.

The following example shows the signature for the `google_ml.embedding()` prediction function.
    
    
    CREATE OR REPLACE FUNCTION generate_headers(model_id VARCHAR(100), input TEXT) RETURNS JSON;
    

For the `google_ml.predict_row()` prediction function, the signature is as follows:
    
    
    CREATE OR REPLACE FUNCTION generate_headers(model_id VARCHAR(100), input JSON) RETURNS JSON;
    

For more information about how to create a header generation function, see [Header generation function example](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/model-endpoint#header-gen-func-example).

## What's next

  * [Set up authentication](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/register-model-endpoint#before-you-begin) for model providers.
  * [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/ai/register-model-endpoint).
  * Learn more about the [model endpoint management reference](https://docs.cloud.google.com/alloydb/omni/containers/15.15.0/docs/reference/model-endpoint).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
