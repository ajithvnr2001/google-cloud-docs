---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Cloud-Speech-V1p1beta1-LongRunningRecognizeMetadata/
title: Cloud Speech-to-Text V1p1beta1 API - Class Google::Cloud::Speech::V1p1beta1::LongRunningRecognizeMetadata (v0.30.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T15:02:57.433752+00:00
---

# Cloud Speech-to-Text V1p1beta1 API - Class Google::Cloud::Speech::V1p1beta1::LongRunningRecognizeMetadata (v0.30.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Cloud-Speech-V1p1beta1-LongRunningRecognizeMetadata/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Cloud Speech-to-Text V1p1beta1 API - Class Google::Cloud::Speech::V1p1beta1::LongRunningRecognizeMetadata (v0.30.1) Stay organized with collections  Save and categorize content based on your preferences. 

0.30.1 (latest)  0.30.0  0.29.1  0.28.0  0.27.1  0.26.0  0.25.0  0.24.1  0.23.0  0.22.0  0.21.1  0.20.2  0.19.0  0.18.1  0.17.1  0.16.0  0.15.3  0.14.0  0.13.0  0.12.4 

Reference documentation and code samples for the Cloud Speech-to-Text V1p1beta1 API class Google::Cloud::Speech::V1p1beta1::LongRunningRecognizeMetadata.

Describes the progress of a long-running `LongRunningRecognize` call. It is included in the `metadata` field of the `Operation` returned by the `GetOperation` call of the `google::longrunning::Operations` service.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #last_update_time
    
    
    def last_update_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time of the most recent processing update. 



### #last_update_time=
    
    
    def last_update_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time of the most recent processing update. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time of the most recent processing update. 



### #output_config
    
    
    def output_config() -> ::Google::Cloud::Speech::V1p1beta1::TranscriptOutputConfig

**Returns**

  * ([::Google::Cloud::Speech::V1p1beta1::TranscriptOutputConfig](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Cloud-Speech-V1p1beta1-TranscriptOutputConfig)) — Output only. A copy of the TranscriptOutputConfig if it was set in the request. 



### #progress_percent
    
    
    def progress_percent() -> ::Integer

**Returns**

  * (::Integer) — Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available. 



### #progress_percent=
    
    
    def progress_percent=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available. 



**Returns**

  * (::Integer) — Approximate percentage of audio processed thus far. Guaranteed to be 100 when the audio is fully processed and the results are available. 



### #start_time
    
    
    def start_time() -> ::Google::Protobuf::Timestamp

**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time when the request was received. 



### #start_time=
    
    
    def start_time=(value) -> ::Google::Protobuf::Timestamp

**Parameter**

  * **value** ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time when the request was received. 



**Returns**

  * ([::Google::Protobuf::Timestamp](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-speech-v1p1beta1/latest/Google-Protobuf-Timestamp)) — Time when the request was received. 



### #uri
    
    
    def uri() -> ::String

**Returns**

  * (::String) — Output only. The URI of the audio file being transcribed. Empty if the audio was sent as byte content. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
