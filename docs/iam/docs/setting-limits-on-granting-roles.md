---
url: https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles/
title: Set limits on granting roles \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:09:35.399632+00:00
---

# Set limits on granting roles  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/setting-limits-on-granting-roles/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Set limits on granting roles Stay organized with collections  Save and categorize content based on your preferences. 

In large organizations, it can be helpful to let teams independently manage the allow policies for their resources. However, letting a principal grant or revoke all IAM roles can greatly increase your security risk.

You can set limits on the roles that a principal can grant and revoke with Identity and Access Management (IAM) Conditions and the `iam.googleapis.com/modifiedGrantsByRole` API attribute. These limits let you create limited IAM admins who can manage their own team's allow policies, but only within the boundaries that you have set.

## Before you begin

  * Enable the Resource Manager API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Be familiar with the [structure of allow policies](https://docs.cloud.google.com/iam/docs/allow-policies#structure).

  * Understand [IAM Conditions](https://docs.cloud.google.com/iam/docs/conditions-overview).




### Required permissions

To get the permissions that you need to create limited IAM admins for a project, folder, or organization, ask your administrator to grant you the following IAM roles on the resource that you want to create a limited IAM admin for (project, folder, or organization): 

  * To create a limited IAM admin for a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * To create a limited IAM admin for a folder: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) 
  * To create a limited IAM admin for a project, folder, or organization: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to create limited IAM admins for a project, folder, or organization. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to create limited IAM admins for a project, folder, or organization:

  * To create a limited IAM admin for a project: 
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`
  * To create a limited IAM admin for a folder: 
    * `resourcemanager.folders.getIamPolicy`
    * `resourcemanager.folders.setIamPolicy`
  * To create a limited IAM admin for an organization: 
    * `resourcemanager.organizations.getIamPolicy`
    * `resourcemanager.organizations.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Common use cases

The following sections describe how you can use limited role granting to enable self-service management of allow policies.

### Create limited IAM admins

Consider a scenario where you want to let a user, Noam, act as a limited IAM admin for your project. You want Noam to be able to grant and revoke only the App Engine Admin (`roles/appengine.appAdmin`) and App Engine Viewer (`roles/appengine.appViewer`) roles for your project.

To grant this limited ability, you conditionally grant Noam the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). The Project IAM Admin role allows Noam to grant and revoke IAM roles, and the condition limits which roles Noam can grant and revoke:
    
    
    {
      "version": 3,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "members": [
            "user:owner@example.com"
          ],
          "role": "roles/owner"
        },
        **{
          "members": [
            "user:noam@example.com"
          ],
          "role": "roles/resourcemanager.projectIamAdmin",
          "condition": {
            "title": "only_appengine_admin_viewer_roles",
            "description": "Only allows changes to role bindings with the App Engine Admin or Viewer roles",
            "expression":
              "api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', []).hasOnly(['roles/appengine.appAdmin', 'roles/appengine.appViewer'])"
          }
        }**
      ]
    }

This conditional role binding lets Noam do the following:

  * Grant the App Engine Admin and App Engine Viewer roles for the project.
  * Revoke the App Engine Admin and App Engine Viewer roles for the project.
  * Add, remove, or modify conditions for project-level role bindings that grant the App Engine Admin and App Engine Viewer roles.
  * Perform other actions allowed by the Project IAM Admin role that don't modify the project's allow policy. For example, Noam could use the [`projects.getIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy) method to get the project's allow policy.



This conditional role binding does not let Noam do any of the following:

  * Modify allow policies for resources other than the project.
  * Grant roles other than the App Engine Admin or App Engine Viewer roles.
  * Revoke roles other than the App Engine Admin or App Engine Viewer roles.
  * Add, remove, or modify conditions for role bindings that don't grant the App Engine Admin or App Engine Viewer roles.



### Allow users to manage limited IAM admins

Consider a scenario where you want to make a user, Lila, a limited IAM admin for her team. You want Lila to be able to grant and revoke only the Compute Admin role (`roles/compute.admin`) for her project. However, you also want to let Lila select other users to act as limited IAM admins. In other words, you want to let Lila allow other users to grant and revoke only the Compute Admin role.

You might think that the solution is to grant Lila the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`), and then give her the ability to grant or revoke that role for others. However, if you grant Lila the Project IAM Admin role, she could remove the condition from her own role and give herself the ability to grant or revoke any IAM role.

