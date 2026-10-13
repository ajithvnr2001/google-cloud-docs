---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/model-endpoint/
title: Model endpoint management reference \u00a0|\u00a0 AlloyDB Omni for Kubernetes: 16.9.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:44:32.300875+00:00
---

# Model endpoint management reference  |  AlloyDB Omni for Kubernetes: 16.9.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/model-endpoint/

This page documents AlloyDB Omni version **16.9.0** using the **Kubernetes** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For Kubernetes: 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/overview)
  * [ Reference ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/kubernetes-crds-1.1.1/backup)



Send feedback 

#  Model endpoint management reference Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 16.9.0keyboard_arrow_down

  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/reference/model-endpoint)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/reference/model-endpoint)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/reference/model-endpoint)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/reference/model-endpoint)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/reference/model-endpoint)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/reference/model-endpoint)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/reference/model-endpoint)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/reference/model-endpoint)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/reference/model-endpoint)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/reference/model-endpoint)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/reference/model-endpoint)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/reference/model-endpoint)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/reference/model-endpoint)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/reference/model-endpoint)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/reference/model-endpoint)

This page lists parameters for different functions provided by the `google_ml_integration` extension to register and manage model endpoints, and secrets with model endpoint management. 

You must set the `google_ml_integration.enable_model_support` database flag to `on` before you can start using the extension.

For more information, see [Use Model endpoint management with AlloyDB Omni for AI models](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/model-endpoint-overview).

## Models

Use this reference to understand parameters for functions that let you manage model endpoints.

### `google_ml.create_model()` function

The following shows how to call the `google_ml.create_model()` SQL function used to register model endpoint metadata:
    
    
      CALL
        google_ml.create_model(
          model_id => 'MODEL_ID',
          model_request_url => 'REQUEST_URL',
          model_provider => 'PROVIDER_ID',
          model_type => 'MODEL_TYPE',
          model_qualified_name => 'MODEL_QUALIFIED_NAME',
          model_auth_type => 'AUTH_TYPE',
          model_auth_id => 'AUTH_ID',
          generate_headers_fn => 'GENERATE_HEADER_FUNCTION',
          model_in_transform_fn => 'INPUT_TRANSFORM_FUNCTION',
          model_out_transform_fn => 'OUTPUT_TRANSFORM_FUNCTION');
    

Parameter | Required | Description  
---|---|---  
`MODEL_ID` | required for all model endpoints | A unique ID for the model endpoint that you define.  
`REQUEST_URL` | optional for other text embedding model endpoints with built-in support | The model-specific endpoint when adding other text embedding and generic model endpoints. For AlloyDB for PostgreSQL, provide an `https` URL.  
  
The request URL that the function generates for built-in model endpoints refers to your cluster's project and region or location. If you want to refer to another project, then ensure that you specify the `model_request_url` explicitly.  
  
For a list of request URLs for Vertex AI model endpoints, see Vertex AI model endpoints request URL.  
  
For custom hosted model endpoints, ensure that the model endpoint is accessible from the network where AlloyDB is located.  
`PROVIDER_ID` | required for text embedding model endpoints with built-in support | The provider of the model endpoint. The default value is `custom`.  
  
Set to one of the following:

  * `google` for Vertex AI model endpoints
  * `open_ai` for OpenAI model endpoints
  * `hugging_face` for Hugging Face model endpoints
  * `anthropic` for Anthropic model endpoints
  * `custom` for other providers

  
`MODEL_TYPE` | optional for generic model endpoints | The model type.   
  
Set to one of the following:

  * `text_embedding` for text embedding model endpoints
  * `generic` for all other model endpoints

  
`MODEL_QUALIFIED_NAME` | required for text embedding models with built-in support; optional for other model endpoints | The fully qualified name for text embedding models with built-in support.   
  
For Vertex AI qualified names that you must use for pre-registered models, see Pre-registered Vertex AI models.  
  
For qualified names that you must use for OpenAI models with built-in support, see Models with built-in support  
`AUTH_TYPE` | optional unless the model endpoint has specific authentication requirement | The authentication type used by the model endpoint.   
  
You can set it to either `alloydb_service_agent_iam` for Vertex AI models or `secret_manager` for other providers, if they use Secret Manager for authentication.   
  
You don't need to set this value if you are using authentication headers.  
`AUTH_ID` | don't set for Vertex AI model endpoints; required for all other model endpoints that store secrets in Secret Manager | The secret ID that you set and is subsequently used when registering a model endpoint.  
`GENERATE_HEADER_FUNCTION` | optional | The name of the function that generates custom headers.   
  
