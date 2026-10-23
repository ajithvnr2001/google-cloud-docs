---
url: https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-overview/
title: Model endpoint management overview \u00a0|\u00a0 Cloud SQL for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:20:12.699857+00:00
---

# Model endpoint management overview  |  Cloud SQL for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ PostgreSQL ](https://docs.cloud.google.com/sql/docs/postgres)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/postgres/features)



Send feedback 

#  Model endpoint management overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[MySQL](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-overview "View this page for the MySQL database engine") | PostgreSQL | SQL Server

This page describes how to register an AI model endpoint and invoke predictions with model endpoint management in Cloud SQL. To use AI models in production environments, see [Build generative AI applications using Cloud SQL](https://docs.cloud.google.com/sql/docs/postgres/ai-overview) and [Work with vector embeddings](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors). 

## Overview

_Model endpoint management_ lets you register a model endpoint, manage model endpoint metadata in your Cloud SQL instance, and then interact with the models using SQL queries. Cloud SQL provides the [`google_ml_integration`](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-management-reference) extension that includes functions to add and register the model endpoint metadata related to the models. You can use these models to generate vector embeddings or invoke predictions.

You can register the following model types by using model endpoint management:

  * [Vertex AI](https://docs.cloud.google.com/vertex-ai/docs) text embedding models.
  * Custom-hosted text embedding models hosted in networks within Google Cloud.
  * Generic models with a JSON-based API. Examples of these models include the following:

    * The `gemini-pro` model from the Vertex AI Model Garden
    * The `open_ai` model for OpenAI models
    * Models hosted in networks within Google Cloud



## How it works

You can use model endpoint management to register a model endpoint that complies to the following:

  * The model input and output support the JSON format.
  * You can use the REST protocol to call the model.



When you [register a model endpoint with model endpoint management](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-register-model), model endpoint management registers each endpoint with a unique model ID as a reference to the model. You can use this model ID to query models, as follows:

  * Generate embeddings to translate text prompts to numerical vectors. You can store generated embeddings as vector data when the `pgvector` extension is enabled in the database. For more information, see [Query and index embeddings with pgvector](https://docs.cloud.google.com/sql/docs/postgres/work-with-vectors#pgvector). 

  * Invoke predictions to call a model using SQL within a transaction.




Your applications can manage their model endpoints using the `google_ml_integration` extension. This extension provides the following SQL functions:

  * `google_ml.create_model()`: registers the model endpoint that's used in the prediction or embedding function
  * `google_ml.create_sm_secret()`: uses secrets in Google Cloud Secret Manager, where the API keys are stored
  * `google_ml.embedding()`: generates text embeddings
  * `google_ml.predict_row()`: generates predictions when you call generic models that support the JSON input and output formats



## Key concepts

Before you start using model endpoint management, understand the concepts required to connect to and use the models.

### Model provider

_Model provider_ is the supported model hosting provider. The following table shows the model provider value you must set based on the model provider that you use:

Model provider | Set in function as…  
---|---  
Vertex AI (includes Gemini) | `google`  
Anthropic | `anthropic`  
Hugging Face | `hugging_face`  
OpenAI | `open_ai`  
Other models hosted outside of Vertex AI,  
Anthropic, Hugging Face, and OpenAI | `custom`  
  
The default model provider is `custom`.

If your Cloud SQL instance isn't configured with a [public IP](https://docs.cloud.google.com/sql/docs/postgres/instance-settings) address, then you can't use a model provider other than Vertex AI.

### Model types

_Model types_ are the types of the AI model. When you register a model endpoint, you can set the `text_embedding` or `generic` model types for the endpoint.

Text embedding models with built-in support
    Model endpoint management provides built-in support for all versions of the `textembedding-gecko` model. To register these model endpoints, use the `google_ml.create_model()` function. Cloud SQL sets up default transform functions for these models automatically.
    The model type for these models is `text_embedding`.

Other text embedding models
    For other text embedding models, you need to create transform functions to handle the input and output formats that the model supports. Optionally, you can use the HTTP header generation function that generates custom headers required by your model.

    The model type for these models is `text_embedding`.

Generic models
    Model endpoint management also supports registering of all other model types apart from text embedding models. To invoke predictions for generic models, use the `google_ml.predict_row()` function. You can set model endpoint metadata, such as a request endpoint and HTTP headers that are specific to your model.
     You can't pass transform functions when you register a generic model endpoint. Ensure that when you invoke predictions the input to the function is in the JSON format, and that you parse the JSON output to derive the final output.
    The model type for these models is `generic`. Because `generic` is the default model type, if you register model endpoints for this type, then setting the model type is optional.

### Authentication methods

You can use the `google_ml_integration` extension to specify different _authentication methods_ to access your model. Setting these methods is optional and is required only if you need to authenticate to access your model. 

For Vertex AI models, the Cloud SQL service account is used for authentication. For other models, the API key or bearer token that is stored as a secret in the Secret Manager can be used with the `google_ml.create_sm_secret()` SQL function.

The following table shows the authentication methods that you can set: 

Authentication method | Set in function as… | Model provider  
---|---|---  
Cloud SQL service agent | `cloudsql_service_agent_iam` | Vertex AI provider  
Secret Manager | `secret_manager` | Models hosted outside of Vertex AI  
  
### Prediction functions

The `google_ml_integration` extension includes the following _prediction functions_ :

`google_ml.embedding()`
    Calls a registered text embedding model endpoint to generate embeddings. It includes built-in support for the `textembedding-gecko` model by Vertex AI.
    For text embedding models without built-in support, the input and output parameters are unique to a model and need to be transformed for the function to call the model. Create a transform input function to transform input of the prediction function to the model specific input, and a transform output function to transform model specific output to the prediction function output. 
`google_ml.predict_row()`
    Calls a registered generic model endpoint, if the endpoint supports JSON-based APIs to invoke predictions.

### Transform functions

_Transform functions_ modify the input to a format that the model understands, and convert the model response to the format that the prediction function expects. The transform functions are used when registering the `text-embedding` model endpoint without built-in support. The signature of the transform functions depends on the prediction function for the model type.

You can't use transform functions when registering a `generic` model endpoint.

The following shows the signatures for the prediction function for text embedding models:
    
    
    // define custom model specific input/output transform functions.
    CREATE OR REPLACE FUNCTION input_transform_function(model_id VARCHAR(100), input_text TEXT) RETURNS JSON;
    
    CREATE OR REPLACE FUNCTION output_transform_function(model_id VARCHAR(100), response_json JSON) RETURNS real[];
    

For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-management-reference#transform-func-example).

### HTTP header generation function

The _HTTP header generation function_ generates the output in JSON key value pairs that are used as HTTP headers. The signature of the prediction function defines the signatures of the header generation function.

The following example shows the signature for the `google_ml.embedding()` prediction function:
    
    
    CREATE OR REPLACE FUNCTION generate_headers(model_id VARCHAR(100), input TEXT) RETURNS JSON;
    

For the `google_ml.predict_row()` prediction function, the signature is as follows:
    
    
    CREATE OR REPLACE FUNCTION generate_headers(model_id VARCHAR(100), input JSON) RETURNS JSON;
    

For more information about how to create a header generation function, see [Header generation function example](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-management-reference#header-gen-func-example).

## Limitations

  * To use AI models with your Cloud SQL instance, the maintenance version of your instance must be `R20240910.01_02` or later. To upgrade your instance to this version, see [Perform self-service maintenance](https://docs.cloud.google.com/sql/docs/postgres/self-service-maintenance).



## What's next

  * [Set up authentication](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-register-model#set-up-auth) for model providers.
  * [Register a model endpoint with model endpoint management](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-register-model).
  * Learn about the [model endpoint management reference](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-management-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
