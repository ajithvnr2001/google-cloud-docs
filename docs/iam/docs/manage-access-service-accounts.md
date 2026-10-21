---
url: https://docs.cloud.google.com/iam/docs/manage-access-service-accounts/
title: Manage access to service accounts \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:09.208163+00:00
---

# Manage access to service accounts  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/manage-access-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Manage access to service accounts Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant, change, and revoke a principal's access to a single service account. To manage a principal's access to all service accounts in a project, folder, or organization, manage their access at the [project, folder, or organization level](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

**Note:** The IAM role picker uses Gemini to help you find and grant the right predefined roles to your principals. For more information, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini). 

In Identity and Access Management (IAM), access is managed through _allow policies_ , also known as IAM policies. An allow policy is attached to a Google Cloud resource. Each allow policy contains a collection of _role bindings_ that associate one or more principals, such as users or service accounts, with an IAM role. These role bindings grant the specified roles to the principals, both on the resource that the allow policy is attached to and on all of that resource's [descendants](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). For more information about allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

Service accounts are both resources that other principals can be granted access to, and principals that can be granted access to other resources. This page treats service accounts as resources and describes how to grant other principals access to them. To learn how to grant a service account access to other resources, the following guides:

  * To grant a service account access to a project, folder, or organization, see [Managing access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * To grant a service account access to other resources, see [Managing access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources).

**Note:** Granting roles on service accounts can allow principals to impersonate service accounts. See [Roles for service account authentication](https://docs.cloud.google.com/iam/docs/service-account-permissions) for more information.

This page describes how to manage access to service accounts using the Google Cloud console, the Google Cloud CLI, and the REST API. You can also manage access using the [IAM client libraries](https://docs.cloud.google.com/iam/docs/client-libraries#iam).

**Note:** You can also use deny policies to prevent principals from using specific IAM permissions. For more information, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview). 

## Before you begin

  * Learn about [service accounts](https://docs.cloud.google.com/iam/docs/service-accounts).
  * Ensure that you have the required IAM roles.



### Required roles

To get the permissions that you need to manage access to a service account, ask your administrator to grant you the [Service Account Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountAdmin) (`roles/iam.serviceAccountAdmin`) IAM role on the service account or the project that owns the service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to manage access to a service account. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage access to a service account:

  * `iam.serviceAccounts.get`
  * `iam.serviceAccounts.list`
  * `iam.serviceAccounts.getIamPolicy`
  * `iam.serviceAccounts.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## View current access

The following section shows you how to use the Google Cloud console, the gcloud CLI, and the REST API to view who has access to a service account. You can also view access by using the [IAM client libraries](https://docs.cloud.google.com/iam/docs/client-libraries#iam) to get the service account's allow policy.

**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

### Console

**Note:** The Google Cloud console shows access in a list form, rather than directly showing the resource's allow policy.

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

  3. Click the email address of the service account.

  4. Go to the **Principals with access** tab. The table lists all the principals who have been granted a role on the service account.

This list includes principals whose access comes from roles that are granted on parent resources. For more information about policy inheritance, see [Policy inheritance and the resource hierarchy](https://docs.cloud.google.com/iam/docs/allow-policies#inheritance).

  5. Optional: To view role grants for [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox.




### gcloud

To see who has access to your service account, get the allow policy for the service account. To learn how to interpret allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

**Note:** A resource's allow policy does not show any roles gained through [policy inheritance](https://docs.cloud.google.com/iam/docs/allow-policies#inheritance). To view inherited roles, use the Google Cloud console, or follow the instructions on [Viewing effective IAM policies](https://docs.cloud.google.com/asset-inventory/docs/view-effective-iam-policies). 

To get the allow policy for the service account, run the [`get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy) command for the service account:
    
    
    gcloud iam service-accounts get-iam-policy SA_ID --format=FORMAT > PATH

Provide the following values:

  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** If you want to identify a service account just after it is created, use the numeric ID rather than the email address to ensure that it is reliably identified. 

  * `FORMAT`: The format for the policy. Use `json` or `yaml`.

  * `PATH`: The path to a new output file for the policy.




For example, the following command gets the policy for the service account `my-service-account` and saves it to your home directory in JSON format:
    
    
    gcloud iam service-accounts get-iam-policy my-service-account --format json > ~/policy.json

### REST

To see who has access to your service account, get the allow policy for the service account. To learn how to interpret allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

**Note:** A resource's allow policy does not show any roles gained through [policy inheritance](https://docs.cloud.google.com/iam/docs/allow-policies#inheritance). To view inherited roles, use the Google Cloud console, or follow the instructions on [Viewing effective IAM policies](https://docs.cloud.google.com/asset-inventory/docs/view-effective-iam-policies). 

The `[serviceAccounts.getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)` method gets a service account's allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** To identify a service account just after it is created, use its numeric ID rather than its email address. 
  * `POLICY_VERSION`: The policy version to be returned. Requests should specify the most recent policy version, which is policy version 3\. See [Specifying a policy version when getting a policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) for details.



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:getIamPolicy

Request JSON body: 
    
    
    {
      "options": {
        "requestedPolicyVersion": POLICY_VERSION
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
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:getIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the service account's allow policy. For example: 
    
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/serviceAccountAdmin",
          "members": [
            "user:my-user@example.com"
          ]
        }
      ]
    }
    

## Grant or revoke a single IAM role

You can use the Google Cloud console and the gcloud CLI to quickly grant or revoke a single role for a single principal, without editing the service account's allow policy directly. Common types of principals include Google Accounts, service accounts, Google groups, and domains. For a list of all principal types, see [Principal types](https://docs.cloud.google.com/iam/docs/principals-overview#principal-types). 

**Note:** If the [`iam.allowedPolicyMemberDomains`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) organization policy constraint is enforced in your organization, then you might not be able to grant roles to newly created groups. If you get a `failedPrecondition` error when trying to grant a role to a newly created group, wait 24 hours, and then try granting the role again. 

In general, policy changes take effect within 2 minutes. However, in some cases, it can take 7 minutes or more for changes to propagate across the system. 

If you need help identifying the most appropriate predefined role, see [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

### Grant a single IAM role

To grant a single role to a principal, do the following:

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

  3. Click the email address of the service account.

  4. Go to the **Permissions** tab and find the section **Principals with access to this service account**.

  5. Select a principal to grant a role to:

     * To grant a role to a principal who already has other roles on the service account, find a row containing the principal, then click edit**Edit principal** in that row, then click add**Add another role**.

To grant a role to a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox to see its email address.

**Note:** You cannot edit inherited roles when managing access to service accounts. To edit inherited roles, go to the resource where the role was granted.
     * To grant a role to a principal who doesn't have any existing roles on the service account, click person_add **Grant access** , then enter an identifier for the principal—for example, `my-user@example.com` or `//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

  6. Click **Select a role** , then search for a role to grant based on the following: 

     * The role name
     * The Google Cloud product that you want to grant access to
     * The permission that you want to give
     * The job function to perform
To follow the principle of least privilege, [choose a role](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) that includes only the permissions that your principal needs.
  7. Optional: Add a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role.

  8. Click **Save**. The principal is granted the role on the service account.




### gcloud

To quickly grant a role to a principal, run the [`add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command:
    
    
    gcloud iam service-accounts add-iam-policy-binding SA_ID \
        --member=PRINCIPAL --role=ROLE_NAME \
        --condition=CONDITION

Provide the following values:

  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** If you want to identify a service account just after it is created, use the numeric ID rather than the email address to ensure that it is reliably identified. 

  * `PRINCIPAL`: An identifier for the principal, or member, which usually has the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`. For a full list of the values that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview). 

  * `ROLE_NAME`: The name of the role that you want to grant. Use one of the following formats:

    * Predefined roles: `roles/SERVICE.IDENTIFIER`
    * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
    * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  * `CONDITION`: Optional. The condition to add to the role binding. For more information about conditions, see the [conditions overview](https://docs.cloud.google.com/iam/docs/conditions-overview).




For example, to grant the Service Account User role to the user my-user@example.com for the service account `my-service-account@my-project.iam.gserviceaccount.com`:
    
    
    gcloud iam service-accounts add-iam-policy-binding my-service-account@my-project.iam.gserviceaccount.com \
        --member=user:my-user@example.com --role=roles/iam.serviceAccountUser

**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

### Revoke a single IAM role

To revoke a single role from a principal, do the following:

### Console

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

  3. Click the email address of the service account.

  4. Go to the **Permissions** tab and find the section **Principals with access to this service account**.

  5. Find the row containing the principal whose access you want to revoke. Then, click  edit **Edit principal** in that row.

**Note:** You cannot edit inherited roles when managing access to service accounts. To edit inherited roles, go to the resource where the role was granted.
  6. Click the **Delete** delete button for the role that you want to revoke, and then click **Save**.




### gcloud

To quickly revoke a role from a user, run the [`remove-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/remove-iam-policy-binding) command:
    
    
    gcloud iam service-accounts remove-iam-policy-binding SA_ID \
        --member=PRINCIPAL --role=ROLE_NAME

Provide the following values:

  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** If you want to identify a service account just after it is created, use the numeric ID rather than the email address to ensure that it is reliably identified. 

  * `PRINCIPAL`: An identifier for the principal, or member, which usually has the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`. For a full list of the values that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview). 

  * `ROLE_NAME`: The name of the role that you want to revoke. Use one of the following formats:

    * Predefined roles: `roles/SERVICE.IDENTIFIER`
    * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
    * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).




For example, to revoke the Service Account User role from the user my-user@example.com for the service account `my-service-account@my-project.iam.gserviceaccount.com`:
    
    
    gcloud iam service-accounts remove-iam-policy-binding my-service-account@my-project.iam.gserviceaccount.com \
        --member=user:my-user@example.com --role=roles/iam.serviceAccountUser

## Grant or revoke multiple IAM roles using the Google Cloud console

You can use the Google Cloud console to grant and revoke multiple roles for a single principal:

  1. In the Google Cloud console, go to the **Service Accounts** page.

[Go to Service Accounts](https://console.cloud.google.com/iam-admin/serviceaccounts)

  2. Select a project.

  3. Click the email address of the service account.

  4. Go to the **Permissions** tab and find the section **Principals with access to this service account**.

  5. Select the principal whose roles you want to modify:

     * To modify roles for a principal who already has roles on the service account, find a row containing the principal, then click edit**Edit principal** in that row, then click add**Add another role**.

To modify roles for a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox to see its email address.

**Note:** You cannot edit inherited roles when managing access to service accounts. To edit inherited roles, go to the resource where the role was granted.
     * To grant roles to a principal who doesn't have any existing roles on the service account, click person_add **Grant access** , then enter the principal's email address or other identifier.

  6. Modify the principal's roles:

     * To grant a role to a principal who doesn't have any existing roles on the resource, click **Select a role** , then search for a role to grant.
     * To grant an additional role to the principal, click **Add another role** , then search for a role to grant.
     * To replace one of the principal's roles with a different role, click the existing role, then search for a different role to grant.
     * To revoke one of the principal's roles, click the **Delete** delete button for each role that you want to revoke.

You can also [add a condition](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add) to a role, [modify a role's condition](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#modify), or [remove a role's condition](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#removing).

  7. Click **Save**.




**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

## Grant or revoke multiple IAM roles programmatically

To make large-scale access changes that involve granting and revoking multiple roles for multiple principals, use the _read-modify-write_ pattern to update the service account's allow policy:

  1. Read the current allow policy by calling `getIamPolicy()`.
  2. Edit the allow policy, either by using a text editor or programmatically, to add or remove any principals or role bindings.
  3. Write the updated allow policy by calling `setIamPolicy()`.



This section shows how to use the gcloud CLI and the REST API to update the allow policy. You can also update the allow policy using the [IAM client libraries](https://docs.cloud.google.com/iam/docs/client-libraries#iam).

**Note:** If the [`iam.allowedPolicyMemberDomains`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) organization policy constraint is enforced in your organization, then you might not be able to grant roles to newly created groups. If you get a `failedPrecondition` error when trying to grant a role to a newly created group, wait 24 hours, and then try granting the role again. 

In general, policy changes take effect within 2 minutes. However, in some cases, it can take 7 minutes or more for changes to propagate across the system. 

### Get the current allow policy

### gcloud

To get the allow policy for the service account, run the [`get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy) command for the service account:
    
    
    gcloud iam service-accounts get-iam-policy SA_ID --format=FORMAT > PATH

Provide the following values:

  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** If you want to identify a service account just after it is created, use the numeric ID rather than the email address to ensure that it is reliably identified. 

  * `FORMAT`: The format for the allow policy. Use `json` or `yaml`.

  * `PATH`: The path to a new output file for the allow policy.




For example, the following command gets the allow policy for the service account `my-service-account` and saves it to your home directory in JSON format:
    
    
    gcloud iam service-accounts get-iam-policy my-service-account --format json > ~/policy.json

### REST

The `[serviceAccounts.getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)` method gets a service account's allow policy. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** To identify a service account just after it is created, use its numeric ID rather than its email address. 
  * `POLICY_VERSION`: The policy version to be returned. Requests should specify the most recent policy version, which is policy version 3\. See [Specifying a policy version when getting a policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) for details.



HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:getIamPolicy

Request JSON body: 
    
    
    {
      "options": {
        "requestedPolicyVersion": POLICY_VERSION
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
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:getIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the service account's allow policy. For example: 
    
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/serviceAccountAdmin",
          "members": [
            "user:my-user@example.com"
          ]
        }
      ]
    }
    

Save the response in a file of the appropriate type (`json` or `yaml`).

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class GetServiceAccountPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
        // TODO: Replace with your service account name.
        String serviceAccount = "your-service-account";
        getPolicy(projectId, serviceAccount);
      }
    
      // Gets a service account's IAM policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getPolicy(String projectId, String serviceAccount) throws IOException {
    
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the name of the service account
        // whose allow policy you want to get.
        String serviceAccountEmail = serviceAccount + "@" + projectId + ".iam.gserviceaccount.com";
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder()
                  .setResource([ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html).of(projectId, serviceAccountEmail).toString())
                  .build();
          [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = iamClient.getIamPolicy(request);
          System.out.println("Policy retrieved: " + policy.toString());
          return policy;
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import iam_admin_v1
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def get_service_account_iam_policy(project_id: str, account: str) -> policy_pb2.Policy:
        """Get policy for service account.
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        """
    
        iam_client = iam_admin_v1.IAMClient()
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}/serviceAccounts/{account}"
    
        policy = iam_client.get_iam_policy(request)
        return policy

### Modify the allow policy

Programmatically or using a text editor, modify the local copy of your service account's allow policy to reflect the roles you want to grant or revoke to given users.

To ensure that you don't overwrite other changes, don't edit or remove the allow policy's `etag` field. The `etag` field identifies the current state of the allow policy. When you set the updated allow policy, IAM compares the `etag` value in the request with the existing `etag`, and only writes the allow policy if the values match.

**Important:** None of your changes to the allow policy will take effect until you set the updated allow policy.

To edit the roles that an allow policy grants, you need to edit the role bindings in the allow policy. Role bindings have the following format:
    
    
    {
      "role": "ROLE_NAME",
      "members": [
        "PRINCIPAL_1",
        "PRINCIPAL_2",
        ...
        "PRINCIPAL_N"
      ],
      "conditions:" {
        CONDITIONS
      }
    }

The placeholders have the following values:

  * `ROLE_NAME`: The name of the role that you want to grant. Use one of the following formats:

    * Predefined roles: `roles/SERVICE.IDENTIFIER`
    * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
    * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  * `PRINCIPAL_1`, `PRINCIPAL_2`, `...PRINCIPAL_N`: Identifiers for the principals that you want to grant the role to.

Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`. For a full list of the values that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview). 

  * `CONDITIONS`: Optional. Any [conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) that specify when access will be granted.




#### Grant a role

To grant roles to your principals, modify the role bindings in the allow policy. To learn what roles you can grant, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles), or [view grantable roles](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles) for the service account. If you need help identifying the most appropriate predefined roles, see [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

Optionally, you can use [conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to grant roles only when certain requirements are met.

To grant a role that is already included in the allow policy, add the principal to an existing role binding:

### gcloud

Edit the allow policy by adding the principal to an existing role binding. Note that this change will not take effect until you set the updated allow policy.

For example, imagine the allow policy contains the following role binding, which grants the Service Account User role (`roles/iam.serviceAccountUser`) to Kai:
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        "user:kai@example.com"
      ]
    }
    

To grant that same role to Raha, add Raha to the existing role binding:
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        "user:kai@example.com",
        **"user:raha@example.com"**
      ]
    }

### REST

Edit the allow policy by adding the principal to an existing role binding. Note that this change will not take effect until you set the updated allow policy.

For example, imagine the allow policy contains the following role binding, which grants the Service Account User role (`roles/iam.serviceAccountUser`) to Kai:
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        "user:kai@example.com"
      ]
    }
    

