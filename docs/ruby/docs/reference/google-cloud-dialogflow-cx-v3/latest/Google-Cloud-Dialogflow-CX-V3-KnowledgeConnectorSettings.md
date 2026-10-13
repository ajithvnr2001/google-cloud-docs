---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-KnowledgeConnectorSettings/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:47:05.158146+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-KnowledgeConnectorSettings/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::KnowledgeConnectorSettings.

The Knowledge Connector settings for this page or flow. This includes information such as the attached Knowledge Bases, and the way to execute fulfillment.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #data_store_connections
    
    
    def data_store_connections() -> ::Array<::Google::Cloud::Dialogflow::CX::V3::DataStoreConnection>

**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::DataStoreConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DataStoreConnection)>) — Optional. List of related data store connections. 



### #data_store_connections=
    
    
    def data_store_connections=(value) -> ::Array<::Google::Cloud::Dialogflow::CX::V3::DataStoreConnection>

**Parameter**

  * **value** (::Array<[::Google::Cloud::Dialogflow::CX::V3::DataStoreConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DataStoreConnection)>) — Optional. List of related data store connections. 



**Returns**

  * (::Array<[::Google::Cloud::Dialogflow::CX::V3::DataStoreConnection](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-DataStoreConnection)>) — Optional. List of related data store connections. 



### #enabled
    
    
    def enabled() -> ::Boolean

**Returns**

  * (::Boolean) — Whether Knowledge Connector is enabled or not. 



### #enabled=
    
    
    def enabled=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether Knowledge Connector is enabled or not. 



**Returns**

  * (::Boolean) — Whether Knowledge Connector is enabled or not. 



### #target_flow
    
    
    def target_flow() -> ::String

**Returns**

  * (::String) — The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.

Note: The following fields are mutually exclusive: `target_flow`, `target_page`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #target_flow=
    
    
    def target_flow=(value) -> ::String

**Parameter**

  * **value** (::String) — The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.

Note: The following fields are mutually exclusive: `target_flow`, `target_page`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The target flow to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.

Note: The following fields are mutually exclusive: `target_flow`, `target_page`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #target_page
    
    
    def target_page() -> ::String

**Returns**

  * (::String) — The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

Note: The following fields are mutually exclusive: `target_page`, `target_flow`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #target_page=
    
    
    def target_page=(value) -> ::String

**Parameter**

  * **value** (::String) — The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

Note: The following fields are mutually exclusive: `target_page`, `target_flow`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * (::String) — The target page to transition to. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>/pages/<PageID>`.

Note: The following fields are mutually exclusive: `target_page`, `target_flow`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #trigger_fulfillment
    
    
    def trigger_fulfillment() -> ::Google::Cloud::Dialogflow::CX::V3::Fulfillment

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Fulfillment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment)) — The fulfillment to be triggered.

When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment. 




### #trigger_fulfillment=
    
    
    def trigger_fulfillment=(value) -> ::Google::Cloud::Dialogflow::CX::V3::Fulfillment

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::Fulfillment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment)) — The fulfillment to be triggered.

When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::Fulfillment](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Fulfillment)) — The fulfillment to be triggered.

When the answers from the Knowledge Connector are selected by Dialogflow, you can utitlize the request scoped parameter `$request.knowledge.answers` (contains up to the 5 highest confidence answers) and `$request.knowledge.questions` (contains the corresponding questions) to construct the fulfillment. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
