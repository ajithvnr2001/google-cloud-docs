---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates
title: REST Resource: projects.locations.spaces.sharedTemplates \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:18.557193+00:00
---

# REST Resource: projects.locations.spaces.sharedTemplates  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.sharedTemplates Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: SharedTemplate
    * JSON representation
  * Methods



## Resource: SharedTemplate

A read-only template that is shared with a space.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "originTemplate": string,
      "createTime": string,
      "updateTime": string,
      "latestRevisionId": string,
      "templateCategory": enum ([TemplateCategory](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateCategory)),
      "type": enum ([TemplateType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateType))
    }  
  
Fields  
---  
`name` |  `string` Identifier. The shared template name. `projects/$project/locations/$location/spaces/$space/sharedTemplates/$sharedTemplate`  
`displayName` |  `string` Optional. The shared template display name.  
`description` |  `string` Optional. The shared template description.  
`originTemplate` |  `string` Output only. The origin template of the shared template.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The shared template creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The shared template update timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`latestRevisionId` |  `string` Output only. Latest revision of the shared template.  
`templateCategory` |  `enum (`[TemplateCategory](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateCategory)`)` Required. The category of the template.  
`type` |  `enum (`[TemplateType](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/TemplateType)`)` Optional. The Application Design Center assembly template type.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates/get)`

|  Gets details about a shared template.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1/projects.locations.spaces.sharedTemplates/list)`

|  Lists shared templates in a given space.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
