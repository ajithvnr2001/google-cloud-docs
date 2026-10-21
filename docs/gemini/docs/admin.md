---
url: https://docs.cloud.google.com/gemini/docs/admin/
title: Modify Gemini Code Assist subscriptions \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-14T08:02:46.166718+00:00
---

# Modify Gemini Code Assist subscriptions  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/admin/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Modify Gemini Code Assist subscriptions Stay organized with collections  Save and categorize content based on your preferences. 

This document describes how to access and use the Gemini Code Assist administrator controls.

Gemini Code Assist subscriptions are subject to Google Cloud [Service Specific Terms](https://cloud.google.com/terms/service-terms) regarding Pricing and Billing for Committed Units.

## Grant IAM permissions

In order to get the required permissions for editing Gemini Code Assist subscriptions, ask your administrator to grant you the [`roles/billing.admin` IAM role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) on the billing account.

Alternatively, ask your administrator to grant you the [`roles/consumerprocurement.orderAdmin` role](https://docs.cloud.google.com/marketplace/docs/access-control#consumerprocurement.orderAdmin) _and_ the [`roles/billing.viewer` role](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer).

These roles contain the permissions required to modify Gemini Code Assist subscriptions. To see the exact permissions that are required, expand the **Required permissions** section.

#### Required permissions

  * `consumerprocurement.orders.place`
  * `billing.billingAccountPrices.list`



## Edit a Gemini Code Assist subscription

**Important:** New Gemini Code Assist subscriptions are [no longer available for purchase](https://docs.cloud.google.com/gemini/docs/codeassist/sunset).

  1. In the Google Cloud console, go to the **Admin for Gemini** page.

[Go to **Admin for Gemini**](https://console.cloud.google.com/gemini-admin)

The **Admin for Gemini** page loads.

  2. Use the project picker at the top of the page to ensure you are scoped to the project or folder that has an existing Gemini Code Assist subscription.

  3. Locate the **Gemini Code Assist** product tile, and then click **Manage Gemini Code Assist**.

  4. Select **Manage subscription**.

The **Manage subscription** page appears.

  5. Select **Manage subscription** to edit the subscription, including:

     * **Manage edition** \- If you're editing your Gemini Code Assist subscription, then you can upgrade from Standard edition to Enterprise edition, which takes effect immediately. Alternatively, you can downgrade from Enterprise edition to Standard edition, which takes effect at end of the current subscription term. To see a list of features available in each edition, see [Supported features](https://docs.cloud.google.com/gemini/docs/codeassist/overview#supported-features).

**Note:** Gemini Code Assist Standard licenses obtained using the Gemini Enterprise bundle cannot be upgraded in the Google Cloud console because they are licenses, not a standalone subscription. To obtain Enterprise features in this scenario, you must purchase a separate Gemini Code Assist Enterprise subscription.
     * **Increase or decrease the number of licenses in the subscription** \- Adding licenses makes them available to you almost immediately. However, if you reduce the number of licenses, then the changes won't take effect until the end of the subscription term. Additionally, the original license count is still reflected in your bill until the changes are applied.

     * **Change the subscription period** \- You can set the subscription to bill monthly or annually. With an annual subscription, you are given a discounted rate that is charged on a monthly basis rather than a one-time payment. If you change from an annual subscription to a monthly subscription, then the change won't take effect until the end of the annual term. Additionally, you cannot change the subscription period unless you have enabled subscription auto-renewal.

     * **Enable or disable auto-renewal** \- If you disable auto-renewal, the subscription expires at the end of the subscription term and all the licenses in the subscription become invalid. You cannot re-enable a subscription after it expires. Additionally, if auto-renewal is disabled, then you can't make the following changes:

       * Reduce number of licenses
       * Change from annual to monthly subscription period
       * Change from Enterprise edition to Standard edition
  6. Select **Continue** , and then select **Confirm changes**.


**Note:** Changes to a subscription that decrease the number of licenses, downgrade the edition, or reduce the subscription period don't take effect immediately; instead, they take effect at the end of the current subscription term. Similarly, you can't cancel a subscription during its term. If you want to end your subscription, make sure that you have auto-renewal disabled. For more information, see [Turn off Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/turn-off).

## What's next

  * Learn more about [Gemini Code Assist billing](https://docs.cloud.google.com/gemini/docs/billing-questions).
  * [Manage your Gemini Code Assist licenses](https://docs.cloud.google.com/gemini/docs/codeassist/manage-licenses).
  * [Turn off Gemini Code Assist](https://docs.cloud.google.com/gemini/docs/codeassist/turn-off).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
