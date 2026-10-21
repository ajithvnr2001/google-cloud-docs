---
url: https://docs.cloud.google.com/document-warehouse/docs/gcs-ingest-pipeline/
title: Cloud Storage Ingest pipeline \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:13.362297+00:00
---

# Cloud Storage Ingest pipeline  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/gcs-ingest-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/document-warehouse/docs/overview)



Send feedback 

#  Cloud Storage Ingest pipeline Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Verify that your data migration is completed before the discontinuation date to prevent any data loss. See [Deprecations](https://docs.cloud.google.com/document-warehouse/docs/deprecations) for details.

This document describes what the Cloud Storage ingest pipeline does and how to run the pipeline.

## What does the Cloud Storage ingest pipeline do?

Your users can transfer documents from Cloud Storage to the Document AI Warehouse. There, users can opt to have them processed for tasks such as searching, document management workflows, or simply testing out Document AI outputs.

## Why use this pipeline?

If many documents must be ingested (with or without processing), this pipeline provides a reliable workflow. It also helps users accelerate time to onboard Document AI Warehouse customers for proofs of concept or production workloads.

## Pipeline features

In general, the Cloud Storage ingest pipeline supports the following actions:

  * Ingest raw documents into Document AI Warehouse.
        
        {
          name: "projects/PROJECT_NUMBER/locations/LOCATION_ID",
          gcs_ingest_pipeline: {
            input_path: "gs://BUCKET_NAME/FOLDER_NAME",
            schema_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID"
          }
        }
        

  * Ingest Document AI processed documents into Document AI Warehouse.
        
        {
          name: "projects/PROJECT_NUMBER/locations/LOCATION_ID",
          gcs_ingest_pipeline: {
            input_path: "gs://BUCKET_NAME/FOLDER_NAME",
            schema_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID",
            processor_type: "PROCESS_TYPE"
          }
        }
        

