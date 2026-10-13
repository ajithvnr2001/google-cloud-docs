---
url: https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/summary_method/
title: Package Methods (0.17.4) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:26:56.813561+00:00
---

# Package Methods (0.17.4)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/summary_method/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Package Methods (0.17.4) Stay organized with collections  Save and categorize content based on your preferences. 

0.17.4 (latest)  0.17.3  0.16.0  0.15.2  0.14.2-a0  0.13.5-a0  0.12.2-a0  0.11.2-a0  0.10.3-a0  0.9.1-a0  0.8.0-a0  0.7.0-a0  0.6.0-a0  0.5.0-a0  0.4.1-a0  0.3.0-a0  0.2.1-a0  0.1.1-a0 

Summary of entries of Methods for documentai-toolbox.

## 

### google.cloud.documentai_toolbox.utilities.gcs_utilities._get_client_info
    
    
    _get_client_info(
        module: typing.Optional[str] = None,
    ) -> google.api_core.gapic_v1.client_info.ClientInfo

Returns a custom user agent header.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities._get_client_info](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities__get_client_info)

### google.cloud.documentai_toolbox.utilities.gcs_utilities._get_storage_client
    
    
    _get_storage_client(
        module: typing.Optional[str] = None,
    ) -> google.cloud.storage.client.Client

Returns a Storage client with custom user agent header.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities._get_storage_client](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities__get_storage_client)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.create_batches
    
    
    create_batches(
        gcs_bucket_name: str, gcs_prefix: str, batch_size: int = 1000
    ) -> typing.List[
        google.cloud.documentai_v1.types.document_io.BatchDocumentsInputConfig
    ]

Create batches of documents in Cloud Storage to process with `batch_process_documents()`.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.create_batches](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_create_batches)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.create_gcs_uri
    
    
    create_gcs_uri(gcs_bucket_name: str, gcs_prefix: str) -> str

Creates a Cloud Storage uri from the bucket_name and prefix.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.create_gcs_uri](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_create_gcs_uri)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.get_blob
    
    
    get_blob(
        gcs_uri: str, module: typing.Optional[str] = "get-bytes"
    ) -> google.cloud.storage.blob.Blob

Returns a blob from Cloud Storage.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.get_blob](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_get_blob)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.get_blobs
    
    
    get_blobs(
        gcs_uri: typing.Optional[str] = None,
        gcs_bucket_name: typing.Optional[str] = None,
        gcs_prefix: typing.Optional[str] = "/",
        module: typing.Optional[str] = "get-bytes",
    ) -> typing.List[google.cloud.storage.blob.Blob]

Returns a list of blobs from Cloud Storage.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.get_blobs](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_get_blobs)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.get_bytes
    
    
    get_bytes(gcs_bucket_name: str, gcs_prefix: str) -> typing.List[bytes]

Returns a list of bytes of json files from Cloud Storage.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.get_bytes](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_get_bytes)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.list_gcs_document_tree
    
    
    list_gcs_document_tree(
        gcs_bucket_name: str, gcs_prefix: str
    ) -> typing.Dict[str, typing.List[str]]

Returns a list path to files in Cloud Storage folder.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.list_gcs_document_tree](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_list_gcs_document_tree)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.print_gcs_document_tree
    
    
    print_gcs_document_tree(
        gcs_bucket_name: str, gcs_prefix: str, files_to_display: int = 4
    ) -> None

Prints a tree of filenames in a Cloud Storage folder.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.print_gcs_document_tree](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_print_gcs_document_tree)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.split_gcs_uri
    
    
    split_gcs_uri(gcs_uri: str) -> typing.Tuple[str, str]

Splits a Cloud Storage uri into the bucket_name and prefix.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.split_gcs_uri](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_split_gcs_uri)

### google.cloud.documentai_toolbox.utilities.gcs_utilities.upload_file
    
    
    upload_file(
        gcs_output_directory: str,
        file_name: str,
        file_content: str,
        content_type: str = "application/json",
        module: typing.Optional[str] = "upload-file",
    ) -> None

Uploads the converted docproto to gcs.

