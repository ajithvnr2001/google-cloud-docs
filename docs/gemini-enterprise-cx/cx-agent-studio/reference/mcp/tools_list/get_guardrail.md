---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_guardrail/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T15:04:15.493780+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/get_guardrail/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `get_guardrail`

Gets details of the specified guardrail.

The following code sample shows how to use `curl` to call the `get_guardrail` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "get_guardrail",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `AgentService.GetGuardrail`.

### GetGuardrailRequest

JSON representation  
---  
      
    
    {
      "name": string
    }  
  
Fields  
---  
`name` |  `string` Required. The resource name of the guardrail to retrieve.  
  
## Output Schema

Guardrail contains a list of checks and balances to keep the agents safe and secure.

### Guardrail

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "enabled": boolean,
      "action": {
        object ([TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.TriggerAction))
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
    
      // Union field guardrail_type can be only one of the following:
      "contentFilter": {
        object ([ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.ContentFilter))
      },
      "llmPromptSecurity": {
        object ([LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.LlmPromptSecurity))
      },
      "llmPolicy": {
        object ([LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.LlmPolicy))
      },
      "modelSafety": {
        object ([ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.ModelSafety))
      },
      "codeCallback": {
        object ([CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.CodeCallback))
      },
      "supervisor": {
        object ([Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Supervisor))
      }
      // End of list of possible types for union field guardrail_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the guardrail. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`displayName` |  `string` Required. Display name of the guardrail.  
`description` |  `string` Optional. Description of the guardrail.  
`enabled` |  `boolean` Optional. Whether the guardrail is enabled.  
`action` |  `object (`[TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.TriggerAction)`)` Optional. Action to take when the guardrail is triggered.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the guardrail was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the guardrail was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
Union field `guardrail_type`. Guardrail type. `guardrail_type` can be only one of the following:  
`contentFilter` |  `object (`[ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.ContentFilter)`)` Optional. Guardrail that bans certain content from being used in the conversation.  
`llmPromptSecurity` |  `object (`[LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.LlmPromptSecurity)`)` Optional. Guardrail that blocks the conversation if the prompt is considered unsafe based on the LLM classification.  
`llmPolicy` |  `object (`[LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.LlmPolicy)`)` Optional. Guardrail that blocks the conversation if the LLM response is considered violating the policy based on the LLM classification.  
`modelSafety` |  `object (`[ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.ModelSafety)`)` Optional. Guardrail that blocks the conversation if the LLM response is considered unsafe based on the model safety settings.  
`codeCallback` |  `object (`[CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.CodeCallback)`)` Optional. Guardrail that potentially blocks the conversation based on the result of the callback execution.  
`supervisor` |  `object (`[Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Supervisor)`)` Optional. Guardrail that runs supervisor intervention.  
  
### ContentFilter

JSON representation  
---  
      
    
    {
      "bannedContents": [
        string
      ],
      "bannedContentsInUserInput": [
        string
      ],
      "bannedContentsInAgentResponse": [
        string
      ],
      "matchType": enum ([MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.MatchType)),
      "disregardDiacritics": boolean
    }  
  
Fields  
---  
`bannedContents[]` |  `string` Optional. List of banned phrases. Applies to both user inputs and agent responses.  
`bannedContentsInUserInput[]` |  `string` Optional. List of banned phrases. Applies only to user inputs.  
`bannedContentsInAgentResponse[]` |  `string` Optional. List of banned phrases. Applies only to agent responses.  
`matchType` |  `enum (`[MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.MatchType)`)` Required. Match type for the content filter.  
`disregardDiacritics` |  `boolean` Optional. If true, diacritics are ignored during matching.  
  
### LlmPromptSecurity

JSON representation  
---  
      
    
    {
      "failOpen": boolean,
    
      // Union field security_config can be only one of the following:
      "defaultSettings": {
        object ([DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.DefaultSecuritySettings))
      },
      "customPolicy": {
        object ([LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.LlmPolicy))
      }
      // End of list of possible types for union field security_config.
    }  
  
Fields  
---  
`failOpen` |  `boolean` Optional. Determines the behavior when the guardrail encounters an LLM error. - If true: the guardrail is bypassed. - If false (default): the guardrail triggers/blocks.Note: If a custom policy is provided, this field is ignored in favor of the policy's 'fail_open' configuration.  
Union field `security_config`. Defines the security configuration mode. The user must choose one of the following configurations. `security_config` can be only one of the following:  
`defaultSettings` |  `object (`[DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.DefaultSecuritySettings)`)` Optional. Use the system's predefined default security settings. To select this mode, include an empty 'default_settings' message in the request. The 'default_prompt_template' field within will be populated by the server in the response.  
`customPolicy` |  `object (`[LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.LlmPolicy)`)` Optional. Use a user-defined LlmPolicy to configure the security guardrail.  
  
### DefaultSecuritySettings

JSON representation  
---  
      
    
    {
      "defaultPromptTemplate": string
    }  
  
Fields  
---  
`defaultPromptTemplate` |  `string` Output only. The default prompt template used by the system. This field is for display purposes to show the user what prompt the system uses by default. It is OUTPUT_ONLY.  
  
### LlmPolicy

JSON representation  
---  
      
    
    {
      "maxConversationMessages": integer,
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "policyScope": enum ([PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.PolicyScope)),
      "failOpen": boolean,
      "allowShortUtterance": boolean
    }  
  
Fields  
---  
`maxConversationMessages` |  `integer` Optional. When checking this policy, consider the last 'n' messages in the conversation. When not set a default value of 10 will be used.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Model settings.  
`prompt` |  `string` Required. Policy prompt.  
`policyScope` |  `enum (`[PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.PolicyScope)`)` Required. Defines when to apply the policy check during the conversation. If set to `POLICY_SCOPE_UNSPECIFIED`, the policy will be applied to the user input. When applying the policy to the agent response, additional latency will be introduced before the agent can respond.  
`failOpen` |  `boolean` Optional. If an error occurs during the policy check, fail open and do not trigger the guardrail.  
`allowShortUtterance` |  `boolean` Optional. By default, the LLM policy check is bypassed for short utterances. Enabling this setting applies the policy check to all utterances, including those that would normally be skipped.  
  
### ModelSettings

JSON representation  
---  
      
    
    {
      "model": string,
      "thinkingLevel": enum ([ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)),
    
      // Union field _temperature can be only one of the following:
      "temperature": number
      // End of list of possible types for union field _temperature.
    }  
  
Fields  
---  
`model` |  `string` Optional. The LLM model that the agent should use. If not set, the agent will inherit the model from its parent agent.  
`thinkingLevel` |  `enum (`[ThinkingLevel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ThinkingLevel)`)` Optional. The thinking level of the model.  
Union field `_temperature`.`_temperature` can be only one of the following:  
`temperature` |  `number` Optional. If set, this temperature will be used for the LLM model. Temperature controls the randomness of the model's responses. Lower temperatures produce responses that are more predictable. Higher temperatures produce responses that are more creative.  
  
### ModelSafety

JSON representation  
---  
      
    
    {
      "safetySettings": [
        {
          object ([SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.SafetySetting))
        }
      ]
    }  
  
Fields  
---  
`safetySettings[]` |  `object (`[SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.SafetySetting)`)` Required. List of safety settings.  
  
### SafetySetting

JSON representation  
---  
      
    
    {
      "category": enum ([HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.HarmCategory)),
      "threshold": enum ([HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.HarmBlockThreshold))
    }  
  
Fields  
---  
`category` |  `enum (`[HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.HarmCategory)`)` Required. The harm category.  
`threshold` |  `enum (`[HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.HarmBlockThreshold)`)` Required. The harm block threshold.  
  
### CodeCallback

JSON representation  
---  
      
    
    {
      "beforeAgentCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
      },
      "afterAgentCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
      },
      "beforeModelCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
      },
      "afterModelCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
      }
    }  
  
