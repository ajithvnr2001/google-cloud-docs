---
url: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools_data_store/
title: Set up OpenAPI tools to access Datastore \u00a0|\u00a0 Agent Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:13:02.669992+00:00
---

# Set up OpenAPI tools to access Datastore  |  Agent Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools_data_store/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ Agent Assist ](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist)



Send feedback 

#  Set up OpenAPI tools to access Datastore Stay organized with collections  Save and categorize content based on your preferences. 

OpenAPI tools enable AI coach to dynamically retrieve data from remote APIs based on the conversation context. 

## Before you begin

If you have difficulties with pre-existing APIs, use the following flexible approach:

  1. Create [Cloud Run functions](https://cloud.google.com/functions) as a wrapper of the pre-existing API. The Cloud Run functions fills in additional required parameters and performs postprocessing of API responses.
  2. Create an OpenAPI tool to call your Cloud Run functions.



While Datastore API might require additional input parameters, such as setting the search result mode, a Cloud Run functions requires only one parameter (query), which AI coach can extract from the conversation context. In terms of response processing, the Cloud Run functions only returns the top hit instead of all results.

Follow these steps to access Datastore.

## Step 1: Create Datastore and search app

  1. Follow the steps in [Datastore](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-data-store-es) to create Datastore.
  2. Follow the steps to [Create a search app](https://docs.cloud.google.com/generative-ai-app-builder/docs/create-engine-es).
  3. Check Datastore and search app using API to verify its solution type, search tier, and if chunking is enabled.



Run the following command to retrieve the chunking.
    
    
    gcurl -sX GET \
    "https://discoveryengine.googleapis.com/v1alpha/projects/${project_id}/locations/global/collections/default_collection/dataStores/${data_store_id}/documentProcessingConfig"
    

The following example shows that chunking is enabled.
    
    
    {
      "name": "projects/${project_id}/locations/global/collections/default_collection/dataStores/${data_store_id}/documentProcessingConfig",
      "chunkingConfig": {
        "layoutBasedChunkingConfig": {
          "chunkSize": 500,
          "includeAncestorHeadings": true
        }
      },
      "defaultParsingConfig": {
        "digitalParsingConfig": {}
      }
    }
    

Run the following command to retrieve the solution type and search tier.
    
    
    gcurl -X GET \
    "https://discoveryengine.googleapis.com/v1alpha/projects/${project_id}/locations/global/collections/default_collection/engines/${data_store_id}"
    

The following example shows that solution type and search tier are verified.
    
    
    {
      "name": "projects/${project_id}/locations/global/collections/default_collection/engines/${data_store_id}",
      "displayName": "iphone_",
      "dataStoreIds": [
        "${data_store_id}"
      ],
      "solutionType": "SOLUTION_TYPE_SEARCH",
      "searchEngineConfig": {
        "searchTier": "SEARCH_TIER_ENTERPRISE"
      },
      "commonConfig": {
        "companyName": "Google"
      },
      "industryVertical": "GENERIC"
    }
    

## Step 2: Create Cloud Run functions to call the Datastore

To authenticate, configure your Cloud Run functions to require an identity token. Cloud Run functions help to wrap complex API into basic API. They perform the following actions:

  1. Fills in additional fields in the request.
  2. Calls the Datastore API to perform the search.
  3. Processes the API response and returns the top results.



After you create Cloud Run functions, create an OpenAPI tool to invoke your Cloud Run functions.

In the following example, the Cloud Run functions convert the Datastore API to perform searches and give you a list of search results.
    
    
    import os
    import requests
    import google.auth
    import google.auth.transport.requests
    import functions_framework
    
    @functions_framework.http
    def call_vertex_search(request):
      """
      HTTP Cloud Function to invoke a Vertex AI Search endpoint.
      """
    
      # --- Configuration - Tailor to your Vertex AI Search specifics ---
      project_id = ${project_id}
      engine_id = "${data_store_id}"
    
      # Establish the Vertex AI Search endpoint URL
      endpoint = f"https://discoveryengine.googleapis.com/v1alpha/projects/${project_id}/locations/global/collections/default_collection/engines/{engine_id}/servingConfigs/default_chat:search"
    
      # --- Acquire Authentication Token ---
      try:
        credentials, project = google.auth.default()
        auth_req = google.auth.transport.requests.Request()
        credentials.refresh(auth_req)
        token = credentials.token
      except Exception as e:
        print(f"Authentication token retrieval error: {e}")
        return f"Authentication token retrieval error: {e}", 500
    
      headers = {
          "Authorization": f"Bearer {token}",
          "Content-Type": "application/json",
      }
    
      # --- Formulate Search Query ---
      # Extract the query from the request; otherwise, employ a default.
      request_json = request.get_json(silent=True)
      query = "what is the price of iphone 13?"  # Default query
      if request_json and 'query' in request_json:
        query = request_json['query']
    
      payload = {
          "query": query,
          "page_size": 5,
          "content_search_spec": {
              "search_result_mode": "CHUNKS"
          }
          # Additional search parameters, such as filters or boost_spec, can be appended here.
          # "filter": "some_attribute:ANY(\"value\")",
      }
    
      # --- Execute Vertex AI Search API Call ---
      try:
        response = requests.post(endpoint, headers=headers, json=payload)
        response.raise_for_status()  # Trigger an exception for unfavorable status codes.
    
        search_results = response.json()
        print(f"Search results: {search_results}")
    
        extracted_data = search_results["results"][0]["chunk"]["content"]
    
        if extracted_data is not None:
          print(f"Extracted data: {extracted_data}")
          return {"content": extracted_data}, 200
        else:
          print("Failed to extract search results from the response.")
          return "Failed to extract search results from the response", 404
    
      except requests.exceptions.RequestException as e:
        print(f"Vertex AI Search invocation error: {e}")
        if e.response is not None:
          print(f"Error details: {e.response.text}")
          return f"Vertex AI Search invocation error: {e.response.text}", e.response.status_code
        return f"Vertex AI Search invocation error: {e}", 500
      except Exception as e:
        print(f"An unanticipated error transpired: {e}")
        return f"An unanticipated error transpired: {e}", 500
    

Use Shell to test the Cloud Run functions. Try sending a query like _what is the price of iphone 13_ , as shown in the following example.
    
    
    export CLOUDSDK_CORE_PROJECT=${project_id}
    curl -H "Authorization: Bearer "$(gcloud auth print-identity-token) -H "X-Goog-User-Project: ${CLOUDSDK_CORE_PROJECT}" -H "Content-Type: application/json; charset=utf-8" -X GET "https://${CLOUD_FUNCTION_ENDPOINT}/?query=what%20is%20the%20price%20of%20iphone%2013"
    

You should receive a response like the following:
    
    
    {"content":"Table of contents\niPhone price history iPhone 4S (2011)\niPhone 4S original starting MSRP: $199\nInflation-adjusted iPhone 4S price: $280\niPhone 5 (2012)\niPhone 5 Original starting MSRP: $199\nInflation-adjusted iPhone 5 price: $276\niPhone 5S/5C (2013) iPhone 5S original starting MSRP: $199\niPhone 5C original starting MSRP: $99\nInflation-adjusted iPhone 5S price: $270\nInflation-adjusted iPhone 5C price: $134\niPhone 6/6 Plus (2014) Table of contents\niPhone price history iPhone 6 original starting MSRP: $199\niPhone 6 Plus original starting MSRP: $299\nInflation-adjusted iPhone 6 price: $266\nInflation-adjusted iPhone 6 Plus price: $398\niPhone 6S/6S Plus (2015)\niPhone 6S original starting MSRP: $199\niPhone 6S Plus original starting MSRP: $299\nInflation-adjusted iPhone 6S price: $265\nInflation-adjusted iPhone 6S Plus price: $397\niPhone 7/7 Plus (2016) Table of contents\niPhone price history iPhone 7 original starting MSRP: $649\niPhone 7 Plus original starting MSRP: $769\nInflation-adjusted iPhone 7 price: $854\nInflation-adjusted iPhone 7 Plus price: $1,011\niPhone 8/8 Plus (2017)\niPhone 8 original starting MSRP: $699\niPhone 8 Plus original starting MSRP: $799\nInflation-adjusted iPhone 8 price: $900\nInflation-adjusted iPhone 8 Plus price: $1,029\niPhone X (2017)\niPhone X original starting MSRP: $999\nInflation-adjusted iPhone X Plus price: $1,287\niPhone XR (2018)\niPhone XR original starting MSRP: $749\nInflation-adjusted iPhone XR Plus price: $942\niPhone XS/S Max (2018) Table of contents\niPhone price history iPhone XS original starting MSRP: $999\niPhone XS Max original starting MSRP: $1,099\nInflation-adjusted iPhone XS price: $1,254\nInflation-adjusted iPhone XS Plus price: $1,380\niPhone 11/Pro/Pro Max (2019)\niPhone 11 original starting MSRP: $699\niPhone 11 Pro original starting MSRP: $999\niPhone 11 Pro Max original starting MSRP: $1099\nInflation-adjusted iPhone 11 price: $863\nInflation-adjusted iPhone 11 Pro price: $1,232\nInflation-adjusted iPhone 11 Pro Max price: $1,355\niPhone 12/Mini/Pro/Pro Max (2020)\niPhone 12 original starting MSRP: $799 Table of contents\niPhone price history Login iPhone 12 Mini original starting MSRP: $699\niPhone 12 Pro original starting MSRP: $999\niPhone 12 Pro Max original starting MSRP: $1099\nInflation-adjusted iPhone 12 price: $976\nInflation-adjusted iPhone 12 Mini price: $853\nInflation-adjusted iPhone 12 Pro price: $1,218\nInflation-adjusted iPhone 12 Pro Max price: $1,340 iPhone 13/Mini/Pro/Pro Max (2021)\niPhone 13 original starting MSRP: $799\niPhone 13 Mini original starting MSRP: $699\niPhone 13 Pro original starting MSRP: $999\niPhone 13 Pro Max original starting MSRP: $1099\nInflation-adjusted iPhone 13 price: $931\nInflation-adjusted iPhone 13 Mini price: $814\nInflation-adjusted iPhone 13 Pro price: $1,163\nInflation-adjusted iPhone 13 Pro Max price: $1,279\niPhone 14/Plus/Pro/Pro Max (2022) Table of contents\niPhone price history Robert Triggs / Android Authority"}
    

## Step 3: Create an OpenAPI tool

Follow the steps in [OpenAPI and Integration Connectors](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools) tools to create an OpenAPI tool.

The following example illustrates how the OpenAPI tool interacts with the new API provided by your Cloud Run functions.
    
    
    openapi: 3.0.0
    info:
      title: iphone_price_tool
      description: An API to search document about iPhone prices.
      version: 1.0.0
    servers:
      - url: https://${CLOUD_FUNCTION_ENDPOINT}
    paths:
      /:
        get:
          summary: Search information about iphone prices
          operationId: search
          parameters:
            - in: query
              name: query
              schema:
                type: string
              required: true
              description: The user's question about iphone price
          responses:
            '200':
              description: Retrieved information about iphone price
              content:
                application/json:
                  schema:
                    type: object
                    properties:
                      content:
                        type: string
                        description: Information about iphone price
            '400':
              description: Bad request, query parameter is missing.
              content:
                text/plain:
                  schema:
                    type: string
                    example: "Please provide a 'query' as a URL parameter for POST requests (e.g., ?query=your_question)."
            '500':
              description: Internal server error.
              content:
                text/plain:
                  schema:
                    type: string
                    example: "Error querying: An unexpected error occurred."
    

## Step 4: Create a generator

Follow the steps in [OpenAPI tool](https://docs.cloud.google.com/gemini-enterprise-cx/agent-assist/tools#step_1_create_a_generator) to create an AI coach generator. Use the AI coach generator content to build LLM prompts.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
