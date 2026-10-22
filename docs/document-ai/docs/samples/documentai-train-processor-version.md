---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-train-processor-version/
title: Train a processor version \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:10.237672+00:00
---

# Train a processor version  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-train-processor-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Train a processor version Stay organized with collections  Save and categorize content based on your preferences. 

Start a new training job for a processor

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Train and evaluate](https://docs.cloud.google.com/document-ai/docs/training-overview)



## Code sample

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Optional
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID'
    # processor_version_display_name = 'new-processor-version'
    # train_data_uri = 'gs://bucket/directory/' # (Optional)
    # test_data_uri = 'gs://bucket/directory/' # (Optional)
    
    
    def train_processor_version_sample(
        project_id: str,
        location: str,
        processor_id: str,
        processor_version_display_name: str,
        train_data_uri: Optional[str] = None,
        test_data_uri: Optional[str] = None,
    ) -> None:
        # You must set the api_endpoint if you use a location other than 'us', e.g.:
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the processor
        # e.g. `projects/{project_id}/locations/{location}/processors/{processor_id}
        parent = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
        processor_version = documentai.[ProcessorVersion](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessorVersion.html)(
            display_name=processor_version_display_name
        )
    
        # If train/test data is not supplied, the default sets in the Cloud Console will be used
        input_data = documentai.[TrainProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.TrainProcessorVersionRequest.html).[InputData](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.TrainProcessorVersionRequest.InputData.html)(
            training_documents=documentai.[BatchDocumentsInputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchDocumentsInputConfig.html)(
                gcs_prefix=documentai.[GcsPrefix](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.GcsPrefix.html)(gcs_uri_prefix=train_data_uri)
            ),
            test_documents=documentai.[BatchDocumentsInputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchDocumentsInputConfig.html)(
                gcs_prefix=documentai.[GcsPrefix](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.GcsPrefix.html)(gcs_uri_prefix=test_data_uri)
            ),
        )
    
        request = documentai.[TrainProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.TrainProcessorVersionRequest.html)(
            parent=parent, processor_version=processor_version, input_data=input_data
        )
    
        operation = client.[train_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_train_processor_version)(request=request)
        # Print operation details
        print(operation.operation.name)
        # Wait for operation to complete
        response = documentai.[TrainProcessorVersionResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.TrainProcessorVersionResponse.html)(operation.result())
    
        metadata = documentai.[TrainProcessorVersionMetadata](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.TrainProcessorVersionMetadata.html)(operation.metadata)
    
        print(f"New Processor Version:{response.processor_version}")
        print(f"Training Set Validation: {metadata.training_dataset_validation}")
        print(f"Test Set Validation: {metadata.test_dataset_validation}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
