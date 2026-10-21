---
url: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-management-reference/
title: Model endpoint management reference \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T04:28:56.713113+00:00
---

# Model endpoint management reference  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-management-reference/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Model endpoint management reference Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-management-reference "View this page for the PostgreSQL database engine") | SQL Server

This page lists parameters for different functions provided by Cloud SQL to register and manage model endpoints. The page also lists the secrets that you can manage by using model endpoint management. **Note:** For more information about model endpoint management, see [Model endpoint management overview](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-overview). 

## Models

Use this reference to understand parameters for functions that let you manage model endpoints.

### `mysql.ml_create_model_registration()`

The following shows how to use the `mysql.ml_create_model_registration()` function to register model endpoint metadata:
    
    
      CALL
        mysql.ml_create_model_registration(
          'MODEL_ID',
          'REQUEST_URL',
          'PROVIDER_ID',
          'MODEL_TYPE',
          'MODEL_QUALIFIED_NAME',
          'AUTH_TYPE',
          'AUTH_ID',
          'GENERATE_HEADER_FUNCTION',
          'INPUT_TRANSFORM_FUNCTION',
          'OUTPUT_TRANSFORM_FUNCTION');
    

Parameter | Required | Description  
---|---|---  
`MODEL_ID` | Required for all model endpoints | A unique ID for the model endpoint that you define.  
`REQUEST_URL` | Can be NULL for Vertex AI models | The model-specific endpoint when adding other text embedding and generic model endpoints.  The request URL that the function generates for built-in model endpoints refers to your cluster's project and region or location. If you want to refer to another project, then ensure that you specify the `model_request_url` explicitly. For custom hosted model endpoints, ensure that the model endpoint is accessible through the internet.  
`PROVIDER_ID` | Required for text embedding model endpoints with built-in support | The provider of the model endpoint. The default value is `custom`. For Cloud SQL, set the provider to `google` for Vertex AI model endpoints, `open_ai` for OpenAI model endpoints, `anthropic` for Anthropic model endpoints, `hugging_face` for Hugging Face model endpoints, or `custom` for custom-hosted model endpoints.  
`MODEL_TYPE` | Can be NULL for generic model endpoints | The model type. You can set this value to `text_embedding` for text embedding model endpoints or `generic` for all other model endpoints.  
`MODEL_QUALIFIED_NAME` | Required for OpenAI model endpoints; can be NULL for other model endpoints | The fully qualified name in case the model endpoint has multiple versions or if the model endpoint defines it—for example, `textembedding-gecko@001` or `textembedding-gecko@002`. Since the `textembedding-gecko@001` model is pre-registered with model endpoint management, you can generate embeddings using `textembedding-gecko@001` as the model ID.  
`AUTH_TYPE` | Can be NULL unless model endpoint has specific authentication requirement | The authentication type used by the model endpoint. You can set it to either `auth_type_cloudsql_service_agent_iam` for Vertex AI models or `auth_type_secret_manager` for other providers.  
`AUTH_ID` | Pass as NULL for Vertex AI endpoints; required for all other model endpoints that store secrets in Secret Manager | The secret ID that you set and is subsequently used when registering a model endpoint.  
`GENERATE_HEADER_FUNCTION` | Can be NULL | The function name you set to generate custom headers. The signature of this function depends on the `mysql.ml_predict_row()` function. See HTTP Header generation function.  
`INPUT_TRANSFORM_FUNCTION` | Optional for text embedding model endpoints with built-in support;don't set for generic model endpoints | The function to transform input of the corresponding prediction function to the model-specific input. See Transform functions.  
`OUTPUT_TRANSFORM_FUNCTION` | Optional for text embedding model endpoints with built-in support;don't set for generic model endpoints | The function to transform model specific output to the prediction function output. See Transform functions.  
  
### `mysql.ml_alter_model_registration()`

The following shows how to call the `mysql.ml_alter_model_registration()` SQL function used to update model endpoint metadata:
    
    
        CALL
        mysql.ml_alter_model_registration(
          'MODEL_ID',
          'REQUEST_URL',
          'PROVIDER_ID',
          'MODEL_TYPE',
          'MODEL_QUALIFIED_NAME',
          'AUTH_TYPE',
          'AUTH_ID',
          'GENERATE_HEADER_FUNCTION',
          'INPUT_TRANSFORM_FUNCTION',
          'OUTPUT_TRANSFORM_FUNCTION');
    

