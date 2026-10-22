---
url: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data/
title: Query an Explore in natural language \u00a0|\u00a0 Looker \u00a0|\u00a0 Google Cloud Documentation
method: scrapling+scrapegraph
fetched_at: 2026-10-21T14:56:42.870088+00:00
---

# Query an Explore in natural language  |  Looker  |  Google Cloud Documentation

> Source: https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data/

  * [ Home ](https://docs.cloud.google.com/)
  * [ Documentation ](https://docs.cloud.google.com/docs)
  * [ Data analytics ](https://docs.cloud.google.com/docs/data)
  * [ Looker ](https://docs.cloud.google.com/looker/docs)
  * [ Guides ](https://docs.cloud.google.com/looker/docs/intro)



Send feedback 

#  Query an Explore in natural language Stay organized with collections  Save and categorize content based on your preferences. 

Conversational analytics, powered by [Gemini for Google Cloud](https://docs.cloud.google.com/gemini/docs/overview), lets you investigate your data by asking questions about it in conversational language through an intuitive chat interface. Conversational analytics provides multiple ways to "converse" with your data. When using Conversational Analytics with Explore data, you can ask questions about a single Explore in a conversation or create an Explore data agent to chat with as many as five Explores at once. You can also use Explore data agents that other users have created and shared with you.

**Note:** This page refers to Explore data agents — data agents that query Explores. For information about data agents that query user-defined and LookML dashboards, see the [Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) and [Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards) documentation pages, respectively.

This page discusses how to use Conversational Analytics to engage with Explore data. It covers the following topics:

  * Starting a conversation with a single Explore
  * Start a conversation with an existing data agent that queries Explores
  * Asking questions about your data
  * Managing queries within a conversation
  * Understanding query results and calculations
  * Managing conversations



Learn [how and when Gemini for Google Cloud uses your data](https://docs.cloud.google.com/gemini/docs/discover/data-governance).

As an early-stage technology, Gemini for Google Cloud products can generate output that seems plausible but is factually incorrect. We recommend that you validate all output from Gemini for Google Cloud products before you use it. For more information, see [Gemini for Google Cloud and responsible AI](https://docs.cloud.google.com/gemini/docs/discover/responsible-ai).

## Before you begin

Before you can use Conversational Analytics to engage with your Explore data, make sure that the [setup and requirements for your Looker instance](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#setup-and-requirements) have been satisfied and that you have been granted the [appropriate permissions](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-setup#required-permissions) to perform the tasks that are described on this page.

## Start a conversation with a single Explore

To start a conversation — a discrete set of questions and answers about your data in regular, natural language in a chat interface — with a single Explore, follow these steps:

  1. Navigate to the Conversational Analytics interface.

     * From the [main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content): Select ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg)**Conversations**. Select the **Explores** tab and then select the Explore that you want to query.
     * From the [**Create** menu](https://docs.cloud.google.com/docs/finding-content#using_the_main_navigation_menu): Select ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg)**Conversation**. Select the **Explores** tab and then select the Explore that you want to query.
     * From a [Looker Explore](https://docs.cloud.google.com/looker/docs/creating-and-editing-explores#explores_are_the_starting_point_for_exploration): Select **Start a conversation**. This option isn't available if you're using the [new Explore experience](https://docs.cloud.google.com/looker/docs/new-explore-experience-overview).
  2. By default the conversation is called "Untitled." After you ask your first question in the conversation, Conversational Analytics automatically generates a conversation title that's based on your question and response. To change the generated name, click the title at the top of the conversation page and enter a new conversation name. To save your changes, click elsewhere on the page, or press return (Mac) or Enter (PC).




Once you have created a conversation, you can ask questions about the data in the send_spark **Ask a question** field within the conversation. You can return to the conversation from the **schedule Recent Conversations** section.

## Start a conversation with an existing data agent that queries Explores

**Note:** To create a new data agent to chat with Explore data, see the [Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents) documentation page. To query a user-defined or LookML dashboard with a data agent, see the [Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards) and [Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards) documentation pages, respectively.

Data agents are customized with context and instructions that are specific to your data. You can start a conversation with an existing [data agent that you created](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#create-and-edit-data-agents) or that another user has [shared with you](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#share-data-agents). To start a conversation with an existing data agent that's connected to up to five Looker Explores follow these steps:

  1. Navigate to the Conversational Analytics interface.

     * From the [main navigation menu](https://docs.cloud.google.com/looker/docs/finding-content): Select ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg)**Conversations**. Select the **Agents** tab and then select the Explore data agent that you want to converse with.
     * From the [**Create** menu](https://docs.cloud.google.com/docs/finding-content#using_the_main_navigation_menu): Select ![](https://fonts.gstatic.com/s/i/short-term/release/googlesymbols/chat_spark/default/24px.svg)**Conversation**. Select the **Agents** tab and then select the Explore data agent that you want to converse with.
  2. By default the conversation is called "Untitled." After you ask your first question in the conversation, Conversational Analytics automatically generates a conversation title that's based on your question and response. To change the generated name, click the title at the top of the conversation page and enter a new conversation name. To save your changes, click elsewhere on the page, or press return (Mac) or Enter (PC).




Once you have created a conversation, you can ask questions about the data in the send_spark **Ask a question** field within the conversation. You can return to the conversation from the **schedule Recent Conversations** section.

## Ask questions about Looker data

When you're beginning a new conversation, Conversational Analytics suggests some starting questions to ask. The questions don't need to be in a specific format or use a specific syntax. However, they do need to relate to the Explore that you've selected.

Type your question in natural language into the **Ask a question** field. Select a question mode and click send. After you submit your query, you can cancel Conversational Analytics's response by clicking stop **Stop response**. Conversational analytics stops running the query and displays the following message: `The query was cancelled.`

For more guidance on the types of questions that you can ask, see [Limitations on questions](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations-on-questions).

### Select a question mode

When you ask a question, you can select the question mode from a drop-down menu that contains the following options:

  * **Fast** (default): Best for most questions.
  * **Thinking**: Detailed reasoning.



Conversational analytics defaults to **Fast** question mode. Conversational analytics will maintain the same question mode throughout any multi-turn conversations, unless you manually change it.

#### Fast mode

**Fast** mode is recommended for most questions and is selected by default. In **Fast** mode, Conversational Analytics maps your natural language query directly to the LookML parameters that are defined in the LookML models that underlie your conversation's Explores. Conversational analytics responds quickly without spending extra tokens on thinking or streaming thoughts summaries in the chat.

Queries in **Fast** mode provide the same level of accuracy as queries in **Thinking** mode. Use **Fast** mode for your questions unless you specifically want to see the agent's reasoning process.

#### Thinking mode

In **Thinking** mode, the agent spends additional tokens thinking through the request and streams a thoughts summary directly in the chat while processing your query, giving you visibility into the agent's detailed reasoning steps.

Although **Thinking** mode does not produce more accurate answers than **Fast** mode, displaying the agent's reasoning lets you observe how Conversational Analytics interprets your query, plans its analytical steps, and references the underlying LookML models.

Select **Thinking** mode if you want to inspect the agent's detailed reasoning steps or test how an agent interacts with your data sources, and you want to spend the additional tokens required for thinking.

### How Conversational Analytics processes your questions

Conversational Analytics may rephrase your question after you've submitted a query, and the rephrased question will be displayed in the conversation window following your original question. For example, Conversational Analytics might rephrase the question "What is the mean of user ages?" to "What is the average user age?"

While Conversational Analytics runs your query, you can observe its reasoning and thought process. Conversational analytics may ask follow-up questions to clarify any ambiguities in the original query. For example, if there are multiple, similarly named fields, Conversational Analytics may ask you to clarify which field is most appropriate to use in processing your query.

### Multi-turn conversations

Conversational Analytics will take previous questions and answers into account as you continue the conversation. You can take previous answers and build on them by further refining results or changing the visualization type.

**Important:** You can only reference previous questions in answers from the active conversation. You cannot reference previous questions and answers from other conversations.

For more guidance on creating questions, see [Limitations on questions](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview#limitations-on-questions).

### Clarifying questions

While Conversational Analytics runs your query, you can observe its reasoning and thought process. Conversational analytics may ask follow-up questions to clarify any ambiguities in the original query. For example, if there are multiple, similarly named fields, Conversational Analytics may ask you to clarify which field is most appropriate to use in processing your query.

### Conversation metadata

When you converse with an Explore or a data agent, the collapsible storage **Data** panel shows the name of the Looker Explore that's being used by the conversation. The storage **Data** panel also provides the following options:

  * open_in_new **View fields** : When chatting with an Explore, you can view the Explore in a new browser window by clicking open_in_new **View fields**.
  * open_in_new **Edit agent** : When chatting with a data agent, you can [edit the details about the data agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents#create-and-edit-data-agents) by clicking open_in_new **Edit agent**.
  * chat_spark **New conversation** : Start a new conversation with the Looker Explore that the current conversation is using.



## Manage queries within a conversation

When you converse with data, you can manage the conversation by stopping an active query response while it is running or by deleting the most recent question and its response.

### Delete the most recent question

To delete the most recent question and its response, follow these steps:

  1. Hold your cursor over the most recent question, and then click delete **Delete message**.
  2. In the **Permanently delete message?** dialog, click **Delete** to permanently delete the question and its response.



## Understand query results and calculations

When you ask questions about your data in Conversational Analytics, the response might include a visualization, a data table, or other details, depending on your specific query and the connected data. To open the query results as an Explore, click explore **Open in Explore** within the query results.

In addition to this query response, Conversational Analytics provides the following options for understanding query results and calculations:

  * Details about how your query was interpreted
  * Details about how the answer was calculated
  * Additional details, such as analytical details and debug info, if enabled for the agent



### Determine how your query was interpreted

If you use **Thinking** mode to ask your question, you can see how Conversational Analytics reasoned through your query. To see its reasoning, expand the **Show reasoning** option. To hide its reasoning, click **Hide reasoning**.

Conversational Analytics analyzes each query and thinks about how to respond, using the keywords from your query to infer the relevant dimensions, measures, and other parameters from the semantic layer of the conversation's associated datasets and interpreting from your query what aggregations may need to be performed. When you expand **Show reasoning** , Conversational Analytics displays a plain text explanation of the steps that it took to interpret your query. The explanation also includes the duration that Conversational Analytics thought about the query.

Following its reasoning, Conversational Analytics generates a response, which may include a request for clarification about your query.

### Determine how an answer was calculated

To see how Conversational Analytics arrived at an answer or created a visualization, click keyboard_arrow_down **How was this calculated?** within the query results.

When you click **How was this calculated?** , Conversational Analytics displays a **Text** section. The **Text** section provides a plain text explanation of the steps that were taken by Conversational Analytics to arrive at the given answer. This explanation includes the raw field names that were used, the calculations that were done, the filters that were applied, the sort order, and other details.

If [Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics) is available for your data agent, the **Code** tab displays the additional generated Python code for any advanced queries.

### Analytical details and debug info

If the data agent that's used for the conversation has specific advanced options enabled, responses can contain the following details:

  * **Show analytical details** : If enabled, the agent's response displays its reasoning steps, generated Looker queries, and underlying data tables.
  * **Show debug info** : If enabled, the agent's response displays the steps that were executed by the agent for that response, which can help with troubleshooting.



These settings are configured in the advanced options when [creating or editing the agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents).

## Manage conversations

Conversations are listed by title in the schedule **Recent** section. You can change the names of conversations, delete conversations, or restore them from the trash folder.

### Delete a conversation

To move a conversation to the trash, open the conversation and click delete **Move to trash**.

**Note:** Conversations that remain in the trash for more than 30 days are automatically deleted.

### Restore or permanently delete a conversation

To restore or permanently delete a conversation from the trash, follow these steps:

  1. Within Conversational Analytics, select delete **Trash** in the left navigation panel to view the list of conversations that have been moved to the trash.
  2. In the **Trash** section, click the name of the conversation that you want to restore or permanently delete.
  3. In the **Are you sure?** dialog, select one of the following options: 
     * **Cancel** : Cancels the action.
     * **Restore** : Restores the conversation. The conversation can be accessed from the schedule **Recent** section of the left navigation menu within Conversational Analytics.
     * **Delete forever** : Permanently deletes the conversation.



## Related resources

  * **[Conversational analytics in Looker overview](https://docs.cloud.google.com/looker/docs/conversational-analytics-overview)** : The landing page for Conversational Analytics with a list of key features links to all Conversational Analytics documentation.
  * **[Create and manage Explore data agents](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents)** : With Explore data agents, you can customize the AI-powered data querying agent by providing context and instructions that are specific to your Explore data, which helps Conversational Analytics generate more accurate and contextually relevant responses.
  * **[Query a user-defined dashboard with a dashboard agent](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-dashboards)** : Chat with a Looker user-defined dashboard using a dashboard data agent.
  * **[Create and manage data agents for LookML dashboards](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-data-agents-lookml-dashboards)** : Use LookML to configure and manage version-controlled data agents for LookML dashboards.
  * **[Best practices for configuring Conversational Analytics in Looker](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-best-practices)** : Strategies and best practices to help Looker administrators and LookML developers successfully configure and optimize Conversational Analytics.
  * **[Enable Advanced Analytics](https://docs.cloud.google.com/looker/docs/conversational-analytics-looker-advanced-analytics)** : Advanced Analytics within Conversational Analytics translates your natural language questions into Python code and executes that code. Compared to standard SQL-based queries, the Advanced Analytics feature's use of Python enables more complex analysis and visualizations.



Send feedback 

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 4.0 License](https://creativecommons.org/licenses/by/4.0/), and code samples are licensed under the [Apache 2.0 License](https://www.apache.org/licenses/LICENSE-2.0). For details, see the [Google Developers Site Policies](https://developers.google.com/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated 2026-10-14 UTC.

Need to tell us more?  [[["Easy to understand","easyToUnderstand","thumb-up"],["Solved my problem","solvedMyProblem","thumb-up"],["Other","otherUp","thumb-up"]],[["Hard to understand","hardToUnderstand","thumb-down"],["Incorrect information or sample code","incorrectInformationOrSampleCode","thumb-down"],["Missing the information/samples I need","missingTheInformationSamplesINeed","thumb-down"],["Other","otherDown","thumb-down"]],["Last updated 2026-10-14 UTC."],[],[]] 
