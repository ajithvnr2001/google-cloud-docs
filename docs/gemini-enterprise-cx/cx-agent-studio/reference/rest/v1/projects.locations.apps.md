---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps
title: REST Resource: projects.locations.apps \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:22:28.329498+00:00
---

# REST Resource: projects.locations.apps  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: App
    * JSON representation
    * LanguageSettings
      * JSON representation
    * TimeZoneSettings
      * JSON representation
    * AudioProcessingConfig
      * JSON representation
    * SynthesizeSpeechConfig
      * JSON representation
    * BargeInConfig
      * JSON representation
    * AmbientSoundConfig
      * JSON representation
    * AmbientSoundConfig.PrebuiltAmbientNoise
    * CustomVoiceSample
      * JSON representation
    * CustomVoiceSample.Warning
      * JSON representation
    * CustomVoiceSample.Warning.WarningType
    * CustomVoiceSample.VoiceInstructionMode
    * LoggingSettings
      * JSON representation
    * RedactionConfig
      * JSON representation
    * AudioRecordingConfig
      * JSON representation
    * BigQueryExportSettings
      * JSON representation
    * CloudLoggingSettings
      * JSON representation
    * ConversationLoggingSettings
      * JSON representation
    * MetricAnalysisSettings
      * JSON representation
    * ErrorHandlingSettings
      * JSON representation
    * ErrorHandlingSettings.ErrorHandlingStrategy
    * ErrorHandlingSettings.FallbackResponseConfig
      * JSON representation
    * ErrorHandlingSettings.EndSessionConfig
      * JSON representation
    * App.ToolExecutionMode
    * EvaluationMetricsThresholds
      * JSON representation
    * EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds
      * JSON representation
    * EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds
      * JSON representation
    * EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel
    * EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds
      * JSON representation
    * EvaluationMetricsThresholds.ToolMatchingSettings
      * JSON representation
    * EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior
    * EvaluationMetricsThresholds.HallucinationMetricBehavior
    * App.VariableDeclaration
      * JSON representation
    * DataStoreSettings
      * JSON representation
    * DataStoreSettings.Engine
      * JSON representation
    * DataStoreSettings.Engine.Type
    * ClientCertificateSettings
      * JSON representation
    * VpcScSettings
      * JSON representation
    * DashboardSettings
      * JSON representation
  * Methods



## Resource: App

