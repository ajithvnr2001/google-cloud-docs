---
url: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/DetectIntentResponse/
title: DetectIntentResponse \u00a0|\u00a0 Dialogflow ES \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:31:20.591336+00:00
---

# DetectIntentResponse  |  Dialogflow ES  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/DetectIntentResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow ES ](https://docs.cloud.google.com/dialogflow/es/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/es/docs/reference)



Send feedback 

#  DetectIntentResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The message returned from the [DetectIntent][] method.

JSON representation  
---  
      
    
    {
      "responseId": string,
      "queryResult": {
        object ([QueryResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryResult))
      },
      "webhookStatus": {
        object ([Status](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Status))
      },
      "outputAudio": string,
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/OutputAudioConfig))
      }
    }  
  
Fields  
---  
`responseId` |  `string` The unique identifier of the response. It can be used to locate a response in the training example set or for reporting issues.  
`queryResult` |  `object (`[QueryResult](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/QueryResult)`)` The selected results of the conversational query or event processing. See `alternativeQueryResults` for additional potential results.  
`webhookStatus` |  `object (`[Status](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/Status)`)` Specifies the status of the webhook request.  
`outputAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The audio data bytes encoded as specified in the request. Note: The output audio is generated based on the values of default platform text responses found in the `queryResult.fulfillment_messages` field. If multiple default text responses exist, they will be concatenated when generating audio. If no default platform text responses exist, the generated audio content will be empty.In some scenarios, multiple output audio fields may be present in the response structure. In these cases, only the top-most-level audio output has content.A base64-encoded string.  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/dialogflow/es/docs/reference/rest/v2/OutputAudioConfig)`)` The config used by the speech synthesizer to generate the output audio.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
