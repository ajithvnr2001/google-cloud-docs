---
url: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups
title: REST Resource: projects.locations.groups \u00a0|\u00a0 Migrate to Virtual Machines \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:37:31.157152+00:00
---

# REST Resource: projects.locations.groups  |  Migrate to Virtual Machines  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Migration ](https://docs.cloud.google.com/docs/migration)
  * [ Migrate to Virtual Machines ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0)
  * [ Reference ](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference)



Send feedback 

#  REST Resource: projects.locations.groups Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Group
    * JSON representation
  * MigrationTargetType
  * Methods



## Resource: Group

Describes message for 'Group' resource. The Group is a collections of several MigratingVms.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "updateTime": string,
      "description": string,
      "displayName": string,
      "migrationTargetType": enum ([MigrationTargetType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups#MigrationTargetType))
    }  
  
Fields  
---  
`name` |  `string` Output only. The Group name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The create time timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The update time timestamp.A timestamp in RFC3339 UTC "Zulu" format, with nanosecond resolution and up to nine fractional digits. Examples: `"2014-10-02T15:01:23Z"` and `"2014-10-02T15:01:23.045123456Z"`.  
`description` |  `string` User-provided description of the group.  
`displayName` |  `string` Display name is a user defined name for this group which can be updated.  
`migrationTargetType` |  `enum (`[MigrationTargetType](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups#MigrationTargetType)`)` Immutable. The target type of this group.  
  
## MigrationTargetType

The possible types of the group.

Enums  
---  
`MIGRATION_TARGET_TYPE_UNSPECIFIED` | Group type is not specified. This defaults to Compute Engine targets.  
`MIGRATION_TARGET_TYPE_GCE` | All MigratingVMs in the group must have Compute Engine targets.  
`MIGRATION_TARGET_TYPE_DISKS` | All MigratingVMs in the group must have Compute Engine Disks targets.  
  
## Methods  
  
---  
  
### `[addGroupMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups/addGroupMigration)`

|  Adds a MigratingVm to a Group.  
  
### `[create](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups/create)`

|  Creates a new Group in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups/delete)`

|  Deletes a single Group.  
  
### `[get](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups/get)`

|  Gets details of a single Group.  
  
### `[list](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups/list)`

|  Lists Groups in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups/patch)`

|  Updates the parameters of a single Group.  
  
### `[removeGroupMigration](https://docs.cloud.google.com/migrate/virtual-machines/docs/5.0/reference/rest/v1/projects.locations.groups/removeGroupMigration)`

|  Removes a MigratingVm from a Group.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2025-07-28 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2025-07-28 UTC."],[],[]] 
