---
url: https://docs.cloud.google.com/document-warehouse/docs/export-to-cdw-pipeline/
title: Export-to-Workbench pipeline \u00a0|\u00a0 Document AI Warehouse \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:41:13.438731+00:00
---

# Export-to-Workbench pipeline  |  Document AI Warehouse  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-warehouse/docs/export-to-cdw-pipeline/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI Warehouse ](https://docs.cloud.google.com/document-warehouse/docs)
  * [ Guides ](https://docs.cloud.google.com/document-warehouse/docs/overview)



Send feedback 

#  Export-to-Workbench pipeline Stay organized with collections  Save and categorize content based on your preferences. 

**Caution** : Document AI Warehouse is deprecated and will no longer be available on Google Cloud after January 16, 2025. To safeguard your data, migrate any documents currently saved in Document AI Warehouse to an alternative like Cloud Storage. Verify that your data migration is completed before the discontinuation date to prevent any data loss. See [Deprecations](https://docs.cloud.google.com/document-warehouse/docs/deprecations) for details.

You can transfer documents from the Document AI Warehouse to the Document AI Workbench using the export-to-Workbench pipeline. The pipeline exports the documents to a Cloud Storage folder, then imports them to a Document AI dataset. You provide the Cloud Storage folder and the Document AI dataset.

## Prerequisites

Before you begin, you need the following:

  * Under the same Google Cloud project, follow the steps to [create a processor](https://cloud.google.com/document-ai/docs/workbench/build-custom-processor#create_a_processor) .
  * Dedicate an empty Cloud Storage folder for storing exported documents.

  * On the custom processor page, click **Configure Your Dataset** and then **Continue** to initialize the dataset.




## Run the pipeline

### REST
    
    
    curl --location --request POST 'https://contentwarehouse.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION:runPipeline' \
    --header 'Content-Type: application/json' \
    --header "Authorization: Bearer ${AUTH_TOKEN}" \
    --data '{
        "name": "projects/PROJECT_NUMBER/locations/LOCATION",
        "export_cdw_pipeline": {
            "documents": [
                "projects/PROJECT_NUMBER/locations/LOCATION/documents/DOCUMENT",
            ],
            "export_folder_path": "gs://CLOUD STORAGE FOLDER",
            "doc_ai_dataset": "projects/PROJECT_NUMBER/locations/LOCATION/processors/PROCESSOR/dataset",
            "training_split_ratio": RATIO,
        },
        "request_metadata": {
            "user_info": {
                "id": "user:USER EMAIL ADDRESS",
            }
        }
    }'

The training and test split ratio can be specified in the `training_split_ratio` field as a floating-point number. For example, for a set of 10 documents, if the ratio is specified as `0.8`, 8 documents will be added to the training set and the remaining 2 documents to the test set. 

This command returns a resource name for a long-running operation. Use it to track the progress of the pipeline in the next step.

## Get long-running operation result

### REST
    
    
    curl --location --request GET 'https://contentwarehouse.googleapis.com/v1/projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION' \
    --header "Authorization: Bearer ${AUTH_TOKEN}"

## Next step

  * Go to your [Document AI](https://console.cloud.google.com/ai/document-ai) to check exported documents.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