An app serves as a top-level container for a group of agents, including the root agent and its sub-agents, along with their associated configurations. These agents work together to achieve specific goals within the app's context.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "pinned": boolean,
      "rootAgent": string,
      "languageSettings": {
        object ([LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.LanguageSettings))
      },
      "timeZoneSettings": {
        object ([TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.TimeZoneSettings))
      },
      "audioProcessingConfig": {
        object ([AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioProcessingConfig))
      },
      "loggingSettings": {
        object ([LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.LoggingSettings))
      },
      "errorHandlingSettings": {
        object ([ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings))
      },
      "modelSettings": {
        object ([ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ModelSettings))
      },
      "toolExecutionMode": enum ([App.ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.App.ToolExecutionMode)),
      "evaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds))
      },
      "variableDeclarations": [
        {
          object ([App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.App.VariableDeclaration))
        }
      ],
      "predefinedVariableDeclarations": [
        {
          object ([App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.App.VariableDeclaration))
        }
      ],
      "globalInstruction": string,
      "guardrails": [
        string
      ],
      "dataStoreSettings": {
        object ([DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DataStoreSettings))
      },
      "defaultChannelProfile": {
        object ([ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile))
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
        object ([ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ClientCertificateSettings))
      },
      "vpcScSettings": {
        object ([VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.VpcScSettings))
      },
      "locked": boolean,
      "validationErrors": [
        string
      ],
      "dashboardSettings": {
        object ([DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DashboardSettings))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the app. Format: `projects/{project}/locations/{location}/apps/{app}`  
`displayName` |  `string` Required. Display name of the app.  
`description` |  `string` Optional. Human-readable description of the app.  
`pinned` |  `boolean` Optional. Whether the app is pinned in the app list.  
`rootAgent` |  `string` Optional. The root agent is the entry point of the app. Format: `projects/{project}/locations/{location}/apps/{app}/agents/{agent}`  
`languageSettings` |  `object (`[LanguageSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.LanguageSettings)`)` Optional. Language settings of the app.  
`timeZoneSettings` |  `object (`[TimeZoneSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.TimeZoneSettings)`)` Optional. TimeZone settings of the app.  
`audioProcessingConfig` |  `object (`[AudioProcessingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioProcessingConfig)`)` Optional. Audio processing configuration of the app.  
`loggingSettings` |  `object (`[LoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.LoggingSettings)`)` Optional. Logging settings of the app.  
`errorHandlingSettings` |  `object (`[ErrorHandlingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings)`)` Optional. Error handling settings of the app.  
`modelSettings` |  `object (`[ModelSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ModelSettings)`)` Optional. The default LLM model settings for the app. Individual resources (e.g. agents, guardrails) can override these configurations as needed.  
`toolExecutionMode` |  `enum (`[App.ToolExecutionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.App.ToolExecutionMode)`)` Optional. The tool execution mode for the app. If not provided, will default to PARALLEL.  
`evaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds)`)` Optional. The evaluation thresholds for the app.  
`variableDeclarations[]` |  `object (`[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.App.VariableDeclaration)`)` Optional. The declarations of the variables.  
`predefinedVariableDeclarations[]` |  `object (`[App.VariableDeclaration](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.App.VariableDeclaration)`)` Output only. The declarations of predefined variables for the app.  
`globalInstruction` |  `string` Optional. Instructions for all the agents in the app. You can use this instruction to set up a stable identity or personality across all the agents.  
`guardrails[]` |  `string` Optional. List of guardrails for the app. Format: `projects/{project}/locations/{location}/apps/{app}/guardrails/{guardrail}`  
`dataStoreSettings` |  `object (`[DataStoreSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DataStoreSettings)`)` Optional. The data store settings for the app.  
`defaultChannelProfile` |  `object (`[ChannelProfile](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile)`)` Optional. The default channel profile used by the app.  
`metadata` |  `map (key: string, value: string)` Optional. Metadata about the app. This field can be used to store additional information relevant to the app's details or intended usages.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the app was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. Etag used to ensure the object hasn't changed during a read-modify-write operation. If the etag is empty, the update will overwrite any concurrent changes.  
`deploymentCount` |  `integer` Output only. Number of deployments in the app.  
`clientCertificateSettings` |  `object (`[ClientCertificateSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ClientCertificateSettings)`)` Optional. The default client certificate settings for the app.  
`vpcScSettings` |  `object (`[VpcScSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.VpcScSettings)`)` Optional. VPC-SC settings for the app.  
`locked` |  `boolean` Optional. Indicates whether the app is locked for changes. If the app is locked, modifications to the app resources will be rejected.  
`validationErrors[]` |  `string` Output only. Misconfigurations or warnings in the app.  
`dashboardSettings` |  `object (`[DashboardSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DashboardSettings)`)` Optional. App-specific dashboard settings for linking and configuring Contact Center Insights dashboards.  
  
### LanguageSettings

Language settings of the app.

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
`supportedLanguageCodes[]` |  `string` Optional. List of languages codes supported by the app, in addition to the `defaultLanguageCode`.  
`enableMultilingualSupport` |  `boolean` Optional. Enables multilingual support. If true, agents in the app will use pre-built instructions to improve handling of multilingual input.  
`fallbackAction  
**(deprecated)**` |  `string` This item is deprecated!Optional. Deprecated: This feature is no longer supported. Use `enableMultilingualSupport` instead to improve handling of multilingual input. The action to perform when an agent receives input in an unsupported language.This can be a predefined action or a custom tool call. Valid values are: - A tool's full resource name, which triggers a specific tool execution. - A predefined system action, such as "escalate" or "exit", which triggers an `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/RunSessionResponse#EndSession)` signal with corresponding `[metadata](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/RunSessionResponse#EndSession.FIELDS.metadata)` to terminate the conversation.  
  
