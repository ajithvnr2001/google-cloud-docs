---
url: https://docs.cloud.google.com/iam/docs/attach-service-accounts/
title: Attach service accounts to resources \u00a0|\u00a0 Identity and Access Management (IAM) \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:28:23.743366+00:00
---

# Attach service accounts to resources  |  Identity and Access Management (IAM)  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/iam/docs/attach-service-accounts/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ IAM ](https://docs.cloud.google.com/iam/docs)
  * [ Guides ](https://docs.cloud.google.com/iam/docs/overview)



Send feedback 

#  Attach service accounts to resources Stay organized with collections  Save and categorize content based on your preferences. 

For some Google Cloud resources, you can specify a user-managed service account that the resource uses as its default identity. This process is known as _attaching_ the service account to the resource, or _associating_ the service account with the resource. When code running on the resource accesses Google Cloud services and resources, it uses the service account attached to the resource as its identity. For example, if you [attach a service account to a Compute Engine instance](https://docs.cloud.google.com/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance), and the applications on the instance use a [client library](https://docs.cloud.google.com/apis/docs/client-libraries-explained) to call Google Cloud APIs, those applications automatically use the attached service account for authentication and authorization. 

This page describes how to configure service accounts so that you can attach them to resources.

## Before you begin

  * Enable the IAM and Resource Manager APIs, if any are not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the APIs](https://console.cloud.google.com/apis/enableflow?apiid=iam.googleapis.com,cloudresourcemanager.googleapis.com&redirect=https%3A//console.cloud.google.com)

  * Make sure you understand [how service accounts work](https://docs.cloud.google.com/iam/docs/service-accounts) in IAM.




### Required roles

To get the permission that you need to attach a service account to a resource, ask your administrator to grant you the [Service Account User ](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) IAM role on the service account. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the `iam.serviceAccounts.actAs` permission, which is required to attach a service account to a resource. 

You might also be able to get this permission with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Configure your organization policies

Depending on the location of the service account that you want to attach to the resource, you might need to update your project's [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) before attaching the service account:

  * If the service account is in the same project as the resource that you want to attach it to, then you don't need to update your project's organization policies.

  * If the service account is in a different project than the resource that you want to attach it to, then you need to update the organization policies for the project containing the service account. For details, see Enable service accounts to be attached across projects on this page.

This might be the case if, for example, you [create all of your service accounts in a single project](https://docs.cloud.google.com/iam/docs/service-account-overview#locations).




## Configure the service account

Before you attach a service account to a resource, you must configure the service account. This process differs depending on whether the service account and the resource are in the same project or in different projects. After you configure the service account, you can create the resource and attach the service account to that resource.

### Configure for a resource in the same project

Before you attach a service account to another resource in the same project, [grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access) to the service account so it can access the appropriate resources, just as you would grant roles to any other principal.

### Configure for a resource in a different project

In some cases, you might need to attach a service account to a resource that is located in a different project. For example, if you [create all of your service accounts in a single project](https://docs.cloud.google.com/iam/docs/service-account-overview#locations), you might need to attach one of them to a new resource in a different project.

Before you attach a service account to a resource in another project, do the following:

  1. In the project where the service account is located, follow the steps on this page to enable service accounts to be attached across projects.
  2. Identify the project where you will create the resource.
  3. Identify the type of resource that you will attach the service account to, as well as the service that owns that type of resource.

For example, if you are creating a Pub/Sub subscription, then Pub/Sub is the service that owns the resource.

  4. Find the email address of the service agent for the service.

Different services use different service agents. For details, see [Service agents](https://docs.cloud.google.com/iam/docs/service-agents).

**Note:** Some services, including Dataflow, Managed Service for Apache Spark, and Google Kubernetes Engine, can create Compute Engine instances or depend on Compute Engine in another way. For these services, you must find the email addresses for multiple service agents: one for Compute Engine, and another for the service that deploys the instances.
  5. Grant the Service Account Token Creator role (`roles/iam.serviceAccountTokenCreator`) to the service agents:

### Console

     1. In the Google Cloud console, go to the **Service accounts** page.

[Go to Service accounts](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts)

     2. Select the project that owns the service account that you will attach to a resource.

     3. Click the email address of the service account that you will attach to a resource.

     4. Go to the **Principals with access** tab.

     5. Click person_add **Grant access** , and then enter the email address of the service agent.

     6. Click **Select a role** , type `Service Account Token Creator`, and click the role.

     7. Click **Save** to save your changes.

     8. Optional: If you need to grant the role to another service agent, repeat the previous steps.

### gcloud

Use the [`gcloud iam service-accounts add-iam-policy-binding`](https://docs.cloud.google.com/sdk/gcloud/reference/iam/service-accounts/add-iam-policy-binding) command:
    
    gcloud iam service-accounts add-iam-policy-binding \
        SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com \
        --member=serviceAccount:SERVICE_AGENT_EMAIL \
        --role=roles/iam.serviceAccountTokenCreator

Replace the following values:

     * `SERVICE_ACCOUNT_NAME`: The name of the user-managed service account that you are attaching to a resource.
     * `PROJECT_ID`: The project ID where the user-managed service account is located.
     * `SERVICE_AGENT_EMAIL`: The email address for the service agent.

The command prints the updated allow policy for the user-managed service account.

Optional: If you need to grant the role to another service agent, run the command again.

### REST

To grant this role, use the read-modify-write pattern to update the allow policy for your user-managed service account.

**First, read the allow policy for the user-managed service account:**

The `[projects.serviceAccounts.getIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy)` method returns the allow policy for the service account. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
     * `USER_SA_NAME`: The name of the user-managed service account that you are binding to a resource. 

HTTP method and URL: 
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/USER_SA_NAME@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy

Request JSON body: 
    
    {
      "requestedPolicyVersion": 3
    }
    

To send your request, expand one of these options:

#### curl (Linux, macOS, or Cloud Shell)

**Note:** The following command assumes that you have logged in to the `gcloud` CLI with your user account by running [`gcloud init`](https://docs.cloud.google.com/sdk/gcloud/reference/init) or [`gcloud auth login`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/login) , or by using [Cloud Shell](https://docs.cloud.google.com/shell/docs), which automatically logs you into the `gcloud` CLI . You can check the currently active account by running [`gcloud auth list`](https://docs.cloud.google.com/sdk/gcloud/reference/auth/list). 

Save the request body in a file named `request.json`, and execute the following command: 
    
    curl -X POST \  
         -H "Authorization: Bearer $(gcloud auth print-access-token)" \  
         -H "Content-Type: application/json; charset=utf-8" \  
         -d @request.json \  
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/USER_SA_NAME@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/USER_SA_NAME@PROJECT_ID.iam.gserviceaccount.com:getIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/getIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    {
      "version": 1,
      "etag": "BwWl3KCTUMY=",
      "bindings": [
        {
          "role": "roles/iam.serviceAccountUser",
          "members": [
            "serviceAccount:my-service-account@my-project.iam.gserviceaccount.com"
          ]
        }
      ]
    }
    

**Next, modify the allow policy to grant the Service Account Token Creator role to the service agent.**
    
    {
      "version": 1,
      "etag": "BwWl3KCTUMY=",
      "bindings": [
        **{
          "role": "roles/iam.serviceAccountTokenCreator",
          "members": [
            "serviceAccount:SERVICE_AGENT_EMAIL"
          ]
        },**
        {
          "role": "roles/iam.serviceAccountUser",
          "members": [
            "serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"
          ]
        }
      ]
    }

Replace the following:

     * `SERVICE_AGENT_EMAIL`: The email address for the service agent
     * `SERVICE_ACCOUNT_NAME`: The name of the user-managed service account.
     * `PROJECT_ID`: The project ID where the user-managed service account is located.
**Note:** If you need to grant the role to more than one service agent, add all of the service accounts to the `members` array.

**Finally, write the updated allow policy:**

The `[projects.serviceAccounts.setIamPolicy](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy)` method updates the allow policy for your service account. 

Before using any of the request data, make the following replacements: 

     * `PROJECT_ID`: Your Google Cloud project ID. Project IDs are alphanumeric strings, like `my-project`.
     * `USER_SERVICE_ACCOUNT_NAME`: The name of the user-managed service account that you are binding to a resource. 
     * `SERVICE_AGENT_EMAIL`: The email address of the service agent that will create access tokens for your user-managed service account. 

HTTP method and URL: 
    
    POST https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy

Request JSON body: 
    
    {
      "policy": {
        "version": 1,
        "etag": "BwWl3KCTUMY=",
        "bindings": [
          {
            "role": "roles/iam.serviceAccountTokenCreator",
            "members": [
              "serviceAccount:SERVICE_AGENT_EMAIL"
            ]
          },
          {
            "role": "roles/iam.serviceAccountUser",
            "members": [
              "serviceAccount:SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com"
            ]
          }
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
         "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy"

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
        -Uri "https://iam.googleapis.com/v1/projects/PROJECT_ID/serviceAccounts/SERVICE_ACCOUNT_NAME@PROJECT_ID.iam.gserviceaccount.com:setIamPolicy" | Select-Object -Expand Content

#### APIs Explorer (browser)

Copy the request body and open the [method reference page](https://docs.cloud.google.com/iam/docs/reference/rest/v1/projects.serviceAccounts/setIamPolicy). The APIs Explorer panel opens on the right side of the page. You can interact with this tool to send requests. Paste the request body in this tool, complete any other required fields, and click **Execute**. 

You should receive a JSON response similar to the following:
    
    {
      "version": 1,
      "etag": "BwWo331TkHE=",
      "bindings": [
        {
          "role": "roles/iam.serviceAccountTokenCreator",
          "members": [
            "serviceAccount:SERVICE_AGENT_EMAIL"
          ]
        },
        {
          "role": "roles/iam.serviceAccountUser",
          "members": [
            "serviceAccount:my-service-account@my-project.iam.gserviceaccount.com"
          ]
        }
      ]
    }
    




## Attach the service account to a resource

After you configure the user-managed service account, you can create a new resource and attach the service account to that resource. Make sure you create the new resource in the appropriate project.

In most cases, you must attach a service account to a resource when you create that resource. After the resource is created, you cannot change which service account is attached to the resource. Compute Engine instances are an exception to this rule; you can [change which service account is attached to an instance](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#changeserviceaccountandscopes) as needed.

See the instructions for the type of resource that you want to create:

Attaching a service account when creating a resource  
---  
AI Platform Prediction |  [Model versions](https://docs.cloud.google.com/ai-platform/prediction/docs/custom-service-account)  
AI Platform Training |  [Jobs](https://docs.cloud.google.com/ai-platform/training/docs/custom-service-account)  
App Engine standard environment |  [App versions](https://docs.cloud.google.com/appengine/docs/standard/python3/user-managed-service-accounts)  
App Engine flexible environment |  [App versions](https://docs.cloud.google.com/appengine/docs/flexible/python/user-managed-service-accounts)  
Managed Service for Apache Airflow |  [Environments](https://docs.cloud.google.com/composer/docs/how-to/managing/creating)  
Cloud Run functions |  [Cloud Run function](https://docs.cloud.google.com/functions/docs/securing/function-identity)  
Cloud Run |  [Services](https://docs.cloud.google.com/run/docs/securing/service-identity)  
Cloud Scheduler |  [Jobs](https://docs.cloud.google.com/sdk/gcloud/reference/scheduler/jobs/create/http)  
Cloud Source Repositories | 

  * [Project configs](https://docs.cloud.google.com/sdk/gcloud/reference/source/project-configs/update)
  * Pub/Sub configuration for [repos](https://docs.cloud.google.com/source-repositories/docs/reference/rest/v1/projects.repos)

  
Compute Engine | 

  * [Instances](https://docs.cloud.google.com/compute/docs/access/create-enable-service-accounts-for-instances#using)
  * [Instance templates](https://docs.cloud.google.com/compute/docs/instance-templates/create-instance-templates)

  
Managed Service for Apache Spark |  [Clusters](https://docs.cloud.google.com/dataproc/docs/concepts/configuring-clusters/service-accounts#using_service_accounts)  
Google Kubernetes Engine | 

  * [Clusters](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#authentication_and_authorization)
  * [Node pools](https://docs.cloud.google.com/kubernetes-engine/docs/concepts/security-overview#authentication_and_authorization)

  
Notebooks |  [Notebook instances](https://docs.cloud.google.com/sdk/gcloud/reference/beta/notebooks/instances/create)  
Pub/Sub |  [Subscriptions](https://docs.cloud.google.com/sdk/gcloud/reference/pubsub/subscriptions/create)  
  
After you have created the resource and attached the service account to that resource, you can grant roles to the service account so it can access the appropriate resources. This process is the same as granting a role to any other principal.

To learn how to grant roles, see [Granting, changing, and revoking access to resources](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).

## Enable service accounts to be attached across projects

If you want to let users attach service accounts in one project to resources in another project, you must update the [organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/overview) for the project that contains the service accounts. Check the following [boolean constraints](https://docs.cloud.google.com/resource-manager/docs/organization-policy/understanding-constraints#boolean_constraint) in the organization policies for that project:

**Important:** After you update your organization policies, we strongly discourage you from undoing the changes, especially in production environments. If you undo the changes, your Google Cloud resources might not work correctly.

  * Ensure that the `iam.disableCrossProjectServiceAccountUsage` boolean constraint _is not enforced_ for the project.

This boolean constraint controls whether you can attach a service account to a resource in another project. It is enforced by default and can only be configured at the project level, not the folder or organization level.

When this constraint is not enforced, IAM adds a [project lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) that prevents the project from being deleted. This lien has the origin `iam.googleapis.com/cross-project-service-accounts`. We strongly discourage you from deleting this lien.

  * Recommended: Ensure that the `iam.restrictCrossProjectServiceAccountLienRemoval` boolean constraint _is enforced_ for the project.

This boolean constraint ensures that principals can remove the project lien only if they have the `resourcemanager.projects.updateLiens` permission at the organization level. If this constraint is not enforced, principals can remove the project lien if they have this permission at the project level.




To learn how to view or change a boolean constraint in an organization policy, see [Creating and managing organization policies](https://docs.cloud.google.com/resource-manager/docs/organization-policy/creating-managing-policies).

## Disable service accounts from being attached across projects

If you previously enabled service accounts to be attached across projects, we strongly discourage you from disabling this feature, especially in production environments.

**Caution:** If you disable service accounts from being attached across projects, your Google Cloud resources might not work correctly.

Specifically, in the project where your service accounts are located, you shouldn't make any of these changes:

  * Don't update the project's organization policies to _enforce_ the `iam.disableCrossProjectServiceAccountUsage` boolean constraint.
  * Don't update the project's organization policies to _not enforce_ the `iam.restrictCrossProjectServiceAccountLienRemoval` boolean constraint.
  * Don't remove the [project lien](https://docs.cloud.google.com/resource-manager/docs/project-liens) with the origin `iam.googleapis.com/cross-project-service-accounts`, which prevents you from deleting the project.
  * Don't delete the project.



If you are willing to accept the risk of disabling this feature, you can reduce your risk by [disabling the service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#disabling) that you are using across projects, then monitoring your Google Cloud environment for issues. If you see any issues, you can [re-enable the service accounts](https://docs.cloud.google.com/iam/docs/service-accounts-disable-enable#enabling). If you don't see any issues, then you might not have any Google Cloud resources that depend on a service account in a different project.

## Audit logs for attaching service accounts

When a principal uses the `iam.serviceAccounts.actAs` permission to attach a service account to a resource, IAM generates an audit log. This audit log contains the following information:

  * The email address of the principal that attached the service account to the resource
  * Details about the service account that was attached to the resource



For a list of resources that you can attach service accounts to, see Attach the service account to the new resource on this page.

For an example of this type of audit log, see [Logs for using the `iam.serviceAccounts.actAs` permission](https://docs.cloud.google.com/iam/docs/audit-logging/examples-service-accounts#use-actas). To learn more about audit logs in general, see [Cloud Audit Logs overview](https://docs.cloud.google.com/logging/docs/audit).

## What's next

  * Find out how to [attach a service account to a Compute Engine instance](https://docs.cloud.google.com/compute/docs/access/service-accounts#associating_a_service_account_to_an_instance).
  * Review and apply [best practices for securing service accounts](https://docs.cloud.google.com/iam/docs/best-practices-service-accounts).
  * Learn more about [audit logging for IAM](https://docs.cloud.google.com/iam/docs/audit-logging).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
