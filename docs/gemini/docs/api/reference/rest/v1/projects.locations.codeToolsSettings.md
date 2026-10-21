---
url: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings
title: REST Resource: projects.locations.codeToolsSettings \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:51:37.594923+00:00
---

# REST Resource: projects.locations.codeToolsSettings  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ API and references ](https://docs.cloud.google.com/gemini/docs/api-and-reference)



Send feedback 

#  REST Resource: projects.locations.codeToolsSettings Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CodeToolsSetting
    * JSON representation
  * ToolSetting
    * JSON representation
  * ConfigItem
    * JSON representation
  * Methods



## Resource: CodeToolsSetting

Message describing CodeToolsSetting object

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
      "enabledTool": [
        {
          object ([ToolSetting](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings#ToolSetting))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the resource. Format:projects/{project}/locations/{location}/codeToolsSettings/{codeToolsSetting}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update time stamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels as key value pairs.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`enabledTool[]` |  `object (`[ToolSetting](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings#ToolSetting)`)` Required. Represents the full set of enabled tools.  
  
## ToolSetting

Represents a single enabled tool.

JSON representation  
---  
      
    
    {
      "accountConnector": string,
      "handle": string,
      "tool": string,
      "config": [
        {
          object ([ConfigItem](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings#ConfigItem))
        }
      ],
      "uriOverride": string
    }  
  
Fields  
---  
`accountConnector` |  `string` Optional. Link to the Dev Connect Account Connector that holds the user credentials. projects/{project}/locations/{location}/accountConnectors/{account_connector_id}  
`handle` |  `string` Required. Handle used to invoke the tool.  
`tool` |  `string` Required. Link to the Tool  
`config[]` |  `object (`[ConfigItem](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings#ConfigItem)`)` Optional. Configuration parameters for the tool.  
`uriOverride` |  `string` Optional. Overridden URI, if allowed by Tool.  
  
## ConfigItem

Message for a single configuration item.

JSON representation  
---  
      
    
    {
      "key": string,
      "value": string
    }  
  
Fields  
---  
`key` |  `string` Required. Key of the configuration item.  
`value` |  `string` Required. Value of the configuration item.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings/create)`

|  Creates a new CodeToolsSetting in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings/delete)`

|  Deletes a single CodeToolsSetting.  
  
### `[get](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings/get)`

|  Gets details of a single CodeToolsSetting.  
  
### `[list](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings/list)`

|  Lists CodeToolsSettings in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/gemini/docs/api/reference/rest/v1/projects.locations.codeToolsSettings/patch)`

|  Updates the parameters of a single CodeToolsSetting.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-09-12 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-09-12 UTC."],[],[]] 
