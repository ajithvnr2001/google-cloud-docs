---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-list-operations/
title: List long-running operations \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:08:02.208251+00:00
---

# List long-running operations  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-list-operations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  List long-running operations Stay organized with collections  Save and categorize content based on your preferences. 

List the long-running operations (LROs) in a Google Cloud project and location.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Managing long-running operations (LROs)](https://docs.cloud.google.com/document-ai/docs/long-running-operations)



## Code sample

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    from google.longrunning.operations_pb2 import ListOperationsRequest  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_PROCESSOR_LOCATION"  # Format is "us" or "eu"
    
    # Create filter in https://google.aip.dev/160 syntax
    # For full options, refer to:
    # https://cloud.google.com/document-ai/docs/long-running-operations#listing_long-running_operations
    # operations_filter = 'YOUR_FILTER'
    
    # Example:
    # operations_filter = "TYPE=BATCH_PROCESS_DOCUMENTS AND STATE=RUNNING"
    
    
    def list_operations_sample(
        project_id: str, location: str, operations_filter: str
    ) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        # Format: `projects/{project_id}/locations/{location}`
        name = client.[common_location_path](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_common_location_path)(project=project_id, location=location)
        request = ListOperationsRequest(
            name=f"{name}/operations",
            filter=operations_filter,
        )
    
        # Make ListOperations request
        operations = client.[list_operations](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_list_operations)(request=request)
    
        # Print the Operation Information
        print(operations)
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
