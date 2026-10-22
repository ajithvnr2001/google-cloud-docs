---
url: https://docs.cloud.google.com/billing/docs/how-to/gemini/ai-cost-summary/
title: Analyze your AI spend with the AI Cost Summary Agent \u00a0|\u00a0 Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-22T09:01:18.290104+00:00
---

# Analyze your AI spend with the AI Cost Summary Agent  |  Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/gemini/ai-cost-summary/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Analyze your AI spend with the AI Cost Summary Agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Use Gemini to analyze your AI costs and gain critical insights into your AI-related spend. The **AI Cost Summary Agent** analyzes spending related to Gemini usage, including Gemini API and Vertex AI.

This agent proactively scans your entire AI footprint (pulling data from the relevant sources) to pinpoint the exact drivers of costs and cost changes, and provides useful next steps. This helps reduce the work necessary to understand cost trends and what changes drove your spend.

**Note:** The AI Cost Summary Agent does not appear for Google Cloud Dedicated customers.

## Permissions required to use the AI Cost Summary Agent

To use the AI Cost Summary widget, you need a role that includes the following permissions on the Cloud Billing account:

  * `billing.anomalies.list`
  * `billing.billingAccountPrices.list`
  * `billing.billingAccountServices.list`
  * `billing.billingAccountSkus.list`



To gain these permissions using a predefined role, ask your administrator to grant you one of the following [Cloud Billing IAM](https://docs.cloud.google.com/billing/docs/how-to/billing-access) role on your Cloud Billing account:

  * [Billing Account Viewer](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.viewer)
  * [Billing Account Administrator](https://docs.cloud.google.com/billing/docs/how-to/billing-access#billing.admin)



## Analyze your AI spend

The AI Cost Summary Agent is presented as a widget on the **Billing Overview** page for your Cloud Billing account. To use the AI Cost Summary Agent, complete the following steps:

  1. In the Google Cloud console, go to the **Billing Overview** page for your Cloud Billing account.

[Go to your Cloud Billing account](https://console.cloud.google.com/billing/overview)

  2. At the prompt, choose the Cloud Billing account for which you'd like to analyze your AI spend. The **Billing Overview** page opens for the selected billing account.

  3. Locate the **Your AI Spend** widget.

  4. Type a question about your AI costs into the input field. To get you started, see Example questions.

  5. The widget begins analyzing your AI-related costs and presents you with a summary of the results. This analysis can take approximately 45 seconds.

  6. Review the results of the analysis and ask the agent follow-up questions about your AI-related spend (for example, how to reduce costs, or to investigate cost drivers).




### Example questions

You can ask the agent questions such as:

  * "Tell me about my AI costs for the past 30 days."
  * "I see a Vertex AI cost spike on Feb 3, what caused this?"
  * "What are my top 3 cost drivers right now across all my AI projects?"
  * "Did I have any anomalies in my spend over the past month? What caused it?"
  * "Break down my total spend by API Key so I can see which integration is expensive."



## Limitations

  * **Scope:** The AI Cost Summary Agent is limited to analyzing AI services and can't answer questions about costs unrelated to AI services. Use [cost reports](https://docs.cloud.google.com/billing/docs/how-to/reports) to analyze costs across all Google Cloud products and services.
  * **Accuracy:** Gemini can make mistakes. Always double-check responses and verify the insights and recommendations before making significant financial or architectural changes.



## What's next

  * [View Gemini Enterprise costs in Cloud Billing reports](https://docs.cloud.google.com/billing/docs/how-to/reports/gemini-enterprise-costs)
  * [Learn more about how to analyze billing data with Reports](https://docs.cloud.google.com/billing/docs/how-to/reports)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-20 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-20 UTC."],[],[]] 
