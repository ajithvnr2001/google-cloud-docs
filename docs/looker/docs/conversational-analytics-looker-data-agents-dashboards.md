---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards/
title: Query a user-defined dashboard with a dashboard agent \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-13T17:33:39.786074+00:00
---

# Query a user-defined dashboard with a dashboard agent  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Query a user-defined dashboard with a dashboard agent Stay organized with collections  Save and categorize content based on your preferences. 

**Preview**

This product or feature is subject to the "Pre-GA Offerings Terms" in the General Service Terms section of the [Service Specific Terms](https://docs.cloud.google.com/terms/service-terms#1). Pre-GA products and features are available "as is" and might have limited support. For more information, see the [launch stage descriptions](https://cloud.google.com/products/#product-launch-stages). 

Conversational Analytics, powered by [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview), lets you investigate your data by asking questions about it in conversational language through an intuitive chat interface. When you use Conversational Analytics with a [user-defined dashboard](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards), Conversational Analytics creates a data agent for you that is connected to the dashboard. As you converse with the dashboard agent, the agent will query your dashboard and any of its [query-linked tiles](https://docs.cloud.google.com/looker/docs/viewing-dashboards#dashboard_tiles). You can customize user-defined dashboard agents with context and instructions that are specific to your dashboard data.

**Note:** This page describes dashboard agents for user-defined dashboards. For information about configuring and managing data agents for LookML dashboards, see the [Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards) [[Preview](https://cloud.google.com/products#product-launch-stages)] documentation page. For information about Explore data agents — data agents that query Explores, see the [Query an Explore in natural language](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data) documentation page. For information about creating Explore data agents, see the [Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents) documentation page.

This page discusses how to use Conversational Analytics to engage with user-defined dashboard data. It covers the following topics:

  * Starting a conversation from within a dashboard
  * Adding agent instructions and context
  * Asking questions about your dashboard data
  * Managing conversations



## Before you begin

Before you can use Conversational Analytics to engage with your dashboard data, make sure that the [setup and requirements for your Looker instance](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#setup-and-requirements) have been satisfied and that you have been granted the [appropriate permissions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) to perform the tasks that are described on this page.

## Start a conversation from within a Looker dashboard

To start a conversation with a dashboard agent from within a [user-defined dashboard](https://docs.cloud.google.com/looker/docs/editing-user-defined-dashboards), select spark **Chat with this dashboard**.

If you don't have sufficient permissions to chat with the dashboard, Looker displays an error.

Once you have created a conversation, you can ask questions about the data in the send_spark **Ask a question** field within the conversation. To access your recent conversations with the dashboard agent, select more_vert **Menu** > **Recent conversations**.

In addition to asking your dashboard agent questions about the data on the dashboard or its query-linked tiles, for user-defined dashboard agents, you can customize the agent's configuration with additional context and instructions.

### Enable or disable dashboard agents for a dashboard

If dashboard agents are enabled for your instance, they're enabled for all user-defined dashboards by default. However, dashboard creators can control whether users can chat with a specific user-defined dashboard by enabling or disabling the dashboard agent setting at the individual dashboard level.

To turn a dashboard agent on or off for a user-defined dashboard, follow these steps:

  1. Select the more_vert **Dashboard actions** menu icon and then select edit **Edit dashboard**.
  2. Click settings **Settings** in the dashboard toolbar.
  3. In the **Settings** dialog, select the **General** tab.
  4. Turn on or turn off the **Enable chat with dashboard** control.
  5. Click **Save** to save your changes to the dashboard.



### Conversation metadata

The **Chat with this dashboard** pane supports the following tasks for user-defined dashboards:

  * To ask a question about the dashboard data, enter a question in the **Ask a question** field.
  * To edit information about the dashboard agent, select tune **Manage agent**. In the **Editor** tab, you can enter [agent instructions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#write-agent-instructions) and expand **Advanced options** to configure settings like **Show thinking** and **Show debug info**. Select **Update** to save your changes to the dashboard agent. Use the **Preview** tab to preview your changes to the dashboard agent.
  * To expand the dashboard agent conversation pane, select open_in_full **View full screen**.
  * To access your recent conversations with the dashboard agent, select more_vert **Menu** > **Recent conversations**.
  * By default, conversations will be named based on your initial question. To rename a conversation, select a conversation from the **Recent conversations** menu option, select more_vert, and then select edit **Rename**.
  * To delete a conversation with a data agent, select more_vert **Menu** > delete **Trash**.



## Modify your dashboard agent

To edit information about the dashboard agent, select tune **Manage agent**.

Optionally, you can expand **Advanced options** in the **Editor** tab to configure the following settings:

  * **Enable Advanced Analytics** : Turn on this setting to allow your agent to use [**Advanced Analytics**](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics), which translates your natural language questions into Python code and executes that code to provide advanced analysis and visualizations. This setting is visible only when the **Advanced Analytics** admin setting is enabled on the **Gemini in Looker** admin page for your instance.
  * **Show thinking** : Turn on this toggle to allow the agent to display its reasoning steps, generated Looker queries, and underlying data tables in all responses in each conversation.
  * **Show debug info** : Turn on this toggle to allow the agent to display the steps that it executed for all responses in each conversation.



Select **Update** to save your changes to the dashboard agent. Use the **Preview** tab to preview your changes to the dashboard agent.

### Write agent instructions

**Note:** [Verified queries](https://docs.cloud.google.com/looker/docs/glossary#verified_query) aren't supported for agents on user-defined dashboards.

You can add free-form instructions that define your data agent's core behavior and provide it with foundational context to consider before processing a user's prompt.

**Important:** Although the **Instructions** field is optional and the structure is up to your discretion, we recommend that you provide well-structured instructions to enable the agent to give more accurate and relevant responses.

Here are some examples of the types of context that you can provide in the **Instructions** field:

  * Key fields: The most important fields for analysis
  * Excluded fields: Fields that the data agent should avoid
  * Filtering and grouping: Fields that the agent should use to filter and group data
  * Persona: A role or expertise, character, or tone that you assign to the agent



For tips and best practices for writing agent instructions, see the [Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices) documentation page.

## Ask questions about Looker data

When you're beginning a new conversation, Conversational Analytics suggests some starting questions to ask. The questions don't need to be in a specific format or use a specific syntax. However, they do need to relate to the Explore that you've selected.

Type your question in natural language into the **Ask a question** field. Select a question mode and click send. After you submit your query, you can cancel Conversational Analytics' response by clicking stop **Stop response**. Conversational Analytics stops running the query and displays the following message: `The query was cancelled.`

For more guidance on the types of questions that you can ask, see [Limitations on questions](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations-on-questions).

### Select a question mode

When you ask a question, you can select the question mode from a drop-down menu that contains the following options:

  * **Fast** (default): Best for most questions.
  * **Thinking**: Detailed reasoning.



Conversational Analytics defaults to **Fast** question mode. Conversational Analytics will maintain the same question mode throughout any multi-turn conversations, unless you manually change it.

#### Fast mode

**Fast** mode is recommended for most questions and is selected by default. In **Fast** mode, Conversational Analytics maps your natural language query directly to the LookML parameters that are defined in the LookML models that underlie your conversation's dashboard or Explores. Conversational Analytics responds quickly without spending extra tokens on thinking or streaming thoughts summaries in the chat.

Queries in **Fast** mode provide the same level of accuracy as queries in **Thinking** mode. Use **Fast** mode for your questions unless you specifically want to see the agent's reasoning process.

#### Thinking mode

In **Thinking** mode, the agent spends additional tokens thinking through the request and streams a thoughts summary directly in the chat while processing your query, giving you visibility into the agent's detailed reasoning steps.

Although **Thinking** mode doesn't produce more accurate answers than **Fast** mode, displaying the agent's reasoning lets you observe how Conversational Analytics interprets your query, plans its analytical steps, and references the underlying LookML models.

Select **Thinking** mode if you want to inspect the agent's detailed reasoning steps or test how an agent interacts with your data sources, and you want to spend the additional tokens required for thinking.

### Multi-turn conversations

Conversational Analytics will take previous questions and answers into account as you continue the conversation. You can take previous answers and build on them by further refining results or changing the visualization type.

**Important:** You can only reference previous questions in answers from the active conversation. You cannot reference previous questions and answers from other conversations.

For more guidance on creating questions, see [Limitations on questions](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations-on-questions).

## Manage queries within a conversation

When you converse with data, you can manage the conversation by stopping an active query response while it is running or by deleting the most recent question and its response.

### Delete the most recent question

To delete the most recent question and its response, follow these steps:

  1. Hold your cursor over the most recent question, and then click delete **Delete message**.
  2. In the **Permanently delete message?** dialog, click **Delete** to permanently delete the question and its response.



## Understand query results and calculations

Conversational Analytics provides the following parameters for understanding query results and calculations:

  * Details about how your query was interpreted
  * Details about how the answer was calculated
  * Additional details, such as analytical details and debug info, if enabled for the agent



### Determine how your query was interpreted

If you use **Thinking** mode to ask your question, you can see how Conversational Analytics reasoned through your query. To see its reasoning, expand the **Show thinking** option. To hide its reasoning, click **Hide thinking**.

Conversational Analytics analyzes each query and thinks about how to respond, using the keywords from your query to infer the relevant dimensions, measures, and other parameters from the semantic layer of the conversation's associated datasets and interpreting from your query what aggregations may need to be performed. When you expand **Show reasoning** , Conversational Analytics displays a plain text explanation of the steps that it took to interpret your query. The explanation also includes the duration that Conversational Analytics thought about the query.

### Determine how an answer was calculated

To see how Conversational Analytics arrived at an answer or created a visualization, click keyboard_arrow_down **How was this calculated?** within the query results.

When you click **How was this calculated?** , Conversational Analytics displays a **Text** section. The **Text** section provides a plain text explanation of the steps that were taken by Conversational Analytics to arrive at the given answer. This explanation includes the raw field names that were used, the calculations that were done, the filters that were applied, the sort order, and other details.

### Analytical details and debug info

If the data agent that's used for the conversation has specific advanced options enabled, responses can contain the following details:

  * **Show thinking** : If enabled, the agent's response displays its reasoning steps, generated Looker queries, and underlying data tables.
  * **Show debug info** : If enabled, the agent's response displays the steps that were executed by the agent for that response, which can help with troubleshooting.



These settings are configured in the advanced options when modifying the dashboard agent.

## Manage conversations

Each conversation remains in the **Recent conversations** section the dashboard conversation more_vert **Menu**. You can change the names of conversations, delete conversations, or restore them from the trash folder.

  * To access your recent conversations with the dashboard agent, select more_vert **Menu** > **Recent conversations**.
  * By default, conversations will be named based on your initial question. To rename a conversation, select a conversation from the **Recent conversations** menu option, select more_vert, and then select edit **Rename**.
  * To delete a conversation with a data agent, select more_vert **Menu** > delete **Trash**.



### Delete a conversation

To delete a conversation with a data agent, select the conversation's more_vert three-dot menu, and then select delete **Delete**.

**Note:** Conversations that remain in the trash for more than 30 days are automatically deleted.

### Restore or permanently delete a conversation

To restore or permanently delete a conversation from the trash, follow these steps:

  1. Select more_vert **Menu** > delete **Trash**.
  2. In the **Trash** pane, find the conversation that you want to restore or permanently delete. Select the conversation's more_vert three-dot menu, and then select one of the following options: 
     * **Restore** : Restores the conversation. The conversation can be accessed from the schedule **Recent conversations** menu option.
     * **Delete Permanently** : Permanently deletes the conversation.



## Related resources

  * **[Conversational Analytics in Looker overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)** : The landing page for Conversational Analytics with a list of key features links to all Conversational Analytics documentation.

  * **[Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards)** [[Preview](https://cloud.google.com/products#product-launch-stages)]: Use LookML to configure and manage version-controlled data agents for LookML dashboards.

  * **[Query an Explore in natural language](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data)** : Start a conversation with a Looker Explore to ask about Explore data using natural language.

  * **[Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents)** : With Explore data agents, you can customize the AI-powered data querying agent by providing context and instructions that are specific to your Explore data, which helps Conversational Analytics generate more accurate and contextually relevant responses.

  * **[Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices)** : Strategies and best practices to help Looker administrators and LookML developers successfully configure and optimize Conversational Analytics.




Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-09 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-09 UTC."],[],[]] 