Fields  
---  
`beforeAgentCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callback to execute before the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`afterAgentCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callback to execute after the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`beforeModelCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callback to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`afterModelCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callback to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
  
### Callback

JSON representation  
---  
      
    
    {
      "description": string,
      "disabled": boolean,
      "proactiveExecutionEnabled": boolean,
    
      // Union field callback can be only one of the following:
      "pythonCode": string
      // End of list of possible types for union field callback.
    }  
  
Fields  
---  
`description` |  `string` Optional. Human-readable description of the callback.  
`disabled` |  `boolean` Optional. Whether the callback is disabled. Disabled callbacks are ignored by the agent.  
`proactiveExecutionEnabled` |  `boolean` Optional. If enabled, the callback will also be executed on intermediate model outputs. This setting only affects after model callback. **ENABLE WITH CAUTION**. Typically after model callback only needs to be executed after receiving all model responses. Enabling proactive execution may have negative implication on the execution cost and latency, and should only be enabled in rare situations.  
Union field `callback`. The callback to execute. `callback` can be only one of the following:  
`pythonCode` |  `string` Required. The python code to execute for the callback.  
  
### Supervisor

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Type)),
      "detectionMode": enum ([DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.DetectionMode))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Type)`)` Optional. The type of the supervisor.  
`detectionMode` |  `enum (`[DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.DetectionMode)`)` Optional. The detection mode of the supervisor.  
  