To help prevent this privilege escalation, you instead [create a Google group](https://support.google.com/groups/answer/2464926), `iam-compute-admins`, for the project's limited IAM admins. Then, you [add Lila to the group](https://support.google.com/groups/answer/2465464) and [make her a group manager](https://support.google.com/groups/answer/2464975).

After you create the group, you conditionally grant the group the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). The Project IAM Admin role allows group members to grant and revoke IAM roles, and the condition limits which roles they can grant and revoke:
    
    
    {
      "version": 3,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "members": [
            "user:owner@example.com"
          ],
          "role": "roles/owner"
        },
        **{
          "members": [
            "group:iam-compute-admins@example.com"
          ],
          "role": "roles/resourcemanager.projectIamAdmin",
          "condition": {
            "title": "only_compute_admin_role",
            "description": "Only allows changes to role bindings for the Compute Admin role",
            "expression":
              "api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', []).hasOnly(['roles/compute.admin'])"
          }
        }**
      ]
    }

As a **member** of the `iam-compute-admins` group, Lila can do the following:

  * Grant the Compute Admin role for the project by adding a new binding for the role, or by adding a principal to an existing binding for the role.
  * Revoke the Compute Admin role by removing an existing binding for the role, or by removing a principal from an existing binding for the role.
  * Modify grants for the Compute Admin role by adding, removing, or modifying conditions attached to bindings for the role.
  * Perform other actions allowed by the Project IAM Admin role that don't modify the project's allow policy. For example, she could use the [`projects.getIamPolicy`](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy) method to get the project's allow policy.



As a **manager** of the `iam-compute-admins` group, Lila can allow other users to grant or revoke the Compute Admin role by adding them to the `iam-compute-admins` group.

Lila cannot do the following:

  * Give herself the ability to grant or revoke other roles.
  * Modify allow policies for resources other than the project.
  * Grant roles other than the Compute Admin role.
  * Revoke roles other than the Compute Admin role.
  * Add, remove, or modify conditions for role bindings that don't grant the Compute Admin role.



## Limit role granting

The following sections explain how to let principals grant or revoke only certain roles.

