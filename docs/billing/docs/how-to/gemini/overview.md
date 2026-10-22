---
url: https://docs.cloud.google.com/billing/docs/how-to/gemini/overview/
title: Gemini Cloud Assist in Cloud Billing \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:25:47.362338+00:00
---

# Gemini Cloud Assist in Cloud Billing  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/billing/docs/how-to/gemini/overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Costs and usage management ](https://docs.cloud.google.com/docs/costs-usage)
  * [ Cloud Billing ](https://docs.cloud.google.com/billing/docs)
  * [ Guides ](https://docs.cloud.google.com/billing/docs/concepts)



Send feedback 

#  Gemini Cloud Assist in Cloud Billing Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

[Gemini Cloud Assist](https://docs.cloud.google.com/cloud-assist/overview) in Cloud Billing provides generative AI-powered assistance to help you analyze your billing data.

## FinOps-focused AI assistance in Cloud Billing

To provide an integrated assistance experience, Gemini Cloud Assist in Cloud Billing is available on the following Billing pages in the Google Cloud console:

  * **Reports**
    * Gemini Cloud Assist in Cost Reports provides insights into your cloud spend to help you create custom reports, identify key trends, and uncover cost drivers.
  * **FinOps hub**
    * Gemini Cloud Assist in Google Cloud FinOps provides insights to help you understand your costs, identify waste, and prioritize cost optimization opportunities.



## AI assistance in Cloud Billing Reports

Gemini Cloud Assist in Cloud Billing Reports provides FinOps-focused AI assistance to create the cost reports you need to analyze your cost trends and to summarize key insights from the cost reports, making it easier to understand your costs.

Gemini Cloud Assist in Cloud Billing Cost Reports provides AI assistance to help you in the following ways:

  * **Using saved reports**. You can select various Google-configured and user-configured cost reports to analyze your cost trends. The saved reports feature updates the previous [_Saved views_](https://docs.cloud.google.com/billing/docs/how-to/reports#saving-views) feature and also replaces the report [_Presets_](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views) with an expanded number of Google-preconfigured reports that are ready to use with a single click.
  * **Creating reports using Gemini assistance**. You can create custom cost reports using natural language prompts.
  * **Summarizing reports**. Gemini Cloud Assist provides summaries of key insights and anomalies from each cost report. The insights might include links that open a new, scoped report, or links that open other pages in the Billing section of the Google Cloud console, such as [Anomalies](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies) or [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub).



### Saved reports

To analyze your cost trends, you can select from various Google-configured and user-configured cost reports:

![Preset and saved reports.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-presets-and-saved-views.png)

Google Cloud offers a range of preconfigured cost reports (formerly known as [_Presets_](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views)) that are ready to use with a single click. These reports address common FinOps cost reporting needs, helping you implement best practices faster. You can scroll through the carousel of preconfigured reports, or click **See all reports** for a comprehensive list.

If you create and save custom cost reports (previously known as [_Saved views_](https://docs.cloud.google.com/billing/docs/how-to/reports#saving-views)), your saved reports are also available for you and your team in the **See all reports** tab.

When you select a preconfigured or saved report, your [report filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) are set based on the saved report settings, and your selected report is shown, along with a report summary. You can further customize the report by manually updating the report [settings and filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping), or by asking Gemini Cloud Assist to find or create a report. You can [save edited and custom-created reports](https://docs.cloud.google.com/billing/docs/how-to/reports#saving-views) to your list of saved reports.

### Configure reports with Gemini Cloud Assist

You can create custom cost reports using natural language prompts:

![Prompt Gemini Cloud Assist for AI assistance to find or create a report.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-gemini-prompt.png)

If the saved reports don't meet your needs, you can describe the report that you want using natural language. Gemini Cloud Assist interprets your request and configures the report [settings and filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filtering_and_grouping) to create the report for you.

#### Write better prompts for reports

When you ask Gemini Cloud Assist in Cloud Billing to find or create a report, include as much context and specific detail as possible when you describe the report you want to view. At a minimum, specify a [time range](https://docs.cloud.google.com/billing/docs/how-to/reports#time-range) and a [group by](https://docs.cloud.google.com/billing/docs/how-to/reports#group-by) when writing a prompt for a report.

  * If you don't explicitly specify the _Time range_ in the prompt, your report settings default to _Current month_.
  * If you don't explicitly specify the _Group by_ option in the prompt, your report settings default to grouping costs by _Service_.



Here are a few example prompts to get you started:

  * `Daily costs and savings by service for the last 5 days`
  * `Invoice costs per SKU for July 2024`
  * `Monthly costs by project for the last 6 months`
  * `Compute Engine spend by SKU in project-name since the beginning of 2024`
  * `Help me understand and optimize my costs by service for the last 30 days`



We recommend starting with a [preconfigured report](https://docs.cloud.google.com/billing/docs/how-to/reports#preset_views) and then prompting for additional filters to focus your cost analysis. When using this method, write the name of the report, followed by the additional [filters](https://docs.cloud.google.com/billing/docs/how-to/reports#filters), as shown in this example:

`SKUs - daily costs this month` for `Compute Engine` in `US regions`

  * `SKUs - daily costs this month` — name of the preconfigured report, which sets the _Time range_ and _Group by_ options.
  * `Compute Engine` — sets the [Services](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-services) filter.
  * `US regions` — sets the [Locations](https://docs.cloud.google.com/billing/docs/how-to/reports#filter-by-locations) filter.



#### Save custom reports to use again

In billing reports, Gemini Cloud Assist helps you create the cost reports that you need to analyze your Google Cloud costs. To reuse a custom report that you created with Gemini Cloud Assist, you can [save the report](https://docs.cloud.google.com/billing/docs/how-to/reports#saving-views). Your saved reports are added to the list of reports available in the **See all reports** tab.

### Report summaries provided by Gemini Cloud Assist

Gemini Cloud Assist summarizes key insights and anomalies from each cost report:

![Example of a report summary provided by Gemini Cloud Assist.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-gemini-summary.png)

The Gemini-assisted report summaries are designed to provide accurate insights. We developed the report insights in partnership with Google's research teams.

Using FinOps-trained models, Gemini Cloud Assist analyzes your cost reports and delivers actionable insights. Depending on your report settings, insights can include a summary of the following:

  * **Overall costs** : total costs for the specified time period, with cost trends (increasing or decreasing).
  * **Cost drivers** : for example, the projects or services responsible for the biggest cost changes, both in terms of absolute amount and percentage, with a direct link to the Anomalies page if unusual spending patterns are detected.
  * **Savings** : how much you've saved through cost optimization, with a direct link to the FinOps hub for further recommendations.
  * **Budgeting** : suggestions to create budgets to track and control spending.



Gemini Cloud Assist provides up to three key insights per report, helping you pinpoint areas for deeper analysis or cost optimization.

## AI assistance in Cloud Billing FinOps hub

Gemini Cloud Assist in the [FinOps hub](https://docs.cloud.google.com/billing/docs/how-to/finops-hub) helps you understand costs, identify waste, and prioritize cost optimization opportunities. Further, on the [Utilization insights dashboard](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights), you can use Gemini Cloud Assist to summarize and send top wasted usage insights to your engineering teams to take action and remediate.

### FinOps hub insights provided by Gemini Cloud Assist

Gemini Cloud Assist provides key optimization and utilization insights from the FinOps hub analysis:

![Example of the FinOps hub insights provided by Gemini Cloud Assist.](https://docs.cloud.google.com/static/billing/docs/images/finops-hub-gemini-insights.png)

Gemini Cloud Assist provides up to three key insights for each FinOps hub page load, helping you pinpoint areas for deeper analysis or cost optimization.

### Draft an email with Gemini-generated insights

On the FinOps [_Utilization insights_](https://docs.cloud.google.com/billing/docs/how-to/finops-utilization-insights) dashboard, you can discover if resources are used efficiently and view high-impact utilization insights based on the potential costs of wasted resources.

Gemini Cloud Assist provides the top three utilization insights.

![Example of the FinOps utilization insights provided by
 Gemini Cloud Assist.](https://docs.cloud.google.com/static/billing/docs/images/finops-utilization-gemini-insights.png)

To help with financial accountability collaboration and data-driven decision making requirements, Gemini Cloud Assist can draft an email report based on the results of the utilization insights and optimization recommendations. You can copy the content of the report to send it in an email, chat, a ticketing system, or any other tool you use.

![Example of an email draft generated by Gemini, with
 utilization insights, identified waste, and optimization recommendations.](https://docs.cloud.google.com/static/billing/docs/images/finops-utilization-email-draft.png)

### Focus on top projects

![Example of the FinOps utilization insights provided by
 Gemini Cloud Assist.](https://docs.cloud.google.com/static/billing/docs/images/finops-utilization-insights-gemini.png)

If you have more than 10 projects in your billing account with utilization insights, you can select filter_list **Focus on the top projects** to filter the utilization insights by the projects with the highest amount of potential cost savings.

## How to interact with Gemini Cloud Assist in Cloud Billing

In Cloud Billing, you can find Gemini-provided assistance in the following places:

  * Cloud Billing:

    * On the **Reports** page, to help you create cost reports and summarize the top insights of the report results.
    * On the **FinOps hub** and **Utilization insights** pages, to provide a summary of the top optimization insights and help you draft email reports to stakeholders.
    * In the [AI Cost Summary Agent](https://docs.cloud.google.com/billing/docs/how-to/gemini/ai-cost-summary) on the **Billing Overview** page, to gain critical insights into your AI-related spend.
    * On the [**Anomalies** page](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies) using an AI-powered algorithm to detect cost anomalies in your projects, including [early anomaly signals for AI workloads](https://docs.cloud.google.com/billing/docs/how-to/manage-anomalies#view-early-anomalies).
  * Google Cloud console, including Cloud Billing pages, using the **Gemini Cloud Assist** chat panel.




### Cloud Billing: Reports page

To access the AI features in your Cloud Billing reports, open your Cloud Billing account and view the **Reports** page.

  1. In the Google Cloud console, go to the Billing **Reports** page.

[Go to Reports](https://console.cloud.google.com/billing/reports)

  2. If prompted, select the Cloud Billing account you want to view.

  3. Use the Gemini Cloud Assist features to interact with the Cloud Billing report.

On the **Reports** page, you see the Gemini Cloud Assist in Cloud Billing features.

![Gemini Cloud Assist in Cloud Billing features are enabled for use in billing reports.](https://docs.cloud.google.com/static/billing/docs/images/billing-reports-gemini-enabled.png)




### Cloud Billing: FinOps hub

To access the AI features in your Cloud Billing FinOps hub, open your Cloud Billing account and view the **FinOps hub** page.

  1. In the Google Cloud console, go to the Billing **FinOps hub** page.

[Go to FinOps hub](https://console.cloud.google.com/billing/optimize)

  2. If prompted, select the Cloud Billing account you want to view.

  3. Use the Gemini Cloud Assist features to interact with the FinOps hub.

When you're viewing the **FinOps hub** page, you see the Gemini Cloud Assist insights in the _Optimization summary_ widget:

![Gemini Cloud Assist in Cloud Billing features are enabled for use in the FinOps hub.](https://docs.cloud.google.com/static/billing/docs/images/finops-hub-gemini-enabled.png)




### Chat in the Gemini Cloud Assist panel in Google Cloud console

You can access AI-powered assistance in the [**Cloud Assist** panel](https://docs.cloud.google.com/cloud-assist/chat-panel) available from any page in the Google Cloud console.

The **Cloud Assist** panel is a conversational assistant that lets you write natural language statements or questions (called _prompts_) to get explanations, suggested actions, or guided workflows that help you complete tasks quickly and efficiently. Beyond general Google Cloud knowledge, the conversational assistant understands context, like your current project and console page.

**Note:** The **Cloud Assist** panel isn't designed to answer questions about product prices or specific Google Cloud cost information. To analyze your Google Cloud costs, use the [tools available in Cloud Billing](https://docs.cloud.google.com/billing/docs/concepts#intro-tools).

To use the **Cloud Assist** panel, do the following:

  1. In the Google Cloud console toolbar, click spark **Open or close Gemini Cloud Assist chat**.
  2. In the **Cloud Assist** panel, enter your prompt—for example, `How can I optimize my costs?`.
  3. Click send **Send prompt**.



#### Billing data limitations in the **Cloud Assist** panel

In Cloud Billing, the Gemini conversational assistant provides _general_ answers to your billing questions, but it doesn't return product pricing or specific Google Cloud cost information. DevOps and FinOps practitioners who want to use Gemini Cloud Assist to understand cloud costs, identify opportunities for cost savings, and get AI insights to maximize cloud resource utilization and performance can use the Gemini-assisted Cloud Billing tools available in the following Billing pages:

  * **Cost Reports** : For assistance in finding or creating a billing report to gain insights into your Google Cloud spending, identify key trends, and uncover what's driving your Cloud Billing costs, use the Gemini Cloud Assist prompt available on the Cloud Billing **Reports** page.
  * **FinOps hub** : For cost optimization insights and recommendations, see the Gemini-generated insights on the **FinOps hub**.



Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## What's next

  * Learn more about the different [types of generative AI assistance available in Google Cloud](https://docs.cloud.google.com/gemini/docs/overview).
  * Learn [how Gemini Cloud Assist uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).
  * Learn more about [Google Cloud compliance](https://cloud.google.com/security/compliance).



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-13 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-13 UTC."],[],[]] 
