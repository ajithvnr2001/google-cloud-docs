---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects
title: REST Resource: projects.locations.migrationJobs.objects \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:38.868403+00:00
---

# REST Resource: projects.locations.migrationJobs.objects  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  REST Resource: projects.locations.migrationJobs.objects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MigrationJobObject
    * JSON representation
  * State
  * Phase
  * HeterogeneousMetadata
    * JSON representation
  * Methods



## Resource: MigrationJobObject

A specific Migration Job Object (e.g. a specifc DB Table)

JSON representation  
---  
      
    
    {
      "name": string,
      "sourceObject": {
        object ([SourceObjectIdentifier](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier))
      },
      "error": {
        object ([Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#State)),
      "phase": enum ([Phase](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#Phase)),
      "createTime": string,
      "updateTime": string,
      "heterogeneousMetadata": {
        object ([HeterogeneousMetadata](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#HeterogeneousMetadata))
      }
    }  
  
Fields  
---  
`name` |  `string` The object's name.  
`sourceObject` |  `object (`[SourceObjectIdentifier](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/SourceObjectIdentifier)`)` The object identifier in the data source.  
`error` |  `object (`[Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The error details in case of failure.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#State)`)` The state of the migration job object.  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#Phase)`)` Output only. The phase of the migration job object.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The creation time of the migration job object.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The last update time of the migration job object.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`heterogeneousMetadata` |  `object (`[HeterogeneousMetadata](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects#HeterogeneousMetadata)`)` Output only. Metadata for heterogeneous migration jobs objects.  
  
## State

The migration job object states. LINT.IfChange

Enums  
---  
`STATE_UNSPECIFIED` | The state of the migration job object is unknown.  
`NOT_STARTED` | The migration job object is not started.  
`RUNNING` | The migration job object is running.  
`STOPPING` | The migration job object is being stopped.  
`STOPPED` | The migration job object is currently stopped.  
`RESTARTING` | The migration job object is restarting.  
`FAILED` | The migration job object failed.  
`REMOVING` | The migration job object is deleting.  
`NOT_SELECTED` | The migration job object is not selected for migration.  
`COMPLETED` | The migration job object is completed.  
  
## Phase

The migration job object phases.

Enums  
---  
`PHASE_UNSPECIFIED` | The phase of the migration job is unknown.  
`FULL_DUMP` | The migration job object is in the full dump phase.  
`CDC` | The migration job object is in CDC phase.  
`READY_FOR_PROMOTE` | The migration job object is ready to be promoted.  
`PROMOTE_IN_PROGRESS` | The migration job object is in running the promote phase.  
`PROMOTED` | The migration job is promoted.  
`DIFF_BACKUP` | The migration job object is in the differential backup phase.  
`CREATING_BACKUP` | The migration job object is creating a fully managed backup of the source.  
`RESTORING_BACKUP` | The migration job object is restoring a fully managed backup to the destination.  
  
## HeterogeneousMetadata

Metadata for heterogeneous migration jobs objects.

JSON representation  
---  
      
    
    {
      "unsupportedEventsCount": string
    }  
  
Fields  
---  
`unsupportedEventsCount` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number of unsupported events.  
  
## Methods  
  
---  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/get)`

|  Use this method to get details about a migration job object.  
  
### `[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/list)`

|  Use this method to list the objects of a specific migration job.  
  
### `[lookup](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/lookup)`

|  Use this method to look up a migration job object by its source object identifier.  
  
### `[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.migrationJobs.objects/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-07-06 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-07-06 UTC."],[],[]] 
