---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs
title: REST Resource: projects.locations.sources.migratingVms.cloneJobs \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:34.275820+00:00
---

# REST Resource: projects.locations.sources.migratingVms.cloneJobs  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.sources.migratingVms.cloneJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CloneJob
    * JSON representation
    * State
    * CloneStep
      * JSON representation
  * Methods



## Resource: CloneJob

CloneJob describes the process of creating a clone of a `[MigratingVM](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms#MigratingVm)` to the requested target based on the latest successful uploaded snapshots. While the migration cycles of a MigratingVm take place, it is possible to verify the uploaded VM can be started in the cloud, by creating a clone. The clone can be created without any downtime, and it is created using the latest snapshots which are already in the cloud. The cloneJob is only responsible for its work, not its products, which means once it is finished, it will never touch the instance it created. It will only delete it in case of the CloneJob being cancelled or upon failure to clone.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "endTime": string,
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs#CloneJob.State)),
      "stateTime": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status))
      },
      "steps": [
        {
          object ([CloneStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs#CloneJob.CloneStep))
        }
      ],
    
      // Union field target_vm_details can be only one of the following:
      "computeEngineTargetDetails": {
        object ([ComputeEngineTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineTargetDetails))
      },
      "computeEngineDisksTargetDetails": {
        object ([ComputeEngineDisksTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails))
      }
      // End of list of possible types for union field target_vm_details.
    }  
  
Fields  
---  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the clone job was created (as an API call, not when it was actually created in the target).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the clone job was ended.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`name` |  `string` Output only. The name of the clone.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs#CloneJob.State)`)` Output only. State of the clone job.  
`stateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the state was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status)`)` Output only. Provides details for the errors that led to the Clone Job's state.  
`steps[]` |  `object (`[CloneStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs#CloneJob.CloneStep)`)` Output only. The clone steps list representing its progress.  
Union field `target_vm_details`. Details of the VM to create as the target of this clone job. `target_vm_details` can be only one of the following:  
`computeEngineTargetDetails` |  `object (`[ComputeEngineTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineTargetDetails)`)` Output only. Details of the target VM in Compute Engine.  
`computeEngineDisksTargetDetails` |  `object (`[ComputeEngineDisksTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails)`)` Output only. Details of the target Persistent Disks in Compute Engine.  
  
### State

Possible states of the clone job.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown. This is used for API compatibility only and is not used by the system.  
`PENDING` | The clone job has not yet started.  
`ACTIVE` | The clone job is active and running.  
`FAILED` | The clone job finished with errors.  
`SUCCEEDED` | The clone job finished successfully.  
`CANCELLED` | The clone job was cancelled.  
`CANCELLING` | The clone job is being cancelled.  
`ADAPTING_OS` | OS adaptation is running as part of the clone job to generate license.  
  
### CloneStep

CloneStep holds information about the clone step progress.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
    
      // Union field step can be only one of the following:
      "adaptingOs": {
        object ([AdaptingOSStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/AdaptingOSStep))
      },
      "preparingVmDisks": {
        object ([PreparingVMDisksStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/PreparingVMDisksStep))
      },
      "instantiatingMigratedVm": {
        object ([InstantiatingMigratedVMStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/InstantiatingMigratedVMStep))
      }
      // End of list of possible types for union field step.
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the step has started.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the step has ended.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
Union field `step`.`step` can be only one of the following:  
`adaptingOs` |  `object (`[AdaptingOSStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/AdaptingOSStep)`)` Adapting OS step.  
`preparingVmDisks` |  `object (`[PreparingVMDisksStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/PreparingVMDisksStep)`)` Preparing VM disks step.  
`instantiatingMigratedVm` |  `object (`[InstantiatingMigratedVMStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/InstantiatingMigratedVMStep)`)` Instantiating migrated VM step.  
  
## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs/cancel)`

|  Initiates the cancellation of a running clone job.  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs/create)`

|  Initiates a Clone of a specific migrating VM.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs/get)`

|  Gets details of a single CloneJob.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cloneJobs/list)`

|  Lists the CloneJobs of a migrating VM.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
