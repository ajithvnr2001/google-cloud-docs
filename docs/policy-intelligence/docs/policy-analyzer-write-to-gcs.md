---
url: https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-write-to-gcs/
title: Write policy analysis to Cloud Storage \u00a0|\u00a0 Policy Intelligence \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:59:00.184246+00:00
---

# Write policy analysis to Cloud Storage  |  Policy Intelligence  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/policy-intelligence/docs/policy-analyzer-write-to-gcs/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Policy Intelligence ](https://docs.cloud.google.com/policy-intelligence/docs)
  * [ Guides ](https://docs.cloud.google.com/policy-intelligence/docs/overview)



Send feedback 

#  Write policy analysis to Cloud Storage Stay organized with collections  Save and categorize content based on your preferences. 

This page explains how to analyze Identity and Access Management (IAM) policies asynchronously and write results to Cloud Storage. The functionality is mostly equivalent to [analyzing IAM policies](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies) except the analysis result is written to a [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets).

## Before you begin

Enable the Cloud Asset API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudasset.googleapis.com&redirect=https%3A//console.cloud.google.com)

You must enable the API in the project you will use to send the query. This doesn't have to be the same resource that you scope your query to.

## Required roles and permissions

The following roles and permissions are required to run a policy analysis and export the results to Cloud Storage.

### Required IAM roles

To get the permissions that you need to analyze a policy and export the results to BigQuery, ask your administrator to grant you the following IAM roles on the project, folder, or organization that you will scope your query to: 

  * [Cloud Asset Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/cloudasset#cloudasset.viewer) (`roles/cloudasset.viewer`)
  * [Storage Object Creator ](https://docs.cloud.google.com/iam/docs/roles-permissions/storage#storage.objectCreator) (`roles/storage.objectCreator`)
  * To analyze policies with [custom IAM roles](https://docs.cloud.google.com/iam/docs/understanding-custom-roles): [Role Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.roleViewer) (`roles/iam.roleViewer`) 
  * To use the Google Cloud CLI to analyze policies: [Service Usage Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/serviceusage#serviceusage.serviceUsageConsumer) (`roles/serviceusage.serviceUsageConsumer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to analyze a policy and export the results to BigQuery. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to analyze a policy and export the results to BigQuery:

  * `cloudasset.assets.analyzeIamPolicy`
  * `cloudasset.assets.searchAllResources`
  * `cloudasset.assets.searchAllIamPolicies`
  * `storage.objects.create`
  * To analyze policies with custom IAM roles: `iam.roles.get`
  * To use the Google Cloud CLI to analyze policies: `serviceusage.services.use`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Required Google Workspace permissions

If you want to see if a principal has certain roles or permissions as a result of their membership in a Google Workspace group, you need the `groups.read` Google Workspace permission. This permission is contained in the Groups Reader Admin role, and in more powerful roles such as the Groups Admin or Super Admin roles. See [Assign specific admin roles](https://support.google.com/a/answer/9807615) for more information.

## Analyze policies and export results

The [`AnalyzeIamPolicyLongrunning`](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning) method allows you to issue an analysis request and get results in the specified [Cloud Storage bucket](https://docs.cloud.google.com/storage/docs/buckets).

### gcloud

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the resource that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Use the value `project`, `folder`, or `organization`. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `PRINCIPAL`: The principal whose access you want to analyze, in the form `PRINCIPAL_TYPE:ID`—for example, `user:my-user@example.com`. For a full list of the principal types, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 
  * `PERMISSIONS`: A comma-separated list of the permissions that you want to check for—for example, `compute.instances.get,compute.instances.start`. If you list multiple permissions, Policy Analyzer will check for any of the permissions listed.
  * `STORAGE_OBJECT_URI`: The unique resource identifier of the Cloud Storage object that you want to export analysis results to, in the form `gs://BUCKET_NAME/OBJECT_NAME`—for example, `gs://my-bucket/analysis.json`. 

**Note:** If you want more detailed query results, you can [enable advanced options](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#options). 

Execute the [gcloud asset analyze-iam-policy-longrunning](https://docs.cloud.google.com/sdk/gcloud/reference/asset/analyze-iam-policy-longrunning) command: 

#### Linux, macOS, or Cloud Shell

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset analyze-iam-policy-longrunning --RESOURCE_TYPE=RESOURCE_ID \
        --full-resource-name=FULL_RESOURCE_NAME \
        --identity=PRINCIPAL \
        --permissions='PERMISSIONS' \
        --gcs-output-path=STORAGE_OBJECT_URI

#### Windows (PowerShell)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). 
    
    
    gcloud asset analyze-iam-policy-longrunning --RESOURCE_TYPE=RESOURCE_ID `
        --full-resource-name=FULL_RESOURCE_NAME `
        --identity=PRINCIPAL `
        --permissions='PERMISSIONS' `
        --gcs-output-path=STORAGE_OBJECT_URI

#### Windows (cmd.exe)

**Note:** Ensure you have initialized the Google Cloud CLI with authentication and a project by running either [gcloud init](https://docs.cloud.google.com/sdk/gcloud/reference/init); or [gcloud auth login](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) and [gcloud config set project](https://docs.cloud.google.com/sdk/gcloud/reference/config/set). **Note:** If this command uses `'` for quoting content, replace these single quotes with double quotes. If quoting is nested, use `\"` to escape the inner quotes. 
    
    
    gcloud asset analyze-iam-policy-longrunning --RESOURCE_TYPE=RESOURCE_ID ^
        --full-resource-name=FULL_RESOURCE_NAME ^
        --identity=PRINCIPAL ^
        --permissions='PERMISSIONS' ^
        --gcs-output-path=STORAGE_OBJECT_URI

You should receive a response similar to the following:
    
    
    Analyze IAM Policy in progress.
    Use [gcloud asset operations describe projects/my-project/operations/AnalyzeIamPolicyLongrunning/1195028485971902504711950280359719028666] to check the status of the operation.
    

### REST

To analyze an IAM allow policy and export the results to Cloud Storage, use the Cloud Asset Inventory API's `[analyzeIamPolicyLongrunning](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning)` method. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the resource that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Use the value `projects`, `folders`, or `organizations`. 
  * `RESOURCE_ID`: The ID of the Google Cloud project, folder, or organization that you want to scope your search to. Only IAM allow policies attached to this resource and to its descendants will be analyzed. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `FULL_RESOURCE_NAME`: Optional. The full resource name of the resource that you want to analyze access for. For a list of full resource name formats, see [Resource name format](https://docs.cloud.google.com/asset-inventory/docs/resource-name-format). 
  * `PRINCIPAL`: Optional. The principal whose access you want to analyze, in the form `PRINCIPAL_TYPE:ID`—for example, `user:my-user@example.com`. For a full list of the principal types, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers). 
  * `PERMISSION_1`, `PERMISSION_2`... `PERMISSION_N`: Optional. The permissions that you want to check for—for example, `compute.instances.get`. If you list multiple permissions, Policy Analyzer will check for any of the permissions listed. 
  * `STORAGE_OBJECT_URI`: The unique resource identifier of the Cloud Storage object that you want to export analysis results to, in the form `gs://BUCKET_NAME/OBJECT_NAME`—for example, `gs://my-bucket/analysis.json`. 

**Note:** If you want more detailed query results, you can [enable advanced options](https://docs.cloud.google.com/policy-intelligence/docs/analyze-iam-policies#options). 

HTTP method and URL: 
    
    
    POST https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID:analyzeIamPolicyLongrunning

Request JSON body: 
    
    
    {
      "analysisQuery": {
        "resourceSelector": {
          "fullResourceName": "FULL_RESOURCE_NAME"
        },
        "identitySelector": {
          "identity": "PRINCIPAL"
        },
        "accessSelector": {
          "permissions": [
            "PERMISSION_1",
            "PERMISSION_2",
            "PERMISSION_N"
          ]
        },
        "outputConfig": {
          "gcsDestination": {
            "uri": "STORAGE_OBJECT_URI"
          }
        }
      }
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID:analyzeIamPolicyLongrunning"

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
        -Uri "https://cloudasset.googleapis.com/v1/RESOURCE_TYPE/RESOURCE_ID:analyzeIamPolicyLongrunning" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/TopLevel/analyzeIamPolicyLongrunning). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/operations/AnalyzeIamPolicyLongrunning/1206385342502762515812063858425027606003",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.asset.v1.AnalyzeIamPolicyLongrunningMetadata",
        "createTime": "2022-04-12T21:31:10.753173929Z"
      }
    }
    

## View IAM policy analysis results

To view your IAM policy analysis results:

  1. In the Google Cloud console, go to the **Buckets** page.

[Go to Buckets](https://console.cloud.google.com/storage/browser)

  2. Open the new file you wrote your analysis to.




The results lists tuples of `{identity, role(s)/permission(s), resource}` together with IAM policies that generate those tuples.

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
