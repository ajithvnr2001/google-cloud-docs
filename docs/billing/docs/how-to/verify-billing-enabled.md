---
url: https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled/
title: Verify the billing status of your projects \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:19.179389+00:00
---

# Verify the billing status of your projects  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/verify-billing-enabled/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Verify the billing status of your projects Stay organized with collections  Save and categorize content based on your preferences. 

A Cloud Billing account defines who pays for a given set of resources, and it can be linked to one or more projects. Project usage is charged to the linked Cloud Billing account.

This document describes how to verify the billing status of your projects.

## Overview

To ensure that billing is enabled on a project, the project must be linked to a valid, _active_ Cloud Billing account. Typically, projects are linked to a billing account at the time that you create the project.

If projects are linked to a Cloud Billing account that's subsequently closed or suspended, then billing is no longer enabled on those projects. If you want to continue using the projects, you must either reopen the billing account, or move the projects to a different, active Cloud Billing account.

It's possible to unlink a project from a billing account, disabling billing on the project. To continue using the project, you must re-enable billing by linking the project to an active Cloud Billing account.

Use this document to help you determine if billing is enabled on your projects.

### Permissions required for this task

To perform the tasks needed to confirm that billing is enabled on your project, you need a role that includes the following [permissions](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * [`billing.resourceAssociations.list`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations) to view project associations for a billing account.
  * [`billing.accounts.get`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#account_management) to view basic information about the billing account (such as account name, currency, open/closed status).



To gain these permissions, ask your administrator to grant you one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) roles on your Cloud Billing account:

  * Billing Account Viewer
  * Billing Account Costs Manager
  * Billing Account Administrator



For more information about billing permissions, see:

  * [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access)
  * [Create custom roles for Cloud Billing](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#resource_associations)
  * [Understanding predefined IAM roles for Cloud Billing](https://docs.cloud.google.com/iam/docs/roles-permissions/billing)



## Check if billing is enabled on a project

Billing is enabled on a project if the following are true:

  1. The project is linked to a Cloud Billing account.
  2. The linked Cloud Billing account is active and in good standing - that is, the billing account isn't closed or suspended.



### 1\. Identify the Cloud Billing account linked to a project

### Console

To view the Cloud Billing account that's linked to a specific project, do the following:

  1. Sign in to the Google Cloud console.

[Sign in to Google Cloud console](https://console.cloud.google.com/)

  2. In the project drop down ( [your project name] arrow_drop_down) at the top of the Google Cloud console page, select your project.

  3. Open the console **Navigation menu** (menu), and then select **Billing**.




**If a billing account _isn't_ linked to the project:**

  * If the project isn't linked to a Cloud Billing account, you see a dialog with text similar to:

"This project has no billing account"

  * To enable billing on the project, select **Link a billing account**. Note that you need adequate permissions to link a billing account. See [enable billing for an existing project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project) for more information.

  * To view a list of billing accounts for your organization, select **Manage billing accounts**.




**If a billing account _is_ linked to the project:**

  * If the project is linked to a Cloud Billing account, and if you have _only one_ Cloud Billing account, the Billing **Overview** page is displayed.

  * If the project is linked to a Cloud Billing account, and if you have _more than one_ Cloud Billing account, a dialog displays, with text similar to:

"Billing account [Name of your Billing Account] is linked to this project"

  * To view the Billing **Overview** page for the Cloud Billing account that's linked to the project, select **Go to linked billing account**.

  * To view a list of Cloud Billing accounts for your organization, select **Manage billing accounts**.




### gcloud

To view the detailed billing information for a project, run the [`gcloud beta billing projects describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing/projects/describe) command:
    
    
    gcloud beta billing projects describe PROJECT_ID
    

Where:

  * PROJECT_ID is the ID or number of the project for which you want to view billing information.



Example:

To see detailed billing information for a project `my-project`, run:
    
    
    gcloud beta billing projects describe my-project
    

Based on the details returned, you can tell if billing is enabled or not.

* * *

  * **Billing is enabled** for `my-project` if you see a `billingAccountName` _and_ `billingEnabled: true`. The `billingAccountName` is the ID of the Cloud Billing account that's linked to the project. For example:


    
    
      billingAccountName: billingAccounts/0X0X0X-0X0X0X-0X0X0X
      billingEnabled: true
      name: projects/my-project/billingInfo
      projectId: my-project
    

* * *

  * If you see a `billingAccountName` for `my-project`, but you see `billingEnabled: false`, then the project is linked to an _inactive_ Cloud Billing account. **Billing is _not_ enabled** for this project. For example:


    
    
      billingAccountName: billingAccounts/0X0X0X-0X0X0X-0X0X0X
      billingEnabled: false
      name: projects/my-project/billingInfo
      projectId: my-project
    

If the billing account isn't active, you can't use the resources within the linked project. Learn how to [reopen a closed billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#reopen_a_closed_billing_account) or [change the billing account linked to a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

* * *

  * If the `billingAccountName` is blank for `my-project`, then the project isn't linked to any Cloud Billing account. **Billing is _not_ enabled** for this project. For example:


    
    
      billingAccountName: ''
      billingEnabled: false
      name: projects/my-project/billingInfo
      projectId: my-project
    

For information on how to link a billing account to a project, see [enable billing for an existing project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#enable_billing_for_an_existing_project).

### 2\. Confirm the status of the linked Cloud Billing account

### Console

To confirm the linked Cloud Billing account is active, do the following:

  1. View the Billing **Overview** page for the linked billing account.

You might already be on the Billing **Overview** page. If not, do the following:

     1. Sign in to your Cloud Billing account in the Google Cloud console.

[Sign in to your Cloud Billing account](https://console.cloud.google.com/billing/overview)

     2. At the prompt, choose the Cloud Billing account you want to view. The Billing **Overview** page opens for the selected billing account.

If the linked billing account is closed or suspended, you'll see a message at the top of the Billing **Overview** page that indicates the status of the account. For example, if the billing account is closed, you'll see a message similar to the following: "This billing account is closed. Visit the account management page to reopen it and continue using linked projects."

You can't use the resources within the linked projects if the billing account isn't active.

     * [Learn how to reopen a closed billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#reopen_a_closed_billing_account).
     * [Learn how to change the billing account linked to a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).
  2. View the **Payment Overview** page for the linked billing account.

If you're already on the Billing **Overview** page, select the **Payment Overview** tab. Otherwise, do the following to open the **Payment Overview** page:

     1. In the Google Cloud console, sign in to the **Payment Overview** page for your Cloud Billing account.

[Sign in to your Cloud Billing account](https://console.cloud.google.com/billing/payment)

     2. At the prompt, choose the Cloud Billing account you want to view. The Billing **Payment Overview** page opens for the selected billing account.

If the linked Cloud Billing account has an overdue, unpaid balance or an issue with your method of payment, your account might be suspended until you resolve any issues and pay the balance due.

[Learn how to resolve declined payments on self-serve (autopay) accounts](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#resolving_declined_payments).




### gcloud

To view the details for a Cloud Billing account, run the [`gcloud beta billing accounts describe`](https://docs.cloud.google.com/sdk/gcloud/reference/beta/billing/accounts/describe) command:
    
    
    gcloud beta billing accounts describe ACCOUNT_ID
    

Where:

  * ACCOUNT_ID is the ID of the billing account you want to view, in the form of 0X0X0X-0X0X0X-0X0X0X. To see available IDs, run `$ gcloud alpha billing accounts list`.



Example:

To see details for billing account `0X0X0X-0X0X0X-0X0X0X`, run:
    
    
    gcloud beta billing accounts describe 0X0X0X-0X0X0X-0X0X0X
    

The information returned for a billing account includes the billing account display name and the active status of the account. For example:
    
    
      displayName: My Billing Account
      masterBillingAccount: ''
      name: billingAccounts/0X0X0X-0X0X0X-0X0X0X
      open: true
    

  * `displayName` is the name you assigned to the billing account.
  * `masterBillingAccount` indicates if the billing account you're viewing is a parent/top-level account or a subaccount. If you see a value in `masterBillingAccount`, then the billing account you're viewing is a subaccount of the parent billing account displayed in `masterBillingAccount`. If `masterBillingAccount` is blank, then the billing account you're viewing isn't a subaccount.
  * `name` is the ID of the billing account you're viewing.
  * `open` indicates if the billing account is active. If `true`, the billing account is open. If `false`, the billing account is closed or suspended. Billing is _not_ enabled for any projects linked to a closed billing account.



If the billing account isn't open, you can't use the resources within the linked project. Learn how to [reopen a closed billing account](https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account#reopen_a_closed_billing_account) or [change the billing account linked to a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

## Related topics

For information on accessing a tabular view of all your projects and the Cloud Billing account linked to each project, see [View projects linked to billing accounts](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
