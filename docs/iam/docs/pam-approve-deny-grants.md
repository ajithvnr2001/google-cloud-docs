---
url: https://docs.cloud.google.com/iam/docs/pam-approve-deny-grants/
title: Approve or deny grants with Privileged Access Manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:21.772249+00:00
---

# Approve or deny grants with Privileged Access Manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-approve-deny-grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Approve or deny grants with Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

When an entitlement has an approval workflow, principals that are specified as approvers can approve or deny grant requests for that entitlement.

If the Security Command Center Premium or Enterprise tier is activated, then the approval workflow can have two levels of approvals. An approver can be in one or both approval levels, but can only approve once. After the required number of first-level approvals are received, email notifications are sent to second-level approvers. After the required number of second-level approvals are received, the grant moves to the `active` state. If any approver denies the grant, then the grant moves to the `denied` state and is not sent to any additional approvers. This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

Keep the following in mind when approving or denying a grant request against an entitlement:

  * You can't approve your own request.

  * If a request isn't approved or denied, its status changes to `expired` as follows:

    * Unscheduled grants expire if they aren't approved or denied within 24 hours of being requested.
    * Scheduled grants expire if they aren't approved or denied by their scheduled activation time.

After a grant expires, a principal must make a new grant request if privilege elevation is still required.




## Approve or deny grants using the Google Cloud console

To approve or deny a grant request that has been made against an entitlement, complete the following instructions:

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Click the **Approve grants** tab, followed by the **Pending approval** tab.

**Note:** Grants created on entitlements that are inherited from a parent resource appear in the **Pending approval** tab of the parent resource.
  3. In the row related to the request you want to approve or deny, click **Approve/deny**.

  4. If a justification is required, enter it in the **Comment** field. You can view the history of the grant in the **History** tab.

  5. Click either **Approve** or **Deny**.




You can view your approval history in the **My approval history** tab. Approval history is available for 30 days after an approval action has been taken. Grants created on entitlements that are inherited from a parent resource appear in the approval history of the parent resource.

**Note:** If an entitlement is deleted, its approval history is also deleted. Recreating the entitlement with the same name and configuration doesn't restore the approval history.

## Approve or deny grants programmatically

To approve or deny grants, you need to complete the following actions:

  1. Search for entitlements you're an approver on.

  2. With the relevant entitlement ID, search for grant requests you can approve or deny.

  3. Approve or deny the grant requests.




### Search for entitlements you're an approver on

### gcloud

The `gcloud pam entitlements search` command with the `grant-approver` caller access type searches for entitlements on which you are an approver. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud pam entitlements search \
        --caller-access-type=grant-approver \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud pam entitlements search `
        --caller-access-type=grant-approver `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud pam entitlements search ^
        --caller-access-type=grant-approver ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    additionalNotificationTargets: {}
    approvalWorkflow:
      manualApprovals:
        requireApproverJustification: true
        steps:
        - approvalsNeeded: 1
          approvers:
          - principals:
            - user:alex@example.com
    createTime: '22024-03-26T11:07:37.009498890Z'
    etag: 00000000000000000000000000000000000000000000000000000000000=
    maxRequestDuration: 3600s
    name: projects/my-project/locations/global/entitlements/ENTITLEMENT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/my-project
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
    requesterJustificationConfig:
      notMandatory: {}
    state: AVAILABLE
    updateTime: '2024-03-26T11:07:40.056780645Z'
    

### REST

The Privileged Access Manager API's `searchEntitlements` method with the `GRANT_APPROVER` caller access type searches for entitlements on which you are an approver. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `FILTER`: Optional. Returns entitlements whose field values match an [ AIP-160 expression](https://google.aip.dev/160). 
  * `PAGE_SIZE`: Optional. The number of items to return in a response.
  * `PAGE_TOKEN`: Optional. Which page to start the response from, using a page token returned in a previous response.



