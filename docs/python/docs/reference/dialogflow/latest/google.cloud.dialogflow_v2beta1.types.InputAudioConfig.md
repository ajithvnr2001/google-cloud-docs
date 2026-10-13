---
url: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InputAudioConfig
title: Class InputAudioConfig (2.52.0) \u00a0|\u00a0 Python client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:07:40.910438+00:00
---

# Class InputAudioConfig (2.52.0)  |  Python client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.InputAudioConfig

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Python ](https://docs.cloud.google.com/python/docs)
  * [ Client libraries ](https://docs.cloud.google.com/python/docs/reference)



Send feedback 

#  Class InputAudioConfig (2.52.0) Stay organized with collections  Save and categorize content based on your preferences. 

2.52.0 (latest)  2.51.0  2.50.0  2.49.0  2.48.0  2.47.0  2.46.0  2.45.0  2.44.0  2.43.0  2.42.0  2.41.2  2.40.0  2.39.1  2.38.0  2.37.0  2.36.0  2.35.0  2.34.0  2.33.0  2.32.0  2.30.2  2.29.0  2.28.3  2.27.0  2.26.0  2.25.0  2.24.1  2.23.3  2.22.0  2.21.0  2.20.0  2.19.1  2.18.0  2.17.0  2.16.1  2.15.2  2.14.1  2.13.0  2.12.0  2.11.0  2.10.0  2.9.1  2.8.1  2.7.1  2.6.0  2.5.0  2.4.0  2.3.0  2.2.0  2.1.2  2.0.0  1.1.3  1.0.0  0.8.0  0.7.2 
    
    
    InputAudioConfig(mapping=None, *, ignore_unknown_fields=False, **kwargs)

Instructs the speech recognizer on how to process the audio content.

## Attributes  
  
---  
**Name** | **Description**  
`audio_encoding` |  `[google.cloud.dialogflow_v2beta1.types.AudioEncoding](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.AudioEncoding)`   
Required. Audio encoding of the audio content to process.   
`sample_rate_hertz` |  `int`   
Required. Sample rate (in Hertz) of the audio content sent in the query. Refer to `Cloud Speech API documentation   
`language_code` |  `str`   
Required. The language of the supplied audio. Dialogflow does not do translations. See `Language Support   
`enable_word_info` |  `bool`   
If `true`, Dialogflow returns SpeechWordInfo in StreamingRecognitionResult with information about the recognized speech words, e.g. start and end time offsets. If false or unspecified, Speech doesn't return any word-level information.   
`phrase_hints` |  `MutableSequence[str]`   
A list of strings containing words and phrases that the speech recognizer should recognize with higher likelihood. See `the Cloud Speech documentation   
`speech_contexts` |  `MutableSequence[[google.cloud.dialogflow_v2beta1.types.SpeechContext](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SpeechContext)]`   
Context information to assist speech recognition. See `the Cloud Speech documentation   
`model` |  `str`   
Optional. Which Speech model to select for the given request. For more information, see `Speech models   
`model_variant` |  `[google.cloud.dialogflow_v2beta1.types.SpeechModelVariant](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.SpeechModelVariant)`   
Which variant of the [Speech model][google.cloud.dialogflow.v2beta1.InputAudioConfig.model] to use.   
`single_utterance` |  `bool`   
If `false` (default), recognition does not cease until the client closes the stream. If `true`, the recognizer will detect a single spoken utterance in input audio. Recognition ceases when it detects the audio's voice has stopped or paused. In this case, once a detected intent is received, the client should close the stream and start a new request with a new stream as needed. Note: This setting is relevant only for streaming methods. Note: When specified, InputAudioConfig.single_utterance takes precedence over StreamingDetectIntentRequest.single_utterance.   
`enable_voice_activity_events` |  `bool`   
Optional. If `true`, responses with voice activity speech events will be returned as they are detected. Note: This setting is relevant only for streaming methods.   
`disable_no_speech_recognized_event` |  `bool`   
Only used in Participants.AnalyzeContent and Participants.StreamingAnalyzeContent. If `false` and recognition doesn't return any result, trigger `NO_SPEECH_RECOGNIZED` event to Dialogflow agent.   
`barge_in_config` |  `[google.cloud.dialogflow_v2beta1.types.BargeInConfig](https://docs.cloud.google.com/python/docs/reference/dialogflow/latest/google.cloud.dialogflow_v2beta1.types.BargeInConfig)`   
Configuration of barge-in behavior during the streaming of input audio.   
`enable_automatic_punctuation` |  `bool`   
Enable automatic punctuation option at the speech backend.   
`default_no_speech_timeout` |  `google.protobuf.duration_pb2.Duration`   
If set, use this no-speech timeout when the agent does not provide a no-speech timeout itself.   
`phrase_sets` |  `MutableSequence[str]`   
A collection of phrase set resources to use for speech adaptation.   
`opt_out_conformer_model_migration` |  `bool`   
If `true`, the request will opt out for STT conformer model migration. This field will be deprecated once force migration takes place in June 2024. Please refer to `Dialogflow ES Speech model migration   
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-02 UTC."],[],[]] 