### TriggerAction

JSON representation  
---  
      
    
    {
    
      // Union field action can be only one of the following:
      "respondImmediately": {
        object ([RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.RespondImmediately))
      },
      "transferAgent": {
        object ([TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.TransferAgent))
      },
      "generativeAnswer": {
        object ([GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.GenerativeAnswer))
      }
      // End of list of possible types for union field action.
    }  
  
Fields  
---  
Union field `action`. The action to take. `action` can be only one of the following:  
`respondImmediately` |  `object (`[RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.RespondImmediately)`)` Optional. Immediately respond with a preconfigured response.  
`transferAgent` |  `object (`[TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.TransferAgent)`)` Optional. Transfer the conversation to a different agent.  
`generativeAnswer` |  `object (`[GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.GenerativeAnswer)`)` Optional. Respond with a generative answer.  
  
### RespondImmediately

JSON representation  
---  
      
    
    {
      "responses": [
        {
          object ([Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Response))
        }
      ]
    }  
  
Fields  
---  
`responses[]` |  `object (`[Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Response)`)` Required. The canned responses for the agent to choose from. The response is chosen randomly.  
  
### Response

JSON representation  
---  
      
    
    {
      "text": string,
      "disabled": boolean
    }  
  
Fields  
---  
`text` |  `string` Required. Text for the agent to respond with.  
`disabled` |  `boolean` Optional. Whether the response is disabled. Disabled responses are not used by the agent.  
  
### TransferAgent

JSON representation  
---  
      
    
    {
      "agent": string
    }  
  
Fields  
---  
`agent` |  `string` Required. The name of the agent to transfer the conversation to. The agent must be in the same app as the current agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
  
### GenerativeAnswer

JSON representation  
---  
      
    
    {
      "prompt": string
    }  
  
Fields  
---  
`prompt` |  `string` Required. The prompt to use for the generative answer.  
  
### Timestamp

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Represents seconds of UTC time since Unix epoch 1970-01-01T00:00:00Z. Must be between -62135596800 and 253402300799 inclusive (which corresponds to 0001-01-01T00:00:00Z to 9999-12-31T23:59:59Z).  
`nanos` |  `integer` Non-negative fractions of a second at nanosecond resolution. This field is the nanosecond portion of the duration, not an alternative to seconds. Negative second values with fractions must still have non-negative nanos values that count forward in time. Must be between 0 and 999,999,999 inclusive.  
  
### MatchType

Match type for the content filter.

