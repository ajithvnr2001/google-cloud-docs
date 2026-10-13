---
url: https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs
title: REST Resource: projects.locations.inputs \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T20:03:09.069443+00:00
---

# REST Resource: projects.locations.inputs  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Reference ](https://docs.cloud.google.com/livestream/docs/apis)



Send feedback 

#  REST Resource: projects.locations.inputs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Input
    * JSON representation
  * Type
  * Tier
  * PreprocessingConfig
    * JSON representation
  * Audio
    * JSON representation
  * Crop
    * JSON representation
  * Pad
    * JSON representation
  * SecurityRule
    * JSON representation
  * InputStreamProperty
    * JSON representation
  * VideoStreamProperty
    * JSON representation
  * VideoFormat
    * JSON representation
  * AudioStreamProperty
    * JSON representation
  * AudioFormat
    * JSON representation
  * Methods



## Resource: Input

Input resource represents the endpoint from which the channel ingests the input stream.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "type": enum ([Type](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Type)),
      "tier": enum ([Tier](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Tier)),
      "uri": string,
      "preprocessingConfig": {
        object ([PreprocessingConfig](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#PreprocessingConfig))
      },
      "securityRules": {
        object ([SecurityRule](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#SecurityRule))
      },
      "inputStreamProperty": {
        object ([InputStreamProperty](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#InputStreamProperty))
      }
    }  
  
Fields  
---  
`name` |  `string` The resource name of the input, in the form of: `projects/{project}/locations/{location}/inputs/{inputId}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` User-defined key/value metadata.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Type)`)` Source type.  
`tier` |  `enum (`[Tier](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Tier)`)` Tier defines the maximum input specification that is accepted by the video pipeline. The billing is charged based on the tier specified here. See [Pricing](https://cloud.google.com/livestream/pricing) for more detail. The default is `HD`.  
`uri` |  `string` Output only. URI to push the input stream to. Its format depends on the input `[type](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Input.FIELDS.type)`, for example:

  * `RTMP_PUSH`: `rtmp://1.2.3.4/live/{STREAM-ID}`
  * `SRT_PUSH`: `srt://1.2.3.4:4201?streamid={STREAM-ID}`

  
`preprocessingConfig` |  `object (`[PreprocessingConfig](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#PreprocessingConfig)`)` Preprocessing configurations.  
`securityRules` |  `object (`[SecurityRule](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#SecurityRule)`)` Security rule for access control.  
`inputStreamProperty` |  `object (`[InputStreamProperty](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#InputStreamProperty)`)` Output only. The information for the input stream. This field will be present only when this input receives the input stream.  
  
## Type

The type of the input.

Enums  
---  
`TYPE_UNSPECIFIED` | Input type is not specified.  
`RTMP_PUSH` | Input will take an rtmp input stream.  
`SRT_PUSH` | Input will take an srt (Secure Reliable Transport) input stream.  
  
## Tier

Tier of the input specification.

Enums  
---  
`TIER_UNSPECIFIED` | Tier is not specified.  
`SD` | Resolution < 1280x720. Bitrate <= 6 Mbps. FPS <= 60.  
`HD` | Resolution <= 1920x1080. Bitrate <= 25 Mbps. FPS <= 60.  
`UHD` | Resolution <= 4096x2160. Bitrate <= 50 Mbps. FPS <= 60.  
`SD_H265` | Resolution <= 1280x720. Bitrate <= 6 Mbps. FPS <= 60. H265 codec.  
`HD_H265` | Resolution <= 1920x1080. Bitrate <= 25 Mbps. FPS <= 60. H265 codec.  
`UHD_H265` | Resolution <= 4096x2160. Bitrate <= 50 Mbps. FPS <= 60. H265 codec.  
  
## PreprocessingConfig

Preprocessing configurations.

JSON representation  
---  
      
    
    {
      "audio": {
        object ([Audio](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Audio))
      },
      "crop": {
        object ([Crop](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Crop))
      },
      "pad": {
        object ([Pad](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Pad))
      }
    }  
  
Fields  
---  
`audio` |  `object (`[Audio](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Audio)`)` Audio preprocessing configuration.  
`crop` |  `object (`[Crop](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Crop)`)` Specify the video cropping configuration.  
`pad` |  `object (`[Pad](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#Pad)`)` Specify the video pad filter configuration.  
  
## Audio

Audio preprocessing configuration.

JSON representation  
---  
      
    
    {
      "lufs": number
    }  
  
Fields  
---  
`lufs` |  `number` Specify audio loudness normalization in loudness units relative to full scale (LUFS). Enter a value between -24 and 0 according to the following:

  * -24 is the Advanced Television Systems Committee (ATSC A/85)
  * -23 is the EU R128 broadcast standard
  * -19 is the prior standard for online mono audio
  * -18 is the ReplayGain standard
  * -16 is the prior standard for stereo audio
  * -14 is the new online audio standard recommended by Spotify, as well as Amazon Echo
  * 0 disables normalization. The default is 0.

  
  
## Crop

Video cropping configuration for the input video. The cropped input video is scaled to match the output resolution.

JSON representation  
---  
      
    
    {
      "topPixels": integer,
      "bottomPixels": integer,
      "leftPixels": integer,
      "rightPixels": integer
    }  
  
Fields  
---  
`topPixels` |  `integer` The number of pixels to crop from the top. The default is 0.  
`bottomPixels` |  `integer` The number of pixels to crop from the bottom. The default is 0.  
`leftPixels` |  `integer` The number of pixels to crop from the left. The default is 0.  
`rightPixels` |  `integer` The number of pixels to crop from the right. The default is 0.  
  
## Pad

Pad filter configuration for the input video. The padded input video is scaled after padding with black to match the output resolution.

JSON representation  
---  
      
    
    {
      "topPixels": integer,
      "bottomPixels": integer,
      "leftPixels": integer,
      "rightPixels": integer
    }  
  
Fields  
---  
`topPixels` |  `integer` The number of pixels to add to the top. The default is 0.  
`bottomPixels` |  `integer` The number of pixels to add to the bottom. The default is 0.  
`leftPixels` |  `integer` The number of pixels to add to the left. The default is 0.  
`rightPixels` |  `integer` The number of pixels to add to the right. The default is 0.  
  
## SecurityRule

Security rules for access control. Each field represents one security rule. Only when the source of the input stream satisfies all the fields, this input stream can be accepted.

JSON representation  
---  
      
    
    {
      "ipRanges": [
        string
      ]
    }  
  
Fields  
---  
`ipRanges[]` |  `string` At least one ip range must match unless none specified. The IP range is defined by CIDR block: for example, `192.0.1.0/24` for a range and `192.0.1.0/32` for a single IP address.  
  
## InputStreamProperty

Properties of the input stream.

JSON representation  
---  
      
    
    {
      "lastEstablishTime": string,
      "videoStreams": [
        {
          object ([VideoStreamProperty](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#VideoStreamProperty))
        }
      ],
      "audioStreams": [
        {
          object ([AudioStreamProperty](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#AudioStreamProperty))
        }
      ]
    }  
  
Fields  
---  
`lastEstablishTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time that the current input stream is accepted and the connection is established.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`videoStreams[]` |  `object (`[VideoStreamProperty](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#VideoStreamProperty)`)` Properties of the video streams.  
`audioStreams[]` |  `object (`[AudioStreamProperty](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#AudioStreamProperty)`)` Properties of the audio streams.  
  
## VideoStreamProperty

Properties of the video stream.

JSON representation  
---  
      
    
    {
      "index": integer,
      "videoFormat": {
        object ([VideoFormat](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#VideoFormat))
      }
    }  
  
Fields  
---  
`index` |  `integer` Index of this video stream.  
`videoFormat` |  `object (`[VideoFormat](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#VideoFormat)`)` Properties of the video format.  
  
## VideoFormat

Properties of the video format.

JSON representation  
---  
      
    
    {
      "codec": string,
      "widthPixels": integer,
      "heightPixels": integer,
      "frameRate": number
    }  
  
Fields  
---  
`codec` |  `string` Video codec used in this video stream.  
`widthPixels` |  `integer` The width of the video stream in pixels.  
`heightPixels` |  `integer` The height of the video stream in pixels.  
`frameRate` |  `number` The frame rate of the input video stream.  
  
## AudioStreamProperty

Properties of the audio stream.

JSON representation  
---  
      
    
    {
      "index": integer,
      "audioFormat": {
        object ([AudioFormat](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#AudioFormat))
      }
    }  
  
Fields  
---  
`index` |  `integer` Index of this audio stream.  
`audioFormat` |  `object (`[AudioFormat](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs#AudioFormat)`)` Properties of the audio format.  
  
## AudioFormat

Properties of the audio format.

JSON representation  
---  
      
    
    {
      "codec": string,
      "channelCount": integer,
      "channelLayout": [
        string
      ]
    }  
  
Fields  
---  
`codec` |  `string` Audio codec used in this audio stream.  
`channelCount` |  `integer` The number of audio channels.  
`channelLayout[]` |  `string` A list of channel names specifying the layout of the audio channels.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/create)`

|  Creates an input with the provided unique ID in the specified region.  
  
### `[delete](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/delete)`

|  Deletes the specified input.  
  
### `[get](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/get)`

|  Returns the specified input.  
  
### `[list](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/list)`

|  Returns a list of all inputs in the specified region.  
  
### `[patch](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/patch)`

|  Updates the specified input.  
  
### `[preview](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.inputs/preview)`

|  Preview the streaming content of the specified input.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-16 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-16 UTC."],[],[]] 
