---
url: https://docs.cloud.google.com/resource-manager/docs/manage-folders/
title: View, update, and delete folders \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:58:04.970938+00:00
---

# View, update, and delete folders  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/manage-folders/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  View, update, and delete folders Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to view folder details, update folder settings, and delete folders using the Google Cloud console, Google Cloud CLI, or API. Learn how to modify folder display names and manage folder placement within your organization's hierarchy.

## List folders and view folder details

To list folders or to view metadata for a specific folder, such as its display name, parent ID, and lifecycle state, you must have the Folder Viewer role (`roles/resourcemanager.folderViewer`) or the Organization Viewer role (`roles/resourcemanager.organizationViewer`).

### Console

  1. In the Google Cloud console, open the **Manage resources** page. 

[ Open Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. The resource list displays your hierarchy as a table. Select your organization resource.

  3. Click the arrow next to the organization name to expand the tree view and see its child folders.

  4. To perform actions, such as moving, deleting, or viewing settings, click the more_vert**Actions** at the end of the row for that specific resource.

  5. Use the **Filter** bar at the top of the resource list to search for resources by name, ID, or label.




**Using the project picker**

The project picker is located in the navigation bar and isn't part of the main Resource Manager page interface. Use it to switch your active global context to a specific project or folder.

  1. Click the project picker. In the dialog that appears, select your organization from the drop-down to filter the results.

  2. Browse the hierarchy or search for the project or folder you want to switch to. Clicking a resource in this picker changes your global context, affecting which resources are visible in other service pages (like Compute Engine or Cloud Storage).

**Note:** Up to 4000 resources can be displayed in the project picker. If you don't see a resource that should appear, go to the **Manage resources** page and filter the list using the name of that resource.



### gcloud

To get details of one folder, use the `resource-manager folders describe` command.
    
    
    gcloud resource-manager folders describe FOLDER_ID
    

Replace `FOLDER_ID` with the ID of the folder you want to view.

To list the child folders of an organization resource, use the `resource-manager folders list` command.
    
    
    gcloud resource-manager folders list \
        --organization ORGANIZATION_ID
    

Replace `ORGANIZATION_ID` with the ID of the organization resource for which you want to see a list of child folders.

To list the child folders of a folder resource, use the `resource-manager folders list` command.
    
    
    gcloud resource-manager folders list \
        --folder FOLDER_ID
    

Replace `FOLDER_ID` with the ID of the folder resource for which you want to see a list of child folders.

To list the projects under an organization or folder resource or folder, use the `projects list` command with the `filter` argument.
    
    
    gcloud projects list \
        --filter=" parent.id: 'RESOURCE_ID' "
    

Replace `RESOURCE_ID` with the ID of the organization or folder resource for which you want to see a list of child projects.

### REST

The curl request to get folders:
    
    
    curl -X GET -H "Content-Type: application/json" \
      -H "Authorization: Bearer ${bearer_token}" \
      https://cloudresourcemanager.googleapis.com/v3/FOLDER_ID
    

Replace `FOLDER_NAME` with the name of the folder, such as `folders/123`.

The curl request to list folders:
    
    
    curl -X GET -H "Content-Type: application/json" \
      -H "Authorization: Bearer ${bearer_token}" \
      https://cloudresourcemanager.googleapis.com/v3/folders?parent=PARENT_NAME
    

Replace `PARENT_NAME` with the name of the parent resource under which you're creating the folder, such as `organizations/123` or `folders/123`.

**Note:** The list command and API method only return the direct children of the specified parent resource. They don't recursively list all folders and projects across the entire hierarchy. To view the full nested structure, you must list the children of each sub-folder individually or use the **Manage resources** page in the Google Cloud console.

## Update folders

To update a folder's display name, you must have the Folder Editor role (`roles/resourcemanager.folderEditor`) or the Folder Admin role (`roles/resourcemanager.folderAdmin`) on the folder.

### Console

  1. In the Google Cloud console, open the **Manage resources** page. 

[ Open Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

  2. Click the arrow next to the organization name to expand the tree view and see its child folders.

  3. In the row of the folder you want to update, click the more_vert**Actions** menu at the end of the row, and click **Settings**.

  4. Enter the new folder name and click **Save**.




### gcloud

To update a folder's display name:
    
    
    gcloud resource-manager folders update FOLDER_ID --display-name="NEW_DISPLAY_NAME"

Replace the following:

  * `FOLDER_ID`: the ID of the folder you want to update.
  * `NEW_DISPLAY_NAME`: the new display name for the folder.



### REST

Before using any of the request data, make the following replacements: 

  * FOLDER_ID: the Google Cloud folder ID
  * NEW_DISPLAY_NAME: the new display name for the folder



HTTP method and URL: 
    
    
    PATCH https://cloudresourcemanager.googleapis.com/v3/folders/FOLDER_ID?updateMask=displayName

Request JSON body: 
    
    
    {
      "displayName": "NEW_DISPLAY_NAME"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v3/folders/FOLDER_ID?updateMask=displayName"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/folders/FOLDER_ID?updateMask=displayName" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "operations/fc.1234567890abcdef",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.resourcemanager.v3.FolderOperationMetadata",
        "displayName": "NEW_DISPLAY_NAME",
        "operationType": "UPDATE",
        "resourceName": "folders/FOLDER_ID"
      },
      "done": false
    }
    

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

To move a folder under the organization resource, run the following command in the Google Cloud CLI:
    
    
    gcloud resource-manager folders move FOLDER_ID \
        --organization=PARENT_ID

Replace the following:

  * `FOLDER_ID`: the ID of the folder you want to move.
  * `PARENT_ID`: the ID of the parent organization resource.



To move a folder under another folder:
    
    
    gcloud resource-manager folders move FOLDER_ID \
        --folder=PARENT_ID

Replace the following:

  * `FOLDER_ID`: the ID of the folder you want to move.
  * `PARENT_ID`: the ID of the parent organization resource or folder.



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
    

## Delete folders

To delete a folder, you must have the Folder Editor role (`roles/resourcemanager.folderEditor`) or the Folder Admin role (`roles/resourcemanager.folderAdmin`) on the folder.

**Note:** When you delete a folder, it enters a soft-deleted state for a 30-day retention period before being permanently deleted. You can only delete a folder if it is empty (contains no projects or sub-folders).

### Console

  1. In the Google Cloud console, open the **Manage resources** page. 

[ Open Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

In the Google Cloud console, go to the Manage resources page.
  2. Click the arrow next to the organization name to expand the tree view and see its child folders.

  3. In the row of the folder you want to delete, click the more_vert**Actions** menu at the end of the row, and click **Delete**.

  4. In the confirmation dialog, type the folder ID or name to confirm and click **Delete**.




### gcloud

To delete a folder, run the following command:
    
    
    gcloud resource-manager folders delete FOLDER_ID

Replace the following:

  * `FOLDER_ID`: the ID of the folder you want to delete.



### REST

Before using any of the request data, make the following replacements: 

  * FOLDER_ID: the Google Cloud folder ID



HTTP method and URL: 
    
    
    DELETE https://cloudresourcemanager.googleapis.com/v3/folders/FOLDER_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudresourcemanager.googleapis.com/v3/folders/FOLDER_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/folders/FOLDER_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "operations/fc.1234567890abcdef",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.resourcemanager.v3.FolderOperationMetadata",
        "operationType": "DELETE",
        "resourceName": "folders/FOLDER_ID"
      },
      "done": false
    }
    

