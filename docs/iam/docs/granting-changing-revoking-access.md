---
url: https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access/
title: Manage access to projects, folders, and organizations \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:30:46.208622+00:00
---

# Manage access to projects, folders, and organizations  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Manage access to projects, folders, and organizations Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to grant, change, and revoke access to projects, folders, and organizations. When you grant access to projects, folders, and organizations, you also grant access to the resources inside them.

**Note:** The IAM role picker uses Gemini to help you find and grant the right predefined roles to your principals. For more information, see [Get predefined role suggestions with Gemini assistance](https://docs.cloud.google.com/iam/docs/role-picker-gemini). 

To learn how to manage access to other resources, see the following guides:

  * [Manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts)
  * [Manage access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources)

**Note:** Granting access to projects, folders, and organizations is considered a sensitive action; in some cases, you might need to reauthenticate before you can initiate the action. For more information, see [Sensitive actions](https://docs.cloud.google.com/docs/authentication/reauthentication#sensitive-actions). 

In Identity and Access Management (IAM), access is granted through _allow policies_ , also known as IAM policies. An allow policy is attached to a Google Cloud resource. Each allow policy contains a collection of _role bindings_ that associate one or more principals, such as users or service accounts, with an IAM role. These role bindings grant the specified roles to the principals, both on the resource that the allow policy is attached to and on all of that resource's [descendants](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). For more information about allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

**Note:** If you're getting started with Google Cloud, you can grant the appropriate IAM roles to your organization administrator groups as part of the [Google Cloud setup process](https://docs.cloud.google.com/docs/enterprise/setup-checklist).

You can manage access to projects, folders, and organizations with the Google Cloud console, the Google Cloud CLI, the REST API, or the [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries).

**Note:** You can also use deny policies to prevent principals from using specific IAM permissions. For more information, see [Deny policies](https://docs.cloud.google.com/iam/docs/deny-overview). 

## Before you begin

  * Ensure that you have the IAM roles required to manage access.

When you create a project, folder, or organization, you are automatically granted a role that lets you manage access for that resource. For more information, see [Default policies](https://docs.cloud.google.com/iam/docs/allow-policies#default).

If you didn't create your project, folder, or organization, then ask your administrator to grant you the required roles.

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

### Console

When you use the Google Cloud console to access Google Cloud services and APIs, you don't need to set up authentication. 

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### C#

To use the .NET samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Java

To use the Java samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### Python

To use the Python samples on this page in a local development environment, install and initialize the gcloud CLI, and then set up Application Default Credentials with your user credentials. 

    1. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

    2. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

    3. If you're using a local shell, then create local authentication credentials for your user account: 
           
           gcloud auth application-default login

You don't need to do this if you're using Cloud Shell.

If an authentication error is returned, and you are using an external identity provider (IdP), confirm that you have [ signed in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [ Set up ADC for a local development environment](https://docs.cloud.google.com/docs/authentication/set-up-adc-local-dev-environment) in the Google Cloud authentication documentation. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 




### Required roles

To get the permissions that you need to manage access to a project, folder, or organization, ask your administrator to grant you the following IAM roles on the resource that you want to manage access for (project, folder, or organization): 

  * To manage access to a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * To manage access to a folder: [Folder Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderAdmin) (`roles/resourcemanager.folderAdmin`) 
  * To manage access to projects, folders, and organizations: [Organization Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) 
  * To manage access to almost all Google Cloud resources: [Security Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.securityAdmin) (`roles/iam.securityAdmin`) 



These predefined roles contain the permissions required to manage access to a project, folder, or organization. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to manage access to a project, folder, or organization:

  * To manage access to projects: 
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`
  * To manage access to folders: 
    * `resourcemanager.folders.getIamPolicy`
    * `resourcemanager.folders.setIamPolicy`
  * To manage access to organizations: 
    * `resourcemanager.organizations.getIamPolicy`
    * `resourcemanager.organizations.setIamPolicy`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

## View current access

You can view who has access to your project, folder, or organization using the Google Cloud console, the gcloud CLI, the REST API, or the Resource Manager client libraries.

**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

### Console

**Note:** The Google Cloud console shows access in a list form, rather than directly showing the resource's allow policy.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

The Google Cloud console lists all the principals who have been granted roles on your project, folder, or organization. This list includes principals who have inherited roles on the resource from parent resources. For more information about policy inheritance, see [Policy inheritance and the resource hierarchy](https://docs.cloud.google.com/iam/docs/allow-policies#inheritance).

  3. Optional: To view role grants for [service agents](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox.

![](https://docs.cloud.google.com/static/iam/img/include-google-provided-role-grants.png)

![](https://docs.cloud.google.com/static/iam/img/include-google-provided-role-grants-2x.png)




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To see who has access to your project, folder, or organization, get the allow policy for the resource. To learn how to interpret allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

**Note:** A resource's allow policy does not show any roles gained through [policy inheritance](https://docs.cloud.google.com/iam/docs/allow-policies#inheritance). To view inherited roles, use the Google Cloud console, or follow the instructions on [Viewing effective IAM policies](https://docs.cloud.google.com/asset-inventory/docs/view-effective-iam-policies). 

To get the allow policy for the resource, run the `get-iam-policy` command for the resource:
         
         gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format=FORMAT > PATH

Provide the following values:

     * `RESOURCE_TYPE`: The type of the resource that you want to view access to. Use one of these values: `projects`, `resource-manager folders`, or `organizations`.

     * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

     * `FORMAT`: The desired format for the policy. Use `json` or `yaml`.

     * `PATH`: The path to a new output file for the policy.

For example, the following command gets the policy for the project `my-project` and saves it to your home directory in JSON format:
    
    gcloud projects get-iam-policy my-project --format=json > ~/policy.json




### C#

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

To see who has access to your project, folder, or organization, get the allow policy for the resource. To learn how to interpret allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy for a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy GetPolicy(string projectId)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            var policy = service.Projects.GetIamPolicy(new GetIamPolicyRequest(),
                projectId).Execute();
            return policy;
        }
    }
    

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

To see who has access to your project, folder, or organization, get the allow policy for the resource. To learn how to interpret allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy for a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class GetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
    
        getProjectPolicy(projectId);
      }
    
      // Gets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getProjectPolicy(String projectId) throws IOException {
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId).toString())
                  .build();
          return projectsClient.getIamPolicy(request);
        }
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

To see who has access to your project, folder, or organization, get the allow policy for the resource. To learn how to interpret allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy for a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    from google.cloud import resourcemanager_v3
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def get_project_policy(project_id: str) -> policy_pb2.Policy:
        """Get policy for project.
    
        project_id: ID or number of the Google Cloud project you want to use.
        """
    
        client = resourcemanager_v3.ProjectsClient()
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        policy = client.get_iam_policy(request)
        print(f"Policy retrieved: {policy}")
    
        return policy

### REST

To see who has access to your project, folder, or organization, get the allow policy for the resource. To learn how to interpret allow policies, see [Understanding allow policies](https://docs.cloud.google.com/iam/docs/allow-policies).

**Note:** A resource's allow policy does not show any roles gained through [policy inheritance](https://docs.cloud.google.com/iam/docs/allow-policies#inheritance). To view inherited roles, use the Google Cloud console, or follow the instructions on [Viewing effective IAM policies](https://docs.cloud.google.com/asset-inventory/docs/view-effective-iam-policies). 

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
    

## Grant or revoke a single IAM role

You can use the Google Cloud console and the gcloud CLI to quickly grant or revoke a single role for a single principal, without editing the resource's allow policy directly. Common types of principals include Google Accounts, service accounts, Google groups, and domains. For a list of all principal types, see [Principal types](https://docs.cloud.google.com/iam/docs/principals-overview#principal-types).

**Note:** If the [`iam.allowedPolicyMemberDomains`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) organization policy constraint is enforced in your organization, then you might not be able to grant roles to newly created groups. If you get a `failedPrecondition` error when trying to grant a role to a newly created group, wait 24 hours, and then try granting the role again. 

In general, policy changes take effect within 2 minutes. However, in some cases, it can take 7 minutes or more for changes to propagate across the system. 

If you need help identifying the most appropriate predefined role, see [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

### Grant a single IAM role

To grant a single role to a principal, do the following:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. Select a principal to grant a role to:

     * To grant a role to a principal who already has other roles on the resource, find a row containing the principal, click edit **Edit principal** in that row, and click add **Add another role**.

To grant a role to a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox to see its email address.

**Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted.
     * To grant a role to a principal who doesn't have any existing roles on the resource, click person_add **Grant Access** , then enter a [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers)—for example, `my-user@example.com` or `//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

  4. Click **Select a role** , then search for a role to grant based on the following: 

     * The role name
     * The Google Cloud product that you want to grant access to
     * The permission that you want to give
     * The job function to perform
To follow the principle of least privilege, [choose a role](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) that includes only the permissions that your principal needs.
  5. Optional: Add a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role.

  6. Click **Save**. The principal is granted the role on the resource.




To grant a role to a principal for more than one project, folder, or organization, do the following:

  1. In the Google Cloud console, go to the **Manage resources** page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. Select all the resources for which you want to grant permissions.

  3. If the info panel is not visible, click **Show info panel**. Then, click **Permissions**.

  4. Select a principal to grant a role to:

     * To grant a role to a principal who already has other roles, find a row containing the principal, click edit**Edit principal** in that row, and click add**Add another role**.
     * To grant a role to a principal who does not already have other roles, click person_add **Grant access** , then enter a [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers)—for example, `my-user@example.com` or `//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.
  5. Click **Select a role** , then search for a role to grant based on the following: 

     * The role name
     * The Google Cloud product that you want to grant access to
     * The permission that you want to give
     * The job function to perform
To follow the principle of least privilege, [choose a role](https://docs.cloud.google.com/iam/docs/choose-predefined-roles) that includes only the permissions that your principal needs.
  6. Optional: Add a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role.

  7. Click **Save**. The principal is granted the selected role on each of the selected resources.




### gcloud

**Note:** To grant the Owner role (`roles/owner`) on a project to a user outside of your organization, you must use the Google Cloud console, not the gcloud CLI. If your project is not part of an organization, you must use the Google Cloud console to grant the Owner role.

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. The `[add-iam-policy-binding](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` command lets you quickly grant a role to a principal. 

Before using any of the command data below, make the following replacements: 

     * `RESOURCE_TYPE`: The resource type that you want to manage access to. Use `projects`, `resource-manager folders`, or `organizations`.

     * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

     * `PRINCIPAL`: An identifier for the principal, or member, which usually has the following form: `PRINCIPAL_TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`. For a full list of the values that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

     * `ROLE_NAME`: The name of the role that you want to grant. Use one of the following formats: 

       * Predefined roles: `roles/SERVICE.IDENTIFIER`
       * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
       * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles). 

     * `CONDITION`: The condition to add to the role binding. If you don't want to add a condition, use the value `None`. For more information about conditions, see the [conditions overview](https://docs.cloud.google.com/iam/docs/conditions-overview).

Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID \
        --member=PRINCIPAL --role=ROLE_NAME \
        --condition=CONDITION

#### Windows (PowerShell)
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID `
        --member=PRINCIPAL --role=ROLE_NAME `
        --condition=CONDITION

#### Windows (cmd.exe)
    
    gcloud RESOURCE_TYPE add-iam-policy-binding RESOURCE_ID ^
        --member=PRINCIPAL --role=ROLE_NAME ^
        --condition=CONDITION

The response contains the updated IAM allow policy. 




**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

### Revoke a single IAM role

To revoke a single role from a principal, do the following:

### Console

  1. In the Google Cloud console, go to the **IAM** page.

[ Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. Find the row containing the principal whose access you want to revoke. Then, click  edit **Edit principal** in that row.

**Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted.
  4. Click the **Delete** delete button for the role that you want to revoke, and then click **Save**.




### gcloud

  1. In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

  2. To quickly revoke a role from a user, run the `remove-iam-policy-binding` command:
         
         gcloud RESOURCE_TYPE remove-iam-policy-binding RESOURCE_ID   
             --member=PRINCIPAL --role=ROLE_NAME

Provide the following values:

     * `RESOURCE_TYPE`: The resource type that you want to manage access to. Use `projects`, `resource-manager folders`, or `organizations`.

     * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

     * `PRINCIPAL`: An identifier for the principal, or member, which usually has the following form: `PRINCIPAL_TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`. 

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview).

     * `ROLE_NAME`: The name of the role that you want to revoke. Use one of the following formats: 

       * Predefined roles: `roles/SERVICE.IDENTIFIER`
       * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
       * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles). 

For example, to revoke the Project Creator role from the service account `example-service-account@example-project.iam.gserviceaccount.com` for the project `example-project`:
    
    gcloud projects remove-iam-policy-binding example-project   
          --member=serviceAccount:example-service-account@example-project.iam.gserviceaccount.com   
          --role=roles/resourcemanager.projectCreator




To help ensure that you don't revoke any necessary roles, you can enable [change risk recommendations](https://docs.cloud.google.com/recommender/docs/change-risk-recommendations). Change risk recommendations generate warnings when you try to revoke project-level roles that Google Cloud has identified as important.

## Grant or revoke multiple IAM roles using the Google Cloud console

You can use the Google Cloud console to grant and revoke multiple roles for a single principal:

  1. In the Google Cloud console, go to the **IAM** page.

[ Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project,folder,organizationId)

  2. Select a project, folder, or organization.

  3. Select the principal whose roles you want to modify:

     * To modify roles for a principal who already has roles on the resource, find a row containing the principal, click edit **Edit principal** in that row, and click add **Add another role**.

To modify roles for a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox to see its email address.

**Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted.
     * To grant roles to a principal who doesn't have any roles on the resource, click person_add **Grant Access** , then enter a [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers)—for example, `my-user@example.com` or `//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

  4. Modify the principal's roles:

     * To grant a role to a principal who doesn't have any existing roles on the resource, click **Select a role** , then search for a role to grant.
     * To grant an additional role to the principal, click **Add another role** , then search for a role to grant.
     * To replace one of the principal's roles with a different role, click the existing role, then search for a different role to grant.
     * To revoke one of the principal's roles, click the **Delete** delete button for each role that you want to revoke.

You can also [add a condition](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#add) to a role, [modify a role's condition](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#modify), or [remove a role's condition](https://docs.cloud.google.com/iam/docs/managing-conditional-role-bindings#removing).

  5. Click **Save**.




**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

## Grant or revoke multiple IAM roles programmatically

To make large-scale access changes that involve granting and revoking multiple roles for multiple principals, use the _read-modify-write_ pattern to update the resource's allow policy:

  1. Read the current allow policy by calling `getIamPolicy()`.
  2. Edit the allow policy, either by using a text editor or programmatically, to add or remove any principals or role bindings.
  3. Write the updated allow policy by calling `setIamPolicy()`.



You can use the gcloud CLI, the REST API, or the Resource Manager client libraries to update the allow policy.

**Note:** If the [`iam.allowedPolicyMemberDomains`](https://docs.cloud.google.com/resource-manager/docs/organization-policy/restricting-domains) organization policy constraint is enforced in your organization, then you might not be able to grant roles to newly created groups. If you get a `failedPrecondition` error when trying to grant a role to a newly created group, wait 24 hours, and then try granting the role again. 

In general, policy changes take effect within 2 minutes. However, in some cases, it can take 7 minutes or more for changes to propagate across the system. 

### Get the current allow policy

### gcloud

The `[gcloud get-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` command gets a project's, folder's, or organization's allow policy. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the resource that you want to get the allow policy for. Valid values are `projects`, `resource-manager folders`, or `organizations`.

  * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

  * `FORMAT`: The desired format for the allow policy. Use `json` or `yaml`.

  * `PATH`: The path to a new output file for the allow policy.




Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format=FORMAT > PATH

#### Windows (PowerShell)
    
    
    gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format=FORMAT > PATH

#### Windows (cmd.exe)
    
    
    gcloud RESOURCE_TYPE get-iam-policy RESOURCE_ID --format=FORMAT > PATH

For example, the following command gets the allow policy for the project `my-project` and saves it to your home directory in JSON format:
    
    
    gcloud projects get-iam-policy my-project --format json > ~/policy.json

### C#

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy of a folder or organization, review the [Resource Managerclient library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy GetPolicy(string projectId)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            var policy = service.Projects.GetIamPolicy(new GetIamPolicyRequest(),
                projectId).Execute();
            return policy;
        }
    }
    

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy of a folder or organization, review the [Resource Managerclient library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.iam.v1.[GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    
    public class GetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
    
        getProjectPolicy(projectId);
      }
    
      // Gets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) getProjectPolicy(String projectId) throws IOException {
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html) request = [GetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.GetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId).toString())
                  .build();
          return projectsClient.getIamPolicy(request);
        }
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to get the allow policy for a project. To learn how to get the allow policy of a folder or organization, review the [Resource Managerclient library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    from google.cloud import resourcemanager_v3
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def get_project_policy(project_id: str) -> policy_pb2.Policy:
        """Get policy for project.
    
        project_id: ID or number of the Google Cloud project you want to use.
        """
    
        client = resourcemanager_v3.ProjectsClient()
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        policy = client.get_iam_policy(request)
        print(f"Policy retrieved: {policy}")
    
        return policy

### REST

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
    

Save the response in a file of the appropriate type (`json` or `yaml`).

### Modify the allow policy

Programmatically or using a text editor, modify the local copy of your resource's allow policy to reflect the roles that you want to grant or revoke.

To help prevent you from overwriting other changes, don't edit or remove the allow policy's `etag` field. The `etag` field identifies the current state of the allow policy. When you set the updated allow policy, IAM compares the `etag` value in the request with the existing `etag`, and only writes the allow policy if the values match.

**Important:** None of your changes will take effect until you set the updated allow policy.

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

Replace the following:

  * `ROLE_NAME`: The name of the role that you want to grant. Use one of the following formats:

    * Predefined roles: `roles/SERVICE.IDENTIFIER`
    * Project-level custom roles: `projects/PROJECT_ID/roles/IDENTIFIER`
    * Organization-level custom roles: `organizations/ORG_ID/roles/IDENTIFIER`

For a list of predefined roles, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles).

  * `PRINCIPAL_1`, `PRINCIPAL_2`, `...PRINCIPAL_N`: Identifiers for the principals that you want to grant the role to.

Principal identifiers usually have the following form: `PRINCIPAL-TYPE:ID`. For example, `user:my-user@example.com` or `principalSet://iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`. For a full list of the values that `PRINCIPAL` can have, see [Principal identifiers](https://docs.cloud.google.com/iam/docs/principal-identifiers).

For the principal type `user`, the domain name in the identifier must be a Google Workspace domain or a Cloud Identity domain. To learn how to set up a Cloud Identity domain, see the [overview of Cloud Identity](https://docs.cloud.google.com/identity/docs/overview). 

  * `CONDITIONS`: Optional. Any [conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) that specify when access will be granted.




#### Grant an IAM role

To grant roles to your principals, modify the role bindings in the allow policy. To learn what roles you can grant, see [Understanding roles](https://docs.cloud.google.com/iam/docs/understanding-roles), or [view grantable roles](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles) for the resource. If you need help to identify the most appropriate predefined roles, see [Find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).

Optionally, you can use [conditions](https://docs.cloud.google.com/iam/docs/conditions-overview) to grant roles only when certain requirements are met.

To grant a role that is already included in the allow policy, add the principal to an existing role binding:

### gcloud

Edit the returned allow policy by adding the principal to an existing role binding. This change won't take effect until you set the updated allow policy.

For example, imagine the allow policy contains the following role binding, which grants the Security Reviewer role (`roles/iam.securityReviewer`) to Kai:
    
    
    {
      "role": "roles/iam.securityReviewer",
      "members": [
        "user:kai@example.com"
      ]
    }
    

To grant that same role to Raha, add Raha's principal identifier to the existing role binding:
    
    
    {
      "role": "roles/iam.securityReviewer",
      "members": [
        "user:kai@example.com",
        **"user:raha@example.com"**
      ]
    }

### C#

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    using System.Linq;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy AddMember(Policy policy, string role, string member)
        {
            var binding = policy.Bindings.First(x => x.Role == role);
            binding.Members.Add(member);
            return policy;
        }
    }
    

### Go

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    import (
    	"fmt"
    	"io"
    
    	"google.golang.org/api/iam/v1"
    )
    
    // addMember adds a member to a role binding.
    func addMember(w io.Writer, policy *iam.Policy, role, member string) {
    	for _, binding := range policy.Bindings {
    		if binding.Role != role {
    			continue
    		}
    		for _, m := range binding.Members {
    			if m != member {
    				continue
    			}
    			fmt.Fprintf(w, "Role %q found. Member already exists.\n", role)
    			return
    		}
    		binding.Members = append(binding.Members, member)
    		fmt.Fprintf(w, "Role %q found. Member added.\n", role)
    		return
    	}
    	fmt.Fprintf(w, "Role %q not found. Member not added.\n", role)
    }
    

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.util.ArrayList;
    import java.util.List;
    
    public class AddMember {
      public static void main(String[] args) {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
        // TODO: Replace with your role.
        String role = "roles/existing-role";
        // TODO: Replace with your principal.
        // For examples, see https://cloud.google.com/iam/docs/principal-identifiers
        String member = "principal-id";
    
        addMember(policy, role, member);
      }
    
      // Adds a principal to a pre-existing role.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) addMember([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String role, String member) {
        List<Binding> newBindingsList = new ArrayList<>();
    
        for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
          if (b.getRole().equals(role)) {
            newBindingsList.add(b.toBuilder().[addMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addMembers_java_lang_String_)(member).build());
          } else {
            newBindingsList.add(b);
          }
        }
    
        // Update the policy to add the principal.
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)()
                .[clearBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__)()
                .[addAllBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__)(newBindingsList)
                .build();
    
        System.out.println("Added principal: " + updatedPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)());
    
        return updatedPolicy;
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    from google.iam.v1 import policy_pb2
    from snippets.get_policy import get_project_policy
    from snippets.set_policy import set_project_policy
    
    
    def modify_policy_add_principal(
        project_id: str, role: str, principal: str
    ) -> policy_pb2.Policy:
        """Add a principal to certain role in project policy.
    
        project_id: ID or number of the Google Cloud project you want to use.
        role: role to which principal need to be added.
        principal: The principal requesting access.
    
        For principal ID formats, see https://cloud.google.com/iam/docs/principal-identifiers
        """
        policy = get_project_policy(project_id)
    
        for bind in policy.bindings:
            if bind.role == role:
                bind.members.append(principal)
                break
    
        return set_project_policy(project_id, policy)

### REST

Edit the returned allow policy by adding the principal to an existing role binding. This change won't take effect until you set the updated allow policy.

For example, imagine the allow policy contains the following role binding, which grants the Security Reviewer role (`roles/iam.securityReviewer`) to Kai:
    
    
    {
      "role": "roles/iam.securityReviewer",
      "members": [
        "user:kai@example.com"
      ]
    }
    

To grant that same role to Raha, add Raha's principal identifier to the existing role binding:
    
    
    {
      "role": "roles/iam.securityReviewer",
      "members": [
        "user:kai@example.com",
        **"user:raha@example.com"**
      ]
    }

To grant a role that is not yet included in the allow policy, add a new role binding:

### gcloud

Edit the allow policy by adding a new role binding that grants the role to the principal. This change won't take effect until you set the updated allow policy.

For example, to grant the Compute Storage Admin role (`roles/compute.storageAdmin`) to Raha, add the following role binding to the `bindings` array for the allow policy:
    
    
    {
      "role": "roles/compute.storageAdmin",
      "members": [
        "user:raha@example.com"
      ]
    }
    

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    using System.Collections.Generic;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy AddBinding(Policy policy, string role, string member)
        {
            var binding = new Binding
            {
                Role = role,
                Members = new List<string> { member }
            };
            policy.Bindings.Add(binding);
            return policy;
        }
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.util.Collections;
    import java.util.List;
    
    public class AddBinding {
      public static void main(String[] args) {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your policy: GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
        // TODO: Replace with your role.
        String role = "roles/role-to-add";
        // TODO: Replace with your principals.
        // For examples, see https://cloud.google.com/iam/docs/principal-identifiers
        List<String> members = Collections.singletonList("principal-id");
    
        addBinding(policy, role, members);
      }
    
      // Adds a principals to a role.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) addBinding([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String role, List<String> members) {
        [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html).newBuilder()
                .setRole(role)
                .[addAllMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__)(members)
                .build();
    
        // Update bindings for the policy.
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)().[addBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addBindings_com_google_iam_v1_Binding_)(binding).build();
    
        System.out.println("Added binding: " + updatedPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)());
    
        return updatedPolicy;
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    def modify_policy_add_role(policy: dict, role: str, principal: str) -> dict:
        """Adds a new role binding to a policy."""
    
        binding = {"role": role, "members": [principal]}
        policy["bindings"].append(binding)
        print(policy)
        return policy

### REST

Edit the allow policy by adding a new role binding that grants the role to the principal. This change won't take effect until you set the updated allow policy.

For example, to grant the Compute Storage Admin role (`roles/compute.storageAdmin`) to Raha, add the following role binding to the `bindings` array for the allow policy:
    
    
    {
      "role": "roles/compute.storageAdmin",
      "members": [
        "user:raha@example.com"
      ]
    }
    

You can only grant roles related to activated API services. If a service, such as Compute Engine, is not active, you cannot grant roles exclusively related to Compute Engine. For more information, see [Enable and disable APIs](https://support.google.com/cloud/answer/6158841).

There are some unique constraints when granting permissions on projects, especially when granting the Owner (`roles/owner`) role. See the [`projects.setIamPolicy()`reference documentation](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy) for more information.

#### Revoke an IAM role

To revoke a role, remove the principal from the role binding. If there are no other principals in the role binding, remove the entire role binding.

**Note:** Role bindings with no principals are not allowed and will result in an error when setting the allow policy.

### gcloud

Revoke a role by editing the JSON or YAML allow policy returned by the `get-iam-policy` command. This change won't take effect until you set the updated allow policy.

To revoke a role from a principal, delete the principal or binding from the `bindings` array for the allow policy.

### C#

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM C# API reference documentation](https://developers.google.com/api-client-library/dotnet/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    using System.Linq;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy RemoveMember(Policy policy, string role, string member)
        {
            try
            {
                var binding = policy.Bindings.First(x => x.Role == role);
                if (binding.Members.Count != 0 && binding.Members.Contains(member))
                {
                    binding.Members.Remove(member);
                }
                if (binding.Members.Count == 0)
                {
                    policy.Bindings.Remove(binding);
                }
                return policy;
            }
            catch (System.InvalidOperationException e)
            {
                System.Diagnostics.Debug.WriteLine("Role does not exist in policy: \n" + e.ToString());
                return policy;
            }
        }
    }

### Go

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Go API reference documentation](https://pkg.go.dev/cloud.google.com/go/iam/admin/apiv1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    import (
    	"fmt"
    	"io"
    
    	"google.golang.org/api/iam/v1"
    )
    
    // removeMember removes a member from a role binding.
    func removeMember(w io.Writer, policy *iam.Policy, role, member string) {
    	bindings := policy.Bindings
    	bindingIndex, memberIndex := -1, -1
    	for bIdx := range bindings {
    		if bindings[bIdx].Role != role {
    			continue
    		}
    		bindingIndex = bIdx
    		for mIdx := range bindings[bindingIndex].Members {
    			if bindings[bindingIndex].Members[mIdx] != member {
    				continue
    			}
    			memberIndex = mIdx
    			break
    		}
    	}
    	if bindingIndex == -1 {
    		fmt.Fprintf(w, "Role %q not found. Member not removed.\n", role)
    		return
    	}
    	if memberIndex == -1 {
    		fmt.Fprintf(w, "Role %q found. Member not found.\n", role)
    		return
    	}
    
    	members := removeIdx(bindings[bindingIndex].Members, memberIndex)
    	bindings[bindingIndex].Members = members
    	if len(members) == 0 {
    		bindings = removeIdx(bindings, bindingIndex)
    		policy.Bindings = bindings
    	}
    	fmt.Fprintf(w, "Role %q found. Member removed.\n", role)
    }
    
    // removeIdx removes arr[idx] from arr.
    func removeIdx[T any](arr []T, idx int) []T {
    	return append(arr[:idx], arr[idx+1:]...)
    }
    

### Java

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Java API reference documentation](https://developers.google.com/api-client-library/java/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    import com.google.iam.v1.[Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import java.io.IOException;
    import java.util.ArrayList;
    import java.util.List;
    
    public class RemoveMember {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
        // TODO: Replace with your role.
        String role = "roles/existing-role";
        // TODO: Replace with your principal.
        // For examples, see https://cloud.google.com/iam/docs/principal-identifiers
        String member = "principal-id";
    
        removeMember(policy, role, member);
      }
    
      // Removes principal from a role; removes binding if binding contains no members.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) removeMember([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String role, String member) {
        // Creating new builder with all values copied from origin policy
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).Builder policyBuilder = policy.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_toBuilder__)();
    
        // Getting binding with suitable role.
        [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) binding = null;
        for ([Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) b : policy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)()) {
          if (b.getRole().equals(role)) {
            binding = b;
            break;
          }
        }
    
        if (binding != null && binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().contains(member)) {
          List<String> newMemberList = new ArrayList<>(binding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)());
          // Removing principal from the role
          newMemberList.remove(member);
    
          System.out.println("Member " + member + " removed from " + role);
    
          // Adding all remaining principals to create new binding
          [Binding](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html) newBinding = binding.[toBuilder](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_toBuilder__)()
                  .[clearMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_clearMembers__)()
                  .[addAllMembers](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.Builder.html#com_google_iam_v1_Binding_Builder_addAllMembers_java_lang_Iterable_java_lang_String__)(newMemberList)
                  .build();
    
          List<Binding> newBindingList = new ArrayList<>(policyBuilder.getBindingsList());
    
          // Removing old binding to replace with new one
          newBindingList.remove(binding);
    
          // If binding has no more members, binding will not be added
          if (!newBinding.[getMembersList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Binding.html#com_google_iam_v1_Binding_getMembersList__)().isEmpty()) {
            newBindingList.add(newBinding);
          }
    
          // Update the policy to remove the principal.
          policyBuilder.[clearBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_clearBindings__)()
                  .[addAllBindings](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.Builder.html#com_google_iam_v1_Policy_Builder_addAllBindings_java_lang_Iterable___extends_com_google_iam_v1_Binding__)(newBindingList);
        }
    
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) updatedPolicy = policyBuilder.build();
    
        System.out.println("Exising principals: " + updatedPolicy.[getBindingsList](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html#com_google_iam_v1_Policy_getBindingsList__)());
    
        return updatedPolicy;
      }
    }

### Python

To learn how to install and use the client library for IAM, see [IAM client libraries](https://docs.cloud.google.com/iam/docs/reference/libraries). For more information, see the [IAM Python API reference documentation](https://developers.google.com/api-client-library/python/apis/iam/v1). 

To authenticate to IAM, set up Application Default Credentials. For more information, see Before you begin. 

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 
    
    
    from google.iam.v1 import policy_pb2
    from snippets.get_policy import get_project_policy
    from snippets.set_policy import set_project_policy
    
    
    def modify_policy_remove_principal(
        project_id: str, role: str, principal: str
    ) -> policy_pb2.Policy:
        """Remove a principal from certain role in project policy.
    
        project_id: ID or number of the Google Cloud project you want to use.
        role: role to revoke.
        principal: The principal to revoke access from.
    
        For principal ID formats, see https://cloud.google.com/iam/docs/principal-identifiers
        """
        policy = get_project_policy(project_id)
    
        for bind in policy.bindings:
            if bind.role == role:
                if principal in bind.members:
                    bind.members.remove(principal)
                break
    
        return set_project_policy(project_id, policy, False)

### REST

Revoke a role by editing the JSON or YAML allow policy returned by the `get-iam-policy` command. This change won't take effect until you set the updated allow policy.

To revoke a role from a principal, delete the principal or binding from the `bindings` array for the allow policy.

### Set the allow policy

After you modify the allow policy to grant and revoke roles, call `setIamPolicy()` to update the policy.

**Warning:** Setting a new allow policy permanently overwrites the existing allow policy on the resource. To avoid removing role bindings unintentionally, always follow the read-modify-write pattern when updating an allow policy: read the existing allow policy, modify it as needed, and then write the updated version of the allow policy.

### gcloud

The `[gcloud set-iam-policy](https://docs.cloud.google.com/sdk/gcloud/reference/projects/add-iam-policy-binding)` command sets the policy in the request as the new allow policy for the project, folder, or organization. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the resource that you want to set the allow policy for. Valid values are `projects`, `resource-manager folders`, or `organizations`.

  * `RESOURCE_ID`: Your Google Cloud project, folder, or organization ID. Project IDs are alphanumeric, like `my-project`. Folder and organization IDs are numeric, like `123456789012`.

  * `PATH`: The path to a file that contains the new allow policy.




Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

#### Windows (PowerShell)
    
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

#### Windows (cmd.exe)
    
    
    gcloud RESOURCE_TYPE set-iam-policy RESOURCE_ID PATH

The response contains the updated allow policy.

For example, the following command sets the allow policy stored in `policy.json` as the allow policy for the project `my-project`:
    
    
    gcloud projects set-iam-policy my-project ~/policy.json

**Note:** If you treat policies as code and store them in a version-control system, you should store the policy that is returned, not the policy that you sent in the request. 

### C#
    
    
    using [Google.Apis.Auth.OAuth2](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.html);
    using Google.Apis.CloudResourceManager.v1;
    using Google.Apis.CloudResourceManager.v1.Data;
    
    public partial class AccessManager
    {
        public static Policy SetPolicy(string projectId, Policy policy)
        {
            var credential = [GoogleCredential](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html).[GetApplicationDefault](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_GetApplicationDefault)()
                .[CreateScoped](https://docs.cloud.google.com/dotnet/docs/reference/Google.Apis/latest/Google.Apis.Auth.OAuth2.GoogleCredential.html#Google_Apis_Auth_OAuth2_GoogleCredential_CreateScoped_System_Collections_Generic_IEnumerable_System_String__)(CloudResourceManagerService.Scope.CloudPlatform);
            var service = new CloudResourceManagerService(
                new CloudResourceManagerService.Initializer
                {
                    HttpClientInitializer = credential
                });
    
            return service.Projects.SetIamPolicy(new SetIamPolicyRequest
            {
                Policy = policy
            }, projectId).Execute();
        }
    }
    

### Java

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to set the allow policy for a project. To learn how to set the allow policy of a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    import com.google.cloud.resourcemanager.v3.[ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html);
    import com.google.iam.admin.v1.[ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html);
    import com.google.iam.v1.[Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html);
    import com.google.iam.v1.[SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html);
    import com.google.protobuf.[FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html);
    import java.io.IOException;
    import java.util.Arrays;
    import java.util.List;
    
    public class SetProjectPolicy {
      public static void main(String[] args) throws IOException {
        // TODO(developer): Replace the variables before running the sample.
        // TODO: Replace with your project ID.
        String projectId = "your-project-id";
        // TODO: Replace with your policy, GetPolicy.getPolicy(projectId, serviceAccount).
        [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy = [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html).newBuilder().build();
    
        setProjectPolicy(policy, projectId);
      }
    
      // Sets a project's policy.
      public static [Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) setProjectPolicy([Policy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.Policy.html) policy, String projectId)
              throws IOException {
    
        // Initialize client that will be used to send requests.
        // This client only needs to be created once, and can be reused for multiple requests.
        try ([ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html) projectsClient = [ProjectsClient](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectsClient.html).create()) {
          List<String> paths = Arrays.asList("bindings", "etag");
          [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html) request = [SetIamPolicyRequest](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.html).newBuilder()
                  .setResource([ProjectName](https://docs.cloud.google.com/java/docs/reference/google-cloud-resourcemanager/latest/com.google.cloud.resourcemanager.v3.ProjectName.html).of(projectId).toString())
                  .[setPolicy](https://docs.cloud.google.com/java/docs/reference/proto-google-iam-v1/latest/com.google.iam.v1.SetIamPolicyRequest.Builder.html#com_google_iam_v1_SetIamPolicyRequest_Builder_setPolicy_com_google_iam_v1_Policy_)(policy)
                  // A FieldMask specifying which fields of the policy to modify. Only
                  // the fields in the mask will be modified. If no mask is provided, the
                  // following default mask is used:
                  // `paths: "bindings, etag"`
                  .setUpdateMask([FieldMask](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.html).newBuilder().[addAllPaths](https://docs.cloud.google.com/java/docs/reference/protobuf/latest/com.google.protobuf.FieldMask.Builder.html#com_google_protobuf_FieldMask_Builder_addAllPaths_java_lang_Iterable_java_lang_String__)(paths).build())
                  .build();
    
          return projectsClient.setIamPolicy(request);
        }
      }
    }

### Python

To authenticate to Resource Manager, set up Application Default Credentials. For more information, see Before you begin. 

To learn how to install and use the client library for Resource Manager, see [Resource Manager client libraries](https://docs.cloud.google.com/resource-manager/docs/libraries). 

The following example shows how to set the allow policy for a project. To learn how to set the allow policy of a folder or organization, review the [Resource Manager client library documentation](https://docs.cloud.google.com/resource-manager/docs/libraries) for your programming language. 
    
    
    from google.cloud import [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest)
    from google.iam.v1 import iam_policy_pb2, policy_pb2
    
    
    def set_project_policy(
        project_id: str, policy: policy_pb2.Policy, merge: bool = True
    ) -> policy_pb2.Policy:
        """
        Set policy for project. Pay attention that previous state will be completely rewritten.
        If you want to update only part of the policy follow the approach read->modify->write.
        For more details about policies check out https://cloud.google.com/iam/docs/policies
    
        project_id: ID or number of the Google Cloud project you want to use.
        policy: Policy which has to be set.
        merge: The strategy to be used forming the request. CopyFrom is clearing both mutable and immutable fields,
        when MergeFrom is replacing only immutable fields and extending mutable.
        https://googleapis.dev/python/protobuf/latest/google/protobuf/message.html#google.protobuf.message.Message.CopyFrom
        """
        client = [resourcemanager_v3](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest).[ProjectsClient](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html)()
    
        request = iam_policy_pb2.GetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
        current_policy = client.[get_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_get_iam_policy)(request)
    
        # Etag should as fresh as possible to lower chance of collisions
        policy.ClearField("etag")
        if merge:
            current_policy.MergeFrom(policy)
        else:
            current_policy.CopyFrom(policy)
    
        request = iam_policy_pb2.SetIamPolicyRequest()
        request.resource = f"projects/{project_id}"
    
        # request.etag field also will be merged which means you are secured from collision,
        # but it means that request may fail and you need to leverage exponential retries approach
        # to be sure policy has been updated.
        request.policy.CopyFrom(current_policy)
    
        policy = client.[set_iam_policy](https://docs.cloud.google.com/python/docs/reference/cloudresourcemanager/latest/google.cloud.resourcemanager_v3.services.projects.ProjectsClient.html#google_cloud_resourcemanager_v3_services_projects_ProjectsClient_set_iam_policy)(request)
        return policy
    
    

### REST

The Resource Manager API's `[set-iam-policy](https://docs.cloud.google.com/resource-manager/reference/rest/v1/projects/setIamPolicy)` method sets the policy in the request as the new allow policy for the project, folder, or organization. 

Before using any of the request data, make the following replacements: 

  * `API_VERSION`: The API version to use. For projects and organizations, use `v1`. For folders, use `v2`.
  * `RESOURCE_TYPE`: The resource type whose policy you want to manage. Use the value `projects`, `folders`, or `organizations`.
  * `RESOURCE_ID`: Your Google Cloud project, organization, or folder ID. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `POLICY`: A JSON representation of the policy that you want to set. For more information about the format of a policy, see the [Policy reference](https://docs.cloud.google.com/iam/docs/reference/rest/v1/Policy).




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

**Note:** If you grant access to a user's email alias or a secondary domain, then the values in your allow policy might not match the values that you initially entered. If you grant access to an email alias, then the allow policy displays the user's primary email address. If you grant access to a secondary domain, then the allow policy displays the primary domain. 

## What's next

  * Learn how to [manage access to service accounts](https://docs.cloud.google.com/iam/docs/manage-access-service-accounts).
  * Learn the general steps for [managing access to other resources](https://docs.cloud.google.com/iam/docs/manage-access-other-resources).
  * Find out how to [choose the most appropriate predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles). 
  * Use the [Policy Troubleshooter](https://docs.cloud.google.com/iam/docs/troubleshooting-access) to understand why a user does or doesn't have access to a resource or have permission to call an API. 
  * Discover how to [view the roles that you can grant on a particular resource](https://docs.cloud.google.com/iam/docs/viewing-grantable-roles).
  * Learn how to make a principal's access conditional with [conditional role bindings](https://docs.cloud.google.com/iam/docs/conditions-overview). 
  * Explore ways to secure your applications with [Identity-Aware Proxy](https://docs.cloud.google.com/iap/docs/concepts-overview). 



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
