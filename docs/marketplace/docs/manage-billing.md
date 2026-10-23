---
url: https://docs.cloud.google.com/marketplace/docs/manage-billing/
title: Managing billing for Cloud Marketplace products \u00a0|\u00a0 Google Cloud Marketplace \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:45:52.078721+00:00
---

# Managing billing for Cloud Marketplace products  |  Google Cloud Marketplace  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/marketplace/docs/manage-billing/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Access and resource management ](https://docs.cloud.google.com/docs/access-resources)
  * [ Google Cloud Marketplace ](https://docs.cloud.google.com/marketplace/docs)
  * [ Guides ](https://docs.cloud.google.com/marketplace/docs/overview)



Send feedback 

#  Managing billing for Cloud Marketplace products Stay organized with collections  Save and categorize content based on your preferences. 

This page describes how to manage, change, or cancel billing for Cloud Marketplace products.

For information on pricing plans and how you are billed, see [Understanding billing](https://docs.cloud.google.com/marketplace/docs/understanding-billing).

## Before you begin

To manage billing for your organization, you must have the correct [Identity and Access Management (IAM)](https://docs.cloud.google.com/iam/docs) roles or permissions for Cloud Billing. For details on billing permissions, see the [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access).

If you're managing billing for a Kubernetes app within your organization:

  * Ensure that all users who will deploy the product have the following IAM roles:

    * [Viewer](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/viewer`) for the project where a Kubernetes app will be deployed.

    * [Editor](https://docs.cloud.google.com/iam/docs/roles-overview#basic) (`roles/editor`) for any project that you want to add a managed service for.

    * [Service Account User](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountUser) (`roles/iam.serviceAccountUser`) for the project or above service account.

    * [Service Account Key Admin](https://docs.cloud.google.com/iam/docs/roles-permissions/iam#iam.serviceAccountKeyAdmin) (`roles/iam.serviceAccountKeyAdmin`) for the project or above service account.

  * Create a [service account](https://docs.cloud.google.com/iam/docs/creating-managing-service-accounts), which is used to report usage data for the product to Google.

The service account does not require any specific roles or permissions, but must be linked to your plan. To add a service account to your billing plan, see Updating your billing plan for Kubernetes apps.

  * Depending on the product, you might need to grant additional IAM roles to your users. For example, if you are deploying a Kubernetes app, users must also have the [Kubernetes Engine Admin role](https://docs.cloud.google.com/iam/docs/roles-permissions/container) (`roles/container.admin`) for the project or cluster where the app will be deployed.

For steps to grant roles to users, see the [IAM documentation](https://docs.cloud.google.com/iam/docs/granting-changing-revoking-access).




## Managing a project's Cloud Billing account

If your project uses any commercial Cloud Marketplace products that are not free, it must be linked to a Cloud Billing account. The cost of the products is charged to your project's linked Cloud Billing account.

You can link one Cloud Billing account to multiple projects, but you can't link more than one Cloud Billing account at a time to a single project.

**Note:** If you purchased a SaaS product, you might see an additional Google Cloud project, which typically has a project ID beginning with `pr` and a lock icon next to it. Cloud Marketplace uses this project to track and report your usage to Google, and it appears in your [Cloud Billing reports](https://docs.cloud.google.com/billing/docs/reports). Don't modify the Cloud Billing account or other settings for this project and don't run workloads in it.

### Changing a project's Cloud Billing account

**Note:** To modify billing for a project, you must have certain IAM permissions for both the project and Cloud Billing account. For details, see the [guide to modifying a project's billing settings](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

Before you change which billing account is linked to a project, verify that the new billing account has purchased all of the resources required to run the project that were previously purchased from Cloud Marketplace. This prevents your project from being disabled or losing data as a result of losing required resources.

To [change a project's linked Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project), go to the [Cloud Billing page](https://console.cloud.google.com/billing) in Google Cloud console. You might need to select the Cloud Billing account that's currently linked to the project. To view the details of your available Cloud Billing account or accounts, including a list of projects linked to each available Cloud Billing account, click **Account Management**.

Click on a linked project to disable or change that project's linked Cloud Billing account. If there are Cloud Marketplace resources that the project needs to run which haven't been purchased by the new Cloud Billing account that you selected, the Google Cloud console detects the discrepancy and displays a warning message as a reminder.

## Viewing your purchases

You can view purchased Google Cloud Marketplace software as a service (SaaS) products and any products with an accepted private offer that are linked to your billing account on the **Your Orders** page. No Google products, such as the Maps SDK, appear on the page.

**Note:** To view the **Your Orders** page, you must have the [Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview-of-cloud-billing-roles-in-cloud-iam) (`roles/billing.viewer`) IAM role for your billing account. For details on billing permissions, see the [Overview of Cloud Billing access control](https://docs.cloud.google.com/billing/docs/how-to/billing-access).

To view purchases associated with a billing account:

  1. [Go to Cloud Marketplace](https://console.cloud.google.com/marketplace).

[Go to Cloud Marketplace](https://console.cloud.google.com/marketplace)

  2. Click **Your Orders**. You might need to select a billing account.




## Managing billing plans

When you purchase a commercial [Kubernetes app](https://console.cloud.google.com/marketplace/browse?filter=solution-type:k8s) or [SaaS product](https://console.cloud.google.com/marketplace/browse?filter=solution-type:service) in Google Cloud Marketplace, you must select a billing plan on behalf of your organization.

**Note:** When purchasing [virtual machines (VMs)](https://console.cloud.google.com/marketplace/browse?filter=solution-type:vm), you don't need a billing plan. For details on how you are billed, see [pricing plans for VMs](https://docs.cloud.google.com/marketplace/docs/understanding-billing#vm-pricing).

After setting up a billing plan, you can make the product available to users in your organization so that they can deploy it. Users in your organization can deploy a product in all projects that are linked to the same billing account.

### Selecting a billing plan

**Note:** To set up a billing plan, you must have the [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#overview_of_billing_roles_in_iam) (`roles/billing.admin`) role.

To select a billing plan for a SaaS product:

  1. In **Your Orders** , click more_vert **Actions available to manage your orders** for the product.

[Open Your Orders](https://console.cloud.google.com/marketplace/orders)

  2. Select **Change Plan**.

  3. Review the terms of service for the app. When you are ready to accept the terms, click **Continue**.




If the products have the option available, you can also modify your auto-renewal options.

Depending on the type of plan, some plan changes take effect immediately, and some go into effect at the end of the subscription term.

### Updating your billing plan for Kubernetes apps

For Kubernetes apps offered through Google Cloud Marketplace, you must link your billing plan to a service account that reports usage data.

  1. In Cloud Marketplace, open the product page.
  2. Select **Manage Accounts**.
  3. Add another service account by entering the account in the **Service account** field. **Caution:** If you remove a service account that is associated with your billing plan, any Kubernetes deployments that use that service account are stopped.



### Viewing billing reports

In **Your Orders** , you can go directly to the billing report for a selected product, or you can go to the credits billing page, if available.

  1. In **Your Orders** , click more_vert **Actions available to manage your orders** for the product.

[Open Your Orders](https://console.cloud.google.com/marketplace/orders)

  2. Select **View billing report** or **View credit**.




## Canceling your plan

If you want to cancel your plan for a product or any pending plan changes, use the following steps.

### Anthos trial

See [Disabling GKE Enterprise](https://docs.cloud.google.com/anthos/docs/setup/disable-anthos).

###  Gemini Code Assist (trial/paid) 

See [Turn off Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/turn-off).

### Kubernetes apps

  1. In **Your Orders** , select the billing account linked to the purchase.

[Open Your Orders](https://console.cloud.google.com/marketplace/orders)

  2. Select the product with the plan you want to cancel.

  3. Click more_vert **Actions available to manage your orders**.

  4. Select **Cancel plan**.




If you're billed separately by the vendor, you might also need to contact them to cancel your license.

After canceling a subscription, review your Kubernetes deployments. Deployments can keep running in the cluster unless you stop them.

### SaaS products

  1. In **Your Orders** , select the billing account linked to the purchase.

[Open Your Orders](https://console.cloud.google.com/marketplace/orders)

  2. Select the product with the plan you want to cancel.

  3. Click more_vert **Actions available to manage your orders**.

  4. Select **Cancel purchase** or **Cancel subscription**. If you don't want your subscription to renew automatically, select **Cancel auto-renewal**.


**Important:** If you signed up for a specific subscription period, your cancellation takes effect at the end of that period. You're billed through the entirety of your subscription period. For example, if you purchase a one-year subscription term and cancel it after you're billed for the second month, you continue to be billed for the remaining 10 months of your subscription. At the end of the one year subscription period, your subscription doesn't renew for the following year.

If you granted access to a service account for the app, you must manually revoke the access through the IAM page and remove any resources created for the service account.

### VMs

Delete your deployment. If you're billed separately by the vendor, you might need to contact them to cancel your license.

## What's next

  * To learn how you are billed, see [Understanding billing for Cloud Marketplace](https://docs.cloud.google.com/marketplace/docs/understanding-billing).

  * To deploy a Kubernetes app, see [Deploying Kubernetes apps](https://docs.cloud.google.com/marketplace/docs/kubernetes-apps).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