### `mysql.ml_drop_model_registration()`

The following shows how to call the `mysql.ml_drop_model_registration()` SQL function used to drop a model endpoint:
    
    
      CALL mysql.ml_drop_model_registration('MODEL_ID');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you define.  
  
### `mysql.ml_list_registered_model()`

The following shows how to call the `mysql.ml_list_registered_model()` SQL function used to list model endpoint information:
    
    
      SELECT mysql.ml_list_registered_model('MODEL_ID');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you define.  
  
### `mysql.cloudsql_ml_models`

The following shows how to query the `mysql.cloudsql_ml_models` table that's used to list model endpoint information for all model endpoints:
    
    
      SELECT * FROM mysql.cloudsql_ml_models;
    

## Secrets

Use this reference to understand parameters for functions that let you manage secrets.

### `mysql.ml_create_sm_secret_registration()`

The following shows how to call the `mysql.ml_create_sm_secret_registration()` SQL function used to add the secret created in Secret Manager:
    
    
        CALL
        mysql.ml_create_sm_secret_registration(
          'SECRET_ID',
          'projects/PROJECT_ID/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
    

Parameter | Description  
---|---  
`SECRET_ID` | The secret ID that you set and is subsequently used when registering a model endpoint.  
`PROJECT_ID` | The ID of your Google Cloud project that contains the secret. This project can be different from the project that contains your Cloud SQL instance.  
`SECRET_MANAGER_SECRET_ID` | The secret ID set in Secret Manager when you created the secret.  
`VERSION_NUMBER` | The version number of the secret ID.  
  
### `mysql.ml_alter_sm_secret_registration()`

The following shows how to call the `mysql.ml_alter_sm_secret_registration()` SQL function used to update secret information:
    
    
      CALL
        mysql.ml_alter_sm_secret_registration(
          'SECRET_ID',
          'projects/PROJECT_ID/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
    

Parameter | Description  
---|---  
`SECRET_ID` | The secret ID that you set and is subsequently used when registering a model endpoint.  
`PROJECT_ID` | The ID of your Google Cloud project that contains the secret. This project can be different from the project that contains your Cloud SQL instance.  
`SECRET_MANAGER_SECRET_ID` | The secret ID set in Secret Manager when you created the secret.  
`VERSION_NUMBER` | The version number of the secret ID.  
  
### `mysql.ml_drop_sm_secret_registration()`

The following shows how to call the `mysql.ml_drop_sm_secret_registration()` SQL function used to drop a secret:
    
    
      CALL mysql.ml_drop_sm_secret_registration('SECRET_ID');
    

Parameter | Description  
---|---  
`SECRET_ID` | The secret ID that you set and is subsequently used when registering a model endpoint.  
  
## Prediction functions

Use this reference to understand parameters for functions that let you generate embeddings or invoke predictions.

### `mysql.ml_embedding()`

The following shows how to generate embeddings:
    
    
    SELECT
      mysql.ml_embedding(
        'MODEL_ID',
        'CONTENT');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you define.  
`CONTENT` | the text to translate into a vector embedding.  
  
For examples of SQL queries to generate text embeddings, see [Examples](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-embeddings#examples).

### `mysql.ml_predict_row()`

The following shows how to invoke predictions:
    
    
    SELECT
      mysql.ml_predict_row(
        'MODEL_ID',
        'REQUEST_BODY');
    

Parameter | Description  
---|---  
`MODEL_ID` | A unique ID for the model endpoint that you define.  
`REQUEST_BODY` | the parameters to the prediction function, in JSON format.  
  
For examples of SQL queries to invoke predictions, see [Examples](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-predictions#examples).

## Transform functions

Use this reference to understand parameters for input and output transform functions.

### Input transform function

The following shows the signature for the prediction function for text embedding model endpoints:
    
    
      CREATE FUNCTION IF NOT EXISTS
      INPUT_TRANSFORM_FUNCTION(model_id VARCHAR(100), input_text TEXT) RETURNS JSON DETERMINISTIC;
    

Parameter | Description  
---|---  
`INPUT_TRANSFORM_FUNCTION` | The function to transform input of the corresponding prediction function to the model endpoint-specific input.  
  
### Output transform function

The following shows the signature for the prediction function for text embedding model endpoints:
    
    
      CREATE FUNCTION IF NOT EXISTS
      OUTPUT_TRANSFORM_FUNCTION(model_id VARCHAR(100), response_json JSON) RETURNS BLOB DETERMINISTIC;
    

Parameter | Description  
---|---  
`OUTPUT_TRANSFORM_FUNCTION` | The function to transform model endpoint-specific output to the prediction function output.  
  
### Transform functions example

To better understand how to create transform functions for your model endpoint, consider a custom-hosted text embedding model endpoint that requires JSON input and output.

The following example curl request creates embeddings based on the prompt and the model endpoint:
    
    
      curl -m 100 -X POST https://cymbal.com/models/text/embeddings/v1 \
        -H "Content-Type: application/json"
        -d '{"prompt": ["Cloud SQL Embeddings"]}'

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
    

Based on this input and response, you can infer the following:

  * The model expects JSON input through the `prompt` field. This field accepts an array of inputs. As the `mysql.ml_embedding()` function is a row level function, it expects one text input at a time. Thus, you need to create an input transform function that builds an array with a single element.

  * The response from the model is an array of embeddings, one for each prompt input to the model. As the `mysql.ml_embedding()` function is a row level function, it returns a single input at a time. Thus, you need to create an output transform function that can be used to extract the embedding from the array.




The following example shows the input and output transform functions that is used for this model endpoint when it is registered with model endpoint management:

### input transform function
    
    
    DELIMITER $$
    CREATE FUNCTION IF NOT EXISTS cymbal_text_input_transform(model_id VARCHAR(100), input_text TEXT)
    RETURNS JSON
    DETERMINISTIC
    
    BEGIN
      RETURN JSON_OBJECT('prompt', JSON_ARRAY(input_text));
    END $$
    

### output transform function
    
    
    CREATE FUNCTION IF NOT EXISTS cymbal_text_output_transform(model_id VARCHAR(100), response_json JSON)
    RETURNS BLOB
    DETERMINISTIC
    
    BEGIN
      RETURN STRING_TO_VECTOR(
             JSON_EXTRACT(
                  content,
                  '$.predictions[0].embeddings.values'
                )
        );
    
    END $$
    DELIMITER ;
    

### Default included transform functions

Model Endpoint Management provides in-built support for two common text embedding model families, Google's Gemini embedding models and OpenAI's text embedding models. The input and output transforms are preloaded when these models are registered, for convenience. They can be overwritten by specifying your own transform functions during registration, or by calling `mysql.ml_alter_model_registration()`.

## HTTP header generation function

The following shows signature for the header generation function that can be used with the `mysql.ml_embedding()` prediction function when registering other text embedding model endpoints.
    
    
      CREATE FUNCTION IF NOT EXISTS GENERATE_HEADERS(model_id VARCHAR(100), input_text TEXT) RETURNS JSON DETERMINISTIC;
    

For the `mysql.ml_predict_row()` prediction function, the signature is as follows:
    
    
    CREATE FUNCTION IF NOT EXISTS GENERATE_HEADERS(model_id TEXT, input JSON) RETURNS JSON DETERMINISTIC;
    

Parameter | Description  
---|---  
`GENERATE_HEADERS` | The function to generate custom headers. You can also pass the authorization header generated by the header generation function while registering the model endpoint.  
  
### Header generation function example

To better understand how to create a function that generates output in JSON key value pairs that are used as HTTP headers, consider a custom-hosted text embedding model endpoint.

The following example curl request passes the `version` HTTP header, which is used by the model endpoint:
    
    
      curl -m 100 -X POST https://cymbal.com/models/text/embeddings/v1 \
          -H "Content-Type: application/json" \
          -H "version: 2024-01-01" \
          -d '{"prompt": ["Cloud SQL Embeddings"]}'

The model expects text input through the `version` field and returns the version value in JSON format. The following example shows the header generation function that is used for this text embedding model endpoint when it is registered with model endpoint management:
    
    
    DELIMITER $$
    CREATE FUNCTION IF NOT EXISTS header_gen_fn(model_id VARCHAR(100), input_text TEXT)
    RETURNS JSON
    DETERMINISTIC
    BEGIN
      RETURN JSON_OBJECT('version', '2024-01-01');
    END;
    $$
    DELIMITER ;
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
