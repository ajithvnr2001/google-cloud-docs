---
url: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces
title: REST Resource: projects.locations.repositories.workspaces \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:08.338647+00:00
---

# REST Resource: projects.locations.repositories.workspaces  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.repositories.workspaces Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Workspace
    * JSON representation
  * Methods



## Resource: Workspace

Represents a Dataform Git workspace.

JSON representation  
---  
      
    
    {
      "name": string,
      "createTime": string,
      "dataEncryptionState": {
        object ([DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1/DataEncryptionState))
      },
      "privateResourceMetadata": {
        object ([PrivateResourceMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1/PrivateResourceMetadata))
      },
      "internalMetadata": string,
      "disableMoves": boolean
    }  
  
Fields  
---  
`name` |  `string` Identifier. The workspace's name.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the workspace was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`dataEncryptionState` |  `object (`[DataEncryptionState](https://docs.cloud.google.com/dataform/reference/rest/v1/DataEncryptionState)`)` Output only. A data encryption state of a Git repository if this Workspace is protected by a KMS key.  
`privateResourceMetadata` |  `object (`[PrivateResourceMetadata](https://docs.cloud.google.com/dataform/reference/rest/v1/PrivateResourceMetadata)`)` Output only. Metadata indicating whether this resource is user-scoped. For `Workspace` resources, the `userScoped` field is always `true`.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
`disableMoves` |  `boolean` Optional. If set to true, workspaces will not be moved if its linked Repository is moved. Instead, it will be deleted.  
  
## Methods  
  
---  
  
### `[commit](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/commit)`

|  Applies a Git commit for uncommitted files in a Workspace.  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/create)`

|  Creates a new Workspace in a given Repository.  
  
### `[delete](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/delete)`

|  Deletes a single Workspace.  
  
### `[fetchFileDiff](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/fetchFileDiff)`

|  Fetches Git diff for an uncommitted file in a Workspace.  
  
### `[fetchFileGitStatuses](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/fetchFileGitStatuses)`

|  Fetches Git statuses for the files in a Workspace.  
  
### `[fetchGitAheadBehind](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/fetchGitAheadBehind)`

|  Fetches Git ahead/behind against a remote branch.  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/get)`

|  Fetches a single Workspace.  
  
### `[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[installNpmPackages](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/installNpmPackages)`

|  Installs dependency NPM packages (inside a Workspace).  
  
### `[list](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/list)`

|  Lists Workspaces in a given Repository.  
  
### `[makeDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/makeDirectory)`

|  Creates a directory inside a Workspace.  
  
### `[moveDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/moveDirectory)`

|  Moves a directory (inside a Workspace), and all of its contents, to a new location.  
  
### `[moveFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/moveFile)`

|  Moves a file (inside a Workspace) to a new location.  
  
### `[pull](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/pull)`

|  Pulls Git commits from the Repository's remote into a Workspace.  
  
### `[push](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/push)`

|  Pushes Git commits from a Workspace to the Repository's remote.  
  
### `[queryDirectoryContents](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/queryDirectoryContents)`

|  Returns the contents of a given Workspace directory.  
  
### `[readFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/readFile)`

|  Returns the contents of a file (inside a Workspace).  
  
### `[removeDirectory](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/removeDirectory)`

|  Deletes a directory (inside a Workspace) and all of its contents.  
  
### `[removeFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/removeFile)`

|  Deletes a file (inside a Workspace).  
  
### `[reset](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/reset)`

|  Performs a Git reset for uncommitted files in a Workspace.  
  
### `[searchFiles](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/searchFiles)`

|  Finds the contents of a given Workspace directory by filter.  
  
### `[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
### `[writeFile](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories.workspaces/writeFile)`

|  Writes to a file (inside a Workspace).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]] 
