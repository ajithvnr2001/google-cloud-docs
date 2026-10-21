---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app_version/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:11:01.666445+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/create_app_version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `create_app_version`

Creates a new app version in the given app.

The following code sample shows how to use `curl` to call the `create_app_version` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "create_app_version",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `AgentService.CreateAppVersion`

### CreateAppVersionRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "appVersionId": string,
      "appVersion": {
        object ([AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AppVersion))
      }
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the app to create an app version in.  
`appVersionId` |  `string` Optional. The ID to use for the app version, which will become the final component of the app version's resource name. If not provided, a unique ID will be automatically assigned for the app version.  
`appVersion` |  `object (`[AppVersion](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AppVersion)`)` Required. The app version to create.  
  
### AppVersion

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "creator": string,
      "createTime": string,
      "updateTime": string,
      "snapshot": {
        object ([AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AppSnapshot))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the app version. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`displayName` |  `string` Optional. The display name of the app version.  
`description` |  `string` Optional. The description of the app version.  
`creator` |  `string` Output only. Email of the user who created the app version.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app version was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app version was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`snapshot` |  `object (`[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AppSnapshot)`)` Output only. The snapshot of the app when the version is created.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
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
  
### AppSnapshot

JSON representation  
---  
      
    
    {
      "app": {
        object ([App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.App))
      },
      "agents": [
        {
          object ([Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Agent))
        }
      ],
      "tools": [
        {
          object ([Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Tool))
        }
      ],
      "examples": [
        {
          object ([Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Example))
        }
      ],
      "guardrails": [
        {
          object ([Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Guardrail))
        }
      ],
      "toolsets": [
        {
          object ([Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.Toolset))
        }
      ]
    }  
  
Fields  
---  
`app` |  `object (`[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.App)`)` Optional. The basic settings for the app.  
`agents[]` |  `object (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Agent)`)` Optional. List of agents in the app.  
`tools[]` |  `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Tool)`)` Optional. List of tools in the app.  
`examples[]` |  `object (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Example)`)` Optional. List of examples in the app.  
`guardrails[]` |  `object (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Guardrail)`)` Optional. List of guardrails in the app.  
`toolsets[]` |  `object (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.Toolset)`)` Optional. List of toolsets in the app.  
  
### App

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "pinned": boolean,
      "rootAgent": string,
      "languageSettings": {
        object ([LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LanguageSettings))
      },
      "timeZoneSettings": {
        object ([TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TimeZoneSettings))
      },
      "audioProcessingConfig": {
        object ([AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioProcessingConfig))
      },
      "loggingSettings": {
        object ([LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LoggingSettings))
      },
      "errorHandlingSettings": {
        object ([ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingSettings))
      },
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "toolExecutionMode": enum ([ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolExecutionMode)),
      "evaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EvaluationMetricsThresholds))
      },
      "variableDeclarations": [
        {
          object ([VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration))
        }
      ],
      "predefinedVariableDeclarations": [
        {
          object ([VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration))
        }
      ],
      "globalInstruction": string,
      "guardrails": [
        string
      ],
      "dataStoreSettings": {
        object ([DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DataStoreSettings))
      },
      "defaultChannelProfile": {
        object ([ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile))
      },
      "metadata": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "deploymentCount": integer,
      "clientCertificateSettings": {
        object ([ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ClientCertificateSettings))
      },
      "vpcScSettings": {
        object ([VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VpcScSettings))
      },
      "locked": boolean,
      "validationErrors": [
        string
      ],
      "dashboardSettings": {
        object ([DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DashboardSettings))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`displayName` |  `string` Required. Display name of the app.  
`description` |  `string` Optional. Human-readable description of the app.  
`pinned` |  `boolean` Optional. Whether the app is pinned in the app list.  
`rootAgent` |  `string` Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`languageSettings` |  `object (`[LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LanguageSettings)`)` Optional. Language settings of the app.  
`timeZoneSettings` |  `object (`[TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TimeZoneSettings)`)` Optional. TimeZone settings of the app.  
`audioProcessingConfig` |  `object (`[AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioProcessingConfig)`)` Optional. Audio processing configuration of the app.  
`loggingSettings` |  `object (`[LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LoggingSettings)`)` Optional. Logging settings of the app.  
`errorHandlingSettings` |  `object (`[ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingSettings)`)` Optional. Error handling settings of the app.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed.  
`toolExecutionMode` |  `enum (`[ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolExecutionMode)`)` Optional. The tool execution mode for the app. If not provided, will default to PARALLEL.  
`evaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EvaluationMetricsThresholds)`)` Optional. The evaluation thresholds for the app.  
`variableDeclarations[]` |  `object (`[VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration)`)` Optional. The declarations of the variables.  
`predefinedVariableDeclarations[]` |  `object (`[VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration)`)` Output only. The declarations of predefined variables for the app.  
`globalInstruction` |  `string` Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents.  
`guardrails[]` |  `string` Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`dataStoreSettings` |  `object (`[DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DataStoreSettings)`)` Optional. The data store settings for the app.  
`defaultChannelProfile` |  `object (`[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile)`)` Optional. The default channel profile used by the app.  
`metadata` |  `map (key: string, value: string)` Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`deploymentCount` |  `integer` Output only. Number of deployments in the app.  
`clientCertificateSettings` |  `object (`[ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ClientCertificateSettings)`)` Optional. The default client certificate settings for the app.  
`vpcScSettings` |  `object (`[VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VpcScSettings)`)` Optional. VPC-SC settings for the app.  
`locked` |  `boolean` Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected.  
`validationErrors[]` |  `string` Output only. Misconfigurations or warnings in the app.  
`dashboardSettings` |  `object (`[DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DashboardSettings)`)` Optional. App-specific dashboard settings for linking and configuring Contact Center Insights dashboards.  
  
### LanguageSettings

JSON representation  
---  
      
    
    {
      "defaultLanguageCode": string,
      "supportedLanguageCodes": [
        string
      ],
      "enableMultilingualSupport": boolean,
      "fallbackAction": string
    }  
  
Fields  
---  
`defaultLanguageCode` |  `string` Optional. The default language code of the app.  
`supportedLanguageCodes[]` |  `string` Optional. List of languages codes supported by the app, in addition to the `default_language_code`.  
`enableMultilingualSupport` |  `boolean` Optional. Enables multilingual support. If true, agents in the app will use pre-built instructions to improve handling of multilingual input.  
`fallbackAction  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: This feature is no longer supported. Use `enable_multilingual_support` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.This can be a predefined action or a custom tool call. Valid values are: - A tool's full resource name, which triggers a specific tool execution. - A predefined system action, such as "escalate" or "exit", which triggers an `EndSession` signal with corresponding `metadata` to terminate the conversation.  
  
### TimeZoneSettings

JSON representation  
---  
      
    
    {
      "timeZone": string
    }  
  
Fields  
---  
`timeZone` |  `string` Optional. The time zone of the app from the [time zone database](https://www.iana.org/time-zones), e.g., America/Los_Angeles, Europe/Paris.  
  
### AudioProcessingConfig

JSON representation  
---  
      
    
    {
      "synthesizeSpeechConfigs": {
        string: {
          object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig))
        },
        ...
      },
      "bargeInConfig": {
        object ([BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BargeInConfig))
      },
      "inactivityTimeout": string,
      "ambientSoundConfig": {
        object ([AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AmbientSoundConfig))
      },
      "customVoiceSamples": [
        {
          object ([CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CustomVoiceSample))
        }
      ]
    }  
  
Fields  
---  
`synthesizeSpeechConfigs` |  `map (key: string, value: object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig)`))` Optional. Configuration of how the agent response should be synthesized, mapping from the language code to `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig)`.If the configuration for the specified language code is not found, the configuration for the root language code will be used. For example, if the map contains "en-us" and "en", and the specified language code is "en-gb", then "en" configuration will be used.Note: Language code is case-insensitive.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`bargeInConfig` |  `object (`[BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BargeInConfig)`)` Optional. Configures the agent behavior for the user barge-in activities.  
`inactivityTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The duration of user inactivity (no speech or interaction) before the agent prompts the user for reengagement. If not set, the agent will not prompt the user for reengagement.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`ambientSoundConfig` |  `object (`[AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AmbientSoundConfig)`)` Optional. Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.  
`customVoiceSamples[]` |  `object (`[CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CustomVoiceSample)`)` Optional. Configures custom voice samples for voice cloning.  
  
### SynthesizeSpeechConfigsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig)`)`  
  
### SynthesizeSpeechConfig

JSON representation  
---  
      
    
    {
      "voice": string,
      "speakingRate": number,
      "model": string,
      "instruction": string
    }  
  
Fields  
---  
`voice` |  `string` Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as language_code.For the list of available voices, please refer to [Supported voices and languages](https://cloud.google.com/text-to-speech/docs/voices) from Cloud Text-to-Speech.  
`speakingRate` |  `number` Optional. The speaking rate/speed in the range [0.25, 2.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. Values outside of the range [0.25, 2.0] will return an error.  
`model` |  `string` Optional. The model used to synthesize audio. Currently supported values: - "gemini-3.1-flash-tts-preview" If empty, Chirp3-HD is used.  
`instruction` |  `string` Optional. The instruction used to synthesize speech when using a generative model.  
  
### BargeInConfig

JSON representation  
---  
      
    
    {
      "disableBargeIn": boolean,
      "bargeInAwareness": boolean
    }  
  
Fields  
---  
`disableBargeIn  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: `disable_barge_in` is deprecated in favor of ``disable_barge_in_control`` in ChannelProfile.Disables user barge-in while the agent is speaking. If true, user input during agent response playback will be ignored.  
`bargeInAwareness` |  `boolean` Optional. If enabled, the agent will adapt its next response based on the assumption that the user hasn't heard the full preceding agent message. This should not be used in scenarios where agent responses are displayed visually.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### AmbientSoundConfig

JSON representation  
---  
      
    
    {
      "volumeGainDb": number,
    
      // Union field source can be only one of the following:
      "prebuiltAmbientNoise": enum ([PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PrebuiltAmbientNoise)),
      "gcsUri": string,
      "prebuiltAmbientSound": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`volumeGainDb` |  `number` Optional. Volume gain (in dB) of the normal native volume supported by ambient noise, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.  
Union field `source`. Ambient noise to be played with the synthesized agent response, to enhance the naturalness of the conversation. `source` can be only one of the following:  
`prebuiltAmbientNoise  
**(deprecated)**` |  `enum (`[PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PrebuiltAmbientNoise)`)` This item is deprecated!Optional. Deprecated: `prebuilt_ambient_noise` is deprecated in favor of `prebuilt_ambient_sound`.  
`gcsUri` |  `string` Optional. Ambient noise as a mono-channel, 16kHz WAV file stored in [Cloud Storage](https://cloud.google.com/storage).Note: Please make sure the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com` has `storage.objects.get` permission to the Cloud Storage object.  
`prebuiltAmbientSound` |  `string` Optional. Name of the prebuilt ambient sound. Valid values are: - "coffee_shop" - "keyboard" - "keypad" - "hum" - "office_1" - "office_2" - "office_3" - "room_1" - "room_2" - "room_3" - "room_4" - "room_5" - "air_conditioner"  
  
### CustomVoiceSample

JSON representation  
---  
      
    
    {
      "name": string,
      "voiceSampleGcsUri": string,
      "consentAudioGcsUri": string,
      "voiceInstruction": string,
      "previewAudioContent": string,
      "previewText": string,
      "warnings": [
        {
          object ([Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Warning))
        }
      ],
      "voiceInstructionMode": enum ([VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VoiceInstructionMode))
    }  
  
Fields  
---  
`name` |  `string` Optional. The user-defined name for the custom voice sample.  
`voiceSampleGcsUri` |  `string` Optional. The Cloud Storage URI to the audio sample for voice cloning. The audio sample should be a mono-channel, 24kHz WAV file.  
`consentAudioGcsUri` |  `string` Optional. Consent audio for voice cloning.  
`voiceInstruction` |  `string` Optional. Natural language instructions for voice style, tone, pacing, or pronunciation.  
`previewAudioContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Synthesized preview audio for custom voice, formatted as canonical WAV (LINEAR16, 24kHz, 16-bit, mono).A base64-encoded string.  
`previewText` |  `string` Optional. Text for synthesizing preview audio for custom voice.  
`warnings[]` |  `object (`[Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Warning)`)` Output only. Warning messages encountered during voice clone processing (e.g. low audio level).  
`voiceInstructionMode` |  `enum (`[VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VoiceInstructionMode)`)` Optional. Instruction mode for the voice sample. If unspecified, defaults to NO_INSTRUCTION.  
  
### Warning

JSON representation  
---  
      
    
    {
      "message": string,
      "type": enum ([WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WarningType))
    }  
  
Fields  
---  
`message` |  `string` Output only. A human-readable description of the warning.  
`type` |  `enum (`[WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WarningType)`)` Output only. The type of the warning.  
  
### LoggingSettings

JSON representation  
---  
      
    
    {
      "redactionConfig": {
        object ([RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.RedactionConfig))
      },
      "audioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig))
      },
      "unredactedAudioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig))
      },
      "bigqueryExportSettings": {
        object ([BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings))
      },
      "unredactedBigqueryExportSettings": {
        object ([BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings))
      },
      "cloudLoggingSettings": {
        object ([CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CloudLoggingSettings))
      },
      "conversationLoggingSettings": {
        object ([ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ConversationLoggingSettings))
      },
      "evaluationAudioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig))
      },
      "metricAnalysisSettings": {
        object ([MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.MetricAnalysisSettings))
      }
    }  
  
Fields  
---  
`redactionConfig` |  `object (`[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.RedactionConfig)`)` Optional. Configuration for how sensitive data should be redacted.  
`audioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig)`)` Optional. Configuration for how audio interactions should be recorded. The audio is subject to redaction as configured in `RedactionConfig`.  
`unredactedAudioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig)`)` Optional. Configures an additional recording of unredacted audio. This can be used to maintain a raw audio copy when audio redaction is `enabled`, typically for auditing or monitoring purposes.  
`bigqueryExportSettings` |  `object (`[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings)`)` Optional. Configures the BigQuery export behaviors for the app. The conversation data is subject to redaction as configured in `RedactionConfig`.  
`unredactedBigqueryExportSettings` |  `object (`[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings)`)` Optional. Configures the BigQuery export behaviors for the app. The unredacted conversation data will be exported to BigQuery tables if it is enabled.  
`cloudLoggingSettings` |  `object (`[CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CloudLoggingSettings)`)` Optional. Settings to describe the Cloud Logging behaviors for the app.  
`conversationLoggingSettings` |  `object (`[ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ConversationLoggingSettings)`)` Optional. Settings to describe the conversation logging behaviors for the app.  
`evaluationAudioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig)`)` Optional. Configuration for how audio interactions should be recorded for the evaluation. By default, audio recording is not enabled for evaluation sessions.  
`metricAnalysisSettings` |  `object (`[MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.MetricAnalysisSettings)`)` Optional. Settings to describe the conversation data collection behaviors for the LLM analysis pipeline for the app.  
  
### RedactionConfig

JSON representation  
---  
      
    
    {
      "enableRedaction": boolean,
      "inspectTemplate": string,
      "deidentifyTemplate": string
    }  
  
Fields  
---  
`enableRedaction` |  `boolean` Optional. If true, redaction will be applied in various logging scenarios, including conversation history, Cloud Logging and audio recording.  
`inspectTemplate` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) inspect template name to configure detection of sensitive data types.Format: `projects/{project}/locations/{location}/inspectTemplates/{inspect_template}`  
`deidentifyTemplate` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) deidentify template name to instruct on how to de-identify content.Format: `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`  
  
### AudioRecordingConfig

JSON representation  
---  
      
    
    {
      "gcsBucket": string,
      "gcsPathPrefix": string
    }  
  
Fields  
---  
`gcsBucket` |  `string` Optional. The [Cloud Storage](https://cloud.google.com/storage) bucket to store the session audio recordings. The URI must start with "gs://".Please choose a bucket location that meets your data residency requirements.Note: If the Cloud Storage bucket is in a different project from the app, you should grant `storage.objects.create` permission to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`gcsPathPrefix` |  `string` Optional. The Cloud Storage path prefix for audio recordings.This prefix can include the following placeholders, which will be dynamically substituted at serving time: - $project: project ID - $location: app location - $app: app ID - $date: session date in YYYY-MM-DD format - $session: session IDIf the path prefix is not specified, the default prefix `$project/$location/$app/$date/$session/` will be used.  
  
### BigQueryExportSettings

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "project": string,
      "dataset": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Indicates whether the BigQuery export is enabled.  
`project` |  `string` Optional. The **project ID** of the BigQuery dataset to export the data to.Note: If the BigQuery dataset is in a different project from the app, you should grant `roles/bigquery.admin` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`dataset` |  `string` Optional. The BigQuery **dataset ID** to export the data to.  
  
### CloudLoggingSettings

JSON representation  
---  
      
    
    {
      "enableCloudLogging": boolean
    }  
  
Fields  
---  
`enableCloudLogging` |  `boolean` Optional. Whether to enable Cloud Logging for the sessions.  
  
### ConversationLoggingSettings

JSON representation  
---  
      
    
    {
      "disableConversationLogging": boolean,
      "retentionWindow": string
    }  
  
Fields  
---  
`disableConversationLogging` |  `boolean` Optional. Whether to disable conversation logging for the sessions.  
`retentionWindow` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Controls the retention window for the conversation. If not set, the conversation will be retained for 365 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### MetricAnalysisSettings

JSON representation  
---  
      
    
    {
      "llmMetricsOptedOut": boolean
    }  
  
Fields  
---  
`llmMetricsOptedOut` |  `boolean` Optional. Whether to collect conversation data for llm analysis metrics. If true, conversation data will not be collected for llm analysis metrics; otherwise, conversation data will be collected.  
  
### ErrorHandlingSettings

JSON representation  
---  
      
    
    {
      "errorHandlingStrategy": enum ([ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingStrategy)),
      "fallbackResponseConfig": {
        object ([FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.FallbackResponseConfig))
      },
      "endSessionConfig": {
        object ([EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EndSessionConfig))
      }
    }  
  
Fields  
---  
`errorHandlingStrategy` |  `enum (`[ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingStrategy)`)` Optional. The strategy to use for error handling.  
`fallbackResponseConfig` |  `object (`[FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.FallbackResponseConfig)`)` Optional. Configuration for handling fallback responses.  
`endSessionConfig` |  `object (`[EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EndSessionConfig)`)` Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).  
  
### FallbackResponseConfig

JSON representation  
---  
      
    
    {
      "customFallbackMessages": {
        string: string,
        ...
      },
      "maxFallbackAttempts": integer
    }  
  
Fields  
---  
`customFallbackMessages` |  `map (key: string, value: string)` Optional. The fallback messages in case of system errors (e.g. LLM errors), mapped by [supported language code](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/language).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`maxFallbackAttempts` |  `integer` Optional. The maximum number of fallback attempts to make before the agent emitting `EndSession` Signal.  
  
### CustomFallbackMessagesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### EndSessionConfig

JSON representation  
---  
      
    
    {
    
      // Union field _escalate_session can be only one of the following:
      "escalateSession": boolean
      // End of list of possible types for union field _escalate_session.
    }  
  
Fields  
---  
Union field `_escalate_session`.`_escalate_session` can be only one of the following:  
`escalateSession` |  `boolean` Optional. Whether to escalate the session in `EndSession`. If session is escalated, `metadata in EndSession` will contain `session_escalated = true`. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#transfer_a_call_to_a_human_agent> for details.  
  
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
  
### EvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "goldenEvaluationMetricsThresholds": {
        object ([GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.GoldenEvaluationMetricsThresholds))
      },
      "hallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)),
      "goldenHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)),
      "scenarioHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`goldenEvaluationMetricsThresholds` |  `object (`[GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.GoldenEvaluationMetricsThresholds)`)` Optional. The golden evaluation metrics thresholds.  
`hallucinationMetricBehavior  
**(deprecated)**` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)`)` This item is deprecated!Optional. Deprecated: Use `golden_hallucination_metric_behavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`goldenHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for golden evaluations.  
`scenarioHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for scenario evaluations.  
  
### GoldenEvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "turnLevelMetricsThresholds": {
        object ([TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TurnLevelMetricsThresholds))
      },
      "expectationLevelMetricsThresholds": {
        object ([ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExpectationLevelMetricsThresholds))
      },
      "toolMatchingSettings": {
        object ([ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolMatchingSettings))
      }
    }  
  
Fields  
---  
`turnLevelMetricsThresholds` |  `object (`[TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TurnLevelMetricsThresholds)`)` Optional. The turn level metrics thresholds.  
`expectationLevelMetricsThresholds` |  `object (`[ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExpectationLevelMetricsThresholds)`)` Optional. The expectation level metrics thresholds.  
`toolMatchingSettings` |  `object (`[ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolMatchingSettings)`)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
### TurnLevelMetricsThresholds

JSON representation  
---  
      
    
    {
      "semanticSimilarityChannel": enum ([SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SemanticSimilarityChannel)),
    
      // Union field _semantic_similarity_success_threshold can be only one of the
      // following:
      "semanticSimilaritySuccessThreshold": integer
      // End of list of possible types for union field
      // _semantic_similarity_success_threshold.
    
      // Union field _overall_tool_invocation_correctness_threshold can be only one
      // of the following:
      "overallToolInvocationCorrectnessThreshold": number
      // End of list of possible types for union field
      // _overall_tool_invocation_correctness_threshold.
    }  
  