To grant that same role to Raha, add Raha to the existing role binding:
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        "user:kai@example.com",
        **"user:raha@example.com"**
      ]
    }

To grant a role that is not yet included in the allow policy, add a new role binding:

### gcloud

Edit the allow policy by adding a new role binding that grants the role to the principal. This change will not take effect until you set the updated allow policy.

For example, to grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to Raha, add the following role binding to the `bindings` array for the allow policy:
    
    
    {
      "role": "roles/iam.serviceAccountTokenCreator",
      "members": [
        "user:raha@example.com"
      ]
    }
    

### REST

Edit the allow policy by adding a new role binding that grants the role to the principal. This change will not take effect until you set the updated allow policy.

For example, to grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to Raha, add the following role binding to the `bindings` array for the allow policy:
    
    
    {
      "role": "roles/iam.serviceAccountTokenCreator",
      "members": [
        "user:raha@example.com"
      ]
    }
    

#### Revoke a role

To revoke a role, remove the principal from the role binding. If there are no other principals in the role binding, remove the entire role binding from the allow policy.

**Note:** Role bindings with no principals are not allowed and will result in an error when setting the allow policy.

### gcloud

Edit the allow policy by removing the principal or the entire role binding. This change will not take effect until you set the updated allow policy.

For example, imagine the allow policy contains the following role binding, which grants Kai and Raha the Service Account User role (`roles/iam.serviceAccountUser`):
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        "user:kai@example.com",
        "user:raha@example.com"
      ]
    }
    

