---
url: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/edit-parameter/
title: Edit a parameter \u00a0|\u00a0 Parameter Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T09:57:40.475420+00:00
---

# Edit a parameter  |  Parameter Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/secret-manager/parameter-manager/docs/edit-parameter/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Secret Manager ](https://docs.cloud.google.com/secret-manager/docs)
  * [ Parameter Manager ](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/overview)



Send feedback 

#  Edit a parameter Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to edit a parameter's metadata. You can update the encryption type and the labels of a parameter. You can't edit the parameter name or value. To add a new value to your parameter, you must [add a parameter version](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/add-parameter-version).

## Required roles

To get the permissions that you need to update a parameter's metadata, ask your administrator to grant you the [Parameter Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/parametermanager#parametermanager.admin) (`roles/parametermanager.admin`) IAM role on the project, folder, or organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to update a parameter's metadata. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to update a parameter's metadata:

  * To update a parameter: `parametermanager.parameters.update`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Edit a parameter

To edit a parameter, use one of the following methods:

**Global parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. To edit a parameter, use one of the following options:

     * Locate the parameter in the list and click the more_vert**Actions** menu associated with that parameter. In the **Actions** menu, click **Edit**.

     * Click the parameter name to go to the parameter details page. On the parameter details page, click edit**Edit**.

  3. On the **Edit parameter** page, update the properties of the parameter as required, and then click **Save**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the unique name of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * KEY_RING: the name of the KMS key ring that contains the key
  * KEY_NAME: the name of the KMS key
  * LABEL_KEY=LABEL_VALUE: use a key-value pair to update a label. If the unique key already exists, its associated value is modified; otherwise, a new label is created.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters update PARAMETER_ID \
        --location=global \
        --kms-key=projects/PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
        --update-labels=LABEL_KEY=LABEL_VALUE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters update PARAMETER_ID `
        --location=global `
        --kms-key=projects/PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/KEY_NAME `
        --update-labels=LABEL_KEY=LABEL_VALUE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters update PARAMETER_ID ^
        --location=global ^
        --kms-key=projects/PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/KEY_NAME ^
        --update-labels=LABEL_KEY=LABEL_VALUE

### REST

Before using any of the request data, make the following replacements: 

  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique name of the parameter
  * LABEL_KEY: the unique name of the label
  * LABEL_VALUE: the corresponding value of the label
  * KEY_RING: the name of the KMS key ring that contains the key
  * KEY_NAME: the name of the KMS key



HTTP method and URL: 
    
    
    PATCH https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID?update_mask=labels,kmsKey

Request JSON body: 
    
    
    {
      "labels": {
        "LABEL_KEY": "LABEL_VALUE"
      },
      "kmsKey": "projects/PROJECT_ID/locations/global/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID?update_mask=labels,kmsKey"

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
        -Uri "https://parametermanager.googleapis.com/v1/projects/PROJECT_ID/locations/global/parameters/PARAMETER_ID?update_mask=labels,kmsKey" | Select-Object -Expand Content

The response returns the updated parameter. 

**Regional parameters**

### Console

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. To edit a parameter, use one of the following options:

     * Locate the parameter in the list and click the more_vert**Actions** menu associated with that parameter. In the **Actions** menu, click **Edit**.

     * Click the parameter name to go to the parameter details page. On the parameter details page, click edit**Edit**.

  3. On the **Edit parameter** page, update the properties of the parameter as required, and then click **Save**.




### gcloud

Before using any of the command data below, make the following replacements: 

  * PARAMETER_ID: the unique name of the parameter
  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * KEY_RING: the name of the KMS key ring that contains the key
  * KEY_NAME: the name of the KMS key
  * LABEL_KEY=LABEL_VALUE: use a key-value pair to update a label. If the unique key already exists, its associated value is modified; otherwise, a new label is created.



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters update PARAMETER_ID \
        --location=LOCATION \
        --kms-key=projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME \
        --update-labels=LABEL_KEY=LABEL_VALUE

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters update PARAMETER_ID `
        --location=LOCATION `
        --kms-key=projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME `
        --update-labels=LABEL_KEY=LABEL_VALUE

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud parametermanager parameters update PARAMETER_ID ^
        --location=LOCATION ^
        --kms-key=projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME ^
        --update-labels=LABEL_KEY=LABEL_VALUE

### REST

Before using any of the request data, make the following replacements: 

  * LOCATION: the Google Cloud [location](https://docs.cloud.google.com/secret-manager/docs/locations) of the parameter
  * PROJECT_ID: the Google Cloud project ID
  * PARAMETER_ID: the unique name of the parameter
  * LABEL_KEY: the unique name of the label
  * LABEL_VALUE: the corresponding value of the label
  * KEY_RING: the name of the KMS key ring that contains the key
  * KEY_NAME: the name of the KMS key



HTTP method and URL: 
    
    
    PATCH https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=labels,kmsKey

Request JSON body: 
    
    
    {
      "labels": {
        "LABEL_KEY": "LABEL_VALUE"
      },
      "kmsKey": "projects/PROJECT_ID/locations/LOCATION/keyRings/KEY_RING/cryptoKeys/KEY_NAME"
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=labels,kmsKey"

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
        -Uri "https://parametermanager.LOCATION.rep.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/parameters/PARAMETER_ID?update_mask=labels,kmsKey" | Select-Object -Expand Content

The response returns the updated parameter. 

## Edit labels for multiple parameters

  1. In the Google Cloud console, go to the **Parameter Manager** page.

[Go to Parameter Manager](https://console.cloud.google.com/security/parametermanager/parameters)

  2. Select the parameters for which you want to edit the labels.

  3. Click sell**Labels**.

  4. In the **Editing labels** side panel, update the labels as required.

  5. Click **Save**.




## What's next

  * [List and view parameter details](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/list-parameter)
  * [Enable CMEK for Parameter Manager](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/cmek)
  * [Set up Pub/Sub notifications](https://docs.cloud.google.com/secret-manager/parameter-manager/docs/pub-sub-notifications)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
