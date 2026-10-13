---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageRequest/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:14:11.861143+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageRequest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageRequest.

Request message for SendMessage and SendStreamingMessage.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #configuration
    
    
    def configuration() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageConfiguration

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageConfiguration)) — Optional. Configuration for the send request. 



### #configuration=
    
    
    def configuration=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageConfiguration

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageConfiguration)) — Optional. Configuration for the send request. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::SendMessageConfiguration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-SendMessageConfiguration)) — Optional. Configuration for the send request. 



### #message
    
    
    def message() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage)) — Required. The message to send to the agent. 



### #message=
    
    
    def message=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage)) — Required. The message to send to the agent. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage)) — Required. The message to send to the agent. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. Optional metadata for the request. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. Optional metadata for the request. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. Optional metadata for the request. 



### #tenant
    
    
    def tenant() -> ::String

**Returns**

  * (::String) — Optional. Optional tenant, provided as a path parameter. 



### #tenant=
    
    
    def tenant=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Optional tenant, provided as a path parameter. 



**Returns**

  * (::String) — Optional. Optional tenant, provided as a path parameter. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
