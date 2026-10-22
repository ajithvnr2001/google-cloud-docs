---
url: https://docs.cloud.google.com/resource-manager/docs/manage-projects-within-folder/
title: Manage projects within folders \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:03.380619+00:00
---

# Manage projects within folders  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/manage-projects-within-folder/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  Manage projects within folders Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to organize your Google Cloud hierarchy by nesting projects within folders.

## Overview

In the Google Cloud resource hierarchy, projects serve as the core organizational and billing units for your resources. They sit between folders (or the organization resource) and the underlying resources, such as virtual machine instances and storage buckets.

While folders are an optional grouping mechanism, organizing your projects within folders provides several key advantages:

  * Scalable governance: Automatically apply Identity and Access Management (IAM) policies and security constraints to multiple projects through hierarchy-based inheritance.

  * Business alignment: Structure your cloud environment to reflect your organization's departments, cost centers, or development lifecycles (such as Dev, Staging, and Prod).

  * Delegated administration: Grant specific teams the autonomy to manage their own projects and sub-folders without requiring broad permissions at the organization level.

  * Cost visibility: Group related projects to simplify spend tracking and enhance billing analysis for specific business units or applications.

  * Security isolation: Establish clear trust boundaries to limit the affected area of configuration changes and reduce security risks across different environments.




## Create a project in a folder

To create a project in a folder, you must have the Project Creator role (`roles/resourcemanager.projectCreator`) on the folder. This role may be inherited from a parent folder.

### Console

  1. In the Google Cloud console, open the Manage resources page. 

[ Open Google Cloud console](https://console.cloud.google.com/cloud-resource-manager)

  2. Go to the **Manage resources** page.
  3. Select your organization resource from the **Organization** drop-down on the top left of the page.
  4. Click **Create Project**.
  5. Enter a **Project name**.
  6. In the **Destination** box, click **Browse** to select the folder under which you want to create the project.
  7. Click **Create**.



### gcloud
    
    
      gcloud projects create PROJECT_ID --folder FOLDER_ID
    

Replace the following:

  * `PROJECT_ID`: the ID of the project ID to create
  * `FOLDER_ID`: the ID of the folder in which the project should be created.



### REST

The request JSON:
    
    
       request_json= '{
          name: DISPLAY_NAME, projectId: PROJECT_ID, parent: {id: PARENT_ID, type: PARENT_TYPE}
       }'
    

The curl request:
    
    
       curl -X POST -H "Content-Type: application/json" \
       -H "Authorization: Bearer ${bearer_token}" \
       -d "$request_json" \
       https://cloudresourcemanager.googleapis.com/v3/projects
    

Replace the following:

  * `PROJECT_ID`: the unique identifier of the project being created. For example, `my-awesome-proj-123`.
  * `DISPLAY_NAME`: the display name of the project being created.
  * `PARENT_ID`: the unique identifier of the parent being created under. For example, `123`.
  * `PARENT_TYPE`: the type of the parent, like `folder` or `organization`.



Don't include sensitive information in your folder name or other resource names. Any reference to the folder or related resources exposes the folder name and resource name.

## Move a project into a folder

You must carefully consider any policy implications before you move a project into or out of a folder. Allow policies that you define at the _project_ level will move with the project, but policies inherited from a parent resource won't move.

**Note:** The following instructions are only for moving a project within an organization resource. For information about migrating a project between organization resources, see [Migrating projects](https://docs.cloud.google.com/resource-manager/docs/project-migration).

When you move a project, any Identity and Access Management policies or organization policies that are directly attached will move with it. However, a project in your resource hierarchy is also affected by the policies that it inherits from parent resources. If a project inherits an IAM role that provides users permission to use a particular service, users won't have access to that service at the destination unless it would inherit the permission at the destination as well.

For example, consider a service account has the **Storage Object Creator** role bound to a user at Folder A. The service account has permissions to upload data to Cloud Storage in any project in Folder A. If you moved one of these projects to Folder B, which does not have the same inherited permissions, the service account for that project loses the ability to upload data, resulting in a service outage.

These same considerations apply if organization policies are defined at the source and destination folders. Like IAM policies, organization policies are inherited. Consequently, you must ensure that your organization policies are consistent between source and destination folders.

To learn more about organization policies, see [Introduction to the organization Policy Service](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview).

To move a project, you need the Project Mover IAM role (`roles/resourcemanager.projectMover`) on both the source folder and the destination folder. If the resource is not in a folder, you need this role on the organization resource.

These roles give you the following required permissions:

  * `resourcemanager.projects.update` on the project
  * **If the resource is in a folder:** `resourcemanager.projects.move` on the source folder and the destination
  * **If the resource is not in a folder:** `resourcemanager.projects.move` on the organization resource



You can also gain these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles), or other predefined roles.

