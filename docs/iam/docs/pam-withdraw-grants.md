---
url: https://docs.cloud.google.com/iam/docs/pam-withdraw-grants/
title: Withdraw grants \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:12.322506+00:00
---

# Withdraw grants  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-withdraw-grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Withdraw grants Stay organized with collections  Save and categorize content based on your preferences. 

****

This feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Requesters can withdraw grant requests that are pending approval or are scheduled and yet to be activated. Requesters can also end their active grants when their privileged task is complete or when the access is no longer required. 

## Withdraw your grants

### Console

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project that you want to withdraw grants from.

  3. Click the **Grants** tab, followed by the **My grants** tab. This lists your grants with grant statuses and their associated entitlement details.

  4. In the table, click more_vert **More options** for the grant that you want to withdraw, and click **Withdraw**.

  5. To confirm, click **Withdraw** again.




### gcloud

The `gcloud alpha pam grants withdraw` command withdraws a grant. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `GRANT_ID`: The ID of the grant you want to withdraw. You can retrieve the ID by [ viewing grants](https://docs.cloud.google.com/iam/docs/pam-view-grants). 
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants withdraw \
         GRANT_ID \
        --entitlement=ENTITLEMENT_ID \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants withdraw `
         GRANT_ID `
        --entitlement=ENTITLEMENT_ID `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants withdraw ^
         GRANT_ID ^
        --entitlement=ENTITLEMENT_ID ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    Parsed [grant] resource: RESOURCE_TYPE/RESOURCE_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    Grant withdrawal initiated. The operation will complete in some time.
    To track its status, run:
    `gcloud alpha pam operations wait RESOURCE_TYPE/RESOURCE_ID/locations/global/operations/OPERATION_ID`
    Note that the wait command requires you to have the `privilegedaccessmanager.operations.get` permission on the resource.
    metadata:
      apiVersion: v1
      createTime: '2024-08-20T10:10:10.101010101Z'
      target: RESOURCE_TYPE/RESOURCE_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    name: RESOURCE_TYPE/RESOURCE_ID/locations/global/operations/OPERATION_ID
    
    

### REST

The Privileged Access Manager API's `withdrawGrant` method withdraws a grant. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `GRANT_ID`: The ID of the grant you want to withdraw. You can retrieve the ID by [ viewing grants](https://docs.cloud.google.com/iam/docs/pam-view-grants). 



HTTP method and URL: 
    
    
    POST https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:withdraw

Request JSON body: 
    
    
    {
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:withdraw"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:withdraw" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "SCOPE/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1beta.OperationMetadata",
        "createTime": "2024-03-06T23:07:48.716396505Z",
        "target": "SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1beta"
      },
      "done": false
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
