---
url: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings
title: REST Resource: projects.locations.geminiGcpEnablementSettings \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:48:51.849733+00:00
---

# REST Resource: projects.locations.geminiGcpEnablementSettings  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ API and references ](https://docs.cloud.google.com/gemini/docs/api-and-reference)



Send feedback 

#  REST Resource: projects.locations.geminiGcpEnablementSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: GeminiGcpEnablementSetting
    * JSON representation
  * WebGroundingType
  * Methods



## Resource: GeminiGcpEnablementSetting

Message describing GeminiGcpEnablementSetting object

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
      "enableCustomerDataSharing": boolean,
      "disableWebGrounding": boolean,
      "webGroundingType": enum ([WebGroundingType](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings#WebGroundingType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource. Format:projects/{project}/locations/{location}/geminiGcpEnablementSettings/{geminiGcpEnablementSetting}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`enableCustomerDataSharing` |  `boolean` Optional. Not implemented.  
`disableWebGrounding` |  `boolean` Optional. Whether web grounding should be disabled.  
`webGroundingType` |  `enum (`[WebGroundingType](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings#WebGroundingType)`)` Optional. Web grounding type.  
  
## WebGroundingType

Web grounding type.

Enums  
---  
`WEB_GROUNDING_TYPE_UNSPECIFIED` | Unspecified grounding.  
`GROUNDING_WITH_GOOGLE_SEARCH` | Grounding with Google Search.  
`WEB_GROUNDING_FOR_ENTERPRISE` | Grounding with Google Search for Enterprise.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings/create)`

|  Creates a new GeminiGcpEnablementSetting in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings/delete)`

|  Deletes a single GeminiGcpEnablementSetting.  
  
### `[get](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings/get)`

|  Gets details of a single GeminiGcpEnablementSetting.  
  
### `[list](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings/list)`

|  Lists GeminiGcpEnablementSettings in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.geminiGcpEnablementSettings/patch)`

|  Updates the parameters of a single GeminiGcpEnablementSetting.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-30 UTC."],[],[]] 
