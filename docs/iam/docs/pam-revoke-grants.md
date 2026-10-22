---
url: https://docs.cloud.google.com/iam/docs/pam-revoke-grants/
title: Revoke grants in Privileged Access Manager \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:13.172747+00:00
---

# Revoke grants in Privileged Access Manager  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/pam-revoke-grants/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Revoke grants in Privileged Access Manager Stay organized with collections  Save and categorize content based on your preferences. 

After a principal has successfully [requested a grant](https://docs.cloud.google.com/iam/docs/pam-request-temporary-elevated-access) against an entitlement and it is active, principals with the `privilegedaccessmanager.grants.revoke` permission can revoke the grant. Grants that don't have an active status can't be revoked.

## Before you begin

Make sure you have [enabled Privileged Access Manager and set up permissions for it](https://docs.cloud.google.com/iam/docs/pam-permissions-and-setup).

## Revoke grants using the Google Cloud console

To revoke a specific grant made against an entitlement, complete the following instructions:

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Select the organization, folder, or project you want to revoke grants in.

  3. Click the **Grants** tab, followed by the **Grants for all users** tab. This contains all grants across all requesters, the grant statuses, and their associated entitlement details.

  4. In the table, click more_vert **More options** in the same row as a grant you want to revoke.

  5. To revoke an active grant, click **Revoke grant**.




To revoke all active grants made against an entitlement, complete the following instructions:

  1. Go to the **Privileged Access Manager** page.

[Go to Privileged Access Manager](https://console.cloud.google.com/iam-admin/pam/entitlements/)

  2. Click the **Entitlements** tab, followed by the **Entitlements for all users** tab. Here you can find the available entitlements, the roles they grant, and their valid requesters and approvers.

  3. In the table, click more_vert **More options** in the same row as an entitlement you want to revoke the grants for.

  4. Click **Revoke all grants**.




## Revoke grants programmatically

### gcloud

The `gcloud pam grants revoke` command revokes an active grant. 

Before using any of the command data below, make the following replacements: 

  * `GRANT_ID`: The ID of the grant you want to revoke. You can retrieve the ID by [ viewing grants](https://docs.cloud.google.com/iam/docs/pam-view-grants). 
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `REVOKE_REASON`: Why the grant has been revoked.
  * `RESOURCE_TYPE`: Optional. The resource type that the entitlement belongs to. Use the value `organization`, `folder`, or `project`.
  * `RESOURCE_ID`: Used with `RESOURCE_TYPE`. The ID of the Google Cloud project, folder, or organization that you want to manage entitlements for. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud pam grants revoke \
         GRANT_ID \
        --entitlement=ENTITLEMENT_ID \
        --reason="REVOKE_REASON" \
        --location=global \
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (PowerShell)
    
    
    gcloud pam grants revoke `
         GRANT_ID `
        --entitlement=ENTITLEMENT_ID `
        --reason="REVOKE_REASON" `
        --location=global `
        --RESOURCE_TYPE=RESOURCE_ID

#### Windows (cmd.exe)
    
    
    gcloud pam grants revoke ^
         GRANT_ID ^
        --entitlement=ENTITLEMENT_ID ^
        --reason="REVOKE_REASON" ^
        --location=global ^
        --RESOURCE_TYPE=RESOURCE_ID

You should receive a response similar to the following:
    
    
    auditTrail:
      accessGrantTime: '2024-04-05T00:29:16.703069535Z'
      accessRemoveTime: '2024-04-05T00:29:55.815041079Z'
    createTime: '2024-04-05T00:27:43.822053968Z'
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
    state: REVOKED
    timeline:
      events:
      - eventTime: '2024-04-05T00:27:44.014277946Z'
        requested:
          expireTime: '2024-04-06T00:27:44.014277946Z'
      - approved:
          actor: alex@example.com
          reason: Access allowed under existing policy
        eventTime: '2024-04-05T00:29:14.921828714Z'
      - eventTime: '2024-04-05T00:29:14.921763008Z'
        scheduled:
          scheduledActivationTime: '2024-04-05T00:29:14.921763008Z'
      - activated: {}
        eventTime: '2024-04-05T00:29:16.703069535Z'
      - eventTime: '2024-04-05T00:29:55.815041079Z'
        revoked:
          actor: alex@example.com
          reason: Revoking due to new access policy
    

### REST

The Privileged Access Manager API's `revokeGrant` method revokes an active grant. 

Before using any of the request data, make the following replacements: 

  * `SCOPE`: The organization, folder, or project that the entitlement is in, in the format of `organizations/ORGANIZATION_ID`, `folders/FOLDER_ID`, or `projects/PROJECT_ID`. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.
  * `ENTITLEMENT_ID`: The ID of the entitlement that the grant belongs to.
  * `GRANT_ID`: The ID of the grant you want to revoke. You can retrieve the ID by [ viewing grants](https://docs.cloud.google.com/iam/docs/pam-view-grants). 
  * `REVOKE_REASON`: The reason the grant was revoked.



HTTP method and URL: 
    
    
    POST https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:revoke

Request JSON body: 
    
    
    {
      "reason": "REVOKE_REASON"
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:revoke"

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
        -Uri "https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID:revoke" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "name": "projects/my-project/locations/global/operations/OPERATION_ID",
      "metadata": {
        "@type": "type.googleapis.com/google.cloud.privilegedaccessmanager.v1.OperationMetadata",
        "createTime": "2024-03-06T23:07:48.716396505Z",
        "target": "projects/my-project/locations/global/entitlements/ENTITLEMENT_ID/grants/GRANT_ID",
        "verb": "update",
        "requestedCancellation": false,
        "apiVersion": "v1"
      },
      "done": false
    }
    

To check on the progress of a revoke operation, you can send a `GET` request to the following endpoint: 
    
    
    https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/operations/OPERATION_ID

Send a `GET` request to the following endpoint to list all operations:
    
    
    https://privilegedaccessmanager.googleapis.com/v1/SCOPE/locations/global/operations

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
