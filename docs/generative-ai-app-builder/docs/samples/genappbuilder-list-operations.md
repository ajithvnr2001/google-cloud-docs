---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-list-operations/
title: List long running operations \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:32:41.597048+00:00
---

# List long running operations  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-list-operations/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  List long running operations Stay organized with collections  Save and categorize content based on your preferences. 

List the long running operations for a specified resource.

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Monitor long-running operations](https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations)
  * [Monitor long-running operations](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations)



## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Optional
    
    from google.cloud import discoveryengine
    from google.longrunning import operations_pb2
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_PROCESSOR_LOCATION"  # Options: "global"
    # search_engine_id = "YOUR_SEARCH_ENGINE_ID"
    
    # Create filter in https://google.aip.dev/160 syntax
    # operations_filter = "YOUR_FILTER"
    
    
    def list_operations_sample(
        project_id: str,
        location: str,
        search_engine_id: str,
        operations_filter: Optional[str] = None,
    ) -> operations_pb2.ListOperationsResponse:
        # Create a client
        client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)()
    
        # The full resource name of the search engine branch.
        name = f"projects/{project_id}/locations/{location}/collections/default_collection/dataStores/{search_engine_id}"
    
        # Make ListOperations request
        request = operations_pb2.ListOperationsRequest(
            name=name,
            filter=operations_filter,
        )
    
        # Make ListOperations request
        response = client.[list_operations](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_list_operations)(request=request)
    
        # Print the Operation Information
        for operation in response.operations:
            print(operation)
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