**Caution:** Some Google Cloud services don't recognize limits on role granting. If a limited IAM admin tries to grant a role on a resource, and the resource's service does not recognize limits on role granting, then the request fails. For a list of services that recognize limits on role granting, see [ IAM API attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#api-attributes-iam). 

The exception to this behavior is [ BigQuery datasets](https://docs.cloud.google.com/bigquery/docs/reference/rest/v2/datasets). Datasets don't recognize the `modifiedGrantsByRole` attribute, but limited IAM admins can still grant or revoke roles on datasets. Specifically, if a limited IAM admin's role includes permissions to grant roles on datasets, **they can do so** , regardless of any limits placed on their role granting. 

### Write a condition expression to limit role granting

To limit a principal's ability to grant roles, write a condition expression that specifies the roles a principal can grant or revoke.

Use the following format for your condition expression:
    
    
    api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', []).hasOnly(roles)
    

This expression does the following:

  * Gets the API attribute `iam.googleapis.com/modifiedGrantsByRole` using the [`api.getAttribute()`](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#api-functions) function.

For a request to set the allow policy of a resource, this attribute contains the role names from the bindings that the request modifies. For other types of requests, the attribute is not defined. In these cases, the function returns the default value (`[]`).

**Note:** Not all services recognize the `iam.googleapis.com/modifiedGrantsByRole` attribute. If a service does not recognize this attribute, you cannot use this attribute to limit role granting for that service. For a list of services that recognize this attribute, see [IAM API attributes](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#api-attributes-iam).
  * Uses the `hasOnly()` [Common Expression Language (CEL)](https://github.com/google/cel-spec) function to define and enforce the roles that the principal is allowed to grant or revoke.

The input for the `hasOnly()` function is a list of the roles that the principal is allowed to grant or revoke. If the roles in the `iam.googleapis.com/modifiedGrantsByRole` attribute are included in this list, the function returns `true`. If they are not, the function returns `false`.

If the `iam.googleapis.com/modifiedGrantsByRole` attribute contains the default value (`[]`), the function returns `true`, because `[]` does not contain any roles not included in the list.




To customize this expression, replace `roles` with a list of the roles that the principal is allowed to grant or revoke. For example, to let the principal grant or revoke only the Pub/Sub Editor (`roles/pubsub.editor`) and Pub/Sub Publisher (`roles/pubsub.publisher`) roles, use the value `['roles/pubsub.editor', 'roles/pubsub.publisher']`.

You can include up to 10 values in the list of allowed roles. All of these values must be string constants.

**Note:** You cannot customize the default value for `api.getAttribute` functions involving `iam.googleapis.com/modifiedGrantsByRole`. It must be an empty list.

**Warning:** Don't include the following types of roles in the list of allowed roles: 

  * Roles with permissions to grant and revoke IAM roles (that is, roles with permission names that end in `setIamPolicy`). 
  * Custom roles that the limited IAM admin can modify. For example, if the limited IAM admin also has the Role Administrator role (`roles/iam.roleAdmin`) on a project, don't allow them to grant or revoke project-level custom roles. 



Both of these types of roles contain, or could contain, permission to modify allow policies. As a result, limited IAM admins who can grant and revoke these types of roles can give themselves permission to grant and revoke all IAM roles. 

For example, if a user is a limited IAM admin for a project, and you let them grant or revoke a custom role that they can modify, they could add the `resourcemanager.projects.setIamPolicy` permission to the custom role, then grant themselves that role unconditionally. They would then be able to grant and revoke all IAM roles for the project. 

#### Logical operators for `hasOnly()` statements

Don't use the `&&` or `||` operators to join multiple `hasOnly()` statements in a single condition. If you do, then requests that grant or revoke multiple roles might fail, even if the principal can grant or revoke those roles individually.

For example, consider the following condition:
    
    
    api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', [])
        .hasOnly(['roles/pubsub.editor']) ||
    api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', [])
        .hasOnly(['roles/pubsub.publisher'])
    

This condition evaluates to `true` if a request grants either the `roles/pubsub.editor` role or the `roles/pubsub.publisher` role, but it evaluates to `false` if a request grants _both_ the `roles/pubsub.editor` role and the `roles/pubsub.publisher` role.

### Limit role granting with conditional role bindings

To allow a principal to grant or revoke only certain roles, use the condition expression from the preceding section to create a conditional role binding. Then, add the conditional role binding to a resource's allow policy.

**Note:** Conditional role bindings do not override role bindings with no conditions. If a principal is bound to a role, and the role binding does not have a condition, then the principal always has that role. Adding the principal to a conditional binding for the same role has no effect. 

  1. Select a resource that represents the scope that you want to let a principal grant and revoke roles for:

     * If you want to let a principal grant and revoke certain roles for all resources within an **organization** , select an organization.
     * If you want to let a principal grant and revoke certain roles for all resources within an **folder** , select a folder.
     * If you want to let a principal grant and revoke certain roles for all resources within a **project** , select a project.
**Note:** While other resource types [recognize limits on role granting](https://docs.cloud.google.com/iam/docs/conditions-attribute-reference#api-attributes-iam), only projects, folders, and organizations accept conditions to limit role granting in their allow policies.
  2. Select a role that allows a principal to set the allow policy for the resource type you selected (project, folder, or organization). To follow the principle of least privilege, choose one of the following predefined roles:

     * **Projects** : Project IAM Admin (`roles/resourcemanager.projectIamAdmin`)
     * **Folders** : Folder IAM Admin (`roles/resourcemanager.folderIamAdmin`)
     * **Organizations** : Organization Admin (`roles/resourcemanager.organizationAdmin`).

**Note:** This role also allows principals to set the allow policy for projects and folders.

Alternatively, choose a custom role that includes the `resourcemanager.resource-type.setIamPolicy` and `resourcemanager.resource-type.getIamPolicy` permissions, where `resource-type` is `project`, `folder`, or `organization`.

**Note:** You can also select a role that allows a principal to set the allow policy for specific resources within a project, folder, or organization. For example, you could select the Storage Admin role, which includes permissions to set allow policies for buckets and objects. However, if you do so, the principal will also be able to use the other permissions included in the role.
  3. Conditionally grant a principal your chosen role on the project, folder, or organization you selected.

The new allow policy is applied, and your principal can modify bindings for only the roles you have allowed.

### Console

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to the IAM page](https://console.cloud.google.com/iam-admin/iam)

     2. Make sure the name of your project, folder, or organization appears in the resource selector at the top of the page. The resource selector tells you what project, folder, or organization you are currently working in.

If you don't see the name of your resource, click the resource selector, then select your resource.

     3. In the list of principals, locate the principal that will grant and revoke roles, and click the _edit_ button.

     4. In the **Edit permissions** panel, select the role you chose previously. Then under **IAM condition (optional)** , click **Add IAM condition**.

     5. In the **Edit condition** panel, enter a title and optional description for the condition.

     6. Click the **Condition editor** tab and enter the expression you wrote in Writing a condition expression to limit role granting. This expression limits which roles the principal can grant or revoke.

For example, the following condition expression limits the principal to granting and revoking the Pub/Sub Editor (`roles/pubsub.editor`) and Pub/Sub Publisher (`roles/pubsub.publisher`) roles:
            
            api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', []).hasOnly(['roles/pubsub.editor', 'roles/pubsub.publisher'])

**Warning:** Don't include the following types of roles in the list of allowed roles: 

        * Roles with permissions to grant and revoke IAM roles (that is, roles with permission names that end in `setIamPolicy`). 
        * Custom roles that the limited IAM admin can modify. For example, if the limited IAM admin also has the Role Administrator role (`roles/iam.roleAdmin`) on a project, don't allow them to grant or revoke project-level custom roles. 

Limited IAM admins who can grant and revoke these types of roles can give themselves permission to grant and revoke all IAM roles. See Writing a condition expression to limit role granting for more information. 

     7. Click **Save** to apply the condition.

     8. After the **Edit condition** panel is closed, click **Save** in the **Edit permissions** panel to update your allow policy.

### gcloud

Allow policies are set using the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern.

**First, read the allow policy for the resource:**

Execute the [`get-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/get-iam-policy) command. This command gets the current allow policy for the resource.

Command:
    
    gcloud resource-type get-iam-policy resource-id --format=json > path

Replace the following values:

     * `resource-type`: The resource type that you want to let a principal grant or revoke roles for. Use one of the following: `projects`, `resource-manager folders`, or `organizations`.
     * `resource-id`: Your Google Cloud project, folder, or organization ID.
     * `path`: The path of the file to download the allow policy to.

The allow policy is saved in JSON format, for example:
    
    {
      "bindings": [
        {
          "members": [
            "user:project-owner@example.com"
          ],
          "role": "roles/owner"
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 1
    }
    

**Next, modify the allow policy.**

To let a principal only modify bindings for certain roles, add the highlighted conditional role binding:
    
    {
      "bindings": [
        {
          "members": [
            "user:owner@example.com"
          ],
          "role": "roles/owner"
        },
        **{
          "members": [
            "principal"
          ],
          "role": "role",
          "condition": {
            "title": "title",
            "description": "description",
            "expression":
              "expression"
          }**
        }
      ],
      "etag": "BwWKmjvelug=",
      "version": 3
    }

Replace the following values:

     * `principal`: The principal that will grant or revoke certain roles. For example, `user:my-user@example.com`. To see the formats of each principal type, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).
     * `role`: The role you chose in the preceding steps. This role must include the `setIamPolicy` permission for the resource type you chose.
     * `title`: A string briefly describing the condition. For example, `only_pubsub_roles`.
     * `description`: Optional. An additional description for the condition. For example, `Only allows granting/revoking the Pub/Sub editor and publisher roles`.
     * `expression`: The expression you wrote in Writing a condition expression to limit role granting. This expression limits which roles that the principal can grant or revoke.

For example, the following condition expression limits the principal to granting and revoking the Pub/Sub Editor (`roles/pubsub.editor`) and Pub/Sub Publisher (`roles/pubsub.publisher`) roles:
           
           api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', []).hasOnly(['roles/pubsub.editor', 'roles/pubsub.publisher'])

**Warning:** Don't include the following types of roles in the list of allowed roles: 

       * Roles with permissions to grant and revoke IAM roles (that is, roles with permission names that end in `setIamPolicy`). 
       * Custom roles that the limited IAM admin can modify. For example, if the limited IAM admin also has the Role Administrator role (`roles/iam.roleAdmin`) on a project, don't allow them to grant or revoke project-level custom roles. 

Limited IAM admins who can grant and revoke these types of roles can give themselves permission to grant and revoke all IAM roles. See Writing a condition expression to limit role granting for more information. 

**Finally, write the updated allow policy:**

Set the new allow policy by executing the [`set-iam-policy`](https://docs.cloud.google.com/sdk/gcloud/reference/projects/set-iam-policy) command for the resource:
    
    gcloud resource-type set-iam-policy resource-id path

Replace the following values:

     * `resource-type`: The resource type that you want to let a principal grant or revoke roles for. Use one of the following: `projects`, `resource-manager folders`, or `organizations`.
     * `resource-id`: Your Google Cloud project, folder, or organization ID.
     * `path`: A path to the file containing the updated allow policy.

The new allow policy is applied, and the principal will be able to modify bindings for only the roles you have allowed.

### REST

Allow policies are set using the [read-modify-write](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access#policy-overview) pattern.

**First, read the allow policy for the resource:**

The Resource Manager API's `[get-iam-policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy)` method gets a project's, folder's, or organization's allow policy. 

Before using any of the request data, make the following replacements: 

     * `API_VERSION`: The API version to use. For projects and organizations, use `v1`. For folders, use `v2`.
     * `RESOURCE_TYPE`: The resource type whose policy you want to manage. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
     * `POLICY_VERSION`: The policy version to be returned. Requests should specify the most recent policy version, which is policy version 3\. See [Specifying a policy version when getting a policy](https://docs.cloud.google.com/iam/docs/allow-policies#specifying-version-get) for details.

HTTP method and URL: 
    
    POST https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:getIamPolicy

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
         "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:getIamPolicy"

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
        -Uri "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the resource's allow policy. For example: 
    
    {
      "version": 1,
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "role": "roles/owner",
          "members": [
            "user:my-user@example.com"
          ]
        }
      ]
    }
    

**Next, modify the allow policy.**

Add a conditional role binding that lets a principal grant and revoke only certain roles. Make sure to change the `version` field to the value `3`:
    
    {
      **"version" : 3,**
      "etag": "BwWKmjvelug=",
      "bindings": [
        {
          "members": [
            "user:owner@example.com"
          ],
          "role": "roles/owner"
        },
        **{
          "members": [
            "PRINCIPAL"
          ],
          "role": "ROLE",
          "condition": {
            "title": "TITLE",
            "description": "DESCRIPTION",
            "expression":
              "EXPRESSION"
          }**
        }
      ]
    }

     * `PRINCIPAL`: The principal that will grant or revoke certain roles. For example, `user:my-user@example.com`. To see the formats of each principal type, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).
     * `ROLE`: The role you chose in the preceding steps. This role must include the `setIamPolicy` permission for the resource type you chose.
     * `TITLE`: A string briefly describing the condition. For example, `only_pubsub_roles`.
     * `DESCRIPTION`: Optional. An additional description for the condition. For example, `Only allows granting/revoking the Pub/Sub editor and publisher roles`.
     * `EXPRESSION`: The expression you wrote in Writing a condition expression to limit role granting. This expression limits which roles that the principal can grant or revoke.

For example, the following condition expression limits the principal to granting and revoking the Pub/Sub Editor (`roles/pubsub.editor`) and Pub/Sub Publisher (`roles/pubsub.publisher`) roles:
           
           api.getAttribute('iam.googleapis.com/modifiedGrantsByRole', []).hasOnly(['roles/pubsub.editor', 'roles/pubsub.publisher'])

**Warning:** Don't include the following types of roles in the list of allowed roles: 

       * Roles with permissions to grant and revoke IAM roles (that is, roles with permission names that end in `setIamPolicy`). 
       * Custom roles that the limited IAM admin can modify. For example, if the limited IAM admin also has the Role Administrator role (`roles/iam.roleAdmin`) on a project, don't allow them to grant or revoke project-level custom roles. 

Limited IAM admins who can grant and revoke these types of roles can give themselves permission to grant and revoke all IAM roles. See Writing a condition expression to limit role granting for more information. 

**Finally, write the updated allow policy:**

The Resource Manager API's `[setIamPolicy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)` method sets the allow policy in the request as the new allow policy for the project, folder, or organization. 

Before using any of the request data, make the following replacements: 

     * `API_VERSION`: The API version to use. For projects and organizations, use `v1`. For folders, use `v2`.
     * `RESOURCE_TYPE`: The resource type whose policy you want to manage. Use the value `projects`, `folders`, or `organizations`.
     * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
     * `POLICY`: A JSON representation of the policy that you want to set. For more information about the format of a policy, see the [Policy reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).

For example, to set the policy shown in the previous step, replace `POLICY` with the following:
           
           {
             "version": 3,
             "etag": "BwWKmjvelug=",
             "bindings": [
               {
                 "members": [
                   "user:owner@example.com"
                 ],
                 "role": "roles/owner"
               },
               **{
                 "members": [
                   "principal"
                 ],
                 "role": "role",
                 "condition": {
                   "title": "title",
                   "description": "description",
                   "expression":
                     "expression"
                 }**
               }
             ]
           }

HTTP method and URL: 
    
    POST https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:setIamPolicy

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
         "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:setIamPolicy"

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
        -Uri "https://cloudresourcemanager.googleapis.com/API_VERSION/RESOURCE_TYPE/RESOURCE_ID:setIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

The response contains the updated allow policy.

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 




## What's next

  * Enforce the principle of least privilege with [role recommendations](https://docs.cloud.google.com/iam/docs/recommender-overview). 
  * Learn how to use IAM Conditions to [configure temporary access](https://docs.cloud.google.com/iam/docs/configuring-temporary-access) and [configure resource-based access](https://docs.cloud.google.com/iam/docs/configuring-resource-based-access).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
