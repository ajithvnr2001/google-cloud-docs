---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-template-version/
title: Render a parameter template version \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:08:27.468552+00:00
---

# Render a parameter template version  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/render-parameter-template-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Render a parameter template version Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to render a parameter template version. When you render a template version, Parameter Manager replaces variables in the template version with values from the chosen parameter version to generate the final configuration.

## Limitations

The following limitations apply when you render a parameter template version: 

  * You can select only one parameter version for the render operation. You can't select multiple parameter versions to render a template version.
  * The variables in a parameter version must meet the following requirements: 
    * A variable must be a key-value pair. For example, `{"environment": "production"}`
    * The value of a variable must not contain an array. For example, `{"tags": ["production", "west-coast", "v2"]}`
    * The value of a variable must not contain a nested key-value pair. For example, `{"database": {"host": "localhost", "port": 5432}}`
  * After the variables are substituted, the system validates the final payload to ensure it's a valid JSON or YAML object. The render operation fails if the output is invalid.
  * The final configuration payload can't exceed 1 MiB.



## Required roles

To get the permissions that you need to render a parameter template version, ask your administrator to grant you the following IAM roles on the parameter, project, folder, or organization : 

  * Access parameter templates: [Parameter Manager Template Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateAccessor) (`roles/parametermanager.templateAccessor`) 
  * Access parameters: [Parameter Manager Parameter Accessor ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterAccessor) (`roles/parametermanager.parameterAccessor`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to render a parameter template version. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to render a parameter template version:

  * Render a template version: `parametermanager.templateversions.render`
  * Render a parameter version: `parametermanager.parameterversions.render`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Render a parameter template version

To render a parameter template version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab to view the list of templates associated with the project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.

  4. Select the parameter template version that you want to render.

  5. Click the more_vert**Actions** menu associated with that version, and then click **Render**.

  6. On the **Render template version** page, select the parameter and parameter version that you want to use to render the template version.

  7. Click **Render**. A new page is displayed with the payload and the rendered value of the template version.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the parameter template
  * TEMPLATE_VERSION_ID: the ID of the parameter template version
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID:render?parameter_version=projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID:render?parameter_version=projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID:render?parameter_version=projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "templateVersion": "projects/123456789012/locations/global/templates/payment_service_blueprint/versions/tv1",
      "payload": {
        "data": "YXBwTmFtZTogZm9yZXgtdHJhZGluldmVsOiB7ey5sb2dfbGV2ZWx9fQ=="
      },
      "renderedPayload": "YXBwTmFtZTogZm9yZXgtdHJhZGluZy1lbmdpbmUKbG9nTG",
      "format": "TEMPLATE_FORMAT_YAML",
      "parameterVersion": "projects/123456789012/locations/global/parameters/prod-overrides/versions/v1"
    }
    

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab to view the list of templates associated with the project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.

  4. Select the parameter template version that you want to render.

  5. Click the more_vert**Actions** menu associated with that version, and then click **Render**.

  6. On the **Render template version** page, select the parameter and parameter version that you want to use to render the template version.

  7. Click **Render**. A new page is displayed with the payload and the rendered value of the template version.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * TEMPLATE_ID: the name of the parameter template
  * TEMPLATE_VERSION_ID: the ID of the parameter template version
  * PARAMETER_ID: the name of the parameter
  * PARAMETER_VERSION_ID: the ID of the parameter version



HTTP method and URL: 
    
    
    GET https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID:render?parameter_version=projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID

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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID:render?parameter_version=projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID:render?parameter_version=projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID/versions/PARAMETER_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "templateVersion": "projects/123456789012/locations/us-central1/templates/payment_service_blueprint/versions/tv1",
      "payload": {
        "data": "YXBwTmFtZTogZm9yZXgtdHJhZGluldmVsOiB7ey5sb2dfbGV2ZWx9fQ=="
      },
      "renderedPayload": "YXBwTmFtZTogZm9yZXgtdHJhZGluZy1lbmdpbmUKbG9nTG",
      "format": "TEMPLATE_FORMAT_YAML",
      "parameterVersion": "projects/123456789012/locations/us-central1/parameters/prod-overrides/versions/v1"
    }
    

## What's next

  * [Disable a parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-template-version)
  * [Enable a disabled parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-parameter-template-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
