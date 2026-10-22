---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview/
title: Agentic workflows overview \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:45.936230+00:00
---

# Agentic workflows overview  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-agentic-workflows-overview/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Agentic workflows overview Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Agentic workflows let you prompt a data agent to generate dynamic notifications about your data from within the Conversational Analytics chat interface. Instead of manually building complex [alerts](https://docs.cloud.google.com/looker/docs/alerts) or [schedules](https://docs.cloud.google.com/looker/docs/scheduling-overview), you can use natural language in a direct chat with an Explore or within a conversation with a data agent to set up threshold-based monitoring of the [measures](https://docs.cloud.google.com/looker/docs/glossary#measure) in the conversation's data source or set up recurring deliveries of data.

When you prompt Conversational Analytics to [create a _triggered_ agentic workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows), you can specify the conditions of the workflow, which are checked at a frequency that you specify. When these conditions are met, the workflow triggers a notification to the recipients that you specify using the method that you specify. You can also specify whether you want the workflow notification to include results from Gemini-powered **Key driver analysis** , which provides insight about why the change that triggered your workflow occurred.

When you prompt Conversational Analytics to create a _scheduled_ agentic workflow, you can set up a data delivery that reaches the recipients that you specify, the method of delivery, and the frequency of the delivery. You can also specify whether you want the delivery to include results from Gemini-powered **Key driver analysis** , which provides insight about why the change in your data occurred.

## Initiate an agentic workflow

**Caution:** Avoid entering sensitive confidential information or personally identifiable information (PII) into prompts. 

You can create an agentic workflow while chatting directly with [Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents), [dashboard data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards), or in a [direct chat with an Explore](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-conversation-single-explore). You can create either a [triggered workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows) (based on threshold conditions) or a [scheduled workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-scheduled-agentic-workflows) (recurring deliveries).

The workflow creation experience is consistent across the Looker UI, [embedded Conversational Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-embedding) content, and the [Looker mobile app](https://docs.cloud.google.com/looker/docs/looker-core-mobile-app). You can also create and manage workflows programmatically using the [Looker API](https://docs.cloud.google.com/looker/docs/api-intro) and the [Conversational Analytics API](https://docs.cloud.google.com/gemini/data-agents/conversational-analytics-api/overview).

You can initiate workflow creation in any of the following ways:

  * **Natural language prompts** : Enter a prompt in the Conversational Analytics chat box to create a triggered or scheduled workflow. For example: 
    * `Notify me when metric [X] goes above [Y]`
    * `Create a workflow to generate a sales insights report every day at 9 a.m.`
  * **Workflow icon** : Select the **Workflow** icon in the chat interface.
  * **Zero-state prompts** : Select the suggested starter prompt that is displayed in a new Conversational Analytics chat window.



When you initiate a workflow, Conversational Analytics automatically inherits the active filters, metrics, dimensions, and the underlying Explore query of the active session. If your prompt explicitly declares a different measure or time range than the active session, the agent overrides the inherited session context with the parameters that you specified in your prompt.

**Caution:** Sensitive business data may be revealed in generated reports. Looker access controls don't apply to external destinations. When sharing externally (such as through Slack or email), the customer and external destination are solely responsible for controlling access to content. 

## List of documentation

To learn more about creating and managing agentic workflows, see the following documentation:

  * [Create a triggered agentic workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows)
  * [Create a scheduled agentic workflow](https://docs.cloud.google.com/looker/docs/conversational-analytics-scheduled-agentic-workflows)
  * [Admin settings – Workflows](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflows)
  * [Admin settings – Workflow Executions](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflow-executions)
  * [Manage your agentic workflows](https://docs.cloud.google.com/looker/docs/user-workflows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
