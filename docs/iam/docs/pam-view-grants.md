---
url: https://docs.cloud.google.com/iam/docs/pam-view-grants/
title: View grants in Privileged Access Manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:03:54.746723+00:00
---

# View grants in Privileged Access Manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-view-grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  View grants in Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

You can view a grant's status and history, or revoke a grant for other principals if it's active. Grant history is available for 30 days after a grant has ended.

## Before you begin

Make sure you have [enabled Privileged Access Manager and set up permissions for it](https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup).

## View grants using the Google Cloud console

To view a grant, complete the following instructions:

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project you want to view grants in.

  3. Click the **Grants** tab, followed by the **Grants for all users** tab. This tab contains all grants, the requesters for those grants, and the grant status. Grants can have the following statuses:

Status | Description  
---|---  
Activating | The grant is in the process of being activated.  
Activation failed | Privileged Access Manager couldn't grant the roles due to a non-retriable error.  
Active | The grant is active and the principal has access to the resources permitted by the roles.  
Approval awaited | The grant request is waiting on a decision from an approver.  
Denied | The grant request has been denied by an approver.  
Ended | The grant has ended and the roles have been removed from the principal.  
Expired | The grant request has expired, as approval wasn't given within 24 hours or by the scheduled activation time.  
Revoked | The grant is revoked, and the principal no longer has access to the resources permitted by the roles.  
Revoking | The grant is in the process of being revoked.  
Scheduled for `DATE` | The grant is scheduled and activates at the chosen activation time, provided all approvals (if needed) are received by then.  
Withdrawing | The grant is in the process of being withdrawn.  
Withdrawn | The grant is withdrawn, and the principal no longer has access to the resources permitted by the roles.  
  
**Status Labels**

In addition to these statuses, grants can have the following status labels displayed next to their status, which indicate special conditions:

**_Modified through IAM_**

