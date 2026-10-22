---
url: https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access/
title: Request temporary elevated access with Privileged Access Manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:29:20.404803+00:00
---

# Request temporary elevated access with Privileged Access Manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Request temporary elevated access with Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

To temporarily elevate your privileges, you can request a grant against an _entitlement_ in [Privileged Access Manager (PAM)](https://docs.cloud.google.com/iam/docs/pam-overview) for a fixed duration.

An entitlement contains [roles](https://docs.cloud.google.com/iam/docs/understanding-roles) that are granted to you after your grant request is successful. These roles are removed by Privileged Access Manager when the grant ends. Grant activation and role removal take time to propagate through the system due to standard [access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).

Keep the following in mind when you want to request a grant against an entitlement:

  * You can only request grants against entitlements that you have been added to. To be added to an entitlement, contact the principal administering the entitlement.

  * One user can have a maximum of 10 open grants per entitlement at a time. These grants can be in the `Active`, `Scheduled`, or `Approval awaited` state.

  * You can't request a grant with the same scope as an existing grant in the `Active`, `Scheduled`, or `Approval awaited` state.

  * You can't have two scheduled grants on the same entitlement if both their scopes and their activation times overlap. Also, you can't schedule a grant to start before an active grant with the same scope ends.

  * Depending on how it's set up, a grant request might require approval to be granted.

  * If a grant request needs approval, it must be approved or denied before it expires. The deadline depends on the activation type:

    * Immediate activation: Within 24 hours of the request.
    * Scheduled activation: Before the scheduled activation time.

If a request isn't approved or denied by the deadline, its status changes to `Expired`.

  * Successful grant requests take time to propagate through the system because Privileged Access Manager uses time-based [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) subject to standard [access change propagation](https://docs.cloud.google.com/iam/docs/access-change-propagation).




## Request a grant

### Console

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project where you want to request a grant.

  3. In the **My entitlements** tab, find the entitlement to request against, and then click **Request grant** in the same row.

For entitlements that are inherited from a parent folder or organization, the scope of the grant is automatically adjusted to the selected organization, folder, or project. You can request a grant against the inherited entitlement at the child resource level. This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

  4. If the Security Command Center Premium or Enterprise tier is activated, then you can customize the scope of your grant request to include only some specific roles and resources. This feature is available in [preview](https://docs.cloud.google.com/products#product-launch-stages).

     1. Turn on the **Customize scope** toggle.
     2. Add the required resource filters. You can add up to five resource filters.
     3. Select the required roles.
  5. Provide the following details:

     * The duration required for the grant, up to the maximum duration set on the entitlement.

     * Optional: To schedule the grant for a later time, click **Schedule grants** and specify an activation time up to seven days in advance. If you don't schedule the grant, it activates immediately after creation or approval.

     * If required, a justification for the grant.

     * Optional: Email addresses for notifications.

Google identities associated with the entitlement, like approvers and requesters, are automatically notified. However, if you want to notify additional people, then you can add their email addresses. This is especially useful if you're using [workforce identities](https://docs.cloud.google.com/iam/docs/workforce-identity-federation) instead of Google Accounts.

  6. Click **Request grant**.




### gcloud

You can request a grant by using one of the following options:

  * Request a grant against an entitlement
  * Request a grant on a child resource of an entitlement
  * Request a grant with fine-grained scope



#### Request a grant against an entitlement

The `[gcloud alpha pam grants create](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants/create)` command requests a grant. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The entitlement ID to create the grant against.
  * `GRANT_DURATION`: The requested duration of the grant, in seconds.
  * `SCHEDULED_ACTIVATION_TIME`: Optional. The time when the grant needs to be activated, in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. If not specified, the grant activates immediately after creation or approval.
  * `JUSTIFICATION`: The justification for requesting the grant.
  * `EMAIL_ADDRESS`: Optional. Additional email addresses to notify of the grant request. Google identities associated with approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants create \
        --entitlement=ENTITLEMENT_ID \
        --requested-duration="GRANT_DURATIONs" \
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] \
        --justification="JUSTIFICATION" \
        --location=global \
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants create `
        --entitlement=ENTITLEMENT_ID `
        --requested-duration="GRANT_DURATIONs" `
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] `
        --justification="JUSTIFICATION" `
        --location=global `
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants create ^
        --entitlement=ENTITLEMENT_ID ^
        --requested-duration="GRANT_DURATIONs" ^
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] ^
        --justification="JUSTIFICATION" ^
        --location=global ^
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    Created [GRANT_ID].
    

#### Request a grant on a child resource of an entitlement

The `[gcloud alpha pam grants create](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants/create)` command requests a grant. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The entitlement ID to create the grant against.
  * `GRANT_DURATION`: The requested duration of the grant, in seconds.
  * `SCHEDULED_ACTIVATION_TIME`: Optional. The time when the grant needs to be activated, in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. If not specified, the grant activates immediately after creation or approval.
  * `JUSTIFICATION`: The justification for requesting the grant.
  * `EMAIL_ADDRESS`: Optional. Additional email addresses to notify of the grant request. Google identities associated with approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `RESOURCE_TYPE`: Optional. The type of the Google Cloud resources to be granted access to. This is used to customize the scope of the grant to a child resource.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `REQUESTED_RESOURCE`: Optional. The Google Cloud resources that you want to be granted access to. This is used to customize the scope of the grant to a child resource. Format: `RESOURCE_TYPE`/RESOURCE_ID. Example: `projects/PROJECT_ID`, `folders/FOLDER_ID`, or `organizations/ORGANIZATION_ID`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants create \
        --entitlement=ENTITLEMENT_ID \
        --requested-duration="GRANT_DURATIONs" \
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] \
        --justification="JUSTIFICATION" \
        --location=global \
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] \
        --RESOURCE_TYPE=RESOURCE_ID \
        --requested-resources=REQUESTED_RESOURCE

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants create `
        --entitlement=ENTITLEMENT_ID `
        --requested-duration="GRANT_DURATIONs" `
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] `
        --justification="JUSTIFICATION" `
        --location=global `
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] `
        --RESOURCE_TYPE=RESOURCE_ID `
        --requested-resources=REQUESTED_RESOURCE

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants create ^
        --entitlement=ENTITLEMENT_ID ^
        --requested-duration="GRANT_DURATIONs" ^
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] ^
        --justification="JUSTIFICATION" ^
        --location=global ^
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --requested-resources=REQUESTED_RESOURCE

