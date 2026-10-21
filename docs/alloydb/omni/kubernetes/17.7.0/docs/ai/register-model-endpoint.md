---
url: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint/
title: Register and call remote AI models in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni using the container orchestrator: 17.7.0 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-20T19:32:18.525626+00:00
---

# Register and call remote AI models in AlloyDB Omni  |  AlloyDB Omni using the container orchestrator: 17.7.0  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint/

This page documents AlloyDB Omni version **17.7.0** using the **container orchestrator** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ Container orchestrator: 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/overview)



Send feedback 

#  Register and call remote AI models in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 17.7.0keyboard_arrow_down

  * [ Current (18.4.0) ](https://docs.cloud.google.com/alloydb/omni/kubernetes/current/docs/ai/register-model-endpoint)
  * [ 18.4.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.4.0/docs/ai/register-model-endpoint)
  * [ 18.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.3.0/docs/ai/register-model-endpoint)
  * [ 18.1.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/18.1.0/docs/ai/register-model-endpoint)
  * [ 17.10.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.10.0/docs/ai/register-model-endpoint)
  * [ 17.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.9.0/docs/ai/register-model-endpoint)
  * [ 17.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint)
  * [ 17.5.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.5.0/docs/ai/register-model-endpoint)
  * [ 16.14.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.14.0/docs/ai/register-model-endpoint)
  * [ 16.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.13.0/docs/ai/register-model-endpoint)
  * [ 16.11.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.11.0/docs/ai/register-model-endpoint)
  * [ 16.9.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.9.0/docs/ai/register-model-endpoint)
  * [ 16.8.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.8.0/docs/ai/register-model-endpoint)
  * [ 16.3.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/16.3.0/docs/ai/register-model-endpoint)
  * [ 15.18.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.18.0/docs/ai/register-model-endpoint)
  * [ 15.17.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.17.0/docs/ai/register-model-endpoint)
  * [ 15.15.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.15.0/docs/ai/register-model-endpoint)
  * [ 15.13.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.13.0/docs/ai/register-model-endpoint)
  * [ 15.12.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.12.0/docs/ai/register-model-endpoint)
  * [ 15.7.1 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.1/docs/ai/register-model-endpoint)
  * [ 15.7.0 ](https://docs.cloud.google.com/alloydb/omni/kubernetes/15.7.0/docs/ai/register-model-endpoint)

To invoke predictions or generate embeddings using a model, register the model endpoint with model endpoint management. 

Before you register a model endpoint with model endpoint management, you must [enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#enable-extension) and set up authentication based on the model provider, if your model endpoint requires authentication.

Make sure that you access your database with the `postgres` default username.

### Enable the extension

You must add and enable the `google_ml_integration` extension before you can start using the associated functions. Model endpoint management requires that the `google_ml_integration` extension is installed.

  1. Verify that the `google_ml_integration.enable_model_support` database flag is set to `on` for an instance. For more information about setting database flags, see [Configure database flags](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/configure-database-flags).

  2. Optional: If the `google_ml_integration` extension is already installed, alter it to update to the latest version:
         
         ALTER EXTENSION google_ml_integration UPDATE;
         

  3. Add the `google_ml_integration` extension using psql:
         
         CREATE EXTENSION IF NOT EXISTS google_ml_integration;
         

  4. Optional: Grant permission to a non-super PostgreSQL user to manage model metadata:
         
         GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA google_ml TO NON_SUPER_USER;
         

Replace `NON_SUPER_USER` with the non-super PostgreSQL username.

  5. Enable model endpoint management on your database:
         
         ALTER SYSTEM SET google_ml_integration.enable_model_support=on;
           SELECT pg_reload_conf();
         

  6. Ensure that outbound connectivity is enabled.




### Set up authentication

The following sections show how to set up authentication before registering a model endpoint.

#### Set up authentication for Vertex AI

To use the Google Vertex AI model endpoints, you must add Vertex AI permissions to the service account that you used while installing AlloyDB Omni. For more information, see [Configure your AlloyDB Omni installation to query cloud-based models](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-with-alloydb-ai#with-cloud).

#### Set up authentication using Secret Manager

This step is optional if your model endpoint doesn't handle authentication through Secret Manager—for example, if your model endpoint uses HTTP headers to pass authentication information or doesn't use authentication at all.

To create and use an API key or a bearer token, complete the following steps:

  1. Create the secret in Secret Manager. For more information, see [Create a secret and access a secret version](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version).

The secret path is used in the [`google_ml.create_sm_secret()`](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint#alter-secret) SQL function.

  2. Grant permissions to the AlloyDB cluster to access the secret.
         
         gcloud secrets add-iam-policy-binding 'SECRET_NAME' \
               --member="serviceAccount:SERVICE_ACCOUNT_ID" \
               --role="roles/secretmanager.secretAccessor"
         

Replace the following:

     * `SECRET_NAME`: the secret name in Secret Manager.
     * `SERVICE_ACCOUNT_ID`: the ID of the service account that you created in the previous step. Ensure that this is the same account you used during AlloyDB Omni installation. This includes the full `PROJECT_ID.iam.gserviceaccount.com` suffix. For example: `my-service@my-project.iam.gserviceaccount.com`

You can also grant this role to the service account at the project level. For more information, see [Add Identity and Access Management policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)




#### Set up authentication using headers

The following example shows how to set up authentication using a function that returns a JSON object that contains the headers that are required to make a request to the embedding model.
    
    
      CREATE OR REPLACE FUNCTION HEADER_GEN_FUNCTION(
        model_id VARCHAR(100),
        input_text TEXT
      )
      RETURNS JSON
      LANGUAGE plpgsql
      AS $$
      #variable_conflict use_variable
      DECLARE
        api_key VARCHAR(255) := 'API_KEY';
        header_json JSON;
      BEGIN
        header_json := json_build_object(
          'Content-Type', 'application/json',
          'Authorization', 'Bearer ' || api_key
        );
        RETURN header_json;
      END;
      $$;
    

Replace the following:

  * `HEADER_GEN_FUNCTION`: the name of the header generation function that you can use when registering a model.
  * `API_KEY`: the API key of the model provider.



## Text embedding models

This section shows how to register model endpoints with model endpoint management.

The model endpoint management supports some text embedding and generic Vertex AI models as pre-registered model endpoints. You can directly use the model ID to generate embeddings or invoke predictions, based on the model type. For more information about supported pre-registered models, see [Pre-registered Vertex AI models](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint#pre-registered-models).

**Note:** Vertex AI model support is governed by Vertex AI model versioning and lifecycle guidelines. For more information about stable versions, see [Model versions and lifecycle](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions).

For example, to call the pre-registered `textembedding-gecko` model, you can directly call the model using the embedding function:  
  

    
    
    SELECT
          google_ml.embedding(
            model_id => 'textembedding-gecko',
            content => 'AlloyDB is a managed, cloud-hosted SQL database service');
    

Similarly, to call the pre-registered `gemini-1.5-pro:generateContent` model, you can directly call the model using the prediction function:  
  

    
    
     SELECT
            json_array_elements(
            google_ml.predict_row(
                model_id => 'gemini-1.5-pro:generateContent',
                request_body => '{
            "contents": [
                {
                    "role": "user",
                    "parts": [
                        {
                            "text": "For TPCH database schema as mentioned here https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf , generate a SQL query to find all supplier names which are located in the India nation."
                        }
                    ]
                }
            ]
            }'))-> 'candidates' -> 0 -> 'content' -> 'parts' -> 0 -> 'text'; 
    

To generate embeddings, see how to [generate embedding for pre-registered model endpoints](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/model-endpoint-embeddings#pre-registered-models). To invoke predictions, see how to [invoke predictions for pre-registered model endpoints](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/model-endpoint-predictions#invoke_predictions_for_generic_models).

### Text embedding models with built-in support

The model endpoint management provides built-in support for some models by Vertex AI and OpenAI. For the list of models with built-in support, see [Models with built-in support](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint#models-built-in).

For models with built-in support, you can set the qualified name as the model qualified name and specify the request URL. Model endpoint management automatically identifies the model and sets up default transform functions.

#### Vertex AI embedding models

**Note:** Use the [public.embedding() function](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/work-with-embeddings) to query Vertex AI models without registration or customization. For passing any custom information such as the task type, you must register the Vertex AI model, and then use the `google_ml.embedding()` function.

The following steps show how to register Vertex AI models with built-in support. The `text-embedding-005` and the `text-multilingual-embedding-002` model endpoint is used as an example.

**Note:** Only the `text-multilingual-embedding-002` model endpoint requires setting up transform functions provided by model endpoint management.

For AlloyDB Omni, make sure that you set up [AlloyDB Omni to query cloud-based Vertex AI models](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-with-alloydb-ai#with-cloud).

  1. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#enable-extension).

  2. Connect to your database using `psql`.

  3. Call the create model function to add the model endpoint:

###  text-embedding-005 
         
         CALL
             google_ml.create_model(
               model_id => 'text-embedding-005',
               model_request_url => 'publishers/google/models/text-embedding-005',
               model_provider => 'google',
               model_qualified_name => 'text-embedding-005',
               model_type => 'text_embedding',
               model_auth_type => 'alloydb_service_agent_iam');
         

###  text-multilingual-embedding-002 
         
         CALL
             google_ml.create_model(
               model_id => 'text-multilingual-embedding-002',
               model_request_url => 'publishers/google/models/text-multilingual-embedding-002',
               model_provider => 'google',
               model_qualified_name => 'text-multilingual-embedding-002',
               model_type => 'text_embedding',
               model_auth_type => 'alloydb_service_agent_iam'
               model_in_transform_fn => 'google_ml.vertexai_text_embedding_input_transform',
               model_out_transform_fn => 'google_ml.vertexai_text_embedding_output_transform');
         




The request URL that the function generates refers to the project associated with the AlloyDB Omni service account. If you want to refer to another project, then ensure that you specify the `model_request_url` explicitly.

If the model is stored in another project and region than your AlloyDB cluster, then set the request URL to `projects/PROJECT_ID/locations/REGION_ID/publishers/google/models/MODEL_ID`, where `REGION_ID` is the region where your model is hosted, and the `MODEL_ID` is the qualified model name.

In addition, [grant the Vertex AI User (`roles/aiplatform.user`) role](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-with-alloydb-ai#with-cloud) to service account of the project where AlloyDB Omni is installed so that the model hosted in the other project can be accessed.

#### Open AI text embedding model

The `google_ml_integration` extension automatically sets up default transform functions and invokes calls to the remote OpenAI models. For the list of OpenAI models with built-in support, see [Models with built-in support](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint#models-built-in).

The following example adds the `text-embedding-ada-002` OpenAI model endpoint. You can register the OpenAI `text-embedding-3-small` and `text-embedding-3-large` model endpoints using the same steps and setting the model qualified names specific to the models.

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#enable-extension).
  3. [Add the OpenAI API key as a secret to the Secret Manager for authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#setup-secret-manager).
  4. Call the secret stored in the Secret Manager:
         
         CALL
         google_ml.create_sm_secret(
           secret_id => 'SECRET_ID',
           secret_path => 'projects/PROJECT_ID/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
         

Replace the following:

     * `SECRET_ID`: the secret ID that you set and is subsequently used when registering a model endpoint—for example, `key1`.
     * `SECRET_MANAGER_SECRET_ID`: the secret ID set in Secret Manager when you created the secret.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `VERSION_NUMBER`: the version number of the secret ID.
  5. Call the create model function to register the `text-embedding-ada-002` model endpoint:
         
         CALL
           google_ml.create_model(
             model_id => 'MODEL_ID',
             model_provider => 'open_ai',
             model_type => 'text_embedding',
             model_qualified_name => 'text-embedding-ada-002',
             model_auth_type => 'secret_manager',
             model_auth_id => 'SECRET_ID');
         

Replace the following:

     * `MODEL_ID`: a unique ID for the model endpoint that you define. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
     * `SECRET_ID`: the secret ID you used earlier in the `google_ml.create_sm_secret()` procedure.



To generate embeddings, see how to [generate embedding for model endpoints with built-in support](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/model-endpoint-embeddings#models_with_built-in_support).

### Custom-hosted text embedding model

This section shows how to register a custom-hosted model endpoint along with creating transform functions, and optionally, custom HTTP headers. All custom-hosted model endpoints are supported regardless of where they are hosted.

The following example adds the `custom-embedding-model` custom model endpoint hosted by Cymbal. The `cymbal_text_input_transform` and `cymbal_text_output_transform` transform functions are used to transform the input and output format of the model to the input and output format of the prediction function.

To register custom-hosted text embedding model endpoints, complete the following steps:

  1. Connect to your database using `psql`.

  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#enable-extension).

  3. [Optional: Add the API key as a secret to the Secret Manager for authentication](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#setup-secret-manager).

  4. Call the secret stored in the Secret Manager:
         
         CALL
           google_ml.create_sm_secret(
             secret_id => 'SECRET_ID',
             secret_path => 'projects/project-id/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
         

Replace the following:

     * `SECRET_ID`: the secret ID that you set and is subsequently used when registering a model endpoint—for example, `key1`.
     * `SECRET_MANAGER_SECRET_ID`: the secret ID set in Secret Manager when you created the secret.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `VERSION_NUMBER`: the version number of the secret ID.
**Note:** Secret Manager generates an `Authorization: Bearer SECRET_VALUE_FROM_SECRET_MANAGER` header for authentication by default. If this format matches your model endpoint's authorization bearer token format, then you don't have to generate auth headers using the header generation function.
  5. Create the input and output transform functions based on the following signature for the prediction function for text embedding model endpoints. For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint#transform-func-example).

The following are example transform functions that are specific to the `custom-embedding-model` text embedding model endpoint:
         
         -- Input Transform Function corresponding to the custom model endpoint
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
         -- Output Transform Function corresponding to the custom model endpoint
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
         

  6. Call the create model function to register the custom embedding model endpoint:
         
         CALL
           google_ml.create_model(
             model_id => 'MODEL_ID',
             model_request_url => 'REQUEST_URL',
             model_provider => 'custom',
             model_type => 'text_embedding',
             model_auth_type => 'secret_manager',
             model_auth_id => 'SECRET_ID',
             model_qualified_name => 'MODEL_QUALIFIED_NAME',
             model_in_transform_fn => 'cymbal_text_input_transform',
             model_out_transform_fn => 'cymbal_text_output_transform');
         

Replace the following:

     * `MODEL_ID`: required. A unique ID for the model endpoint that you define-for example `custom-embedding-model`. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
     * `REQUEST_URL`: required. The model-specific endpoint when adding custom text embedding and generic model endpoints—for example, `https://cymbal.com/models/text/embeddings/v1`.
     * `MODEL_QUALIFIED_NAME`: required if your model endpoint uses a qualified name. The fully qualified name in case the model endpoint has multiple versions.
     * `SECRET_ID`: the secret ID you used earlier in the `google_ml.create_sm_secret()` procedure.



## Generic models

This section shows how to register any generic model endpoint that is available on a hosted model provider such as Hugging Face, OpenAI, Vertex AI, Anthropic, or any other provider. This section shows examples to register a generic model endpoint hosted on Hugging Face, a generic `gemini-pro` model from Vertex AI Model Garden, and the `claude-haiku` model endpoint.

You can register any generic model endpoint as long as the input and output is in the JSON format. Based on your model endpoint metadata, you might need to generate HTTP headers or define request URLs.

For more information about pre-registered generic models and models with built-in support, see [Supported models](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint#supported-models).

### Gemini model

Since some `gemini-pro` models are pre-registered, you can directly call the model ID to invoke predictions. Ensure that you set up [AlloyDB Omni to query cloud-based Vertex AI models](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-with-alloydb-ai#with-cloud).

The following example uses the `gemini-1.5-pro:generateContent` model endpoint from the Vertex AI Model Garden.

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#enable-extension).
  3. Invoke predictions using the pre-registered model ID:
         
         SELECT
             json_array_elements(
             google_ml.predict_row(
                 model_id => 'gemini-1.5-pro:generateContent',
                 request_body => '{
             "contents": [
                 {
                     "role": "user",
                     "parts": [
                         {
                             "text": "For TPCH database schema as mentioned here https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf , generate a SQL query to find all supplier names which are located in the India nation."
                         }
                     ]
                 }
             ]
             }'))-> 'candidates' -> 0 -> 'content' -> 'parts' -> 0 -> 'text';
         




### Generic model on Hugging Face

The following example adds the `facebook/bart-large-mnli` custom classification model endpoint hosted on Hugging Face.

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#enable-extension).
  3. Add the OpenAI API key as a secret to the Secret Manager for authentication. If you have already created a secret for any other OpenAI model, you can reuse the same secret.
  4. Call the secret stored in the Secret Manager:
         
         CALL
           google_ml.create_sm_secret(
             secret_id => 'SECRET_ID',
             secret_path => 'projects/project-id/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
         

Replace the following:

     * `SECRET_ID`: the secret ID that you set and is subsequently used when registering a model endpoint.
     * `SECRET_MANAGER_SECRET_ID`: the secret ID set in Secret Manager when you created the secret.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `VERSION_NUMBER`: the version number of the secret ID.
  5. Call the create model function to register the `facebook/bart-large-mnli` model endpoint:
         
         CALL
           google_ml.create_model(
             model_id => 'MODEL_ID',
             model_provider => 'hugging_face',
             model_request_url => 'REQUEST_URL',
             model_qualified_name => 'MODEL_QUALIFIED_NAME',
             model_auth_type => 'secret_manager',
             model_auth_id => 'SECRET_ID');
         

Replace the following:

     * `MODEL_ID`: a unique ID for the model endpoint that you define—for example, `custom-classification-model`. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
     * `REQUEST_URL`: the model-specific endpoint when adding custom text embedding and generic model endpoints—for example, `https://api-inference.huggingface.co/models/facebook/bart-large-mnli`.
     * `MODEL_QUALIFIED_NAME`: the fully qualified name of the model endpoint version-for example, `facebook/bart-large-mnli`.
     * `SECRET_ID`: the secret ID you used earlier in the `google_ml.create_sm_secret()` procedure.



### Anthropic generic model

The following example adds the `claude-3-opus-20240229` model endpoint. Model endpoint management provides the header function required for registering Anthropic models.

Ensure that you set up [AlloyDB Omni to query cloud-based Vertex AI models](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/install-with-alloydb-ai#with-cloud).

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/register-model-endpoint#enable-extension).

###  Secret Manager 

     1. Add the bearer token as a secret to the Secret Manager for authentication.
     2. Call the secret stored in the Secret Manager:
            
            CALL
              google_ml.create_sm_secret(
                secret_id => 'SECRET_ID',
                secret_path => 'projects/project-id/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
            

Replace the following:

        * `SECRET_ID`: the secret ID that you set and is subsequently used when registering a model endpoint.
        * `SECRET_MANAGER_SECRET_ID`: the secret ID set in Secret Manager when you created the secret.
        * `PROJECT_ID`: the ID of your Google Cloud project.
        * `VERSION_NUMBER`: the version number of the secret ID.
     3. Call the create model function to register the `claude-3-opus-20240229` model endpoint.
            
            CALL
              google_ml.create_model(
                model_id => 'MODEL_ID',
                model_provider => 'anthropic',
                model_request_url => 'REQUEST_URL',
                model_auth_type => 'secret_manager',
                model_auth_id => 'SECRET_ID',
                generate_headers_fn => 'google_ml.anthropic_claude_header_gen_fn');
            

Replace the following:

        * `MODEL_ID`: a unique ID for the model endpoint that you define—for example, `anthropic-opus`. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
        * `REQUEST_URL`: the model-specific endpoint when adding custom text embedding and generic model endpoints—for example, `https://api.anthropic.com/v1/messages`.

###  Auth header 

     1. Use the `google_ml.anthropic_claude_header_gen_fn` default header generation function or create a header generation function.
            
            CREATE OR REPLACE FUNCTION anthropic_sample_header_gen_fn(model_id VARCHAR(100), request_body JSON)
              RETURNS JSON
              LANGUAGE plpgsql
              AS $$
              #variable_conflict use_variable
              BEGIN
                    RETURN json_build_object('x-api-key', 'ANTHROPIC_API_KEY', 'anthropic-version', 'ANTHROPIC_VERSION')::JSON;
              END;
              $$;
            

Replace the following:

        * `ANTHROPIC_API_KEY`: the anthropic API key.
        * `ANTHROPIC_VERSION` (Optional): the specific model version you want to use—for example, `2023-06-01`.
     2. Call the create model function to register the `claude-3-opus-20240229` model endpoint.
            
            CALL
              google_ml.create_model(
                model_id => 'MODEL_ID',
                model_provider => 'anthropic',
                model_request_url => 'REQUEST_URL',
                generate_headers_fn => 'google_ml.anthropic_claude_header_gen_fn');
            

Replace the following:

        * `MODEL_ID`: a unique ID for the model endpoint that you define—for example, `anthropic-opus`. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
        * `REQUEST_URL`: the model-specific endpoint when adding custom text embedding and generic model endpoints—for example, `https://api.anthropic.com/v1/messages`.




For more information, see how to [invoke predictions for generic model endpoints](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/ai/model-endpoint-predictions#invoke_predictions_for_generic_models).

## What's next

  * Learn about the [model endpoint management reference](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint).
  * Use [sample templates for registering model endpoints](https://docs.cloud.google.com/alloydb/omni/kubernetes/17.7.0/docs/reference/model-endpoint-sample-template).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
