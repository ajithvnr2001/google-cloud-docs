---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-and-manage-tags/
title: Create and manage tags \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:43.277352+00:00
---

# Create and manage tags  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/create-and-manage-tags/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Create and manage tags Stay organized with collections  Save and categorize content based on your preferences. 

This guide describes how to create and manage tags on parameters in Google Cloud Parameter Manager. You can use tags to group related parameters and store metadata about those resources based on their tags.

## About tags

A tag is a key-value pair that you can attach to a resource within Google Cloud. You can use tags to conditionally allow or deny policies based on whether a resource has a specific tag. For example, you can conditionally grant Identity and Access Management (IAM) roles based on whether a resource has a specific tag. For more information, see the [Tags overview](https://docs.cloud.google.com/resource-manager/docs/tags/tags-overview).

Tags are attached to resources by creating a tag binding resource that links the value to the Google Cloud resource.

## Required permissions

To get the permissions that you need to manage tags, ask your administrator to grant you the following IAM roles:

  * [Tag Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagViewer) (`roles/resourcemanager.tagViewer`) on the resources the tags are attached to
  * View and manage tags at the organization level: [Organization Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationViewer) (`roles/resourcemanager.organizationViewer`) on the organization
  * Create, update, and delete tag definitions: [Tag Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagAdmin) (`roles/resourcemanager.tagAdmin`) on the resource you're creating, updating, or deleting tags for
  * Attach and remove tags from resources: [Tag User](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.tagUser) (`roles/resourcemanager.tagUser`) on the tag value and the resources that you're attaching the tag value to or removing it from



To attach tags to Parameter Manager parameters, you need the [Parameter Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) role (`roles/parametermanager.admin`) or a custom role containing the following permissions:

  * `parametermanager.googleapis.com/parameters.createTagBinding`
  * `parametermanager.googleapis.com/parameters.deleteTagBinding`
  * `parametermanager.googleapis.com/parameters.listTagBindings`
  * `parametermanager.googleapis.com/parameters.listEffectiveTags`



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). You might also be able to get the required permissions through custom roles or other predefined roles.

## Create tag keys and values

