---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails
title: REST Resource: projects.locations.apps.guardrails \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:34.079530+00:00
---

# REST Resource: projects.locations.apps.guardrails  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.guardrails Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Guardrail
    * JSON representation
    * Guardrail.ContentFilter
      * JSON representation
    * Guardrail.ContentFilter.MatchType
    * Guardrail.LlmPromptSecurity
      * JSON representation
    * Guardrail.LlmPromptSecurity.DefaultSecuritySettings
      * JSON representation
    * Guardrail.LlmPolicy
      * JSON representation
    * Guardrail.LlmPolicy.PolicyScope
    * Guardrail.ModelSafety
      * JSON representation
    * Guardrail.ModelSafety.SafetySetting
      * JSON representation
    * Guardrail.ModelSafety.HarmCategory
    * Guardrail.ModelSafety.HarmBlockThreshold
    * Guardrail.CodeCallback
      * JSON representation
    * Guardrail.Supervisor
      * JSON representation
    * Guardrail.Supervisor.Type
    * Guardrail.Supervisor.DetectionMode
    * TriggerAction
      * JSON representation
    * TriggerAction.RespondImmediately
      * JSON representation
    * TriggerAction.Response
      * JSON representation
    * TriggerAction.TransferAgent
      * JSON representation
    * TriggerAction.GenerativeAnswer
      * JSON representation
  * Methods



## Resource: Guardrail

Guardrail contains a list of checks and balances to keep the agents safe and secure.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "enabled": boolean,
      "action": {
        object ([TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction))
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "contentFilter": {
        object ([Guardrail.ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ContentFilter))
      },
      "llmPromptSecurity": {
        object ([Guardrail.LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPromptSecurity))
      },
      "llmPolicy": {
        object ([Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPolicy))
      },
      "modelSafety": {
        object ([Guardrail.ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety))
      },
      "codeCallback": {
        object ([Guardrail.CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.CodeCallback))
      },
      "supervisor": {
        object ([Guardrail.Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.Supervisor))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the guardrail. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`displayName` |  `string` Required. Display name of the guardrail.  
`description` |  `string` Optional. Description of the guardrail.  
`enabled` |  `boolean` Optional. Whether the guardrail is enabled.  
`action` |  `object (`[TriggerAction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction)`)` Optional. Action to take when the guardrail is triggered.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the guardrail was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the guardrail was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
Guardrail type. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`contentFilter` |  `object (`[Guardrail.ContentFilter](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ContentFilter)`)` Optional. Guardrail that bans certain content from being used in the conversation.  
`llmPromptSecurity` |  `object (`[Guardrail.LlmPromptSecurity](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPromptSecurity)`)` Optional. Guardrail that blocks the conversation if the prompt is considered unsafe based on the LLM classification.  
`llmPolicy` |  `object (`[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPolicy)`)` Optional. Guardrail that blocks the conversation if the LLM response is considered violating the policy based on the LLM classification.  
`modelSafety` |  `object (`[Guardrail.ModelSafety](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety)`)` Optional. Guardrail that blocks the conversation if the LLM response is considered unsafe based on the model safety settings.  
`codeCallback` |  `object (`[Guardrail.CodeCallback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.CodeCallback)`)` Optional. Guardrail that potentially blocks the conversation based on the result of the callback execution.  
`supervisor` |  `object (`[Guardrail.Supervisor](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.Supervisor)`)` Optional. Guardrail that runs supervisor intervention.  
End of mutually exclusive fields.  
  
### Guardrail.ContentFilter

Guardrail that bans certain content from being used in the conversation.

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
      "matchType": enum ([Guardrail.ContentFilter.MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ContentFilter.MatchType)),
      "disregardDiacritics": boolean
    }  
  
Fields  
---  
`bannedContents[]` |  `string` Optional. List of banned phrases. Applies to both user inputs and agent responses.  
`bannedContentsInUserInput[]` |  `string` Optional. List of banned phrases. Applies only to user inputs.  
`bannedContentsInAgentResponse[]` |  `string` Optional. List of banned phrases. Applies only to agent responses.  
`matchType` |  `enum (`[Guardrail.ContentFilter.MatchType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ContentFilter.MatchType)`)` Required. Match type for the content filter.  
`disregardDiacritics` |  `boolean` Optional. If true, diacritics are ignored during matching.  
  
### Guardrail.ContentFilter.MatchType

Match type for the content filter.

Enums  
---  
`MATCH_TYPE_UNSPECIFIED` | Match type is not specified.  
`SIMPLE_STRING_MATCH` | Content is matched for substrings character by character.  
`WORD_BOUNDARY_STRING_MATCH` | Content only matches if the pattern found in the text is surrounded by word delimiters. Banned phrases can also contain word delimiters.  
`REGEXP_MATCH` | Content is matched using regular expression syntax.  
  
### Guardrail.LlmPromptSecurity

Guardrail that blocks the conversation if the input is considered unsafe based on the LLM classification.

JSON representation  
---  
      
    
    {
      "failOpen": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "defaultSettings": {
        object ([Guardrail.LlmPromptSecurity.DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPromptSecurity.DefaultSecuritySettings))
      },
      "customPolicy": {
        object ([Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPolicy))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`failOpen` |  `boolean` Optional. Determines the behavior when the guardrail encounters an LLM error. - If true: the guardrail is bypassed. - If false (default): the guardrail triggers/blocks.Note: If a custom policy is provided, this field is ignored in favor of the policy's 'failOpen' configuration.  
Defines the security configuration mode. The user must choose one of the following configurations. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`defaultSettings` |  `object (`[Guardrail.LlmPromptSecurity.DefaultSecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPromptSecurity.DefaultSecuritySettings)`)` Optional. Use the system's predefined default security settings. To select this mode, include an empty 'defaultSettings' message in the request. The 'defaultPromptTemplate' field within will be populated by the server in the response.  
`customPolicy` |  `object (`[Guardrail.LlmPolicy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPolicy)`)` Optional. Use a user-defined LlmPolicy to configure the security guardrail.  
End of mutually exclusive fields.  
  
### Guardrail.LlmPromptSecurity.DefaultSecuritySettings

Configuration for default system security settings.

JSON representation  
---  
      
    
    {
      "defaultPromptTemplate": string
    }  
  
Fields  
---  
`defaultPromptTemplate` |  `string` Output only. The default prompt template used by the system. This field is for display purposes to show the user what prompt the system uses by default. It is OUTPUT_ONLY.  
  
### Guardrail.LlmPolicy

Guardrail that blocks the conversation if the LLM response is considered violating the policy based on the LLM classification.

JSON representation  
---  
      
    
    {
      "maxConversationMessages": integer,
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ModelSettings))
      },
      "prompt": string,
      "policyScope": enum ([Guardrail.LlmPolicy.PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPolicy.PolicyScope)),
      "failOpen": boolean,
      "allowShortUtterance": boolean
    }  
  
