---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks
title: REST Resource: projects.locations.agents.playbooks \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:14.433634+00:00
---

# REST Resource: projects.locations.agents.playbooks  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.playbooks Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Playbook
    * JSON representation
    * Instruction
      * JSON representation
    * Step
      * JSON representation
    * CodeBlock
      * JSON representation
    * Handler
      * JSON representation
    * EventHandler
      * JSON representation
    * LifecycleHandler
      * JSON representation
    * PlaybookType
  * Methods



## Resource: Playbook

Playbook is the basic building block to instruct the LLM how to execute a certain task.

A playbook consists of a goal to accomplish, an optional list of step by step instructions (the step instruction may refers to name of the custom or default plugin tools to use) to perform the task, a list of contextual input data to be passed in at the beginning of the invoked, and a list of output parameters to store the playbook result.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "goal": string,
      "inputParameterDefinitions": [
        {
          object ([ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition))
        }
      ],
      "outputParameterDefinitions": [
        {
          object ([ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition))
        }
      ],
      "instruction": {
        object ([Instruction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Instruction))
      },
      "tokenCount": string,
      "createTime": string,
      "updateTime": string,
      "referencedPlaybooks": [
        string
      ],
      "referencedFlows": [
        string
      ],
      "referencedTools": [
        string
      ],
      "inlineActions": [
        string
      ],
      "codeBlock": {
        object ([CodeBlock](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.CodeBlock))
      },
      "llmModelSettings": {
        object ([LlmModelSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/LlmModelSettings))
      },
      "handlers": [
        {
          object ([Handler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Handler))
        }
      ],
      "playbookType": enum ([PlaybookType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.PlaybookType))
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the playbook. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`.  
`displayName` |  `string` Required. The human-readable name of the playbook, unique within an agent.  
`goal` |  `string` Required. High level description of the goal the playbook intend to accomplish. A goal should be concise since it's visible to other playbooks that may reference this playbook.  
`inputParameterDefinitions[]` |  `object (`[ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition)`)` Optional. Defined structured input parameters for this playbook.  
`outputParameterDefinitions[]` |  `object (`[ParameterDefinition](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/ParameterDefinition)`)` Optional. Defined structured output parameters for this playbook.  
`instruction` |  `object (`[Instruction](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Instruction)`)` Instruction to accomplish target goal.  
`tokenCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. Estimated number of tokes current playbook takes when sent to the LLM.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of initial playbook creation.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last time the playbook version was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`referencedPlaybooks[]` |  `string` Output only. The resource name of other playbooks referenced by the current playbook in the instructions.  
`referencedFlows[]` |  `string` Output only. The resource name of flows referenced by the current playbook in the instructions.  
`referencedTools[]` |  `string` Optional. The resource name of tools referenced by the current playbook in the instructions. If not provided explicitly, they are will be implied using the tool being referenced in goal and steps.  
`inlineActions[]` |  `string` Optional. Output only. Names of inline actions scoped to this playbook. These actions are in addition to those belonging to referenced tools, child playbooks, and flows, e.g. actions that are defined in the playbook's code block.  
`codeBlock` |  `object (`[CodeBlock](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.CodeBlock)`)` Optional. The playbook's scoped code block, which may implement handlers and actions.  
`llmModelSettings` |  `object (`[LlmModelSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/LlmModelSettings)`)` Optional. Llm model settings for the playbook.  
`handlers[]` |  `object (`[Handler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Handler)`)` Optional. A list of registered handlers to execuate based on the specified triggers.  
`playbookType` |  `enum (`[PlaybookType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.PlaybookType)`)` Optional. Type of the playbook.  
  
### Instruction

Message of the Instruction of the playbook.

JSON representation  
---  
      
    
    {
      "guidelines": string,
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Step))
        }
      ]
    }  
  
Fields  
---  
`guidelines` |  `string` General guidelines for the playbook. These are unstructured instructions that are not directly part of the goal, e.g. "Always be polite". It's valid for this text to be long and used instead of steps altogether.  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Step)`)` Ordered list of step by step execution instructions to accomplish target goal.  
  
### Step

Message of single step execution.

JSON representation  
---  
      
    
    {
      "steps": [
        {
          object ([Step](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Step))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "text": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`steps[]` |  `object (`[Step](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.Step)`)` Sub-processing needed to execute the current step.  
Instruction on how to execute current step. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`text` |  `string` Step instruction in text format.  
End of mutually exclusive fields.  
  
### CodeBlock

Represents a code block.

JSON representation  
---  
      
    
    {
      "code": string
    }  
  
Fields  
---  
`code` |  `string` Optional. Source code of the block in Python.  
  
### Handler

Handler can be used to define custom logic to be executed based on the user-specified triggers.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "eventHandler": {
        object ([EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.EventHandler))
      },
      "lifecycleHandler": {
        object ([LifecycleHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.LifecycleHandler))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
Specifies the type of handler to invoke. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`eventHandler` |  `object (`[EventHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.EventHandler)`)` A handler triggered by event.  
`lifecycleHandler` |  `object (`[LifecycleHandler](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.LifecycleHandler)`)` A handler triggered during specific lifecycle of the playbook execution.  
End of mutually exclusive fields.  
  
### EventHandler

A handler that is triggered by the specified `[event](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.EventHandler.FIELDS.event)`.

JSON representation  
---  
      
    
    {
      "event": string,
      "condition": string,
      "fulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment))
      }
    }  
  
Fields  
---  
`event` |  `string` Required. The name of the event that triggers this handler.  
`condition` |  `string` Optional. The condition that must be satisfied to trigger this handler.  
`fulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment)`)` Required. The fulfillment to call when the event occurs.  
  
### LifecycleHandler

A handler that is triggered on the specific `[lifecycleStage](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks#Playbook.LifecycleHandler.FIELDS.lifecycle_stage)` of the playbook execution.

JSON representation  
---  
      
    
    {
      "lifecycleStage": string,
      "condition": string,
      "fulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment))
      }
    }  
  
Fields  
---  
`lifecycleStage` |  `string` Required. The name of the lifecycle stage that triggers this handler. Supported values: * `playbook-start` * `pre-action-selection` * `pre-action-execution`  
`condition` |  `string` Optional. The condition that must be satisfied to trigger this handler.  
`fulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment)`)` Required. The fulfillment to call when this handler is triggered.  
  
### PlaybookType

Type of the playbook.

Enums  
---  
`PLAYBOOK_TYPE_UNSPECIFIED` | Unspecified type. Default to TASK.  
`TASK` | Task playbook.  
`ROUTINE` | Routine playbook.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/create)`

|  Creates a playbook in a specified agent.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/delete)`

|  Deletes a specified playbook.  
  
### `[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/export)`

|  Exports the specified playbook to a binary file.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/get)`

|  Retrieves the specified Playbook.  
  
### `[import](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/import)`

|  Imports the specified playbook to the specified agent from a binary file.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/list)`

|  Returns a list of playbooks in the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.playbooks/patch)`

|  Updates the specified Playbook.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