Fields  
---  
`semanticSimilarityChannel` |  `enum (`[SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SemanticSimilarityChannel)`)` Optional. The semantic similarity channel to use for evaluation.  
Union field `_semantic_similarity_success_threshold`.`_semantic_similarity_success_threshold` can be only one of the following:  
`semanticSimilaritySuccessThreshold` |  `integer` Optional. The success threshold for semantic similarity. Must be an integer between 0 and 4. Default is >= 3.  
Union field `_overall_tool_invocation_correctness_threshold`.`_overall_tool_invocation_correctness_threshold` can be only one of the following:  
`overallToolInvocationCorrectnessThreshold` |  `number` Optional. The success threshold for overall tool invocation correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### ExpectationLevelMetricsThresholds

JSON representation  
---  
      
    
    {
    
      // Union field _tool_invocation_parameter_correctness_threshold can be only one
      // of the following:
      "toolInvocationParameterCorrectnessThreshold": number
      // End of list of possible types for union field
      // _tool_invocation_parameter_correctness_threshold.
    }  
  
Fields  
---  
Union field `_tool_invocation_parameter_correctness_threshold`.`_tool_invocation_parameter_correctness_threshold` can be only one of the following:  
`toolInvocationParameterCorrectnessThreshold` |  `number` Optional. The success threshold for individual tool invocation parameter correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### ToolMatchingSettings

JSON representation  
---  
      
    
    {
      "extraToolCallBehavior": enum ([ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExtraToolCallBehavior))
    }  
  
Fields  
---  
`extraToolCallBehavior` |  `enum (`[ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExtraToolCallBehavior)`)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
### VariableDeclaration

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the variable. The name must start with a letter or underscore and contain only letters, numbers, or underscores.  
`description` |  `string` Required. The description of the variable.  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Required. The schema of the variable.  
  
### Schema

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)),
      "properties": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "required": [
        string
      ],
      "description": string,
      "items": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "nullable": boolean,
      "uniqueItems": boolean,
      "prefixItems": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "additionalProperties": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "anyOf": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "enum": [
        string
      ],
      "default": value,
      "ref": string,
      "defs": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "title": string,
      "minItems": string,
      "maxItems": string,
    
      // Union field _minimum can be only one of the following:
      "minimum": number
      // End of list of possible types for union field _minimum.
    
      // Union field _maximum can be only one of the following:
      "maximum": number
      // End of list of possible types for union field _maximum.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)`)` Required. The type of the data.  
`properties` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. Properties of Type.OBJECT.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`required[]` |  `string` Optional. Required properties of Type.OBJECT.  
`description` |  `string` Optional. The description of the data.  
`items` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schema of the elements of Type.ARRAY.  
`nullable` |  `boolean` Optional. Indicates if the value may be null.  
`uniqueItems` |  `boolean` Optional. Indicate the items in the array must be unique. Only applies to TYPE.ARRAY.  
`prefixItems[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schemas of initial elements of Type.ARRAY.  
`additionalProperties` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Can either be a boolean or an object, controls the presence of additional properties.  
`anyOf[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The value should be validated against any (one or more) of the subschemas in the list.  
`enum[]` |  `string` Optional. Possible values of the element of primitive type with enum format. Examples: 1. We can define direction as : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH", "WEST"]} 2. We can define apartment number as : {type:INTEGER, format:enum, enum:["101", "201", "301"]}  
`default` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. Default value of the data.  
`ref` |  `string` Optional. Allows indirect references between schema nodes. The value should be a valid reference to a child of the root `defs`.For example, the following schema defines a reference to a schema node named "Pet":
    
    
    type: object
    properties:
      pet:
        ref: #/defs/Pet
    defs:
      Pet:
        type: object
        properties:
          name:
            type: string
    

The value of the "pet" property is a reference to the schema node named "Pet". See details in <https://json-schema.org/understanding-json-schema/structuring>.  
`defs` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. A map of definitions for use by `ref`. Only allowed at the root of the schema.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`title` |  `string` Optional. The title of the schema.  
`minItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Minimum number of the elements for Type.ARRAY.  
`maxItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum number of the elements for Type.ARRAY.  
Union field `_minimum`.`_minimum` can be only one of the following:  
`minimum` |  `number` Optional. Minimum value for Type.INTEGER and Type.NUMBER.  
Union field `_maximum`.`_maximum` can be only one of the following:  
`maximum` |  `number` Optional. Maximum value for Type.INTEGER and Type.NUMBER.  
  
### PropertiesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### DefsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
### DataStoreSettings

JSON representation  
---  
      
    
    {
      "engines": [
        {
          object ([Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Engine))
        }
      ]
    }  
  
Fields  
---  
`engines[]` |  `object (`[Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Engine)`)` Output only. The engines for the app.  
  
### Engine

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type_1))
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type_1)`)` Output only. The type of the engine.  
  
### ChannelProfile

JSON representation  
---  
      
    
    {
      "profileId": string,
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)),
      "personaProperty": {
        object ([PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty))
      },
      "webWidgetConfig": {
        object ([WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig))
      },
      "whatsappConfig": {
        object ([WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig))
      },
      "instagramConfig": {
        object ([InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig))
      },
    
      // Union field _disable_dtmf can be only one of the following:
      "disableDtmf": boolean
      // End of list of possible types for union field _disable_dtmf.
    
      // Union field _disable_barge_in_control can be only one of the following:
      "disableBargeInControl": boolean
      // End of list of possible types for union field _disable_barge_in_control.
    
      // Union field _noise_suppression_level can be only one of the following:
      "noiseSuppressionLevel": string
      // End of list of possible types for union field _noise_suppression_level.
    }  
  
Fields  
---  
`profileId` |  `string` Optional. The unique identifier of the channel profile.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)`)` Optional. The type of the channel profile.  
`personaProperty` |  `object (`[PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty)`)` Optional. The persona property of the channel profile.  
`webWidgetConfig` |  `object (`[WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig)`)` Optional. The configuration for the web widget.  
`whatsappConfig` |  `object (`[WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig)`)` Optional. Configuration specific to WhatsApp deployments.  
`instagramConfig` |  `object (`[InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig)`)` Optional. Configuration specific to Instagram deployments.  
Union field `_disable_dtmf`.`_disable_dtmf` can be only one of the following:  
`disableDtmf` |  `boolean` Optional. Whether to disable DTMF (dual-tone multi-frequency).  
Union field `_disable_barge_in_control`.`_disable_barge_in_control` can be only one of the following:  
`disableBargeInControl` |  `boolean` Optional. Whether to disable user barge-in control in the conversation. - **true** : User interruptions are disabled while the agent is speaking. - **false** : The agent retains automatic control over when the user can interrupt.  
Union field `_noise_suppression_level`.`_noise_suppression_level` can be only one of the following:  
`noiseSuppressionLevel` |  `string` Optional. The noise suppression level of the channel profile. Available values are "low", "moderate", "high", "very_high".  
  
### PersonaProperty

JSON representation  
---  
      
    
    {
      "persona": enum ([Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona))
    }  
  
Fields  
---  
`persona` |  `enum (`[Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona)`)` Optional. The persona of the channel.  
  
### WebWidgetConfig

JSON representation  
---  
      
    
    {
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)),
      "theme": enum ([Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)),
      "webWidgetTitle": string,
      "securitySettings": {
        object ([SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings))
      }
    }  
  
Fields  
---  
`modality` |  `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)`)` Optional. The modality of the web widget.  
`theme` |  `enum (`[Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)`)` Optional. The theme of the web widget.  
`webWidgetTitle` |  `string` Optional. The title of the web widget.  
`securitySettings` |  `object (`[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings)`)` Optional. The security settings of the web widget.  
  
### SecuritySettings

JSON representation  
---  
      
    
    {
      "enablePublicAccess": boolean,
      "enableOriginCheck": boolean,
      "allowedOrigins": [
        string
      ],
      "enableRecaptcha": boolean
    }  
  
Fields  
---  
`enablePublicAccess` |  `boolean` Optional. Indicates whether public access to the web widget is enabled. If `true`, the web widget will be publicly accessible. If `false`, the web widget must be integrated with your own authentication and authorization system to return valid credentials for accessing the CES agent.  
`enableOriginCheck` |  `boolean` Optional. Indicates whether origin check for the web widget is enabled. If `true`, the web widget will check the origin of the website that loads the web widget and only allow it to be loaded in the same origin or any of the allowed origins.  
`allowedOrigins[]` |  `string` Optional. The origins that are allowed to host the web widget. An origin is defined by RFC 6454. If empty, all origins are allowed. A maximum of 100 origins is allowed. Example: "https://example.com"  
`enableRecaptcha` |  `boolean` Optional. Indicates whether reCAPTCHA verification for the web widget is enabled.  
  
### WhatsAppConfig

JSON representation  
---  
      
    
    {
      "wabaId": string,
      "phoneNumberId": string,
      "phoneNumber": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`wabaId` |  `string` Required. The WhatsApp Business Account ID.  
`phoneNumberId` |  `string` Required. The Meta phone number ID.  
`phoneNumber` |  `string` Optional. The phone number in E.164 format.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### InstagramConfig

JSON representation  
---  
      
    
    {
      "instagramAccountId": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`instagramAccountId` |  `string` Required. The Instagram Account ID.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### MetadataEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### ClientCertificateSettings

JSON representation  
---  
      
    
    {
      "tlsCertificate": string,
      "privateKey": string,
      "passphrase": string
    }  
  
Fields  
---  
`tlsCertificate` |  `string` Required. The TLS certificate encoded in PEM format. This string must include the begin header and end footer lines.  
`privateKey` |  `string` Required. The name of the SecretManager secret version resource storing the private key encoded in PEM format. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`passphrase` |  `string` Optional. The name of the SecretManager secret version resource storing the passphrase to decrypt the private key. Should be left unset if the private key is not encrypted. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
  
### VpcScSettings

JSON representation  
---  
      
    
    {
      "allowedOrigins": [
        string
      ]
    }  
  
Fields  
---  
`allowedOrigins[]` |  `string` Optional. The allowed HTTP(s) origins that OpenAPI tools in the App are able to directly call when VPC Service Controls are enabled. These strings must match the origin exactly, including the port if specified. For example, "https://example.com" or "https://example.com:443". This list does not yet apply to Python tools that may make direct HTTP calls.  
  
### DashboardSettings

JSON representation  
---  
      
    
    {
      "defaultDashboard": string
    }  
  
Fields  
---  
`defaultDashboard` |  `string` Optional. The resource name of the default Contact Center Insights dashboard associated with the app. This is the dashboard that will be displayed when users navigate to the Monitoring view for the app.Format: `projects/{project}/locations/{location}/dashboards/{dashboard}`  
  
### Agent

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
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
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
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
          object ([AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset))
        }
      ],
      "generatedSummary": string,
      "transferRules": [
        {
          object ([TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule))
        }
      ],
      "validationErrors": [
        string
      ],
    
      // Union field agent_type can be only one of the following:
      "llmAgent": {
        object (LlmAgent)
      },
      "remoteDialogflowAgent": {
        object ([RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent))
      },
      "remoteA2aAgent": {
        object ([RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent))
      }
      // End of list of possible types for union field agent_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Required. Display name of the agent.  
`description` |  `string` Optional. Human-readable description of the agent.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`instruction` |  `string` Optional. Instructions for the LLM model to guide the agent's behavior.  
`tools[]` |  `string` Optional. List of available tools for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`childAgents[]` |  `string` Optional. List of child agents in the agent tree. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`beforeAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`guardrails[]` |  `string` Optional. List of guardrails for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`toolsets[]` |  `object (`[AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset)`)` Optional. List of toolsets for the agent.  
`generatedSummary` |  `string` Output only. If the agent is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`transferRules[]` |  `object (`[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule)`)` Optional. Agent transfer rules. If multiple rules match, the first one in the list will be used.  
`validationErrors[]` |  `string` Output only. Misconfigurations or errors in the agent that may affect agent quality.  
Union field `agent_type`. The type of agent. `agent_type` can be only one of the following:  
`llmAgent` |  `object (`LlmAgent`)` Optional. The default agent type.  
`remoteDialogflowAgent` |  `object (`[RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent)`)` Optional. The remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent to be used for the agent execution. If this field is set, all other agent level properties will be ignored.Note: If the Dialogflow agent is in a different project from the app, you should grant `roles/dialogflow.client` to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`remoteA2aAgent` |  `object (`[RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent)`)` Optional. The remote [A2A](https://github.com/a2aproject/A2A) agent to be used for the agent execution.  
  
### RemoteDialogflowAgent

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
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### RemoteA2aAgent

JSON representation  
---  
      
    
    {
      "a2aConfig": {
        object ([RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig))
      }
    }  
  
Fields  
---  
`a2aConfig` |  `object (`[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig)`)` Required. The A2A connection configuration.  
  
### RemoteA2aConfig

JSON representation  
---  
      
    
    {
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
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
    
      // Union field agent_spec can be only one of the following:
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "agentRegistry": string
      // End of list of possible types for union field agent_spec.
    }  
  
Fields  
---  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent. Optional if the registry reference already handles authentication.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`streamingEnabled` |  `boolean` Optional. Whether streaming is enabled for the remote agent.  
`contextId` |  `string` Optional. If not empty, interactions with the remote A2A agent will use this context ID. This context_id field can refer to a session variable like `$context.variables.order_agent_session_id`.  
Union field `agent_spec`. Specification of the remote agent. `agent_spec` can be only one of the following:  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Optional. The full agent card defined inline.  
`agentRegistry` |  `string` Optional. Reference to the agent in the Agent Registry. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
### AgentCard

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "supportedInterfaces": [
        {
          object ([AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface))
        }
      ],
      "version": string,
      "skills": [
        {
          object ([AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. A human-readable name for the agent.  
`description` |  `string` Required. A description of the agent's domain of action/solution space.  
`supportedInterfaces[]` |  `object (`[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface)`)` Required. Ordered list of supported interfaces. The first entry is preferred.  
`version` |  `string` Required. The version of the agent.  
`skills[]` |  `object (`[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill)`)` Required. Skills represent a unit of ability an agent can perform. This may somewhat abstract but represents a more focused set of actions that the agent is highly likely to succeed at.  
  
### AgentInterface

JSON representation  
---  
      
    
    {
      "url": string,
      "protocolBinding": string,
      "tenant": string,
      "protocolVersion": string
    }  
  
Fields  
---  
`url` |  `string` Required. The URL where this interface is available. Must be a valid absolute HTTPS URL in production. Example: "https://api.example.com/a2a/v1", "https://grpc.example.com/a2a"  
`protocolBinding` |  `string` Required. The protocol binding supported at this URL. This is an open form string, to be easily extended for other protocol bindings. The core ones officially supported are `JSONRPC`, `GRPC` and `HTTP+JSON`.  
`tenant` |  `string` Tenant ID to be used in the request when calling the agent.  
`protocolVersion` |  `string` Required. The version of the A2A protocol this interface exposes. Use the latest supported minor version per major version. Examples: "0.3", "1.0"  
  
### AgentSkill

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "description": string,
      "tags": [
        string
      ],
      "examples": [
        string
      ],
      "inputModes": [
        string
      ],
      "outputModes": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A unique identifier for the agent's skill.  
`name` |  `string` Required. A human-readable name for the skill.  
`description` |  `string` Required. A detailed description of the skill.  
`tags[]` |  `string` Required. A set of keywords describing the skill's capabilities.  
`examples[]` |  `string` Example prompts or scenarios that this skill can handle.  
`inputModes[]` |  `string` The set of supported input media types for this skill, overriding the agent's defaults.  
`outputModes[]` |  `string` The set of supported output media types for this skill, overriding the agent's defaults.  
  
### ApiAuthentication

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig))
      },
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig))
      },
      "serviceAgentIdTokenAuthConfig": {
        object (ServiceAgentIdTokenAuthConfig)
      },
      "serviceAccountAuthConfig": {
        object ([ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig))
      },
      "bearerTokenConfig": {
        object ([BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`apiKeyConfig` |  `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig)`)` Optional. Config for API key auth.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig)`)` Optional. Config for OAuth.  
`serviceAgentIdTokenAuthConfig` |  `object (`ServiceAgentIdTokenAuthConfig`)` Optional. Config for ID token auth generated from CES service agent.  
`serviceAccountAuthConfig` |  `object (`[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig)`)` Optional. Config for service account authentication.  
`bearerTokenConfig` |  `object (`[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig)`)` Optional. Config for bearer token auth.  
  
### ApiKeyConfig

JSON representation  
---  
      
    
    {
      "keyName": string,
      "apiKeySecretVersion": string,
      "requestLocation": enum ([RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation))
    }  
  
Fields  
---  
`keyName` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`apiKeySecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the API key. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`requestLocation` |  `enum (`[RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation)`)` Required. Key location in the request.  
  
### OAuthConfig

JSON representation  
---  
      
    
    {
      "oauthGrantType": enum ([OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)),
      "clientId": string,
      "clientSecretVersion": string,
      "tokenEndpoint": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`oauthGrantType` |  `enum (`[OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)`)` Required. OAuth grant types.  
`clientId` |  `string` Required. The client ID from the OAuth provider.  
`clientSecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the client secret. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`tokenEndpoint` |  `string` Required. The token endpoint in the OAuth provider to exchange for an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
### ServiceAccountAuthConfig

JSON representation  
---  
      
    
    {
      "serviceAccount": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`serviceAccount` |  `string` Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant. If not specified, the default scope `https://www.googleapis.com/auth/cloud-platform` is used.  
  
### BearerTokenConfig

JSON representation  
---  
      
    
    {
      "token": string
    }  
  
Fields  
---  
`token` |  `string` Required. The bearer token. Must be in the format `$context.variables.<name_of_variable>`.  
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
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
  
### AgentToolset

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

JSON representation  
---  
      
    
    {
      "childAgent": string,
      "direction": enum ([Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)),
    
      // Union field rule_type can be only one of the following:
      "deterministicTransfer": {
        object ([DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer))
      },
      "disablePlannerTransfer": {
        object ([DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer))
      }
      // End of list of possible types for union field rule_type.
    }  
  
Fields  
---  
`childAgent` |  `string` Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)`)` Required. The direction of the transfer.  
Union field `rule_type`. The rule type. `rule_type` can be only one of the following:  
`deterministicTransfer` |  `object (`[DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer)`)` Optional. A rule that immediately transfers to the target agent when the condition is met.  
`disablePlannerTransfer` |  `object (`[DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer)`)` Optional. Rule that prevents the planner from transferring to the target agent.  
  
### DeterministicTransfer

JSON representation  
---  
      
    
    {
    
      // Union field condition_type can be only one of the following:
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      },
      "pythonCodeCondition": {
        object ([PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition))
      }
      // End of list of possible types for union field condition_type.
    }  
  
Fields  
---  
Union field `condition_type`. The condition to evaluate. `condition_type` can be only one of the following:  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Optional. A rule that evaluates a session state condition. If the condition evaluates to true, the transfer occurs.  
`pythonCodeCondition` |  `object (`[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition)`)` Optional. A rule that uses Python code block to evaluate the conditions. If the condition evaluates to true, the transfer occurs.  
  
### ExpressionCondition

JSON representation  
---  
      
    
    {
      "expression": string
    }  
  
Fields  
---  
`expression` |  `string` Required. The string representation of cloud.api.Expression condition.  
  
### PythonCodeCondition

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. The python code to execute.  
  
### DisablePlannerTransfer

JSON representation  
---  
      
    
    {
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      }
    }  
  
Fields  
---  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Required. If the condition evaluates to true, planner will not be allowed to transfer to the target agent.  
  
### Tool

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)),
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "generatedSummary": string,
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig))
      },
      "readOnly": boolean,
    
      // Union field tool_type can be only one of the following:
      "clientFunction": {
        object ([ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction))
      },
      "openApiTool": {
        object ([OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool))
      },
      "googleSearchTool": {
        object ([GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool))
      },
      "connectorTool": {
        object ([ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool))
      },
      "dataStoreTool": {
        object ([DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool))
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mcpTool": {
        object ([McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool))
      },
      "fileSearchTool": {
        object ([FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool))
      },
      "systemTool": {
        object ([SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool))
      },
      "agentTool": {
        object ([AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool))
      },
      "widgetTool": {
        object ([WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool))
      },
      "remoteAgentTool": {
        object ([RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool))
      }
      // End of list of possible types for union field tool_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the tool. Format:

  * `projects/{project}/locations/{location}/apps/{app}/tools/{tool}` for standalone tools.
  * `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}/tools/{tool}` for tools retrieved from a toolset.

These tools are dynamic and output-only; they cannot be referenced directly where a tool is expected.  
`displayName` |  `string` Output only. The display name of the tool, derived based on the tool's type. For example, display name of a [ClientFunction][Tool.ClientFunction] is derived from its `name` property.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)`)` Optional. The execution type of the tool.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the tool execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` tools and 60 seconds for `ASYNCHRONOUS` tools.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`generatedSummary` |  `string` Output only. If the tool is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig)`)` Optional. Configuration for tool behavior in fake mode.  
`readOnly` |  `boolean` Output only. Indicates whether the tool is read-only. If true, the tool cannot be modified by the user.  
Union field `tool_type`. The type of the tool. `tool_type` can be only one of the following:  
`clientFunction` |  `object (`[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction)`)` Optional. The client function.  
`openApiTool` |  `object (`[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool)`)` Optional. The open API tool.  
`googleSearchTool` |  `object (`[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool)`)` Optional. The google search tool.  
`connectorTool` |  `object (`[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool)`)` Optional. The Integration Connector tool.  
`dataStoreTool` |  `object (`[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool)`)` Optional. The data store tool.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. The python function tool.  
`mcpTool` |  `object (`[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool)`)` Optional. The MCP tool. An MCP tool cannot be created or updated directly and is managed by the MCP toolset.  
`fileSearchTool` |  `object (`[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool)`)` Optional. The file search tool.  
`systemTool` |  `object (`[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool)`)` Optional. The system tool.  
`agentTool` |  `object (`[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool)`)` Optional. The agent tool.  
`widgetTool` |  `object (`[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool)`)` Optional. The widget tool.  
`remoteAgentTool` |  `object (`[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool)`)` Optional. The remote agent tool.  
  
### ClientFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "response": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The function name.  
`description` |  `string` Optional. The function description.  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function parameters.  
`response` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function response.  
  
### OpenApiTool

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "name": string,
      "description": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "ignoreUnknownFields": boolean,
      "url": string
    }  
  
Fields  
---  
`openApiSchema` |  `string` Required. The OpenAPI schema in JSON or YAML format.  
`name` |  `string` Optional. The name of the tool. If not provided, the name of the tool will be derived from the OpenAPI schema, from `operation.operationId`.  
`description` |  `string` Optional. The description of the tool. If not provided, the description of the tool will be derived from the OpenAPI schema, from `operation.description` or `operation.summary`.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client will trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in tools in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### TlsConfig

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert)`)` Required. Specifies a list of allowed custom CA certificates for HTTPS verification.  
  
### CaCert

JSON representation  
---  
      
    
    {
      "displayName": string,
      "cert": string
    }  
  
Fields  
---  
`displayName` |  `string` Required. The name of the allowed custom CA certificates. This can be used to disambiguate the custom CA certificates.  
`cert` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, CES will use Google's default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with "subject alt name". For instance a certificate can be self-signed using the following command:
    
    
       openssl x509 -req -days 200 -in example.com.csr \
         -signkey example.com.key \
         -out example.com.crt \
         -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
    

A base64-encoded string.  
  
### ServiceDirectoryConfig

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}`. Location of the service directory must be the same as the location of the app.  
  
### GoogleSearchTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "contextUrls": [
        string
      ],
      "preferredDomains": [
        string
      ],
      "excludeDomains": [
        string
      ],
      "promptConfig": {
        object ([PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`contextUrls[]` |  `string` Optional. Content will be fetched directly from these URLs for context and grounding. Example: "https://example.com/path.html". A maximum of 20 URLs are allowed.  
`preferredDomains[]` |  `string` Optional. Specifies domains to restrict search results to. Example: "example.com", "another.site". A maximum of 20 domains can be specified.  
`excludeDomains[]` |  `string` Optional. List of domains to be excluded from the search results. Example: "example.com". A maximum of 2000 domains can be excluded.  
`promptConfig` |  `object (`[PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig)`)` Optional. Prompt instructions passed to planner on how the search results should be processed for text and voice.  
  
### PromptConfig

JSON representation  
---  
      
    
    {
      "textPrompt": string,
      "voicePrompt": string
    }  
  
Fields  
---  
`textPrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in chat conversations. If not set, default prompt will be used.  
`voicePrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in voice conversations. If not set, default prompt will be used.  
  
### ConnectorTool

JSON representation  
---  
      
    
    {
      "connection": string,
      "action": {
        object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action))
      },
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig))
      },
      "name": string,
      "description": string
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`action` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action)`)` Required. Action for the tool to use.  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the ConnectorTool creation will fail. See <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override> for details.  
`name` |  `string` Optional. The name of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
`description` |  `string` Optional. The description of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
  
### Action

JSON representation  
---  
      
    
    {
      "inputFields": [
        string
      ],
      "outputFields": [
        string
      ],
    
      // Union field action_spec can be only one of the following:
      "connectionActionId": string,
      "entityOperation": {
        object ([EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation))
      }
      // End of list of possible types for union field action_spec.
    }  
  
Fields  
---  
`inputFields[]` |  `string` Optional. Entity fields to use as inputs for the operation. If no fields are specified, all fields of the Entity will be used.  
`outputFields[]` |  `string` Optional. Entity fields to return from the operation. If no fields are specified, all fields of the Entity will be returned.  
Union field `action_spec`. Specification for an action to configure for the tool to use. `action_spec` can be only one of the following:  
`connectionActionId` |  `string` ID of a Connection action for the tool to use.  
`entityOperation` |  `object (`[EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation)`)` Entity operation configuration for the tool to use.  
  
### EntityOperation

JSON representation  
---  
      
    
    {
      "entityId": string,
      "operation": enum ([OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType))
    }  
  
Fields  
---  
`entityId` |  `string` Required. ID of the entity.  
`operation` |  `enum (`[OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType)`)` Required. Operation to perform on the entity.  
  
### EndUserAuthConfig

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "oauth2AuthCodeConfig": {
        object ([Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig))
      },
      "oauth2JwtBearerConfig": {
        object ([Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`oauth2AuthCodeConfig` |  `object (`[Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig)`)` Oauth 2.0 Authorization Code authentication.  
`oauth2JwtBearerConfig` |  `object (`[Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig)`)` JWT Profile Oauth 2.0 Authorization Grant authentication.  
  
### Oauth2AuthCodeConfig

JSON representation  
---  
      
    
    {
      "oauthToken": string
    }  
  
Fields  
---  
`oauthToken` |  `string` Required. Oauth token parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### Oauth2JwtBearerConfig

JSON representation  
---  
      
    
    {
      "issuer": string,
      "subject": string,
      "clientKey": string
    }  
  
Fields  
---  
`issuer` |  `string` Required. Issuer parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`subject` |  `string` Required. Subject parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`clientKey` |  `string` Required. Client parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### DataStoreTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "boostSpecs": [
        {
          object ([BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs))
        }
      ],
      "modalityConfigs": [
        {
          object ([ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig))
        }
      ],
      "filterParameterBehavior": enum ([FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)),
    
      // Union field search_source can be only one of the following:
      "dataStoreSource": {
        object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
      },
      "engineSource": {
        object ([EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource))
      }
      // End of list of possible types for union field search_source.
    }  
  
Fields  
---  
`name` |  `string` Required. The data store tool name.  
`description` |  `string` Optional. The tool description.  
`boostSpecs[]` |  `object (`[BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs)`)` Optional. Boost specification to boost certain documents.  
`modalityConfigs[]` |  `object (`[ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig)`)` Optional. The modality configs for the data store.  
`filterParameterBehavior` |  `enum (`[FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)`)` Optional. The filter parameter behavior.  
Union field `search_source`. Defines the search source, either a single DataStore or an Engine. `search_source` can be only one of the following:  
`dataStoreSource` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Search within a single specific DataStore.  
`engineSource` |  `object (`[EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource)`)` Optional. Search within an Engine (potentially across multiple DataStores).  
  
### DataStoreSource

JSON representation  
---  
      
    
    {
      "filter": string,
      "dataStore": {
        object ([DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore))
      }
    }  
  
Fields  
---  
`filter` |  `string` Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
`dataStore` |  `object (`[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore)`)` Optional. The data store.  
  
### DataStore

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)),
      "documentProcessingMode": enum ([DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)),
      "displayName": string,
      "createTime": string,
      "connectorConfig": {
        object ([ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Full resource name of the DataStore. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`  
`type` |  `enum (`[DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)`)` Output only. The type of the data store. This field is readonly and populated by the server.  
`documentProcessingMode` |  `enum (`[DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)`)` Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.  
`displayName` |  `string` Output only. The display name of the data store.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the data store was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`connectorConfig` |  `object (`[ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig)`)` Output only. The connector config for the data store connection.  
  
### ConnectorConfig

JSON representation  
---  
      
    
    {
      "collection": string,
      "collectionDisplayName": string,
      "dataSource": string
    }  
  
Fields  
---  
`collection` |  `string` Resource name of the collection the data store belongs to.  
`collectionDisplayName` |  `string` Display name of the collection the data store belongs to.  
`dataSource` |  `string` The name of the data source. Example: `salesforce`, `jira`, `confluence`, `bigquery`.  
  
### EngineSource

JSON representation  
---  
      
    
    {
      "engine": string,
      "dataStoreSources": [
        {
          object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
        }
      ],
      "filter": string
    }  
  
Fields  
---  
`engine` |  `string` Required. Full resource name of the Engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`dataStoreSources[]` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Use to target specific DataStores within the Engine. If empty, the search applies to all DataStores associated with the Engine.  
`filter` |  `string` Optional. A filter applied to the search across the Engine. Not relevant and not used if 'data_store_sources' is provided. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
  
### BoostSpecs

JSON representation  
---  
      
    
    {
      "dataStores": [
        string
      ],
      "spec": [
        {
          object ([BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec))
        }
      ]
    }  
  
Fields  
---  
`dataStores[]` |  `string` Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}.  
`spec[]` |  `object (`[BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec)`)` Required. A list of boosting specifications.  
  
### BoostSpec

JSON representation  
---  
      
    
    {
      "conditionBoostSpecs": [
        {
          object ([ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec))
        }
      ]
    }  
  
Fields  
---  
`conditionBoostSpecs[]` |  `object (`[ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec)`)` Required. A list of boosting specifications.  
  
### ConditionBoostSpec

JSON representation  
---  
      
    
    {
      "condition": string,
      "boost": number,
      "boostControlSpec": {
        object ([BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec))
      }
    }  
  
Fields  
---  
`condition` |  `string` Required. An expression which specifies a boost condition. The syntax is the same as filter expression syntax. Currently, the only supported condition is a list of BCP-47 lang codes. Example: To boost suggestions in languages en or fr: (lang_code: ANY("en", "fr"))  
`boost` |  `number` Optional. Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`boostControlSpec` |  `object (`[BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec)`)` Optional. Complex specification for custom ranking based on customer defined attribute value.  
  
### BoostControlSpec

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "attributeType": enum ([AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)),
      "interpolationType": enum ([InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)),
      "controlPoints": [
        {
          object ([ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint))
        }
      ]
    }  
  
Fields  
---  
`fieldName` |  `string` Optional. The name of the field whose value will be used to determine the boost amount.  
`attributeType` |  `enum (`[AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)`)` Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified field_name. In the case of numerical it is straightforward i.e. attribute_value = numerical_field_value. In the case of freshness however, attribute_value = (time.now() - datetime_field_value).  
`interpolationType` |  `enum (`[InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)`)` Optional. The interpolation type to be applied to connect the control points listed below.  
`controlPoints[]` |  `object (`[ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint)`)` Optional. The control points used to define the curve. The monotonic function (defined through the interpolation_type above) passes through the control points listed here.  
  
### ControlPoint

JSON representation  
---  
      
    
    {
      "attributeValue": string,
      "boostAmount": number
    }  
  
Fields  
---  
`attributeValue` |  `string` Optional. Can be one of: 1. The numerical field value. 2. The duration spec for freshness: The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`.  
`boostAmount` |  `number` Optional. The value between -1 to 1 by which to boost the score if the attribute_value evaluates to the value specified above.  
  
### ModalityConfig

JSON representation  
---  
      
    
    {
      "modalityType": enum ([ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)),
      "rewriterConfig": {
        object ([RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig))
      },
      "summarizationConfig": {
        object ([SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig))
      },
      "groundingConfig": {
        object ([GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig))
      },
      "snippetsConfig": {
        object ([SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig))
      }
    }  
  
Fields  
---  
`modalityType` |  `enum (`[ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)`)` Required. The modality type.  
`rewriterConfig` |  `object (`[RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig)`)` Optional. The rewriter config.  
`summarizationConfig` |  `object (`[SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig)`)` Optional. The summarization config.  
`groundingConfig` |  `object (`[GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig)`)` Optional. The grounding configuration.  
`snippetsConfig` |  `object (`[SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig)`)` Optional. The snippets configuration.  
  
### RewriterConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Required. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether the rewriter is disabled.  
  
### SummarizationConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether summarization is disabled.  
  
### GroundingConfig

JSON representation  
---  
      
    
    {
      "groundingLevel": number,
      "disabled": boolean
    }  
  
Fields  
---  
`groundingLevel` |  `number` Optional. The groundedness threshold of the answer based on the retrieved sources. The value has a configurable range of [1, 5]. The level is used to threshold the groundedness of the answer, meaning that all responses with a groundedness score below the threshold will fall back to returning relevant snippets only.For example, a level of 3 means that the groundedness score must be 3 or higher for the response to be returned.  
`disabled` |  `boolean` Optional. Whether grounding is disabled.  
  
### SnippetsConfig

JSON representation  
---  
      
    
    {
      "enableSnippets": boolean,
      "maxSnippets": integer
    }  
  
Fields  
---  
`enableSnippets` |  `boolean` Optional. Whether snippets are enabled.  
`maxSnippets` |  `integer` Optional. Number of snippets to return per query. If unset, returns all snippets from the service by default.  
  
### PythonFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "pythonCode": string,
      "description": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the Python function to execute. Must match a Python function name defined in the python code. Case sensitive. If the name is not provided, the first function defined in the python code will be used.  
`pythonCode` |  `string` Optional. The Python code to execute for the tool.  
`description` |  `string` Output only. The description of the Python function, parsed from the python code's docstring.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for the tool.  
  
### McpTool

JSON representation  
---  
      
    
    {
      "name": string,
      "nameOverride": string,
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State))
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the MCP tool.  
`nameOverride` |  `string` Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override.  
`description` |  `string` Optional. The description of the MCP tool.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the output arguments of the MCP tool.  
`serverAddress` |  `string` Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State)`)` Output only. The dynamic availability state of the tool on the external server.  
  
### CustomHeadersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### FileSearchTool

JSON representation  
---  
      
    
    {
      "corpusType": enum ([CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)),
      "name": string,
      "description": string,
      "fileCorpus": string
    }  
  
Fields  
---  
`corpusType` |  `enum (`[CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)`)` Optional. The type of the corpus. Default is FULLY_MANAGED.  
`name` |  `string` Required. The tool name.  
`description` |  `string` Optional. The tool description.  
`fileCorpus` |  `string` Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus}  
  
### SystemTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the system tool.  
`description` |  `string` Output only. The description of the system tool.  
  
### AgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agent": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the agent tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`agent` |  `string` Optional. The resource name of the agent that is the entry point of the tool. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
### WidgetTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "widgetType": enum ([WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)),
      "uiConfig": {
        object
      },
      "dataMapping": {
        object ([DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping))
      },
      "textResponseConfig": {
        object ([TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig))
      },
    
      // Union field input can be only one of the following:
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
      // End of list of possible types for union field input.
    }  
  
Fields  
---  
`name` |  `string` Required. The display name of the widget tool.  
`description` |  `string` Optional. The description of the widget tool.  
`widgetType` |  `enum (`[WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)`)` Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED.  
`uiConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Configuration for rendering the widget.  
`dataMapping` |  `object (`[DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping)`)` Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters.  
`textResponseConfig` |  `object (`[TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig)`)` Optional. Configuration for always-included text responses.  
Union field `input`. The input of the widget tool. `input` can be only one of the following:  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The input parameters of the widget tool.  
  
### DataMapping

JSON representation  
---  
      
    
    {
      "sourceToolName": string,
      "fieldMappings": {
        string: string,
        ...
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)),
      "pythonScript": string
    }  
  
Fields  
---  
`sourceToolName` |  `string` Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`fieldMappings` |  `map (key: string, value: string)` Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)`)` Optional. The mode of the data mapping.  
`pythonScript  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `python_function` instead.  
  
### FieldMappingsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### TextResponseConfig

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)),
      "staticText": string,
      "textResponseInstruction": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)`)` Optional. The strategy for providing the text response.  
`staticText` |  `string` Optional. The static text response to return when type is STATIC.  
`textResponseInstruction` |  `string` Optional. Instruction for the LLM on how to generate the text response. Used as the description for the text response parameter if type is LLM_GENERATED.  
  
### RemoteAgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "statefulAgent": boolean,
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Required. The description of the tool.  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Required. The agent card of the remote agent that this tool invokes.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent.  
`statefulAgent` |  `boolean` Optional. When enabled, the interaction between the CXAS app and the remote agent will share the same context. If the remote agent returns a context_id, it will be persisted for the entirety of the session for this remote agent tool.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### ToolFakeConfig

JSON representation  
---  
      
    
    {
      "enableFakeMode": boolean,
    
      // Union field tool_response can be only one of the following:
      "codeBlock": {
        object ([CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock))
      }
      // End of list of possible types for union field tool_response.
    }  
  
Fields  
---  
`enableFakeMode` |  `boolean` Optional. Whether the tool is using fake mode.  
Union field `tool_response`. The response is either static or it is provided by a python function. `tool_response` can be only one of the following:  
`codeBlock` |  `object (`[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock)`)` Optional. Code block which will be executed instead of a real tool call.  
  
### CodeBlock

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. Python code which will be invoked in tool fake mode. Expected Python function signature - To catch all tool calls: def fake_tool_call(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: To catch a specific tool call: def fake_{tool_id}(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: If the function returns None, the real tool will be invoked instead.  
  
### Example

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "entryAgent": string,
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "invalid": boolean,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the example. Format: `projects/{project}/locations/{location}/apps/{app}/examples/{example}`  
`displayName` |  `string` Required. Display name of the example.  
`description` |  `string` Optional. Human-readable description of the example.  
`entryAgent` |  `string` Optional. The agent that initially handles the conversation. If not specified, the example represents a conversation that is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message)`)` Optional. The collection of messages that make up the conversation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the example was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the example was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`invalid` |  `boolean` Output only. The example may become invalid if referencing resources are deleted. Invalid examples will not be used as few-shot examples.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
### Message

JSON representation  
---  
      
    
    {
      "role": string,
      "chunks": [
        {
          object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Chunk))
        }
      ],
      "eventTime": string
    }  
  
Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Chunk)`)` Optional. Content of the message as a series of chunks.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `[example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Example)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Chunk

JSON representation  
---  
      
    
    {
    
      // Union field data can be only one of the following:
      "text": string,
      "transcript": string,
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Blob))
      },
      "payload": {
        object
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Image))
      },
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolResponse))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "defaultVariables": {
        object
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
Union field `data`. Chunk data. `data` can be only one of the following:  
`text` |  `string` Optional. Text data.  
`transcript` |  `string` Optional. Transcript associated with the audio.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Blob)`)` Optional. Blob data.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom payload data.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Image)`)` Optional. Image data.  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall)`)` Optional. Tool execution request.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolResponse)`)` Optional. Tool execution response.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AgentTransfer)`)` Optional. Agent transfer event.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`defaultVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents default variables at the start of the conversation, keyed by variable names.  
  
### Blob

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the blob.A base64-encoded string.  
  
### Image

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "altText": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data. Supported image types includes: * image/png * image/jpeg * image/webp  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the image.A base64-encoded string.  
`altText` |  `string` Optional. The alternative text for the image.  
  
### ToolCall

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "args": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `ToolResponse`.  
`displayName` |  `string` Output only. Display name of the tool.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool)`)` Optional. The toolset tool to execute.  
  
### ToolsetTool

JSON representation  
---  
      
    
    {
      "toolset": string,
      "toolId": string
    }  
  
Fields  
---  
`toolset` |  `string` Required. The resource name of the Toolset from which this tool is derived. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`toolId` |  `string` Optional. The tool ID to filter the tools to retrieve the schema for.  
  
### ToolResponse

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "response": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall)` the response is for.  
`displayName` |  `string` Output only. Display name of the tool.  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool)`)` Optional. The toolset tool that got executed.  
  
### AgentTransfer

JSON representation  
---  
      
    
    {
      "targetAgent": string,
      "displayName": string
    }  
  
Fields  
---  
`targetAgent` |  `string` Required. The agent to which the conversation is being transferred. The agent will handle the conversation from this point forward. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Output only. Display name of the agent.  
  
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
  
### Toolset

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)),
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig))
      },
    
      // Union field toolset_type can be only one of the following:
      "mcpToolset": {
        object ([McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolset))
      },
      "openApiToolset": {
        object ([OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.OpenApiToolset))
      },
      "connectorToolset": {
        object ([ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.ConnectorToolset))
      }
      // End of list of possible types for union field toolset_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`displayName` |  `string` Optional. The display name of the toolset. Must be unique within the same app.  
`description` |  `string` Optional. The description of the toolset.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the toolset execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` toolsets and 60 seconds for `ASYNCHRONOUS` toolsets.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the toolset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the toolset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` ETag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)`)` Optional. The execution type of the tools in the toolset.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig)`)` Optional. Configuration for tools behavior in fake mode.  
Union field `toolset_type`. The type of the toolset. `toolset_type` can be only one of the following:  
`mcpToolset` |  `object (`[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolset)`)` Optional. A toolset that contains a list of tools that are offered by the MCP server.  
`openApiToolset` |  `object (`[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.OpenApiToolset)`)` Optional. A toolset that contains a list of tools that are defined by an OpenAPI schema.  
`connectorToolset` |  `object (`[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.ConnectorToolset)`)` Optional. A toolset that generates tools from an Integration Connectors Connection.  
  
### McpToolset

JSON representation  
---  
      
    
    {
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "toolOverrides": [
        {
          object ([McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolOverride))
        }
      ]
    }  
  
Fields  
---  
`serverAddress` |  `string` Required. The address of the MCP server, for example, "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required to access tools and execute a tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`toolOverrides[]` |  `object (`[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolOverride)`)` Optional. Overrides for individual tools within this toolset. This allows overriding specific details like descriptions, names, or pinning the tools' states so they aren't fully dynamic.  
  
### CustomHeadersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### McpToolOverride

JSON representation  
---  
      
    
    {
      "tool": string,
      "nameOverride": string,
      "descriptionOverride": string,
      "snapshot": {
        object ([McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolDefinition))
      }
    }  
  
