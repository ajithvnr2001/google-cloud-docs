---
url: https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions
title: REST Resource: projects.locations.investigations.revisions \u00a0|\u00a0 Gemini Cloud Assist \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T11:07:30.474072+00:00
---

# REST Resource: projects.locations.investigations.revisions  |  Gemini Cloud Assist  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Cloud Assist ](https://docs.cloud.google.com/cloud-assist)
  * [ API and references ](https://docs.cloud.google.com/cloud-assist/api-and-reference)



Send feedback 

#  REST Resource: projects.locations.investigations.revisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: InvestigationRevision
    * JSON representation
  * Methods



## Resource: InvestigationRevision

A revision holds a snapshot of the investigation at a past point in time. The most recent revision holds the investigation's current state, while previous revisions are immutable.

JSON representation  
---  
      
    
    {
      "name": string,
      "snapshot": {
        object ([Investigation](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations#Investigation))
      },
      "createTime": string,
      "labels": {
        string: string,
        ...
      },
      "index": integer
    }  
  
Fields  
---  
`name` |  `string` Identifier. The name of the revision resource, of the form: projects/{projectNumber}/locations/{locationId}/investigations/{investigationId}/revisions/{revision_id}  
`snapshot` |  `object (`[Investigation](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations#Investigation)`)` Optional. Snapshot of the investigation contents at this revision.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time when the revision was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. User-defined labels for the revision.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`index` |  `integer` Output only. Revision index number, in order of creation.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/create)   
**(deprecated)**`

|  Deprecated: Investigations should only be modified by the agent.  
  
### `[delete](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/delete)`

|  Deletes a single revision of an Investigation.  
  
### `[get](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/get)`

|  Gets details of a single revision of an Investigation.  
  
### `[list](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/list)`

|  Lists Investigations in a given project.  
  
### `[run](https://docs.cloud.google.com/cloud-assist/reference/rest/v1alpha/projects.locations.investigations.revisions/run)   
**(deprecated)**`

|  Deprecated: Investigations should only be run by the agent.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-21 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-21 UTC."],[],[]] 
