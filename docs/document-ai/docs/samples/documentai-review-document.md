---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-review-document/
title: Request Human Review of a document \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:07:14.031060+00:00
---

# Request Human Review of a document  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-review-document/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Request Human Review of a document Stay organized with collections  Save and categorize content based on your preferences. 

Sends a request for ad-hoc human review of a processed document.

## Code sample

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID' # Create processor before running sample
    # file_path = '/path/to/local/pdf'
    # mime_type = 'application/pdf'  # https://cloud.google.com/document-ai/docs/file-types
    
    
    def review_document_sample(
        project_id: str, location: str, processor_id: str, file_path: str, mime_type: str
    ) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        # Create a client
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # Make Processing Request
        inline_document = process_document(
            project_id, location, processor_id, file_path, mime_type
        )
    
        # Get the full resource name of the human review config, e.g.:
        # projects/project_id/locations/location/processor/processor_id/humanReviewConfig
        human_review_config = client.[human_review_config_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_human_review_config_path)(
            project_id, location, processor_id
        )
    
        # Options are DEFAULT, URGENT
        priority = documentai.[ReviewDocumentRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ReviewDocumentRequest.html).[Priority](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ReviewDocumentRequest.Priority.html).DEFAULT
    
        # Configure the human review request
        request = documentai.[ReviewDocumentRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ReviewDocumentRequest.html)(
            inline_document=inline_document,
            human_review_config=human_review_config,
            enable_schema_validation=False,
            priority=priority,
        )
    
        # Make a request for human review of the processed document
        operation = client.[review_document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_review_document)(request=request)
    
        # Print operation name, can be used to check status of the request
        print(operation.operation.name)
    
    
    def process_document(
        project_id: str, location: str, processor_id: str, file_path: str, mime_type: str
    ) -> documentai.Document:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the processor, e.g.:
        # projects/project_id/locations/location/processor/processor_id
        name = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
        # Read the file into memory
        with open(file_path, "rb") as image:
            image_content = image.read()
    
        # Load Binary Data into Document AI RawDocument Object
        raw_document = documentai.[RawDocument](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.RawDocument.html)(content=image_content, mime_type=mime_type)
    
        # Configure the process request
        request = documentai.[ProcessRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.ProcessRequest.html)(name=name, raw_document=raw_document)
    
        result = client.[process_document](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_process_document)(request=request)
    
        return result.[document](https://docs.cloud.google.com/python/docs/reference/documentai-toolbox/latest/google.cloud.documentai_toolbox.wrappers.document.html)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