Fields  
---  
`maxConversationMessages` |  `integer` Optional. When checking this policy, consider the last 'n' messages in the conversation. When not set a default value of 10 will be used.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ModelSettings)`)` Optional. Model settings.  
`prompt` |  `string` Required. Policy prompt.  
`policyScope` |  `enum (`[Guardrail.LlmPolicy.PolicyScope](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.LlmPolicy.PolicyScope)`)` Required. Defines when to apply the policy check during the conversation. If set to `POLICY_SCOPE_UNSPECIFIED`, the policy will be applied to the user input. When applying the policy to the agent response, additional latency will be introduced before the agent can respond.  
`failOpen` |  `boolean` Optional. If an error occurs during the policy check, fail open and do not trigger the guardrail.  
`allowShortUtterance` |  `boolean` Optional. By default, the LLM policy check is bypassed for short utterances. Enabling this setting applies the policy check to all utterances, including those that would normally be skipped.  
  
### Guardrail.LlmPolicy.PolicyScope

Defines when to apply the policy check during the conversation.

Enums  
---  
`POLICY_SCOPE_UNSPECIFIED` | Policy scope is not specified.  
`USER_QUERY` | Policy check is triggered on user input.  
`AGENT_RESPONSE` | Policy check is triggered on agent response. Applying this policy scope will introduce additional latency before the agent can respond.  
`USER_QUERY_AND_AGENT_RESPONSE` | Policy check is triggered on both user input and agent response. Applying this policy scope will introduce additional latency before the agent can respond.  
  
### Guardrail.ModelSafety

Model safety settings overrides. When this is set, it will override the default settings and trigger the guardrail if the response is considered unsafe.

JSON representation  
---  
      
    
    {
      "safetySettings": [
        {
          object ([Guardrail.ModelSafety.SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety.SafetySetting))
        }
      ]
    }  
  
Fields  
---  
`safetySettings[]` |  `object (`[Guardrail.ModelSafety.SafetySetting](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety.SafetySetting)`)` Required. List of safety settings.  
  
### Guardrail.ModelSafety.SafetySetting

Safety setting.

JSON representation  
---  
      
    
    {
      "category": enum ([Guardrail.ModelSafety.HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety.HarmCategory)),
      "threshold": enum ([Guardrail.ModelSafety.HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety.HarmBlockThreshold))
    }  
  
Fields  
---  
`category` |  `enum (`[Guardrail.ModelSafety.HarmCategory](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety.HarmCategory)`)` Required. The harm category.  
`threshold` |  `enum (`[Guardrail.ModelSafety.HarmBlockThreshold](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.ModelSafety.HarmBlockThreshold)`)` Required. The harm block threshold.  
  
