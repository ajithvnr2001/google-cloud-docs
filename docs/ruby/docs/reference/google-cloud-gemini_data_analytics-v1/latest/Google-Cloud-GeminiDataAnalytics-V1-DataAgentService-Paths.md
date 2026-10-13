---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-DataAgentService-Paths/
title: Data Analytics API with Gemini V1 API - Module Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Paths (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:17:46.182729+00:00
---

# Data Analytics API with Gemini V1 API - Module Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Paths (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-DataAgentService-Paths/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1 API - Module Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Paths (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1 API module Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Paths.

Path helper methods for the DataAgentService API.

## Extended By

  * [Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-DataAgentService-Paths)



## Included In

  * [Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-DataAgentService-Client)
  * [Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Paths](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-DataAgentService-Paths)
  * [Google::Cloud::GeminiDataAnalytics::V1::DataAgentService::Rest::Client](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-DataAgentService-Rest-Client)



## Methods 

### #crypto_key_path
    
    
    def crypto_key_path(project:, location:, key_ring:, crypto_key:) -> ::String

Create a fully-qualified CryptoKey resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/keyRings/{key_ring}/cryptoKeys/{crypto_key}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **key_ring** (String) 
  * **crypto_key** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #data_agent_path
    
    
    def data_agent_path(project:, location:, data_agent:) -> ::String

Create a fully-qualified DataAgent resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}/dataAgents/{data_agent}`

**Parameters**

  * **project** (String) 
  * **location** (String) 
  * **data_agent** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



### #location_path
    
    
    def location_path(project:, location:) -> ::String

Create a fully-qualified Location resource string.

The resource will be in the following format:

`projects/{project}/locations/{location}`

**Parameters**

  * **project** (String) 
  * **location** (String) 



**Returns**

  * (::String) 



**Raises**

  * (::ArgumentError) 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
