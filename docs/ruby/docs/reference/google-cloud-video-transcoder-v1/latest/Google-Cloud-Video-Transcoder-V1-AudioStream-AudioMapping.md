---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-AudioStream-AudioMapping/
title: Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::AudioStream::AudioMapping (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:34:40.157738+00:00
---

# Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::AudioStream::AudioMapping (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-AudioStream-AudioMapping/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::AudioStream::AudioMapping (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Transcoder V1 API class Google::Cloud::Video::Transcoder::V1::AudioStream::AudioMapping.

The mapping for the [JobConfig.edit_list](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-JobConfig#Google__Cloud__Video__Transcoder__V1__JobConfig_edit_list_instance_ "Google::Cloud::Video::Transcoder::V1::JobConfig#edit_list \(method\)") atoms with audio [EditAtom.inputs](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-EditAtom#Google__Cloud__Video__Transcoder__V1__EditAtom_inputs_instance_ "Google::Cloud::Video::Transcoder::V1::EditAtom#inputs \(method\)").

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #atom_key
    
    
    def atom_key() -> ::String

**Returns**

  * (::String) — Required. The [EditAtom.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-EditAtom#Google__Cloud__Video__Transcoder__V1__EditAtom_key_instance_ "Google::Cloud::Video::Transcoder::V1::EditAtom#key \(method\)") that references the atom with audio inputs in the [JobConfig.edit_list](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-JobConfig#Google__Cloud__Video__Transcoder__V1__JobConfig_edit_list_instance_ "Google::Cloud::Video::Transcoder::V1::JobConfig#edit_list \(method\)"). 



### #atom_key=
    
    
    def atom_key=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The [EditAtom.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-EditAtom#Google__Cloud__Video__Transcoder__V1__EditAtom_key_instance_ "Google::Cloud::Video::Transcoder::V1::EditAtom#key \(method\)") that references the atom with audio inputs in the [JobConfig.edit_list](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-JobConfig#Google__Cloud__Video__Transcoder__V1__JobConfig_edit_list_instance_ "Google::Cloud::Video::Transcoder::V1::JobConfig#edit_list \(method\)"). 



**Returns**

  * (::String) — Required. The [EditAtom.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-EditAtom#Google__Cloud__Video__Transcoder__V1__EditAtom_key_instance_ "Google::Cloud::Video::Transcoder::V1::EditAtom#key \(method\)") that references the atom with audio inputs in the [JobConfig.edit_list](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-JobConfig#Google__Cloud__Video__Transcoder__V1__JobConfig_edit_list_instance_ "Google::Cloud::Video::Transcoder::V1::JobConfig#edit_list \(method\)"). 



### #gain_db
    
    
    def gain_db() -> ::Float

**Returns**

  * (::Float) — Audio volume control in dB. Negative values decrease volume, positive values increase. The default is 0. 



### #gain_db=
    
    
    def gain_db=(value) -> ::Float

**Parameter**

  * **value** (::Float) — Audio volume control in dB. Negative values decrease volume, positive values increase. The default is 0. 



**Returns**

  * (::Float) — Audio volume control in dB. Negative values decrease volume, positive values increase. The default is 0. 



### #input_channel
    
    
    def input_channel() -> ::Integer

**Returns**

  * (::Integer) — Required. The zero-based index of the channel in the input audio stream. 



### #input_channel=
    
    
    def input_channel=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The zero-based index of the channel in the input audio stream. 



**Returns**

  * (::Integer) — Required. The zero-based index of the channel in the input audio stream. 



### #input_key
    
    
    def input_key() -> ::String

**Returns**

  * (::String) — Required. The [Input.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Input#Google__Cloud__Video__Transcoder__V1__Input_key_instance_ "Google::Cloud::Video::Transcoder::V1::Input#key \(method\)") that identifies the input file. 



### #input_key=
    
    
    def input_key=(value) -> ::String

**Parameter**

  * **value** (::String) — Required. The [Input.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Input#Google__Cloud__Video__Transcoder__V1__Input_key_instance_ "Google::Cloud::Video::Transcoder::V1::Input#key \(method\)") that identifies the input file. 



**Returns**

  * (::String) — Required. The [Input.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-Input#Google__Cloud__Video__Transcoder__V1__Input_key_instance_ "Google::Cloud::Video::Transcoder::V1::Input#key \(method\)") that identifies the input file. 



### #input_track
    
    
    def input_track() -> ::Integer

**Returns**

  * (::Integer) — Required. The zero-based index of the track in the input file. 



### #input_track=
    
    
    def input_track=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The zero-based index of the track in the input file. 



**Returns**

  * (::Integer) — Required. The zero-based index of the track in the input file. 



### #output_channel
    
    
    def output_channel() -> ::Integer

**Returns**

  * (::Integer) — Required. The zero-based index of the channel in the output audio stream. 



### #output_channel=
    
    
    def output_channel=(value) -> ::Integer

**Parameter**

  * **value** (::Integer) — Required. The zero-based index of the channel in the output audio stream. 



**Returns**

  * (::Integer) — Required. The zero-based index of the channel in the output audio stream. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