You should receive a response similar to the following:
    
    
    Created [GRANT_ID].
    

#### Request a grant with fine-grained scope

The `[gcloud alpha pam grants create](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants/create)` command requests a grant. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The entitlement ID to create the grant against.
  * `GRANT_DURATION`: The requested duration of the grant, in seconds.
  * `SCHEDULED_ACTIVATION_TIME`: Optional. The time when the grant needs to be activated, in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. If not specified, the grant activates immediately after creation or approval.
  * `JUSTIFICATION`: The justification for requesting the grant.
  * `EMAIL_ADDRESS`: Optional. Additional email addresses to notify of the grant request. Google identities associated with approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
  * `ENTITLEMENT_ROLE_BINDING_ID`: Optional. The role binding ID of the role to be granted from the entitlement.
  * `ACCESS_RESTRICTION_NAME`: Optional. The resource names to restrict the access to. For information about the format, see [Resource name format](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).
  * `ACCESS_RESTRICTION_PREFIX`: Optional. The resource name prefixes to restrict the access to. For information about the format, see [Resource name format](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `REQUESTED_RESOURCE_TYPE`. Optional. The type of the Google Cloud resources to be granted access to. This is used to customize the scope of the grant to a child resource.
  * `REQUESTED_RESOURCE`: Optional. The Google Cloud resources that you want to be granted access to. This is used to customize the scope of the grant to a child resource. Format: `RESOURCE_TYPE`/RESOURCE_ID. Example: `projects/PROJECT_ID`, `folders/FOLDER_ID`, or `organizations/ORGANIZATION_ID`.



Save the following content in a file called `requested-scope.yaml `: 
    
    
    - gcpIamAccess:
        resource: REQUESTED_RESOURCE
        resourceType: REQUESTED_RESOURCE_TYPE
        roleBindings:
        - entitlementRoleBindingId: ENTITLEMENT_ROLE_BINDING_ID_1
          accessRestrictions:
            resourceNames:
            - ACCESS_RESTRICTION_NAME_1
            - ACCESS_RESTRICTION_NAME_2
        - entitlementRoleBindingId: ENTITLEMENT_ROLE_BINDING_ID_2
          accessRestrictions:
            resourceNamePrefixes:
            - ACCESS_RESTRICTION_PREFIX_1
            - ACCESS_RESTRICTION_PREFIX_2

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants create \
        --entitlement=ENTITLEMENT_ID \
        --requested-duration="GRANT_DURATIONs" \
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] \
        --justification="JUSTIFICATION" \
        --location=global \
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] \
        --RESOURCE_TYPE=RESOURCE_ID \
        --requested-access-from-file=requested-scope.yaml

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants create `
        --entitlement=ENTITLEMENT_ID `
        --requested-duration="GRANT_DURATIONs" `
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] `
        --justification="JUSTIFICATION" `
        --location=global `
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] `
        --RESOURCE_TYPE=RESOURCE_ID `
        --requested-access-from-file=requested-scope.yaml

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants create ^
        --entitlement=ENTITLEMENT_ID ^
        --requested-duration="GRANT_DURATIONs" ^
        [--scheduled-activation-time=SCHEDULED_ACTIVATION_TIME] ^
        --justification="JUSTIFICATION" ^
        --location=global ^
        [--additional-email-recipients=EMAIL_ADDRESS_1, EMAIL_ADDRESS_2] ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --requested-access-from-file=requested-scope.yaml

