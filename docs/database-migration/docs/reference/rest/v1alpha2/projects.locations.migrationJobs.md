---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs
title: REST Resource: projects.locations.migrationJobs \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:51.228543+00:00
---

# REST Resource: projects.locations.migrationJobs  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  REST Resource: projects.locations.migrationJobs Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: MigrationJob
    * JSON representation
  * State
  * Phase
  * Type
  * ReverseSshConnectivity
    * JSON representation
  * VpcPeeringConnectivity
    * JSON representation
  * StaticIpConnectivity
  * DatabaseType
    * JSON representation
  * DatabaseEngine
  * Methods



## Resource: MigrationJob

Represents a Database Migration Service migration job object.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "labels": {
        string: string,
        ...
      },
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#State)),
      "phase": enum ([Phase](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#Phase)),
      "type": enum ([Type](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#Type)),
      "dumpPath": string,
      "source": string,
      "destination": string,
      "duration": string,
      "error": {
        object ([Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status))
      },
      "sourceDatabase": {
        object ([DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#DatabaseType))
      },
      "destinationDatabase": {
        object ([DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#DatabaseType))
      },
      "endTime": string,
    
      // Union field connectivity can be only one of the following:
      "reverseSshConnectivity": {
        object ([ReverseSshConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#ReverseSshConnectivity))
      },
      "vpcPeeringConnectivity": {
        object ([VpcPeeringConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#VpcPeeringConnectivity))
      },
      "staticIpConnectivity": {
        object ([StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#StaticIpConnectivity))
      }
      // End of list of possible types for union field connectivity.
    }  
  
Fields  
---  
`name` |  `string` The name (URI) of this migration job resource, in the form of: projects/{project}/locations/{location}/migrationJobs/{migrationJob}.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the migration job resource was created. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the migration job resource was last updated. A timestamp in RFC3339 UTC "Zulu" format, accurate to nanoseconds. Example: "2014-10-02T15:01:23.045123456Z".Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The resource labels for migration job to use to annotate any related underlying resources such as Compute Engine VMs. An object containing a list of "key": "value" pairs.Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.An object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`displayName` |  `string` The migration job display name.  
`state` |  `enum (`[State](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#State)`)` The current migration job state.  
`phase` |  `enum (`[Phase](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#Phase)`)` Output only. The current migration job phase.  
`type` |  `enum (`[Type](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#Type)`)` Required. The migration job type.  
`dumpPath` |  `string` The path to the dump file in Google Cloud Storage, in the format: (gs://[BUCKET_NAME]/[OBJECT_NAME]).  
`source` |  `string` Required. The resource name (URI) of the source connection profile.  
`destination` |  `string` Required. The resource name (URI) of the destination connection profile.  
`duration` |  `string (`[Duration](https://protobuf.dev/reference/protobuf/google.protobuf/#duration)` format)` Output only. The duration of the migration job (in seconds). A duration in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s".A duration in seconds with up to nine fractional digits, ending with '`s`'. Example: `"3.5s"`.  
`error` |  `object (`[Status](https://docs.cloud.google.com/database-migration/docs/reference/rest/Shared.Types/ListOperationsResponse#Status)`)` Output only. The error details in case of state FAILED.  
`sourceDatabase` |  `object (`[DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#DatabaseType)`)` The database engine type and provider of the source.  
`destinationDatabase` |  `object (`[DatabaseType](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#DatabaseType)`)` The database engine type and provider of the destination.  
`endTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. If the migration job is completed, the time when it was completed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
Union field `connectivity`. The connectivity method. `connectivity` can be only one of the following:  
`reverseSshConnectivity` |  `object (`[ReverseSshConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#ReverseSshConnectivity)`)` The details needed to communicate to the source over Reverse SSH tunnel connectivity.  
`vpcPeeringConnectivity` |  `object (`[VpcPeeringConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#VpcPeeringConnectivity)`)` The details of the VPC network that the source database is located in.  
`staticIpConnectivity` |  `object (`[StaticIpConnectivity](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#StaticIpConnectivity)`)` static ip connectivity data (default, no additional details needed).  
  
## State

The current migration job states.

Enums  
---  
`STATE_UNSPECIFIED` | The state of the migration job is unknown.  
`MAINTENANCE` | The migration job is down for maintenance.  
`DRAFT` | The migration job is in draft mode and no resources are created.  
`CREATING` | The migration job is being created.  
`NOT_STARTED` | The migration job is created and not started.  
`RUNNING` | The migration job is running.  
`FAILED` | The migration job failed.  
`COMPLETED` | The migration job has been completed.  
`DELETING` | The migration job is being deleted.  
`STOPPING` | The migration job is being stopped.  
`STOPPED` | The migration job is currently stopped.  
`DELETED` | The migration job has been deleted.  
`UPDATING` | The migration job is being updated.  
`STARTING` | The migration job is starting.  
`RESTARTING` | The migration job is restarting.  
`RESUMING` | The migration job is resuming.  
  
## Phase

The current migration job phase.

Enums  
---  
`PHASE_UNSPECIFIED` | The phase of the migration job is unknown.  
`FULL_DUMP` | The migration job is in the full dump phase.  
`CDC` | The migration job is CDC phase.  
`PROMOTE_IN_PROGRESS` | The migration job is running the promote phase.  
`WAITING_FOR_SOURCE_WRITES_TO_STOP` | Only RDS flow - waiting for source writes to stop  
`PREPARING_THE_DUMP` | Only RDS flow - the sources writes stopped, waiting for dump to begin  
  
## Type

The type of migration job (one-time or continuous).

Enums  
---  
`TYPE_UNSPECIFIED` | The type of the migration job is unknown.  
`ONE_TIME` | The migration job is a one time migration.  
`CONTINUOUS` | The migration job is a continuous migration.  
  
## ReverseSshConnectivity

The details needed to configure a reverse SSH tunnel between the source and destination databases. These details will be used when calling the generateSshScript method (see <https://cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript>) to produce the script that will help set up the reverse SSH tunnel, and to set up the VPC peering between the Cloud SQL private network and the VPC.

JSON representation  
---  
      
    
    {
      "vmIp": string,
      "vmPort": integer,
      "vm": string,
      "vpc": string
    }  
  
Fields  
---  
`vmIp` |  `string` Required. The IP of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vmPort` |  `integer` Required. The forwarding port of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vm` |  `string` The name of the virtual machine (Compute Engine) used as the bastion server for the SSH tunnel.  
`vpc` |  `string` The name of the VPC to peer with the Cloud SQL private network.  
  
## VpcPeeringConnectivity

The details of the VPC where the source database is located in Google Cloud. We will use this information to set up the VPC peering connection between Cloud SQL and this VPC.

JSON representation  
---  
      
    
    {
      "vpc": string
    }  
  
Fields  
---  
`vpc` |  `string` The name of the VPC network to peer with the Cloud SQL private network.  
  
## StaticIpConnectivity

This type has no fields.

The source database will allow incoming connections from the destination database's public IP. You can retrieve the Cloud SQL instance's public IP from the Cloud SQL console or using Cloud SQL APIs. No additional configuration is required.

## DatabaseType

A message defining the database engine and provider.

JSON representation  
---  
      
    
    {
      "provider": enum ([DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/DatabaseProvider)),
      "engine": enum ([DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#DatabaseEngine))
    }  
  
Fields  
---  
`provider` |  `enum (`[DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/DatabaseProvider)`)` The database provider.  
`engine` |  `enum (`[DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs#DatabaseEngine)`)` The database engine.  
  
## DatabaseEngine

The database engine types.

Enums  
---  
`DATABASE_ENGINE_UNSPECIFIED` | The source database engine of the migration job is unknown.  
`MYSQL` | The source engine is MySQL.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/create)`

|  Creates a new migration job in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/delete)`

|  Deletes a single migration job.  
  
### `[generateSshScript](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/generateSshScript)`

|  Generate a SSH configuration script to configure the reverse SSH connectivity.  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/get)`

|  Gets details of a single migration job.  
  
### `[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/list)`

|  Lists migration jobs in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/patch)`

|  Updates the parameters of a single migration job.  
  
### `[promote](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/promote)`

|  Promote a migration job, stopping replication to the destination and promoting the destination to be a standalone database.  
  
### `[restart](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/restart)`

|  Restart a stopped or failed migration job, resetting the destination instance to its original state and starting the migration process from scratch.  
  
### `[resume](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/resume)`

|  Resume a migration job that is currently stopped and is resumable (was stopped during CDC phase).  
  
### `[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[start](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/start)`

|  Start an already created migration job.  
  
### `[stop](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/stop)`

|  Stops a running migration job.  
  
### `[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[verify](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1alpha2/projects.locations.migrationJobs/verify)`

|  Verify a migration job, making sure the destination can reach the source and that all configuration and prerequisites are met.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