For Anthropic models, model endpoint management provides a `google_ml.anthropic_claude_header_gen_fn` function that you can use for default versions.   
  
The signature of this function depends on the prediction function that you use. See Header generation function.  
`INPUT_TRANSFORM_FUNCTION` | optional for text embedding model endpoints with built-in support; don't set for generic model endpoints | The function to transform input of the corresponding prediction function to the model-specific input. See Transform functions.  
`OUTPUT_TRANSFORM_FUNCTION` | optional for text embedding model endpoints with built-in support; don't set for generic model endpoints | The function to transform model specific output to the prediction function output. See Transform functions.  
  
### `google_ml.alter_model()`

The following shows how to call the `google_ml.alter_model()` SQL function used to update model endpoint metadata:
    
    
        CALL
        google_ml.alter_model(
          model_id => 'MODEL_ID',
          model_request_url => 'REQUEST_URL',
          model_provider => 'PROVIDER_ID',
          model_type => 'MODEL_TYPE',
          model_qualified_name => 'MODEL_QUALIFIED_NAME',
          model_auth_type => 'AUTH_TYPE',
          model_auth_id => 'AUTH_ID',
          generate_headers_fn => 'GENERATE_HEADER_FUNCTION',
          model_in_transform_fn => 'INPUT_TRANSFORM_FUNCTION',
          model_out_transform_fn => 'OUTPUT_TRANSFORM_FUNCTION');
    

For information about the values that you must set for each parameter, see Create a model.

### `google_ml.drop_model()` function

The following shows how to call the `google_ml.drop_model()` SQL function used to drop a model endpoint:
    
    
      CALL google_ml.drop_model('MODEL_ID');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you defined.  
  
### `google_ml.list_model()` function

The following shows how to call the `google_ml.list_model()` SQL function used to list model endpoint information:
    
    
      SELECT google_ml.list_model('MODEL_ID');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you defined.  
  
### `google_ml.model_info_view` view

The following shows how to call the `google_ml.model_info_view` view that is used to list model endpoint information for all model endpoints:
    
    
      SELECT * FROM google_ml.model_info_view;
    

## Secrets

Use this reference to understand parameters for functions that let you manage secrets.

### `google_ml.create_sm_secret()` function

