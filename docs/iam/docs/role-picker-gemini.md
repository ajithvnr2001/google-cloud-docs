---
url: https://docs.cloud.google.com/iam/docs/role-picker-gemini/
title: Get predefined role suggestions with Gemini assistance \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:10:07.653212+00:00
---

# Get predefined role suggestions with Gemini assistance  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/role-picker-gemini/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Get predefined role suggestions with Gemini assistance Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how you can find and grant Identity and Access Management (IAM) predefined roles to your principals with Gemini assistance.

The IAM role picker lets you ask Gemini which roles you should grant to your principals. Typically, to find the right predefined roles to grant, you need to search through the [IAM roles and permissions index](https://docs.cloud.google.com/iam/docs/roles-permissions) or the [**Roles** page in the Google Cloud console](https://console.cloud.google.com/iam-admin/roles). With the IAM role picker, you can describe the actions you want the principal to perform and the resources that they need to perform them on. Based on your input, Gemini suggests the predefined roles that it considers appropriate.

Gemini can suggest predefined roles for individual principals. If Gemini suggests granting a role at the project level, then you can use the IAM role picker to grant that role.

You _can't_ use the IAM role picker to get suggestions for the following things:

  * Custom roles
  * Roles for multiple principals (with a single prompt)
  * Roles for Google Workspace products like Google Sheets and Google Docs

**Note:** Gemini can't suggest custom roles through the IAM role picker, but you can still get custom role suggestions from Gemini by using the Policy Assist API ([Preview](https://cloud.google.com/products#product-launch-stages)) or the Gemini Cloud Assist chat panel. For instructions, see [Use Gemini Cloud Assist in the Google Cloud console](https://docs.cloud.google.com/cloud-assist/chat-panel) in the Gemini Cloud Assist documentation.

Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

## Before you begin

Before you can get predefined role suggestions from Gemini, ensure you have completed the following prerequisites.

### Console

You can use the IAM role picker in the Google Cloud console without enabling any APIs.

### REST

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To get role suggestions with the [Policy Assist REST API](https://docs.cloud.google.com/policy-intelligence/docs/reference/policyassist/rest/v1/projects.locations.global/recommendIamRoles), you must enable the Policy Assist API on your project in the Google Cloud console:

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  3. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  4. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  5. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. Enable the Policy Assist API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable policyassist.googleapis.com

  8. [Install](https://docs.cloud.google.com/sdk/docs/install) the Google Cloud CLI. 

  9. If you're using an external identity provider (IdP), you must first [ sign in to the gcloud CLI with your federated identity](https://docs.cloud.google.com/iam/docs/workforce-log-in-gcloud). 

  10. To [initialize](https://docs.cloud.google.com/sdk/docs/initializing) the gcloud CLI, run the following command: 
         
         gcloud init

  11. [Create or select a Google Cloud project](https://cloud.google.com/resource-manager/docs/creating-managing-projects).

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.
     * Create a Google Cloud project:
           
           gcloud projects create PROJECT_ID

Replace `PROJECT_ID` with a name for the Google Cloud project you are creating.

     * Select the Google Cloud project that you created:
           
           gcloud config set project PROJECT_ID

Replace `PROJECT_ID` with your Google Cloud project name.

  12. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  13. Enable the Policy Assist API, if it is not already enabled: 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
         
         gcloud services enable policyassist.googleapis.com




### Required roles

To get the permissions that you need to use the IAM role picker, ask your administrator to grant you the following IAM roles on project: 

  * Get role suggestions in the console: [Project IAM Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/resourcemanager#resourcemanager.projectIamAdmin) (`roles/resourcemanager.projectIamAdmin`) 
  * Get custom role suggestions with the API: [IAM Viewer ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.viewer) (`roles/iam.viewer`) 



For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

These predefined roles contain the permissions required to use the IAM role picker. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to use the IAM role picker:

  * Get role suggestions in the console: 
    * `resourcemanager.projects.get`
    * `resourcemanager.projects.getIamPolicy`
    * `resourcemanager.projects.setIamPolicy`
  * Get custom role suggestions with the API: `iam.roles.list`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Get role suggestions with Gemini assistance

You can ask Gemini for role suggestions using the Google Cloud console or the Policy Assist REST API.

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

### Console

To get role suggestions from Gemini in the Google Cloud console, you can access the IAM role picker on pages that let you grant access at the project level. For example, the IAM role picker is available on the following pages in the Google Cloud console:

  * The **IAM** page
  * The **Service Accounts** page
  * The Google Cloud console **Dashboard** page



The following procedure uses the **IAM** page as the primary entry point.

  1. In the Google Cloud console, go to the **IAM** page.

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=project)

  2. Select a project.

  3. Select a principal to get role suggestions for:

     * To get role suggestions for a principal who already has other roles on the resource, find a row containing the principal, and then click edit **Edit principal** in that row.

To grant a role to a [service agent](https://docs.cloud.google.com/iam/docs/service-account-types#service-agents), select the **Include Google-provided role grants** checkbox to see its email address.

**Note:** You cannot edit inherited roles when managing access to a resource. To edit inherited roles, go to the resource where the role was granted.
     * To get role suggestions for a principal who doesn't have any existing roles on the resource, click person_add **Grant Access** , then enter a [principal identifier](https://docs.cloud.google.com/iam/docs/principal-identifiers)—for example, `my-user@example.com` or `//iam.googleapis.com/locations/global/workforcePools/example-pool/group/example-group@example.com`.

  4. To open the IAM role picker dialog, click **Help me choose roles**.

  5. In your own words, describe the action you want the principal to perform and the resource in the project that they need to perform it on.

  6. Click **Suggest roles**. Based on your input, Gemini suggests the predefined roles that it considers appropriate.

To get more information about the roles and why Gemini suggested them, click **Show reasoning**. We also recommend using the [roles and permissions reference](https://docs.cloud.google.com/iam/docs/roles-permissions) to validate Gemini's suggested roles before granting them to the principal.

  7. Optional: If Gemini doesn't suggest the right roles, you can refine your prompt.

     1. To modify your prompt, click **Edit**.
     2. Edit the description and then click **Update**. Gemini updates its role suggestions based on the new description.
  8. To accept the suggestions, click **Add roles**.

  9. Optional: Add a [condition](https://docs.cloud.google.com/iam/docs/conditions-overview) to the role.

  10. Click **Save**. The principal is granted the role on the resource.




You can grant _project-level_ roles suggested by Gemini directly from the IAM role picker. For organization-, folder-, or resource-level role suggestions, note the suggested roles and grant them to the principal at the appropriate level using the typical process in the Google Cloud console. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If you don't have the permissions to grant the roles at the organization, folder, or resource levels, contact your administrator.

### REST

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

To get role suggestions with the Policy Assist REST API, call the [`recommendIamRoles`](https://docs.cloud.google.com/policy-intelligence/docs/reference/policyassist/rest/v1/projects.locations.global/recommendIamRoles) method.

Before using any of the request data, make the following replacements: 

  * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric, like `my-project`.
  * `USER_INSTRUCTIONS`: The natural language prompt that describes the permissions you need. For example, "Suggest a role that lets me view storage buckets."



HTTP method and URL: 
    
    
    POST https://policyassist.googleapis.com/v1/projects/PROJECT_ID/locations/global:recommendIamRoles

Request JSON body: 
    
    
    {
      "prompt": {
        "userInstructions": "USER_INSTRUCTIONS"
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
         "https://policyassist.googleapis.com/v1/projects/PROJECT_ID/locations/global:recommendIamRoles"

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
        -Uri "https://policyassist.googleapis.com/v1/projects/PROJECT_ID/locations/global:recommendIamRoles" | Select-Object -Expand Content

You should receive a JSON response similar to the following:
    
    
    {
      "summary": "",
      "recommendations": [
        {
          "type": "RECOMMENDATION_TYPE_PREDEFINED_ROLES",
          "roles": [
            {
              "name": "roles/storage.objectViewer",
              "roleType": "ROLE_TYPE_PREDEFINED",
              "grantableScopes": [
                "Projects",
                "Buckets"
              ]
            },
            {
              "name": "roles/storage.legacyBucketReader",
              "roleType": "ROLE_TYPE_PREDEFINED",
              "grantableScopes": [
                "Projects"
              ]
            }
          ],
          "intro": "The following roles match your description:"
          "detailedReasoning": "The roles/storage.objectViewer role grants permissions to view objects and their metadata. The roles/storage.legacyBucketReader grants broader read access to buckets and objects. Choose the one that best fits the principle of least privilege for your use case."
        }
      ]
    }
    

To learn how to grant the suggested roles to the principal at the appropriate level, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). If you don't have the permissions to grant the roles, contact your administrator.

## Sample use cases

The following table illustrates some example use cases for the IAM role picker. By default, Gemini suggests roles that are designed to cover common user journeys within a service. For example, Gemini often suggests a service's Admin, Editor, or Viewer roles.

If you want Gemini to suggest the most granular, least privileged roles, you must specify this preference in your prompt using specific keywords. For a list of keywords you can use, see Keywords for least privileged roles. However, be aware that least privileged roles might not be sufficient for a user's future needs.

Use case | Prompt examples  
---|---  
Identifying roles for general service management | 

  * "What permissions do I need to manage our AlloyDB for PostgreSQL setup?"
  * "What roles do I need to work with BigQuery?"
  * "How do I give someone access to run and debug Cloud Run services?"
  * "I need to provision a Vertex AI Agent identity to execute basic tool calls."

  
Identifying the roles necessary to perform specific tasks | 

  * "What role is required to create, start, and stop VMs?"
  * "I need to allow a user to create and manage BigQuery datasets and tables."
  * "I need to grant a service account access to invoke Cloud Run functions."
  * "I want my agent to trigger a local MCP server that I have deployed on Cloud Run."

Prompts that yield least privileged role suggestions:

  * "What is the _minimal role_ required to create, start, and stop VMs?"
  * "What are the _least-privileged_ IAM roles required to create IAM policies?"
  * "I need to grant a service account access to invoke Cloud Run functions. What's the _narrowest access_ required?"
  * "What is the _least permissive_ role my agent needs to trigger a local MCP server I have deployed on Cloud Run?"

  
Identifying roles necessary to run Google Cloud CLI commands | 

  * "What IAM role is required to run: `gcloud compute instances create instance-1`?"

Prompt that yields least privileged role suggestions:

  * "What is the _smallest role_ a service account needs to execute: `gcloud datastore instances describe`?"

  
Identifying roles for a task that includes transitive dependencies | 

  * "I need to configure a Compute Engine instance to automatically scale based on CPU utilization. Which IAM roles should I grant to the service account?"

Prompt that yields least privileged role suggestions:

  * "I need to configure a Compute Engine instance to automatically scale based on CPU utilization. What are the _minimum permissions_ I need to grant to a service account used by a Compute Engine instance autoscaler?"

  
Identifying roles for a task that might require a combination of multiple granular roles | 

  * "Provide users access only to a particular dataset in BigQuery. They shouldn't be able to create or delete datasets."

Prompt that yields least privileged role suggestions:

  * "What is the _most secure role_ to give users read-only access to a single dataset in BigQuery, without allowing create or delete actions on any dataset?"

  
  
## Best practices

To help Gemini provide the most accurate suggestions for your use case, we recommend that you adhere to the following best practices when drafting your prompt.

  * **Clearly describe your use case.** Avoid using vague language in your prompts. Be as clear as possible about what actions you want the principal to perform on which services and resource types. If you want Gemini to suggest the least privileged roles, be sure to create your prompt with specific keywords that describe your intent to adhere to the principle of least privilege.

Do | Don't | Details  
---|---|---  
"What role is required to execute SQL queries on a BigQuery table and read the data from it?" | "What role is required to execute SQL statements?" | SQL is a generic language used across multiple Google Cloud services. Without specifying the service or actions, Gemini can't suggest a precise role.  
"I need roles to start, stop, and reboot Compute Engine virtual machine instances." | "I need to manage my virtual machines." | The term _manage_ is too vague. Manage could mean creating, deleting, updating, or viewing VMs. Clearly listing the specific actions to be performed (start, stop, reboot) and the exact resource type (Compute Engine virtual machine instances) yields more accurate suggestions.  
"I need to upload and download objects from a Cloud Storage bucket named `example-bucket`." | "Give me access to storage." | The term _Storage_ alone could refer to various services like Cloud Storage, Filestore, or Persistent Disk. In addition, there are no actions specified. Without specifying the service (Cloud Storage), the resource type name (`example-bucket`), or the actions (upload and download objects), Gemini doesn't have enough information to suggest the right roles.  
"I need the least permissive role that provides list-only access to Secret Manager." | "I need limited access to manage my secrets." | The phrase _limited access_ doesn't clearly define the required restrictions. _Manage my secrets_ covers a broad range of actions (create, list, update, delete, access versions). Without using explicit keywords like _least privilege_ , Gemini defaults to suggesting more general service-specific Admin, Editor, or Viewer roles.  
  * **Use official names.** Use the official names of Google Cloud services, resource types, and API operations in your prompt. If you are unsure about the official names of services, resource types, or API operations, we recommend consulting the official product documentation.

Do | Don't | Details  
---|---|---  
"What role do I need to update BigQuery datasets?" | "What role do I need to update Big query datasets? | _BigQuery_ is the official name of the product—not _Big query_.  
"What role is required to create a Cloud Storage bucket in my project?" | "What role is required to create a Storage bucket in my project?" | _Storage bucket_ could refer to different resource types from services like Cloud Storage, Filestore, or Persistent Disk. Specifying the product name and the associated resource type will yield more accurate suggestions.  



### Keywords for least privileged roles

If you need role suggestions from Gemini that adhere to the principle of least privilege, you must use specific keywords in your prompt. The following is a non-exhaustive list of keywords that you can use to request least privileged roles:

  * _least permissive_
  * _most secure_
  * _smallest role_
  * _least privileged_
  * _minimum permissions_
  * _strictly granular_
  * _narrowest access_
  * _only the absolute minimum_
  * _only with the exact permissions_



## Troubleshooting

This section describes resolutions for common issues with the IAM role picker.

### Gemini suggests roles that you can't grant at the project level

Gemini can suggest roles at all resource levels; however, you can only use the IAM role picker to grant the _project-level_ roles that are suggested. When Gemini suggests organization, folder, or resource-level roles, the IAM role picker indicates that there are suggested roles that can't be granted and the **Add roles** button will be disabled.

When this occurs, you can copy the suggested roles and grant them to the principal at the appropriate level using the typical process in the Google Cloud console. For more information on granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

If you don't have the permissions to grant the roles at the organization, folder, or resource levels, contact your administrator.

## What's next

  * Read [Gemini for Google Cloud overview](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Learn how to manually [find the right predefined roles](https://docs.cloud.google.com/iam/docs/choose-predefined-roles).
  * [Use the Policy Assist remote MCP server](https://docs.cloud.google.com/policy-intelligence/docs/use-policy-assist-mcp) to give external agents access to the IAM role picker.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
