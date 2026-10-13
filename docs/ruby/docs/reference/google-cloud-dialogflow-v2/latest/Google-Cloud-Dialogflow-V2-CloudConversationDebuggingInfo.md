---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CloudConversationDebuggingInfo/
title: Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::CloudConversationDebuggingInfo (v1.18.0) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:09:21.507800+00:00
---

# Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::CloudConversationDebuggingInfo (v1.18.0)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Cloud-Dialogflow-V2-CloudConversationDebuggingInfo/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Dialogflow V2 API - Class Google::Cloud::Dialogflow::V2::CloudConversationDebuggingInfo (v1.18.0) Stay organized with collections  Save and categorize content based on your preferences. 

1.18.0 (latest)  1.17.1  1.16.1  1.15.0  1.14.0  1.13.0  1.12.1  1.11.0  1.10.1  1.9.1  1.8.0  1.7.0  1.6.0  1.5.0  1.4.1  1.3.0  1.2.0  1.1.1  1.0.0  0.34.0  0.33.0  0.32.2  0.31.0  0.30.0  0.29.0  0.28.0  0.27.0  0.26.2  0.25.0  0.24.0  0.23.0  0.22.0  0.21.0  0.20.0  0.19.0  0.18.0  0.17.1  0.16.0  0.15.2  0.14.0  0.13.0  0.12.0 

Reference documentation and code samples for the Dialogflow V2 API class Google::Cloud::Dialogflow::V2::CloudConversationDebuggingInfo.

Cloud conversation info for easier debugging. It will get populated in `StreamingDetectIntentResponse` or `StreamingAnalyzeContentResponse` when the flag `enable_debugging_info` is set to true in corresponding requests.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #audio_data_chunks
    
    
    def audio_data_chunks() -> ::Integer

**Returns**

  * (::Integer) — Number of input audio data chunks in streaming requests. 



### #audio_data_chunks=
    
    
    def audio_data_chunks=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Number of input audio data chunks in streaming requests. 



**Returns**

  * (::Integer) — Number of input audio data chunks in streaming requests. 



### #bargein_event_triggered
    
    
    def bargein_event_triggered() -> ::Boolean

**Returns**

  * (::Boolean) — Whether a barge-in event is triggered in this request. 



### #bargein_event_triggered=
    
    
    def bargein_event_triggered=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether a barge-in event is triggered in this request. 



**Returns**

  * (::Boolean) — Whether a barge-in event is triggered in this request. 



### #client_half_close_streaming_time_offset
    
    
    def client_half_close_streaming_time_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Client half close time in terms of API streaming duration. 



### #client_half_close_streaming_time_offset=
    
    
    def client_half_close_streaming_time_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Client half close time in terms of API streaming duration. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Client half close time in terms of API streaming duration. 



### #client_half_close_time_offset
    
    
    def client_half_close_time_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Client half close time in terms of input audio duration. 



### #client_half_close_time_offset=
    
    
    def client_half_close_time_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Client half close time in terms of input audio duration. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Client half close time in terms of input audio duration. 



### #dtmf_final_results_times
    
    
    def dtmf_final_results_times() -> ::Array<::Google::Protobuf::Duration>

**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the DTMF final results relative to the beginning of the stream. 



### #dtmf_final_results_times=
    
    
    def dtmf_final_results_times=(value) -> ::Array<::Google::Protobuf::Duration>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the DTMF final results relative to the beginning of the stream. 



**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the DTMF final results relative to the beginning of the stream. 



### #dtmf_partial_results_times
    
    
    def dtmf_partial_results_times() -> ::Array<::Google::Protobuf::Duration>

**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the DTMF partial results relative to the beginning of the stream. 



### #dtmf_partial_results_times=
    
    
    def dtmf_partial_results_times=(value) -> ::Array<::Google::Protobuf::Duration>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the DTMF partial results relative to the beginning of the stream. 



**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the DTMF partial results relative to the beginning of the stream. 



### #endpointing_timeout
    
    
    def endpointing_timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Speech endpointing timeout settings for the stream. 



### #endpointing_timeout=
    
    
    def endpointing_timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Speech endpointing timeout settings for the stream. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Speech endpointing timeout settings for the stream. 



### #first_audio_duration
    
    
    def first_audio_duration() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Duration of first audio chunk. 



