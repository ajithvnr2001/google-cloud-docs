---
url: https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources/
title: Quickstart: Create your Google Cloud resource hierarchy \u00a0|\u00a0 Resource Manager \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T03:20:26.069482+00:00
---

# Quickstart: Create your Google Cloud resource hierarchy  |  Resource Manager  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Security ](https://docs.cloud.google.com/docs/security)
  * [ Resource Manager ](https://docs.cloud.google.com/resource-manager/docs)
  * [ Guides ](https://docs.cloud.google.com/resource-manager/docs/resource-manager-overview)



Send feedback  Stay organized with collections  Save and categorize content based on your preferences. 

# Manage your Google Cloud resources

This page explains how to view and manage your Google Cloud resources, grant Identity and Access Management (IAM) roles at the organization level, and manage organization resource billing accounts using the [Google Cloud console](https://console.cloud.google.com/).

## Before you begin

  1. Make sure that you have an [organization resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#organizations).

An organization resource is available for Google Workspace and Cloud Identity customers:

     * **Google Workspace:** Sign up for [Google Workspace](https://support.google.com/a/answer/53926). 
     * **Cloud Identity:** Sign up for [Cloud Identity](https://docs.cloud.google.com/identity/docs/set-up-cloud-identity-admin). 

Once you have created your Google Workspace or Cloud Identity account and associated it with a domain, your organization resource will be automatically created for you. The resource will be provisioned at different times depending on your account status: 

     * If you are new to Google Cloud and have not created a project yet, the organization resource will be created for you when you log in to the Google Cloud console and accept the terms and conditions. 
     * If you are an existing Google Cloud user, the organization resource will be created for you when you create a new project or billing account (if one doesn't already exist). Any projects you created previously will be listed under "No organization", and this is normal. The organization resource will appear and the new project you created will be linked to it automatically. 

You will need to move any projects you created under "No organization" into your new organization resource. For instructions on how to move your projects, see [Migrating projects into an organization resource](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing). 

The organization resource that is created will be linked to your Google Workspace or Cloud Identity account with the project or billing account you created set as a child resource. All projects and billing accounts created under your Google Workspace or Cloud Identity domain will be children of this organization resource. 

     * For information about how to migrate pre-existing projects, see [Migrating existing projects](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing). 

Each Google Workspace or Cloud Identity account is associated with exactly one organization resource. An organization resource is associated with exactly one domain, which is set when the organization resource is created. 

**Note:** Trying to register an organization with a domain that already exists will result in a "This domain is already in use" error. To resolve this, follow the steps in [Resolve "This domain is already in use"](https://support.google.com/a/answer/80610#zippy=%2Cthis-domain-is-already-in-use%2Cthis-domain-has-been-registered-and-is-in-the-process-of-ownership-verification). 

  2. Make sure that you have the Organization Administrator role on the organization resource.

If you're the Super Admin of your Google Workspace domain account, you can add yourself and others as the Organization Administrator of the corresponding organization resource. For instructions on adding Organization Administrators, see [Adding an organization administrator](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#adding_an_organization_admin). 

  3. Make sure that you have the following role or roles on the organization: Billing Account Creator, Folder Creator, Project Creator 

#### Check for the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. In the **Principal** column, find all rows that identify you or a group that you're included in. To learn which groups you're included in, contact your administrator. 

     4. For all rows that specify or include you, check the **Role** column to see whether the list of roles includes the required roles. 

#### Grant the roles

     1. In the Google Cloud console, go to the **IAM** page. 

[Go to IAM](https://console.cloud.google.com/projectselector/iam-admin/iam?supportedpurview=organizationId)
     2. Select the organization. 
     3. Click person_add **Grant access**. 
     4. In the **New principals** field, enter your user identifier. This is typically the email address for a Google Account.

     5. Click **Select a role** , then search for the role. 
     6. To grant additional roles, click add **Add another role** and add each additional role. 
     7. Click **Save**. 



## View your resources

To view your Google Cloud resources, follow these steps:

  1. Go to the Google Cloud console [Manage resources](https://console.cloud.google.com/cloud-resource-manager) page.   
[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)
  2. All projects and folders in the organization resource are listed on the page.



## Create a project resource

To create a new project, do the following:

  1. Go to the **Manage resources** page in the Google Cloud console. 

[Go to Manage Resources](https://console.cloud.google.com/cloud-resource-manager?walkthrough_id=resource-manager--create-project&start_index=1#step_index=1)

The remaining steps appear in the Google Cloud console.

  2. Click **Create project**. 
  3. In the **New project** window that appears, enter a project name and select a billing account as applicable. A project name can contain only letters, numbers, single quotes, hyphens, spaces, or exclamation points, and must be between 4 and 30 characters. **Note:** A billing account is available for selection only if you have the [Billing Account User](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.user) role (`roles/billing.user`) on the organization or billing account. When granted in combination with the Project Creator role (`roles/resourcemanager.projectCreator`), these roles let you create new projects linked to that billing account. When granted in combination with the Project Billing Manager role (`roles/billing.projectManager`), these roles let you link and unlink projects on the billing account. 
  4. Enter the parent organization or folder resource in the **Parent resource** box. That resource will be the hierarchical parent of the new project. If **No organization** is an option, you can select it to create your new project as the top level of its own resource hierarchy. 
  5. When you're finished entering new project details, click **Create**.



Once you have created your first project, your organization resource will be provisioned automatically.

## Create a folder resource

Once you have an organization resource, you can create folder resources and begin to organize your resource hierarchy. To create a folder in your organization resource, follow these steps:

  1. Go to the Google Cloud console [Manage resources](https://console.cloud.google.com/cloud-resource-manager) page.   
[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)
  2. Click **Create folder** , and select one of the following options: 
     * **Standard Google Cloud folder** : A standard [folder resource](https://docs.cloud.google.com/resource-manager/docs/cloud-platform-resource-hierarchy#folders).
     * **Compliant folder** : An [Assured Workloads folder](https://docs.cloud.google.com/assured-workloads/docs/key-concepts#folders), which provides additional regulatory, regional, or sovereign controls for Google Cloud resources. Selecting this option will take you to Assured Workloads to [create a folder](https://docs.cloud.google.com/assured-workloads/docs/create-folder).
     * In the **Folder name** box, enter your new folder's name.
     * Under **Parent resource** , click **Browse** , then select the organization resource or folder under which you want to create your new folder.
     * When you're finished entering new folder details, click **Create**.



## Grant IAM roles at the organization level

To grant organization-level roles, follow these steps:

  1. Go to the Google Cloud console [IAM & admin](https://console.cloud.google.com/iam-admin/iam/) page:   
[Go to IAM & Admin](https://console.cloud.google.com/iam-admin/iam/)
  2. The **IAM** page that appears shows the following details: 
     * The **Principals** column shows the accounts that have roles in the organization resource, including your account and domain.
     * The **Role(s)** column shows the roles that each principal has. 
       * Next to your account, you should see **Organization Administrator** under **Role(s)**.
       * Next to the domain account, you should see **Project Creator** under **Role(s)**.
       * If you see **Multiple** under **Role(s)** , the account has more than one role. Click the drop-down to see what roles a principal has.
  3. To grant roles to an existing principal, click the drop-down under **Role(s)** and then select each role you want the principal to have. 
     1. When you're finished selecting roles, click **Save**.
  4. To add a new principal, click **Add** at the top of the page. In the **Add principals** dialog that appears: 
     1. Enter an email address in the **Principals** field.
     2. Under **Roles** , select each role you want the principal to have.
     3. When you're finished selecting roles, click **Add**.



The principals you added now have the organization-level permissions you selected.

## Create a billing account

  1. Go to the Google Cloud console [Billing](https://console.cloud.google.com/billing) page:   
[Go to the Billing page](https://console.cloud.google.com/billing)
  2. Click **Create account**.
  3. In the **Create a new billing account** dialog that appears, enter the appropriate details, including a billing account name and your billing information. 
     * The options you see depend on the country of your billing address.
     * For United States accounts, you can't change tax status after you create the billing account.
  4. When you're finished entering details, click **Submit and enable billing**.



You've now created a new billing account for your organization resource.

## Migrate existing billing accounts

If you are a Google Workspace or Cloud Identity customer with existing Cloud Billing accounts, you can migrate them to your organization resource. Migrating a Cloud Billing account into an organization resource doesn't affect project services. 

You must have these roles to migrate billing accounts:

  * You must be a **Billing Account Administrator** for the Cloud Billing account that you want to migrate. 
  * You must be a **Billing Account Creator** on the organization resource to which you want to migrate your Cloud Billing account. 
  * If you want to migrate a Cloud Billing account from an existing organization resource, you must be a **Billing Account Administrator** for the organization resource that you are migrating the Cloud Billing account from. 



To learn about granting these roles, see the [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access). 

To migrate your existing billing accounts into an organization resource, follow the steps below:

  1. Go to the Google Cloud console [Billing](https://console.cloud.google.com/billing) page:   
[Go to the Billing page](https://console.cloud.google.com/billing)
  2. From the **Select an organization** menu, select an organization resource to see the Cloud Billing accounts associated with it, or select **No organization** to see billing accounts that aren't associated with an organization resource. 
  3. Under **Billing account name** , click the name of the Cloud Billing account that you want to migrate. The billing account overview page opens. 
  4. In the Billing navigation menu, click **Account management**. 
  5. At the top of the Account management page, click business **Change Organization** , then select the organization resource to which you want to migrate the Cloud Billing account. 



## View billing accounts under the organization resource

To view billing accounts under an organization resource, follow these steps:

  1. Go to the Google Cloud console [Billing](https://console.cloud.google.com/billing) page:   
[Go to the Billing page](https://console.cloud.google.com/billing)



All billing accounts for the organization resource are listed on the page.

## Clean up

To delete the project you created for this quickstart:

  1. Go to the Google Cloud console [Manage resources](https://console.cloud.google.com/cloud-resource-manager) page.

[Go to Manage resources](https://console.cloud.google.com/cloud-resource-manager)

  2. In the list of resources, select the project that you want to delete.

  3. Click **Delete**.

  4. In the **Shut down project** dialog that appears, enter the project ID, and then click **Shut down**.




The project resources you selected are deleted and all billing and traffic serving stops.

The organization resource is bound to your Google Workspace or Cloud Identity account, and deleting it is potentially a very damaging action that might be impossible to fully reverse. For more information, see [Deleting an organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization#deleting_an_organization_resource). 

## What's next

  * Try [Migrating existing projects into the organization resource](https://docs.cloud.google.com/resource-manager/docs/migrating-projects-billing). 
    * You don't have to move all your project resources at the same time.
    * It's best to start by moving a test project first, and then move the rest of the projects later. 
  * [Learn more about the organization resource](https://docs.cloud.google.com/resource-manager/docs/creating-managing-organization). 



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
