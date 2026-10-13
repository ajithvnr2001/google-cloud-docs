---
url: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs
title: REST Resource: projects.patchJobs \u00a0|\u00a0 Compute Engine \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T19:01:31.207479+00:00
---

# REST Resource: projects.patchJobs  |  Compute Engine  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Compute ](https://docs.cloud.google.com/docs/compute-area)
  * [ Compute Engine ](https://docs.cloud.google.com/compute/docs)
  * [ APIs & Reference ](https://docs.cloud.google.com/compute/docs/apis)



Send feedback 

#  REST Resource: projects.patchJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: PatchJob
    * JSON representation
  * State
  * InstanceDetailsSummary
    * JSON representation
  * Methods



## Resource: PatchJob

A high level representation of a patch job that is either in progress or has completed.

Instance details are not included in the job. To paginate through instance details, use `ListPatchJobInstanceDetails`.

For more information about patch jobs, see [Creating patch jobs](https://cloud.google.com/compute/docs/os-patch-management/create-patch-job).

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "description": string,
      "createTime": string,
      "updateTime": string,
      "state": enum ([State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs#State)),
      "instanceFilter": {
        object ([PatchInstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter))
      },
      "patchConfig": {
        object ([PatchConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig))
      },
      "duration": string,
      "instanceDetailsSummary": {
        object ([InstanceDetailsSummary](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs#InstanceDetailsSummary))
      },
      "dryRun": boolean,
      "errorMessage": string,
      "percentComplete": number,
      "patchDeployment": string,
      "rollout": {
        object ([PatchRollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchRollout))
      }
    }  
  
Fields  
---  
`name` |  `string` Unique identifier for this patch job in the form `projects/*/patchJobs/*`  
`displayName` |  `string` Display name for this patch job. This is not a unique identifier.  
`description` |  `string` Description of the patch job. Length of the description is limited to 1024 characters.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Time this patch job was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Last time this patch job was updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs#State)`)` The current state of the PatchJob.  
`instanceFilter` |  `object (`[PatchInstanceFilter](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchInstanceFilter)`)` Instances to patch.  
`patchConfig` |  `object (`[PatchConfig](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchConfig)`)` Patch configuration being applied.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Duration of the patch job. After the duration ends, the patch job times out.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`instanceDetailsSummary` |  `object (`[InstanceDetailsSummary](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs#InstanceDetailsSummary)`)` Summary of instance details.  
`dryRun` |  `boolean` If this patch job is a dry run, the agent reports that it has finished without running any updates on the VM instance.  
`errorMessage` |  `string` If this patch job failed, this message provides information about the failure.  
`percentComplete` |  `number` Reflects the overall progress of the patch job in the range of 0.0 being no progress to 100.0 being complete.  
`patchDeployment` |  `string` Output only. Name of the patch deployment that created this patch job.  
`rollout` |  `object (`[PatchRollout](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/PatchRollout)`)` Rollout strategy being applied.  
  
## State

Enumeration of the various states a patch job passes through as it executes.

Enums  
---  
`STATE_UNSPECIFIED` | State must be specified.  
`STARTED` | The patch job was successfully initiated.  
`INSTANCE_LOOKUP` | The patch job is looking up instances to run the patch on.  
`PATCHING` | Instances are being patched.  
`SUCCEEDED` | Patch job completed successfully.  
`COMPLETED_WITH_INACTIVE_VMS` | The patch job completed without errors, but some instances were inactive and therefore not patched.  
`COMPLETED_WITH_ERRORS` | Patch job completed but there were errors.  
`CANCELED` | The patch job was canceled.  
`TIMED_OUT` | The patch job timed out.  
  
## InstanceDetailsSummary

A summary of the current patch state across all instances that this patch job affects. Contains counts of instances in different states. These states map to `InstancePatchState`. List patch job instance details to see the specific states of each instance.

JSON representation  
---  
      
    
    {
      "pendingInstanceCount": string,
      "inactiveInstanceCount": string,
      "notifiedInstanceCount": string,
      "startedInstanceCount": string,
      "downloadingPatchesInstanceCount": string,
      "applyingPatchesInstanceCount": string,
      "rebootingInstanceCount": string,
      "succeededInstanceCount": string,
      "succeededRebootRequiredInstanceCount": string,
      "failedInstanceCount": string,
      "ackedInstanceCount": string,
      "timedOutInstanceCount": string,
      "prePatchStepInstanceCount": string,
      "postPatchStepInstanceCount": string,
      "noAgentDetectedInstanceCount": string,
      "skippedInstanceCount": string
    }  
  
Fields  
---  
`pendingInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances pending patch job.  
`inactiveInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that are inactive.  
`notifiedInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances notified about patch job.  
`startedInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that have started.  
`downloadingPatchesInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that are downloading patches.  
`applyingPatchesInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that are applying patches.  
`rebootingInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances rebooting.  
`succeededInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that have completed successfully.  
`succeededRebootRequiredInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that require reboot.  
`failedInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that failed.  
`ackedInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that have acked and will start shortly.  
`timedOutInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that exceeded the time out while applying the patch.  
`prePatchStepInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that are running the pre-patch step.  
`postPatchStepInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that are running the post-patch step.  
`noAgentDetectedInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that do not appear to be running the agent. Check to ensure that the agent is installed, running, and able to communicate with the service.  
`skippedInstanceCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Number of instances that were skipped during patching.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/cancel)`

|  Cancel a patch job.  
  
### `[execute](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/execute)`

|  Patch VM instances by creating and running a patch job.  
  
### `[get](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/get)`

|  Get the patch job.  
  
### `[list](https://docs.cloud.google.com/compute/docs/osconfig/rest/v1/projects.patchJobs/list)`

|  Get a list of patch jobs.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-11-17 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-11-17 UTC."],[],[]] 
