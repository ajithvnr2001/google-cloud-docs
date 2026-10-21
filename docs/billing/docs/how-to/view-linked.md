---
url: https://docs.cloud.google.com/billing/docs/how-to/view-linked/
title: View projects linked to Cloud Billing accounts \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:19.125565+00:00
---

# View projects linked to Cloud Billing accounts  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/view-linked/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  View projects linked to Cloud Billing accounts Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Billing account defines who pays for a given set of resources, and it can be linked to one or more projects. Project usage is charged to the linked Cloud Billing account. In most cases, you configure billing when you create a project.

If you're managing billing for projects under a cost center or if you need to close your Cloud Billing account, you'll need to know which projects are linked to your Cloud Billing account.

## View the projects linked to a billing account

### Permissions required to complete this task

To view the list of projects linked to a Cloud Billing account, you need a role that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * [`billing.resourceAssociations.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) to view project associations for the billing account.



To gain this permission using a predefined role, ask your administrator to grant you one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) roles on your Cloud Billing account:

  * Billing Account Viewer
  * Billing Account Costs Manager
  * Billing Account Administrator



### How to view the projects linked to a billing account

Follow these steps to open a billing account and then view a list of projects linked to that billing account.

  1. In the Google Cloud console, go to the **Account management** page for the Cloud Billing account.

[Go to Account Management page](https://console.cloud.google.com/billing/manage)

  2. At the prompt, choose the Cloud Billing account that you want to view.

  3. On the **Account management** page, linked projects are listed under **Projects linked to this billing account**.




A padlock icon lock displays next to each project that's locked to its linked Cloud Billing account. For information about unlocking or locking this link, see [Secure the link between a project and its billing account](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link).

For information about changing the billing account for a project, see [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

## View the billing account linked to each of your projects

### Permissions required to complete this task

To view a tabular list of all your projects and their linked Cloud Billing, you need a role that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on each of your projects:

  * [`resourcemanager.projects.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) to view projects.



To gain this permission using a predefined role, ask your administrator to grant you one of the following roles on your projects:

  * Project Browser
  * Project Viewer
  * Project Editor
  * Project Owner



### How to view a list of projects and their linked billing account

Follow these steps to view a list of all your projects and the billing account linked to each project.

  1. In the Google Cloud console, go to the **Manage Billing Accounts** page.

[Go to Manage Billing Accounts page](https://console.cloud.google.com/billing)

  2. Select the **My projects** tab.

You'll see a table that lists all of your projects, and the associated billing account name and billing account ID. If a billing account isn't linked to a project, in the **Billing account** column, you see _Billing is disabled_.




A padlock icon lock displays next to each project that's locked to its linked Cloud Billing account. For information about unlocking or locking this link, see [Secure the link between a project and its billing account](https://docs.cloud.google.com/billing/docs/how-to/secure-project-billing-account-link).

For information about enabling billing on a project, see [Enable billing for an existing project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project).

For information about changing the billing account for a project, see [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project).

## Verify the status of the linked billing account

A Cloud Billing account can be closed or suspended at any time, causing billing to become disabled on all projects that remain linked to that account. [Learn how to confirm the status of the linked Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled#billing_account_status).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
