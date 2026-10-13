---
url: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/generate-embeddings/
title: Generate embeddings \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:58:39.034955+00:00
---

# Generate embeddings  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/generate-embeddings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Generate embeddings Stay organized with collections  Save and categorize content based on your preferences. 

On-premises or any cloud edition v1.14keyboard_arrow_down

  * [ SAP BTP edition v1.1 ](https://docs.cloud.google.com/sap/docs/abap-sdk/btp/latest/vertex-ai-sdk/generate-embeddings)
  * [ On-premises or any cloud edition v1.14 ](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/vertex-ai-sdk/generate-embeddings)



This document describes how to invoke the embedding models to generate text and multimodal embeddings, by using the Agent Platform SDK for ABAP.

[Embeddings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings) are essentially numerical codes that represent text, images, or videos in a way that captures how they are related. Applications use these codes to understand and generate language by recognizing semantic relationships within your content. The process works by transforming text, images, and videos into lists of numbers, known as vectors, which are designed to effectively capture the meaning of the original content.

Some common use cases for text embeddings include:

  * **Semantic search** : Search text ranked by semantic similarity.
  * **Classification** : Return the class of items whose text attributes are similar to the given text.
  * **Clustering** : Cluster items whose text attributes are similar to the given text.
  * **Outlier detection** : Return items where text attributes are least related to the given text.
  * **Conversational interface** : Clusters groups of sentences which can lead to similar responses, like in a conversation-level embedding space.



With the Agent Platform SDK for ABAP, you can generate embeddings from the ABAP application logic by using the classes and methods provided by the SDK. The SDK also provides built-in methods to push the generated embeddings to the following datastores:

  * Cloud Storage: You can use the embeddings from a Cloud Storage bucket for building vector indexes and performing Vector Search.
  * BigQuery: You can use the embeddings from a BigQuery dataset as a vector database for your enterprise data.



You can also publish the embeddings to a Pub/Sub topic to route them to a BigQuery dataset or to a subscriber system.

## Before you begin

Before using the Agent Platform SDK for ABAP with the embedding models, make sure that you or your administrators have completed the following prerequisites:

  * [Enabled the Agent Platform API](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#enable-api) in your Google Cloud project.
  * [Installed](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#installation) the Agent Platform SDK for ABAP in your SAP environment.
  * [Set up authentication](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#authentication) to access the Agent Platform API.
  * [Configured the model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters). For generating embeddings, only the following parameters are required: **Model Key** , **Model ID** , **Google Cloud Key Name** , **Google Cloud Region Location ID** and **Publisher ID of the LLM**.



## Generate embeddings

This section explains how to generate embeddings by using the Agent Platform SDK for ABAP.

### Instantiate the multimodal embeddings class

To invoke the Agent Platform multimodal embeddings models by using text or multimodal inputs, you can use the `/GOOG/CL_EMBEDDINGS_MODEL` class. You instantiate the class by passing the model key configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
    
    
    DATA(lo_embeddings_model) = NEW /goog/cl_embeddings_model( iv_model_key = 'MODEL_KEY' ).
    

Replace `MODEL_KEY` with the model key name, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).

### Generate text embeddings

To generate embeddings for a snippet of text, you can use the `GEN_TEXT_EMBEDDINGS` method of the `/GOOG/CL_EMBEDDINGS_MODEL` class. You can also optionally specify a dimension for the output embeddings.
    
    
    DATA(ls_addln_params) = VALUE /goog/cl_embeddings_model=>ty_addln_params(
                                    output_dimensionality = 'DIMENSION' ).
    DATA(lt_embeddings) = lo_embeddings_model->gen_text_embeddings(
                                                 iv_content      = 'INPUT_TEXT'
                                                 is_addln_params = ls_addln_params
                                            )->get_vector( ).
    

Replace the following:

  * `DIMENSION`: Optional. The dimensionality of the output embeddings. The default dimension is `768`.
  * `INPUT_TEXT`: The input text to generate embeddings for.



You can also generate embeddings for a snippet of text by using the `/GOOG/CL_EMBEDDINGS_MODEL=>TY_EMBEDDINGS_TEMPLATE` template provided by the SDK. This template lets you capture enterprise specific schematic information in the generated embeddings file along with the embeddings.

To generate embeddings for a snippet of text, based on the `/GOOG/CL_EMBEDDINGS_MODEL=>TY_EMBEDDINGS_TEMPLATE` template, you can use the `GEN_TEXT_EMBEDDINGS_BY_STRUCT` method.
    
    
    DATA(ls_embedding_template) = VALUE /goog/cl_embeddings_model=>ty_embeddings_template(
                                          id      = ENTITY_ID
                                          content = INPUT_TEXT
                                          source  = SOURCE_MODULE ).
    DATA(ls_addln_params) = VALUE /goog/cl_embeddings_model=>ty_addln_params(
                              output_dimensionality = 'DIMENSION' ).
    DATA(lt_embeddings) = lo_embeddings_model->gen_text_embeddings_by_struct(
                                                 is_input        = ls_embedding_template
                                                 is_addln_params = ls_addln_params
                                            )->get_vector_by_struct( ).
    

Replace the following:

  * `ENTITY_ID`: Entity ID for the embeddings record.
  * `INPUT_TEXT`: The input text to generate embeddings for.
  * `SOURCE_MODULE`: Source module of the embeddings content.
  * `DIMENSION`: Optional. The dimensionality of the output embeddings. The default dimension is `768`.



### Generate image embeddings

To generate embeddings for an input image, you can use the `GEN_IMAGE_EMBEDDINGS` method of the `/GOOG/CL_EMBEDDINGS_MODEL` class. You can either pass the raw data of an image or the Cloud Storage URI of an image file. You can also optionally specify a contextual text for the image and a dimension for the output embeddings.
    
    
    DATA(ls_image) = VALUE /goog/cl_embeddings_model=>ty_image( gcs_uri = 'IMAGE_URI' ).
    DATA(lt_embeddings) = lo_embeddings_model->gen_image_embeddings( iv_image           = ls_image
                                                                     iv_contextual_text = 'CONTEXTUAL_TEXT'
                                            )->get_vector( ).
    

Replace the following:

  * `IMAGE_URI`: The Cloud Storage URI of the target image to get embeddings for.
  * `CONTEXTUAL_TEXT`: Optional. Additional context and meaning to the content of an image to the embeddings model.



You can also generate embeddings for images by using the `/GOOG/CL_EMBEDDINGS_MODEL=>TY_EMBEDDINGS_TEMPLATE` template provided by the SDK. This template lets you capture enterprise specific schematic information in the generated embeddings file along with the embeddings.

To generate embeddings for an image, based on the `/GOOG/CL_EMBEDDINGS_MODEL=>TY_EMBEDDINGS_TEMPLATE` template, you can use the `GEN_IMAGE_EMBEDDINGS_BY_STRUCT` method.
    
    
    DATA(ls_image) = VALUE /goog/cl_embeddings_model=>ty_image( gcs_uri = 'IMAGE_URI' ).
    DATA(ls_embedding_template) = VALUE /goog/cl_embeddings_model=>ty_embeddings_template(
                                          id      = ENTITY_ID
                                          content = INPUT_TEXT
                                          source  = SOURCE_MODULE ).
    DATA(lt_embeddings) = lo_embeddings_model->gen_image_embeddings_by_struct(
                                                 iv_image = ls_image
                                                 is_input = ls_embedding_template
                                            )->get_vector_by_struct( ).
    

Replace the following:

  * `IMAGE_URI`: The Cloud Storage URI of the target image to get embeddings for.
  * `ENTITY_ID`: Entity ID for the embeddings record.
  * `INPUT_TEXT`: The input text to generate embeddings for.
  * `SOURCE_MODULE`: Source module of the embeddings content.



To retrieve embeddings for a contextual text, use the following code:
    
    
    DATA(lt_context_embeddings) = lo_embeddings_model->get_context_text_vector( ).
    

This option is available only for single image embedding creation.

### Generate video embeddings

To generate embeddings for an input video, you can use the `GET_VIDEO_EMBEDDINGS` method of the `/GOOG/CL_EMBEDDINGS_MODEL` class. You can pass the Cloud Storage URI of a video file along with optional start and end offset time in seconds. You can also optionally specify a contextual text for the video and a dimension for the output embeddings.
    
    
    DATA(ls_video) = VALUE /goog/cl_embeddings_model=>ty_video( gcs_uri = 'VIDEO_URI' ).
    DATA(lt_embeddings) = lo_embeddings_model->gen_video_embeddings( iv_video           = ls_video
                                                                     iv_contextual_text = 'CONTEXTUAL_TEXT'
                                                                     iv_dimension       = 'DIMENSION'
                                            )->get_vector( ).
    

  * `VIDEO_URI`: The Cloud Storage URI of the target video to get embeddings for.
  * `CONTEXTUAL_TEXT`: Optional. Additional context and meaning to the content of a video to the embeddings model.
  * `DIMENSION`: Optional. The dimensionality of the output embeddings. The available dimensions are: `128`, `256`, `512`, and `1408` (default).



The `GET_VECTOR` method returns the embeddings only for the first segment of the video.

To retrieve the embedding for contextual text, use the following code:
    
    
    DATA(lt_context_embeddings) = lo_embeddings_model->get_context_text_vector( ).
    

This option is available only for single video embedding creation.

### Collect all generated embeddings

To collect all generated embeddings in an internal table of type `/GOOG/CL_EMBEDDINGS_MODEL=>TY_T_EMBEDDINGS_TEMPLATE`, you can use the `COLLECT` method of the `/GOOG/CL_EMBEDDINGS_MODEL` class in combination with the methods `GEN_TEXT_EMBEDDINGS_BY_STRUCT` and `GEN_IMAGE_EMBEDDINGS_BY_STRUCT`.

Use this method to generate embeddings for an array of items (`text/image`) in a loop and collect all the embeddings into an internal table. Use the `GET_VECTOR_BY_TABLE` method to get the final internal table of embeddings.
    
    
    LOOP AT ....
    lo_embeddings_model->gen_text_embeddings_by_struct( is_input        = ls_embedding_template
                                                        is_addln_params = ls_addln_params
                      )->collect( ).
    
    ENDLOOP.
    
    DATA(lt_embeddings) = lo_embeddings_model->get_vector_by_table( ).
    

## Send embeddings to a datastore

You can send the generated embeddings to a Cloud Storage bucket or a BigQuery dataset by using the template provided by the SDK.

### Store embeddings in Cloud Storage

To send the generated embeddings to a Cloud Storage bucket, you can use the `SEND_STRUCT_TO_GCS` method of the `/GOOG/CL_EMBEDDINGS_MODEL` class.

Before sending embeddings to Cloud Storage, make sure to have a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/creating-buckets) that you want to send the embeddings to.

#### Send individual embeddings to a Cloud Storage bucket

The following code sample illustrates how to send individual image embeddings to a Cloud Storage bucket:
    
    
    DATA(ls_image) = VALUE /goog/cl_embeddings_model=>ty_image( gcs_uri = 'IMAGE_URI' ).
    lo_embeddings_model->gen_image_embeddings_by_struct( iv_image        = ls_image
                                                         is_input        = ls_embedding_template
                                                         is_addln_params = ls_addln_params
                      )->send_struct_to_gcs( iv_key         = 'CLIENT_KEY'
                                             iv_bucket_name = 'BUCKET_NAME'
                                             iv_file_name   = 'FILE_NAME' ).
    

Replace the following:

  * `IMAGE_URI`: The Cloud Storage URI of the target image to get embeddings for.
  * `CLIENT_KEY`: Client key for invoking the Cloud Storage API.
  * `BUCKET_NAME`: Target Cloud Storage bucket name.
  * `FILE_NAME`: Embeddings filename.



#### Send collected embeddings to a Cloud Storage bucket

The following code sample illustrates how to send collected embeddings to a Cloud Storage bucket:
    
    
    LOOP AT ....
    lo_embeddings_model->gen_text_embeddings_by_struct( is_input        = ls_embedding_template
                                                        is_addln_params = ls_addln_params
                      )->collect( ).
    
    ENDLOOP.
    
    lo_embeddings_model->send_struct_to_gcs( iv_key         = 'CLIENT_KEY'
                                             iv_bucket_name = 'BUCKET_NAME'
                                             iv_file_name   = 'FILE_NAME' ).
    

Replace the following:

  * `CLIENT_KEY`: Client key for invoking the Cloud Storage API.
  * `BUCKET_NAME`: Target Cloud Storage bucket name.
  * `FILE_NAME`: Embeddings filename.



### Store embeddings in BigQuery

To send the generated embeddings to a BigQuery dataset, you can use the `SEND_STRUCT_TO_BQ` method of the `/GOOG/CL_EMBEDDINGS_MODEL`.

Before sending embeddings to BigQuery, make sure to have a BigQuery [dataset](https://docs.cloud.google.com/bigquery/docs/datasets) and a [table](https://docs.cloud.google.com/bigquery/docs/tables#create-table) that you want to send the embeddings to.

#### Send individual embeddings to a BigQuery dataset

The following code sample illustrates how to send individual image embeddings to a BigQuery dataset:
    
    
    lo_embeddings_model->gen_image_embeddings_by_struct( iv_image        = ls_image
                                                         is_input        = ls_embedding_template
                                                         is_addln_params = ls_addln_params
                      )->send_struct_to_bq( iv_key        = 'CLIENT_KEY'
                                            iv_dataset_id = 'DATASET_ID'
                                            iv_table_id   = 'TABLE_ID' ).
    

Replace the following:

  * `CLIENT_KEY`: Client key for invoking the BigQuery API.
  * `DATASET_ID`: BigQuery dataset ID.
  * `TABLE_ID`: BigQuery table ID.



#### Send collected embeddings to a BigQuery dataset

The following code sample illustrates how to send collected embeddings to a BigQuery dataset:
    
    
    LOOP AT ....
    lo_embeddings_model->gen_text_embeddings_by_struct( is_input        = ls_embedding_template
                                                        is_addln_params = ls_addln_params
                      )->collect( ).
    
    ENDLOOP.
    
    lo_embeddings_model->send_struct_to_bq( iv_key        = 'CLIENT_KEY'
                                            iv_dataset_id = 'DATASET_ID'
                                            iv_table_id   = 'TABLE_ID' ).
    

Replace the following:

  * `CLIENT_KEY`: Client key for invoking the BigQuery API.
  * `DATASET_ID`: BigQuery dataset ID.
  * `TABLE_ID`: BigQuery table ID.



## Publish embeddings to a Pub/Sub topic

To publish the generated embeddings to a Pub/Sub topic, you can use the `SEND_STRUCT_TO_PUBSUB` method of the `/GOOG/CL_EMBEDDINGS_MODEL` class. This can be useful for scenarios where you need to build your own custom pipelines for storing embeddings and building follow-on business processes.

Before sending the embeddings to a Pub/Sub topic, make sure to have a [Pub/Sub topic](https://docs.cloud.google.com/pubsub/docs/create-topic#create_a_topic) that you want to send the embeddings to.

### Publish individual embeddings to a Pub/Sub topic

The following code sample illustrates how to publish individual image embeddings to a Pub/Sub topic:
    
    
    lo_embeddings_model->gen_image_embeddings_by_struct( iv_image        = ls_image
                                                         is_input        = ls_embedding_template
                                                         is_addln_params = ls_addln_params
                      )->send_struct_to_pubsub( iv_key      = 'CLIENT_KEY'
                                                iv_topic_id = 'TOPIC_ID' ).
    

Replace the following:

  * `CLIENT_KEY`: Client key for invoking the Pub/Sub API.
  * `TOPIC_ID`: Pub/Sub topic ID.



### Publish collected embeddings to a Pub/Sub topic

The following code sample illustrates how to publish collected embeddings to a Pub/Sub topic:
    
    
    LOOP AT ....
    lo_embeddings_model->gen_text_embeddings_by_struct( is_input        = ls_embedding_template
                                                        is_addln_params = ls_addln_params
                      )->collect( ).
    
    ENDLOOP.
    
    lo_embeddings_model->send_struct_to_pubsub( iv_key      = 'CLIENT_KEY'
                                                iv_topic_id = 'TOPIC_ID' ).
    

Replace the following:

  * `CLIENT_KEY`: Client key for invoking the Pub/Sub API.
  * `TOPIC_ID`: Pub/Sub topic ID.



## What's next

  * Learn about [application development with the on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/developer).
  * Ask your questions and discuss the Agent Platform SDK for ABAP with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
