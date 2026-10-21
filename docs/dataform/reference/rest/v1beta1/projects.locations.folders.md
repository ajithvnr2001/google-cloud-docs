---
url: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders
title: REST Resource: projects.locations.folders \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T00:42:15.708756+00:00
---

# REST Resource: projects.locations.folders  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders

  * [ Home ](https://docs.cloud.google.com/)
  * [ Dataform ](https://docs.cloud.google.com/dataform)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  REST Resource: projects.locations.folders Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Folder
    * JSON representation
  * Methods



## Resource: Folder

Represents a Dataform Folder. This is a resource that is used to organize Files and other Folders and provide hierarchical access controls.

JSON representation  
---  
      
    
    {
      "name": string,
      "displayName": string,
      "containingFolder": string,
      "teamFolderName": string,
      "createTime": string,
      "updateTime": string,
      "internalMetadata": string,
      "creatorIamPrincipal": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The Folder's name.  
`displayName` |  `string` Required. The Folder's user-friendly name.  
`containingFolder` |  `string` Optional. The containing Folder resource name. This should take the format: projects/{project}/locations/{location}/folders/{folder}, projects/{project}/locations/{location}/teamFolders/{teamFolder}, or just "" if this is a root Folder. This field can only be updated through folders.move.  
`teamFolderName` |  `string` Output only. The resource name of the TeamFolder that this Folder is associated with. This should take the format: projects/{project}/locations/{location}/teamFolders/{teamFolder}. If this is not set, the Folder is not associated with a TeamFolder and is a UserFolder.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the Folder was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The timestamp of when the Folder was last updated.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`internalMetadata` |  `string` Output only. All the metadata information that is used internally to serve the resource. For example: timestamps, flags, status fields, etc. The format of this field is a JSON string.  
`creatorIamPrincipal` |  `string` Output only. The IAM principal identifier of the creator of the Folder.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/create)`

|  Creates a new Folder in a given project and location.  
  
### `[delete](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/delete)`

|  Deletes a single Folder.  
  
### `[deleteTree](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/deleteTree)`

|  Deletes a Folder with its contents (Folders, Repositories, Workspaces, ReleaseConfigs, and WorkflowConfigs).  
  
### `[get](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/get)`

|  Fetches a single Folder.  
  
### `[getIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/getIamPolicy)`

|  Gets the access control policy for a resource.  
  
### `[move](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/move)`

|  Moves a Folder to a new Folder, TeamFolder, or the root location.  
  
### `[patch](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/patch)`

|  Updates a single Folder.  
  
### `[queryFolderContents](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/queryFolderContents)`

|  Returns the contents of a given Folder.  
  
### `[setIamPolicy](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/setIamPolicy)`

|  Sets the access control policy on the specified resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/dataform/reference/rest/v1beta1/projects.locations.folders/testIamPermissions)`

|  Returns permissions that a caller has on the specified resource.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-04-01 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-04-01 UTC."],[],[]] 