See more: [google.cloud.documentai_toolbox.utilities.gcs_utilities.upload_file](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.utilities.gcs_utilities#google_cloud_documentai_toolbox_utilities_gcs_utilities_upload_file)

### google.cloud.documentai_toolbox.wrappers.document._apply_text_offset
    
    
    _apply_text_offset(
        documentai_object: typing.Union[
            typing.Dict[str, typing.Any], typing.List[typing.Any]
        ],
        text_offset: int,
    ) -> None

Applies a text offset to all text_segments in `documentai_object`.

See more: [google.cloud.documentai_toolbox.wrappers.document._apply_text_offset](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__apply_text_offset)

### google.cloud.documentai_toolbox.wrappers.document._bigquery_column_name
    
    
    _bigquery_column_name(input_string: str) -> str

Converts a string into a BigQuery column name.

See more: [google.cloud.documentai_toolbox.wrappers.document._bigquery_column_name](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__bigquery_column_name)

### google.cloud.documentai_toolbox.wrappers.document._dict_to_bigquery
    
    
    _dict_to_bigquery(
        dic: typing.Dict[str, typing.Union[str, typing.List[str]]],
        dataset_name: str,
        table_name: str,
        project_id: typing.Optional[str],
    ) -> google.cloud.bigquery.job.load.LoadJob

Loads dictionary to a BigQuery table.

See more: [google.cloud.documentai_toolbox.wrappers.document._dict_to_bigquery](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__dict_to_bigquery)

### google.cloud.documentai_toolbox.wrappers.document._entities_from_shards
    
    
    _entities_from_shards(
        shards: typing.List[google.cloud.documentai_v1.types.document.Document],
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.entity.Entity]

Returns a list of Entities and Properties from a list of documentai.Document shards.

See more: [google.cloud.documentai_toolbox.wrappers.document._entities_from_shards](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__entities_from_shards)

### google.cloud.documentai_toolbox.wrappers.document._get_batch_process_metadata
    
    
    _get_batch_process_metadata(
        operation_name: str,
        location: typing.Optional[str] = None,
        timeout: typing.Optional[float] = None,
    ) -> google.cloud.documentai_v1.types.document_processor_service.BatchProcessMetadata

Get `BatchProcessMetadata` from a `batch_process_documents()` long-running operation.

See more: [google.cloud.documentai_toolbox.wrappers.document._get_batch_process_metadata](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__get_batch_process_metadata)

### google.cloud.documentai_toolbox.wrappers.document._get_shards
    
    
    _get_shards(
        gcs_bucket_name: str, gcs_prefix: str
    ) -> typing.List[google.cloud.documentai_v1.types.document.Document]

Returns a list of `documentai.Document` shards from a Cloud Storage folder.

See more: [google.cloud.documentai_toolbox.wrappers.document._get_shards](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__get_shards)

### google.cloud.documentai_toolbox.wrappers.document._insert_into_dictionary_with_list
    
    
    _insert_into_dictionary_with_list(
        dic: typing.Dict[str, typing.Union[str, typing.List[str]]], key: str, value: str
    ) -> typing.Dict[str, typing.Union[str, typing.List[str]]]

Inserts value into a dictionary that can contain lists.

See more: [google.cloud.documentai_toolbox.wrappers.document._insert_into_dictionary_with_list](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__insert_into_dictionary_with_list)

### google.cloud.documentai_toolbox.wrappers.document._pages_from_shards
    
    
    _pages_from_shards(
        shards: typing.List[google.cloud.documentai_v1.types.document.Document],
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.page.Page]

Returns a list of Pages from a list of documentai.Document shards.

See more: [google.cloud.documentai_toolbox.wrappers.document._pages_from_shards](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document#google_cloud_documentai_toolbox_wrappers_document__pages_from_shards)

### google.cloud.documentai_toolbox.wrappers.page._get_hocr_bounding_box
    
    
    _get_hocr_bounding_box(
        element_with_layout: typing.Union[
            google.cloud.documentai_v1.types.document.Document.Page.Paragraph,
            google.cloud.documentai_v1.types.document.Document.Page,
            google.cloud.documentai_v1.types.document.Document.Page.Token,
            google.cloud.documentai_v1.types.document.Document.Page.Block,
            google.cloud.documentai_v1.types.document.Document.Page.Symbol,
        ],
        page_dimension: google.cloud.documentai_v1.types.document.Document.Page.Dimension,
    ) -> typing.Optional[str]

Returns a hOCR bounding box string.

See more: [google.cloud.documentai_toolbox.wrappers.page._get_hocr_bounding_box](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page#google_cloud_documentai_toolbox_wrappers_page__get_hocr_bounding_box)

### google.cloud.documentai_toolbox.wrappers.page._text_from_layout
    
    
    _text_from_layout(
        layout: google.cloud.documentai_v1.types.document.Document.Page.Layout, text: str
    ) -> str

Returns a text from a single layout element.

See more: [google.cloud.documentai_toolbox.wrappers.page._text_from_layout](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page#google_cloud_documentai_toolbox_wrappers_page__text_from_layout)

### google.cloud.documentai_toolbox.wrappers.page._trim_text
    
    
    _trim_text(text: str) -> str

Remove extra space characters from text (blank, newline, tab, etc.) .

See more: [google.cloud.documentai_toolbox.wrappers.page._trim_text](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page#google_cloud_documentai_toolbox_wrappers_page__trim_text)

### google.cloud.documentai_toolbox.wrappers.document.Document.convert_document_to_annotate_file_json_response
    
    
    convert_document_to_annotate_file_json_response() -> str

Convert OCR data from `Document.proto` to JSON str of `AnnotateFileResponse` for Vision API.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.convert_document_to_annotate_file_json_response](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_convert_document_to_annotate_file_json_response)

### google.cloud.documentai_toolbox.wrappers.document.Document.convert_document_to_annotate_file_response
    
    
    convert_document_to_annotate_file_response() -> (
        google.cloud.vision_v1.types.image_annotator.AnnotateFileResponse
    )

Convert OCR data from `Document.proto` to `AnnotateFileResponse.proto` for Vision API.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.convert_document_to_annotate_file_response](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_convert_document_to_annotate_file_response)

### google.cloud.documentai_toolbox.wrappers.document.Document.entities_to_bigquery
    
    
    entities_to_bigquery(
        dataset_name: str, table_name: str, project_id: typing.Optional[str] = None
    ) -> google.cloud.bigquery.job.load.LoadJob

Adds extracted entities to a BigQuery table.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.entities_to_bigquery](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_entities_to_bigquery)

### google.cloud.documentai_toolbox.wrappers.document.Document.entities_to_dict
    
    
    entities_to_dict() -> typing.Dict[str, typing.Union[str, typing.List[str]]]

Returns Dictionary of entities in document.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.entities_to_dict](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_entities_to_dict)

### google.cloud.documentai_toolbox.wrappers.document.Document.export_hocr_str
    
    
    export_hocr_str(title: str) -> str

Exports a string hOCR version of the Document.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.export_hocr_str](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_export_hocr_str)