### #first_audio_duration=
    
    
    def first_audio_duration=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Duration of first audio chunk. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Duration of first audio chunk. 



### #is_input_text
    
    
    def is_input_text() -> ::Boolean

**Returns**

  * (::Boolean) — Whether the streaming terminates with an injected text query. 



### #is_input_text=
    
    
    def is_input_text=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether the streaming terminates with an injected text query. 



**Returns**

  * (::Boolean) — Whether the streaming terminates with an injected text query. 



### #no_speech_timeout
    
    
    def no_speech_timeout() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — No speech timeout settings for the stream. 



### #no_speech_timeout=
    
    
    def no_speech_timeout=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — No speech timeout settings for the stream. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — No speech timeout settings for the stream. 



### #partial_responses
    
    
    def partial_responses() -> ::Integer

**Returns**

  * (::Integer) — Total number of partial responses. 



### #partial_responses=
    
    
    def partial_responses=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Total number of partial responses. 



**Returns**

  * (::Integer) — Total number of partial responses. 



### #result_end_time_offset
    
    
    def result_end_time_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Time offset of the end of speech utterance relative to the beginning of the first audio chunk. 



### #result_end_time_offset=
    
    
    def result_end_time_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Time offset of the end of speech utterance relative to the beginning of the first audio chunk. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Time offset of the end of speech utterance relative to the beginning of the first audio chunk. 



### #single_utterance
    
    
    def single_utterance() -> ::Boolean

**Returns**

  * (::Boolean) — Whether client used single utterance mode. 



### #single_utterance=
    
    
    def single_utterance=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether client used single utterance mode. 



**Returns**

  * (::Boolean) — Whether client used single utterance mode. 



### #single_utterance_end_time_offset
    
    
    def single_utterance_end_time_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Time offset of the end-of-single-utterance signal relative to the beginning of the stream. 



### #single_utterance_end_time_offset=
    
    
    def single_utterance_end_time_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Time offset of the end-of-single-utterance signal relative to the beginning of the stream. 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)) — Time offset of the end-of-single-utterance signal relative to the beginning of the stream. 



### #speaker_id_passive_latency_ms_offset
    
    
    def speaker_id_passive_latency_ms_offset() -> ::Integer

**Returns**

  * (::Integer) — Time offset of Speaker ID stream close time relative to the Speech stream close time in milliseconds. Only meaningful for conversations involving passive verification. 



### #speaker_id_passive_latency_ms_offset=
    
    
    def speaker_id_passive_latency_ms_offset=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Time offset of Speaker ID stream close time relative to the Speech stream close time in milliseconds. Only meaningful for conversations involving passive verification. 



**Returns**

  * (::Integer) — Time offset of Speaker ID stream close time relative to the Speech stream close time in milliseconds. Only meaningful for conversations involving passive verification. 



### #speech_final_results_end_times
    
    
    def speech_final_results_end_times() -> ::Array<::Google::Protobuf::Duration>

**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the speech final results (is_final=true) relative to the beginning of the stream. 



### #speech_final_results_end_times=
    
    
    def speech_final_results_end_times=(value) -> ::Array<::Google::Protobuf::Duration>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the speech final results (is_final=true) relative to the beginning of the stream. 



**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the speech final results (is_final=true) relative to the beginning of the stream. 



### #speech_partial_results_end_times
    
    
    def speech_partial_results_end_times() -> ::Array<::Google::Protobuf::Duration>

**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the speech partial results relative to the beginning of the stream. 



### #speech_partial_results_end_times=
    
    
    def speech_partial_results_end_times=(value) -> ::Array<::Google::Protobuf::Duration>

**Parameter**

  * **value** (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the speech partial results relative to the beginning of the stream. 



**Returns**

  * (::Array<[::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-dialogflow-v2/latest/Google-Protobuf-Duration)>) — Time offsets of the speech partial results relative to the beginning of the stream. 



### #speech_single_utterance
    
    
    def speech_single_utterance() -> ::Boolean

**Returns**

  * (::Boolean) — Whether speech uses single utterance mode. 



### #speech_single_utterance=
    
    
    def speech_single_utterance=(value) -> ::Boolean

**Parameter**

  * **value** (::Boolean) — Whether speech uses single utterance mode. 



**Returns**

  * (::Boolean) — Whether speech uses single utterance mode. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
