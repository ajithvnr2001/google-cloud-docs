---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-template-version/
title: Add a parameter template version \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T03:09:40.148000+00:00
---

# Add a parameter template version  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-template-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Add a parameter template version Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This page describes how to add a version to an existing parameter template. A template version contains the structural data in YAML or JSON format with variables that are placeholders for instance-specific values.

### Required roles

To get the permission that you need to add a parameter template version, ask your administrator to grant you the [Parameter Manager Template Version Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.templateVersionManager) (`roles/parametermanager.templateVersionManager`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `parametermanager.templateVersions.create` permission, which is required to add a parameter template version. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Add variables to your template

You can define variables in your template version by using dot notation enclosed in double curly braces.

  * For key-value pairs, use `{{.key}}`. For example, `{{.cpuCount}}` or `{{.env}}`.
  * For nested values, use lookups in `{{.key1.key2}}` format. For example, `{{.database.port}}` or `{{.market.dataProviderName}}`.



When you render the template, Parameter Manager substitutes the variables with the values from the parameter version.

**Note:**

  * The payload must be a valid `JSON` or `YAML` object. Unformatted text is not supported.
  * You can only use direct variable substitution. Control flow statements, such as `if...else`, `loops`, or the `range` function, are not supported.
  * A single template version can contain a maximum of 64 variables.
  * Don't embed Secret Manager secrets directly in a template version. Instead, use the `__REF__()` syntax within a parameter version to reference secrets. When you render the template, Parameter Manager substitutes the variables with the values. For more information, see [Reference secrets in parameters](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/reference-secrets-in-parameter).



## Add a parameter template version

Parameter Manager lets you create multiple versions of a parameter template. Each version contains the structural data of the configuration. To add a parameter template version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Select the parameter template, and then click the **Versions** tab.

  4. Click add **Create version**. The **Create template version** page appears.

  5. Enter the version name. A template version name can be up to 63 characters long and can contain letters, numbers, dashes (-), and underscores (_). It can't begin with a dash.

  6. In the **Payload** section, enter the template version payload. Alternatively, you can upload a file containing the template version value, and then edit the values in the payload editor. The template value must be in the format specified for the parameter template.

Ensure that the payload is a valid JSON or YAML object and follows the limitations listed above.

  7. Click **Create**.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the parameter template
  * TEMPLATE_VERSION_ID: the ID of the template version
  * TEMPLATE_PAYLOAD: the Base64 encoded string corresponding to the data that you want to store within the parameter template version



HTTP method and URL: 
    
    
    POST https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions?template_version_id=TEMPLATE_VERSION_ID

Request JSON body: 
    
    
    {
      "payload": {
        "data": "TEMPLATE_PAYLOAD"
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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions?template_version_id=TEMPLATE_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions?template_version_id=TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789012/locations/global/templates/payment_service_blueprint/versions/tv1",
      "createTime": "2026-04-14T10:41:59.677512Z",
      "updateTime": "2026-04-14T10:41:59.677512Z",
      "disabled": false,
      "payload": {
        "data": "YmFzZTY0X2VuY29kZWRfcGF5bG9hZA=="
      }
    }
    

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Select the parameter template, and then click the **Versions** tab.

  4. Click add **Create version**. The **Create template version** page appears.

  5. Enter the version name. A template version name can be up to 63 characters long and can contain letters, numbers, dashes (-), and underscores (_). It can't begin with a dash.

  6. In the **Payload** section, enter the template version payload. Alternatively, you can upload a file containing the template version value, and then edit the values in the payload editor. The template value must be in the format specified for the parameter template.

Ensure that the payload is a valid JSON or YAML object and follows the limitations listed above.

  7. Click **Create**.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter template
  * TEMPLATE_ID: the name of the parameter template
  * TEMPLATE_VERSION_ID: the ID of the template version
  * TEMPLATE_PAYLOAD: the Base64 encoded string corresponding to the data that you want to store within the parameter template version



HTTP method and URL: 
    
    
    POST https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions?template_version_id=TEMPLATE_VERSION_ID

Request JSON body: 
    
    
    {
      "payload": {
        "data": "TEMPLATE_PAYLOAD"
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
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions?template_version_id=TEMPLATE_VERSION_ID"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions?template_version_id=TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/123456789012/locations/us-central1/templates/payment_service_blueprint/versions/tv1",
      "createTime": "2026-04-14T10:41:59.677512Z",
      "updateTime": "2026-04-14T10:41:59.677512Z",
      "disabled": false,
      "payload": {
        "data": "YmFzZTY0X2VuY29kZWRfcGF5bG9hZA=="
      }
    }
    

## What's next

  * [Disable a parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-template-version)
  * [Enable a disabled parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/enable-disabled-parameter-template-version)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
