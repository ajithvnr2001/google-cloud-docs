---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences
title: REST Resource: projects.locations.rolloutSequences \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:09.102280+00:00
---

# REST Resource: projects.locations.rolloutSequences  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.rolloutSequences Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: RolloutSequence
    * JSON representation
  * RolloutSequence.Stage
    * JSON representation
  * ClusterSelector
    * JSON representation
  * Methods



## Resource: RolloutSequence

RolloutSequence defines the desired order of upgrades.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "uid": string,
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "labels": {
        string: string,
        ...
      },
      "stages": [
        {
          object ([RolloutSequence.Stage](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences#RolloutSequence.Stage))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the rollout sequence in the format of: projects/{PROJECT_ID}/locations/global/rolloutSequences/{NAME}  
`displayName` |  `string` Optional. Human readable display name of the Rollout Sequence.  
`uid` |  `string` Output only. Google-generated UUID for this resource. This is unique across all Rollout Sequence resources. If a Rollout Sequence resource is deleted and another resource with the same name is created, it gets a different uid.  
`etag` |  `string` Output only. etag of the Rollout Sequence Ex. abc1234  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the Rollout Sequence was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the Rollout Sequence was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at the Rollout Sequence was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels for this Rollout Sequence.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`stages[]` |  `object (`[RolloutSequence.Stage](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences#RolloutSequence.Stage)`)` Required. Ordered list of stages that constitutes this Rollout.  
  
## RolloutSequence.Stage

Rollout stage.

JSON representation  
---  
      
    
    {
      "fleetProjects": [
        string
      ],
      "clusterSelector": {
        object ([ClusterSelector](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences#ClusterSelector))
      },
      "soakDuration": string
    }  
  
Fields  
---  
`fleetProjects[]` |  `string` Required. List of Fleet projects to select the clusters from. Expected format: projects/{project}  
`clusterSelector` |  `object (`[ClusterSelector](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences#ClusterSelector)`)` Optional. Filter members of fleets (above) to a subset of clusters. If not specified, all clusters in the fleets are selected.  
`soakDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Soak time after upgrading all the clusters in the stage.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
  
## ClusterSelector

Selector for clusters.

JSON representation  
---  
      
    
    {
    
      // Union field selector can be only one of the following:
      "labelSelector": string
      // End of list of possible types for union field selector.
    }  
  
Fields  
---  
Union field `selector`. Options to select clusters. `selector` can be only one of the following:  
`labelSelector` |  `string` Required. A valid CEL (Common Expression Language) expression which evaluates `resource.labels`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/create)`

|  Create a new rollout sequence resource.  
  
### `[delete](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/delete)`

|  Remove a RolloutSequence.  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/get)`

|  Retrieve a single rollout sequence.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/list)`

|  Retrieve the list of all rollout sequences.  
  
### `[patch](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rolloutSequences/patch)`

|  Update a rollout sequence.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-28 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-28 UTC."],[],[]] 