The `processor_type` is required to indicate that the input files have been processed by Document AI. `processor_type` (`OCR_PROCESSOR`, `INVOICE_PROCESSOR`, `FORM_PARSER_PROCESSOR`) can be found under the **Type in API** field [here](https://cloud.google.com/document-ai/docs/processors-list).

  * Ingest Document AI processed documents and corresponding raw documents in the same request.
        
        {
          name: "projects/PROJECT_NUMBER/locations/LOCATION_ID",
          gcs_ingest_pipeline: {
            input_path: "gs://BUCKET_NAME/FOLDER_NAME",
            schema_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID",
            processor_type: "PROCESS_TYPE"
          }
        }
        

The `input_path` location must contain Document AI processed documents. The pipeline finds corresponding raw documents for each Doc AI processed document under that URI path.

  * Ingest one type of raw document and trigger Document AI processing in the pipeline.
        
        {
          name: "projects/PROJECT_NUMBER/locations/LOCATION_ID",
          gcs_ingest_with_doc_ai_processors_pipeline: {
            input_path: "gs://BUCKET_NAME/FOLDER_NAME",
            extract_processor_infos: {
              processor_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/processors/PROCESSOR_ID",
              schema_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID"
            },
            processor_results_folder_path: "gs://OUTPUT_BUCKET_NAME/OUTPUT_BUCKET_FOLDER_NAME"
          }
        }
        

The `extract_processor_infos` field must contain only one extract processor. All documents under the `input_path` field are regarded as one document type and processed by the same extract processor.

  * Ingest multiple types of raw documents and trigger Document AI processing in the pipeline.
        
        {
          name: "projects/PROJECT_NUMBER/locations/LOCATION_ID",
          gcs_ingest_with_doc_ai_processors_pipeline: {
            input_path: "gs://BUCKET_NAME/FOLDER_NAME",
            split_classify_processor_info: {
              processor_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/processors/PROCESSOR_ID"
            },
            extract_processor_infos: [
              {
                processor_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/processors/PROCESSOR_ID",
                document_type: "DOCUMENT_TYPE",
                schema_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID"
              }
            ],
            processor_results_folder_path: "gs://OUTPUT_BUCKET_NAME/OUTPUT_BUCKET_FOLDER_NAME"
          }
        }
        

The `split_classify_processor_info` field classifies documents by type. The `extract_processor_infos` field (passed as an array) must contain different extract processors corresponding to each document type from the classification result.




### Ingest configuration

The Cloud Storage ingest pipeline supports optional customizations during document ingestion, as described by the following options:

  * Use the `skip_ingested_documents` flag to skip ingested documents when the pipeline is triggered on the same Cloud Storage folder more than once. If documents in Cloud Storage contain the `status=ingested` metadata, which is a status tracking feature of the pipeline, the documents aren't re-ingested if this flag is enabled.

  * Use the `document_acl_policy` flag to provide an additional document-level ACL policy during documents creation. This flag is for projects that have document-level ACLs enabled in Document AI Warehouse.

  * Use the `enable_document_text_extraction` flag to have Document AI Warehouse extract text on raw documents if the documents contain content. This flag is different from Document AI processing and document extraction supports only the following document file types in Document AI Warehouse.

    * `RAW_DOCUMENT_FILE_TYPE_TEXT`
    * `RAW_DOCUMENT_FILE_TYPE_DOCX`
  * Use the `folder` field to specify the target folder for the ingested documents. All ingested documents will be linked under the given parent folder.

  * Use the `cloud_function` field to further customize fields in the document proto file before it goes to Document AI Warehouse. The `cloud_function` value must be a valid URL accessible to the Document AI Warehouse service account. Each call must end within 5 minutes. Requests and responses are in JSON format. You might find these keys in the request payload:

    * `display_name`
    * `properties`
    * `plain_text` or `cloud_ai_document.text`
    * `reference_id`
    * `document_schema_name`
    * `raw_document_path`
    * `raw_document_file_type`

The keys from the response payload are ingested in Document AI Warehouse as part of the proto. The original value is overwritten if a key is modified or added to the response. Extra keys in the response are discarded. If the corresponding value is invalid, document ingestion fails.

    * `display_name`
    * `properties`
    * `plain_text` or `cloud_ai_document.text`
    * `reference_id`
    * `document_acl_policy`
    * `folder`
  * Ingest pipeline customization using `pipeline_config`.
        
        {
          name: "projects/PROJECT_NUMBER/locations/LOCATION_ID",
          gcs_ingest_pipeline: {
            input_path: "gs://BUCKET_NAME/FOLDER_NAME",
            schema_name: "projects/PROJECT_NUMBER/locations/LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID",
            skip_ingested_documents: "true",
            pipeline_config: {
              enable_document_text_extraction: "true"
              folder: "projects/PROJECT_NUMBER/locations/LOCATION_ID/documents/FOLDER_DOCUMENT_ID",
              cloud_function: "https://REGION-PROJECT_ID.cloudfunctions.net/CLOUD_FUNCTION_NAME"
            }
          }
        }
        




### Status tracking

Status tracking shows the progress of ingestion results on the whole pipeline and each document.

  * You can check if the pipeline is complete by checking if the LRO is done.

  * You can check the status of each document in the pipeline by viewing the [Cloud Storage metadata](https://cloud.google.com/storage/docs/metadata). Cloud Storage creates the following key-value pairs on each document.

    * Key: `status`; Value: `status=queued` or `status=processed` or `status=ingested` or `status=failed`.
    * Key: `error`; Value: `the error message`.



### Supported document types

**Note:** Document AI Warehouse supports ingestion of Microsoft Office file types. However, processing through Document AI is not possible as of now.

The supported document types in the pipeline are the same as the Document AI Warehouse supported document types: Text, PDFs, Images (scanned PDFs, TIFF files, JPEG files), Microsoft Office file (DOCX, PPTX, XSLX).

### Document properties from Cloud Storage metadata

You can use the Cloud Storage metadata in the pipeline to create customized properties in Document AI Warehouse. A metadata value of the Cloud Storage document will be automatically copied to the corresponding Document AI Warehouse document property if its key matches a property name in the schema.

**Note:** Keys related to status tracking (for example `status`, `error`) are reserved and not allowed to be used.

## Run the pipeline

The different parameters are required to trigger different functionalities in Cloud Storage ingest pipeline. Refer to [Method: projects.locations.runPipeline](https://cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations/runPipeline) for more information.

The following part provides two examples to trigger the Cloud Storage ingest pipeline.

  * Run the Cloud Storage ingest pipeline without Document AI processors.

### REST
        
        curl --location --request POST 'https://contentwarehouse.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID:runPipeline' \
        --header 'Content-Type: application/json' \
        --header "Authorization: Bearer ${AUTH_TOKEN}" \
        --data '{
                "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID",
                "gcs_ingest_pipeline": {
                    "input_path": "gs://BUCKET_NAME/FOLDER_NAME/",
        "schema_name": "projects/PROJECT_NUMBER/locations/
        LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID",
                    "skip_ingested_documents": "true"
                },
                "request_metadata": {
                    "user_info": {
                        "id": "user:USER EMAIL ADDRESS"
                    }
                }
        }'

  * Run Cloud Storage Ingest Pipeline with Document AI processors.

**Note:** The Cloud Storage Ingest Pipeline with Document AI processors can only process documents up to 200 pages.

### REST
        
        curl --location --request POST 'https://contentwarehouse.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION_ID:runPipeline' \
        --header 'Content-Type: application/json' \
        --header "Authorization: Bearer ${AUTH_TOKEN}" \
        --data '{
                "name": "projects/PROJECT_NUMBER/locations/LOCATION_ID",
                "gcs_ingest_with_doc_ai_processors_pipeline": {
                    "input_path": "gs://BUCKET_NAME/FOLDER_NAME/",
                    "split_classify_processor_info": {
                      "processor_name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/processors/PROCESSOR_ID"
                    },
                    "extract_processor_infos": [
                      {
                        "processor_name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/processors/PROCESSOR_ID",
                        "document_type": "DOCUMENT_TYPE",
                        "schema_name": "projects/PROJECT_NUMBER/locations/LOCATION_ID/documentSchemas/DOCUMENT_SCHEMA_ID"
                      }
                    ],
                    "processor_results_folder_path": "gs://OUTPUT_BUCKET_NAME/OUTPUT_BUCKET_FOLDER_NAME/"
                    "skip_ingested_documents": "true"
                },
                "request_metadata": {
                    "user_info": {
                        "id": "user:USER EMAIL ADDRESS"
                    }
                }
        }'




This command returns a resource name for a long-running operation. With this resource name, you can track the progress of the pipeline by following the next step.

## Get Long-running operation result

### REST
    
    
    curl --location --request GET 'https://contentwarehouse.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION' \
    --header "Authorization: Bearer ${AUTH_TOKEN}"

## Next steps

To check ingested documents, go to Document AI Warehouse's [web application](https://documentwarehouse.cloud.google.com/).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
