---
url: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.StreamingRecognitionConfig
title: Class StreamingRecognitionConfig (2.41.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:09:13.259491+00:00
---

# Class StreamingRecognitionConfig (2.41.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.StreamingRecognitionConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class StreamingRecognitionConfig (2.41.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.41.0 (latest)  2.40.0  2.39.0  2.38.0  2.37.0  2.36.1  2.35.0  2.34.0  2.33.0  2.32.0  2.31.0  2.30.0  2.29.0  2.28.1  2.27.0  2.26.1  2.25.1  2.24.1  2.23.0  2.22.0  2.21.1  2.20.1  2.19.0  2.18.0  2.17.3  2.16.2  2.15.1  2.14.1  2.13.1  2.12.0  2.11.1  2.10.0  2.9.3  2.8.0  2.7.0  2.6.0  2.5.1  2.4.1  2.3.0  2.2.1  2.1.0  2.0.1  1.3.4  1.2.0  1.1.0 
    
    
    StreamingRecognitionConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Provides information to the recognizer that specifies how to process the request.

## Attributes  
  
---  
**Name** | **Description**  
`config` |  `[google.cloud.speech_v1.types.RecognitionConfig](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.RecognitionConfig)`   
Required. Provides information to the recognizer that specifies how to process the request.   
`single_utterance` |  `bool`   
If `false` or omitted, the recognizer will perform continuous recognition (continuing to wait for and process audio even if the user pauses speaking) until the client closes the input stream (gRPC API) or until the maximum time limit has been reached. May return multiple `StreamingRecognitionResult`\ s with the `is_final` flag set to `true`. If `true`, the recognizer will detect a single spoken utterance. When it detects that the user has paused or stopped speaking, it will return an `END_OF_SINGLE_UTTERANCE` event and cease recognition. It will return no more than one `StreamingRecognitionResult` with the `is_final` flag set to `true`. The `single_utterance` field can only be used with specified models, otherwise an error is thrown. The `model` field in [`RecognitionConfig`][] must be set to: \- `command_and_search` \- `phone_call` AND additional field `useEnhanced`\ =\ `true` \- The `model` field is left undefined. In this case the API auto-selects a model based on any other parameters that you set in `RecognitionConfig`.   
`interim_results` |  `bool`   
If `true`, interim results (tentative hypotheses) may be returned as they become available (these interim results are indicated with the `is_final=false` flag). If `false` or omitted, only `is_final=true` result(s) are returned.   
`enable_voice_activity_events` |  `bool`   
If `true`, responses with voice activity speech events will be returned as they are detected.   
`voice_activity_timeout` |  `[google.cloud.speech_v1.types.StreamingRecognitionConfig.VoiceActivityTimeout](https://docs.cloud.google.com/python/docs/reference/speech/latest/google.cloud.speech_v1.types.StreamingRecognitionConfig.VoiceActivityTimeout)`   
If set, the server will automatically close the stream after the specified duration has elapsed after the last VOICE_ACTIVITY speech event has been sent. The field `voice_activity_events` must also be set to true.   
  
## Classes 

### VoiceActivityTimeout
    
    
    VoiceActivityTimeout(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Events that a timeout can be set on for voice activity.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