You should receive a response similar to the following:
    
    
    Created [GRANT_ID].
    

### REST

  1. Search for entitlements you're eligible to request.   


The Privileged Access Manager API's `[searchEntitlements](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/folders.locations.entitlements/search)` method with the `GRANT_REQUESTER` caller access type searches for entitlements you can request a grant against. 

Before using any of the request data, make the following replacements: 

     * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `FILTER`: Optional. Returns entitlements whose field values match an [ AIP-160 expression](https://google.aip.dev/160). 
     * `PAGE_SIZE`: Optional. The number of items to return in a response.
     * `PAGE_TOKEN`: Optional. Which page to start the response from, using a page token returned in a previous response.

HTTP method and URL: 
    
    GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements:search?callerAccessType=GRANT_REQUESTER&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements:search?callerAccessType=GRANT_REQUESTER&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements:search?callerAccessType=GRANT_REQUESTER&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/folders.locations.entitlements/search). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    {
      "name": "SCOPE/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1beta.OperationMetadata",
        "createTime": "2024-03-05T03:35:14.596739353Z",
        "target": "SCOPE/locations/global/entitlements/ENTITLEMENT_ID",
        "verb": "create",
        "requestedCancellation": false,
        "apiVersion": "v1beta"
      },
      "done": false
    }
    
    

  2. Request a grant against an entitlement.   


The Privileged Access Manager API's `[createGrant](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements.grants/create)` method requests a grant. 

