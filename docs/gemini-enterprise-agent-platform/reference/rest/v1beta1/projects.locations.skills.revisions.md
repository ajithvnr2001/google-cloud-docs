---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills.revisions
title: REST Resource: projects.locations.skills.revisions \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:40:42.954065+00:00
---

# REST Resource: projects.locations.skills.revisions  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills.revisions

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.skills.revisions Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: SkillRevision

A revision of a Skill.

Fields  
  
`name` `string` Identifier. The resource name of the Skill Revision. Format: `projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}` | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Skill Revision was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `skill` `object (`[Skill](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills#Skill)`)` Output only. The state of the Skill at this revision. | `state` `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills.revisions#State)`)` Output only. The state of the Skill Revision. | JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "skill": {
        object ([Skill](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills#Skill))
      },
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills.revisions#State))
    }  
  
## State

The state of the Skill Revision.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the Skill Revision is unspecified.  
`ACTIVE` | The Skill Revision is active.  
`CREATING` | The Skill Revision is being created.  
`FAILED` | The Skill Revision was created, but failed to process.  
`DELETING` | The Skill Revision is being deleted.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills.revisions/get)`

|  Get a Skill Revision.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills.revisions/list)`

|  List Skill Revisions for a Skill.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
