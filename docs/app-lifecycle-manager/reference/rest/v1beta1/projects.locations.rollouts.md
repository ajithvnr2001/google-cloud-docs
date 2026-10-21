---
url: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts
title: REST Resource: projects.locations.rollouts \u00a0|\u00a0 App Lifecycle Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T10:43:05.964878+00:00
---

# REST Resource: projects.locations.rollouts  |  App Lifecycle Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts

We are looking for your feedback on our feature flags capabilities and user experience. Register your interest to provide feedback and influence our product design by [filling out this form](https://forms.gle/boGXCgKyoB7Lr6yd9). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application hosting ](https://docs.cloud.google.com/docs/application-hosting)
  * [ App Lifecycle Manager ](https://docs.cloud.google.com/app-lifecycle-manager)
  * [ Reference ](https://docs.cloud.google.com/app-lifecycle-manager/apis)



Send feedback 

#  REST Resource: projects.locations.rollouts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Rollout
    * JSON representation
  * RolloutState
  * RolloutStats
    * JSON representation
  * Aggregate
    * JSON representation
  * RolloutControl
    * JSON representation
  * RunRolloutActionParams
    * JSON representation
  * RolloutAction
  * Methods



## Resource: Rollout

Represents a single rollout execution and its results

JSON representation  
---  
      
    
    {
      "name": string,
      "release": string,
      "flagRelease": string,
      "startTime": string,
      "endTime": string,
      "state": enum ([RolloutState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutState)),
      "stateMessage": string,
      "stateTransitionTime": string,
      "rootRollout": string,
      "parentRollout": string,
      "rolloutOrchestrationStrategy": string,
      "unitFilter": string,
      "rolloutKind": string,
      "stats": {
        object ([RolloutStats](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutStats))
      },
      "control": {
        object ([RolloutControl](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutControl))
      },
      "effectiveUnitFilter": string,
      "labels": {
        string: string,
        ...
      },
      "annotations": {
        string: string,
        ...
      },
      "uid": string,
      "etag": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/rollout/{rolloutId}"  
`release` |  `string` Optional. Immutable. Name of the Release that gets rolled out to target Units. Required if no other type of release is specified.  
`flagRelease` |  `string` Optional. Immutable. Name of the FlagRelease to be rolled out to the target Units. Release and FlagRelease are mutually exclusive.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time when the rollout started executing. Will be empty if the rollout hasn't started yet.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time when the rollout finished execution (regardless of success, failure, or cancellation). Will be empty if the rollout hasn't finished yet. Once set, the rollout is in terminal state and all the results are final.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[RolloutState](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutState)`)` Output only. Current state of the rollout.  
`stateMessage` |  `string` Output only. Human readable message indicating details about the last state transition.  
`stateTransitionTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Optional. Output only. The time when the rollout transitioned into its current state.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`rootRollout` |  `string` Optional. Output only. The root rollout that this rollout is stemming from. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/rollouts/{rolloutId}"  
`parentRollout` |  `string` Optional. Output only. The direct parent rollout that this rollout is stemming from. The resource name (full URI of the resource) following the standard naming scheme:"projects/{project}/locations/{location}/rollouts/{rolloutId}"  
`rolloutOrchestrationStrategy` |  `string` Optional. The strategy used for executing this Rollout. This strategy will override whatever strategy is specified in the RolloutKind. If not specified on creation, the strategy from RolloutKind will be used.There are two supported values strategies which are used to control - "Google.Cloud.Simple.AllAtOnce" - "Google.Cloud.Simple.OneLocationAtATime"A rollout with one of these simple strategies will rollout across all locations defined in the targeted UnitKind's Saas Locations.  
`unitFilter` |  `string` Optional. CEL(<https://github.com/google/cel-spec>) formatted filter string against Unit. The filter will be applied to determine the eligible unit population. This filter can only reduce, but not expand the scope of the rollout. If not provided, the unitFilter from the RolloutKind will be used.  
`rolloutKind` |  `string` Required. Immutable. Name of the RolloutKind this rollout is stemming from and adhering to.  
`stats` |  `object (`[RolloutStats](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutStats)`)` Optional. Output only. Details about the progress of the rollout.  
`control` |  `object (`[RolloutControl](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutControl)`)` Optional. Requested change to the execution of this rollout. Default RolloutControl.action is ROLLOUT_ACTION_RUN meaning the rollout will be executed to completion while progressing through all natural Rollout States (such as RUNNING -> SUCCEEDED or RUNNING -> FAILED). Requests can only be made when the Rollout is in a non-terminal state.  
`effectiveUnitFilter` |  `string` Optional. Output only. Output only snapshot of the effective unit filter at Rollout start time. Contains a CEL(<https://github.com/google/cel-spec>) expression consisting of a conjunction of Rollout.unit_filter and RolloutKind.unit_filter. This field captures the filter applied by the Rollout to determine the Unit population. If the associated RolloutKind's unitFilter is modified after the rollout is started, it will not be updated here.  
`labels` |  `map (key: string, value: string)` Optional. The labels on the resource, which can be used for categorization. similar to Kubernetes resource labels.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`annotations` |  `map (key: string, value: string)` Optional. Annotations is an unstructured key-value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects.More info: <https://kubernetes.io/docs/user-guide/annotations>An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`uid` |  `string` Output only. The unique identifier of the resource. UID is unique in the time and space for this resource within the scope of the service. It is typically generated by the server on successful creation of a resource and must not be changed. UID is used to uniquely identify resources with resource name reuses. This should be a UUID4.  
`etag` |  `string` Output only. An opaque value that uniquely identifies a version or generation of a resource. It can be used to confirm that the client and server agree on the ordering of a resource being written.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was last updated. Any change to the resource made by users must refresh this value. Changes to a resource made by the service should refresh this value.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the resource was marked for deletion (deletion is an asynchronous operation).Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
  
## RolloutState

The current state of the rollout.

Enums  
---  
`ROLLOUT_STATE_UNSPECIFIED` | Unspecified state.  
`ROLLOUT_STATE_RUNNING` | Rollout is in progress.  
`ROLLOUT_STATE_PAUSED` | Rollout has been paused.  
`ROLLOUT_STATE_SUCCEEDED` | Rollout completed successfully.  
`ROLLOUT_STATE_FAILED` | Rollout has failed.  
`ROLLOUT_STATE_CANCELLED` | Rollout has been canceled.  
`ROLLOUT_STATE_WAITING` | Rollout is waiting for some condition to be met before starting.  
`ROLLOUT_STATE_CANCELLING` | Rollout is being canceled.  
`ROLLOUT_STATE_RESUMING` | Rollout is being resumed.  
`ROLLOUT_STATE_PAUSING` | Rollout is being paused.  
  
## RolloutStats

RolloutStats contains information about the progress of a rollout.

JSON representation  
---  
      
    
    {
      "operationsByState": [
        {
          object ([Aggregate](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#Aggregate))
        }
      ],
      "estimatedTotalUnitCount": string
    }  
  
Fields  
---  
`operationsByState[]` |  `object (`[Aggregate](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#Aggregate)`)` Optional. Output only. Unordered list. A breakdown of the progress of operations triggered by the rollout. Provides a count of Operations by their state. This can be used to determine the number of units which have been updated, or are scheduled to be updated.There will be at most one entry per group. Possible values for operation groups are: - "SCHEDULED" - "PENDING" - "RUNNING" - "SUCCEEDED" - "FAILED" - "CANCELLED"  
`estimatedTotalUnitCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Optional. Output only. Estimated number of units based. The estimation is computed upon creation of the rollout.  
  
## Aggregate

Represents the aggregation of a set of population of like records by a certain group. For example, a collection of unit counts can be aggregated and grouped by their state.

JSON representation  
---  
      
    
    {
      "group": string,
      "count": integer
    }  
  
Fields  
---  
`group` |  `string` Required. Group by which to aggregate.  
`count` |  `integer` Required. Number of records in the group.  
  
## RolloutControl

RolloutControl provides a way to request a change to the execution of a Rollout by pausing or canceling it.

JSON representation  
---  
      
    
    {
      "action": enum ([RolloutAction](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutAction)),
    
      // Union field action_params can be only one of the following:
      "runParams": {
        object ([RunRolloutActionParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RunRolloutActionParams))
      }
      // End of list of possible types for union field action_params.
    }  
  
Fields  
---  
`action` |  `enum (`[RolloutAction](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RolloutAction)`)` Required. Action to be performed on the Rollout. The default behavior is to run the rollout until it naturally reaches a terminal state.  
Union field `action_params`. Setting for the action. The setting must match the action e.g.: action=RUN may only set run_params or omit all parameters. It is an error to set a setting that is not applicable to the action. `action_params` can be only one of the following:  
`runParams` |  `object (`[RunRolloutActionParams](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts#RunRolloutActionParams)`)` Optional. Parameters for the RUN action. It is an error to specify this if the RolloutAction is not set to RUN. By default, the rollout will retry failed operations when resumed.  
  
## RunRolloutActionParams

Parameters for the RUN action controlling the behavior of the rollout when it is resumed from a PAUSED state.

JSON representation  
---  
      
    
    {
      "retryFailedOperations": boolean
    }  
  
Fields  
---  
`retryFailedOperations` |  `boolean` Required. If true, the rollout will retry failed operations when resumed. This is applicable only the current state of the Rollout is PAUSED and the requested action is RUN.  
  
## RolloutAction

RolloutAction indicates the action to be performed on the Rollout.

Enums  
---  
`ROLLOUT_ACTION_UNSPECIFIED` | Unspecified action, will be treated as RUN by default.  
`ROLLOUT_ACTION_RUN` | Run the Rollout until it naturally reaches a terminal state. A rollout requested to run will progress through all natural Rollout States (such as RUNNING -> SUCCEEDED or RUNNING -> FAILED). If retriable errors are encountered during the rollout, the rollout will paused by default and can be resumed by re-requesting this RUN action.  
`ROLLOUT_ACTION_PAUSE` | Pause the Rollout until it is resumed (i.e. RUN is requested).  
`ROLLOUT_ACTION_CANCEL` | Cancel the Rollout permanently.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/create)`

|  Create a new rollout.  
  
### `[delete](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/delete)`

|  Delete a single rollout.  
  
### `[get](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/get)`

|  Retrieve a single rollout.  
  
### `[list](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/list)`

|  Retrieve a collection of rollouts.  
  
### `[patch](https://docs.cloud.google.com/app-lifecycle-manager/reference/rest/v1beta1/projects.locations.rollouts/patch)`

|  Update a single rollout.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-17 UTC."],[],[]] 
