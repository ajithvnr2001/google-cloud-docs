---
url: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/setup/
title: Set up Enterprise Knowledge Graph API \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:11:46.269744+00:00
---

# Set up Enterprise Knowledge Graph API  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/enterprise-knowledge-graph/docs/setup/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Enterprise Knowledge Graph ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs)
  * [ Guides ](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/overview)



Send feedback 

#  Set up Enterprise Knowledge Graph API Stay organized with collections  Save and categorize content based on your preferences. 

This guide provides all required setup steps to start using Enterprise Knowledge Graph.

## About the Google Cloud console

The [Google Cloud console](https://console.cloud.google.com/) is a web UI used to provision, configure, manage, and monitor systems that use Google Cloud products. You use the Google Cloud console to set up and manage Enterprise Knowledge Graph resources.

## Create a project

To use services provided by Google Cloud, you must create a _project_.

A project organizes all your Google Cloud resources. A project consists of the following components:

  * A set of collaborators
  * Enabled APIs (and other resources)
  * Monitoring tools
  * Billing information
  * Authentication and access controls



You can create one project, or you can create multiple projects. You can use your projects to organize your Google Cloud resources in a [resource hierarchy](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy). For more information about projects, see the [Resource Manager documentation](https://docs.cloud.google.com/resource-manager/docs/creating-managing-projects).

In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

  * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
  * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 



[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

## Enable the API

You must enable the Enterprise Knowledge Graph API for your project. For more information about enabling APIs, see the [Service Usage documentation](https://docs.cloud.google.com/service-usage/docs/enable-disable).

Enable the Enterprise Knowledge Graph API, if it is not already enabled. 

**Roles required to enable APIs**

To enable APIs, you need the `serviceusage.services.enable` permission. If you created the project, then you likely already have this permission through the Owner role (`roles/owner`). Otherwise, you can get this permission through the Service Usage Admin role (`roles/serviceusage.serviceUsageAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

[Enable the API](https://console.cloud.google.com/apis/enableflow?apiid=enterpriseknowledgegraph.googleapis.com)

## Set up authentication

Any client application that uses the API must be authenticated and granted access to the requested resources. This section describes important authentication concepts and provides steps for setting it up. For more information, see the [Authentication overview](https://docs.cloud.google.com/docs/authentication).

### About service accounts

There are multiple options for authentication, but we recommend that you use _service accounts_ for authentication and access control. A service account provides credentials for applications, as opposed to end users. Projects own their service accounts. You can create many service accounts for a project. For more information, see [Service accounts](https://docs.cloud.google.com/docs/authentication#service-accounts).

### About roles

When calling an API, Google Cloud requires the calling [identity](https://docs.cloud.google.com/iam/docs/overview) (any applicable person, entity, or process and their defined attributes) to have the appropriate permissions. You can grant permissions by granting roles to a service account. For more information, see the [Identity and Access Management (IAM) documentation](https://docs.cloud.google.com/iam/docs/understanding-roles).

For the purpose of trying the Enterprise Knowledge Graph API, you can use the **Project > Owner** role in the following steps. The **Project > Owner** role grants the service account full permission to resources in your project. If your service account does not require full permissions, you specify a more restrictive role using the [Google Cloud console](https://console.cloud.google.com/). For a list of permissions and roles for Enterprise Knowledge Graph, see [Enterprise Knowledge Graph permissions](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/access-control/iam-permissions) and [Enterprise Knowledge Graph roles](https://docs.cloud.google.com/enterprise-knowledge-graph/docs/access-control/iam-roles). For information about managing permissions using IAM roles, see [granting roles to service accounts](https://docs.cloud.google.com/iam/docs/granting-roles-to-service-accounts).

### About service account keys

Service accounts are associated with one or more public or private key pairs. When you create a new key pair, you download the private key. The Google Cloud CLI uses your private key to generate credentials when calling the API.

**Note:** Service account keys are a security risk if not managed correctly. You should [ choose a more secure alternative to service account keys](https://docs.cloud.google.com/docs/authentication#auth-decision-tree) whenever possible. If you must authenticate with a service account key, you are responsible for the security of the private key and for other operations described by [ Best practices for managing service account keys](https://docs.cloud.google.com/iam/docs/best-practices-for-managing-service-account-keys). If you are prevented from creating a service account key, service account key creation might be disabled for your organization. For more information, see [ Managing secure-by-default organization resources](https://docs.cloud.google.com/resource-manager/docs/secure-by-default-organizations). 

If you acquired the service account key from an external source, you must validate it before use. For more information, see [ Security requirements for externally sourced credentials](https://docs.cloud.google.com/docs/authentication/external/externally-sourced-credentials). 

### Create a service account and download the private key file

Create a service account: 

  1. Ensure that you have the Create Service Accounts IAM role (`roles/iam.serviceAccountCreator`) and the Project IAM Admin role (`roles/resourcemanager.projectIamAdmin`). [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
  2. In the Google Cloud console, go to the **Create service account** page. 

[Go to Create service account](https://console.cloud.google.com/projectselector/iam-admin/serviceaccounts/create?supportedpurview=project)
  3. Select your project. 
  4. In the **Service account name** field, enter a name. The Google Cloud console fills in the **Service account ID** field based on this name. 

In the **Service account description** field, enter a description. For example, `Service account for quickstart`. 

  5. Click **Create and continue**. 
  6. Grant the **Project > Owner** role to the service account. 

To grant the role, find the **Select a role** list, then select **Project > Owner**. 

**Note** : The **Role** field affects which resources the service account can access in your project. You can revoke these roles or grant additional roles later. In production environments, do not grant the Owner, Editor, or Viewer roles. Instead, grant a [predefined role](https://docs.cloud.google.com/iam/docs/understanding-roles#predefined_roles) or [custom role](https://docs.cloud.google.com/iam/docs/understanding-custom-roles) that meets your needs. 
  7. Click **Continue**. 
  8. Click **Done** to finish creating the service account. 

Do not close your browser window. You will use it in the next step. 




Create a service account key: 

  1. In the Google Cloud console, click the email address for the service account that you created. 
  2. Click **Keys**. 
  3. Click **Add key** , and then click **Create new key**. 
  4. Click **Create**. A JSON key file is downloaded to your computer. 
  5. Click **Close**. 



### Use the service account key file in your environment

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
