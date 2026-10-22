---
url: https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint/
title: Register and call remote AI models using model endpoint management \u00a0|\u00a0 AlloyDB for PostgreSQL \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:39:03.911730+00:00
---

# Register and call remote AI models using model endpoint management  |  AlloyDB for PostgreSQL  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ AlloyDB for PostgreSQL ](https://docs.cloud.google.com/alloydb/docs)
  * [ Guides ](https://docs.cloud.google.com/alloydb/docs/overview)



Send feedback 

#  Register and call remote AI models using model endpoint management Stay organized with collections  Save and categorize content based on your preferences. 

Model endpoint management in AlloyDB for PostgreSQL lets you register remote AI model endpoints so that you can generate vector embeddings and invoke predictions directly from SQL queries. You can register models hosted on Gemini Enterprise Agent Platform, third-party providers such as OpenAI and Anthropic, or custom-hosted endpoints.

## Before you begin

  * [Verify that the `google_ml_integration` extension is installed](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai#verify-installed-extension).

  * [Verify that the `google_ml_integration.enable_model_support` flag is set to `on`](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags)




### Set up the extension

  1. [Connect to your database using `psql`](https://docs.cloud.google.com/alloydb/docs/connect-psql) or AlloyDB for PostgreSQL Studio using the `postgres` user.

  2. Optional: [Request access to interact with AlloyDB for PostgreSQL AI functions (](https://docs.google.com/forms/d/e/1FAIpQLSfJ9vHIJ79nI7JWBDELPFL75pDQa4XVZQ2fxShfYddW0RwmLw/viewform)[Preview](https://cloud.google.com/products#product-launch-stages)) features including support for multimodal models, ranking models, and operator functions.

  3. Optional: Grant permission to a non-super PostgreSQL user to manage model metadata:
         
         GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA google_ml TO NON_SUPER_USER;
         

Replace the following variable:

     * `NON_SUPER_USER`: the non-super PostgreSQL username.
  4. Ensure that outbound IP is enabled to access models hosted outside of your VPC, such as third-party models. For more information, see [Add outbound connectivity](https://docs.cloud.google.com/alloydb/docs/connect-public-ip#add-outbound-connectivity).




### Set up authentication

The following sections show how to set up authentication before registering a model endpoint.

#### Integrate with Gemini Enterprise Agent Platform and install the extension

To use the Agent Platform model endpoints, you must add Agent Platform permissions to the IAM-based AlloyDB service account you use to connect to the database.

  1. [Configure user access to Agent Platform models](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).
  2. Verify that the latest version of `google_ml_integration` is installed. 
     1. To check the installed version, run the following command:
            
            SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
            extversion 
            ------------
            1.5.2
            (1 row)

     2. If the extension isn't installed or if the installed version is earlier than 1.5.2, update the extension.
            
            CREATE EXTENSION IF NOT EXISTS google_ml_integration;
            ALTER EXTENSION google_ml_integration UPDATE;

If you experience issues when you run the preceding commands, or if the extension isn't updated to version 1.5.2 after you run the preceding commands, contact [Google Cloud support](https://cloud.google.com/support).

  3. To use the AlloyDB AI query engine functionality, set the `google_ml_integration.enable_ai_query_engine` flag to `on`.

### SQL

     1. Enable the AI query engine for the current session.  

            
            SET google_ml_integration.enable_ai_query_engine = on;

     2. Enable features for a specific database across sessions.  

            
            ALTER DATABASE DATABASE_NAME SET google_ml_integration.enable_ai_query_engine = 'on';

     3. Enable the AI query engine for a specific user across sessions and databases.  

            
            ALTER ROLE postgres SET google_ml_integration.enable_ai_query_engine = 'on';

### Console

To modify the value of the `google_ml_integration.enable_ai_query_engine` flag, follow the steps in [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console). 

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

You can modify the value of the `google_ml_integration.enable_ai_query_engine` flag. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console). 
    
    gcloud alloydb instances update INSTANCE_ID \
      --database-flags google_ml_integration.enable_ai_query_engine=on \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID




#### Set up authentication using Secret Manager

This section explains how to set up authentication if you are using Secret Manager to store authentication details for third party providers.

This step is optional if your model endpoint doesn't handle authentication through Secret Manager—for example, if your model endpoint uses HTTP headers to pass authentication information or doesn't use authentication at all.

To create and use an API key or a bearer token, complete the following steps:

  1. Create the secret in Secret Manager. For more information, see [Create a secret and access a secret version](https://docs.cloud.google.com/secret-manager/docs/create-secret-quickstart#create_a_secret_and_access_a_secret_version).

The secret path is used in the [`google_ml.create_sm_secret()`](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint#create-secret) SQL function.

  2. Grant permissions to the AlloyDB cluster to access the secret.
         
         gcloud secrets add-iam-policy-binding 'SECRET_NAME' \
               --member="serviceAccount:SERVICE_ACCOUNT_ID" \
               --role="roles/secretmanager.secretAccessor"
         

Replace the following:

     * `SECRET_NAME`: the secret name in Secret Manager.
     * `SERVICE_ACCOUNT_ID`: the ID of the IAM-based service account in the `serviceAccount:service-PROJECT_ID@gcp-sa-alloydb.iam.gserviceaccount.com` format—for example, `service-212340152456@gcp-sa-alloydb.iam.gserviceaccount.com`.

You can also grant this role to the service account at the project level. For more information, see [Add Identity and Access Management policy binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)




#### Set up authentication using headers

The following example shows how to set up authentication using a function. The function returns a JSON object that contains the headers required to make a request to the embedding model.
    
    
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



### Deploy Model Garden models to an Agent Platform endpoint

In addition to Gemini or other Agent Platform models available by default, you can host models from Model Garden that are optimized for specific tasks. The common process is to first deploy a model from Model Garden to a public Agent Platform endpoint, and then register that endpoint with AlloyDB. These task-specific models are registered with a corresponding `model_type`, such as `ts_forecasting` in case of the `TimesFM` model, and used with specialized SQL functions.

To deploy a model hosted in Model Garden to an Agent Platform endpoint, complete the following steps:

  1. Go to the **Model Garden** page in the Google Cloud console:

[Go to Model Garden](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden)

  2. Find the model, and select **Deploy**.

  3. In the deployment settings, select **Public (Shared endpoint)** under **Endpoint access** to make the endpoint publicly accessible and reachable by AlloyDB for PostgreSQL.

  4. After the deployment is complete, navigate to the endpoint's details page and copy the model request URL from the **Sample request** pane.




## Text embedding models

This section shows how to register model endpoints with model endpoint management.

The model endpoint management supports some text embedding and generic Agent Platform models as pre-registered model endpoints. You can directly use the model ID to generate embeddings or invoke predictions, based on the model type. For more information about supported pre-registered models, see [Pre-registered Agent Platform models](https://docs.cloud.google.com/alloydb/docs/reference/supported-ai-models#pre-registered-models).

**Note:** Agent Platform model support is governed by Agent Platform model versioning and lifecycle guidelines. For more information about stable versions, see [Model versions and lifecycle](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/model-versions).

The `gemini-embedding-001` model is only available in the `us-central1` region.

For example, to call the pre-registered `gemini-embedding-001` model, you can directly call the model using the embedding function:
    
    
    SELECT
          embedding(
            model_id => 'gemini-embedding-001',
            content => 'AlloyDB is a managed, cloud-hosted SQL database service');
    

If your AlloyDB cluster and the Agent Platform endpoint are in different projects, then set the `model_id` to the qualified path of the endpoint—for example, `projects/PROJECT_ID/locations/REGION_ID/publishers/google/models/gemini-embedding-001`.

To generate embeddings, see how to [generate text embeddings](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings).

### Text embedding models with built-in support

The model endpoint management provides built-in support for some models by Agent Platform and OpenAI. For the list of models with built-in support, see [Models with built-in support](https://docs.cloud.google.com/alloydb/docs/reference/supported-ai-models#models-built-in-support).

For models with built-in support, you can set the qualified name as the model qualified name and specify the request URL. Model endpoint management automatically identifies the model and sets up default transform functions.

#### Agent Platform embedding models

**Note:** Use the the [public.embedding() function](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings) to query Agent Platform models without registration or customization. For passing any custom information such as the task type, you must register the Agent Platform model, and then use the `google_ml.embedding()` function.

The following steps show how to register Agent Platform models with built-in support. The `gemini-embedding-001` and the `text-multilingual-embedding-002` model endpoint is used as an example.

**Note:** Only the `text-multilingual-embedding-002` model endpoint requires setting up transform functions provided by model endpoint management.

Make sure that both the AlloyDB cluster and the Agent Platform model that you're querying are in the same region.

  1. [Connect to your database using `psql`.](https://docs.cloud.google.com/alloydb/docs/connect-psql)

  2. Set up the `google_ml_integration` extension.

  3. Call the create model function to add the model endpoint:

###  gemini-embedding-001 
         
         CALL
             google_ml.create_model(
               model_id => 'gemini-embedding-001',
               model_request_url => 'publishers/google/models/gemini-embedding-001',
               model_provider => 'google',
               model_qualified_name => 'gemini-embedding-001',
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
               model_auth_type => 'alloydb_service_agent_iam',
               model_in_transform_fn => 'google_ml.vertexai_text_embedding_input_transform',
               model_out_transform_fn => 'google_ml.vertexai_text_embedding_output_transform');
         




If the model is stored in the another project and region than your AlloyDB cluster, then set the request URL to `projects/PROJECT_ID/locations/REGION_ID/publishers/google/models/MODEL_ID`, where `REGION_ID` is the region where your model is hosted, and the `MODEL_ID` is the qualified model name.

In addition, [grant the Vertex AI User (`roles/aiplatform.user`) role](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai#enable-access) to AlloyDB service account of the project where AlloyDB instance resides so that AlloyDB can access the model hosted in the other project.

#### Open AI text embedding model

The `google_ml_integration` extension automatically sets up default transform functions and invokes calls to the remote OpenAI models. For the list of OpenAI models with built-in support, see [Models with built-in support](https://docs.cloud.google.com/alloydb/docs/reference/supported-ai-models#models-built-in-support).

The following example adds the `text-embedding-ada-002` OpenAI model endpoint. You can register the OpenAI `text-embedding-3-small` and `text-embedding-3-large` model endpoints using the same steps and setting the model qualified names specific to the models.

  1. Connect to your database using `psql`.
  2. Set up the `google_ml_integration` extension.
  3. Add the OpenAI API key as a secret to the Secret Manager for authentication.
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



To generate embeddings, see [generate text embeddings](https://docs.cloud.google.com/alloydb/docs/ai/work-with-embeddings).

### Custom-hosted text embedding model

This section shows how to register a custom-hosted model endpoint along with creating transform functions, and optionally, custom HTTP headers. All custom-hosted model endpoints are supported regardless of where they are hosted.

The following example adds the `custom-embedding-model` custom model endpoint hosted by Cymbal. The `cymbal_text_input_transform` and `cymbal_text_output_transform` transform functions are used to transform the input and output format of the model to the input and output format of the prediction function.

To register custom-hosted text embedding model endpoints, complete the following steps:

  1. [Connect to your database using `psql`.](https://docs.cloud.google.com/alloydb/docs/connect-psql)

  2. Set up the `google_ml_integration` extension.

  3. Optional: Add the API key as a secret to the Secret Manager for authentication.

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
**Note:** Secret Manager generates an `Authorization: Bearer SECRET_VALUE_FROM_SECRET_MANAGER` header for authentication by default. If this format matches your model endpoint's authorization bearer token format, then you don't have to generate auth headers using the header generation function.
  5. Create the input and output transform functions based on the following signature for the prediction function for text embedding model endpoints. For more information about how to create transform functions, see [Transform functions example](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint#transform-func-example).

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
     * `REQUEST_URL`: required. The model-specific endpoint when adding custom text embedding and generic model endpoints—for example, `https://cymbal.com/models/text/embeddings/v1`. Ensure that the model endpoint is accessible through an internal IP address. Model endpoint management doesn't support public IP addresses.
     * `MODEL_QUALIFIED_NAME`: required if your model endpoint uses a qualified name. The fully qualified name in case the model endpoint has multiple versions.
     * `SECRET_ID`: the secret ID you used earlier in the `google_ml.create_sm_secret()` procedure.



## Multimodal model with built-in support

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://docs.google.com/forms/d/1Ux9AZoGv9dwraS6lXa9Qgwvj17NTk1stagUXFW5mu5k). 

**Note:** This experimental launch is a Pre-GA offering.

### Integrate with Vertex AI and install the extension

  1. [Configure user access to Agent Platform models](https://docs.cloud.google.com/alloydb/docs/ai/configure-vertex-ai).
  2. Verify that the latest version of `google_ml_integration` is installed. 
     1. To check the installed version, run the following command:
            
            SELECT extversion FROM pg_extension WHERE extname = 'google_ml_integration';
            extversion 
            ------------
            1.5.2
            (1 row)

     2. If the extension isn't installed or if the installed version is earlier than 1.5.2, update the extension.
            
            CREATE EXTENSION IF NOT EXISTS google_ml_integration;
            ALTER EXTENSION google_ml_integration UPDATE;

If you experience issues when you run the preceding commands, or if the extension isn't updated to version 1.5.2 after you run the preceding commands, contact [Google Cloud support](https://cloud.google.com/support).

  3. To use the AlloyDB AI query engine functionality, set the `google_ml_integration.enable_ai_query_engine` flag to `on`.

### SQL

     1. Enable the AI query engine for the current session.  

            
            SET google_ml_integration.enable_ai_query_engine = on;

     2. Enable features for a specific database across sessions.  

            
            ALTER DATABASE DATABASE_NAME SET google_ml_integration.enable_ai_query_engine = 'on';

     3. Enable the AI query engine for a specific user across sessions and databases.  

            
            ALTER ROLE postgres SET google_ml_integration.enable_ai_query_engine = 'on';

### Console

To modify the value of the `google_ml_integration.enable_ai_query_engine` flag, follow the steps in [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console). 

### gcloud

To use the gcloud CLI, you can [install and initialize](https://docs.cloud.google.com/sdk/docs/install-sdk) the Google Cloud CLI, or you can use [Cloud Shell](https://docs.cloud.google.com/shell/docs/using-cloud-shell).

You can modify the value of the `google_ml_integration.enable_ai_query_engine` flag. For more information, see [Configure an instance's database flags](https://docs.cloud.google.com/alloydb/docs/instance-configure-database-flags#console). 
    
    gcloud alloydb instances update INSTANCE_ID \
      --database-flags google_ml_integration.enable_ai_query_engine=on \
      --region=REGION_ID \
      --cluster=CLUSTER_ID \
      --project=PROJECT_ID




### Call the model to generate multimodal embeddings

Since Model endpoint management provides built-in support for the `multimodalembedding@001` model by Vertex AI, you can directly call the model to generate multimodal embeddings.

The following example uses the `multimodalembedding@001` qualified model name as model ID to generate multimodal image embeddings:

  1. Connect to your database using `psql`.
  2. Set up the `google_ml_integration` extension.
  3. Generate multimodal image embeddings:
         
         SELECT
           ai.image_embedding(
             model_id => 'multimodalembedding@001',
             image => 'IMAGE_PATH_OR_TEXT',
             mimetype => 'MIMETYPE');
         




Replace the following:

  * IMAGE_PATH_OR_TEXT with Cloud Storage path to the image, for example-`gs://cymbal_user_data/image-85097193-cd9788aacebb.jpeg` to translate into a vector embedding or base64 string of the image.
  * MIMETYPE with the mimetype of the image.



## Ranking models

**Preview**

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

For information about access to this release, see the [ access request page](https://docs.google.com/forms/d/1Ux9AZoGv9dwraS6lXa9Qgwvj17NTk1stagUXFW5mu5k). 

**Note:** This feature is an experimental pre-GA offering.

### Vertex AI ranking models

You can use Vertex AI models mentioned in [Supported models](https://docs.cloud.google.com/generative-ai-app-builder/docs/ranking#models) without registration.

To learn how to rank your search results using an Agent Platform ranking model, see [Rank search results](https://docs.cloud.google.com/alloydb/docs/ai/rank-rerank-search-results-rag).

### Registering a third-party ranking model

The following example shows how to register a reranking model from Cohere.
    
    
    CREATE OR REPLACE FUNCTION cohere_rerank_input_transform(
        model_id VARCHAR(100),
        search_string TEXT,
        documents TEXT[],
        top_n INT DEFAULT NULL
    )
    RETURNS JSON
    LANGUAGE plpgsql
    AS $$
    #variable_conflict use_variable
    DECLARE
      transformed_input JSONB;
    BEGIN
      -- Basic Input Validation
      IF search_string IS NULL OR search_string = '' THEN
        RAISE EXCEPTION 'Invalid input: search_string cannot be NULL or empty.';
      END IF;
    
      IF documents IS NULL OR array_length(documents, 1) IS NULL OR array_length(documents, 1) = 0 THEN
        RAISE EXCEPTION 'Invalid input: documents array cannot be NULL or empty.';
      END IF;
    
      IF top_n IS NOT NULL AND top_n < 0 THEN
        RAISE EXCEPTION 'Invalid input: top_n must be greater than or equal to zero. Provided value: %', top_n;
      END IF;
    
      -- Construct the base JSON payload for Cohere Rerank API
      transformed_input := jsonb_build_object(
        'model', google_ml.model_qualified_name_of(model_id),
        'query', search_string,
        'documents', to_jsonb(documents), -- Convert TEXT[] directly to JSON array
        'return_documents', false -- Explicitly set to false (optional, as its default)
      );
    
      -- Add top_n to the payload only if it's provided and valid
      IF top_n IS NOT NULL THEN
         transformed_input := transformed_input || jsonb_build_object('top_n', top_n);
      END IF;
    
      -- Return the final JSON payload
      RETURN transformed_input::JSON;
    
    END;
    $$;
    
    CREATE OR REPLACE FUNCTION cohere_rerank_output_transform(
        model_id VARCHAR(100),
        response_json JSON
    )
    RETURNS TABLE (index INT, score REAL)
    LANGUAGE plpgsql
    AS $$
    DECLARE
      result_item JSONB;
      response_jsonb JSONB;
      cohere_index INT; -- 0-based index from Cohere response
    BEGIN
      -- Validate response_json
      IF response_json IS NULL THEN
        RAISE EXCEPTION 'Invalid model response: response cannot be NULL.';
      END IF;
    
      -- Convert JSON to JSONB for easier processing
      response_jsonb := response_json::JSONB;
    
      -- Check top-level structure
      IF jsonb_typeof(response_jsonb) != 'object' THEN
        RAISE EXCEPTION 'Invalid model response: response must be a JSON object. Found: %', jsonb_typeof(response_jsonb);
      END IF;
    
      -- Check for the 'results' array
      IF response_jsonb->'results' IS NULL OR jsonb_typeof(response_jsonb->'results') != 'array' THEN
        -- Check for potential Cohere error structure
        IF response_jsonb->'message' IS NOT NULL THEN
           RAISE EXCEPTION 'Cohere API Error: %', response_jsonb->>'message';
        ELSE
           RAISE EXCEPTION 'Invalid model response: response does not contain a valid "results" array.';
        END IF;
      END IF;
    
      -- Loop through the 'results' array (JSONB array indices are 0-based)
      FOR i IN 0..jsonb_array_length(response_jsonb->'results') - 1 LOOP
        result_item := response_jsonb->'results'->i;
    
        -- Validate individual result item structure
        IF result_item IS NULL OR jsonb_typeof(result_item) != 'object' THEN
          RAISE WARNING 'Skipping invalid result item at array index %.', i;
          CONTINUE;
        END IF;
    
        IF result_item->'index' IS NULL OR jsonb_typeof(result_item->'index') != 'number' THEN
           RAISE WARNING 'Missing or invalid "index" field in result item at array index %.', i;
           CONTINUE;
        END IF;
    
        IF result_item->'relevance_score' IS NULL OR jsonb_typeof(result_item->'relevance_score') != 'number' THEN
           RAISE WARNING 'Missing or invalid "relevance_score" field in result item at array index %.', i;
           CONTINUE;
        END IF;
    
        -- Extract values
        BEGIN
          cohere_index := (result_item->>'index')::INT;
          -- Assign values to the output table columns
          -- Cohere returns 0-based index, map it to 1-based for consistency
          -- with input document array position
          index := cohere_index + 1;
          score := (result_item->>'relevance_score')::REAL;
          RETURN NEXT; -- Return the current row
        EXCEPTION WHEN others THEN
          RAISE WARNING 'Error processing result item at array index %: %', i, SQLERRM;
          CONTINUE; -- Skip this item and continue with the next
        END;
      END LOOP;
    
      RETURN; -- End of function
    END;
    $$;
    
    CALL
      google_ml.create_sm_secret(
        '<SECRET_ID>',
        'projects/<PROJECT_NUMBER>/secrets/<SECRET_ID>/versions/latest');
    
    CALL
      google_ml.create_model(
        model_id => 'cohere-reranker',
        model_type => 'reranking',
        model_provider => 'custom',
        model_request_url => 'https://api.cohere.com/v2/rerank',
        model_qualified_name => 'rerank-v3.5',
        model_auth_type => 'secret_manager',
        model_auth_id => '<SECRET_ID>',
        model_in_transform_fn => 'cohere_rerank_input_transform',
        model_out_transform_fn => 'cohere_rerank_output_transform'
      );
    

## Generic models

This section shows how to register any generic model endpoint that is available on a hosted model provider such as Hugging Face, OpenAI, Agent Platform, Anthropic, or any other provider. This section shows examples to register a generic model endpoint hosted on Hugging Face, a generic Gemini model from Agent Platform Model Garden, and the `claude-haiku` model endpoint.

You can register any generic model endpoint as long as the input and output is in the JSON format. Based on your model endpoint metadata, you might need to generate HTTP headers or define request URLs.

For more information about pre-registered generic models and models with built-in support, see [Supported models](https://docs.cloud.google.com/alloydb/docs/reference/supported-ai-models).

### Generic Gemini models

This section shows how to register generic Gemini models.

#### gemini-3.5-flash model

AlloyDB pre-registers some Gemini models so they are ready to use. However, newer models might not be registered by default. To register new Gemini models as they become available, follow these steps:

The following example uses the `gemini-3.5-flash:generateContent` model endpoint from Model Garden.

  1. Connect to your database using `psql`.
  2. Set up the `google_ml_integration` extension.
  3. Register the model:
         
         CALL google_ml.create_model(
           model_id             => 'gemini-3.5-flash:generateContent',
           model_request_url    => 'https://aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/global/publishers/google/models/gemini-3.5-flash:generateContent',
           model_qualified_name => 'gemini-3.5-flash',
           model_provider       => 'google',
           model_type           => 'llm',
           model_auth_type      => 'alloydb_service_agent_iam'
         );
         

Replace `PROJECT_ID` with the ID of your Google Cloud project.

  4. Invoke predictions using the registered model ID:
         
         SELECT
           google_ml.predict_row(
             model_id     => 'gemini-3.5-flash:generateContent',
             request_body => '{
               "contents": [
                 {
                   "role": "user",
                   "parts": [
                     {
                       "text": "For TPCH database schema as mentioned here https://www.tpc.org/TPC_Documents_Current_Versions/pdf/TPC-H_v3.0.1.pdf , generate a SQL query to find all supplier names that are located in India."
                     }
                   ]
                 }
               ]
             }'
           ) -> 'candidates' -> 0 -> 'content' -> 'parts' -> 0 ->> 'text' AS response;
         




### Generic model on Hugging Face

The following example adds the `facebook/bart-large-mnli` custom classification model endpoint hosted on Hugging Face.

  1. Connect to your database using `psql`.
  2. Set up the `google_ml_integration` extension.
  3. Add the OpenAI API key as a secret to the Secret Manager for authentication. If you have already created a secret for any other OpenAI model, you can reuse the same secret.
  4. Call the secret stored in the Secret Manager:
         
         CALL
           google_ml.create_sm_secret(
             secret_id => 'SECRET_ID',
             secret_path => 'projects/PROJECT_ID/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
         

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

  1. Connect to your database using `psql`.
  2. [Create and enable the `google_ml_integration` extension](https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint).

###  Secret Manager 

     1. [Add the bearer token as a secret to the Secret Manager for authentication](https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint).
     2. Call the secret stored in the Secret Manager:
            
            CALL
              google_ml.create_sm_secret(
                secret_id => 'SECRET_ID',
                secret_path => 'projects/PROJECT_ID/secrets/SECRET_MANAGER_SECRET_ID/versions/VERSION_NUMBER');
            

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




For more information, see how to [invoke predictions for generic model endpoints](https://docs.cloud.google.com/alloydb/docs/ai/invoke-predictions).

## Forecasting models

In addition to generic models, you can register forecasting models from [Model Garden](https://console.cloud.google.com/vertex-ai/publishers/google/model-garden).

### Time-series forecasting with the TimesFM model

A common use case for task-specific models is [performing time-series forecasting](https://docs.cloud.google.com/alloydb/docs/ai/perform-time-series-forecasting) with the TimesFM model.

To deploy and register this model, complete the following steps:

  1. Deploy the TimesFM model from Model Garden to an Agent Platform endpoint to obtain a publicly accessible model request URL. For more information, see [Deploy Model Garden models to an Agent Platform endpoint](https://docs.cloud.google.com/alloydb/docs/ai/register-model-endpoint#deploy-model-model-garden).

  2. To register the deployed TimesFM model in AlloyDB for PostgreSQL, use the `google_ml.create_model` function. For time-series forecasting, the `model_type` must be `ts_forecasting`:



    
    
    CALL
    google_ml.create_model(
      model_id => 'vertex_timesfm',
      model_qualified_name => 'timesfm_v2',
      model_type => 'ts_forecasting',
      model_provider => 'google',
      model_request_url => 'https://REGION-aiplatform.googleapis.com/v1/projects/PROJECT_ID/locations/REGION/endpoints/ENDPOINT_ID:predict',
      model_auth_type => 'alloydb_service_agent_iam'
    );
    

**Note:** If your AlloyDB instance is in a different Google Cloud project than the Agent Platform model endpoint, you must grant the AlloyDB Service Account the `Vertex AI User` role - `roles/aiplatform.user` \- in the project where the model is hosted.

After you register the model, you can use the `ai.forecast()` or `google_ml.forecast()` function to generate predictions.

## What's next

  * Learn about the [model endpoint management reference](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint).
  * Use [sample templates for registering model endpoints](https://docs.cloud.google.com/alloydb/docs/reference/model-endpoint-sample-template).
  * [Generate multimodal Embeddings](https://docs.cloud.google.com/alloydb/docs/ai/generate-multimodal-embeddings).
  * [Rank and score search results for RAG](https://docs.cloud.google.com/alloydb/docs/ai/rank-rerank-search-results-rag).
  * [Use natural language in SQL operators](https://docs.cloud.google.com/alloydb/docs/ai/evaluate-semantic-queries-ai-operators).
  * [Perform time series forecasting](https://docs.cloud.google.com/alloydb/docs/ai/perform-time-series-forecasting).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
