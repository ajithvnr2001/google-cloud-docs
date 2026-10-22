---
url: https://docs.cloud.google.com/data-studio/change-billing-account/
title: Change your Data Studio Pro billing account \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T05:44:36.356222+00:00
---

# Change your Data Studio Pro billing account  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/data-studio/change-billing-account/

Looker Studio is now called Data Studio. [Learn more about this change](https://docs.cloud.google.com/data-studio/welcome#looker_studio_is_now_called). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Data Studio ](https://docs.cloud.google.com/data-studio)
  * [ Guides ](https://docs.cloud.google.com/data-studio/welcome)



Send feedback 

#  Change your Data Studio Pro billing account Stay organized with collections  Save and categorize content based on your preferences. 

You can change the Google Cloud billing account that is associated with a Data Studio Pro subscription without interrupting access to your Pro assets.

**Note:** the following information applies only to subscriptions that were set up directly from the no-cost version of Data Studio, or that were set up from the Google Cloud console. To update payment methods for subscriptions that were set up using the Google Workspace Admin console, see [Change which payment method to use](https://support.google.com/a/answer/1218673) in the Google Workspace Admin Help Center.

## Before you begin

To change your billing account, you need permissions to unlink the Google Cloud project that you use with Data Studio Pro from the current billing account and to link that project to the target billing account. These permissions are described in the [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#required-permissions-change) page in the Cloud Billing documentation.

## How to change the Google Cloud billing account

To change the Google Cloud billing account that is associated with your Data Studio Pro subscription, complete the following steps:

  * End your current Data Studio Pro subscription. A self-service option lets you do this without a 30-day grace period and without your Data Studio Pro assets being moved out of your Pro project.
  * Update the billing account that is associated with the Google Cloud project that you use with Data Studio Pro.
  * Start a new Data Studio Pro subscription.

**Warning:** Changing the billing account requires ending your current subscription and starting a new one. Users, groups, and their specific Pro licenses are **NOT** automatically transferred from the old subscription to the new one. You must manually add users and groups to the new subscription after it is created to restore their access to Pro features and content.

### End your current Data Studio Pro subscription

Before ending your current subscription, navigate to the Data Studio Pro subscription page and carefully note or export the list of all users and Google Groups that have been granted licenses. This list will be required to manually re-add them to the new subscription.

To end your current subscription, follow these steps:

  1. In Data Studio, click the **Settings** (gear) icon, select **Enterprise admin** , and then select **Pro subscription**.
  2. In the **Looker Studio Pro subscriptions** page, locate the project that is associated with the subscription that you want to change and then click cancel **Cancel subscription**.
  3. In the cancellation dialog, select the checkbox that says **Cancel immediately. Skip the grace period and keep assets in your Google Cloud project.** This action immediately ends your subscription.



### Update the Google Cloud project's billing account

To switch the Google Cloud project that you use with Data Studio Pro to a different billing account, follow these steps:

  1. Navigate to the [Google Cloud console](https://console.cloud.google.com/).
  2. Follow the instructions in [Enable, disable, or change billing for a project](https://docs.cloud.google.com/billing/docs/how-to/modify-project#change_the_billing_account_for_a_project).



### Start a new Data Studio Pro subscription

Finally, start a new Pro subscription that uses the billing account that you selected in the previous step:

  1. [Sign in to Data Studio](https://datastudio.google.com).
  2. Click the **Settings** (gear) icon and select **Enterprise admin**.
  3. Click **Pro subscription** and then, in the **Looker Studio Pro subscriptions** page, follow the steps in [Start a new Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/start-a-new-pro-subscription) to start your new subscription.
  4. When you're prompted to select a project, choose the original Google Cloud project that you used with the previous subscription and that is now associated with the new billing account.



Once the new subscription is active, remember to add the users and groups that you noted down from the previous subscription to restore their access.

**Warning:** If you cancel your subscription but don't re-subscribe within 30 days, your users may lose access to all Data Studio Pro assets. [Learn more about the 30-day cancellation grace period](https://docs.cloud.google.com/data-studio/cancel-a-pro-subscription#grace-period).

## Related resources

  * [Cancel a Data Studio Pro subscription](https://docs.cloud.google.com/data-studio/cancel-a-pro-subscription)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
