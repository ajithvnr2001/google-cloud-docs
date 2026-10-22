---
url: https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link/
title: Secure the link between a project and its billing account \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:08:33.682265+00:00
---

# Secure the link between a project and its billing account  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Secure the link between a project and its billing account Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to lock or unlock the link between a project and a Cloud Billing account.

## Why lock a project to its billing account?

To use Google Cloud resources in a project, billing must be enabled on the project. Billing is enabled when the project is linked to an active Cloud Billing account. Projects that aren't linked to an active Cloud Billing account can't use Google Cloud or Google Maps Platform services. To prevent unintentionally changing the billing account that pays for a project, or disabling billing on a project, secure the billing relationship of your project by locking the link between a project and its Cloud Billing account.

**Note:** Locking or unlocking a project to its linked Cloud Billing account is considered a sensitive action; in some cases, you might need to reauthenticate before you can initiate the action. For more information, see [Sensitive actions](https://docs.cloud.google.com/docs/authentication/reauthentication#sensitive-actions). 

By securing the billing relationship of your project, you can protect against an outage to your normal business operations by preventing accidental or unintentional project shutdowns due to the lack of a billing account. When you lock the link between a project and its billing account, changes between the billing account and project can't be made until the relationship is unlocked. Locking creates an intentional, two-step process to change a project's billing status.

**Warning:** Locking the link between a project and its billing account doesn't guarantee that billing will remain enabled on the project. Your billing administrator can close the Cloud Billing account or the billing account might be suspended for nonpayment, causing billing to become disabled on all projects that remain linked to that account. [Learn how to confirm the status of the linked Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#billing_account_status).

## Lock the link between a project and its billing account

When you lock a project to its linked billing account, you can prevent the project from unintentionally being moved (linked) to a different billing account or the project link being deleted from the billing account, disabling billing. By locking the billing account and project relationship, changes between the billing account and project linkage can't be made until the relationship is unlocked.

### Permissions required to lock the link

To perform the tasks needed to lock the link between a project and a Cloud Billing account, you need both project permissions and billing account permissions.

These predefined roles have adequate permissions to perform this task:

  * On the _project_ : Project Billing Manager and Project Browser _or_ Project Owner

**_AND_**

  * On the linked _Cloud Billing account_ : Billing Account User and Billing Account Viewer _or_ Billing Account Administrator


**Using an Organization?** If you're set up to use an [ Organization](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources) to manage your Google Cloud resources and manage Organization billing accounts, then the Billing Account Administrator role granted at the _Organization level_ will have adequate permissions to perform this task.

Specifically, to perform this task, you must have the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing). 

**Action** | **Permission** | **Roles with permission** | **Resource**  
---|---|---|---  
View projects and Cloud Billing account associations | [ `billing.resourceAssociations.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Viewer, Billing Account Costs Manager, or Billing Account Administrator | Billing account  
AND  
[ `resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Browser, Project Viewer, Project Editor, or Project Owner | Project  
Lock the link between a project and its Cloud Billing account | [ `billing.resourceAssociations.create`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account User or Billing Account Administrator | Billing account  
AND  
[ `resourcemanager.projects.createBillingAssignment`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Billing Manager or Project Owner | Project  
  
### How to lock the link between a project and a billing account

To lock the link between a billing account and project, complete the following steps:

  1. In the **Billing** section of the Google Cloud console, locate the project using one of the following methods:

     * View the list of projects linked to a specific billing account.

       1. In the Google Cloud console, go to the **Account management** page for the Cloud Billing account.

[Go to Account Management in Cloud Billing](https://console.cloud.google.com/billing/manage)

       2. At the prompt, choose the Cloud Billing account you want to view.

       3. On the **Account management** page, from the list of projects, locate the project you want to lock.

     * View a list of all your projects and their associated Cloud Billing accounts.

       1. In the Google Cloud console, go to the **My Projects** page in the **Billing** section.

[Go to My Projects in Cloud Billing](https://console.cloud.google.com/billing/projects)

       2. From the list of projects, locate the project you want to lock.

  2. In the project row, open the **Actions** menu (more_vert) and then select **Lock billing**.

  3. On the confirmation screen, click **Lock**.




When successful, you see a confirmation message similar to _The link between "Project Name" and "Billing Account Name" has been locked._ A padlock icon lock displays next to each project that's locked to its linked Cloud Billing account.

After the relationship is locked, changes between the billing account and project can't be made until the relationship is unlocked.

## Unlock the link between a project and its billing account

If the link between a billing account and project is locked, you can't change or disable billing on the project until the relationship is unlocked. If you want to intentionally move (link) the project to a different billing account or delete the link to disable billing on the project, first unlock the link between the project and its billing account.

### Permissions required to unlock the link

To perform the tasks needed to unlock the link between a project and a Cloud Billing account, you need both project permissions and billing account permissions.

These predefined roles have adequate permissions to perform this task:

  * On the _project_ : Project Billing Manager and Project Browser _or_ Project Owner

**_OR_**

  * On the linked _Cloud Billing account_ : Billing Account Administrator


**Using an Organization?** If you're set up to use an [ Organization](https://docs.cloud.google.com/resource-manager/docs/manage-google-cloud-resources) to manage your Google Cloud resources and manage Organization billing accounts, then the Billing Account Administrator role granted at the _Organization level_ will have adequate permissions to perform this task.

Specifically, to perform this task, you must have the following [ permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing). 

**Action** | **Permission** | **Roles with permission** | **Resource**  
---|---|---|---  
View projects and Cloud Billing account associations | [ `billing.resourceAssociations.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Viewer, Billing Account Costs Manager, or Billing Account Administrator | Billing account  
AND  
[ `resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Browser, Project Viewer, Project Editor, or Project Owner | Project  
  
Unlock the link between a project and its Cloud Billing account | [ `billing.resourceAssociations.delete`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Billing Account Administrator | Billing account  
OR  
[ `resourcemanager.projects.deleteBillingAssignment`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) | Project Billing Manager or Project Owner | Project  
  
### How to unlock the link between a project and a billing account

To unlock the link between a billing account and project, complete the following steps:

  1. In the **Billing** section of the Google Cloud console, locate the project using one of the following methods:

     * View the list of projects linked to a specific billing account.

       1. In the Google Cloud console, go to the **Account management** page for the Cloud Billing account.

[Go to Account Management in Cloud Billing](https://console.cloud.google.com/billing/manage)

       2. At the prompt, choose the Cloud Billing account you want to view.

       3. On the **Account management** page, from the list of projects, locate the project you want to unlock. Tip: A padlock icon  lock displays next to each project that's locked to its linked Cloud Billing account.

     * View a list of all your projects and their associated Cloud Billing account.

       1. In the Google Cloud console, go to the **My Projects** page in the **Billing** section.

[Go to My Projects in Cloud Billing](https://console.cloud.google.com/billing/projects)

       2. From the list of projects, locate the project you want to unlock. Tip: A padlock icon  lock displays next to each project that's locked to its linked Cloud Billing account.

  2. In the project row, open the **Actions** menu (more_vert) and then select **Unlock billing**.

  3. On the confirmation screen, click **Unlock**.




When successful, you see a confirmation message similar to _The link between "Project Name" and "Billing Account Name" has been unlocked_.

After the relationship is unlocked, changes between the billing account and project can be made. These changes include [disabling billing on the project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) or [linking the project to a different Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

## Related topics

  * [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project)
  * [View linked projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked)
  * [Verify the billing status of your projects](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled)
  * [Create, modify, or close your Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/manage-billing-account)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