### google.cloud.documentai_toolbox.wrappers.document.Document.export_images
    
    
    export_images(
        output_path: str, output_file_prefix: str, output_file_extension: str
    ) -> typing.List[str]

Exports images from `Document.entities` to files.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.export_images](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_export_images)

### google.cloud.documentai_toolbox.wrappers.document.Document.form_fields_to_bigquery
    
    
    form_fields_to_bigquery(
        dataset_name: str, table_name: str, project_id: typing.Optional[str] = None
    ) -> google.cloud.bigquery.job.load.LoadJob

Adds extracted form fields to a BigQuery table.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.form_fields_to_bigquery](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_form_fields_to_bigquery)

### google.cloud.documentai_toolbox.wrappers.document.Document.form_fields_to_dict
    
    
    form_fields_to_dict() -> typing.Dict[str, typing.Union[str, typing.List[str]]]

Returns dictionary of form fields in document.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.form_fields_to_dict](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_form_fields_to_dict)

### google.cloud.documentai_toolbox.wrappers.document.Document.from_batch_process_metadata
    
    
    from_batch_process_metadata(
        metadata: google.cloud.documentai_v1.types.document_processor_service.BatchProcessMetadata,
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.document.Document]

Loads Documents from Cloud Storage, using the output from `BatchProcessMetadata`.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.from_batch_process_metadata](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_from_batch_process_metadata)

### google.cloud.documentai_toolbox.wrappers.document.Document.from_batch_process_operation
    
    
    from_batch_process_operation(
        location: str, operation_name: str, timeout: typing.Optional[float] = None
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.document.Document]

Loads Documents from Cloud Storage, using the operation name returned from `batch_process_documents()`.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.from_batch_process_operation](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_from_batch_process_operation)

### google.cloud.documentai_toolbox.wrappers.document.Document.from_document_path
    
    
    from_document_path(
        document_path: str,
    ) -> google.cloud.documentai_toolbox.wrappers.document.Document

Loads `Document` from local `document_path`.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.from_document_path](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_from_document_path)

### google.cloud.documentai_toolbox.wrappers.document.Document.from_documentai_document
    
    
    from_documentai_document(
        documentai_document: google.cloud.documentai_v1.types.document.Document,
    ) -> google.cloud.documentai_toolbox.wrappers.document.Document

Loads `Document` from local `documentai_document`.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.from_documentai_document](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_from_documentai_document)

### google.cloud.documentai_toolbox.wrappers.document.Document.from_gcs
    
    
    from_gcs(
        gcs_bucket_name: str, gcs_prefix: str, gcs_input_uri: typing.Optional[str] = None
    ) -> google.cloud.documentai_toolbox.wrappers.document.Document