To revoke the role from Kai, remove Kai's principal identifier from the role binding:
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        user:raha@example.com
      ]
    }
    

To revoke the role from both Kai and Raha, remove the role binding from the allow policy.

### REST

Edit the allow policy by removing the principal or the entire role binding. This change will not take effect until you set the updated allow policy.

For example, imagine the allow policy contains the following role binding, which grants Kai and Raha the Service Account User role (`roles/iam.serviceAccountUser`):
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        "user:kai@example.com",
        "user:raha@example.com"
      ]
    }
    

To revoke the role from Kai, remove Kai's principal identifier from the role binding:
    
    
    {
      "role": "roles/iam.serviceAccountUser",
      "members": [
        user:raha@example.com
      ]
    }
    

To revoke the role from both Kai and Raha, remove the role binding from the allow policy.

### Set the allow policy

After you modify the allow policy to grant and revoke roles, call `setIamPolicy()` to make the updates.

**Warning:** Setting a new allow policy permanently overwrites the existing allow policy on the service account. To avoid removing role bindings unintentionally, always follow the read-modify-write pattern when updating an allow policy: read the existing policy, modify it as needed, and then write the updated version of the allow policy.

### gcloud

To set the allow policy for the resource, run the [`set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/get-iam-policy) command for the service account:
    
    
    gcloud iam service-accounts set-iam-policy SA_ID PATH

Provide the following values:

  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** If you want to identify a service account just after it is created, use the numeric ID rather than the email address to ensure that it is reliably identified. 

  * `PATH`: The path to a file that contains the new allow policy.




The response contains the updated allow policy.

For example, the following command sets the allow policy stored in `policy.json` as the allow policy for the service account `my-service-account@my-project.iam.gserviceaccount.com`:
    
    
    gcloud iam service-accounts set-iam-policy my-service-account@my-project.iam.gserviceaccount.com \
        ~/policy.json

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 

### REST

The `[serviceAccounts.setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)` method sets an updated allow policy for the service account. 

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
  * `SA_ID`: The ID of your service account. This can either be the service account's email address in the form `SA_NAME@PROJECT_ID.iam.gserviceaccount.com`, or the service account's unique numeric ID.

**Note:** To identify a service account just after it is created, use its numeric ID rather than its email address. 
  * `POLICY`: A JSON representation of the policy that you want to set. For more information about the format of a policy, see the [Policy reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

For example, to set the allow policy shown in the previous step, replace `policy` with the following:
        
        {
          "version": 1,
          "etag": "BwUqLaVeua8=",
          "bindings": [
            {
              "role": "roles/iam.serviceAccountUser",
              "members": [
                "group:my-group@example.com"
              ]
            },
            {
              "role": "roles/serviceAccountAdmin",
              "members": [
                "user:my-user@example.com"
              ]
            }
          ]
        }




HTTP method and URL: 
    
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:setIamPolicy

Request JSON body: 
    
    
    {
      "policy": POLICY
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:setIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SA_ID:setIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated allow policy.

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    import com.google.cloud.iam.admin.v1.[IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html);
    import com.google.iam.admin.v1.[ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class SetServiceAccountPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
        // TODO: Replace with your service account name.
        String serviceAccount = "your-service-account";
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
    
        setServiceAccountPolicy(policy, projectId, serviceAccount);
      }
    
      // Sets a service account's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) setServiceAccountPolicy([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String projectId,
                                                   String serviceAccount) throws IOException {
    
        // Construct the service account email.
        // You can modify the ".iam.gserviceaccount.com" to match the name of the service account
        // whose allow policy you want to set.
        String accountEmail = String.format("%s@%s.iam.gserviceaccount.com", serviceAccount, projectId);
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html) iamClient = [IAMClient](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.cloud.iam.admin.v1.IAMClient.html).create()) {
          List<String> paths = Arrays.asList("bindings", "etag");
          [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource([ServiceAccountName](https://docs.cloud.google.com/java/docs/reference/google-iam-admin/latest/com.google.iam.admin.v1.ServiceAccountName.html).of(projectId, accountEmail).toString())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policy)
                  // A FieldMask specifying which fields of the policy to modify. Only
                  // the fields in the mask will be modified. If no mask is provided, the
                  // following default mask is used:
                  // `paths: "bindings, etag"`
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(paths).build())
                  .build();
    
          return iamClient.setIamPolicy(request);
        }
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see [Set up authentication for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment). 
    
    
    from google.cloud import iam_admin_v1
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def set_service_account_iam_policy(
        project_id: str, account: str, policy: policy_pb2.Policy
    ) -> policy_pb2.Policy:
        """Set policy for service account.
    
        Pay attention that previous state will be completely rewritten.
        If you want to update only part of the policy follow the approach
        read->modify->write.
        For more details about policies check out
        https://cloud.google.com/iam/docs/policies
    
        project_id: ID or number of the Google Cloud project you want to use.
        account: ID or email which is unique identifier of the service account.
        policy: Policy which has to be set.
        """
    
        # Same approach as for policies on project level,
        # but client stub is different.
        iam_client = iam_admin_v1.[IAMClient](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html)()
        request = iam_policy_pb2.SetIamPolicyRequest()
        request.resource = f"projects/{project_id}/serviceAccounts/{account}"
    
        # request.etag field also will be merged which means
        # you are secured from collision, but it means that request
        # may fail and you need to leverage exponential retries approach
        # to be sure policy has been updated.
        request.policy.MergeFrom(policy)
    
        policy = iam_client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/iam/latest/google.cloud.iam_admin_v1.services.iam.IAMClient.html#google_cloud_iam_admin_v1_services_iam_IAMClient_set_iam_policy)(request)
        return policy

**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

## What's next

  * Learn which roles to grant to allow principals to [authenticate as service accounts](https://docs.cloud.google.com/iam/docs/service-account-permissions).
  * Find out how to [choose the most appropriate predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).
  * Review [Best practices for working with service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts) to learn how to use service accounts securely.
  * Learn how to [manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).
  * Learn the general steps for [managing access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources).
  * Learn how to make a principal's access conditional with [conditional role bindings](https://docs.cloud.google.com/iam/docs/conditions-overview).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
