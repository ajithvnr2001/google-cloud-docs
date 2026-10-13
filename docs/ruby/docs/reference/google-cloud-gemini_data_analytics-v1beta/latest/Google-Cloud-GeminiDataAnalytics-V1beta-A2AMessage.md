---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:13:56.005654+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage.

A2AMessage is one unit of communication between client and server.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #content
    
    
    def content() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::Part>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Part](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Part)>) — Optional. Content is the container of the message content. 



### #content=
    
    
    def content=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::Part>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Part](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Part)>) — Optional. Content is the container of the message content. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::Part](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Part)>) — Optional. Content is the container of the message content. 



### #context_id
    
    
    def context_id() -> ::String

**Returns**

  * (::String) — Optional. The context id of the message. 



### #context_id=
    
    
    def context_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The context id of the message. 



**Returns**

  * (::String) — Optional. The context id of the message. 



### #extensions
    
    
    def extensions() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — Optional. The URIs of extensions that are present or contributed to this Message. 



### #extensions=
    
    
    def extensions=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — Optional. The URIs of extensions that are present or contributed to this Message. 



**Returns**

  * (::Array<::String>) — Optional. The URIs of extensions that are present or contributed to this Message. 



### #message_id
    
    
    def message_id() -> ::String

**Returns**

  * (::String) — Optional. The unique identifier (e.g. UUID) of the message. 



### #message_id=
    
    
    def message_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The unique identifier (e.g. UUID) of the message. 



**Returns**

  * (::String) — Optional. The unique identifier (e.g. UUID) of the message. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. Any optional metadata to provide along with the message. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. Any optional metadata to provide along with the message. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. Any optional metadata to provide along with the message. 



### #role
    
    
    def role() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Role

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Role](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Role)) — Optional. A role for the message. 



### #role=
    
    
    def role=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::Role

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::Role](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Role)) — Optional. A role for the message. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::Role](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-Role)) — Optional. A role for the message. 



### #task_id
    
    
    def task_id() -> ::String

**Returns**

  * (::String) — Optional. The task id of the message. 



### #task_id=
    
    
    def task_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The task id of the message. 



**Returns**

  * (::String) — Optional. The task id of the message. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
