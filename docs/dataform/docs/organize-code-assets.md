---
url: https://docs.cloud.google.com/dataform/docs/organize-code-assets/
title: Organize code assets with folders and repositories \u00a0|\u00a0 Dataform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T16:44:09.121262+00:00
---

# Organize code assets with folders and repositories  |  Dataform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/dataform/docs/organize-code-assets/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Dataform ](https://docs.cloud.google.com/dataform/docs)
  * [ Reference ](https://docs.cloud.google.com/dataform/docs/authentication)



Send feedback 

#  Organize code assets with folders and repositories Stay organized with collections  Save and categorize content based on your preferences. 

This document presents a conceptual overview of the folders and repositories system. It also summarizes the Dataform API fields and methods used for working with folders and repositories.

The Dataform API provides resources that you can use to organize code assets in a hierarchical structure that's similar to a typical operating system file system. This structure also enables Identity and Access Management (IAM) policy inheritance, allowing permissions to propagate down the path.

**Important:** Only single file assets such as [notebooks](https://docs.cloud.google.com/bigquery/docs/create-notebooks), [saved queries](https://docs.cloud.google.com/bigquery/docs/work-with-saved-queries), [data canvases](https://docs.cloud.google.com/bigquery/docs/data-canvas), and [data preparations](https://docs.cloud.google.com/bigquery/docs/data-prep-get-suggestions) can interact with the folder structure.

The following list defines key terms used to describe the folders and repositories system:

Folder
    A folder is the basic container for organizing resources, similar to a standard file system folder. It lets you organize other folders and repositories, and you can move resources into and out of folders. You can grant permissions at the folder node, and these permissions propagate to all contents.
User root folder
    A user root folder represents a user's personal space. It contains all the folders and repositories that a user creates or accesses. A user root folder isn't part of a team folder's subtree. A user root folder is a virtual concept that doesn't have an associated API resource.
Team folder
    A team folder is similar to a folder, but it's designed for team collaboration, similar to a shared drive in Google Drive. It provides a dedicated space for core code assets and supports stricter sharing and access permissions for a team's core assets.
File
    In the context of this folder structure, a file is represented by a Dataform repository resource. Each repository contains a single file asset, such as a notebook, saved query, data canvas, or data preparation.

## Required roles

To get the permissions that you need to complete the tasks in this document, ask your administrator to grant you the appropriate IAM roles on the project, folder, or resource.

Permissions granted on a folder propagate to all the folders and files contained within it.

The following roles apply folders and files:

Role | Granted on | Permissions and use cases  
---|---|---  
[Code Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.codeOwner) (`roles/dataform.codeOwner`) | Folder or file | Grants full control over a resource for managing code assets. A user with this role can perform all actions, including deleting the resource, deleting the folder tree, setting the resource's IAM policy, and moving the resource.  
[Code Editor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.codeEditor) (`roles/dataform.codeEditor`) | Folder or file | Allows for editing and managing content. A user with this role can add content to folders, edit files, and get the IAM policy for a folder or file. This role is also required on the destination folder when moving a resource.  
[Code Commenter](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.codeCommenter) (`roles/dataform.codeCommenter`) | Folder or file | Allows for commenting on code assets or folders.  
[Code Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.codeViewer) (`roles/dataform.codeViewer`) | Folder or file | Provides read-only access. A user with this role can query the contents of folders and files.  
[Code Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.codeCreator) (`roles/dataform.codeCreator`) | Project | Grants permission to create new folders and files within a project.  
  
The following roles are specific to managing team folders:

Role | Granted on | Permissions and use cases  
---|---|---  
[Team Folder Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.teamFolderOwner) (`roles/dataform.teamFolderOwner`) | Team folder | Grants full control over a team folder for managing code assets. A user with this role can delete the team folder, delete the team folder tree, and set the team folder's IAM policy.  
[Team Folder Contributor](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.teamFolderContributor) (`roles/dataform.teamFolderContributor`) | Team folder | Allows for content management within a team folder. A user with this role can update a team folder.  
[Team Folder Commenter](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.teamFolderCommenter) (`roles/dataform.teamFolderCommenter`) | Team folder | Allows for commenting on a team folder and the code assets that it contains.  
[Team Folder Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.teamFolderViewer) (`roles/dataform.teamFolderViewer`) | Team folder | Provides read-only access to a team folder and its contents. A user with this role can view a team folder and get its IAM policy.  
[Team Folder Creator](https://docs.cloud.google.com/iam/docs/roles-permissions/dataform#dataform.teamFolderCreator) (`roles/dataform.teamFolderCreator`) | Project | Grants permission to create new team folders within a project.  
  
For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

These predefined roles contain the permissions required to complete the tasks in this document. To see the exact permissions that are required, expand the **Required permissions** section:

#### Required permissions

  * Create a folder: 
    * `folders.create` on the parent user folder, team folder, or project
    * `folders.addContents` on the parent folder or team folder
  * Retrieve the properties of a folder: `folders.get` on the folder
  * Query the contents of a folder or team folder: `folders.queryContents` on the folder
  * Update a folder: `folders.update` on the folder
  * Delete a folder: `folders.delete` on the folder
  * Get the IAM policy for a folder: `folders.getIamPolicy` on the folder
  * Set the IAM policy for a folder: `folders.setIamPolicy` on the folder
  * Move a folder: 
    * `folders.move` on the folder being moved
    * `folders.addContents` on the destination folder or team folder (not needed if moving to a root folder)
  * Create a team folder: `teamFolders.create` on the project
  * Delete a team folder: `teamFolders.delete` on the team folder
  * Get the IAM policy for a team folder: `teamFolders.getIamPolicy` on the team folder
  * Set the IAM policy for a team folder: `teamFolders.setIamPolicy` on the team folder
  * Retrieve the properties of a team folder: `teamFolders.get` on the team folder
  * Update a team folder: `teamFolders.update` on the team folder
  * Create a repository: 
    * `repositories.create` on the parent user folder, team folder, or project
    * `folders.addContents` on the parent folder or team folder
  * Read a repository: `repositories.readFile` on the repository
  * Write to a repository: `repositories.commit` on the repository
  * Move a repository: 
    * `repositories.move` on the repository being moved
    * `folders.addContents` on the destination parent user folder, team folder, or project (not needed if moving to a root folder)
  * Retrieve the properties of a repository: `repositories.get` on the repository
  * Update a repository: `repositories.update` on the repository
  * Delete a repository: `repositories.delete` on the repository



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined).

To gain full access for managing the code assets in your project, ask your administrator to grant you the following IAM roles on the project:

  * [Dataform Admin](https://docs.cloud.google.com/dataform/docs/access-control#dataform.admin) (`roles/dataform.admin`)
  * [Dataform Editor](https://docs.cloud.google.com/dataform/docs/access-control#dataform.editor) (`roles/dataform.editor`)
  * [Dataform Viewer](https://docs.cloud.google.com/dataform/docs/access-control#dataform.viewer) (`roles/dataform.viewer`)



## IAM policy inheritance

IAM access for folder and repository resources leverages a hierarchical structure. This hierarchy ensures that access policies are inherited from parent folders to their contents.

When an IAM policy is set on a folder, the permissions granted by that policy also apply to all the repositories and nested subfolders in the folder's subtree. This has the following consequences:

  * Permissions are inherited through the folder hierarchy. When a user is granted a specific role on a high-level folder, they possess the permissions included in that role for all the resources contained in that folder and its subfolders.
  * The permissions that a user has on a resource consist of the policies set directly on that resource and all the policies inherited from every folder in its path up to the root.



As a result, you don't need project-level permissions to perform actions on resources located deep in a folder structure. You only need the proper permission on any folder in the path to that resource. For example, if you want to create a repository in a subfolder, you need the necessary permissions on either the specific subfolder or any of its parent folders, which includes the top-level folder.

The following are best practices for applying IAM policies to folders and repositories:

  * Apply IAM policies to the highest folder in the hierarchy where the permissions are uniformly needed. For example, if a team needs access to all the data in their team's directory, grant the necessary roles at the level of the team folder instead of at the level of individual project subfolders.
  * Always grant the minimum set of permissions required for users or services to perform their tasks. Avoid granting broad roles where you can use more specific folder-level roles and permissions.

**Note:** Roles granted to folders and repositories are preserved when moving resources. Additionally, roles configured on the source and destination folders and repositories remain unaffected by a move.

## IAM roles granted on resource creation

The following roles are granted automatically upon resource creation:

  * Users who create folders that are not in a team folder subtree automatically receive the [Dataform Admin role](https://docs.cloud.google.com/dataform/docs/access-control#dataform.admin) (`roles/dataform.admin`) on those folders.
  * The creator of a root team folder automatically receives the [Dataform Admin role](https://docs.cloud.google.com/dataform/docs/access-control#dataform.admin) (`roles/dataform.admin`) on that team folder.
  * When you set `setAuthenticatedUserAdmin` to `true` in the [`projects.locations.repositories` resource](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories#resource:-repository), users who create a repository in the user root node automatically receive the [Dataform Admin role](https://docs.cloud.google.com/dataform/docs/access-control#dataform.admin) (`roles/dataform.admin`) on the repository.



You can [use the Config API to grant a specific role upon resource creation](https://docs.cloud.google.com/dataform/docs/access-control#grant-specific-role).

You don't automatically receive any roles when you create new folders or repositories within a team folder's subtree.

## Limitations

Folders and repositories have the following limitations:

  * You can only nest folders up to 5 levels deep.
  * You can't move or delete a folder that contains more than 100 resources in one operation.
  * Having a very large number of folders (hundreds of thousands) slows performance when working with folders.



## Organize resources

The following sections describe how you can organize folder, team folder, and repository resources with the Dataform API.

### Folder resources

The following table describes the API fields for folders:

Field | Description  
---|---  
`containing_folder` | A reference to the parent folder or the team folder's name. You can set this to a folder ID or a team folder ID. If you don't set this field, this is a root folder.  
`display_name` | The user-visible name for the resource. The `display_name` field must be unique according to the following rules: 

  * Within the user root, all folders must have unique display names. However, repository display names at the user root are allowed to clash with other repository and folder names.
  * Within a folder, display names must be unique across all folders and repositories in that folder.
  * Within a team folder, display names must be unique across all folders and repositories in that team folder.
  * Team folder display names must be unique across the project.

  
  
The following table describes the main [`projects.locations.folders`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders) API methods:

API method | Description  
---|---  
[`create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/create) | Creates a new folder.  
[`get`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/get) | Gets a folder's properties.  
[`patch`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/patch) | Updates a folder's properties, such as its name.  
[`queryFolderContents`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/queryFolderContents) | Lists the items in a folder.  
[`move`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/move) | Moves the folder and its entire subtree to a new containing folder. A move operation is atomic, meaning, it succeeds only if all the resources in the folder's subtree are properly moved and there are no partial failures.  
[`delete`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/delete) | Deletes the folder. Succeeds only if the folder is empty.  
[`deleteTree`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/deleteTree) | Asynchronously deletes the folder and its entire subtree, including non-empty folders and repositories. For more information, see Folder deletion parameter.  
[`setIamPolicy`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.folders/setIamPolicy) | Grants roles to the folder. Granted roles automatically propagate to the entire subtree of the folder.  
  
The following example demonstrates how to create a root-level folder:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -X POST \
      -d '{
          "displayName": "DISPLAY_NAME"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/folders"
    

Replace the following:

  * `DISPLAY_NAME`: the user-visible name for the resource.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the Dataform repository where resources are created.



The following example demonstrates how to create a folder that's nested inside another folder:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -X POST \
      -d '{
          "displayName": "DISPLAY_NAME",
          "containingFolder": "projects/PROJECT_ID/locations/LOCATION/folders/PARENT_FOLDER_ID"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/folders"
    

Replace the following:

  * `DISPLAY_NAME`: the user-visible name for the resource.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the Dataform repository where resources are created.
  * `PARENT_FOLDER_ID`: the ID of the existing folder where you want to create the new folder.



The following example demonstrates how to move a folder into another folder:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -X POST \
      -d '{
          "destination_containing_folder": "projects/PROJECT_ID/locations/LOCATION/folders/DESTINATION_PARENT_FOLDER_ID"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/folders/FOLDER_ID_TO_MOVE:move"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the Dataform repository.
  * `DESTINATION_PARENT_FOLDER_ID`: the ID of the folder where you want to move the target folder.
  * `FOLDER_ID_TO_MOVE`: the ID of the folder that you are moving.



### Team folder resources

The following table describes the main [`projects.locations.teamFolders`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders) API methods:

API method | Description  
---|---  
[`create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/create) | Creates a new team folder.  
[`get`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/get) | Gets a team folder's properties.  
[`patch`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/patch) | Updates a team folder's properties, such as its name.  
[`queryContents`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/queryContents) | Lists the items in a team folder.  
[`delete`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/delete) | Deletes the team folder. Succeeds only if the team folder is empty.  
[`deleteTree`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/deleteTree) | Asynchronously deletes the team folder and its entire subtree, including non-empty folders and repositories. For more information, see Folder deletion parameter.  
[`setIamPolicy`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.teamFolders/setIamPolicy) | Grants roles to the team folder. Granted roles automatically propagate to the entire subtree of the team folder.  
  
The following example demonstrates how to query the contents of a team folder:
    
    
    curl -X GET \
      -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/teamFolders/TEAM_FOLDER_ID:queryContents"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) of the Dataform resources.
  * `TEAM_FOLDER_ID`: the ID of the specific Dataform team folder you're querying.



### Folder deletion parameter

The `deleteTree` methods for deleting folders and team folders include a `force` parameter to manage repositories with active configurations.

Parameter | Behavior  
---|---  
`force` | 

  * If set to `true`, the operation forcefully deletes all API resources contained within the folder or team folder subtree, along with their child API resources.
  * If set to `false` (default), the operation fails if it discovers repositories that have associated release configurations, workflow configurations, or workspaces. In this scenario, no resources are deleted.

  
**Note:** These delete operations are long-running operations, and they aren't atomic. Delete operations can partially succeed. If a failure occurs during the process, resources that were successfully deleted before the error occurred can't be recovered.

### Repository resources

You can organize existing repository resources in folder and team folder resources with the `containing_folder` field at the folder node.

The following table describes the API methods for repositories:

The following table describes the main [`projects.locations.repositories`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories) API methods:

API method | Description  
---|---  
[`create`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/create) | Creates a new repository.  
[`get`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/get) | Gets a repository's properties.  
[`patch`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/patch) | Updates a repository's properties, such as its name.  
[`move`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/move) | Moves the repository to a new containing folder.  
[`delete`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/delete) | Deletes the repository.  
[`setIamPolicy`](https://docs.cloud.google.com/dataform/reference/rest/v1/projects.locations.repositories/setIamPolicy) | Grants roles to the repository. Granted roles automatically propagate to the entire subtree of the repository.  
  
The following example demonstrates how to create a repository in the user root node while setting `setAuthenticatedUserAdmin` to `true`:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -X POST \
      -d '{
          "displayName": "REPOSITORY_DISPLAY_NAME",
          "setAuthenticatedUserAdmin": true
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories?repositoryId=REPOSITORY_ID"
    

Replace the following:

  * `REPOSITORY_DISPLAY_NAME`: a user-friendly name for the repository.
  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) for the repository.
  * `REPOSITORY_ID`: the ID of the new repository.



The following example demonstrates how to create a repository inside a team folder:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -X POST \
      -d '{
          "containingFolder": "projects/PROJECT_ID/locations/LOCATION/teamFolders/CONTAINING_TEAM_FOLDER_ID"
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories?repositoryId=REPOSITORY_ID"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) where resources are created. This must be the same location as the location of the `CONTAINING_TEAM_FOLDER_ID`.
  * `CONTAINING_TEAM_FOLDER_ID`: the ID of the specific team folder where you want to place the new repository.
  * `REPOSITORY_ID`: the ID for the new repository.



The following example demonstrates how to move a repository into the root folder:
    
    
    curl -H "Authorization: Bearer $(gcloud auth print-access-token)" \
      -H "Content-Type: application/json" \
      -X POST \
      -d '{
          "destination_containing_folder": ""
      }' \
      "https://dataform.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/repositories/REPOSITORY_ID:move"
    

Replace the following:

  * `PROJECT_ID`: your Google Cloud project ID.
  * `LOCATION`: the [location](https://docs.cloud.google.com/bigquery/docs/locations) where the repository exists.
  * `REPOSITORY_ID`: the ID of the repository you want to move to the root level.



## Busy resources

A folder, team folder, or repository is "busy" if it's actively involved in a move operation, either as the object being moved or the destination of the move. The system restricts busy resources from the following actions to ensure data integrity during the move:

  * Being the object of another move operation.
  * Being the destination of another move operation.
  * Being an ancestor of a move object.
  * Being the object of a delete operation.



## What's next

  * To learn how to organize code assets in BigQuery, see [Organize code assets with folders](https://docs.cloud.google.com/bigquery/docs/code-asset-folders) and [Create and manage folders](https://docs.cloud.google.com/bigquery/docs/create-manage-folders).
  * To learn more about managing permissions for Dataform resources, see [Control access with IAM](https://docs.cloud.google.com/dataform/docs/access-control).
  * To view the complete details of Dataform API methods, see the [Dataform API](https://docs.cloud.google.com/dataform/reference/rest).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
