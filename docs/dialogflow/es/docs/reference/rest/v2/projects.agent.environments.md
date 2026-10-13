---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments
title: REST Resource: projects.agent.environments \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:47.080052+00:00
---

# REST Resource: projects.agent.environments  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  REST Resource: projects.agent.environments Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Environment
    * JSON representation
    * State
    * TextToSpeechSettings
      * JSON representation
    * OutputAudioEncoding
    * Fulfillment
      * JSON representation
    * GenericWebService
      * JSON representation
    * Feature
      * JSON representation
    * Type
  * Methods



## Resource: Environment

You can create multiple versions of your agent and publish them to separate environments.

When you edit an agent, you are editing the draft agent. At any point, you can save the draft agent as an agent version, which is an immutable snapshot of your agent.

When you save the draft agent, it is published to the default environment. When you create agent versions, you can publish them to custom environments. You can create a variety of custom environments for:

  * testing
  * development
  * production
  * etc.



For more information, see the [versions and environments guide](https://cloud.google.com/dialogflow/docs/agents-versions).

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "agentVersion": string,
      "state": enum ([State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.State)),
      "updateTime": string,
      "textToSpeechSettings": {
        object ([TextToSpeechSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.TextToSpeechSettings))
      },
      "fulfillment": {
        object ([Fulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Fulfillment))
      }
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique identifier of this agent environment. Supported formats:

  * `projects/<Project ID>/agent/environments/<Environment ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/environments/<Environment ID>`

The environment ID for the default environment is `-`.  
`description` |  `string` Optional. The developer-provided description for this environment. The maximum length is 500 characters. If exceeded, the request is rejected.  
`agentVersion` |  `string` Optional. The agent version loaded into this environment. Supported formats:

  * `projects/<Project ID>/agent/versions/<Version ID>`
  * `projects/<Project ID>/locations/<Location ID>/agent/versions/<Version ID>`

  
`state` |  `enum (`[State](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.State)`)` Output only. The state of this environment. This field is read-only, i.e., it cannot be set by create and update methods.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time of this environment. This field is read-only, i.e., it cannot be set by create and update methods.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`textToSpeechSettings` |  `object (`[TextToSpeechSettings](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.TextToSpeechSettings)`)` Optional. Text to speech settings for this environment.  
`fulfillment` |  `object (`[Fulfillment](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Fulfillment)`)` Optional. The fulfillment settings to use for this environment.  
  
### State

Represents an environment state. When an environment is pointed to a new agent version, the environment is temporarily set to the `LOADING` state. During that time, the environment keeps on serving the previous version of the agent. After the new agent version is done loading, the environment is set back to the `RUNNING` state.

Enums  
---  
`STATE_UNSPECIFIED` | Not specified. This value is not used.  
`STOPPED` | Stopped.  
`LOADING` | Loading.  
`RUNNING` | Running.  
  
### TextToSpeechSettings

Instructs the speech synthesizer on how to generate the output audio content.

JSON representation  
---  
      
    
    {
      "enableTextToSpeech": boolean,
      "outputAudioEncoding": enum ([OutputAudioEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.OutputAudioEncoding)),
      "sampleRateHertz": integer,
      "synthesizeSpeechConfigs": {
        string: {
          object ([SynthesizeSpeechConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SynthesizeSpeechConfig))
        },
        ...
      }
    }  
  
Fields  
---  
`enableTextToSpeech` |  `boolean` Optional. Indicates whether text to speech is enabled. Even when this field is false, other settings in this proto are still retained.  
`outputAudioEncoding` |  `enum (`[OutputAudioEncoding](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.OutputAudioEncoding)`)` Required. Audio encoding of the synthesized audio content.  
`sampleRateHertz` |  `integer` Optional. The synthesis sample rate (in hertz) for this audio. If not provided, then the synthesizer will use the default sample rate based on the audio encoding. If this is different from the voice's natural sample rate, then the synthesizer will honor this request by converting to the desired sample rate (which might result in worse audio quality).  
`synthesizeSpeechConfigs` |  `map (key: string, value: object (`[SynthesizeSpeechConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/SynthesizeSpeechConfig)`))` Optional. Configuration of how speech should be synthesized, mapping from language (<https://cloud.google.com/dialogflow/docs/reference/language>) to SynthesizeSpeechConfig.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
  
### OutputAudioEncoding

Audio encoding of the output audio format in Text-To-Speech.

Enums  
---  
`OUTPUT_AUDIO_ENCODING_UNSPECIFIED` | Not specified.  
`OUTPUT_AUDIO_ENCODING_LINEAR_16` | Uncompressed 16-bit signed little-endian samples (Linear PCM). Audio content returned as LINEAR16 also contains a WAV header.  
`OUTPUT_AUDIO_ENCODING_MP3` | MP3 audio at 64kbps.This item is deprecated!  
`OUTPUT_AUDIO_ENCODING_MP3_64_KBPS` | MP3 audio at 64kbps.  
`OUTPUT_AUDIO_ENCODING_OGG_OPUS` | Opus encoded audio wrapped in an ogg container. The result will be a file which can be played natively on Android, and in browsers (at least Chrome and Firefox). The quality of the encoding is considerably higher than MP3 while using approximately the same bitrate.  
`OUTPUT_AUDIO_ENCODING_MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`OUTPUT_AUDIO_ENCODING_ALAW` | 8-bit samples that compand 13-bit audio samples using G.711 PCMU/a-law.  
  
### Fulfillment

By default, your agent responds to a matched intent with a static response. As an alternative, you can provide a more dynamic response by using fulfillment. When you enable fulfillment for an intent, Dialogflow responds to that intent by calling a service that you define. For example, if an end-user wants to schedule a haircut on Friday, your service can check your database and respond to the end-user with availability information for Friday.

For more information, see the [fulfillment guide](https://cloud.google.com/dialogflow/docs/fulfillment-overview).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "enabled": boolean,
      "features": [
        {
          object ([Feature](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Feature))
        }
      ],
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "genericWebService": {
        object ([GenericWebService](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.GenericWebService))
      }
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`name` |  `string` Required. The unique identifier of the fulfillment. Supported formats:

  * `projects/<Project ID>/agent/fulfillment`
  * `projects/<Project ID>/locations/<Location ID>/agent/fulfillment`

This field is not used for Fulfillment in an Environment.  
`displayName` |  `string` Optional. The human-readable name of the fulfillment, unique within the agent.This field is not used for Fulfillment in an Environment.  
`enabled` |  `boolean` Optional. Whether fulfillment is enabled.  
`features[]` |  `object (`[Feature](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Feature)`)` Optional. The field defines whether the fulfillment is enabled for certain features.  
Required. The fulfillment configuration. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`genericWebService` |  `object (`[GenericWebService](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.GenericWebService)`)` Configuration for a generic web service.  
End of mutually exclusive fields.  
  
### GenericWebService

Represents configuration for a generic web service. Dialogflow supports two mechanisms for authentications:

  * Basic authentication with username and password.
  * Authentication with additional authentication headers.



More information could be found at: <https://cloud.google.com/dialogflow/docs/fulfillment-configure>.

JSON representation  
---  
      
    
    {
      "uri": string,
      "username": string,
      "password": string,
      "requestHeaders": {
        string: string,
        ...
      },
      "isCloudFunction": boolean
    }  
  
Fields  
---  
`uri` |  `string` Required. The fulfillment URI for receiving POST requests. It must use https protocol.  
`username` |  `string` Optional. The user name for HTTP Basic authentication.  
`password` |  `string` Optional. The password for HTTP Basic authentication.  
`requestHeaders` |  `map (key: string, value: string)` Optional. The HTTP request headers to send together with fulfillment requests.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`isCloudFunction  
**(deprecated)**` |  `boolean` This item is deprecated!Optional. Indicates if generic web service is created through Cloud Functions integration. Defaults to false.isCloudFunction is deprecated. Cloud functions can be configured by its uri as a regular web service now.  
  
### Feature

Whether fulfillment is enabled for the specific feature.

JSON representation  
---  
      
    
    {
      "type": enum ([Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Type))
    }  
  
Fields  
---  
`type` |  `enum (`[Type](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments#Environment.Type)`)` The type of the feature that enabled for fulfillment.  
  
### Type

The type of the feature.

Enums  
---  
`TYPE_UNSPECIFIED` | Feature type not specified.  
`SMALLTALK` | Fulfillment is enabled for SmallTalk.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/create)`

|  Creates an agent environment.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/delete)`

|  Deletes the specified agent environment.  
  
### `[get](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/get)`

|  Retrieves the specified agent environment.  
  
### `[getHistory](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/getHistory)`

|  Gets the history of the specified environment.  
  
### `[list](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/list)`

|  Returns the list of all non-default environments of the specified agent.  
  
### `[patch](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/projects.agent.environments/patch)`

|  Updates the specified agent environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-24 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-24 UTC."],[],[]] 
