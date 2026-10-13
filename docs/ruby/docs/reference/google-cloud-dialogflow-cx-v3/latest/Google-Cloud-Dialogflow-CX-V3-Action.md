---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Action/
title: Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Action (v1.12.2) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:31:51.677562+00:00
---

# Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Action (v1.12.2)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-Action/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow CX V3 API - Class Google::Cloud::Dialogflow::CX::V3::Action (v1.12.2) Stay organized with collections  Save and categorize content based on your preferences. 

1.12.2 (latest)  1.12.1  1.11.0  1.10.1  1.9.0  1.8.0  1.7.0  1.6.1  1.5.0  1.4.0  1.3.0  1.2.0  1.1.1  1.0.0  0.26.0  0.25.0  0.24.2  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.0  0.16.0  0.15.1  0.14.0  0.13.0  0.12.0  0.11.0  0.10.2  0.9.0  0.8.1  0.7.1  0.6.0  0.5.0  0.4.0 

Reference documentation and code samples for the Dialogflow CX V3 API class Google::Cloud::Dialogflow::CX::V3::Action.

Action performed by end user or Dialogflow agent in the conversation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #agent_utterance
    
    
    def agent_utterance() -> ::Google::Cloud::Dialogflow::CX::V3::AgentUtterance

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AgentUtterance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AgentUtterance)) — Optional. Action performed by the agent as a message.

Note: The following fields are mutually exclusive: `agent_utterance`, `user_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #agent_utterance=
    
    
    def agent_utterance=(value) -> ::Google::Cloud::Dialogflow::CX::V3::AgentUtterance

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::AgentUtterance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AgentUtterance)) — Optional. Action performed by the agent as a message.

Note: The following fields are mutually exclusive: `agent_utterance`, `user_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::AgentUtterance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-AgentUtterance)) — Optional. Action performed by the agent as a message.

Note: The following fields are mutually exclusive: `agent_utterance`, `user_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #flow_invocation
    
    
    def flow_invocation() -> ::Google::Cloud::Dialogflow::CX::V3::FlowInvocation

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowInvocation)) — Optional. Action performed on behalf of the agent by invoking a CX flow.

Note: The following fields are mutually exclusive: `flow_invocation`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #flow_invocation=
    
    
    def flow_invocation=(value) -> ::Google::Cloud::Dialogflow::CX::V3::FlowInvocation

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::FlowInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowInvocation)) — Optional. Action performed on behalf of the agent by invoking a CX flow.

Note: The following fields are mutually exclusive: `flow_invocation`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowInvocation)) — Optional. Action performed on behalf of the agent by invoking a CX flow.

Note: The following fields are mutually exclusive: `flow_invocation`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #flow_transition
    
    
    def flow_transition() -> ::Google::Cloud::Dialogflow::CX::V3::FlowTransition

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowTransition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowTransition)) — Optional. Action performed on behalf of the agent by transitioning to a target CX flow.

Note: The following fields are mutually exclusive: `flow_transition`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #flow_transition=
    
    
    def flow_transition=(value) -> ::Google::Cloud::Dialogflow::CX::V3::FlowTransition

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::FlowTransition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowTransition)) — Optional. Action performed on behalf of the agent by transitioning to a target CX flow.

Note: The following fields are mutually exclusive: `flow_transition`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::FlowTransition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-FlowTransition)) — Optional. Action performed on behalf of the agent by transitioning to a target CX flow.

Note: The following fields are mutually exclusive: `flow_transition`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #playbook_invocation
    
    
    def playbook_invocation() -> ::Google::Cloud::Dialogflow::CX::V3::PlaybookInvocation

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::PlaybookInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookInvocation)) — Optional. Action performed on behalf of the agent by invoking a child playbook.

Note: The following fields are mutually exclusive: `playbook_invocation`, `user_utterance`, `agent_utterance`, `tool_use`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #playbook_invocation=
    
    
    def playbook_invocation=(value) -> ::Google::Cloud::Dialogflow::CX::V3::PlaybookInvocation

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::PlaybookInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookInvocation)) — Optional. Action performed on behalf of the agent by invoking a child playbook.

Note: The following fields are mutually exclusive: `playbook_invocation`, `user_utterance`, `agent_utterance`, `tool_use`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::PlaybookInvocation](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookInvocation)) — Optional. Action performed on behalf of the agent by invoking a child playbook.

Note: The following fields are mutually exclusive: `playbook_invocation`, `user_utterance`, `agent_utterance`, `tool_use`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #playbook_transition
    
    
    def playbook_transition() -> ::Google::Cloud::Dialogflow::CX::V3::PlaybookTransition

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::PlaybookTransition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookTransition)) — Optional. Action performed on behalf of the agent by transitioning to a target playbook.

Note: The following fields are mutually exclusive: `playbook_transition`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #playbook_transition=
    
    
    def playbook_transition=(value) -> ::Google::Cloud::Dialogflow::CX::V3::PlaybookTransition

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::PlaybookTransition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookTransition)) — Optional. Action performed on behalf of the agent by transitioning to a target playbook.

Note: The following fields are mutually exclusive: `playbook_transition`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::PlaybookTransition](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-PlaybookTransition)) — Optional. Action performed on behalf of the agent by transitioning to a target playbook.

Note: The following fields are mutually exclusive: `playbook_transition`, `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #tool_use
    
    
    def tool_use() -> ::Google::Cloud::Dialogflow::CX::V3::ToolUse

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ToolUse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ToolUse)) — Optional. Action performed on behalf of the agent by calling a plugin tool.

Note: The following fields are mutually exclusive: `tool_use`, `user_utterance`, `agent_utterance`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #tool_use=
    
    
    def tool_use=(value) -> ::Google::Cloud::Dialogflow::CX::V3::ToolUse

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::ToolUse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ToolUse)) — Optional. Action performed on behalf of the agent by calling a plugin tool.

Note: The following fields are mutually exclusive: `tool_use`, `user_utterance`, `agent_utterance`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::ToolUse](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-ToolUse)) — Optional. Action performed on behalf of the agent by calling a plugin tool.

Note: The following fields are mutually exclusive: `tool_use`, `user_utterance`, `agent_utterance`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #user_utterance
    
    
    def user_utterance() -> ::Google::Cloud::Dialogflow::CX::V3::UserUtterance

**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::UserUtterance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UserUtterance)) — Optional. Agent obtained a message from the customer.

Note: The following fields are mutually exclusive: `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




### #user_utterance=
    
    
    def user_utterance=(value) -> ::Google::Cloud::Dialogflow::CX::V3::UserUtterance

**Parameter**

  * **value** ([::Google::Cloud::Dialogflow::CX::V3::UserUtterance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UserUtterance)) — Optional. Agent obtained a message from the customer.

Note: The following fields are mutually exclusive: `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




**Returns**

  * ([::Google::Cloud::Dialogflow::CX::V3::UserUtterance](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-cx-v3/latest/Google-Cloud-Dialogflow-CX-V3-UserUtterance)) — Optional. Agent obtained a message from the customer.

Note: The following fields are mutually exclusive: `user_utterance`, `agent_utterance`, `tool_use`, `playbook_invocation`, `flow_invocation`, `playbook_transition`, `flow_transition`. If a field in that set is populated, all other fields in the set will automatically be cleared. 




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
