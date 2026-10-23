---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/delete-parameter-template-version/
title: Delete parameter template versions \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:41.802571+00:00
---

# Delete parameter template versions  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/delete-parameter-template-version/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Delete parameter template versions Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how to delete a parameter template version.

Consider deleting a parameter template version in the following scenarios:

  * The parameter template version is obsolete and is no longer needed.
  * The parameter template version contains sensitive information that needs to be permanently removed.
  * You want to simplify the management of parameter template versions by deleting old and unused versions.

**Note:** If you want to retain a record for audits but want to prevent further use, disable the template version instead of deleting. For more information, see [Disable a parameter template version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/disable-parameter-template-version).

## Required roles

To get the permission that you need to delete a parameter template version, ask your administrator to grant you the [Parameter Manager Parameter Version Manager ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.parameterVersionManager) (`roles/parametermanager.parameterVersionManager`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `parametermanager.templateversions.delete` permission, which is required to delete a parameter template version. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Delete a parameter template version

To delete a parameter version, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.

  4. Select the template version that you want to delete.

  5. Click the more_vert**Actions** menu associated with that template version, and then click **Delete**.

  6. In the confirmation dialog that appears, enter the TEMPLATE_ID to confirm, and then click **Delete**.




### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the template
  * TEMPLATE_VERSION_ID: the ID of the template version



HTTP method and URL: 
    
    
    DELETE https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X DELETE \  
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
        -Method DELETE `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    
    

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Navigate to the **Templates** tab. You'll see the list of templates for that project.

  3. Click the template name. The template details page opens to the **Versions** tab, which lists all versions of the template.

  4. Select the template version that you want to delete.

  5. Click the more_vert**Actions** menu associated with that template version, and then click **Delete**.

  6. In the confirmation dialog that appears, enter the TEMPLATE_ID to confirm, and then click **Delete**.




### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter template
  * PROJECT_ID: the Google Cloud project ID
  * TEMPLATE_ID: the name of the template
  * TEMPLATE_VERSION_ID: the ID of the template version



HTTP method and URL: 
    
    
    DELETE https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID

Request JSON body: 
    
    
    {}
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID"

#### PowerShell

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/templates/TEMPLATE_ID/versions/TEMPLATE_VERSION_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {}
    
    

## What's next

  * [View audit logs](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/audit-logging)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
