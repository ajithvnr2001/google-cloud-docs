---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-CreateConversationRequest/
title: Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::CreateConversationRequest (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:16:49.286045+00:00
---

# Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::CreateConversationRequest (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-CreateConversationRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1 API - Class Google::Cloud::GeminiDataAnalytics::V1::CreateConversationRequest (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1 API class Google::Cloud::GeminiDataAnalytics::V1::CreateConversationRequest.

Request for creating a conversation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #conversation
    
    
    def conversation() -> ::Google::Cloud::GeminiDataAnalytics::V1::Conversation

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-Conversation)) — Required. The conversation to create. 



### #conversation=
    
    
    def conversation=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1::Conversation

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-Conversation)) — Required. The conversation to create. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1::Conversation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1/latest/Google-Cloud-GeminiDataAnalytics-V1-Conversation)) — Required. The conversation to create. 



### #conversation_id
    
    
    def conversation_id() -> ::String

**Returns**

  * (::String) — Optional. The conversation id of the conversation to create. Must be unique within the parent. The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. If not provided, the server will auto-generate a value for the id. 



### #conversation_id=
    
    
    def conversation_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The conversation id of the conversation to create. Must be unique within the parent. The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. If not provided, the server will auto-generate a value for the id. 



**Returns**

  * (::String) — Optional. The conversation id of the conversation to create. Must be unique within the parent. The allowed format is: `^[a-z]([a-z0-9-]{0,61}[a-z0-9])?$`. If not provided, the server will auto-generate a value for the id. 



### #parent
    
    
    def parent() -> ::String

**Returns**

  * (::String) — Required. Parent value for CreateConversationRequest. Format: `projects/{project}/locations/{location}`



### #parent=
    
    
    def parent=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. Parent value for CreateConversationRequest. Format: `projects/{project}/locations/{location}`



**Returns**

  * (::String) — Required. Parent value for CreateConversationRequest. Format: `projects/{project}/locations/{location}`



### #request_id
    
    
    def request_id() -> ::String

**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 



### #request_id=
    
    
    def request_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 



**Returns**

  * (::String) — Optional. An optional request ID to identify requests. Specify a unique request ID so that if you must retry your request, the server will know to ignore the request if it has already been completed. The server will guarantee that for at least 60 minutes since the first request. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
