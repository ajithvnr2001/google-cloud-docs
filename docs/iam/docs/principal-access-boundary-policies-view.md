---
url: https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-view/
title: View Principal Access Boundary policies \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:10.402216+00:00
---

# View Principal Access Boundary policies  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-view/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  View Principal Access Boundary policies Stay organized with collections  Save and categorize content based on your preferences. 

Principal Access Boundary (PAB) policies let you limit the resources that a set of principals are eligible to access. This page explains how to view Principal Access Boundary policies and policy bindings for Principal Access Boundary policies.

## Before you begin

  * Set up authentication.

Select the tab for how you plan to use the samples on this page:

### gcloud

In the Google Cloud console, activate Cloud Shell.

[Activate Cloud Shell](https://console.cloud.google.com/?cloudshell=true)

At the bottom of the Google Cloud console, a [Cloud Shell](https://docs.cloud.google.com/shell/docs/how-cloud-shell-works) session starts and displays a command-line prompt. Cloud Shell is a shell environment with the Google Cloud CLI already installed and with values already set for your current project. It can take a few seconds for the session to initialize. 

### REST

To use the REST API samples on this page in a local development environment, you use the credentials you provide to the gcloud CLI. 

[Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

For more information, see [Authenticate for using REST](https://docs.cloud.google.com/docs/authentication/rest) in the Google Cloud authentication documentation. 

  * Read the [overview of Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies).




### Roles required to view Principal Access Boundary policies

To get the permissions that you need to view Principal Access Boundary policies, ask your administrator to grant you the [Principal Access Boundary Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.principalAccessBoundaryViewer) (`roles/iam.principalAccessBoundaryViewer`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to view Principal Access Boundary policies. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view Principal Access Boundary policies:

  * View a single Principal Access Boundary policy: `iam.principalaccessboundarypolicies.get`
  * List Principal Access Boundary policies in an organization: `iam.principalaccessboundarypolicies.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Roles required to view policy bindings

To get the permissions that you need to view policy bindings, ask your administrator to grant you the following IAM roles on the policy bindings' [parent resource](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets): 

  * View policy bindings in a project: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * View policy bindings in a folder: [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderIamAdmin) (`roles/resourcemanager.folderIamAdmin`) 
  * View policy bindings in an organization: [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view policy bindings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view policy bindings:

  * View a single policy binding: `iam.policybindings.get`
  * List policy bindings in a project, folder, or organization: `iam.policybindings.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Roles required to view all policy bindings for a Principal Access Boundary policy

To get the permission that you need to view all policy bindings for a Principal Access Boundary policy, ask your administrator to grant you the [Principal Access Boundary Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.principalAccessBoundaryViewer) (`roles/iam.principalAccessBoundaryViewer`) IAM role on the organization. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `iam.principalaccessboundarypolicies.searchIamPolicyBindings` permission, which is required to view all policy bindings for a Principal Access Boundary policy. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

### Roles required to view policy bindings for a principal set

The permissions that you need in order to view all policy bindings for a principal set depend on the principal set that you want to view policies for.

To get the permissions that you need to view policy bindings, ask your administrator to grant you the following IAM roles: 

  * View policy bindings for Workforce Identity Federation pools: [IAM Workforce Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workforcePoolAdmin) (`roles/iam.workforcePoolAdmin`) on the target Workforce Identity Federation pool 
  * View policy bindings for Workload Identity Federation pools: [IAM Workload Identity Pool Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workloadIdentityPoolAdmin) (`roles/iam.workloadIdentityPoolAdmin`) on the project that owns the target Workload Identity Federation pool 
  * View policy bindings for a Google Workspace domain: [Workspace Pool IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.workspacePoolAdmin) (`roles/iam.workspacePoolAdmin`) on the organization 
  * View policy bindings for a project's principal set: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) on the project 
  * View policy bindings for a folder's principal set: [Folder IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.folderIamAdmin) (`roles/resourcemanager.folderIamAdmin`) on the folder 
  * View policy bindings for an organization's principal set: [Organization Administrator ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.organizationAdmin) (`roles/resourcemanager.organizationAdmin`) on the organization 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to view policy bindings. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to view policy bindings:

  * View policy bindings for Workforce Identity Federation pools: `iam.workforcePools.searchPolicyBindings` on the target Workforce Identity Federation pool 
  * View policy bindings for Workload Identity Federation pools: `iam.workloadIdentityPools.searchPolicyBindings` on the project that owns the target Workload Identity Federation pool 
  * View policy bindings for a Google Workspace domain: `iam.workspacePools.searchPolicyBindings` on the organization 
  * View policy bindings for a project's principal set: `resourcemanager.projects.searchPolicyBindings` on the project 
  * View policy bindings for a folder's principal set: `resourcemanager.folders.searchPolicyBindings` on the folder 
  * View policy bindings for an organization's principal set: `resourcemanager.organizations.searchPolicyBindings` on the organization 



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## List Principal Access Boundary policies for an organization

To view all Principal Access Boundary policies created in an organization, list the Principal Access Boundary policies in the organization.

You can list the Principal Access Boundary policies in an organization using the Google Cloud console, the gcloud CLI, or the IAM REST API.

### Console

  1. In the Google Cloud console, go to the **Principal Access Boundary policies** page.

[Go to Principal Access Boundary policies](https://console.cloud.google.com/iam-admin/principal-access-boundary)

  2. Select the organization that you want to view Principal Access Boundary policies for.




The Google Cloud console lists all policies in the organization that you select.

### gcloud

The `[gcloud iam principal-access-boundary-policies list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/list)` command lists all Principal Access Boundary policies in an organization. 

Before using any of the command data below, make the following replacements: 

  * `ORG_ID`: The ID of the Google Cloud organization that you want to list Principal Access Boundary policies for. Organization IDs are numeric, like `123456789012`. 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam principal-access-boundary-policies list --organization=ORG_ID \
        --location=global  --format=FORMAT

#### Windows (PowerShell)
    
    
    gcloud iam principal-access-boundary-policies list --organization=ORG_ID `
        --location=global  --format=FORMAT

#### Windows (cmd.exe)
    
    
    gcloud iam principal-access-boundary-policies list --organization=ORG_ID ^
        --location=global  --format=FORMAT

The response contains the Principal Access Boundary policies in the specified organization.
    
    
    {
      "principalAccessBoundaryPolicies": [
        {
          "createTime": "2026-07-07T00:05:48.295209Z",
          "details": {
            "enforcementVersion": "4",
            "rules": [
              {
                "description": "Make principals eligible to manage but not delete Compute resources in example.com",
                "effect": "ALLOW",
                "resources": [
                  "//cloudresourcemanager.googleapis.com/organizations/123456789012"
                ]
              }
            ]
          },
          "displayName": "Example policy 1",
          "etag": "W/\"Gh/PcTdJD/AWHUhPW45kdw==\"",
          "name": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-policy-1",
          "uid": "puid_13364150419245236225",
          "updateTime": "2026-07-07T00:05:48.295209Z"
        },
        {
          "createTime": "2026-05-29T23:25:01.606730Z",
          "details": {
            "enforcementVersion": "4",
            "rules": [
              {
                "description": "Make principals eligible to access resources in example-project",
                "effect": "ALLOW",
                "resources": [
                  "//cloudresourcemanager.googleapis.com/projects/example-project"
                ]
              }
            ]
          },
          "displayName": "Example policy 2",
          "etag": "d6BJBTsk2+oDCygmr5ANxA==",
          "name": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-policy-2",
          "uid": "puid_13064942519001808897",
          "updateTime": "2026-05-29T23:25:01.606730Z"
        }
      ]
    }
    

### REST

The `[principalAccessBoundaryPolicies.list](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/list)` method lists all Principal Access Boundary policies in an organization. 

Before using any of the request data, make the following replacements: 

  * `ORG_ID`: The ID of the Google Cloud organization that you want to list Principal Access Boundary policies for. Organization IDs are numeric, like `123456789012`. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies" | Select-Object -Expand Content

The response contains the Principal Access Boundary policies in the specified organization.
    
    
    {
      "principalAccessBoundaryPolicies": [
        {
          "name": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-policy-1",
          "uid": "puid_13364150419245236225",
          "etag": "W/\"Gh/PcTdJD/AWHUhPW45kdw==\"",
          "displayName": "Example policy 1",
          "createTime": "2026-07-07T00:05:48.295209Z",
          "updateTime": "2026-07-07T00:05:48.295209Z",
          "details": {
            "rules": [
              {
                "description": "Make principals eligible to access resources in example.com",
                "resources": [
                  "//cloudresourcemanager.googleapis.com/organizations/123456789012"
                ],
                "effect": "ALLOW"
              }
            ],
            "enforcementVersion": "4"
          }
        },
        {
          "name": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-policy-2",
          "uid": "puid_13064942519001808897",
          "etag": "d6BJBTsk2+oDCygmr5ANxA==",
          "displayName": "Example policy 2",
          "createTime": "2026-05-29T23:25:01.606730Z",
          "updateTime": "2026-05-29T23:25:01.606730Z",
          "details": {
            "rules": [
              {
                "description": "Make principals eligible to access resources in example-project",
                "resources": [
                  "//cloudresourcemanager.googleapis.com/projects/example-project"
                ],
                "effect": "ALLOW"
              }
            ],
            "enforcementVersion": "4"
          }
        }
      ]
    }
    

## Get a single Principal Access Boundary policy

To view the details of a single Principal Access Boundary policy, use the policy's ID to get the policy.

You can get a Principal Access Boundary policy using the Google Cloud console, the gcloud CLI, or the IAM REST API.

### Console

  1. In the Google Cloud console, go to the **Principal Access Boundary policies** page.

[Go to Principal Access Boundary policies](https://console.cloud.google.com/iam-admin/principal-access-boundary)

  2. Select the organization that you want to view Principal Access Boundary policies for.

  3. Click the policy ID of the Principal Access Boundary policy that you want to view.




The Google Cloud console shows the details of the Principal Access Boundary policy that you select.

### gcloud

The `[gcloud iam principal-access-boundary-policies describe](https://docs.cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/describe)` command gets a single Principal Access Boundary policy. 

Before using any of the command data below, make the following replacements: 

  * `PAB_POLICY_ID`: The ID of the Principal Access Boundary policy that you want to get—for example, `example-policy`. 
  * `ORG_ID`: The ID of the organization that owns the Principal Access Boundary policy. Organization IDs are numeric, like `123456789012`. 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam principal-access-boundary-policies describe PAB_POLICY_ID \
        --organization=ORG_ID --location=global \
        --format=FORMAT

#### Windows (PowerShell)
    
    
    gcloud iam principal-access-boundary-policies describe PAB_POLICY_ID `
        --organization=ORG_ID --location=global `
        --format=FORMAT

#### Windows (cmd.exe)
    
    
    gcloud iam principal-access-boundary-policies describe PAB_POLICY_ID ^
        --organization=ORG_ID --location=global ^
        --format=FORMAT

The response contains the Principal Access Boundary policy specified in the request.
    
    
    {
      "createTime": "2026-07-07T00:05:48.295209Z",
      "details": {
        "enforcementVersion": "4",
        "rules": [
          {
            "description": "Make principals eligible to access resources in example.com",
            "effect": "ALLOW",
            "resources": [
              "//cloudresourcemanager.googleapis.com/organizations/123456789012"
            ]
          }
        ]
      },
      "displayName": "Example policy",
      "etag": "W/\"Gh/PcTdJD/AWHUhPW45kdw==\"",
      "name": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-policy",
      "uid": "puid_13364150419245236225",
      "updateTime": "2026-07-07T00:05:48.295209Z"
    }
    

### REST

The `[principalAccessBoundaryPolicies.get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/get)` method gets a single Principal Access Boundary policy. 

Before using any of the request data, make the following replacements: 

  * `ORG_ID`: The ID of the organization that owns the Principal Access Boundary policy. Organization IDs are numeric, like `123456789012`. 
  * `PAB_POLICY_ID`: The ID of the Principal Access Boundary policy that you want to get—for example, `example-policy`. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies/PAB_POLICY_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies/PAB_POLICY_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies/PAB_POLICY_ID" | Select-Object -Expand Content

The response contains the Principal Access Boundary policy specified in the request.
    
    
    {
      "name": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-policy",
      "uid": "puid_13364150419245236225",
      "etag": "W/\"Gh/PcTdJD/AWHUhPW45kdw==\"",
      "displayName": "Example policy",
      "createTime": "2026-07-07T00:05:48.295209Z",
      "updateTime": "2026-07-07T00:05:48.295209Z",
      "details": {
        "rules": [
          {
            "description": "Make principals eligible to access resources in example.com",
            "resources": [
              "//cloudresourcemanager.googleapis.com/organizations/123456789012"
            ],
            "effect": "ALLOW"
          }
        ],
        "enforcementVersion": "4"
      }
    }
    

## List policy bindings for Principal Access Boundary policies

There are several ways that you can list policy bindings for Principal Access Boundary policies:

  * List policy bindings for a Principal Access Boundary policy
  * List policy bindings for a principal set
  * List policy bindings for a project, folder, or organization



### List policy bindings for a Principal Access Boundary policy

To view all policy bindings that include a certain Principal Access Boundary policy, search the bindings for the Principal Access Boundary policy.

You can view all policy bindings for a Principal Access Boundary policy using the Google Cloud console, the gcloud CLI, or the IAM REST API.

### Console

  1. In the Google Cloud console, go to the **Principal Access Boundary policies** page.

[Go to Principal Access Boundary policies](https://console.cloud.google.com/iam-admin/principal-access-boundary)

  2. Select the organization that owns the Principal Access Boundary policy that you want to view bindings for.

  3. Click the policy ID of the Principal Access Boundary policy that you want to view bindings for.

  4. Click the **Bindings** tab.




The **Bindings** tab lists all Principal Access Boundary policy bindings that include the Principal Access Boundary policy.

### gcloud

The `[gcloud iam principal-access-boundary-policies search-policy-bindings](https://docs.cloud.google.com/sdk/gcloud/reference/iam/principal-access-boundary-policies/search-policy-bindings)` command lists all policy bindings for the specified Principal Access Boundary policy. 

Before using any of the command data below, make the following replacements: 

  * `PAB_POLICY_ID`: The ID of the Principal Access Boundary policy that you want to list policy bindings for—for example, `example-policy`. 
  * `ORG_ID`: The ID of the organization that owns the Principal Access Boundary policy. Organization IDs are numeric, like `123456789012`. 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam principal-access-boundary-policies search-policy-bindings PAB_POLICY_ID \
        --organization=ORG_ID --location=global \
        --format=FORMAT

#### Windows (PowerShell)
    
    
    gcloud iam principal-access-boundary-policies search-policy-bindings PAB_POLICY_ID `
        --organization=ORG_ID --location=global `
        --format=FORMAT

#### Windows (cmd.exe)
    
    
    gcloud iam principal-access-boundary-policies search-policy-bindings PAB_POLICY_ID ^
        --organization=ORG_ID --location=global ^
        --format=FORMAT

The response contains the policy bindings for the specified Principal Access Boundary policy.
    
    
    {
      "policyBindings": [
        {
          "createTime": "2024-05-06T18:08:24.729843Z",
          "displayName": "Example binding 1",
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding1",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_9519202237377675265",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "uid": "buid_9904260005517852673", 
          "updateTime": "2024-05-06T18:08:24.729843Z"
        },
        {
          "createTime": "2024-05-07T07:05:06.203861Z",
          "displayName": "Example binding 2",
          "etag": "W/\"cRMdDXbT82aLuZlvoL9Gqg==\"",
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding2",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_9519202237377675265",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/projects/example-project"
          },
          "uid": "buid_4331055466646863873", 
          "updateTime": "2024-05-07T07:05:06.203861Z"
        }
      ]
    }
    

### REST

The `[principalAccessBoundaryPolicies.searchPolicyBindings](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.principalAccessBoundaryPolicies/searchPolicyBindings)` method lists all policy bindings for the specified Principal Access Boundary policy. 

Before using any of the request data, make the following replacements: 

  * `ORG_ID`: The ID of the organization that owns the Principal Access Boundary policy. Organization IDs are numeric, like `123456789012`. 
  * `PAB_POLICY_ID`: The ID of the Principal Access Boundary policy that you want to list policy bindings for—for example, `example-policy`. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies/PAB_POLICY_ID:searchPolicyBindings

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies/PAB_POLICY_ID:searchPolicyBindings"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v3/organizations/ORG_ID/locations/global/principalAccessBoundaryPolicies/PAB_POLICY_ID:searchPolicyBindings" | Select-Object -Expand Content

The response contains the policy bindings for the specified Principal Access Boundary policy.
    
    
    {
      "policyBindings": [
        {
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding1",
          "uid": "buid_9904260005517852673", 
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "displayName": "Example binding 1",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy",
          "policyUid": "puid_9519202237377675265",
          "createTime": "2024-05-06T18:08:24.729843Z",
          "updateTime": "2024-05-06T18:08:24.729843Z"
        },
        {
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding2",
          "uid": "buid_4331055466646863873", 
          "etag": "W/\"cRMdDXbT82aLuZlvoL9Gqg==\"",
          "displayName": "Example binding 2",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/projects/example-project"
          },
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy",
          "policyUid": "puid_9519202237377675265",
          "createTime": "2024-05-07T07:05:06.203861Z",
          "updateTime": "2024-05-07T07:05:06.203861Z"
        }
      ]
    }
    

### List policy bindings for a principal set

To view all policy bindings that include a certain principal set, search the bindings for the principal set.

These bindings contain the IDs of the Principal Access Boundary policies that are bound to the principal set. To see the details of these policies, use the policy ID to get the Principal Access Boundary policy.

You can view all policy bindings for a principal set using the gcloud CLI or the IAM REST API.

### gcloud

The `[gcloud iam policy-bindings search-target-policy-bindings](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/search-target-policy-bindings)` command gets all Principal Access Boundary policy bindings for a principal set. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the Resource Manager resource (project, folder, or organization) that the target principal set is a child of. Use the value `project`, `folder`, or `organization`.

The resource type depends on the type of principal set you want to list the policy bindings of. To see which resource type to use, see [Supported principal sets](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 

  * `RESOURCE_ID`: The ID of the project, folder, or organization that the target principal set is a child of. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `PRINCIPAL_SET`: The principal set whose Principal Access Boundary policy bindings you want to view. For a list of valid principal types, see [Supported principal sets](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam policy-bindings search-target-policy-bindings \
        --RESOURCE_TYPE=RESOURCE_ID \
        --target=PRINCIPAL_SET \
        --format=FORMAT

#### Windows (PowerShell)
    
    
    gcloud iam policy-bindings search-target-policy-bindings `
        --RESOURCE_TYPE=RESOURCE_ID `
        --target=PRINCIPAL_SET `
        --format=FORMAT

#### Windows (cmd.exe)
    
    
    gcloud iam policy-bindings search-target-policy-bindings ^
        --RESOURCE_TYPE=RESOURCE_ID ^
        --target=PRINCIPAL_SET ^
        --format=FORMAT

The response contains all policy bindings that include the target principal set.
    
    
    {
      "policyBindings": [
        {
          "createTime": "2024-05-06T18:08:24.729843Z",
          "displayName": "Example binding 1",
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding1",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy1",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_9519202237377675265",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "uid": "buid_9904260005517852673", 
          "updateTime": "2024-05-06T18:11:16.798841Z"
        },
        {
          "createTime": "2024-05-06T18:08:24.729843Z",
          "displayName": "Example binding 2",
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding2",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy2",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_10358560617928851457",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "uid": "buid_4331055466646863873", 
          "updateTime": "2024-05-06T18:11:16.798841Z"
        }
      ]
    }
    

### REST

The `[SearchTargetPolicyBindings.search](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/searchTargetPolicyBindings)` method gets all Principal Access Boundary policy bindings for a principal set. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the Resource Manager resource (project, folder, or organization) that the target principal set is a child of. Use the value `projects`, `folders`, or `organizations`.

The resource type depends on the type of principal set you want to list the policy bindings of. To see which resource type to use, see [Supported principal sets](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 

  * `RESOURCE_ID`: The ID of the project, folder, or organization that the target principal set is a child of. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `PRINCIPAL_SET`: The principal set whose Principal Access Boundary policy bindings you want to view. For a list of valid principal types, see [Supported principal sets](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 




HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings:searchTargetPolicyBindings?target=PRINCIPAL_SET

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings:searchTargetPolicyBindings?target=PRINCIPAL_SET"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings:searchTargetPolicyBindings?target=PRINCIPAL_SET" | Select-Object -Expand Content

The response contains all policy bindings that include the target principal set.
    
    
    {
      "policyBindings": [
        {
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding1",
          "uid": "buid_9904260005517852673", 
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "displayName": "Example binding 1",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy1",
          "createTime": "2024-05-06T18:08:24.729843Z",
          "updateTime": "2024-05-06T18:11:16.798841Z",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_9519202237377675265"
        },
        {
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding2",
          "uid": "buid_4331055466646863873", 
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "displayName": "Example binding 2",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy2",
          "createTime": "2024-05-06T18:08:24.729843Z",
          "updateTime": "2024-05-06T18:11:16.798841Z",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_10358560617928851457"
        }
      ]
    }
    

### List policy bindings for a project, folder, or organization

To view all policy bindings that are children of a specific project, folder, or organization, list the policy bindings for that project, folder, or organization.

A policy binding's parent resource depends on the principal set in the policy binding. To learn more, see [Supported principal types](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets).

You can view all policy bindings for a project, folder, or organization using the gcloud CLI or the IAM REST API.

### gcloud

The `[gcloud iam policy-bindings list](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/list)` command lists all policy bindings that are children of a certain resource. 

Before using any of the command data below, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the Resource Manager resource (project, folder, or organization) that the policy binding is a child of. Use the value `project`, `folder`, or `organization`

The resource type depends on the principal set in the policy binding. To see which resource type to use, see [Supported principal types](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 

  * `RESOURCE_ID`: The ID of the project, folder, or organization that the policy binding is a child of. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam policy-bindings list --RESOURCE_TYPE=RESOURCE_ID \
        --location=global \
        --filter=policyKind:PRINCIPAL_ACCESS_BOUNDARY \
        --format=FORMAT

#### Windows (PowerShell)
    
    
    gcloud iam policy-bindings list --RESOURCE_TYPE=RESOURCE_ID `
        --location=global `
        --filter=policyKind:PRINCIPAL_ACCESS_BOUNDARY `
        --format=FORMAT

#### Windows (cmd.exe)
    
    
    gcloud iam policy-bindings list --RESOURCE_TYPE=RESOURCE_ID ^
        --location=global ^
        --filter=policyKind:PRINCIPAL_ACCESS_BOUNDARY ^
        --format=FORMAT

The response contains the policy bindings that are children of the resource in the command.
    
    
    {
      "policyBindings": [
        {
          "createTime": "2024-05-06T18:08:24.729843Z",
          "displayName": "Example binding 1",
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding-1",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy-1",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_9519202237377675265",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "uid": "buid_9904260005517852673", 
          "updateTime": "2024-05-06T18:08:24.729843Z"
        },
        {
          "createTime": "2024-05-07T07:05:06.203861Z",
          "displayName": "Example binding 2",
          "etag": "W/\"cRMdDXbT82aLuZlvoL9Gqg==\"",
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding-2",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy-2",
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policyUid": "puid_1566408245394800641",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "uid": "buid_4331055466646863873", 
          "updateTime": "2024-05-07T07:05:06.203861Z"
        }
      ]
    }
    

### REST

The `[policyBindings.list](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/list)` method lists all policy bindings that are children of a certain resource. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the Resource Manager resource (project, folder, or organization) that the policy binding is a child of. Use the value `projects`, `folders`, or `organizations`

The resource type depends on the principal set in the policy binding. To see which resource type to use, see [Supported principal types](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 

  * `RESOURCE_ID`: The ID of the project, folder, or organization that the policy binding is a child of. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings?filter=policyKind:PRINCIPAL_ACCESS_BOUNDARY

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings?filter=policyKind:PRINCIPAL_ACCESS_BOUNDARY"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings?filter=policyKind:PRINCIPAL_ACCESS_BOUNDARY" | Select-Object -Expand Content

The response contains the policy bindings that are children of the resource in the request.
    
    
    {
      "policyBindings": [
        {
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding-1",
          "uid": "buid_9904260005517852673", 
          "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
          "displayName": "Example binding 1",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy-1",
          "policyUid": "puid_9519202237377675265",
          "createTime": "2024-05-06T18:08:24.729843Z",
          "updateTime": "2024-05-06T18:08:24.729843Z"
        },
        {
          "name": "organizations/123456789012/locations/global/policyBindings/example-binding-2",
          "uid": "buid_4331055466646863873", 
          "etag": "W/\"cRMdDXbT82aLuZlvoL9Gqg==\"",
          "displayName": "Example binding 2",
          "target": {
            "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
          },
          "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
          "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy-2",
          "policyUid": "puid_1566408245394800641",
          "createTime": "2024-05-07T07:05:06.203861Z",
          "updateTime": "2024-05-07T07:05:06.203861Z"
        }
      ]
    }
    

## Get a policy binding for a Principal Access Boundary policy

To view the details of a single policy binding, use the policy binding's ID to get the policy binding.

You can get a policy binding using the gcloud CLI or the IAM REST API.

### gcloud

The `[gcloud iam policy-bindings describe](https://docs.cloud.google.com/sdk/gcloud/reference/iam/policy-bindings/describe)` command gets a policy binding. 

Before using any of the command data below, make the following replacements: 

  * `BINDING_ID`: The ID of the policy binding that you want to get—for example, `example-binding`. 
  * `RESOURCE_TYPE`: The type of the Resource Manager resource (project, folder, or organization) that the policy binding is a child of. Use the value `project`, `folder`, or `organization`

The resource type depends on the principal set in the policy binding. To see which resource type to use, see [Supported principal types](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 

  * `RESOURCE_ID`: The ID of the project, folder, or organization that the policy binding is a child of. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `FORMAT`: The format for the response. Use `json` or `yaml`. 



Execute the following command: 

#### Linux, macOS, or Cloud Shell
    
    
    gcloud iam policy-bindings describe BINDING_ID \
        --RESOURCE_TYPE=RESOURCE_ID --location=global \
        --format=FORMAT

#### Windows (PowerShell)
    
    
    gcloud iam policy-bindings describe BINDING_ID `
        --RESOURCE_TYPE=RESOURCE_ID --location=global `
        --format=FORMAT

#### Windows (cmd.exe)
    
    
    gcloud iam policy-bindings describe BINDING_ID ^
        --RESOURCE_TYPE=RESOURCE_ID --location=global ^
        --format=FORMAT

The response contains the policy binding.
    
    
    {
      "createTime": "2024-05-06T18:08:24.729843Z",
      "displayName": "Example binding",
      "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
      "name": "organizations/123456789012/locations/global/policyBindings/example-binding",
      "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy",
      "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
      "policyUid": "puid_9519202237377675265",
      "target": {
        "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
      },
      "uid": "buid_9904260005517852673", 
      "updateTime": "2024-05-06T18:08:24.729843Z"
    }
    

### REST

The `[policyBindings.get](https://docs.cloud.google.com/iam/docs/reference/rest/v3/organizations.locations.policyBindings/get)` method gets a policy binding. 

Before using any of the request data, make the following replacements: 

  * `RESOURCE_TYPE`: The type of the Resource Manager resource (project, folder, or organization) that the policy binding is a child of. Use the value `projects`, `folders`, or `organizations`

The resource type depends on the principal set in the policy binding. To see which resource type to use, see [Supported principal types](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies#principal-sets). 

  * `RESOURCE_ID`: The ID of the project, folder, or organization that the policy binding is a child of. Project IDs are alphanumeric strings, like `my-project`. Folder and organization IDs are numeric, like `123456789012`. 
  * `BINDING_ID`: The ID of the policy binding that you want to get—for example, `example-binding`. 



HTTP method and URL: 
    
    
    GET https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings/BINDING_ID

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    curl -X GET \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         "https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings/BINDING_ID"

#### PowerShell (Windows)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Execute the following command: 
    
    
    $cred = gcloud auth print-access-token  
    $headers = @{ "Authorization" = "Bearer $cred" }  
      
    Invoke-WebRequest `  
        -Method GET `  
        -Headers $headers `  
        -Uri "https://iam.googleapis.com/v3/RESOURCE_TYPE/RESOURCE_ID/locations/global/policyBindings/BINDING_ID" | Select-Object -Expand Content

The response contains the policy binding.
    
    
    {
      "name": "organizations/123456789012/locations/global/policyBindings/example-binding",
      "uid": "buid_9904260005517852673", 
      "etag": "W/\"xkdnPfTxoxyVqOwhQSJbMg==\"",
      "displayName": "Example binding",
      "target": {
        "principalSet": "//cloudresourcemanager.googleapis.com/organizations/123456789012"
      },
      "policyKind": "PRINCIPAL_ACCESS_BOUNDARY",
      "policy": "organizations/123456789012/locations/global/principalAccessBoundaryPolicies/example-pab-policy",
      "policyUid": "puid_9519202237377675265",
      "createTime": "2024-05-06T18:08:24.729843Z",
      "updateTime": "2024-05-06T18:08:24.729843Z"
    }
    

## What's next

  * [Create and apply Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-create)
  * [Edit Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-edit)
  * [Remove Principal Access Boundary policies](https://docs.cloud.google.com/iam/docs/principal-access-boundary-policies-remove)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
