---
url: https://docs.cloud.google.com/gemini/enterprise/docs/view-costs/
title: View costs \u00a0|\u00a0 Gemini Enterprise \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T12:42:38.400550+00:00
---

# View costs  |  Gemini Enterprise  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/gemini/enterprise/docs/view-costs/

**Note:** This documentation set is for the Standard, Plus, Pay-as-you-go, and Frontline editions of Gemini Enterprise. For the Business edition documentation, see the [Gemini Enterprise - Business edition Help Center](https://support.google.com/g). 

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ AI and ML ](https://docs.cloud.google.com/docs/ai-ml)
  * [ Gemini Enterprise ](https://docs.cloud.google.com/gemini/enterprise/docs)
  * [ Administrator guide ](https://docs.cloud.google.com/gemini/enterprise/docs/before-you-begin)



Send feedback 

#  View costs Stay organized with collections  Save and categorize content based on your preferences. 

In Gemini Enterprise, the **Billing** tab on the **Usage & Spending** page displays a summary of your overage and Pay-as-you-go usage costs over the last 30 days across your enabled features and tools.

**Note:** The **Usage & Spending** page displays overages and Pay-as-you-go edition usage costs. It doesn't include license-based Gemini Enterprise subscription costs.

The **Billing** tab displays total overage and Pay-as-you-go usage costs that include charges for:

  * Gemini Enterprise app
  * Gemini Enterprise Agent Platform
  * AI developer tools (such as Google Antigravity)



## Before you begin

To view cost details on the **Usage & Spending** page, you need the following IAM roles and permissions:

  * **Required roles** :

    * [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) (`roles/discoveryengine.agentspaceAdmin`) on the project
    * [Billing Account Viewer](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.viewer) (`roles/billing.viewer`) or [Billing Account Administrator](https://docs.cloud.google.com/iam/docs/roles-permissions/billing#billing.admin) (`roles/billing.admin`) on the target billing account
  * **Required permissions** :

    * `monitoring.timeSeries.list` (included by default in the [Gemini Enterprise Administrator](https://docs.cloud.google.com/gemini/enterprise/docs/access-control#discoveryengine.agentspaceAdmin) role)
    * `serviceconsumermanagement.quota.get`

Without these permissions, the **Billing** tab isn't visible. If you use custom roles that don't include these permissions, you must [add the required permissions to the role](https://docs.cloud.google.com/iam/docs/creating-custom-roles#edit-role).




## View costs and cost trends

To view your project's overages and Pay-as-you-go edition usage costs, follow these steps:

  1. In the Google Cloud console, go to the **Gemini Enterprise > Usage & Spending** page.

[Go to Usage & Spending](https://console.cloud.google.com/gemini-enterprise/usage-and-spending)

  2. Select the **Billing** tab.

The **Gemini Enterprise costs (Last 30 days)** section displays the following cost breakdown:

Cost item | Description  
---|---  
Gemini Enterprise app | Charges for Gemini Enterprise feature usages.  
Gemini Enterprise Agent Platform | Charges for building and deploying AI models and agents.  
AI developer tools (such as Antigravity) |  Charges for AI coding and developer tool usage, including Antigravity.   
Total cost |  The combined sum of these overage and Pay-as-you-go usage costs, along with a 30-day cost trend chart.   
  3. To inspect detailed cost breakdowns, invoices, or reports in the Cloud Billing console, click **View details in Billing**.

For more information on billing reports and cost analysis in Cloud Billing, see [View your billing reports and cost trends](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs).




## What's next

  * Learn how to [view feature usage](https://docs.cloud.google.com/gemini/enterprise/docs/feature-usage).
  * Learn how to [configure overages and spend limits](https://docs.cloud.google.com/gemini/enterprise/docs/configure-overages).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
