---
url: https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account/
title: Close or reopen your Cloud Billing account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T13:57:19.782661+00:00
---

# Close or reopen your Cloud Billing account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/close-or-reopen-billing-account/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Close or reopen your Cloud Billing account Stay organized with collections  Save and categorize content based on your preferences. 

To use Google Cloud or Google Maps Platform services, you must have an active Cloud Billing account linked to your projects to pay for your usage costs. However, you might want to cancel your Google Cloud account or stop accruing any charges for your Google Cloud or Google Maps Platform usage. This document describes how to close a Cloud Billing account, or how to reopen a Cloud Billing account that was previously closed.

## Close a Cloud Billing account

When you close a Cloud Billing account, all services are stopped in all projects that are paid for by that billing account.

### Permissions required for this task

To close a Cloud Billing account, you need a role that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * [`billing.accounts.close`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#account_management)



To gain this permission using a predefined role, ask your administrator to grant you the following role on the Cloud Billing account:

  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access)

**Warning:** Closing an active Cloud Billing account stops _all_ billable services in _any_ [projects linked to the account](https://docs.cloud.google.com/billing/docs/how-to/view-linked), such as running VM instances or storage buckets. For Google Cloud, Google Maps Platform, Firebase, and Google AI Studio services, if your projects are linked to a Cloud Billing account that is not in a billable state (such as an account suspension or billing account closure), you can't use the products and services enabled in your projects. This is true even if your projects only use Google Cloud or other billing-eligible [services that are free](https://docs.cloud.google.com/free/docs/gcp-free-tier).

### Before you close a billing account

Before closing a Cloud Billing account, we recommend you do the following:

  * Identify the [projects that are linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked) that you intend to close.
  * If you want to keep services and resources running in any [associated projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked), [link those projects to a different active Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project) before you close the current one.
  * Alternatively, you can [**disable billing on each project**](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) before closing the Cloud Billing account.

    * For **Google Cloud** and **Google Maps Platform** services, when you disable billing on the project, your services are stopped and billing on that project stops.
    * For **Gemini API in AI Studio** usage, when you disable billing on a project, the project's billing tier is downgraded to the Free tier, which allows [limited free usage](https://ai.google.dev/gemini-api/docs/billing).
    * For **Firebase** services, when you disable billing on a project, the project is downgraded to the [no-cost _Spark plan_](https://firebase.google.com/docs/projects/billing/firebase-pricing-plans), which provides full usage of free services, plus limited usage and quota for paid Firebase services.
  * For **Gemini API in AI Studio** users with projects on a paid tier:

    * If your projects are linked to a Cloud Billing account with a [**Prepay** charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view_your_charging_cycle) and you have a positive credit balance in your [Prepay Google payments account](https://ai.google.dev/gemini-api/docs/billing#prepay), any remaining **_Prepay_ credits are forfeited when you close the Cloud Billing account**.
    * If you [meet the criteria](https://ai.google.dev/gemini-api/docs/billing#about-billing) to upgrade your _Prepay_ account to a _Postpay_ billing tier, consider upgrading to Postpay before you close the Cloud Billing account. When you upgrade to a Postpay payments account, you'll receive a refund for the balance of any unused Prepay credits.

**Caution:** Be aware that when a project is linked to a Cloud Billing account that is not in a billable state (such as an account suspension or billing account closure), the project might be shut down, or services within the project might be degraded, stopped, or removed. To understand how your data can be impacted, see [Data deletion on Google Cloud](https://docs.cloud.google.com/docs/security/deletion).

### How to close an account

To close a Cloud Billing account, follow the steps for the [type of account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) (self-serve or invoiced) you want to close.

### Self-serve account

You can manage many settings for your [self-serve (online) Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) in the Google Cloud console, including closing an account. Complete the following steps to close a self-serve billing account:

  1. In the Google Cloud console, go to the **Account management** page.

[Go to Account management in the Cloud Billing console](https://console.cloud.google.com/billing/manage)

  2. At the prompt, choose the Cloud Billing account that you want to close.

The **Account management** page opens for the selected Cloud Billing account.

  3. At the top of the page, click cancel **Close billing account**.

**After you close your Cloud Billing account** , we'll bill you for the usage costs you accrued prior to canceling your account. This bill is the last bill you receive, unless you reopen the account and reactivate your services.




**Why can't I see or access the cancel **Close billing account** button?**

If you're on the **Account management** page of the Cloud Billing account that you want to close and you don't see or can't access the cancel **Close billing account** button, the reasons could include the following:

  * You don't have the permissions needed to close this Cloud Billing account. Contact your Cloud Billing account administrator.
  * Your Cloud Billing account has outstanding charges or outdated payment information. You can't close a billing account until you [pay off any previous balance](https://docs.cloud.google.com/billing/docs/how-to/manual-payment) or [fix payment information](https://docs.cloud.google.com/billing/docs/how-to/payment-methods).
  * Your Cloud Billing account is configured as an [invoiced account](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle). To close an invoiced Cloud Billing account, contact your [Google Cloud sales specialist](https://cloud.google.com/contact) or [contact Cloud Billing Support](https://docs.cloud.google.com/support/billing).



**Tip** : To stop new charges from accruing in a Cloud Billing account, [disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) on each [project linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked) or [link those projects to a different, active Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

### Invoiced account

If your Cloud Billing account is configured as an [invoiced account](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle), you can't close the billing account online, in the Google Cloud console. Rather, we must perform this action for you.

To close an invoiced Cloud Billing account, contact your [Google Cloud sales specialist](https://cloud.google.com/contact) or [contact Cloud Billing Support](https://docs.cloud.google.com/support/billing).

**Tip** : To stop new charges from accruing in a Cloud Billing account, [disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) on each [project linked to the Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked) or [link those projects to a different, active Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).

**Note:** If your Cloud Billing account is configured as a [self-serve (online) Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you _can_ close the billing account online. Follow the instructions in the **Self-serve account** tab.

## Reopen a closed Cloud Billing account

When you reopen a closed a Cloud Billing account, all projects that are linked to and paid by that billing account will start incurring charges for the usage of any billable services in the projects.

### Permissions required for this task

To reopen a Cloud Billing account, you need a role that includes the following [permission](https://docs.cloud.google.com/iam/docs/roles-permissions/billing) on your Cloud Billing account:

  * [`billing.accounts.reopen`](https://docs.cloud.google.com/billing/docs/how-to/custom-roles#account_management)



To gain this permission using a predefined role, ask your administrator to grant you the following role on the Cloud Billing account:

  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access)



### Before you reopen an account

  1. Before a Cloud Billing account can be reactivated, you must resolve any Google payments-related issues or suspensions. Follow the steps in the [resolving declined payments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#resolving-declined-payments) troubleshooter for assistance.
  2. To reopen a Cloud Billing account, make sure you have the permissions required to reopen the account; typically, you must be a Billing Account Administrator on the Cloud Billing account.



### How to reopen a closed account:

To reopen a closed Cloud Billing account, follow the steps for the [type of account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) (self-serve or invoiced) you want to reopen.

### Self-serve account

You can manage many settings for your [self-serve (online) Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) in the Google Cloud console, including reopening a closed account. Complete the following steps to reopen a self-serve billing account:

  1. Sign in to the **Manage billing accounts** page in the Google Cloud console.

[Sign in to Manage billing accounts](https://console.cloud.google.com/billing)

By default, when you first access the list of Cloud Billing accounts, the account list is filtered to display _Active_ accounts.

  2. In the filter_list **Filter** row, clear the **Status: Active** filter.

All Cloud Billing accounts are displayed. Look for Cloud Billing accounts with a _Closed_ status.

  3. **Click the name** of the Cloud Billing account you want to reopen.

The **Overview** page opens for the billing account.

  4. In the **Billing management** section of the **Billing navigation menu** , click **Account Management**.

  5. At the top of the page, click replay **Reopen billing account**.




**Why can't I see or access the replay **Reopen billing account** button?**

If you're on the **Account Management** page of the closed Cloud Billing account and you don't see or can't access the replay **Reopen billing account** button, the reasons could include the following:

  * This account has unresolved Google payments-related issues or suspensions. You must resolve these issues before you can reopen the account. You might need to [update the payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods) linked to this Cloud Billing account, or [resolve declined payments](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues#resolving_declined_payments).
  * You don't have the permissions needed to reopen this Cloud Billing account. Contact your Cloud Billing account administrator.
  * Your Cloud Billing account is configured as an [invoiced account](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle). To reopen an invoiced Cloud Billing account, contact your [Google Cloud sales specialist](https://cloud.google.com/contact) or [contact Cloud Billing Support](https://docs.cloud.google.com/billing/docs/support#contact-billing-support).



### Invoiced account

If your Cloud Billing account is configured as an [invoiced account](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle), you can't reopen the closed billing account online, in the Google Cloud console. Rather, we must perform this action for you.

To reopen an invoiced Cloud Billing account, contact your [Google Cloud sales specialist](https://cloud.google.com/contact) or [contact Cloud Billing Support](https://docs.cloud.google.com/support/billing).

**Note:** If your Cloud Billing account is configured as a [self-serve (online) Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types), you _can_ reopen the billing account online. Follow the instructions in the **Self-serve account** tab.

## Cancel or delete a Cloud Billing account

**After creation, Cloud Billing accounts can't be canceled or deleted.** Even if you close your Cloud Billing account, the Cloud Billing account information is retained for reporting and auditing purposes.

## Close a Google payments profile

In the **Google payments center** , you can [permanently close your Google payments profile](https://support.google.com/paymentscenter/answer/7688666). Closing your Google payments profile stops payment for **_all_** Google services associated with the profile, and removes your transaction and payment information permanently. **After 30 days have passed, you can't reopen a closed payments profile**.

Before you can close a payments profile, you must cancel any of the following paid Google services or subscriptions that are associated with that profile:

  * Google Workspace, including Google Workspace add-ons
  * Google Ads
  * Android Developer



In addition, you must close the active Cloud Billing account associated with the payments profile. Otherwise, attempting to delete your payments profile will fail with the message, _You have active subscriptions or services_.

If you or another administrator closes your payments profile, you can reopen it within 30 days. To reopen a profile, contact [Google payments center support](https://support.google.com/googlepay/gethelp). After 30 days, you can't reopen a payments profile or find past transaction or payment method information. For steps on closing your payments profile, go to [Permanently end your Google payments service](https://support.google.com/googlepay/answer/7643930).

### Consider alternatives to canceling your account

  * If you want to prevent a Cloud Billing account from accruing charges, you can close the Cloud Billing account, or [disable billing](https://docs.cloud.google.com/billing/docs/how-to/modify-project#disable_billing_for_a_project) on the [associated projects](https://docs.cloud.google.com/billing/docs/how-to/view-linked).

  * If you want to change the form of payment associated with your self-serve Cloud Billing account, you can [manage your payment methods](https://docs.cloud.google.com/billing/docs/how-to/payment-methods) in the [Google payments center](https://support.google.com/paymentscenter/topic/9023854).




## Related topics

  * [Create a new Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/create-billing-account)
  * [Modify a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/modify-billing-account)
  * [View projects linked to a Cloud Billing account](https://docs.cloud.google.com/billing/docs/how-to/view-linked)
  * [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project)
  * [Add, remove, or update a payment method](https://docs.cloud.google.com/billing/docs/how-to/payment-methods)
  * [Resolve billing issues](https://docs.cloud.google.com/billing/docs/how-to/resolve-issues)
  * [View your cost and payment history](https://docs.cloud.google.com/billing/docs/how-to/view-history)
  * [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports)
  * [Split charging cycles for self-serve (online) Cloud Billing accounts](https://docs.cloud.google.com/billing/docs/how-to/split-charging-cycle).



##  Try it for yourself 

If you're new to Google Cloud, create an account to evaluate how our products perform in real-world scenarios. New customers also get $300 in free credits to run, test, and deploy workloads. 

[ Get started for free ](https://console.cloud.google.com/freetrial)

Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
