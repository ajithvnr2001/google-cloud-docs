---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles
title: REST Resource: projects.locations.sources.migratingVms.replicationCycles \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:35.361315+00:00
---

# REST Resource: projects.locations.sources.migratingVms.replicationCycles  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.sources.migratingVms.replicationCycles Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ReplicationCycle
    * JSON representation
    * CycleStep
      * JSON representation
    * InitializingReplicationStep
    * ReplicatingStep
      * JSON representation
    * PostProcessingStep
    * State
  * Methods



## Resource: ReplicationCycle

ReplicationCycle contains information about the current replication cycle status.

JSON representation  
---  
      
    
    {
      "name": string,
      "cycleNumber": integer,
      "startTime": string,
      "endTime": string,
      "totalPauseDuration": string,
      "progressPercent": integer,
      "steps": [
        {
          object ([CycleStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.CycleStep))
        }
      ],
      "state": enum ([State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.State)),
      "error": {
        object ([Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status))
      },
      "warnings": [
        {
          object ([MigrationWarning](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/MigrationWarning))
        }
      ]
    }  
  
Fields  
---  
`name` |  `string` The identifier of the ReplicationCycle.  
`cycleNumber` |  `integer` The cycle's ordinal number.  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the replication cycle has started.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the replication cycle has ended.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`totalPauseDuration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` The accumulated duration the replication cycle was paused.A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`progressPercent  
**(deprecated)**` |  `integer` This item is deprecated!The current progress in percentage of this cycle. Was replaced by 'steps' field, which breaks down the cycle progression more accurately.  
`steps[]` |  `object (`[CycleStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.CycleStep)`)` The cycle's steps list representing its progress.  
`state` |  `enum (`[State](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.State)`)` State of the ReplicationCycle.  
`error` |  `object (`[Status](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/Status)`)` Output only. Provides details on the state of the cycle in case of an error.  
`warnings[]` |  `object (`[MigrationWarning](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/MigrationWarning)`)` Output only. Warnings that occurred during the cycle.  
  
### CycleStep

CycleStep holds information about a step progress.

JSON representation  
---  
      
    
    {
      "startTime": string,
      "endTime": string,
    
      // Union field step can be only one of the following:
      "initializingReplication": {
        object ([InitializingReplicationStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.InitializingReplicationStep))
      },
      "replicating": {
        object ([ReplicatingStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.ReplicatingStep))
      },
      "postProcessing": {
        object ([PostProcessingStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.PostProcessingStep))
      }
      // End of list of possible types for union field step.
    }  
  
Fields  
---  
`startTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the cycle step has started.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` The time the cycle step has ended.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
Union field `step`.`step` can be only one of the following:  
`initializingReplication` |  `object (`[InitializingReplicationStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.InitializingReplicationStep)`)` Initializing replication step.  
`replicating` |  `object (`[ReplicatingStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.ReplicatingStep)`)` Replicating step.  
`postProcessing` |  `object (`[PostProcessingStep](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles#ReplicationCycle.PostProcessingStep)`)` Post processing step.  
  
### InitializingReplicationStep

This type has no fields.

InitializingReplicationStep contains specific step details.

### ReplicatingStep

ReplicatingStep contains specific step details.

JSON representation  
---  
      
    
    {
      "totalBytes": string,
      "replicatedBytes": string,
      "lastTwoMinutesAverageBytesPerSecond": string,
      "lastThirtyMinutesAverageBytesPerSecond": string
    }  
  
Fields  
---  
`totalBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Total bytes to be handled in the step.  
`replicatedBytes` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` Replicated bytes in the step.  
`lastTwoMinutesAverageBytesPerSecond` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The source disks replication rate for the last 2 minutes in bytes per second.  
`lastThirtyMinutesAverageBytesPerSecond` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The source disks replication rate for the last 30 minutes in bytes per second.  
  
### PostProcessingStep

This type has no fields.

PostProcessingStep contains specific step details.

### State

Possible states of a replication cycle.

Enums  
---  
`STATE_UNSPECIFIED` | The state is unknown. This is used for API compatibility only and is not used by the system.  
`RUNNING` | The replication cycle is running.  
`PAUSED` | The replication cycle is paused.  
`FAILED` | The replication cycle finished with errors.  
`SUCCEEDED` | The replication cycle finished successfully.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles/get)`

|  Gets details of a single ReplicationCycle.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.sources.migratingVms.replicationCycles/list)`

|  Lists ReplicationCycles in a given MigratingVM.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
