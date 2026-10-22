---
url: https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages/
title: Configure overages \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T08:37:36.611933+00:00
---

# Configure overages  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Configure overages Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

When your project reaches its pooled quota for a feature in Gemini Enterprise, feature usage stops unless you enable overages. Enabling overages lets users in your project continue using features beyond the included pooled quota limits at pay-as-you-go overage rates.

You can enable overages only if your project has an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and at least one active, non-free-trial subscription, and uses one of the following license-based product editions:

  * Gemini Enterprise Standard
  * Gemini Enterprise Plus
  * Gemini Enterprise Frontline Starter and Frontline Worker
  * Gemini Enterprise EDU and EDU Pro
  * Gemini Enterprise Standard Emerging Market, Emerging Market EDU, Emerging Market governments. Emerging market editions are available only to eligible customers. Your Google account team assesses the requirements to determine your eligibility.

**Note:** Overages don't apply to the **Gemini Enterprise Pay-as-you-go** edition because you pay for all feature usage on a pay-as-you-go basis.

To learn how overage pricing works and view the pricing tables for each feature, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages#overages).

**Caution:** If you enable overages without setting a monthly spend limit, feature usage continues without restriction after your project exceeds its pooled quota, and you pay for all excess usage at pay-as-you-go overage rates. To prevent unexpected charges, set a monthly spend limit.

## Before you begin

You can enable overages and set spend limits if you meet the following requirements:

  * You are a [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin).

  * You have at least one active, non-free-trial [Gemini Enterprise subscription](https://docs.cloud.google.com/gemini/enterprise/docs/licenses#about-subscriptions) for a license-based edition (such as Gemini Enterprise Standard, Plus, Frontline, EDU, or Emerging Market editions).

  * Your project has an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types). To check your billing account type, see [Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).




## Enable overages

To enable overages for your project, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page.

[Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the tier selector banner, select the edition you want to configure from the **Choose another tier** drop-down menu. Each edition must be configured separately.

  4. Under **Feature usage** > **Pay-as-you-go usage above quota** , turn the toggle to **Enabled**.

  5. Click **Save changes**.

  6. In the **Pay-as-you-go usage above quota enabled** dialog, click **Got it**.




## Set a monthly spend limit

You can set a monthly spend limit on overages and the Pay-as-you-go edition usage for your project. When your project reaches this limit, Gemini Enterprise automatically stops overage usage to prevent unexpected charges.

**Note:** Because stopping usage can take a few minutes to take effect, you might incur charges that exceed your limit.

The budget you set applies to the following product areas:

  * Gemini Enterprise app
  * Gemini Enterprise Agent Platform
  * AI coding tools such as Google Antigravity



To configure a monthly spend limit, do the following:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page.

[Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the **Project monthly spend limit** section, click **Set limit**.

  4. In Cloud Billing, configure your budget and spend cap actions. When defining the scope of your budget, select **Vertex AI (aiplatform.googleapis.com)** from the **Services** list. Cloud Billing bills overages for Gemini Enterprise and AI developer tools under Vertex AI API.

For more information about creating budgets and configuring spend limits, see [Set budget spend caps](https://docs.cloud.google.com/billing/docs/how-to/budgets-spend-caps).




## Turn off overages

When you turn off overages, feature usage stops after your project reaches its pooled quota limits.

Because overages are configured per edition, you turn off overages individually for each edition where you previously enabled them.

To turn off overages for an edition, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page.

[Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Usage** tab.

  3. In the tier selector banner, select the edition you want to configure from the **Choose another tier** drop-down menu. Each edition must be configured separately.

  4. Under **Feature usage** > **Pay-as-you-go usage above quota** , turn the toggle to **Disabled**.

  5. Click **Save changes**.

  6. In the **Disable pay-as-you-go usage above quota?** dialog, click **Disable**.




## What's next

  * Learn how to [view feature usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage).
  * Learn how to [view costs](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
