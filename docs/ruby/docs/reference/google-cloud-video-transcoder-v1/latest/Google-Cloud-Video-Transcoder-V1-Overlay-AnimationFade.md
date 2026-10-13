---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-AnimationFade/
title: Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::Overlay::AnimationFade (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:05:49.045057+00:00
---

# Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::Overlay::AnimationFade (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-AnimationFade/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::Overlay::AnimationFade (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Transcoder V1 API class Google::Cloud::Video::Transcoder::V1::Overlay::AnimationFade.

Display overlay object with fade animation.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #end_time_offset
    
    
    def end_time_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Protobuf-Duration)) — The time to end the fade animation, in seconds. Default: `start_time_offset` \+ 1s 



### #end_time_offset=
    
    
    def end_time_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Protobuf-Duration)) — The time to end the fade animation, in seconds. Default: `start_time_offset` \+ 1s 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Protobuf-Duration)) — The time to end the fade animation, in seconds. Default: `start_time_offset` \+ 1s 



### #fade_type
    
    
    def fade_type() -> ::Google::Cloud::Video::Transcoder::V1::Overlay::FadeType

**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::Overlay::FadeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-FadeType)) — Required. Type of fade animation: `FADE_IN` or `FADE_OUT`. 



### #fade_type=
    
    
    def fade_type=(value) -> ::Google::Cloud::Video::Transcoder::V1::Overlay::FadeType

**Parameter**

  * **value** ([::Google::Cloud::Video::Transcoder::V1::Overlay::FadeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-FadeType)) — Required. Type of fade animation: `FADE_IN` or `FADE_OUT`. 



**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::Overlay::FadeType](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-FadeType)) — Required. Type of fade animation: `FADE_IN` or `FADE_OUT`. 



### #start_time_offset
    
    
    def start_time_offset() -> ::Google::Protobuf::Duration

**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Protobuf-Duration)) — The time to start the fade animation, in seconds. Default: 0 



### #start_time_offset=
    
    
    def start_time_offset=(value) -> ::Google::Protobuf::Duration

**Parameter**

  * **value** ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Protobuf-Duration)) — The time to start the fade animation, in seconds. Default: 0 



**Returns**

  * ([::Google::Protobuf::Duration](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Protobuf-Duration)) — The time to start the fade animation, in seconds. Default: 0 



### #xy
    
    
    def xy() -> ::Google::Cloud::Video::Transcoder::V1::Overlay::NormalizedCoordinate

**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::Overlay::NormalizedCoordinate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-NormalizedCoordinate)) — Normalized coordinates based on output video resolution. Valid values: `0.0`–`1.0`. `xy` is the upper-left coordinate of the overlay object. For example, use the x and y coordinates {0,0} to position the top-left corner of the overlay animation in the top-left corner of the output video. 



### #xy=
    
    
    def xy=(value) -> ::Google::Cloud::Video::Transcoder::V1::Overlay::NormalizedCoordinate

**Parameter**

  * **value** ([::Google::Cloud::Video::Transcoder::V1::Overlay::NormalizedCoordinate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-NormalizedCoordinate)) — Normalized coordinates based on output video resolution. Valid values: `0.0`–`1.0`. `xy` is the upper-left coordinate of the overlay object. For example, use the x and y coordinates {0,0} to position the top-left corner of the overlay animation in the top-left corner of the output video. 



**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::Overlay::NormalizedCoordinate](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Overlay-NormalizedCoordinate)) — Normalized coordinates based on output video resolution. Valid values: `0.0`–`1.0`. `xy` is the upper-left coordinate of the overlay object. For example, use the x and y coordinates {0,0} to position the top-left corner of the overlay animation in the top-left corner of the output video. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
