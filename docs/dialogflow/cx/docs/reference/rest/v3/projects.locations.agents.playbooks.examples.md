---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples
title: REST Resource: projects.locations.agents.playbooks.examples \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:15.905750+00:00
---

# REST Resource: projects.locations.agents.playbooks.examples  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.playbooks.examples Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Example
    * JSON representation
    * PlaybookInput
      * JSON representation
    * PlaybookOutput
      * JSON representation
    * Action
      * JSON representation
    * UserUtterance
      * JSON representation
    * AgentUtterance
      * JSON representation
    * ToolUse
      * JSON representation
    * PlaybookInvocation
      * JSON representation
    * OutputState
    * FlowInvocation
      * JSON representation
    * PlaybookTransition
      * JSON representation
    * FlowTransition
      * JSON representation
  * Methods



## Resource: Example

Example represents a sample execution of the playbook in the conversation.

An example consists of a list of ordered actions performed by end user or Dialogflow agent according the playbook instructions to fulfill the task.

JSON representation  
---  
      
    
    {
      "name": string,
      "playbookInput": {
        object ([PlaybookInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookInput))
      },
      "playbookOutput": {
        object ([PlaybookOutput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookOutput))
      },
      "actions": [
        {
          object ([Action](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.Action))
        }
      ],
      "displayName": string,
      "description": string,
      "tokenCount": string,
      "createTime": string,
      "updateTime": string,
      "conversationState": enum ([OutputState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.OutputState)),
      "languageCode": string
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the playbook example. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>/examples/<ExampleID>`.  
`playbookInput` |  `object (`[PlaybookInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookInput)`)` Optional. The input to the playbook in the example.  
`playbookOutput` |  `object (`[PlaybookOutput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookOutput)`)` Optional. The output of the playbook in the example.  
`actions[]` |  `object (`[Action](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.Action)`)` Required. The ordered list of actions performed by the end user and the Dialogflow agent.  
`displayName` |  `string` Required. The display name of the example.  
`description` |  `string` Optional. The high level concise description of the example. The max number of characters is 200.  
`tokenCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Estimated number of tokes current example takes when sent to the LLM.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of initial example creation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last time the example was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`conversationState` |  `enum (`[OutputState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.OutputState)`)` Required. Example's output state.  
`languageCode` |  `string` Optional. The language code of the example. If not specified, the agent's default language is used. Note: languages must be enabled in the agent before they can be used. Note: example's language code is not currently used in dialogflow agents.  
  
### PlaybookInput

Input of the playbook.

JSON representation  
---  
      
    
    {
      "precedingConversationSummary": string
    }  
  
Fields  
---  
`precedingConversationSummary` |  `string` Optional. Summary string of the preceding conversation for the child playbook invocation.  
  
### PlaybookOutput

Output of the playbook.

JSON representation  
---  
      
    
    {
      "executionSummary": string
    }  
  
Fields  
---  
`executionSummary` |  `string` Optional. Summary string of the execution result of the child playbook.  
  
### Action

Action performed by end user or Dialogflow agent in the conversation.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "userUtterance": {
        object ([UserUtterance](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.UserUtterance))
      },
      "agentUtterance": {
        object ([AgentUtterance](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.AgentUtterance))
      },
      "toolUse": {
        object ([ToolUse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.ToolUse))
      },
      "playbookInvocation": {
        object ([PlaybookInvocation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookInvocation))
      },
      "flowInvocation": {
        object ([FlowInvocation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.FlowInvocation))
      },
      "playbookTransition": {
        object ([PlaybookTransition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookTransition))
      },
      "flowTransition": {
        object ([FlowTransition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.FlowTransition))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Action details. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`userUtterance` |  `object (`[UserUtterance](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.UserUtterance)`)` Optional. Agent obtained a message from the customer.  
`agentUtterance` |  `object (`[AgentUtterance](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.AgentUtterance)`)` Optional. Action performed by the agent as a message.  
`toolUse` |  `object (`[ToolUse](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.ToolUse)`)` Optional. Action performed on behalf of the agent by calling a plugin tool.  
`playbookInvocation` |  `object (`[PlaybookInvocation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookInvocation)`)` Optional. Action performed on behalf of the agent by invoking a child playbook.  
`flowInvocation` |  `object (`[FlowInvocation](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.FlowInvocation)`)` Optional. Action performed on behalf of the agent by invoking a CX flow.  
`playbookTransition` |  `object (`[PlaybookTransition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookTransition)`)` Optional. Action performed on behalf of the agent by transitioning to a target playbook.  
`flowTransition` |  `object (`[FlowTransition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.FlowTransition)`)` Optional. Action performed on behalf of the agent by transitioning to a target CX flow.  
End of mutually exclusive fields.  
  
### UserUtterance

UserUtterance represents one message sent by the customer.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Required. Message content in text.  
  
### AgentUtterance

AgentUtterance represents one message sent by the agent.

JSON representation  
---  
      
    
    {
      "text": string
    }  
  
Fields  
---  
`text` |  `string` Required. Message content in text.  
  
### ToolUse

Stores metadata of the invocation of an action supported by a tool.

JSON representation  
---  
      
    
    {
      "tool": string,
      "displayName": string,
      "action": string,
      "inputActionParameters": {
        object
      },
      "outputActionParameters": {
        object
      }
    }  
  
Fields  
---  
`tool` |  `string` Required. The `[tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)` that should be used. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>`.  
`displayName` |  `string` Output only. The display name of the tool.  
`action` |  `string` Optional. Name of the action to be called during the tool use.  
`inputActionParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A list of input parameters for the action.  
`outputActionParameters` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. A list of output parameters generated by the action.  
  
### PlaybookInvocation

Stores metadata of the invocation of a child playbook.

JSON representation  
---  
      
    
    {
      "playbook": string,
      "displayName": string,
      "playbookInput": {
        object ([PlaybookInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookInput))
      },
      "playbookOutput": {
        object ([PlaybookOutput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookOutput))
      },
      "playbookState": enum ([OutputState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.OutputState))
    }  
  
Fields  
---  
`playbook` |  `string` Required. The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
`displayName` |  `string` Output only. The display name of the playbook.  
`playbookInput` |  `object (`[PlaybookInput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookInput)`)` Optional. Input of the child playbook invocation.  
`playbookOutput` |  `object (`[PlaybookOutput](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.PlaybookOutput)`)` Optional. Output of the child playbook invocation.  
`playbookState` |  `enum (`[OutputState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.OutputState)`)` Required. Playbook invocation's output state.  
  
### OutputState

Output state.

Enums  
---  
`OUTPUT_STATE_UNSPECIFIED` | Unspecified output.  
`OUTPUT_STATE_OK` | Succeeded.  
`OUTPUT_STATE_CANCELLED` | Cancelled.  
`OUTPUT_STATE_FAILED` | Failed.  
`OUTPUT_STATE_ESCALATED` | Escalated.  
`OUTPUT_STATE_PENDING` | Pending.  
  
### FlowInvocation

Stores metadata of the invocation of a CX flow.

JSON representation  
---  
      
    
    {
      "flow": string,
      "displayName": string,
      "flowState": enum ([OutputState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.OutputState))
    }  
  
Fields  
---  
`flow` |  `string` Required. The unique identifier of the flow. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`.  
`displayName` |  `string` Output only. The display name of the flow.  
`flowState` |  `enum (`[OutputState](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples#Example.OutputState)`)` Required. Flow invocation's output state.  
  
### PlaybookTransition

Stores metadata of the transition to another target playbook. Playbook transition actions exit the caller playbook and enter the target playbook.

JSON representation  
---  
      
    
    {
      "playbook": string,
      "displayName": string
    }  
  
Fields  
---  
`playbook` |  `string` Required. The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
`displayName` |  `string` Output only. The display name of the playbook.  
  
### FlowTransition

Stores metadata of the transition to a target CX flow. Flow transition actions exit the caller playbook and enter the child flow.

JSON representation  
---  
      
    
    {
      "flow": string,
      "displayName": string
    }  
  
Fields  
---  
`flow` |  `string` Required. The unique identifier of the flow. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<Agentflows/<FlowID>`.  
`displayName` |  `string` Output only. The display name of the flow.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/create)`

|  Creates an example in the specified playbook.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/delete)`

|  Deletes the specified example.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/get)`

|  Retrieves the specified example.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/list)`

|  Returns a list of examples in the specified playbook.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks.examples/patch)`

|  Update the specified example.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
