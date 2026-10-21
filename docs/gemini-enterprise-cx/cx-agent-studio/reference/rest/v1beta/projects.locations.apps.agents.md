---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents
title: REST Resource: projects.locations.apps.agents \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:44.292417+00:00
---

# REST Resource: projects.locations.apps.agents  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.agents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Agent
    * JSON representation
    * Agent.LlmAgent
    * Agent.RemoteDialogflowAgent
      * JSON representation
    * Agent.RemoteA2aAgent
      * JSON representation
    * RemoteA2aConfig
      * JSON representation
    * Agent.AgentToolset
      * JSON representation
    * TransferRule
      * JSON representation
    * TransferRule.DeterministicTransfer
      * JSON representation
    * ExpressionCondition
      * JSON representation
    * PythonCodeCondition
      * JSON representation
    * TransferRule.DisablePlannerTransfer
      * JSON representation
    * TransferRule.Direction
  * Methods



## Resource: Agent

An agent acts as the fundamental building block that provides instructions to the Large Language Model (LLM) for executing specific tasks.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings))
      },
      "instruction": string,
      "tools": [
        string
      ],
      "childAgents": [
        string
      ],
      "beforeAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback))
        }
      ],
      "afterAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback))
        }
      ],
      "beforeModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback))
        }
      ],
      "afterModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback))
        }
      ],
      "beforeToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback))
        }
      ],
      "afterToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "guardrails": [
        string
      ],
      "etag": string,
      "toolsets": [
        {
          object ([Agent.AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.AgentToolset))
        }
      ],
      "generatedSummary": string,
      "transferRules": [
        {
          object ([TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule))
        }
      ],
      "validationErrors": [
        string
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "llmAgent": {
        object ([Agent.LlmAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.LlmAgent))
      },
      "remoteDialogflowAgent": {
        object ([Agent.RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.RemoteDialogflowAgent))
      },
      "remoteA2aAgent": {
        object ([Agent.RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.RemoteA2aAgent))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Required. Display name of the agent.  
`description` |  `string` Optional. Human-readable description of the agent.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ModelSettings)`)` Optional. Configurations for the LLM model.  
`instruction` |  `string` Optional. Instructions for the LLM model to guide the agent's behavior.  
`tools[]` |  `string` Optional. List of available tools for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`childAgents[]` |  `string` Optional. List of child agents in the agent tree. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`beforeAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback)`)` Optional. The callbacks to execute before the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback)`)` Optional. The callbacks to execute after the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback)`)` Optional. The callbacks to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback)`)` Optional. The callbacks to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback)`)` Optional. The callbacks to execute before the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/Callback)`)` Optional. The callbacks to execute after the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`guardrails[]` |  `string` Optional. List of guardrails for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`toolsets[]` |  `object (`[Agent.AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.AgentToolset)`)` Optional. List of toolsets for the agent.  
`generatedSummary` |  `string` Output only. If the agent is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`transferRules[]` |  `object (`[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule)`)` Optional. Agent transfer rules. If multiple rules match, the first one in the list will be used.  
`validationErrors[]` |  `string` Output only. Misconfigurations or errors in the agent that may affect agent quality.  
The type of agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`llmAgent` |  `object (`[Agent.LlmAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.LlmAgent)`)` Optional. The default agent type.  
`remoteDialogflowAgent` |  `object (`[Agent.RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.RemoteDialogflowAgent)`)` Optional. The remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent to be used for the agent execution. If this field is set, all other agent level properties will be ignored.Note: If the Dialogflow agent is in a different project from the app, you should grant `roles/dialogflow.client` to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`remoteA2aAgent` |  `object (`[Agent.RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.Agent.RemoteA2aAgent)`)` Optional. The remote [A2A](https://github.com/a2aproject/A2A) agent to be used for the agent execution.  
End of mutually exclusive fields.  
  
### Agent.LlmAgent

This type has no fields.

Default agent type. The agent uses instructions and callbacks specified in the agent to perform the task using a large language model.

### Agent.RemoteDialogflowAgent

The agent which will transfer execution to a remote [Dialogflow CX](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent. The Dialogflow agent will process subsequent user queries until the session ends or flow ends, and the control is transferred back to the parent CES agent.

JSON representation  
---  
      
    
    {
      "agent": string,
      "flowId": string,
      "environmentId": string,
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      },
      "respectResponseInterruptionSettings": boolean,
      "languageCodeVariable": string
    }  
  
Fields  
---  
`agent` |  `string` Required. The [Dialogflow](https://docs.cloud.google.com/dialogflow/cx/docs/concept/agent) agent resource name. Format: `projects/{project}/locations/{location}/agents/{agent}`  
`flowId` |  `string` Optional. The flow ID of the flow in the Dialogflow agent.  
`environmentId` |  `string` Optional. The environment ID of the Dialogflow agent to be used for the agent execution. If not specified, the draft environment will be used.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. The mapping of the app variables names to the Dialogflow session parameters names to be sent to the Dialogflow agent as input.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. The mapping of the Dialogflow session parameters names to the app variables names to be sent back to the CES agent after the Dialogflow agent execution ends.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`respectResponseInterruptionSettings` |  `boolean` Optional. Indicates whether to respect the message-level interruption settings configured in the Dialogflow agent.

  * If false: all response messages from the Dialogflow agent follow the app-level barge-in settings.
  * If true: only response messages with [`allow_playback_interruption`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rpc/google.cloud.dialogflow.cx.v3#text) set to true will be interruptable, all other messages follow the app-level barge-in settings.

  
`languageCodeVariable` |  `string` Optional. The name of the variable that contains the language code to be used for the Dialogflow session. If unspecified, the default language code of the Dialogflow agent will be used.  
  
### Agent.RemoteA2aAgent

The agent which will transfer execution to a remote [A2A](https://github.com/a2aproject/A2A) agent.

JSON representation  
---  
      
    
    {
      "a2aConfig": {
        object ([RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.RemoteA2aConfig))
      }
    }  
  
Fields  
---  
`a2aConfig` |  `object (`[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.RemoteA2aConfig)`)` Required. The A2A connection configuration.  
  
### RemoteA2aConfig

Shared configuration for connecting to a remote [A2A](https://github.com/a2aproject/A2A) agent.

JSON representation  
---  
      
    
    {
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication))
      },
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      },
      "streamingEnabled": boolean,
      "contextId": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentCard))
      },
      "agentRegistry": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent. Optional if the registry reference already handles authentication.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`streamingEnabled` |  `boolean` Optional. Whether streaming is enabled for the remote agent.  
`contextId` |  `string` Optional. If not empty, interactions with the remote A2A agent will use this context ID. This contextId field can refer to a session variable like `$context.variables.order_agent_session_id`.  
Specification of the remote agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/AgentCard)`)` Optional. The full agent card defined inline.  
`agentRegistry` |  `string` Optional. Reference to the agent in the Agent Registry. Format: `projects/{project}/locations/{location}/agents/{agent}`  
End of mutually exclusive fields.  
  
### Agent.AgentToolset

A toolset with a selection of its tools.

JSON representation  
---  
      
    
    {
      "toolset": string,
      "toolIds": [
        string
      ]
    }  
  
Fields  
---  
`toolset` |  `string` Required. The resource name of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`toolIds[]` |  `string` Optional. The tools IDs to filter the toolset.  
  
### TransferRule

Rule for transferring to a specific agent.

JSON representation  
---  
      
    
    {
      "childAgent": string,
      "direction": enum ([TransferRule.Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule.Direction)),
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "deterministicTransfer": {
        object ([TransferRule.DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule.DeterministicTransfer))
      },
      "disablePlannerTransfer": {
        object ([TransferRule.DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule.DisablePlannerTransfer))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`childAgent` |  `string` Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`direction` |  `enum (`[TransferRule.Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule.Direction)`)` Required. The direction of the transfer.  
The rule type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`deterministicTransfer` |  `object (`[TransferRule.DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule.DeterministicTransfer)`)` Optional. A rule that immediately transfers to the target agent when the condition is met.  
`disablePlannerTransfer` |  `object (`[TransferRule.DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.TransferRule.DisablePlannerTransfer)`)` Optional. Rule that prevents the planner from transferring to the target agent.  
End of mutually exclusive fields.  
  
### TransferRule.DeterministicTransfer

Deterministic transfer rule. When the condition evaluates to true, the transfer occurs.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.ExpressionCondition))
      },
      "pythonCodeCondition": {
        object ([PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.PythonCodeCondition))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The condition to evaluate. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.ExpressionCondition)`)` Optional. A rule that evaluates a session state condition. If the condition evaluates to true, the transfer occurs.  
`pythonCodeCondition` |  `object (`[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.PythonCodeCondition)`)` Optional. A rule that uses Python code block to evaluate the conditions. If the condition evaluates to true, the transfer occurs.  
End of mutually exclusive fields.  
  
### ExpressionCondition

Expression condition based on session state.

JSON representation  
---  
      
    
    {
      "expression": string
    }  
  
Fields  
---  
`expression` |  `string` Required. The string representation of cloud.api.Expression condition.  
  
### PythonCodeCondition

Python code block to evaluate the condition.

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. The python code to execute.  
  
### TransferRule.DisablePlannerTransfer

A rule that prevents the planner from transferring to the target agent.

JSON representation  
---  
      
    
    {
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.ExpressionCondition))
      }
    }  
  
Fields  
---  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents#Agent.ExpressionCondition)`)` Required. If the condition evaluates to true, planner will not be allowed to transfer to the target agent.  
  
### TransferRule.Direction

The direction of the transfer.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified direction.  
`PARENT_TO_CHILD` | Transfer from the parent agent to the child agent.  
`CHILD_TO_PARENT` | Transfer from the child agent to the parent agent.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents/create)`

|  Creates a new agent in the given app.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents/delete)`

|  Deletes the specified agent.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents/get)`

|  Gets details of the specified agent.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents/list)`

|  Lists agents in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/projects.locations.apps.agents/patch)`

|  Updates the specified agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
