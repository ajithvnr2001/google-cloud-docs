---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/
title: REST Resource: projects \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:30.077122+00:00
---

# REST Resource: projects  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: projects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Project
    * JSON representation
  * State
  * Methods



## Resource: Project

A project is a high-level Google Cloud entity. It is a container for ACLs, APIs, App Engine Apps, VMs, and other Google Cloud Platform resources.

JSON representation  
---  
      
    
    {
      "name": string,
      "parent": string,
      "projectId": string,
      "state": enum ([State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#State)),
      "displayName": string,
      "createTime": string,
      "updateTime": string,
      "deleteTime": string,
      "etag": string,
      "labels": {
        string: string,
        ...
      },
      "tags": {
        string: string,
        ...
      },
      "configuredCapabilities": [
        string
      ]
    }  
  
Fields  
---  
`name` |  `string` Output only. The unique resource name of the project. It is an int64 generated number prefixed by "projects/".Example: `projects/415104041262`  
`parent` |  `string` Optional. A reference to a parent Resource. eg., `organizations/123` or `folders/876`.  
`projectId` |  `string` Immutable. The unique, user-assigned id of the project. It must be 6 to 30 lowercase ASCII letters, digits, or hyphens. It must start with a letter. Trailing hyphens are prohibited.Example: `tokyo-rain-123`  
`state` |  `enum (`[State](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects#State)`)` Output only. The project lifecycle state.  
`displayName` |  `string` Optional. A user-assigned display name of the project. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point.Example: `My Project`  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. Creation time.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`updateTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The most recent time this resource was modified.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`deleteTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Output only. The time at which this resource was requested for deletion.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`etag` |  `string` Output only. A checksum computed by the server based on the current value of the Project resource. This may be sent on update and delete requests to ensure the client has an up-to-date value before proceeding.  
`labels` |  `map (key: string, value: string)` Optional. The labels associated with this project.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: [a-z]([-a-z0-9]*[a-z0-9])?.Label values must be between 0 and 63 characters long and must conform to the regular expression ([a-z]([-a-z0-9]*[a-z0-9])?)?.No more than 64 labels can be associated with a given resource.Clients should store labels in a representation such as JSON that does not depend on specific characters being disallowed.Example: `"myBusinessDimension" : "businessValue"`  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this project. Each item in the map must be expressed as " : ". For example: "123/environment" : "production", "123/costCenter" : "marketing"Note: Currently this field is in Preview.  
`configuredCapabilities[]` |  `string` Output only. If this project is a Management Project, list of capabilities configured on the parent folder. Note, presence of any capability implies that this is a Management Project. Example: `folders/123/capabilities/app-management`. OUTPUT ONLY.  
  
## State

Project lifecycle states.

Enums  
---  
`STATE_UNSPECIFIED` | Unspecified state. This is only used/useful for distinguishing unset values.  
`ACTIVE` | The normal and active state.  
`DELETE_REQUESTED` | The project has been marked for deletion by the user (by invoking `[projects.delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/delete#google.cloud.resourcemanager.v3.Projects.DeleteProject)`) or by the system (Google Cloud Platform). This can generally be reversed by invoking `[projects.undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/undelete#google.cloud.resourcemanager.v3.Projects.UndeleteProject)`.  
  
## Methods  
  
---  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/create)`

|  Request that a new project be created.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/delete)`

|  Marks the project identified by the specified `name` (for example, `projects/415104041262`) for deletion.  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get)`

|  Retrieves the project identified by the specified `name` (for example, `projects/415104041262`).  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/getIamPolicy)`

|  Returns the IAM access control policy for the specified project, in the format `projects/{ProjectIdOrNumber}` e.g.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list)`

|  Lists projects that are direct children of the specified folder or organization resource.  
  
### `[move](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/move)`

|  Move a project to another place in your resource hierarchy, under a new resource parent.  
  
### `[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/patch)`

|  Updates the `display_name` and labels of the project identified by the specified `name` (for example, `projects/415104041262`).  
  
### `[search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search)`

|  Search for projects that the caller has the `resourcemanager.projects.get` permission on, and also satisfy the specified query.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/setIamPolicy)`

|  Sets the IAM access control policy for the specified project, in the format `projects/{ProjectIdOrNumber}` e.g.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/testIamPermissions)`

|  Returns permissions that a caller has on the specified project, in the format `projects/{ProjectIdOrNumber}` e.g.  
  
### `[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/undelete)`

|  Restores the project identified by the specified `name` (for example, `projects/415104041262`).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
