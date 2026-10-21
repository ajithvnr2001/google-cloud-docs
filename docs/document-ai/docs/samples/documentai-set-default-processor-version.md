---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-set-default-processor-version/
title: Change the default processor version \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:38:46.413314+00:00
---

# Change the default processor version  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-set-default-processor-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Change the default processor version Stay organized with collections  Save and categorize content based on your preferences. 

A processor's default version specifies the version that is used to process documents when you don't specify a specific version. When you create a processor, the initial default version is the latest version in the stable channel. If you change the default version, incoming requests are processed using the newly selected version. If you change the default version while the processor is in the middle of a request, the request will continue to use the previously selected version.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Managing processor versions](https://docs.cloud.google.com/document-ai/docs/manage-processor-versions)



## Code sample

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.api_core.exceptions import NotFound
    from google.cloud import documentai  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = 'YOUR_PROJECT_ID'
    # location = 'YOUR_PROCESSOR_LOCATION' # Format is 'us' or 'eu'
    # processor_id = 'YOUR_PROCESSOR_ID' # Create processor before running sample
    # processor_version_id = 'YOUR_PROCESSOR_VERSION_ID'
    
    
    def set_default_processor_version_sample(
        project_id: str, location: str, processor_id: str, processor_version_id: str
    ) -> None:
        # You must set the api_endpoint if you use a location other than 'us'.
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
    
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # The full resource name of the processor
        # e.g.: projects/project_id/locations/location/processors/processor_id
        processor = client.[processor_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_path)(project_id, location, processor_id)
    
        # The full resource name of the processor version
        # e.g.: projects/project_id/locations/location/processors/processor_id/processorVersions/processor_version_id
        processor_version = client.[processor_version_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_processor_version_path)(
            project_id, location, processor_id, processor_version_id
        )
    
        request = documentai.[SetDefaultProcessorVersionRequest](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.types.SetDefaultProcessorVersionRequest.html)(
            processor=processor, default_processor_version=processor_version
        )
    
        # Make SetDefaultProcessorVersion request
        try:
            operation = client.[set_default_processor_version](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_set_default_processor_version)(request)
            # Print operation details
            print(operation.operation.name)
            # Wait for operation to complete
            operation.result()
        except NotFound as e:
            print(e.message)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