Fields  
---  
`tool` |  `string` Required. The original name of the tool as it is emitted by the MCP server.  
`nameOverride` |  `string` Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools.  
`descriptionOverride` |  `string` Optional. If present, this tool uses this description instead of the original description from the server.  
`snapshot` |  `object (`[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolDefinition)`)` Output only. If present, this tool is "Pinned" and uses the snapshot values as fallbacks if the server becomes temporarily unavailable or if no Override is present.  
  
### McpToolDefinition

JSON representation  
---  
      
    
    {
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`description` |  `string` Output only. The description of the MCP tool. This can be overridden by `description_override` in `McpToolOverride`.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Output only. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Output only. The schema of the output arguments of the MCP tool.  
  
### OpenApiToolset

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "ignoreUnknownFields": boolean,
      "url": string
    }  
  
Fields  
---  
`openApiSchema` |  `string` Required. The OpenAPI schema of the toolset.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### ConnectorToolset

JSON representation  
---  
      
    
    {
      "connection": string,
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig))
      },
      "connectorActions": [
        {
          object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action))
        }
      ]
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the Toolset creation will fail. See: <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override>  
`connectorActions[]` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action)`)` Required. The list of connector actions/entity operations to generate tools for.  
  
### PrebuiltAmbientNoise

Prebuilt ambient noise.

Enums  
---  
`PREBUILT_AMBIENT_NOISE_UNSPECIFIED` | Not specified.  
`RETAIL_STORE` | Ambient noise of a retail store.  
`CONVENTION_HALL` | Ambient noise of a convention hall.  
`OUTDOOR` | Ambient noise of a street.  
  
### WarningType

Type of warning encountered during voice sample processing.

Enums  
---  
`WARNING_TYPE_UNSPECIFIED` | Unspecified warning type.  
`LOW_AUDIO_LEVEL` | The audio level of the voice sample is too low (e.g. low RMS amplitude).  
  
### VoiceInstructionMode

Instruction mode for the voice sample.

Enums  
---  
`VOICE_INSTRUCTION_MODE_UNSPECIFIED` | Unspecified instruction mode. Defaults to NO_INSTRUCTION.  
`NO_INSTRUCTION` | No voice instruction will be used.  
`GENERATE_INSTRUCTION` | Voice instruction will be automatically generated by AI from the audio sample.  
`CUSTOM_INSTRUCTION` | Custom voice instruction provided by the user.  
  
### ErrorHandlingStrategy

Defines the strategy for handling errors.

Enums  
---  
`ERROR_HANDLING_STRATEGY_UNSPECIFIED` | Unspecified error handling strategy.  
`NONE` | No specific handling is enabled.  
`FALLBACK_RESPONSE` | A fallback message will be returned to the user in case of system errors (e.g. LLM errors).  
`END_SESSION` | An `EndSession` signal will be emitted in case of system errors (e.g. LLM errors).  
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### ToolExecutionMode

Defines the tool execution behavior if there are **multiple** tools being selected by the agent **at the same time**.

Enums  
---  
`TOOL_EXECUTION_MODE_UNSPECIFIED` | Unspecified tool execution mode. Default to PARALLEL.  
`PARALLEL` | If there are multiple tools being selected, they will be executed in parallel, with the same [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context).  
`SEQUENTIAL` | If there are multiple tools being selected, they will be executed sequentially. The next tool will only be executed after the previous tool completes and it can see updated [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context) from the previous tool.  
  
### SemanticSimilarityChannel

Semantic similarity channel to use.

Enums  
---  
`SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED` | Metric unspecified. Defaults to TEXT.  
`TEXT` | Use text semantic similarity.  
`AUDIO` | Use audio semantic similarity.  
  
### ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
### HallucinationMetricBehavior

The hallucination metric behavior. Regardless of the behavior, the metric will always be calculated. The difference is that when disabled, the metric is not used to calculate the overall evaluation score.

Enums  
---  
`HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED` | Unspecified hallucination metric behavior.  
`DISABLED` | Disable hallucination metric.  
`ENABLED` | Enable hallucination metric.  
  
### Type

OpenAPI data types.

Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`STRING` | String type.  
`INTEGER` | Integer type.  
`NUMBER` | Number type.  
`BOOLEAN` | Boolean type.  
`OBJECT` | Object type.  
`ARRAY` | Array type.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Type

The type of the engine. See the documentation available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType> and <https://cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest>.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified engine type.  
`ENGINE_TYPE_SEARCH` | The SOLUTION_TYPE_SEARCH engine for the app. All connector data stores added to the app will be added to this engine.  
`ENGINE_TYPE_CHAT` | Chat engine type. The SOLUTION_TYPE_CHAT engine for the app. All connector data stores added to the app will be added to this engine.  
  
### ChannelType

The type of the channel profile.

Enums  
---  
`UNKNOWN` | Unknown channel type.  
`WEB_UI` | Web UI channel.  
`API` | API channel.  
`TWILIO` | Twilio channel.  
`GOOGLE_TELEPHONY_PLATFORM` | Google Telephony Platform channel.  
`CONTACT_CENTER_AS_A_SERVICE` | Contact Center as a Service (CCaaS) channel.  
`CONTACT_CENTER_AS_A_SERVICE_CHAT` | Contact Center as a Service (CCaaS Chat) channel.  
`FIVE9` | Five9 channel.  
`CONTACT_CENTER_INTEGRATION` | Third party contact center integration channel.  
`WHATSAPP` | WhatsApp channel.  
`INSTAGRAM` | Instagram channel.  
  
### Persona

The persona of the channel.

Enums  
---  
`UNKNOWN` | UNKNOWN persona.  
`CONCISE` | The agent keeps the responses concise and to the point  
`CHATTY` | The agent provides additional context, explanations, and details  
  
### Modality

Modality of the web widget.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`CHAT_AND_VOICE` | Widget supports both chat and voice input.  
`VOICE_ONLY` | Widget supports only voice input.  
`CHAT_ONLY` | Widget supports only chat input.  
`CHAT_VOICE_AND_VIDEO` | Widget supports chat, voice, and video input.  
  
### Theme

Theme of the web widget.

Enums  
---  
`THEME_UNSPECIFIED` | Unknown theme.  
`LIGHT` | Light theme.  
`DARK` | Dark theme.  
  
### RequestLocation

The location of the API key in the request.

Enums  
---  
`REQUEST_LOCATION_UNSPECIFIED` | Unspecified. This value should not be used.  
`HEADER` | Represents the key in http header.  
`QUERY_STRING` | Represents the key in query string.  
  
### OauthGrantType

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

Enums  
---  
`OAUTH_GRANT_TYPE_UNSPECIFIED` | Unspecified. Defaults to CLIENT_CREDENTIAL.  
`CLIENT_CREDENTIAL` | Represents the [client credential flow](https://oauth.net/2/grant-types/client-credentials).  
  
### Direction

The direction of the transfer.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified direction.  
`PARENT_TO_CHILD` | Transfer from the parent agent to the child agent.  
`CHILD_TO_PARENT` | Transfer from the child agent to the parent agent.  
  
### OperationType

The operation to perform on the entity.

Enums  
---  
`OPERATION_TYPE_UNSPECIFIED` | Operation type unspecified. Invalid, ConnectorTool create/update will fail.  
`LIST` | List operation.  
`GET` | Get operation.  
`CREATE` | Create operation.  
`UPDATE` | Update operation.  
`DELETE` | Delete operation.  
  
### DataStoreType

The type of the data store.

Enums  
---  
`DATA_STORE_TYPE_UNSPECIFIED` | Not specified. This value indicates that the data store type is not specified, so it will not be used during search.  
`PUBLIC_WEB` | A data store that contains public web content.  
`UNSTRUCTURED` | A data store that contains unstructured private data.  
`FAQ` | A data store that contains structured data used as FAQ.  
`CONNECTOR` | A data store that is a connector to a first-party or a third-party service.  
  
### DocumentProcessingMode

The document processing mode of the data store.

Enums  
---  
`DOCUMENT_PROCESSING_MODE_UNSPECIFIED` | Not specified.  
`DOCUMENTS` | Documents are processed as documents.  
`CHUNKS` | Documents are converted to chunks.  
  
### AttributeType

The attribute(or function) for which the custom ranking is to be applied.

Enums  
---  
`ATTRIBUTE_TYPE_UNSPECIFIED` | Unspecified AttributeType.  
`NUMERICAL` | The value of the numerical field will be used to dynamically update the boost amount. In this case, the attribute_value (the x value) of the control point will be the actual value of the numerical field for which the boost_amount is specified.  
`FRESHNESS` | For the freshness use case the attribute value will be the duration between the current time and the date in the datetime field specified. The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`. E.g. `5D`, `3DT12H30M`, `T24H`.  
  
### InterpolationType

The interpolation type to be applied. Default will be linear (Piecewise Linear).

Enums  
---  
`INTERPOLATION_TYPE_UNSPECIFIED` | Interpolation type is unspecified. In this case, it defaults to Linear.  
`LINEAR` | Piecewise linear interpolation will be applied.  
  
### ModalityType

The modality type.

Enums  
---  
`MODALITY_TYPE_UNSPECIFIED` | Unspecified modality type.  
`TEXT` | Text modality.  
`AUDIO` | Audio modality.  
  
### FilterParameterBehavior

Filter parameter behavior.

Enums  
---  
`FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED` | Default filter behavior. Include filter parameter for connector datastores. For the rest of the datastore types, the filter input parameter is omitted.  
`ALWAYS_INCLUDE` | Always include filter parameter for all datastore types.  
`NEVER_INCLUDE` | The filter parameter is never included in the list of tool parameters, regardless of the datastore type.  
  
### State

Represents the dynamic availability state of the tool.

Enums  
---  
`STATE_UNSPECIFIED` | Default state.  
`ACTIVE` | The tool is available and actively offered by the server.  
`INACTIVE` | The tool is configured or pinned, but currently not offered by the server.  
`STALE` | The tool exists on the server, but does not match the version on the server.  
  
### CorpusType

The type of the Vertex RAG corpus.

Enums  
---  
`CORPUS_TYPE_UNSPECIFIED` | Unspecified corpus type.  
`USER_OWNED` | The corpus is created and owned by the user.  
`FULLY_MANAGED` | The corpus is created by the agent.  
  
### WidgetType

All available widget types. New values may be added to this enum in the future.

Enums  
---  
`WIDGET_TYPE_UNSPECIFIED` | Unspecified widget type.  
`CUSTOM` | Custom widget type.  
`PRODUCT_CAROUSEL` | Product carousel widget.  
`PRODUCT_DETAILS` | Product details widget.  
`QUICK_ACTIONS` | Quick actions widget.  
`PRODUCT_COMPARISON` | Product comparison widget.  
`ADVANCED_PRODUCT_DETAILS` | Advanced product details widget.  
`SHORT_FORM` | Short form widget.  
`OVERALL_SATISFACTION` | Overall satisfaction widget.  
`ORDER_SUMMARY` | Order summary widget.  
`APPOINTMENT_DETAILS` | Appointment details widget.  
`APPOINTMENT_SCHEDULER` | Appointment scheduler widget.  
`CONTACT_FORM` | Contact form widget.  
  
### Mode

The strategy used to map data from the source tool to the widget.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified mode.  
`FIELD_MAPPING` | Use the `field_mappings` map for data transformation.  
`PYTHON_SCRIPT` | Use the `python_script` for data transformation.  
  
### Type

Defines how the text response is produced.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NONE` | The LLM dynamically decides whether to generate a text response alongside the widget based on the conversation context.  
`LLM_GENERATED` | The LLM is explicitly required to generate a text response.  
`STATIC` | A pre-defined static text response is always used.  
  
### ExecutionType

The execution type of the tool or toolset.

Enums  
---  
`EXECUTION_TYPE_UNSPECIFIED` | The execution type is unspecified. Defaults to `SYNCHRONOUS` if unspecified.  
`SYNCHRONOUS` | The tool is executed synchronously. The session is blocked until the tool returns.  
`ASYNCHRONOUS` | The tool is executed asynchronously. The session will continue while the tool is executing.  
  
### MatchType

Match type for the content filter.

Enums  
---  
`MATCH_TYPE_UNSPECIFIED` | Match type is not specified.  
`SIMPLE_STRING_MATCH` | Content is matched for substrings character by character.  
`WORD_BOUNDARY_STRING_MATCH` | Content only matches if the pattern found in the text is surrounded by word delimiters. Banned phrases can also contain word delimiters.  
`REGEXP_MATCH` | Content is matched using regular expression syntax.  
  
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
  
## Output Schema

In Customer Engagement Suite (CES), an app version is a snapshot of the app at a specific point in time. It is immutable and cannot be modified once created.

### AppVersion

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "creator": string,
      "createTime": string,
      "updateTime": string,
      "snapshot": {
        object ([AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AppSnapshot))
      },
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the app version. Format: `projects/{project}/locations/{location}/apps/{app}/versions/{version}`  
`displayName` |  `string` Optional. The display name of the app version.  
`description` |  `string` Optional. The description of the app version.  
`creator` |  `string` Output only. Email of the user who created the app version.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app version was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app version was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`snapshot` |  `object (`[AppSnapshot](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AppSnapshot)`)` Output only. The snapshot of the app when the version is created.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
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
  
### AppSnapshot

JSON representation  
---  
      
    
    {
      "app": {
        object ([App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.App))
      },
      "agents": [
        {
          object ([Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Agent))
        }
      ],
      "tools": [
        {
          object ([Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Tool))
        }
      ],
      "examples": [
        {
          object ([Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Example))
        }
      ],
      "guardrails": [
        {
          object ([Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Guardrail))
        }
      ],
      "toolsets": [
        {
          object ([Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.Toolset))
        }
      ]
    }  
  
Fields  
---  
`app` |  `object (`[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.App)`)` Optional. The basic settings for the app.  
`agents[]` |  `object (`[Agent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Agent)`)` Optional. List of agents in the app.  
`tools[]` |  `object (`[Tool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Tool)`)` Optional. List of tools in the app.  
`examples[]` |  `object (`[Example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Example)`)` Optional. List of examples in the app.  
`guardrails[]` |  `object (`[Guardrail](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_guardrails#Output.Schema.Guardrail)`)` Optional. List of guardrails in the app.  
`toolsets[]` |  `object (`[Toolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.Toolset)`)` Optional. List of toolsets in the app.  
  
### App

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "pinned": boolean,
      "rootAgent": string,
      "languageSettings": {
        object ([LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LanguageSettings))
      },
      "timeZoneSettings": {
        object ([TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TimeZoneSettings))
      },
      "audioProcessingConfig": {
        object ([AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioProcessingConfig))
      },
      "loggingSettings": {
        object ([LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LoggingSettings))
      },
      "errorHandlingSettings": {
        object ([ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingSettings))
      },
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "toolExecutionMode": enum ([ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolExecutionMode)),
      "evaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EvaluationMetricsThresholds))
      },
      "variableDeclarations": [
        {
          object ([VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration))
        }
      ],
      "predefinedVariableDeclarations": [
        {
          object ([VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration))
        }
      ],
      "globalInstruction": string,
      "guardrails": [
        string
      ],
      "dataStoreSettings": {
        object ([DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DataStoreSettings))
      },
      "defaultChannelProfile": {
        object ([ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile))
      },
      "metadata": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "deploymentCount": integer,
      "clientCertificateSettings": {
        object ([ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ClientCertificateSettings))
      },
      "vpcScSettings": {
        object ([VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VpcScSettings))
      },
      "locked": boolean,
      "validationErrors": [
        string
      ],
      "dashboardSettings": {
        object ([DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DashboardSettings))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`displayName` |  `string` Required. Display name of the app.  
`description` |  `string` Optional. Human-readable description of the app.  
`pinned` |  `boolean` Optional. Whether the app is pinned in the app list.  
`rootAgent` |  `string` Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`languageSettings` |  `object (`[LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LanguageSettings)`)` Optional. Language settings of the app.  
`timeZoneSettings` |  `object (`[TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TimeZoneSettings)`)` Optional. TimeZone settings of the app.  
`audioProcessingConfig` |  `object (`[AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioProcessingConfig)`)` Optional. Audio processing configuration of the app.  
`loggingSettings` |  `object (`[LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.LoggingSettings)`)` Optional. Logging settings of the app.  
`errorHandlingSettings` |  `object (`[ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingSettings)`)` Optional. Error handling settings of the app.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed.  
`toolExecutionMode` |  `enum (`[ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolExecutionMode)`)` Optional. The tool execution mode for the app. If not provided, will default to PARALLEL.  
`evaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EvaluationMetricsThresholds)`)` Optional. The evaluation thresholds for the app.  
`variableDeclarations[]` |  `object (`[VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration)`)` Optional. The declarations of the variables.  
`predefinedVariableDeclarations[]` |  `object (`[VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VariableDeclaration)`)` Output only. The declarations of predefined variables for the app.  
`globalInstruction` |  `string` Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents.  
`guardrails[]` |  `string` Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`dataStoreSettings` |  `object (`[DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DataStoreSettings)`)` Optional. The data store settings for the app.  
`defaultChannelProfile` |  `object (`[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelProfile)`)` Optional. The default channel profile used by the app.  
`metadata` |  `map (key: string, value: string)` Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`deploymentCount` |  `integer` Output only. Number of deployments in the app.  
`clientCertificateSettings` |  `object (`[ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ClientCertificateSettings)`)` Optional. The default client certificate settings for the app.  
`vpcScSettings` |  `object (`[VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VpcScSettings)`)` Optional. VPC-SC settings for the app.  
`locked` |  `boolean` Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected.  
`validationErrors[]` |  `string` Output only. Misconfigurations or warnings in the app.  
`dashboardSettings` |  `object (`[DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.DashboardSettings)`)` Optional. App-specific dashboard settings for linking and configuring Contact Center Insights dashboards.  
  
### LanguageSettings

JSON representation  
---  
      
    
    {
      "defaultLanguageCode": string,
      "supportedLanguageCodes": [
        string
      ],
      "enableMultilingualSupport": boolean,
      "fallbackAction": string
    }  
  
Fields  
---  
`defaultLanguageCode` |  `string` Optional. The default language code of the app.  
`supportedLanguageCodes[]` |  `string` Optional. List of languages codes supported by the app, in addition to the `default_language_code`.  
`enableMultilingualSupport` |  `boolean` Optional. Enables multilingual support. If true, agents in the app will use pre-built instructions to improve handling of multilingual input.  
`fallbackAction  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: This feature is no longer supported. Use `enable_multilingual_support` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.This can be a predefined action or a custom tool call. Valid values are: - A tool's full resource name, which triggers a specific tool execution. - A predefined system action, such as "escalate" or "exit", which triggers an `EndSession` signal with corresponding `metadata` to terminate the conversation.  
  
### TimeZoneSettings

JSON representation  
---  
      
    
    {
      "timeZone": string
    }  
  
Fields  
---  
`timeZone` |  `string` Optional. The time zone of the app from the [time zone database](https://www.iana.org/time-zones), e.g., America/Los_Angeles, Europe/Paris.  
  
### AudioProcessingConfig

JSON representation  
---  
      
    
    {
      "synthesizeSpeechConfigs": {
        string: {
          object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig))
        },
        ...
      },
      "bargeInConfig": {
        object ([BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BargeInConfig))
      },
      "inactivityTimeout": string,
      "ambientSoundConfig": {
        object ([AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AmbientSoundConfig))
      },
      "customVoiceSamples": [
        {
          object ([CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CustomVoiceSample))
        }
      ]
    }  
  
Fields  
---  
`synthesizeSpeechConfigs` |  `map (key: string, value: object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig)`))` Optional. Configuration of how the agent response should be synthesized, mapping from the language code to `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig)`.If the configuration for the specified language code is not found, the configuration for the root language code will be used. For example, if the map contains "en-us" and "en", and the specified language code is "en-gb", then "en" configuration will be used.Note: Language code is case-insensitive.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`bargeInConfig` |  `object (`[BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BargeInConfig)`)` Optional. Configures the agent behavior for the user barge-in activities.  
`inactivityTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The duration of user inactivity (no speech or interaction) before the agent prompts the user for reengagement. If not set, the agent will not prompt the user for reengagement.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`ambientSoundConfig` |  `object (`[AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AmbientSoundConfig)`)` Optional. Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.  
`customVoiceSamples[]` |  `object (`[CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CustomVoiceSample)`)` Optional. Configures custom voice samples for voice cloning.  
  
### SynthesizeSpeechConfigsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SynthesizeSpeechConfig)`)`  
  
### SynthesizeSpeechConfig

JSON representation  
---  
      
    
    {
      "voice": string,
      "speakingRate": number,
      "model": string,
      "instruction": string
    }  
  
