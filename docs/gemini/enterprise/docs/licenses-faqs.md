---
url: https://docs.cloud.google.com/gemini/enterprise/docs/licenses-faqs/
title: Frequently asked questions about Gemini Enterprise subscriptions and licenses \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T13:12:11.776781+00:00
---

# Frequently asked questions about Gemini Enterprise subscriptions and licenses  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/licenses-faqs/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Frequently asked questions about Gemini Enterprise subscriptions and licenses Stay organized with collections  Save and categorize content based on your preferences. 

This page provides answers to common questions about managing and using the Gemini Enterprise licenses.

## Manage subscriptions

This section covers common questions related to managing your Gemini Enterprise subscriptions.

### Why can't I view and modify subscriptions, including reclaiming, and distributing licenses?

You must have the [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) role to manage subscriptions. You can also use a custom role with specific permissions. Verify that you have this role or the required permissions. If you don't have either, contact your billing account administrator.

For more information, see:

  * [Find a Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/find-billing-account-administrator)
  * [Before you begin in Get subscriptions and assign licenses for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#before-you-begin).



### Can I update the subscription name?

No, you can't update the subscription name after the subscription is created.

If the subscription name is shown as `n/a`, it is a placeholder for a subscription purchased through a sales channel or an offline order form, and it doesn't mean the subscription is invalid.

### Can I reduce the license count?

No, you can't reduce the license count during an active subscription term. License reductions are only possible when the subscription term ends or is up for renewal.

### Why can't I modify or manage the subscription through Google Cloud console?

If you purchased your subscription through an offline order form, you can't modify or manage it directly within the Google Cloud console. Offline order forms are handled outside of the console's self-service interface. To make any changes or updates to your subscription, such as adjusting license counts or renewing, contact your Google Account Manager.

### Why is Edit turned off on the Manage Users page?

In the **Gemini Enterprise licenses** section on the **Manage Users** page, the **Edit** button is turned off.

You can't modify subscription settings directly on this page. Instead, to update settings like license counts, see [Update subscription settings](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#update-subscription).

### What does the `Subscription already exists` error mean when trying to purchase a new subscription?

This error means that you have already purchased a subscription for the same Gemini Enterprise edition and subscription period (monthly or annually) within the same billing account.

To use a subscription for a different project or projects, you need to:

  1. [Update the existing subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#update-subscription) to increase the license count.
  2. [Distribute the licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to the new project.



### Do free-trial licenses include the AI developer tools quota?

Yes. If your project uses an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), a free-trial subscription for the Gemini Enterprise Standard or Plus edition includes access to [AI developer tools](https://docs.cloud.google.com/gemini/enterprise/docs/ai-developer-tools-overview) and its base pooled credit quota. For details on credit amounts and weekly pool calculations, see [Quotas for Standard and Plus editions](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#quotas-standard-plus).

Free-trial seats draw from the same project-level pooled quota allocation as paid seats. However, free-trial subscriptions aren't eligible for [overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#overages).

## Distribute and assign licenses

This section covers common questions related to distributing and assigning Gemini Enterprise licenses to projects and users.

### Can I use one Gemini Enterprise subscription across multiple projects?

Yes, the Gemini Enterprise subscription is managed at the billing account level. This means that any project associated with that billing account can be allocated licenses from your subscription. You can [distribute the licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to multiple projects as needed, allowing flexibility in how you manage access across your different development or production environments.

### Can I distribute licenses to a project in a different organization?

Yes, you can distribute licenses to a project in a different organization. Gemini Enterprise subscriptions are managed at the billing account level. Since a single billing account can be linked to projects across different organizations, you can allocate licenses to any project associated with that billing account, regardless of its organizational affiliation.

### How do I move or share licenses to a different project or region?

To move, share, or correct a license allocation to a different project or region, follow these steps:

  1. [Reclaim the unassigned licenses](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#reclaim-licenses) from the project where they are allocated.
  2. After the licenses are reclaimed, [distribute them](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) to the new target project or the correct region.



### How do I check the list of projects the licenses are allocated to?

To see which projects are allocated licenses from your Gemini Enterprise subscription, use the REST API. The [subscription details method](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#subscription-detail) provides the information you need, including how you distribute licenses across projects linked to your billing account.

### Can I use a license assigned to me in different projects?

No, a user's license for Gemini Enterprise is only valid within the specific project where you distributed it. While you manage subscriptions at the billing account level, you allocate licenses on a per-project basis. Therefore, if you need to use Gemini Enterprise features in multiple projects, you must explicitly distribute licenses to each of those projects.

## Troubleshoot

This section covers common issues and their solutions related to Gemini Enterprise licenses.

### Why am I unable to distribute licenses?

Check the following details:

  * Verify that you have enabled the Discovery Engine API in the project you are distributing the licenses to. 
  * Verify you have the [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) role (`roles/billing.admin`) or a custom role with the required permissions. For more information, see [Before you begin in Get subscriptions and assign licenses for Gemini Enterprise](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#before-you-begin). 
  * The Google Cloud console does not support distributing licenses to multiple projects. Therefore, use the [REST API method](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#distribute-licenses) for this task. 



### What does the `Not enough licenses remaining` error mean?

This error means you are trying to reclaim more licenses than what is available and unassigned. You can only reclaim licenses that are not assigned to users. To resolve this, reduce the number of licenses you are attempting to reclaim, or unassign licenses from users.

### What does the `The quantity exceeds the maximum limit of seats for this account` error mean?

When you're purchasing or modifying licenses directly in the Google Cloud console, this error occurs if you try to buy more seats than allowed for your Cloud Billing account type.

  * **Self-serve (or Online) and resold billing accounts:** Up to **25 seats**.
  * **Invoiced (or Offline) billing accounts:** Up to **1,000 seats**.



If you attempt to increase your seat count beyond these thresholds from the Google Cloud console, or if you attempt to add seats to an account that was previously provisioned above these limits using an offline order form, the operation fails with a maximum seat limit error.

To request seat counts above the online limits, contact your Google Cloud sales representative or account manager to update your order or apply an allowlist exception for your billing account.

### What does the `404 Error: License config not found` error mean?

This error means there is a problem with the request parameter. Before reclaiming or distributing any licenses, verify the subscription information on the [Subscription details page](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#subscription-detail) and the region (Current location) and license config ID (Subscription ID) in the [Manage Users page](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#view-licenses).

### Why can't users access Gemini Enterprise features even though they have licenses?

Common reasons why users might not be able to access features:

  * **Subscription type:** Check if the user's license is from a subscription type that includes the specific features they are trying to access. 
  * **IAM Roles:** Confirm the user has the [Gemini Enterprise User role](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceUser) (`roles/discoveryengine.agentspaceUser`) for the Gemini Enterprise project. For more information, see [IAM roles and permissions](https://docs.cloud.google.com/gemini/enterprise/docs/access-control). 
  * **Workforce Identity Federation:** If you are using [Workforce Identity Federation](https://docs.cloud.google.com/gemini/enterprise/docs/configure-identity-provider), verify that it is correctly configured, as misconfigurations can lead to access issues. 



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
