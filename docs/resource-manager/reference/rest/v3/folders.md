---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/
title: REST Resource: folders \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T21:25:17.208209+00:00
---

# REST Resource: folders  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: folders Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Folder
    * JSON representation
  * State
  * Methods



## Resource: Folder

A folder in an organization's resource hierarchy, used to organize that organization's resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "displayName": string,
      "state": enum ([State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#State)),
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "etag": string,
      "tags": {
        string: string,
        ...
      },
      "configuredCapabilities": [
        string
      ],
      "managementProject": string
    }  
  
Fields  
---  
`name` |  `string` Identifier. The resource name of the folder. Its format is `folders/{folder_id}`, for example: "folders/1234".  
`parent` |  `string` Required. The folder's parent's resource name. Updates to the folder's parent must be performed using `[folders.move](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/move#google.cloud.resourcemanager.v3.Folders.MoveFolder)`.  
`displayName` |  `string` The folder's display name. A folder's display name must be unique amongst its siblings. For example, no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters. This is captured by the regular expression: `[\p{L}\p{N}]([\p{L}\p{N}_- ]{0,28}[\p{L}\p{N}])?`.  
`state` |  `enum (`[State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders#State)`)` Output only. The lifecycle state of the folder. Updates to the state must be performed using `[folders.delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/delete#google.cloud.resourcemanager.v3.Folders.DeleteFolder)` and `[folders.undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/undelete#google.cloud.resourcemanager.v3.Folders.UndeleteFolder)`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the folder was created.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the folder was last modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the folder was requested to be deleted.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. A checksum computed by the server based on the current value of the folder resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this folder. Each item in the map must be expressed as " : ". For example: "123/environment" : "production", "123/costCenter" : "marketing"Note: Currently this field is in Preview.  
`configuredCapabilities[]` |  `string` Output only. Optional capabilities configured for this folder (via capabilities.patch API). Example: `folders/123/capabilities/app-management`.  
`managementProject` |  `string` Output only. Management Project associated with this folder (if app-management capability is enabled). Example: `projects/google-mp-123` OUTPUT ONLY.  
  
## State

Folder lifecycle states.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | The normal and active state.  
`DELETE_REQUESTED` | The folder has been marked for deletion by the user.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/create)`

|  Creates a folder in the resource hierarchy.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/delete)`

|  Requests deletion of a folder.  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/get)`

|  Retrieves a folder identified by the supplied resource name.  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/getIamPolicy)`

|  Gets the access control policy for a folder.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/list)`

|  Lists the folders that are direct descendants of supplied parent resource.  
  
### `[move](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/move)`

|  Moves a folder under a new resource parent.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/patch)`

|  Updates a folder, changing its `display_name`.  
  
### `[search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/search)`

|  Search for folders that match specific filter criteria.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/setIamPolicy)`

|  Sets the access control policy on a folder, replacing any existing policy.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/testIamPermissions)`

|  Returns permissions that a caller has on the specified folder.  
  
### `[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/undelete)`

|  Cancels the deletion request for a folder.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
