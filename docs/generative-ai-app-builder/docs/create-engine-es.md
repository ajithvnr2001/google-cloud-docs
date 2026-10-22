---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es/
title: Create a search app \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:35:13.364948+00:00
---

# Create a search app  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)



Send feedback 

#  Create a search app Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to create a search app.

## Create an app

### Console

To create a search app using the Google Cloud console, follow these steps:

  1. In the Google Cloud console, go to the **AI Applications** page.

[AI Applications](https://console.cloud.google.com/gen-app-builder/engines)

  2. On the **Apps** page, click add**Create app**.

  3. On the add**Create app** page, under **Site search with AI mode** , click **Create**.

  4. Decide if you want Enterprise features for this app and then click the toggle on or off. Turning on Enterprise edition features is required to get features such as website search and choosing a region for your app. Enterprise edition features incur additional cost. For more information, see [Enterprise edition features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#enterprise-features).

  5. Decide if you want generative responses with advanced LLM features for this app and then click the toggle on or off. Activating the **Generative Responses** option is required to get features such as [search summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries) or [search with follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search). For more information, see [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm).

  6. In the **Your app name** field, enter a name for your app.

  7. In the **External name of your company or organization** field, enter the common name for your company or organization. Avoid suffixes like Inc or LLC. This field helps the LLM identify the company that the app represents.

  8. Select a location for your app. Enterprise features must be turned on to pick a location. Google recommends that you use the default, **global (Global)** , unless you have a reason to restrict your data to a particular geography.

  9. Click **Continue**.

  10. To connect to a data store, on the **Data stores** page, select a data store that you previously created or create a new data store.

**Note:** If you plan to attach more than one data store to your app, review the capabilities and limitations of doing so in [About blended search](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest#blended). If you attach only one data store, you can't attach more later.

Choose one of the following options:

     * Select an existing data store: If you attach only one data store, you cannot remove it or add other data stores to the app later. Attaching multiple data stores lets you update the attached data stores later, but the app always requires at least two data stores.
     * Create a new data store and ingest data into it: 
       1. Click add**Create data store** and follow the steps in the **Create a new data store** page.
       2. Choose your new data store and click **Select**. For more information, see [Create a search data store](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).



### REST

Before you use the command line to create an app, you must have an existing data store. If you don't have a data store, create one following the steps in [Create a data store and ingest data for Agent Search](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es).

To use the [`engines.create`](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/projects.locations.collections.engines/create) method to create a search app from the command line, follow these steps:

  1. Find your data store ID. If you already have your data store ID, skip to the next step.

     1. In the Google Cloud console, go to the **AI Applications** page and in the navigation menu, click **Data Stores**.

[Go to the Data Stores page](https://console.cloud.google.com/gen-app-builder/data-stores)

     2. Click the name of your data store.

     3. On the **Data** page for your data store, get the data store ID.

  2. Create a search app and connect it to a data store. A data store can be attached to only one app and can't be removed from the app later.

**Key Term:** In Agent Search, the term _app_ can be used interchangeably with the term _engine_ in the context of APIs.
         
         curl -X POST \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json" \
         -H "X-Goog-User-Project: PROJECT_ID" \
         "https://discoveryengine.googleapis.com/v1/projects/PROJECT_ID/locations/global/collections/default_collection/engines?engineId=APP_ID" \
         -d '{
           "displayName": "APP_DISPLAY_NAME",
           "dataStoreIds": ["DATA_STORE_ID"],
           "solutionType": "SOLUTION_TYPE_SEARCH",
           "industryVertical": "GENERIC",
           "searchEngineConfig": {
              "searchTier": "SEARCH_TIER",
              "searchAddOns": ["SEARCH_ADD_ON"]
            }
         }'
         

Replace the following:

     * `PROJECT_ID`: the ID of your Google Cloud project.
     * `APP_ID`: the ID of the Agent Search app that you want to create.
     * `APP_DISPLAY_NAME`: the display name of the Agent Search app that you want to create.
     * `DATA_STORE_ID`: the ID of an existing Agent Search data store that you want to add to the Agent Search app.
     * `SEARCH_TIER`: the search tier can be `SEARCH_TIER_STANDARD` or `SEARCH_TIER_ENTERPRISE`. `SEARCH_TIER_ENTERPRISE` is required to get features such as website search and choosing a region for your app. Enterprise edition features incur additional cost. For more information, see [Enterprise edition features](https://docs.cloud.google.com/generative-ai-app-builder/docs/about-advanced-features#enterprise-features).
     * `SEARCH_ADD_ON`: if you want generative responses with advanced LLM features for this app, then specify `SEARCH_ADD_ON_LLM`. Generative responses include [search summaries](https://docs.cloud.google.com/generative-ai-app-builder/docs/get-search-summaries) and [search with follow-ups](https://docs.cloud.google.com/generative-ai-app-builder/docs/multi-turn-search).

If you don't want generative responses, then either specify `SEARCH_ADD_ON_UNSPECIFIED` as the search add-on or remove the `searchAddOns` field.

For more information, see [Generative responses](https://docs.cloud.google.com/generative-ai-app-builder/docs/advanced-llm).

**Note:** The [industry vertical](https://docs.cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/IndustryVertical) `GENERIC` is used to create custom search apps that contain structured, unstructured, website data stores, or multiple data stores (blended search).



### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from typing import List
    
    from google.api_core.client_options import ClientOptions
    from google.cloud import discoveryengine_v1 as discoveryengine
    
    # TODO(developer): Uncomment these variables before running the sample.
    # project_id = "YOUR_PROJECT_ID"
    # location = "YOUR_LOCATION" # Values: "global"
    # engine_id = "YOUR_ENGINE_ID"
    # data_store_ids = ["YOUR_DATA_STORE_ID"]
    
    
    def create_engine_sample(
        project_id: str, location: str, engine_id: str, data_store_ids: List[str]
    ) -> str:
        #  For more information, refer to:
        # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
        client_options = (
            ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
            if location != "global"
            else None
        )
    
        # Create a client
        client = discoveryengine.EngineServiceClient(client_options=client_options)
    
        # The full resource name of the collection
        # e.g. projects/{project}/locations/{location}/collections/default_collection
        parent = client.collection_path(
            project=project_id,
            location=location,
            collection="default_collection",
        )
    
        engine = discoveryengine.Engine(
            display_name="Test Engine",
            # Options: GENERIC, MEDIA, HEALTHCARE_FHIR
            industry_vertical=discoveryengine.IndustryVertical.GENERIC,
            # Options: SOLUTION_TYPE_RECOMMENDATION, SOLUTION_TYPE_SEARCH, SOLUTION_TYPE_CHAT, SOLUTION_TYPE_GENERATIVE_CHAT
            solution_type=discoveryengine.SolutionType.SOLUTION_TYPE_SEARCH,
            # For search apps only
            search_engine_config=discoveryengine.Engine.SearchEngineConfig(
                # Options: SEARCH_TIER_STANDARD, SEARCH_TIER_ENTERPRISE
                search_tier=discoveryengine.SearchTier.SEARCH_TIER_ENTERPRISE,
                # Options: SEARCH_ADD_ON_LLM, SEARCH_ADD_ON_UNSPECIFIED
                search_add_ons=[discoveryengine.SearchAddOn.SEARCH_ADD_ON_LLM],
            ),
            # For generic recommendation apps only
            # similar_documents_config=discoveryengine.Engine.SimilarDocumentsEngineConfig,
            data_store_ids=data_store_ids,
        )
    
        request = discoveryengine.CreateEngineRequest(
            parent=parent,
            engine=engine,
            engine_id=engine_id,
        )
    
        # Make the request
        operation = client.create_engine(request=request)
    
        print(f"Waiting for operation to complete: {operation.operation.name}")
        response = operation.result()
    
        # After the operation is complete,
        # get information from operation metadata
        metadata = discoveryengine.CreateEngineMetadata(operation.metadata)
    
        # Handle the response
        print(response)
        print(metadata)
    
        return operation.operation.name
    
    

### Terraform

To learn how to apply or remove a Terraform configuration, see [Basic Terraform commands](https://docs.cloud.google.com/docs/terraform/basic-commands). For more information, see the [ Terraform provider reference documentation](https://registry.terraform.io/providers/hashicorp/google/latest/docs). 

To create a search app using Terraform, see [` discovery_engine_search_engine`](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/discovery_engine_search_engine).

## What's next

  * [Get search results](https://docs.cloud.google.com/generative-ai-app-builder/docs/preview-search-results).
  * [Add the search widget to a web page](https://docs.cloud.google.com/generative-ai-app-builder/docs/add-widget).
  * Decide whether you need to [set up configurable pricing for your app](https://docs.cloud.google.com/generative-ai-app-builder/docs/enable-configurable-pricing).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
