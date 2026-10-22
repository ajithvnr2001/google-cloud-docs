---
url: https://docs.cloud.google.com/gemini/docs/codeassist/turn-off/
title: Turn off Gemini Code Assist \u00a0|\u00a0 Gemini for Google Cloud \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:50:16.874106+00:00
---

# Turn off Gemini Code Assist  |  Gemini for Google Cloud  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/docs/codeassist/turn-off/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini for Google Cloud ](https://docs.cloud.google.com/gemini/docs)
  * [ Guides ](https://docs.cloud.google.com/gemini/docs/overview)



Send feedback 

#  Turn off Gemini Code Assist Stay organized with collections  Save and categorize content based on your preferences. 

This document explains how to turn off Gemini Code Assist.

## Before you begin

  * To update a Gemini Code Assist subscription, make sure you have the `billing.subscriptions.update` Identity and Access Management (IAM) permission. The `billing.subscriptions.update` permission is included in the [`roles/billing.admin`](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin) IAM role, or you can add the permission to a custom role.



## Turn off Gemini Code Assist

To turn off Gemini Code Assist, do the following:

  1. In the Google Cloud console, go to the **Gemini Products** page.

[Go to Gemini Products](https://console.cloud.google.com/gemini-admin)

  2. From the **Gemini Products** page, navigate to the **Manage Subscription** page for the billing account associated with your project:

     * If you are prompted to select a billing account, select it and click **Continue to Admin for Gemini page**. Then, from the navigation menu, click **Manage Subscription**.
     * If you are not prompted to select a billing account, you are taken to the **Admin for Gemini** page. From the navigation menu, click **Manage Subscription**.
  3. Click the Gemini Code Assist subscription. The name of the subscription depends on the name given when Gemini Code Assist was set up.

  4. Review the subscription details and check the **Auto renew** setting.

     * If **Auto renew** is set to **Off** , then your subscription is already set to end on the subscription end date. No further action is needed.

     * If **Auto renew** is set to **On** , follow these step to disable it:

       1. Click **Manage subscription**.
       2. To proceed to renewal settings, click **Continue**.
       3. For **Automatic subscription renewal** , select **No, don't automatically renew** , and then click **Continue**.
       4. If you agree to the terms of purchase, select **I agree to the terms of this purchase** , and then click **Save changes**.
  5. Optional: If you are disabling all Gemini products in Google Cloud, then turn off the [Gemini for Google Cloud API](https://docs.cloud.google.com/gemini/docs/turn-off-gemini#companion-api).




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
