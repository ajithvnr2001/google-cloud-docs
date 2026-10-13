---
url: https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize/
title: Method: text.synthesize \u00a0|\u00a0 Cloud Text-to-Speech \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:41:50.297866+00:00
---

# Method: text.synthesize  |  Cloud Text-to-Speech  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Text-to-Speech ](https://docs.cloud.google.com/text-to-speech/docs)
  * [ Reference ](https://docs.cloud.google.com/text-to-speech/docs/apis)



Send feedback 

#  Method: text.synthesize Stay organized with collections  Save and categorize content based on your preferences. 

  * HTTP request
  * Request body
    * JSON representation
  * Response body
    * JSON representation
  * Authorization scopes
  * TimepointType
  * AdvancedVoiceOptions
    * JSON representation
  * Timepoint
    * JSON representation
  * Try it!



Synthesizes speech synchronously: receive results after all text input has been processed.

### HTTP request

`POST https://texttospeech.googleapis.com/v1beta1/text:synthesize`

The URL uses [gRPC Transcoding](https://google.aip.dev/127) syntax.

### Request body

The request body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "input": {
        object ([SynthesisInput](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/SynthesisInput))
      },
      "voice": {
        object (VoiceSelectionParams)
      },
      "audioConfig": {
        object ([AudioConfig](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/AudioConfig))
      },
      "enableTimePointing": [
        enum ([TimepointType](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize#TimepointType))
      ],
      "advancedVoiceOptions": {
        object ([AdvancedVoiceOptions](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize#AdvancedVoiceOptions))
      }
    }  
  
Fields  
---  
`input` |  `object (`[SynthesisInput](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/SynthesisInput)`)` Required. The Synthesizer requires either plain text or SSML as input.  
`voice` |  `object (`VoiceSelectionParams`)` Required. The desired voice of the synthesized audio.  
`audioConfig` |  `object (`[AudioConfig](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/AudioConfig)`)` Required. The configuration of the synthesized audio.  
`enableTimePointing[]` |  `enum (`[TimepointType](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize#TimepointType)`)` Whether and what timepoints are returned in the response.  
`advancedVoiceOptions` |  `object (`[AdvancedVoiceOptions](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize#AdvancedVoiceOptions)`)` Advanced voice options.  
  
### Response body

The message returned to the client by the `text.synthesize` method.

If successful, the response body contains data with the following structure:

JSON representation  
---  
      
    
    {
      "audioContent": string,
      "timepoints": [
        {
          object ([Timepoint](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize#Timepoint))
        }
      ],
      "audioConfig": {
        object ([AudioConfig](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/AudioConfig))
      }
    }  
  
Fields  
---  
`audioContent` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The audio data bytes encoded as specified in the request, including the header for encodings that are wrapped in containers (e.g. MP3, OGG_OPUS). For LINEAR16 audio, we include the WAV header. Note: as with all bytes fields, protobuffers use a pure binary representation, whereas JSON representations use base64.A base64-encoded string.  
`timepoints[]` |  `object (`[Timepoint](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/text/synthesize#Timepoint)`)` A link between a position in the original request input and a corresponding time in the output audio. It's only supported via `<mark>` of SSML input.  
`audioConfig` |  `object (`[AudioConfig](https://docs.cloud.google.com/text-to-speech/docs/reference/rest/v1beta1/AudioConfig)`)` The audio metadata of `audioContent`.  
  
### Authorization scopes

Requires the following OAuth scope:

  * `https://www.googleapis.com/auth/cloud-platform`



For more information, see the [Authentication Overview](https://docs.cloud.google.com/docs/authentication#authorization-gcp).

## TimepointType

The type of timepoint information that is returned in the response.

Enums  
---  
`TIMEPOINT_TYPE_UNSPECIFIED` | Not specified. No timepoint information will be returned.  
`SSML_MARK` | Timepoint information of `<mark>` tags in SSML input will be returned.  
  
## AdvancedVoiceOptions

Used for advanced voice options.

JSON representation  
---  
      
    
    {
      "lowLatencyJourneySynthesis": boolean
    }  
  
Fields  
---  
`lowLatencyJourneySynthesis` |  `boolean` Only for Journey voices. If false, the synthesis is context aware and has a higher latency.  
  
## Timepoint

This contains a mapping between a certain point in the input text and a corresponding time in the output audio.

JSON representation  
---  
      
    
    {
      "markName": string,
      "timeSeconds": number
    }  
  
Fields  
---  
`markName` |  `string` Timepoint name as received from the client within `<mark>` tag.  
`timeSeconds` |  `number` Time offset in seconds from the start of the synthesized audio.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
