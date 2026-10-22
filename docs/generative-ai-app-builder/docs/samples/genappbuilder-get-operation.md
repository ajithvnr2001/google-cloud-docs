---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-get-operation/
title: Get details about a long running operation \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:46.959543+00:00
---

# Get details about a long running operation  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-get-operation/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Get details about a long running operation Stay organized with collections  Save and categorize content based on your preferences. 

Get the status and details about a long running operation (LRO).

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Monitor long-running operations](https://docs.cloud.google.com/gemini/enterprise/docs/long-running-operations)
  * [Monitor long-running operations](https://docs.cloud.google.com/generative-ai-app-builder/docs/long-running-operations)



## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import discoveryengine
    from google.longrunning import operations_pb2
    
    # TODO(developer): Uncomment these variables before running the sample.
    # Example: `projects/{project}/locations/{location}/collections/{default_collection}/dataStores/{search_engine_id}/branches/{0}/operations/{operation_id}`
    # operation_name = "YOUR_OPERATION_NAME"
    
    
    def get_operation_sample(operation_name: str) -> operations_pb2.Operation:
        # Create a client
        client = discoveryengine.DocumentServiceClient()
    
        # Make GetOperation request
        request = operations_pb2.GetOperationRequest(name=operation_name)
        operation = client.get_operation(request=request)
    
        # Print the Operation Information
        print(operation)
    
        return operation
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