HTTP method and URL: 
    
    
    GET https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements:search?callerAccessType=GRANT_APPROVER&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements:search?callerAccessType=GRANT_APPROVER&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements:search?callerAccessType=GRANT_APPROVER&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    [
      {
        "name": "projects/my-project/locations/global/entitlements/ENTITLEMENT_ID",
        "createTime": "2023-11-21T17:28:39.962144708Z",
        "updateTime": "2023-11-21T17:28:43.160309410Z",
        "eligibleUsers": [
          {
            "principals": [
              "user:alex@example.com"
            ]
          }
        ],
        "approvalWorkflow": {
          "manualApprovals": {
            "steps": [
              {
                "approvers": [
                  {
                    "principals": [
                      "user:bola@example.com"
                    ]
                  }
                ],
                "approvalsNeeded": 1
              }
            ]
          }
        },
        "privilegedAccess": {
          "gcpIamAccess": {
            "resourceType": "cloudresourcemanager.googleapis.com/Project",
            "resource": "//cloudresourcemanager.googleapis.com/projects/my-project",
            "roleBindings": [
              {
                "role": "roles/storage.admin"
              }
            ]
          }
        },
        "maxRequestDuration": "14400s",
        "state": "AVAILABLE",
        "requesterJustificationConfig": {
          "unstructured": {}
        },
        "additionalNotificationTargets": {
          "adminEmailRecipients": [
            "alex@example.com"
          ]
        },
        "etag": "00000000000000000000000000000000000000000000000000000000000="
      }
    ]
    

### Search for grant requests you can approve or deny

### gcloud

The `gcloud alpha pam grants search` command searches for a grant you can approve or deny, or have already approved or denied. This method doesn't require specific Privileged Access Manager permissions to use. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. You can retrieve the ID by  searching for entitlements you're an approver on. 
  * `CALLER_RELATIONSHIP_TYPE`: Use one of the following values:

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

The Privileged Access Manager API's `searchGrants` method searches for a grant you can approve or deny, or have already approved or denied. This method doesn't require specific Privileged Access Manager permissions to use. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. You can retrieve the ID by  searching for entitlements you're an approver on. 
  * `RELATIONSHIP_TYPE`: Valid values are: 
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
    
    

### Approve grants programmatically

### gcloud

The `gcloud pam grants describe` command approves a specific grant request. 

Before using any of the command data below, make the following replacements: 

  * `GRANT_ID`: The ID of the grant you're approving. You can retrieve the ID by  searching for grant requests you can approve or deny. 
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `APPROVAL_REASON`: Why the grant has been approved.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud pam grants approve \
        GRANT_ID \
        --entitlement=ENTITLEMENT_ID \
        --reason="APPROVAL_REASON" \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud pam grants approve `
        GRANT_ID `
        --entitlement=ENTITLEMENT_ID `
        --reason="APPROVAL_REASON" `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud pam grants approve ^
        GRANT_ID ^
        --entitlement=ENTITLEMENT_ID ^
        --reason="APPROVAL_REASON" ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    createTime: '2024-04-05T01:17:04.596455403Z'
    justification:
      unstructuredJustification: Renaming a file to mitigate issue #312
    name: projects/my-project/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/my-project
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
    requestedDuration: 2700s
    requester: cruz@example.com
    state: SCHEDULED
    timeline:
      events:
      - eventTime: '2024-04-05T01:17:04.732226659Z'
        requested:
          expireTime: '2024-04-06T01:17:04.732226659Z'
      - approved:
          actor: alex@example.com
          reason: Access allowed under existing policy
        eventTime: '2024-04-05T01:21:49.139539732Z'
      - eventTime: '2024-04-05T01:21:49.139463954Z'
        scheduled:
          scheduledActivationTime: '2024-04-05T01:21:49.139463954Z'
    updateTime: '2024-04-05T01:21:49.139463954Z'
    

### REST

The Privileged Access Manager API's `approveGrant` method approves a specific grant request. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `GRANT_ID`: The ID of the grant you are approving. You can retrieve the ID by  searching for grant requests you can approve or deny. 
  * `REASON`: The reason the grant request was approved.



HTTP method and URL: 
    
    
    POST https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:approve

