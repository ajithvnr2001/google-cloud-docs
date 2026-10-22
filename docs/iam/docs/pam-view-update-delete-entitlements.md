---
url: https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements/
title: View, update, and delete entitlements in Privileged Access Manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:54:00.224314+00:00
---

# View, update, and delete entitlements in Privileged Access Manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  View, update, and delete entitlements in Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

After you have [created an entitlement](https://docs.cloud.google.com/iam/docs/pam-create-entitlements), you can view, update, or delete it. Changes to an entitlement's requesters and approvers [might take a few minutes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation).

## Before you begin

To get the permissions that you need to manage entitlements, ask your administrator to grant you the following IAM roles on the organization, folder, or project: 

  * To manage entitlements for an organization: 
    * [Privileged Access Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)
    * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)
  * To manage for a folder: 
    * [Privileged Access Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)
    * [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`)
  * To manage entitlements for a project: 
    * [Privileged Access Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * To view audit logs: Logs Viewer (`roles/logs.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to manage entitlements. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage entitlements:

  * To manage entitlements for an organization: 
    * `resourcemanager.organizations.get`
    * `resourcemanager.organizations.setIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
    * `privilegedaccessmanager.entitlements.delete`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.entitlements.setIamPolicy`
    * `privilegedaccessmanager.operations.delete`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view entitlements for an organization: 
    * `resourcemanager.organizations.get`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To manage entitlements for a folder: 
    * `resourcemanager.folders.get`
    * `resourcemanager.folders.setIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
    * `privilegedaccessmanager.entitlements.delete`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.entitlements.setIamPolicy`
    * `privilegedaccessmanager.operations.delete`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view entitlements for a folder: 
    * `resourcemanager.folders.get`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To manage entitlements for a project: 
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.getIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
    * `privilegedaccessmanager.entitlements.delete`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.entitlements.setIamPolicy`
    * `privilegedaccessmanager.operations.delete`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view entitlements for a project: 
    * `resourcemanager.projects.get`
    * `privilegedaccessmanager.entitlements.get`
    * `privilegedaccessmanager.entitlements.list`
    * `privilegedaccessmanager.operations.get`
    * `privilegedaccessmanager.operations.list`
  * To view audit logs: `logging.logEntries.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View, update, and delete entitlements using the Google Cloud console

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project you want to manage entitlements in.

  3. In the **Entitlements** tab, click the **Entitlements for all users** tab. Here you can find the available entitlements, the roles they grant, and their valid requesters and approvers.

  4. In the table, click more_vert **More options** in the same row as an entitlement you want to inspect.

     * To view the entitlement details, click **View entitlement details**.

     * To view grants associated with the entitlement, click **View associated grants**.

     * To revoke all active grants for the entitlement, click **Revoke all grants**.

     * To delete the entitlement, click **Delete entitlement**. You can't delete an entitlement with active grants. You must revoke the grants first.

  5. To update an entitlement, click edit **Edit entitlement** in the same row as the entitlement you want to update.

Keep the following things in mind when updating an entitlement:

     * The updated entitlement configuration only applies to grants requested after the update is made. Approver changes, however, also apply to existing grant requests that haven't yet been approved or denied.

     * To make changes to an entitlement's approval workflow that require a second level of approval, or more than one approval in any level, you must have the Security Command Center Premium or Enterprise tier activated. This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

     * You can make the following structural changes to an entitlement's approval workflow only if no grants for that entitlement are awaiting approval:

       * Adding or removing an approval level.
       * Changing the number of required approvals for any level.

This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

     * You can change the list of approvers in any approval level, even if there are grants awaiting approval.




## View entitlements programmatically

To view entitlements programmatically, you can search, list, get, and export them.

### List entitlements

### gcloud

The `gcloud alpha pam entitlements list` command lists entitlements that belong to a specific scope. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam entitlements list \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam entitlements list `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam entitlements list ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    additionalNotificationTargets:
      adminEmailRecipients:
      - alex@example.com
    approvalWorkflow:
      manualApprovals:
        requireApproverJustification: true
        steps:
        - id: step-1
          approvalsNeeded: 3
          approvers:
          - principals:
            - user:alex@example.com
            - user:dev-team@example.com
        - id: step-2
          approvalsNeeded: 1
          approvers:
          - principals:
            - user:alex@example.com
    createTime: '2024-04-09T02:39:37.011866832Z'
    eligibleUsers:
    - principals:
      - user:bola@example.com
    etag: 00000000000000000000000000000000000000000000000000000000000=
    maxRequestDuration: 7200s
    name: projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          id: hwarq_1
          conditionExpression: "request.time.getHours() >= 8"
    requesterJustificationConfig:
      unstructured: {}
    state: AVAILABLE
    updateTime: '2024-04-09T02:39:40.066770306Z'
    

### REST

The Privileged Access Manager API's `listEntitlements` method lists entitlements that belong to a specific scope. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `FILTER`: Optional. Returns entitlements whose field values match an [ AIP-160 expression](https://google.aip.dev/160). 
  * `PAGE_SIZE`: Optional. The number of items to return in a response.
  * `PAGE_TOKEN`: Optional. Which page to start the response from, using a page token returned in a previous response.



HTTP method and URL: 
    
    
    GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements?filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements?filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements?filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    [
      {
        "name": "projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID",
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
                "approvalsNeeded": 1,
                "id": "step-1"
              },
              {
                "approvers": [
                  {
                    "principals": [
                      "user:bob@example.com",
                      "user:jacob@example.com"
                    ]
                  }
                ],
                "approvalsNeeded": 2,
                "id": "step-2"
              }
            ]
          }
        },
        "privilegedAccess": {
          "gcpIamAccess": {
            "resourceType": "cloudresourcemanager.googleapis.com/Project",
            "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
            "roleBindings": [
              {
                "role": "roles/storage.admin",
                "id": "hwqrt_1",
                "conditionExpression": "request.time.getHours() >= 8"
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
    
    

### Get entitlements

### gcloud

The `gcloud alpha pam entitlements describe` command retrieves a specific entitlement. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement you want the details for.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam entitlements describe \
        ENTITLEMENT_ID \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam entitlements describe `
        ENTITLEMENT_ID `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam entitlements describe ^
        ENTITLEMENT_ID ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    additionalNotificationTargets:
     adminEmailRecipients:
     - alex@example.com
    approvalWorkflow:
      manualApprovals:
        requireApproverJustification: true
        steps:
        - id: step-1
          approvalsNeeded: 3
          approvers:
          - principals:
            - user:alex@example.com
            - user:dev-team@example.com
        - id: step-2
          approvalsNeeded: 1
          approvers:
          - principals:
            - user:alex@example.com
    createTime: '2024-04-09T02:39:37.011866832Z'
    eligibleUsers:
    - principals:
      - user:bola@example.com
    etag: 00000000000000000000000000000000000000000000000000000000000=
    maxRequestDuration: 7200s
    name: RESOURCE_TYPE/RESOURCE_ID/locations/global/entitlements/ENTITLEMENT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/projects/PROJECT_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          id: hwarq_1
          conditionExpression: "request.time.getHours() >= 8"
    requesterJustificationConfig:
      unstructured: {}
    state: AVAILABLE
    updateTime: '2024-04-09T02:39:40.066770306Z'
    

### REST

The Privileged Access Manager API's `getEntitlement` method retrieves a specific entitlement. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project to get the entitlement from, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement you want the details for.



HTTP method and URL: 
    
    
    GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID",
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
              "approvalsNeeded": 1,
              "id": "step-1"
            },
            {
              "approvers": [
                {
                  "principals": [
                    "user:bob@example.com",
                    "user:jacob@example.com"
                  ]
                }
              ],
              "approvalsNeeded": 2,
              "id": "step-2"
            }
          ]
        }
      },
      "privilegedAccess": {
        "gcpIamAccess": {
          "resourceType": "cloudresourcemanager.googleapis.com/Project",
          "resource": "//cloudresourcemanager.googleapis.com/projects/PROJECT_ID",
          "roleBindings": [
            {
              "role": "roles/storage.admin",
              "id": "hwqrt_1",
              "conditionExpression": "request.time.getHours() >= 8"
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
    
    

### Export entitlements using the gcloud CLI

The `gcloud alpha pam entitlements export` command exports a specific entitlement to a YAML file. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement to export.
  * `FILENAME`: The filename to export the entitlement contents to.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam entitlements export \
        ENTITLEMENT_ID \
        --destination=FILENAME.yaml \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam entitlements export `
        ENTITLEMENT_ID `
        --destination=FILENAME.yaml `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam entitlements export ^
        ENTITLEMENT_ID ^
        --destination=FILENAME.yaml ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    Exported [projects/my-project/locations/global/entitlements/ENTITLEMENT_ID] to 'FILENAME.yaml'.
    

## Update entitlements programmatically

Keep the following things in mind when updating an entitlement:

  * The updated entitlement configuration only applies to grants requested after the update is made. Approver changes, however, also apply to existing grant requests that haven't yet been approved or denied.

  * To make changes to an entitlement's approval workflow that require a second level of approval, or more than one approval in any level, you must have the Security Command Center Premium or Enterprise tier activated. This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

  * You can make the following structural changes to an entitlement's approval workflow only if no grants for that entitlement are awaiting approval:

    * Adding or removing an approval level.
    * Changing the number of required approvals for any level.

This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

  * You can change the list of approvers in any approval level, even if there are grants awaiting approval.




### gcloud

The `gcloud alpha pam entitlements update` command updates a specific entitlement. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement to update.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `FILENAME`: A file containing the modified configuration of the entitlement. To create this file, get or export the existing entitlement, save the response in a YAML file, and then modify it to use as the body of your update request. You must include the ETAG in the body to update the latest version of the entitlement. For available fields you can change or add, see [ Create entitlements programmatically](https://docs.cloud.google.com/iam/docs/pam-create-entitlements#create_entitlements_programmatically). 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam entitlements update \
        ENTITLEMENT_ID \
        --entitlement-file=FILENAME.yaml \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam entitlements update `
        ENTITLEMENT_ID `
        --entitlement-file=FILENAME.yaml `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam entitlements update ^
        ENTITLEMENT_ID ^
        --entitlement-file=FILENAME.yaml ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    Request issued for: [ENTITLEMENT_ID]
    Waiting for operation [RESOURCE_TYPE/RESOURCE_ID/locations/global/operations/OPERATION_ID] to complete...done.
    Updated entitlement [ENTITLEMENT_ID].
    additionalNotificationTargets: {}
    approvalWorkflow:
      manualApprovals:
        requireApproverJustification: true
        steps:
        - id: step-1
          approvalsNeeded: 3
          approvers:
          - principals:
            - user:alex@example.com
            - user:dev-team@example.com
        - id: step-2
          approvalsNeeded: 1
          approvers:
          - principals:
            - user:alex@example.com
    createTime: '2024-04-09T02:39:37.011866832Z'
    eligibleUsers:
    - principals:
      - user:bola@example.com
    etag: 00000000000000000000000000000000000000000000000000000000000=
    maxRequestDuration: 7200s
    name: projects/my-project/locations/global/entitlements/ENTITLEMENT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          id: hwarq_1
          conditionExpression: "request.time.getHours() >= 8"
    requesterJustificationConfig:
      unstructured: {}
    state: AVAILABLE
    updateTime: '2024-04-09T02:39:40.066770306Z'
    

### REST

The Privileged Access Manager API's `updateEntitlement` method updates a specific entitlement. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement to update.
  * `UPDATED_FIELDS`: A comma-separated list of fields that are being updated in the entitlement. For example:
        
        ?updateMask=privilegedAccess,maxRequestDuration

For all updatable fields, set the update mask to `*`.

  * `REQUEST_ID`: Optional. Must be a non-zero UUID. If the server receives a request with a request ID, it checks if another request with that ID has already been completed within the last 60 minutes. If so, the new request is ignored.
  * `request.json`: A file containing the modified configuration of the entitlement. To create this file, get or export the existing entitlement, save the response in file named `request.json`, and then modify it to use as the body of your update request. You must include the ETAG in the body to update the latest version of the entitlement. For available fields you can change or add, see [ Create entitlements programmatically](https://docs.cloud.google.com/iam/docs/pam-create-entitlements#create_entitlements_programmatically). 



HTTP method and URL: 
    
    
    PATCH https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID?updateMask=UPDATED_FIELDS&requestId=REQUEST_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X PATCH \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID?updateMask=UPDATED_FIELDS&requestId=REQUEST_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method PATCH `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID?updateMask=UPDATED_FIELDS&requestId=REQUEST_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1beta.OperationMetadata",
        "createTime": "2024-03-25T01:55:02.544562950Z",
        "target": "projects/my-project/locations/global/entitlements/ENTITLEMENT_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1beta"
      },
      "done": false
    }
    

