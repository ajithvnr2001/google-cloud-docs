---
url: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/vector-search-for-intelligent-sap-applications/
title: Vector Search for intelligent SAP applications \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:46.272549+00:00
---

# Vector Search for intelligent SAP applications  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/vector-search-for-intelligent-sap-applications/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Vector Search for intelligent SAP applications Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a reference architecture for building intelligent SAP applications with [Agent Platform Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview), by using the [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview). With Vector Search, you can build SAP applications that go beyond keyword matching, using semantic understanding to help users find precisely what they need from their enterprise data. You can also use Vector Search with [Retrieval-augmented generation (RAG)](https://developers.google.com/machine-learning/glossary#retrieval-augmented_generation) to build powerful AI applications in your SAP environment. RAG improves the quality of your AI model's responses by providing relevant context from your enterprise data, ensuring that the AI model stays grounded to your enterprise data. 

The intended audience for this document includes ABAP developers, SAP solution architects, and cloud architects. This document assumes that you're familiar with the [Vector Search terminology](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview#terminology).

## Architecture

The following diagram shows a reference architecture for using Vector Search in SAP application landscape:

![Vector Search for SAP](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-vector-search-for-sap.svg)

This reference architecture includes the following components:

# | Component | Details  
---|---|---  
1 | Query starting point in SAP | Start a search by using one of the following options:

  * OData service: Provide a search query through the [OData service](https://community.sap.com/t5/technology-blogs-by-members/introduction-to-odata-and-how-to-implement-them-in-abap/ba-p/13474383) in your SAP frontend application.
  * SAP application logic: Provide a search query through SAP application logic, such as SAP enhancements, reports, or background jobs.

  
2 | Agent Platform SDK for ABAP | The Vector Search Invoker module of the SDK performs vector search based on your search query.  
3 | Vector Search | Enterprise data is indexed as vector embeddings and organized within a deployed index. When a search query is entered, a vector search is performed on this indexed data to find the closest matches. These closest matches are then returned to the SAP applications, enabling features such semantic search and RAG.  
  
## Products used

This reference architecture uses the following Google Cloud products:

  * [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/overview): Provides you with modules and toolsets to build AI-centric applications natively from ABAP.
  * [Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview): Allows high-scale and efficient searches across your enterprise data by using vector embeddings. This means that you can search by meaning and context, and not just keywords.



## Use Cases

The following list shows use cases of Vector Search in SAP applications:

  * **Building recommendation engines** : Analyze user inputs and behavior to suggest relevant items across SAP businesses such as products, company codes, and GL accounts, going beyond just keyword matching.
  * **Building RAG pipelines** : Access and integrate information from various sources to enrich an AI model's context with relevant SAP and non-SAP information to generate accurate and relevant model responses.
  * **Performing semantic image search** : Enable searching for visually similar images, useful for shopping, visual discovery, and medical imaging analysis.
  * **Performing semantic text search** : Understand the meaning and context of text to improve search accuracy in legal, academic, and customer feedback analysis.
  * **Performing Natural Language based search** : Provide instant answers to user questions, enhancing FAQs, knowledge bases, and educational tools.
  * **Performing anomaly detection** : Identify unusual patterns and potential threats in finance, network security, and manufacturing.



## Design considerations

This section provides guidance to help you use this reference architecture to develop architectures that help you meet your specific requirements for security, privacy, compliance, cost, and performance.

### Security, privacy, and compliance

Security and compliance are shared responsibilities. For detailed information, see [Gemini Enterprise Agent Platform shared responsibility](https://docs.cloud.google.com/vertex-ai/docs/shared-responsibility).

For information about Google Cloud's commitment to data privacy, see [Privacy Resource Center](https://cloud.google.com/privacy).

### Cost optimization

To lower your costs, consider choosing lower shard sizes and lower-dimensional embeddings for your indexes, which lets you use a smaller compute machine for deploying the indexes.

Agent Platform is a billable offering from Google Cloud. For information about pricing, see [Agent Platform pricing](https://cloud.google.com/vertex-ai/pricing) and [Vector Search pricing](https://cloud.google.com/vertex-ai/pricing#vectorsearch). To generate a cost estimate based on your projected usage, use the [Pricing Calculator](https://cloud.google.com/products/calculator/).

### Performance optimization

To improve latency to look up large datasets, consider choosing higher shard sizes while creating your index and high performance compute machines while deploying your index. To learn more about shard sizes for an index, see [Index size](https://docs.cloud.google.com/vertex-ai/docs/vector-search/create-manage-index#index_size).

To increase relevance of search responses, generate embeddings of your enterprise data in higher dimensions. Compute machines and higher embedding dimensions are cost intensive. To generate a cost estimate based on your projected usage, use the [Pricing Calculator](https://cloud.google.com/products/calculator/).

## Before you begin

Before using Vector Search in your SAP application landscape, make sure that you or your administrators have completed the following:

  * Installed the latest version of [on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/install-config).
  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the Vector Search parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-vector-search-parameters).



### Create and manage vector index

For using Vector Search, you need to have your enterprise data indexed and deployed in the form of vector embeddings. To achieve this, follow these steps:

  1. Generate vector embeddings by using text or multimodal embeddings AI models in Agent Platform or any other platform.
  2. Upload the embeddings into a Cloud Storage bucket.
  3. Create a vector index with the Cloud Storage bucket containing embeddings.
  4. Create an index endpoint and deploy the vector index to the endpoint to perform a semantic search on your indexed enterprise data.



You can perform the preceding steps from the Google Cloud console or use the [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search#create-manage-vector-index) to trigger these from your SAP environment.

To get the most accurate Vector Search results for an enterprise AI solution, you also need to keep the index updated with the most recent enterprise data. For more information, see [Update and rebuild a vector index](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search#update_and_rebuild_a_vector_index).

## Invoke Vector Search from SAP applications

From your SAP applications, you can use the Agent Platform SDK for ABAP to perform semantic searches on your indexed enterprise data in the following ways:

  * Search by using text prompts: Perform semantic search on your text and multimodal data by using search string.
  * Search by using multimodal prompts: Perform semantic search on your multimodal data by using multimodal input such as an image or a video.
  * Search by using enterprise entity IDs: Perform semantic search on your enterprise data by using enterprise specific IDs, such as product ID, order ID, or customer ID.



You can use the results from Vector Search to enhance your AI model's context with enterprise context using RAG. This keeps the model responses grounded to your enterprise data. You can also use these results as input for business processes or to generate recommendations.

### Semantic search by using text prompts

To search on your indexed text and multimodal data by using text prompts, you can use the `FIND_NEIGHBORS_BY_STRING` method of the `/GOOG/CL_VECTOR_SEARCH` class of the Agent Platform SDK for ABAP. You can chain the method `GET_NEAREST_NEIGHBORS` call with the method `FIND_NEIGHBORS_BY_STRING` call to get the search response.

The following code sample illustrates how to perform a semantic search by using text prompts:
    
    
    TRY.
        DATA(lo_vector_search) = NEW /goog/cl_vector_search( iv_search_key  = 'SEARCH_KEY' ).
        DATA(lt_vector_search_response) = lo_vector_search->find_neighbors_by_string(
                                                              iv_search_string         = 'SEARCH_STRING'
                                                              iv_embeddings_model_key  = 'MODEL_KEY'
                                                              iv_neighbor_count        = NEIGHBOR_COUNT
                                                         )->get_nearest_neighbors( ).
        cl_demo_output=>display( lt_vector_search_response ).
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( 'Search not successful.' && lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `SEARCH_KEY`: The search key, which is configured in the [Vector Search parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-vector-search-parameters).
  * `SEARCH_STRING`: The input text prompt.
  * `MODEL_KEY`: The model key configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters). This model is used for converting your search query into embeddings.
  * `NEIGHBOR_COUNT`: The number of nearest neighbors to be retrieved by the search query.



To find examples of text-based search on sample enterprise text and multimodal data, see the GitHub code samples for [Semantic search on text dataset using text prompts](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/zgoog_sdk_vector_search_recipe#semantic-search-on-text-dataset-using-text-prompts) and [Semantic search on images using text prompts](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/zgoog_sdk_vector_search_recipe#semantic-search-on-images-using-text-prompts).

### Semantic search by using multimodal prompts

This type of search is useful when you want to find closest matches from your multimodal data, which can be images or videos. For example, if you have an SAP web application (`Fiori` or `UI5`) and you want to take a picture of a clothing, a product, or an equipment part, and find the closest matches with respect to the picture, then you can choose this search option.

To search on your indexed multimodal data by using multimodal prompts, you can use the `FIND_NEIGHBORS_BY_EMBEDDING` method of the `/GOOG/CL_VECTOR_SEARCH` class of the Agent Platform SDK for ABAP. You can chain the method `GET_NEAREST_NEIGHBORS` call with the method `FIND_NEIGHBORS_BY_EMBEDDING` call to get the search response.

The following code sample illustrates how to perform a semantic search by using an image:
    
    
    DATA lv_search_string TYPE string,
    DATA ls_image TYPE /goog/cl_embeddings_model=>ty_image.
    
    TRY.
        DATA(lo_vector_search) = NEW /goog/cl_vector_search( iv_search_key = 'SEARCH_KEY' ).
        DATA(lo_embeddings_model) = NEW /goog/cl_embeddings_model( iv_model_key = 'MODEL_KEY' ).
    
        ls_image-bytes_base64_encoded = 'RAW_DATA'.
    
        DATA(lt_embeddings) = lo_embeddings_model->gen_image_embeddings( iv_image     = ls_image
                                                                         iv_dimension = 'DIMENSION'
                                                )->get_vector( ).
        DATA(lt_vector_search_response) = lo_vector_search->find_neighbors_by_embedding(
                                                              iv_neighbor_count = NEIGHBOR_COUNT
                                                              it_embeddings     = lt_embeddings
                                                         )->get_nearest_neighbors( ).
        cl_demo_output=>display( lt_vector_search_response ).
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( 'Search not successful.' && lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `SEARCH_KEY`: The search key, which is configured in the [Vector Search parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-vector-search-parameters).
  * `MODEL_KEY`: The model key configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters). This model is used for converting your search query into embeddings.
  * `RAW_DATA`: The Base64-encoded raw data of the image, PDF, or video to include inline in the query.
  * `DIMENSION`: The number of dimensions for the output embeddings.
  * `NEIGHBOR_COUNT`: The number of nearest neighbors to be retrieved by the search query.



To find examples of image based search on sample enterprise data, see the [GitHub code sample](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/zgoog_sdk_vector_search_recipe#semantic-search-on-images-using-image-prompts).

### Semantic search by using an enterprise entity ID

This type of search can be useful for SAP use cases where you would want to look up similar enterprise entities for a particular entity ID, for example finding or recommending similar products if a particular product is out of stock. Entity IDs correspond to the data points stored in your vector index.

To search a vector index by using an enterprise entity ID, you can use the `FIND_NEIGHBORS_BY_ENTITY_ID` method of the `/GOOG/CL_VECTOR_SEARCH` class of the Agent Platform SDK for ABAP. You can chain the method `GET_NEAREST_NEIGHBORS` call with the method `FIND_NEIGHBORS_BY_ENTITY_ID` call to get the search response.

The following code sample illustrates how to perform a semantic search by using an enterprise entity ID:
    
    
    Below is a code snippet that can be taken as reference for an entity id search.
    TRY.
        DATA(lo_vector_search) = NEW /goog/cl_vector_search( iv_search_key  = 'SEARCH_KEY' ).
        DATA(lt_vector_search_response) = lo_vector_search->find_neighbors_by_entity_id(
                                                              iv_entity_id = 'ENTITY_ID'
                                                         )->get_nearest_neighbors( ).
        cl_demo_output=>display( lt_vector_search_response ).
      CATCH /goog/cx_sdk INTO DATA(lo_cx_sdk).
        cl_demo_output=>display( 'Search not successful.' && lo_cx_sdk->get_text( ) ).
    
    ENDTRY.
    

Replace the following:

  * `SEARCH_KEY`: The search key, which is configured in the [Vector Search parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-vector-search-parameters).
  * `ENTITY_ID`: The entity ID to search.



To find examples of search by using entity ID on sample enterprise data, see the [GitHub code sample](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/zgoog_sdk_vector_search_recipe#semantic-search-using-an-enterprise-entity-id).

## Use Vector Search with RAG to provide additional context to your AI model

Vector Search brings back the most relevant enterprise data as a response based on your search query. You can provide additional context to your AI model by feeding it with the search response from Vector Search by using [RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation). RAG improves the quality of your AI model's responses by providing relevant context from retrieved enterprise data, ensuring that the model responses stay grounded to your enterprise data.

To provide additional context to your AI model by using Vector Search with RAG, perform the following steps:

  1. Prepare a search query to get the enterprise context.
  2. Perform Vector Search on the index that has the enterprise data.
  3. Concatenate or augment the search response to the final prompt following the best practices for efficient prompting.



To get the most relevant responses from AI models for your RAG based architectures, keep your index updated with the embeddings of your most recent enterprise data. For more information, see [Update and rebuild a vector index](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search#update_and_rebuild_a_vector_index).

To experiment with an enterprise use case with sample datasets, try out the [Vector Search fueled by Embeddings from SAP](https://github.com/GoogleCloudPlatform/google-cloud-abap/tree/main/abap-sdk/ZGOOG_SDK_RECIPES/zgoog_sdk_vector_search_recipe) sample solution on GitHub. This sample solution showcases a product recommendation engine in ABAP, providing guidance on required configurations and implementation details. You can use the sample codes and references as a basis for other recommendation systems, where you can execute semantic search directly from your SAP applications.

## What's next

  * To determine how relevant each search result is to your query, see [Get the distance of the fetched neighbor](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search#get_the_distance_of_the_fetched_neighbor).
  * To learn about how to use Vector Search with the Agent Platform SDK for ABAP, see [Use Agent Platform Vector Search](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search).
  * If you need help resolving problems with the ABAP SDK for Google Cloud, then do the following:

    * Refer to the [ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).
    * Ask your questions and discuss the ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).
    * Collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).



## Contributors

Author: [Devesh Singh](https://www.linkedin.com/in/devesh-singh-3447b054/) | SAP Application Engineer

Other contributor: [Vikash Kumar](https://www.linkedin.com/in/vikash-kumar-91923636/) | Technical Writer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