Enums  
---  
`MATCH_TYPE_UNSPECIFIED` | Match type is not specified.  
`SIMPLE_STRING_MATCH` | Content is matched for substrings character by character.  
`WORD_BOUNDARY_STRING_MATCH` | Content only matches if the pattern found in the text is surrounded by word delimiters. Banned phrases can also contain word delimiters.  
`REGEXP_MATCH` | Content is matched using regular expression syntax.  
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### PolicyScope

Defines when to apply the policy check during the conversation.

Enums  
---  
`POLICY_SCOPE_UNSPECIFIED` | Policy scope is not specified.  
`USER_QUERY` | Policy check is triggered on user input.  
`AGENT_RESPONSE` | Policy check is triggered on agent response. Applying this policy scope will introduce additional latency before the agent can respond.  
`USER_QUERY_AND_AGENT_RESPONSE` | Policy check is triggered on both user input and agent response. Applying this policy scope will introduce additional latency before the agent can respond.  
  
### HarmCategory

Harm category.

Enums  
---  
`HARM_CATEGORY_UNSPECIFIED` | The harm category is unspecified.  
`HARM_CATEGORY_HATE_SPEECH` | The harm category is hate speech.  
`HARM_CATEGORY_DANGEROUS_CONTENT` | The harm category is dangerous content.  
`HARM_CATEGORY_HARASSMENT` | The harm category is harassment.  
`HARM_CATEGORY_SEXUALLY_EXPLICIT` | The harm category is sexually explicit content.  
`HARM_CATEGORY_PROFANITY` | The harm category is profanity.  
`HARM_CATEGORY_TOXIC` | The harm category is toxic.  
  
### HarmBlockThreshold

Probability based thresholds levels for blocking.

Enums  
---  
`HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Unspecified harm block threshold.  
`BLOCK_LOW_AND_ABOVE` | Block low threshold and above (i.e. block more).  
`BLOCK_MEDIUM_AND_ABOVE` | Block medium threshold and above.  
`BLOCK_ONLY_HIGH` | Block only high threshold (i.e. block less).  
`BLOCK_NONE` | Block none.  
`OFF` | Turn off the safety filter.  
  
### Type

Type of supervisor.

Enums  
---  
`TYPE_UNSPECIFIED` | Type is unspecified.  
`INVALID_TEXT` | Invalid text issue type.  
`LANGUAGE_SHIFT` | Language shift issue type.  
`SPEAKER_SHIFT` | Speaker shift issue type.  
`AUDIO_MISMATCH` | Audio mismatch issue type.  
`MISSING_TOOL_CALL` | Missing tool call issue type.  
`CUSTOM` | Custom issue type.  
`CHOPPY_AUDIO` | Choppy audio issue type.  
`PROFANITY` | Agent profanity issue type.  
  
### DetectionMode

Detection mode of the supervisor.

Enums  
---  
`DETECTION_MODE_UNSPECIFIED` | Detection mode is unspecified. Default to NON_BLOCKING.  
`NON_BLOCKING` | Non blocking detection mode. Response is not blocked when the supervisor detection is ongoing.  
`BLOCKING` | Blocking detection mode. Response is blocked when the supervisor detection is ongoing.  
  
### Tool Annotations

[Tool annotations](https://modelcontextprotocol.io/specification/latest/schema#toolannotations) are sent to MCP clients to describe the basic risk of a given tool. Most clients treat these hints as untrusted, but they can be used to decide when a confirmation prompt might be sent to a user. 

Along with the title string, the following boolean hints are defined as follows: 

  * `readOnlyHint`: If true, the tool doesn't modify its environment. Default: false.
  * `destructiveHint`: If true, then the tool can perform destructive actions. If false, then the tool can only perform additive actions. Default: true.
  * `idempotentHint`: If true, then calling the tool repeatedly with the same arguments will have no additional effect on its environment. Default: false.
  * `openWorldHint`: If true, then the tool can interact with an 'open world' of external entities. If false, then the tool can only interact with internal entities. For example, a web search tool would be open world, while a memory tool would not be open world.



Destructive Hint: ❌ | Idempotent Hint: ✅ | Read Only Hint: ✅ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
