---
url: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions
title: REST Resource: projects.locations.agents.tools.versions \u00a0|\u00a0 Dialogflow CX \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:50:17.012305+00:00
---

# REST Resource: projects.locations.agents.tools.versions  |  Dialogflow CX  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions

Some products and features are in the process of being renamed. Generative playbook and flow features are also being migrated to a single [consolidated console](https://docs.cloud.google.com/dialogflow/cx/docs/concept/console-conversational-agents). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Dialogflow ](https://docs.cloud.google.com/dialogflow/docs)
  * [ Dialogflow CX ](https://docs.cloud.google.com/dialogflow/cx/docs)
  * [ Reference ](https://docs.cloud.google.com/dialogflow/cx/docs/reference)



Send feedback 

#  REST Resource: projects.locations.agents.tools.versions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ToolVersion
    * JSON representation
  * Methods



## Resource: ToolVersion

Tool version is a snapshot of the tool at certain timestamp.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "tool": {
        object ([Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool))
      },
      "createTime": string,
      "updateTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The unique identifier of the tool version. Format: `projects/<ProjectID>/locations/<LocationID>/agents/<AgentID>/tools/<ToolID>/versions/<VersionID>`.  
`displayName` |  `string` Required. The display name of the tool version.  
`tool` |  `object (`[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`)` Required. Snapshot of the tool to be associated with this version.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last time the tool version was created or modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Last time the tool version was created or modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/create)`

|  Creates a version for the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
### `[delete](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/delete)`

|  Deletes the specified version of the `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
### `[get](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/get)`

|  Retrieves the specified version of the `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
### `[list](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/list)`

|  List versions of the specified `[Tool](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools#Tool)`.  
  
### `[restore](https://docs.cloud.google.com/dialogflow/cx/docs/reference/rest/v3/projects.locations.agents.tools.versions/restore)`

|  Retrieves the specified version of the Tool and stores it as the current tool draft, returning the tool with resources updated.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-08-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-08-21 UTC."],[],[]] 