### Console

To move a project:

  1. In the Google Cloud console, go to the **Manage resources** page. 

[ Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Select your Organization from the **Organization** drop-down on the top left of the page.

  3. Click the project's row to select your project from the list of resources. Note that you _must not_ click the name of the project, which takes you to the project's Identity and Access Management (IAM) page.

  4. Click the options menu (the vertical ellipsis) in the row and click **Move**.

  5. Click **Browse** to select the folder to which you want to move the project.

  6. Click **Move**.




### gcloud

To move a project, run the [`gcloud beta projects move`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/projects/move) command:
    
    
    gcloud beta projects move PROJECT_ID \
       --DESTINATION_TYPE DESTINATION_ID

Replace the following:

  * `PROJECT_ID`: The ID or number of the project you want to move.
  * `DESTINATION_TYPE`: The type of the destination, either `organization` or `folder`.
  * `DESTINATION_ID`: The ID of the organization resource or folder where you want to move the project.



### REST

You can use the v3 [`projects.move`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/move) method to move a project.

Request:
    
    
    POST https://cloudresourcemanager.googleapis.com/v3/{name=PROJECT_NAME}:move
    {
      "destinationParent": DESTINATION_PARENT
    }
    

Replace the following:

  * `PROJECT_NAME`: the name of the project you want to update. For example, `projects/415104041262`

  * `DESTINATION_PARENT`: the new parent organization resource or folder under which you want to move the project. For example: `organizations/12345678901`




If successful, the request will return an [Operation](https://docs.cloud.google.com/resource-manager/reference/rest/Shared.Types/Operation) which can be used to track the project move.

## Move a folder into another folder

To move a folder into another folder, you must have the **resourcemanager.folders.move** permission for both the source and destination folders.

### Console

The process of moving folders into other folders in the console is similar to moving projects.

  1. In the Google Cloud console, open the Manage resources page. 

[ Open Google Cloud console](https://console.cloud.google.com/cloud-resource-manager)

  2. Select your organization resource from the **Organization** drop-down on the top left of the page.
  3. Click your folder's row to select your folder from the list of projects and folders.
  4. Click the options menu (the vertical ellipsis) in the row and click **Move**.
  5. Click **Browse** to select the folder to which you want to move the folder.
  6. Click **Move**.



### gcloud

To move a folder under the organization resource, run the following command:
    
    
    gcloud resource-manager folders move FOLDER_ID \
        --organization=PARENT_ID
    

Replace the following:

  * `FOLDER_ID`: the ID of the folder to move
  * `PARENT_ID`: the ID of the parent organization resource



To move a folder under another folder, run the following command:
    
    
    gcloud resource-manager folders move FOLDER_ID \
        --folder=PARENT_ID
    

Replace the following:

  * `FOLDER_ID`: the ID of the folder to move
  * `PARENT_ID`: the ID of the parent folder



### REST

The request JSON:
    
    
    request_json= '{
       destinationParent: "folders/DESTINATION_FOLDER_ID"
    }'
    

The Move Folder curl request:
    
    
    curl -X POST -H "Content-Type: application/json" \
    -H "Authorization: Bearer ${bearer_token} \
    -d "$request_json" \
    https://cloudresourcemanager.googleapis.com/v3/folders/DISPLAY_NAME:move
    

Replace the following:

  * DESTINATION_FOLDER_ID: the ID of the folder under which you're moving another folder, for example `98765`.
  * DISPLAY_NAME: the display name of the folder being moved, for example "My Awesome Folder."



The Move Folder response:
    
    
    {
      "name": "operations/fm.1234567890",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.resourcemanager.v3.FolderOperation",
        "displayName": "DISPLAY_NAME",
        "operationType": "MOVE"
      }
    }
    

The Get Operation curl request:
    
    
    curl -H "Authorization: Bearer ${bearer_token}" \
    https://cloudresourcemanager.googleapis.com/v3/operations/fm.1234567890
    

The Get Operation response:
    
    
    {
      "name": "operations/fm.1234567890",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.resourcemanager.v3.FolderOperation",
        "displayName": "DISPLAY_NAME",
        "operationType": "MOVE"
      },
      "done": true,
      "response": {
        "@type": "type.googleapis.com/google.cloud.resourcemanager.v3.Folder",
        "name": "folders/12345",
        "parent": "folders/98765",
        "displayName": "DISPLAY_NAME",
        "lifecycleState": "ACTIVE",
        "createTime": "2017-07-19T23:29:26.018Z",
        "updateTime": "2017-07-20T00:54:44.295Z"
      }
    }
    