Fields  
---  
`voice` |  `string` Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as language_code.For the list of available voices, please refer to [Supported voices and languages](https://cloud.google.com/text-to-speech/docs/voices) from Cloud Text-to-Speech.  
`speakingRate` |  `number` Optional. The speaking rate/speed in the range [0.25, 2.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. Values outside of the range [0.25, 2.0] will return an error.  
`model` |  `string` Optional. The model used to synthesize audio. Currently supported values: - "gemini-3.1-flash-tts-preview" If empty, Chirp3-HD is used.  
`instruction` |  `string` Optional. The instruction used to synthesize speech when using a generative model.  
  
### BargeInConfig

JSON representation  
---  
      
    
    {
      "disableBargeIn": boolean,
      "bargeInAwareness": boolean
    }  
  
Fields  
---  
`disableBargeIn  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: `disable_barge_in` is deprecated in favor of ``disable_barge_in_control`` in ChannelProfile.Disables user barge-in while the agent is speaking. If true, user input during agent response playback will be ignored.  
`bargeInAwareness` |  `boolean` Optional. If enabled, the agent will adapt its next response based on the assumption that the user hasn't heard the full preceding agent message. This should not be used in scenarios where agent responses are displayed visually.  
  
### Duration

JSON representation  
---  
      
    
    {
      "seconds": string,
      "nanos": integer
    }  
  
Fields  
---  
`seconds` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Signed seconds of the span of time. Must be from -315,576,000,000 to +315,576,000,000 inclusive. Note: these bounds are computed from: 60 sec/min * 60 min/hr * 24 hr/day * 365.25 days/year * 10000 years  
`nanos` |  `integer` Signed fractions of a second at nanosecond resolution of the span of time. Durations less than one second are represented with a 0 `seconds` field and a positive or negative `nanos` field. For durations of one second or more, a non-zero value for the `nanos` field must be of the same sign as the `seconds` field. Must be from -999,999,999 to +999,999,999 inclusive.  
  
### AmbientSoundConfig

JSON representation  
---  
      
    
    {
      "volumeGainDb": number,
    
      // Union field source can be only one of the following:
      "prebuiltAmbientNoise": enum ([PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PrebuiltAmbientNoise)),
      "gcsUri": string,
      "prebuiltAmbientSound": string
      // End of list of possible types for union field source.
    }  
  
Fields  
---  
`volumeGainDb` |  `number` Optional. Volume gain (in dB) of the normal native volume supported by ambient noise, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.  
Union field `source`. Ambient noise to be played with the synthesized agent response, to enhance the naturalness of the conversation. `source` can be only one of the following:  
`prebuiltAmbientNoise  
**(deprecated)**` |  `enum (`[PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PrebuiltAmbientNoise)`)` This item is deprecated!Optional. Deprecated: `prebuilt_ambient_noise` is deprecated in favor of `prebuilt_ambient_sound`.  
`gcsUri` |  `string` Optional. Ambient noise as a mono-channel, 16kHz WAV file stored in [Cloud Storage](https://cloud.google.com/storage).Note: Please make sure the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com` has `storage.objects.get` permission to the Cloud Storage object.  
`prebuiltAmbientSound` |  `string` Optional. Name of the prebuilt ambient sound. Valid values are: - "coffee_shop" - "keyboard" - "keypad" - "hum" - "office_1" - "office_2" - "office_3" - "room_1" - "room_2" - "room_3" - "room_4" - "room_5" - "air_conditioner"  
  
### CustomVoiceSample

JSON representation  
---  
      
    
    {
      "name": string,
      "voiceSampleGcsUri": string,
      "consentAudioGcsUri": string,
      "voiceInstruction": string,
      "previewAudioContent": string,
      "previewText": string,
      "warnings": [
        {
          object ([Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Warning))
        }
      ],
      "voiceInstructionMode": enum ([VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VoiceInstructionMode))
    }  
  
Fields  
---  
`name` |  `string` Optional. The user-defined name for the custom voice sample.  
`voiceSampleGcsUri` |  `string` Optional. The Cloud Storage URI to the audio sample for voice cloning. The audio sample should be a mono-channel, 24kHz WAV file.  
`consentAudioGcsUri` |  `string` Optional. Consent audio for voice cloning.  
`voiceInstruction` |  `string` Optional. Natural language instructions for voice style, tone, pacing, or pronunciation.  
`previewAudioContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Synthesized preview audio for custom voice, formatted as canonical WAV (LINEAR16, 24kHz, 16-bit, mono).A base64-encoded string.  
`previewText` |  `string` Optional. Text for synthesizing preview audio for custom voice.  
`warnings[]` |  `object (`[Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Warning)`)` Output only. Warning messages encountered during voice clone processing (e.g. low audio level).  
`voiceInstructionMode` |  `enum (`[VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.VoiceInstructionMode)`)` Optional. Instruction mode for the voice sample. If unspecified, defaults to NO_INSTRUCTION.  
  
### Warning

JSON representation  
---  
      
    
    {
      "message": string,
      "type": enum ([WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WarningType))
    }  
  
Fields  
---  
`message` |  `string` Output only. A human-readable description of the warning.  
`type` |  `enum (`[WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WarningType)`)` Output only. The type of the warning.  
  
### LoggingSettings

JSON representation  
---  
      
    
    {
      "redactionConfig": {
        object ([RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.RedactionConfig))
      },
      "audioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig))
      },
      "unredactedAudioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig))
      },
      "bigqueryExportSettings": {
        object ([BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings))
      },
      "unredactedBigqueryExportSettings": {
        object ([BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings))
      },
      "cloudLoggingSettings": {
        object ([CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CloudLoggingSettings))
      },
      "conversationLoggingSettings": {
        object ([ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ConversationLoggingSettings))
      },
      "evaluationAudioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig))
      },
      "metricAnalysisSettings": {
        object ([MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.MetricAnalysisSettings))
      }
    }  
  
Fields  
---  
`redactionConfig` |  `object (`[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.RedactionConfig)`)` Optional. Configuration for how sensitive data should be redacted.  
`audioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig)`)` Optional. Configuration for how audio interactions should be recorded. The audio is subject to redaction as configured in `RedactionConfig`.  
`unredactedAudioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig)`)` Optional. Configures an additional recording of unredacted audio. This can be used to maintain a raw audio copy when audio redaction is `enabled`, typically for auditing or monitoring purposes.  
`bigqueryExportSettings` |  `object (`[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings)`)` Optional. Configures the BigQuery export behaviors for the app. The conversation data is subject to redaction as configured in `RedactionConfig`.  
`unredactedBigqueryExportSettings` |  `object (`[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.BigQueryExportSettings)`)` Optional. Configures the BigQuery export behaviors for the app. The unredacted conversation data will be exported to BigQuery tables if it is enabled.  
`cloudLoggingSettings` |  `object (`[CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.CloudLoggingSettings)`)` Optional. Settings to describe the Cloud Logging behaviors for the app.  
`conversationLoggingSettings` |  `object (`[ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ConversationLoggingSettings)`)` Optional. Settings to describe the conversation logging behaviors for the app.  
`evaluationAudioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.AudioRecordingConfig)`)` Optional. Configuration for how audio interactions should be recorded for the evaluation. By default, audio recording is not enabled for evaluation sessions.  
`metricAnalysisSettings` |  `object (`[MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.MetricAnalysisSettings)`)` Optional. Settings to describe the conversation data collection behaviors for the LLM analysis pipeline for the app.  
  
### RedactionConfig

JSON representation  
---  
      
    
    {
      "enableRedaction": boolean,
      "inspectTemplate": string,
      "deidentifyTemplate": string
    }  
  
Fields  
---  
`enableRedaction` |  `boolean` Optional. If true, redaction will be applied in various logging scenarios, including conversation history, Cloud Logging and audio recording.  
`inspectTemplate` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) inspect template name to configure detection of sensitive data types.Format: `projects/{project}/locations/{location}/inspectTemplates/{inspect_template}`  
`deidentifyTemplate` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) deidentify template name to instruct on how to de-identify content.Format: `projects/{project}/locations/{location}/deidentifyTemplates/{deidentify_template}`  
  
### AudioRecordingConfig

JSON representation  
---  
      
    
    {
      "gcsBucket": string,
      "gcsPathPrefix": string
    }  
  
Fields  
---  
`gcsBucket` |  `string` Optional. The [Cloud Storage](https://cloud.google.com/storage) bucket to store the session audio recordings. The URI must start with "gs://".Please choose a bucket location that meets your data residency requirements.Note: If the Cloud Storage bucket is in a different project from the app, you should grant `storage.objects.create` permission to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`gcsPathPrefix` |  `string` Optional. The Cloud Storage path prefix for audio recordings.This prefix can include the following placeholders, which will be dynamically substituted at serving time: - $project: project ID - $location: app location - $app: app ID - $date: session date in YYYY-MM-DD format - $session: session IDIf the path prefix is not specified, the default prefix `$project/$location/$app/$date/$session/` will be used.  
  
### BigQueryExportSettings

JSON representation  
---  
      
    
    {
      "enabled": boolean,
      "project": string,
      "dataset": string
    }  
  
Fields  
---  
`enabled` |  `boolean` Optional. Indicates whether the BigQuery export is enabled.  
`project` |  `string` Optional. The **project ID** of the BigQuery dataset to export the data to.Note: If the BigQuery dataset is in a different project from the app, you should grant `roles/bigquery.admin` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`dataset` |  `string` Optional. The BigQuery **dataset ID** to export the data to.  
  
### CloudLoggingSettings

JSON representation  
---  
      
    
    {
      "enableCloudLogging": boolean
    }  
  
Fields  
---  
`enableCloudLogging` |  `boolean` Optional. Whether to enable Cloud Logging for the sessions.  
  
### ConversationLoggingSettings

JSON representation  
---  
      
    
    {
      "disableConversationLogging": boolean,
      "retentionWindow": string
    }  
  
Fields  
---  
`disableConversationLogging` |  `boolean` Optional. Whether to disable conversation logging for the sessions.  
`retentionWindow` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Controls the retention window for the conversation. If not set, the conversation will be retained for 365 days.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
### MetricAnalysisSettings

JSON representation  
---  
      
    
    {
      "llmMetricsOptedOut": boolean
    }  
  
Fields  
---  
`llmMetricsOptedOut` |  `boolean` Optional. Whether to collect conversation data for llm analysis metrics. If true, conversation data will not be collected for llm analysis metrics; otherwise, conversation data will be collected.  
  
### ErrorHandlingSettings

JSON representation  
---  
      
    
    {
      "errorHandlingStrategy": enum ([ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingStrategy)),
      "fallbackResponseConfig": {
        object ([FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.FallbackResponseConfig))
      },
      "endSessionConfig": {
        object ([EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EndSessionConfig))
      }
    }  
  
Fields  
---  
`errorHandlingStrategy` |  `enum (`[ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ErrorHandlingStrategy)`)` Optional. The strategy to use for error handling.  
`fallbackResponseConfig` |  `object (`[FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.FallbackResponseConfig)`)` Optional. Configuration for handling fallback responses.  
`endSessionConfig` |  `object (`[EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.EndSessionConfig)`)` Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).  
  
### FallbackResponseConfig

JSON representation  
---  
      
    
    {
      "customFallbackMessages": {
        string: string,
        ...
      },
      "maxFallbackAttempts": integer
    }  
  
Fields  
---  
`customFallbackMessages` |  `map (key: string, value: string)` Optional. The fallback messages in case of system errors (e.g. LLM errors), mapped by [supported language code](https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/reference/language).An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`maxFallbackAttempts` |  `integer` Optional. The maximum number of fallback attempts to make before the agent emitting `EndSession` Signal.  
  
### CustomFallbackMessagesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### EndSessionConfig

JSON representation  
---  
      
    
    {
    
      // Union field _escalate_session can be only one of the following:
      "escalateSession": boolean
      // End of list of possible types for union field _escalate_session.
    }  
  
Fields  
---  
Union field `_escalate_session`.`_escalate_session` can be only one of the following:  
`escalateSession` |  `boolean` Optional. Whether to escalate the session in `EndSession`. If session is escalated, `metadata in EndSession` will contain `session_escalated = true`. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#transfer_a_call_to_a_human_agent> for details.  
  
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
  
### EvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "goldenEvaluationMetricsThresholds": {
        object ([GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.GoldenEvaluationMetricsThresholds))
      },
      "hallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)),
      "goldenHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)),
      "scenarioHallucinationMetricBehavior": enum ([HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`goldenEvaluationMetricsThresholds` |  `object (`[GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.GoldenEvaluationMetricsThresholds)`)` Optional. The golden evaluation metrics thresholds.  
`hallucinationMetricBehavior  
**(deprecated)**` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)`)` This item is deprecated!Optional. Deprecated: Use `golden_hallucination_metric_behavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`goldenHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for golden evaluations.  
`scenarioHallucinationMetricBehavior` |  `enum (`[HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for scenario evaluations.  
  
### GoldenEvaluationMetricsThresholds

JSON representation  
---  
      
    
    {
      "turnLevelMetricsThresholds": {
        object ([TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TurnLevelMetricsThresholds))
      },
      "expectationLevelMetricsThresholds": {
        object ([ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExpectationLevelMetricsThresholds))
      },
      "toolMatchingSettings": {
        object ([ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolMatchingSettings))
      }
    }  
  
Fields  
---  
`turnLevelMetricsThresholds` |  `object (`[TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.TurnLevelMetricsThresholds)`)` Optional. The turn level metrics thresholds.  
`expectationLevelMetricsThresholds` |  `object (`[ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExpectationLevelMetricsThresholds)`)` Optional. The expectation level metrics thresholds.  
`toolMatchingSettings` |  `object (`[ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ToolMatchingSettings)`)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
### TurnLevelMetricsThresholds

JSON representation  
---  
      
    
    {
      "semanticSimilarityChannel": enum ([SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SemanticSimilarityChannel)),
    
      // Union field _semantic_similarity_success_threshold can be only one of the
      // following:
      "semanticSimilaritySuccessThreshold": integer
      // End of list of possible types for union field
      // _semantic_similarity_success_threshold.
    
      // Union field _overall_tool_invocation_correctness_threshold can be only one
      // of the following:
      "overallToolInvocationCorrectnessThreshold": number
      // End of list of possible types for union field
      // _overall_tool_invocation_correctness_threshold.
    }  
  
Fields  
---  
`semanticSimilarityChannel` |  `enum (`[SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SemanticSimilarityChannel)`)` Optional. The semantic similarity channel to use for evaluation.  
Union field `_semantic_similarity_success_threshold`.`_semantic_similarity_success_threshold` can be only one of the following:  
`semanticSimilaritySuccessThreshold` |  `integer` Optional. The success threshold for semantic similarity. Must be an integer between 0 and 4. Default is >= 3.  
Union field `_overall_tool_invocation_correctness_threshold`.`_overall_tool_invocation_correctness_threshold` can be only one of the following:  
`overallToolInvocationCorrectnessThreshold` |  `number` Optional. The success threshold for overall tool invocation correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### ExpectationLevelMetricsThresholds

JSON representation  
---  
      
    
    {
    
      // Union field _tool_invocation_parameter_correctness_threshold can be only one
      // of the following:
      "toolInvocationParameterCorrectnessThreshold": number
      // End of list of possible types for union field
      // _tool_invocation_parameter_correctness_threshold.
    }  
  
Fields  
---  
Union field `_tool_invocation_parameter_correctness_threshold`.`_tool_invocation_parameter_correctness_threshold` can be only one of the following:  
`toolInvocationParameterCorrectnessThreshold` |  `number` Optional. The success threshold for individual tool invocation parameter correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### ToolMatchingSettings

JSON representation  
---  
      
    
    {
      "extraToolCallBehavior": enum ([ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExtraToolCallBehavior))
    }  
  
Fields  
---  
`extraToolCallBehavior` |  `enum (`[ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ExtraToolCallBehavior)`)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
### VariableDeclaration

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the variable. The name must start with a letter or underscore and contain only letters, numbers, or underscores.  
`description` |  `string` Required. The description of the variable.  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Required. The schema of the variable.  
  
### Schema

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)),
      "properties": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "required": [
        string
      ],
      "description": string,
      "items": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "nullable": boolean,
      "uniqueItems": boolean,
      "prefixItems": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "additionalProperties": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "anyOf": [
        {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        }
      ],
      "enum": [
        string
      ],
      "default": value,
      "ref": string,
      "defs": {
        string: {
          object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
        },
        ...
      },
      "title": string,
      "minItems": string,
      "maxItems": string,
    
      // Union field _minimum can be only one of the following:
      "minimum": number
      // End of list of possible types for union field _minimum.
    
      // Union field _maximum can be only one of the following:
      "maximum": number
      // End of list of possible types for union field _maximum.
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type)`)` Required. The type of the data.  
`properties` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. Properties of Type.OBJECT.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`required[]` |  `string` Optional. Required properties of Type.OBJECT.  
`description` |  `string` Optional. The description of the data.  
`items` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schema of the elements of Type.ARRAY.  
`nullable` |  `boolean` Optional. Indicates if the value may be null.  
`uniqueItems` |  `boolean` Optional. Indicate the items in the array must be unique. Only applies to TYPE.ARRAY.  
`prefixItems[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Schemas of initial elements of Type.ARRAY.  
`additionalProperties` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. Can either be a boolean or an object, controls the presence of additional properties.  
`anyOf[]` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The value should be validated against any (one or more) of the subschemas in the list.  
`enum[]` |  `string` Optional. Possible values of the element of primitive type with enum format. Examples: 1. We can define direction as : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH", "WEST"]} 2. We can define apartment number as : {type:INTEGER, format:enum, enum:["101", "201", "301"]}  
`default` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Optional. Default value of the data.  
`ref` |  `string` Optional. Allows indirect references between schema nodes. The value should be a valid reference to a child of the root `defs`.For example, the following schema defines a reference to a schema node named "Pet":
    
    
    type: object
    properties:
      pet:
        ref: #/defs/Pet
    defs:
      Pet:
        type: object
        properties:
          name:
            type: string
    

The value of the "pet" property is a reference to the schema node named "Pet". See details in <https://json-schema.org/understanding-json-schema/structuring>.  
`defs` |  `map (key: string, value: object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`))` Optional. A map of definitions for use by `ref`. Only allowed at the root of the schema.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`title` |  `string` Optional. The title of the schema.  
`minItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Minimum number of the elements for Type.ARRAY.  
`maxItems` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Maximum number of the elements for Type.ARRAY.  
Union field `_minimum`.`_minimum` can be only one of the following:  
`minimum` |  `number` Optional. Minimum value for Type.INTEGER and Type.NUMBER.  
Union field `_maximum`.`_maximum` can be only one of the following:  
`maximum` |  `number` Optional. Maximum value for Type.INTEGER and Type.NUMBER.  
  
### PropertiesEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
### Value

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "nullValue": null,
      "numberValue": number,
      "stringValue": string,
      "boolValue": boolean,
      "structValue": {
        object
      },
      "listValue": array
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The kind of value. `kind` can be only one of the following:  
`nullValue` |  `null` Represents a JSON `null`.  
`numberValue` |  `number` Represents a JSON number. Must not be `NaN`, `Infinity` or `-Infinity`, since those are not supported in JSON. This also cannot represent large Int64 values, since JSON format generally does not support them in its number type.  
`stringValue` |  `string` Represents a JSON string.  
`boolValue` |  `boolean` Represents a JSON boolean (`true` or `false` literal in JSON).  
`structValue` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Represents a JSON object.  
`listValue` |  `array (`[ListValue](https://protobuf.dev/reference/protobuf/google.protobuf/#list-value)` format)` Represents a JSON array.  
  
### Struct

JSON representation  
---  
      
    
    {
      "fields": {
        string: value,
        ...
      }
    }  
  
Fields  
---  
`fields` |  `map (key: string, value: value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format))` Unordered map of dynamically typed values.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### FieldsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": value
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)`  
  
### ListValue

JSON representation  
---  
      
    
    {
      "values": [
        value
      ]
    }  
  
Fields  
---  
`values[]` |  `value (`[Value](https://protobuf.dev/reference/protobuf/google.protobuf/#value)` format)` Repeated field of dynamically typed values.  
  
### DefsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)`  
  
### DataStoreSettings

JSON representation  
---  
      
    
    {
      "engines": [
        {
          object ([Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Engine))
        }
      ]
    }  
  
Fields  
---  
`engines[]` |  `object (`[Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Engine)`)` Output only. The engines for the app.  
  
### Engine

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type_1))
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Type_1)`)` Output only. The type of the engine.  
  
### ChannelProfile

JSON representation  
---  
      
    
    {
      "profileId": string,
      "channelType": enum ([ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)),
      "personaProperty": {
        object ([PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty))
      },
      "webWidgetConfig": {
        object ([WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig))
      },
      "whatsappConfig": {
        object ([WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig))
      },
      "instagramConfig": {
        object ([InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig))
      },
    
      // Union field _disable_dtmf can be only one of the following:
      "disableDtmf": boolean
      // End of list of possible types for union field _disable_dtmf.
    
      // Union field _disable_barge_in_control can be only one of the following:
      "disableBargeInControl": boolean
      // End of list of possible types for union field _disable_barge_in_control.
    
      // Union field _noise_suppression_level can be only one of the following:
      "noiseSuppressionLevel": string
      // End of list of possible types for union field _noise_suppression_level.
    }  
  
Fields  
---  
`profileId` |  `string` Optional. The unique identifier of the channel profile.  
`channelType` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ChannelType)`)` Optional. The type of the channel profile.  
`personaProperty` |  `object (`[PersonaProperty](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.PersonaProperty)`)` Optional. The persona property of the channel profile.  
`webWidgetConfig` |  `object (`[WebWidgetConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WebWidgetConfig)`)` Optional. The configuration for the web widget.  
`whatsappConfig` |  `object (`[WhatsAppConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.WhatsAppConfig)`)` Optional. Configuration specific to WhatsApp deployments.  
`instagramConfig` |  `object (`[InstagramConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.InstagramConfig)`)` Optional. Configuration specific to Instagram deployments.  
Union field `_disable_dtmf`.`_disable_dtmf` can be only one of the following:  
`disableDtmf` |  `boolean` Optional. Whether to disable DTMF (dual-tone multi-frequency).  
Union field `_disable_barge_in_control`.`_disable_barge_in_control` can be only one of the following:  
`disableBargeInControl` |  `boolean` Optional. Whether to disable user barge-in control in the conversation. - **true** : User interruptions are disabled while the agent is speaking. - **false** : The agent retains automatic control over when the user can interrupt.  
Union field `_noise_suppression_level`.`_noise_suppression_level` can be only one of the following:  
`noiseSuppressionLevel` |  `string` Optional. The noise suppression level of the channel profile. Available values are "low", "moderate", "high", "very_high".  
  
### PersonaProperty

JSON representation  
---  
      
    
    {
      "persona": enum ([Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona))
    }  
  
Fields  
---  
`persona` |  `enum (`[Persona](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Persona)`)` Optional. The persona of the channel.  
  
