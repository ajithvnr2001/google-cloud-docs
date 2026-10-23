---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-scheduled-agentic-workflows/
title: Create a scheduled agentic workflow \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:54.396660+00:00
---

# Create a scheduled agentic workflow  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-scheduled-agentic-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create a scheduled agentic workflow Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [looker-workflows-fb@google.com](mailto:looker-workflows-fb@google.com) and include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



You can use Conversational Analytics to generate a scheduled agentic workflow with an [Explore data agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation), [dashboard agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards), or within a Conversational Analytics [direct chat with an Explore](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-conversation-single-explore).

A scheduled workflow delivers data reports and natural language insights to designated recipients at specified intervals without requiring a threshold trigger condition. Workflows can deliver notifications to Slack and email in accordance with [Looker email domain allowlists](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content).

## Before you begin

Before you can use Conversational Analytics to generate a scheduled agentic workflow, you must fulfill the following requirements.

## Required permissions

To create a scheduled agentic workflow, a Looker admin must grant you the `chat_with_agent` permission for at least one [model](https://docs.cloud.google.com/looker/docs/glossary#model) that underlies the dashboard, Explore data agent, or Explore that is used in the conversation.

For more information about Conversational Analytics permissions, see the [Set up Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) documentation page.

## Scheduling frequency

**Caution:** Avoid entering sensitive confidential information or personally identifiable information (PII) into prompts. 

When configuring a scheduled workflow, you can set the delivery schedule using standard Looker evaluation frequencies, including the following:

  * **Minutes** : Run every specified number of minutes. Minute-level configurations are limited to a maximum frequency of **15 minutes**. If you specify an interval shorter than 15 minutes, Conversational Analytics adjusts the schedule to 15 minutes and notes the adjustment in the workflow plan summary table.
  * **Hourly** : Run at specified intervals throughout the day.
  * **Daily** : Run once each day at a designated time.
  * **Weekly** : Run on specified days of the week.
  * **Monthly** : Run on a specific day of the month.
  * **Custom days** : Run on specific, selected days of the week or month.



## Delivery methods and message content

**Caution:** Looker access controls don't apply to external destinations. When sharing externally (such as through Slack or email), the customer and external destination are solely responsible for controlling access to content. 

You can configure scheduled workflows to deliver reports to **Email** or **Slack** :

  * **Header disclaimer** : For insights delivered over email and Slack messages, the header to reports, emails, and messages is "Powered by Gemini. Verify as AI can make mistakes."
  * **Natural language narrative summary** : The body of the email or the text block of the Slack message renders an AI-generated natural language summary generated directly from the execution of your prompt and instructions.
  * **Data tables** : Deliveries include a clean, readable data table presenting the underlying query results. Multiple data blocks are rendered in separate blocks.
  * **Embedded visual charts** : Visual charts and graphs generated by the agent can be rendered and embedded directly into the email body or Slack message blocks.



### Slack delivery limits

When delivering scheduled workflows to Slack channels or direct messages, the following limits apply:

  * **Narrative character limit** : The AI narrative summary is delivered in a single text block capped at **3,000 characters**. If the narrative exceeds 3,000 characters, Conversational Analytics truncates the text.
  * **Table capping** : Native data tables in Slack are limited to a maximum of **100 rows** and **10 columns**. If the dataset exceeds either limit, the system renders only the top 100 rows or top 10 columns.
  * **Truncation notice** : If a message or data table is truncated due to Slack limits, the message displays the following notice: > _This insight has been truncated due to Slack limits. Click Investigate below to view the full analysis and dataset_



## PDF report generation

When you select the **PDF** option for a scheduled workflow, Conversational Analytics compiles and generates a high-fidelity PDF report artifact:

  * **Combined content** : The PDF combines the agent's natural language insights summaries with the corresponding visualizations (charts and graphs) according to the presentation formatting defined in the workflow instructions.
  * **Delivery** : The generated PDF is attached directly to the delivery email or uploaded as a file attachment within the designated Slack channel or direct message.

**Caution:** Sensitive business data may be revealed in generated reports. Looker access controls don't apply to external destinations. When sharing externally (such as through Slack or email), the customer and external destination are solely responsible for controlling access to content. 

## Investigate workflow notifications

When you receive a workflow delivery by email or in Slack, you can select the **Investigate** link in the notification message to ask follow-up questions and explore the data in Conversational Analytics.

When you investigate a workflow delivery, Conversational Analytics initiates an investigation session with the following behaviors:

  * **Private and isolated conversations** : Each recipient who selects **Investigate** receives their own dedicated, private conversation thread with the primary data agent where the workflow originated. Other recipients, including members of email distribution lists or shared Slack channels, can't see your questions or analysis.
  * **Persistent conversation history** : Your investigation conversation is persistent. If you leave the conversation and select the **Investigate** link in the notification again later, Conversational Analytics returns you to your existing conversation history for that specific workflow run.
  * **Primary agent routing** : The investigation conversation automatically opens on the primary agent that generated the workflow. If the agent is deleted and the associated Explores can't be identified, an error appears.
  * **Access control and data permissions** : You must have access to the underlying Explores associated with the conversation. If you don't have access to any of the associated Explores, an error message appears informing you that you lack the required data permissions to investigate the insight.



## Related resources

  * [Agentic workflows overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview)
  * [Create a triggered agentic workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows)
  * [Admin settings – Workflows](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflows)
  * [Admin settings – Workflow Executions](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflow-executions)
  * [Manage your agentic workflows](https://docs.cloud.google.com/looker/docs/user-workflows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
