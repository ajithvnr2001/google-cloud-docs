---
url: https://docs.cloud.google.com/document-ai/docs/samples/documentai-cancel-operation/
title: Cancel a long-running operation \u00a0|\u00a0 Document AI \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:39:46.520049+00:00
---

# Cancel a long-running operation  |  Document AI  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/document-ai/docs/samples/documentai-cancel-operation/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Document AI ](https://docs.cloud.google.com/document-ai/docs)
  * [ Samples ](https://docs.cloud.google.com/document-ai/docs/samples)



#  Cancel a long-running operation Stay organized with collections  Save and categorize content based on your preferences. 

Cancels a long-running operation (LRO)

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Managing long-running operations (LROs)](https://docs.cloud.google.com/document-ai/docs/long-running-operations)



## Code sample

### Python

For more information, see the [Document AI Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/documentai/latest). 

To authenticate to Document AI, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import documentai  # type: ignore
    from google.longrunning.operations_pb2 import CancelOperationRequest  # type: ignore
    
    # TODO(developer): Uncomment these variables before running the sample.
    # location = "YOUR_PROCESSOR_LOCATION"  # Format is "us" or "eu"
    # operation_name = "YOUR_OPERATION_NAME"  # Format is "projects/{project_id}/locations/{location}/operations/{operation_id}"
    
    
    def cancel_operation_sample(location: str, operation_name: str) -> None:
        # You must set the `api_endpoint` if you use a location other than "us".
        opts = ClientOptions(api_endpoint=f"{location}-documentai.googleapis.com")
        client = documentai.[DocumentProcessorServiceClient](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html)(client_options=opts)
    
        request = CancelOperationRequest(name=operation_name)
    
        # Make CancelOperation request
        client.[cancel_operation](https://docs.cloud.google.com/python/docs/reference/documentai/latest/google.cloud.documentai_v1.services.document_processor_service.DocumentProcessorServiceClient.html#google_cloud_documentai_v1_services_document_processor_service_DocumentProcessorServiceClient_cancel_operation)(request=request)
        print(f"Operation {operation_name} cancelled")
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=documentai). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
