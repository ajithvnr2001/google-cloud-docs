---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns
title: REST Resource: projects.locations.deliveryPipelines.automationRuns \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:57.885218+00:00
---

# REST Resource: projects.locations.deliveryPipelines.automationRuns  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.deliveryPipelines.automationRuns Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: AutomationRun
    * JSON representation
  * State
  * PolicyViolation
    * JSON representation
  * PolicyViolationDetails
    * JSON representation
  * PromoteReleaseOperation
    * JSON representation
  * AdvanceRolloutOperation
    * JSON representation
  * RepairRolloutOperation
    * JSON representation
  * RepairPhase
    * JSON representation
  * RetryPhase
    * JSON representation
  * RetryAttempt
    * JSON representation
  * RepairState
  * RollbackAttempt
    * JSON representation
  * TimedPromoteReleaseOperation
    * JSON representation
  * Methods



## Resource: AutomationRun

An `AutomationRun` resource in the Cloud Deploy API.

An `AutomationRun` represents an execution instance of an automation rule.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "etag": string,
      "serviceAccount": string,
      "automationSnapshot": {
        object ([Automation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation))
      },
      "targetId": string,
      "state": enum ([State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#State)),
      "stateDescription": string,
      "policyViolation": {
        object ([PolicyViolation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#PolicyViolation))
      },
      "expireTime": string,
      "ruleId": string,
      "automationId": string,
      "waitUntilTime": string,
      "uid": string,
    
      // Union field operation can be only one of the following:
      "promoteReleaseOperation": {
        object ([PromoteReleaseOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#PromoteReleaseOperation))
      },
      "advanceRolloutOperation": {
        object ([AdvanceRolloutOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#AdvanceRolloutOperation))
      },
      "repairRolloutOperation": {
        object ([RepairRolloutOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairRolloutOperation))
      },
      "timedPromoteReleaseOperation": {
        object ([TimedPromoteReleaseOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#TimedPromoteReleaseOperation))
      }
      // End of list of possible types for union field operation.
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the `AutomationRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/automationRuns/{automationRun}`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `AutomationRun` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the automationRun was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. The weak etag of the `AutomationRun` resource. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`serviceAccount` |  `string` Output only. Email address of the user-managed IAM service account that performs the operations against Cloud Deploy resources.  
`automationSnapshot` |  `object (`[Automation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automations#Automation)`)` Output only. Snapshot of the Automation taken at AutomationRun creation time.  
`targetId` |  `string` Output only. The ID of the source target that initiates the `AutomationRun`. The value of this field is the last segment of a target name.  
`state` |  `enum (`[State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#State)`)` Output only. Current state of the `AutomationRun`.  
`stateDescription` |  `string` Output only. Explains the current state of the `AutomationRun`. Present only when an explanation is needed.  
`policyViolation` |  `object (`[PolicyViolation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#PolicyViolation)`)` Output only. Contains information about what policies prevented the `AutomationRun` from proceeding.  
`expireTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time the `AutomationRun` expires. An `AutomationRun` expires after 14 days from its creation date.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`ruleId` |  `string` Output only. The ID of the automation rule that initiated the operation.  
`automationId` |  `string` Output only. The ID of the automation that initiated the operation.  
`waitUntilTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Earliest time the `AutomationRun` will attempt to resume. Wait-time is configured by `wait` in automation rule.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`uid` |  `string` Output only. Unique identifier of the `AutomationRun`.  
Union field `operation`. The operation that the `AutomationRun` will perform. `operation` can be only one of the following:  
`promoteReleaseOperation` |  `object (`[PromoteReleaseOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#PromoteReleaseOperation)`)` Output only. Promotes a release to a specified 'Target'.  
`advanceRolloutOperation` |  `object (`[AdvanceRolloutOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#AdvanceRolloutOperation)`)` Output only. Advances a rollout to the next phase.  
`repairRolloutOperation` |  `object (`[RepairRolloutOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairRolloutOperation)`)` Output only. Repairs a failed 'Rollout'.  
`timedPromoteReleaseOperation` |  `object (`[TimedPromoteReleaseOperation](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#TimedPromoteReleaseOperation)`)` Output only. Promotes a release to a specified 'Target' as defined in a Timed Promote Release rule.  
  
## State

Valid state of an `AutomationRun`.

Enums  
---  
`STATE_UNSPECIFIED` | The `AutomationRun` has an unspecified state.  
`SUCCEEDED` | The `AutomationRun` has succeeded.  
`CANCELLED` | The `AutomationRun` was cancelled.  
`FAILED` | The `AutomationRun` has failed.  
`IN_PROGRESS` | The `AutomationRun` is in progress.  
`PENDING` | The `AutomationRun` is pending.  
`ABORTED` | The `AutomationRun` was aborted.  
  
## PolicyViolation

Returned from an action if one or more policies were violated, and therefore the action was prevented. Contains information about what policies were violated and why.

JSON representation  
---  
      
    
    {
      "policyViolationDetails": [
        {
          object ([PolicyViolationDetails](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#PolicyViolationDetails))
        }
      ]
    }  
  
Fields  
---  
`policyViolationDetails[]` |  `object (`[PolicyViolationDetails](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#PolicyViolationDetails)`)` Policy violation details.  
  
## PolicyViolationDetails

Policy violation details.

JSON representation  
---  
      
    
    {
      "policy": string,
      "ruleId": string,
      "failureMessage": string
    }  
  
Fields  
---  
`policy` |  `string` Name of the policy that was violated. Policy resource will be in the format of `projects/{project}/locations/{location}/policies/{policy}`.  
`ruleId` |  `string` Id of the rule that triggered the policy violation.  
`failureMessage` |  `string` User readable message about why the request violated a policy. This is not intended for machine parsing.  
  
## PromoteReleaseOperation

Contains the information of an automated promote-release operation.

JSON representation  
---  
      
    
    {
      "targetId": string,
      "wait": string,
      "rollout": string,
      "phase": string
    }  
  
Fields  
---  
`targetId` |  `string` Output only. The ID of the target that represents the promotion stage to which the release will be promoted. The value of this field is the last segment of a target name.  
`wait` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. How long the operation will be paused.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`rollout` |  `string` Output only. The name of the rollout that initiates the `AutomationRun`.  
`phase` |  `string` Output only. The starting phase of the rollout created by this operation.  
  
## AdvanceRolloutOperation

Contains the information of an automated advance-rollout operation.

JSON representation  
---  
      
    
    {
      "sourcePhase": string,
      "wait": string,
      "rollout": string,
      "destinationPhase": string
    }  
  
Fields  
---  
`sourcePhase` |  `string` Output only. The phase of a deployment that initiated the operation.  
`wait` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. How long the operation will be paused.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`rollout` |  `string` Output only. The name of the rollout that initiates the `AutomationRun`.  
`destinationPhase` |  `string` Output only. The phase the rollout will be advanced to.  
  
## RepairRolloutOperation

Contains the information for an automated `repair rollout` operation.

JSON representation  
---  
      
    
    {
      "rollout": string,
      "currentRepairPhaseIndex": string,
      "repairPhases": [
        {
          object ([RepairPhase](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairPhase))
        }
      ],
      "phaseId": string,
      "jobId": string
    }  
  
Fields  
---  
`rollout` |  `string` Output only. The name of the rollout that initiates the `AutomationRun`.  
`currentRepairPhaseIndex` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The index of the current repair action in the repair sequence.  
`repairPhases[]` |  `object (`[RepairPhase](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairPhase)`)` Output only. Records of the repair attempts. Each repair phase may have multiple retry attempts or single rollback attempt.  
`phaseId` |  `string` Output only. The phase ID of the phase that includes the job being repaired.  
`jobId` |  `string` Output only. The job ID for the Job to repair.  
  
## RepairPhase

RepairPhase tracks the repair attempts that have been made for each `RepairPhaseConfig` specified in the `Automation` resource.

JSON representation  
---  
      
    
    {
    
      // Union field repair_phase can be only one of the following:
      "retry": {
        object ([RetryPhase](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RetryPhase))
      },
      "rollback": {
        object ([RollbackAttempt](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RollbackAttempt))
      }
      // End of list of possible types for union field repair_phase.
    }  
  
Fields  
---  
Union field `repair_phase`. The `RepairPhase` type and the information for that type. `repair_phase` can be only one of the following:  
`retry` |  `object (`[RetryPhase](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RetryPhase)`)` Output only. Records of the retry attempts for retry repair mode.  
`rollback` |  `object (`[RollbackAttempt](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RollbackAttempt)`)` Output only. Rollback attempt for rollback repair mode .  
  
## RetryPhase

RetryPhase contains the retry attempts and the metadata for initiating a new attempt.

JSON representation  
---  
      
    
    {
      "totalAttempts": string,
      "backoffMode": enum ([BackoffMode](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/BackoffMode)),
      "attempts": [
        {
          object ([RetryAttempt](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RetryAttempt))
        }
      ]
    }  
  
Fields  
---  
`totalAttempts` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The number of attempts that have been made.  
`backoffMode` |  `enum (`[BackoffMode](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/BackoffMode)`)` Output only. The pattern of how the wait time of the retry attempt is calculated.  
`attempts[]` |  `object (`[RetryAttempt](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RetryAttempt)`)` Output only. Detail of a retry action.  
  
## RetryAttempt

RetryAttempt represents an action of retrying the failed Cloud Deploy job.

JSON representation  
---  
      
    
    {
      "attempt": string,
      "wait": string,
      "state": enum ([RepairState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairState)),
      "stateDesc": string
    }  
  
Fields  
---  
`attempt` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Output only. The index of this retry attempt.  
`wait` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. How long the operation will be paused.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`state` |  `enum (`[RepairState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairState)`)` Output only. Valid state of this retry action.  
`stateDesc` |  `string` Output only. Description of the state of the Retry.  
  
## RepairState

Valid state of a repair attempt.

Enums  
---  
`REPAIR_STATE_UNSPECIFIED` | The `repair` has an unspecified state.  
`REPAIR_STATE_SUCCEEDED` | The `repair` action has succeeded.  
`REPAIR_STATE_CANCELLED` | The `repair` action was cancelled.  
`REPAIR_STATE_FAILED` | The `repair` action has failed.  
`REPAIR_STATE_IN_PROGRESS` | The `repair` action is in progress.  
`REPAIR_STATE_PENDING` | The `repair` action is pending.  
`REPAIR_STATE_ABORTED` | The `repair` action was aborted.  
  
## RollbackAttempt

RollbackAttempt represents an action of rolling back a Cloud Deploy 'Target'.

JSON representation  
---  
      
    
    {
      "destinationPhase": string,
      "rolloutId": string,
      "state": enum ([RepairState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairState)),
      "stateDesc": string,
      "disableRollbackIfRolloutPending": boolean
    }  
  
Fields  
---  
`destinationPhase` |  `string` Output only. The phase to which the rollout will be rolled back to.  
`rolloutId` |  `string` Output only. ID of the rollback `Rollout` to create.  
`state` |  `enum (`[RepairState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns#RepairState)`)` Output only. Valid state of this rollback action.  
`stateDesc` |  `string` Output only. Description of the state of the Rollback.  
`disableRollbackIfRolloutPending` |  `boolean` Output only. If active rollout exists on the target, abort this rollback.  
  
## TimedPromoteReleaseOperation

Contains the information of an automated timed promote-release operation.

JSON representation  
---  
      
    
    {
      "targetId": string,
      "release": string,
      "phase": string
    }  
  
Fields  
---  
`targetId` |  `string` Output only. The ID of the target that represents the promotion stage to which the release will be promoted. The value of this field is the last segment of a target name.  
`release` |  `string` Output only. The name of the release to be promoted.  
`phase` |  `string` Output only. The starting phase of the rollout created by this operation.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns/cancel)`

|  Cancels an AutomationRun.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns/get)`

|  Gets details of a single AutomationRun.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.automationRuns/list)`

|  Lists AutomationRuns in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-01-30 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-01-30 UTC."],[],[]] 
