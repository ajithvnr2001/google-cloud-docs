---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/perform-vector-search/
title: Perform vector search in BigQuery \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:14:07.468882+00:00
---

# Perform vector search in BigQuery  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/perform-vector-search/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Perform vector search in BigQuery Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/bq-ai-ml-sdk/perform-vector-search)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/perform-vector-search)



The BigQuery AI and ML SDK for ABAP lets you perform vector search on your vectorized enterprise data in BigQuery through natural language based search strings, and bring back the results, from your ABAP-based agents or applications.

BigQuery Vector Search lets you use GoogleSQL to do semantic search using vector indexes for approximate results. With Vector Search, you can find semantically similar data points within large datasets by using high-dimensional vectors or embeddings. You can store your vector embeddings in BigQuery, making BigQuery as your vector database and apply vector similarity search on it by using the BigQuery function [`VECTOR_SEARCH`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search).

## Before you begin

Before using the BigQuery AI and ML SDK for ABAP with the Gemini models, make sure that you or your administrators have completed the following prerequisites:

  * Enabled the BigQuery API in your Google Cloud project. For information about how to enable Google Cloud APIs, see [Enabling APIs](https://docs.cloud.google.com/apis/docs/getting-started#enabling_apis).
  * [Billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project).
  * You've your vector embeddings generated and stored in a vector dataset in BigQuery. For information on how to do that from your SAP applications by using the BigQuery AI and ML SDK for ABAP, see [Generate embeddings](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/generate-manage-embeddings#generate-embeddings).
  * You've created vector index of your enterprise data. For more information, see [Create a vector index](https://docs.cloud.google.com/bigquery/docs/vector-index#create_a_vector_index).
  * Granted [required permissions](https://docs.cloud.google.com/bigquery/docs/vector-search#required_permissions) to the service account configured in the client key for authentication.
  * [Installed the BigQuery AI and ML SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/install-configure-bq-ai-ml-sdk-abap) in your SAP environment.



## Pricing

The BigQuery AI and ML SDK for ABAP is offered at no cost. However, you're responsible for the charges for the `CREATE VECTOR INDEX` statement and the `VECTOR_SEARCH` function, which use BigQuery compute pricing.

To generate a cost estimate based on your projected usage, use the [pricing calculator](https://cloud.google.com/products/calculator).

For more information about BigQuery pricing, see the [BigQuery pricing](https://cloud.google.com/bigquery/pricing) page.

## Perform vector search on BigQuery

This section explains how to perform vector semantic search on your enterprise data stored in BigQuery from your ABAP application by using the BigQuery AI and ML SDK for ABAP.

### Instantiate the BigQuery vector search invoker class

To perform vector search using a search string, you instantiate the class `/GOOG/CL_BQ_VECTOR_SEARCH`.
    
    
    TRY.
        DATA(lo_bq_vector_search) = NEW /goog/cl_bq_vector_search( iv_key = 'CLIENT_KEY' ).
    CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace `CLIENT_KEY` with the client key that you've configured for authentication to Google Cloud during the [authentication setup](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/authentication).

### Find similar items for a search string

To run queries to perform vector search with BigQuery function `VECTOR_SEARCH`, use the method `FIND_NEAREST_NEIGHBORS` of the class `/GOOG/CL_BQ_VECTOR_SEARCH`.

The object of the class `/GOOG/CL_BQ_QUERY` set with the query is passed as an input to the method.
    
    
    lo_bq_vector_search->find_nearest_neighbors( io_query = lo_bq_query ).
    

`LO_BQ_QUERY` is the reference of the class `/GOOG/CL_BQ_QUERY` after [setting the query](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/bq-ai-ml-sdk/get-gemini-insights#set-gemini-query). You can pass the search string from the query text.

### Override vector search parameters

You can define [vector search parameters](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search) (under `VECTOR_SEARCH` function definitions) in the saved query on BigQuery or passed query text. But if you need to override the parameters for the same query from ABAP application logic, you can use the method `SET_SEARCH_PARAMETERS` of the class `/GOOG/CL_BQ_VECTOR_SEARCH` to do so. The search parameters in the initial query are completely overridden with the parameters passed through this method.
    
    
    lo_bq_vector_search->set_search_parameters( iv_top_k            = TOP_K
        iv_distance_type            = DISTANCE_TYPE
        iv_fraction_lists_to_search = 'FRACTION_LISTS_TO_SEARCH' ).
    

Replace the following:

  * `TOP_K`: An `INT64` value that specifies the number of nearest neighbors to return.
  * `DISTANCE_TYPE`: A string value that specifies the type of metric to use to compute the distance between two vectors, look for probable values from the `DISTANCE_TYPE` argument under definitions for the [`VECTOR_SEARCH`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search) function.
  * `FRACTION_LISTS_TO_SEARCH`: A string value that specifies the percentage of lists to search, look for probable values from `FRACTION_LISTS_TO_SEARCH` argument under options of definition of the [`VECTOR_SEARCH`](https://docs.cloud.google.com/bigquery/docs/reference/standard-sql/search_functions#vector_search) function.



## Get the vector search response

To receive processed responses from the BigQuery ML for vector search queries and present them in a meaningful way, use the class `/GOOG/CL_BQ_SEARCH_RESPONSE`.

The response captured by the `/GOOG/CL_BQ_SEARCH_RESPONSE` class is chained to the requests made through the methods of the `/GOOG/CL_BQ_VECTOR_SEARCH` class, so that you can directly access the response in a single statement without requiring variables to store the intermediate results.

### Get nearest neighbors for the search string

To get nearest neighbors for the search string, use the `GET_NEAREST_NEIGHBORS` method. The number of neighbors returned depends on the value specified or set in the `TOP_K` parameter of the function `VECTOR_SEARCH` in the invoked query.
    
    
    DATA(lt_search_response) = lo_bq_vector_search->find_nearest_neighbors( io_query = lo_bq_query
                                                 )->get_nearest_neighbors( ).
    

`LT_SEARCH_RESPONSE` also contains the distance of the search response item from the search string to indicate the degree of similarity.

### Get nearest neighbor for the search string

To get the nearest neighbor for the search string, use the `GET_NEAREST_NEIGHBOR` method. With this only the closest neighbor is fetched against the search string irrespective of the value specified or set in the `TOP_K` parameter of the function `VECTOR_SEARCH` in the invoked query.
    
    
    DATA(ls_search_response) = lo_bq_vector_search->find_nearest_neighbors( io_query = lo_bq_query
                                                 )->get_nearest_neighbor( ).
    

`LS_SEARCH_RESPONSE` also contains the distance of the search response from the search string to indicate the degree of similarity.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