Before you can attach a tag, you need to create a tag key and configure its value. For more information, see [create a tag key](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#creating_tag) and [add tag values](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#add_tag_values).

## Add tags during resource creation

You can add tags when you create parameters. Doing so lets you provide essential metadata for your resources and allows for better organization, cost tracking, and automated policy application.

**Global parameters**

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter
  * TAG_KEY: the namespaced name of the tag key to attach, for example, `123456789012/environment`
  * TAG_VALUE: the short name of the tag value to attach, for example, `production`.



To specify multiple tags, add other key-value pairs to the `tags` object.

HTTP method and URL: 
    
    
    POST https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameterId=PARAMETER_ID

Request JSON body: 
    
    
    {
      "tags": {
        "TAG_KEY": "TAG_VALUE"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameterId=PARAMETER_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters?parameterId=PARAMETER_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and a response containing the details of the created parameter.

**Regional parameters**

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the location of your resource, for example `us-central1`
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter
  * TAG_KEY: the namespaced name of the tag key to attach, for example, `123456789012/environment`
  * TAG_VALUE: the short name of the tag value to attach, for example, `production`



To specify multiple tags, add other key-value pairs to the `tags` object.

HTTP method and URL: 
    
    
    POST https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameterId=PARAMETER_ID

Request JSON body: 
    
    
    {
      "tags": {
        "TAG_KEY": "TAG_VALUE"
      }
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameterId=PARAMETER_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters?parameterId=PARAMETER_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and a response containing the details of the created parameter.

## Add tags to existing resources

To add a tag to existing parameters, follow these steps:

**Global parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

  * TAG_VALUE: the permanent ID or namespaced name of the tag value that's attached. For example, `tagValues/567890123456`.
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAG_VALUE \
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create `
        --tag-value=TAG_VALUE `
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create ^
        --tag-value=TAG_VALUE ^
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter
  * TAG_VALUE: the permanent ID or namespaced name of the tag value that is attached. For example, `tagValues/567890123456`.



HTTP method and URL: 
    
    
    POST https://cloudresourcemanager.googleapis.com/v3/tagBindings

Request JSON body: 
    
    
    {
      "parent": "//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID",
      "tagValue": "TAG_VALUE"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudresourcemanager.googleapis.com/v3/tagBindings"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/tagBindings" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

**Regional parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

  * TAG_VALUE: the permanent ID or namespaced name of the tag value that's attached. For example, `tagValues/567890123456`.
  * PROJECT_ID: the Google Cloud project ID
  * LOCATION: the location of your resource, for example, `us-central1`
  * PARAMETER_ID: the unique identifier of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create \
        --tag-value=TAG_VALUE \
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create `
        --tag-value=TAG_VALUE `
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings create ^
        --tag-value=TAG_VALUE ^
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID ^
        --location=LOCATION

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the location of your resource, for example, `us-central1`
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter
  * TAG_VALUE: the permanent ID or namespaced name of the tag value to attach, for example, `tagValues/567890123456`



HTTP method and URL: 
    
    
    POST https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings

Request JSON body: 
    
    
    {
      "parent": "//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID",
      "tagValue": "TAG_VALUE"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## List tags attached to resources

You can view a list of tag bindings directly attached to or inherited by the parameter.

**Global parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter



To list inherited tags, append the `--effective` flag.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list \
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list `
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list ^
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter



HTTP method and URL: 
    
    
    GET https://cloudresourcemanager.googleapis.com/v3/tagBindings?parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudresourcemanager.googleapis.com/v3/tagBindings?parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/tagBindings?parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

**Regional parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * LOCATION: the location of your resource, for example, `us-central1`
  * PARAMETER_ID: the unique identifier of the parameter



To list inherited tags, append the `--effective` flag.

Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list \
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list `
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings list ^
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID ^
        --location=LOCATION

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the location of your resource, for example, `us-central1`
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter



HTTP method and URL: 
    
    
    GET https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings?parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings?parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings?parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Detach tags from resources

You can detach tags that have been directly attached to a parameter. Inherited tags can be overridden by attaching a tag with the same key and a different value, but they can't be detached.

**Global parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

  * TAG_VALUE: the permanent ID or namespaced name of the tag value to detach. For example, `tagValues/567890123456`.
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique identifier of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAG_VALUE \
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete `
        --tag-value=TAG_VALUE `
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete ^
        --tag-value=TAG_VALUE ^
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID

### REST

Before using any of the request data, make the following replacements: 

  * TAG_BINDING_NAME: the name of the tag binding to delete



HTTP method and URL: 
    
    
    DELETE https://cloudresourcemanager.googleapis.com/v3/tagBindings/TAG_BINDING_NAME

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://cloudresourcemanager.googleapis.com/v3/tagBindings/TAG_BINDING_NAME"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://cloudresourcemanager.googleapis.com/v3/tagBindings/TAG_BINDING_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

**Regional parameters**

### gcloud

Before using any of the command data below, make the following replacements: 

  * TAG_VALUE: the permanent ID or namespaced name of the tag value to detach. For example, `tagValues/567890123456`.
  * PROJECT_ID: the Google Cloud project ID
  * LOCATION: the location of your resource, for example, `us-central1`
  * PARAMETER_ID: the unique identifier of the parameter



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete \
        --tag-value=TAG_VALUE \
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID \
        --location=LOCATION

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete `
        --tag-value=TAG_VALUE `
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID `
        --location=LOCATION

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud resource-manager tags bindings delete ^
        --tag-value=TAG_VALUE ^
        --parent=//parametermanager.googleapis.com/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID ^
        --location=LOCATION

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the location of your resource, for example `us-central1`
  * TAG_BINDING_NAME: the name of the tag binding to delete



HTTP method and URL: 
    
    
    DELETE https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings/TAG_BINDING_NAME

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings/TAG_BINDING_NAME"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://LOCATION-cloudresourcemanager.googleapis.com/v3/tagBindings/TAG_BINDING_NAME" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Delete tag keys and values

When removing a tag key or value definition, ensure that the tag is detached from all parameters. You must delete existing tag attachments, called tag bindings, before deleting the tag definition itself. For more information, see [Deleting tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#deleting).

## IAM conditions and tags

You can use tags and IAM conditions to conditionally grant role bindings to users in your hierarchy. Changing or deleting the tag attached to a resource can remove user access to that resource if an IAM policy with conditional role bindings has been applied. For more information, see [IAM conditions and tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-creating-and-managing#iam_conditions_and_tags).

## What's next

  * See the other [services that support tags](https://docs.cloud.google.com/resource-manager/docs/tags/tags-supported-services).
  * See [Tags and access control](https://docs.cloud.google.com/iam/docs/tags-access-control) to learn how to use tags with IAM.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
