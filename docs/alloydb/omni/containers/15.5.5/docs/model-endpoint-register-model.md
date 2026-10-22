---
url: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model/
title: Register and call remote AI models in AlloyDB Omni \u00a0|\u00a0 AlloyDB Omni for containers: 15.5.5 \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T15:27:37.209613+00:00
---

# Register and call remote AI models in AlloyDB Omni  |  AlloyDB Omni for containers: 15.5.5  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model/

This page documents AlloyDB Omni version **15.5.5** using the **containers** deployment option. [Choose a different deployment option](https://docs.cloud.google.com/alloydb/omni/docs/choose-deployment). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB Omni ](https://docs.cloud.google.com/alloydb/omni/docs)
  * [ For containers: 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/overview)



Send feedback 

#  Register and call remote AI models in AlloyDB Omni Stay organized with collections  Save and categorize content based on your preferences. 

Select a documentation version: 15.5.5keyboard_arrow_down

  * [ 15.5.5 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model)
  * [ 15.5.4 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.4/docs/model-endpoint-register-model)
  * [ 15.5.2 ](https://docs.cloud.google.com/alloydb/omni/containers/15.5.2/docs/model-endpoint-register-model)



**Preview — Model endpoint management**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To invoke predictions or generate embeddings using a model, register the model endpoint with model endpoint management.

For more information about the `google_ml.create_model()` function, see [model endpoint management reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint-reference).

Before you register a model endpoint with model endpoint management, you must [enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension) and set up authentication based on the model provider, if your model endpoint requires authentication.

Make sure that you access your database with the `postgres` default username.

### Enable the extension

You must add and enable the `google_ml_integration` extension before you can start using the associated functions. Model endpoint management requires that the `google_ml_integration` extension is installed.

  1. Connect to your database using `psql`.

  2. Optional: If the `google_ml_integration` extension is already installed, alter it to update to the latest version:
         
         ALTER EXTENSION google_ml_integration UPDATE;
         

  3. Add the `google_ml_integration` extension using psql:
         
         CREATE EXTENSION google_ml_integration;
         

  4. Optional: Grant permission to a non-super PostgreSQL user to manage model metadata:
         
         GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA google_ml TO NON_SUPER_USER;
         

Replace `NON_SUPER_USER` with the non-super PostgreSQL username.

  5. Enable model endpoint management on your database:
         
         ALTER SYSTEM SET google_ml_integration.enable_model_support=on;
           SELECT pg_reload_conf();
         




### Set up authentication

The following sections show how to set up authentication before adding a Vertex AI model endpoint or model endpoints by other providers.

#### Set up authentication for Vertex AI

To use the Google Vertex AI model endpoints, you must add Vertex AI permissions to the service account that you used while installing AlloyDB Omni. For more information, see [Configure your AlloyDB Omni installation to query cloud-based models](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-with-alloydb-ai#with-cloud).

#### Set up authentication for other model providers

For all models except Vertex AI models, you can store your API keys or bearer tokens in Secret Manager. This step is optional if your model endpoint doesn't handle authentication through Secret Manager—for example, if your model endpoint uses HTTP headers to pass authentication information or doesn't use authentication at all.

This section explains how to set up authentication if you are using Secret Manager.

To create and use an API key or a bearer token, complete the following steps:

  1. Create the secret in Secret Manager. For more information, see [Create a secret and access a secret version](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version).

The secret name and the secret path is used in the [`google_ml.create_sm_secret()`](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint-reference#google_mlcreate_sm_secret) SQL function.

  2. Grant permissions to the AlloyDB cluster to access the secret.
         
         gcloud secrets add-iam-policy-binding 'SECRET_ID' \
               --member="serviceAccount:SERVICE_ACCOUNT_ID" \
               --role="roles/secretmanager.secretAccessor"
         

Replace the following:

     * `SECRET_ID`: the secret ID in Secret Manager.
     * `SERVICE_ACCOUNT_ID`: the ID of the service account that you created in the previous step. Ensure that this is the same account you used during AlloyDB Omni installation. This includes the full `PROJECT_ID.iam.gserviceaccount.com` suffix. For example: `my-service@my-project.iam.gserviceaccount.com`

You can also grant this role to the service account at the project level. For more information, see [Add Identity and Access Management policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)




## Text embedding models with built-in support

This section shows how to register model endpoints that the model endpoint management provides built-in support for.

#### Vertex AI embedding models

The model endpoint management provides built-in support for all versions of the `text-embedding-gecko` model by Vertex AI. Use the qualified name to set the model version to either `textembedding-gecko@001` or `textembedding-gecko@002`.

Since the `textembedding-gecko` and `textembedding-gecko@001` model endpoint ID is pre-registered with model endpoint management, you can directly use them as the model ID. For these models, the extension automatically sets up default transform functions.

To register the `textembedding-gecko@002` model endpoint version, complete the following steps:

For AlloyDB Omni, make sure that you set up [AlloyDB Omni to query cloud-based Vertex AI models](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-with-alloydb-ai#with-cloud).

  1. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension).

  2. [Connect to your database using `psql`.](https://docs.cloud.google.com/alloydb/omni/15.5.5/docs/run-connect#psql)

  3. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension).

  4. Call the create model function to add the `textembedding-gecko@002` model endpoint:
         
         CALL
           google_ml.create_model(
             model_id => 'textembedding-gecko@002',
             model_provider => 'google',
             model_qualified_name => 'textembedding-gecko@002',
             model_type => 'text_embedding',
             model_auth_type => 'alloydb_service_agent_iam');
         
           The request URL that the function generates refers to the project associated with the AlloyDB Omni service account. If you want to refer to another project, then ensure that you specify the `model_request_url` explicitly.
         




#### Open AI text embedding model

The model endpoint management provides built-in support for the `text-embedding-ada-002` model by OpenAI.The `google_ml_integration` extension automatically sets up default transform functions and invokes calls to the remote model.

The following example adds the `text-embedding-ada-002` OpenAI model endpoint.

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension).
  3. [Add the OpenAI API key as a secret to the Secret Manager for authentication](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#other_model_providers).
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



To generate embeddings, see how to [generate embedding for model endpoints with built-in support](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-embeddings#models_with_built-in_support).

## Other text embedding models

This section shows how to register any custom-hosted text embedding model endpoint or text embedding model endpoints provided by model hosting providers. Based on your model endpoint metadata, you might need to add transform functions, generate HTTP headers, or define endpoints.

#### Custom-hosted text embedding model

This section shows how to register a custom-hosted model endpoint along with creating transform functions, and optionally, custom HTTP headers. AlloyDB Omni supports all custom-hosted model endpoints regardless of where they are hosted.

The following example adds the `custom-embedding-model` custom model endpoint hosted by Cymbal. The `cymbal_text_input_transform` and `cymbal_text_output_transform` transform functions are used to transform the input and output format of the model to the input and output format of the prediction function.

To register custom-hosted text embedding model endpoints, complete the following steps:

  1. Connect to your database using `psql`.

  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension).

  3. [Optional: Add the API key as a secret to the Secret Manager for authentication](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#set_up_authentication_for_custom-hosted_models).

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
  5. Create the input and output transform functions based on the following signature for the prediction function for text embedding model endpoints. For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint-reference#transform-func-example).

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



#### OpenAI Text Embedding 3 Small and Large models

You can register the OpenAI `text-embedding-3-small` and `text-embedding-3-large` model endpoints using the embedding prediction function and transform functions specific to the model endpoint. The following example shows how to register the OpenAI `text-embedding-3-small` model endpoint.

To register the `text-embedding-3-small` embedding model endpoint, do the following:

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension).
  3. [Add the OpenAI API key as a secret to the Secret Manager for authentication](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#other_model_providers). If you have already created a secret for any other OpenAI model, you can reuse the same secret.
  4. Call the secret stored in the Secret Manager:
         
         CALL
           google_ml.create_sm_secret(
             secret_id => 'SECRET_ID',_
             secret_path => 'projects/project-id/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
         

Replace the following:

     * `SECRET_ID`: the secret ID that you set and is subsequently used when registering a model endpoint.
     * `SECRET_MANAGER_SECRET_ID`: the secret ID set in Secret Manager when you created the secret.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `VERSION_NUMBER`: the version number of the secret ID.
  5. Create the input and output transform functions based on the following signature for the prediction function for text embedding models. For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint-reference#transform-func-example). To learn about the input and output formats that OpenAI model endpoints expect, see [Embeddings](https://platform.openai.com/docs/api-reference/embeddings).

The following are example transform functions for the `text-embedding-ada-002`, `text-embedding-3-small`, and `text-embedding-3-large`OpenAI text embedding model endpoints. 
         
         -- Input Transform Function corresponding to openai_text_embedding model endpoint family
         CREATE OR REPLACE FUNCTION openai_text_input_transform(model_id VARCHAR(100), input_text TEXT)
         RETURNS JSON
         LANGUAGE plpgsql
         AS $$
         #variable_conflict use_variable
         DECLARE
           transformed_input JSON;
           model_qualified_name TEXT;
         BEGIN
           SELECT google_ml.model_qualified_name_of(model_id) INTO model_qualified_name;
           SELECT json_build_object('input', input_text, 'model', model_qualified_name)::JSON INTO transformed_input;
           RETURN transformed_input;
         END;
         $$;
         
         -- Output Transform Function corresponding to openai_text_embedding model endpoint family
         CREATE OR REPLACE FUNCTION openai_text_output_transform(model_id VARCHAR(100), response_json JSON)
         RETURNS REAL[]
         LANGUAGE plpgsql
         AS $$
         DECLARE
           transformed_output REAL[];
         BEGIN
           SELECT ARRAY(SELECT json_array_elements_text(response_json->'data'->0->'embedding')) INTO transformed_output;
           RETURN transformed_output;
         END;
         $$;
         

  6. Call the create model function to register the `text-embedding-3-small` embedding model endpoint:
         
         CALL
           google_ml.create_model(
             model_id => 'MODEL_ID',
             model_provider => 'open_ai',
             model_type => 'text_embedding',
             model_auth_type => 'secret_manager',
             model_auth_id => 'SECRET_ID',
             model_qualified_name => 'text-embedding-3-small',
             model_in_transform_fn => 'openai_text_input_transform',
             model_out_transform_fn => 'openai_text_output_transform');
         

Replace the following:

     * `MODEL_ID`: a unique ID for the model endpoint that you define—for example `openai-te-3-small`. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
     * `SECRET_ID`: the secret ID you used earlier in the `google_ml.create_sm_secret()` procedure.



For more information, see how to [generate embedding for other text embedding model endpoints](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-embeddings#other_text_embedding_models).

## Generic models

This section shows how to register any generic model endpoint that is available on a hosted model provider such as Hugging Face, OpenAI, Vertex AI, or any other provider. This section shows examples to register a generic model endpoint hosted on Hugging Face and a generic `gemini-pro` model from Vertex AI Model Garden, which doesn't have built-in support.

You can register any generic model endpoint as long as the input and output is in the JSON format. Based on your model endpoint metadata, you might need to generate HTTP headers or define endpoints.

#### Generic model on Hugging Face

The following example adds the `facebook/bart-large-mnli` custom classification model endpoint hosted on Hugging Face.

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension).
  3. [Add the bearer token as a secret to the Secret Manager for authentication](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#other_model_providers).
  4. Call the secret stored in the Secret Manager:
         
         CALL
           google_ml.create_sm_secret(
             secret_id => 'SECRET_ID',
             secret_path => 'projects/project-id/secrets/SECRE_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
         

Replace the following:

     * `SECRET_ID`: the secret ID that you set and is subsequently used when registering a model endpoint.
     * `SECRET_MANAGER_SECRET_ID`: the secret ID set in Secret Manager when you created the secret.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `VERSION_NUMBER`: the version number of the secret ID.
  5. Call the create model function to register the `facebook/bart-large-mnli` model endpoint:
         
         CALL
           google_ml.create_model(
             model_id => 'MODEL_ID',
             model_provider => 'custom',
             model_request_url => 'REQUEST_URL',
             model_qualified_name => 'MODEL_QUALIFIED_NAME',
             model_auth_type => 'secret_manager',
             model_auth_id => 'SECRET_ID');
         

Replace the following:

     * `MODEL_ID`: a unique ID for the model endpoint that you define—for example, `custom-classification-model`. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
     * `REQUEST_URL`: the model-specific endpoint when adding custom text embedding and generic model endpoints—for example, `https://api-inference.huggingface.co/models/facebook/bart-large-mnli`.
     * `MODEL_QUALIFIED_NAME`: the fully qualified name of the model endpoint version-for example, `facebook/bart-large-mnli`.
     * `SECRET_ID`: the secret ID you used earlier in the `google_ml.create_sm_secret()` procedure.



#### Gemini model

Ensure that you set up [AlloyDB Omni to query cloud-based Vertex AI models](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/install-with-alloydb-ai#with-cloud).

The following example adds the `gemini-1.0-pro` model endpoint from the Vertex AI Model Garden.

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-register-model#enable-extension).
  3. Call the create model function to register the `gemini-1.0-pro` model:
         
         CALL
           google_ml.create_model(
             model_id => 'MODEL_ID',
             model_request_url => 'https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-1.0-pro:streamGenerateContent',
             model_provider => 'google',
             model_auth_type => 'alloydb_service_agent_iam');
         

Replace the following:

     * `MODEL_ID`: a unique ID for the model endpoint that you define—for example, `gemini-1`. This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
     * `PROJECT_ID`: the ID of your Google Cloud project.



For more information, see how to [invoke predictions for generic model endpoints](https://docs.cloud.google.com/alloydb/omni/containers/15.5.5/docs/model-endpoint-predictions#invoke_predictions_for_generic_models).

## What's next

  * Learn about the [model endpoint management reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
