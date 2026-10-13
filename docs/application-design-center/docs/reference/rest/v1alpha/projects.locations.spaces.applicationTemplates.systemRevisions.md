---
url: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.systemRevisions
title: REST Resource: projects.locations.spaces.applicationTemplates.systemRevisions \u00a0|\u00a0 Application Design Center \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:30:29.251769+00:00
---

# REST Resource: projects.locations.spaces.applicationTemplates.systemRevisions  |  Application Design Center  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.systemRevisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Application Design Center ](https://docs.cloud.google.com/application-design-center/docs)
  * [ Reference ](https://docs.cloud.google.com/application-design-center/docs/apis)



Send feedback 

#  REST Resource: projects.locations.spaces.applicationTemplates.systemRevisions Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ApplicationTemplateSystemRevision
    * JSON representation
  * Methods



## Resource: ApplicationTemplateSystemRevision

Application template system revision resource.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "annotations": {
        string: string,
        ...
      },
      "snapshot": {
        object (SerializedApplicationTemplate)
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. The application template system revision name. Format: projects/{project}/locations/{location}/spaces/{space}/applicationTemplates/{applicationTemplate}/systemRevisions/{system_revision}  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The application template system revision creation timestamp.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`annotations` |  `map (key: string, value: string)` Output only. Annotations from agentic workflows or other system processes. For example: { "designcenter.googleapis.com/agent_id": "gemini-3-flash-v1", "designcenter.googleapis.com/llm_agent_summary": "Added a Cloud SQL instance", "designcenter.googleapis.com/external_ref_id": "trace-uuid-88921-xyz" }An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`snapshot` |  `object (`SerializedApplicationTemplate`)` Output only. The serialized application template snapshot at this revision.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.systemRevisions/get)`

|  Gets the given application template system revision.  
  
### `[list](https://docs.cloud.google.com/application-design-center/docs/reference/rest/v1alpha/projects.locations.spaces.applicationTemplates.systemRevisions/list)`

|  Lists application template system revisions in a given application template.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-13 UTC."],[],[]] 
