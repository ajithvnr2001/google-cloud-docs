---
url: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-register-model/
title: Register and call remote AI models using model endpoint management \u00a0|\u00a0 Cloud SQL for MySQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:18:37.948601+00:00
---

# Register and call remote AI models using model endpoint management  |  Cloud SQL for MySQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-register-model/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Cloud SQL ](https://docs.cloud.google.com/sql/docs)
  * [ MySQL ](https://docs.cloud.google.com/sql/docs/mysql)
  * [ Guides ](https://docs.cloud.google.com/sql/docs/mysql/features)



Send feedback 

#  Register and call remote AI models using model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

MySQL | [PostgreSQL](https://docs.cloud.google.com/sql/docs/postgres/model-endpoint-register-model "View this page for the PostgreSQL database engine") | SQL Server

This page describes how to invoke predictions or generate embeddings using a model, and then register the model endpoint with model endpoint management.

For more information about the `mysql.ml_create_model_registration()` function, see [Model endpoint management reference](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-management-reference).

## Before you begin

  * Based on the model provider, set up authentication.


  * [Connect to your primary instance using either a `mysql` client](https://docs.cloud.google.com/sql/docs/mysql/connect-admin-ip) or [Cloud SQL Studio](https://docs.cloud.google.com/sql/docs/mysql/manage-data-using-studio).

  * Make sure that you connect to the database as a MySQL database user with the database privileges described in [Required database user privileges](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-overview#req-mysql-user).




### Set up authentication

The following sections show how to set up authentication before adding a Vertex AI model endpoint or model endpoints hosted within Google Cloud.

#### Set up authentication for Vertex AI

To use the Google Vertex AI model endpoints, you must add Vertex AI permissions to the IAM-based Cloud SQL service account you use to connect to the database. For more information about integrating with Vertex AI, see [Integrate Cloud SQL with Vertex AI](https://docs.cloud.google.com/sql/docs/mysql/integrate-cloud-sql-with-vertex-ai).

#### Set up authentication for custom-hosted models

This section explains how to set up authentication if you're using Secret Manager. For all models except Vertex AI model endpoints, you can store your API keys or bearer tokens in Secret Manager.

If your model endpoint doesn't handle authentication through Secret Manager, then this section is optional. For example, if your model endpoint uses HTTP headers to pass authentication information or doesn't use authentication at all, then don't complete the steps in this section.

To create and use an API key or a bearer token, complete the following steps:

  1. Create a secret in Secret Manager. For more information, see [Create a secret and access a secret version](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version).

The secret name and the secret path are used in the [`mysql.ml_create_sm_secret_registration()`](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-management-reference#mysqlml_create_sm_secret_registration) SQL function.

  2. Grant permissions to the Cloud SQL instance to access the secret.
         
         gcloud secrets add-iam-policy-binding SECRET_ID \
               --member="serviceAccount:SERVICE_ACCOUNT_EMAIL" \
               --role="roles/secretmanager.secretAccessor"
         

Replace the following:

     * `SECRET_ID`: the secret ID in Secret Manager.
     * `SERVICE_ACCOUNT_EMAIL`: the email address of the IAM-based Cloud SQL service account. To find this email address, use the `[gcloud sql instances describe](https://docs.cloud.google.com/sdk/gcloud/reference/sql/instances/describe) INSTANCE_NAME` command and replace INSTANCE_NAME with the name of the instance. The value that appears next to the `serviceAccountEmailAddress` parameter is the email address.



## Text embedding models with built-in support

This section shows how to register model endpoints for model endpoint management.

### Vertex AI embedding models

Model endpoint management provides built-in support for all versions of the `text-embedding-gecko`, `text-embedding`, and `gemini-embedding` models by Vertex AI. Use the qualified name to set the model version to either `textembedding-gecko@001` or `textembedding-gecko@002`.

Because Vertex AI embedding model endpoint IDs are supported by default with model endpoint management, you can use any of them directly as the model ID. For these models, the embedding function automatically performs input and output transformation. 

Ensure that both the Cloud SQL instance and the Vertex AI model that you're querying are in the same region.

To register the `gemini-embedding-001` model endpoint, call the `ml_create_model_registration` function:
    
    
      CALL
        mysql.ml_create_model_registration(
          'gemini-embedding-001',
          'publishers/google/models/gemini-embedding-001',
          'google','text_embedding', 'gemini-embedding-001',
          'AUTH_TYPE_CLOUDSQL_SERVICE_AGENT_IAM',
           NULL,
          'mysql.cloudsql_ml_text_embedding_input_transform',
          'mysql.cloudsql_ml_text_embedding_output_transform', NULL);
    

## Custom-hosted text embedding models

This section shows how to register custom model endpoints hosted in networks within Google Cloud.

Adding custom-hosted text embedding model endpoints involves creating transform functions, and optionally, custom HTTP headers. On the other hand, adding custom-hosted generic model endpoints involves optionally generating custom HTTP headers and setting the model request URL.

The following example adds the `custom-embedding-model` text embedding model endpoint hosted by Cymbal, which is hosted within Google Cloud. The `cymbal_text_input_transform` and `cymbal_text_output_transform` transform functions are used to transform the input and output format of the model to the input and output format of the prediction function.

To register custom-hosted text embedding model endpoints, complete the following steps:

  1. Call the secret stored in the Secret Manager:
         
         CALL
           mysql.ml_create_sm_secret_registration(
             'SECRET_ID',
             'projects/project-id/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
         

Replace the following:

     * `SECRET_ID`: the secret ID that you set and is subsequently used when registering a model endpoint—for example, `key1`.
     * `SECRET_MANAGER_SECRET_ID`: the secret ID set in Secret Manager when you created the secret.
     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `VERSION_NUMBER`: the version number of the secret ID.
**Note:** Secret Manager generates an `Authorization: Bearer SECRET_VALUE_FROM_SECRET_MANAGER ` header for authentication by default. If this format matches your model endpoint's authorization bearer token format, then you don't have to generate auth headers using the header generation function.
  2. Create the input and output transform functions based on the following signature for the prediction function for text embedding model endpoints. For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-management-reference#transform-func-example).

The following are example transform functions that are specific to the `custom-embedding-model` text embedding model endpoint:

**Note:** If you're parsing a vector from a JSON object in your output transform in Cloud SQL for MySQL 9.7 or later, then make sure that you use `JSON_UNQUOTE` or `JSON_VALUE` to extract the value as a string. `string_to_vector` in MySQL 9.7 and later won't accept JSON input.
         
         -- Input Transform Function corresponding to the custom model endpoint
         DELIMITER $$
         CREATE FUNCTION IF NOT EXISTS cymbal_text_input_transform(model_id VARCHAR(100), input_text TEXT)
         RETURNS JSON
         DETERMINISTIC
         
         BEGIN
           RETURN JSON_OBJECT('prompt', JSON_ARRAY(input_text));
         END $$
         
         -- Output Transform Function corresponding to the custom model endpoint
         CREATE FUNCTION IF NOT EXISTS cymbal_text_output_transform(model_id VARCHAR(100), response_json JSON)
         RETURNS BLOB
         DETERMINISTIC
         
         BEGIN
           RETURN STRING_TO_VECTOR(
                  JSON_EXTRACT(JSON_UNQUOTE(
                       content,
                       '$.predictions[0].embeddings.values'
                     ))
              );
         
         END $$
         DELIMITER ;
         

  3. Call the create model function to register the custom embedding model endpoint:



    
    
       CALL
          mysql.ml_create_model_registration(
            'MODEL_ID',
            'REQUEST_URL',
            'custom',
            'text_embedding',
            'MODEL_QUALIFIED_NAME',
            'auth_type_secret_manager',
            'SECRET_ID'
            'database_name.cymbal_text_input_transform',
            'database_name.cymbal_text_output_transform', NULL);
    

Replace the following:

  * `MODEL_ID`: required. A unique ID for the model endpoint that you define (for example, `custom-embedding-model`). This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
  * `REQUEST_URL`: required. The model-specific endpoint when adding custom text embedding and generic model endpoints—for example, `https://cymbal.com/models/text/embeddings/v1`. Ensure that the model endpoint is accessible through an internal IP address. Model endpoint management doesn't support external IP addresses.
  * `MODEL_QUALIFIED_NAME`: required if your model endpoint uses a qualified name. The fully qualified name in case the model endpoint has multiple versions.
  * `SECRET_ID`: the secret ID you used earlier in the `mysql.ml_create_sm_secret_registration()` procedure.



## Generic models

This section shows how to register a generic `gemini-flash` model endpoint from Vertex AI Model Garden, which is pre-registered in the catalog by default. You can register any generic model endpoint that is hosted within Google Cloud. 

Cloud SQL only supports model endpoints that are available through Vertex AI Model Garden and model endpoints hosted in networks within Google Cloud.

### Gemini model

The following example uses the `gemini-2.5-flash` model endpoint from the Vertex AI Model Garden.

To register the `gemini-2.5-flash` model endpoint, call the `mysql.ml_create_model_registration` function:
    
    
        CALL
          mysql.ml_create_model_registration(
            'MODEL_ID',
            'https://us-central1-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/us-central1/publishers/google/models/gemini-2.5-flash:streamGenerateContent',
            'google',
            'auth_type_cloudsql_service_agent_iam',
            NULL, NULL, NULL, NULL);
    

Replace the following:

  * `MODEL_ID`: a unique ID for the model endpoint that you define (for example,  
`gemini-1`). This model ID is referenced for metadata that the model endpoint needs to generate embeddings or invoke predictions.
  * `PROJECT_ID`: the ID of your Google Cloud project.



For more information, see how to [invoke predictions for generic model endpoints](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-predictions#invoke_predictions_for_generic_models).

## What's next

  * Learn about the [model endpoint management reference](https://docs.cloud.google.com/sql/docs/mysql/model-endpoint-management-reference).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