To check on the progress of an update operation, you can send a `GET` request to the following endpoint: 
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations/OPERATION_ID

Send a `GET` request to the following endpoint to list all operations:
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations

## Delete entitlements programmatically

### gcloud

The `gcloud alpha pam entitlements delete` command deletes a specific entitlement. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement to delete.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam entitlements delete \
        ENTITLEMENT_ID \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam entitlements delete `
        ENTITLEMENT_ID `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam entitlements delete ^
        ENTITLEMENT_ID ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    Delete request issued for: [ENTITLEMENT_ID]
    Waiting for operation [projects/my-project/locations/global/operations/OPERATION_ID] to complete...done.
    Deleted entitlement [ENTITLEMENT_ID].
    

### REST

The Privileged Access Manager API's `deleteEntitlement` method deletes a specific entitlement. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project to delete the entitlement in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement to delete.
  * `REQUEST_ID`: Optional. Must be a non-zero UUID. If the server receives a request with a request ID, it checks if another request with that ID has already been completed within the last 60 minutes. If so, the new request is ignored.



HTTP method and URL: 
    
    
    DELETE https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID?requestId=REQUEST_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X DELETE \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID?requestId=REQUEST_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method DELETE `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID?requestId=REQUEST_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1beta.OperationMetadata",
        "createTime": "2024-03-06T02:28:28.020293460Z",
        "target": "projects/my-project/locations/global/entitlements/ENTITLEMENT_ID",
        "verb": "delete",
        "requestedCancellation": false,
        "apiVersion": "v1beta"
      },
      "done": false
    }
    

To check on the progress of a delete operation, you can send a `GET` request to the following endpoint: 
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations/OPERATION_ID

Send a `GET` request to the following endpoint to list all operations:
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations

## What's next

  * [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings)
  * [Audit entitlement events](https://docs.cloud.google.com/iam/docs/pam-audit-entitlement-events)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
