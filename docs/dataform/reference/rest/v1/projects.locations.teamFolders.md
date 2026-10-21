---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders
title: REST Resource: projects.locations.teamFolders \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:12.336901+00:00
---

# REST Resource: projects.locations.teamFolders  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.teamFolders Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: TeamFolder
    * JSON representation
  * Methods



## Resource: TeamFolder

Represents a Dataform TeamFolder. This is a resource that sits at the project level and is used to organize Repositories and Folders with hierarchical access controls. They provide a team context and stricter access controls.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "internalMetadata": string,
      "creatorIamPrincipal": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The TeamFolder's name.  
`displayName` |  `string` Required. The TeamFolder's user-friendly name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the TeamFolder was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the TeamFolder was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
`creatorIamPrincipal` |  `string` Output only. The IAM principal identifier of the creator of the TeamFolder.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/create)`

|  Creates a new TeamFolder in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/delete)`

|  Deletes a single TeamFolder.  
  
### `[deleteTree](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/deleteTree)`

|  Deletes a TeamFolder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/get)`

|  Fetches a single TeamFolder.  
  
### `[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[patch](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/patch)`

|  Updates a single TeamFolder.  
  
### `[queryContents](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/queryContents)`

|  Returns the contents of a given TeamFolder.  
  
### `[search](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/search)`

|  Returns all TeamFolders in a given location that the caller has access to and match the provided filter.  
  
### `[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]] 
