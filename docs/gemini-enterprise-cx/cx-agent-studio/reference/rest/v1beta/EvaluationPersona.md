---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona/
title: EvaluationPersona \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:26:19.961419+00:00
---

# EvaluationPersona  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  EvaluationPersona Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * EvaluationPersona.SpeechConfig
    * JSON representation
  * EvaluationPersona.SpeechConfig.BackgroundEnvironment



A persona represents an end user in an evaluation.

JSON representation  
---  
      
    
    {
      "name": string,
      "description": string,
      "displayName": string,
      "personality": string,
      "speechConfig": {
        object ([EvaluationPersona.SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona#EvaluationPersona.SpeechConfig))
      }
    }  
  
Fields  
---  
`name` |  `string` Required. The unique identifier of the persona. Format: `projects/{project}/locations/{location}/apps/{app}/evaluationPersonas/{evaluationPersona}`  
`description` |  `string` Optional. The description of the persona.  
`displayName` |  `string` Required. The display name of the persona. Unique within an app.  
`personality` |  `string` Required. An instruction for the agent on how to behave in the evaluation.  
`speechConfig` |  `object (`[EvaluationPersona.SpeechConfig](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona#EvaluationPersona.SpeechConfig)`)` Optional. Configuration for how the persona sounds (TTS settings).  
  
## EvaluationPersona.SpeechConfig

Configuration for Text-to-Speech generation.

JSON representation  
---  
      
    
    {
      "speakingRate": number,
      "environment": enum ([EvaluationPersona.SpeechConfig.BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona#EvaluationPersona.SpeechConfig.BackgroundEnvironment)),
      "voiceId": string
    }  
  
Fields  
---  
`speakingRate` |  `number` Optional. The speaking rate. 1.0 is normal. Lower is slower (e.g., 0.8), higher is faster (e.g., 1.5). Useful for testing how the agent handles fast talkers.  
`environment` |  `enum (`[EvaluationPersona.SpeechConfig.BackgroundEnvironment](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1beta/EvaluationPersona#EvaluationPersona.SpeechConfig.BackgroundEnvironment)`)` Optional. The simulated audio environment.  
`voiceId` |  `string` Optional. The specific voice identifier/accent to use. Example: "en-US-Wavenet-D" or "en-GB-Standard-A"  
  
## EvaluationPersona.SpeechConfig.BackgroundEnvironment

Simulated audio environment.

Enums  
---  
`BACKGROUND_ENVIRONMENT_UNSPECIFIED` | Background environment unspecified.  
`CALL_CENTER` | Call center environment.  
`TRAFFIC` | Traffic noise environment.  
`KIDS_NOISE` | Kids noise environment.  
`CAFE` | Cafe environment.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