## View or list projects within a folder

To view or list projects that are direct children of a folder, you must have the Folder Viewer role (`roles/resourcemanager.folderViewer`) or the Browser role (`roles/browser`) on the folder.

### Console

  1. In the Google Cloud console, open the **Manage resources** page. 

[ Open Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. In the **Organization** drop-down, select your organization.

  3. In the resource list, click the name of the folder to expand it and view its projects.

Optional: Use the **Filter** bar at the top of the list to search for a specific project by name or ID.




### gcloud

To list all projects that are direct children of a specific folder, use the `gcloud projects list` command with a filter:
    
    
    gcloud projects list --filter="parent.id:FOLDER_ID AND parent.type:folder"

Replace FOLDER_ID with the unique ID of the folder.

### REST

Use the `projects.list` method with a query parameter defining the parent folder.

HTTP request: GET https://cloudresourcemanager.googleapis.com/v3/projects?parent=folders/FOLDER_ID

Example curl command:

Bash

curl -H "Authorization: Bearer $(gcloud auth print-access-token)"   
"https://cloudresourcemanager.googleapis.com/v3/projects?parent=folders/FOLDER_ID"

Replace `FOLDER_ID` with the unique ID of the folder.

## Filter projects by Tags or Labels (Optional)

If you have a large number of projects within a folder, you can use filters to find specific resources based on metadata.

### Console

  * In the **Filter** bar on the **Manage resources** page, type `Labels:key=value` to narrow the list to projects with specific labels. Note that the console provides limited support for visual filtering by Tags; use the Google Cloud CLI for advanced Tag queries.



### gcloud

To list projects within a folder that have a specific Tag value, use the `--filter` flag with the tags attribute:
    
    
    gcloud projects list \
      --filter="parent.id:FOLDER_ID AND tags.TAG_KEY_PARENT/TAG_KEY_SHORT_NAME:TAG_VALUE_SHORT_NAME"

Replace the following:

  * `FOLDER_ID`: the unique ID of the folder.
  * `TAG_KEY_PARENT`: the ID of the tag key's parent resource, such as an organization or project.
  * `TAG_KEY_SHORT_NAME`: the short name of the tag key.
  * `TAG_VALUE_SHORT_NAME`: the short name of the tag value.



To filter by Labels:
    
    
    gcloud projects list \
      --filter="parent.id:FOLDER_ID AND labels.KEY=VALUE"

Replace the following:

  * `FOLDER_ID`: the unique ID of the folder.
  * `KEY`: the key of the label.
  * `VALUE`: the value of the label.



## What's next

  * Learn about [viewing and updating projects](https://docs.cloud.google.com/resource-manager/docs/manage-folders).
  * Learn about [roles and permissions for managing projects](https://docs.cloud.google.com/resource-manager/docs/access-control-proj). 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