### Guardrail.ModelSafety.HarmCategory

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
  
### Guardrail.ModelSafety.HarmBlockThreshold

Probability based thresholds levels for blocking.

Enums  
---  
`HARM_BLOCK_THRESHOLD_UNSPECIFIED` | Unspecified harm block threshold.  
`BLOCK_LOW_AND_ABOVE` | Block low threshold and above (i.e. block more).  
`BLOCK_MEDIUM_AND_ABOVE` | Block medium threshold and above.  
`BLOCK_ONLY_HIGH` | Block only high threshold (i.e. block less).  
`BLOCK_NONE` | Block none.  
`OFF` | Turn off the safety filter.  
  
### Guardrail.CodeCallback

Guardrail that blocks the conversation based on the code callbacks provided.

JSON representation  
---  
      
    
    {
      "beforeAgentCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback))
      },
      "afterAgentCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback))
      },
      "beforeModelCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback))
      },
      "afterModelCallback": {
        object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback))
      }
    }  
  
Fields  
---  
`beforeAgentCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback)`)` Optional. The callback to execute before the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`afterAgentCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback)`)` Optional. The callback to execute after the agent is called. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`beforeModelCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback)`)` Optional. The callback to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
`afterModelCallback` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Callback)`)` Optional. The callback to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. Each callback function is expected to return a structure (e.g., a dict or object) containing at least: - 'decision': Either 'OK' or 'TRIGGER'. - 'reason': A string explaining the decision. A 'TRIGGER' decision may halt further processing.  
  
### Guardrail.Supervisor

Guardrail that runs supervisor intervention.

JSON representation  
---  
      
    
    {
      "type": enum ([Guardrail.Supervisor.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.Supervisor.Type)),
      "detectionMode": enum ([Guardrail.Supervisor.DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.Supervisor.DetectionMode))
    }  
  
Fields  
---  
`type` |  `enum (`[Guardrail.Supervisor.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.Supervisor.Type)`)` Optional. The type of the supervisor.  
`detectionMode` |  `enum (`[Guardrail.Supervisor.DetectionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.Guardrail.Supervisor.DetectionMode)`)` Optional. The detection mode of the supervisor.  
  
### Guardrail.Supervisor.Type

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
  
### Guardrail.Supervisor.DetectionMode

Detection mode of the supervisor.

Enums  
---  
`DETECTION_MODE_UNSPECIFIED` | Detection mode is unspecified. Default to NON_BLOCKING.  
`NON_BLOCKING` | Non blocking detection mode. Response is not blocked when the supervisor detection is ongoing.  
`BLOCKING` | Blocking detection mode. Response is blocked when the supervisor detection is ongoing.  
  
### TriggerAction

Action that is taken when a certain precondition is met.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "respondImmediately": {
        object ([TriggerAction.RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.RespondImmediately))
      },
      "transferAgent": {
        object ([TriggerAction.TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.TransferAgent))
      },
      "generativeAnswer": {
        object ([TriggerAction.GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.GenerativeAnswer))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The action to take. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`respondImmediately` |  `object (`[TriggerAction.RespondImmediately](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.RespondImmediately)`)` Optional. Immediately respond with a preconfigured response.  
`transferAgent` |  `object (`[TriggerAction.TransferAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.TransferAgent)`)` Optional. Transfer the conversation to a different agent.  
`generativeAnswer` |  `object (`[TriggerAction.GenerativeAnswer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.GenerativeAnswer)`)` Optional. Respond with a generative answer.  
End of mutually exclusive fields.  
  
### TriggerAction.RespondImmediately

The agent will immediately respond with a preconfigured response.

JSON representation  
---  
      
    
    {
      "responses": [
        {
          object ([TriggerAction.Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.Response))
        }
      ]
    }  
  
Fields  
---  
`responses[]` |  `object (`[TriggerAction.Response](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails#Guardrail.TriggerAction.Response)`)` Required. The canned responses for the agent to choose from. The response is chosen randomly.  
  
### TriggerAction.Response

Represents a response from the agent.

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
  
### TriggerAction.TransferAgent

The agent will transfer the conversation to a different agent.

JSON representation  
---  
      
    
    {
      "agent": string
    }  
  
Fields  
---  
`agent` |  `string` Required. The name of the agent to transfer the conversation to. The agent must be in the same app as the current agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
  
### TriggerAction.GenerativeAnswer

The agent will immediately respond with a generative answer.

JSON representation  
---  
      
    
    {
      "prompt": string
    }  
  
Fields  
---  
`prompt` |  `string` Required. The prompt to use for the generative answer.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/create)`

|  Creates a new guardrail in the given app.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/delete)`

|  Deletes the specified guardrail.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/get)`

|  Gets details of the specified guardrail.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/list)`

|  Lists guardrails in the given app.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.guardrails/patch)`

|  Updates the specified guardrail.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
