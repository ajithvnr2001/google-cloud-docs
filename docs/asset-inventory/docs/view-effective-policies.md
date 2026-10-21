---
url: https://docs.cloud.google.com/asset-inventory/docs/view-effective-policies/
title: View effective IAM policies \u00a0|\u00a0 Cloud Asset Inventory \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:06:27.208697+00:00
---

# View effective IAM policies  |  Cloud Asset Inventory  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/asset-inventory/docs/view-effective-policies/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Cloud Asset Inventory ](https://docs.cloud.google.com/asset-inventory/docs)
  * [ Guides ](https://docs.cloud.google.com/asset-inventory/docs/asset-inventory-overview)



Send feedback 

#  View effective IAM policies Stay organized with collections  Save and categorize content based on your preferences. 

In IAM, [effective policies](https://docs.cloud.google.com/iam/docs/policies#inheritance) describe how all parent and ancestor policies in the [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy) are inherited for a resource.

Only [allow policies](https://docs.cloud.google.com/iam/docs/policies) are supported for retrieval through Cloud Asset Inventory. The following forms of access control aren't supported:

  * [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview)

  * [IAM principal access boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies)

  * [Google Kubernetes Engine role-based access control](https://docs.cloud.google.com/kubernetes-engine/docs/how-to/role-based-access-control)

  * [Cloud Storage access control lists](https://docs.cloud.google.com/storage/docs/access-control/lists)

  * [Cloud Storage public access prevention](https://docs.cloud.google.com/storage/docs/public-access-prevention)




## Before you begin

  1. Enable the Cloud Asset Inventory API in the project you're running Cloud Asset Inventory commands from.

[Enable the Cloud Asset Inventory API](https://console.cloud.google.com/apis/library/cloudasset.googleapis.com)

  2. Make sure your account has the [correct role to call the Cloud Asset Inventory API](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions#roles). For individual permissions for each call type, see [Permissions](https://docs.cloud.google.com/asset-inventory/docs/roles-permissions#permissions).




## View effective policies on resources

#### gcloud
    
    
    gcloud asset get-effective-iam-policy \
        --scope=SCOPE_PATH \
        --names=ASSET_NAME_1,ASSET_NAME_2,...

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that is the top level to check effective IAM policies from. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that is the top level to check effective IAM policies from. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that is the top level to check effective IAM policies from. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that is the top level to check effective IAM policies from. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `ASSET_NAME_#`: A comma-separated list of [asset full names](https://docs.cloud.google.com/asset-inventory/docs/asset-names). 



You can retrieve policies for a maximum of 20 assets in one batch.

See the [gcloud CLI reference](https://docs.cloud.google.com/sdk/gcloud/reference/asset/get-effective-iam-policy) for all options. 

### Example

Run the following command to view the effective IAM policies on the `my-instance` Compute Engine instance that are inherited from the organization with the ID `my-organization-id`. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"
    
    
    gcloud asset get-effective-iam-policy \
        --scope=organizations/**my-organization-id** \
        --names=//compute.googleapis.com/projects/**my-project** /zones/**us-central1-a** /instances/**my-instance**

#### Example response
    
    
    policyResults:
    - fullResourceName: //compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/my-instance
      policies:
      - attachedResource: //cloudresourcemanager.googleapis.com/projects/my-project
        policy:
          bindings:
          - members:
            - user:alex@example.com
            - user:bola@example.com
            role: roles/cloudkms.admin
          - members:
            - serviceAccount:000000000000-compute@developer.gserviceaccount.com
            role: roles/editor
      - attachedResource: //cloudresourcemanager.googleapis.com/folders/000000000000
        policy:
          bindings:
          - members:
            - user:cruz@example.com
            role: roles/resourcemanager.folderAdmin
          - members:
            - user:dani@example.com
            role: roles/resourcemanager.folderEditor
      - attachedResource: //cloudresourcemanager.googleapis.com/organizations/0000000000000
        policy:
          bindings:
          - members:
            - user:hao@example.com
            role: organizations/0000000000000/roles/CustomProjectAdmin
          - members:
            - serviceAccount:000000000000@cloudservices.gserviceaccount.com
            - user:ira@example.com
            - user:jie@example.com
            role: roles/accesscontextmanager.policyAdmin
    

#### REST

HTTP method and URL:
    
    
    POST https://cloudasset.googleapis.com/v1/SCOPE_PATH/effectiveIamPolicies:batchGet
    

**Note** : You can use a `GET` method for this request with parameters as a query string. However, the request URL is [length limited](https://docs.cloud.google.com/apis/docs/http#long_request_urls), meaning the server rejects the request if the query string is too long. To avoid length restrictions, use a `POST` request instead, set a header of `X-HTTP-Method-Override: GET`, and use a JSON body for your parameters. 

Request JSON body:
    
    
    {
      "names": [
        "ASSET_NAME_1",
        "ASSET_NAME_2",
        "..."
      ]
    }

Provide the following values:

  * `SCOPE_PATH`: Use one of the following values:

    * `projects/PROJECT_ID`, where `PROJECT_ID` is the ID of the project that is the top level to check effective IAM policies from. 
    * `projects/PROJECT_NUMBER`, where `PROJECT_NUMBER` is the number of the project that is the top level to check effective IAM policies from. 

How to find a Google Cloud project number

### Google Cloud console

To find a Google Cloud project number, complete the following steps:

      1. Go to the **Welcome** page in the Google Cloud console.

[ Go to Welcome](https://console.cloud.google.com/welcome)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box, and then search for your project name. The project name, project number, and project ID are shown near the **Welcome** heading. 

Up to 4,000 resources are displayed. If you don't see the project you're looking for, go to the [**Manage resources**](https://console.cloud.google.com//cloud-resource-manager) page and filter the list using the name of that project. 

### gcloud CLI

You can retrieve a Google Cloud project number with the following command:
    
    gcloud projects describe PROJECT_ID --format="value(projectNumber)"

    * `folders/FOLDER_ID`, where `FOLDER_ID` is the ID of the folder that is the top level to check effective IAM policies from. 

How to find the ID of a Google Cloud folder

### Google Cloud console

To find the ID of a Google Cloud folder, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Search for your folder name. The folder ID is shown next to the folder name.

### gcloud CLI

You can retrieve the ID of a Google Cloud folder that's located at the organization level with the following command:
    
    gcloud resource-manager folders list \
        --organization=$(gcloud organizations describe ORGANIZATION_NAME \
          --format="value(name.segment(1))") \
        --filter='"DISPLAY_NAME":"TOP_LEVEL_FOLDER_NAME"' \
        --format="value(ID)"

Where TOP_LEVEL_FOLDER_NAME is a partial or full string match for the folder's name. Remove the `--format` flag to see more information about the found folders.

The previous command doesn't return the IDs of subfolders within folders. To do so, run the following command using a top level folder's ID:
    
    gcloud resource-manager folders list --folder=FOLDER_ID

    * `organizations/ORGANIZATION_ID`, where `ORGANIZATION_ID` is the ID of the organization that is the top level to check effective IAM policies from. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

      1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

      2. Click the **switcher** list box in the menu bar.
      3. Select your organization from the list box.
      4. Click the **All** tab. The organization ID is shown next to the organization name.

### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

  * `ASSET_NAME_#`: An array of [ asset full names](https://docs.cloud.google.com/asset-inventory/docs/asset-names). 



You can retrieve policies for a maximum of 20 assets in one batch.

See the [REST reference](https://docs.cloud.google.com/asset-inventory/docs/reference/rest/v1/effectiveIamPolicies/batchGet) for all options.

### Command examples

Run one of the following commands to view the effective IAM policies on the `my-instance` Compute Engine instance that are inherited from the organization with the ID `my-organization-id`. 

How to find the ID of a Google Cloud organization

### Google Cloud console

To find the ID of a Google Cloud organization, complete the following steps:

  1. Go to the Google Cloud console.

[ Go to the Google Cloud console ](https://console.cloud.google.com/)

  2. Click the **switcher** list box in the menu bar.
  3. Select your organization from the list box.
  4. Click the **All** tab. The organization ID is shown next to the organization name.



### gcloud CLI

You can retrieve the ID of a Google Cloud organization with the following command:
    
    
    gcloud organizations describe ORGANIZATION_NAME --format="value(name.segment(1))"

#### curl (Linux, macOS, or Cloud Shell)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login), or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the gcloud CLI. You can check the active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    curl -X POST \
         -H "X-HTTP-Method-Override: GET" \
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \
         -H "Content-Type: application/json; charset=utf-8" \
         -d '{
                "names": [
                  "//compute.googleapis.com/projects/**my-project** /zones/**us-central1-a** /instances/**my-instance** "
                ]
              }' \
         https://cloudasset.googleapis.com/v1/organizations/my-organization-id/effectiveIamPolicies:batchGet

#### PowerShell (Windows)

**Note** : The following command assumes that you have logged in to the gcloud CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [ `gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login). You can check the active account by running [ `gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 
    
    
    $cred = gcloud auth print-access-token
    
    $headers = @{ 
      "X-HTTP-Method-Override" = "GET";
      "Authorization" = "Bearer $cred"
    }
    
    
    $body = @"
    {
      "names": [
        "//compute.googleapis.com/projects/**my-project** /zones/**us-central1-a** /instances/**my-instance** "
      ]
    }
    "@
    
    Invoke-WebRequest `
      -Method POST `
      -Headers $headers `
      -ContentType: "application/json; charset=utf-8" `
      -Body $body `
      -Uri "https://cloudasset.googleapis.com/v1/organizations/my-organization-id/effectiveIamPolicies:batchGet" | Select-Object -Expand Content

#### Example response
    
    
    {
      "policyResults": [
        {
          "fullResourceName": "//compute.googleapis.com/projects/my-project/zones/us-central1-a/instances/instance-1",
          "policies": [
            {
              "attachedResource": "//cloudresourcemanager.googleapis.com/projects/my-project",
              "policy": {
                "bindings": [
                  {
                    "role": "roles/cloudkms.admin",
                    "members": [
                      "user:alex@example.com",
                      "user:bola@example.com"
                    ]
                  },
                  {
                    "role": "roles/editor",
                    "members": [
                      "serviceAccount:000000000000-compute@developer.gserviceaccount.com"
                    ]
                  }
                ]
              }
            },
            {
              "attachedResource": "//cloudresourcemanager.googleapis.com/folders/000000000000",
              "policy": {
                "bindings": [
                  {
                    "role": "roles/resourcemanager.folderAdmin",
                    "members": [
                      "user:cruz@example.com"
                    ]
                  },
                  {
                    "role": "roles/resourcemanager.folderEditor",
                    "members": [
                      "user:dani@example.com"
                    ]
                  }
                ]
              }
            },
            {
              "attachedResource": "//cloudresourcemanager.googleapis.com/organizations/000000000000",
              "policy": {
                "bindings": [
                  {
                    "role": "organizations/1060291660910/roles/CustomProjectAdmin",
                    "members": [
                      "user:hao@example.com"
                    ]
                  },
                  {
                    "role": "roles/accesscontextmanager.policyAdmin",
                    "members": [
                      "serviceAccount:000000000000@cloudservices.gserviceaccount.com",
                      "user:ira@example.com",
                      "user:jie@example.com"
                    ]
                  }
                ]
              }
            }
          ]
        }
      ]
    }

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
