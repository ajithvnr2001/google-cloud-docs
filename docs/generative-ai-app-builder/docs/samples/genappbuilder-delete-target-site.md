---
url: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-delete-target-site/
title: Remove website from data store \u00a0|\u00a0 Agent Search \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:10:53.112340+00:00
---

# Remove website from data store  |  Agent Search  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/generative-ai-app-builder/docs/samples/genappbuilder-delete-target-site/

**Note:** Vertex AI Search is being renamed to Agent Search. We are in the process of updating content to reflect the new branding. 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Search ](https://docs.cloud.google.com/generative-ai-app-builder/docs)
  * [ Samples ](https://docs.cloud.google.com/generative-ai-app-builder/docs/samples)



#  Remove website from data store Stay organized with collections  Save and categorize content based on your preferences. 

Remove website from data store

## Code sample

### Python

For more information, see the [Agent Search Python API reference documentation](https://docs.cloud.google.com/python/docs/reference/discoveryengine/latest). 

To authenticate to Agent Search, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    #     from google.api_core.client_options import ClientOptions
    #
    #     from google.cloud import discoveryengine_v1 as discoveryengine
    #
    #     # TODO(developer): Uncomment these variables before running the sample.
    #     # project_id = "YOUR_PROJECT_ID"
    #     # location = "YOUR_LOCATION" # Values: "global"
    #     # data_store_id = "YOUR_DATA_STORE_ID"
    #     # target_site_id = "YOUR_TARGET_SITE_ID"
    #
    #     #  For more information, refer to:
    #     # https://cloud.google.com/generative-ai-app-builder/docs/locations#specify_a_multi-region_for_your_data_store
    #     client_options = (
    #         ClientOptions(api_endpoint=f"{location}-discoveryengine.googleapis.com")
    #         if location != "global"
    #         else None
    #     )
    #
    #     # Create a client
    #     client = discoveryengine.SiteSearchEngineServiceClient(
    #         client_options=client_options
    #     )
    #
    #     # The full resource name of the data store
    #     # e.g. projects/{project}/locations/{location}/collections/{collection}/dataStores/{data_store_id}/siteSearchEngine/targetSites/{target_site}
    #     name = client.target_site_path(
    #         project=project_id,
    #         location=location,
    #         data_store=data_store_id,
    #         target_site=target_site_id,
    #     )
    #
    #     # Make the request
    #     operation = client.delete_target_site(name=name)
    #
    #     print(f"Operation: {operation.operation.name}")

## What's next

To search and filter code samples for other Google Cloud products, see the [Google Cloud sample browser](https://docs.cloud.google.com/docs/samples?product=genappbuilder). 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],[],[],[]] 
