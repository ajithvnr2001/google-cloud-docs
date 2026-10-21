---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig/
title: EvaluationConfig \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T14:41:21.908270+00:00
---

# EvaluationConfig  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EvaluationConfig Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * InputAudioConfig
    * JSON representation
  * AudioEncoding
  * OutputAudioConfig
    * JSON representation
  * EvaluationConfig.EvaluationChannel



EvaluationConfig configures settings for running the evaluation.

JSON representation  
---  
      
    
    {
      "inputAudioConfig": {
        object ([InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#InputAudioConfig))
      },
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#OutputAudioConfig))
      },
      "evaluationChannel": enum ([EvaluationConfig.EvaluationChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#EvaluationConfig.EvaluationChannel)),
      "toolCallBehaviour": enum ([EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationToolCallBehaviour))
    }  
  
Fields  
---  
`inputAudioConfig` |  `object (`[InputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#InputAudioConfig)`)` Optional. Configuration for processing the input audio.  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#OutputAudioConfig)`)` Optional. Configuration for generating the output audio.  
`evaluationChannel` |  `enum (`[EvaluationConfig.EvaluationChannel](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#EvaluationConfig.EvaluationChannel)`)` Optional. The channel to evaluate.  
`toolCallBehaviour` |  `enum (`[EvaluationToolCallBehaviour](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationToolCallBehaviour)`)` Optional. Specifies whether the evaluation should use real tool calls or fake tools.  
  
## InputAudioConfig

InputAudioConfig configures how the CES agent should interpret the incoming audio data.

JSON representation  
---  
      
    
    {
      "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#AudioEncoding)),
      "sampleRateHertz": integer,
      "noiseSuppressionLevel": string
    }  
  
Fields  
---  
`audioEncoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#AudioEncoding)`)` Required. The encoding of the input audio data.  
`sampleRateHertz` |  `integer` Required. The sample rate (in Hertz) of the input audio data.  
`noiseSuppressionLevel` |  `string` Optional. Whether to enable noise suppression on the input audio. Available values are "low", "moderate", "high", "very_high".  
  
## AudioEncoding

AudioEncoding specifies the encoding format for audio data.

Enums  
---  
`AUDIO_ENCODING_UNSPECIFIED` | Unspecified audio encoding.  
`LINEAR16` | 16-bit linear PCM audio encoding.  
`MULAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/mu-law.  
`ALAW` | 8-bit samples that compand 14-bit audio samples using G.711 PCMU/A-law.  
  
## OutputAudioConfig

OutputAudioConfig configures how the CES agent should synthesize outgoing audio responses.

JSON representation  
---  
      
    
    {
      "audioEncoding": enum ([AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#AudioEncoding)),
      "sampleRateHertz": integer
    }  
  
Fields  
---  
`audioEncoding` |  `enum (`[AudioEncoding](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationConfig#AudioEncoding)`)` Required. The encoding of the output audio data.  
`sampleRateHertz` |  `integer` Required. The sample rate (in Hertz) of the output audio data.  
  
## EvaluationConfig.EvaluationChannel

The channel to evaluate.

Enums  
---  
`EVALUATION_CHANNEL_UNSPECIFIED` | Unspecified evaluation channel.  
`TEXT` | Text-only evaluation channel.  
`AUDIO` | Audio evaluation channel.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-23 UTC."],[],[]] 
