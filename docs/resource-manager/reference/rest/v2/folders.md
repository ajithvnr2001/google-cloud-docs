---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/
title: REST Resource: folders \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:23.709550+00:00
---

# REST Resource: folders  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: folders Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Folder
    * JSON representation
  * LifecycleState
  * Methods



## Resource: Folder

A Folder in an Organization's resource hierarchy, used to organize that Organization's resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "displayName": string,
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders#LifecycleState)),
      "createTime": string,
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
`name` |  `string` Output only. The resource name of the Folder. Its format is `folders/{folder_id}`, for example: "folders/1234".  
`parent` |  `string` Required. The Folder's parent's resource name. Updates to the folder's parent must be performed via `[folders.move](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/move#google.cloud.resourcemanager.v2.Folders.MoveFolder)`.  
`displayName` |  `string` The folder's display name. A folder's display name must be unique amongst its siblings, e.g. no two folders with the same parent can share the same display name. The display name must start and end with a letter or digit, may contain letters, digits, spaces, hyphens and underscores and can be no longer than 30 characters. This is captured by the regular expression: `[\p{L}\p{N}]([\p{L}\p{N}_- ]{0,28}[\p{L}\p{N}])?`.  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders#LifecycleState)`)` Output only. The lifecycle state of the folder. Updates to the lifecycleState must be performed via `[folders.delete](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/delete#google.cloud.resourcemanager.v2.Folders.DeleteFolder)` and `[folders.undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/undelete#google.cloud.resourcemanager.v2.Folders.UndeleteFolder)`.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Timestamp when the Folder was created. Assigned by the server.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this folder. Each item in the map must be expressed as " : ". For example: "123/environment" : "production", "123/costCenter" : "marketing"Note: Currently this field is in Preview.  
`configuredCapabilities[]` |  `string` Output only. Optional capabilities configured for this folder (via capabilities.patch API). Example: `folders/123/capabilities/app-management`.  
`managementProject` |  `string` Output only. Management Project associated with this folder (if app-management capability is enabled). Example: `projects/google-mp-123` OUTPUT ONLY.  
  
## LifecycleState

Folder lifecycle states.

Enums  
---  
`LIFECYCLE_STATE_UNSPECIFIED` | Unspecified state.  
`ACTIVE` | The normal and active state.  
`DELETE_REQUESTED` | The folder has been marked for deletion by the user.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/create)`

|  Creates a Folder in the resource hierarchy.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/delete)`

|  Requests deletion of a Folder.  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/get)`

|  Retrieves a Folder identified by the supplied resource name.  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/getIamPolicy)`

|  Gets the access control policy for a Folder.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/list)`

|  Lists the Folders that are direct descendants of supplied parent resource.  
  
### `[move](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/move)`

|  Moves a Folder under a new resource parent.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/patch)`

|  Updates a Folder, changing its display_name.  
  
### `[search](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/search)`

|  Search for folders that match specific filter criteria.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/setIamPolicy)`

|  Sets the access control policy on a Folder, replacing any existing policy.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/testIamPermissions)`

|  Returns permissions that a caller has on the specified Folder.  
  
### `[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/undelete)`

|  Cancels the deletion request for a Folder.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
