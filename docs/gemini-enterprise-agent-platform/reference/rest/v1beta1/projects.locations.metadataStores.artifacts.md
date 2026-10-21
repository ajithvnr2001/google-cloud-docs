---
url: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts
title: REST Resource: projects.locations.metadataStores.artifacts \u00a0|\u00a0 Gemini Enterprise Agent Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T20:00:47.979694+00:00
---

# REST Resource: projects.locations.metadataStores.artifacts  |  Gemini Enterprise Agent Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise Agent Platform ](https://docs.cloud.google.com/gemini-enterprise-agent-platform)
  * [ API reference ](https://docs.cloud.google.com/gemini-enterprise-agent-platform/apis)



Send feedback 

#  REST Resource: projects.locations.metadataStores.artifacts Stay organized with collections  Save and categorize content based on your preferences. 

## Resource: Artifact

Instance of a general artifact.

Fields  
  
`name` `string` Output only. The resource name of the Artifact. | `displayName` `string` user provided display name of the Artifact. May be up to 128 Unicode characters. | `uri` `string` The uniform resource identifier of the artifact file. May be empty if there is no actual artifact file. | `etag` `string` An eTag used to perform consistent read-modify-write updates. If not set, a blind "overwrite" update happens. | `labels` `map (key: string, value: string)` The labels with user-defined metadata to organize your Artifacts.label keys and values can be no longer than 64 characters (Unicode codepoints), can only contain lowercase letters, numeric characters, underscores and dashes. International characters are allowed. No more than 64 user labels can be associated with one Artifact (System labels are excluded). | `createTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Artifact was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `updateTime` `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. timestamp when this Artifact was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`. | `state` `enum (`[State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts#Artifact.State)`)` The state of this Artifact. This is a property of the Artifact, and does not imply or capture any ongoing process. This property is managed by clients (such as Agent Platform Pipelines), and the system does not prescribe or check the validity of state transitions. | `schemaTitle` `string` The title of the schema describing the metadata.Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. | `schemaVersion` `string` The version of the schema in schemaName to use.Schema title and version is expected to be registered in earlier Create Schema calls. And both are used together as unique identifiers to identify schemas within the local metadata store. | `metadata` `object (`[Struct](https://protobuf.dev/reference/protobuf/google.protobuf/#struct)` format)` Properties of the Artifact. top level metadata keys' heading and trailing spaces will be trimmed. The size of this field should not exceed 200KB. | `description` `string` description of the Artifact | JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "uri": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts#Artifact.State)),
      "schemaTitle": string,
      "schemaVersion": string,
      "metadata": {
        object
      },
      "description": string
    }  
  
### State

Describes the state of the Artifact.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state for the Artifact.  
`PENDING` | A state used by systems like Agent Platform Pipelines to indicate that the underlying data item represented by this Artifact is being created.  
`LIVE` | A state indicating that the Artifact should exist, unless something external to the system deletes it.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts/create)`

|  Creates an Artifact associated with a MetadataStore.  
  
### `[delete](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts/delete)`

|  Deletes an Artifact.  
  
### `[get](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts/get)`

|  Retrieves a specific Artifact.  
  
### `[list](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts/list)`

|  Lists Artifacts in the MetadataStore.  
  
### `[patch](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts/patch)`

|  Updates a stored Artifact.  
  
### `[purge](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts/purge)`

|  Purges Artifacts.  
  
### `[queryArtifactLineageSubgraph](https://docs.cloud.google.com/gemini-enterprise-agent-platform/reference/rest/v1beta1/projects.locations.metadataStores.artifacts/queryArtifactLineageSubgraph)`

|  Retrieves lineage of an Artifact represented through Artifacts and Executions connected by Event edges and returned as a LineageSubgraph.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-22 UTC."],[],[]] 
