---
url: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts
title: REST Resource: projects.locations.rollouts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:06:09.958909+00:00
---

# REST Resource: projects.locations.rollouts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts

  * [ Reference ](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest)



#  REST Resource: projects.locations.rollouts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Rollout
    * JSON representation
  * Rollout.VersionUpgrade
    * JSON representation
  * Rollout.VersionUpgrade.Type
  * Rollout.State
  * Rollout.Stage
    * JSON representation
  * Rollout.Stage.State
  * Rollout.RolloutMembershipState
    * JSON representation
  * Rollout.RolloutMembershipState.RolloutTarget
    * JSON representation
  * Rollout.RolloutMembershipState.RolloutTarget.State
  * Methods



## Resource: Rollout

Rollout contains the Rollout metadata and configuration.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "uid": string,
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "completeTime": string,
      "deleteTime": string,
      "labels": {
        string: string,
        ...
      },
      "state": enum ([Rollout.State](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.State)),
      "stateReason": string,
      "rolloutSequence": string,
      "stages": [
        {
          object ([Rollout.Stage](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.Stage))
        }
      ],
      "membershipStates": {
        string: {
          object ([Rollout.RolloutMembershipState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.RolloutMembershipState))
        },
        ...
      },
    
      // Union field rollout_type can be only one of the following:
      "versionUpgrade": {
        object ([Rollout.VersionUpgrade](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.VersionUpgrade))
      }
      // End of list of possible types for union field rollout_type.
    }  
  
Fields  
---  
`name` |  `string` Identifier. The full, unique resource name of this Rollout in the format of `projects/{project}/locations/global/rollouts/{rollout}`.  
`displayName` |  `string` Optional. Human readable display name of the Rollout.  
`uid` |  `string` Output only. Google-generated UUID for this resource. This is unique across all Rollout resources. If a Rollout resource is deleted and another resource with the same name is created, it gets a different uid.  
`etag` |  `string` Output only. etag of the Rollout Ex. abc1234  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the Rollout was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the Rollout was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`completeTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at which the Rollout was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp at the Rollout was deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` Optional. Labels for this Rollout.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`state` |  `enum (`[Rollout.State](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.State)`)` Output only. State specifies various states of the Rollout.  
`stateReason` |  `string` Output only. A human-readable description explaining the reason for the current state.  
`rolloutSequence` |  `string` Optional. Immutable. The full, unique resource name of the rollout sequence that initiatied this Rollout. In the format of `projects/{project}/locations/global/rolloutSequences/{rolloutSequence}`.  
`stages[]` |  `object (`[Rollout.Stage](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.Stage)`)` Output only. The stages of the Rollout.  
`membershipStates` |  `map (key: string, value: object (`[Rollout.RolloutMembershipState](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.RolloutMembershipState)`))` Output only. States of upgrading control plane or node pool targets of a single cluster (GKE Hub membership) that's part of this Rollout. The key is the membership name of the cluster. The value is the state of the cluster.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
Union field `rollout_type`. Rollout type. `rollout_type` can be only one of the following:  
`versionUpgrade` |  `object (`[Rollout.VersionUpgrade](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.VersionUpgrade)`)` Optional. Config for version upgrade of clusters.  
  
## Rollout.VersionUpgrade

Config for version upgrade of clusters.

JSON representation  
---  
      
    
    {
      "type": enum ([Rollout.VersionUpgrade.Type](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.VersionUpgrade.Type)),
      "desiredVersion": string
    }  
  
Fields  
---  
`type` |  `enum (`[Rollout.VersionUpgrade.Type](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.VersionUpgrade.Type)`)` Optional. Type of version upgrade specifies which component should be upgraded.  
`desiredVersion` |  `string` Optional. Desired version of the component.  
  
## Rollout.VersionUpgrade.Type

Type of the upgrade.

Enums  
---  
`TYPE_UNSPECIFIED` | Default value.  
`TYPE_CONTROL_PLANE` | Control plane upgrade.  
`TYPE_NODE_POOL` | Node pool upgrade.  
  
## Rollout.State

State of the Rollout.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`RUNNING` | The Rollout is running.  
`PAUSED` | The Rollout is paused.  
`CANCELLED` | The Rollout is in a failure terminal state.  
`COMPLETED` | The Rollout is in a terminal state.  
  