Before using any of the request data, make the following replacements: 

     * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
     * `ENTITLEMENT_ID`: The entitlement ID to create the grant against.
     * `REQUEST_ID`: Optional. Must be a non-zero UUID. If the server receives a request with a request ID, it checks if another request with that ID has already been completed within the last 60 minutes. If so, the new request is ignored.
     * `GRANT_DURATION`: The requested duration of the grant, in seconds.
     * `SCHEDULED_ACTIVATION_TIME`: Optional. The time when the grant needs to be activated, in [RFC 3339](https://www.ietf.org/rfc/rfc3339.txt) format. If not specified, the grant activates immediately after creation or approval.
     * `JUSTIFICATION`: The justification for requesting the grant.
     * `EMAIL_ADDRESS`: Optional. Additional email addresses to notify of the grant request. Google identities associated with approvers are automatically notified. However, you might want to notify a different set of email addresses, especially if you're using [ Workforce Identity Federation](https://docs.cloud.google.com/iam/docs/workforce-identity-federation). 
     * `ENTITLEMENT_ROLE_BINDING_ID`: Optional. The role binding ID of the role to be granted from the entitlement.
     * `ACCESS_RESTRICTION_NAME`: Optional. The resource names to restrict access to. For information about the format, see [Resource name format](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).
     * `ACCESS_RESTRICTION_PREFIX`: Optional. The resource name prefixes to restrict access to. For information about the format, see [Resource name format](https://cloud.google.com/iam/docs/conditions-resource-attributes#resource-name).

HTTP method and URL: 
    
    POST https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants?requestId=REQUEST_ID

Request JSON body: 
    
    {
      "requestedDuration": "GRANT_DURATIONs",
      "activationTrigger": {
        "requestedActivationTime": "SCHEDULED_ACTIVATION_TIME"
      },
      "justification": {
        "unstructuredJustification": "JUSTIFICATION"
      },
      "additionalEmailRecipients": [
        "EMAIL_ADDRESS_1",
        "EMAIL_ADDRESS_2",
      ],
      "requestedPrivilegedAccess": {
        "gcpIamAccess": {
          "resourceType": "REQUESTED_RESOURCE_TYPE",
          "resource": "REQUESTED_RESOURCE",
          "roleBindings": [
            {
              "entitlementRoleBindingId": "ENTITLEMENT_ROLE_BINDING_ID",
              "accessRestrictions": {
                "resourceNames": [
                  "ACCESS_RESTRICTION_NAME"
                ],
                "resourceNamePrefixes": [
                  "ACCESS_RESTRICTION_PREFIX"
                ],
              },
            }
          ],
        }
      },
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants?requestId=REQUEST_ID"

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
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants?requestId=REQUEST_ID" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements.grants/create). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    {
       "name": "SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
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
           "resource": "//cloudresourcemanager.googleapis.com/SCOPE",
           "roleBindings": [
             {
               "role": "roles/storage.admin",
               "id": "hwqrt_1",
               "conditionExpression": "resource.name == \"//cloudresourcemanager.googleapis.com/SCOPE/buckets/bucket-1\" && resource.name.startsWith(\"//cloudresourcemanager.googleapis.com/SCOPE/compute/vms\")"
             }
           ]
         }
       },
       "requestedPrivilegedAccess": {
         "gcpIamAccess": {
           "resourceType": "cloudresourcemanager.googleapis.com/Project",
           "resource": "//cloudresourcemanager.googleapis.com/SCOPE",
           "roleBindings": [
             {
               "role": "roles/storage.admin",
               "entitlementRoleBindingId": "hwqrt_1",
               "accessRestrictions": {
                 "resourceNames": [
    "//cloudresourcemanager.googleapis.com/SCOPE/buckets/bucket-1"
                 ],
                 "resourceNamePrefixes": [                  "//cloudresourcemanager.googleapis.com/SCOPE/compute/vms"
                 ]
               }
             }
           ]
         }
       },
       "additionalEmailRecipients": [
         "bola@google.com"
       ]
    }
    
    




## Check your grant request status

### Console

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project that you want to view grants in.

  3. In the **Grants** tab, click **My grants**.

Your grant can have one of the following statuses:

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



### gcloud

The `[gcloud alpha pam grants search](https://docs.cloud.google.com/sdk/gcloud/reference/pam/grants/search)` command used with the `had-created` caller relationship searches for grants you have created. To check their status, look for the `state` field in the response. 

