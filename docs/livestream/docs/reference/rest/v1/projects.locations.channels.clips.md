---
url: https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips
title: REST Resource: projects.locations.channels.clips \u00a0|\u00a0 Live Stream API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:47:34.919074+00:00
---

# REST Resource: projects.locations.channels.clips  |  Live Stream API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Live Stream API ](https://docs.cloud.google.com/livestream/docs)
  * [ Reference ](https://docs.cloud.google.com/livestream/docs/apis)



Send feedback 

#  REST Resource: projects.locations.channels.clips Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Clip
    * JSON representation
  * State
  * Slice
    * JSON representation
  * TimeSlice
    * JSON representation
  * ClipManifest
    * JSON representation
  * OutputType
  * Methods



## Resource: Clip

Clip is a sub-resource under channel. Each clip represents a clipping operation that generates a VOD playlist from its channel given a set of timestamp ranges.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "startTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "state": enum ([State](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#State)),
      "outputUri": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/Status))
      },
      "slices": [
        {
          object ([Slice](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#Slice))
        }
      ],
      "clipManifests": [
        {
          object ([ClipManifest](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#ClipManifest))
        }
      ],
      "outputType": enum ([OutputType](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#OutputType))
    }  
  
Fields  
---  
`name` |  `string` The resource name of the clip, in the following format: `projects/{project}/locations/{location}/channels/{channelId}/clips/{clipId}`. `{clipId}` is a user-specified resource id that conforms to the following criteria:

  1. 1 character minimum, 63 characters maximum
  2. Only contains letters, digits, underscores, and hyphens

  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation timestamp of the clip resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the clip request starts to be processed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The update timestamp of the clip resource.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The labels associated with this resource. Each label is a key-value pair.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#State)`)` Output only. The state of the clip.  
`outputUri` |  `string` Specify the `outputUri` to determine where to place the clip segments and clip manifest files in Cloud Storage. The manifests specified in `clipManifests` fields will be placed under this URI. The exact URI of the generated manifests will be provided in `clipManifests.output_uri` for each manifest. Example: "outputUri": "gs://my-bucket/clip-outputs" "clipManifests.output_uri": "gs://my-bucket/clip-outputs/main.m3u8"  
`error` |  `object (`[Status](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/Status)`)` Output only. An error object that describes the reason for the failure. This property only presents when `state` is `FAILED`.  
`slices[]` |  `object (`[Slice](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#Slice)`)` The specified ranges of segments to generate a clip.  
`clipManifests[]` |  `object (`[ClipManifest](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#ClipManifest)`)` Required. A list of clip manifests. Currently only one clip manifest is allowed.  
`outputType` |  `enum (`[OutputType](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#OutputType)`)` Optional. OutputType of the clip. If not specified, the default value is MANIFEST.  
  
## State

State of clipping operation.

Enums  
---  
`STATE_UNSPECIFIED` | State is not specified.  
`PENDING` | The operation is pending to be picked up by the server.  
`CREATING` | The server admitted this create clip request, and outputs are under processing.  
`SUCCEEDED` | Outputs are available in the specified Cloud Storage bucket. For additional information, see the `outputs` field.  
`FAILED` | The operation has failed. For additional information, see the `error` field.  
  
## Slice

Slice represents a slice of the requested clip.

JSON representation  
---  
      
    
    {
    
      // Union field kind can be only one of the following:
      "timeSlice": {
        object ([TimeSlice](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#TimeSlice))
      }
      // End of list of possible types for union field kind.
    }  
  
Fields  
---  
Union field `kind`. The allowlist forms of a slice. `kind` can be only one of the following:  
`timeSlice` |  `object (`[TimeSlice](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips#TimeSlice)`)` A slice in form of a tuple of Unix epoch time.  
  
## TimeSlice

TimeSlice represents a tuple of Unix epoch timestamps that specifies a time range.

JSON representation  
---  
      
    
    {
      "markinTime": string,
      "markoutTime": string
    }  
  
Fields  
---  
`markinTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The mark-in Unix epoch time in the original live stream manifest.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`markoutTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The mark-out Unix epoch time in the original live stream manifest.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## ClipManifest

ClipManifest identifies a source manifest for the generated clip manifest.

JSON representation  
---  
      
    
    {
      "manifestKey": string,
      "outputUri": string
    }  
  
Fields  
---  
`manifestKey` |  `string` Required. A unique key that identifies a manifest config in the parent channel. This key is the same as `channel.manifests.key` for the selected manifest.  
`outputUri` |  `string` Output only. The output URI of the generated clip manifest. This field will be populated when the clips.create request is accepted. Current output format is provided below but may change in the future. Please read this field to get the uri to the generated clip manifest. Format: {clip.output_uri}/{channel.manifest.fileName} Example: gs://my-bucket/clip-outputs/main.m3u8  
  
## OutputType

OutputType represents the output type of the clip.

Enums  
---  
`OUTPUT_TYPE_UNSPECIFIED` | OutputType is not specified.  
`MANIFEST` | OutputType is a VOD manifest. This is the default value.  
`MP4` | OutputType is an MP4 file.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/create)`

|  Creates a clip with the provided clip ID in the specified channel.  
  
### `[delete](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/delete)`

|  Deletes the specified clip job resource.  
  
### `[get](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/get)`

|  Returns the specified clip.  
  
### `[list](https://docs.cloud.google.com/livestream/docs/reference/rest/v1/projects.locations.channels.clips/list)`

|  Returns a list of all clips in the specified channel.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-10 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-10 UTC."],[],[]] 
