---
url: https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting/
title: FloorSetting \u00a0|\u00a0 Model Armor \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:46:30.450904+00:00
---

# FloorSetting  |  Model Armor  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Model Armor ](https://docs.cloud.google.com/model-armor)
  * [ Reference ](https://docs.cloud.google.com/model-armor/reference/libraries)



Send feedback 

#  FloorSetting Stay organized with collections  Save and categorize content based on your preferences. 

  * JSON representation
  * IntegratedService
  * AiPlatformFloorSetting
    * JSON representation
  * FloorSettingMetadata
    * JSON representation
  * MultiLanguageDetection
    * JSON representation
  * McpServerFloorSetting
    * JSON representation



Message describing FloorSetting resource

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "filterConfig": {
        object ([FilterConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterConfig))
      },
      "integratedServices": [
        enum ([IntegratedService](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#IntegratedService))
      ],
      "floorSettingMetadata": {
        object ([FloorSettingMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#FloorSettingMetadata))
      },
      "enableFloorSettingEnforcement": boolean,
      "aiPlatformFloorSetting": {
        object ([AiPlatformFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#AiPlatformFloorSetting))
      },
      "googleMcpServerFloorSetting": {
        object ([McpServerFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#McpServerFloorSetting))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Create timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. [Output only] Update timestampUses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`filterConfig` |  `object (`[FilterConfig](https://docs.cloud.google.com/model-armor/reference/rest/v1/projects.locations.templates#FilterConfig)`)` Required. ModelArmor filter configuration.  
`integratedServices[]` |  `enum (`[IntegratedService](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#IntegratedService)`)` Optional. List of integrated services for which the floor setting is applicable.  
`floorSettingMetadata` |  `object (`[FloorSettingMetadata](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#FloorSettingMetadata)`)` Optional. Metadata for FloorSetting  
`enableFloorSettingEnforcement` |  `boolean` Optional. Floor Settings enforcement status.  
`aiPlatformFloorSetting` |  `object (`[AiPlatformFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#AiPlatformFloorSetting)`)` Optional. AI Platform floor setting.  
`googleMcpServerFloorSetting` |  `object (`[McpServerFloorSetting](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#McpServerFloorSetting)`)` Optional. Google MCP Server floor setting.  
  
## IntegratedService

Integrated service for which the floor setting is applicable.

Enums  
---  
`INTEGRATED_SERVICE_UNSPECIFIED` | Unspecified integrated service.  
`AI_PLATFORM` | AI Platform.  
`GOOGLE_MCP_SERVER` | Google MCP Server (via Shim Service Extension)  
  
## AiPlatformFloorSetting

message describing AiPlatformFloorSetting

JSON representation  
---  
      
    
    {
      "enableCloudLogging": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inspectOnly": boolean,
      "inspectAndBlock": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`enableCloudLogging` |  `boolean` Optional. If true, log Model Armor filter results to Cloud Logging.  
enforcement type for Model Armor filters. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inspectOnly` |  `boolean` Optional. If true, Model Armor filters will be run in inspect only mode. No action will be taken on the request.  
`inspectAndBlock` |  `boolean` Optional. If true, Model Armor filters will be run in inspect and block mode. Requests that trip Model Armor filters will be blocked.  
End of mutually exclusive fields.  
  
## FloorSettingMetadata

message describing FloorSetting Metadata

JSON representation  
---  
      
    
    {
      "multiLanguageDetection": {
        object ([MultiLanguageDetection](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#MultiLanguageDetection))
      }
    }  
  
Fields  
---  
`multiLanguageDetection` |  `object (`[MultiLanguageDetection](https://docs.cloud.google.com/model-armor/reference/rest/v1/FloorSetting#MultiLanguageDetection)`)` Optional. Metadata for multi language detection.  
  
## MultiLanguageDetection

Metadata to enable multi language detection via floor setting.

JSON representation  
---  
      
    
    {
      "enableMultiLanguageDetection": boolean
    }  
  
Fields  
---  
`enableMultiLanguageDetection` |  `boolean` Required. If true, multi language detection will be enabled.  
  
## McpServerFloorSetting

Message describing MCP Server Floor Setting.

JSON representation  
---  
      
    
    {
      "enableCloudLogging": boolean,
    
      // The following is a list of mutually exclusive fields. At most one of the
      // fields will be set in a response:
      "inspectOnly": boolean,
      "inspectAndBlock": boolean
      // End of mutually exclusive fields.
    }  
  
Fields  
---  
`enableCloudLogging` |  `boolean` Optional. If true, log Model Armor filter results to Cloud Logging.  
enforcement type for Model Armor filters. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:  
`inspectOnly` |  `boolean` Optional. If true, Model Armor filters will be run in inspect only mode. No action will be taken on the request.  
`inspectAndBlock` |  `boolean` Optional. If true, Model Armor filters will be run in inspect and block mode. Requests that trip Model Armor filters will be blocked.  
End of mutually exclusive fields.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-07 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-07 UTC."],[],[]] 