Loads a Document from a Cloud Storage directory.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.from_gcs](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_from_gcs)

### google.cloud.documentai_toolbox.wrappers.document.Document.from_gcs_uri
    
    
    from_gcs_uri(
        gcs_uri: str, gcs_input_uri: typing.Optional[str] = None
    ) -> google.cloud.documentai_toolbox.wrappers.document.Document

Loads a Document from a Cloud Storage uri.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.from_gcs_uri](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_from_gcs_uri)

### google.cloud.documentai_toolbox.wrappers.document.Document.get_entity_by_type
    
    
    get_entity_by_type(
        target_type: str,
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.entity.Entity]

Returns the list of `Entities` of `target_type`.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.get_entity_by_type](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_get_entity_by_type)

### google.cloud.documentai_toolbox.wrappers.document.Document.get_form_field_by_name
    
    
    get_form_field_by_name(
        target_field: str,
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.page.FormField]

Returns the list of `FormFields` named `target_field`.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.get_form_field_by_name](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_get_form_field_by_name)

### google.cloud.documentai_toolbox.wrappers.document.Document.search_pages
    
    
    search_pages(
        target_string: typing.Optional[str] = None, pattern: typing.Optional[str] = None
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.page.Page]

Returns the list of Pages containing target_string or text matching pattern.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.search_pages](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_search_pages)

### google.cloud.documentai_toolbox.wrappers.document.Document.split_pdf
    
    
    split_pdf(pdf_path: str, output_path: str) -> typing.List[str]

Splits local PDF file into multiple PDF files based on output from a Splitter processor.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.split_pdf](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_split_pdf)

### google.cloud.documentai_toolbox.wrappers.document.Document.to_merged_documentai_document
    
    
    to_merged_documentai_document() -> (
        google.cloud.documentai_v1.types.document.Document
    )

Exports a documentai.Document from the wrapped document with shards merged.

See more: [google.cloud.documentai_toolbox.wrappers.document.Document.to_merged_documentai_document](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.Document#google_cloud_documentai_toolbox_wrappers_document_Document_to_merged_documentai_document)

### google.cloud.documentai_toolbox.wrappers.entity.Entity.crop_image
    
    
    crop_image(
        documentai_page: google.cloud.documentai_v1.types.document.Document.Page,
    ) -> typing.Optional[PIL.Image.Image]

Return image cropped from page image for detected entity.

See more: [google.cloud.documentai_toolbox.wrappers.entity.Entity.crop_image](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.entity.Entity#google_cloud_documentai_toolbox_wrappers_entity_Entity_crop_image)

### google.cloud.documentai_toolbox.wrappers.page.Page._get_elements
    
    
    _get_elements(element_type: typing.Type, attribute_name: str) -> typing.List

Helper method to create elements based on specified type.

See more: [google.cloud.documentai_toolbox.wrappers.page.Page._get_elements](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.Page#google_cloud_documentai_toolbox_wrappers_page_Page__get_elements)

### google.cloud.documentai_toolbox.wrappers.page.Table._extract_table_rows
    
    
    _extract_table_rows(
        table_rows: typing.Iterable[
            google.cloud.documentai_v1.types.document.Document.Page.Table.TableRow
        ],
    ) -> typing.List[typing.List[str]]

Returns a list of rows from table_rows.

See more: [google.cloud.documentai_toolbox.wrappers.page.Table._extract_table_rows](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.Table#google_cloud_documentai_toolbox_wrappers_page_Table__extract_table_rows)

### google.cloud.documentai_toolbox.wrappers.page.Table.to_dataframe
    
    
    to_dataframe() -> pandas.core.frame.DataFrame

Returns pd.DataFrame from documentai.table .

See more: [google.cloud.documentai_toolbox.wrappers.page.Table.to_dataframe](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page.Table#google_cloud_documentai_toolbox_wrappers_page_Table_to_dataframe)

### google.cloud.documentai_toolbox.wrappers.page._BasePageElement._get_children_of_element
    
    
    _get_children_of_element(
        potential_children: typing.List[google.cloud.documentai_toolbox.wrappers.page.T],
    ) -> typing.List[google.cloud.documentai_toolbox.wrappers.page.T]

Filters potential child elements to identify only those fully contained within this element.

See more: [google.cloud.documentai_toolbox.wrappers.page._BasePageElement._get_children_of_element](https://cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.page._BasePageElement#google_cloud_documentai_toolbox_wrappers_page__BasePageElement__get_children_of_element)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
