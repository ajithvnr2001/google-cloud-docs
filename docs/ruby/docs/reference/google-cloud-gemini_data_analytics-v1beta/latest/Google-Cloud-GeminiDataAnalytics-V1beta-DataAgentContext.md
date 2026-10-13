---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataAgentContext/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:24:21.072470+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataAgentContext/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext.

Context for the chat request using a data agent.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #context_version
    
    
    def context_version() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext::ContextVersion

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext::ContextVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataAgentContext-ContextVersion)) — Optional. Version of context to be used by DCS (e.g. STAGING, PUBLISHED) 



### #context_version=
    
    
    def context_version=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext::ContextVersion

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext::ContextVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataAgentContext-ContextVersion)) — Optional. Version of context to be used by DCS (e.g. STAGING, PUBLISHED) 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::DataAgentContext::ContextVersion](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-DataAgentContext-ContextVersion)) — Optional. Version of context to be used by DCS (e.g. STAGING, PUBLISHED) 



### #credentials
    
    
    def credentials() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Credentials

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Credentials](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Credentials)) — Optional. Deprecated: Use credentials in ChatRequest. The credentials to use when calling the Looker data source.

Currently supports both OAuth token and API key-based credentials, as described in [Authentication with an SDK](https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk). 




### #credentials=
    
    
    def credentials=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Credentials

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::Credentials](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Credentials)) — Optional. Deprecated: Use credentials in ChatRequest. The credentials to use when calling the Looker data source.

Currently supports both OAuth token and API key-based credentials, as described in [Authentication with an SDK](https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk). 




**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Credentials](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Credentials)) — Optional. Deprecated: Use credentials in ChatRequest. The credentials to use when calling the Looker data source.

Currently supports both OAuth token and API key-based credentials, as described in [Authentication with an SDK](https://cloud.google.com/looker/docs/api-auth#authentication_with_an_sdk). 




### #data_agent
    
    
    def data_agent() -> ::String

**Returns**

  * (::String) — Required. The name of the data agent resource. 



### #data_agent=
    
    
    def data_agent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The name of the data agent resource. 



**Returns**

  * (::String) — Required. The name of the data agent resource. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
