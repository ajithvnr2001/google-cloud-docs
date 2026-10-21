---
url: https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview/
title: Overview of overages and spend controls \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T23:21:16.563559+00:00
---

# Overview of overages and spend controls  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/manage-costs-overview/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  Overview of overages and spend controls Stay organized with collections  Save and categorize content based on your preferences. 

**Note:** To use this feature, your project must be linked to an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) that receives an active monthly invoice.

In Gemini Enterprise, your subscription entitles your users to specific feature quotas. When your project reaches its pooled quota for a feature, feature usage stops unless you enable overages.

How overages work depends on your product edition:

Product edition | Overages support  
---|---  
**All Gemini Enterprise editions (Gemini Enterprise Standard, Plus, Frontline, EDU, and Emerging Market editions)** |  Supported. You can enable overages to let users exceed included quotas at pay-as-you-go rates. For more information about how pooled quotas work, see [Quotas and overages](https://docs.cloud.google.com/gemini/enterprise/docs/quotas-and-overages).   
  
Overages and spend controls are available only if your project has an [invoiced Cloud Billing account](https://docs.cloud.google.com/billing/docs/concepts#billing_account_types) and at least one active, non-free-trial subscription. To verify your account type, see [ Find out your Cloud Billing account type and charging cycle](https://docs.cloud.google.com/billing/docs/how-to/billing-cycle#view-your-charging-cycle).   
**Gemini Enterprise Pay-as-you-go** |  Not applicable. You pay for all usage on a pay-as-you-go basis without pooled quota limits.   
**Note:** Gemini Enterprise Emerging Market editions are available only to eligible customers. Contact your Google account team to assess the requirements and determine your eligibility.

For more information, see the following resources:

  * [View feature usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage)
  * [Configure overages](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages)



## Cap costs with a project spend limit

To prevent unexpected charges when you enable overages, you can configure a monthly spend limit on your total spend in Cloud Billing. When defining a budget for your project, you select **Vertex AI (aiplatform.googleapis.com)** as the service scope. This sets a project-level spend cap that applies across all of the following areas:

  * Gemini Enterprise app
  * Gemini Enterprise Agent Platform
  * AI coding and developer tools (such as Antigravity)



When your project reaches this spend limit, overage usage is automatically stopped. To configure a monthly spend limit for your project, see [Set a monthly spend limit](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages#set-spend-limit).

**Note:** Because stopping usage can take a few minutes to take effect, you might incur charges that exceed your limit.

## End-user experience when limits are reached

When your project reaches a usage or spending limit, Gemini Enterprise restricts further usage. Feature access resumes automatically when the quota resets or at the start of the next billing cycle.

Gemini Enterprise app displays the **Usage limit reached** error message when you chat with the assistant or use Gemini Enterprise features in either of the following scenarios: 

  * Your project reached its monthly spend cap.
  * Your project exceeds its pooled quota limit for a specific feature and your Gemini Enterprise administrator hasn't enabled overages. 



This error affects only the feature that reached its limit. You can continue using other features that have remaining quota. 

## Budget alert notifications

The Gemini Enterprise app doesn't send automated email alerts or push notifications when your project reaches its pooled feature quotas or starts incurring overage charges. When your project reaches a pooled quota and you haven't enabled overages, end users see the **Usage limit reached** error message in the app.

When you configure a monthly spend limit in Cloud Billing, you can set alert threshold rules to monitor your costs. Cloud Billing automatically sends email notifications when your spend reaches specified percentages of your budget, such as 50%, 80%, and 100% of the budget amount.

The following principals receive budget alert notifications:

  * **Default recipients:** Cloud Billing sends email alerts to users who have the **Billing Account Administrator** or **Billing Account User** IAM roles on the target billing account.
  * **Custom recipients:** You can configure custom email recipients, such as specific project administrators, team distribution lists, or Pub/Sub channels, in your budget alert rules.



For more information, see the following resources:

  * [Create, edit, or delete budgets and budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)
  * [Manage budget alert recipients](https://docs.cloud.google.com/billing/docs/how-to/budgets-notification-recipients)
  * [View costs and cost trends](https://docs.cloud.google.com/gemini/enterprise/docs/view-costs)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
