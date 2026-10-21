---
url: https://docs.cloud.google.com/resource-manager/docs/view-update-projects/
title: View and update projects \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:27.690866+00:00
---

# View and update projects  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/view-update-projects/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback 

#  View and update projects Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to retrieve project metadata and modify existing project settings. You can also search for specific projects within your resource hierarchy based on their state or display names.

## Find the project name, number, and ID

To interact with Google Cloud resources, you must provide the identifying project information for every request. A project is identified by its project ID and project number.

### Console

  1. Go to the **Welcome** page in the Google Cloud console. 

[ Go to Welcome](https://console.cloud.google.com/welcome)

  2. From the project picker at the top of the page, select your project.

**Note:** Up to 4000 resources can be displayed in the project picker. If you don't see a resource that should appear, go to the **Manage resources** page and filter the list using the name of that resource.

The project name, project number, and project ID appear after the **Welcome** heading.




### gcloud

To find the project number, ID, or name, use the [`gcloud projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/describe) command:
    
    
    gcloud projects describe PROJECT_ID
    

To retrieve only the project number as a value, use the `--format` flag:
    
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"
    

## Get an existing project

To get the detailed metadata of a specific Google Cloud project, such as the project's lifecycle state, creation time, and parent resource, use the Google Cloud CLI or the API.

You must have Project Owner status or the permissions of the Browser role (`roles/browser`) to access project details.

### gcloud

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud projects describe PROJECT_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud projects describe PROJECT_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud projects describe PROJECT_ID

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID



HTTP method and URL: 
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/projects/PROJECT_ID

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v3/projects/PROJECT_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/projects/PROJECT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
        "projectNumber": "464036093014",
        "projectId": "our-project-123",
        "lifecycleState": "ACTIVE",
        "name": "my project",
        "labels": {
            "mylabel": "prod"
        },
        "createTime": "2016-01-07T21:59:43.314Z"
    }
    
    

## List all projects under a resource

To list all projects that are direct children of a resource, use the v3 [`projects.list`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/list) method and specify the parent resource in the query:

### REST

Before using any of the request data, make the following replacements: 

  * FOLDER_ID: the Google Cloud folder ID



HTTP method and URL: 
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/projects

Request JSON body: 
    
    
    {
        "parent": "folders/662951040570"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v3/projects"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/projects" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
        "projectNumber": "464036093014",
        "projectId": "our-project-123",
        "lifecycleState": "ACTIVE",
        "name": "my project",
        "labels": {
            "mylabel": "prod"
        },
        "createTime": "2016-01-07T21:59:43.314Z"
    }
    
    

## Search for projects

To find projects that match specific criteria, such as a display name prefix or a specific lifecycle state, use the [`projects.search`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/search) method or the [`gcloud alpha resource-manager projects search`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/search) command.

The scope of the search includes all projects for which you have the `resourcemanager.projects.get` permission.

**Query syntax**

You can filter your search using the `--query` flag (gcloud) or the `query` parameter (API). Common search filters include the following:

  * `displayName`: the user-friendly name of the project.
  * `state`: the lifecycle state of the project, for example, `ACTIVE` or `DELETE_REQUESTED`
  * `parent.type` and `parent.id`: filters results by a specific organization or folder.



**Permissions**

If you specify a parent in the query (for example, `parent:folders/123`), you must have `resourcemanager.projects.list` permissions on that parent. If you have this permission, all projects under the parent are returned after the remaining filters have been applied.

If you lack this permission, all projects for which you have the `resourcemanager.projects.get` permission are returned after remaining filters have been applied.

If you don't specify a parent, the results include all projects where you have `resourcemanager.projects.get` permissions.

###  Console 

You can search for projects from the **Manage resources** page:

  1. In the Google Cloud console, go to the **Manage resources** page. [Go to Manage resources](https://console.cloud.google.com/iam-admin/projects)
  2. In the **Filter** box, enter the property you want to search by, such as `name` or `ID`.
  3. Select the property from the drop-down list and enter the value you want to search for.



###  gcloud 

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha projects search --query="name:z*"

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha projects search --query="name:z*"

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud alpha projects search --query="name:z*"

You should receive a response similar to the following:
    
    
    The response contains the projects with names starting with 'z'

###  REST 

HTTP method and URL: 
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/projects:search?query=displayName%3ATokyo%2BRain

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v3/projects:search?query=displayName%3ATokyo%2BRain"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/projects:search?query=displayName%3ATokyo%2BRain" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
          "projects": [
            {
              "name": "projects/951040570662",
              "parent": "folders/662951040570",
              "projectId": "tokyo-rain-123",
              "state": "ACTIVE",
              "displayName": "Tokyo Rain",
              "createTime": "2013-11-13T20:31:53.308Z",
              "updateTime": "2013-11-13T20:31:53.308Z",
              "etag": "BwWUlZ6XEfY="
            }
          ]
    }
    

## Update projects

You can update the project name, labels, and tags. For more information about updating projects, see the [project API reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects). To update projects, use one of the following methods:

###  Console 

To update a project's name or labels using the Google Cloud console, do the following:

  1. In the Google Cloud console, go to the IAM & Admin **Settings** page. 

[Go to IAM & Admin Settings](https://console.cloud.google.com/iam-admin/settings?walkthrough_id=resource-manager--update-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. At the top of the screen, click the project selection drop-down list.
  3. On the **Select from** window that appears, click the organization drop-down list and then select your organization. If you are a free trial user, skip this step, as the organization list does not appear.
  4. Select your project from the list that appears.
  5. To change the project name, edit **Project name** , then click **Save**.
  6. To add or edit tags, go to the **Tags** section on the page, and click **Manage tags**. For information about adding or updating tags keys and values, see [Create and manage tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing).
  7. To change labels, click **Labels** on the left nav. 

Learn more about [Using Labels](https://docs.cloud.google.com/resource-manager/docs/using-labels).




###  gcloud 

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To update a project's name or labels, use the [`gcloud alpha projects update`](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/update) command:
         
         gcloud alpha projects update PROJECT_ID \
            --name=NAME \
            --update-labels=KEY=VALUE, ...

Replace the following:

     * `PROJECT_ID`: the ID of the project you want to update.
     * `NAME`: the new name you want to assign to the project.
     * `KEY`: the key of a label you want to update.
     * `VALUE`: the value of a label you want to update.

For more information and additional flags that can be used with this command, see the [Google Cloud CLI SDK](https://docs.cloud.google.com/sdk/gcloud/reference/alpha/projects/update).




### REST

To update a project, do the following:

  * Get the `project` object using the [`projects.get`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/get) method.

  * Modify the fields you want to update.

  * Call the [`projects.patch`](https://docs.cloud.google.com/resource-manager/reference/rest/v3/projects/patch) method.




The following example updates the display name of the project to `myproject` and sets the `color` label to `red`:

Request:
    
    
    PATCH https://cloudresourcemanager.googleapis.com/v3/projects/PROJECT_NUMBER?updateMask=displayName,labels
    

Where `PROJECT_NUMBER` is the numeric ID of the project you want to update.

Request JSON body:
    
    
    {
      "displayName": "myproject",
      "labels": {
        "color": "red"
      }
    }
    

Response:
    
    
    {
      "projects": [
        {
          "name": "projects/951054970012",
          "parent": "folders/662951040570",
          "projectId": "Osaka-rain-234",
          "state": "ACTIVE",
          "displayName": "myproject",
          "createTime": "2013-11-13T20:31:53.308Z",
          "updateTime": "2013-11-13T20:35:42.308Z",
          "etag": "BwWUlZ6XEfY=",
          "labels": {
            "color": "red"
          }
        }
      ]
    }
    

## What's next

  * Learn how to [move a project within your resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/moving-projects-folders).
  * Learn how to [migrate a project from one organization resource to another](https://docs.cloud.google.com/resource-manager/docs/project-migration).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