### TimeZoneSettings

TimeZone settings of the app.

JSON representation  
---  
      
    
    {
      "timeZone": string
    }  
  
Fields  
---  
`timeZone` |  `string` Optional. The time zone of the app from the [time zone database](https://www.iana.org/time-zones), e.g., America/Los_Angeles, Europe/Paris.  
  
### AudioProcessingConfig

Configuration for how the input and output audio should be processed and delivered.

JSON representation  
---  
      
    
    {
      "synthesizeSpeechConfigs": {
        string: {
          object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.SynthesizeSpeechConfig))
        },
        ...
      },
      "bargeInConfig": {
        object ([BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.BargeInConfig))
      },
      "inactivityTimeout": string,
      "ambientSoundConfig": {
        object ([AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AmbientSoundConfig))
      },
      "customVoiceSamples": [
        {
          object ([CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample))
        }
      ]
    }  
  
Fields  
---  
`synthesizeSpeechConfigs` |  `map (key: string, value: object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.SynthesizeSpeechConfig)`))` Optional. Configuration of how the agent response should be synthesized, mapping from the language code to `[SynthesizeSpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.SynthesizeSpeechConfig)`.If the configuration for the specified language code is not found, the configuration for the root language code will be used. For example, if the map contains "en-us" and "en", and the specified language code is "en-gb", then "en" configuration will be used.Note: Language code is case-insensitive.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`bargeInConfig` |  `object (`[BargeInConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.BargeInConfig)`)` Optional. Configures the agent behavior for the user barge-in activities.  
`inactivityTimeout` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. The duration of user inactivity (no speech or interaction) before the agent prompts the user for reengagement. If not set, the agent will not prompt the user for reengagement.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`ambientSoundConfig` |  `object (`[AmbientSoundConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AmbientSoundConfig)`)` Optional. Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.  
`customVoiceSamples[]` |  `object (`[CustomVoiceSample](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample)`)` Optional. Configures custom voice samples for voice cloning.  
  
### SynthesizeSpeechConfig

Configuration for how the agent response should be synthesized.

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
`voice` |  `string` Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode.For the list of available voices, please refer to [Supported voices and languages](https://cloud.google.com/text-to-speech/docs/voices) from Cloud Text-to-Speech.  
`speakingRate` |  `number` Optional. The speaking rate/speed in the range [0.25, 2.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. Values outside of the range [0.25, 2.0] will return an error.  
`model` |  `string` Optional. The model used to synthesize audio. Currently supported values: - "gemini-3.1-flash-tts-preview" If empty, Chirp3-HD is used.  
`instruction` |  `string` Optional. The instruction used to synthesize speech when using a generative model.  
  
### BargeInConfig

Configuration for how the user barge-in activities should be handled.

JSON representation  
---  
      
    
    {
      "disableBargeIn": boolean,
      "bargeInAwareness": boolean
    }  
  
Fields  
---  
`disableBargeIn  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Deprecated: `disableBargeIn` is deprecated in favor of `[`disableBargeInControl`](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/ChannelProfile#FIELDS.disable_barge_in_control)` in ChannelProfile.Disables user barge-in while the agent is speaking. If true, user input during agent response playback will be ignored.  
`bargeInAwareness` |  `boolean` Optional. If enabled, the agent will adapt its next response based on the assumption that the user hasn't heard the full preceding agent message. This should not be used in scenarios where agent responses are displayed visually.  
  
### AmbientSoundConfig

Configuration for the ambient sound to be played with the synthesized agent response, to enhance the naturalness of the conversation.