### WebWidgetConfig

JSON representation  
---  
      
    
    {
      "modality": enum ([Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)),
      "theme": enum ([Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)),
      "webWidgetTitle": string,
      "securitySettings": {
        object ([SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings))
      }
    }  
  
Fields  
---  
`modality` |  `enum (`[Modality](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Modality)`)` Optional. The modality of the web widget.  
`theme` |  `enum (`[Theme](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Theme)`)` Optional. The theme of the web widget.  
`webWidgetTitle` |  `string` Optional. The title of the web widget.  
`securitySettings` |  `object (`[SecuritySettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.SecuritySettings)`)` Optional. The security settings of the web widget.  
  
### SecuritySettings

JSON representation  
---  
      
    
    {
      "enablePublicAccess": boolean,
      "enableOriginCheck": boolean,
      "allowedOrigins": [
        string
      ],
      "enableRecaptcha": boolean
    }  
  
Fields  
---  
`enablePublicAccess` |  `boolean` Optional. Indicates whether public access to the web widget is enabled. If `true`, the web widget will be publicly accessible. If `false`, the web widget must be integrated with your own authentication and authorization system to return valid credentials for accessing the CES agent.  
`enableOriginCheck` |  `boolean` Optional. Indicates whether origin check for the web widget is enabled. If `true`, the web widget will check the origin of the website that loads the web widget and only allow it to be loaded in the same origin or any of the allowed origins.  
`allowedOrigins[]` |  `string` Optional. The origins that are allowed to host the web widget. An origin is defined by RFC 6454. If empty, all origins are allowed. A maximum of 100 origins is allowed. Example: "https://example.com"  
`enableRecaptcha` |  `boolean` Optional. Indicates whether reCAPTCHA verification for the web widget is enabled.  
  
### WhatsAppConfig

JSON representation  
---  
      
    
    {
      "wabaId": string,
      "phoneNumberId": string,
      "phoneNumber": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`wabaId` |  `string` Required. The WhatsApp Business Account ID.  
`phoneNumberId` |  `string` Required. The Meta phone number ID.  
`phoneNumber` |  `string` Optional. The phone number in E.164 format.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### InstagramConfig

JSON representation  
---  
      
    
    {
      "instagramAccountId": string,
      "displayName": string,
      "thumbnailUrl": string,
      "description": string
    }  
  
Fields  
---  
`instagramAccountId` |  `string` Required. The Instagram Account ID.  
`displayName` |  `string` Output only. The fetched Meta business page name.  
`thumbnailUrl` |  `string` Output only. The fetched Meta business profile thumbnail URL.  
`description` |  `string` Output only. The description of the Meta business page or profile.  
  
### MetadataEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### ClientCertificateSettings

JSON representation  
---  
      
    
    {
      "tlsCertificate": string,
      "privateKey": string,
      "passphrase": string
    }  
  
Fields  
---  
`tlsCertificate` |  `string` Required. The TLS certificate encoded in PEM format. This string must include the begin header and end footer lines.  
`privateKey` |  `string` Required. The name of the SecretManager secret version resource storing the private key encoded in PEM format. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`passphrase` |  `string` Optional. The name of the SecretManager secret version resource storing the passphrase to decrypt the private key. Should be left unset if the private key is not encrypted. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
  
### VpcScSettings

JSON representation  
---  
      
    
    {
      "allowedOrigins": [
        string
      ]
    }  
  
Fields  
---  
`allowedOrigins[]` |  `string` Optional. The allowed HTTP(s) origins that OpenAPI tools in the App are able to directly call when VPC Service Controls are enabled. These strings must match the origin exactly, including the port if specified. For example, "https://example.com" or "https://example.com:443". This list does not yet apply to Python tools that may make direct HTTP calls.  
  
### DashboardSettings

JSON representation  
---  
      
    
    {
      "defaultDashboard": string
    }  
  
Fields  
---  
`defaultDashboard` |  `string` Optional. The resource name of the default Contact Center Insights dashboard associated with the app. This is the dashboard that will be displayed when users navigate to the Monitoring view for the app.Format: `projects/{project}/locations/{location}/dashboards/{dashboard}`  
  
### Agent

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
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
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterAgentCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterModelCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "beforeToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
        }
      ],
      "afterToolCallbacks": [
        {
          object ([Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback))
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
          object ([AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset))
        }
      ],
      "generatedSummary": string,
      "transferRules": [
        {
          object ([TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule))
        }
      ],
      "validationErrors": [
        string
      ],
    
      // Union field agent_type can be only one of the following:
      "llmAgent": {
        object (LlmAgent)
      },
      "remoteDialogflowAgent": {
        object ([RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent))
      },
      "remoteA2aAgent": {
        object ([RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent))
      }
      // End of list of possible types for union field agent_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Required. Display name of the agent.  
