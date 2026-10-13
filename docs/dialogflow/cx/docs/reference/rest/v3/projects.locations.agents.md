---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents
title: REST Resource: projects.locations.agents \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:22:58.236001+00:00
---

# REST Resource: projects.locations.agents  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Agent
    * JSON representation
  * SpeechToTextSettings
    * JSON representation
  * GitIntegrationSettings
    * JSON representation
  * GithubSettings
    * JSON representation
  * TextToSpeechSettings
    * JSON representation
  * SynthesizeSpeechConfig
    * JSON representation
  * VoiceSelectionParams
    * JSON representation
  * SsmlVoiceGender
  * GenAppBuilderSettings
    * JSON representation
  * AnswerFeedbackSettings
    * JSON representation
  * PersonalizationSettings
    * JSON representation
  * ClientCertificateSettings
    * JSON representation
  * Methods



## Resource: Agent

Agents are best described as Natural Language Understanding (NLU) modules that transform user requests into actionable data. You can include agents in your app, product, or service to determine user intent and respond to the user in a natural way.

After you create an agent, you can add `[Intents](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.intents#Intent)`, `[Entity Types](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.entityTypes#EntityType)`, `[Flows](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows#Flow)`, `[Fulfillments](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/Fulfillment)`, `[Webhooks](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.webhooks#Webhook)`, `[TransitionRouteGroups](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.flows.transitionRouteGroups#TransitionRouteGroup)` and so on to manage the conversation flows.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "defaultLanguageCode": string,
      "supportedLanguageCodes": [
        string
      ],
      "timeZone": string,
      "description": string,
      "avatarUri": string,
      "speechToTextSettings": {
        object ([SpeechToTextSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#SpeechToTextSettings))
      },
      "securitySettings": string,
      "enableStackdriverLogging": boolean,
      "enableSpellCorrection": boolean,
      "enableMultiLanguageTraining": boolean,
      "locked": boolean,
      "advancedSettings": {
        object ([AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings))
      },
      "gitIntegrationSettings": {
        object ([GitIntegrationSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#GitIntegrationSettings))
      },
      "textToSpeechSettings": {
        object ([TextToSpeechSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#TextToSpeechSettings))
      },
      "answerFeedbackSettings": {
        object ([AnswerFeedbackSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#AnswerFeedbackSettings))
      },
      "personalizationSettings": {
        object ([PersonalizationSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#PersonalizationSettings))
      },
      "clientCertificateSettings": {
        object ([ClientCertificateSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#ClientCertificateSettings))
      },
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "startFlow": string,
      "startPlaybook": string
      // End of mutually exclusive fields.
      "genAppBuilderSettings": {
        object ([GenAppBuilderSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#GenAppBuilderSettings))
      },
      "satisfiesPzs": boolean,
      "satisfiesPzi": boolean
    }  
  
Fields  
---  
`name` |  `string` The unique identifier of the agent. Required for the `[Agents.UpdateAgent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/patch#google.cloud.dialogflow.cx.v3.Agents.UpdateAgent)` method. `[Agents.CreateAgent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/create#google.cloud.dialogflow.cx.v3.Agents.CreateAgent)` populates the name automatically. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>`.  
`displayName` |  `string` Required. The human-readable name of the agent, unique within the location.  
`defaultLanguageCode` |  `string` Required. Immutable. The default language of the agent as a language tag. See [Language Support](https://cloud.google.com/dialogflow/cx/docs/reference/language) for a list of the currently supported language codes. This field cannot be set by the `[Agents.UpdateAgent](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/patch#google.cloud.dialogflow.cx.v3.Agents.UpdateAgent)` method.  
`supportedLanguageCodes[]` |  `string` The list of all languages supported by the agent (except for the `defaultLanguageCode`).  
`timeZone` |  `string` Required. The time zone of the agent from the [time zone database](https://www.iana.org/time-zones), e.g., America/New_York, Europe/Paris.  
`description` |  `string` The description of the agent. The maximum length is 500 characters. If exceeded, the request is rejected.  
`avatarUri` |  `string` The URI of the agent's avatar. Avatars are used throughout the Dialogflow console and in the self-hosted [Web Demo](https://cloud.google.com/dialogflow/docs/integrations/web-demo) integration.  
`speechToTextSettings` |  `object (`[SpeechToTextSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#SpeechToTextSettings)`)` Speech recognition related settings.  
`securitySettings` |  `string` Name of the `[SecuritySettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.securitySettings#SecuritySettings)` reference for the agent. Format: `projects/<ProjectID>/locations/<LocationID>/securitySettings/<SecuritySettingsID>`.  
`enableStackdriverLogging  
**(deprecated)**` |  `boolean` This item is deprecated!Indicates if stackdriver logging is enabled for the agent. Please use `[agent.advanced_settings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings#LoggingSettings)` instead.  
`enableSpellCorrection` |  `boolean` Indicates if automatic spell correction is enabled in detect intent requests.  
`enableMultiLanguageTraining` |  `boolean` Optional. Enable training multi-lingual models for this agent. These models will be trained on all the languages supported by the agent.  
`locked` |  `boolean` Indicates whether the agent is locked for changes. If the agent is locked, modifications to the agent will be rejected except for [agents.restore][].  
`advancedSettings` |  `object (`[AdvancedSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/AdvancedSettings)`)` Hierarchical advanced settings for this agent. The settings exposed at the lower level overrides the settings exposed at the higher level.  
`gitIntegrationSettings` |  `object (`[GitIntegrationSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#GitIntegrationSettings)`)` Git integration settings for this agent.  
`textToSpeechSettings` |  `object (`[TextToSpeechSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#TextToSpeechSettings)`)` Settings on instructing the speech synthesizer on how to generate the output audio content.  
`answerFeedbackSettings` |  `object (`[AnswerFeedbackSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#AnswerFeedbackSettings)`)` Optional. Answer feedback collection settings.  
`personalizationSettings` |  `object (`[PersonalizationSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#PersonalizationSettings)`)` Optional. Settings for end user personalization.  
`clientCertificateSettings` |  `object (`[ClientCertificateSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#ClientCertificateSettings)`)` Optional. Settings for custom client certificates.  
The resource to start the conversations with for the agent. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`startFlow` |  `string` Name of the start flow in this agent. A start flow will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/flows/<FlowID>`. Currently only the default start flow with id "00000000-0000-0000-0000-000000000000" is allowed.  
`startPlaybook` |  `string` Name of the start playbook in this agent. A start playbook will be automatically created when the agent is created, and can only be deleted by deleting the agent. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/playbooks/<PlaybookID>`. Currently only the default playbook with id "00000000-0000-0000-0000-000000000000" is allowed.  
End of mutually exclusive fields.  
`genAppBuilderSettings` |  `object (`[GenAppBuilderSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#GenAppBuilderSettings)`)` Gen App Builder-related agent-level settings.  
`satisfiesPzs` |  `boolean` Optional. Output only. A read only boolean field reflecting Zone Separation status of the agent.  
`satisfiesPzi` |  `boolean` Optional. Output only. A read only boolean field reflecting Zone Isolation status of the agent.  
  
## SpeechToTextSettings

Settings related to speech recognition.

JSON representation  
---  
      
    
    {
      "enableSpeechAdaptation": boolean
    }  
  
Fields  
---  
`enableSpeechAdaptation` |  `boolean` Whether to use speech adaptation for speech recognition.  
  
## GitIntegrationSettings

Settings for connecting to Git repository for an agent.

JSON representation  
---  
      
    
    {
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "githubSettings": {
        object ([GithubSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#GithubSettings))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
The git settings to specific systems. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`githubSettings` |  `object (`[GithubSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#GithubSettings)`)` GitHub settings.  
End of mutually exclusive fields.  
  
## GithubSettings

Settings of integration with GitHub.

JSON representation  
---  
      
    
    {
      "displayName": string,
      "repositoryUri": string,
      "trackingBranch": string,
      "accessToken": string,
      "branches": [
        string
      ]
    }  
  
Fields  
---  
`displayName` |  `string` The unique repository display name for the GitHub repository.  
`repositoryUri` |  `string` The GitHub repository URI related to the agent.  
`trackingBranch` |  `string` The branch of the GitHub repository tracked for this agent.  
`accessToken` |  `string` The access token used to authenticate the access to the GitHub repository.  
`branches[]` |  `string` A list of branches configured to be used from Dialogflow.  
  
## TextToSpeechSettings

Settings related to speech synthesizing.

JSON representation  
---  
      
    
    {
      "synthesizeSpeechConfigs": {
        string: {
          object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#SynthesizeSpeechConfig))
        },
        ...
      }
    }  
  
Fields  
---  
`synthesizeSpeechConfigs` |  `map (key: string, value: object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#SynthesizeSpeechConfig)`))` Configuration of how speech should be synthesized, mapping from language (<https://cloud.google.com/dialogflow/cx/docs/reference/language>) to SynthesizeSpeechConfig.These settings affect:

  * The [phone gateway](https://cloud.google.com/dialogflow/cx/docs/concept/integration/phone-gateway) synthesize configuration set via `[Agent.text_to_speech_settings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#Agent.FIELDS.text_to_speech_settings)`.
  * How speech is synthesized when invoking `session` APIs. `[Agent.text_to_speech_settings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#Agent.FIELDS.text_to_speech_settings)` only applies if `[OutputAudioConfig.synthesize_speech_config](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig#FIELDS.synthesize_speech_config)` is not specified.

An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
## SynthesizeSpeechConfig

Configuration of how speech should be synthesized.

JSON representation  
---  
      
    
    {
      "speakingRate": number,
      "pitch": number,
      "volumeGainDb": number,
      "effectsProfileId": [
        string
      ],
      "voice": {
        object ([VoiceSelectionParams](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#VoiceSelectionParams))
      }
    }  
  
Fields  
---  
`speakingRate` |  `number` Optional. Speaking rate/speed, in the range [0.25, 4.0]. 1.0 is the normal native speed supported by the specific voice. 2.0 is twice as fast, and 0.5 is half as fast. If unset(0.0), defaults to the native 1.0 speed. Any other values < 0.25 or > 4.0 will return an error.  
`pitch` |  `number` Optional. Speaking pitch, in the range [-20.0, 20.0]. 20 means increase 20 semitones from the original pitch. -20 means decrease 20 semitones from the original pitch.  
`volumeGainDb` |  `number` Optional. Volume gain (in dB) of the normal native volume supported by the specific voice, in the range [-96.0, 16.0]. If unset, or set to a value of 0.0 (dB), will play at normal native signal amplitude. A value of -6.0 (dB) will play at approximately half the amplitude of the normal native signal amplitude. A value of +6.0 (dB) will play at approximately twice the amplitude of the normal native signal amplitude. We strongly recommend not to exceed +10 (dB) as there's usually no effective increase in loudness for any value greater than that.  
`effectsProfileId[]` |  `string` Optional. An identifier which selects 'audio effects' profiles that are applied on (post synthesized) text to speech. Effects are applied on top of each other in the order they are given.  
`voice` |  `object (`[VoiceSelectionParams](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#VoiceSelectionParams)`)` Optional. The desired voice of the synthesized audio.  
  
## VoiceSelectionParams

Description of which voice to use for speech synthesis.

JSON representation  
---  
      
    
    {
      "name": string,
      "ssmlGender": enum ([SsmlVoiceGender](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#SsmlVoiceGender))
    }  
  
Fields  
---  
`name` |  `string` Optional. The name of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and `[ssmlGender](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#VoiceSelectionParams.FIELDS.ssml_gender)`.For the list of available voices, please refer to [Supported voices and languages](https://cloud.google.com/text-to-speech/docs/voices).  
`ssmlGender` |  `enum (`[SsmlVoiceGender](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#SsmlVoiceGender)`)` Optional. The preferred gender of the voice. If not set, the service will choose a voice based on the other parameters such as languageCode and `[name](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents#VoiceSelectionParams.FIELDS.name)`. Note that this is only a preference, not requirement. If a voice of the appropriate gender is not available, the synthesizer substitutes a voice with a different gender rather than failing the request.  
  
## SsmlVoiceGender

Gender of the voice as described in [SSML voice element](https://www.w3.org/TR/speech-synthesis11/#edef_voice).

Enums  
---  
`SSML_VOICE_GENDER_UNSPECIFIED` | An unspecified gender, which means that the client doesn't care which gender the selected voice will have.  
`SSML_VOICE_GENDER_MALE` | A male voice.  
`SSML_VOICE_GENDER_FEMALE` | A female voice.  
`SSML_VOICE_GENDER_NEUTRAL` | A gender-neutral voice.  
  
## GenAppBuilderSettings

Settings for Gen App Builder.

JSON representation  
---  
      
    
    {
      "engine": string
    }  
  
Fields  
---  
`engine` |  `string` Required. The full name of the Gen App Builder engine related to this agent if there is one. Format: `projects/{Project ID}/locations/{Location ID}/collections/{Collection ID}/engines/{Engine ID}`  
  
## AnswerFeedbackSettings

Settings for answer feedback collection.

JSON representation  
---  
      
    
    {
      "enableAnswerFeedback": boolean
    }  
  
Fields  
---  
`enableAnswerFeedback` |  `boolean` Optional. If enabled, end users will be able to provide `[answer feedback](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/submitAnswerFeedback#body.AnswerFeedback)` to Dialogflow responses. Feature works only if interaction logging is enabled in the Dialogflow agent.  
  
## PersonalizationSettings

Settings for end user personalization.

JSON representation  
---  
      
    
    {
      "defaultEndUserMetadata": {
        object
      }
    }  
  
Fields  
---  
`defaultEndUserMetadata` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Optional. Default end user metadata, used when processing DetectIntent requests. Recommended to be filled as a template instead of hard-coded value, for example { "age": "$session.params.age" }. The data will be merged with the `[QueryParameters.end_user_metadata](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryParameters#FIELDS.end_user_metadata)` in `[DetectIntentRequest.query_params](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.sessions/detectIntent#body.request_body.FIELDS.query_params)` during query processing.  
  
## ClientCertificateSettings

Settings for custom client certificates.

JSON representation  
---  
      
    
    {
      "sslCertificate": string,
      "privateKey": string,
      "passphrase": string
    }  
  
Fields  
---  
`sslCertificate` |  `string` Required. The ssl certificate encoded in PEM format. This string must include the begin header and end footer lines.  
`privateKey` |  `string` Required. The name of the SecretManager secret version resource storing the private key encoded in PEM format. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
`passphrase` |  `string` Optional. The name of the SecretManager secret version resource storing the passphrase. 'passphrase' should be left unset if the private key is not encrypted. Format: `projects/{project}/secrets/{secret}/versions/{version}`  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/create)`

|  Creates an agent in the specified location.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/delete)`

|  Deletes the specified agent.  
  
### `[export](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/export)`

|  Exports the specified agent to a binary file.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/get)`

|  Retrieves the specified agent.  
  
### `[getGenerativeSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/getGenerativeSettings)`

|  Gets the generative settings for the agent.  
  
### `[getValidationResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/getValidationResult)`

|  Gets the latest agent validation result.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/list)`

|  Returns the list of all agents in the specified location.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/patch)`

|  Updates the specified agent.  
  
### `[restore](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/restore)`

|  Restores the specified agent from a binary file.  
  
### `[updateGenerativeSettings](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/updateGenerativeSettings)`

|  Updates the generative settings for the agent.  
  
### `[validate](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents/validate)`

|  Validates the specified agent and creates or updates validation results.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
