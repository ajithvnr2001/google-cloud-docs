---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-parameter-template-version/
title: Enable a disabled parameter template version \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:41.499741+00:00
---

# Enable a disabled parameter template version  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-parameter-template-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Enable a disabled parameter template version Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to enable a disabled parameter template version.

You might want to enable a previously disabled parameter template version for the following reasons:

  * To diagnose a problem with your current configuration, you might re-enable a disabled parameter template version that was known to work correctly.
  * To reuse previous configurations as your requirements change.
  * To restore a temporary configuration that you might have disabled after use.



## Required roles

To get the permission that you need to enable a disabled parameter template version, ask your administrator to grant you the [Parameter Manager Parameter Version Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`) IAM role on the parameter, project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `parametermanager.templateversions.update` permission, which is required to enable a disabled parameter template version. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable a disabled parameter template version

To enable a disabled parameter template version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.

  4. Select the template version that you want to enable.

  5. Click the more_vert**Actions** menu associated with that template version, and then click **Enable**.

  6. In the confirmation dialog that appears, click **Enable**.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the template
  * TEMPLATE_VERSION_ID: the ID of the template version



HTTP method and URL: 
    
    
    PATCH https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID

Request JSON body: 
    
    
    {
      "disabled": false
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
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
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789012/locations/global/templates/payment_service_blueprint/versions/tv1",
      "createTime": "2026-04-10T15:01:23.045123Z",
      "updateTime": "2026-04-14T20:42:33.992450Z",
      "disabled": false,
      "payload": {
        "data": "YXBwTmFtZTogZm9yZXgtdHJhZGluZy1lbmdpbmUKZW52aXJvbm1lbnQ6IHt7LmVudn19CmxvZ0xldmVsOiB7ey5sb2dfbGV2ZWx9fQ=="
      }
    }
    

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.

  4. Select the template version that you want to enable.

  5. Click the more_vert**Actions** menu associated with that template version, and then click **Enable**.

  6. In the confirmation dialog that appears, click **Enable**.




### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the template
  * TEMPLATE_VERSION_ID: the ID of the template version



HTTP method and URL: 
    
    
    PATCH https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID

Request JSON body: 
    
    
    {
      "disabled": false
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
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
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789012/locations/us-central1/templates/payment_service_blueprint/versions/tv1",
      "createTime": "2026-04-10T15:01:23.045123Z",
      "updateTime": "2026-04-14T20:42:33.992450Z",
      "disabled": false,
      "payload": {
        "data": "YXBwTmFtZTogZm9yZXgtdHJhZGluZy1lbmdpbmUKZW52aXJvbm1lbnQ6IHt7LmVudn19CmxvZ0xldmVsOiB7ey5sb2dfbGV2ZWx9fQ=="
      }
    }
    

## What's next

  * [Delete a parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/delete-parameter-template-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
