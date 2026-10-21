---
url: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations/
title: Conversational Analytics API locations \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:21:56.513193+00:00
---

# Conversational Analytics API locations  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/locations/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Data Agents ](https://docs.cloud.google.com/gemini/data-agents)
  * [ Conversational Analytics API ](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview)



Send feedback 

#  Conversational Analytics API locations Stay organized with collections  Save and categorize content based on your preferences. 

The Conversational Analytics API lets you control the geographic location of your agent's resources, configuration, and data by specifying a regional or multi-regional API endpoint.

The API defaults to the `global` endpoint and supports specific regional and multi-regional endpoints.

**Important:** The default `global` endpoint does not restrict where your data is stored at rest. Its data centers are spread throughout the world, and you cannot control the location of your data with this endpoint. To meet data residency requirements for data at rest, you must specify one of the regional or multi-regional endpoints that are listed on this page. Depending on the service, there is a distinction between "US" and "us", and between "EU" and "eu". For the list of services and the corresponding values, see the [multi-regional locations](https://cloud.google.com/about/locations?_gl=1*p78l2t*_ga*Njc4NTc2NDMzLjE3NzM5NDg4MDA.*_ga_WH2QY8WWF5*czE3NzQzNzgyNzEkbzEkZzEkdDE3NzQzNzk1MTYkajIyJGwwJGgw#multi-region).

To see a list of the locations that are available for the Conversational Analytics API for different parts of the world, select one of the following options:

**Important:** If your location is not included in the following table, use the `global` default location.

### Americas

Location name | Location type | Location description  
---|---|---  
`us` | Multi-region | Data centers in the United States  
`northamerica-northeast1` | Region | Data centers in Montréal (BigQuery data sources only)  
`northamerica-northeast2` | Region | Data centers in Toronto (BigQuery data sources only)  
`us-east4` | Region | Data centers in Northern Virginia  
  
### Europe

Location name | Location type | Location description  
---|---|---  
`eu` | Multi-region | Data centers within member states of the European Union  
  
**Important:** When you use regional or multi-regional endpoints, ensure that the location in your request path matches the endpoint. For example, if you use the `geminidataanalytics.us.rep.googleapis.com` endpoint, specify `us` in your request path (such as `/locations/us`). For more details, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).

## What's next:

For details on how to use these locations to control where your data is stored at rest, see [Data residency](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/data-residency).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-16 UTC."],[],[]] 