## Rollout.Stage

Stage represents a single stage in the Rollout.

JSON representation  
---  
      
    
    {
      "stageNumber": integer,
      "state": enum ([Rollout.Stage.State](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.Stage.State)),
      "soakDuration": string,
      "startTime": string,
      "endTime": string
    }  
  
Fields  
---  
`stageNumber` |  `integer` Output only. The wave number to which this status applies.  
`state` |  `enum (`[Rollout.Stage.State](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.Stage.State)`)` Output only. The state of the wave.  
`soakDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Optional. Duration to soak after this wave before starting the next wave.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time at which the wave started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time at which the wave ended.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Rollout.Stage.State

Enums  
---  
`STATE_UNSPECIFIED` | Default value.  
`PENDING` | The wave is pending.  
`RUNNING` | The wave is running.  
`SOAKING` | The wave is soaking.  
`COMPLETED` | The wave is completed.  
`FORCED_SOAKING` | The wave is force soaking.  
  
## Rollout.RolloutMembershipState

Metadata about single cluster (GKE Hub membership) that's part of this Rollout.

JSON representation  
---  
      
    
    {
      "stageAssignment": integer,
      "targets": [
        {
          object ([Rollout.RolloutMembershipState.RolloutTarget](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.RolloutMembershipState.RolloutTarget))
        }
      ],
      "lastUpdateTime": string
    }  
  
Fields  
---  
`stageAssignment` |  `integer` Output only. The stage assignment of this cluster in this rollout.  
`targets[]` |  `object (`[Rollout.RolloutMembershipState.RolloutTarget](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.RolloutMembershipState.RolloutTarget)`)` Output only. The targets of the rollout - clusters or node pools that are being upgraded. All targets belongs to the same cluster, identified by the membership name (key of membershipStates map).  
`lastUpdateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time this status and any related Rollout-specific details for the membership were updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## Rollout.RolloutMembershipState.RolloutTarget

Metadata about the status of targets (clusters or node pools) involved in the Rollout.

JSON representation  
---  
      
    
    {
      "state": enum ([Rollout.RolloutMembershipState.RolloutTarget.State](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.RolloutMembershipState.RolloutTarget.State)),
      "reason": string,
      "operation": string,
    
      // Union field target can be only one of the following:
      "cluster": string,
      "nodePool": string
      // End of list of possible types for union field target.
    }  
  
Fields  
---  
`state` |  `enum (`[Rollout.RolloutMembershipState.RolloutTarget.State](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts#Rollout.RolloutMembershipState.RolloutTarget.State)`)` Output only. The high-level, machine-readable status of this Rollout for the target.  
`reason` |  `string` Optional. Output only. A human-readable description of the current status.  
`operation` |  `string` Optional. Output only. The operation resource name performing the mutation.  
Union field `target`. The target of the rollout - cluster or node pool that is being upgraded. `target` can be only one of the following:  
`cluster` |  `string` Optional. Output only. The resource link of the Cluster resource upgraded in this Rollout. It is formatted as: `//{api_service}/projects/{project_number}/locations/{location}/clusters/{clusterName}`..  
`nodePool` |  `string` Optional. Output only. The resource link of the NodePool resource upgraded in this Rollout. It is formatted as: `//{api_service}/projects/{project_number}/locations/{location}/clusters/{clusterName}/nodePools/{node_pool_name}`.  
  
## Rollout.RolloutMembershipState.RolloutTarget.State

Status represents a machine-readable, high-level status of the target after actuating the Rollout on it.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`PENDING` | The Rollout is pending for the target.  
`RUNNING` | The Rollout is running for the target.  
`FAILED` | The Rollout failed for the target.  
`SUCCEEDED` | The Rollout succeeded for the target.  
`PAUSED` | The Rollout is paused for the target.  
`REMOVED` | The target was removed from the Rollout.  
`INELIGIBLE` | The target is ineligible for the Rollout.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts/get)`

|  Retrieve a single rollout.  
  
### `[list](https://docs.cloud.google.com/kubernetes-engine/fleet-management/docs/reference/rest/v1alpha/projects.locations.rollouts/list)`

|  Retrieve the list of all rollouts.  
  
Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-30 UTC.

[[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 
