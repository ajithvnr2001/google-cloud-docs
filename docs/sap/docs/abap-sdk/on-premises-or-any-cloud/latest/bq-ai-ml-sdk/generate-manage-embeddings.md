---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/generate-manage-embeddings/
title: Generate and manage embeddings in BigQuery \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:12.708946+00:00
---

# Generate and manage embeddings in BigQuery  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/generate-manage-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Generate and manage embeddings in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-ai-ml-sdk/generate-manage-embeddings)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/generate-manage-embeddings)



BigQuery AI and ML SDK for ABAP lets you generate and manage embeddings on your enterprise data at source in BigQuery.

BigQuery can serve as a cost-effective vector database for using its vector search capabilities, letting you store and query embeddings (vector representations of data) directly within the data warehouse, potentially reducing the need for separate vector database infrastructure. You can generate embeddings for your enterprise data stored in your BigQuery datasets by using the BigQuery function [`ML.GENERATE_EMBEDDING`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding).

Embedding models on Agent Platform can be accessed by creating a [remote model](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) in BigQuery ML that represents the Agent Platform model's endpoint. Once you have created a remote model over the Agent Platform model that you want to use, you can access that model's capabilities by running the BigQuery ML function against the remote model.

With the BigQuery AI and ML SDK for ABAP, you can use embedding models for the following:

  * Generate and store embeddings for text data
  * Generate and store embeddings for multimodal data
  * Keep your BigQuery vector database updated with your most recent enterprise data



## Before you begin

