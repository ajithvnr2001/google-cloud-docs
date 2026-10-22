---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-list-documents/
title: List documents in a data store \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:54.366675+00:00
---

# List documents in a data store  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-list-documents/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  List documents in a data store Stay organized with collections  Save and categorize content based on your preferences. 

List all documents in a data store.

## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import Any
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION"            # Values: "global", "us", "eu"
    # data_store_id = "YOUR_DATA_STORE_ID"
    
    
    def list_documents_sample(project_id: str, location: str, data_store_id: str) -> Any:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.[DocumentServiceClient](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html)(client_options=client_options)
    
        # The full resource name of the search engine branch.
        # e.g. projects/{project}/locations/{location}/dataStores/{data_store_id}/branches/{branch}
        parent = client.[branch_path](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_branch_path)(
            project=project_id,
            location=location,
            data_store=data_store_id,
            branch="default_branch",
        )
    
        response = client.[list_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_list_documents)(parent=parent)
    
        print(f"Documents in {data_store_id}:")
        for result in response:
            print(result)
    
        return response
    
    

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