### Additional information

When you delete a folder, it enters a soft-deleted state for a 30-day retention period before being permanently deleted, or hard-deleted.

**Soft-delete state** : During the 30-day retention period, the folder is marked for deletion and is no longer active. You can't create new projects or sub-folders within a soft-deleted folder.

**Hard-delete state** : After 30 days, Google Cloud permanently removes the folder and its metadata. This action is irreversible.

**Undelete** : If you accidentally delete a folder, you can restore it within the 30-day window using the `gcloud resource-manager folders undelete` command or the API.

Prerequisites and constraints

  * Folder must be empty: You can't delete a folder that still contains active projects or sub-folders. You must first move or delete all child resources.
  * Required permissions: To delete or undelete a folder, you must have the Folder Editor (`roles/resourcemanager.folderEditor`) or Folder Admin (`roles/resourcemanager.folderAdmin`) role.



### Search

To search for folders matching the specified query, use `gcloud alpha resource-manager folders search`, passing the condition in the `--query` flag. The scope of search is all the folders for which the user has view permission.
    
    
    gcloud alpha resource-manager folders search --query="name:vij*"
    <table output showing the folders with names starting from vij eg. vijeta, vijay-folder>
    
    gcloud alpha resource-manager folders search --query="state:DELETE_REQUESTED"
    <table output showing folders for which delete has been requested>
    

All folders for which the user has view permission can be shown using the `gcloud folders search` command.
    
    
    gcloud folders search
    <table output showing all viewable folders>
    

**Note:** The search command is in alpha and can be changed without notice.

## What's next

  * Learn about [managing projects within folders](https://docs.cloud.google.com/resource-manager/docs/manage-projects-within-folder).
  * Learn about [roles and permissions for folders](https://docs.cloud.google.com/resource-manager/docs/access-control-folders).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
