---
url: https://docs.cloud.google.com/document-warehouse/docs/process-with-docai-pipeline/
title: Process-with-Document-AI pipeline \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:13.481336+00:00
---

# Process-with-Document-AI pipeline  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/process-with-docai-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/document-warehouse/docs/overview)



Send feedback 

#  Process-with-Document-AI pipeline Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Verify that your data migration is completed before the discontinuation date to prevent any data loss. See [Deprecations](https://docs.cloud.google.com/document-warehouse/docs/deprecations) for details.

The Process-with-Document AI pipeline allows users to process existing documents with a Document AI processor and update the document properties with the newly extracted entities.

## Prerequisites

Before you begin, you need the following:

  1. A Document AI processor ready under the same Google Cloud project.

     * If you don't have a processor, follow the steps to [create one](https://docs.cloud.google.com/document-ai/docs/create-processor). You can choose to create any type as long as the processor type matches the document type.
  2. Dedicated Cloud Storage folders for storing exported documents and processed documents.

     * Make sure the folders are empty before you start the pipeline.
  3. A schema with mappings between Document AI entities and Document AI Warehouse properties.

     * The newly extracted entities might not be correctly converted to Document AI Warehouse entities without such a mapping.

     * To add mappings to the schema, follow [set schemas with mapping](https://docs.cloud.google.com/document-warehouse/docs/set-schema-with-mapping).


**Note:** The Process-with-Document AI pipeline can only process documents up to 200 pages.

## Run the pipeline

### REST
    
    
    curl --location --request POST 'https://contentwarehouse.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION:runPipeline' \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer ${AUTH_TOKEN}" \
    --data '{
        "name": "projects/PROJECT_NUMBER/locations/LOCATION",
        "process_with_doc_ai_pipeline": {
            "documents": [
              "projects/PROJECT_NUMBER/locations/LOCATION/documents/DOCUMENT"
            ],
            "export_folder_path": "gs://EXPORT_FOLDER",
            "processor_info": {
              "processor_name": "projects/PROJECT_NUMBER/locations/LOCATION/processors/PROCESSOR"
            },
            "processor_results_folder_path": "gs://PROCESS_FOLDER"
        },
        "request_metadata": {
            "user_info": {
                "id": "user:USER EMAIL ADDRESS"
            }
        }
    }'

The `documents` list is the resource names of the documents to be processed. The Cloud Storage folder path `export_folder_path` is used to store the exported documents before being sent to the processor. For more information about the request body fields, refer to the [API documentation](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations/runPipeline#processwithdocaipipeline).

This command returns a resource name for a long-running operation. With this resource name, you can track the progress of the pipeline by following the next step.

## Get long-running operation result

### REST
    
    
    curl --location --request GET 'https://contentwarehouse.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION' \
    --header "Authorization: Bearer ${AUTH_TOKEN}"

## Next steps

Go to [Document AI Warehouse UI](https://documentwarehouse.cloud.google.com/) or call the [document:get](https://docs.cloud.google.com/document-warehouse/docs/reference/rest/v1/projects.locations.documents/get) API to check if documents are successfully updated.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
