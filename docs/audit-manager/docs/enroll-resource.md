---
url: https://docs.cloud.google.com/audit-manager/docs/enroll-resource/
title: Enroll a resource for auditing \u00a0|\u00a0 Audit Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:18:52.439931+00:00
---

# Enroll a resource for auditing  |  Audit Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/audit-manager/docs/enroll-resource/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Audit Manager ](https://docs.cloud.google.com/audit-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/audit-manager/docs/overview)



Send feedback 

#  Enroll a resource for auditing Stay organized with collections  Save and categorize content based on your preferences. 

To audit your Google Cloud environment, you must enroll an organization, a folder, or a project as a resource in Audit Manager.

Enrollment accomplishes the following tasks:

  * A [Google-managed service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents) associated with Audit Manager is created, which monitors the specified resource on your behalf. The service agent's email address uses one of the following formats:

    * For organization-level enablement:
          
          service-org-ORGANIZATION_ID@gcp-sa-audit-manager.iam.gserviceaccount.com
          

    * For folder-level enablement:
          
          service-folder-FOLDER_ID@gcp-sa-audit-manager.iam.gserviceaccount.com
          

    * For project-level enablement:
          
          service-PROJECT_NUMBER@gcp-sa-audit-manager.iam.gserviceaccount.com
          

  * The specified Cloud Storage buckets are configured as the destination to store the audit data.




When you enroll a resource, its child resources are also enrolled. For example, if you enroll an organization, any projects within that organization are also enrolled. If a parent resource is already enrolled and you attempt to enroll one of its child resources, then the child resource is enrolled independently.

You can enroll resources and set up Cloud Storage buckets for auditing using Audit Manager or [Compliance Manager](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit#enroll-resources). The resources and buckets that you enroll are available for both Audit Manager and Compliance Manager to use for auditing purposes.

## Before you begin

  * Ensure that you have the following IAM roles and permissions:

    * [Audit Manager Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/auditmanager#auditmanager.admin) (`roles/auditmanager.admin`).
    * [Storage Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.admin) (`roles/storage.admin`) or [Storage Legacy Bucket Owner](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.legacyBucketOwner) (`roles/storage.legacyBucketOwner`)
  * To enroll an organization or a folder, you must have the following additional permissions:

    * Organization: `resourcemanager.organizations.setIamPolicy`
    * Folder: `resourcemanager.folders.setIamPolicy`
  * Identify or create Cloud Storage buckets where the audit data needs to be exported.

To learn about how to create Cloud Storage buckets, see [Create a bucket](https://docs.cloud.google.com/storage/docs/discover-object-storage-console#create_a_bucket).




## Enroll a resource for auditing

You can enroll an organization, a folder, or a project for auditing in Audit Manager or Compliance Manager.

The simplest way to enroll a resource is through the Google Cloud console. Alternatively, you can use the Audit Manager API, the Google Cloud CLI, or the [Compliance Manager console](https://docs.cloud.google.com/security-command-center/docs/compliance-manager-audit#enroll-resources).

### Console

  1. In the Google Cloud console, go to the **Audit Manager** page.

[Go to Audit Manager](https://console.cloud.google.com/compliance/auditmanager)

  2. Click settings**Settings**.

Depending on the resource you have selected in the project selector, a list of folders or projects are displayed on the **Settings** page.

  3. On the **Settings** page, select the resource that you want to enroll for Audit Manager, click settings**Enroll** in the **Status** column.

  4. In the **Select storage bucket details** dialog, select one or more Cloud Storage buckets where you want to save your reports and evidence, and click **Enroll**.

Your resource is now enrolled for auditing.




### gcloud

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The type of resource. Possible values are `organization`, `folder`, and `project`. 
  * `RESOURCE_ID`: The resource ID of the organization, folder, or project. For example: `8767234`. 
  * `BUCKET_URI`: The URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager enrollments add \
        --RESOURCE_TYPE=RESOURCE_ID \
        --eligible-gcs-buckets=BUCKET_URI

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager enrollments add `
        --RESOURCE_TYPE=RESOURCE_ID `
        --eligible-gcs-buckets=BUCKET_URI

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud audit-manager enrollments add ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --eligible-gcs-buckets=BUCKET_URI

### REST

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The type of resource. Possible values are `organizations`, `folders`, and `projects`. 
  * `RESOURCE_ID`: The resource ID of the organization, folder, or project. For example: `8767234`. 
  * `BUCKET_URI`: The URI of the Cloud Storage bucket. For example: `gs://testbucketauditmanager`. 



HTTP method and URL: 
    
    
    POST https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global:enrollResource

Request JSON body: 
    
    
    {
      "destinations": [
        {
          "eligibleGcsBucket": "BUCKET_URI"
        }
      ]
    }
    

To send your request, choose one of these options:

#### curl

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global:enrollResource"

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
        -Uri "https://auditmanager.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID/locations/global:enrollResource" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

If you want to change the storage location for audit data after enrollment, you need to update enrollment of your resource and specify the new storage locations. The previous enrollment and storage locations are overwritten by the new request.

## What's next

  * [Run an audit](https://docs.cloud.google.com/audit-manager/docs/run-audit).
  * [Troubleshoot enrollment issues](https://docs.cloud.google.com/audit-manager/docs/troubleshoot-enrollment-issues)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
