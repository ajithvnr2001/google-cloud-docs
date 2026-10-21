---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts
title: REST Resource: projects.locations.deliveryPipelines.releases.rollouts \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:14:59.080064+00:00
---

# REST Resource: projects.locations.deliveryPipelines.releases.rollouts  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.deliveryPipelines.releases.rollouts Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Rollout
    * JSON representation
  * ApprovalState
  * State
  * FailureCause
  * Phase
    * JSON representation
  * State
  * DeploymentJobs
    * JSON representation
  * Job
    * JSON representation
  * State
  * DeployJob
  * VerifyJob
    * JSON representation
  * PredeployJob
    * JSON representation
  * PostdeployJob
    * JSON representation
  * CreateChildRolloutJob
  * AdvanceChildRolloutJob
  * AnalysisJob
    * JSON representation
  * ChildRolloutJobs
    * JSON representation
  * Metadata
    * JSON representation
  * AutomationRolloutMetadata
    * JSON representation
  * Methods



## Resource: Rollout

A `Rollout` resource in the Cloud Deploy API.

A `Rollout` contains information around a specific deployment to a `Target`.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "description": string,
      "annotations": {
        string: string,
        ...
      },
      "labels": {
        string: string,
        ...
      },
      "createTime": string,
      "approveTime": string,
      "enqueueTime": string,
      "deployStartTime": string,
      "deployEndTime": string,
      "targetId": string,
      "approvalState": enum ([ApprovalState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#ApprovalState)),
      "state": enum ([State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#State)),
      "failureReason": string,
      "deployingBuild": string,
      "etag": string,
      "deployFailureCause": enum ([FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#FailureCause)),
      "phases": [
        {
          object ([Phase](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Phase))
        }
      ],
      "metadata": {
        object ([Metadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Metadata))
      },
      "controllerRollout": string,
      "rollbackOfRollout": string,
      "rolledBackByRollouts": [
        string
      ],
      "activeRepairAutomationRun": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. Name of the `Rollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`. The `rollout` component must match `[a-z]([a-z0-9-]{0,61}[a-z0-9])?`  
`uid` |  `string` Output only. Unique identifier of the `Rollout`.  
`description` |  `string` Optional. Description of the `Rollout` for user purposes. Max length is 255 characters.  
`annotations` |  `map (key: string, value: string)` Optional. User annotations. These attributes can only be set and used by the user, and not by Cloud Deploy. See <https://google.aip.dev/128#annotations> for more details such as format and size limitations.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`labels` |  `map (key: string, value: string)` Labels are attributes that can be set and used by both the user and by Cloud Deploy. Labels must meet the following constraints:

  * Keys and values can contain only lowercase letters, numeric characters, underscores, and dashes.
  * All characters must use UTF-8 encoding, and international characters are allowed.
  * Keys must start with a lowercase letter or international character.
  * Each resource is limited to a maximum of 64 labels.

Both keys and values are additionally constrained to be <= 128 bytes.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `Rollout` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`approveTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `Rollout` was approved.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`enqueueTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `Rollout` was enqueued.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deployStartTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `Rollout` started deploying.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deployEndTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `Rollout` finished deploying.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`targetId` |  `string` Required. The ID of Target to which this `Rollout` is deploying.  
`approvalState` |  `enum (`[ApprovalState](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#ApprovalState)`)` Output only. Approval state of the `Rollout`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#State)`)` Output only. Current state of the `Rollout`.  
`failureReason` |  `string` Output only. Additional information about the rollout failure, if available.  
`deployingBuild` |  `string` Output only. The resource name of the Cloud Build `Build` object that is used to deploy the Rollout. Format is `projects/{project}/locations/{location}/builds/{build}`.  
`etag` |  `string` This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`deployFailureCause` |  `enum (`[FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#FailureCause)`)` Output only. The reason this rollout failed. This will always be unspecified while the rollout is in progress.  
`phases[]` |  `object (`[Phase](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Phase)`)` Output only. The phases that represent the workflows of this `Rollout`.  
`metadata` |  `object (`[Metadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Metadata)`)` Output only. Metadata contains information about the rollout.  
`controllerRollout` |  `string` Output only. Name of the `ControllerRollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`.  
`rollbackOfRollout` |  `string` Output only. Name of the `Rollout` that is rolled back by this `Rollout`. Empty if this `Rollout` wasn't created as a rollback.  
`rolledBackByRollouts[]` |  `string` Output only. Names of `Rollouts` that rolled back this `Rollout`.  
`activeRepairAutomationRun` |  `string` Output only. The AutomationRun actively repairing the rollout.  
  
## ApprovalState

Valid approval states of a `Rollout`.

Enums  
---  
`APPROVAL_STATE_UNSPECIFIED` | The `Rollout` has an unspecified approval state.  
`NEEDS_APPROVAL` | The `Rollout` requires approval.  
`DOES_NOT_NEED_APPROVAL` | The `Rollout` does not require approval.  
`APPROVED` | The `Rollout` has been approved.  
`REJECTED` | The `Rollout` has been rejected.  
  
## State

Valid states of a `Rollout`.

Enums  
---  
`STATE_UNSPECIFIED` | The `Rollout` has an unspecified state.  
`SUCCEEDED` | The `Rollout` has completed successfully.  
`FAILED` | The `Rollout` has failed.  
`IN_PROGRESS` | The `Rollout` is being deployed.  
`PENDING_APPROVAL` | The `Rollout` needs approval.  
`APPROVAL_REJECTED` | An approver rejected the `Rollout`.  
`PENDING` | The `Rollout` is waiting for an earlier Rollout(s) to complete on this `Target`.  
`PENDING_RELEASE` | The `Rollout` is waiting for the `Release` to be fully rendered.  
`CANCELLING` | The `Rollout` is in the process of being cancelled.  
`CANCELLED` | The `Rollout` has been cancelled.  
`HALTED` | The `Rollout` is halted.  
  
## FailureCause

Well-known rollout failures.

Enums  
---  
`FAILURE_CAUSE_UNSPECIFIED` | No reason for failure is specified.  
`CLOUD_BUILD_UNAVAILABLE` | Cloud Build is not available, either because it is not enabled or because Cloud Deploy has insufficient permissions. See [required permission](https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions).  
`EXECUTION_FAILED` | The deploy operation did not complete successfully; check Cloud Build logs.  
`DEADLINE_EXCEEDED` | Deployment did not complete within the allotted time.  
`RELEASE_FAILED` | Release is in a failed state.  
`RELEASE_ABANDONED` | Release is abandoned.  
`VERIFICATION_CONFIG_NOT_FOUND` | No Skaffold verify configuration was found.  
`CLOUD_BUILD_REQUEST_FAILED` | Cloud Build failed to fulfill Cloud Deploy's request. See failureMessage for additional details.  
`OPERATION_FEATURE_NOT_SUPPORTED` | A Rollout operation had a feature configured that is not supported.  
  
## Phase

Phase represents a collection of jobs that are logically grouped together for a `Rollout`.

JSON representation  
---  
      
    
    {
      "id": string,
      "state": enum ([State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#State_1)),
      "skipMessage": string,
    
      // Union field jobs can be only one of the following:
      "deploymentJobs": {
        object ([DeploymentJobs](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#DeploymentJobs))
      },
      "childRolloutJobs": {
        object ([ChildRolloutJobs](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#ChildRolloutJobs))
      }
      // End of list of possible types for union field jobs.
    }  
  
Fields  
---  
`id` |  `string` Output only. The ID of the Phase.  
`state` |  `enum (`[State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#State_1)`)` Output only. Current state of the Phase.  
`skipMessage` |  `string` Output only. Additional information on why the Phase was skipped, if available.  
Union field `jobs`. The job composition of this Phase. `jobs` can be only one of the following:  
`deploymentJobs` |  `object (`[DeploymentJobs](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#DeploymentJobs)`)` Output only. Deployment job composition.  
`childRolloutJobs` |  `object (`[ChildRolloutJobs](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#ChildRolloutJobs)`)` Output only. ChildRollout job composition.  
  
## State

Valid states of a Phase.

Enums  
---  
`STATE_UNSPECIFIED` | The Phase has an unspecified state.  
`PENDING` | The Phase is waiting for an earlier Phase(s) to complete.  
`IN_PROGRESS` | The Phase is in progress.  
`SUCCEEDED` | The Phase has succeeded.  
`FAILED` | The Phase has failed.  
`ABORTED` | The Phase was aborted.  
`SKIPPED` | The Phase was skipped.  
  
## DeploymentJobs

Deployment job composition.

JSON representation  
---  
      
    
    {
      "predeployJob": {
        object ([Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job))
      },
      "deployJob": {
        object ([Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job))
      },
      "verifyJob": {
        object ([Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job))
      },
      "analysisJob": {
        object ([Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job))
      },
      "postdeployJob": {
        object ([Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job))
      }
    }  
  
Fields  
---  
`predeployJob` |  `object (`[Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job)`)` Output only. The predeploy Job, which is the first job on the phase.  
`deployJob` |  `object (`[Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job)`)` Output only. The deploy Job. This is the deploy job in the phase.  
`verifyJob` |  `object (`[Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job)`)` Output only. The verify Job. Runs after a deploy if the deploy succeeds.  
`analysisJob` |  `object (`[Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job)`)` Output only. The analysis Job. Runs after a verify if there is a verify job and the verify job succeeds.  
`postdeployJob` |  `object (`[Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job)`)` Output only. The postdeploy Job, which is the last job on the phase.  
  
## Job

Job represents an operation for a `Rollout`.

JSON representation  
---  
      
    
    {
      "id": string,
      "state": enum ([State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#State_2)),
      "skipMessage": string,
      "jobRun": string,
    
      // Union field job_type can be only one of the following:
      "deployJob": {
        object ([DeployJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#DeployJob))
      },
      "verifyJob": {
        object ([VerifyJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#VerifyJob))
      },
      "predeployJob": {
        object ([PredeployJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#PredeployJob))
      },
      "postdeployJob": {
        object ([PostdeployJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#PostdeployJob))
      },
      "createChildRolloutJob": {
        object ([CreateChildRolloutJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#CreateChildRolloutJob))
      },
      "advanceChildRolloutJob": {
        object ([AdvanceChildRolloutJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#AdvanceChildRolloutJob))
      },
      "analysisJob": {
        object ([AnalysisJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#AnalysisJob))
      }
      // End of list of possible types for union field job_type.
    }  
  
Fields  
---  
`id` |  `string` Output only. The ID of the Job.  
`state` |  `enum (`[State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#State_2)`)` Output only. The current state of the Job.  
`skipMessage` |  `string` Output only. Additional information on why the Job was skipped, if available.  
`jobRun` |  `string` Output only. The name of the `JobRun` responsible for the most recent invocation of this Job.  
Union field `job_type`. The type of Job. `job_type` can be only one of the following:  
`deployJob` |  `object (`[DeployJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#DeployJob)`)` Output only. A deploy Job.  
`verifyJob` |  `object (`[VerifyJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#VerifyJob)`)` Output only. A verify Job.  
`predeployJob` |  `object (`[PredeployJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#PredeployJob)`)` Output only. A predeploy Job.  
`postdeployJob` |  `object (`[PostdeployJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#PostdeployJob)`)` Output only. A postdeploy Job.  
`createChildRolloutJob` |  `object (`[CreateChildRolloutJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#CreateChildRolloutJob)`)` Output only. A createChildRollout Job.  
`advanceChildRolloutJob` |  `object (`[AdvanceChildRolloutJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#AdvanceChildRolloutJob)`)` Output only. An advanceChildRollout Job.  
`analysisJob` |  `object (`[AnalysisJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#AnalysisJob)`)` Output only. An analysis Job.  
  
## State

Valid states of a Job.

Enums  
---  
`STATE_UNSPECIFIED` | The Job has an unspecified state.  
`PENDING` | The Job is waiting for an earlier Phase(s) or Job(s) to complete.  
`DISABLED` | The Job is disabled.  
`IN_PROGRESS` | The Job is in progress.  
`SUCCEEDED` | The Job succeeded.  
`FAILED` | The Job failed.  
`ABORTED` | The Job was aborted.  
`SKIPPED` | The Job was skipped.  
`IGNORED` | The Job was ignored.  
  
## DeployJob

This type has no fields.

A deploy Job.

## VerifyJob

A verify Job.

JSON representation  
---  
      
    
    {
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
        }
      ]
    }  
  
Fields  
---  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Output only. The tasks that are executed as part of the verify Job.  
  
## PredeployJob

A predeploy Job.

JSON representation  
---  
      
    
    {
      "actions": [
        string
      ],
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
        }
      ]
    }  
  
Fields  
---  
`actions[]` |  `string` Output only. The custom actions that the predeploy Job executes.  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Output only. The tasks that are executed as part of the predeploy Job.  
  
## PostdeployJob

A postdeploy Job.

JSON representation  
---  
      
    
    {
      "actions": [
        string
      ],
      "tasks": [
        {
          object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
        }
      ]
    }  
  
Fields  
---  
`actions[]` |  `string` Output only. The custom actions that the postdeploy Job executes.  
`tasks[]` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Output only. The tasks that are executed as part of the postdeploy Job.  
  
## CreateChildRolloutJob

This type has no fields.

A createChildRollout Job.

## AdvanceChildRolloutJob

This type has no fields.

An advanceChildRollout Job.

## AnalysisJob

An analysis Job.

JSON representation  
---  
      
    
    {
      "duration": string,
      "googleCloud": {
        object ([GoogleCloudAnalysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/GoogleCloudAnalysis))
      },
      "customChecks": [
        {
          object ([CustomCheck](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomCheck))
        }
      ]
    }  
  
Fields  
---  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The amount of time in minutes the analysis Job will run, up to a maximum of 48 hours. If any check in this Job is still running when the duration ends, the Job keeps running until that check completes.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`googleCloud` |  `object (`[GoogleCloudAnalysis](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/GoogleCloudAnalysis)`)` Output only. Google Cloud - based analysis checks that are run as part of the analysis Job.  
`customChecks[]` |  `object (`[CustomCheck](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomCheck)`)` Output only. Custom analysis checks from 3P metric providers that are run as part of the analysis Job.  
  
## ChildRolloutJobs

ChildRollouts job composition

JSON representation  
---  
      
    
    {
      "createRolloutJobs": [
        {
          object ([Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job))
        }
      ],
      "advanceRolloutJobs": [
        {
          object ([Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job))
        }
      ]
    }  
  
Fields  
---  
`createRolloutJobs[]` |  `object (`[Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job)`)` Output only. List of CreateChildRolloutJobs  
`advanceRolloutJobs[]` |  `object (`[Job](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#Job)`)` Output only. List of AdvanceChildRolloutJobs  
  
## Metadata

Metadata includes information associated with a `Rollout`.

JSON representation  
---  
      
    
    {
      "cloudRun": {
        object ([CloudRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CloudRunMetadata))
      },
      "automation": {
        object ([AutomationRolloutMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#AutomationRolloutMetadata))
      },
      "custom": {
        object ([CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata))
      }
    }  
  
Fields  
---  
`cloudRun` |  `object (`[CloudRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CloudRunMetadata)`)` Output only. The name of the Cloud Run Service that is associated with a `Rollout`.  
`automation` |  `object (`[AutomationRolloutMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts#AutomationRolloutMetadata)`)` Output only. AutomationRolloutMetadata contains the information about the interactions between Automation service and this rollout.  
`custom` |  `object (`[CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata)`)` Output only. Custom metadata provided by user-defined `Rollout` operations.  
  
## AutomationRolloutMetadata

AutomationRolloutMetadata contains Automation-related actions that were performed on a rollout.

JSON representation  
---  
      
    
    {
      "promoteAutomationRun": string,
      "advanceAutomationRuns": [
        string
      ],
      "repairAutomationRuns": [
        string
      ]
    }  
  
Fields  
---  
`promoteAutomationRun` |  `string` Output only. The name of the AutomationRun initiated by a promote release rule.  
`advanceAutomationRuns[]` |  `string` Output only. The names of the AutomationRuns initiated by an advance rollout rule.  
`repairAutomationRuns[]` |  `string` Output only. The names of the AutomationRuns initiated by a repair rollout rule.  
  
## Methods  
  
---  
  
### `[advance](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/advance)`

|  Advances a Rollout in a given project and location.  
  
### `[approve](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/approve)`

|  Approves a Rollout.  
  
### `[cancel](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/cancel)`

|  Cancels a Rollout in a given project and location.  
  
### `[create](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/create)`

|  Creates a new Rollout in a given project and location.  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/get)`

|  Gets details of a single Rollout.  
  
### `[ignoreJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/ignoreJob)`

|  Ignores the specified Job in a Rollout.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/list)`

|  Lists Rollouts in a given project and location.  
  
### `[retryJob](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts/retryJob)`

|  Retries the specified Job in a Rollout.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
