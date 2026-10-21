---
url: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/
title: REST Resource: projects \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T09:08:20.392551+00:00
---

# REST Resource: projects  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  REST Resource: projects Stay organized with collections  Save and categorize content based on your preferences. 

  * Resource: Project
    * JSON representation
  * LifecycleState
  * ResourceId
    * JSON representation
  * Methods



## Resource: Project

A Project is a high-level Google Cloud Platform entity. It is a container for ACLs, APIs, App Engine Apps, VMs, and other Google Cloud Platform resources.

JSON representation  
---  
      
    
    {
      "projectNumber": string,
      "projectId": string,
      "lifecycleState": enum ([LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#LifecycleState)),
      "name": string,
      "createTime": string,
      "labels": {
        string: string,
        ...
      },
      "parent": {
        object ([ResourceId](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#ResourceId))
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
`projectNumber` |  `string ([int64](https://developers.google.com/discovery/v1/type-format) format)` The number uniquely identifying the project.Example: `415104041262`Read-only.  
`projectId` |  `string` The unique, user-assigned ID of the Project. It must be 6 to 30 lowercase letters, digits, or hyphens. It must start with a letter. Trailing hyphens are prohibited.Example: `tokyo-rain-123`Read-only after creation.  
`lifecycleState` |  `enum (`[LifecycleState](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#LifecycleState)`)` The Project lifecycle state.Read-only.  
`name` |  `string` The optional user-assigned display name of the Project. When present it must be between 4 to 30 characters. Allowed characters are: lowercase and uppercase letters, numbers, hyphen, single-quote, double-quote, space, and exclamation point.Example: `My Project`Read-write.  
`createTime` |  `string (`[Timestamp](https://protobuf.dev/reference/protobuf/google.protobuf/#timestamp)` format)` Creation time.Read-only.Uses RFC 3339, where generated output will always be Z-normalized and use 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted. Examples: `"2014-10-02T15:01:23Z"`, `"2014-10-02T15:01:23.045123456Z"` or `"2014-10-02T15:01:23+05:30"`.  
`labels` |  `map (key: string, value: string)` The labels associated with this Project.Label keys must be between 1 and 63 characters long and must conform to the following regular expression: [a-z][a-z0-9_-]{0,62}.Label values must be between 0 and 63 characters long and must conform to the regular expression [a-z0-9_-]{0,63}. A label value can be empty.No more than 256 labels can be associated with a given resource.Clients should store labels in a representation such as JSON that does not depend on specific characters being disallowed.Example:  `"environment" : "dev"` Read-write.  
`parent` |  `object (`[ResourceId](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects#ResourceId)`)` An optional reference to a parent Resource.Supported parent types include "organization" and "folder". Once set, the parent cannot be cleared. The `parent` can be set on creation or using the `projects.update` method; the end user must have the `resourcemanager.projects.create` permission on the parent.  
`tags` |  `map (key: string, value: string)` Optional. Input only. Immutable. Tag keys/values directly bound to this project. Each item in the map must be expressed as " : ". For example: "123/environment" : "production", "123/costCenter" : "marketing"Note: Currently this field is in Preview.  
`configuredCapabilities[]` |  `string` Output only. If this project is a Management Project, list of capabilities configured on the parent folder. Note, presence of any capability implies that this is a Management Project. Example: `folders/123/capabilities/app-management`. OUTPUT ONLY.  
  
## LifecycleState

Project lifecycle states.

Enums  
---  
`LIFECYCLE_STATE_UNSPECIFIED` | Unspecified state. This is only used/useful for distinguishing unset values.  
`ACTIVE` | The normal and active state.  
`DELETE_REQUESTED` | The project has been marked for deletion by the user (by invoking `[projects.delete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/delete#google.cloudresourcemanager.v1.Projects.DeleteProject)`) or by the system (Google Cloud Platform). This can generally be reversed by invoking `[projects.undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/undelete#google.cloudresourcemanager.v1.Projects.UndeleteProject)`.  
`DELETE_IN_PROGRESS` | This lifecycle state is no longer used and not returned by the API.  
  
## ResourceId

A container to reference an id for any resource type. A `resource` in Google Cloud Platform is a generic term for something you (a developer) may want to interact with through one of our API's. Some examples are an App Engine app, a Compute Engine instance, a Cloud SQL database, and so on.

JSON representation  
---  
      
    
    {
      "type": string,
      "id": string
    }  
  
Fields  
---  
`type` |  `string` The resource type this id is for. At present, the valid types are: "organization", "folder", and "project".  
`id` |  `string` The type-specific id. This should correspond to the id used in the type-specific API's.  
  
## Methods  
  
---  
  
### `[clearOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/clearOrgPolicy)`

|  Clears a `Policy` from a resource.  
  
### `[create](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/create)`

|  Request that a new Project be created.  
  
### `[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/delete)`

|  Marks the Project identified by the specified `project_id` (for example, `my-project-123`) for deletion.  
  
### `[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/get)`

|  Retrieves the Project identified by the specified `project_id` (for example, `my-project-123`).  
  
### `[getAncestry](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getAncestry)`

|  Gets a list of ancestors in the resource hierarchy for the Project identified by the specified `project_id` (for example, `my-project-123`).  
  
### `[getEffectiveOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getEffectiveOrgPolicy)`

|  Gets the effective `Policy` on a resource.  
  
### `[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy)`

|  Returns the IAM access control policy for the specified Project.  
  
### `[getOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getOrgPolicy)`

|  Gets a `Policy` on a resource.  
  
### `[list](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/list)`

|  Lists Projects that the caller has the `resourcemanager.projects.get` permission on and satisfy the specified filter.  
  
### `[listAvailableOrgPolicyConstraints](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/listAvailableOrgPolicyConstraints)`

|  Lists `Constraints` that could be applied on the specified resource.  
  
### `[listOrgPolicies](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/listOrgPolicies)`

|  Lists all the `Policies` set for a particular resource.  
  
### `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)`

|  Sets the IAM access control policy for the specified Project.  
  
### `[setOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy)`

|  Updates the specified `Policy` on the resource.  
  
### `[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions)`

|  Returns permissions that a caller has on the specified Project.  
  
### `[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/undelete)`

|  Restores the Project identified by the specified `project_id` (for example, `my-project-123`).  
  
### `[update](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/update)`

|  Updates the attributes of the Project identified by the specified `project_id` (for example, `my-project-123`).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-02-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-02-09 UTC."],[],[]] 
