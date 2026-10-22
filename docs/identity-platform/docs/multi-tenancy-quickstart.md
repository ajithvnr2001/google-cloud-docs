---
url: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-quickstart/
title: Set up multi-tenancy in Identity Platform \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:53:26.661084+00:00
---

# Set up multi-tenancy in Identity Platform  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-quickstart/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Identity Platform ](https://docs.cloud.google.com/identity-platform/docs)
  * [ Guides ](https://docs.cloud.google.com/identity-platform/docs/how-to)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Set up multi-tenancy in Identity Platform

This quickstart shows you how to enable multi-tenancy in Identity Platform and create and select new tenants using the Google Cloud console.

To learn more about multi-tenancy in Identity Platform, see [multi-tenancy](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy).

* * *

To follow step-by-step guidance for this task directly in the Google Cloud console, click **Guide me** : 

[Guide me](https://console.cloud.google.com/?walkthrough_id=identity-platform--multi-tenancy-quickstart)

* * *

## Before you begin

  1. Sign in to your Google Cloud account. If you're new to Google Cloud, [ create an account](https://console.cloud.google.com/freetrial) to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 
  2. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  3. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  4. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 

  5. In the Google Cloud console, on the project selector page, select or create a Google Cloud project.

**Roles required to select or create a project**

     * **Select a project** : Selecting a project doesn't require a specific IAM role—you can select any project that you've been granted a role on. 
     * **Create a project** : To create a project, you need the Project Creator role (`roles/resourcemanager.projectCreator`), which contains the `resourcemanager.projects.create` permission. [Learn how to grant roles](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 
**Note** : If you don't plan to keep the resources that you create in this procedure, create a project instead of selecting an existing project. After you finish these steps, you can delete the project, removing all resources associated with the project.

[Go to project selector](https://console.cloud.google.com/projectselector2/home/dashboard)

  6. If you're using an existing project for this guide, verify that you have the permissions required to complete this guide. If you created a new project, then you already have the required permissions. 

  7. [Verify that billing is enabled for your Google Cloud project](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#confirm_billing_is_enabled_on_a_project). 




### Required roles

To get the permissions that you need to set up multi-tenancy, ask your administrator to grant you the [Identity Platform Admin ](https://docs.cloud.google.com/iam/docs/roles-permissions/identityplatform#identityplatform.admin) (`roles/identityplatform.admin`) IAM role on your project. For more information about granting roles, see [Manage access to projects, folders, and organizations](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access). 

This predefined role contains the permissions required to set up multi-tenancy. To see the exact permissions that are required, expand the **Required permissions** section: 

#### Required permissions

The following permissions are required to set up multi-tenancy:

  * `firebaseauth.configs.update`
  * `identitytoolkit.tenants.create`



You might also be able to get these permissions with [custom roles](https://docs.cloud.google.com/iam/docs/creating-custom-roles) or other [predefined roles](https://docs.cloud.google.com/iam/docs/roles-overview#predefined). 

## Enable multi-tenancy

  1. In the Google Cloud console, go to the **Identity Platform > Settings** page.  
[Go to Settings](https://console.cloud.google.com/customer-identity/settings)

  2. Click the **Security** tab.

  3. In the **Multi-tenancy** section, click **Allow tenants**.




This enables multi-tenancy and opens the **Tenants** page.

You are now ready to create your first tenant.

## Create a tenant

  1. In the **Tenants** page, click **Add tenant**.

  2. In the **Name** field, enter a name for the tenant. This does not need to be unique; Identity Platform automatically assigns a distinct ID.

  3. Click **Save**.




Congratulations! You've created an Identity Platform tenant.

## Select a tenant

In the **Settings** page, select your tenant from the **Scope to a tenant** list.

Each tenant has its own providers and users. After you've selected a tenant, you can manage it the same way you manage a non-tenant Identity Platform project.

## Disable multi-tenancy

To disable multi-tenancy, use the [Identity Toolkit API](https://docs.cloud.google.com/identity-platform/docs/reference/rest/v2/projects/updateConfig).

## What's next

  * [Sign in users with tenants](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-authentication)
  * [Create a sign-in page for multiple tenants](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-ui)
  * [Migrate existing users to a tenant](https://docs.cloud.google.com/identity-platform/docs/migrate-users-between-projects-tenants)
  * [Manage tenants programmatically](https://docs.cloud.google.com/identity-platform/docs/multi-tenancy-managing-tenants)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
