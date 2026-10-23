---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows/
title: Create a triggered agentic workflow \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-23T10:35:54.152013+00:00
---

# Create a triggered agentic workflow  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-triggered-agentic-workflows/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Create a triggered agentic workflow Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

**Note:** This feature is in preview with limited support. We encourage you to share your feedback to help us improve. To report bugs or issues, reach out to [looker-workflows-fb@google.com](mailto:looker-workflows-fb@google.com) and include the following details: 

  * A clear description of the problem and the expected behavior
  * Steps to reproduce the issue
  * Any additional relevant details



You can use Conversational Analytics to generate a triggered agentic workflow with an [Explore data agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation), [dashboard agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards), or within a Conversational Analytics [direct chat with an Explore](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-conversation-single-explore).

Workflows can deliver notifications to Slack and email in accordance with [Looker email domain allowlists](https://docs.cloud.google.com/looker/docs/admin-panel-general-settings#email_domain_allowlist_for_scheduled_content).

**Warning:** Workflows that were created on an instance running a version of Looker that is earlier than 26.14 will need to be recreated. Use the [Manage workflows](https://docs.cloud.google.com/looker/docs/user-workflows) user page to manage your legacy workflows.

## What data can you monitor?

You can use Conversational Analytics to generate a triggered agentic workflow that monitors any [measures](https://docs.cloud.google.com/looker/docs/glossary#measure) in the conversation's data source. For [Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-a-conversation), you can monitor any measures in any of the Explores that are being used by that data agent. For [dashboard agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards), you can monitor any measures in any of the query-based tiles on the dashboard. For a Conversational Analytics [direct chat with an Explore](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data#start-conversation-single-explore), you can monitor any measures in that Explore.

## Before you begin

Before you can use Conversational Analytics to generate a triggered agentic workflow, you must fulfill the following requirements.

### Required permissions

To prompt Conversational Analytics to generate a workflow, a Looker admin must grant you a role that contains the `create_alerts` permission for at least one underlying model of the Conversational Analytics data source. You must also have both the `gemini_in_looker` and `chat_with_agent` permissions enabled for this model.

For more information about Conversational Analytics permissions, see the [Set up Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) documentation page.

### Required authentication

Before you can send workflow notifications to Slack, a Looker admin must enable and configure the Slack action in the [Looker Action Hub](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions) for your Slack workspace. To enable installation of the Looker app, your Slack workspace owner may need to [adjust the app installation settings](https://slack.com/help/articles/222386767-Manage-app-installation-settings-for-your-workspace) for your Slack workspace.

After Slack is enabled, you must authenticate into Slack, either from your [Looker user profile's **Account** page](https://docs.cloud.google.com/looker/docs/scheduling-slack#authenticating_into_a_slack_workspace_from_the_account_page) or from within the Conversational Analytics conversation. If your Looker admin has connected multiple Slack workspaces to your Looker instance, you'll see a list of workspaces with options to sign in to each one individually.

## Prompt Conversational Analytics to generate the workflow

**Caution:** Avoid entering sensitive confidential information or personally identifiable information (PII) into prompts. 

To prompt Conversational Analytics to generate a triggered workflow, follow these steps:

  1. Ask a question to establish your data's key metrics.
  2. Select automation **Workflows** or prompt Conversational Analytics to generate a workflow that looks for changes to one of your data source's [measures](https://docs.cloud.google.com/looker/docs/glossary#measure). Use keywords like "alert," "monitor," and "notify." For example: 
     * "Create an alert workflow"
     * "Create a workflow to monitor measure X"
     * "Create a workflow to notify me"



Conversational analytics will clarify the remaining components of the workflow until you have established all workflow settings, which include the following:

  * **Model** : The underlying model that is being queried.
  * **Explore** : The data source for the conversation.
  * **Metric** : The measure that is to be monitored.
  * **Condition** : The change that the selected measure must undergo to trigger the workflow notification, including the magnitude or threshold of the change.
  * **Destination** :  The destination of the workflow notification. Options include email, Slack, and the [Looker mobile app](https://docs.cloud.google.com/looker/docs/mobile-app-alerts) (to use the mobile app, a Looker admin must [enable the Firebase action in the Looker Action Hub](https://docs.cloud.google.com/looker/docs/admin-panel-platform-actions)). 
    * For email destinations, list the email addresses of users whom you want to receive the workflow notification in the **Recipients** field. Although there is no limit to the number of recipients that you can notify, if your organization is using an external SMTP server, the server may have its own daily or per-message recipient limits.
    * For notifications to Slack, if you have not already authenticated into Slack, you must authenticate from your user profile. When prompted in the conversation, enter the workspace ID and the user ID or channel ID for where you would like to send your workflow notifications. For notifications to Slack channels, the notification is visible to everyone in the channel.
    * Looker access controls don't apply to external destinations. When sharing externally (such as through Slack or email), the customer and external destination are solely responsible for controlling access to content.
  * **Frequency** : You can set the frequency at which Looker checks your data for changes (and sends a notification if the workflow conditions are met). The default frequency is **Weekly** on Mondays at **09:00**. You can prompt the agent to adjust the frequency as needed. The available frequency options are as follows:

    * **Monthly** on a specified **Day** of the month (the default is the **1st** of the month) at a specified **Time** (the default is **05:00**).
    * **Weekly** on a specified **Day** of the week (the default is **Sun** for Sunday) at a specified **Time** (the default is **05:00**).
    * **Daily** at a specified **Time** (the default is **05:00**).
    * **Hourly** at a specified interval (the default is to check the data every hour) with specified **Start** and **End** times (the default is **05:00** and **18:00**). With hourly intervals you can have Looker check the data at these intervals: 
      * **Hour**
      * **2 hours**
      * **3 hours**
      * **4 hours**
      * **6 hours**
      * **8 hours**
      * **12 hours**
    * **Minutes** at a specified interval (the default is to check the data every 15 minutes) with specified **Start** and **End** times (the default is **05:00** and **17:00**). With minute-based intervals, you can have Looker check the data at these intervals: 
      * **15 minutes**
      * **30 minutes**

**Start** and **End** times are inclusive. For example, if you set **Check every** to **12 hours** with a **Start** time of **05:00** and an **End** time of **17:00** , Looker will check the data at 05:00 _and_ 17:00.

**Note:** Looker sends alerts according to the time zone that is indicated in the [**Application Time Zone**](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#application_time_zone) setting on the Admin **Settings** page, or, if enabled, the alert creator's [User Specific Time Zone](https://docs.cloud.google.com/looker/docs/using-time-zone-settings#user_specific_time_zones).
  * Gemini-powered **Key driver analysis** : If this setting is enabled, the workflow notification provides insight about the change in your data that triggered the workflow, and why that change may have occurred. This option is disabled by default. Insights delivered over email and Slack messages include the header: "Powered by Gemini. Verify as AI can make mistakes."




## Agentic workflow notifications

Agentic workflow notifications include the following information:

  * A PNG image of the workflow visualization.
  * A message with the name of the workflow and the conditions that triggered the workflow.
  * A link to investigate the workflow — select this link to open a new conversation with the agent that generated the workflow.
  * A link to unsubscribe from the workflow notification.
  * If enabled, the insights provided by Gemini-powered **Key driver analysis**. Insights delivered over email and Slack messages include the header: "Powered by Gemini. Verify as AI can make mistakes."

**Note:** For [single value visualizations](https://docs.cloud.google.com/looker/docs/single-value-options), the notification will include the single value as text, rather than a PNG of the visualization.

**Caution:** Sensitive business data may be revealed in generated reports. Looker access controls don't apply to external destinations. When sharing externally (such as through Slack or email), the customer and external destination are solely responsible for controlling access to content. 

## Investigate workflow notifications

When you receive a workflow notification by email or in Slack, you can select the **Investigate** link in the notification message to ask follow-up questions and explore the data that triggered the workflow.

When you investigate a workflow notification, Conversational Analytics initiates an investigation session with the following behaviors:

  * **Private and isolated conversations** : Each recipient who selects **Investigate** receives their own dedicated, private conversation thread with the primary data agent where the workflow originated. Other recipients, including members of email distribution lists, can't see your questions or analysis.
  * **Persistent conversation history** : Your investigation conversation is persistent. If you leave the conversation and select the **Investigate** link in the notification again later, Conversational Analytics returns you to your existing conversation history for that specific workflow run.
  * **Primary agent routing** : The investigation conversation automatically opens on the primary agent that generated the workflow. If the agent is deleted and the associated Explores can't be identified, an error appears.
  * **Access control and data permissions** : You must have access to the underlying Explores associated with the conversation. If you don't have access to any of the associated Explores, an error message appears informing you that you lack the required data permissions to investigate the insight.



## Limitations of triggered workflows

The following limitations apply when you use Conversational Analytics to generate a triggered agentic workflow:

  * Conversational analytics is not able to generate workflows to monitor the more complex custom metrics that are produced with the use of [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics).
  * Conversational analytics is not able to generate workflows to monitor data [dimensions](https://docs.cloud.google.com/looker/docs/glossary#dimension) or [table calculations](https://docs.cloud.google.com/looker/docs/glossary#table-calc).
  * Conversational analytics dashboard agents can't generate workflows for embed users.



## View your triggered workflows

When a Looker admin grants you the `see_alerts` permission, you can view the workflows that you own on the [**Manage Workflows** user page](https://docs.cloud.google.com/looker/docs/user-workflows) and all workflows for the Looker instance on the [**Manage Workflows** admin page](https://docs.cloud.google.com/looker/docs/admin-panel-alerts-and-schedules-workflows).

## Related resources

  * [Conversational analytics overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)
  * [Manage your agentic workflows](https://docs.cloud.google.com/looker/docs/user-workflows)



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-22 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-22 UTC."],[],[]] 