The IAM policy bindings associated with this grant have been modified directly through IAM. For details on modified bindings, see the [IAM page](https://console.cloud.google.com/iam-admin) in the Google Cloud console. When a modified grant is revoked or ends, Privileged Access Manager only removes the bindings it has created that haven't been modified through IAM.

Modifying the IAM condition title or expression, or removing the requester's access to the granted role is treated as an external modification. Adding or modifying the IAM condition description is not considered an external modification.

Privileged Access Manager checks for external modifications to grants every 5 minutes. It can take up to 5 minutes to reflect these changes. Transient changes made and reverted within this 5-minute window might not be detected by Privileged Access Manager.

**Note:** Each binding created by Privileged Access Manager has a time-based condition that expires with the grant duration. As long as the time condition is not altered, the requester's privileged access will end when the grant expires.
  4. In the table, click more_vert **More options** in the same row as an entitlement you want to inspect.

     * To view the grant details including its history, click **View details**. You can also revoke a grant from this panel.

     * To revoke an active grant, click **Revoke grant**.




You can also view temporarily granted roles on the [IAM page](https://console.cloud.google.com/iam-admin) in the Google Cloud console. On the **View by principals** tab, temporarily granted roles have a condition of **Created by: PAM**.

## View grants programmatically

To view grants programmatically, you can search, list, and get them.

### Search grants

### gcloud

The `gcloud alpha pam grants search` command searches for a grant you have created, can approve or deny, or have already approved or denied. This method doesn't require specific Privileged Access Manager permissions to use. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. You can retrieve the ID by [ viewing entitlements](https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements). 
  * `CALLER_RELATIONSHIP_TYPE`: Use one of the following values:

    * `had-created`: Returns grants the caller has created.
    * `had-approved`: Returns grants the caller has approved or denied.
    * `can-approve`: Returns grants the caller can approve or deny.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants search \
        --entitlement=ENTITLEMENT_ID \
        --caller-relationship=CALLER_RELATIONSHIP_TYPE \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants search `
        --entitlement=ENTITLEMENT_ID `
        --caller-relationship=CALLER_RELATIONSHIP_TYPE `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants search ^
        --entitlement=ENTITLEMENT_ID ^
        --caller-relationship=CALLER_RELATIONSHIP_TYPE ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    additionalEmailRecipients:
    - bola@example.com
    createTime: '2024-03-07T00:34:32.557017289Z'
    justification:
      unstructuredJustification: Renaming a file to mitigate issue #312
    name: projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          id: hwqrt_1
    requestedDuration: 3600s
    requestedPrivilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          entitlementRoleBindingId: hwqrt_1
    requester: cruz@example.com
    state: DENIED
    timeline:
      events:
      - eventTime: '2024-03-07T00:34:32.793769042Z'
        requested:
          expireTime: '2024-03-08T00:34:32.793769042Z'
      - denied:
          actor: alex@example.com
          reason: Issue has already been resolved
        eventTime: '2024-03-07T00:36:08.309116203Z'
    updateTime: '2024-03-07T00:34:32.926967128Z'
    

### REST

The Privileged Access Manager API's `searchGrants` method searches for a grant you have created, can approve or deny, or have already approved or denied. This method doesn't require specific Privileged Access Manager permissions to use. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. You can retrieve the ID by [ viewing entitlements](https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements). 
  * `RELATIONSHIP_TYPE`: Valid values are: 
    * `HAD_CREATED`: Returns grants the caller has created.
    * `HAD_APPROVED`: Returns grants the caller has previously approved or denied.
    * `CAN_APPROVE`: Returns grants the caller can approve or deny.
  * `FILTER`: Optional. Returns grants whose field values match an [ AIP-160 expression](https://google.aip.dev/160). 
  * `PAGE_SIZE`: Optional. The number of items to return in a response.
  * `PAGE_TOKEN`: Optional. Which page to start the response from, using a page token returned in a previous response.



HTTP method and URL: 
    
    
    GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants:search?callerRelationship=RELATIONSHIP_TYPE&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants:search?callerRelationship=RELATIONSHIP_TYPE&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants:search?callerRelationship=RELATIONSHIP_TYPE&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "grants": [
        {
          "name": "projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
          "createTime": "2024-03-06T03:08:49.330577625Z",
          "updateTime": "2024-03-06T03:08:49.625874598Z",
          "requester": "alex@example.com",
          "requestedDuration": "3600s",
          "justification": {
            "unstructuredJustification": "Emergency service for outage"
          },
          "state": "APPROVAL_AWAITED",
          "timeline": {
            "events": [
              {
                "eventTime": "2024-03-06T03:08:49.462765846Z",
                "requested": {
                  "expireTime": "2024-03-07T03:08:49.462765846Z"
                }
              }
            ]
          },
          "privilegedAccess": {
            "gcpIamAccess": {
              "resourceType": "cloudresourcemanager.googleapis.com/Project",
              "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
              "roleBindings": [
                {
                  "role": "roles/storage.admin"
                  "id": "hwqrt_1"
                }
              ]
            }
          },
          "requestedPrivilegedAccess": {
            "gcpIamAccess": {
              "resourceType": "cloudresourcemanager.googleapis.com/Project",
              "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
              "roleBindings": [
                {
                  "role": "roles/storage.admin",
                  "entitlementRoleBindingId": "hwqrt_1"
                }
              ]
            }
          },
          "additionalEmailRecipients": [
            "bola@google.com"
          ]
        }
      ]
    }
    
    

### List grants

### gcloud

The `gcloud alpha pam grants list` command lists grants that belong to a specific entitlement. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. You can retrieve the ID by [ viewing entitlements](https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements). 
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants list \
        --entitlement=ENTITLEMENT_ID \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants list `
        --entitlement=ENTITLEMENT_ID `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants list ^
        --entitlement=ENTITLEMENT_ID ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    additionalEmailRecipients:
    - bola@example.com
    createTime: '2024-03-07T00:34:32.557017289Z'
    justification:
      unstructuredJustification: Renaming a file to mitigate issue #312
    name: projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          id: hwqrt_1
    requestedDuration: 3600s
    requestedPrivilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          entitlementRoleBindingId: hwqrt_1
    requester: cruz@example.com
    state: DENIED
    timeline:
      events:
      - eventTime: '2024-03-07T00:34:32.793769042Z'
        requested:
          expireTime: '2024-03-08T00:34:32.793769042Z'
      - denied:
          actor: alex@example.com
          reason: Issue has already been resolved
        eventTime: '2024-03-07T00:36:08.309116203Z'
    updateTime: '2024-03-07T00:34:32.926967128Z'
    

### REST

The Privileged Access Manager API's `listGrants` method lists grants that belong to a specific entitlement. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. You can retrieve the ID by [ viewing entitlements](https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements). 
  * `FILTER`: Optional. Returns grants whose field values match an [ AIP-160 expression](https://google.aip.dev/160). 
  * `PAGE_SIZE`: Optional. The number of items to return in a response.
  * `PAGE_TOKEN`: Optional. Which page to start the response from, using a page token returned in a previous response.



HTTP method and URL: 
    
    
    GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants?filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants?filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants?filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "grants": [
        {
          "name": "projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
          "createTime": "2024-03-06T03:08:49.330577625Z",
          "updateTime": "2024-03-06T03:08:49.625874598Z",
          "requester": "alex@example.com",
          "requestedDuration": "3600s",
          "justification": {
            "unstructuredJustification": "Emergency service for outage"
          },
          "state": "APPROVAL_AWAITED",
          "timeline": {
            "events": [
              {
                "eventTime": "2024-03-06T03:08:49.462765846Z",
                "requested": {
                  "expireTime": "2024-03-07T03:08:49.462765846Z"
                }
              }
            ]
          },
          "privilegedAccess": {
            "gcpIamAccess": {
              "resourceType": "cloudresourcemanager.googleapis.com/Project",
              "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
              "roleBindings": [
                {
                  "role": "roles/storage.admin",
                  "id": "hwqrt_1"
                }
              ]
            }
          },
          "requestedPrivilegedAccess": {
            "gcpIamAccess": {
              "resourceType": "cloudresourcemanager.googleapis.com/Project",
              "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
              "roleBindings": [
                {
                  "role": "roles/storage.admin",
                  "entitlementRoleBindingId": "hwqrt_1"
                }
              ]
            }
          },
          "additionalEmailRecipients": [
            "bola@google.com"
          ]
        }
      ]
    }
    

### Get grants

### gcloud

The `gcloud alpha pam grants describe` command retrieves a specific grant. 

Before using any of the command data below, make the following replacements: 

  * `GRANT_ID`: The ID of the grant you want the details for.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants describe \
        GRANT_ID \
        --entitlement=ENTITLEMENT_ID \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants describe `
        GRANT_ID `
        --entitlement=ENTITLEMENT_ID `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants describe ^
        GRANT_ID ^
        --entitlement=ENTITLEMENT_ID ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    additionalEmailRecipients:
    - bola@example.com
    createTime: '2024-03-07T00:34:32.557017289Z'
    justification:
      unstructuredJustification: Renaming a file to mitigate issue #312
    name: projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          id: hwqrt_1
    requestedDuration: 3600s
    requestedPrivilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          entitlementRoleBindingId: hwqrt_1
    requester: cruz@example.com
    state: DENIED
    timeline:
      events:
      - eventTime: '2024-03-07T00:34:32.793769042Z'
        requested:
          expireTime: '2024-03-08T00:34:32.793769042Z'
      - denied:
          actor: alex@example.com
          reason: Issue has already been resolved
        eventTime: '2024-03-07T00:36:08.309116203Z'
    updateTime: '2024-03-07T00:34:32.926967128Z'
    

### REST

The Privileged Access Manager API's `getGrant` method retrieves a specific grant. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `GRANT_ID`: The ID of the grant you want the details for.



HTTP method and URL: 
    
    
    GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID,
      "createTime": "2024-03-06T03:08:49.330577625Z",
      "updateTime": "2024-03-06T03:08:49.625874598Z",
      "requester": "alex@example.com",
      "requestedDuration": "3600s",
      "justification": {
        "unstructuredJustification": "Emergency service for outage"
      },
      "state": "APPROVAL_AWAITED",
      "timeline": {
        "events": [
          {
            "eventTime": "2024-03-06T03:08:49.462765846Z",
            "requested": {
              "expireTime": "2024-03-07T03:08:49.462765846Z"
            }
          }
        ]
      },
      "privilegedAccess": {
        "gcpIamAccess": {
          "resourceType": "cloudresourcemanager.googleapis.com/Project",
          "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "roleBindings": [
            {
              "role": "roles/storage.admin"
              "id": "hwqrt_1"
            }
          ]
        }
      },
      "requestedPrivilegedAccess": {
        "gcpIamAccess": {
          "resourceType": "cloudresourcemanager.googleapis.com/Project",
          "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "roleBindings": [
            {
              "role": "roles/storage.admin",
              "entitlementRoleBindingId": "hwqrt_1"
            }
          ]
        }
      },
      "additionalEmailRecipients": [
        "bola@google.com"
      ]
    }
    
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
