---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-evaluate-processor-version/
title: Evaluate a processor version \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:23:18.154710+00:00
---

# Evaluate a processor version  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-evaluate-processor-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Evaluate a processor version Stay organized with collections  Save and categorize content based on your preferences. 

Evaluate a processor version with a supplied dataset.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Evaluate performance](https://docs.cloud.google.com/document-ai/docs/evaluate)



## Code sample

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID'
    # processor_version_id = 'YOUR_PROCESSOR_VERSION_ID'
    # gcs_input_uri = # Format: gs://bucket/directory/
    
    
    def evaluate_processor_version_sample(
        project_id: str,
        location: str,
        processor_id: str,
        processor_version_id: str,
        gcs_input_uri: str,
    ) -> None:
        # You must set the api_endpoint if you use a location other than 'us', e.g.:
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the processor version
        # e.g. `projects/{project_id}/locations/{location}/processors/{processor_id}/processorVersions/{processor_version_id}`
        name = client.[processor_version_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_version_path)(
            project_id, location, processor_id, processor_version_id
        )
    
        evaluation_documents = documentai.[BatchDocumentsInputConfig](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.BatchDocumentsInputConfig.html)(
            gcs_prefix=documentai.[GcsPrefix](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.GcsPrefix.html)(gcs_uri_prefix=gcs_input_uri)
        )
    
        # NOTE: Alternatively, specify a list of GCS Documents
        #
        # gcs_input_uri = "gs://bucket/directory/file.pdf"
        # input_mime_type = "application/pdf"
        #
        # gcs_document = documentai.GcsDocument(
        #     gcs_uri=gcs_input_uri, mime_type=input_mime_type
        # )
        # gcs_documents = [gcs_document]
        # evaluation_documents = documentai.BatchDocumentsInputConfig(
        #     gcs_documents=documentai.GcsDocuments(documents=gcs_documents)
        # )
        #
    
        request = documentai.[EvaluateProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.EvaluateProcessorVersionRequest.html)(
            processor_version=name,
            evaluation_documents=evaluation_documents,
        )
    
        # Make EvaluateProcessorVersion request
        # Continually polls the operation until it is complete.
        # This could take some time for larger files
        operation = client.[evaluate_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_evaluate_processor_version)(request=request)
        # Print operation details
        # Format: projects/PROJECT_NUMBER/locations/LOCATION/operations/OPERATION_ID
        print(f"Waiting for operation {operation.operation.name} to complete...")
        # Wait for operation to complete
        response = documentai.[EvaluateProcessorVersionResponse](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.EvaluateProcessorVersionResponse.html)(operation.result())
    
        # After the operation is complete,
        # Print evaluation ID from operation response
        print(f"Evaluation Complete: {response.evaluation}")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