`description` |  `string` Optional. Human-readable description of the agent.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`instruction` |  `string` Optional. Instructions for the LLM model to guide the agent's behavior.  
`tools[]` |  `string` Optional. List of available tools for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`childAgents[]` |  `string` Optional. List of child agents in the agent tree. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`beforeAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterAgentCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the agent is called. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterModelCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the model is called. If there are multiple calls to the model, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`beforeToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute before the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`afterToolCallbacks[]` |  `object (`[Callback](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Callback)`)` Optional. The callbacks to execute after the tool is invoked. If there are multiple tool invocations, the callback will be executed multiple times. The provided callbacks are executed sequentially in the exact order they are given in the list. If a callback returns an overridden response, execution stops and any remaining callbacks are skipped.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the agent was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`guardrails[]` |  `string` Optional. List of guardrails for the agent. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`toolsets[]` |  `object (`[AgentToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentToolset)`)` Optional. List of toolsets for the agent.  
`generatedSummary` |  `string` Output only. If the agent is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`transferRules[]` |  `object (`[TransferRule](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.TransferRule)`)` Optional. Agent transfer rules. If multiple rules match, the first one in the list will be used.  
`validationErrors[]` |  `string` Output only. Misconfigurations or errors in the agent that may affect agent quality.  
Union field `agent_type`. The type of agent. `agent_type` can be only one of the following:  
`llmAgent` |  `object (`LlmAgent`)` Optional. The default agent type.  
`remoteDialogflowAgent` |  `object (`[RemoteDialogflowAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteDialogflowAgent)`)` Optional. The remote [Dialogflow](https://cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents) agent to be used for the agent execution. If this field is set, all other agent level properties will be ignored.Note: If the Dialogflow agent is in a different project from the app, you should grant `roles/dialogflow.client` to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`remoteA2aAgent` |  `object (`[RemoteA2aAgent](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aAgent)`)` Optional. The remote [A2A](https://github.com/a2aproject/A2A) agent to be used for the agent execution.  
  
### RemoteDialogflowAgent

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
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### RemoteA2aAgent

JSON representation  
---  
      
    
    {
      "a2aConfig": {
        object ([RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig))
      }
    }  
  
Fields  
---  
`a2aConfig` |  `object (`[RemoteA2aConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RemoteA2aConfig)`)` Required. The A2A connection configuration.  
  
### RemoteA2aConfig

JSON representation  
---  
      
    
    {
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
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
    
      // Union field agent_spec can be only one of the following:
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "agentRegistry": string
      // End of list of possible types for union field agent_spec.
    }  
  
Fields  
---  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent. Optional if the registry reference already handles authentication.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`streamingEnabled` |  `boolean` Optional. Whether streaming is enabled for the remote agent.  
`contextId` |  `string` Optional. If not empty, interactions with the remote A2A agent will use this context ID. This context_id field can refer to a session variable like `$context.variables.order_agent_session_id`.  
Union field `agent_spec`. Specification of the remote agent. `agent_spec` can be only one of the following:  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Optional. The full agent card defined inline.  
`agentRegistry` |  `string` Optional. Reference to the agent in the Agent Registry. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
### AgentCard

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "supportedInterfaces": [
        {
          object ([AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface))
        }
      ],
      "version": string,
      "skills": [
        {
          object ([AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Required. A human-readable name for the agent.  
`description` |  `string` Required. A description of the agent's domain of action/solution space.  
`supportedInterfaces[]` |  `object (`[AgentInterface](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentInterface)`)` Required. Ordered list of supported interfaces. The first entry is preferred.  
`version` |  `string` Required. The version of the agent.  
`skills[]` |  `object (`[AgentSkill](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentSkill)`)` Required. Skills represent a unit of ability an agent can perform. This may somewhat abstract but represents a more focused set of actions that the agent is highly likely to succeed at.  
  
### AgentInterface

JSON representation  
---  
      
    
    {
      "url": string,
      "protocolBinding": string,
      "tenant": string,
      "protocolVersion": string
    }  
  
Fields  
---  
`url` |  `string` Required. The URL where this interface is available. Must be a valid absolute HTTPS URL in production. Example: "https://api.example.com/a2a/v1", "https://grpc.example.com/a2a"  
`protocolBinding` |  `string` Required. The protocol binding supported at this URL. This is an open form string, to be easily extended for other protocol bindings. The core ones officially supported are `JSONRPC`, `GRPC` and `HTTP+JSON`.  
`tenant` |  `string` Tenant ID to be used in the request when calling the agent.  
`protocolVersion` |  `string` Required. The version of the A2A protocol this interface exposes. Use the latest supported minor version per major version. Examples: "0.3", "1.0"  
  
### AgentSkill

JSON representation  
---  
      
    
    {
      "id": string,
      "name": string,
      "description": string,
      "tags": [
        string
      ],
      "examples": [
        string
      ],
      "inputModes": [
        string
      ],
      "outputModes": [
        string
      ]
    }  
  
Fields  
---  
`id` |  `string` Required. A unique identifier for the agent's skill.  
`name` |  `string` Required. A human-readable name for the skill.  
`description` |  `string` Required. A detailed description of the skill.  
`tags[]` |  `string` Required. A set of keywords describing the skill's capabilities.  
`examples[]` |  `string` Example prompts or scenarios that this skill can handle.  
`inputModes[]` |  `string` The set of supported input media types for this skill, overriding the agent's defaults.  
`outputModes[]` |  `string` The set of supported output media types for this skill, overriding the agent's defaults.  
  
### ApiAuthentication

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "apiKeyConfig": {
        object ([ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig))
      },
      "oauthConfig": {
        object ([OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig))
      },
      "serviceAgentIdTokenAuthConfig": {
        object (ServiceAgentIdTokenAuthConfig)
      },
      "serviceAccountAuthConfig": {
        object ([ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig))
      },
      "bearerTokenConfig": {
        object ([BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`apiKeyConfig` |  `object (`[ApiKeyConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiKeyConfig)`)` Optional. Config for API key auth.  
`oauthConfig` |  `object (`[OAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OAuthConfig)`)` Optional. Config for OAuth.  
`serviceAgentIdTokenAuthConfig` |  `object (`ServiceAgentIdTokenAuthConfig`)` Optional. Config for ID token auth generated from CES service agent.  
`serviceAccountAuthConfig` |  `object (`[ServiceAccountAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ServiceAccountAuthConfig)`)` Optional. Config for service account authentication.  
`bearerTokenConfig` |  `object (`[BearerTokenConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.BearerTokenConfig)`)` Optional. Config for bearer token auth.  
  
### ApiKeyConfig

JSON representation  
---  
      
    
    {
      "keyName": string,
      "apiKeySecretVersion": string,
      "requestLocation": enum ([RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation))
    }  
  
Fields  
---  
`keyName` |  `string` Required. The parameter name or the header name of the API key. E.g., If the API request is "https://example.com/act?X-Api-Key=", "X-Api-Key" would be the parameter name.  
`apiKeySecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the API key. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`requestLocation` |  `enum (`[RequestLocation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.RequestLocation)`)` Required. Key location in the request.  
  
### OAuthConfig

JSON representation  
---  
      
    
    {
      "oauthGrantType": enum ([OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)),
      "clientId": string,
      "clientSecretVersion": string,
      "tokenEndpoint": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`oauthGrantType` |  `enum (`[OauthGrantType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.OauthGrantType)`)` Required. OAuth grant types.  
`clientId` |  `string` Required. The client ID from the OAuth provider.  
`clientSecretVersion` |  `string` Required. The name of the SecretManager secret version resource storing the client secret. Format: `projects/{project}/secrets/{secret}/versions/{version}`Note: You should grant `roles/secretmanager.secretAccessor` role to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`tokenEndpoint` |  `string` Required. The token endpoint in the OAuth provider to exchange for an access token.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant.  
  
### ServiceAccountAuthConfig

JSON representation  
---  
      
    
    {
      "serviceAccount": string,
      "scopes": [
        string
      ]
    }  
  
Fields  
---  
`serviceAccount` |  `string` Required. The email address of the service account used for authentication. CES uses this service account to exchange an access token and the access token is then sent in the `Authorization` header of the request.The service account must have the `roles/iam.serviceAccountTokenCreator` role granted to the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com`.  
`scopes[]` |  `string` Optional. The OAuth scopes to grant. If not specified, the default scope `https://www.googleapis.com/auth/cloud-platform` is used.  
  
### BearerTokenConfig

JSON representation  
---  
      
    
    {
      "token": string
    }  
  
Fields  
---  
`token` |  `string` Required. The bearer token. Must be in the format `$context.variables.<name_of_variable>`.  
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
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
  
### AgentToolset

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

JSON representation  
---  
      
    
    {
      "childAgent": string,
      "direction": enum ([Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)),
    
      // Union field rule_type can be only one of the following:
      "deterministicTransfer": {
        object ([DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer))
      },
      "disablePlannerTransfer": {
        object ([DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer))
      }
      // End of list of possible types for union field rule_type.
    }  
  
Fields  
---  
`childAgent` |  `string` Required. The resource name of the child agent the rule applies to. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`direction` |  `enum (`[Direction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.Direction)`)` Required. The direction of the transfer.  
Union field `rule_type`. The rule type. `rule_type` can be only one of the following:  
`deterministicTransfer` |  `object (`[DeterministicTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DeterministicTransfer)`)` Optional. A rule that immediately transfers to the target agent when the condition is met.  
`disablePlannerTransfer` |  `object (`[DisablePlannerTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.DisablePlannerTransfer)`)` Optional. Rule that prevents the planner from transferring to the target agent.  
  
### DeterministicTransfer

JSON representation  
---  
      
    
    {
    
      // Union field condition_type can be only one of the following:
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      },
      "pythonCodeCondition": {
        object ([PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition))
      }
      // End of list of possible types for union field condition_type.
    }  
  
Fields  
---  
Union field `condition_type`. The condition to evaluate. `condition_type` can be only one of the following:  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Optional. A rule that evaluates a session state condition. If the condition evaluates to true, the transfer occurs.  
`pythonCodeCondition` |  `object (`[PythonCodeCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.PythonCodeCondition)`)` Optional. A rule that uses Python code block to evaluate the conditions. If the condition evaluates to true, the transfer occurs.  
  
### ExpressionCondition

JSON representation  
---  
      
    
    {
      "expression": string
    }  
  
Fields  
---  
`expression` |  `string` Required. The string representation of cloud.api.Expression condition.  
  
### PythonCodeCondition

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. The python code to execute.  
  
### DisablePlannerTransfer

JSON representation  
---  
      
    
    {
      "expressionCondition": {
        object ([ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition))
      }
    }  
  
Fields  
---  
`expressionCondition` |  `object (`[ExpressionCondition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ExpressionCondition)`)` Required. If the condition evaluates to true, planner will not be allowed to transfer to the target agent.  
  
### Tool

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)),
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "generatedSummary": string,
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig))
      },
      "readOnly": boolean,
    
      // Union field tool_type can be only one of the following:
      "clientFunction": {
        object ([ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction))
      },
      "openApiTool": {
        object ([OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool))
      },
      "googleSearchTool": {
        object ([GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool))
      },
      "connectorTool": {
        object ([ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool))
      },
      "dataStoreTool": {
        object ([DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool))
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mcpTool": {
        object ([McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool))
      },
      "fileSearchTool": {
        object ([FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool))
      },
      "systemTool": {
        object ([SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool))
      },
      "agentTool": {
        object ([AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool))
      },
      "widgetTool": {
        object ([WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool))
      },
      "remoteAgentTool": {
        object ([RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool))
      }
      // End of list of possible types for union field tool_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the tool. Format:

  * `projects/{project}/locations/{location}/apps/{app}/tools/{tool}` for standalone tools.
  * `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}/tools/{tool}` for tools retrieved from a toolset.

These tools are dynamic and output-only; they cannot be referenced directly where a tool is expected.  
`displayName` |  `string` Output only. The display name of the tool, derived based on the tool's type. For example, display name of a [ClientFunction][Tool.ClientFunction] is derived from its `name` property.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)`)` Optional. The execution type of the tool.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the tool execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` tools and 60 seconds for `ASYNCHRONOUS` tools.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the tool was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`generatedSummary` |  `string` Output only. If the tool is generated by the LLM assistant, this field contains a descriptive summary of the generation.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig)`)` Optional. Configuration for tool behavior in fake mode.  
`readOnly` |  `boolean` Output only. Indicates whether the tool is read-only. If true, the tool cannot be modified by the user.  
Union field `tool_type`. The type of the tool. `tool_type` can be only one of the following:  
`clientFunction` |  `object (`[ClientFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ClientFunction)`)` Optional. The client function.  
`openApiTool` |  `object (`[OpenApiTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OpenApiTool)`)` Optional. The open API tool.  
`googleSearchTool` |  `object (`[GoogleSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GoogleSearchTool)`)` Optional. The google search tool.  
`connectorTool` |  `object (`[ConnectorTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorTool)`)` Optional. The Integration Connector tool.  
`dataStoreTool` |  `object (`[DataStoreTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreTool)`)` Optional. The data store tool.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. The python function tool.  
`mcpTool` |  `object (`[McpTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.McpTool)`)` Optional. The MCP tool. An MCP tool cannot be created or updated directly and is managed by the MCP toolset.  
`fileSearchTool` |  `object (`[FileSearchTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FileSearchTool)`)` Optional. The file search tool.  
`systemTool` |  `object (`[SystemTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SystemTool)`)` Optional. The system tool.  
`agentTool` |  `object (`[AgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AgentTool)`)` Optional. The agent tool.  
`widgetTool` |  `object (`[WidgetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetTool)`)` Optional. The widget tool.  
`remoteAgentTool` |  `object (`[RemoteAgentTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RemoteAgentTool)`)` Optional. The remote agent tool.  
  
### ClientFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "response": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The function name.  
`description` |  `string` Optional. The function description.  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function parameters.  
`response` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the function response.  
  
### OpenApiTool

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "name": string,
      "description": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "ignoreUnknownFields": boolean,
      "url": string
    }  
  
Fields  
---  
`openApiSchema` |  `string` Required. The OpenAPI schema in JSON or YAML format.  
`name` |  `string` Optional. The name of the tool. If not provided, the name of the tool will be derived from the OpenAPI schema, from `operation.operationId`.  
`description` |  `string` Optional. The description of the tool. If not provided, the description of the tool will be derived from the OpenAPI schema, from `operation.description` or `operation.summary`.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client will trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in tools in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### TlsConfig

JSON representation  
---  
      
    
    {
      "caCerts": [
        {
          object ([CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert))
        }
      ]
    }  
  
Fields  
---  
`caCerts[]` |  `object (`[CaCert](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CaCert)`)` Required. Specifies a list of allowed custom CA certificates for HTTPS verification.  
  
### CaCert

JSON representation  
---  
      
    
    {
      "displayName": string,
      "cert": string
    }  
  
Fields  
---  
`displayName` |  `string` Required. The name of the allowed custom CA certificates. This can be used to disambiguate the custom CA certificates.  
`cert` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. The allowed custom CA certificates (in DER format) for HTTPS verification. This overrides the default SSL trust store. If this is empty or unspecified, CES will use Google's default trust store to verify certificates. N.B. Make sure the HTTPS server certificates are signed with "subject alt name". For instance a certificate can be self-signed using the following command:
    
    
       openssl x509 -req -days 200 -in example.com.csr \
         -signkey example.com.key \
         -out example.com.crt \
         -extfile <(printf "\nsubjectAltName='DNS:www.example.com'")
    

A base64-encoded string.  
  
### ServiceDirectoryConfig

JSON representation  
---  
      
    
    {
      "service": string
    }  
  
Fields  
---  
`service` |  `string` Required. The name of [Service Directory](https://cloud.google.com/service-directory) service. Format: `projects/{project}/locations/{location}/namespaces/{namespace}/services/{service}`. Location of the service directory must be the same as the location of the app.  
  
### GoogleSearchTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "contextUrls": [
        string
      ],
      "preferredDomains": [
        string
      ],
      "excludeDomains": [
        string
      ],
      "promptConfig": {
        object ([PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`contextUrls[]` |  `string` Optional. Content will be fetched directly from these URLs for context and grounding. Example: "https://example.com/path.html". A maximum of 20 URLs are allowed.  
`preferredDomains[]` |  `string` Optional. Specifies domains to restrict search results to. Example: "example.com", "another.site". A maximum of 20 domains can be specified.  
`excludeDomains[]` |  `string` Optional. List of domains to be excluded from the search results. Example: "example.com". A maximum of 2000 domains can be excluded.  
`promptConfig` |  `object (`[PromptConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PromptConfig)`)` Optional. Prompt instructions passed to planner on how the search results should be processed for text and voice.  
  
### PromptConfig

JSON representation  
---  
      
    
    {
      "textPrompt": string,
      "voicePrompt": string
    }  
  
Fields  
---  
`textPrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in chat conversations. If not set, default prompt will be used.  
`voicePrompt` |  `string` Optional. Defines the prompt used for the system instructions when interacting with the agent in voice conversations. If not set, default prompt will be used.  
  
### ConnectorTool

JSON representation  
---  
      
    
    {
      "connection": string,
      "action": {
        object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action))
      },
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig))
      },
      "name": string,
      "description": string
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`action` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action)`)` Required. Action for the tool to use.  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the ConnectorTool creation will fail. See <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override> for details.  
`name` |  `string` Optional. The name of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
`description` |  `string` Optional. The description of the tool that can be used by the Agent to decide whether to call this ConnectorTool.  
  
### Action

JSON representation  
---  
      
    
    {
      "inputFields": [
        string
      ],
      "outputFields": [
        string
      ],
    
      // Union field action_spec can be only one of the following:
      "connectionActionId": string,
      "entityOperation": {
        object ([EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation))
      }
      // End of list of possible types for union field action_spec.
    }  
  
Fields  
---  
`inputFields[]` |  `string` Optional. Entity fields to use as inputs for the operation. If no fields are specified, all fields of the Entity will be used.  
`outputFields[]` |  `string` Optional. Entity fields to return from the operation. If no fields are specified, all fields of the Entity will be returned.  
Union field `action_spec`. Specification for an action to configure for the tool to use. `action_spec` can be only one of the following:  
`connectionActionId` |  `string` ID of a Connection action for the tool to use.  
`entityOperation` |  `object (`[EntityOperation](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EntityOperation)`)` Entity operation configuration for the tool to use.  
  
### EntityOperation

JSON representation  
---  
      
    
    {
      "entityId": string,
      "operation": enum ([OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType))
    }  
  
Fields  
---  
`entityId` |  `string` Required. ID of the entity.  
`operation` |  `enum (`[OperationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.OperationType)`)` Required. Operation to perform on the entity.  
  
### EndUserAuthConfig

JSON representation  
---  
      
    
    {
    
      // Union field auth_config can be only one of the following:
      "oauth2AuthCodeConfig": {
        object ([Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig))
      },
      "oauth2JwtBearerConfig": {
        object ([Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig))
      }
      // End of list of possible types for union field auth_config.
    }  
  
Fields  
---  
Union field `auth_config`. The auth configuration. `auth_config` can be only one of the following:  
`oauth2AuthCodeConfig` |  `object (`[Oauth2AuthCodeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2AuthCodeConfig)`)` Oauth 2.0 Authorization Code authentication.  
`oauth2JwtBearerConfig` |  `object (`[Oauth2JwtBearerConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Oauth2JwtBearerConfig)`)` JWT Profile Oauth 2.0 Authorization Grant authentication.  
  
### Oauth2AuthCodeConfig

JSON representation  
---  
      
    
    {
      "oauthToken": string
    }  
  
Fields  
---  
`oauthToken` |  `string` Required. Oauth token parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### Oauth2JwtBearerConfig

JSON representation  
---  
      
    
    {
      "issuer": string,
      "subject": string,
      "clientKey": string
    }  
  
Fields  
---  
`issuer` |  `string` Required. Issuer parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`subject` |  `string` Required. Subject parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
`clientKey` |  `string` Required. Client parameter name to pass through. Must be in the format `$context.variables.<name_of_variable>`.  
  
### DataStoreTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "boostSpecs": [
        {
          object ([BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs))
        }
      ],
      "modalityConfigs": [
        {
          object ([ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig))
        }
      ],
      "filterParameterBehavior": enum ([FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)),
    
      // Union field search_source can be only one of the following:
      "dataStoreSource": {
        object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
      },
      "engineSource": {
        object ([EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource))
      }
      // End of list of possible types for union field search_source.
    }  
  
Fields  
---  
`name` |  `string` Required. The data store tool name.  
`description` |  `string` Optional. The tool description.  
`boostSpecs[]` |  `object (`[BoostSpecs](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpecs)`)` Optional. Boost specification to boost certain documents.  
`modalityConfigs[]` |  `object (`[ModalityConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityConfig)`)` Optional. The modality configs for the data store.  
`filterParameterBehavior` |  `enum (`[FilterParameterBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.FilterParameterBehavior)`)` Optional. The filter parameter behavior.  
Union field `search_source`. Defines the search source, either a single DataStore or an Engine. `search_source` can be only one of the following:  
`dataStoreSource` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Search within a single specific DataStore.  
`engineSource` |  `object (`[EngineSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EngineSource)`)` Optional. Search within an Engine (potentially across multiple DataStores).  
  
### DataStoreSource

JSON representation  
---  
      
    
    {
      "filter": string,
      "dataStore": {
        object ([DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore))
      }
    }  
  
Fields  
---  
`filter` |  `string` Optional. Filter specification for the DataStore. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
`dataStore` |  `object (`[DataStore](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStore)`)` Optional. The data store.  
  
### DataStore

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)),
      "documentProcessingMode": enum ([DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)),
      "displayName": string,
      "createTime": string,
      "connectorConfig": {
        object ([ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. Full resource name of the DataStore. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`  
`type` |  `enum (`[DataStoreType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreType)`)` Output only. The type of the data store. This field is readonly and populated by the server.  
`documentProcessingMode` |  `enum (`[DocumentProcessingMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DocumentProcessingMode)`)` Output only. The document processing mode for the data store connection. Only set for PUBLIC_WEB and UNSTRUCTURED data stores.  
`displayName` |  `string` Output only. The display name of the data store.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the data store was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`connectorConfig` |  `object (`[ConnectorConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConnectorConfig)`)` Output only. The connector config for the data store connection.  
  
### ConnectorConfig

JSON representation  
---  
      
    
    {
      "collection": string,
      "collectionDisplayName": string,
      "dataSource": string
    }  
  
Fields  
---  
`collection` |  `string` Resource name of the collection the data store belongs to.  
`collectionDisplayName` |  `string` Display name of the collection the data store belongs to.  
`dataSource` |  `string` The name of the data source. Example: `salesforce`, `jira`, `confluence`, `bigquery`.  
  
### EngineSource

JSON representation  
---  
      
    
    {
      "engine": string,
      "dataStoreSources": [
        {
          object ([DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource))
        }
      ],
      "filter": string
    }  
  
Fields  
---  
`engine` |  `string` Required. Full resource name of the Engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`dataStoreSources[]` |  `object (`[DataStoreSource](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataStoreSource)`)` Optional. Use to target specific DataStores within the Engine. If empty, the search applies to all DataStores associated with the Engine.  
`filter` |  `string` Optional. A filter applied to the search across the Engine. Not relevant and not used if 'data_store_sources' is provided. See: <https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata>  
  
### BoostSpecs

JSON representation  
---  
      
    
    {
      "dataStores": [
        string
      ],
      "spec": [
        {
          object ([BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec))
        }
      ]
    }  
  
Fields  
---  
`dataStores[]` |  `string` Required. The Data Store where the boosting configuration is applied. Full resource name of DataStore, such as projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}.  
`spec[]` |  `object (`[BoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostSpec)`)` Required. A list of boosting specifications.  
  
### BoostSpec

JSON representation  
---  
      
    
    {
      "conditionBoostSpecs": [
        {
          object ([ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec))
        }
      ]
    }  
  
Fields  
---  
`conditionBoostSpecs[]` |  `object (`[ConditionBoostSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ConditionBoostSpec)`)` Required. A list of boosting specifications.  
  
### ConditionBoostSpec

JSON representation  
---  
      
    
    {
      "condition": string,
      "boost": number,
      "boostControlSpec": {
        object ([BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec))
      }
    }  
  
Fields  
---  
`condition` |  `string` Required. An expression which specifies a boost condition. The syntax is the same as filter expression syntax. Currently, the only supported condition is a list of BCP-47 lang codes. Example: To boost suggestions in languages en or fr: (lang_code: ANY("en", "fr"))  
`boost` |  `number` Optional. Strength of the boost, which should be in [-1, 1]. Negative boost means demotion. Default is 0.0.Setting to 1.0 gives the suggestions a big promotion. However, it does not necessarily mean that the top result will be a boosted suggestion.Setting to -1.0 gives the suggestions a big demotion. However, other suggestions that are relevant might still be shown.Setting to 0.0 means no boost applied. The boosting condition is ignored.  
`boostControlSpec` |  `object (`[BoostControlSpec](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.BoostControlSpec)`)` Optional. Complex specification for custom ranking based on customer defined attribute value.  
  
### BoostControlSpec

JSON representation  
---  
      
    
    {
      "fieldName": string,
      "attributeType": enum ([AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)),
      "interpolationType": enum ([InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)),
      "controlPoints": [
        {
          object ([ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint))
        }
      ]
    }  
  
Fields  
---  
`fieldName` |  `string` Optional. The name of the field whose value will be used to determine the boost amount.  
`attributeType` |  `enum (`[AttributeType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.AttributeType)`)` Optional. The attribute type to be used to determine the boost amount. The attribute value can be derived from the field value of the specified field_name. In the case of numerical it is straightforward i.e. attribute_value = numerical_field_value. In the case of freshness however, attribute_value = (time.now() - datetime_field_value).  
`interpolationType` |  `enum (`[InterpolationType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.InterpolationType)`)` Optional. The interpolation type to be applied to connect the control points listed below.  
`controlPoints[]` |  `object (`[ControlPoint](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ControlPoint)`)` Optional. The control points used to define the curve. The monotonic function (defined through the interpolation_type above) passes through the control points listed here.  
  
### ControlPoint

JSON representation  
---  
      
    
    {
      "attributeValue": string,
      "boostAmount": number
    }  
  
Fields  
---  
`attributeValue` |  `string` Optional. Can be one of: 1. The numerical field value. 2. The duration spec for freshness: The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`.  
`boostAmount` |  `number` Optional. The value between -1 to 1 by which to boost the score if the attribute_value evaluates to the value specified above.  
  
### ModalityConfig

JSON representation  
---  
      
    
    {
      "modalityType": enum ([ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)),
      "rewriterConfig": {
        object ([RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig))
      },
      "summarizationConfig": {
        object ([SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig))
      },
      "groundingConfig": {
        object ([GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig))
      },
      "snippetsConfig": {
        object ([SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig))
      }
    }  
  
Fields  
---  
`modalityType` |  `enum (`[ModalityType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ModalityType)`)` Required. The modality type.  
`rewriterConfig` |  `object (`[RewriterConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.RewriterConfig)`)` Optional. The rewriter config.  
`summarizationConfig` |  `object (`[SummarizationConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SummarizationConfig)`)` Optional. The summarization config.  
`groundingConfig` |  `object (`[GroundingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.GroundingConfig)`)` Optional. The grounding configuration.  
`snippetsConfig` |  `object (`[SnippetsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.SnippetsConfig)`)` Optional. The snippets configuration.  
  
### RewriterConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Required. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether the rewriter is disabled.  
  
### SummarizationConfig

JSON representation  
---  
      
    
    {
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings))
      },
      "prompt": string,
      "disabled": boolean
    }  
  
Fields  
---  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.ModelSettings)`)` Optional. Configurations for the LLM model.  
`prompt` |  `string` Optional. The prompt definition. If not set, default prompt will be used.  
`disabled` |  `boolean` Optional. Whether summarization is disabled.  
  
### GroundingConfig

JSON representation  
---  
      
    
    {
      "groundingLevel": number,
      "disabled": boolean
    }  
  
Fields  
---  
`groundingLevel` |  `number` Optional. The groundedness threshold of the answer based on the retrieved sources. The value has a configurable range of [1, 5]. The level is used to threshold the groundedness of the answer, meaning that all responses with a groundedness score below the threshold will fall back to returning relevant snippets only.For example, a level of 3 means that the groundedness score must be 3 or higher for the response to be returned.  
`disabled` |  `boolean` Optional. Whether grounding is disabled.  
  
### SnippetsConfig

JSON representation  
---  
      
    
    {
      "enableSnippets": boolean,
      "maxSnippets": integer
    }  
  
Fields  
---  
`enableSnippets` |  `boolean` Optional. Whether snippets are enabled.  
`maxSnippets` |  `integer` Optional. Number of snippets to return per query. If unset, returns all snippets from the service by default.  
  
### PythonFunction

JSON representation  
---  
      
    
    {
      "name": string,
      "pythonCode": string,
      "description": string,
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the Python function to execute. Must match a Python function name defined in the python code. Case sensitive. If the name is not provided, the first function defined in the python code will be used.  
`pythonCode` |  `string` Optional. The Python code to execute for the tool.  
`description` |  `string` Output only. The description of the Python function, parsed from the python code's docstring.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for the tool.  
  
### McpTool

JSON representation  
---  
      
    
    {
      "name": string,
      "nameOverride": string,
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State))
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the MCP tool.  
`nameOverride` |  `string` Optional. The name override of the MCP tool. This is populated if the name was overridden by a Toolset override.  
`description` |  `string` Optional. The description of the MCP tool.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The schema of the output arguments of the MCP tool.  
`serverAddress` |  `string` Required. The server address of the MCP server, e.g., "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. This is the same as the server_address in the McpToolset. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required to execute the tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.State)`)` Output only. The dynamic availability state of the tool on the external server.  
  
### CustomHeadersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### FileSearchTool

JSON representation  
---  
      
    
    {
      "corpusType": enum ([CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)),
      "name": string,
      "description": string,
      "fileCorpus": string
    }  
  
Fields  
---  
`corpusType` |  `enum (`[CorpusType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CorpusType)`)` Optional. The type of the corpus. Default is FULLY_MANAGED.  
`name` |  `string` Required. The tool name.  
`description` |  `string` Optional. The tool description.  
`fileCorpus` |  `string` Optional. The corpus where files are stored. Format: projects/{project}/locations/{location}/ragCorpora/{rag_corpus}  
  
### SystemTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the system tool.  
`description` |  `string` Output only. The description of the system tool.  
  
### AgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agent": string
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the agent tool.  
`description` |  `string` Optional. Description of the tool's purpose.  
`agent` |  `string` Optional. The resource name of the agent that is the entry point of the tool. Format: `projects/{project}/locations/{location}/agents/{agent}`  
  
### WidgetTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "widgetType": enum ([WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)),
      "uiConfig": {
        object
      },
      "dataMapping": {
        object ([DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping))
      },
      "textResponseConfig": {
        object ([TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig))
      },
    
      // Union field input can be only one of the following:
      "parameters": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
      // End of list of possible types for union field input.
    }  
  
Fields  
---  
`name` |  `string` Required. The display name of the widget tool.  
`description` |  `string` Optional. The description of the widget tool.  
`widgetType` |  `enum (`[WidgetType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.WidgetType)`)` Optional. The type of the widget tool. If not specified, the default type will be CUSTOMIZED.  
`uiConfig` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Configuration for rendering the widget.  
`dataMapping` |  `object (`[DataMapping](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.DataMapping)`)` Optional. The mapping that defines how data from a source tool is mapped to the widget's input parameters.  
`textResponseConfig` |  `object (`[TextResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TextResponseConfig)`)` Optional. Configuration for always-included text responses.  
Union field `input`. The input of the widget tool. `input` can be only one of the following:  
`parameters` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Optional. The input parameters of the widget tool.  
  
### DataMapping

JSON representation  
---  
      
    
    {
      "sourceToolName": string,
      "fieldMappings": {
        string: string,
        ...
      },
      "pythonFunction": {
        object ([PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction))
      },
      "mode": enum ([Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)),
      "pythonScript": string
    }  
  
Fields  
---  
`sourceToolName` |  `string` Optional. The resource name of the tool that provides the data for the widget (e.g., a search tool or a custom function). Format: `projects/{project}/locations/{location}/agents/{agent}/tools/{tool}`  
`fieldMappings` |  `map (key: string, value: string)` Optional. A map of widget input parameter fields to the corresponding output fields of the source tool.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`pythonFunction` |  `object (`[PythonFunction](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.PythonFunction)`)` Optional. Configuration for a Python function used to transform the source tool's output into the widget's input format.  
`mode` |  `enum (`[Mode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Mode)`)` Optional. The mode of the data mapping.  
`pythonScript  
**(deprecated)**` |  `string` This item is deprecated!Deprecated: Use `python_function` instead.  
  
### FieldMappingsEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### TextResponseConfig

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)),
      "staticText": string,
      "textResponseInstruction": string
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Type_1)`)` Optional. The strategy for providing the text response.  
`staticText` |  `string` Optional. The static text response to return when type is STATIC.  
`textResponseInstruction` |  `string` Optional. Instruction for the LLM on how to generate the text response. Used as the description for the text response parameter if type is LLM_GENERATED.  
  
### RemoteAgentTool

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agentCard": {
        object ([AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard))
      },
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "statefulAgent": boolean,
      "inputVariableMapping": {
        string: string,
        ...
      },
      "outputVariableMapping": {
        string: string,
        ...
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the tool.  
`description` |  `string` Required. The description of the tool.  
`agentCard` |  `object (`[AgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.AgentCard)`)` Required. The agent card of the remote agent that this tool invokes.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication configuration for calling the remote agent.  
`statefulAgent` |  `boolean` Optional. When enabled, the interaction between the CXAS app and the remote agent will share the same context. If the remote agent returns a context_id, it will be persisted for the entirety of the session for this remote agent tool.  
`inputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of input variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`outputVariableMapping` |  `map (key: string, value: string)` Optional. Mapping of output variable names of remote agent to GECX variable names.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### InputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### OutputVariableMappingEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### ToolFakeConfig

JSON representation  
---  
      
    
    {
      "enableFakeMode": boolean,
    
      // Union field tool_response can be only one of the following:
      "codeBlock": {
        object ([CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock))
      }
      // End of list of possible types for union field tool_response.
    }  
  
Fields  
---  
`enableFakeMode` |  `boolean` Optional. Whether the tool is using fake mode.  
Union field `tool_response`. The response is either static or it is provided by a python function. `tool_response` can be only one of the following:  
`codeBlock` |  `object (`[CodeBlock](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.CodeBlock)`)` Optional. Code block which will be executed instead of a real tool call.  
  
### CodeBlock

JSON representation  
---  
      
    
    {
      "pythonCode": string
    }  
  
