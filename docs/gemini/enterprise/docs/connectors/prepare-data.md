---
url: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/prepare-data/
title: Prepare data for custom data sources \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:28.745804+00:00
---

# Prepare data for custom data sources  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/connectors/prepare-data/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Prepare data for custom data sources Stay organized with collections  Save and categorize content based on your preferences. 

Enterprises often have custom applications that are built in-house. If you want Gemini Enterprise to connect to the data sources in these custom applications, first you need to prepare the data. How you prepare data depends on the kind of data that you're importing from your custom data source and the way you choose to import it. Start with what kind of data you plan to import:

  * Unstructured data
  * Structured data



For limitations for blended search, where multiple data stores can be connected to a single app, see [About connecting multiple data stores](https://docs.cloud.google.com/gemini/enterprise/docs/apps-data-stores#blended).

## Unstructured data

Gemini Enterprise supports search over documents that are in TXT, PDF, HTML, DOCX, PPTX, XLSX, and XLSM formats.

The following table lists the file size limits of each file type with different configurations (for more information, see [Parse and chunk documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents)). You can import up to 100,000 files at a time.

File type | Default import  
---|---  
Text-based files such as HTML, TXT, JSON, XHTML, and XML | < 200 MB  
PPTX, DOCX, XLSX, and XLSM | < 200 MB  
PDF | < 200 MB  
  
If you plan to include embeddings in your unstructured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation.

If you have non-searchable PDFs (scanned PDFs or PDFs with text inside images, such as infographics), we recommend turning on the layout parser during data store creation. This allows Gemini Enterprise to extract elements such as text blocks and tables. If you have searchable PDFs that are mostly composed of machine-readable text and contain many tables, you can consider turning on OCR processing with the option for machine-readable text enabled in order to improve detection and parsing. For more information, see [Parse and chunk documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents).

If you want to use Gemini Enterprise for retrieval-augmented generation (RAG), turn on document chunking when you create your data store. For more information, see [Parse and chunk documents](https://docs.cloud.google.com/gemini/enterprise/docs/parse-chunk-documents).

You can import unstructured data from the following sources:

  * Cloud Storage
  * BigQuery
  * Google Drive



### Cloud Storage

You can import data from Cloud Storage with or without metadata using [Google Cloud console](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage), by the `ImportDocuments` method, or by streaming ingestion through CRUD methods. For API reference information, see [`DocumentService`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.cloud.discoveryengine.v1#documentservice) and [`documents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents).

Data import is recursive. That is, if there are folders within the bucket or folder that you specify, files within those folders are imported.

If you plan to import documents from Cloud Storage without metadata, put your documents directly into a Cloud Storage bucket. The document ID is an example of metadata.

For testing, you can use the following publicly available Cloud Storage folders, which contain PDFs:

  * `gs://cloud-samples-data/gen-app-builder/search/alphabet-investor-pdfs`
  * `gs://cloud-samples-data/gen-app-builder/search/CUAD_v1`
  * `gs://cloud-samples-data/gen-app-builder/search/kaiser-health-surveys`
  * `gs://cloud-samples-data/gen-app-builder/search/stanford-cs-224`



If you plan to import data from Cloud Storage with metadata, put a JSON file that contains the metadata into a Cloud Storage bucket whose location you provide during import.

Your unstructured documents can be in the same Cloud Storage bucket as your metadata or a different one.

The metadata file must be a [JSON Lines](https://jsonlines.org/) or an NDJSON file. The document ID is an example of metadata. Each row of the metadata file must follow one of the following JSON formats:

  * Using `jsonData`:
        
        { "id": "<your-id>", "jsonData": "<JSON string>", "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }
        

  * Using `structData`:
        
        { "id": "<your-id>", "structData": { <JSON object> }, "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }
        




Use the `uri` field in each row to point to the Cloud Storage location of the document.

Here is an example of an NDJSON metadata file for an unstructured document. In this example, each line of the metadata file points to a PDF document and contains the metadata for that document. The first two lines use `jsonData` and the second two lines use `structData`. With `structData` you don't need to escape quotation marks that appear within quotation marks.
    
    
    {"id":"doc-0","jsonData":"{\"title\":\"test_doc_0\",\"uri\":\"https://test_doc_0.html\",\"description\":\"This document uses a blue color theme\",\"color_theme\":\"blue\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_0.pdf"}}
    {"id":"doc-1","jsonData":"{\"title\":\"test_doc_1\",\"uri\":\"https://test_doc_1.html\",\"description\":\"This document uses a green color theme\",\"color_theme\":\"green\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_1.pdf"}}
    {"id":"doc-2","structData":{"title":"test_doc_2","uri":"https://test_doc_2.html","description":"This document uses a red color theme","color_theme":"red"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_3.pdf"}}
    {"id":"doc-3","structData":{"title":"test_doc_3","uri":"https://test_doc_3.html","description":"This is document uses a yellow color theme","color_theme":"yellow"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_4.pdf"}}
    

To create your data store, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).

### BigQuery

If you plan to import metadata from BigQuery, follow these steps:

  1. Create a BigQuery table that contains metadata. The document ID is an example of metadata.

  2. Put your unstructured documents into a Cloud Storage bucket.

You can import using [Google Cloud console](https://docs.cloud.google.com/gemini/enterprise/docs/connectors/connect-cloud-storage), by the `ImportDocuments` method, or by streaming ingestion through CRUD methods. For API reference information, see [`DocumentService`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rpc/google.cloud.discoveryengine.v1#documentservice) and [`documents`](https://docs.cloud.google.com/gemini/enterprise/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents).




Use the following BigQuery schema. Use the `uri` field in each record to point to the Cloud Storage location of the document.
    
    
    [
      {
        "name": "id",
        "mode": "REQUIRED",
        "type": "STRING",
        "fields": []
      },
      {
        "name": "jsonData",
        "mode": "NULLABLE",
        "type": "STRING",
        "fields": []
      },
      {
        "name": "content",
        "type": "RECORD",
        "mode": "NULLABLE",
        "fields": [
          {
            "name": "mimeType",
            "type": "STRING",
            "mode": "NULLABLE"
          },
          {
            "name": "uri",
            "type": "STRING",
            "mode": "NULLABLE"
          }
        ]
      }
    ]
    

For more information, see [Create and use tables](https://docs.cloud.google.com/bigquery/docs/tables) in the BigQuery documentation.

To create your data store, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).

### Google Drive

Syncing data from Google Drive is supported for search.

If you plan to import data from Google Drive, you must set up Google Identity as your identity provider in Gemini Enterprise. For information about setting up access control, see [Identity and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/identity).

To create your data store, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).

## Structured data

Prepare your data according to the import method that you plan to use.

You can import structured data from the following sources:

  * BigQuery
  * Cloud Storage
  * Local JSON data



When you import structured data from BigQuery or from Cloud Storage, you are given the option to import the data with metadata. (Structured with metadata is also referred to as _enhanced structured data_.)

### BigQuery

You can import structured data from BigQuery datasets.

Your schema is auto-detected. After importing, Google recommends that you edit the auto-detected schema to map key properties, such as titles. If you import using the API instead of the Google Cloud console, you have the option to provide your own schema as a JSON object. For more information, see [Provide or auto-detect a schema](https://docs.cloud.google.com/gemini/enterprise/docs/provide-schema).

For examples of publicly available structured data, see the [BigQuery public datasets](https://docs.cloud.google.com/bigquery/public-data).

If you plan to include embeddings in your structured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation.

If you select to import structured data with metadata, you include two fields in your BigQuery tables:

  * An `id` field to identify the document. If you import structured data without metadata, then the `id` is generated for you. Including metadata lets you specify the value of `id`.

  * A `jsonData` field that contains the data. For examples of `jsonData` strings, see the preceding section Cloud Storage.




Use the following BigQuery schema for structured data with metadata imports:
    
    
    [
      {
        "name": "id",
        "mode": "REQUIRED",
        "type": "STRING",
        "fields": []
      },
      {
        "name": "jsonData",
        "mode": "NULLABLE",
        "type": "STRING",
        "fields": []
      }
    ]
    

To create your data store, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).

**Notes** : 

  * You can't import from BigQuery tables that have external data sources. For information about external data sources in BigQuery, see [Introduction to external tables](https://docs.cloud.google.com/bigquery/docs/external-tables) in the _BigQuery documentation_.
  * If your BigQuery tables contain columns with flexible column names, those columns aren't imported. For information about flexible column names, see [Flexible column names](https://docs.cloud.google.com/bigquery/docs/schemas#flexible-column-names) in the _BigQuery documentation_.



### Cloud Storage

Structured data in Cloud Storage must be in either [JSON Lines](https://jsonlines.org/) or NDJSON format. Each file must be less than 2 GB, and each row of the file less than 1 MB. You can import up to 1,000 files in a single import request.

For examples of publicly available structured data, refer to the following folders in Cloud Storage, which contain NDJSON files:

  * `gs://cloud-samples-data/gen-app-builder/search/kaggle_movies`
  * `gs://cloud-samples-data/gen-app-builder/search/austin_311`



If you plan to include embeddings in your structured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation.

Here is an example of an NDJSON metadata file of structured data. Each line of the file represents a document and is made up of a set of fields.
    
    
    {"id": 10001, "title": "Hotel 1", "location": {"address": "1600 Amphitheatre Parkway, Mountain View, CA 94043"}, "available_date": "2024-02-10", "non_smoking": true, "rating": 3.7, "room_types": ["Deluxe", "Single", "Suite"]}
    {"id": 10002, "title": "Hotel 2", "location": {"address": "Manhattan, New York, NY 10001"}, "available_date": "2023-07-10", "non_smoking": false, "rating": 5.0, "room_types": ["Deluxe", "Double", "Suite"]}
    {"id": 10003, "title": "Hotel 3", "location": {"address": "Moffett Park, Sunnyvale, CA 94089"}, "available_date": "2023-06-24", "non_smoking": true, "rating": 2.5, "room_types": ["Double", "Penthouse", "Suite"]}
    

To create your data store, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).

### Local JSON data

You can directly upload a JSON document or object using the API.

Google recommends providing your own schema as a JSON object for better results. If you don't provide your own schema, the schema is auto-detected. After importing, we recommend that you edit the auto-detected schema to map key properties, such as titles. For more information, see [Provide or auto-detect a schema](https://docs.cloud.google.com/gemini/enterprise/docs/provide-schema).

If you plan to include embeddings in your structured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings) in the Agent Search documentation.

To create your data store, see [Connect a Google data source](https://docs.cloud.google.com/gemini/enterprise/docs/create-data-store).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
