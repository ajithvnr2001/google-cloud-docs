---
url: https://docs.cloud.google.com/document-ai/docs/toolbox/
title: Document AI Toolbox client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:11:43.141070+00:00
---

# Document AI Toolbox client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/toolbox/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Guides ](https://docs.cloud.google.com/document-ai/docs/overview)



Send feedback 

#  Document AI Toolbox client libraries Stay organized with collections  Save and categorize content based on your preferences. 

This page shows how to get started with the Cloud Client Libraries for the Document AI Toolbox API. Client libraries make it easier to access Google Cloud APIs from a supported language. Although you can use Google Cloud APIs directly by making raw requests to the server, client libraries provide simplifications that significantly reduce the amount of code you need to write.

Read more about the Cloud Client Libraries and the older Google API Client Libraries in [Client libraries explained](https://docs.cloud.google.com/apis/docs/client-libraries-explained).

**Experimental**

This library is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA libraries are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

## Install the client library

### Python
    
    
    pip install --upgrade google-cloud-documentai-toolbox

For more information, see [Setting Up a Python Development Environment](https://docs.cloud.google.com/python/docs/setup).

## Set up authentication

To authenticate calls to Google Cloud APIs, client libraries support [Application Default Credentials (ADC)](https://docs.cloud.google.com/docs/authentication/application-default-credentials); the libraries look for credentials in a set of defined locations and use those credentials to authenticate requests to the API. With ADC, you can make credentials available to your application in a variety of environments, such as local development or production, without needing to modify your application code. 

For production environments, the way you set up ADC depends on the service and context. For more information, see [Set up Application Default Credentials](https://docs.cloud.google.com/docs/authentication/provide-credentials-adc).

For a local development environment, you can set up ADC with the credentials that are associated with your Google Account:

  1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. After installation, [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the Google Cloud CLI by running the following command: 
         
         gcloud init

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  2. If you're using a local shell, then create local authentication credentials for your user account: 
         
         gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

A sign-in screen appears. After you sign in, your credentials are stored in the [ local credential file used by ADC](https://docs.cloud.google.com/docs/authentication/application-default-credentials#personal). 




## Use the client library

[Document AI Toolbox](https://docs.cloud.google.com/document-ai/docs/toolbox) is an SDK for Python that provides utility functions for managing, manipulating, and extracting information from the document response. It creates a "wrapped" document object from a processed document response from JSON files in Cloud Storage, local JSON files, or output directly from the [`process_document()`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/projects.locations.processors/process) method. 

It can perform the following actions: 

  * Combine fragmented [`Document`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document) JSON files from Batch Processing into a single "wrapped" document.
    * Export shards as a unified [`Document`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document).
  * Get [`Document`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document) output from: 
    * [Cloud Storage](https://docs.cloud.google.com/storage)
    * [`BatchProcessMetadata`](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/BatchProcessMetadata)
    * [`Operation` name](https://docs.cloud.google.com/document-ai/docs/reference/rest/Shared.Types/ListOperationsResponse#Operation.FIELDS.name)
  * Access text from [`Pages`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#page), [`Lines`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#line), [`Paragraphs`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#paragraph), [`FormFields`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#formfield), and [`Tables`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#table) without handling [`Layout`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#Layout) information.
  * Search for a [`Pages`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#page) containing a target string or matching a regular expression.
  * Search for [`FormFields`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#formfield) by name.
  * Search for [`Entities`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#entity) by type.
  * Convert [`Tables`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#table) to a [Pandas](https://pandas.pydata.org/) Dataframe or CSV.
  * Insert [`Entities`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#entity) and [`FormFields`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#formfield) into a [BigQuery](https://docs.cloud.google.com/bigquery) table.
  * Split a PDF file based on output from a Splitter/Classifier processor.
  * Extract image [`Entities`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#entity) from [`Document`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document) [bounding boxes](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document#boundingpoly).
  * Convert [`Documents`](https://docs.cloud.google.com/document-ai/docs/reference/rest/v1/Document) to and from commonly used formats: 
    * [Cloud Vision API](https://docs.cloud.google.com/vision) [`AnnotateFileResponse`](https://docs.cloud.google.com/vision/docs/reference/rest/v1/BatchAnnotateFilesResponse#AnnotateFileResponse)
    * [hOCR](https://en.wikipedia.org/wiki/HOCR)
    * Third-party document processing formats
**Note** : When importing documents and converting their annotations to the Document AI format, they will be classified as `Labeled` in the Google Cloud console.
  * Create batches of documents for processing from a Cloud Storage folder.



### Code Samples

The following code samples demonstrate how to use Document AI Toolbox.

### Quickstart
    
    
    from typing import Optional
    
    from google.cloud import documentai
    from google.cloud.documentai_toolbox import [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html), [gcs_utilities](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities.html)
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a Document JSON or sharded Document JSON in path gs://bucket/path/to/folder
    # gcs_bucket_name = "bucket"
    # gcs_prefix = "path/to/folder"
    
    # Or, given a Document JSON in path gs://bucket/path/to/folder/document.json
    # gcs_uri = "gs://bucket/path/to/folder/document.json"
    
    # Or, given a Document JSON in path local/path/to/folder/document.json
    # document_path = "local/path/to/folder/document.json"
    
    # Or, given a Document object from Document AI
    # documentai_document = documentai.Document()
    
    # Or, given a BatchProcessMetadata object from Document AI
    # operation = client.batch_process_documents(request)
    # operation.result(timeout=timeout)
    # batch_process_metadata = documentai.BatchProcessMetadata(operation.metadata)
    
    # Or, given a BatchProcessOperation name from Document AI
    # batch_process_operation = "projects/project_id/locations/location/operations/operation_id"
    
    
    def quickstart_sample(
        gcs_bucket_name: Optional[str] = None,
        gcs_prefix: Optional[str] = None,
        gcs_uri: Optional[str] = None,
        document_path: Optional[str] = None,
        documentai_document: Optional[documentai.Document] = None,
        batch_process_metadata: Optional[documentai.[BatchProcessMetadata](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchProcessMetadata.html)] = None,
        batch_process_operation: Optional[str] = None,
    ) -> document.Document:
        if gcs_bucket_name and gcs_prefix:
            # Load from Google Cloud Storage Directory
            print("Document structure in Cloud Storage")
            [gcs_utilities](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities.html).[print_gcs_document_tree](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities.html)(
                gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix
            )
    
            wrapped_document = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).Document.[from_gcs](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_from_gcs)(
                gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix
            )
        elif gcs_uri:
            # Load a single Document from a Google Cloud Storage URI
            wrapped_document = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).Document.[from_gcs_uri](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_from_gcs_uri)(gcs_uri=gcs_uri)
        elif document_path:
            # Load from local `Document` JSON file
            wrapped_document = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).Document.[from_document_path](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_from_document_path)(document_path)
        elif documentai_document:
            # Load from `documentai.Document` object
            wrapped_document = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).Document.[from_documentai_document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_from_documentai_document)(
                documentai_document
            )
        elif batch_process_metadata:
            # Load Documents from `BatchProcessMetadata` object
            wrapped_documents = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).Document.[from_batch_process_metadata](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_from_batch_process_metadata)(
                metadata=batch_process_metadata
            )
            wrapped_document = wrapped_documents[0]
        elif batch_process_operation:
            wrapped_documents = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).Document.[from_batch_process_operation](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_from_batch_process_operation)(
                location="us", operation_name=batch_process_operation
            )
            wrapped_document = wrapped_documents[0]
        else:
            raise ValueError("No document source provided.")
    
        # For all properties and methods, refer to:
        # https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document
    
        print("Document Successfully Loaded!")
        print(f"\t Number of Pages: {len(wrapped_document.pages)}")
        print(f"\t Number of Entities: {len(wrapped_document.entities)}")
    
        for page in wrapped_document.pages:
            print(f"Page {[page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).page_number}")
            for block in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).blocks:
                print(block.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
            for paragraph in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).paragraphs:
                print(paragraph.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
            for line in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).lines:
                print(line.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
            for token in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).tokens:
                print(token.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
    
            # Only supported with Form Parser processor
            # https://cloud.google.com/document-ai/docs/form-parser
            for form_field in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).form_fields:
                print(f"{form_field.field_name} : {form_field.field_value}")
    
            # Only supported with Enterprise Document OCR version `pretrained-ocr-v2.0-2023-06-02`
            # https://cloud.google.com/document-ai/docs/process-documents-ocr#enable_symbols
            for symbol in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).symbols:
                print(symbol.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
    
            # Only supported with Enterprise Document OCR version `pretrained-ocr-v2.0-2023-06-02`
            # https://cloud.google.com/document-ai/docs/process-documents-ocr#math_ocr
            for math_formula in [page](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.html).math_formulas:
                print(math_formula.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text))
    
        # Only supported with Entity Extraction processors
        # https://cloud.google.com/document-ai/docs/processors-list
        for entity in wrapped_document.entities:
            print(f"{[entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).type_} : {[entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).mention_text}")
            if [entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).normalized_text:
                print(f"\tNormalized Text: {[entity](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.html).normalized_text}")
    
        # Only supported with Layout Parser
        for chunk in wrapped_document.chunks:
            print(f"Chunk {chunk.chunk_id}: {chunk.content}")
    
        for block in wrapped_document.document_layout_blocks:
            print(f"Document Layout Block {block.block_id}")
    
            if block.text_block:
                print(f"{block.text_block.type_}: {block.text_block.[text](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement.html#google_cloud_documentai_toolbox_wrappers_page__BasePageElement_text)}")
            if block.list_block:
                print(f"{block.list_block.type_}: {block.list_block.list_entries}")
            if block.table_block:
                print(block.table_block.header_rows, block.table_block.body_rows)
    

### Tables
    
    
    from google.cloud.documentai_toolbox import document
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a local document.proto or sharded document.proto in path
    # document_path = "path/to/local/document.json"
    # output_file_prefix = "output/table"
    
    
    def table_sample(document_path: str, output_file_prefix: str) -> None:
        wrapped_document = document.Document.from_document_path(document_path=document_path)
    
        print("Tables in Document")
        for page in wrapped_document.pages:
            for table_index, table in enumerate(page.tables):
                # Convert table to Pandas Dataframe
                # Refer to https://pandas.pydata.org/docs/reference/frame.html for all supported methods
                df = table.to_dataframe()
                print(df)
    
                output_filename = f"{output_file_prefix}-{page.page_number}-{table_index}"
    
                # Write Dataframe to CSV file
                df.to_csv(f"{output_filename}.csv", index=False)
    
                # Write Dataframe to HTML file
                df.to_html(f"{output_filename}.html", index=False)
    
                # Write Dataframe to Markdown file
                df.to_markdown(f"{output_filename}.md", index=False)
    
    

### BigQuery export
    
    
    from google.cloud.documentai_toolbox import document
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a document.proto or sharded document.proto in path gs://bucket/path/to/folder
    # gcs_bucket_name = "bucket"
    # gcs_prefix = "path/to/folder"
    # dataset_name = "test_dataset"
    # table_name = "test_table"
    # project_id = "YOUR_PROJECT_ID"
    
    
    def entities_to_bigquery_sample(
        gcs_bucket_name: str,
        gcs_prefix: str,
        dataset_name: str,
        table_name: str,
        project_id: str,
    ) -> None:
        wrapped_document = document.Document.from_gcs(
            gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix
        )
    
        job = wrapped_document.entities_to_bigquery(
            dataset_name=dataset_name, table_name=table_name, project_id=project_id
        )
    
        # Also supported:
        # job = wrapped_document.form_fields_to_bigquery(
        #     dataset_name=dataset_name, table_name=table_name, project_id=project_id
        # )
    
        print("Document entities loaded into BigQuery")
        print(f"Job ID: {job.job_id}")
        print(f"Table: {job.destination.path}")
    
    

### PDF split
    
    
    from google.cloud.documentai_toolbox import document
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a local document.proto or sharded document.proto from a splitter/classifier in path
    # document_path = "path/to/local/document.json"
    # pdf_path = "path/to/local/document.pdf"
    # output_path = "resources/output/"
    
    
    def split_pdf_sample(document_path: str, pdf_path: str, output_path: str) -> None:
        wrapped_document = document.Document.from_document_path(document_path=document_path)
    
        output_files = wrapped_document.split_pdf(
            pdf_path=pdf_path, output_path=output_path
        )
    
        print("Document Successfully Split")
        for output_file in output_files:
            print(output_file)
    
    

### Image extraction
    
    
    from google.cloud.documentai_toolbox import document
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a local document.proto or sharded document.proto from an identity processor in path
    # document_path = "path/to/local/document.json"
    # output_path = "resources/output/"
    # output_file_prefix = "exported_photo"
    # output_file_extension = "png"
    
    
    def export_images_sample(
        document_path: str,
        output_path: str,
        output_file_prefix: str,
        output_file_extension: str,
    ) -> None:
        wrapped_document = document.Document.from_document_path(document_path=document_path)
    
        output_files = wrapped_document.export_images(
            output_path=output_path,
            output_file_prefix=output_file_prefix,
            output_file_extension=output_file_extension,
        )
        print("Images Successfully Exported")
        for output_file in output_files:
            print(output_file)
    
    

### Vision conversion
    
    
    from google.cloud.documentai_toolbox import document
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a document.proto or sharded document.proto in path gs://bucket/path/to/folder
    # gcs_bucket_name = "bucket"
    # gcs_prefix = "path/to/folder"
    
    
    def convert_document_to_vision_sample(
        gcs_bucket_name: str,
        gcs_prefix: str,
    ) -> None:
        wrapped_document = document.Document.from_gcs(
            gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix
        )
    
        # Converting wrapped_document to vision AnnotateFileResponse
        annotate_file_response = (
            wrapped_document.convert_document_to_annotate_file_response()
        )
    
        print("Document converted to AnnotateFileResponse!")
        print(
            f"Number of Pages : {len(annotate_file_response.responses[0].full_text_annotation.pages)}"
        )
    
    

### hOCR conversion
    
    
    from google.cloud.documentai_toolbox import document
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a document.proto or sharded document.proto in path gs://bucket/path/to/folder
    # document_path = "path/to/local/document.json"
    # document_title = "your-document-title"
    
    
    def convert_document_to_hocr_sample(document_path: str, document_title: str) -> str:
        wrapped_document = document.Document.from_document_path(document_path=document_path)
    
        # Converting wrapped_document to hOCR format
        hocr_string = wrapped_document.export_hocr_str(title=document_title)
    
        print("Document converted to hOCR!")
        return hocr_string
    
    

### Third-party conversion
    
    
    from google.cloud.documentai_toolbox import converter
    
    # TODO(developer): Uncomment these variables before running the sample.
    # This sample will convert external annotations to the Document.json format used by Document AI Workbench for training.
    # To process this the external annotation must have these type of objects:
    #       1) Type
    #       2) Text
    #       3) Bounding Box (bounding boxes must be 1 of the 3 optional types)
    #
    # This is the bare minimum requirement to convert the annotations but for better accuracy you will need to also have:
    #       1) Document width & height
    #
    # Bounding Box Types:
    #   Type 1:
    #       bounding_box:[{"x":1,"y":2},{"x":2,"y":2},{"x":2,"y":3},{"x":1,"y":3}]
    #   Type 2:
    #       bounding_box:{ "Width": 1, "Height": 1, "Left": 1, "Top": 1}
    #   Type 3:
    #       bounding_box: [1,2,2,2,2,3,1,3]
    #
    #   Note: If these types are not sufficient you can propose a feature request or contribute the new type and conversion functionality.
    #
    # Given a folders in gcs_input_path with the following structure :
    #
    # gs://path/to/input/folder
    #   ├──test_annotations.json
    #   ├──test_config.json
    #   └──test.pdf
    #
    # An example of the config is in sample-converter-configs/Azure/form-config.json
    #
    # location = "us",
    # processor_id = "my_processor_id"
    # gcs_input_path = "gs://path/to/input/folder"
    # gcs_output_path = "gs://path/to/input/folder"
    
    
    def convert_external_annotations_sample(
        location: str,
        processor_id: str,
        project_id: str,
        gcs_input_path: str,
        gcs_output_path: str,
    ) -> None:
        converter.convert_from_config(
            project_id=project_id,
            location=location,
            processor_id=processor_id,
            gcs_input_path=gcs_input_path,
            gcs_output_path=gcs_output_path,
        )
    
    

### Document batches
    
    
    from google.cloud import documentai
    from google.cloud.documentai_toolbox import [gcs_utilities](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities.html)
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given unprocessed documents in path gs://bucket/path/to/folder
    # gcs_bucket_name = "bucket"
    # gcs_prefix = "path/to/folder"
    # batch_size = 50
    
    
    def create_batches_sample(
        gcs_bucket_name: str,
        gcs_prefix: str,
        batch_size: int = 50,
    ) -> None:
        # Creating batches of documents for processing
        batches = [gcs_utilities](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities.html).[create_batches](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities.html)(
            gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix, batch_size=batch_size
        )
    
        print(f"{len(batches)} batch(es) created.")
        for batch in batches:
            print(f"{len(batch.gcs_documents.documents)} files in batch.")
            print(batch.gcs_documents.documents)
    
            # Use as input for batch_process_documents()
            # Refer to https://cloud.google.com/document-ai/docs/send-request
            # for how to send a batch processing request
            request = documentai.[BatchProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchProcessRequest.html)(
                name="processor_name", input_documents=batch
            )
            print(request)
    
    

### Merge Document shards
    
    
    from google.cloud import documentai
    from google.cloud.documentai_toolbox import [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html)
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Given a document.proto or sharded document.proto in path gs://bucket/path/to/folder
    # gcs_bucket_name = "bucket"
    # gcs_prefix = "path/to/folder"
    # output_file_name = "path/to/folder/file.json"
    
    
    def merge_document_shards_sample(
        gcs_bucket_name: str, gcs_prefix: str, output_file_name: str
    ) -> None:
        wrapped_document = [document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html).Document.[from_gcs](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_from_gcs)(
            gcs_bucket_name=gcs_bucket_name, gcs_prefix=gcs_prefix
        )
    
        merged_document = wrapped_document.[to_merged_documentai_document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document.html#google_cloud_documentai_toolbox_wrappers_document_Document_to_merged_documentai_document)()
    
        with open(output_file_name, "w") as f:
            f.write(documentai.Document.to_json(merged_document))
    
        print(f"Document with {len(wrapped_document.shards)} shards successfully merged.")
    
    

## Additional resources

### Python

The following list contains links to more resources related to the client library for Python:

  * [API reference](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest)
  * [Client libraries best practices](https://docs.cloud.google.com/apis/docs/client-libraries-best-practices)
  * [Issue tracker](https://github.com/googleapis/python-documentai-toolbox/issues)
  * [`cloud-document-ai` on Stack Overflow](https://stackoverflow.com/search?q=%5Bcloud-document-ai%5D+%5Bpython%5D)
  * [Source code](https://github.com/googleapis/python-documentai-toolbox)



[ Previous arrow_back  Regional and multi-regional support  ](https://docs.cloud.google.com/document-ai/docs/regions)

[ Next Client libraries  arrow_forward  ](https://docs.cloud.google.com/document-ai/docs/libraries)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
