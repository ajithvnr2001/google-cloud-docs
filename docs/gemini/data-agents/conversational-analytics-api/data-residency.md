---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency/
title: Data residency \u00a0|\u00a0 Conversational Analytics API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:45:25.992572+00:00
---

# Data residency  |  Conversational Analytics API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Data residency Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how the Conversational Analytics API supports data residency. _Data residency_ refers to the physical location of your data and the commitments to store and process your data within a specific geographic area to meet regulatory or policy requirements. To control the location of your data, you specify a regional service endpoint for your API requests.

In this document, _location_ refers to a Google Cloud [region or multi-region](https://cloud.google.com/about/locations) where data resides, and _your data_ has the same meaning as "Customer Data" in the _Data Location_ section of the [Service Specific Terms](https://cloud.google.com/terms/service-terms).

Data residency commitments for the Conversational Analytics API vary based on whether your agent connects to BigQuery or to Looker.

## Data residency scope

The Conversational Analytics API helps you meet data residency requirements by providing controls over the location of customer data in different states:

  * Data is _at rest_ when it is stored in persistent storage, rather than actively being processed or transmitted.
  * Data is _in use_ when it is in memory, such as when machine learning (ML) models process data to generate a response or when the service executes a query. For the Conversational Analytics API, data residency commitments for data in use are specific to jurisdictional ML processing and don't provide comprehensive residency for all states of data in use.
  * Data is _in transit_ when it is entering or exiting the Google network perimeter.



Data residency commitments for the Conversational Analytics API apply to `DataAgent` resources (including customer configurations, context, system instructions, and example queries) and `Conversation` resources (including message content and state history). These commitments don't apply to service data, such as resource identifiers and labels, or to data in transit.

## Supported data locations

The Conversational Analytics API supports global, regional, and multi-regional locations. When you use a regional or multi-regional endpoint, you control the location where your data is stored at rest.

In the following tables, jurisdictional machine learning (ML) processing (identified as **In use (jurisdictional)**) refers to ML processing commitments for your data. As defined in the [Service Specific Terms](https://cloud.google.com/terms/service-terms), Google performs machine learning processing of your data only in your selected region or multi-region.

The following sections provide details about data residency support for agents and conversations that use BigQuery and Looker data sources.

### BigQuery data

For data agents that connect to BigQuery, regional and multi-regional endpoints support data residency for data at rest and jurisdictional ML processing for data in use. Regardless of the endpoint location that you specify, the agent can connect to BigQuery datasets in any location or combination of locations:

Location | Location description | Endpoint type | Endpoint URL | Dataset location | Data residency support  
---|---|---|---|---|---  
`global` | Global | Global | `geminidataanalytics.googleapis.com` | Any region or multi-region | Not supported  
`eu` | European Union | Multi-regional | `geminidataanalytics.eu.rep.googleapis.com` | Any region or multi-region | **At rest** , **In use (jurisdictional)**  
`us` | United States | Multi-regional | `geminidataanalytics.us.rep.googleapis.com` | Any region or multi-region | **At rest** , **In use (jurisdictional)**  
`us-east4` | Northern Virginia | Regional | `geminidataanalytics-us-east4.googleapis.com` | Any region or multi-region | **At rest** , **In use (jurisdictional)**  
**Note:** The [`ThinkingMode` parameter](https://docs.cloud.google.com/gemini/data-agents/reference/rest/v1beta/projects.locations/chat#ThinkingMode) is supported only with preview model versions. Because GA model versions don't support this parameter, enabling thinking mode automatically switches the agent to a preview model version.

### Looker data

For data agents that connect to Looker, regional and multi-regional endpoints support data residency for data at rest. Regardless of the endpoint location that you specify, the agent can connect to data sources in any location or combination of locations:

Location | Location description | Endpoint type | Endpoint URL | Dataset location | Data residency support  
---|---|---|---|---|---  
`global` | Global | Global | `geminidataanalytics.googleapis.com` | Any region or multi-region | Not supported  
`eu` | European Union | Multi-regional | `geminidataanalytics.eu.rep.googleapis.com` | Any region or multi-region | **At rest**  
`us` | United States | Multi-regional | `geminidataanalytics.us.rep.googleapis.com` | Any region or multi-region | **At rest**  
`us-east4` | Northern Virginia | Regional | `geminidataanalytics-us-east4.googleapis.com` | Any region or multi-region | **At rest**  
  
For the full list of available regional and multi-regional endpoints, see [Conversational Analytics API locations](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations).

## Enforce data residency with regional endpoints

To enforce data residency for your `DataAgent` and `Conversation` resources, use a regional endpoint when you create and access them. When you call regional endpoints, the location in your request path or request parent must match the location of the endpoint that you're calling. For example, if you call the `geminidataanalytics.us.rep.googleapis.com` endpoint, you must specify `us` in your request path or request parent (such as `/locations/us` or `projects/PROJECT_ID/locations/us`).

The service endpoints for the Conversational Analytics API use the following formats, depending on the location type:

  * **Global** : `geminidataanalytics.googleapis.com`
  * **Multi-regional** : `geminidataanalytics.LOCATION.rep.googleapis.com`
  * **Regional** : `geminidataanalytics-LOCATION.googleapis.com`



Replace the LOCATION placeholder with a supported single region or multi-region, such as `eu`, `us`, or `us-east4`.

The following examples show how to configure a regional endpoint for HTTP and Python SDK requests:

### HTTP

To use a regional endpoint with HTTP, construct the request URL with the regional base URL. First, configure the `base_url` to use your chosen regional endpoint, as shown in the following example from [Configure initial settings and authentication](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#configure_initial_settings_and_authentication):
    
    
    project_id = "PROJECT_ID"
    location = "LOCATION"
    
    # Set the base URL based on location.
    if not location or location == "global":
      base_url = "https://geminidataanalytics.googleapis.com"
    elif "-" in location:
      # Regional endpoints
      base_url = f"https://geminidataanalytics-{location}.googleapis.com"
    else:
      # Multi-regional endpoints
      base_url = f"https://geminidataanalytics.{location}.rep.googleapis.com"
    

Then, use the `base_url` variable when constructing URLs for API requests, such as in this example from [Ask questions with stateful and stateless chat](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-http#chat-modes):
    
    
    # Example API request URL construction using base_url:
    chat_url = f"{base_url}/v1beta/projects/{project_id}/locations/{location}:chat"
    

### Python SDK

To use a regional endpoint with the Python SDK, pass `client_options` with the regional `api_endpoint` parameter when initializing API clients, as shown in the following example from [Configure settings and initialize clients](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/build-agent-sdk#configure-settings-and-initialize-clients).
    
    
    from google.cloud import geminidataanalytics
    from google.api_core import client_options
    
    project_id = "PROJECT_ID"
    location = "LOCATION"
    
    # Set client options based on location.
    if not location or location == "global":
      endpoint = "geminidataanalytics.googleapis.com"
    elif "-" in location:
      # Regional endpoints
      endpoint = f"geminidataanalytics-{location}.googleapis.com"
    else:
      # Multi-regional endpoints
      endpoint = f"geminidataanalytics.{location}.rep.googleapis.com"
    opts = client_options.ClientOptions(api_endpoint=endpoint)
    
    # Use client options when initializing API clients.
    data_agent_client = geminidataanalytics.[DataAgentServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_agent_service.DataAgentServiceClient.html)(client_options=opts)
    data_chat_client = geminidataanalytics.[DataChatServiceClient](https://docs.cloud.google.com/python/docs/reference/google-cloud-geminidataanalytics/latest/google.cloud.geminidataanalytics_v1.services.data_chat_service.DataChatServiceClient.html)(client_options=opts)
    
    # Use clients to make API requests. For example:
    # response = data_chat_client.chat(request=request)
    

Replace the sample values as follows:

  * PROJECT_ID: Your Google Cloud project ID.
  * LOCATION: The region or multi-region where you want to create your resources. To use one of the regional endpoints, specify `eu`, `us`, or `us-east4`.



## Limitations

When you use regional endpoints, consider the following points:

  * If you use [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/cmek) with the Conversational Analytics API, your Cloud KMS key must be in the same location as your regional endpoint.



## What's next

  * View the list of [supported locations for Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations).
  * Learn about [customer-managed encryption keys (CMEK)](https://docs.cloud.google.com/kms/docs/cmek).
  * Learn more about [Google Cloud locations](https://cloud.google.com/about/locations).
  * See the [Service Specific Terms](https://cloud.google.com/terms/service-terms) for general Data Location commitments.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
