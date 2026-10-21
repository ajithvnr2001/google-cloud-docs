---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots
title: REST Resource: projects.locations.reasoningEngines.sandboxEnvironmentSnapshots \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-15T10:10:17.196137+00:00
---

# REST Resource: projects.locations.reasoningEngines.sandboxEnvironmentSnapshots  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.reasoningEngines.sandboxEnvironmentSnapshots Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: SandboxEnvironmentSnapshot

SandboxEnvironmentSnapshot is a snapshot of the SandboxEnvironment.

Fields  
  
`name` `string` Identifier. The resource name of the SandboxEnvironmentSnapshot. Format: `projects/{project}/locations/{location}/reasoningEngines/{reasoningEngine}/sandboxEnvironmentSnapshots/{sandboxEnvironmentSnapshot}` | `displayName` `string` Required. The display name of the SandboxEnvironmentSnapshot. | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this SandboxEnvironmentSnapshot was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when this SandboxEnvironment was most recently updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `sourceSandboxEnvironment` `string` Required. The resource name of the source SandboxEnvironment this snapshot was taken from. | `parentSnapshot` `string` Output only. The resource name of the parent SandboxEnvironmentSnapshot. Empty if this is a root Snapshot (the first snapshot from a newly created sandbox). Can be used to reconstruct the whole ancestry tree of snapshots. | `sizeBytes` `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Output only. Size of the snapshot data in bytes. | `owner` `string` Optional. owner information for this sandbox snapshot. Different owners will have isolations on snapshot storage and identity. If not set, snapshot will be created as the default owner. | `postSnapshotAction` `enum (`[PostSnapshotAction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots#PostSnapshotAction)`)` Optional. Input only. Action to take on the source SandboxEnvironment after the snapshot is taken. This field is only used in CreateSandboxEnvironmentSnapshotRequest and it is not stored in the resource. | `expiration` `Union type`  
  
The expiration of the SandboxEnvironmentSnapshot. If not set, the SandboxEnvironmentSnapshot will have a default TTL of 30 days. `expire_time` is recommended for specifying a precise expiration time. The following is a list of mutually exclusive fields. At most one of the fields will be set in a response:

`expireTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. timestamp in UTC of when this SandboxEnvironmentSnapshot is considered expired. This is _always_ provided on output, regardless of what `expiration` was sent on input.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `ttl` `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Input only. The TTL for the sandbox environment snapshot. The expiration time is computed: now + TTL.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`. End of mutually exclusive fields. | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "sourceSandboxEnvironment": string,
      "parentSnapshot": string,
      "sizeBytes": string,
      "owner": string,
      "postSnapshotAction": enum ([PostSnapshotAction](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots#PostSnapshotAction)),
    
      // expiration
      "expireTime": string,
      "ttl": string
      // Union type
    }  
  
## PostSnapshotAction

Action to take on the source SandboxEnvironment after the snapshot is taken.

Enums  
---  
`POST_SNAPSHOT_ACTION_UNSPECIFIED` | The default value. This value is unused.  
`RUNNING` | Sandbox environment will continue to run after snapshot is taken.  
`PAUSE` | Sandbox environment will be paused after snapshot is taken.  
  
## Methods  
  
---  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots/delete)`

|  Deletes the specific `[SandboxEnvironmentSnapshot](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots#SandboxEnvironmentSnapshot)`.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots/get)`

|  Gets details of the specific `[SandboxEnvironmentSnapshot](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots#SandboxEnvironmentSnapshot)`.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots/list)`

|  Lists `[SandboxEnvironmentSnapshot](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1/projects.locations.reasoningEngines.sandboxEnvironmentSnapshots#SandboxEnvironmentSnapshot)`s in a given reasoning engine.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-01 UTC."],[],[]] 