The following shows how to call the `google_ml.create_sm_secret()` SQL function used to add the secret created in Secret Manager:
    
    
        CALL
        google_ml.create_sm_secret(
          secret_id => 'SECRET_ID',
          secret_path => 'projects/project-id/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
    

Parameter | Description  
---|---  
`SECRET_ID` | The secret ID that you set and is subsequently used when registering a model endpoint.  
`PROJECT_ID` | The ID of your Google Cloud project that contains the secret.  
`SECRET_MANAGER_SECRET_ID` | The secret ID set in Secret Manager when you created the secret.  
`VERSION_NUMBER` | The version number of the secret ID.  
  
### `google_ml.alter_sm_secret()` function

The following shows how to call the `google_ml.alter_sm_secret()` SQL function used to update secret information:
    
    
      CALL
        google_ml.alter_sm_secret(
          secret_id => 'SECRET_ID',
          secret_path => 'projects/project-id/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
    

For information about the values that you must set for each parameter, see Create a secret.

### `google_ml.drop_sm_secret()` function

The following shows how to call the `google_ml.drop_sm_secret()` SQL function used to drop a secret:
    
    
      CALL google_ml.drop_sm_secret('SECRET_ID');
    

Parameter | Description  
---|---  
`SECRET_ID` | The secret ID that you set and was subsequently used when registering a model endpoint.  
  
## Prediction functions

Use this reference to understand parameters for functions that let you generate embeddings or invoke predictions.

### `google_ml.embedding()` function

The following shows how to generate embeddings:
    
    
    SELECT
      google_ml.embedding(
        model_id => 'MODEL_ID',
        contents => 'CONTENT');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you define.  
`CONTENT` | The text to translate into a vector embedding.  
  
For example SQL queries to generate text embeddings, see [Transform function examples for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/model-endpoint-embeddings#generate_embeddings).

### `google_ml.predict_row()` function

The following shows how to invoke predictions:
    
    
    SELECT
      google_ml.predict_row(
        model_id => 'MODEL_ID',
        request_body => 'REQUEST_BODY');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you define.  
`REQUEST_BODY` | The parameters to the prediction function, in JSON format.  
  
For example SQL queries to invoke predictions, see [Examples for AlloyDB Omni](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/model-endpoint-predictions#examples).

## Transform functions

Use this reference to understand parameters for input and output transform functions.

### Input transform function

The following shows the signature for the prediction function for text embedding model endpoints:
    
    
      CREATE OR REPLACE FUNCTION INPUT_TRANSFORM_FUNCTION(model_id VARCHAR(100), input_text TEXT) RETURNS JSON;
    

Parameter | Description  
---|---  
`INPUT_TRANSFORM_FUNCTION` | The function to transform input of the corresponding prediction function to the model endpoint-specific input.  
  
### Output transform function

The following shows the signature for the prediction function for text embedding model endpoints:
    
    
      CREATE OR REPLACE FUNCTION OUTPUT_TRANSFORM_FUNCTION(model_id VARCHAR(100), response_json JSON) RETURNS real[];
    

Parameter | Description  
---|---  
`OUTPUT_TRANSFORM_FUNCTION` | The function to transform model endpoint-specific output to the prediction function output.  
  
### Transform functions example

To better understand how to create transform functions for your model endpoint, consider a custom-hosted text embedding model endpoint that requires JSON input and output.

The following example cURL request creates embeddings based on the prompt and the model endpoint:
    
    
      curl -m 100 -X POST https://cymbal.com/models/text/embeddings/v1 \
        -H "Content-Type: application/json" 
        -d '{"prompt": ["AlloyDB Embeddings"]}'

The following example response is returned:
    
    
    [[ 0.3522231  -0.35932037  0.10156056  0.17734447 -0.11606089 -0.17266059
       0.02509351  0.20305622 -0.09787305 -0.12154685 -0.17313677 -0.08075467
       0.06821183 -0.06896557  0.1171584  -0.00931572  0.11875633 -0.00077482
       0.25604948  0.0519384   0.2034983  -0.09952664  0.10347155 -0.11935943
      -0.17872004 -0.08706985 -0.07056875 -0.05929353  0.4177883  -0.14381726
       0.07934926  0.31368294  0.12543282  0.10758053 -0.30210832 -0.02951015
       0.3908268  -0.03091059  0.05302926 -0.00114946 -0.16233777  0.1117468
      -0.1315904   0.13947351 -0.29569918 -0.12330773 -0.04354299 -0.18068913
       0.14445548  0.19481727]]
    

Based on this input and response, we can infer the following:

  * The model expects JSON input through the `prompt` field. This field accepts an array of inputs. As the `google_ml.embedding()` function is a row level function, it expects one text input at a time. Thus,you need to create an input transform function that builds an array with single element.

  * The response from the model is an array of embeddings, one for each prompt input to the model. As the `google_ml.embedding()` function is a row level function, it returns single input at a time. Thus, you need to create an output transform function that can be used to extract the embedding from the array.




The following example shows the input and output transform functions that is used for this model endpoint when it is registered with model endpoint management:

### input transform function
    
    
    CREATE OR REPLACE FUNCTION cymbal_text_input_transform(model_id VARCHAR(100), input_text TEXT)
    RETURNS JSON
    LANGUAGE plpgsql
    AS $$
    DECLARE
      transformed_input JSON;
      model_qualified_name TEXT;
    BEGIN
      SELECT json_build_object('prompt', json_build_array(input_text))::JSON INTO transformed_input;
      RETURN transformed_input;
    END;
    $$;
    

### output transform function
    
    
    CREATE OR REPLACE FUNCTION cymbal_text_output_transform(model_id VARCHAR(100), response_json JSON)
    RETURNS REAL[]
    LANGUAGE plpgsql
    AS $$
    DECLARE
      transformed_output REAL[];
    BEGIN
    SELECT ARRAY(SELECT json_array_elements_text(response_json->0)) INTO transformed_output;
    RETURN transformed_output;
    END;
    $$;
    

## HTTP header generation function

The following shows signature for the header generation function that can be used with the `google_ml.embedding()` prediction function when registering other text embedding model endpoints.
    
    
      CREATE OR REPLACE FUNCTION GENERATE_HEADERS(model_id VARCHAR(100), input_text TEXT) RETURNS JSON;
    

For the `google_ml.predict_row()` prediction function, the signature is as follows:
    
    
    CREATE OR REPLACE FUNCTION GENERATE_HEADERS(model_id TEXT, input JSON) RETURNS JSON;
    

Parameter | Description  
---|---  
`GENERATE_HEADERS` | The function to generate custom headers. You can also pass the authorization header generated by the header generation function while registering the model endpoint.  
  
### Header generation function example

To better understand how to create a function that generates output in JSON key value pairs that are used as HTTP headers, consider a custom-hosted text embedding model endpoint.

The following example cURL request passes the `version` HTTP header which is used by the model endpoint:
    
    
      curl -m 100 -X POST https://cymbal.com/models/text/embeddings/v1 \
          -H "Content-Type: application/json" \
          -H "version: 2024-01-01" \
          -d '{"prompt": ["AlloyDB Embeddings"]}'

The model expects text input through the `version` field and returns the version value in JSON format. The following example shows the header generation function that is used for this text embedding model endpoint when it is registered with model endpoint management:
    
    
    CREATE OR REPLACE FUNCTION header_gen_fn(model_id VARCHAR(100), input_text TEXT)
    RETURNS JSON
    LANGUAGE plpgsql
    AS $$
    BEGIN
      RETURN json_build_object('version', '2024-01-01')::JSON;
    END;
    $$;
    

#### Header generation function using API Key

The following examples show how to set up authentication using the API key.

###  embedding model
    
    
    CREATE OR REPLACE FUNCTION header_gen_func(
      model_id VARCHAR(100),
      input_text TEXT
    )
    RETURNS JSON
    LANGUAGE plpgsql
    AS $$
    #variable_conflict use_variable
    BEGIN
      RETURN json_build_object('Authorization', 'API_KEY')::JSON;
    END;
    $$;
    

Replace the `API_KEY` with the API key of the model provider.

###  generic model
    
    
    CREATE OR REPLACE FUNCTION header_gen_func(
      model_id VARCHAR(100),
      response_json JSON
    )
    RETURNS JSON
    LANGUAGE plpgsql
    AS $$
    #variable_conflict use_variable
    DECLARE
    transformed_output REAL[];
    BEGIN
      -- code to add Auth token to API request
    RETURN json_build_object('x-api-key', 'API_KEY', 'anthropic-version', '2023-06-01')::JSON;
    END;
    $$;
    

Replace the `API_KEY` with the API key of the model provider.

## Request URL generation

Use the request URL generation function to infer the request URLs for the model endpoints with built-in support. The following shows the signature for this function:
    
    
    CREATE OR REPLACE FUNCTION GENERATE_REQUEST_URL(provider google_ml.model_provider, model_type google_ml.MODEL_TYPE, model_qualified_name VARCHAR(100), model_region VARCHAR(100) DEFAULT NULL)
    

Parameter | Description  
---|---  
`GENERATE_REQUEST_URL` | The function to generate request URL generated by the extension for model endpoints with built-in support.  
  
## Supported models

You can use model endpoint management to register any text embedding or generic model endpoint. Model endpoint management also includes pre-registered Vertex AI models and models with built-in support. For more information about different model types, see [Model type](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/model-endpoint-overview).

### Pre-registered Vertex AI models

**Note:** Vertex AI model support is governed by Vertex AI model versioning and lifecycle guidelines. For more information about stable versions, see [Model versions and lifecycle](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions).Model type | Model ID | Extension version  
---|---|---  
`generic` | 

  * `gemini-1.5-pro:streamGenerateContent`
  * `gemini-1.5-pro:generateContent`
  * `gemini-1.0-pro:generateContent`

| version 1.4.2 and later  
`text_embedding` | 

  * `textembedding-gecko`
  * `text-embedding-gecko@001`

| version 1.3 and later  
  
### Models with built-in support

###  Vertex AI

Qualified model name | Model type  
---|---  
`text-embedding-gecko@001` | `text-embedding`  
`text-embedding-gecko@003` | `text-embedding`  
`text-embedding-004` | `text-embedding`  
`text-embedding-005` | `text-embedding`  
`text-embedding-preview-0815` | `text-embedding`  
`text-multilingual-embedding-002` | `text-embedding`  
  
###  OpenAI 

Qualified model name | Model type  
---|---  
`text-embedding-ada-002` | `text-embedding`  
`text-embedding-3-small` | `text-embedding`  
`text-embedding-3-large` | `text-embedding`  
  
###  Anthropic 

Qualified model name | Model type  
---|---  
`claude-3-opus-20240229` | `generic`  
`claude-3-sonnet-20240229` | `generic`  
`claude-3-haiku-20240307` | `generic`  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