JSON representation  
---  
      
    
    {
      "volumeGainDb": number,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "prebuiltAmbientNoise": enum ([AmbientSoundConfig.PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AmbientSoundConfig.PrebuiltAmbientNoise)),
      "gcsUri": string,
      "prebuiltAmbientSound": string
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`volumeGainDb` |  `number` Optional. Volume gain (in dB) of the normal native volume supported by ambient noise, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.  
Ambient noise to be played with the synthesized agent response, to enhance the naturalness of the conversation. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`prebuiltAmbientNoise  
**(deprecated)**` |  `enum (`[AmbientSoundConfig.PrebuiltAmbientNoise](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AmbientSoundConfig.PrebuiltAmbientNoise)`)` This item is deprecated!Optional. Deprecated: `prebuiltAmbientNoise` is deprecated in favor of `prebuiltAmbientSound`.  
`gcsUri` |  `string` Optional. Ambient noise as a mono-channel, 16kHz WAV file stored in [Cloud Storage](https://cloud.google.com/storage).Note: Please make sure the CES service agent `service-<PROJECT-NUMBER>@gcp-sa-ces.iam.gserviceaccount.com` has `storage.objects.get` permission to the Cloud Storage object.  
`prebuiltAmbientSound` |  `string` Optional. Name of the prebuilt ambient sound. Valid values are: - "coffee_shop" - "keyboard" - "keypad" - "hum" - "office_1" - "office_2" - "office_3" - "room_1" - "room_2" - "room_3" - "room_4" - "room_5" - "air_conditioner"  
End of mutually exclusive fields.  
  
### AmbientSoundConfig.PrebuiltAmbientNoise

Prebuilt ambient noise.

Enums  
---  
`PREBUILT_AMBIENT_NOISE_UNSPECIFIED` | Not specified.  
`RETAIL_STORE` | Ambient noise of a retail store.  
`CONVENTION_HALL` | Ambient noise of a convention hall.  
`OUTDOOR` | Ambient noise of a street.  
  
### CustomVoiceSample

Configuration for a custom voice sample used for voice cloning.

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
          object ([CustomVoiceSample.Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample.Warning))
        }
      ],
      "voiceInstructionMode": enum ([CustomVoiceSample.VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample.VoiceInstructionMode))
    }  
  
