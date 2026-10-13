---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2ATask/
title: Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::A2ATask (v1.2.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:13:44.516990+00:00
---

# Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::A2ATask (v1.2.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2ATask/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Data Analytics API with Gemini V1BETA API - Class Google::Cloud::GeminiDataAnalytics::V1beta::A2ATask (v1.2.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.2.0 (latest)  1.1.0  1.0.0  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.1  0.4.0  0.3.1  0.2.0  0.1.0 

Reference documentation and code samples for the Data Analytics API with Gemini V1BETA API class Google::Cloud::GeminiDataAnalytics::V1beta::A2ATask.

A2ATask is the core unit of action for A2A. It has a current status and when results are created for the task they are stored in the artifact. If there are multiple turns for a task, these are stored in history.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #artifacts
    
    
    def artifacts() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::A2AArtifact>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::A2AArtifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AArtifact)>) — Optional. A set of output artifacts for a Task. 



### #artifacts=
    
    
    def artifacts=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::A2AArtifact>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::A2AArtifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AArtifact)>) — Optional. A set of output artifacts for a Task. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::A2AArtifact](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AArtifact)>) — Optional. A set of output artifacts for a Task. 



### #context_id
    
    
    def context_id() -> ::String

**Returns**

  * (::String) — Optional. Unique identifier (e.g. UUID) for the contextual collection of interactions (tasks and messages). Created by the A2A server. 



### #context_id=
    
    
    def context_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Unique identifier (e.g. UUID) for the contextual collection of interactions (tasks and messages). Created by the A2A server. 



**Returns**

  * (::String) — Optional. Unique identifier (e.g. UUID) for the contextual collection of interactions (tasks and messages). Created by the A2A server. 



### #history
    
    
    def history() -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage>

**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage)>) — Optional. The history of interactions from a task. 



### #history=
    
    
    def history=(value) -> ::Array<::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage>

**Parameter**

  * **value** (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage)>) — Optional. The history of interactions from a task. 



**Returns**

  * (::Array<[::Google::Cloud::GeminiDataAnalytics::V1beta::A2AMessage](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-A2AMessage)>) — Optional. The history of interactions from a task. 



### #id
    
    
    def id() -> ::String

**Returns**

  * (::String) — Optional. Unique identifier (e.g. UUID) for the task, generated by the server for a new task. 



### #id=
    
    
    def id=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Unique identifier (e.g. UUID) for the task, generated by the server for a new task. 



**Returns**

  * (::String) — Optional. Unique identifier (e.g. UUID) for the task, generated by the server for a new task. 



### #metadata
    
    
    def metadata() -> ::Google::Protobuf::Struct

**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. A key/value object to store custom metadata about a task. 



### #metadata=
    
    
    def metadata=(value) -> ::Google::Protobuf::Struct

**Parameter**

  * **value** ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. A key/value object to store custom metadata about a task. 



**Returns**

  * ([::Google::Protobuf::Struct](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Protobuf-Struct)) — Optional. A key/value object to store custom metadata about a task. 



### #status
    
    
    def status() -> ::Google::Cloud::GeminiDataAnalytics::V1beta::TaskStatus

**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::TaskStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-TaskStatus)) — Optional. The current status of a Task, including state and a message. 



### #status=
    
    
    def status=(value) -> ::Google::Cloud::GeminiDataAnalytics::V1beta::TaskStatus

**Parameter**

  * **value** ([::Google::Cloud::GeminiDataAnalytics::V1beta::TaskStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-TaskStatus)) — Optional. The current status of a Task, including state and a message. 



**Returns**

  * ([::Google::Cloud::GeminiDataAnalytics::V1beta::TaskStatus](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-gemini_data_analytics-v1beta/latest/Google-Cloud-GeminiDataAnalytics-V1beta-TaskStatus)) — Optional. The current status of a Task, including state and a message. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
