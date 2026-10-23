---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/get-gemini-insights/
title: Get Gemini insights on BigQuery data \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:11.945254+00:00
---

# Get Gemini insights on BigQuery data  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/get-gemini-insights/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Get Gemini insights on BigQuery data Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-ai-ml-sdk/get-gemini-insights)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/get-gemini-insights)



The BigQuery AI and ML SDK for ABAP lets you use Gemini queries on your enterprise data stored in BigQuery and bring back the results, from your ABAP-based agents or applications. With the SDK, you can use Gemini models to do the following:

  * Generate insights from text data in BigQuery
  * Generate insights from image or video data in BigQuery



You can run Gemini-based insights on your enterprise data stored in your BigQuery datasets by using the BigQuery function [`ML.GENERATE_TEXT`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text).

You can access Gemini models on Agent Platform by creating a [remote model](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) in BigQuery ML that represents the Agent Platform model's endpoint. Once you've created a remote model over the Agent Platform model that you want to use, you can access that model's capabilities by running the BigQuery ML function against the remote model.

## Before you begin

Before using the BigQuery AI and ML SDK for ABAP with the Gemini models, make sure that you or your administrators have completed the following prerequisites:

  * Enabled the BigQuery API, BigQuery Connection API, and Agent Platform API in your Google Cloud project. For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).
  * [Make sure that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * The service account configured in the client key for authentication must have the [required permissions](https://docs.cloud.google.com/bigquery/docs/generate-text-tutorial-gemini#required_permissions).
  * [Installed the BigQuery AI and ML SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap) in your SAP environment.
  * Created a [remote model](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-create-remote-model) for the [supported Gemini models](https://docs.cloud.google.com/bigquery/docs/generative-ai-overview#supported_models).



## Pricing

The BigQuery AI and ML SDK for ABAP is offered at no cost. However, you're responsible for the charges at the BigQuery and Agent Platform services as follows:

  * BigQuery ML: You incur costs for the data that you process in BigQuery.
  * Agent Platform: You incur costs for calls to the Agent Platform service that's represented by the remote model.



To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

For more information about BigQuery pricing, see the [BigQuery pricing](https://cloud.google.com/bigquery/pricing) page.

For more information about Agent Platform pricing, see the [Agent Platform pricing](https://cloud.google.com/vertex-ai/pricing#generative_ai_models) page.

## Run Gemini queries on BigQuery

This section explains how to generate Gemini-based insights from enterprise data in BigQuery by using the BigQuery AI and ML SDK for ABAP.

The ABAP class `/GOOG/CL_BQ_GENERATIVE_MODEL` shipped with the SDK lets you run Gemini queries by using the BigQuery function `ML.GENERATE_TEXT`.

### Set Gemini query

You can use the SDK to run Gemini queries in the following ways:

  * Save your query to run Gemini in BigQuery. Use the class `/GOOG/CL_BQ_QUERY` and provide the saved query name when you instantiate the class from your application logic.
        
        TRY.
            DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                      iv_location_id = 'QUERY_LOCATION_ID'
              iv_query_name  = 'SAVED_QUERY_NAME' ).
        CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
            cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
        
        ENDTRY.
        

Replace the following:

    * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
    * `QUERY_LOCATION_ID`: The Google Cloud location under which the query is saved.
    * `SAVED_QUERY_NAME`: The name of the query with which the query is saved in BigQuery.
  * Pass the query text to invoke Gemini when you instantiate the class `/GOOG/CL_BQ_QUERY` from your application logic.
        
        TRY.
            DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                      iv_location_id = 'QUERY_LOCATION_ID'
              iv_query_text  = 'QUERY_TEXT' ).
        CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
            cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
        
        ENDTRY.
        

Replace the following:

    * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
    * `QUERY_LOCATION_ID`: The Google Cloud location under which the query is saved.
    * `QUERY_TEXT`: The query text that you want to run with Gemini.



When you instantiate the `/GOOG/CL_BQ_QUERY` class with the saved query name or direct query text, it sets the query within the class. Then, you can pass the class reference as input to the `/GOOG/CL_BQ_GENERATIVE_MODEL` ABAP class to invoke the query.

### Instantiate the BigQuery Gemini invoker class

To invoke the Gemini text and multimodal models on BigQuery datasets, use the class `/GOOG/CL_BQ_GENERATIVE_MODEL`.
    
    
    TRY.
        DATA(lo_bq_generative_model) = NEW /goog/cl_bq_generative_model( iv_key = 'CLIENT_KEY' ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the `CLIENT_KEY` with the client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

### Run Gemini query

To run Gemini queries with BigQuery function `ML.GENERATE_TEXT`, use the method `EXECUTE_QUERY` of the class `/GOOG/CL_BQ_GENERATIVE_MODEL`. The object of the class `/GOOG/CL_BQ_QUERY` set with the query is passed as an input to the method.
    
    
    lo_bq_generative_model->execute_query( io_query = lo_bq_query ).
    

`LO_BQ_QUERY` is the reference of the class `/GOOG/CL_BQ_QUERY` after setting the query.

### Override model generation parameters

You can define Gemini model [generation parameters](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text#syntax) in a saved query in BigQuery or passed query text. But if you need to override the parameters for the same query from ABAP application logic, then you can use the method `SET_GENERATION_CONFIG` of the class `/GOOG/CL_BQ_GENERATIVE_MODEL`. The generation parameters in the initial query are overridden with the parameters passed through this method.
    
    
    DATA lt_stop_sequences TYPE /goog/cl_bigquery_v2=>ty_t_string.
    DATA lt_safety_settings TYPE /goog/cl_bq_generative_model=>ty_t_safety_settings.
    DATA ls_safety_settings TYPE /goog/cl_bq_generative_model=>ty_safety_setting.
    
    APPEND 'STOP_SEQUENCE' TO lt_stop_sequences.
    
    ls_safety_settings-category = 'CATEGORY'.
    ls_safety_settings-threshold = 'THRESHOLD'.
    
    APPEND ls_safety_settings TO lt_safety_settings.
    
    lo_bq_generative_model->set_generation_config( iv_temperature               = 'TEMPERATURE'
                                   iv_top_p                     = 'TOP_P'
           iv_top_k                     = 'TOP_K'
           iv_max_output_tokens         = 'MAX_OUTPUT_TOKENS'
           iv_flatten_json_output       = 'IS_FLATTEN_JSON_OUTPUT'
           iv_ground_with_google_search = 'IS_GROUND_WITH_GOOGLE_SEARCH'
    it_stop_sequences            = lt_stop_sequences
    it_safety_settings           = lt_safety_settings ).
    

Replace the following:

  * `STOP_SEQUENCE`: The value that removes the specified strings if they are included in responses from the model.
  * `CATEGORY`: The content safety category to filter responses, look for probable values from safety settings argument under [input syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text#syntax) for `ML.GENERATE_TEXT`.
  * `THRESHOLD`: The corresponding blocking threshold to filter responses, look for probable values from the safety settings argument under [input syntax](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/bigqueryml-syntax-generate-text#syntax) for `ML.GENERATE_TEXT`.
  * `TEMPERATURE`: The value that controls the degree of randomness in token selection.
  * `TOP_P`: The value that changes how the model selects tokens for output.
  * `TOP_K`: The value that changes how the model selects tokens for output.
  * `MAX_OUTPUT_TOKENS`: The value that sets the maximum number of tokens that can be generated in the response.
  * `IS_FLATTEN_JSON_OUTPUT`: A boolean value that determines whether the JSON content returned by the function is parsed into separate columns.
  * `IS_GROUND_WITH_GOOGLE_SEARCH`: A boolean value that determines whether the Agent Platform model uses [Grounding with Google Search](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/grounding/overview#ground-public) when generating responses.



### Get query results of Gemini queries

To receive processed responses from the BigQuery ML for Gemini queries and present them in a meaningful way, use the class `/GOOG/CL_BQ_MODEL_RESPONSE`.

The response captured by the `/GOOG/CL_BQ_MODEL_RESPONSE` class is chained to the requests made through the methods of the `/GOOG/CL_BQ_GENERATIVE_MODEL` class, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

#### Get text response

To receive a text response from the model, use the method `GET_TEXT_RESPONSE`.
    
    
    DATA(lt_bq_response) = lo_bq_generative_model->execute_query( io_query = lo_bq_query
                                                )->get_text_response( ).
    

#### Get query job status

Each query in BigQuery is executed as a query job. To get the status of the query job, use the method `GET_QUERY_JOB_STATUS`.
    
    
    lo_bq_generative_model->execute_query( io_query = lo_bq_query
                         )->get_query_job_status(
    IMPORTING ev_job_complete          = DATA(lv_job_complete)
      ev_job_creation_reason   = DATA(lv_job_creation_reason)
      ev_job_id                = DATA(lv_job_id)
      ev_query_id              = DATA(lv_query_id)
      ev_total_bytes_processed = DATA(lv_total_bytes_processed)
      ev_total_rows            = DATA(lv_total_rows) ).
    

The method returns the following job status metrics:

  * Whether the query has completed or not
  * The reason why a Job was created
  * Reference to the Job that was created to run the query
  * Auto-generated ID for the query
  * The total number of bytes processed for this query
  * The total number of rows in the complete query result set



#### Get query job errors

To fetch the errors (if any), use the method `GET_QUERY_JOB_ERRORS`.
    
    
    DATA(lt_query_job_errors) = lo_bq_generative_model->execute_query( io_query = lo_bq_query
                                                     )->get_query_job_errors( ).
    

#### Get finish reason

To get the [reason](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/reference/rest/v1/GenerateContentResponse#FinishReason) why the model stopped generating tokens for each row, use the method `GET_FINISH_REASON`.
    
    
    DATA(lt_finish_reason) = lo_bq_generative_model->execute_query( io_query = lo_bq_query
                                                  )->get_finish_reason( ).
    

#### Get usage metadata

To get the usage metadata about the response generated for each row, use the method `GET_USAGE_METADATA` .
    
    
    DATA(lt_usage_metadata) = lo_bq_generative_model->execute_query( io_query = lo_bq_query
                                                   )->get_usage_metadata( ).
    

Usage metadata consists of the following metrics:

  * Total token count in the response for a row
  * Token count in the input prompt
  * Total token count



#### Get safety rating

To get the safety rating for the response, use the `GET_SAFETY_RATING` method. Safety ratings must be set as model generation parameters in the input query to get the safety rating for the response.
    
    
    DATA(lt_safety_ratings) = lo_bq_generative_model->execute_query( io_query = lo_bq_query
                                                   )->get_safety_rating( ).
    

#### Get overall response table

To get the overall response table for the Gemini query that you run, use the method `GET_RESPONSE_TABLE`.
    
    
    lo_bq_model_response->get_response_table(
    IMPORTING et_bqml_response              = DATA(lt_bqml_response)
                      et_bqml_response_flatten_json = DATA(lt_bqml_response_flatten_json)
                      et_bqml_response_grounding    = DATA(lt_bqml_response_grounding) ).
    

Only one response table is populated based on the generation parameter set in the query:

  * `ET_BQML_RESPONSE` is populated when the parameter `FLATTEN_JSON_OUTPUT` is not set to `TRUE` in the input query.
  * `ET_BQML_RESPONSE_FLATTEN_JSON` is populated when the parameter `FLATTEN_JSON_OUTPUT` is set to `TRUE` in the input query.
  * `ET_BQML_RESPONSE_GROUNDING` is populated when the parameter `FLATTEN_JSON_OUTPUT` is set to `TRUE` in the input query and the parameter `GROUNDING_WITH_GOOGLE_SEARCH` is also set to `TRUE` in the input query.



#### Get grounding source

To list the grounding sources that the model used to generate the responses, use the method `GET_GROUNDING_SOURCE`.
    
    
    DATA(lt_query_grounding_sources) = lo_bq_generative_model->execute_query( io_query = lo_bq_query
                                                            )->get_grounding_source( ).
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
