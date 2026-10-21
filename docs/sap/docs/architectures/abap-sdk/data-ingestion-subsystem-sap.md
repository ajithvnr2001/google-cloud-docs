---
url: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/data-ingestion-subsystem-sap/
title: Design a data ingestion subsystem in SAP for RAG-capable generative AI applications \u00a0|\u00a0 SAP on Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T00:11:47.635407+00:00
---

# Design a data ingestion subsystem in SAP for RAG-capable generative AI applications  |  SAP on Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/data-ingestion-subsystem-sap/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ SAP on Google Cloud ](https://docs.cloud.google.com/sap/docs)
  * [ Guides ](https://docs.cloud.google.com/sap/docs/overview-of-sap-on-google-cloud)



Send feedback 

#  Design a data ingestion subsystem in SAP for RAG-capable generative AI applications Stay organized with collections  Save and categorize content based on your preferences. 

This document describes a reference architecture for designing a data ingestion subsystem in SAP to use with RAG-capable generative AI applications. This subsystem uses the [on-premises or any cloud edition of ABAP SDK for Google Cloud](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/all-guides) to integrate with the Google Cloud services required for building RAG-capable generative AI applications.

A [retrieval-augmented generation (RAG)](https://developers.google.com/machine-learning/glossary#retrieval-augmented-generation-rag) capable generative AI application has various components, among which the data ingestion subsystem is responsible for preparing and processing the enterprise data. This subsystem helps you prepare and store your enterprise data as embeddings in a vector database, for accurate and insightful AI interactions.

As many organizations use SAP ERP systems to store their enterprise data, this document offers guidance on integrating Google Cloud's data storage solutions and vector search databases as part of your data ingestion subsystem. This lets you make informed choices and effectively use Google Cloud's services to build a robust and efficient pipeline for your RAG-capable generative AI applications.

The intended audience for this document includes ABAP developers, SAP solution architects, and cloud architects. The document assumes that you're familiar with the [Vector Search terminology](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview#terminology) and [RAG](https://cloud.google.com/use-cases/retrieval-augmented-generation) concepts.

## Architecture

The following diagram shows a reference architecture illustrating the components of a data ingestion subsystem in SAP:

![Data ingestion subsystem in SAP](https://docs.cloud.google.com/static/sap/docs/architectures/architecture-images/abap-sdk/abap-sdk-data-ingestion-subsystem-sap.svg)

This data ingestion subsystem architecture includes the following components:

# | Component | Details  
---|---|---  
1 | Data ingestion subsystem | Prepares and processes enterprise data to generate vector embeddings. These embeddings are then stored in a suitable [vector database](https://cloud.google.com/discover/what-is-a-vector-database) on Google Cloud. Optionally, you can store your enterprise data on Google Cloud.  
2 | ABAP SDK for Google Cloud | The SDK handles communication between the data ingestion subsystem and various Google Cloud services.  
3 | Data storage | Optional. Google Cloud data storage solution such as BigQuery or Cloud Storage, used for storing enterprise data, both structured and unstructured. For more information, see Store enterprise data in Google Cloud.  
4 | Embeddings model (Agent Platform) | AI models that [generate embeddings](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/generate-embeddings) from various enterprise data sources.  
5 | Vector Search products | Stores embeddings in a [vector database](https://cloud.google.com/discover/what-is-a-vector-database) such as [Cloud Storage](https://docs.cloud.google.com/storage) or [BigQuery](https://docs.cloud.google.com/bigquery), where you can perform semantic search.  
  
## Data ingestion subsystem

This section explains the data ingestion subsystem that transforms your enterprise data into embeddings, and stores the embeddings in a vector database for use with RAG-capable generative AI applications. This subsystem can process a wide range of SAP data, including documents, images, business rules, and prompts, to generate embeddings.

### Prepare enterprise data

Before deploying your RAG-capable generative AI application for the first time, you need to load embeddings for existing enterprise data from your SAP system. You can handle this by building new batch programs or reusing existing ones that can read your enterprise data in manageable chunks.

Once you've performed the initial load of data and embeddings, your data ingestion subsystem needs to keep up with any changes in your SAP data. Whether it's new records, updates to existing ones, or deletions, the vector search index needs to reflect these changes. To do this, you can use appropriate spots within the SAP application development framework such as [Business Add-Ins (BAdIs)](https://help.sap.com/doc/saphelp_nw75/7.5.5/en-US/8f/f2e540f8648431e10000000a1550b0/frameset.htm) and [RAP Event Handlers](https://help.sap.com/doc/abapdocu_cp_index_htm/CLOUD/en-US/index.htm?file=abenrap_events.htm). This ensures your embeddings stay current and your AI applications always have the latest information.

### Store enterprise data in Google Cloud (optional)

SAP systems can contain both structured and unstructured enterprise data. Optionally, you can store this enterprise data in Google Cloud for retrieval from the [serving subsystem](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai#serving_subsystem).

To store your enterprise data, you can use the following Google Cloud services:

  * For streaming structured data from SAP to BigQuery, you can use the [BigQuery Connector for SAP](https://docs.cloud.google.com/sap/docs/bq-connector/whats-new) or use the `INSERT_ALL_TABLEDATA`method of the [`/GOOG/CL_BIGQUERY_V2`](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_bigquery_v2) class of the ABAP SDK for Google Cloud.
  * For storing unstructured data such as images and PDF documents in Cloud Storage, you can use the [`/GOOG/CL_STORAGE_V1`](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/reference/googcl_storage_v1) class of the ABAP SDK for Google Cloud. For a code sample that illustrates how to upload an object to a Cloud Storage bucket, see [Upload file to a bucket](https://docs.cloud.google.com/sap/docs/abap-sdk/samples/gcs-upload-file-bucket).
  * For configuring Cloud Storage as a content repository for SAP, you can implement and customize the sample solution available on GitHub, [Google Cloud Storage: Content Server for SAP](https://github.com/GoogleCloudPlatform/abap-sdk-sample-archivelink-content-repository).



### Generate embeddings from enterprise data

To generate text and multimodal embeddings from your enterprise data, you can use [embedding models](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions#embeddings_stable_model_versions) with the [Agent Platform SDK for ABAP](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/generate-embeddings).

[Embeddings](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/embeddings) are essentially numerical codes that represent text, images, or videos in a way that captures how they are related. Applications use these codes to understand and generate language, recognizing even the most complex meanings and relationships within your specific content. The process works by transforming text, images, and videos into lists of numbers, known as vectors, which are designed to effectively capture the meaning of the original content.

### Store the embeddings

To efficiently store and search the embeddings generated from your SAP enterprise data, you can use Google Cloud's vector search products, which act as a [vector database](https://cloud.google.com/discover/what-is-a-vector-database).

To store the embeddings for your SAP enterprise data, choose a vector database from the following list:

  * [Cloud Storage](https://docs.cloud.google.com/storage)
  * [Agent Platform Vector Search](https://docs.cloud.google.com/vertex-ai/docs/vector-search/overview)
  * [BigQuery](https://docs.cloud.google.com/bigquery)
  * [Agent Platform Feature Store](https://docs.cloud.google.com/vertex-ai/docs/featurestore/latest/overview)



#### Design considerations

The following are key design considerations for choosing a vector database:

  * **Performance** : Factors such as indexing speed for new vectors, search speed (latency), scalability, trade-off between retrieving all relevant results (recall) and only the most relevant ones (precision).
  * **Data characteristics** : Size of embedding vectors, size of vector dataset and data distribution impact cost, performance and indexing.
  * **Features** : Supported distance functions such as [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm) and [cosine similarity](https://en.wikipedia.org/wiki/Cosine_similarity), ability to do filtering, combining keyword and vector search, and support for approximate nearest neighbors (ANN) search.
  * **Integration** : Existing integration and ease of data ingestion from your applications.
  * **Cost** : Pricing model, storage, and query costs corresponding to the data and search volume.



To enable efficient search and analysis, store the embeddings in a vector database, along with the identifiers that link them back to their source data.

The decision to store enterprise data in a Google Cloud storage solution depends primarily on the location of your serving subsystem:

  * If your serving subsystem is SAP, then storing enterprise data outside of SAP is optional, as you already have access to your enterprise data within SAP.

  * If your serving subsystem resides outside of SAP, such as App Engine, then you might need to store your enterprise data in an appropriate Google Cloud storage solution for efficient data retrieval. You can avoid this if your serving subsystem can make remote calls into SAP to retrieve the data.




## Explore how to generate and store embeddings

This section explains how to generate and store embeddings from your enterprise data. There are two primary patterns for generating and storing embeddings:

  * **Generate embeddings in SAP** : Generate embeddings from the enterprise data residing in your SAP ERP system by using a suitable embeddings model with the Agent Platform SDK for ABAP, and store them in a vector database.

  * **Generate embeddings in Google Cloud** : Generate embeddings from the enterprise data residing in a storage medium on Google Cloud by using a serverless approach, such as Cloud Run functions or BigQuery, and store them in a vector database.




### Generate embeddings in SAP

To generate embeddings from SAP enterprise data locally within the SAP system, you can use various embedding models with the Agent Platform SDK for ABAP. These generated embeddings can then be sent to a suitable vector database on Google Cloud using one of the inbuilt ingestion mechanisms of the SDK.

You can decide which data to convert into embeddings based on your need for vector search capabilities. To learn about how to generate embeddings with the Agent Platform SDK for ABAP, see [Generate embeddings](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/generate-embeddings).

This section explains common SAP data types and how to generate embeddings by using the Agent Platform SDK for ABAP.

#### Structured enterprise data stored in SAP tables

You primarily generate embeddings for one or more text columns in SAP tables. For example, if you want to search suppliers by their name, address, or phone number, you concatenate values of these columns, and then generate a text-embedding of this combined value. Few other text values that are good candidates for text embedding are descriptions in text tables, long texts linked to business transactions.

The following code sample illustrates how to generate text embeddings and store them in a Cloud Storage bucket:
    
    
    DATA(lv_supplier) = CONV i_supplier-supplier( 'SUPPLIER' ).
    
    SELECT SINGLE
         concat_with_space( supplierfullname, phonenumber1, 1 )
           AS line
           FROM i_supplier
           WHERE supplier = @lv_supplier
           INTO @DATA(lv_search_string).
    
    DATA(ls_embedding_template) =
      VALUE /goog/cl_embeddings_model=>ty_embeddings_template(
             id = lv_supplier
             content = lv_search_string ).
    
    NEW /goog/cl_embeddings_model(
            iv_model_key = 'EMBEDDING_MODEL_KEY'
            )->gen_text_embeddings_by_struct(
            is_input = ls_embedding_template
            )->send_struct_to_gcs( iv_bucket_name = 'BUCKET_NAME' ).
    
    

Replace the following:

  * `SUPPLIER`: A unique alphanumeric code to identify a supplier.
  * `EMBEDDING_MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `BUCKET_NAME`: The name of the target Cloud Storage bucket.



#### Images

Many industries, including manufacturing and retail, capture and store images of key business objects such as raw materials, finished products, and a wide range of equipment. To enable efficient search for these business objects using either textual descriptions or visual similarity, you can use multimodal embeddings.

The following code sample illustrates how to generate multimodal embeddings for images and publish them to a Pub/Sub topic:
    
    
    "Populate image data in XSTRING format
    DATA(lv_image_xstring) = VALUE xstring( ).
    
    DATA(lv_image_base64) =
       xco_cp=>xstring( lv_image_xstring
        )->as_string( xco_cp_binary=>text_encoding->base64
        )->value.
    
    DATA(ls_image) =
      VALUE /goog/cl_embeddings_model=>ty_image(
         bytes_base64_encoded = lv_image_base64 ).
    
    DATA(ls_embedding_template) =
      VALUE /goog/cl_embeddings_model=>ty_embeddings_template(
             id = 'UNIQUE_ID'
             content = 'CONTEXTUAL_TEXT' ).
    
    NEW /goog/cl_embeddings_model(
            iv_model_key = 'EMBEDDING_MODEL_KEY'
            )->gen_image_embeddings_by_struct(
            iv_image = ls_image
            is_input = ls_embedding_template
            )->send_struct_to_pubsub( iv_topic_id = 'PUBSUB_TOPIC_ID' ).
    
    

Replace the following:

  * `UNIQUE_ID`: An identifier that uniquely identifies an image. For example, it can be a combination of filename and image creation date.
  * `CONTEXTUAL_TEXT`: Optional. Additional context and meaning to the input content that is passed to the embeddings model.
  * `EMBEDDING_MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `PUBSUB_TOPIC_ID`: The Pub/Sub topic ID to publish the embeddings to.



#### Documents

SAP business processes handle different types of documents such as contracts, manuals, guides, and safety data sheets. These documents can contain important information that are needed for making business decisions. To seamlessly find this data stored within documents, you can use multimodal embeddings. To effectively search within long documents, a chunking mechanism needs to be implemented. It divides the document into smaller units, such as pages or sections, enabling the contextualization of search results within a specific area.

The following code sample illustrates how to extract data from a PDF document and generate multimodal embeddings for each page, and then send those embeddings to a BigQuery table:
    
    
    "Populate PDF data in XSTRING format
    DATA(lv_pdf_xstring) = VALUE xstring( ).
    
    DATA(lv_pdf_base64) =
       xco_cp=>xstring( lv_pdf_xstring
        )->as_string( xco_cp_binary=>text_encoding->base64
        )->value.
    
    DATA(ls_document_input) = VALUE /goog/cl_documentai_v1=>ty_084(
       raw_document-content   = lv_pdf_base64
       raw_document-mime_type = 'application/pdf' ).
    
    NEW /goog/cl_documentai_v1( iv_key_name = 'DOC_AI_CLIENT_KEY'
        )->process_processors(
          EXPORTING
           iv_p_projects_id   = 'PROJECT_ID'
           iv_p_locations_id  = 'LOCATION_ID'
           iv_p_processors_id = 'PROCESSOR_ID'
           is_input           = ls_document_input
          IMPORTING
           es_output          = DATA(ls_docai_output) ).
    
    LOOP AT ls_docai_output-document-pages REFERENCE INTO DATA(ls_pages).
    
      DATA(ls_image) =
        VALUE /goog/cl_embeddings_model=>ty_image(
           bytes_base64_encoded = ls_pages->image-content ).
    
      DATA(ls_embedding_template) =
        VALUE /goog/cl_embeddings_model=>ty_embeddings_template(
               id = 'UNIQUE_ID'                 "Document Name + Page #
               content = 'CONTEXTUAL_TEXT' ).   "Optional Text
    
      NEW /goog/cl_embeddings_model(
              iv_model_key = 'EMBEDDING_MODEL_KEY'
              )->gen_image_embeddings_by_struct(
              iv_image = ls_image
              is_input = ls_embedding_template
              )->send_struct_to_bq(
              iv_dataset_id = 'BIGQUERY_DATASET_ID'
              iv_table_id   = 'BIGQUERY_TABLE_ID' ).
    
    ENDLOOP.
    

Replace the following:

  * `DOC_AI_CLIENT_KEY`: The client key for authentication.
  * `PROJECT_ID`: The ID of the Google Cloud project where the processor is created.
  * `LOCATION_ID`: The processor's location. For information about how to view processor details, see [View details about a processor](https://docs.cloud.google.com/document-ai/docs/create-processor).
  * `PROCESSOR_ID`: The ID of the processor. For information about how to view processor details, see [View details about a processor](https://docs.cloud.google.com/document-ai/docs/create-processor).
  * `UNIQUE_ID`: An identifier that uniquely identifies a specific chunk of knowledge. For example, it can be a combination of document name and page number.
  * `CONTEXTUAL_TEXT`: Optional. Additional context and meaning to the input content that is passed to the embeddings model.
  * `EMBEDDING_MODEL_KEY`: The model key for generating embeddings, which is configured in the [model generation parameters](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/install-configure-vertex-ai-sdk-abap#configure-model-generation-parameters).
  * `BIGQUERY_DATASET_ID`: The BigQuery dataset ID.
  * `BIGQUERY_TABLE_ID`: The BigQuery table ID.



### Generate embeddings in Google Cloud

As an alternative to generating embeddings in SAP, you can generate embeddings natively in Google Cloud with minimal to no coding. This approach requires you to store your enterprise data in Google Cloud before generating embeddings.

If your enterprise data is loaded to BigQuery, then you can generate text embeddings directly by running a SQL command. For more information, see [Generate text embeddings by using the `ML.GENERATE_EMBEDDING` function](https://docs.cloud.google.com/bigquery/docs/generate-text-embedding).

If your enterprise data is uploaded to a Cloud Storage bucket, then use one of the following methods for generating embeddings:

  * Develop a Cloud Run application. For more information, see [Infrastructure for a RAG-capable generative AI application using Gemini Enterprise Agent Platform](https://docs.cloud.google.com/architecture/rag-capable-gen-ai-app-using-vertex-ai#data_ingestion_subsystem).
  * For an [object table](https://docs.cloud.google.com/bigquery/docs/object-table-introduction) that represents the Cloud Storage bucket, use the `ML.GENERATE_EMBEDDING` function. For more information, see [Generate text embeddings by using the `ML.GENERATE_EMBEDDING` function](https://docs.cloud.google.com/bigquery/docs/generate-visual-content-embedding).



## What's next

  * To learn about how to use Vector Search for semantic search with SAP applications, see [Agent Platform Vector Search for intelligent SAP applications](https://docs.cloud.google.com/sap/docs/architectures/abap-sdk/vector-search-for-intelligent-sap-applications).

  * To learn about how to use Vector Search with the Agent Platform SDK for ABAP, see [Use Agent Platform Vector Search](https://docs.cloud.google.com/sap/docs/abap-sdk/vertex-ai-sdk/latest/use-vector-search).

  * If you need help resolving problems with the ABAP SDK for Google Cloud, then do the following:

    * Refer to the [ABAP SDK for Google Cloud troubleshooting guide](https://docs.cloud.google.com/sap/docs/abap-sdk/on-premises-or-any-cloud/latest/troubleshooting).
    * Ask your questions and discuss the ABAP SDK for Google Cloud with the community on [Cloud Forums](https://discuss.google.dev/tags/c/google-cloud/14/abap-sdk).
    * Collect all available diagnostic information and contact Cloud Customer Care. For information about contacting Customer Care, see [Getting support for SAP on Google Cloud](https://docs.cloud.google.com/sap/docs/getting-support).



## Contributors

Author: [Ajith Urimajalu](https://www.linkedin.com/in/ajith-urimajalu/) | SAP Application Engineer Team Lead

Other contributor: [Vikash Kumar](https://www.linkedin.com/in/vikash-kumar-91923636/) | Technical Writer

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
