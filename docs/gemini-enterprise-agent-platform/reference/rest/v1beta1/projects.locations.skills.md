---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills
title: REST Resource: projects.locations.skills \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T18:07:15.418013+00:00
---

# REST Resource: projects.locations.skills  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.skills Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Skill

A skill.

Fields  
  
`name` `string` Identifier. The resource name of the Skill. Format: `projects/{project}/locations/{location}/skills/{skill}` | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Skill was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Skill was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `displayName` `string` Required. Provides the display name of the Skill. This should align with `name` in the `SKILL.md` file. | `description` `string` Required. Describes the Skill. Should describe both what the skill does and when to use it. Should include specific keywords that help agents identify relevant tasks. This should align with `description` in the `SKILL.md` file. | `license` `string` Optional. Specifies the license of the Skill. This should be an SPDX license identifier (e.g., "MIT", "Apache-2.0"). See <https://spdx.org/licenses/>. This should align with `license` in the `SKILL.md` file. | `compatibility` `string` Optional. Specifies the compatibility of the Skill. Indicates environment requirements (intended product, system packages, network access, etc.). This should align with `compatibility` in the `SKILL.md` file. | `zippedFilesystem` `string ([bytes](https://developers.google.com/discovery/v1/type-format) format)` Required. Provides the zipped filesystem of the Skill. This should contain the `SKILL.md` file at the root of the zip and optional directories for scripts, references, and assets. Directory should align with the directory structure specified at <https://agentskills.io/specification#directory-structure>.A base64-encoded string. | `state` `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills#Skill.State)`)` Output only. The state of the Skill. | `labels` `map (key: string, value: string)` The labels with user-defined metadata to organize Skills. | `sha256` `string` Output only. The SHA256 checksum of the zipped filesystem. | `skillSource` `enum (`[SkillSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills#Skill.SkillSource)`)` Output only. The source of the Skill. | JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "description": string,
      "license": string,
      "compatibility": string,
      "zippedFilesystem": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills#Skill.State)),
      "labels": {
        string: string,
        ...
      },
      "sha256": string,
      "skillSource": enum ([SkillSource](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills#Skill.SkillSource))
    }  
  
### State

The state of the Skill.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the Skill is unspecified.  
`ACTIVE` | The Skill is active.  
`CREATING` | The Skill is being created.  
`FAILED` | The Skill was created, but failed to process.  
`DELETING` | The Skill is being deleted.  
  
### SkillSource

The source of the Skill (system or user-created).

Enums  
---  
`SKILL_SOURCE_UNSPECIFIED` | The skill source is unspecified.  
`USER` | The skill is created by a user.  
`SYSTEM` | The skill is a system skill.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/create)`

|  Create a Skill.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/delete)`

|  Delete a Skill.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/get)`

|  Get a Skill.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/list)`

|  List Skills.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/patch)`

|  Update a Skill.  
  
### `[retrieve](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.skills/retrieve)`

|  Retrieves skills.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-05-19 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-05-19 UTC."],[],[]] 