Before using any of the command data below, make the following replacements: 

  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. 
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud alpha pam grants search \
        --entitlement=ENTITLEMENT_ID \
        --caller-relationship=had-created \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud alpha pam grants search `
        --entitlement=ENTITLEMENT_ID `
        --caller-relationship=had-created `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud alpha pam grants search ^
        --entitlement=ENTITLEMENT_ID ^
        --caller-relationship=had-created ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    additionalEmailRecipients:
    - bola@example.com
    createTime: '2024-03-07T00:34:32.557017289Z'
    justification:
      unstructuredJustification: Renaming a file to mitigate issue #312
    name: SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID
    privilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          id: hwqrt_1
          conditionExpression: resource.name == "//cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_ID/buckets/bucket-1" && resource.name.startsWith("//cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_ID/compute/vms")
    requestedPrivilegedAccess:
      gcpIamAccess:
        resource: //cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_ID
        resourceType: cloudresourcemanager.googleapis.com/Project
        roleBindings:
        - role: roles/storage.admin
          entitlementRoleBindingId: hwqrt_1
          accessRestrictions:
            resourceNames:
            - //cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_ID/buckets/bucket-1
            resourceNamePrefixes:
            - //cloudresourcemanager.googleapis.com/RESOURCE_TYPE/RESOURCE_ID/compute/vms
    requestedDuration: 3600s
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
    

Grants can have the following statuses:

Status | Description  
---|---  
ACTIVATING | The grant is in the process of being activated.  
ACTIVATION_FAILED | Privileged Access Manager couldn't grant the roles due to a non-retriable error.  
ACTIVE | The grant is active and the principal has access to the resources permitted by the roles.  
APPROVAL_AWAITED | The grant request is waiting on a decision from an approver.  
DENIED | The grant request has been denied by an approver.  
ENDED | The grant has ended and the roles have been removed from the principal.  
EXPIRED | The grant request has expired, as approval wasn't given within 24 hours or by the scheduled activation time.  
REVOKED | The grant is revoked, and the principal no longer has access to the resources permitted by the roles.  
REVOKING | The grant is in the process of being revoked.  
SCHEDULED | The grant is scheduled and activates at the chosen activation time, provided all approvals (if needed) are received by then.  
WITHDRAWING | The grant is in the process of being withdrawn.  
WITHDRAWN | The grant is withdrawn, and the principal no longer has access to the resources permitted by the roles.  
  
### REST

The Privileged Access Manager API's `[searchGrants](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements.grants/search)` method used with the `HAD_CREATED` caller relationship searches for grants you have created. To check their status, look for the `state` field in the response. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to. 
  * `FILTER`: Optional. Returns grants whose field values match an [ AIP-160 expression](https://google.aip.dev/160). 
  * `PAGE_SIZE`: Optional. The number of items to return in a response.
  * `PAGE_TOKEN`: Optional. Which page to start the response from, using a page token returned in a previous response.



HTTP method and URL: 
    
    
    GET https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants:search?callerRelationship=HAD_CREATED&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants:search?callerRelationship=HAD_CREATED&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://privilegedaccessmanager.googleapis.com/v1beta/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants:search?callerRelationship=HAD_CREATED&filter=FILTER&pageSize=PAGE_SIZE&pageToken=PAGE_TOKEN" | Select-Object -Expand Content

#### APIs Explorer (browser)

Open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/pam/rest/v1/projects.locations.entitlements.grants/search). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Complete any required fields and click **Execute**. 

You should receive a JSON response similar to the following:
    
    
    {
      "grants": [
        {
          "name": "SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
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
              "resource": "//cloudresourcemanager.googleapis.com/SCOPE",
              "roleBindings": [
                {
                  "role": "roles/storage.admin",
                  "id": "hwqrt_1",
                  "conditionExpression": "resource.name == \"//cloudresourcemanager.googleapis.com/SCOPE/buckets/bucket-1\" && resource.name.startsWith(\"//cloudresourcemanager.googleapis.com/SCOPE/compute/vms\")"
                  "conditionExpression": "resource.name == \"//cloudresourcemanager.googleapis.com/SCOPE/buckets/bucket-1\" && resource.name.startsWith(\"//cloudresourcemanager.googleapis.com/SCOPE/compute/vms\")"
                }
              ]
            }
          },
          "requestedPrivilegedAccess": {
            "gcpIamAccess": {
              "resourceType": "cloudresourcemanager.googleapis.com/Project",
              "resource": "//cloudresourcemanager.googleapis.com/SCOPE",
              "roleBindings": [
                {
                  "role": "roles/storage.admin",
                  "entitlementRoleBindingId": "hwqrt_1",
                  "accessRestrictions": {
                    "resourceNames": ["//cloudresourcemanager.googleapis.com/SCOPE/buckets/bucket-1"
                    ],
                    "resourceNamePrefixes": ["//cloudresourcemanager.googleapis.com/SCOPE/compute/vms"
                    ]
                  }
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
    
    

Grant statuses are detailed in the following table.

Status | Description  
---|---  
ACTIVATING | The grant is in the process of being activated.  
ACTIVATION_FAILED | Privileged Access Manager couldn't grant the roles due to a non-retriable error.  
ACTIVE | The grant is active and the principal has access to the resources permitted by the roles.  
APPROVAL_AWAITED | The grant request is waiting on a decision from an approver.  
DENIED | The grant request has been denied by an approver.  
ENDED | The grant has ended and the roles have been removed from the principal.  
EXPIRED | The grant request has expired, as approval wasn't given within 24 hours or by the scheduled activation time.  
REVOKED | The grant is revoked, and the principal no longer has access to the resources permitted by the roles.  
REVOKING | The grant is in the process of being revoked.  
SCHEDULED | The grant is scheduled and activates at the chosen activation time, provided all approvals (if needed) are received by then.  
WITHDRAWING | The grant is in the process of being withdrawn.  
WITHDRAWN | The grant is withdrawn, and the principal no longer has access to the resources permitted by the roles.  
  
Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
