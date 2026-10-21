---
url: https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests/
title: Manage change requests with governance workflows \u00a0|\u00a0 Knowledge Catalog \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T04:37:35.385977+00:00
---

# Manage change requests with governance workflows  |  Knowledge Catalog  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/knowledge-catalog/docs/manage-requests/

As of April 10, 2026, Dataplex Universal Catalog is now called Knowledge Catalog. The API, client library, CLI, and IAM names remain unchanged. For more information, see [Introducing the Google Cloud Knowledge Catalog](https://docs.cloud.google.com/blog/products/data-analytics/introducing-the-google-cloud-knowledge-catalog). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Knowledge Catalog ](https://docs.cloud.google.com/knowledge-catalog/docs)
  * [ Guides ](https://docs.cloud.google.com/knowledge-catalog/docs/introduction)



Send feedback 

#  Manage change requests with governance workflows Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

This document describes how requesters, approvers, and workflow administrators manage governance requests in Knowledge Catalog.

## Before you begin

To use governance workflows, ensure that you have enabled the required APIs and that approvers and administrators have the necessary Identity and Access Management (IAM) roles and permissions.

Enable the Dataplex API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=dataplex.googleapis.com)

### Required roles

To get the permissions that you need to use governance workflows, ask your administrator to grant you the following IAM roles on your project: 

  * Search for data products: [Dataplex Catalog Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.catalogViewer) (`roles/dataplex.catalogViewer`) 
  * Search for data assets and request access: [Dataplex Data Products Consumer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsConsumer) (`roles/dataplex.dataProductsConsumer`) 
  * Read-only access to view data product definitions and metadata: [Dataplex Data Products Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsViewer) (`roles/dataplex.dataProductsViewer`) 
  * Approve data product access requests: 
    * [Dataplex Data Products Editor ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsEditor) (`roles/dataplex.dataProductsEditor`)
    * [Dataplex Data Products Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.dataProductsAdmin) (`roles/dataplex.dataProductsAdmin`)
    * [Dataplex Workflow Approver ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowApprover) (`roles/dataplex.workflowApprover`)
  * Administer governance workflows: [Dataplex Workflow Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/dataplex#dataplex.workflowAdmin) (`roles/dataplex.workflowAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

You might also be able to get the required permissions through [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

For more information, see [Knowledge Catalog IAM roles](https://docs.cloud.google.com/knowledge-catalog/docs/iam-roles).

## Manage requests as a requester

As a requester, you initiate change requests, such as requesting access to data products. After submitting a request, you can monitor its progress, view request details, edit details for pending requests in the `NEW` state, or delete requests before an approver addresses them.

### View authored requests

To list all requests you have created, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **My requests** tab to view a list that displays all your past and pending requests.




###  REST 

### View authored requests

To get a list of the requests you authored:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists (for example, `us-central1`).
  * `USER_EMAIL`: your email address.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests?filter=author=USER_EMAIL

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests?filter=author=USER_EMAIL"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests?filter=author=USER_EMAIL" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "changeRequests": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/changeRequests/sample-change-request-1",
          "uid": "123e4567-e89b-12d3-a456-426614174000",
          "createTime": "2026-07-20T10:00:00Z",
          "updateTime": "2026-07-20T10:00:00Z",
          "justification": "Proposing a new glossary term definition for business accuracy.",
          "author": "USER_EMAIL",
          "state": "NEW",
          "resource": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
          "createGlossaryTerm": {
            "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
            "termId": "sample-term-id",
            "term": {
              "displayName": "Sample term name",
              "description": "Sample term description",
              "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary"
            }
          }
        }
      ]
    }
    

### View a specific request

To view a specific request:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists (for example, `us-central1`).
  * `CHANGE_REQUEST_ID`: the ID of the request.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID",
      "uid": "123e4567-e89b-12d3-a456-426614174000",
      "createTime": "2026-07-20T10:00:00Z",
      "updateTime": "2026-07-20T10:00:00Z",
      "justification": "Proposing a new glossary term definition for business accuracy.",
      "author": "user@example.com",
      "state": "NEW",
      "resource": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
      "createGlossaryTerm": {
        "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
        "termId": "sample-term-id",
        "term": {
          "displayName": "Sample term name",
          "description": "Sample term description",
          "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary"
        }
      }
    }
    

### Edit a request

You can update details of an existing pending request in the `NEW` state. For example, you can change the justification provided in the request.

###  REST 

To edit a request, send a `PATCH` request containing the changed field:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists (for example, `us-central1`).
  * `CHANGE_REQUEST_ID`: the unique ID of the change request.
  * `NEW_JUSTIFICATION`: the updated justification for the change request.



HTTP method and URL: 
    
    
    PATCH https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID?updateMask=justification