Fields  
---  
`name` |  `string` Optional. The user-defined name for the custom voice sample.  
`voiceSampleGcsUri` |  `string` Optional. The Cloud Storage URI to the audio sample for voice cloning. The audio sample should be a mono-channel, 24kHz WAV file.  
`consentAudioGcsUri` |  `string` Optional. Consent audio for voice cloning.  
`voiceInstruction` |  `string` Optional. Natural language instructions for voice style, tone, pacing, or pronunciation.  
`previewAudioContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Output only. Synthesized preview audio for custom voice, formatted as canonical WAV (LINEAR16, 24kHz, 16-bit, mono).A base64-encoded string.  
`previewText` |  `string` Optional. Text for synthesizing preview audio for custom voice.  
`warnings[]` |  `object (`[CustomVoiceSample.Warning](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample.Warning)`)` Output only. Warning messages encountered during voice clone processing (e.g. low audio level).  
`voiceInstructionMode` |  `enum (`[CustomVoiceSample.VoiceInstructionMode](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample.VoiceInstructionMode)`)` Optional. Instruction mode for the voice sample. If unspecified, defaults to NO_INSTRUCTION.  
  
### CustomVoiceSample.Warning

A warning message encountered during voice sample processing.

JSON representation  
---  
      
    
    {
      "message": string,
      "type": enum ([CustomVoiceSample.Warning.WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample.Warning.WarningType))
    }  
  
Fields  
---  
`message` |  `string` Output only. A human-readable description of the warning.  
`type` |  `enum (`[CustomVoiceSample.Warning.WarningType](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CustomVoiceSample.Warning.WarningType)`)` Output only. The type of the warning.  
  
### CustomVoiceSample.Warning.WarningType

Type of warning encountered during voice sample processing.

Enums  
---  
`WARNING_TYPE_UNSPECIFIED` | Unspecified warning type.  
`LOW_AUDIO_LEVEL` | The audio level of the voice sample is too low (e.g. low RMS amplitude).  
  
### CustomVoiceSample.VoiceInstructionMode

Instruction mode for the voice sample.

Enums  
---  
`VOICE_INSTRUCTION_MODE_UNSPECIFIED` | Unspecified instruction mode. Defaults to NO_INSTRUCTION.  
`NO_INSTRUCTION` | No voice instruction will be used.  
`GENERATE_INSTRUCTION` | Voice instruction will be automatically generated by AI from the audio sample.  
`CUSTOM_INSTRUCTION` | Custom voice instruction provided by the user.  
  
### LoggingSettings

Settings to describe the logging behaviors for the app.

JSON representation  
---  
      
    
    {
      "redactionConfig": {
        object ([RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.RedactionConfig))
      },
      "audioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioRecordingConfig))
      },
      "unredactedAudioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioRecordingConfig))
      },
      "bigqueryExportSettings": {
        object ([BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.BigQueryExportSettings))
      },
      "unredactedBigqueryExportSettings": {
        object ([BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.BigQueryExportSettings))
      },
      "cloudLoggingSettings": {
        object ([CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CloudLoggingSettings))
      },
      "conversationLoggingSettings": {
        object ([ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ConversationLoggingSettings))
      },
      "evaluationAudioRecordingConfig": {
        object ([AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioRecordingConfig))
      },
      "metricAnalysisSettings": {
        object ([MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.MetricAnalysisSettings))
      }
    }  
  
Fields  
---  
`redactionConfig` |  `object (`[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.RedactionConfig)`)` Optional. Configuration for how sensitive data should be redacted.  
`audioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioRecordingConfig)`)` Optional. Configuration for how audio interactions should be recorded. The audio is subject to redaction as configured in `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.LoggingSettings.FIELDS.redaction_config)`.  
`unredactedAudioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioRecordingConfig)`)` Optional. Configures an additional recording of unredacted audio. This can be used to maintain a raw audio copy when audio redaction is `[enabled](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.RedactionConfig.FIELDS.enable_redaction)`, typically for auditing or monitoring purposes.  
`bigqueryExportSettings` |  `object (`[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.BigQueryExportSettings)`)` Optional. Configures the BigQuery export behaviors for the app. The conversation data is subject to redaction as configured in `[RedactionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.LoggingSettings.FIELDS.redaction_config)`.  
`unredactedBigqueryExportSettings` |  `object (`[BigQueryExportSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.BigQueryExportSettings)`)` Optional. Configures the BigQuery export behaviors for the app. The unredacted conversation data will be exported to BigQuery tables if it is enabled.  
`cloudLoggingSettings` |  `object (`[CloudLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.CloudLoggingSettings)`)` Optional. Settings to describe the Cloud Logging behaviors for the app.  
`conversationLoggingSettings` |  `object (`[ConversationLoggingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ConversationLoggingSettings)`)` Optional. Settings to describe the conversation logging behaviors for the app.  
`evaluationAudioRecordingConfig` |  `object (`[AudioRecordingConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.AudioRecordingConfig)`)` Optional. Configuration for how audio interactions should be recorded for the evaluation. By default, audio recording is not enabled for evaluation sessions.  
`metricAnalysisSettings` |  `object (`[MetricAnalysisSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.MetricAnalysisSettings)`)` Optional. Settings to describe the conversation data collection behaviors for the LLM analysis pipeline for the app.  
  
### RedactionConfig

Configuration to instruct how sensitive data should be handled.

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
`inspectTemplate` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) inspect template name to configure detection of sensitive data types.Format: `projects/{project}/locations/{location}/inspectTemplates/{inspectTemplate}`  
`deidentifyTemplate` |  `string` Optional. [DLP](https://cloud.google.com/dlp/docs) deidentify template name to instruct on how to de-identify content.Format: `projects/{project}/locations/{location}/deidentifyTemplates/{deidentifyTemplate}`  
  
### AudioRecordingConfig

Configuration for how the audio interactions should be recorded.

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

Settings to describe the BigQuery export behaviors for the app.

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

Settings to describe the Cloud Logging behaviors for the app.

JSON representation  
---  
      
    
    {
      "enableCloudLogging": boolean
    }  
  
Fields  
---  
`enableCloudLogging` |  `boolean` Optional. Whether to enable Cloud Logging for the sessions.  
  
### ConversationLoggingSettings

Settings to describe the conversation logging behaviors for the app.

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

Settings to describe the conversation data collection behaviors for LLM analysis metrics pipeline.

JSON representation  
---  
      
    
    {
      "llmMetricsOptedOut": boolean
    }  
  
Fields  
---  
`llmMetricsOptedOut` |  `boolean` Optional. Whether to collect conversation data for llm analysis metrics. If true, conversation data will not be collected for llm analysis metrics; otherwise, conversation data will be collected.  
  
### ErrorHandlingSettings

Settings to describe how errors should be handled in the app.

JSON representation  
---  
      
    
    {
      "errorHandlingStrategy": enum ([ErrorHandlingSettings.ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings.ErrorHandlingStrategy)),
      "fallbackResponseConfig": {
        object ([ErrorHandlingSettings.FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings.FallbackResponseConfig))
      },
      "endSessionConfig": {
        object ([ErrorHandlingSettings.EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings.EndSessionConfig))
      }
    }  
  
Fields  
---  
`errorHandlingStrategy` |  `enum (`[ErrorHandlingSettings.ErrorHandlingStrategy](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings.ErrorHandlingStrategy)`)` Optional. The strategy to use for error handling.  
`fallbackResponseConfig` |  `object (`[ErrorHandlingSettings.FallbackResponseConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings.FallbackResponseConfig)`)` Optional. Configuration for handling fallback responses.  
`endSessionConfig` |  `object (`[ErrorHandlingSettings.EndSessionConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.ErrorHandlingSettings.EndSessionConfig)`)` Optional. Configuration for ending the session in case of system errors (e.g. LLM errors).  
  
### ErrorHandlingSettings.ErrorHandlingStrategy

Defines the strategy for handling errors.

Enums  
---  
`ERROR_HANDLING_STRATEGY_UNSPECIFIED` | Unspecified error handling strategy.  
`NONE` | No specific handling is enabled.  
`FALLBACK_RESPONSE` | A fallback message will be returned to the user in case of system errors (e.g. LLM errors).  
`END_SESSION` | An `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/RunSessionResponse#EndSession)` signal will be emitted in case of system errors (e.g. LLM errors).  
  
