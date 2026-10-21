---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs
title: REST Resource: projects.locations.sources.migratingVms.cutoverJobs \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:34.722372+00:00
---

# REST Resource: projects.locations.sources.migratingVms.cutoverJobs  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.sources.migratingVms.cutoverJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: CutoverJob
    * JSON representation
    * State
    * CutoverStep
      * JSON representation
    * ShuttingDownSourceVMStep
  * Methods



## Resource: CutoverJob

CutoverJob message describes a cutover of a migrating VM. The CutoverJob is the operation of shutting down the VM, creating a snapshot and clonning the VM using the replicated snapshot.

JSON representation  
---  
      
    
    {
      "createTime": string,
      "endTime": string,
      "name": string,
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob.State)),
      "stateTime": string,
      "progressPercent": integer,
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status))
      },
      "stateMessage": string,
      "steps": [
        {
          object ([CutoverStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob.CutoverStep))
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
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the cutover job was created (as an API call, not when it was actually created in the target).A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the cutover job had finished.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`name` |  `string` Output only. The name of the cutover job.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob.State)`)` Output only. State of the cutover job.  
`stateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time the state was last updated.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`progressPercent` |  `integer` Output only. The current progress in percentage of the cutover job.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status)`)` Output only. Provides details for the errors that led to the Cutover Job's state.  
`stateMessage` |  `string` Output only. A message providing possible extra details about the current state.  
`steps[]` |  `object (`[CutoverStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob.CutoverStep)`)` Output only. The cutover steps list representing its progress.  
Union field `target_vm_details`. Details of the VM to create as the target of this cutover job. `target_vm_details` can be only one of the following:  
`computeEngineTargetDetails` |  `object (`[ComputeEngineTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineTargetDetails)`)` Output only. Details of the target VM in Compute Engine.  
`computeEngineDisksTargetDetails` |  `object (`[ComputeEngineDisksTargetDetails](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/ComputeEngineDisksTargetDetails)`)` Output only. Details of the target Persistent Disks in Compute Engine.  
  
### State

Possible states of the cutover job.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown. This is used for API compatibility only and is not used by the system.  
`PENDING` | The cutover job has not yet started.  
`FAILED` | The cutover job finished with errors.  
`SUCCEEDED` | The cutover job finished successfully.  
`CANCELLED` | The cutover job was cancelled.  
`CANCELLING` | The cutover job is being cancelled.  
`ACTIVE` | The cutover job is active and running.  
`ADAPTING_OS` | OS adaptation is running as part of the cutover job to generate license.  
  
### CutoverStep

CutoverStep holds information about the cutover step progress.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
    
      // Union field step can be only one of the following:
      "previousReplicationCycle": {
        object ([ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle))
      },
      "shuttingDownSourceVm": {
        object ([ShuttingDownSourceVMStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob.ShuttingDownSourceVMStep))
      },
      "finalSync": {
        object ([ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle))
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
`previousReplicationCycle` |  `object (`[ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle)`)` A replication cycle prior cutover step.  
`shuttingDownSourceVm` |  `object (`[ShuttingDownSourceVMStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs#CutoverJob.ShuttingDownSourceVMStep)`)` Shutting down VM step.  
`finalSync` |  `object (`[ReplicationCycle](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle)`)` Final sync step.  
`preparingVmDisks` |  `object (`[PreparingVMDisksStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/PreparingVMDisksStep)`)` Preparing VM disks step.  
`instantiatingMigratedVm` |  `object (`[InstantiatingMigratedVMStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/InstantiatingMigratedVMStep)`)` Instantiating migrated VM step.  
  
### ShuttingDownSourceVMStep

This type has no fields.

ShuttingDownSourceVMStep contains specific step details.

## Methods  
  
---  
  
### `[cancel](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs/cancel)`

|  Initiates the cancellation of a running cutover job.  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs/create)`

|  Initiates a Cutover of a specific migrating VM.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs/get)`

|  Gets details of a single CutoverJob.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.cutoverJobs/list)`

|  Lists the CutoverJobs of a migrating VM.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
