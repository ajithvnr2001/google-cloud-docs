---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/store-manage-enterprise-queries/
title: Store and manage enterprise queries in BigQuery \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:02:11.605891+00:00
---

# Store and manage enterprise queries in BigQuery  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/store-manage-enterprise-queries/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Store and manage enterprise queries in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-ai-ml-sdk/store-manage-enterprise-queries)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/store-manage-enterprise-queries)



The BigQuery AI and ML SDK for ABAP lets you use BigQuery as a centralized query repository to store, maintain, and retrieve queries that you can run from your ABAP applications.

A centralized query repository provides a single source of truth for validated and optimized queries. BigQuery as a centralized query repository is used by different modules of the BigQuery AI and ML SDK for ABAP to retrieve and run the saved queries.

For more information about saved queries in BigQuery, see [Introduction to saved queries](https://docs.cloud.google.com/bigquery/docs/saved-queries-introduction).

## Before you begin

Before using the BigQuery as a centralized query repository, make sure that you or your administrators have completed the following prerequisites:

  * Enabled the BigQuery API in your Google Cloud project. For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).
  * [Enabled BigQuery Studio](https://docs.cloud.google.com/bigquery/docs/enable-assets) in your Google Cloud project.
  * You've the [required roles](https://docs.cloud.google.com/bigquery/docs/manage-saved-queries#required_roles) to be able to create and save queries.
  * [Billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * [Installed the BigQuery AI and ML SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap) in your SAP environment.



## Create enterprise queries in BigQuery

To draft, validate and save your queries in BigQuery, use the [BigQuery Studio](https://docs.cloud.google.com/bigquery/docs/query-overview#bigquery-studio). For information about how to create queries in BigQuery Studio, see [Create saved queries](https://docs.cloud.google.com/bigquery/docs/work-with-saved-queries). The queries are saved in your Google Cloud project against a query name and a location.

You can also share the queries to other users. For details on how to share a saved query with a user, see [Share saved queries](https://docs.cloud.google.com/bigquery/docs/manage-saved-queries#share-saved-query).

### Query samples

The following query samples illustrate how to structure your queries.

#### Query for invoking Gemini models
    
    
    SELECT *
      FROM ML.GENERATE_TEXT(MODEL `PROJECT_ID_DATASET_GEMINI_MODEL`,
        (SELECT `UNIQUE_TABLE_FIELD` AS id,
     'PROMPT_TEXT' AS prompt
       FROM `PROJECT_ID_DATASET_TABLE`),
     STRUCT( <Temperature> AS temperature,
      <Top_P> AS top_p,
      <Top_K> AS top_k,
                <Max Output Token> AS max_output_tokens,
                   <Is Flatten JSON Output> AS flatten_json_output,
                <Stop Sequences[]> AS stop_sequences,
            <Ground with Google Search> AS ground_with_google_search,
            <Safety Settings[]> AS safety_settings ) );
    

Replace the following:

  * `PROJECT_ID_DATASET_GEMINI_MODEL`: The Gemini remote model created in your Google Cloud project, prefixed with project ID and BigQuery dataset.
  * `UNIQUE_TABLE_FIELD`: The unique table field in the BigQuery table against which you want to get the Gemini response.
  * `PROMPT_TEXT`: The prompt string that you want to provide Gemini.
  * `PROJECT_ID_DATASET_TABLE`: The BigQuery table having data which you want to analyze using Gemini with the passed prompt.



#### Query for keeping BigQuery vector database updated
    
    
    CREATE OR REPLACE TABLE `PROJECT_ID_DATASET_BQ_VECTOR_DB_TABLE` AS (
     SELECT id, content, ml_generate_embedding_result AS embedding
     FROM ML.GENERATE_EMBEDDING(
       MODEL `PROJECT_ID_DATASET_EMBEDDING_MODEL`,
       ( SELECT `TABLE_FIELD_NAME_WHICH_HAS_THE_TEXT` AS content,
                `<Unique Table Field>` as id
         FROM `PROJECT_ID_DATASET_TABLE` ),
       STRUCT( <Is Flatten JSON Output> AS flatten_json_output,
               <Task Type> as task_type,
               <Output Dimensionality> as output_dimensionality )));
    

Replace the following:

  * `PROJECT_ID_DATASET_BQ_VECTOR_DB_TABLE`: The BigQuery vector database table to store embeddings for your most recent enterprise data.
  * `PROJECT_ID_DATASET_EMBEDDING_MODEL`: The Gemini remote model created in your Google Cloud project, prefixed with project ID and BigQuery dataset.
  * `TABLE_FIELD_NAME_WHICH_HAS_THE_TEXT`: The BigQuery table field name which has the data for which you want to generate embeddings.
  * `UNIQUE_TABLE_FIELD`: The unique table field in the BigQuery table against which you want to save the embeddings in the BigQuery vector database table.
  * `PROJECT_ID_DATASET_TABLE`: The BigQuery table having data for which you want to generate embeddings.



#### Query for performing vector search
    
    
    DECLARE search_query STRING DEFAULT SEARCH_STRING;
    SELECT *
      FROM VECTOR_SEARCH(
      TABLE `PROJECT_ID_DATASET_BQ_VECTOR_DB_TABLE`, 'embedding',
      (
        SELECT ml_generate_embedding_result, content AS query
        FROM ML.GENERATE_EMBEDDING(
          MODEL `PROJECT_ID_DATASET_EMBEDDING_MODEL`,
          (SELECT search_query AS content))
        ), top_k => <number of nearest neighbors to return> );
    

Replace the following:

  * `SEARCH_STRING`: The natural language based search string against which you want to find similar items from the BigQuery vector database. You can also set a named parameter for this and pass the search string as a query parameter from ABAP application logic using the SDK.
  * `PROJECT_ID_DATASET_BQ_VECTOR_DB_TABLE`: The BigQuery vector database table name having the embeddings, prefixed with project ID and BigQuery dataset.
  * `PROJECT_ID_DATASET_EMBEDDING_MODEL`: The Gemini remote model created in your Google Cloud project, prefixed with project ID and BigQuery dataset.



## Retrieve enterprise queries from BigQuery

To retrieve the queries saved in BigQuery, use the ABAP class `/GOOG/CL_BQ_QUERY`. The class internally uses the [Dataform API](https://docs.cloud.google.com/dataform/reference/rest) to retrieve the saved queries, which are then used by other modules of the SDK.

### Instantiate the class

Instantiate the class by using the client key name and the query location.
    
    
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



The reference of the class once instantiated holds the saved query text, and is used by the other modules of the BigQuery AI and ML SDK for ABAP to refer to the saved query.

You can also pass the query as query text from program logic under parameter `IV_QUERY_TEXT`.
    
    
    TRY.
        DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                   iv_location_id = 'QUERY_LOCATION_ID'
           iv_query_text  = 'QUERY_TEXT' ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

### Override a set query

To override the set query in the reference of the class `/GOOG/CL_BQ_QUERY` with another query, use the method `SET_QUERY` of the class `/GOOG/CL_BQ_QUERY`. This replaces the query set at the time of instantiation of the class.

The overriding can be done either by passing the saved query name in BigQuery or the query text passed from the program logic.

#### Override using a saved query name
    
    
    lo_bq_query->set_query( iv_query_name = 'QUERY_NAME' ).
    

#### Override using a query text
    
    
    lo_bq_query->set_query( iv_query_text = 'QUERY_TEXT' ).
    

### Set query parameters

To pass named parameters for a [parameterized query](https://docs.cloud.google.com/bigquery/docs/parameterized-queries#using_structs_in_parameterized_queries) saved in BigQuery, use the method `SET_QUERY_PARAMETERS` of the class `/GOOG/CL_BQ_QUERY`. Parameter names for these parameters are of the same name as defined in the saved queries. Parameter values for the parameter names can be passed from the application logic during runtime using this method.
    
    
    DATA lt_query_parameters    TYPE /goog/cl_bq_query=>ty_t_query_parameters.
    <Prepare lt_query_parameters>
    TRY.
        DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                   iv_location_id = 'QUERY_LOCATION_ID'
           iv_query_name  = 'SAVED_QUERY_NAME' ).
        lo_bq_query->set_query_parameters( it_query_parameters = lt_query_patameters ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

#### Pass value based parameters

To pass value based parameters along with parameter name and type, use the method `SET_QUERY_PARAMETERS` of the class `/GOOG/CL_BQ_QUERY`.
    
    
    DATA lt_query_parameters    TYPE /goog/cl_bq_query=>ty_t_query_parameters,
    DATA ls_query_parameter     TYPE /goog/cl_bq_query=>ty_query_parameter.
    
    ls_query_parameter-parameter_name  = 'PARAMETER_NAME'.
    ls_query_parameter-parameter_type  = 'PARAMETER_TYPE'.
    ls_query_parameter-parameter_value = 'PARAMETER_VALUE'.
    
    APPEND ls_query_parameter TO lt_query_parameters.
    CLEAR ls_query_parameter.
    
    TRY.
        DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                   iv_location_id = 'QUERY_LOCATION_ID'
           iv_query_name  = 'SAVED_QUERY_NAME' ).
        lo_bq_query->set_query_parameters( it_query_parameters = lt_query_patameters ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `PARAMETER_NAME`: The name of the parameter defined in the saved query as named parameter.
  * `PARAMETER_TYPE`: The valid data type of the parameter.
  * `PARAMETER_VALUE`: The value in the form of a string.
  * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * `QUERY_LOCATION_ID`: The Google Cloud location under which the query is saved.
  * `SAVED_QUERY_NAME`: The name of the query with which the query is saved in BigQuery.



#### Pass array based parameters

To pass array based parameters along with the parameter name and array values, use the method `SET_QUERY_PARAMETERS` of the class `/GOOG/CL_BQ_QUERY`.
    
    
    DATA lt_query_parameters    TYPE /goog/cl_bq_query=>ty_t_query_parameters,
    DATA ls_query_parameter     TYPE /goog/cl_bq_query=>ty_query_parameter.
    
    ls_query_parameter-parameter_name  = 'PARAMETER_NAME'.
    ls_query_parameter-parameter_type = 'ARRAY'.
    ls_query_parameter-array_type = 'ARRAY_TYPE'.
    
    APPEND 'ARRAY_VALUE' TO ls_query_parameter-array_values.
    APPEND 'ARRAY_VALUE' TO ls_query_parameter-array_values.
    APPEND....
    
    APPEND ls_query_parameter TO lt_query_parameters.
    CLEAR ls_query_parameter.
    
    TRY.
        DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                   iv_location_id = 'QUERY_LOCATION_ID'
           iv_query_name  = 'SAVED_QUERY_NAME' ).
        lo_bq_query->set_query_parameters( it_query_parameters = lt_query_patameters ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `PARAMETER_NAME`: The name of the parameter defined in the saved query as named parameter.
  * `ARRAY_TYPE`: The valid array data type.
  * `ARRAY_VALUE`: The values of the array in the form of string,
  * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * `QUERY_LOCATION_ID`: The Google Cloud location under which the query is saved.
  * `SAVED_QUERY_NAME`: The name of the query with which the query is saved in BigQuery.



#### Pass struct based parameters

To pass a structure as a parameter along with the structure field name, structure field type and structure field value, use the method `SET_QUERY_PARAMETERS` of the class `/GOOG/CL_BQ_QUERY`.
    
    
    DATA lt_query_parameters    TYPE /goog/cl_bq_query=>ty_t_query_parameters,
    DATA ls_query_parameter     TYPE /goog/cl_bq_query=>ty_query_parameter,
    DATA ls_struct_values       TYPE /goog/cl_bq_query=>ty_struct_values.
    
    ls_query_parameter-parameter_name  = 'PARAMETER_NAME'.
    ls_query_parameter-parameter_type = 'STRUCT'.
    
    ls_struct_values-field_name = 'STRUCT_FIELD_NAME'.
    ls_struct_values-field_type = 'STRUCT_FIELD_TYPE'.
    ls_struct_values-field_value = 'STRUCT_FIELD_VALUE'.
    
    APPEND ls_struct_values TO ls_query_parameter-struct_values.
    CLEAR ls_struct_values.
    ....
    
    APPEND ls_query_parameter TO lt_query_parameters.
    CLEAR ls_query_parameter.
    
    TRY.
        DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                   iv_location_id = 'QUERY_LOCATION_ID'
           iv_query_name  = 'SAVED_QUERY_NAME' ).
        lo_bq_query->set_query_parameters( it_query_parameters = lt_query_patameters ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `PARAMETER_NAME`: The name of the parameter defined in the saved query as named parameter.
  * `STRUCT_FIELD_NAME`: The field name of the structure.
  * `STRUCT_FIELD_TYPE`: The valid struct data type.
  * `STRUCT_FIELD_VALUE`: The value of the structure field in the form of string.
  * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * `QUERY_LOCATION_ID`: The Google Cloud location under which the query is saved.
  * `SAVED_QUERY_NAME`: The name of the query with which the query is saved in BigQuery.



### Get query text

To fetch the query text for a query saved in BigQuery, use the method `GET_QUERY_TEXT` of the class `/GOOG/CL_BQ_QUERY`.
    
    
    TRY.
        DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                   iv_location_id = 'QUERY_LOCATION_ID'
           iv_query_name  = 'SAVED_QUERY_NAME' ).
        DATA(lv_query_text) = lo_bq_query->get_query_text( ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * `QUERY_LOCATION_ID`: The Google Cloud location under which the query is saved.
  * `SAVED_QUERY_NAME`: The name of the query with which the query is saved in BigQuery.



`LV_QUERY_TEXT` holds the query maintained against the `SAVED_QUERY_NAME`.

### Get query parameters

To fetch the query parameters set through the SDK method `SET_QUERY_PARAMETERS`, use the method `GET_QUERY_PARAMETERS` of the class `/GOOG/CL_BQ_QUERY`.
    
    
    DATA lt_query_parameters    TYPE /goog/cl_bq_query=>ty_t_query_parameters,
    DATA ls_query_parameter     TYPE /goog/cl_bq_query=>ty_query_parameter.
    
    ls_query_parameter-parameter_name  = 'PARAMETER_NAME'.
    ls_query_parameter-parameter_type  = 'PARAMETER_TYPE'.
    ls_query_parameter-parameter_value = 'PARAMETER_VALUE'.
    
    APPEND ls_query_parameter TO lt_query_parameters.
    CLEAR ls_query_parameter.
    
    TRY.
        DATA(lo_bq_query) = NEW /goog/cl_bq_query( iv_key         = 'CLIENT_KEY'
                                                   iv_location_id = 'QUERY_LOCATION_ID'
           iv_query_name  = 'SAVED_QUERY_NAME' ).
        lo_bq_query->set_query_parameters( it_query_parameters = lt_query_patameters ).
        DATA(lt_parameters) = lo_bq_query->get_query_parameters( ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `PARAMETER_NAME`: The name of the parameter defined in the saved query as named parameter.
  * `PARAMETER_TYPE`: The valid data type of the parameter.
  * `PARAMETER_VALUE`: The value in the form of a string.
  * `CLIENT_KEY`: The client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).
  * `QUERY_LOCATION_ID`: The Google Cloud location under which the query is saved.
  * `SAVED_QUERY_NAME`: The name of the query with which the query is saved on BigQuery.



`LT_PARAMETERS` holds the query parameters set against the `SAVED_QUERY_NAME`.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