Fields  
---  
`pythonCode` |  `string` Required. Python code which will be invoked in tool fake mode. Expected Python function signature - To catch all tool calls: def fake_tool_call(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: To catch a specific tool call: def fake_{tool_id}(tool: Tool, input: dict[str, Any], callback_context: CallbackContext) -> Optional[dict[str, Any]]: If the function returns None, the real tool will be invoked instead.  
  
### Example

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "entryAgent": string,
      "messages": [
        {
          object ([Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message))
        }
      ],
      "createTime": string,
      "updateTime": string,
      "invalid": boolean,
      "etag": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the example. Format: `projects/{project}/locations/{location}/apps/{app}/examples/{example}`  
`displayName` |  `string` Required. Display name of the example.  
`description` |  `string` Optional. Human-readable description of the example.  
`entryAgent` |  `string` Optional. The agent that initially handles the conversation. If not specified, the example represents a conversation that is handled by the root agent. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`messages[]` |  `object (`[Message](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Message)`)` Optional. The collection of messages that make up the conversation.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the example was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the example was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`invalid` |  `boolean` Output only. The example may become invalid if referencing resources are deleted. Invalid examples will not be used as few-shot examples.  
`etag` |  `string` Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
  
### Message

JSON representation  
---  
      
    
    {
      "role": string,
      "chunks": [
        {
          object ([Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Chunk))
        }
      ],
      "eventTime": string
    }  
  
Fields  
---  
`role` |  `string` Optional. The role within the conversation, e.g., user, agent.  
`chunks[]` |  `object (`[Chunk](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Chunk)`)` Optional. Content of the message as a series of chunks.  
`eventTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Timestamp when the message was sent or received. Should not be used if the message is part of an `[example](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Example)`.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
### Chunk

JSON representation  
---  
      
    
    {
    
      // Union field data can be only one of the following:
      "text": string,
      "transcript": string,
      "blob": {
        object ([Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Blob))
      },
      "payload": {
        object
      },
      "image": {
        object ([Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Image))
      },
      "toolCall": {
        object ([ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall))
      },
      "toolResponse": {
        object ([ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolResponse))
      },
      "agentTransfer": {
        object ([AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AgentTransfer))
      },
      "updatedVariables": {
        object
      },
      "defaultVariables": {
        object
      }
      // End of list of possible types for union field data.
    }  
  
Fields  
---  
Union field `data`. Chunk data. `data` can be only one of the following:  
`text` |  `string` Optional. Text data.  
`transcript` |  `string` Optional. Transcript associated with the audio.  
`blob` |  `object (`[Blob](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Blob)`)` Optional. Blob data.  
`payload` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Custom payload data.  
`image` |  `object (`[Image](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.Image)`)` Optional. Image data.  
`toolCall` |  `object (`[ToolCall](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall)`)` Optional. Tool execution request.  
`toolResponse` |  `object (`[ToolResponse](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolResponse)`)` Optional. Tool execution response.  
`agentTransfer` |  `object (`[AgentTransfer](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.AgentTransfer)`)` Optional. Agent transfer event.  
`updatedVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents variables that were updated in the conversation, keyed by variable names.  
`defaultVariables` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` A struct represents default variables at the start of the conversation, keyed by variable names.  
  
### Blob

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data.  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the blob.A base64-encoded string.  
  
### Image

JSON representation  
---  
      
    
    {
      "mimeType": string,
      "data": string,
      "altText": string
    }  
  
Fields  
---  
`mimeType` |  `string` Required. The IANA standard MIME type of the source data. Supported image types includes: * image/png * image/jpeg * image/webp  
`data` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Raw bytes of the image.A base64-encoded string.  
`altText` |  `string` Optional. The alternative text for the image.  
  
### ToolCall

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "args": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The unique identifier of the tool call. If populated, the client should return the execution result with the matching ID in `ToolResponse`.  
`displayName` |  `string` Output only. Display name of the tool.  
`args` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. The input parameters and values for the tool in JSON object format.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool to execute. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool)`)` Optional. The toolset tool to execute.  
  
### ToolsetTool

JSON representation  
---  
      
    
    {
      "toolset": string,
      "toolId": string
    }  
  
Fields  
---  
`toolset` |  `string` Required. The resource name of the Toolset from which this tool is derived. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`toolId` |  `string` Optional. The tool ID to filter the tools to retrieve the schema for.  
  
### ToolResponse

JSON representation  
---  
      
    
    {
      "id": string,
      "displayName": string,
      "response": {
        object
      },
      "parentToolCallId": string,
      "agentName": string,
    
      // Union field tool_identifier can be only one of the following:
      "tool": string,
      "toolsetTool": {
        object ([ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool))
      }
      // End of list of possible types for union field tool_identifier.
    }  
  
Fields  
---  
`id` |  `string` Optional. The matching ID of the `[tool call](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolCall)` the response is for.  
`displayName` |  `string` Output only. Display name of the tool.  
`response` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Required. The tool execution result in JSON object format. Use "output" key to specify tool response and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as tool execution result.  
`parentToolCallId` |  `string` Output only. The id of the tool call that caused this one, when it was issued by a sub-agent working on behalf of a parent call. Empty for top-level calls. Lets a client group a sub-agent's work under the call that started it instead of rendering every step as a sibling.  
`agentName` |  `string` Output only. Human-readable name of the agent that issued this call, e.g. "Contract Architect". Empty when the root agent issued it.  
Union field `tool_identifier`. The identifier of the tool that got executed. It could be either a persisted tool or a tool from a toolset. `tool_identifier` can be only one of the following:  
`tool` |  `string` Optional. The name of the tool to execute. Format: `projects/{project}/locations/{location}/apps/{app}/tools/{tool}`  
`toolsetTool` |  `object (`[ToolsetTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_app_versions#Output.Schema.ToolsetTool)`)` Optional. The toolset tool that got executed.  
  
### AgentTransfer

JSON representation  
---  
      
    
    {
      "targetAgent": string,
      "displayName": string
    }  
  
Fields  
---  
`targetAgent` |  `string` Required. The agent to which the conversation is being transferred. The agent will handle the conversation from this point forward. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`displayName` |  `string` Output only. Display name of the agent.  
  
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
  
### Toolset

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "timeout": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "executionType": enum ([ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)),
      "toolFakeConfig": {
        object ([ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig))
      },
    
      // Union field toolset_type can be only one of the following:
      "mcpToolset": {
        object ([McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolset))
      },
      "openApiToolset": {
        object ([OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.OpenApiToolset))
      },
      "connectorToolset": {
        object ([ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.ConnectorToolset))
      }
      // End of list of possible types for union field toolset_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the toolset. Format: `projects/{project}/locations/{location}/apps/{app}/toolsets/{toolset}`  
`displayName` |  `string` Optional. The display name of the toolset. Must be unique within the same app.  
`description` |  `string` Optional. The description of the toolset.  
`timeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The timeout for the toolset execution. If not set, the default timeout is 30 seconds for `SYNCHRONOUS` toolsets and 60 seconds for `ASYNCHRONOUS` toolsets.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the toolset was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the toolset was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` ETag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`executionType` |  `enum (`[ExecutionType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ExecutionType)`)` Optional. The execution type of the tools in the toolset.  
`toolFakeConfig` |  `object (`[ToolFakeConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ToolFakeConfig)`)` Optional. Configuration for tools behavior in fake mode.  
Union field `toolset_type`. The type of the toolset. `toolset_type` can be only one of the following:  
`mcpToolset` |  `object (`[McpToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolset)`)` Optional. A toolset that contains a list of tools that are offered by the MCP server.  
`openApiToolset` |  `object (`[OpenApiToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.OpenApiToolset)`)` Optional. A toolset that contains a list of tools that are defined by an OpenAPI schema.  
`connectorToolset` |  `object (`[ConnectorToolset](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.ConnectorToolset)`)` Optional. A toolset that generates tools from an Integration Connectors Connection.  
  
### McpToolset

JSON representation  
---  
      
    
    {
      "serverAddress": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "customHeaders": {
        string: string,
        ...
      },
      "toolOverrides": [
        {
          object ([McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolOverride))
        }
      ]
    }  
  
Fields  
---  
`serverAddress` |  `string` Required. The address of the MCP server, for example, "https://example.com/mcp/". If the server is built with the MCP SDK, the url should be suffixed with "/mcp/". Only Streamable HTTP transport based servers are supported. See <https://modelcontextprotocol.io/specification/2025-03-26/basic/transports#streamable-http> for more details.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required to access tools and execute a tool against the MCP server. For bearer token authentication, the token applies only to tool execution, not to listing tools. This requires that tools can be listed without authentication.  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration for VPC-SC, used to resolve service names within a perimeter.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates that the client should trust.  
`customHeaders` |  `map (key: string, value: string)` Optional. The custom headers to send in the request to the MCP server. The values must be in the format `$context.variables.<name_of_variable>` and can be set in the session variables. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/tool/open-api#openapi-injection> for more details.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`toolOverrides[]` |  `object (`[McpToolOverride](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolOverride)`)` Optional. Overrides for individual tools within this toolset. This allows overriding specific details like descriptions, names, or pinning the tools' states so they aren't fully dynamic.  
  
### CustomHeadersEntry

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string`  
`value` |  `string`  
  
### McpToolOverride

JSON representation  
---  
      
    
    {
      "tool": string,
      "nameOverride": string,
      "descriptionOverride": string,
      "snapshot": {
        object ([McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolDefinition))
      }
    }  
  
Fields  
---  
`tool` |  `string` Required. The original name of the tool as it is emitted by the MCP server.  
`nameOverride` |  `string` Optional. If present, this tool uses this name in the Agent instead of the original name. This is primarily used as an alias if the MCP server offers poorly named tools.  
`descriptionOverride` |  `string` Optional. If present, this tool uses this description instead of the original description from the server.  
`snapshot` |  `object (`[McpToolDefinition](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_toolsets#Output.Schema.McpToolDefinition)`)` Output only. If present, this tool is "Pinned" and uses the snapshot values as fallbacks if the server becomes temporarily unavailable or if no Override is present.  
  
### McpToolDefinition

JSON representation  
---  
      
    
    {
      "description": string,
      "inputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      },
      "outputSchema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema))
      }
    }  
  
Fields  
---  
`description` |  `string` Output only. The description of the MCP tool. This can be overridden by `description_override` in `McpToolOverride`.  
`inputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Output only. The schema of the input arguments of the MCP tool.  
`outputSchema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.Schema)`)` Output only. The schema of the output arguments of the MCP tool.  
  
### OpenApiToolset

JSON representation  
---  
      
    
    {
      "openApiSchema": string,
      "apiAuthentication": {
        object ([ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication))
      },
      "tlsConfig": {
        object ([TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig))
      },
      "serviceDirectoryConfig": {
        object ([ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig))
      },
      "ignoreUnknownFields": boolean,
      "url": string
    }  
  
Fields  
---  
`openApiSchema` |  `string` Required. The OpenAPI schema of the toolset.  
`apiAuthentication` |  `object (`[ApiAuthentication](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_agents#Output.Schema.ApiAuthentication)`)` Optional. Authentication information required by the API.  
`tlsConfig` |  `object (`[TlsConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.TlsConfig)`)` Optional. The TLS configuration. Includes the custom server certificates  
`serviceDirectoryConfig` |  `object (`[ServiceDirectoryConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.ServiceDirectoryConfig)`)` Optional. Service Directory configuration.  
`ignoreUnknownFields` |  `boolean` Optional. If true, the agent will ignore unknown fields in the API response for all operations defined in the OpenAPI schema.  
`url` |  `string` Optional. The server URL of the Open API schema. This field is only set in toolsets in the environment dependencies during the export process if the schema contains a server url. During the import process, if this url is present in the environment dependencies and the schema has the $env_var placeholder, it will replace the placeholder in the schema.  
  
### ConnectorToolset

JSON representation  
---  
      
    
    {
      "connection": string,
      "authConfig": {
        object ([EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig))
      },
      "connectorActions": [
        {
          object ([Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action))
        }
      ]
    }  
  
Fields  
---  
`connection` |  `string` Required. The full resource name of the referenced Integration Connectors Connection. Format: `projects/{project}/locations/{location}/connections/{connection}`  
`authConfig` |  `object (`[EndUserAuthConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.EndUserAuthConfig)`)` Optional. Configures how authentication is handled in Integration Connectors. By default, an admin authentication is passed in the Integration Connectors API requests. You can override it with a different end-user authentication config. **Note** : The Connection must have authentication override enabled in order to specify an EUC configuration here - otherwise, the Toolset creation will fail. See: <https://cloud.google.com/application-integration/docs/configure-connectors-task#configure-authentication-override>  
`connectorActions[]` |  `object (`[Action](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_tools#Output.Schema.Action)`)` Required. The list of connector actions/entity operations to generate tools for.  
  
### PrebuiltAmbientNoise

Prebuilt ambient noise.

Enums  
---  
`PREBUILT_AMBIENT_NOISE_UNSPECIFIED` | Not specified.  
`RETAIL_STORE` | Ambient noise of a retail store.  
`CONVENTION_HALL` | Ambient noise of a convention hall.  
`OUTDOOR` | Ambient noise of a street.  
  
### WarningType

Type of warning encountered during voice sample processing.

Enums  
---  
`WARNING_TYPE_UNSPECIFIED` | Unspecified warning type.  
`LOW_AUDIO_LEVEL` | The audio level of the voice sample is too low (e.g. low RMS amplitude).  
  
### VoiceInstructionMode

Instruction mode for the voice sample.

Enums  
---  
`VOICE_INSTRUCTION_MODE_UNSPECIFIED` | Unspecified instruction mode. Defaults to NO_INSTRUCTION.  
`NO_INSTRUCTION` | No voice instruction will be used.  
`GENERATE_INSTRUCTION` | Voice instruction will be automatically generated by AI from the audio sample.  
`CUSTOM_INSTRUCTION` | Custom voice instruction provided by the user.  
  
### ErrorHandlingStrategy

Defines the strategy for handling errors.

Enums  
---  
`ERROR_HANDLING_STRATEGY_UNSPECIFIED` | Unspecified error handling strategy.  
`NONE` | No specific handling is enabled.  
`FALLBACK_RESPONSE` | A fallback message will be returned to the user in case of system errors (e.g. LLM errors).  
`END_SESSION` | An `EndSession` signal will be emitted in case of system errors (e.g. LLM errors).  
  
### ThinkingLevel

Thinking level configuration for the model.

Enums  
---  
`THINKING_LEVEL_UNSPECIFIED` | Thinking level is unspecified.  
`DEFAULT` | Default thinking level.  
`LOW` | Low thinking level.  
`MEDIUM` | Medium thinking level.  
`HIGH` | High thinking level.  
  
### ToolExecutionMode

Defines the tool execution behavior if there are **multiple** tools being selected by the agent **at the same time**.

Enums  
---  
`TOOL_EXECUTION_MODE_UNSPECIFIED` | Unspecified tool execution mode. Default to PARALLEL.  
`PARALLEL` | If there are multiple tools being selected, they will be executed in parallel, with the same [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context).  
`SEQUENTIAL` | If there are multiple tools being selected, they will be executed sequentially. The next tool will only be executed after the previous tool completes and it can see updated [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context) from the previous tool.  
  
### SemanticSimilarityChannel

Semantic similarity channel to use.

Enums  
---  
`SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED` | Metric unspecified. Defaults to TEXT.  
`TEXT` | Use text semantic similarity.  
`AUDIO` | Use audio semantic similarity.  
  
### ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
### HallucinationMetricBehavior

The hallucination metric behavior. Regardless of the behavior, the metric will always be calculated. The difference is that when disabled, the metric is not used to calculate the overall evaluation score.

Enums  
---  
`HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED` | Unspecified hallucination metric behavior.  
`DISABLED` | Disable hallucination metric.  
`ENABLED` | Enable hallucination metric.  
  
### Type

OpenAPI data types.

Enums  
---  
`TYPE_UNSPECIFIED` | Type unspecified.  
`STRING` | String type.  
`INTEGER` | Integer type.  
`NUMBER` | Number type.  
`BOOLEAN` | Boolean type.  
`OBJECT` | Object type.  
`ARRAY` | Array type.  
  
### NullValue

Represents a JSON `null`.

`NullValue` is a sentinel, using an enum with only one value to represent the null value for the `Value` type union.

A field of type `NullValue` with any value other than `0` is considered invalid. Most ProtoJSON serializers will emit a `Value` with a `null_value` set as a JSON `null` regardless of the integer value, and so will round trip to a `0` value.

Enums  
---  
`NULL_VALUE` | Null value.  
  
### Type

The type of the engine. See the documentation available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType> and <https://cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest>.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified engine type.  
`ENGINE_TYPE_SEARCH` | The SOLUTION_TYPE_SEARCH engine for the app. All connector data stores added to the app will be added to this engine.  
`ENGINE_TYPE_CHAT` | Chat engine type. The SOLUTION_TYPE_CHAT engine for the app. All connector data stores added to the app will be added to this engine.  
  
### ChannelType

The type of the channel profile.

Enums  
---  
`UNKNOWN` | Unknown channel type.  
`WEB_UI` | Web UI channel.  
`API` | API channel.  
`TWILIO` | Twilio channel.  
`GOOGLE_TELEPHONY_PLATFORM` | Google Telephony Platform channel.  
`CONTACT_CENTER_AS_A_SERVICE` | Contact Center as a Service (CCaaS) channel.  
`CONTACT_CENTER_AS_A_SERVICE_CHAT` | Contact Center as a Service (CCaaS Chat) channel.  
`FIVE9` | Five9 channel.  
`CONTACT_CENTER_INTEGRATION` | Third party contact center integration channel.  
`WHATSAPP` | WhatsApp channel.  
`INSTAGRAM` | Instagram channel.  
  
### Persona

The persona of the channel.

Enums  
---  
`UNKNOWN` | UNKNOWN persona.  
`CONCISE` | The agent keeps the responses concise and to the point  
`CHATTY` | The agent provides additional context, explanations, and details  
  
### Modality

Modality of the web widget.

Enums  
---  
`MODALITY_UNSPECIFIED` | Unknown modality.  
`CHAT_AND_VOICE` | Widget supports both chat and voice input.  
`VOICE_ONLY` | Widget supports only voice input.  
`CHAT_ONLY` | Widget supports only chat input.  
`CHAT_VOICE_AND_VIDEO` | Widget supports chat, voice, and video input.  
  
### Theme

Theme of the web widget.

Enums  
---  
`THEME_UNSPECIFIED` | Unknown theme.  
`LIGHT` | Light theme.  
`DARK` | Dark theme.  
  
### RequestLocation

The location of the API key in the request.

Enums  
---  
`REQUEST_LOCATION_UNSPECIFIED` | Unspecified. This value should not be used.  
`HEADER` | Represents the key in http header.  
`QUERY_STRING` | Represents the key in query string.  
  
### OauthGrantType

OAuth grant types. Only [client credential grant](https://oauth.net/2/grant-types/client-credentials) is supported.

Enums  
---  
`OAUTH_GRANT_TYPE_UNSPECIFIED` | Unspecified. Defaults to CLIENT_CREDENTIAL.  
`CLIENT_CREDENTIAL` | Represents the [client credential flow](https://oauth.net/2/grant-types/client-credentials).  
  
### Direction

The direction of the transfer.

Enums  
---  
`DIRECTION_UNSPECIFIED` | Unspecified direction.  
`PARENT_TO_CHILD` | Transfer from the parent agent to the child agent.  
`CHILD_TO_PARENT` | Transfer from the child agent to the parent agent.  
  
### OperationType

The operation to perform on the entity.

Enums  
---  
`OPERATION_TYPE_UNSPECIFIED` | Operation type unspecified. Invalid, ConnectorTool create/update will fail.  
`LIST` | List operation.  
`GET` | Get operation.  
`CREATE` | Create operation.  
`UPDATE` | Update operation.  
`DELETE` | Delete operation.  
  
### DataStoreType

The type of the data store.

Enums  
---  
`DATA_STORE_TYPE_UNSPECIFIED` | Not specified. This value indicates that the data store type is not specified, so it will not be used during search.  
`PUBLIC_WEB` | A data store that contains public web content.  
`UNSTRUCTURED` | A data store that contains unstructured private data.  
`FAQ` | A data store that contains structured data used as FAQ.  
`CONNECTOR` | A data store that is a connector to a first-party or a third-party service.  
  
### DocumentProcessingMode

The document processing mode of the data store.

Enums  
---  
`DOCUMENT_PROCESSING_MODE_UNSPECIFIED` | Not specified.  
`DOCUMENTS` | Documents are processed as documents.  
`CHUNKS` | Documents are converted to chunks.  
  
### AttributeType

The attribute(or function) for which the custom ranking is to be applied.

Enums  
---  
`ATTRIBUTE_TYPE_UNSPECIFIED` | Unspecified AttributeType.  
`NUMERICAL` | The value of the numerical field will be used to dynamically update the boost amount. In this case, the attribute_value (the x value) of the control point will be the actual value of the numerical field for which the boost_amount is specified.  
`FRESHNESS` | For the freshness use case the attribute value will be the duration between the current time and the date in the datetime field specified. The value must be formatted as an XSD `dayTimeDuration` value (a restricted subset of an ISO 8601 duration value). The pattern for this is: `[nD][T[nH][nM][nS]]`. E.g. `5D`, `3DT12H30M`, `T24H`.  
  
### InterpolationType

The interpolation type to be applied. Default will be linear (Piecewise Linear).

Enums  
---  
`INTERPOLATION_TYPE_UNSPECIFIED` | Interpolation type is unspecified. In this case, it defaults to Linear.  
`LINEAR` | Piecewise linear interpolation will be applied.  
  
### ModalityType

The modality type.

Enums  
---  
`MODALITY_TYPE_UNSPECIFIED` | Unspecified modality type.  
`TEXT` | Text modality.  
`AUDIO` | Audio modality.  
  
### FilterParameterBehavior

Filter parameter behavior.

Enums  
---  
`FILTER_PARAMETER_BEHAVIOR_UNSPECIFIED` | Default filter behavior. Include filter parameter for connector datastores. For the rest of the datastore types, the filter input parameter is omitted.  
`ALWAYS_INCLUDE` | Always include filter parameter for all datastore types.  
`NEVER_INCLUDE` | The filter parameter is never included in the list of tool parameters, regardless of the datastore type.  
  
### State

Represents the dynamic availability state of the tool.

Enums  
---  
`STATE_UNSPECIFIED` | Default state.  
`ACTIVE` | The tool is available and actively offered by the server.  
`INACTIVE` | The tool is configured or pinned, but currently not offered by the server.  
`STALE` | The tool exists on the server, but does not match the version on the server.  
  
### CorpusType

The type of the Vertex RAG corpus.

Enums  
---  
`CORPUS_TYPE_UNSPECIFIED` | Unspecified corpus type.  
`USER_OWNED` | The corpus is created and owned by the user.  
`FULLY_MANAGED` | The corpus is created by the agent.  
  
### WidgetType

All available widget types. New values may be added to this enum in the future.

Enums  
---  
`WIDGET_TYPE_UNSPECIFIED` | Unspecified widget type.  
`CUSTOM` | Custom widget type.  
`PRODUCT_CAROUSEL` | Product carousel widget.  
`PRODUCT_DETAILS` | Product details widget.  
`QUICK_ACTIONS` | Quick actions widget.  
`PRODUCT_COMPARISON` | Product comparison widget.  
`ADVANCED_PRODUCT_DETAILS` | Advanced product details widget.  
`SHORT_FORM` | Short form widget.  
`OVERALL_SATISFACTION` | Overall satisfaction widget.  
`ORDER_SUMMARY` | Order summary widget.  
`APPOINTMENT_DETAILS` | Appointment details widget.  
`APPOINTMENT_SCHEDULER` | Appointment scheduler widget.  
`CONTACT_FORM` | Contact form widget.  
  
### Mode

The strategy used to map data from the source tool to the widget.

Enums  
---  
`MODE_UNSPECIFIED` | Unspecified mode.  
`FIELD_MAPPING` | Use the `field_mappings` map for data transformation.  
`PYTHON_SCRIPT` | Use the `python_script` for data transformation.  
  
### Type

Defines how the text response is produced.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified type.  
`NONE` | The LLM dynamically decides whether to generate a text response alongside the widget based on the conversation context.  
`LLM_GENERATED` | The LLM is explicitly required to generate a text response.  
`STATIC` | A pre-defined static text response is always used.  
  
### ExecutionType

The execution type of the tool or toolset.

Enums  
---  
`EXECUTION_TYPE_UNSPECIFIED` | The execution type is unspecified. Defaults to `SYNCHRONOUS` if unspecified.  
`SYNCHRONOUS` | The tool is executed synchronously. The session is blocked until the tool returns.  
`ASYNCHRONOUS` | The tool is executed asynchronously. The session will continue while the tool is executing.  
  
### MatchType

Match type for the content filter.

Enums  
---  
`MATCH_TYPE_UNSPECIFIED` | Match type is not specified.  
`SIMPLE_STRING_MATCH` | Content is matched for substrings character by character.  
`WORD_BOUNDARY_STRING_MATCH` | Content only matches if the pattern found in the text is surrounded by word delimiters. Banned phrases can also contain word delimiters.  
`REGEXP_MATCH` | Content is matched using regular expression syntax.  
  
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



Destructive Hint: ✅ | Idempotent Hint: ❌ | Read Only Hint: ❌ | Open World Hint: ❌

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
