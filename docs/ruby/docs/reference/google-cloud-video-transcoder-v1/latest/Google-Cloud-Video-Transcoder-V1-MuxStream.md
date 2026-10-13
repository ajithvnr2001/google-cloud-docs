---
url: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream/
title: Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::MuxStream (v2.6.1) \u00a0|\u00a0 Ruby client libraries \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:31:26.287178+00:00
---

# Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::MuxStream (v2.6.1)  |  Ruby client libraries  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Developer tools ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Google Cloud SDK ](https://docs.cloud.google.com/sdk/docs)
  * [ Ruby ](https://docs.cloud.google.com/ruby/docs)
  * [ Client libraries ](https://docs.cloud.google.com/ruby/docs/reference)



Send feedback 

#  Transcoder V1 API - Class Google::Cloud::Video::Transcoder::V1::MuxStream (v2.6.1) Stay organized with collections  Save and categorize content based on your preferences. 

2.6.1 (latest)  2.6.0  2.5.0  2.4.1  2.3.0  2.2.0  2.1.0  2.0.1  1.2.0  1.1.0  1.0.1  0.13.0  0.12.2  0.11.0  0.10.0  0.9.1  0.8.0  0.7.0  0.6.0  0.5.0  0.4.0  0.3.0  0.2.2 

Reference documentation and code samples for the Transcoder V1 API class Google::Cloud::Video::Transcoder::V1::MuxStream.

Multiplexing settings for output stream.

## Inherits

  * Object 



## Extended By

  * Google::Protobuf::MessageExts::ClassMethods 



## Includes

  * Google::Protobuf::MessageExts 



## Methods 

### #container
    
    
    def container() -> ::String

**Returns**

  * (::String) — The container format. The default is `mp4`

Supported streaming formats:

    * `ts`
    * `fmp4`\- the corresponding file extension is `.m4s`

Supported standalone file formats:

    * `mp4`
    * `mp3`
    * `ogg`
    * `vtt`

See also: [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats)




### #container=
    
    
    def container=(value) -> ::String

**Parameter**

  * **value** (::String) — The container format. The default is `mp4`

Supported streaming formats:

    * `ts`
    * `fmp4`\- the corresponding file extension is `.m4s`

Supported standalone file formats:

    * `mp4`
    * `mp3`
    * `ogg`
    * `vtt`

See also: [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats)




**Returns**

  * (::String) — The container format. The default is `mp4`

Supported streaming formats:

    * `ts`
    * `fmp4`\- the corresponding file extension is `.m4s`

Supported standalone file formats:

    * `mp4`
    * `mp3`
    * `ogg`
    * `vtt`

See also: [Supported input and output formats](https://cloud.google.com/transcoder/docs/concepts/supported-input-and-output-formats)




### #elementary_streams
    
    
    def elementary_streams() -> ::Array<::String>

**Returns**

  * (::Array<::String>) — List of [ElementaryStream.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-ElementaryStream#Google__Cloud__Video__Transcoder__V1__ElementaryStream_key_instance_ "Google::Cloud::Video::Transcoder::V1::ElementaryStream#key \(method\)") values multiplexed in this stream. 



### #elementary_streams=
    
    
    def elementary_streams=(value) -> ::Array<::String>

**Parameter**

  * **value** (::Array<::String>) — List of [ElementaryStream.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-ElementaryStream#Google__Cloud__Video__Transcoder__V1__ElementaryStream_key_instance_ "Google::Cloud::Video::Transcoder::V1::ElementaryStream#key \(method\)") values multiplexed in this stream. 



**Returns**

  * (::Array<::String>) — List of [ElementaryStream.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-ElementaryStream#Google__Cloud__Video__Transcoder__V1__ElementaryStream_key_instance_ "Google::Cloud::Video::Transcoder::V1::ElementaryStream#key \(method\)") values multiplexed in this stream. 



### #encryption_id
    
    
    def encryption_id() -> ::String

**Returns**

  * (::String) — Identifier of the encryption configuration to use. If omitted, output will be unencrypted. 



### #encryption_id=
    
    
    def encryption_id=(value) -> ::String

**Parameter**

  * **value** (::String) — Identifier of the encryption configuration to use. If omitted, output will be unencrypted. 



**Returns**

  * (::String) — Identifier of the encryption configuration to use. If omitted, output will be unencrypted. 



### #file_name
    
    
    def file_name() -> ::String

**Returns**

  * (::String) — The name of the generated file. The default is [MuxStream.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream#Google__Cloud__Video__Transcoder__V1__MuxStream_key_instance_ "Google::Cloud::Video::Transcoder::V1::MuxStream#key \(method\)") with the extension suffix corresponding to the [MuxStream.container](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream#Google__Cloud__Video__Transcoder__V1__MuxStream_container_instance_ "Google::Cloud::Video::Transcoder::V1::MuxStream#container \(method\)").

Individual segments also have an incremental 10-digit zero-padded suffix starting from 0 before the extension, such as `mux_stream0000000123.ts`. 




### #file_name=
    
    
    def file_name=(value) -> ::String

**Parameter**

  * **value** (::String) — The name of the generated file. The default is [MuxStream.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream#Google__Cloud__Video__Transcoder__V1__MuxStream_key_instance_ "Google::Cloud::Video::Transcoder::V1::MuxStream#key \(method\)") with the extension suffix corresponding to the [MuxStream.container](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream#Google__Cloud__Video__Transcoder__V1__MuxStream_container_instance_ "Google::Cloud::Video::Transcoder::V1::MuxStream#container \(method\)").

Individual segments also have an incremental 10-digit zero-padded suffix starting from 0 before the extension, such as `mux_stream0000000123.ts`. 




**Returns**

  * (::String) — The name of the generated file. The default is [MuxStream.key](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream#Google__Cloud__Video__Transcoder__V1__MuxStream_key_instance_ "Google::Cloud::Video::Transcoder::V1::MuxStream#key \(method\)") with the extension suffix corresponding to the [MuxStream.container](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream#Google__Cloud__Video__Transcoder__V1__MuxStream_container_instance_ "Google::Cloud::Video::Transcoder::V1::MuxStream#container \(method\)").

Individual segments also have an incremental 10-digit zero-padded suffix starting from 0 before the extension, such as `mux_stream0000000123.ts`. 




### #fmp4
    
    
    def fmp4() -> ::Google::Cloud::Video::Transcoder::V1::MuxStream::Fmp4Config

**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::MuxStream::Fmp4Config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream-Fmp4Config)) — Optional. `fmp4` container configuration. 



### #fmp4=
    
    
    def fmp4=(value) -> ::Google::Cloud::Video::Transcoder::V1::MuxStream::Fmp4Config

**Parameter**

  * **value** ([::Google::Cloud::Video::Transcoder::V1::MuxStream::Fmp4Config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream-Fmp4Config)) — Optional. `fmp4` container configuration. 



**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::MuxStream::Fmp4Config](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-MuxStream-Fmp4Config)) — Optional. `fmp4` container configuration. 



### #key
    
    
    def key() -> ::String

**Returns**

  * (::String) — A unique key for this multiplexed stream. 



### #key=
    
    
    def key=(value) -> ::String

**Parameter**

  * **value** (::String) — A unique key for this multiplexed stream. 



**Returns**

  * (::String) — A unique key for this multiplexed stream. 



### #segment_settings
    
    
    def segment_settings() -> ::Google::Cloud::Video::Transcoder::V1::SegmentSettings

**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::SegmentSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-SegmentSettings)) — Segment settings for `ts`, `fmp4` and `vtt`. 



### #segment_settings=
    
    
    def segment_settings=(value) -> ::Google::Cloud::Video::Transcoder::V1::SegmentSettings

**Parameter**

  * **value** ([::Google::Cloud::Video::Transcoder::V1::SegmentSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-SegmentSettings)) — Segment settings for `ts`, `fmp4` and `vtt`. 



**Returns**

  * ([::Google::Cloud::Video::Transcoder::V1::SegmentSettings](https://docs.cloud.google.com/ruby/docs/reference/google-cloud-video-transcoder-v1/latest/Google-Cloud-Video-Transcoder-V1-SegmentSettings)) — Segment settings for `ts`, `fmp4` and `vtt`. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-03 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-03 UTC."],[],[]] 
