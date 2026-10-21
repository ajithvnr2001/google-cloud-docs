---
url: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills
title: REST Resource: projects.locations.skills \u00a0|\u00a0 Agent Registry \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T22:06:43.940990+00:00
---

# REST Resource: projects.locations.skills  |  Agent Registry  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Agent Registry ](https://docs.cloud.google.com/agent-registry)
  * [ Reference ](https://docs.cloud.google.com/agent-registry/apis)



Send feedback 

#  REST Resource: projects.locations.skills Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Skill
    * JSON representation
  * Type
  * State
  * TargetState
  * Methods



## Resource: Skill

Represents an Executable Agent Skill or a Composite Tool Suite (Bundle). Sibling resource with Agent and McpServer under agentregistry.googleapis.com.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "displayName": string,
      "description": string,
      "type": enum ([Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#Type)),
      "state": enum ([State](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#State)),
      "targetState": enum ([TargetState](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#TargetState)),
      "defaultRevision": string,
      "frontmatter": {
        object ([Frontmatter](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Frontmatter))
      },
      "skillId": string,
      "createTime": string,
      "updateTime": string,
      "publisher": string,
      "initialRevision": {
        object ([SkillRevision](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision))
      }
    }  
  
Fields  
---  
`name` |  `string` Identifier. Resource name of the Skill. Format: `projects/{project}/locations/{location}/skills/{skill}` The `{skill}` segment acts as the resource ID. If the skill is associated with a Publisher, this segment typically uses a hyphenated namespace prefix corresponding to the publisher (e.g., `google-workspace-create-docs`).  
`uid` |  `string` Output only. Universally unique identifier (UUID4) for the logical container.  
`displayName` |  `string` Required. Human-readable display name of the skill. Maximum length is 128 characters.  
`description` |  `string` Optional. Brief summary describing the capabilities of the skill. Maximum length is 2048 characters.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#Type)`)` Required. Structural deployment type (SIMPLE leaf vs COMPOSITE bundle).  
`state` |  `enum (`[State](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#State)`)` Output only. The system-managed state of the skill.  
`targetState` |  `enum (`[TargetState](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills#TargetState)`)` Required. User-managed target state of the skill.  
`defaultRevision` |  `string` Optional. The full resource name of the revision currently served by default (floating track). Format: `projects/{project}/locations/{location}/skills/{skill}/revisions/{revision}`  
`frontmatter` |  `object (`[Frontmatter](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/Frontmatter)`)` Output only. Lightweight frontmatter metadata attributes copied from the default revision.  
`skillId` |  `string` Output only. A stable, globally unique logical identifier for the skill. It is securely constructed by the backend by combining the associated `publisher`'s verified namespace and the skill's resource ID to enforce strict ownership. For example, the prefix `google-` is reserved exclusively for first-party Google publishers to prevent namespace squatting. Example: `urn:skill:google-workspace:create-docs`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Create time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Update time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`publisher` |  `string` Optional. The publisher resource associated with this skill. Format: `projects/{project}/locations/{location}/publishers/{publisher}` The publisher dictates the allowed namespace prefixes for the skill's name and logical `skillId` (e.g., Publisher `google` authorizes the `google-*` prefix).  
`initialRevision` |  `object (`[SkillRevision](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills.revisions#SkillRevision)`)` Optional. Input only. Optional nested initial revision payload to support standard one-shot creation. The server processes this field on input during creation but must never return it in responses.  
  
## Type

The structural type of the Skill.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value. This value is unused.  
`SIMPLE` | A standard, leaf executable skill containing natural language and code.  
  
## State

System-managed state.

Enums  
---  
`STATE_UNSPECIFIED` | Default value. This value is unused.  
`STATE_CREATING` | The skill is being created. It is not served.  
`STATE_DRAFT` | The skill is in draft, or lacks a valid payload. It is not served.  
`STATE_ACTIVE` | The skill is active and is served.  
`STATE_DISABLED` | The skill is disabled and is not served.  
`STATE_DEPRECATED` | The skill is deprecated. It is served, but emits warnings.  
`STATE_DECOMMISSIONED` | The skill is decommissioned and is not served.  
`STATE_DELETING` | The skill is being deleted. It is not served.  
  
## TargetState

User-configurable target state.

Enums  
---  
`TARGET_STATE_UNSPECIFIED` | Default value. This value is unused.  
`TARGET_STATE_DRAFT` | The skill is in draft and cannot be served.  
`TARGET_STATE_ACTIVE` | The skill is active and can be served.  
`TARGET_STATE_DISABLED` | The skill is disabled and cannot be served.  
`TARGET_STATE_DEPRECATED` | The skill is deprecated. It can still be served, but emits warnings.  
`TARGET_STATE_DECOMMISSIONED` | The skill is decommissioned and cannot be served.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/create)`

|  =========================================================================

# Skills Collection APIs

Creates a Skill resource container, optionally publishing the initial SkillRevision inline in a single, atomic CRUD roundtrip.  
  
### `[delete](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/delete)`

|  Deletes a Skill container along with all its revisions.  
  
### `[get](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/get)`

|  Fetches the active configuration and metadata of a Skill.  
  
### `[getIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/list)`

|  Lists logical Skills available in a project.  
  
### `[patch](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/patch)`

|  Updates Skill metadata or overrides active pointers/state using REST standard PATCH.  
  
### `[search](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/search)`

|  Custom deep-search method to filter by frontmatter or query SKILL.md text blobs.  
  
### `[setIamPolicy](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/agent-registry/reference/rest/v1alpha/projects.locations.skills/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-17 UTC."],[],[]] 