Request JSON body: 
    
    
    {
        "reason": "REASON"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:approve"

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
        -Uri "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:approve" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
      "createTime": "2024-03-06T03:08:49.330577625Z",
      "updateTime": "2024-03-06T23:01:13.964619844Z",
      "requester": "alex@example.com",
      "requestedDuration": "3600s",
      "justification": {
        "unstructuredJustification": "Emergency service for outage"
      },
      "state": "SCHEDULED",
      "timeline": {
        "events": [
          {
            "eventTime": "2024-03-06T03:08:49.462765846Z",
            "requested": {
              "expireTime": "2024-03-07T03:08:49.462765846Z"
            }
          },
          {
            "eventTime": "2024-03-06T23:01:13.964685709Z",
            "approved": {
              "reason": "Approved escalation",
              "actor": "cruz@example.com"
            }
          },
          {
            "eventTime": "2024-03-06T23:01:13.964619844Z",
            "scheduled": {
              "scheduledActivationTime": "2024-03-06T23:01:13.964619844Z"
            }
          }
        ]
      },
      "privilegedAccess": {
        "gcpIamAccess": {
          "resourceType": "cloudresourcemanager.googleapis.com/Project",
          "resource": "//cloudresourcemanager.googleapis.com/projects/my-project",
          "roleBindings": [
            {
              "role": "roles/storage.admin"
            }
          ]
        }
      },
      "additionalEmailRecipients": [
        "bola@example.com.com"
      ]
    }
    

### Deny grants programmatically

### gcloud

The `gcloud pam grants describe` command denies a specific grant request. 

Before using any of the command data below, make the following replacements: 

  * `GRANT_ID`: The ID of the grant you're denying. You can retrieve the ID by [ searching for grants you can approve or deny](https://docs.cloud.google.com/iam/docs/pam-view-grants). 
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `DENIAL_REASON`: Why the grant has been denied.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud pam grants deny \
        GRANT_ID \
        --entitlement=ENTITLEMENT_ID \
        --reason="DENIAL_REASON" \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud pam grants deny `
        GRANT_ID `
        --entitlement=ENTITLEMENT_ID `
        --reason="DENIAL_REASON" `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud pam grants deny ^
        GRANT_ID ^
        --entitlement=ENTITLEMENT_ID ^
        --reason="DENIAL_REASON" ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    createTime: '2024-04-05T01:29:13.129192816Z'
    justification:
      unstructuredJustification: Renaming a file to mitigate issue #312
    name: projects/my-project/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/my-project
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
    requestedDuration: 2700s
    requester: cruz@example.com
    state: DENIED
    timeline:
      events:
      - eventTime: '2024-04-05T01:29:13.267878626Z'
        requested:
          expireTime: '2024-04-06T01:29:13.267878626Z'
      - denied:
          actor: alex@example.com
          reason: Access denied under existing policy
        eventTime: '2024-04-05T01:29:49.492161363Z'
    updateTime: '2024-04-05T01:29:49.492097724Z'
    

### REST

The Privileged Access Manager API's `denyGrant` method denies a specific grant request. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `GRANT_ID`: The ID of the grant you are denying. You can retrieve the ID by [ searching for grants you can approve or deny](https://docs.cloud.google.com/iam/docs/pam-view-grants). 
  * `REASON`: The reason the grant request was denied.



HTTP method and URL: 
    
    
    POST https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:deny

Request JSON body: 
    
    
    {
        "reason": "REASON"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:deny"

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
        -Uri "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:deny" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
      "createTime": "2024-03-07T00:34:32.557017289Z",
      "updateTime": "2024-03-07T00:36:08.309046580Z",
      "requester": "alex@example.com",
      "requestedDuration": "3600s",
      "justification": {
        "unstructuredJustification": "Emergency service for outage"
      },
      "state": "DENIED",
      "timeline": {
        "events": [
          {
            "eventTime": "2024-03-07T00:34:32.793769042Z",
            "requested": {
              "expireTime": "2024-03-08T00:34:32.793769042Z"
            }
          },
          {
            "eventTime": "2024-03-07T00:36:08.309116203Z",
            "denied": {
              "reason": "Outage already resolved",
              "actor": "cruz@example.com"
            }
          }
        ]
      },
      "privilegedAccess": {
        "gcpIamAccess": {
          "resourceType": "cloudresourcemanager.googleapis.com/Project",
          "resource": "//cloudresourcemanager.googleapis.com/projects/my-project",
          "roleBindings": [
            {
              "role": "roles/storage.admin"
            }
          ]
        }
      },
      "additionalEmailRecipients": [
        "bola@example.com"
      ]
    }
    

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
