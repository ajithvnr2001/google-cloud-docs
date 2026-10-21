---
url: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings
title: REST Resource: projects.locations.releaseChannelSettings \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:00:01.858881+00:00
---

# REST Resource: projects.locations.releaseChannelSettings  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ API and references ](https://docs.cloud.google.com/gemini/docs/api-and-reference)



Send feedback 

#  REST Resource: projects.locations.releaseChannelSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ReleaseChannelSetting
    * JSON representation
  * ChannelType
  * Methods



## Resource: ReleaseChannelSetting

Message describing ReleaseChannelSetting object

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
      "releaseChannel": enum ([ChannelType](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings#ChannelType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource. Format:projects/{project}/locations/{location}/releaseChannelSettings/{releaseChannelSetting}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`releaseChannel` |  `enum (`[ChannelType](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings#ChannelType)`)` Optional. Release channel to be used.  
  
## ChannelType

Release channel type.

Enums  
---  
`CHANNEL_TYPE_UNSPECIFIED` | Unspecified release channel.  
`STABLE` | Stable channel.  
`EXPERIMENTAL` | Experimental release channel.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings/create)`

|  Creates a new ReleaseChannelSetting in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings/delete)`

|  Deletes a single ReleaseChannelSetting.  
  
### `[get](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings/get)`

|  Gets details of a single ReleaseChannelSetting.  
  
### `[list](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings/list)`

|  Lists ReleaseChannelSettings in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.releaseChannelSettings/patch)`

|  Updates the parameters of a single ReleaseChannelSetting.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-12 UTC."],[],[]] 
