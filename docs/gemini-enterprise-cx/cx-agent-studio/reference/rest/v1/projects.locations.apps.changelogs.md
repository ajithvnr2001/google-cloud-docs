---
url: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.changelogs
title: REST Resource: projects.locations.apps.changelogs \u00a0|\u00a0 CX Agent Studio \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T12:52:46.245445+00:00
---

# REST Resource: projects.locations.apps.changelogs  |  CX Agent Studio  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.changelogs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise for Customer Experience ](https://docs.cloud.google.com/gemini-enterprise-cx)
  * [ CX Agent Studio ](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio)



Send feedback 

#  REST Resource: projects.locations.apps.changelogs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Changelog
    * JSON representation
  * Methods



## Resource: Changelog

Changelogs represent a change made to the app or to an resource within the app.

JSON representation  
---  
      
    
    {
      "name": string,
      "author": string,
      "displayName": string,
      "description": string,
      "resource": string,
      "resourceType": string,
      "action": string,
      "originalResource": {
        object
      },
      "newResource": {
        object
      },
      "dependentResources": [
        {
          object
        }
      ],
      "createTime": string,
      "sequenceNumber": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the changelog. Format: `projects/{project}/locations/{location}/apps/{app}/changelogs/{changelog}`  
`author` |  `string` Output only. Email address of the change author.  
`displayName` |  `string` Output only. Display name of the change. It typically should be the display name of the resource that was changed.  
`description` |  `string` Output only. Description of the change. which typically captures the changed fields in the resource.  
`resource` |  `string` Output only. The resource that was changed.  
`resourceType` |  `string` Output only. The type of the resource that was changed.  
`action` |  `string` Output only. The action that was performed on the resource.  
`originalResource` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The original resource before the change.  
`newResource` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The new resource after the change.  
`dependentResources[]` |  `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Output only. The dependent resources that were changed.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the change was made.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`sequenceNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The monotonically increasing sequence number of the changelog.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.changelogs/get)`

|  Gets the specified changelog.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-cx/cx-agent-studio/reference/rest/v1/projects.locations.apps.changelogs/list)`

|  Lists the changelogs of the specified app.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-01 UTC."],[],[]] 