Before using the BigQuery AI and ML SDK for ABAP with the embedding models, make sure that you or your administrators have completed the following prerequisites:

  * Enabled the BigQuery API, BigQuery Connection API, and Agent Platform API in your Google Cloud project. For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).
  * [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * The service account configured in the client key for authentication must have the [required permissions](https://docs.cloud.google.com/bigquery/docs/generate-text-tutorial-gemini#required_permissions).
  * [Installed the BigQuery AI and ML SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap) in your SAP environment.
  * Created a [remote model](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) for the [supported embedding models](https://docs.cloud.google.com/bigquery/docs/generative-ai-overview#supported_models_2).



## Pricing

The BigQuery AI and ML SDK for ABAP is offered at no cost. However, you're responsible for the charges at the BigQuery and Agent Platform services:

  * BigQuery ML: You incur costs for the data that you process in BigQuery.
  * Agent Platform: You incur costs for calls to the Agent Platform service that's represented by the remote model.



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

For more information about BigQuery pricing, see the [BigQuery pricing](https://cloud.google.com/bigquery/pricing) page.

For more information about Agent Platform pricing, see the [Agent Platformpricing](https://cloud.google.com/vertex-ai/pricing#generative_ai_models) page.

## Generate embeddings on BigQuery

This section explains how to generate embeddings for the enterprise data stored in BigQuery from your ABAP application logic by using the BigQuery AI and ML SDK for ABAP.

### Instantiate the BigQuery embeddings invoker class

To invoke the embeddings text and multimodal models on BigQuery datasets, you instantiate the class `/GOOG/CL_BQ_GENERATIVE_MODEL`.
    
    
    TRY.
        DATA(lo_bqml_embeddings_model) = NEW /goog/cl_bq_embeddings_model( iv_key = 'CLIENT_KEY' ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the `CLIENT_KEY` with the client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

### Generate embeddings

To run queries to generate embeddings for text and multimodal data with the BigQuery function `ML.GENERATE_EMBEDDING`, use the method `GENERATE_EMBEDDINGS` of the class `/GOOG/CL_BQ_EMBEDDINGS_MODEL`.

The object of the class `/GOOG/CL_BQ_QUERY` set with the query is passed as an input to the method.
    
    
    lo_bqml_embeddings_model->generate_embeddings( io_query = lo_bq_query ).
    

`LO_BQ_QUERY` is the reference of the class `/GOOG/CL_BQ_QUERY` after [setting the query](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/get-gemini-insights#set-gemini-query).

### Override model generation parameters

You can define embedding model [generation parameters](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding#syntax) in the saved query on BigQuery or passed query text. But if you need to override the parameters for the same query from ABAP application logic, then you can use the method `SET_GENERATION_CONFIG` of the class `/GOOG/CL_BQ_EMBEDDINGS_MODEL`. The generation parameters in the initial query are overridden with the parameters passed through this method.
    
    
    lo_bqml_embeddings_model->set_generation_config( iv_flatten_json_output   = 'IS_FLATTEN_JSON_OUTPUT'
                                     iv_task_type             = 'TASK_TYPE'
             iv_output_dimensionality = 'OUTPUT_DIMENSIONALITY' ).
    

Replace the following:

  * `IS_FLATTEN_JSON_OUTPUT`: A boolean value that determines whether the JSON content returned by the function is parsed into separate columns.
  * `TASK_TYPE`: The value that specifies the intended downstream application to help the model produce better quality embeddings, look for probable values from `task_type` argument under [input syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding#syntax) for `ML.GENERATE_EMBEDDING`.
  * `OUTPUT_DIMENSIONALITY`: The value that specifies the number of dimensions to use when generating embeddings, look for probable values from `output_dimensionality` argument under [input syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-embedding#syntax) for `ML.GENERATE_EMBEDDING`.



## Get query results of queries for generating embeddings

To receive processed responses from the BigQuery ML for generating embeddings and presenting them in a meaningful way, the SDK uses chained methods in the class `/GOOG/CL_BQ_GENERATIVE_MODEL`, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

### Get text embedding vectors

To get the text embedding vectors for each row in your ABAP application logic, use the method `GET_TEXT_EMBEDDING_VECTORS`.
    
    
    DATA(lt_embeddings) = lo_bqml_embeddings_model->generate_embeddings( io_query = lo_bq_query
                                                 )->get_text_embedding_vectors( ).
    

### Get text embeddings status

To get the status of each text embeddings generation for each row, use the method `GET_TEXT_EMBEDDING_STATUS`.

If the operation was successful, then the status is empty.
    
    
    DATA(lt_embeddings_status) = lo_bqml_embeddings_model->generate_embeddings( io_query = lo_bq_query
                                                        )->get_text_embedding_status( ).
    

### Get query job status

Each query on BigQuery is executed as a query job.

To get the status of the embeddings query job, use the method `GET_QUERY_JOB_STATUS`.
    
    
    lo_bqml_embeddings_model->generate_embeddings( io_query = lo_bq_query
                           )->get_query_job_status(
    IMPORTING ev_job_complete          = DATA(lv_job_complete)
      ev_job_creation_reason   = DATA(lv_job_creation_reason)
      ev_job_id                = DATA(lv_job_id)
      ev_query_id              = DATA(lv_query_id)
      ev_total_bytes_processed = DATA(lv_total_bytes_processed)
      ev_total_rows            = DATA(lv_total_rows) ).
    

The method returns the following job status metrics:

  * Whether the query has completed or not.
  * The reason why a Job was created.
  * Reference to the Job that was created to run the query.
  * Auto-generated ID for the query.
  * The total number of bytes processed for this query.
  * The total number of rows in the complete query result set.



### Get query job errors

To fetch the query job errors (if any), use the method `GET_QUERY_JOB_ERRORS`.
    
    
    DATA(lt_query_job_errors) = lo_bqml_embeddings_model->execute_query( io_query = lo_bq_query
                                                       )->get_query_job_errors( ).
    

### Get overall response for text embeddings

To get an overall response table for the text embeddings query that you run, use the method `GET_TEXT_EMBEDDING_RESPONSE`.

A response is populated only when the model generation parameter `FLATTEN_JSON_OUTPUT` is set to `TRUE` in the query.
    
    
    DATA(lt_text_embeddings_response) = lo_bqml_embeddings_model->execute_query( io_query = lo_bq_query
                                                               )->get_text_embedding_response( ).
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