### ErrorHandlingSettings.FallbackResponseConfig

Configuration for handling fallback responses.

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
`maxFallbackAttempts` |  `integer` Optional. The maximum number of fallback attempts to make before the agent emitting `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/RunSessionResponse#EndSession)` Signal.  
  
### ErrorHandlingSettings.EndSessionConfig

Configuration for ending the session in case of system errors (e.g. LLM errors).

JSON representation  
---  
      
    
    {
      "escalateSession": boolean
    }  
  
Fields  
---  
`escalateSession` |  `boolean` Optional. Whether to escalate the session in `[EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/RunSessionResponse#EndSession)`. If session is escalated, `[metadata in EndSession](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/RunSessionResponse#EndSession.FIELDS.metadata)` will contain `sessionEscalated = true`. See <https://docs.cloud.google.com/customer-engagement-ai/conversational-agents/ps/deploy/google-telephony-platform#transfer_a_call_to_a_human_agent> for details.  
  
### App.ToolExecutionMode

Defines the tool execution behavior if there are **multiple** tools being selected by the agent **at the same time**.

Enums  
---  
`TOOL_EXECUTION_MODE_UNSPECIFIED` | Unspecified tool execution mode. Default to PARALLEL.  
`PARALLEL` | If there are multiple tools being selected, they will be executed in parallel, with the same [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context).  
`SEQUENTIAL` | If there are multiple tools being selected, they will be executed sequentially. The next tool will only be executed after the previous tool completes and it can see updated [ToolContext](https://google.github.io/adk-docs/context/#the-different-types-of-context) from the previous tool.  
  
### EvaluationMetricsThresholds

Threshold settings for metrics in an Evaluation.

JSON representation  
---  
      
    
    {
      "goldenEvaluationMetricsThresholds": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds))
      },
      "hallucinationMetricBehavior": enum ([EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.HallucinationMetricBehavior)),
      "goldenHallucinationMetricBehavior": enum ([EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.HallucinationMetricBehavior)),
      "scenarioHallucinationMetricBehavior": enum ([EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.HallucinationMetricBehavior))
    }  
  