Request JSON body: 
    
    
    {
      "justification": "NEW_JUSTIFICATION"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID?updateMask=justification"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -ContentType: "application/json; charset=utf-8" `  
        -InFile request.json `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID?updateMask=justification" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

### Delete a request

You can only delete requests that are in the `NEW` state. To delete a request, follow these steps: 

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **My requests** tab.

  3. Locate the row containing your target request. If necessary, apply a filter to isolate the entry.

  4. Click more_vert **Actions** and then click **Delete**.




###  REST 

To delete a request, send a `DELETE` request that includes the request ID:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists (for example, `us-central1`).
  * `CHANGE_REQUEST_ID`: the ID of your request you want to delete.



HTTP method and URL: 
    
    
    DELETE https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

## Manage requests as an approver

As an approver, you review, evaluate, and act on pending governance requests submitted for your data resources. When you approve or reject a request, the system automatically processes the decision and sends an email notification to the requester containing the decision details and your justification.

### List pending requests

To list requests pending the review, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **Pending Approvals** tab to view requests pending the review. You can filter requests by resource type, request type, or date.




###  REST 

To list access requests pending review within a specific project and location, send a `GET` request:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists. For example, `us-central1`.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "changeRequests": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/changeRequests/sample-change-request-1",
          "uid": "123e4567-e89b-12d3-a456-426614174000",
          "createTime": "2026-07-20T10:00:00Z",
          "updateTime": "2026-07-20T10:00:00Z",
          "justification": "Proposing a new glossary term definition for business accuracy.",
          "author": "user@example.com",
          "state": "NEW",
          "resource": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
          "createGlossaryTerm": {
            "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
            "termId": "sample-term-id",
            "term": {
              "displayName": "Sample term name",
              "description": "Sample term description",
              "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary"
            }
          }
        }
      ]
    }
    

### Approve a request

To approve a request, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **Pending Approvals** tab.

  3. Locate the row containing the request you want to approve.

  4. Click more_vert **Actions** and then click **Approve**.




###  REST 

To approve a request, send a `POST` request to the custom method `:approve`:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists (for example, `us-central1`).
  * `CHANGE_REQUEST_ID`: the unique ID of the change request you want to approve.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:approve

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d "" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:approve"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method POST `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:approve" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

Once processed, the request status updates automatically and the entry moves to the **Approval log** tab.

### Reject a request

To reject a request, follow these steps:

###  Console 

  1. In the Google Cloud console, go to the Knowledge Catalog **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Click the **Pending Approvals** tab.

  3. Locate the row containing the request you want to reject.

  4. Click more_vert **Actions** and then click **Reject**.

  5. In the dialog, enter a justification for the rejection.

  6. Click **Reject** to confirm.




###  REST 

To reject a request, send a `POST` request to the custom method `:reject` along with a justification payload:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists (for example, `us-central1`).
  * `CHANGE_REQUEST_ID`: the unique ID of the change request you want to reject.
  * `REJECTION_REASON`: the justification for the rejection.



HTTP method and URL: 
    
    
    POST https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:reject

Request JSON body: 
    
    
    {
      "comment": "REJECTION_REASON"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:reject"

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
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests/CHANGE_REQUEST_ID:reject" | Select-Object -Expand Content

You should receive a successful status code (2xx) and an empty response.

Providing a clear rejection comment helps requesters understand the decision and refine their access justifications before they resubmit the request. 

## Manage requests as a workflow administrator

As a workflow administrator, you oversee all governance requests across your organization, monitor approval history, and ensure compliance. You can list all active and historical requests, track audit trails across all request states (`NEW`, `APPROVED`, `REJECTED`, `DELETED`), and delete any request regardless of its current state.

### View all requests

To list all request within a specific project and location follow these steps:

###  REST 

To list access all requests within a specific project and location, send a `GET` request:

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists. For example, `us-central1`.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "changeRequests": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/changeRequests/sample-change-request-1",
          "uid": "123e4567-e89b-12d3-a456-426614174000",
          "createTime": "2026-07-20T10:00:00Z",
          "updateTime": "2026-07-20T10:00:00Z",
          "justification": "Proposing a new glossary term definition for business accuracy.",
          "author": "user@example.com",
          "state": "NEW",
          "resource": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
          "createGlossaryTerm": {
            "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
            "termId": "sample-term-id",
            "term": {
              "displayName": "Sample term name",
              "description": "Sample term description",
              "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary"
            }
          }
        }
      ]
    }
    

### Track approval history

The approval log provides end-to-end audit visibility for data product access requests, allowing administrators and compliance teams to track changes and access across all states.

### Console

  1. In the Google Cloud console, go to the **Governance Workflows** page.

[Go to Governance Workflows](https://console.cloud.google.com/dataplex/govern/workflows)

  2. Go to the **Approvals Log** tab to view completed approvals, rejections, and historical audit trails.




###  REST 

To list all requests for a specific project, send a `GET` request: 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: the ID of your Google Cloud project.
  * `LOCATION`: the region where the resource exists. For example, `us-central1`.



HTTP method and URL: 
    
    
    GET https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://dataplex.googleapis.com/v1/projects/PROJECT_ID/locations/LOCATION/changeRequests" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "changeRequests": [
        {
          "name": "projects/PROJECT_ID/locations/LOCATION/changeRequests/sample-change-request-1",
          "uid": "123e4567-e89b-12d3-a456-426614174000",
          "createTime": "2026-07-20T10:00:00Z",
          "updateTime": "2026-07-20T10:00:00Z",
          "justification": "Proposing a new glossary term definition for business accuracy.",
          "author": "user@example.com",
          "state": "NEW",
          "resource": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
          "createGlossaryTerm": {
            "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary",
            "termId": "sample-term-id",
            "term": {
              "displayName": "Sample term name",
              "description": "Sample term description",
              "parent": "projects/PROJECT_ID/locations/LOCATION/glossaries/sample-glossary"
            }
          }
        }
      ]
    }
    

## What's next

  * Learn more about [governance workflows](https://docs.cloud.google.com/knowledge-catalog/docs/about-governance-workflows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
