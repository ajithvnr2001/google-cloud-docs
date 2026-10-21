---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps/
title: MCP Tools Reference: ces.googleapis.com \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T00:33:37.431057+00:00
---

# MCP Tools Reference: ces.googleapis.com  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  MCP Tools Reference: ces.googleapis.com Stay organized with collections  Save and categorize content based on your preferences. 

## Tool: `list_apps`

Lists apps in the given project and location.

The following code sample shows how to use `curl` to call the `list_apps` MCP tool. 

Curl Request  
---  
      
    
    curl --location 'https://ces.googleapis.com/mcp' \
    --header 'content-type: application/json' \
    --header 'accept: application/json, text/event-stream' \
    --data '{
      "method": "tools/call",
      "params": {
        "name": "list_apps",
        "arguments": {
          // Provide these details according to the MCP tool specification.
        }
      },
      "jsonrpc": "2.0",
      "id": 1
    }'  
  
## Input Schema

Request message for `AgentService.ListApps`.

### ListAppsRequest

JSON representation  
---  
      
    
    {
      "parent": string,
      "pageSize": integer,
      "pageToken": string,
      "filter": string,
      "orderBy": string
    }  
  
Fields  
---  
`parent` |  `string` Required. The resource name of the location to list apps from.  
`pageSize` |  `integer` Optional. Requested page size. Server may return fewer items than requested. If unspecified, server will pick an appropriate default.  
`pageToken` |  `string` Optional. The `next_page_token` value returned from a previous list `AgentService.ListApps` call.  
`filter` |  `string` Optional. Filter to be applied when listing the apps. See <https://google.aip.dev/160> for more details.  
`orderBy` |  `string` Optional. Field to sort by. Only "name" and "create_time" is supported. See <https://google.aip.dev/132#ordering> for more details.  
  
## Output Schema

Response message for `AgentService.ListApps`.

### ListAppsResponse

JSON representation  
---  
      
    
    {
      "apps": [
        {
          object ([App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.App))
        }
      ],
      "nextPageToken": string,
      "unreachable": [
        string
      ]
    }  
  
Fields  
---  
`apps[]` |  `object (`[App](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/mcp/tools_list/list_apps#Output.Schema.App)`)` The list of apps.  
`nextPageToken` |  `string` A token that can be sent as `ListAppsRequest.page_token` to retrieve the next page. Absence of this field indicates there are no subsequent pages.  
`unreachable[]` |  `string` Unordered list. Locations that could not be reached.  
  
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
