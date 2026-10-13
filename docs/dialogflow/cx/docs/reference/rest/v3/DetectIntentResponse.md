---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponse/
title: DetectIntentResponse \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:23:29.086439+00:00
---

# DetectIntentResponse  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponse/

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  DetectIntentResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * ResponseType



The message returned from the DetectIntent method.

JSON representation  
---  
      
    
    {
      "responseId": string,
      "queryResult": {
        object ([QueryResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult))
      },
      "outputAudio": string,
      "outputAudioConfig": {
        object ([OutputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig))
      },
      "responseType": enum ([ResponseType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponse#ResponseType)),
      "allowCancellation": boolean
    }  
  
Fields  
---  
`responseId` |  `string` Output only. The unique identifier of the response. It can be used to locate a response in the training example set or for reporting issues.  
`queryResult` |  `object (`[QueryResult](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult)`)` The result of the conversational query.  
`outputAudio` |  `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` The audio data bytes encoded as specified in the request. Note: The output audio is generated based on the values of default platform text responses found in the `[`queryResult.response_messages`](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/QueryResult#FIELDS.response_messages)` field. If multiple default text responses exist, they will be concatenated when generating audio. If no default platform text responses exist, the generated audio content will be empty.In some scenarios, multiple output audio fields may be present in the response structure. In these cases, only the top-most-level audio output has content.A base64-encoded string.  
`outputAudioConfig` |  `object (`[OutputAudioConfig](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/OutputAudioConfig)`)` The config used by the speech synthesizer to generate the output audio.  
`responseType` |  `enum (`[ResponseType](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/DetectIntentResponse#ResponseType)`)` Response type.  
`allowCancellation` |  `boolean` Indicates whether the partial response can be cancelled when a later response arrives. e.g. if the agent specified some music as partial response, it can be cancelled.  
  
## ResponseType

Represents different DetectIntentResponse types.

Enums  
---  
`RESPONSE_TYPE_UNSPECIFIED` | Not specified. This should never happen.  
`PARTIAL` | Partial response. e.g. Aggregated responses in a Fulfillment that enables `return_partial_response` can be returned as partial response. WARNING: partial response is not eligible for barge-in.  
`FINAL` | Final response.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-06-27 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-06-27 UTC."],[],[]] 
