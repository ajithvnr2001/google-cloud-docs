---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-import-documents-spanner/
title: Import documents from Spanner \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:30.813686+00:00
---

# Import documents from Spanner  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-import-documents-spanner/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Import documents from Spanner Stay organized with collections  Save and categorize content based on your preferences. 

Import documents from Spanner

## Explore further

For detailed documentation that includes this code sample, see the following: 

  * [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es)



## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # data_store_id = "YOUR_DATA_STORE_ID"
    # spanner_project_id = "YOUR_SPANNER_PROJECT_ID"
    # spanner_instance_id = "YOUR_SPANNER_INSTANCE_ID"
    # spanner_database_id = "YOUR_SPANNER_DATABASE_ID"
    # spanner_table_id = "YOUR_SPANNER_TABLE_ID"
    
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
    
    request = discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html)(
        parent=parent,
        spanner_source=discoveryengine.[SpannerSource](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.SpannerSource.html)(
            project_id=spanner_project_id,
            instance_id=spanner_instance_id,
            database_id=spanner_database_id,
            table_id=spanner_table_id,
        ),
        # Options: `FULL`, `INCREMENTAL`
        reconciliation_mode=discoveryengine.[ImportDocumentsRequest](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.html).[ReconciliationMode](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsRequest.ReconciliationMode.html).INCREMENTAL,
    )
    
    # Make the request
    operation = client.[import_documents](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.services.document_service.DocumentServiceClient.html#google_cloud_discoveryengine_v1_services_document_service_DocumentServiceClient_import_documents)(request=request)
    
    print(f"Waiting for operation to complete: {operation.operation.name}")
    response = operation.result()
    
    # After the operation is complete,
    # get information from operation metadata
    metadata = discoveryengine.[ImportDocumentsMetadata](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest/google.cloud.discoveryengine_v1.types.ImportDocumentsMetadata.html)(operation.metadata)
    
    # Handle the response
    print(response)
    print(metadata)

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
