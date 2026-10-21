---
url: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns
title: REST Resource: projects.locations.deliveryPipelines.releases.rollouts.jobRuns \u00a0|\u00a0 Cloud Deploy \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:15:00.247805+00:00
---

# REST Resource: projects.locations.deliveryPipelines.releases.rollouts.jobRuns  |  Cloud Deploy  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Application development ](https://docs.cloud.google.com/docs/application-development)
  * [ Cloud Deploy ](https://docs.cloud.google.com/deploy/docs)
  * [ Reference ](https://docs.cloud.google.com/deploy/docs/api)



Send feedback 

#  REST Resource: projects.locations.deliveryPipelines.releases.rollouts.jobRuns Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: JobRun
    * JSON representation
  * State
  * DeployJobRun
    * JSON representation
  * FailureCause
  * DeployJobRunMetadata
    * JSON representation
  * CustomTargetDeployMetadata
    * JSON representation
  * DeployArtifact
    * JSON representation
  * VerifyJobRun
    * JSON representation
  * FailureCause
  * VerifyJobRunMetadata
    * JSON representation
  * PredeployJobRun
    * JSON representation
  * FailureCause
  * PredeployJobRunMetadata
    * JSON representation
  * PostdeployJobRun
    * JSON representation
  * FailureCause
  * PostdeployJobRunMetadata
    * JSON representation
  * CreateChildRolloutJobRun
    * JSON representation
  * AdvanceChildRolloutJobRun
    * JSON representation
  * AnalysisJobRun
    * JSON representation
  * AlertPolicyCheckStatus
    * JSON representation
  * FailedAlertPolicy
    * JSON representation
  * CustomCheckStatus
    * JSON representation
  * FailureCause
  * Methods



## Resource: JobRun

A `JobRun` resource in the Cloud Deploy API.

A `JobRun` contains information of a single `Rollout` job evaluation.

JSON representation  
---  
      
    
    {
      "name": string,
      "uid": string,
      "phaseId": string,
      "jobId": string,
      "createTime": string,
      "startTime": string,
      "endTime": string,
      "state": enum ([State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#State)),
      "etag": string,
    
      // Union field job_run can be only one of the following:
      "deployJobRun": {
        object ([DeployJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#DeployJobRun))
      },
      "verifyJobRun": {
        object ([VerifyJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#VerifyJobRun))
      },
      "predeployJobRun": {
        object ([PredeployJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PredeployJobRun))
      },
      "postdeployJobRun": {
        object ([PostdeployJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PostdeployJobRun))
      },
      "createChildRolloutJobRun": {
        object ([CreateChildRolloutJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#CreateChildRolloutJobRun))
      },
      "advanceChildRolloutJobRun": {
        object ([AdvanceChildRolloutJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#AdvanceChildRolloutJobRun))
      },
      "analysisJobRun": {
        object ([AnalysisJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#AnalysisJobRun))
      }
      // End of list of possible types for union field job_run.
    }  
  
Fields  
---  
`name` |  `string` Output only. Name of the `JobRun`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{releases}/rollouts/{rollouts}/jobRuns/{uuid}`.  
`uid` |  `string` Output only. Unique identifier of the `JobRun`.  
`phaseId` |  `string` Output only. ID of the `Rollout` phase this `JobRun` belongs in.  
`jobId` |  `string` Output only. ID of the `Rollout` job this `JobRun` corresponds to.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `JobRun` was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `JobRun` was started.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Time at which the `JobRun` ended.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#State)`)` Output only. The current state of the `JobRun`.  
`etag` |  `string` Output only. This checksum is computed by the server based on the value of other fields, and may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
Union field `job_run`. The `JobRun` type and the information for that type. `job_run` can be only one of the following:  
`deployJobRun` |  `object (`[DeployJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#DeployJobRun)`)` Output only. Information specific to a deploy `JobRun`.  
`verifyJobRun` |  `object (`[VerifyJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#VerifyJobRun)`)` Output only. Information specific to a verify `JobRun`.  
`predeployJobRun` |  `object (`[PredeployJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PredeployJobRun)`)` Output only. Information specific to a predeploy `JobRun`.  
`postdeployJobRun` |  `object (`[PostdeployJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PostdeployJobRun)`)` Output only. Information specific to a postdeploy `JobRun`.  
`createChildRolloutJobRun` |  `object (`[CreateChildRolloutJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#CreateChildRolloutJobRun)`)` Output only. Information specific to a createChildRollout `JobRun`.  
`advanceChildRolloutJobRun` |  `object (`[AdvanceChildRolloutJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#AdvanceChildRolloutJobRun)`)` Output only. Information specific to an advanceChildRollout `JobRun`  
`analysisJobRun` |  `object (`[AnalysisJobRun](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#AnalysisJobRun)`)` Output only. Information specific to an analysis `JobRun`.  
  
## State

Valid states of a `JobRun`.

Enums  
---  
`STATE_UNSPECIFIED` | The `JobRun` has an unspecified state.  
`IN_PROGRESS` | The `JobRun` is in progress.  
`SUCCEEDED` | The `JobRun` has succeeded.  
`FAILED` | The `JobRun` has failed.  
`TERMINATING` | The `JobRun` is terminating.  
`TERMINATED` | The `JobRun` was terminated.  
  
## DeployJobRun

DeployJobRun contains information specific to a deploy `JobRun`.

JSON representation  
---  
      
    
    {
      "build": string,
      "failureCause": enum ([FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause)),
      "failureMessage": string,
      "metadata": {
        object ([DeployJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#DeployJobRunMetadata))
      },
      "artifact": {
        object ([DeployArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#DeployArtifact))
      }
    }  
  
Fields  
---  
`build` |  `string` Output only. The resource name of the Cloud Build `Build` object that is used to deploy. Format is `projects/{project}/locations/{location}/builds/{build}`.  
`failureCause` |  `enum (`[FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause)`)` Output only. The reason the deploy failed. This will always be unspecified while the deploy is in progress or if it succeeded.  
`failureMessage` |  `string` Output only. Additional information about the deploy failure, if available.  
`metadata` |  `object (`[DeployJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#DeployJobRunMetadata)`)` Output only. Metadata containing information about the deploy job run.  
`artifact` |  `object (`[DeployArtifact](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#DeployArtifact)`)` Output only. The artifact of a deploy job run, if available.  
  
## FailureCause

Well-known deploy failures.

Enums  
---  
`FAILURE_CAUSE_UNSPECIFIED` | No reason for failure is specified.  
`CLOUD_BUILD_UNAVAILABLE` | Cloud Build is not available, either because it is not enabled or because Cloud Deploy has insufficient permissions. See [Required permission](https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions).  
`EXECUTION_FAILED` | The deploy operation did not complete successfully; check Cloud Build logs.  
`DEADLINE_EXCEEDED` | The deploy job run did not complete within the allotted time.  
`MISSING_RESOURCES_FOR_CANARY` | There were missing resources in the runtime environment required for a canary deployment. Check the Cloud Build logs for more information.  
`CLOUD_BUILD_REQUEST_FAILED` | Cloud Build failed to fulfill Cloud Deploy's request. See failureMessage for additional details.  
`DEPLOY_FEATURE_NOT_SUPPORTED` | The deploy operation had a feature configured that is not supported.  
  
## DeployJobRunMetadata

DeployJobRunMetadata surfaces information associated with a `DeployJobRun` to the user.

JSON representation  
---  
      
    
    {
      "cloudRun": {
        object ([CloudRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CloudRunMetadata))
      },
      "customTarget": {
        object ([CustomTargetDeployMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#CustomTargetDeployMetadata))
      },
      "custom": {
        object ([CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata))
      }
    }  
  
Fields  
---  
`cloudRun` |  `object (`[CloudRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CloudRunMetadata)`)` Output only. The name of the Cloud Run Service that is associated with a `DeployJobRun`.  
`customTarget` |  `object (`[CustomTargetDeployMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#CustomTargetDeployMetadata)`)` Output only. Custom Target metadata associated with a `DeployJobRun`.  
`custom` |  `object (`[CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata)`)` Output only. Custom metadata provided by user-defined deploy operation.  
  
## CustomTargetDeployMetadata

CustomTargetDeployMetadata contains information from a Custom Target deploy operation.

JSON representation  
---  
      
    
    {
      "skipMessage": string
    }  
  
Fields  
---  
`skipMessage` |  `string` Output only. Skip message provided in the results of a custom deploy operation.  
  
## DeployArtifact

The artifacts produced by a deploy operation.

JSON representation  
---  
      
    
    {
      "artifactUri": string,
      "manifestPaths": [
        string
      ]
    }  
  
Fields  
---  
`artifactUri` |  `string` Output only. URI of a directory containing the artifacts. All paths are relative to this location.  
`manifestPaths[]` |  `string` Output only. File paths of the manifests applied during the deploy operation relative to the URI.  
  
## VerifyJobRun

VerifyJobRun contains information specific to a verify `JobRun`.

JSON representation  
---  
      
    
    {
      "build": string,
      "artifactUri": string,
      "eventLogPath": string,
      "failureCause": enum ([FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_1)),
      "failureMessage": string,
      "metadata": {
        object ([VerifyJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#VerifyJobRunMetadata))
      }
    }  
  
Fields  
---  
`build` |  `string` Output only. The resource name of the Cloud Build `Build` object that is used to verify. Format is `projects/{project}/locations/{location}/builds/{build}`.  
`artifactUri` |  `string` Output only. URI of a directory containing the verify artifacts. This contains the Skaffold event log.  
`eventLogPath` |  `string` Output only. File path of the Skaffold event log relative to the artifact URI.  
`failureCause` |  `enum (`[FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_1)`)` Output only. The reason the verify failed. This will always be unspecified while the verify is in progress or if it succeeded.  
`failureMessage` |  `string` Output only. Additional information about the verify failure, if available.  
`metadata` |  `object (`[VerifyJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#VerifyJobRunMetadata)`)` Output only. Metadata containing information about the verify `JobRun`.  
  
## FailureCause

Well-known verify failures.

Enums  
---  
`FAILURE_CAUSE_UNSPECIFIED` | No reason for failure is specified.  
`CLOUD_BUILD_UNAVAILABLE` | Cloud Build is not available, either because it is not enabled or because Cloud Deploy has insufficient permissions. See [required permission](https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions).  
`EXECUTION_FAILED` | The verify operation did not complete successfully; check Cloud Build logs.  
`DEADLINE_EXCEEDED` | The verify job run did not complete within the allotted time.  
`VERIFICATION_CONFIG_NOT_FOUND` | No Skaffold verify configuration was found.  
`CLOUD_BUILD_REQUEST_FAILED` | Cloud Build failed to fulfill Cloud Deploy's request. See failureMessage for additional details.  
  
## VerifyJobRunMetadata

VerifyJobRunMetadata contains metadata about the verify `JobRun`.

JSON representation  
---  
      
    
    {
      "custom": {
        object ([CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata))
      }
    }  
  
Fields  
---  
`custom` |  `object (`[CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata)`)` Output only. Custom metadata provided by user-defined verify operation.  
  
## PredeployJobRun

PredeployJobRun contains information specific to a predeploy `JobRun`.

JSON representation  
---  
      
    
    {
      "build": string,
      "failureCause": enum ([FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_2)),
      "failureMessage": string,
      "metadata": {
        object ([PredeployJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PredeployJobRunMetadata))
      }
    }  
  
Fields  
---  
`build` |  `string` Output only. The resource name of the Cloud Build `Build` object that is used to execute the custom actions associated with the predeploy Job. Format is `projects/{project}/locations/{location}/builds/{build}`.  
`failureCause` |  `enum (`[FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_2)`)` Output only. The reason the predeploy failed. This will always be unspecified while the predeploy is in progress or if it succeeded.  
`failureMessage` |  `string` Output only. Additional information about the predeploy failure, if available.  
`metadata` |  `object (`[PredeployJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PredeployJobRunMetadata)`)` Output only. Metadata containing information about the predeploy `JobRun`.  
  
## FailureCause

Well-known predeploy failures.

Enums  
---  
`FAILURE_CAUSE_UNSPECIFIED` | No reason for failure is specified.  
`CLOUD_BUILD_UNAVAILABLE` | Cloud Build is not available, either because it is not enabled or because Cloud Deploy has insufficient permissions. See [required permission](https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions).  
`EXECUTION_FAILED` | The predeploy operation did not complete successfully; check Cloud Build logs.  
`DEADLINE_EXCEEDED` | The predeploy job run did not complete within the allotted time.  
`CLOUD_BUILD_REQUEST_FAILED` | Cloud Build failed to fulfill Cloud Deploy's request. See failureMessage for additional details.  
  
## PredeployJobRunMetadata

PredeployJobRunMetadata contains metadata about the predeploy `JobRun`.

JSON representation  
---  
      
    
    {
      "custom": {
        object ([CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata))
      }
    }  
  
Fields  
---  
`custom` |  `object (`[CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata)`)` Output only. Custom metadata provided by user-defined predeploy operation.  
  
## PostdeployJobRun

PostdeployJobRun contains information specific to a postdeploy `JobRun`.

JSON representation  
---  
      
    
    {
      "build": string,
      "failureCause": enum ([FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_3)),
      "failureMessage": string,
      "metadata": {
        object ([PostdeployJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PostdeployJobRunMetadata))
      }
    }  
  
Fields  
---  
`build` |  `string` Output only. The resource name of the Cloud Build `Build` object that is used to execute the custom actions associated with the postdeploy Job. Format is `projects/{project}/locations/{location}/builds/{build}`.  
`failureCause` |  `enum (`[FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_3)`)` Output only. The reason the postdeploy failed. This will always be unspecified while the postdeploy is in progress or if it succeeded.  
`failureMessage` |  `string` Output only. Additional information about the postdeploy failure, if available.  
`metadata` |  `object (`[PostdeployJobRunMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#PostdeployJobRunMetadata)`)` Output only. Metadata containing information about the postdeploy `JobRun`.  
  
## FailureCause

Well-known postdeploy failures.

Enums  
---  
`FAILURE_CAUSE_UNSPECIFIED` | No reason for failure is specified.  
`CLOUD_BUILD_UNAVAILABLE` | Cloud Build is not available, either because it is not enabled or because Cloud Deploy has insufficient permissions. See [required permission](https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions).  
`EXECUTION_FAILED` | The postdeploy operation did not complete successfully; check Cloud Build logs.  
`DEADLINE_EXCEEDED` | The postdeploy job run did not complete within the allotted time.  
`CLOUD_BUILD_REQUEST_FAILED` | Cloud Build failed to fulfill Cloud Deploy's request. See failureMessage for additional details.  
  
## PostdeployJobRunMetadata

PostdeployJobRunMetadata contains metadata about the postdeploy `JobRun`.

JSON representation  
---  
      
    
    {
      "custom": {
        object ([CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata))
      }
    }  
  
Fields  
---  
`custom` |  `object (`[CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata)`)` Output only. Custom metadata provided by user-defined postdeploy operation.  
  
## CreateChildRolloutJobRun

CreateChildRolloutJobRun contains information specific to a createChildRollout `JobRun`.

JSON representation  
---  
      
    
    {
      "rollout": string,
      "rolloutPhaseId": string
    }  
  
Fields  
---  
`rollout` |  `string` Output only. Name of the `ChildRollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`.  
`rolloutPhaseId` |  `string` Output only. The ID of the childRollout Phase initiated by this JobRun.  
  
## AdvanceChildRolloutJobRun

AdvanceChildRolloutJobRun contains information specific to a advanceChildRollout `JobRun`.

JSON representation  
---  
      
    
    {
      "rollout": string,
      "rolloutPhaseId": string
    }  
  
Fields  
---  
`rollout` |  `string` Output only. Name of the `ChildRollout`. Format is `projects/{project}/locations/{location}/deliveryPipelines/{deliveryPipeline}/releases/{release}/rollouts/{rollout}`.  
`rolloutPhaseId` |  `string` Output only. the ID of the ChildRollout's Phase.  
  
## AnalysisJobRun

AnalysisJobRun contains information specific to an analysis `JobRun`.

JSON representation  
---  
      
    
    {
      "alertPolicyAnalyses": [
        {
          object ([AlertPolicyCheckStatus](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#AlertPolicyCheckStatus))
        }
      ],
      "customCheckAnalyses": [
        {
          object ([CustomCheckStatus](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#CustomCheckStatus))
        }
      ],
      "failedCheckId": string
    }  
  
Fields  
---  
`alertPolicyAnalyses[]` |  `object (`[AlertPolicyCheckStatus](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#AlertPolicyCheckStatus)`)` Output only. The status of the running alert policy checks configured for this analysis.  
`customCheckAnalyses[]` |  `object (`[CustomCheckStatus](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#CustomCheckStatus)`)` Output only. The status of the running custom checks configured for this analysis.  
`failedCheckId` |  `string` Output only. The ID of the configured check that failed. This will always be blank while the analysis is in progress or if it succeeded.  
  
## AlertPolicyCheckStatus

AlertPolicyCheckStatus contains information specific to a single run of an alert policy check.

JSON representation  
---  
      
    
    {
      "id": string,
      "alertPolicies": [
        string
      ],
      "labels": {
        string: string,
        ...
      },
      "failedAlertPolicies": [
        {
          object ([FailedAlertPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailedAlertPolicy))
        }
      ],
      "failureMessage": string
    }  
  
Fields  
---  
`id` |  `string` Output only. The ID of this analysis.  
`alertPolicies[]` |  `string` Output only. The alert policies that this analysis monitors. Format is `projects/{project}/locations/{location}/alertPolicies/{alertPolicy}`.  
`labels` |  `map (key: string, value: string)` Output only. The resolved labels used to filter for specific incidents.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`failedAlertPolicies[]` |  `object (`[FailedAlertPolicy](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailedAlertPolicy)`)` Output only. The alert policies that were found to be firing during this check. This will be empty if no incidents were found.  
`failureMessage` |  `string` Output only. Additional information about the alert policy check failure, if available. This will be empty if the alert policy check succeeded.  
  
## FailedAlertPolicy

FailedAlertPolicy contains information about an alert policy that was found to be firing during an alert policy check.

JSON representation  
---  
      
    
    {
      "alertPolicy": string,
      "alerts": [
        string
      ]
    }  
  
Fields  
---  
`alertPolicy` |  `string` Output only. The name of the alert policy that was found to be firing. Format is `projects/{project}/locations/{location}/alertPolicies/{alertPolicy}`.  
`alerts[]` |  `string` Output only. Open alerts for the alerting policies that matched the alert policy check configuration.  
  
## CustomCheckStatus

CustomCheckStatus contains information specific to a single iteration of a custom analysis job.

JSON representation  
---  
      
    
    {
      "id": string,
      "frequency": string,
      "task": {
        object ([Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task))
      },
      "latestBuild": string,
      "failureCause": enum ([FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_4)),
      "failureMessage": string,
      "metadata": {
        object ([CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata))
      }
    }  
  
Fields  
---  
`id` |  `string` Output only. The ID of the custom check.  
`frequency` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The frequency in minutes at which the custom check is run.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`task` |  `object (`[Task](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/Task)`)` Output only. The task that ran for this custom check.  
`latestBuild` |  `string` Output only. The resource name of the Cloud Build `Build` object that was used to execute the latest run of this custom action check. Format is `projects/{project}/locations/{location}/builds/{build}`.  
`failureCause` |  `enum (`[FailureCause](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns#FailureCause_4)`)` Output only. The reason the analysis failed. This will always be unspecified while the analysis is in progress or if it succeeded.  
`failureMessage` |  `string` Output only. Additional information about the analysis failure, if available.  
`metadata` |  `object (`[CustomMetadata](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/CustomMetadata)`)` Output only. Custom metadata provided by the user-defined custom check operation. result.  
  
## FailureCause

Well-known custom analysis check failures.

Enums  
---  
`FAILURE_CAUSE_UNSPECIFIED` | No reason for failure is specified.  
`CLOUD_BUILD_UNAVAILABLE` | Cloud Build is not available, either because it is not enabled or because Cloud Deploy has insufficient permissions. See [required permission](https://cloud.google.com/deploy/docs/cloud-deploy-service-account#required_permissions).  
`EXECUTION_FAILED` | The analysis operation did not complete successfully; check Cloud Build logs.  
`DEADLINE_EXCEEDED` | The analysis job run did not complete within the alloted time defined in the target's execution environment configuration.  
`CLOUD_BUILD_REQUEST_FAILED` | Cloud Build failed to fulfill Cloud Deploy's request. See failureMessage for additional details.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns/get)`

|  Gets details of a single JobRun.  
  
### `[list](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns/list)`

|  Lists JobRuns in a given project and location.  
  
### `[terminate](https://docs.cloud.google.com/deploy/docs/api/reference/rest/v1/projects.locations.deliveryPipelines.releases.rollouts.jobRuns/terminate)`

|  Terminates a Job Run in a given project and location.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-06-02 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-06-02 UTC."],[],[]] 
