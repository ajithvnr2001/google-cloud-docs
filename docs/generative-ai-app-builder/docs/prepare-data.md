---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data/
title: Prepare data for ingesting \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:41.084218+00:00
---

# Prepare data for ingesting  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/prepare-data/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Prepare data for ingesting Stay organized with collections  Save and categorize content based on your preferences. 

How you prepare data depends on the kind of data you're importing and the way you choose to import it. Start with what kind of data you plan to import:

  * Website data
  * Unstructured data
  * Structured data
  * Structured media data
  * Healthcare FHIR data



For information about blended search, where multiple data stores can be connected to a single custom search app, see [About connecting multiple data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#blended).

**Note:** Use multiple smaller data stores and search apps instead of one large data store. As your data store size increases, the search latency increases. Splitting your data into smaller, targeted data stores and connecting them to separate search apps helps maintain optimal performance and minimizes latency.

## Website data

When you create a data store for website data, you provide the URLs of web pages that Google should crawl and index for searching or recommending.

Before indexing your website data:

  * Decide which URL patterns to include in your indexing and which to exclude. You can include URL patterns either from the same or different domains that need to be indexed and exclude patterns that must not be indexed. The number of URL patterns that you can include and exclude differs in the following way: 

Indexing type  | Included sites  | Excluded sites   
---|---|---  
Basic website search  |  Maximum of 50 URL patterns  |  Maximum of 50 URL patterns   
Advanced website indexing  |  Maximum of 500 URL patterns  |  Maximum of 500 URL patterns   
  * Exclude the patterns for dynamic URLs. Dynamic URLs are URLs that change at the time of serving depending on the request.

One example of dynamic URLs is web pages that serve search results. The URL patterns for the web pages that serve the search results might be of the form `www.example.com/search?*`. If a user searches for the phrase `Nobel Prize`, the dynamic search URL might be a unique URL: `www.example.com/search?q=nobel%20prize/UNIQUE_STRING`. If the URL pattern `www.example.com/search?*` is not excluded, then all such unique, dynamic search URLs that follow this pattern are indexed. This results in diluted search quality, a bloated index, and increased index storage costs.

Some common patterns to exclude are the following:

Pattern type | Example pattern | Reason to exclude  
---|---|---  
Highlighted views | `example.com/*/highlight/true` | Alternate view of an existing post.  
Topic versus message paths | `example.com/*/td-p/*` | Alternate canonical path for the same message.  
Attachment permutations | `example.com/*?attachment-id=*` | Pages centered on attachments rather than content.  
User profiles | `example.com/*/user/*` | Low-value metadata pages that increase doc count.  
Dynamic search | `example.com/search?*` | All such unique, dynamic search URLs that follow this pattern are indexed. This results in diluted search quality, a bloated index, and increased index storage costs.  
**Caution:** If you forget to exclude dynamic URLs during initial data store setup, edit the **Sites to exclude** list as soon as possible: click **Data Stores** > data store name > **Add new websites** > **Sites to exclude**. Google Cloud doesn't issue refunds or billing credits for excess indexing charges resulting from incorrect pattern configurations.
  * Eliminate duplicate URLs using canonical URL patterns. This provides a single canonical URL for Google Search when crawling the website and removes ambiguity. For examples of canonicalization and more information, see [What is URL canonicalization](https://developers.google.com/search/docs/crawling-indexing/canonicalization) and [How to specify a canonical URL with rel="canonical" and other methods](https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls).

  * Avoid billable document bloat from URL variants: Many content management systems and community forum platforms (for example, Khoros and Discourse) serve the same page under multiple URL patterns. Agent Search treats each unique URL as a separate document, which can lead to:

    * Increased costs because you are billed for each unique URL variant stored in your data store.

    * Search quality dilution because search results can show the same content multiple times.

Identify the duplicate URL patterns before [creating a website data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es#website).

**Caution:** If you forget to exclude duplicate URLs during initial data store setup, edit the **Sites to exclude** list as soon as possible: click **Data Stores** > data store name > **Add new websites** > **Sites to exclude**. Google Cloud doesn't issue refunds or billing credits for excess indexing charges resulting from incorrect pattern configurations.
  * If you use the `robots.txt` file in your website, do the following:

    * [Verify Google's crawlers and fetchers](https://developers.google.com/search/docs/crawling-indexing/verifying-googlebot).

    * Make sure that [Google-CloudVertexBot](https://developers.google.com/search/docs/crawling-indexing/google-common-crawlers#google-cloudvertexbot) can access your content. `Google-CloudVertexBot` needs to crawl and index your information, including any paywalled content.

The following table lists the user agent string as it appears in the HTTP requests and the user agent token in `robots.txt` for `Google-CloudVertexBot`.

**User-Agent in HTTP requests** | 
    
    Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5X Build/MMB29P) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.7559.132 Mobile Safari/537.36 (compatible; Google-CloudVertexBot; +https://cloud.google.com/enterprise-search)  
  
---|---  
**robots.txt** |  | User-agent token in `robots.txt` |  `Google-CloudVertexBot`  
---|---  
Example `robots.txt` group | 
    
    user-agent: **Google-CloudVertexBot**
                  allow: /
                    
  
It is necessary for `Google-CloudVertexBot` to crawl and index your information, including the paywalled content. For more information on crawling and indexing your content, including paywalled content, see the following:

    * [Structured data for subscription and paywalled content](https://developers.google.com/search/docs/appearance/structured-data/paywalled-content)
    * [Fix Search-related JavaScript problems](https://developers.google.com/search/docs/crawling-indexing/javascript/fix-search-javascript)

    * Check that the web pages you plan to add to your data store don't block indexing.

    * If you submit a [sitemap](https://docs.cloud.google.com/generative-ai-app-builder/docs/index-refresh-sitemap) to index and refresh your web pages, make sure that your `robots.txt` file also permits the [Googlebot](https://developers.google.com/search/docs/crawling-indexing/googlebot) user agent to fetch the sitemap file. Agent Search crawls and indexes your web pages using `Google-CloudVertexBot`, but it fetches the sitemap file itself using `Googlebot`. If your `robots.txt` file, CDN, or firewall permits `Google-CloudVertexBot` but blocks `Googlebot`, your web pages are still crawled but the sitemap can't be fetched and its URLs aren't indexed or refreshed through the sitemap.

For more information, see [Introduction to robots.txt](https://developers.google.com/search/docs/crawling-indexing/robots/intro) and [How to write and submit a robots.txt file](https://developers.google.com/search/docs/crawling-indexing/robots/create-robots-txt).

  * In addition to allowing the crawler in your `robots.txt` file, your organization must allow the search requests through all the upstream proxy servers that your users might encounter.

  * If you plan to use [Advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features), you must be able to [verify the domains](https://docs.cloud.google.com/generative-ai-app-builder/docs/domain-verification) for the URL patterns in your data store.

  * Add structured data in the form of `meta` tags and PageMaps to your data store schema to enrich your indexing as explained in [Use structured data for advanced website indexing](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-website-metadata).

To see an example of inline documents ingestion, run the "Inline documents ingestion" notebook in one of the following environments: 

[![](https://docs.cloud.google.com/static/vertex-ai/images/colab-logo-32px.png)Open in Colab](https://colab.research.google.com/github/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/inline_ingestion_of_documents.ipynb) | [![](https://docs.cloud.google.com/static/vertex-ai/images/github-logo-32px.png)View on GitHub](https://github.com/GoogleCloudPlatform/generative-ai/blob/main/search/vais-building-blocks/inline_ingestion_of_documents.ipynb)




## Unstructured data

Agent Search supports search over documents that are in TXT, JSON, Markdown, PDF, HTML, DOCX, PPTX, XLSX, and XLSM formats.

The maximum size for a file is 200 MB, and you can import up to 100,000 files at a time.

You import your documents from a [Cloud Storage](https://docs.cloud.google.com/storage/docs) bucket. You can import using Google Cloud console, by the `ImportDocuments` method, or by streaming ingestion through CRUD methods. For API reference information, see [DocumentService](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#documentservice) and [`documents`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.dataStores.branches.documents). If you plan to include embeddings in your unstructured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings).

If you have non-searchable PDFs (scanned PDFs or PDFs with text inside images, such as infographics), we recommend turning on the layout parser during data store creation. This allows Agent Search to extract elements such as text blocks and tables. If you have searchable PDFs that are mostly composed of machine-readable text and contain many tables, you can consider turning on OCR processing with the option for machine-readable text enabled in order to improve detection and parsing. For more information, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).

If you want to use Agent Search for retrieval-augmented generation (RAG), turn on document chunking when you create your data store. For more information, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents).

You can import unstructured data from the following sources:

  * Cloud Storage
  * BigQuery
  * Google Drive



### Cloud Storage

You can import data from Cloud Storage with or without metadata.

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
    * `{ "id": "<your-id>", "jsonData": "<JSON string>", "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }`
  * Using `structData`: 
    * `{ "id": "<your-id>", "structData": { <JSON object> }, "content": { "mimeType": "<application/pdf or text/html>", "uri": "gs://<your-gcs-bucket>/directory/filename.pdf" } }`



Use the `uri` field in each row to point to the Cloud Storage location of the document.

Here is an example of an NDJSON metadata file for an unstructured document. In this example, each line of the metadata file points to a PDF document and contains the metadata for that document. The first two lines use `jsonData` and the second two lines use `structData`. With `structData` you don't need to escape quotation marks that appear within quotation marks.
    
    
    {"id":"doc-0","jsonData":"{\"title\":\"test_doc_0\",\"uri\":\"https://test_doc_0.html\",\"description\":\"This document uses a blue color theme\",\"color_theme\":\"blue\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_0.pdf"}}
    {"id":"doc-1","jsonData":"{\"title\":\"test_doc_1\",\"uri\":\"https://test_doc_1.html\",\"description\":\"This document uses a green color theme\",\"color_theme\":\"green\"}","content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_1.pdf"}}
    {"id":"doc-2","structData":{"title":"test_doc_2","uri":"https://test_doc_2.html", "description":"This document uses a red color theme","color_theme":"red"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_3.pdf"}}
    {"id":"doc-3","structData":{"title":"test_doc_3","uri":"https://test_doc_3.html","description":"This is document uses a yellow color theme","color_theme":"yellow"},"content":{"mimeType":"application/pdf","uri":"gs://test-bucket-12345678/test_doc_4.pdf"}}
    

To create your data store, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

### BigQuery

If you plan to import metadata from BigQuery, create a BigQuery table that contains metadata. The document ID is an example of metadata.

Put your unstructured documents into a Cloud Storage bucket.

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

To create your data store, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

### Google Drive

Syncing data from Google Drive is supported for custom search.

If you plan to import data from Google Drive, you must set up Google Identity as your identity provider in Agent Search. For information about setting up access control, see [Use data source access control](https://docs.cloud.google.com/generative-ai-app-builder/docs/data-source-access-control).

To create your data store, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

## Structured data

Prepare your data according to the import method that you plan to use. If you plan to ingest media data, also see Structured media data.

You can import structured data from the following sources:

  * Cloud Storage
  * Local JSON data



When you import structured data from BigQuery or from Cloud Storage, you are given the option to import the data with metadata. (Structured with metadata is also referred to as _enhanced structured data_.)

### BigQuery

You can import structured data from BigQuery datasets.

Your schema is auto-detected. After importing, Google recommends that you edit the auto-detected schema to map key properties, such as titles. If you import using the API instead of the Google Cloud console, you have the option to provide your own schema as a JSON object. For more information, see [Provide or auto-detect a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema).

For examples of publicly available structured data, see the [BigQuery public datasets](https://docs.cloud.google.com/bigquery/public-data).

If you plan to include embeddings in your structured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings).

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
    

For instructions on creating your data store, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es) or [Create a recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).

**Notes** : 

  * You can't import from BigQuery tables that have external data sources. For information about external data sources in BigQuery, see [Introduction to external tables](https://docs.cloud.google.com/bigquery/docs/external-tables) in the _BigQuery documentation_.
  * If your BigQuery tables contain columns with flexible column names, those columns aren't imported. For information about flexible column names, see [Flexible column names](https://docs.cloud.google.com/bigquery/docs/schemas#flexible-column-names) in the _BigQuery documentation_.



### Cloud Storage

Structured data in Cloud Storage must be in either [JSON Lines](https://jsonlines.org/) or NDJSON format. Each file must be less than 2 GB, and each row of the file less than 1 MB. You can import up to 1,000 files in a single import request.

For examples of publicly available structured data, refer to the following folders in Cloud Storage, which contain NDJSON files:

  * `gs://cloud-samples-data/gen-app-builder/search/kaggle_movies`
  * `gs://cloud-samples-data/gen-app-builder/search/austin_311`



If you plan to include embeddings in your structured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings).

Here is an example of an NDJSON metadata file of structured data. Each line of the file represents a document and is made up of a set of fields.
    
    
    {"id": 10001, "title": "Hotel 1", "location": {"address": "1600 Amphitheatre Parkway, Mountain View, CA 94043"}, "available_date": "2024-02-10", "non_smoking": true, "rating": 3.7, "room_types": ["Deluxe", "Single", "Suite"]}
    {"id": 10002, "title": "Hotel 2", "location": {"address": "Manhattan, New York, NY 10001"}, "available_date": "2023-07-10", "non_smoking": false, "rating": 5.0, "room_types": ["Deluxe", "Double", "Suite"]}
    {"id": 10003, "title": "Hotel 3", "location": {"address": "Moffett Park, Sunnyvale, CA 94089"}, "available_date": "2023-06-24", "non_smoking": true, "rating": 2.5, "room_types": ["Double", "Penthouse", "Suite"]}
    

To create your data store, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es) or [Create a recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).

### Local JSON data

You can directly upload a JSON document or object using the API.

Google recommends providing your own schema as a JSON object for better results. If you don't provide your own schema, the schema is auto-detected. After importing, we recommend that you edit the auto-detected schema to map key properties, such as titles. For more information, see [Provide or auto-detect a schema](https://docs.cloud.google.com/generative-ai-app-builder/docs/provide-schema).

If you plan to include embeddings in your structured data, see [Use custom embeddings](https://docs.cloud.google.com/generative-ai-app-builder/docs/bring-embeddings).

To create your data store, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es) or [Create a recommendations data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-recommendations).

## Structured media data

If you plan to ingest structured media data, such as videos, news, or music, review the following:

  * Information about your import method (BigQuery or Cloud Storage): Structured data
  * Required schemas and fields for media documents and data stores: [About media documents and data stores](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-documents)
  * User event requirements and schemas: [About media user events](https://docs.cloud.google.com/generative-ai-app-builder/docs/media-user-events)
  * Information about media recommendations types: [About media recommendations types](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-media-recommendations-types)



## Healthcare FHIR data

**Deprecated:** Agent Search for healthcare is deprecated and won't be available after May 15, 2027. 

If you plan to ingest FHIR data from Cloud Healthcare API, ensure the following:

  * Location: The source FHIR store must be in a Cloud Healthcare API dataset that's in the `us-central1`, `us`, or `eu` location. For more information, see [Create and manage datasets in Cloud Healthcare API](https://docs.cloud.google.com/healthcare-api/docs/datasets).
  * FHIR store type: The source FHIR store must be an R4 data store. You can check the versions of your FHIR stores by [listing the FHIR stores in your dataset](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir#listing_the_fhir_stores_in_a_dataset). To create a FHIR R4 store, see [Create FHIR stores](https://docs.cloud.google.com/healthcare-api/docs/how-tos/fhir#creating_a_fhir_store).
  * Import quota: The source FHIR store must have fewer than 1 million FHIR resources. If there are more than 1 million FHIR resources, the import process stops after this limit is reached. For more information, see [Quotas and limits](https://docs.cloud.google.com/generative-ai-app-builder/quotas).
  * Review the list of FHIR R4 resources that Agent Search supports. For more information, see [Healthcare FHIR R4 data schema reference](https://docs.cloud.google.com/generative-ai-app-builder/docs/fhir-schema-reference).
  * Resource references: Ensure that relative resource references are in the format `Resource/resourceId`. For example, `subject.reference` must have its value as `Patient/034AB16`. For more information on how Cloud Healthcare API supports FHIR resource references, see [FHIR resource references](https://docs.cloud.google.com/healthcare-api/docs/concepts/fhir-references).

  * The files referenced in a [`DocumentReference` resource](https://hl7.org/fhir/R4/documentreference.html) must be PDF, RTF, or image files that are stored in Cloud Storage. The link to the referenced files must be in the `content[].attachment.url` field of the resource in the standard Cloud Storage path format: `gs://BUCKET_NAME/PATH_TO_REFERENCED_FILE`.

The following table lists the file size limits of each file type with different configurations (for more information, see [Parse and chunk documents](https://docs.cloud.google.com/generative-ai-app-builder/docs/parse-chunk-documents)). You can import up to 100,000 files at a time.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-21 UTC."],[],[]] 
