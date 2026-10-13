---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AgentCoachingInstruction/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AgentCoachingInstruction (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:05:21.850427+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AgentCoachingInstruction (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AgentCoachingInstruction/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::AgentCoachingInstruction (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::AgentCoachingInstruction.

Agent Coaching instructions that customer can configure.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #agent_action
    
    
    def agent_action() -> ::String

**Returns**

  * (::String) — Optional. The action that human agent should take. For example, "apologize for the slow shipping". If the users only want to use agent coaching for intent detection, agent_action can be empty 



### #agent_action=
    
    
    def agent_action=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The action that human agent should take. For example, "apologize for the slow shipping". If the users only want to use agent coaching for intent detection, agent_action can be empty 



**Returns**

  * (::String) — Optional. The action that human agent should take. For example, "apologize for the slow shipping". If the users only want to use agent coaching for intent detection, agent_action can be empty 



### #condition
    
    
    def condition() -> ::String

**Returns**

  * (::String) — Optional. The condition of the instruction. For example, "the customer wants to cancel an order". If the users want the instruction to be triggered unconditionally, the condition can be empty. 



### #condition=
    
    
    def condition=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The condition of the instruction. For example, "the customer wants to cancel an order". If the users want the instruction to be triggered unconditionally, the condition can be empty. 



**Returns**

  * (::String) — Optional. The condition of the instruction. For example, "the customer wants to cancel an order". If the users want the instruction to be triggered unconditionally, the condition can be empty. 



### #display_details
    
    
    def display_details() -> ::String

**Returns**

  * (::String) — Optional. The detailed description of this instruction. 



### #display_details=
    
    
    def display_details=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The detailed description of this instruction. 



**Returns**

  * (::String) — Optional. The detailed description of this instruction. 



### #display_name
    
    
    def display_name() -> ::String

**Returns**

  * (::String) — Optional. Display name for the instruction. 



### #display_name=
    
    
    def display_name=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. Display name for the instruction. 



**Returns**

  * (::String) — Optional. Display name for the instruction. 



### #duplicate_check_result
    
    
    def duplicate_check_result() -> ::Google::Cloud::Dialogflow::V2::AgentCoachingInstruction::DuplicateCheckResult

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AgentCoachingInstruction::DuplicateCheckResult](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AgentCoachingInstruction-DuplicateCheckResult)) — Output only. Duplication check for the AgentCoachingInstruction. 



### #system_action
    
    
    def system_action() -> ::String

**Returns**

  * (::String) — Optional. The action that system should take. For example, "call GetOrderTime with order_number={order number provided by the customer}". If the users don't have plugins or don't want to trigger plugins, the system_action can be empty 



### #system_action=
    
    
    def system_action=(value) -> ::String

**Parameter**

  * **value** (::String) — Optional. The action that system should take. For example, "call GetOrderTime with order_number={order number provided by the customer}". If the users don't have plugins or don't want to trigger plugins, the system_action can be empty 



**Returns**

  * (::String) — Optional. The action that system should take. For example, "call GetOrderTime with order_number={order number provided by the customer}". If the users don't have plugins or don't want to trigger plugins, the system_action can be empty 



### #triggering_event
    
    
    def triggering_event() -> ::Google::Cloud::Dialogflow::V2::AgentCoachingInstruction::TriggerEvent

**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AgentCoachingInstruction::TriggerEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AgentCoachingInstruction-TriggerEvent)) — Optional. The event that should trigger this instruction. If UNSPECIFIED, the instruction triggering will be same as the generator's trigger_event. 



### #triggering_event=
    
    
    def triggering_event=(value) -> ::Google::Cloud::Dialogflow::V2::AgentCoachingInstruction::TriggerEvent

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::V2::AgentCoachingInstruction::TriggerEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AgentCoachingInstruction-TriggerEvent)) — Optional. The event that should trigger this instruction. If UNSPECIFIED, the instruction triggering will be same as the generator's trigger_event. 



**Returns**

  * ([::Google::Cloud::Dialogflow::V2::AgentCoachingInstruction::TriggerEvent](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-AgentCoachingInstruction-TriggerEvent)) — Optional. The event that should trigger this instruction. If UNSPECIFIED, the instruction triggering will be same as the generator's trigger_event. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
