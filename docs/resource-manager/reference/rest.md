---
url: https://docs.cloud.google.com/resource-manager/reference/rest/
title: Cloud Resource Manager API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:24.772368+00:00
---

# Cloud Resource Manager API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/reference/rest/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager)
  * [ Reference ](https://docs.cloud.google.com/resource-manager/reference/rest)



Send feedback 

#  Cloud Resource Manager API Stay organized with collections  Save and categorize content based on your preferences. 

Creates, reads, and updates metadata for Google Cloud Platform resource containers.

  * REST Resource: v3.effectiveTags
  * REST Resource: v3.folders
  * REST Resource: v3.folders.capabilities
  * REST Resource: v3.liens
  * REST Resource: v3.locations.effectiveTagBindingCollections
  * REST Resource: v3.locations.tagBindingCollections
  * REST Resource: v3.operations
  * REST Resource: v3.organizations
  * REST Resource: v3.projects
  * REST Resource: v3.tagBindings
  * REST Resource: v3.tagKeys
  * REST Resource: v3.tagValues
  * REST Resource: v3.tagValues.tagHolds
  * REST Resource: v2beta1.folders
  * REST Resource: v2.folders
  * REST Resource: v1beta1.organizations
  * REST Resource: v1beta1.projects
  * REST Resource: v1.folders
  * REST Resource: v1.liens
  * REST Resource: v1.operations
  * REST Resource: v1.organizations
  * REST Resource: v1.projects



## Service: cloudresourcemanager.googleapis.com

To call this service, we recommend that you use the Google-provided [client libraries](https://cloud.google.com/apis/docs/client-libraries-explained). If your application needs to use your own libraries to call this service, use the following information when you make the API requests.

### Discovery document

A [Discovery Document](https://developers.google.com/discovery/v1/reference/apis) is a machine-readable specification for describing and consuming REST APIs. It is used to build client libraries, IDE plugins, and other tools that interact with Google APIs. One service may provide multiple discovery documents. This service provides the following discovery documents:

  * <https://cloudresourcemanager.googleapis.com/$discovery/rest?version=v3>
  * <https://cloudresourcemanager.googleapis.com/$discovery/rest?version=v2>
  * <https://cloudresourcemanager.googleapis.com/$discovery/rest?version=v2beta1>
  * <https://cloudresourcemanager.googleapis.com/$discovery/rest?version=v1>
  * <https://cloudresourcemanager.googleapis.com/$discovery/rest?version=v1beta1>



### Service endpoint

A [service endpoint](https://cloud.google.com/apis/design/glossary#api_service_endpoint) is a base URL that specifies the network address of an API service. One service might have multiple service endpoints. This service has the following service endpoint and all URIs below are relative to this service endpoint:

  * `https://cloudresourcemanager.googleapis.com`



## REST Resource: [v3.effectiveTags](https://docs.cloud.google.com/resource-manager/reference/rest/v3/effectiveTags)

Methods  
---  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/effectiveTags/list)` |  `GET /v3/effectiveTags`   
Return a list of effective tags for the given Google Cloud resource, as specified in `parent`.  
  
## REST Resource: [v3.folders](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/create)` |  `POST /v3/folders`   
Creates a folder in the resource hierarchy.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/delete)` |  `DELETE /v3/{name=folders/*}`   
Requests deletion of a folder.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/get)` |  `GET /v3/{name=folders/*}`   
Retrieves a folder identified by the supplied resource name.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/getIamPolicy)` |  `POST /v3/{resource=folders/*}:getIamPolicy`   
Gets the access control policy for a folder.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/list)` |  `GET /v3/folders`   
Lists the folders that are direct descendants of supplied parent resource.  
`[move](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/move)` |  `POST /v3/{name=folders/*}:move`   
Moves a folder under a new resource parent.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/patch)` |  `PATCH /v3/{folder.name=folders/*}`   
Updates a folder, changing its `display_name`.  
`[search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/search)` |  `GET /v3/folders:search`   
Search for folders that match specific filter criteria.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/setIamPolicy)` |  `POST /v3/{resource=folders/*}:setIamPolicy`   
Sets the access control policy on a folder, replacing any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/testIamPermissions)` |  `POST /v3/{resource=folders/*}:testIamPermissions`   
Returns permissions that a caller has on the specified folder.  
`[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders/undelete)` |  `POST /v3/{name=folders/*}:undelete`   
Cancels the deletion request for a folder.  
  
## REST Resource: [v3.folders.capabilities](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilities)

Methods  
---  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilities/get)` |  `GET /v3/{name=folders/*/capabilities/*}`   
Retrieves the Capability identified by the supplied resource name.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/folders.capabilities/patch)` |  `PATCH /v3/{capability.name=folders/*/capabilities/*}`   
Updates the Capability.  
  
## REST Resource: [v3.liens](https://docs.cloud.google.com/resource-manager/reference/rest/v3/liens)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/liens/create)` |  `POST /v3/liens`   
Create a Lien which applies to the resource denoted by the `parent` field.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/liens/delete)` |  `DELETE /v3/{name=liens/**}`   
Delete a Lien by `name`.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/liens/get)` |  `GET /v3/{name=liens/**}`   
Retrieve a Lien by `name`.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/liens/list)` |  `GET /v3/liens`   
List all Liens applied to the `parent` resource.  
  
## REST Resource: [v3.locations.effectiveTagBindingCollections](https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.effectiveTagBindingCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.effectiveTagBindingCollections/get)` |  `GET /v3/{name=locations/*/effectiveTagBindingCollections/*}`   
Returns effective tag bindings on a Google Cloud resource.  
  
## REST Resource: [v3.locations.tagBindingCollections](https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.tagBindingCollections)

Methods  
---  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.tagBindingCollections/get)` |  `GET /v3/{name=locations/*/tagBindingCollections/*}`   
Returns tag bindings directly attached to a Google Cloud resource.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/locations.tagBindingCollections/patch)` |  `PATCH /v3/{tagBindingCollection.name=locations/*/tagBindingCollections/*}`   
Updates tag bindings directly attached to a Google Cloud resource.  
  
## REST Resource: [v3.operations](https://docs.cloud.google.com/resource-manager/reference/rest/v3/operations)

Methods  
---  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/operations/get)` |  `GET /v3/{name=operations/**}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v3.organizations](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations)

Methods  
---  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/get)` |  `GET /v3/{name=organizations/*}`   
Fetches an organization resource identified by the specified resource name.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/getIamPolicy)` |  `POST /v3/{resource=organizations/*}:getIamPolicy`   
Gets the access control policy for an organization resource.  
`[search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/search)` |  `GET /v3/organizations:search`   
Searches organization resources that are visible to the user and satisfy the specified filter.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/setIamPolicy)` |  `POST /v3/{resource=organizations/*}:setIamPolicy`   
Sets the access control policy on an organization resource.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/organizations/testIamPermissions)` |  `POST /v3/{resource=organizations/*}:testIamPermissions`   
Returns the permissions that a caller has on the specified organization.  
  
## REST Resource: [v3.projects](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/create)` |  `POST /v3/projects`   
Request that a new project be created.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/delete)` |  `DELETE /v3/{name=projects/*}`   
Marks the project identified by the specified `name` (for example, `projects/415104041262`) for deletion.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get)` |  `GET /v3/{name=projects/*}`   
Retrieves the project identified by the specified `name` (for example, `projects/415104041262`).  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/getIamPolicy)` |  `POST /v3/{resource=projects/*}:getIamPolicy`   
Returns the IAM access control policy for the specified project, in the format `projects/{ProjectIdOrNumber}` e.g.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list)` |  `GET /v3/projects`   
Lists projects that are direct children of the specified folder or organization resource.  
`[move](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/move)` |  `POST /v3/{name=projects/*}:move`   
Move a project to another place in your resource hierarchy, under a new resource parent.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/patch)` |  `PATCH /v3/{project.name=projects/*}`   
Updates the `display_name` and labels of the project identified by the specified `name` (for example, `projects/415104041262`).  
`[search](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search)` |  `GET /v3/projects:search`   
Search for projects that the caller has the `resourcemanager.projects.get` permission on, and also satisfy the specified query.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/setIamPolicy)` |  `POST /v3/{resource=projects/*}:setIamPolicy`   
Sets the IAM access control policy for the specified project, in the format `projects/{ProjectIdOrNumber}` e.g.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/testIamPermissions)` |  `POST /v3/{resource=projects/*}:testIamPermissions`   
Returns permissions that a caller has on the specified project, in the format `projects/{ProjectIdOrNumber}` e.g.  
`[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/undelete)` |  `POST /v3/{name=projects/*}:undelete`   
Restores the project identified by the specified `name` (for example, `projects/415104041262`).  
  
## REST Resource: [v3.tagBindings](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/create)` |  `POST /v3/tagBindings`   
Creates a TagBinding between a TagValue and a Google Cloud resource.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/delete)` |  `DELETE /v3/{name=tagBindings/**}`   
Deletes a TagBinding.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagBindings/list)` |  `GET /v3/tagBindings`   
Lists the TagBindings for the given Google Cloud resource, as specified with `parent`.  
  
## REST Resource: [v3.tagKeys](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/create)` |  `POST /v3/tagKeys`   
Creates a new TagKey.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/delete)` |  `DELETE /v3/{name=tagKeys/*}`   
Deletes a TagKey.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/get)` |  `GET /v3/{name=tagKeys/*}`   
Retrieves a TagKey.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/getIamPolicy)` |  `POST /v3/{resource=tagKeys/*}:getIamPolicy`   
Gets the access control policy for a TagKey.  
`[getNamespaced](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/getNamespaced)` |  `GET /v3/tagKeys/namespaced`   
Retrieves a TagKey by its namespaced name.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/list)` |  `GET /v3/tagKeys`   
Lists all TagKeys for a parent resource.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/patch)` |  `PATCH /v3/{tagKey.name=tagKeys/*}`   
Updates the attributes of the TagKey resource.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/setIamPolicy)` |  `POST /v3/{resource=tagKeys/*}:setIamPolicy`   
Sets the access control policy on a TagKey, replacing any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagKeys/testIamPermissions)` |  `POST /v3/{resource=tagKeys/*}:testIamPermissions`   
Returns permissions that a caller has on the specified TagKey.  
  
## REST Resource: [v3.tagValues](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/create)` |  `POST /v3/tagValues`   
Creates a TagValue as a child of the specified TagKey.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/delete)` |  `DELETE /v3/{name=tagValues/*}`   
Deletes a TagValue.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/get)` |  `GET /v3/{name=tagValues/*}`   
Retrieves a TagValue.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/getIamPolicy)` |  `POST /v3/{resource=tagValues/*}:getIamPolicy`   
Gets the access control policy for a TagValue.  
`[getNamespaced](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/getNamespaced)` |  `GET /v3/tagValues/namespaced`   
Retrieves a TagValue by its namespaced name.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/list)` |  `GET /v3/tagValues`   
Lists all TagValues for a specific TagKey.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/patch)` |  `PATCH /v3/{tagValue.name=tagValues/*}`   
Updates the attributes of the TagValue resource.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/setIamPolicy)` |  `POST /v3/{resource=tagValues/*}:setIamPolicy`   
Sets the access control policy on a TagValue, replacing any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues/testIamPermissions)` |  `POST /v3/{resource=tagValues/*}:testIamPermissions`   
Returns permissions that a caller has on the specified TagValue.  
  
## REST Resource: [v3.tagValues.tagHolds](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds/create)` |  `POST /v3/{parent=tagValues/*}/tagHolds`   
Creates a TagHold.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds/delete)` |  `DELETE /v3/{name=tagValues/*/tagHolds/*}`   
Deletes a TagHold.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v3/tagValues.tagHolds/list)` |  `GET /v3/{parent=tagValues/*}/tagHolds`   
Lists TagHolds under a TagValue.  
  
## REST Resource: [v2beta1.folders](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/create)` |  `POST /v2beta1/folders`   
Creates a Folder in the resource hierarchy.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/delete)` |  `DELETE /v2beta1/{name=folders/*}`   
Requests deletion of a Folder.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/get)` |  `GET /v2beta1/{name=folders/*}`   
Retrieves a Folder identified by the supplied resource name.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/getIamPolicy)` |  `POST /v2beta1/{resource=folders/*}:getIamPolicy`   
Gets the access control policy for a Folder.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/list)` |  `GET /v2beta1/folders`   
Lists the Folders that are direct descendants of supplied parent resource.  
`[move](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/move)` |  `POST /v2beta1/{name=folders/*}:move`   
Moves a Folder under a new resource parent.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/patch)` |  `PATCH /v2beta1/{folder.name=folders/*}`   
Updates a Folder, changing its display_name.  
`[search](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/search)` |  `POST /v2beta1/folders:search`   
Search for folders that match specific filter criteria.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/setIamPolicy)` |  `POST /v2beta1/{resource=folders/*}:setIamPolicy`   
Sets the access control policy on a Folder, replacing any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/testIamPermissions)` |  `POST /v2beta1/{resource=folders/*}:testIamPermissions`   
Returns permissions that a caller has on the specified Folder.  
`[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v2beta1/folders/undelete)` |  `POST /v2beta1/{name=folders/*}:undelete`   
Cancels the deletion request for a Folder.  
  
## REST Resource: [v2.folders](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/create)` |  `POST /v2/folders`   
Creates a Folder in the resource hierarchy.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/delete)` |  `DELETE /v2/{name=folders/*}`   
Requests deletion of a Folder.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/get)` |  `GET /v2/{name=folders/*}`   
Retrieves a Folder identified by the supplied resource name.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/getIamPolicy)` |  `POST /v2/{resource=folders/*}:getIamPolicy`   
Gets the access control policy for a Folder.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/list)` |  `GET /v2/folders`   
Lists the Folders that are direct descendants of supplied parent resource.  
`[move](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/move)` |  `POST /v2/{name=folders/*}:move`   
Moves a Folder under a new resource parent.  
`[patch](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/patch)` |  `PATCH /v2/{folder.name=folders/*}`   
Updates a Folder, changing its display_name.  
`[search](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/search)` |  `POST /v2/folders:search`   
Search for folders that match specific filter criteria.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/setIamPolicy)` |  `POST /v2/{resource=folders/*}:setIamPolicy`   
Sets the access control policy on a Folder, replacing any existing policy.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/testIamPermissions)` |  `POST /v2/{resource=folders/*}:testIamPermissions`   
Returns permissions that a caller has on the specified Folder.  
`[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v2/folders/undelete)` |  `POST /v2/{name=folders/*}:undelete`   
Cancels the deletion request for a Folder.  
  
## REST Resource: [v1beta1.organizations](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations)

Methods  
---  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/get)` |  `GET /v1beta1/{name=organizations/*}`   
Fetches an Organization resource identified by the specified resource name.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/getIamPolicy)` |  `POST /v1beta1/{resource=organizations/*}:getIamPolicy`   
Gets the access control policy for an Organization resource.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/list)` |  `GET /v1beta1/organizations`   
Lists Organization resources that are visible to the user and satisfy the specified filter.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/setIamPolicy)` |  `POST /v1beta1/{resource=organizations/*}:setIamPolicy`   
Sets the access control policy on an Organization resource.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/testIamPermissions)` |  `POST /v1beta1/{resource=organizations/*}:testIamPermissions`   
Returns permissions that a caller has on the specified Organization.  
`[update](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/organizations/update)   
**(deprecated)**` |  `PUT /v1beta1/{name=organizations/*}`   
Updates an Organization resource identified by the specified resource name.  
  
## REST Resource: [v1beta1.projects](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/create)` |  `POST /v1beta1/projects`   
Creates a Project resource.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/delete)` |  `DELETE /v1beta1/projects/{projectId}`   
Marks the Project identified by the specified `project_id` (for example, `my-project-123`) for deletion.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/get)` |  `GET /v1beta1/projects/{projectId}`   
Retrieves the Project identified by the specified `project_id` (for example, `my-project-123`).  
`[getAncestry](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/getAncestry)` |  `POST /v1beta1/projects/{projectId}:getAncestry`   
Gets a list of ancestors in the resource hierarchy for the Project identified by the specified `project_id` (for example, `my-project-123`).  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/getIamPolicy)` |  `POST /v1beta1/projects/{resource}:getIamPolicy`   
Returns the IAM access control policy for the specified Project.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/list)` |  `GET /v1beta1/projects`   
Lists Projects that the caller has the `resourcemanager.projects.get` permission on and satisfy the specified filter.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/setIamPolicy)` |  `POST /v1beta1/projects/{resource}:setIamPolicy`   
Sets the IAM access control policy for the specified Project.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/testIamPermissions)` |  `POST /v1beta1/projects/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified Project.  
`[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/undelete)` |  `POST /v1beta1/projects/{projectId}:undelete`   
Restores the Project identified by the specified `project_id` (for example, `my-project-123`).  
`[update](https://docs.cloud.google.com/resource-manager/reference/rest/v1beta1/projects/update)` |  `PUT /v1beta1/projects/{projectId}`   
Updates the attributes of the Project identified by the specified `project_id` (for example, `my-project-123`).  
  
## REST Resource: [v1.folders](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders)

Methods  
---  
`[clearOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/clearOrgPolicy)` |  `POST /v1/{resource=folders/*}:clearOrgPolicy`   
Clears a `Policy` from a resource.  
`[getEffectiveOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/getEffectiveOrgPolicy)` |  `POST /v1/{resource=folders/*}:getEffectiveOrgPolicy`   
Gets the effective `Policy` on a resource.  
`[getOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/getOrgPolicy)` |  `POST /v1/{resource=folders/*}:getOrgPolicy`   
Gets a `Policy` on a resource.  
`[listAvailableOrgPolicyConstraints](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/listAvailableOrgPolicyConstraints)` |  `POST /v1/{resource=folders/*}:listAvailableOrgPolicyConstraints`   
Lists `Constraints` that could be applied on the specified resource.  
`[listOrgPolicies](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/listOrgPolicies)` |  `POST /v1/{resource=folders/*}:listOrgPolicies`   
Lists all the `Policies` set for a particular resource.  
`[setOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/folders/setOrgPolicy)` |  `POST /v1/{resource=folders/*}:setOrgPolicy`   
Updates the specified `Policy` on the resource.  
  
## REST Resource: [v1.liens](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens)

Methods  
---  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/create)` |  `POST /v1/liens`   
Create a Lien which applies to the resource denoted by the `parent` field.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/delete)` |  `DELETE /v1/{name=liens/**}`   
Delete a Lien by `name`.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/get)` |  `GET /v1/{name=liens/**}`   
Retrieve a Lien by `name`.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v1/liens/list)` |  `GET /v1/liens`   
List all Liens applied to the `parent` resource.  
  
## REST Resource: [v1.operations](https://docs.cloud.google.com/resource-manager/reference/rest/v1/operations)

Methods  
---  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/operations/get)` |  `GET /v1/{name=operations/**}`   
Gets the latest state of a long-running operation.  
  
## REST Resource: [v1.organizations](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations)

Methods  
---  
`[clearOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/clearOrgPolicy)` |  `POST /v1/{resource=organizations/*}:clearOrgPolicy`   
Clears a `Policy` from a resource.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/get)` |  `GET /v1/{name=organizations/*}`   
Fetches an Organization resource identified by the specified resource name.  
`[getEffectiveOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/getEffectiveOrgPolicy)` |  `POST /v1/{resource=organizations/*}:getEffectiveOrgPolicy`   
Gets the effective `Policy` on a resource.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/getIamPolicy)` |  `POST /v1/{resource=organizations/*}:getIamPolicy`   
Gets the access control policy for an Organization resource.  
`[getOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/getOrgPolicy)` |  `POST /v1/{resource=organizations/*}:getOrgPolicy`   
Gets a `Policy` on a resource.  
`[listAvailableOrgPolicyConstraints](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/listAvailableOrgPolicyConstraints)` |  `POST /v1/{resource=organizations/*}:listAvailableOrgPolicyConstraints`   
Lists `Constraints` that could be applied on the specified resource.  
`[listOrgPolicies](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/listOrgPolicies)` |  `POST /v1/{resource=organizations/*}:listOrgPolicies`   
Lists all the `Policies` set for a particular resource.  
`[search](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/search)` |  `POST /v1/organizations:search`   
Searches Organization resources that are visible to the user and satisfy the specified filter.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/setIamPolicy)` |  `POST /v1/{resource=organizations/*}:setIamPolicy`   
Sets the access control policy on an Organization resource.  
`[setOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/setOrgPolicy)` |  `POST /v1/{resource=organizations/*}:setOrgPolicy`   
Updates the specified `Policy` on the resource.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v1/organizations/testIamPermissions)` |  `POST /v1/{resource=organizations/*}:testIamPermissions`   
Returns permissions that a caller has on the specified Organization.  
  
## REST Resource: [v1.projects](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects)

Methods  
---  
`[clearOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/clearOrgPolicy)` |  `POST /v1/{resource=projects/*}:clearOrgPolicy`   
Clears a `Policy` from a resource.  
`[create](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/create)` |  `POST /v1/projects`   
Request that a new Project be created.  
`[delete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/delete)` |  `DELETE /v1/projects/{projectId}`   
Marks the Project identified by the specified `project_id` (for example, `my-project-123`) for deletion.  
`[get](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/get)` |  `GET /v1/projects/{projectId}`   
Retrieves the Project identified by the specified `project_id` (for example, `my-project-123`).  
`[getAncestry](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getAncestry)` |  `POST /v1/projects/{projectId}:getAncestry`   
Gets a list of ancestors in the resource hierarchy for the Project identified by the specified `project_id` (for example, `my-project-123`).  
`[getEffectiveOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getEffectiveOrgPolicy)` |  `POST /v1/{resource=projects/*}:getEffectiveOrgPolicy`   
Gets the effective `Policy` on a resource.  
`[getIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy)` |  `POST /v1/projects/{resource}:getIamPolicy`   
Returns the IAM access control policy for the specified Project.  
`[getOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getOrgPolicy)` |  `POST /v1/{resource=projects/*}:getOrgPolicy`   
Gets a `Policy` on a resource.  
`[list](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/list)` |  `GET /v1/projects`   
Lists Projects that the caller has the `resourcemanager.projects.get` permission on and satisfy the specified filter.  
`[listAvailableOrgPolicyConstraints](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/listAvailableOrgPolicyConstraints)` |  `POST /v1/{resource=projects/*}:listAvailableOrgPolicyConstraints`   
Lists `Constraints` that could be applied on the specified resource.  
`[listOrgPolicies](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/listOrgPolicies)` |  `POST /v1/{resource=projects/*}:listOrgPolicies`   
Lists all the `Policies` set for a particular resource.  
`[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)` |  `POST /v1/projects/{resource}:setIamPolicy`   
Sets the IAM access control policy for the specified Project.  
`[setOrgPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setOrgPolicy)` |  `POST /v1/{resource=projects/*}:setOrgPolicy`   
Updates the specified `Policy` on the resource.  
`[testIamPermissions](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/testIamPermissions)` |  `POST /v1/projects/{resource}:testIamPermissions`   
Returns permissions that a caller has on the specified Project.  
`[undelete](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/undelete)` |  `POST /v1/projects/{projectId}:undelete`   
Restores the Project identified by the specified `project_id` (for example, `my-project-123`).  
`[update](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/update)` |  `PUT /v1/projects/{projectId}`   
Updates the attributes of the Project identified by the specified `project_id` (for example, `my-project-123`).  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-09-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-09-09 UTC."],[],[]] 
