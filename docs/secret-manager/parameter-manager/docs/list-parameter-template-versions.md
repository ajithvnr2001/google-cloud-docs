---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter-template-versions/
title: View parameter template version details \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:37.764316+00:00
---

# View parameter template version details  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter-template-versions/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  View parameter template version details Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to get a list of parameter template versions and view the payload of a specific version.

A parameter template version represents the specific setting or configuration value that the parameter template holds at a given point in time. While a parameter template acts as a metadata container, the parameter template version contains the payload.

## Required roles

To get the permissions that you need to list parameter template versions, ask your administrator to grant you the [Parameter Manager Parameter Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterViewer) (`roles/parametermanager.parameterViewer`) IAM role on the parameter, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to list parameter template versions. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to list parameter template versions:

  * To list all the parameter template versions: `parametermanager.templateVersions.list`
  * To view the details of a parameter template version: `parametermanager.templateVersions.get`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List all parameter template versions

To list all the parameter template versions associated with a parameter template, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the template



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "templateVersions": [
        {
          "name": "projects/123456789012/locations/global/templates/payment_service_blueprint/versions/tv1",
          "createTime": "2026-03-02T09:42:23.775599162Z",
          "updateTime": "2026-03-16T08:02:07.849662444Z"
        },
        {
          "name": "projects/123456789012/locations/global/templates/payment_service_blueprint/versions/tv2",
          "createTime": "2026-04-14T10:41:59.677512784Z",
          "updateTime": "2026-04-14T10:42:00.186564947Z"
        }
      ]
    }
    

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * TEMPLATE_ID: the name of the template



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "templateVersions": [
        {
          "name": "projects/123456789012/locations/us-central1/templates/payment_service_blueprint/versions/tv1",
          "createTime": "2026-03-02T09:42:23.775599162Z",
          "updateTime": "2026-03-16T08:02:07.849662444Z"
        },
        {
          "name": "projects/123456789012/locations/us-central1/templates/payment_service_blueprint/versions/tv2",
          "createTime": "2026-04-14T10:41:59.677512784Z",
          "updateTime": "2026-04-14T10:42:00.186564947Z"
        }
      ]
    }
    

## View payload of a parameter template version

To view the details of a parameter template version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name to access its versions.

The template details page opens with the **Versions** tab in focus where you can see all the versions of the selected template. For each version, the version ID and its metadata are displayed in the table.

  4. To view the payload of a specific version, select the version and then click **View payload** from the more_vert**Actions** menu.

You can view the payload to verify the template configuration and see its structure




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the template
  * TEMPLATE_VERSION_ID: the ID of the template version



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789012/locations/global/templates/payment_service_blueprint/versions/tv1",
      "createTime": "2026-04-14T10:41:59.677512Z",
      "updateTime": "2026-04-14T10:42:00.186564Z",
      "payload": {
        "data": "YXBwTmFtZTogZm9yZXgtdHJhZGluZy1lbmdpbmUKZW52aXJvbm1lbnQ6IHt7LmVudn19CmxvZ0xldmVsOiB7ey5sb2dfbGV2ZWx9fQ=="
      }
    }
    

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name to access its versions.

The template details page opens with the **Versions** tab in focus where you can see all the versions of the selected template. For each version, the version ID and its metadata are displayed in the table.

  4. To view the payload of a specific version, select the version and then click **View payload** from the more_vert**Actions** menu.

You can view the payload to verify the template configuration and see its structure




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * TEMPLATE_ID: the name of the template
  * TEMPLATE_VERSION_ID: the ID of the template version



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789012/locations/us-central1/templates/payment_service_blueprint/versions/tv1",
      "createTime": "2026-04-14T10:41:59.677512Z",
      "updateTime": "2026-04-14T10:42:00.186564Z",
      "payload": {
        "data": "YXBwTmFtZTogZm9yZXgtdHJhZGluZy1lbmdpbmUKZW52aXJvbm1lbnQ6IHt7LmVudn19CmxvZ0xldmVsOiB7ey5sb2dfbGV2ZWx9fQ=="
      }
    }
    

## What's next

  * [Disable a parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-template-version)
  * [Enable a disabled parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-parameter-template-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
