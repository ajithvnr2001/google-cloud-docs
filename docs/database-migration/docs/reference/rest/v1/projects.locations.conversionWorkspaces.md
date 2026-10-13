---
url: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces
title: REST Resource: projects.locations.conversionWorkspaces \u00a0|\u00a0 Database Migration Service \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T14:00:30.182040+00:00
---

# REST Resource: projects.locations.conversionWorkspaces  |  Database Migration Service  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Databases ](https://docs.cloud.google.com/docs/databases)
  * [ Database Migration Service ](https://docs.cloud.google.com/database-migration/docs)
  * [ APIs and reference ](https://docs.cloud.google.com/database-migration/docs/reference/mcp)



Send feedback 

#  REST Resource: projects.locations.conversionWorkspaces Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: ConversionWorkspace
    * JSON representation
  * DatabaseEngineInfo
    * JSON representation
  * Methods



## Resource: ConversionWorkspace

The main conversion workspace resource entity.

JSON representation  
---  
      
    
    {
      "name": string,
      "source": {
        object ([DatabaseEngineInfo](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces#DatabaseEngineInfo))
      },
      "destination": {
        object ([DatabaseEngineInfo](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces#DatabaseEngineInfo))
      },
      "globalSettings": {
        string: string,
        ...
      },
      "hasUncommittedChanges": boolean,
      "latestCommitId": string,
      "latestCommitTime": string,
      "createTime": string,
      "updateTime": string,
      "displayName": string,
      "destinationProvider": enum ([DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider)),
      "sourceProvider": enum ([DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider))
    }  
  
Fields  
---  
`name` |  `string` Full name of the workspace resource, in the form of: projects/{project}/locations/{location}/conversionWorkspaces/{conversionWorkspace}.  
`source` |  `object (`[DatabaseEngineInfo](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces#DatabaseEngineInfo)`)` Required. The source engine details.  
`destination` |  `object (`[DatabaseEngineInfo](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces#DatabaseEngineInfo)`)` Required. The destination engine details.  
`globalSettings` |  `map (key: string, value: string)` Optional. A generic list of settings for the workspace. The settings are database pair dependant and can indicate default behavior for the mapping rules engine or turn on or off specific features. Such examples can be: convert_foreign_key_to_interleave=true, skip_triggers=false, ignore_non_table_synonyms=trueAn object containing a list of `"key": value` pairs. Example: `{ "name": "wrench", "mass": "1.3kg", "count": "3" }`.  
`hasUncommittedChanges` |  `boolean` Output only. Whether the workspace has uncommitted changes (changes which were made after the workspace was committed).  
`latestCommitId` |  `string` Output only. The latest commit ID.  
`latestCommitTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the workspace was committed.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the workspace resource was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp when the workspace resource was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`displayName` |  `string` Optional. The display name for the workspace.  
`destinationProvider` |  `enum (`[DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider)`)` Optional. The provider for the destination database.  
`sourceProvider` |  `enum (`[DatabaseProvider](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseProvider)`)` Optional. The provider for the source database.  
  
## DatabaseEngineInfo

The type and version of a source or destination database.

JSON representation  
---  
      
    
    {
      "engine": enum ([DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseEngine)),
      "version": string
    }  
  
Fields  
---  
`engine` |  `enum (`[DatabaseEngine](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/DatabaseEngine)`)` Required. Engine type.  
`version` |  `string` Required. Engine version, for example "12.c.1".  
  
## Methods  
  
---  
  
### `[apply](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/apply)`

|  Applies draft tree onto a specific destination database.  
  
### `[commit](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/commit)`

|  Marks all the data in the conversion workspace as committed.  
  
### `[convert](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/convert)`

|  Creates a draft tree schema for the destination database.  
  
### `[create](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/create)`

|  Creates a new conversion workspace in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/delete)`

|  Deletes a single conversion workspace.  
  
### `[describeConversionWorkspaceRevisions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeConversionWorkspaceRevisions)`

|  Retrieves a list of committed revisions of a specific conversion workspace.  
  
### `[describeDatabaseEntities](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/describeDatabaseEntities)`

|  Describes the database entities tree for a specific conversion workspace and a specific tree type.  
  
### `[get](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/get)`

|  Gets details of a single conversion workspace.  
  
### `[getIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[list](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/list)`

|  Lists conversion workspaces in a given project and location.  
  
### `[patch](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/patch)`

|  Updates the parameters of a single conversion workspace.  
  
### `[rollback](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/rollback)`

|  Rolls back a conversion workspace to the last committed snapshot.  
  
### `[searchBackgroundJobs](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/searchBackgroundJobs)`

|  Searches/lists the background jobs for a specific conversion workspace.  
  
### `[seed](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/seed)`

|  Imports a snapshot of the source database into the conversion workspace.  
  
### `[setIamPolicy](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/database-migration/docs/reference/rest/v1/projects.locations.conversionWorkspaces/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-26 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-26 UTC."],[],[]] 