Fields  
---  
`goldenEvaluationMetricsThresholds` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds)`)` Optional. The golden evaluation metrics thresholds.  
`hallucinationMetricBehavior  
**(deprecated)**` |  `enum (`[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.HallucinationMetricBehavior)`)` This item is deprecated!Optional. Deprecated: Use `goldenHallucinationMetricBehavior` instead. The hallucination metric behavior is currently used for golden evaluations.  
`goldenHallucinationMetricBehavior` |  `enum (`[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for golden evaluations.  
`scenarioHallucinationMetricBehavior` |  `enum (`[EvaluationMetricsThresholds.HallucinationMetricBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.HallucinationMetricBehavior)`)` Optional. The hallucination metric behavior for scenario evaluations.  
  
### EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds

Settings for golden evaluations.

JSON representation  
---  
      
    
    {
      "turnLevelMetricsThresholds": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds))
      },
      "expectationLevelMetricsThresholds": {
        object ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds))
      },
      "toolMatchingSettings": {
        object ([EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.ToolMatchingSettings))
      }
    }  
  
Fields  
---  
`turnLevelMetricsThresholds` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds)`)` Optional. The turn level metrics thresholds.  
`expectationLevelMetricsThresholds` |  `object (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds)`)` Optional. The expectation level metrics thresholds.  
`toolMatchingSettings` |  `object (`[EvaluationMetricsThresholds.ToolMatchingSettings](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.ToolMatchingSettings)`)` Optional. The tool matching settings. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.  
  
### EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds

Turn level metrics thresholds.

JSON representation  
---  
      
    
    {
      "semanticSimilarityChannel": enum ([EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel)),
      "semanticSimilaritySuccessThreshold": integer,
      "overallToolInvocationCorrectnessThreshold": number
    }  
  
Fields  
---  
`semanticSimilarityChannel` |  `enum (`[EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel)`)` Optional. The semantic similarity channel to use for evaluation.  
`semanticSimilaritySuccessThreshold` |  `integer` Optional. The success threshold for semantic similarity. Must be an integer between 0 and 4. Default is >= 3.  
`overallToolInvocationCorrectnessThreshold` |  `number` Optional. The success threshold for overall tool invocation correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.TurnLevelMetricsThresholds.SemanticSimilarityChannel

Semantic similarity channel to use.

Enums  
---  
`SEMANTIC_SIMILARITY_CHANNEL_UNSPECIFIED` | Metric unspecified. Defaults to TEXT.  
`TEXT` | Use text semantic similarity.  
`AUDIO` | Use audio semantic similarity.  
  
### EvaluationMetricsThresholds.GoldenEvaluationMetricsThresholds.ExpectationLevelMetricsThresholds

Expectation level metrics thresholds.

JSON representation  
---  
      
    
    {
      "toolInvocationParameterCorrectnessThreshold": number
    }  
  
Fields  
---  
`toolInvocationParameterCorrectnessThreshold` |  `number` Optional. The success threshold for individual tool invocation parameter correctness. Must be a float between 0 and 1. Default is 1.0.  
  
### EvaluationMetricsThresholds.ToolMatchingSettings

Settings for matching tool calls.

JSON representation  
---  
      
    
    {
      "extraToolCallBehavior": enum ([EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior))
    }  
  
Fields  
---  
`extraToolCallBehavior` |  `enum (`[EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior)`)` Optional. Behavior for extra tool calls. Defaults to FAIL.  
  
### EvaluationMetricsThresholds.ToolMatchingSettings.ExtraToolCallBehavior

Defines the behavior when an extra tool call is encountered. An extra tool call is a tool call that is present in the execution but does not match any tool call in the golden expectation.

Enums  
---  
`EXTRA_TOOL_CALL_BEHAVIOR_UNSPECIFIED` | Unspecified behavior. Defaults to FAIL.  
`FAIL` | Fail the evaluation if an extra tool call is encountered.  
`ALLOW` | Allow the extra tool call.  
  
### EvaluationMetricsThresholds.HallucinationMetricBehavior

The hallucination metric behavior. Regardless of the behavior, the metric will always be calculated. The difference is that when disabled, the metric is not used to calculate the overall evaluation score.

Enums  
---  
`HALLUCINATION_METRIC_BEHAVIOR_UNSPECIFIED` | Unspecified hallucination metric behavior.  
`DISABLED` | Disable hallucination metric.  
`ENABLED` | Enable hallucination metric.  
  
### App.VariableDeclaration

Defines the structure and metadata for a variable.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "schema": {
        object ([Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The name of the variable. The name must start with a letter or underscore and contain only letters, numbers, or underscores.  
`description` |  `string` Required. The description of the variable.  
`schema` |  `object (`[Schema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/Schema)`)` Required. The schema of the variable.  
  
### DataStoreSettings

Data store related settings for the app.

JSON representation  
---  
      
    
    {
      "engines": [
        {
          object ([DataStoreSettings.Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DataStoreSettings.Engine))
        }
      ]
    }  
  
Fields  
---  
`engines[]` |  `object (`[DataStoreSettings.Engine](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DataStoreSettings.Engine)`)` Output only. The engines for the app.  
  
### DataStoreSettings.Engine

An engine to which the data stores are connected. See Vertex AI Search: <https://cloud.google.com/generative-ai-app-builder/docs/enterprise-search-introduction>.

JSON representation  
---  
      
    
    {
      "name": string,
      "type": enum ([DataStoreSettings.Engine.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DataStoreSettings.Engine.Type))
    }  
  
Fields  
---  
`name` |  `string` Output only. The resource name of the engine. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`  
`type` |  `enum (`[DataStoreSettings.Engine.Type](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps#App.DataStoreSettings.Engine.Type)`)` Output only. The type of the engine.  
  
### DataStoreSettings.Engine.Type

The type of the engine. See the documentation available at <https://cloud.google.com/generative-ai-app-builder/docs/reference/rest/v1/SolutionType> and <https://cloud.google.com/generative-ai-app-builder/docs/create-datastore-ingest>.

Enums  
---  
`TYPE_UNSPECIFIED` | Unspecified engine type.  
`ENGINE_TYPE_SEARCH` | The SOLUTION_TYPE_SEARCH engine for the app. All connector data stores added to the app will be added to this engine.  
`ENGINE_TYPE_CHAT` | Chat engine type. The SOLUTION_TYPE_CHAT engine for the app. All connector data stores added to the app will be added to this engine.  
  
### ClientCertificateSettings

Settings for custom client certificates.

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

VPC-SC settings for the app.

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

Settings for dashboards associated with the app, that show up in the Monitoring view.

JSON representation  
---  
      
    
    {
      "defaultDashboard": string
    }  
  
Fields  
---  
`defaultDashboard` |  `string` Optional. The resource name of the default Contact Center Insights dashboard associated with the app. This is the dashboard that will be displayed when users navigate to the Monitoring view for the app.Format: `projects/{project}/locations/{location}/dashboards/{dashboard}`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/create)`

|  Creates a new app in the given project and location.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/delete)`

|  Deletes the specified app.  
  
### `[executeTool](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/executeTool)`

|  Executes the given tool with the given arguments.  
  
### `[exportApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/exportApp)`

|  Exports the specified app.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/get)`

|  Gets details of the specified app.  
  
### `[getExtendedAgentCard](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/getExtendedAgentCard)`

|  Gets the extended agent card for the authenticated agent.  
  
### `[importApp](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/importApp)`

|  Imports the specified app.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/list)`

|  Lists apps in the given project and location.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/patch)`

|  Updates the specified app.  
  
### `[retrieveToolSchema](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps/retrieveToolSchema)`

|  Retrieve the schema of the given tool.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-28 UTC."],[],[]] 
