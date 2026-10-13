---
url: https://docs.cloud.google.com/iam/docs/pam-create-entitlements/
title: Create entitlements in Privileged Access Manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:07:50.761407+00:00
---

# Create entitlements in Privileged Access Manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-create-entitlements/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Create entitlements in Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

You can create entitlements to allow temporary privilege elevation for a select set of principals. Keep the following in mind when creating entitlements:

  * You can create entitlements at the organization, folder, or project level. Roles granted by an entitlement at each level follow the Google Cloud [resource hierarchy](https://docs.cloud.google.com/iam/docs/resource-hierarchy-access-control). For example, roles granted by an entitlement at the organization level are inherited at the folder and project levels.

  * If Security Command Center Premium or Enterprise tier is activated, then you can mandate more than one approval level per entitlement, allowing up to two levels of sequential approvals for each entitlement. You can mandate up to five approvals per level.

After the required number of first-level approvals are received, email notifications are sent to second-level approvers. After the required number of second-level approvals are received, the grant moves to the `active` state. If any approver denies the grant, then the grant moves to the `denied` state and is not sent to any additional approvers.

This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

  * If service accounts and agent identities are allowed to approve grants for this resource, then you can add service accounts, agent identities, and workload pool identities as approvers. To learn how to enable this setting, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

  * If you add a group as a requester to an entitlement, all individual accounts in that group can request a grant of that entitlement. However, only the individual account requesting the grant can receive elevated privileges.

  * If you add a group as an approver to an entitlement, all individual accounts in that group can approve or deny a grant request.

  * [Basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (Admin, Writer, and Reader) are supported, but [legacy basic roles](https://docs.cloud.google.com/iam/docs/roles-overview#legacy-basic) (Owner, Editor, and Viewer) are not supported.

  * Privileged Access Manager only supports services that support granular access through IAM because it uses IAM conditions to manage temporary access.

  * Don't include service agent roles in entitlements.

Some service agent roles contain very powerful permissions, and the permissions within these roles can change without notice. Instead, choose a different [predefined role](https://docs.cloud.google.com/iam/docs/roles-permissions), or create a [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) with the permissions you need. 




**Caution:** Be careful when including the following types of roles in an entitlement: 

  * Roles with permissions to grant and revoke IAM roles (that is, roles with permission names that end in `setIamPolicy`). 
  * Roles with the `iam.roles.update` permission, which lets users modify custom roles.



These types of roles contain permissions that can let a user modify their own IAM permissions. As a result, requesting principals can use these roles to increase their own access to resources, or give themselves additional access to resources. 

For example, imagine a user that has a custom role with very limited permissions. If this user successfully requests a grant against an entitlement with the Role Administrator role (`roles/iam.roleAdmin`), then they can use the permissions in that role to add the `resourcemanager.projects.setIamPolicy` permission to their custom role. This permission would let them grant and revoke all IAM roles for the project, even after the grant expires. 

## Before you begin

To get the permissions that you need to create entitlements, ask your administrator to grant you the following IAM roles on the organization, folder, or project that you want to create entitlements for: 

  * Create entitlements for an organization: 
    * [Privileged Access Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)
    * [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`)
  * Create for a folder: 
    * [Privileged Access Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)
    * [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`)
  * Create entitlements for a project: 
    * [Privileged Access Manager Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/privilegedaccessmanager#privilegedaccessmanager.admin) (`roles/privilegedaccessmanager.admin`)
    * [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`)
  * To view audit logs: [Logs Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/logging#logging.viewer) (`roles/logs.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create entitlements. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create entitlements:

  * To create entitlements and grants for an organization: 
    * `resourcemanager.organizations.get`
    * `resourcemanager.organizations.setIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
  * To create entitlements and grants for a folder: 
    * `resourcemanager.folders.get`
    * `resourcemanager.folders.setIamPolicy`
    * `privilegedaccessmanager.entitlements.create`
  * To create entitlements and grants for a project: 
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.setIamPolicy`
    * `privilegedaccessmanager.entitlements.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Create entitlements

### Console

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project you want the entitlement to apply to.

  3. Click the **Entitlements** tab.

  4. Click **Create**.

  5. In the **Entitlement details** section, enter the following entitlement details:

     * An entitlement name. An entitlement name can have 4 to 63 characters. It must start with a lowercase letter and can only contain lowercase letters, numbers, and hyphens.

     * Up to 30 roles to be granted on the organization, folder, or project.

You can also add [IAM conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to these roles in the same way that you add conditions to allow policy role bindings.

     * The maximum duration for a grant. The maximum duration you can set for an entitlement is 7 days.

  6. Click **Next**.

  7. In the **Add requesters** section, enter up to 20 valid requesting principals for the entitlement.

All [principal types](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1) are supported except `allUsers` and `allAuthenticatedUsers`. You can add more than 20 identities by adding them to a group and listing the group in the entitlement.

  8. Choose whether the principals need to provide a justification for the grant request.

  9. Enter additional email addresses of users to be notified when the entitlement is eligible to request.

Google identities associated with the entitlement, like approvers and requesters, are automatically notified. However, if you want to notify additional people, then you can add their email addresses. This is especially useful if you're using [workforce identities](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) instead of Google Accounts.

  10. Click **Next**.

  11. In the **Add approvers** section, do one of the following:

     * To allow role grants without approval, select **Activate access without approvals**.

     * To mandate approvals, do the following:

**Note:** Adding second-level approvers and configuring the number of approvals required are available only if the [Security Command Center Premium or Enterprise tier](https://docs.cloud.google.com/security-command-center/docs/service-tiers) is activated.
       1. Optional: To require approvers to enter justifications for approving requests, select **Justification required from approvers**.
       2. Enter first-level approver details:

          * A list of approvers for the entitlement

You can add any of the following principal types as approvers:

            * Google accounts

            * Google groups

            * Google Workspace domains

            * Workforce pool identifiers

            * Workload pool identifiers

            * Service accounts and agent identities

Service accounts, agent identities, and workload pool identifiers are available only if service accounts and agent identities are allowed to approve grants for this resource. For details, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

          * Number of approvals required

If you added a group as an approver, ensure that the number of required approvals is less than or equal to the number of principals in the group. Otherwise, grants will remain perpetually stuck in the `approval awaited` state.

          * Approvers' email addresses for notification

       3. Optional: Add second-level approver details:

          * A list of approvers for the entitlement

You can add any of the following principal types as approvers:

            * Google accounts

            * Google groups

            * Google Workspace domains

            * Workforce pool identifiers

            * Workload pool identifiers

            * Service accounts and agent identities

Service accounts, agent identities, and workload pool identifiers are available only if service accounts and agent identities are allowed to approve grants for this resource. For details, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

          * Number of approvals required

If you added a group as an approver, ensure that the number of required approvals is less than or equal to the number of principals in the group. Otherwise, grants will remain perpetually stuck in the `approval awaited` state.

          * Approvers' email addresses for notification

You can add up to 20 approving principals (identities or groups) per approval. If you want to add more than 20 approvers, you can do so by adding them to a group and listing the group as an approver for the entitlement.

  12. Click **Next**.

  13. Click **Create Entitlement**.




Newly created entitlements [might take a few minutes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation) and become ready for use. 

### gcloud

The `gcloud alpha pam entitlements create` command creates an entitlement at the organization, folder, or project level. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The entitlement ID to create. An ID must be 4-63 characters in length, and use the following characters: `[a-z0-9-]`. The first character must be a letter.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `SCOPE`: The organization, folder, or project to create the entitlement in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `RESOURCE_MANAGER_RESOURCE_TYPE`: Either `Organization`, `Folder`, or `Project`, depending on the scope.
  * `ROLE`: The [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to assign when an entitlement is granted.
  * `MAXIMUM_GRANT_DURATION`: The maximum duration a grant can be requested for, in seconds, ending with an `s` suffix. For example, to specify 30 minutes, use `1800s`. The supported range is between 30 minutes (`1800s`) and 168 hours (`604800s`).
  * `REQUESTING_MEMBER`: Principals that can request that the entitlement be granted. All [ principal types](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1) are supported except `allUsers` and `allAuthenticatedUsers`.

  * `APPROVING_MEMBER`: Principals that can approve the entitlement request. The valid [ principal types](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1) are as follows:

    * User
    * Group
    * Domain
    * Workforce pool identifiers
    * Workload pool identifiers 

This is available only if service accounts and agent identities are allowed to approve entitlement requests for this resource. For details, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

    * Service accounts and agent identities 

This is available only if service accounts and agent identities are allowed to approve entitlement requests for this resource. For details, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

  * `APPROVALS_NEEDED`: The number of approvers required to approve the entitlement request. 

If you added a group as an approver, ensure that the number of required approvals is less than or equal to the number of principals in the group. Otherwise, grants will remain perpetually stuck in the `approval awaited` state.

  * `APPROVER_EMAIL_ADDRESSES`: Optional. Additional email addresses to notify when a grant has been requested. Google identities associated with grant approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `ADMIN_EMAIL_ADDRESS`: Optional. Additional email addresses to notify when a requester is granted access. Google identities associated with grant approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `REQUESTER_EMAIL_ADDRESS`: Optional. Additional email addresses to notify when this entitlement is available to request. Google identities associated with grant requesters are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `CONDITION_EXPRESSION`: Optional. The [condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview) that specifies when the principal can use the permissions in the role. This condition only applies when the grant is active. **Note:** Privileged Access Manager doesn't support using [access level attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#access-levels) in an entitlement's IAM condition. 



Save the following content in a file called `entitlement.yaml`: 
    
    
    privilegedAccess:
      gcpIamAccess:
        resourceType: cloudresourcemanager.googleapis.com/RESOURCE_MANAGER_RESOURCE_TYPE
        resource: //cloudresourcemanager.googleapis.com/SCOPE
        roleBindings:
        - role: ROLE_1
          conditionExpression: CONDITION_EXPRESSION_1
        - role: ROLE_2
          conditionExpression: CONDITION_EXPRESSION_2
    maxRequestDuration: MAXIMUM_GRANT_DURATION
    eligibleUsers:
    - principals:
      - REQUESTING_MEMBER_1
      - REQUESTING_MEMBER_2
    approvalWorkflow:
      manualApprovals:
        requireApproverJustification: true
        steps:
        - approvalsNeeded: APPROVALS_NEEDED_1
          approverEmailRecipients:
          - APPROVER_EMAIL_ADDRESSES_1
          - APPROVER_EMAIL_ADDRESSES_2
          approvers:
          - principals:
           - APPROVING_MEMBER_1
           - APPROVING_MEMBER_2
        - approvalsNeeded: APPROVALS_NEEDED_2
          approverEmailRecipients:
           - APPROVER_EMAIL_ADDRESSES_3
           - APPROVER_EMAIL_ADDRESSES_4
          approvers:
          - principals:
            - APPROVING_MEMBER_3
            - APPROVING_MEMBER_4
    requesterJustificationConfig:
      unstructured: {}
    additionalNotificationTargets:
      adminEmailRecipients:
      - ADMIN_EMAIL_ADDRESS_1
      - ADMIN_EMAIL_ADDRESS_2
      requesterEmailRecipients:
      - REQUESTER_EMAIL_ADDRESS_1
      - REQUESTER_EMAIL_ADDRESS_2

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam entitlements create \
        ENTITLEMENT_ID \
        --entitlement-file=entitlement.yaml \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam entitlements create `
        ENTITLEMENT_ID `
        --entitlement-file=entitlement.yaml `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam entitlements create ^
        ENTITLEMENT_ID ^
        --entitlement-file=entitlement.yaml ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    Create request issued for: [ENTITLEMENT_ID]
    Waiting for operation [projects/PROJECT_ID/locations/global/operations/OPERATION_ID] to complete...done.
    Created entitlement [ENTITLEMENT_ID].
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
            - group:dev-team@example.com
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
    

Newly created entitlements [might take a few minutes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation) and become ready for use. 

### REST

The Privileged Access Manager API's `createEntitlement` method creates an entitlement at the organization, folder, or project level. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project to create the entitlement in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The entitlement ID to create. An ID must be 4-63 characters in length, and use the following characters: `[a-z0-9-]`. The first character must be a letter.
  * `RESOURCE_MANAGER_RESOURCE_TYPE`: Either `Organization`, `Folder`, or `Project`, depending on the scope.
  * `ROLE`: The [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) to assign when an entitlement is granted.
  * `MAXIMUM_GRANT_DURATION`: The maximum duration a grant can be requested for, in seconds, ending with an `s` suffix. For example, to specify 30 minutes, use `1800s`. The supported range is between 30 minutes (`1800s`) and 168 hours (`604800s`).
  * `REQUESTING_MEMBER`: Principals that can request the entitlement be granted. All [ principal types](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1) are supported except `allUsers` and `allAuthenticatedUsers`.

  * `APPROVING_MEMBER`: Principals that can approve the entitlement request. The valid [ principal types](https://docs.cloud.google.com/iam/docs/principal-identifiers#v1) are as follows:

    * User
    * Group
    * Domain
    * Workforce pool identifiers
    * Workload pool identifiers 

This is available only if service accounts and agent identities are allowed to approve entitlement requests for this resource. For details, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

    * Service accounts and agent identities 

This is available only if service accounts and agent identities are allowed to approve entitlement requests for this resource. For details, see [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings).

  * `APPROVALS_NEEDED`: The number of approvers required to approve the entitlement request. 

If you added a group as an approver, ensure that the number of required approvals is less than or equal to the number of principals in the group. Otherwise, grants will remain perpetually stuck in the `approval awaited` state.

  * `APPROVER_EMAIL_ADDRESSES`: Optional. Additional email addresses to notify when a grant has been requested. Google identities associated with grant approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `ADMIN_EMAIL_ADDRESS`: Optional. Additional email addresses to notify when a requester is granted access. Google identities associated with grant approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `REQUESTER_EMAIL_ADDRESS`: Optional. Additional email addresses to notify when this entitlement is available to request. Google identities associated with grant requesters are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `CONDITION_EXPRESSION`: Optional. The [condition expression](https://docs.cloud.google.com/iam/docs/conditions-overview) that specifies when the principal can use the permissions in the role. This condition only applies when the grant is active. **Note:** Privileged Access Manager doesn't support using [access level attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#access-levels) in an entitlement's IAM condition. 



HTTP method and URL: 
    
    
    POST https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements?entitlementId=ENTITLEMENT_ID

Request JSON body: 
    
    
    {
      "privilegedAccess": {
        "gcpIamAccess": {
          "resourceType": "cloudresourcemanager.googleapis.com/RESOURCE_MANAGER_RESOURCE_TYPE",
          "resource": "//cloudresourcemanager.googleapis.com/SCOPE",
          "roleBindings": [
            {
              "role": "ROLE_1",
              "conditionExpression": "CONDITION_EXPRESSION_1",
            },
            {
              "role": "ROLE_2",
              "conditionExpression": "CONDITION_EXPRESSION_2",
            },
          ]
        }
      },
      "maxRequestDuration": "MAXIMUM_GRANT_DURATION",
      "eligibleUsers": [
        {
          "principals": [
            "REQUESTING_MEMBER_1",
            "REQUESTING_MEMBER_2",
            ...
          ]
        }
      ],
      "approvalWorkflow": {
        "manualApprovals": {
          "requireApproverJustification": true,
          "steps": [
            {
              "approvers": [
                {
                  "principals": [
                    "APPROVING_MEMBER_1",
                    "APPROVING_MEMBER_2",
                  ]
                }
              ],
              "approvalsNeeded": APPROVALS_NEEDED_1,
              "approverEmailRecipients": [
                "APPROVER_EMAIL_ADDRESSES_1",
                "APPROVER_EMAIL_ADDRESSES_2",
              ]
            },
            {
              "approvers": [
                {
                  "principals": [
                    "APPROVING_MEMBER_3",
                    "APPROVING_MEMBER_4",
                  ]
                }
              ],
              "approvalsNeeded": APPROVALS_NEEDED_2,
              "approverEmailRecipients": [
                "APPROVER_EMAIL_ADDRESSES_3",
                "APPROVER_EMAIL_ADDRESSES_4",
              ]
            }
          ]
        }
      },
      "requesterJustificationConfig": {
        "unstructured": {
        }
      },
      "additionalNotificationTargets": {
        "adminEmailRecipients": [
          "ADMIN_EMAIL_ADDRESS_1",
          "ADMIN_EMAIL_ADDRESS_2",
        ],
        "requesterEmailRecipients": [
          "REQUESTER_EMAIL_ADDRESS_1",
          "REQUESTER_EMAIL_ADDRESS_2",
        ]
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
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements?entitlementId=ENTITLEMENT_ID"

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
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements?entitlementId=ENTITLEMENT_ID" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    
    {
      "name": "projects/PROJECT_ID/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1beta.OperationMetadata",
        "createTime": "2024-03-05T03:35:14.596739353Z",
        "target": "projects/PROJECT_ID/locations/global/entitlements/ENTITLEMENT_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1beta"
      },
      "done": false
    }
    
    

To check on the progress of a create operation, you can send a `GET` request to the following endpoint: 
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations/OPERATION_ID

Send a `GET` request to the following endpoint to list all operations:
    
    
    https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/operations

Newly created entitlements [might take a few minutes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation) and become ready for use. 

### Terraform

You can use [Terraform](https://www.terraform.io/) to create entitlements. For more information, see [google_privileged_access_manager_entitlement](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/privileged_access_manager_entitlement) in the Terraform documentation. Newly created entitlements [might take a few minutes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation) and become ready for use. 

### Config Connector

You can use [Kubernetes Config Connector](https://docs.cloud.google.com/config-connector/docs/overview) to create entitlements. For more information, see [PrivilegedAccessManagerEntitlement](https://docs.cloud.google.com/config-connector/docs/reference/resource-docs/privilegedaccessmanager/privilegedaccessmanagerentitlement) in the Config Connector documentation. Newly created entitlements [might take a few minutes to propagate](https://docs.cloud.google.com/iam/docs/access-change-propagation) and become ready for use. 

## What's next

  * [View, update, and delete entitlements](https://docs.cloud.google.com/iam/docs/pam-view-update-delete-entitlements)
  * [Configure Privileged Access Manager settings](https://docs.cloud.google.com/iam/docs/pam-configure-settings)
  * [Audit entitlement events](https://docs.cloud.google.com/iam/docs/pam-audit-entitlement-events)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
