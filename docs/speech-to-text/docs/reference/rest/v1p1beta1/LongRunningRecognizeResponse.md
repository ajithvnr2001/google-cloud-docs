---
url: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/LongRunningRecognizeResponse/
title: LongRunningRecognizeResponse \u00a0|\u00a0 Cloud Speech-to-Text \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:51:17.976705+00:00
---

# LongRunningRecognizeResponse  |  Cloud Speech-to-Text  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/LongRunningRecognizeResponse/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Cloud Speech-to-Text ](https://docs.cloud.google.com/speech-to-text/docs)
  * [ Reference ](https://docs.cloud.google.com/speech-to-text/docs/apis)



Send feedback 

#  LongRunningRecognizeResponse Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation



The only message returned to the client by the `LongRunningRecognize` method. It contains the result as zero or more sequential `SpeechRecognitionResult` messages. It is included in the `result.response` field of the `Operation` returned by the `operations.get` call of the `google::longrunning::Operations` service.

JSON representation  
---  
      
    
    {
      "results": [
        {
          object ([SpeechRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize#SpeechRecognitionResult))
        }
      ],
      "totalBilledTime": string,
      "outputConfig": {
        object ([TranscriptOutputConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/longrunningrecognize#TranscriptOutputConfig))
      },
      "outputError": {
        object ([Status](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "speechAdaptationInfo": {
        object ([SpeechAdaptationInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize#SpeechAdaptationInfo))
      },
      "requestId": string
    }  
  
Fields  
---  
`results[]` |  `object (`[SpeechRecognitionResult](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize#SpeechRecognitionResult)`)` Sequential list of transcription results corresponding to sequential portions of audio.  
`totalBilledTime` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` When available, billed audio seconds for the corresponding request.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`outputConfig` |  `object (`[TranscriptOutputConfig](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/longrunningrecognize#TranscriptOutputConfig)`)` Original output config if present in the request.  
`outputError` |  `object (`[Status](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` If the transcript output fails this field contains the relevant error.  
`speechAdaptationInfo` |  `object (`[SpeechAdaptationInfo](https://docs.cloud.google.com/speech-to-text/docs/reference/rest/v1p1beta1/speech/recognize#SpeechAdaptationInfo)`)` Provides information on speech adaptation behavior in response  
`requestId` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The ID associated with the request. This is a unique ID specific only to the given request.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-10-23 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-10-23 UTC."],[],[]] 
